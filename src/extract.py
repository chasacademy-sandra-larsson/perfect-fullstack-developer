"""Skill extraction.

LLM-based per ad with structured taxonomy from prompts/extraction_system.md.
Falls back to a deterministic keyword extraction if no API key is present
or if a single LLM call fails.
"""
from __future__ import annotations

import json
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).resolve().parents[1]
PROMPT_PATH = ROOT / "prompts/extraction_system.md"

MODEL = "claude-sonnet-4-6"
MAX_AD_CHARS = 6000  # ~1500 tokens; keeps cost predictable and avoids irrelevant footer noise
MAX_WORKERS = 3  # 50 req/min on Anthropic Tier 1 ⇒ ≈40 req/min with 3 workers and ~4s avg latency

# Canonical signal vocabulary — must match prompts/extraction_system.md
SIGNAL_FIELDS = (
    "craft_signals",
    "architecture_signals",
    "methodology_signals",
    "collaboration_signals",
    "ai_workflow_signals",
    "professional_signals",
)


# ---------------------------------------------------------------------------
# Normalisation (multi-source → common ad shape)
# ---------------------------------------------------------------------------
def _strip_html(s: str) -> str:
    return BeautifulSoup(s or "", "html.parser").get_text(" ").strip()


def _normalize_jobtech(raw):
    for h in raw:
        yield {
            "source": "jobtech",
            "region": "SE",
            "id": str(h.get("id")),
            "title": h.get("headline", ""),
            "location": (h.get("workplace_address") or {}).get("city") or "",
            "text": (h.get("description") or {}).get("text", "") or "",
            "url": h.get("webpage_url", ""),
            "employer": (h.get("employer") or {}).get("name", ""),
        }


def _normalize_remoteok(raw):
    for h in raw:
        yield {
            "source": "remoteok",
            "region": "intl",
            "id": str(h.get("id") or h.get("slug") or h.get("url")),
            "title": h.get("position", ""),
            "location": h.get("location", "") or "remote",
            "text": _strip_html(h.get("description", "")),
            "url": h.get("url", ""),
            "employer": h.get("company", ""),
        }


def _normalize_wwr(raw):
    for h in raw:
        yield {
            "source": "weworkremotely",
            "region": "intl",
            "id": h.get("link", "") or h.get("title", ""),
            "title": h.get("title", ""),
            "location": h.get("region", "") or "remote",
            "text": _strip_html(h.get("description_html", "")),
            "url": h.get("link", ""),
            "employer": "",
        }


def _normalize_hn(raw):
    for h in raw:
        yield {
            "source": "hackernews",
            "region": "intl",
            "id": str(h.get("id")),
            "title": "HN Who is hiring",
            "location": "",
            "text": h.get("text", ""),
            "url": f"https://news.ycombinator.com/item?id={h.get('id')}",
            "employer": h.get("by", ""),
        }


def _load(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return json.loads(path.read_text())


def collect_ads(data_root: Path) -> list[dict]:
    ads: list[dict] = []
    ads.extend(_normalize_jobtech(_load(data_root / "raw/jobtech/jobtech.json")))
    ads.extend(_normalize_remoteok(_load(data_root / "raw/intl/remoteok.json")))
    ads.extend(_normalize_wwr(_load(data_root / "raw/intl/weworkremotely.json")))
    ads.extend(_normalize_hn(_load(data_root / "raw/intl/hackernews.json")))
    return ads


# ---------------------------------------------------------------------------
# Keyword fallback — used when LLM unavailable or a call fails
# ---------------------------------------------------------------------------
TOOL_PATTERNS = {
    "typescript": [r"\btypescript\b"],
    "javascript": [r"\bjavascript\b"],
    "python": [r"\bpython\b"],
    "go": [r"\bgolang\b"],
    "rust": [r"\brust\b"],
    "ruby": [r"\bruby\b"],
    "php": [r"\bphp\b"],
    "kotlin": [r"\bkotlin\b"],
    "react": [r"\breact(?:\.js)?\b"],
    "nextjs": [r"\bnext\.?js\b"],
    "vue": [r"\bvue(?:\.js)?\b"],
    "nuxt": [r"\bnuxt\b"],
    "angular": [r"\bangular\b"],
    "svelte": [r"\bsvelte(?:kit)?\b"],
    "tailwind": [r"\btailwind\b"],
    "nodejs": [r"\bnode(?:\.js)?\b"],
    "express": [r"\bexpress(?:\.js)?\b"],
    "nestjs": [r"\bnest\.?js\b"],
    "django": [r"\bdjango\b"],
    "flask": [r"\bflask\b"],
    "fastapi": [r"\bfastapi\b"],
    "rails": [r"\brails\b"],
    "laravel": [r"\blaravel\b"],
    "postgresql": [r"\bpostgres(?:ql)?\b"],
    "mysql": [r"\bmysql\b"],
    "mongodb": [r"\bmongo(?:db)?\b"],
    "redis": [r"\bredis\b"],
    "graphql": [r"\bgraphql\b"],
    "rest": [r"\brest(?:ful)?\s*api\b"],
    "aws": [r"\baws\b"],
    "azure": [r"\bazure\b"],
    "gcp": [r"\bgcp\b", r"\bgoogle cloud\b"],
    "vercel": [r"\bvercel\b"],
    "docker": [r"\bdocker\b"],
    "kubernetes": [r"\bkubernetes\b", r"\bk8s\b"],
    "java": [r"\bjava\b(?!script)"],
    "csharp_dotnet": [r"\bc#\b", r"\.net\b", r"\basp\.net\b"],
}
_COMPILED_TOOLS = {k: [re.compile(p, re.I) for p in v] for k, v in TOOL_PATTERNS.items()}


def keyword_tools(text: str) -> list[str]:
    return [name for name, patterns in _COMPILED_TOOLS.items() if any(p.search(text) for p in patterns)]


def keyword_stack_primary(tools: list[str]) -> str:
    has_jd = "java" in tools or "csharp_dotnet" in tools
    other_backend = {"nodejs", "express", "nestjs", "django", "flask", "fastapi", "rails", "laravel"}
    has_other = bool(other_backend & set(tools))
    if has_jd and has_other:
        return "mixed"
    if has_jd:
        return "java_dotnet"
    if "python" in tools:
        return "python"
    if "javascript" in tools or "typescript" in tools or "nodejs" in tools:
        return "javascript_node"
    return "unspecified"


def keyword_fallback(text: str) -> dict:
    tools = keyword_tools(text)
    return {
        "is_actually_fullstack": True,
        "seniority": "unspecified",
        "stack_primary": keyword_stack_primary(tools),
        "craft_signals": [],
        "architecture_signals": [],
        "methodology_signals": [],
        "collaboration_signals": [],
        "ai_workflow_signals": [],
        "professional_signals": [],
        "tools": tools,
    }


# ---------------------------------------------------------------------------
# LLM extraction
# ---------------------------------------------------------------------------
def llm_available() -> bool:
    return bool(os.environ.get("ANTHROPIC_API_KEY"))


def _load_system_prompt() -> str:
    return PROMPT_PATH.read_text()


def _build_user_message(ad: dict) -> str:
    text = ad["text"][:MAX_AD_CHARS]
    return (
        f"Källa: {ad['source']} | Region: {ad['region']} | Rubrik: {ad['title']}\n"
        f"Arbetsgivare: {ad.get('employer', '') or '—'}\n"
        f"Ort: {ad.get('location', '') or '—'}\n\n"
        f"--- ANNONSTEXT ---\n{text}"
    )


def _parse_response(raw_text: str) -> dict | None:
    raw = raw_text.strip()
    raw = re.sub(r"^```(?:json)?", "", raw)
    raw = re.sub(r"```$", "", raw)
    raw = raw.strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", raw, re.DOTALL)
        if m:
            try:
                return json.loads(m.group(0))
            except json.JSONDecodeError:
                return None
        return None


def _llm_extract_one(client, system_prompt: str, ad: dict) -> dict | None:
    for attempt in range(5):
        try:
            resp = client.messages.create(
                model=MODEL,
                max_tokens=800,
                system=[{
                    "type": "text",
                    "text": system_prompt,
                    "cache_control": {"type": "ephemeral"},
                }],
                messages=[{"role": "user", "content": _build_user_message(ad)}],
            )
            parsed = _parse_response(resp.content[0].text)
            if parsed:
                return parsed
        except Exception as e:  # noqa: BLE001
            msg = str(e)
            is_rate_limit = "429" in msg or "rate_limit" in msg.lower()
            if attempt < 4:
                # Rate-limit window is 60s, so back off proportionally
                wait = 35 if is_rate_limit else 2 ** attempt
                time.sleep(wait)
                continue
            print(f"  LLM error on ad {ad['id']} after retries: {msg[:200]}")
    return None


def extract_all(ads: list[dict], use_llm: bool = False) -> list[dict]:
    out: list[dict] = []
    if not use_llm:
        print(f"  Keyword fallback for all {len(ads)} ads")
        for ad in ads:
            extracted = keyword_fallback(ad["text"])
            out.append({**ad, **extracted, "extraction_method": "keyword"})
        return out

    from anthropic import Anthropic

    client = Anthropic()
    system_prompt = _load_system_prompt()
    print(f"  LLM extraction: {len(ads)} ads via {MODEL} (prompt caching enabled)")

    done = 0
    failures = 0
    cache_hits = 0
    cache_writes = 0
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(_llm_extract_one, client, system_prompt, ad): ad for ad in ads}
        for fut in as_completed(futures):
            ad = futures[fut]
            llm = fut.result()
            if llm is None:
                fallback = keyword_fallback(ad["text"])
                out.append({**ad, **fallback, "extraction_method": "keyword_fallback"})
                failures += 1
            else:
                # Ensure all expected fields exist
                for f in SIGNAL_FIELDS:
                    llm.setdefault(f, [])
                llm.setdefault("tools", [])
                llm.setdefault("seniority", "unspecified")
                llm.setdefault("stack_primary", "unspecified")
                llm.setdefault("is_actually_fullstack", True)
                out.append({**ad, **llm, "extraction_method": "llm"})
            done += 1
            if done % 25 == 0:
                print(f"    {done}/{len(ads)} done (fallbacks: {failures})")
    print(f"  LLM extraction complete: {done} ads, {failures} fallbacks")
    return out


def main() -> None:
    data_root = ROOT / "data"
    ads = collect_ads(data_root)
    print(f"Loaded {len(ads)} ads from disk")
    enriched = extract_all(ads, use_llm=llm_available())
    out_path = data_root / "processed/ads.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(enriched, ensure_ascii=False, indent=2))
    print(f"  → {len(enriched)} enriched ads → {out_path}")


if __name__ == "__main__":
    main()
