#!/usr/bin/env python3
"""Fetch paper candidates from Semantic Scholar, arXiv, and lab blog RSS feeds."""

import argparse
import json
import logging
import os
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

import feedparser
import requests
import yaml

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

S2_BASE = "https://api.semanticscholar.org/graph/v1"
S2_FIELDS = "title,abstract,authors,venue,citationCount,publicationDate,tldr,externalIds,url"
ARXIV_API = "https://export.arxiv.org/api/query"

# S2 rate limit is 1 req/s across all endpoints, even with a key.
# The key prevents aggressive 429 enforcement on public tier.
S2_DELAY = 1.1
S2_MAX_RETRIES = 3


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _s2_headers(api_key: str | None) -> dict:
    if api_key:
        return {"x-api-key": api_key}
    return {}


def _s2_get(path: str, params: dict, api_key: str | None) -> dict | list | None:
    """GET from S2 API with exponential backoff on 429s."""
    url = f"{S2_BASE}{path}"
    for attempt in range(S2_MAX_RETRIES + 1):
        try:
            r = requests.get(url, params=params, headers=_s2_headers(api_key), timeout=30)
            if r.status_code == 429:
                backoff = 5 * (2 ** attempt)  # 5s, 10s, 20s, 40s
                log.warning("S2 rate limited (attempt %d/%d), backing off %ds",
                            attempt + 1, S2_MAX_RETRIES + 1, backoff)
                time.sleep(backoff)
                continue
            r.raise_for_status()
            return r.json()
        except requests.exceptions.HTTPError:
            log.warning("S2 request failed (%s): HTTP %s", path, r.status_code)
            return None
        except Exception as e:
            log.warning("S2 request failed (%s): %s", path, e)
            return None
    log.warning("S2 request exhausted retries (%s)", path)
    return None


def _s2_rec_get(url: str, params: dict, api_key: str | None) -> dict | None:
    """GET from S2 Recommendations API with exponential backoff on 429s."""
    for attempt in range(S2_MAX_RETRIES + 1):
        try:
            r = requests.get(url, params=params, headers=_s2_headers(api_key), timeout=30)
            if r.status_code == 429:
                backoff = 5 * (2 ** attempt)
                log.warning("S2 recs rate limited (attempt %d/%d), backing off %ds",
                            attempt + 1, S2_MAX_RETRIES + 1, backoff)
                time.sleep(backoff)
                continue
            r.raise_for_status()
            return r.json()
        except requests.exceptions.HTTPError:
            log.warning("S2 recs request failed: HTTP %s", r.status_code)
            return None
        except Exception as e:
            log.warning("S2 recs request failed: %s", e)
            return None
    log.warning("S2 recs request exhausted retries")
    return None


def _normalize_paper(raw: dict, source: str, query: str = "") -> dict:
    ext = raw.get("externalIds") or {}
    authors = raw.get("authors") or []
    tldr = raw.get("tldr")
    return {
        "title": raw.get("title", ""),
        "authors": [a.get("name", "") for a in authors],
        "abstract": raw.get("abstract") or "",
        "venue": raw.get("venue") or "",
        "year": raw.get("year"),
        "citation_count": raw.get("citationCount") or 0,
        "arxiv_id": ext.get("ArXiv", ""),
        "doi": ext.get("DOI", ""),
        "s2_id": raw.get("paperId", ""),
        "url": raw.get("url") or raw.get("openAccessPdf", {}).get("url", ""),
        "tldr": tldr.get("text", "") if isinstance(tldr, dict) else "",
        "source": source,
        "query": query,
        "published": raw.get("publicationDate") or "",
    }


def _cutoff_date(days: int) -> str:
    return (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")


# ---------------------------------------------------------------------------
# Semantic Scholar
# ---------------------------------------------------------------------------

def fetch_s2_keyword(queries: list[dict], api_key: str | None) -> list[dict]:
    papers = []
    for q in queries:
        text = q["text"]
        log.info("S2 keyword search: %s", text)
        data = _s2_get("/paper/search", {
            "query": text,
            "fieldsOfStudy": "Computer Science",
            "year": "2025-",
            "fields": S2_FIELDS,
            "limit": 20,
        }, api_key)
        if data and "data" in data:
            for p in data["data"]:
                if p:
                    papers.append(_normalize_paper(p, "s2_keyword", text))
        time.sleep(S2_DELAY)
    return papers


def fetch_s2_recommendations(seed_ids: list[str], api_key: str | None) -> list[dict]:
    papers = []
    cutoff = _cutoff_date(30)
    for sid in seed_ids:
        if not sid:
            continue
        log.info("S2 recommendations for seed: %s", sid)
        url = f"https://api.semanticscholar.org/recommendations/v1/papers/forpaper/{sid}"
        data = _s2_rec_get(url, {"fields": S2_FIELDS, "limit": 10}, api_key)
        if data:
            for p in data.get("recommendedPapers", []):
                if p and (p.get("publicationDate") or "") >= cutoff:
                    papers.append(_normalize_paper(p, "s2_recommend"))
        time.sleep(S2_DELAY)
    return papers


def fetch_s2_authors(authors: list[dict], api_key: str | None, lookback_days: int = 7) -> list[dict]:
    papers = []
    cutoff = _cutoff_date(lookback_days)
    for author in authors:
        aid = author.get("s2_id", "")
        if not aid:
            continue
        log.info("S2 author papers: %s (%s)", author["name"], aid)
        data = _s2_get(f"/author/{aid}/papers", {
            "fields": S2_FIELDS,
            "limit": 5,
        }, api_key)
        if data and "data" in data:
            for p in data["data"]:
                if p and (p.get("publicationDate") or "") >= cutoff:
                    papers.append(_normalize_paper(p, "s2_author"))
        time.sleep(S2_DELAY)
    return papers


# ---------------------------------------------------------------------------
# arXiv
# ---------------------------------------------------------------------------

def fetch_arxiv(categories: list[str], lookback_hours: int = 48) -> list[dict]:
    papers = []
    cat_query = " OR ".join(f"cat:{c}" for c in categories)
    log.info("arXiv search: %s (last %dh)", categories, lookback_hours)

    try:
        r = requests.get(ARXIV_API, params={
            "search_query": cat_query,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "max_results": 200,
        }, timeout=60)
        r.raise_for_status()

        ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
        root = ET.fromstring(r.text)
        cutoff = datetime.now(timezone.utc) - timedelta(hours=lookback_hours + 1)

        for entry in root.findall("atom:entry", ns):
            published_str = entry.findtext("atom:published", "", ns)
            if published_str:
                pub_dt = datetime.fromisoformat(published_str.replace("Z", "+00:00"))
                if pub_dt < cutoff:
                    continue

            title = (entry.findtext("atom:title", "", ns) or "").replace("\n", " ").strip()
            abstract = (entry.findtext("atom:summary", "", ns) or "").replace("\n", " ").strip()
            authors = [a.findtext("atom:name", "", ns) for a in entry.findall("atom:author", ns)]

            arxiv_id = ""
            entry_id = entry.findtext("atom:id", "", ns)
            if entry_id and "abs/" in entry_id:
                arxiv_id = entry_id.split("abs/")[-1].split("v")[0]

            link = ""
            for lnk in entry.findall("atom:link", ns):
                if lnk.get("type") == "text/html":
                    link = lnk.get("href", "")
                    break
            if not link:
                link = entry_id or ""

            papers.append({
                "title": title,
                "authors": authors,
                "abstract": abstract,
                "venue": "arXiv",
                "year": pub_dt.year if published_str else None,
                "citation_count": 0,
                "arxiv_id": arxiv_id,
                "doi": "",
                "s2_id": "",
                "url": link,
                "tldr": "",
                "source": "arxiv",
                "query": "",
                "published": published_str[:10] if published_str else "",
            })
        log.info("arXiv: fetched %d papers", len(papers))
    except Exception as e:
        log.warning("arXiv fetch failed: %s", e)

    return papers


# ---------------------------------------------------------------------------
# RSS
# ---------------------------------------------------------------------------

RSS_HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; research-digest/1.0)"}


def fetch_rss(feeds: list[dict]) -> list[dict]:
    posts = []
    cutoff = datetime.now(timezone.utc) - timedelta(hours=24)

    for feed_cfg in feeds:
        name = feed_cfg["name"]
        url = feed_cfg["url"]
        log.info("RSS: %s", name)
        try:
            r = requests.get(url, headers=RSS_HEADERS, timeout=15)
            r.raise_for_status()
            d = feedparser.parse(r.text)
            for entry in d.entries:
                pub = entry.get("published_parsed") or entry.get("updated_parsed")
                if pub:
                    pub_dt = datetime(*pub[:6], tzinfo=timezone.utc)
                    if pub_dt < cutoff:
                        continue
                    pub_str = pub_dt.strftime("%Y-%m-%d")
                else:
                    pub_str = ""

                posts.append({
                    "title": entry.get("title", ""),
                    "authors": [],
                    "abstract": entry.get("summary", ""),
                    "venue": name,
                    "year": None,
                    "citation_count": 0,
                    "arxiv_id": "",
                    "doi": "",
                    "s2_id": "",
                    "url": entry.get("link", ""),
                    "tldr": "",
                    "source": "rss",
                    "query": "",
                    "published": pub_str,
                })
            log.info("RSS %s: %d recent posts", name, len([p for p in posts if p["venue"] == name]))
        except Exception as e:
            log.warning("RSS failed for %s: %s", name, e)

    return posts


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Fetch research paper candidates")
    parser.add_argument("config", help="Path to config.yaml")
    parser.add_argument("output", help="Output JSON path")
    args = parser.parse_args()

    with open(args.config) as f:
        cfg = yaml.safe_load(f)

    api_key = cfg["settings"].get("s2_api_key", "") or os.environ.get("S2_API_KEY", "")
    if not api_key:
        log.warning("No S2 API key found; requests may be rate-limited")

    settings = cfg["settings"]
    all_categories = cfg["arxiv"]["primary"] + cfg["arxiv"]["secondary"]

    all_papers = []
    all_papers.extend(fetch_s2_keyword(cfg["queries"], api_key))
    seed_ids = [p["s2_id"] for p in cfg["seed_papers"] if p.get("s2_id")]
    all_papers.extend(fetch_s2_recommendations(seed_ids, api_key))
    all_papers.extend(fetch_s2_authors(cfg["tracked_authors"], api_key, settings["lookback_days"]))
    all_papers.extend(fetch_arxiv(all_categories, settings["arxiv_lookback_hours"]))
    all_papers.extend(fetch_rss(cfg["rss_feeds"]))

    log.info("Total raw candidates: %d", len(all_papers))

    with open(args.output, "w") as f:
        json.dump(all_papers, f, indent=2, ensure_ascii=False)

    print(f"Wrote {len(all_papers)} candidates to {args.output}")


if __name__ == "__main__":
    main()
