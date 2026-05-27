"""Hacker News 'Who is hiring' fetcher.

Uses the Algolia HN Search API to find the latest 'Ask HN: Who is hiring?' thread,
then pulls top-level comments (one per ad) and filters those mentioning fullstack.
"""
from __future__ import annotations

import json
import re
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup

SEARCH = "https://hn.algolia.com/api/v1/search_by_date"
ITEM = "https://hacker-news.firebaseio.com/v0/item/{id}.json"
KEYWORDS = ("fullstack", "full-stack", "full stack", "full-stack engineer")


def _latest_whoishiring_thread() -> int:
    # search_by_date returns chronologically newest first
    r = requests.get(
        SEARCH,
        params={"tags": "story,author_whoishiring", "hitsPerPage": 10},
        timeout=30,
    )
    r.raise_for_status()
    hits = r.json()["hits"]
    # The whoishiring account posts two threads per month: "Who is hiring?" and
    # "Who wants to be hired?". We want the former.
    for h in hits:
        title = (h.get("title") or "").lower()
        if "who is hiring" in title:
            return int(h["objectID"])
    raise RuntimeError("Could not find a 'Who is hiring' thread")


def _strip_html(s: str) -> str:
    return BeautifulSoup(s or "", "html.parser").get_text("\n").strip()


def fetch_all(out_dir: Path) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    thread_id = _latest_whoishiring_thread()
    print(f"  hn: latest 'Who is hiring' thread = {thread_id}")

    thread = requests.get(ITEM.format(id=thread_id), timeout=30).json()
    kids = thread.get("kids", []) or []

    ads = []
    for kid in kids:
        try:
            item = requests.get(ITEM.format(id=kid), timeout=30).json()
        except requests.RequestException:
            continue
        if not item or item.get("dead") or item.get("deleted"):
            continue
        text = _strip_html(item.get("text", ""))
        if not text:
            continue
        if any(re.search(rf"\b{re.escape(k)}\b", text, re.I) for k in KEYWORDS):
            ads.append({"id": kid, "text": text, "by": item.get("by"), "time": item.get("time")})
        time.sleep(0.05)

    out_path = out_dir / "hackernews.json"
    out_path.write_text(json.dumps(ads, ensure_ascii=False, indent=2))
    print(f"  hn: {len(ads)} fullstack-mentioning ads (of {len(kids)} comments) → {out_path}")
    return len(ads)


if __name__ == "__main__":
    fetch_all(Path(__file__).resolve().parents[2] / "data/raw/intl")
