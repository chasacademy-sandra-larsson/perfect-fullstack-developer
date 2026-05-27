"""We Work Remotely fetcher — uses the public RSS feed for the Full-Stack Programming category."""
from __future__ import annotations

import json
from pathlib import Path

import requests
from bs4 import BeautifulSoup

FEED = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs.rss"


def fetch_all(out_dir: Path) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    r = requests.get(
        FEED,
        headers={"User-Agent": "perfect-fullstack-research/0.1"},
        timeout=30,
    )
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "xml")
    items = []
    for it in soup.find_all("item"):
        items.append(
            {
                "title": (it.title.text if it.title else "").strip(),
                "link": (it.link.text if it.link else "").strip(),
                "pub_date": (it.pubDate.text if it.pubDate else "").strip(),
                "description_html": (it.description.text if it.description else "").strip(),
                "region": (it.region.text if it.region else "").strip() if it.find("region") else "",
            }
        )

    out_path = out_dir / "weworkremotely.json"
    out_path.write_text(json.dumps(items, ensure_ascii=False, indent=2))
    print(f"  weworkremotely: {len(items)} fullstack ads → {out_path}")
    return len(items)


if __name__ == "__main__":
    fetch_all(Path(__file__).resolve().parents[2] / "data/raw/intl")
