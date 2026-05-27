"""Aggregation — turn LLM-enriched ads into track-based frequency tables.

Outputs structured aggregates that downstream report.py consumes.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

SIGNAL_FIELDS = (
    "craft_signals",
    "architecture_signals",
    "methodology_signals",
    "collaboration_signals",
    "ai_workflow_signals",
    "professional_signals",
)

# Canonical signal labels for prose presentation
SIGNAL_TRACK_LABELS = {
    "craft_signals": "Hantverket",
    "architecture_signals": "Arkitektur och systemtänkande",
    "methodology_signals": "Metodik och utvecklingsdisciplin",
    "collaboration_signals": "Projektkunnande och samarbete",
    "ai_workflow_signals": "AI-drivet arbetssätt",
    "professional_signals": "Yrkesmässighet och självledning",
}


def _pct(n: int, total: int) -> float:
    return round(100.0 * n / total, 1) if total else 0.0


def _filter_main_population(ads: list[dict]) -> list[dict]:
    """Apply the curriculum-design filter: not Java/.NET, not mixed, is fullstack."""
    return [
        a for a in ads
        if a.get("is_actually_fullstack", True)
        and a.get("stack_primary") not in ("java_dotnet", "mixed")
    ]


def _by_region(ads: list[dict]) -> dict[str, list[dict]]:
    out = {"SE": [], "intl": []}
    for a in ads:
        out.setdefault(a.get("region", "intl"), []).append(a)
    return out


def _by_seniority(ads: list[dict]) -> dict[str, list[dict]]:
    out = {"junior": [], "mid": [], "senior": [], "unspecified": []}
    for a in ads:
        out.setdefault(a.get("seniority", "unspecified"), []).append(a)
    return out


def _by_stack(ads: list[dict]) -> dict[str, int]:
    return dict(Counter(a.get("stack_primary", "unspecified") for a in ads))


def _frequency(ads: list[dict], field: str) -> list[dict]:
    n = len(ads)
    counter: Counter[str] = Counter()
    for a in ads:
        counter.update(set(a.get(field, [])))
    return [
        {"signal": s, "count": c, "pct": _pct(c, n)}
        for s, c in counter.most_common()
    ]


def _track_frequencies(ads: list[dict]) -> dict[str, list[dict]]:
    return {field: _frequency(ads, field) for field in SIGNAL_FIELDS} | {
        "tools": _frequency(ads, "tools"),
    }


def aggregate(ads_path: Path) -> dict:
    ads_all = json.loads(ads_path.read_text())

    # Sanity counts (pre-filter)
    n_total = len(ads_all)
    n_real_fullstack = sum(1 for a in ads_all if a.get("is_actually_fullstack", True))
    stack_distribution_all = _by_stack(ads_all)
    extraction_methods = dict(Counter(a.get("extraction_method", "unknown") for a in ads_all))

    # SE pre-filter snapshot — needed for the "junior is rare in SE" finding
    se_all = [a for a in ads_all if a.get("region") == "SE"]
    seniority_distribution_se_all = dict(Counter(a.get("seniority") for a in se_all))

    # Filtered population — the one we actually design curriculum from
    main = _filter_main_population(ads_all)
    region = _by_region(main)
    se_main = region["SE"]
    intl_main = region["intl"]

    # Primary population: ALL SE in the niche (not just junior — junior is too rare in Sweden)
    # Seniority split is reported separately for trajectory analysis.
    se_by_seniority = _by_seniority(se_main)
    se_junior_or_unspec = se_by_seniority["junior"] + se_by_seniority["unspecified"]
    se_senior_or_mid = se_by_seniority["senior"] + se_by_seniority["mid"]

    return {
        "meta": {
            "n_total_ads": n_total,
            "n_actually_fullstack": n_real_fullstack,
            "stack_distribution_all_regions": stack_distribution_all,
            "stack_distribution_SE": dict(Counter(a.get("stack_primary") for a in se_all)),
            "seniority_distribution_SE_all": seniority_distribution_se_all,
            "extraction_methods": extraction_methods,
            "n_main_population": len(main),
            "n_SE_main": len(se_main),
            "n_intl_main": len(intl_main),
            "n_SE_junior_or_unspec": len(se_junior_or_unspec),
            "n_SE_mid_or_senior": len(se_senior_or_mid),
            "seniority_distribution_SE_main": {k: len(v) for k, v in se_by_seniority.items()},
        },
        # Primary curriculum signal — ALL filtered SE ads (junior is too rare to use alone)
        "primary_tracks": _track_frequencies(se_main),
        # Junior+unspec view, for direct junior signal (small n, treat carefully)
        "junior_tracks": _track_frequencies(se_junior_or_unspec),
        # Mid+senior view, for trajectory signal (what graduates should grow toward)
        "trajectory_tracks": _track_frequencies(se_senior_or_mid),
        # Intl (filtered) — triangulation that SE isn't an island
        "intl_tracks": _track_frequencies(intl_main),
    }


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    agg = aggregate(root / "data/processed/ads.json")
    out = root / "data/processed/aggregate.json"
    out.write_text(json.dumps(agg, ensure_ascii=False, indent=2))
    print(f"  → {out}")
    m = agg["meta"]
    print(f"  meta: total={m['n_total_ads']}, fullstack={m['n_actually_fullstack']}, "
          f"main={m['n_main_population']}, SE_main={m['n_SE_main']}, "
          f"SE_junior_or_unspec={m['n_SE_junior_or_unspec']}")
    print(f"  stacks: {m['stack_distribution_all_regions']}")
    print(f"  SE seniority: {m['seniority_distribution_SE_main']}")
