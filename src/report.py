"""Markdown report generator — competence-track structured."""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from src.analyze import SIGNAL_FIELDS, SIGNAL_TRACK_LABELS


def _table(rows, cols):
    head = "| " + " | ".join(c[1] for c in cols) + " |"
    sep = "| " + " | ".join("---" for _ in cols) + " |"
    body = ["| " + " | ".join(str(r.get(c[0], "")) for c in cols) + " |" for r in rows]
    return "\n".join([head, sep, *body])


def _signal_table(rows: list[dict], limit: int = 20) -> str:
    return _table(
        rows[:limit],
        [("signal", "Signal"), ("count", "Antal"), ("pct", "% av annonser")],
    )


def _track_section(track_field: str, primary: dict, trajectory: dict, intl: dict) -> str:
    label = SIGNAL_TRACK_LABELS.get(track_field, track_field)
    lines = [f"\n### {label}\n"]
    p = primary.get(track_field, [])
    t = {r["signal"]: r for r in trajectory.get(track_field, [])}
    i = {r["signal"]: r for r in intl.get(track_field, [])}
    if not p:
        lines.append("_Inga signaler hittades i primärpopulationen._")
        return "\n".join(lines)
    rows = []
    for r in p[:15]:
        rows.append({
            "signal": r["signal"],
            "primary_pct": f"{r['pct']}%",
            "trajectory_pct": f"{t[r['signal']]['pct']}%" if r["signal"] in t else "—",
            "intl_pct": f"{i[r['signal']]['pct']}%" if r["signal"] in i else "—",
        })
    lines.append(_table(
        rows,
        [
            ("signal", "Signal"),
            ("primary_pct", "Primär (SE niche)"),
            ("trajectory_pct", "Trajectory (SE mid+senior)"),
            ("intl_pct", "Intl (icke-JD)"),
        ],
    ))
    return "\n".join(lines)


def _exec_summary(meta: dict) -> str:
    lines = ["## Exekutiv sammanfattning\n"]
    lines.append(
        f"**Underlag:** {meta['n_total_ads']} annonser extraherade och klassificerade av Claude Sonnet 4.6 "
        f"({meta['n_actually_fullstack']} bekräftade som faktiska fullstack-roller).\n"
    )

    se_stack = meta.get("stack_distribution_SE", {})
    se_total = sum(se_stack.values())
    se_stack_parts = ", ".join(f"`{k}`={v}" for k, v in sorted(se_stack.items(), key=lambda x: -x[1]))
    lines.append(f"**Svensk marknad — stackfördelning** (n={se_total}):  \n{se_stack_parts}\n")

    se_seniority = meta.get("seniority_distribution_SE_all", {})
    sen_parts = ", ".join(f"`{k}`={v}" for k, v in sorted(se_seniority.items(), key=lambda x: -x[1]))
    lines.append(
        f"**Svensk marknad — seniority** (n={se_total}):  \n{sen_parts}\n\n"
        f"> 🔑 **Centralt fynd:** explicita junior-annonser är extremt sällsynta i Sverige "
        f"(`{se_seniority.get('junior', 0)}` av `{se_total}` = "
        f"{(100*se_seniority.get('junior', 0)/se_total if se_total else 0):.0f}%). "
        f"Det betyder att **LIA är en kritisk anställningskanal** — utbildningen måste producera "
        f"studenter som företag *vill ta in på LIA*, inte bara studenter som matchar junior-annonser.\n"
    )

    lines.append(
        f"**Populationsfilter:**\n"
        f"- Steg 1: Inkluderas bara annonser där Sonnet bekräftar `is_actually_fullstack = true`\n"
        f"- Steg 2: Exkluderas annonser med `stack_primary` = `java_dotnet` eller `mixed` "
        f"(skolan har redan utbildningar i dessa)\n"
        f"- Resultat: **{meta['n_SE_main']} SE-annonser** i målnischen + **{meta['n_intl_main']} intl-annonser** för triangulering\n"
    )

    sen_main = meta["seniority_distribution_SE_main"]
    sen_main_parts = ", ".join(f"`{k}`={v}" for k, v in sen_main.items() if v)
    lines.append(
        f"**Primärpopulation** (SE niche, n={meta['n_SE_main']}) seniority-fördelning: {sen_main_parts}\n\n"
        f"Vi använder **hela primärpopulationen** för huvudsignalen. För *trajectory*-analys "
        f"(vad ska studenten växa mot) tittar vi separat på mid+senior-annonser (n={meta['n_SE_mid_or_senior']}).\n"
    )

    em = meta.get("extraction_methods", {})
    em_parts = ", ".join(f"`{k}`={v}" for k, v in em.items())
    lines.append(f"_Extraktionsmetod: {em_parts}_\n")
    return "\n".join(lines)


def _entry_barriers_vs_differentiators(primary: dict) -> str:
    """Group signals across all tracks by relative frequency."""
    all_signals = []
    for field in SIGNAL_FIELDS:
        for row in primary.get(field, []):
            all_signals.append({**row, "track": SIGNAL_TRACK_LABELS[field]})
    all_signals.sort(key=lambda r: -r["pct"])

    barriers = [r for r in all_signals if r["pct"] >= 40]
    differentiators = [r for r in all_signals if 15 <= r["pct"] < 40]
    growth = [r for r in all_signals if 5 <= r["pct"] < 15]

    lines = [
        "\n## Inträdesbarriärer vs. differentierare\n",
        "Indelningen är gjord på hela primärpopulationen (SE, icke-Java/.NET, faktisk fullstack). "
        "Tröskelnivåerna är _ungefärliga_: inträdeshöjden är där fler än 4 av 10 annonser "
        "kräver det, differentierare där 15–40% kräver det, växande där 5–15% gör det.\n",
        "**Användning:** Inträdesbarriärer ska vara obligatoriskt i utbildningen. "
        "Differentierare ska finnas i utbildningen som fördjupning eller projektmoment. "
        "Växande ska minst beröras (workshops, gästföreläsare, LIA-projekt) så studenten är medveten om dem.\n",
    ]
    lines.append(f"### Inträdesbarriärer (≥40%) — *utan dessa, inga intervjuer*\n")
    lines.append(_table(barriers, [("signal", "Signal"), ("track", "Spår"), ("pct", "%")]))
    lines.append(f"\n### Differentierare (15–40%) — *edge mot andra juniorer*\n")
    lines.append(_table(differentiators, [("signal", "Signal"), ("track", "Spår"), ("pct", "%")]))
    lines.append(f"\n### Växande (5–15%) — *bevaka, projekt/workshop-spår*\n")
    lines.append(_table(growth, [("signal", "Signal"), ("track", "Spår"), ("pct", "%")]))
    return "\n".join(lines)


def _tools_section(primary: dict, trajectory: dict, intl: dict) -> str:
    lines = ["\n## Tekniker (medel, inte mål)\n"]
    lines.append(
        "Verktygsfrekvensen i primärpopulationen styr tekniska val. "
        "**Mainstream slår nyfikenhet** är beslutsregeln.\n"
    )
    p = primary.get("tools", [])
    t = {r["signal"]: r for r in trajectory.get("tools", [])}
    i = {r["signal"]: r for r in intl.get("tools", [])}
    rows = []
    for r in p[:30]:
        rows.append({
            "signal": r["signal"],
            "primary_pct": f"{r['pct']}%",
            "trajectory_pct": f"{t[r['signal']]['pct']}%" if r["signal"] in t else "—",
            "intl_pct": f"{i[r['signal']]['pct']}%" if r["signal"] in i else "—",
        })
    lines.append(_table(
        rows,
        [
            ("signal", "Teknik"),
            ("primary_pct", "SE niche"),
            ("trajectory_pct", "SE mid+senior"),
            ("intl_pct", "Intl"),
        ],
    ))
    return "\n".join(lines)


def generate(agg_path: Path, ads_path: Path, out_path: Path) -> None:
    agg = json.loads(agg_path.read_text())
    meta = agg["meta"]
    primary = agg["primary_tracks"]
    trajectory = agg["trajectory_tracks"]
    intl = agg["intl_tracks"]

    md = []
    md.append("<!-- markdownlint-disable -->")
    md.append("<!-- vale off -->\n")
    md.append(f"# Fullstack-kompetensprofil — datadriven analys\n")
    md.append(f"_Genererad {date.today().isoformat()}_\n")
    md.append("> **Optimeringsmål:** maximera juniors anställningschans i Sverige inom 6 månader från examen, "
              "för fullstack-roller **utanför Java/.NET-stacken**.\n")
    md.append("> Profileringen utgår från `UPPDRAG.md`. Tekniker är medel — kompetensspår är mål.\n")

    md.append(_exec_summary(meta))

    md.append("\n## Kompetensspår — frekvenstabeller\n")
    md.append(
        "Varje tabell visar tre kolumner:\n"
        "1. **Primär (SE niche)** = alla svenska annonser efter filter (icke-Java/.NET, faktisk fullstack). Detta är basen för rekommendationer.\n"
        "2. **Trajectory (SE mid+senior)** = vad mer erfarna utvecklare i samma nisch förväntas kunna — visar vad studenten ska *kunna växa mot*.\n"
        "3. **Intl** = internationella annonser efter filter (triangulering, säkerställer att svensk bild inte är en ö).\n"
    )
    for field in SIGNAL_FIELDS:
        md.append(_track_section(field, primary, trajectory, intl))

    md.append(_entry_barriers_vs_differentiators(primary))

    md.append(_tools_section(primary, trajectory, intl))

    md.append("\n## Förbehåll\n")
    md.append(
        "- **AI-arbetsflöde-spåret är underrapporterat** i 2026-annonser. Värdena underskattar verkligheten. "
        "Det här spårets innehåll måste byggas på branschpraktik + curated ramverk, inte annonsdata.\n"
        "- **Seniority-klassificering är konservativ.** När annonsen är otydlig sätts `unspecified` — och de inkluderas "
        "i primärpopulationen tillsammans med uttalade junior-annonser. Det är medvetet: en otydlig annons är ofta "
        "en mid/senior-annons formulerad som om alla kunde söka, vilket gör att signalen är mer junior-relevant än seniority-stämpeln säger.\n"
        "- **Korrelation ≠ kausation.** Att en signal nämns ofta betyder att arbetsgivare *säger sig vilja ha* den. "
        "Det är ofta sant, men inte alltid: rituella formuleringar smiter med.\n"
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(md))
    print(f"  → report → {out_path}")


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    generate(
        root / "data/processed/aggregate.json",
        root / "data/processed/ads.json",
        root / "output/report.md",
    )
