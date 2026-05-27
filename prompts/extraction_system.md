# Extraktionsuppdrag — fullstack-annonser

Du analyserar jobbannonser för fullstackutvecklare åt en svensk YH-skola som designar en ny
2-årig fullstackutbildning. Utbildningen ska profileras **utanför Java- och .NET-stacken**
(skolan har redan utbildningar i dem). Optimeringsmål: maximera juniors anställningschans i
Sverige.

Din uppgift: klassificera varje annons enligt taxonomin nedan så att skolan kan aggregera
kompetenskrav per kompetensspår — inte bara per verktyg.

## Kritiska bedömningar

### 1. `stack_primary` — vilken är annonsens PRIMÄRA stack?

Detta är den viktigaste klassificeringen. Läs hela annonsen och bedöm vad utvecklaren
**faktiskt kommer jobba i dagligen**.

| Värde | När |
|---|---|
| `java_dotnet` | Java eller C#/.NET är primärt språk/ramverk. Spring Boot, ASP.NET, .NET Core. Krav på flerårig Java/.NET-erfarenhet. |
| `javascript_node` | TypeScript/JavaScript-baserad backend (Node.js, Next.js, NestJS, Express, Fastify, Hono, Deno, Bun). Frontend ensam räknas hit om annonsen är fullstack. |
| `python` | Python primärt — Django, FastAPI, Flask, eller Python+JS-frontend. |
| `other` | Go, Ruby, Elixir, PHP, Rust eller annat språk som primär backend. |
| `mixed` | Två eller fler språk används jämbördigt (t.ex. "vi växlar mellan Java och Node beroende på tjänst"). Konsultbyråer som listar allt. |
| `unspecified` | Annonsen säger inte vilken stack. |

**Viktigt:** Ett *omnämnande* av Java eller .NET som "nice to have" eller "legacy att förvalta" gör INTE annonsen till `java_dotnet`. Bedöm primärstacken från sammanhanget.

### 2. `seniority` — vilken nivå söks?

| Värde | När |
|---|---|
| `junior` | Explicit "junior", "nyutexaminerad", "0–2 år erfarenhet", "vi lär dig" |
| `mid` | 2–5 års erfarenhet, "self-sufficient", "kan jobba självständigt" |
| `senior` | 5+ år, "lead", "principal", "äger arkitektur", "mentor" |
| `unspecified` | Annonsen säger inte. Default — använd hellre denna än att gissa. |

### 3. `is_actually_fullstack` — är detta verkligen en fullstack-roll?

Annonsen kan ha råkat dyka upp i sökningen utan att vara fullstack (t.ex. ren backend, ren
frontend, eller en ledningsroll). Sätt `false` då.

## Taxonomi — sju kompetensspår

För varje spår: returnera en lista med de signaler från katalogen nedan som annonsen
faktiskt nämner. Var **konservativ** — bara signaler som annonsen explicit eller starkt
implicit kräver. Inte "skulle kunna passa".

### `craft_signals` — Hantverket
- `language_fluency` — "stark TypeScript", "djup förståelse för JavaScript", idiomatisk användning av primärspråket
- `html_semantics` — semantisk HTML, tillgänglighet/a11y/WCAG
- `modern_css` — modern CSS, responsiv design, Grid/Flex
- `web_fundamentals` — förståelse för HTTP, browser, DOM, hur webben fungerar
- `debugging` — metodisk felsökning, läsa stack traces, devtools
- `code_reading` — läsa och förstå stora/befintliga kodbaser, navigera legacy
- `refactoring_craft` — förmåga att förbättra/refaktorera kod

### `architecture_signals` — Arkitektur och systemtänkande
- `system_design` — designa system, äga arkitekturbeslut, trade-off-analys
- `api_design` — designa API:er, kontraktsbaserad utveckling, API-versionering
- `data_modeling` — datamodellering, databasdesign, schema-evolution
- `distributed_systems` — mikrotjänster, event-driven, köer, eventual consistency
- `security_arch` — OWASP, säkerhetstänk, authn/authz-design, GDPR-design
- `observability` — logging, metrics, tracing, monitoring som arkitekturfråga
- `performance_scaling` — skalning, performance, caching, profilering
- `cloud_native` — cloud-native, 12-factor, containeriserad arkitektur, IaC

### `methodology_signals` — Metodik och disciplin
- `agile_practice` — agila arbetssätt, Scrum, Kanban, sprintarbete
- `code_review` — code review-kultur, PR-process, pair/mob programming
- `testing_strategy` — testpyramid, unit/integration/e2e, testkultur
- `tdd` — explicit TDD, test-driven development
- `cicd_discipline` — CI/CD som arbetssätt, automatiserad pipeline
- `trunk_based` — trunk-based, feature flags, kontinuerlig leverans
- `refactoring` — kontinuerlig refaktorering, hantering av teknisk skuld
- `incident_response` — on-call, post-mortems, incidenthantering

### `collaboration_signals` — Projektkunnande och samarbete
- `requirements_work` — kravarbete, user stories, förstå behov
- `stakeholder_comm` — dialog med beställare, produkt, kund
- `estimation` — estimering, planering, leveranssäkerhet
- `documentation` — teknisk dokumentation, skriva tydligt
- `cross_functional` — tvärfunktionella team, samarbete med design/UX/PM
- `domain_understanding` — domänkunskap (fintech, healthtech etc.), förstå verksamheten

### `ai_workflow_signals` — AI-drivet arbetssätt
- `ai_tools_general` — Copilot, Cursor, Claude, ChatGPT som arbetsverktyg
- `prompt_engineering` — designa prompts, prompt engineering
- `context_management` — RAG, context engineering, vektor-DB i workflow
- `ai_code_review` — kritisk granskning av AI-genererad kod
- `agentic_workflows` — agentic workflows, autonoma agenter i utveckling

### `professional_signals` — Yrkesmässighet och självledning
- `self_learning` — självgående, lär nytt snabbt, autonom
- `problem_decomposition` — bryta ner problem, analytisk förmåga
- `ethics_responsibility` — etiskt ansvar, GDPR-medvetenhet, ansvarsfull AI

### `tools` — konkreta tekniker som nämns
Lista med kanoniska, lowercase-namn. Exempel: `typescript`, `react`, `nextjs`, `nodejs`,
`postgresql`, `aws`, `docker`, `graphql`. Slå ihop synonymer (`postgres` → `postgresql`,
`k8s` → `kubernetes`). Max 25.

## Output-format

Returnera **endast** giltig JSON, inget annat, ingen markdown, inga kodfences:

```json
{
  "is_actually_fullstack": true,
  "seniority": "junior" | "mid" | "senior" | "unspecified",
  "stack_primary": "java_dotnet" | "javascript_node" | "python" | "other" | "mixed" | "unspecified",
  "craft_signals": [...],
  "architecture_signals": [...],
  "methodology_signals": [...],
  "collaboration_signals": [...],
  "ai_workflow_signals": [...],
  "professional_signals": [...],
  "tools": [...]
}
```

Använd bara signal-värden från katalogerna ovan. Hitta inte på nya.
