# Beslutsunderlag: ny 2-årig YH-fullstackutbildning

**Till:** Ledningsgruppen
**Från:** Sandra Larsson
**Datum:** 2026-05-27
**Status:** Beslutsunderlag — kräver ledningsgruppsbeslut

---

## Sammanfattning på en sida

Skolan föreslås starta en tredje fullstackutbildning som komplement till de existerande Java- och .NET-programmen. Den nya utbildningen profileras mot **TypeScript/React/Node.js-stacken på AWS, med Python som dedikerat AI-integrationsspår** — den dominerande icke-Java/.NET-nischen på svensk arbetsmarknad.

**Optimeringsmål:** maximera andelen utexaminerade som inom 6 månader från examen har en anställningsrelevant tjänst.

**Tre vägledande beslut formar utbildningen:**

1. **Tekniken är medel, kompetensen är mål.** Annonsanalysen visar att 6 av 10 inträdesbarriärer på arbetsmarknaden är *arkitekturella* eller *systemtänkande* — inte verktygsspecifika. Utbildningen byggs runt sju kompetensspår där tekniker är vehikeln.
2. **LIA är huvudanställningskanalen, inte ett bihang.** Av 206 svenska fullstack-annonser söker bara 4 (2%) explicit juniorer. Anställning sker huvudsakligen via LIA, rekryteringsevent och relaxade senior-krav. LIA-strategin måste därför genomsyra utbildningens design.
3. **AI-arbetsflöde är 2026-grundkompetens.** 38% av svenska annonser i nischen nämner explicit AI-verktyg i arbetsbeskrivningen — mer än internationellt. Det är inte ett bihang utan en löpande tråd genom hela utbildningen.

**Underlagets evidens:** Datadriven analys av 453 jobbannonser (206 svenska från Arbetsförmedlingens JobTech-API, 247 internationella från RemoteOK/We Work Remotely/Hacker News), strukturerat klassificerade av Claude Sonnet 4.6 mot en taxonomi i sju kompetensspår. Full kompetensfrekvens i `output/report.md`. Detaljerad uppdragsbeskrivning i `UPPDRAG.md`.

**Beslut som efterfrågas** (sida 7): start­datum, antal platser, lärarrekrytering, branschråd, finansieringsbeslut, beslut att lämna in MYH-ansökan.

---

## 1. Profilering och differentiering

| Aspekt | Java-fullstack (befintlig) | .NET-fullstack (befintlig) | **Ny utbildning** |
|---|---|---|---|
| Primärspråk | Java | C# | **TypeScript** |
| Backend-ramverk | Spring Boot | ASP.NET Core | **Node.js (Express/Hono/Nest)** |
| Frontend | Varierande | Blazor, React | **React + Next.js** |
| Cloud | Azure, AWS | Azure | **AWS, Vercel** |
| Andra-spår / specialisering | — | — | **Python (FastAPI) för AI-integrerade applikationer** — egen 15 YHp-kurs i HT2 |
| Marknadsandel SE-fullstack | 41% | (ingår i 41%) | **35%** (JS/Python/Other tillsammans) |
| Differentierande styrkor | Stora företag, bank, försäkring | Microsoft-ekosystem, offentlig sektor | **Startup/scale-up, modern produktutveckling, AI-tunga produkter** |

**Profilen i en mening:** *"Utbilda fullstack-utvecklare för moderna produktorganisationer och scale-ups där hastighet, arkitektur­medvetenhet och AI-integration är avgörande."*

---

## 2. Marknadsbild — vad evidensen visar

### Underlag

| Källa | Antal annonser | Region | Roll i analysen |
|---|---|---|---|
| JobTech Dev (Arbetsförmedlingen) | 206 | Sverige | **Primärkälla — driver alla rekommendationer** |
| RemoteOK | 45 | Internationell | Triangulering |
| We Work Remotely | 112 | Internationell | Triangulering |
| Hacker News "Who is hiring" maj 2026 | 90 | Internationell | Triangulering (scale-up-signal) |
| **Totalt** | **453** | | |

Sonnet 4.6 klassificerade varje annons mot sju kompetensspår + seniority + primärstack. Analysen omfattar därför *kompetensspår*, inte bara verktygslistor — vilket är en kvalitativ förbättring jämfört med branschens standard­analyser.

### Tre fynd som styr beslutet

**Fynd 1: Java/.NET dominerar — men det finns en distinkt, stor nisch utanför.**

| Primärstack i SE-annonser | Antal | Andel |
|---|---|---|
| Java eller .NET | 84 | 41% |
| Mixed (ofta Java-tungt) | 28 | 14% |
| **JavaScript/Node** | **40** | **19%** |
| Unspecified | 22 | 11% |
| Other (Go, Rails, PHP, Elixir) | 18 | 9% |
| Python | 14 | 7% |

Nischen utanför Java/.NET är **~46% av marknaden** (95 av 206 ads inkl. unspecified). Inom nischen är JavaScript/Node dominerande och kandiderar därför till primärstack.

**Fynd 2: Explicit junior-annonser är extremt sällsynta (2%).**

| Seniority i SE-annonser | Antal | Andel |
|---|---|---|
| Senior | 97 | 47% |
| Mid | 64 | 31% |
| Unspecified | 41 | 20% |
| **Junior** | **4** | **2%** |

Detta är inte ett analysfel — det är marknadsverkligheten. Svenska arbetsgivare anställer juniorer via *andra kanaler* än explicit junior-annonser: LIA, rekryteringsmässor, kontakter, och genom att tumma på senior-krav när rätt person dyker upp. **Implikation: LIA är en kärnstrategisk fråga, inte en logistisk.**

**Fynd 3: AI-arbetsflöde är högre i SE än internationellt.**

| Signal | SE-nisch | Internationellt |
|---|---|---|
| AI-verktyg generellt | **38%** | 24% |
| Agentic workflows | **25%** | 24% |

Detta är överraskande och har två tolkningar: (a) svenska arbetsgivare är tidiga med att skriva ut AI-krav i annonser, (b) svenska arbetsgivare ser AI som differentierande och nämner det aktivt. Båda stödjer slutsatsen att utbildningen *måste* hantera AI-arbetsflöde — inte som bonus, utan som grundkompetens.

---

## 3. Kompetensprofil — vad utbildningen producerar

Utbildningen ska producera en utexaminerad som kan **alla inträdesbarriärer** och som har **bevisad förmåga inom minst hälften av differentiererna**. Varje krav nedan är data­drivet — siffran anger andel av primärpopulationen (SE-nisch) som efterfrågar det.

### Inträdesbarriärer (≥40% — obligatoriskt i utbildningen)

| # | Kompetens | Spår | Marknads­krav |
|---|---|---|---|
| 1 | Lärautonomi och självgång | Yrkesmässighet | **91%** |
| 2 | Språkflyt i primärspråket (TS/JS) | Hantverket | **90%** |
| 3 | Samarbete tvärfunktionellt | Projektkunnande | **87%** |
| 4 | Cloud-native arkitekturtänk | Arkitektur | 78% |
| 5 | Problem­decomposition | Yrkesmässighet | 78% |
| 6 | Web fundamentals (HTTP/DOM/browser) | Hantverket | 75% |
| 7 | CI/CD som arbetssätt | Metodik | 73% |
| 8 | API-design | Arkitektur | 65% |
| 9 | Performance & skalning | Arkitektur | 59% |
| 10 | Domänförståelse | Projektkunnande | 58% |
| 11 | Systemdesign-tänk | Arkitektur | 48% |
| 12 | Distribuerade system-koncept | Arkitektur | 48% |
| 13 | Testningsstrategi | Metodik | 46% |
| 14 | Observabilitet | Arkitektur | 44% |
| 15 | Stakeholder-kommunikation | Projektkunnande | 42% |

**Mönster:** *Sex av de femton inträdesbarriärerna är arkitektur eller systemtänk.* Detta bekräftar att utbildningen måste vara arkitektur-tung, inte verktygs-tung.

### Differentierare (15–40% — ger edge mot andra juniorer)

`security_arch` 39% · `ai_tools_general` 38% · `data_modeling` 35% · `agile_practice` 33% · `requirements_work` 29% · `code_review` 25% · `agentic_workflows` 25% · `debugging` 22% · `refactoring_craft` 22% · `documentation` 19% · `modern_css` 17%

### Vad utbildningen *inte* prioriterar

Signaler under 15% i nischen prioriteras ner till workshop-format eller LIA-projekt: `code_reading`, `context_management` (AI), `incident_response`, `refactoring`-disciplin, `html_semantics`, `ethics_responsibility`, `trunk_based`, `TDD`, `prompt_engineering`, `ai_code_review`, `estimation`.

**OBS:** Att en signal är låg-frekvent i annonser betyder inte att den är oviktig — det betyder att arbetsgivare inte kräver den explicit. Vi tar in dem i utbildningen som *exponering* (workshops, gästföreläsare, valbar fördjupning) men gör dem inte till obligatoriska bedömningsmoment.

---

## 4. Förslag på kursstruktur (58 veckor undervisning + LIA i VT2)

Programstruktur enligt skolans terminsmodell:

| Termin | Längd | YHp | Roll i utbildningen |
|---|---|---|---|
| HT1 (höst år 1) | 16 v | 80 | Fundament — från noll till kan-skriva-kod |
| VT1 (vår år 1) | 25 v | 125 | Bredden — frontend, backend, projekt i team |
| HT2 (höst år 2) | 17 v | 85 | Djupet — arkitektur, drift, examensprojekt |
| VT2 (vår år 2) | ~20 v | ~100 | LIA (anställningsförberedelse) |
| **Totalt** | **~78 v** | **~390 YHp** | |

### HT1 — 16 veckor / 80 YHp
Fokus: **från noll till kan-skriva-kod**. Studenter kommer in med gymnasie-Programmering 1 — fundament måste etableras innan något annat fungerar.

| # | Kurs | YHp | Veckor | Innehåll |
|---|---|---|---|---|
| 1 | Yrkesintroduktion och utvecklingsmiljö | 15 | 3 | YH-rollen, agila grunder, lärautonomi, Git/terminal/IDE, CI-introduktion, AI som hjälpverktyg från dag 1 |
| 2 | Programmering i TypeScript | 40 | 8 | Fundament + datastrukturer + tester + debugging + refactoring-hantverk + kodgranskning. Mängdträning. |
| 3 | Webbutveckling fundamentals | 25 | 5 | HTML semantik, modern CSS (Grid/Flex), HTTP, DOM, browser, accessibility |

### VT1 — 25 veckor / 125 YHp
Fokus: **bredden över hela stacken**. VT1:s ovanliga längd ger utrymme att gå djupt på frontend och även få in backend + databas — vilket gör att studenten kommer in i HT2 med fullstack-bas redan på plats.

| # | Kurs | YHp | Veckor | Innehåll |
|---|---|---|---|---|
| 4 | Frontend med React och Next.js | 50 | 10 | Komponenter, state, hooks, Next.js, server components, prestanda, a11y, designsystem, AI-driven UI-utveckling |
| 5 | Backend och datalager | 50 | 10 | Node.js (Express/Hono), REST-design, auth/sessions, validation, PostgreSQL, relationsmodellering, ORM (Prisma/Drizzle) |
| 6 | Projektkurs 1 — fullstack-leverans i team | 25 | 5 | Riktig brief, agila praktiker, code review, dokumentation, presentation till bransch |

### HT2 — 17 veckor / 85 YHp
Fokus: **arkitektur, drift, Python+AI, examen**. Den senior-trajectory-laddade terminen — där "junior med senior-potential" levereras.

| # | Kurs | YHp | Veckor | Innehåll |
|---|---|---|---|---|
| 7 | Arkitektur och säkerhet | 25 | 5 | System design, API-design (kontrakt, versionering), OWASP, GDPR, secrets management, observability, distribuerade-system-koncept, performance/skalning |
| 8 | Python för AI och data | 15 | 3 | Python-syntax (snabbgenomgång), FastAPI-grund, Python i AI-stacken (LangChain/MCP), scripting och data-manipulation. **Inte ett alternativt fullstack-spår** — Python som verktyg för AI-integrerade applikationer. |
| 9 | DevOps och molntjänster | 20 | 4 | Docker, CI/CD, AWS/Vercel-deployment, monitoring, IaC-introduktion |
| 10 | Examensprojekt | 25 | 5 | Individuellt projekt med arkitekturmotivering, presentation till branschpanel |

### VT2 — LIA, ca 20 veckor / ca 100 YHp
LIA designas som en *anställningskanal*. Se §7 nedan för LIA-strategi.

**Total: 10 kurser + LIA = 11 läromoment.** Strukturen kan ytterligare slås samman om skolans norm är färre, men under ~8 kurser börjar varje kurs bli så bred att lärandemålen blir svåra att hålla sammanhängande för MYH-ansökan.

### Genomgående trådar (inte separata kurser)

- **AI-arbetsflöde:** varje kurs har ett AI-tillämpningsmoment där det är pedagogiskt motiverat. Kursplanerna specificerar *när* AI ska användas, *när inte*, och *hur AI-output ska granskas kritiskt*.
- **Hantverket:** mängdträning genomsyrar alla programmeringskurser. Kodgranskning, refactoring och problem-decomposition är återkommande bedömningsmoment.
- **Projektkunnande:** alla projektmoment kör skarpa agila praktiker (stand-up, retro, sprint review). Detta är *inte* en separat kurs utan en *praktik*.
- **Yrkesmässighet:** kontinuerlig handledning, mentor­program, reflexionsmoment. Detta är där "senior-trajectory" odlas.

---

## 5. Senior-trajectory — så bygger vi för 3-5 års framtid

> *"Utbildningen ska producera en utvecklare som är junior idag men senior om 3-5 år."*

Detta kräver fyra explicita designval:

1. **Lär ut principer, inte bara verktyg.** Varje teknikval introduceras tillsammans med *varför* det ser ut som det gör. Studenten ska kunna resonera om alternativ, inte bara reproducera mönster.
2. **Arkitektur är obligatoriskt, inte bonus.** Sex av femton inträdesbarriärer är arkitekturella. Kurs 12 (Systemtänkande och arkitektur) får inte krympas i schema­optimering.
3. **Lärautonomi är ett bedömningsmoment, inte en personlighet.** Studenten ska bevisa att hen kan lära sig nytt material utan kurs — det är vad en senior gör hela tiden. Examensprojektet inkluderar en valbar teknik som inte täckts i undervisningen.
4. **Critical thinking om AI-output.** I en värld där AI genererar 50%+ av kod måste studenten kunna *granska* AI:s arbete — inte bara producera kod med AI. Detta är en yrkesetisk fråga, inte bara en teknisk.

---

## 6. AI-arbetsflöde som genomgående tråd

**Beslut: AI är inte en separat kurs — det är en löpande tråd genom hela utbildningen.**

### Varför inte separat kurs

- Det "AI-rätta" arbetssättet ändras 4 gånger per år. En separat kurs blir föråldrad innan den körs.
- Att skilja "AI-arbete" från "vanligt arbete" är att lära fel mental modell. Inom 2 år är distinktionen meningslös för en utvecklare.
- AI är fundamentalt en *arbetssätts­fråga*, inte en kunskaps­domän. Det måste *praktiseras* i varje annan kurs.

### Konkreta moment per termin

| Termin | AI-fokus |
|---|---|
| 1 | Lär AI-verktyg som assistent (Claude Code, Cursor, Copilot). Förbjudet på kunskapsprov, tillåtet (och förväntat) i workshops och projektarbete. Reflexion om vad man lärt sig vs vad AI gjort. |
| 2 | AI-assisterad UI-utveckling, designsystem-iteration, kritisk granskning av AI-genererad React-kod. |
| 3 | AI för API-design (specgenerering, mock-data, testfall), context engineering, säkerhetsgranskning av AI-output. |
| 4 | Agentic workflows i större projekt (Claude Code med custom skills, multi-agent), yrkesetik och GDPR vid AI-användning. |
| LIA | Anpassning till varje företags AI-policy och verktygsstack. |

### Lärar­kompetenskrav

Att undervisa detta kräver lärare som *själva* använder AI-verktyg dagligen i arbete. Lärarrekrytering måste väga in detta. Branschråd ska besättas med medlemmar som har AI-arbetsflöde i sin egen produktion.

---

## 7. LIA-strategi — huvudanställningskanalen

Eftersom explicit junior-annonser är 2% av marknaden måste LIA designas som *anställningsförberedelse*, inte bara praktik.

### LIA-format
- **20 veckor**, en period (inte uppdelad). Tidsperioden ska räcka för att studenten ska kunna bidra med ett *levererat* projekt.
- LIA placeras **efter termin 4**, så att studenten kommer ut med full kompetens­ryggsäck.

### Värdval och relationer
- **Branschråd** med 5-8 företag i tech-scenen (start-up, scale-up, byrå, produkt­bolag). Branschrådets primära syfte är LIA-platser, sekundära är curriculum­råd.
- **Inriktning på företag som anställer**. Skolan kvalitetssäkrar att LIA-värdar har dokumenterad junior-anställning.

### LIA-projekt som leveransbevis
- Studenten ska komma ut med ett *visningsbart* projekt: en deployad applikation, en pull-request mergad i värdens kodbas, en presentation till värdens team.
- Detta blir CV-material och *portföljbevis* — den utan junior-titel-jakt på arbetsmarknaden.

### Mätning
Andelen studenter som får anställning hos LIA-värd inom 3 månader efter LIA-slut är ett primärt KPI för programmet. Mål: 40-50%.

---

## 8. Risker och mitigationsåtgärder

| Risk | Sannolikhet | Konsekvens | Mitigering |
|---|---|---|---|
| Stack-skifte under utbildningens livstid (t.ex. React tappar marknadsandel) | Medium | Hög — utbildningen designad mot specifik stack | Lär ut **principer först**, ramverk-flytt är då 2-3 v workshop. Kör analysen om varje år. |
| AI förändrar yrket så att junior-rollen i sig krymper | Hög | Hög — anställningsbarheten påverkas direkt | Designa explicit för "junior som *använder* AI", inte "junior som *gör* det AI inte kan". Differentiera mot AI-naiva utbildningar. |
| LIA-platser blir bristvara om svensk tech-marknad försämras | Medium | Hög — anställningsmål kraschar | Branschråd med formellt åtagande. Plan B: utländsk LIA (remote). |
| Lärarrekrytering — få lärare har TS/React/Node + AI-arbetsflöde + pedagogisk erfarenhet | Hög | Medium-hög | Hybrid­modell: anlita branschpraktiker som adjunkter för 30-50% av undervisningen. Inhouse-personal för didaktik. |
| Programmet konkurrerar trots allt med Java/.NET-programmen om sökande | Medium | Medium | Tydlig profilering mot start-up/scale-up i marknadsföring. Olika sökandegrupper. |
| Studenter med Programmering 1 är för tunna för Y1-tempot | Hög | Medium | Termin 1 designad explicit för noll-bas. Tidig diagnos och stödjande resurser för svaga studenter (extra workshop, peer-tutoring). |
| MYH-ansökan accepteras inte (för likt befintliga utbildningar) | Låg-medium | Total — programmet startar ej | Tydlig differentierings­motivering i ansökan (denna fil). Visa i ansökan att samtliga 3 program har olika målgrupper och tekniker. |

---

## 9. Mätbarhet och uppföljning

### Primära KPI:er (för MYH-uppföljning)
- **Examensgrad** — mål: ≥80%
- **Anställningsgrad inom 6 månader** — mål: ≥85%
- **Anställningsrelevant** — mål: ≥75% inom utbildningens kompetensspår

### Operativa KPI:er
- **LIA→anställning** — andel studenter anställda av LIA-värd inom 3 månader. Mål: 40-50%.
- **Lärar-NPS** — hur lärarna betygsätter programmet termin för termin.
- **Student-NPS efter examen** — vad rekommenderar utexaminerade?

### Återkommande marknadsanalys
Denna analys (`output/report.md`) körs **inför varje ansökningsomgång till MYH** och **inför varje större kursplane­revision**. Datapipelinen i `perfect-fullstack`-repot är byggd för att köras om utan manuella ingrepp.

---

## 10. Beslut som efterfrågas

Ledningsgruppen ombeds besluta om:

1. **Startbeslut** — ska MYH-ansökan lämnas in för utbildningsstart augusti 2027?
2. **Antal platser** — föreslås 25–30 studenter per kohort.
3. **Lärarrekrytering** — ska rekrytering inledas under hösten 2026? Vilken budgetram?
4. **Branschråd** — vilka företag bjuds in? Sandra föreslår en kortlista i separat dokument.
5. **Profilerings­namn** — föreslagna alternativ: *Fullstack Web Engineer*, *Modern Webbutveckling*, *Fullstack Cloud-Native*. Beslut kan tas senare.
6. **Budget för marknadsanalysens årliga återkörning** — ~50 SEK i API-kostnader per körning. Försumbart.

---

## Bilagor

- `UPPDRAG.md` — Uppdragsbeskrivning med taxonomi och resonemang
- `output/report.md` — Datadriven kompetensanalys med fullständiga frekvenstabeller
- `data/processed/ads.json` — Sonnet-klassificerade annonser (453 st)
- `data/processed/aggregate.json` — Aggregerade signaler
- `prompts/extraction_system.md` — LLM-prompt för reproducibilitet
