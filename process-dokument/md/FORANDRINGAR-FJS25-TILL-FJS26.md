# Förändringar FJS25 → FJS26

> Sammanfattning av kursplaneförändringar mellan nuvarande utbildning (FJS25) och den nya profilen Fullstack JavaScript 2026 (FJS26). Strategiska huvudförändringar först, kursvis nedbrytning därefter.

---

## 1. Strategiska huvudförändringar

### 1.1 Optimeringsmål: maximera junior-anställning utanför Java/.NET

Hela FJS26 är optimerad för anställning i fullstack-roller **utanför Java/.NET-stacken** i Sverige inom 6 månader från examen. Skolan har redan utbildningar i Java- och .NET-stackarna — FJS26 ska komplementera, inte konkurrera. Underlaget är datadrivet via projektet `perfect-fullstack` (LLM-extraktion av 453 jobannonser, primärpopulation 69 SE-niche-annonser).

### 1.2 LIA som primär anställningskanal

Explicita junior-annonser är extremt sällsynta i SE-niche (2 % = 4 av 206). FJS26 är designad så att studenten ska vara **attraktiv att ta in på LIA**, inte att matcha junior-annonser. Detta påverkar flera kursval — LIA-employability är en first-class designparameter.

### 1.3 Strukturell omfördelning av kurser

| FJS25 | FJS26 | Förändring |
|---|---|---|
| UX, användbarhet och tillgänglighet (15 YHp) | **Borttagen** — A11y/WCAG flyttat till kurs 2 och kurs 6 | -15 YHp |
| Cloud, CI/CD och arbetsmetodik (20 YHp) + Avancerad fullstackutveckling (50 YHp) | **Sammanslagna** till kurs 8 *Avancerad fullstackutveckling, Cloud och DevOps* (65 YHp) | -5 YHp |
| — | **Ny kurs 6** *Kvalitetssäkrad leverans* (25 YHp) | +25 YHp |
| Frontendutveckling (55 YHp) | Frontendutveckling (40 YHp) — SEO, XML, metadata för sociala medier borttaget | -15 YHp |

### 1.4 Backend-tyngning

LG-mötet 2026-05-26 beslutade att förstärka backend-fokus. Kurs 4 *Fullstackutveckling* (75 YHp) är expanderad: SQL prioriteras (70/30 SQL/NoSQL), routes/controllers/services-arkitektur, SOLID-light (SRP + DIP), OWASP top 10, autentisering/autorisering/validering, secrets-hantering, Docker, React med ekosystem.

### 1.5 AI som tråd i hela programmet

AI är **aldrig ett kursmål** (fältet rör sig för fort). Istället löper AI som löpande tråd genom alla kurser. Kurs 7 *AI inom fullstackutveckling* (20 YHp) hålls medvetet på primer-/översiktlig nivå.

### 1.6 Formativ bedömning + code review som programprincip

Code reviews, utkastfeedback och completion problems genomsyrar alla kurser från och med kurs 4. Formativ bedömning är operationaliserad i `FORMATIV-BEDOMNING.md` och som §6 i UPPDRAG.md. Code review introduceras explicit i kurs 4 och är därefter implicit i alla efterföljande kurser (ingen ny "introduktion" av konceptet).

### 1.7 Datadrivet underlag

Verktygsfrekvens och kompetensspår är extraherade från riktiga annonser och styr tekniska val: mainstream slår nyfikenhet. Topp 5 verktyg: React 65 %, TypeScript 49 %, Node.js 44 %, AWS 42 %, Docker 33 %, PostgreSQL 32 %.

---

## 2. Omfattningstabell

| # | Kurs | FJS25 YHp | FJS26 YHp | Δ |
|---|---|:---:|:---:|:---:|
| 1 | Branschen för fullstackutvecklare | 10 | 10 | — |
| 2 | Frontendutveckling | 55 | 40 | **-15** |
| 3 | Avancerad frontendutveckling (med Typescript) | 40 | 40 | — |
| 4 | Fullstackutveckling | 75 | 75 | — |
| 5 | Projektmetodik och agila metoder | 15 | 15 | — |
| 6 | (FJS25: UX) → (FJS26: Kvalitetssäkrad leverans) | 15 | 25 | **+10** |
| 7 | AI inom fullstackutveckling | 20 | 20 | — |
| 8 | (FJS25: Cloud+CICD 20 + Avancerad FS 50 = 70) → (FJS26: sammanslaget) | 70 | 65 | **-5** |
| 9 | LIA | 110 | 110 | — |
| 10 | Examensarbete | 20 | 20 | — |
| | **Totalt** | **430** | **420** | **-10** |

**Anm:** FJS26 ligger för närvarande på 420 YHp. 10 YHp behöver allokeras (öppna kandidater: utöka kurs 7 för Python/FastAPI som AI-backend, utöka kurs 8 för observability/distributed systems/backend-prestanda, eller utöka LIA med 1-2 v).

---

## 3. Kursvis nedbrytning

### Kurs 1 — Branschen för fullstackutvecklare (10 YHp)

Oförändrad från FJS25. Innehåll: IT-branschens roller, teknikstackar, arbetsmetoder, AI-verktyg, säkerhet, hållbarhetsbegrepp.

### Kurs 2 — Frontendutveckling (40 YHp, -15 från FJS25)

**Borttaget:**
- Teknisk SEO-anpassning
- XML
- Metadata för sociala medier och externa tjänster

**Tillagt:**
- Ny färdighet: *Ta fram mockups och wireframes för webbgränssnitt*
- UX/UI, användbarhet och tillgänglighet (a11y/WCAG) — flyttat hit från FJS25 kurs 6 som yrkesmässig baslinje
- Moderna JavaScript-standarder (ES2024+) explicit (spread/rest, destructuring, modulsystem)
- AI-verktyg som tråd i utvecklingsarbetet (med kritisk granskning)

**Fokus:** Webbteknik och webbutveckling med HTML, CSS, moderna JavaScript-standarder, Git, browser-API:er (Fetch, localStorage), JSON, HTTP-protokollet, responsiv design.

### Kurs 3 — Avancerad frontendutveckling med Typescript (40 YHp)

**Namnbyte:** "Avancerad frontendutveckling och Typescript" → "Avancerad frontendutveckling **med** Typescript" (TS som primärt språk genom hela kursen).

**Borttaget:**
- DOM, Fetch, localStorage (redan i kurs 2)

**Tillagt/förstärkt:**
- Asynkrona mönster (Promises, async/await)
- Verktygskedja (Node.js, npm, Vite, linting/formatting)
- Programmeringsparadigm (funktionell + objektorienterad)
- TS-djup (generics, utility types, narrowing/typeguards, tsconfig)
- Projektarkitektur (modul-uppdelning, separation of concerns, loose coupling)
- Felsökningstekniker (devtools, source maps)
- Frontendsäkerhet (API-nycklar, secrets)
- Kodgranskning och refaktorering som arbetsmetoder
- AI som stöd, kritisk granskning av AI-kod

### Kurs 4 — Fullstackutveckling (75 YHp)

Stor expansion i innehåll trots oförändrad YHp. Är navet i hela programmet.

**Tillagt/förstärkt:**
- Node.js + TypeScript som primär backend-stack
- Routes → controllers → services-arkitektur (lager-uppdelning)
- SOLID-light: SRP (Single Responsibility) + DIP (Dependency Inversion)
- SQL-databaser fördjupat (PostgreSQL, raw SQL + ORM som Drizzle, 70/30 SQL/NoSQL)
- NoSQL där det är lämpligt utifrån krav
- REST-API:er med autentisering, autorisering, validering, felhantering
- OWASP top 10 + secrets-hantering
- Docker för utvecklingsmiljö och containerisering
- React (komponenter, hooks, state management med Context + Zustand/Redux), routing (React Router), fullstackramverk (Next.js), prestandamedveten utveckling
- Stora fullstackprojektet i grupp (v 12-23) som examination

**Examination:** Skriftlig tentamen (kunskaper) + individuell inlämning (färdigheter) + projektarbete i grupp (kompetenser).

### Kurs 5 — Projektmetodik och agila metoder (15 YHp)

Oförändrad från FJS25.

### Kurs 6 — Kvalitetssäkrad leverans (25 YHp, ny i FJS26)

**Ersätter:** FJS25 kurs 6 *UX, användbarhet och tillgänglighet* (15 YHp). UX/A11y flyttat till kurs 2 som baslinje.

**Innehåll:**
- Testning (enhets-, integrations-, E2E-tester; kritiska tester i fullstackprojektet)
- A11y/WCAG som kvalitetskrav (utöver baslinjen i kurs 2)
- Migrationer i dev-perspektiv
- Dokumentation av kod och API:er
- Change management från dev-perspektiv (release-strategier, feature flags som rollout, zero-downtime är *trimmat till dev-perspektiv*; drift-perspektivet ligger i kurs 8)

**Position i program:** Brygga mellan implementationsfärdighet (kurs 4) och avancerad fullstack (kurs 8).

### Kurs 7 — AI inom fullstackutveckling (20 YHp)

**Hålls på primer-/översiktlig nivå** — medvetet val: fältet rör sig för fort för djup mästring, och AI löper som tråd genom hela programmet.

**Innehåll:**
- AI-modeller (ML, neurala nätverk, LLM:er)
- Risker (bias, integritet, ansvar, svagheter i AI-kod)
- AI-komponenter (klassificering, semantisk sökning, NLP-moduler)
- Prompt- och context engineering
- Moderna AI-utvecklingsmiljöer (Claude Code, Cursor, OpenCode) och deras komponenter (context, tokens, skills, agenter)
- AI-systemarkitekturer med fokus på RAG (Retrieval-Augmented Generation)
- Testning och bedömning av AI-lösningar
- Etiska och hållbarhetsmässiga aspekter

**Öppen diskussionspunkt:** Python/FastAPI som AI-backend (se `LG-DISKUSSION-kurs7-python.md`).

### Kurs 8 — Avancerad fullstackutveckling, Cloud och DevOps (65 YHp)

**Sammanslagning** av FJS25 kurs 8 (*Cloud, CI/CD och arbetsmetodik*, 20 YHp) + kurs 9 (*Avancerad fullstackutveckling*, 50 YHp) = 70 YHp → 65 YHp i FJS26 (5 YHp besparing eftersom delar nu täcks tidigare).

**Innehåll:**
- Cloud hosting (AWS, Azure, GCP) + serverless
- CI/CD-pipelines och DevOps-metoder
- Avancerad Git
- GraphQL (som alternativ till REST)
- Valbart JavaScript-ramverk (Vue, Svelte, Angular — utöver React i kurs 4)
- Routing, state management, rendering, prestanda och skalbarhet inom valt ramverk
- Headless CMS

**Borttaget från denna kurs eftersom täckt tidigare:**
- NoSQL-databaser (kurs 4)
- Docker (kurs 4)
- TypeScript som fullstack-språk (kurs 3, 4)
- OWASP-säkerhet (kurs 4)
- Testning (kurs 6)
- AI-verktyg generellt (kurs 7 + tråd)

**Öppna diskussionspunkter:** observability (44 % i niche), backend-prestanda, distributed systems, Kubernetes/Terraform (se `LG-DISKUSSION-kurs8.md`).

### Kurs 9 — LIA (110 YHp)

Oförändrad från FJS25 i innehåll och struktur. **Förkunskapskrav uppdaterade** till FJS26:s 8 år-1-kurser. Eventuellt utökas med 1-2 veckor (öppen fråga).

### Kurs 10 — Examensarbete (20 YHp)

Oförändrad från FJS25.

---

## 4. Tillkomna pedagogiska principer

| Princip | Var |
|---|---|
| **Formativ bedömning** som programprincip — code reviews, utkastfeedback, completion problems | UPPDRAG.md §6, FORMATIV-BEDOMNING.md, genomsyrar alla kurser |
| **Code review** som implicit arbetsmetod från kurs 4 | Inte ny "introduktion" i senare kurser |
| **Worked examples + fading + completion problems** (Cognitive Load Theory) | Pedagogisk grund i kurs 2-4 |
| **AI som tråd** istället för isolerad ämnesblock | Alla kurser; kurs 7 är primer |
| **Lärautonomi** | UPPDRAG.md §7 — lärare har frihet inom uppdragets ramar |
| **Datadriven validering** | `perfect-fullstack` pipeline kör mot kursinnehåll |

---

## 5. Avgränsningar och medvetna val

- **Programidentiteten "Fullstack JavaScript" behålls.** Python är inte primärt språk — möjlig framtida inkludering som *AI-backend* (FastAPI) i kurs 7 är under utredning (LG-diskussion).
- **Mainstream slår nyfikenhet** är beslutsregeln för tekniska val. React (65 % i niche) prioriteras framför Vue/Svelte/Angular.
- **Senior-trajectory är inte målet.** Studenten ska kunna växa mot mid/senior men huvudoptimering är junior + LIA-attraktivitet.

---

## 6. Öppna frågor inför LG-möte

1. **De 10 fattande YHp:** Python i kurs 7 (+10), kurs 8 gap-stoppning (observability/distrib/backend-perf, +10), eller LIA-utökning (+10) — eller kompromiss?
2. **Observability** explicit kursmål eller implicit i kurs 8? (44 % signal)
3. **Distributed systems** explicit eller implicit i kurs 8? (48 % signal)
4. **Backend-prestanda** (caching, query-opt, indexstrategi) i kurs 8? (59 % signal)
5. **JS-ramverk i kurs 8:** valbart (Vue/Svelte/Angular) eller fördjupad React?
6. **Python/FastAPI som AI-backend i kurs 7?**
