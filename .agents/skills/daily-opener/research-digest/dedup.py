#!/usr/bin/env python3
"""Deduplicate paper candidates by arXiv ID, DOI, and fuzzy title matching."""

import argparse
import json
import re
import sys

from rapidfuzz import fuzz


def normalize_title(title: str) -> str:
    t = title.lower().strip()
    t = re.sub(r"[^a-z0-9\s]", "", t)
    t = re.sub(r"\s+", " ", t)
    return t


def merge_records(existing: dict, new: dict) -> dict:
    """Merge two records for the same paper. Prefer S2 data (richer metadata)."""
    if "s2_" in new["source"] and "s2_" not in existing["source"]:
        merged = dict(new)
    else:
        merged = dict(existing)

    sources = set()
    for s in [existing.get("source", ""), new.get("source", "")]:
        sources.update(s.split(","))
    merged["source"] = ",".join(sorted(sources - {""}))

    queries = set()
    for q in [existing.get("query", ""), new.get("query", "")]:
        queries.update(q.split(","))
    merged["query"] = ",".join(sorted(queries - {""}))

    if not merged.get("arxiv_id") and new.get("arxiv_id"):
        merged["arxiv_id"] = new["arxiv_id"]
    if not merged.get("doi") and new.get("doi"):
        merged["doi"] = new["doi"]
    if not merged.get("s2_id") and new.get("s2_id"):
        merged["s2_id"] = new["s2_id"]
    if not merged.get("abstract") and new.get("abstract"):
        merged["abstract"] = new["abstract"]
    if not merged.get("tldr") and new.get("tldr"):
        merged["tldr"] = new["tldr"]

    return merged


def dedup(papers: list[dict], fuzzy_threshold: int = 90) -> list[dict]:
    by_arxiv: dict[str, int] = {}
    by_doi: dict[str, int] = {}
    results: list[dict] = []
    norm_titles: list[str] = []

    for paper in papers:
        arxiv_id = paper.get("arxiv_id", "").strip()
        doi = paper.get("doi", "").strip()
        title = paper.get("title", "")
        norm = normalize_title(title)

        matched_idx = None

        if arxiv_id and arxiv_id in by_arxiv:
            matched_idx = by_arxiv[arxiv_id]
        elif doi and doi in by_doi:
            matched_idx = by_doi[doi]
        else:
            for i, existing_norm in enumerate(norm_titles):
                if fuzz.ratio(norm, existing_norm) >= fuzzy_threshold:
                    matched_idx = i
                    break

        if matched_idx is not None:
            results[matched_idx] = merge_records(results[matched_idx], paper)
        else:
            idx = len(results)
            results.append(paper)
            norm_titles.append(norm)
            if arxiv_id:
                by_arxiv[arxiv_id] = idx
            if doi:
                by_doi[doi] = idx

    return results


def main():
    parser = argparse.ArgumentParser(description="Deduplicate paper candidates")
    parser.add_argument("input", help="Input JSON (raw candidates)")
    parser.add_argument("output", help="Output JSON (deduplicated)")
    parser.add_argument("--threshold", type=int, default=90, help="Fuzzy title threshold")
    args = parser.parse_args()

    with open(args.input) as f:
        papers = json.load(f)

    deduped = dedup(papers, args.threshold)
    print(f"Dedup: {len(papers)} → {len(deduped)} papers")

    with open(args.output, "w") as f:
        json.dump(deduped, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
