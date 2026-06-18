# LG-diskussion — Python/FastAPI som AI-backend i kurs 7

> **Syfte:** beslutsunderlag inför ledningsgruppens diskussion om strategiskt vägval för kurs 7 i FJS26.
> **Status:** Kursplanen för kurs 7 är skapad (`kursplaner-fjs26/7. AI inom fullstackutveckling.md`) i en första version på 20 YHp / 4 v ("primer-nivå"). Detta dokument samlar bakgrund och alternativ för en eventuell utökning där **Python/FastAPI introduceras som AI-backend**.
> **Beslut krävs innan kursplanen för kurs 7 uppdateras.**

---

## Sammanfattning

Frågan: ska FJS26 introducera Python (med FastAPI) som backendspråk i kurs 7, för att bygga AI-fullstack-applikationer i kombination med React-frontend?

**Kort svar från datan:** sannolikt ja — Python+FastAPI är JS-fullstackens naturliga backend-partner i AI-tunga produkter, och AI-fullstack är junior-nischens hetaste lucka utanför Java/.NET. Modest direkt anställningseffekt (annons-match) men starkare indirekt effekt (LIA-attraktivitet, polyglot-signal, AI-engineering-trajectory).

**Kostnad:** 10 YHp (kurs 7: 20 → 30 YHp, 4 → 6 v). Matchar exakt de 10 YHp som idag fattas mellan FJS26 (420) och FJS25 (430).

---

## Bakgrund — hur Python kom på bordet

Nuvarande FJS26 är medvetet optimerad för JavaScript/TypeScript-fullstack. Python har **inte fått en datadriven prövning** mot andra kandidater (K8s, Vue, Angular) utan har sorterats bort som en följd av programidentitet ("Fullstack JavaScript").

Frågan väcktes när vi observerade att Python ofta fungerar som **backend-partner till React/Next.js**, särskilt i AI/ML-tunga produkter — inte som *alternativ* till JS-fullstack, utan som dess naturliga *komplement*.

| Framing | Konsekvens |
|---|---|
| Python som alt-stack (gammal framing) | Krockar med programidentitet, splittar fokus, junior blir "okej på två istället för bra på en" |
| Python som **alt-backend i AI-fullstack** (ny framing) | Förlänger JS-fullstack-stacken med en specifik teknisk dimension; transfer learning från Express → FastAPI är hög |

Den nya framingen är vad detta dokument utgår från.

---

## Marknadssignal — datadriven läsning

Från `output/report.md`:

| Signal | SE niche | SE mid+senior | Intl |
|---|:---:|:---:|:---:|
| `python` | **17.4%** | 14.5% | **24.3%** |
| `nodejs` | 43.5% | 43.6% | 20.0% |
| `ai_tools_general` | 37.7% | 38.2% | 24.3% |
| `agentic_workflows` | 24.6% | 27.3% | 24.3% |

**Tolkning:**
- Python ligger på 17% i svensk niche — samma band som Kubernetes (17%), Vue (12%), Angular (13%). Inte inträdesbarriär (under 40%), men substantiellt.
- **Python är högre internationellt än Node** (24% vs 20%). Studenten som vill söka remote/utomlands får större marknad.
- Kombinerat med AI-signalerna (38% + 25%) öppnas en specifik trajectory: **AI-engineering / AI-fullstack**.
- `mixed` (28 annonser) och `unspecified` (22 annonser) filtrerades bort. Många av dessa innehåller troligen React+Python-kombinationer. **Den verkliga Python+JS-kombo-signalen är gömd** — vi vet inte exakt hur stor den är, men den är sannolikt större än 17%.

---

## Anställningseffekt — ärlig bedömning

| Mätning | Effekt |
|---|---|
| Direkt annons-match | **Modest** — kanske +10-15% fler annonser studenten kvalificerar för |
| LIA-attraktivitet | **Meningsfullt större** — företag som söker "AI-curious fullstack junior" är desperata efter studenter som redan byggt något med RAG/LLM, och då måste backenden vara Python |
| Polyglot-signal | **Positiv differentierare** — visar att studenten kan växla paradigm |
| Future-proofing | **Stark positiv** — AI-ekosystemet är Python-tungt och växer |

**Förbehåll:**
- Datasignalen är *sparse* eftersom `mixed` filtrerades bort. Detta är välgrundad inferens, inte certainhet.
- Vinsten är **kvalitetskritisk** — om Python lärs ut som "lite syntax också" blir det utspätt. Måste byggas som *AI-fullstack story* med ett färdigt React+FastAPI+RAG-projekt i portfolion.

---

## Pedagogisk placering — varför kurs 7

| Argument | Detalj |
|---|---|
| Naturlig hemvist | Python ↔ AI är industristandard (LangChain, FastAPI, OpenAI SDK) |
| Transfer learning hög | FastAPI ≈ Express (routes, dependency injection, Pydantic ≈ Zod) |
| Levereras i kontext | Python kommer in *för att studenten ska bygga AI-system*, inte som "andra backendspråk" |
| AI som tråd | Stärker AI-tråden som löper genom hela programmet ([[feedback-ai-not-a-kursmal]]) |

---

## Konkret förslag på utökning av kurs 7

> **OBS:** detta är ett **skissförslag** för diskussion — inte ett beslutat upplägg. Den exakta utformningen (kursmål, veckostruktur, examinations­moment) tas fram först efter LG-beslut.

**Omfattning:** 20 YHp / 4 v → **30 YHp / 6 v**

**Tillkommande innehåll:**
- Python-grunder (syntax, typer, async, venv/uv, paketshantering)
- FastAPI (routes, Pydantic, dependency injection, async)
- LLM-API-anrop från Python (OpenAI SDK, Anthropic SDK, LangChain primer)
- Vektordatabas (pgvector eller Chroma) som del av RAG
- React-frontend integrerad med FastAPI-backend (CORS, autentisering, datavalidering)

**Skiss veckostruktur (6 v):**

| V | Innehåll |
|---|---|
| 1 | Python-grunder + FastAPI-grunder (med transfer från Express) |
| 2 | AI-modeller (ML, NN, LLM) + risker + AI-utvecklingsverktyg (Claude Code etc.) |
| 3 | Prompt/context engineering + AI-komponenter (klassificering, NLP, semantisk sökning) |
| 4 | RAG-arkitektur + vektordatabas i FastAPI |
| 5 | AI-fullstack-projekt — React + FastAPI + RAG |
| 6 | Projektförädling + muntlig redovisning |

**Förslag på nya kursmål** (utöver befintliga 13):

- **Kunskap:** Python som backendspråk i AI-fullstacksammanhang
- **Kunskap:** FastAPI och dess användning för att exponera AI-funktionalitet
- **Färdighet:** Implementera en backend-tjänst i Python med FastAPI som exponerar AI-funktionalitet mot en React-frontend
- **Färdighet:** Integrera en React-frontend med en Python-baserad AI-backend

---

## Konsekvens för totalprogrammet

| Kurs | Före | Efter (förslag) |
|---|:---:|:---:|
| 7. AI inom fullstackutveckling | 20 YHp | **30 YHp** |
| Alla övriga | 400 YHp | 400 YHp |
| **Totalt** | **420 YHp** | **430 YHp** ✅ (matchar FJS25) |

LIA kvar på 110 YHp. Kurs 8 kvar på 65 YHp.

**Konflikt med tidigare diskussion:** Detta använder hela 10 YHp-utrymmet och lämnar **inget** kvar till de hårda gapen i kurs 8 (observability 44%, distributed_systems 48%, backend-prestanda 59%) som identifieras i `LG-DISKUSSION-kurs8.md`. LG måste välja prioritet:

| Alternativ | Kurs 7 | Kurs 8 | LIA |
|---|:---:|:---:|:---:|
| A. Allt till Python | +10 (30 YHp) | 65 YHp | 110 YHp |
| B. Allt till kurs 8 gap-stoppning | 20 YHp | +10 (75 YHp) | 110 YHp |
| C. Allt till LIA-utökning | 20 YHp | 65 YHp | +10 (120 YHp) |
| D. Split (Python + obs/perf) | +5 (25 YHp) | +5 (70 YHp) | 110 YHp |
| E. Utöka programmet | +10 (30 YHp) | +10 (75 YHp) | 110 YHp (totalt 440 YHp, kräver MYH-OK) |

---

## Risker och förbehåll

| Risk | Mitigering |
|---|---|
| **Programidentitet** — "FJS = JavaScript" blir grumlig | Python framing som AI-backend, inte som alt-stack. Programnamnet behöver inte ändras. |
| **Spädning av JS-djup** — 2 v mindre på Node-fördjupning | Node är redan fördjupat i kurs 4 (75 YHp). Studenter har solid JS-grund innan kurs 7. |
| **Cognitive load** — ny syntax, paradigm | Python är pedagogiskt approachable. FastAPI ≈ Express. Lägre cognitive load än ny domän. |
| **Kvalitetsrisk** — om det görs halvhjärtat blir det utspätt | Måste byggas runt ett *konkret AI-fullstack-projekt* med React+FastAPI+RAG i portfolio |
| **Datasignal är osäker** | 17% är säkert; verklig kombo-signal är sannolikt högre men inte verifierbar utan att ta in `mixed` |

---

## Frågor till LG-beslut

1. **Strategiskt vägval:** Ska Python (FastAPI) introduceras i FJS26 som AI-backend i kurs 7?
2. **Om ja — prioritet mellan tre kandidater för de 10 fattande YHp:**
   - Python i kurs 7 (AI-fullstack trajectory)
   - Hårda gap i kurs 8 (observability, distributed_systems, backend-prestanda)
   - Utökning av LIA (1-2 v extra praktik)
3. **Om Python ja men det krockar med kurs 8 gap:** kompromiss (5+5) eller utöka programmet totalt till 435/440 YHp (kräver MYH-godkännande)?
4. **Identitetsfråga:** påverkar Python-tillägget hur programmet ska marknadsföras och positioneras gentemot studerande och företag?

---

## Datasignaler för referens

Från `output/report.md` — SE-niche (n=69, icke-Java/.NET fullstack-annonser):

| Teknik | SE niche | SE mid+senior | Intl |
|---|:---:|:---:|:---:|
| `python` | **17.4%** | 14.5% | **24.3%** |
| `nodejs` | 43.5% | 43.6% | 20.0% |
| `react` | 65.2% | 70.9% | 47.8% |
| `typescript` | 49.3% | 56.4% | 40.0% |

Och AI-trajectory-signaler:

| Signal | SE niche | SE mid+senior |
|---|:---:|:---:|
| `ai_tools_general` | 37.7% | 38.2% |
| `agentic_workflows` | 24.6% | 27.3% |
| `context_management` | 11.6% | 10.9% |

---

## Bestämt / inte under omprövning

- Programidentitet förblir "Fullstack JavaScript" — Python kommer in som *AI-backend*, inte som primärt språk
- Kurs 4 (Fullstackutveckling, 75 YHp) med Node+Express som primär backend förblir oförändrad
- Kurs 8 (Avancerad fullstackutveckling) JS-ramverkets-val (Vue/Svelte/Angular) förblir oförändrad
- Om Python inkluderas ska kurs 7:s utökning matchas med YHp-ökning, inte packas in på 20 YHp ([[feedback-kurs7-oversiktlig-niva]])
