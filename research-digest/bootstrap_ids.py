#!/usr/bin/env python3
"""One-time setup: resolve Semantic Scholar IDs for seed papers and tracked authors."""

import os
import sys
import time

import requests
import yaml

S2_BASE = "https://api.semanticscholar.org/graph/v1"


def get_api_key() -> str:
    key = os.environ.get("S2_API_KEY", "")
    if not key:
        print("Warning: No S2_API_KEY set. Requests will be heavily rate-limited.")
    return key


def s2_headers(api_key: str) -> dict:
    if api_key:
        return {"x-api-key": api_key}
    return {}


def search_paper(title: str, api_key: str) -> dict | None:
    try:
        r = requests.get(f"{S2_BASE}/paper/search", params={
            "query": title,
            "fields": "title,authors,year,externalIds",
            "limit": 5,
        }, headers=s2_headers(api_key), timeout=30)
        if r.status_code == 429:
            time.sleep(5)
            r = requests.get(f"{S2_BASE}/paper/search", params={
                "query": title,
                "fields": "title,authors,year,externalIds",
                "limit": 5,
            }, headers=s2_headers(api_key), timeout=30)
        r.raise_for_status()
        data = r.json()
        if data.get("data"):
            return data["data"][0]
    except Exception as e:
        print(f"  Error searching: {e}")
    return None


def search_author(name: str, api_key: str) -> dict | None:
    try:
        r = requests.get(f"{S2_BASE}/author/search", params={
            "query": name,
            "fields": "name,affiliations,paperCount,hIndex",
            "limit": 5,
        }, headers=s2_headers(api_key), timeout=30)
        if r.status_code == 429:
            time.sleep(5)
            r = requests.get(f"{S2_BASE}/author/search", params={
                "query": name,
                "fields": "name,affiliations,paperCount,hIndex",
                "limit": 5,
            }, headers=s2_headers(api_key), timeout=30)
        r.raise_for_status()
        data = r.json()
        if data.get("data"):
            return data["data"][0]
    except Exception as e:
        print(f"  Error searching: {e}")
    return None


def main():
    if len(sys.argv) < 2:
        print("Usage: python bootstrap_ids.py <config.yaml>")
        sys.exit(1)

    config_path = sys.argv[1]
    with open(config_path) as f:
        cfg = yaml.safe_load(f)

    api_key = get_api_key()
    modified = False

    print("\n=== Resolving seed paper IDs ===\n")
    for paper in cfg["seed_papers"]:
        if paper.get("s2_id"):
            print(f"  ✓ {paper['title'][:60]}... → {paper['s2_id']}")
            continue

        result = search_paper(paper["title"], api_key)
        if result:
            authors = ", ".join(a["name"] for a in (result.get("authors") or [])[:3])
            year = result.get("year", "?")
            print(f"  Found: {result['title'][:60]}...")
            print(f"         {authors} ({year})")
            print(f"         ID: {result['paperId']}")

            accept = input("  Accept? [Y/n] ").strip().lower()
            if accept in ("", "y", "yes"):
                paper["s2_id"] = result["paperId"]
                modified = True
                print("  ✓ Saved")
            else:
                print("  ✗ Skipped")
        else:
            print(f"  ✗ Not found: {paper['title'][:60]}...")

        time.sleep(0.5)

    print("\n=== Resolving author IDs ===\n")
    for author in cfg["tracked_authors"]:
        if author.get("s2_id"):
            print(f"  ✓ {author['name']} → {author['s2_id']}")
            continue

        result = search_author(author["name"], api_key)
        if result:
            affiliations = ", ".join(result.get("affiliations") or ["?"])
            h = result.get("hIndex", "?")
            count = result.get("paperCount", "?")
            print(f"  Found: {result['name']}")
            print(f"         {affiliations} | h-index: {h} | papers: {count}")
            print(f"         ID: {result['authorId']}")

            accept = input("  Accept? [Y/n] ").strip().lower()
            if accept in ("", "y", "yes"):
                author["s2_id"] = result["authorId"]
                modified = True
                print("  ✓ Saved")
            else:
                print("  ✗ Skipped")
        else:
            print(f"  ✗ Not found: {author['name']}")

        time.sleep(0.5)

    if modified:
        with open(config_path, "w") as f:
            yaml.dump(cfg, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        print(f"\nConfig updated: {config_path}")
    else:
        print("\nNo changes made.")


if __name__ == "__main__":
    main()
