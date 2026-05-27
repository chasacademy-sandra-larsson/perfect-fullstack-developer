"""RemoteOK fetcher — open JSON feed at remoteok.com/api."""
from __future__ import annotations

import json
from pathlib import Path

import requests

API = "https://remoteok.com/remote-full-stack-jobs.json"
KEYWORDS = ("fullstack", "full-stack", "full stack", "full_stack")


def fetch_all(out_dir: Path) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    r = requests.get(
        API,
        headers={"User-Agent": "perfect-fullstack-research/0.1 (YH education research)"},
        timeout=30,
    )
    r.raise_for_status()
    raw = r.json()
    # First element is a metadata blob, rest are ads
    ads = [a for a in raw if isinstance(a, dict) and a.get("position")]

    def matches(ad: dict) -> bool:
        # The category endpoint already pre-filters, but some entries are not actual fullstack roles
        # so require the keyword in position title to keep precision high.
        return any(k in ad.get("position", "").lower() for k in KEYWORDS)

    filtered = [a for a in ads if matches(a)]
    out_path = out_dir / "remoteok.json"
    out_path.write_text(json.dumps(filtered, ensure_ascii=False, indent=2))
    print(f"  remoteok: {len(filtered)} fullstack ads (of {len(ads)} total) → {out_path}")
    return len(filtered)


if __name__ == "__main__":
    fetch_all(Path(__file__).resolve().parents[2] / "data/raw/intl")
