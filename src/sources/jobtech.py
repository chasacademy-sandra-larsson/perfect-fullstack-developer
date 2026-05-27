"""JobTech Dev API fetcher (Arbetsförmedlingen, Sweden).

API docs: https://jobsearch.api.jobtechdev.se/
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import requests

API = "https://jobsearch.api.jobtechdev.se/search"
PAGE_SIZE = 100  # API max
QUERIES = ["fullstack", "full-stack", "full stack", "fullstackutvecklare"]


def _fetch_page(query: str, offset: int) -> dict:
    r = requests.get(
        API,
        params={"q": query, "limit": PAGE_SIZE, "offset": offset},
        headers={"accept": "application/json"},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def fetch_all(out_dir: Path) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    seen: dict[str, dict] = {}

    for q in QUERIES:
        first = _fetch_page(q, 0)
        total = first.get("total", {}).get("value", 0)
        print(f"  query={q!r:25s} total={total}")
        for hit in first.get("hits", []):
            seen[hit["id"]] = hit

        offset = PAGE_SIZE
        while offset < total and offset < 2000:  # API hard limit is 2000
            page = _fetch_page(q, offset)
            for hit in page.get("hits", []):
                seen[hit["id"]] = hit
            offset += PAGE_SIZE
            time.sleep(0.2)

    out_path = out_dir / "jobtech.json"
    out_path.write_text(json.dumps(list(seen.values()), ensure_ascii=False, indent=2))
    print(f"  → {len(seen)} unique ads saved to {out_path}")
    return len(seen)


if __name__ == "__main__":
    fetch_all(Path(__file__).resolve().parents[2] / "data/raw/jobtech")
