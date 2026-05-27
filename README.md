# perfect-fullstack

Data-driven curriculum design for a 2-year YH fullstack program — scrapes Swedish and international fullstack job ads, extracts required skills, and produces a frequency-ranked skill profile that excludes the Java/.NET stack.

## Sources

- **Sweden:** JobTech Dev API (Arbetsförmedlingen, official open API)
- **International:** RemoteOK API, We Work Remotely RSS, Hacker News "Who is hiring" latest thread

LinkedIn is intentionally excluded — ToS issues, technical anti-scraping, and third-party API costs are not justified for a one-off analysis.

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # optional: add ANTHROPIC_API_KEY for LLM extraction

python3 run.py
```

Output ends up in `output/report.md`.

## Pipeline

1. `src/sources/*` — fetch raw ads, save to `data/raw/<source>/`
2. `src/extract.py` — extract tech skills per ad (LLM if API key set, else keyword dictionary)
3. `src/analyze.py` — aggregate into frequency tables, group SE vs international
4. `src/report.py` — markdown report with curriculum profile suggestion
