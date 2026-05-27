"""End-to-end pipeline runner."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from src.analyze import aggregate
from src.extract import collect_ads, extract_all, llm_available
from src.report import generate
from src.sources import hackernews, jobtech, remoteok, weworkremotely

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"


def step_fetch(skip_hn: bool) -> None:
    print("\n[1/4] Fetching ads …")
    jobtech.fetch_all(DATA / "raw/jobtech")
    remoteok.fetch_all(DATA / "raw/intl")
    weworkremotely.fetch_all(DATA / "raw/intl")
    if skip_hn:
        print("  hn: skipped (--skip-hn)")
    else:
        hackernews.fetch_all(DATA / "raw/intl")


def step_extract(use_llm: bool) -> None:
    print("\n[2/4] Extracting skills …")
    ads = collect_ads(DATA)
    print(f"  loaded {len(ads)} ads")
    enriched = extract_all(ads, use_llm=use_llm)
    out = DATA / "processed/ads.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(enriched, ensure_ascii=False, indent=2))
    print(f"  → {len(enriched)} enriched ads → {out}")


def step_retry_fallbacks() -> None:
    """Re-extract only ads that previously fell back to keyword extraction."""
    print("\n[2b] Retry LLM on previous fallbacks …")
    path = DATA / "processed/ads.json"
    ads = json.loads(path.read_text())
    fallbacks = [a for a in ads if a.get("extraction_method") in ("keyword_fallback", "keyword")]
    others = [a for a in ads if a.get("extraction_method") == "llm"]
    print(f"  {len(fallbacks)} fallbacks to retry, {len(others)} keep")
    if not fallbacks:
        return
    redone = extract_all(fallbacks, use_llm=True)
    path.write_text(json.dumps(others + redone, ensure_ascii=False, indent=2))
    success = sum(1 for r in redone if r.get("extraction_method") == "llm")
    print(f"  retry done: {success}/{len(fallbacks)} now have LLM data")


def step_aggregate() -> None:
    print("\n[3/4] Aggregating …")
    agg = aggregate(DATA / "processed/ads.json")
    out = DATA / "processed/aggregate.json"
    out.write_text(json.dumps(agg, ensure_ascii=False, indent=2))
    m = agg["meta"]
    print(f"  meta: total={m['n_total_ads']}, main_pop={m['n_main_population']}, "
          f"SE_main={m['n_SE_main']}, SE_junior_or_unspec={m['n_SE_junior_or_unspec']}")
    print(f"  stacks: {m['stack_distribution_all_regions']}")


def step_report() -> None:
    print("\n[4/4] Writing report …")
    generate(
        DATA / "processed/aggregate.json",
        DATA / "processed/ads.json",
        ROOT / "output/report.md",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-fetch", action="store_true", help="Use existing data/raw/")
    parser.add_argument("--skip-hn", action="store_true", help="Skip slow HN scrape")
    parser.add_argument("--no-llm", action="store_true", help="Force keyword-only extraction")
    parser.add_argument("--retry-fallbacks", action="store_true",
                        help="Only re-extract ads that previously fell back to keyword extraction")
    parser.add_argument("--only-aggregate", action="store_true",
                        help="Skip extraction; just aggregate + report from existing ads.json")
    args = parser.parse_args()

    if args.only_aggregate:
        step_aggregate()
        step_report()
        print("\nDone. Open output/report.md")
        return

    if args.retry_fallbacks:
        step_retry_fallbacks()
        step_aggregate()
        step_report()
        print("\nDone. Open output/report.md")
        return

    if not args.skip_fetch:
        step_fetch(skip_hn=args.skip_hn)

    use_llm = (not args.no_llm) and llm_available()
    if use_llm:
        print("\nLLM extraction ENABLED (ANTHROPIC_API_KEY found)")
    else:
        print("\nLLM extraction disabled — using keyword dictionary only")

    step_extract(use_llm=use_llm)
    step_aggregate()
    step_report()
    print("\nDone. Open output/report.md")


if __name__ == "__main__":
    main()
