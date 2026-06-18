# Uppdragsbeskrivning — datadriven kompetensprofil för ny fullstack-YH

_Senast uppdaterad: 2026-05-26_

Detta dokument är arbetsunderlaget för analysen i `perfect-fullstack`. Det fungerar som:

- Brief för Sandra (uppdragsägare) och ledningsgruppen
- Kontext till LLM-extraktionen så modellen vet vad vi letar efter i annonserna
- Permanent referens när analysen körs om över tid

---

## 1. Bakgrund och stakes

Sandra arbetar på en svensk YH-skola med IT-utbildningar. Skolans förmåga att fortsätta bedriva och starta nya utbildningar styrs av två faktorer som båda är pressade just nu:

1. **Examinationsgrad** (andel som tar examen)
2. **Anställningsbarhet** — andel som landar i utbildningsrelevanta jobb

Arbetsmarknaden för frontend/backend/fullstack är ovanligt tuff 2026. Skolan har redan två fullstack-program: ett med Java-inriktning och ett med .NET-inriktning. Den utbildning som ska formas är *en tredje fullstack-utbildning* som **profileras bort från Java/.NET-stacken** för att undvika kannibalisering internt och täcka en annan del av marknaden.

Detta arbete är **beslutsunderlag till ledningsgruppen**. Det måste tåla granskning: spårbara datakällor, motiverade kursval, tydliga risker.

---

## 2. Målbild för utbildningen

> *"Den optimala 2-åriga fullstackutbildningen utanför Java/.NET-stacken — som **maximerar varje studerandes chans att få ett anställningsrelevant jobb** vid examen, och samtidigt ger bästa möjliga förutsättningar att växa mot senior."*

**Optimeringsmålet är anställningschans — inte teknisk perfektion, branschtrender eller bredd.** Allt curriculumval testas mot frågan: *gör detta en junior mer eller mindre anställningsbar i Sverige?*

Sex saker som följer av detta:

- **Junior på utexamenstid, senior om 3–5 år.** Vi lär ut **principer**, inte bara verktygsknappar. Verktyg är medium — inte mål.
- **Differentiering mot Java/.NET-programmen** är ett designkrav, inte en bieffekt. Annars konkurrerar utbildningarna om samma studenter och samma arbetsgivare.
- **Anställningsbar i Sverige** är primärt. Internationell trendspaning är validering, inte styrning.
- **Mainstream slår nyfikenhet.** Stora annonspoolar styr teknikval. En examenstagare som är trygg i React/TS/Node får fler intervjuer än en som flörtar med Svelte/Bun/Deno — oavsett vad som är roligare att undervisa.
- **Depth-first, inte breadth-first.** 60 veckor ger bättre anställningsbarhet om vi gör studenterna *djupt trygga* i en mindre stack än om vi sveper igenom åtta ramverk.
- **LIA är en av två huvudanställningskanaler**, inte ett bihang. Många får sitt första jobb där de gjorde LIA. Utbildningen ska producera studenter som *företag vill ta in på LIA* — vilket kräver snabb produktivitet på bekant stack, förmåga att arbeta i existerande kodbas, och starka soft skills.

### Mätbart framgångskriterium

> Andelen utexaminerade som inom 6 månader från examen har en anställningsrelevant tjänst, jämfört med branschens snittsiffra för YH IT-utbildningar.

Detta är vad MYH faktiskt mäter. Allt annat är proxy.

---

## 3. Studerandeprofil (förkunskaper)

Inkommande studerande har **gymnasie-Programmering 1**. I praktiken innebär det att de kan:

- Variabler, datatyper, operatorer
- Conditionals, loops, funktioner
- Basala datastrukturer (listor, ev. dictionaries)
- Något om OOP — ofta ytligt
- Oftast i Python eller Java

De kan **inte**:

- Git / versionshantering
- Projektstrukturer större än en fil
- Testning utöver print-debugging
- Hur webben fungerar tekniskt (HTTP, DNS, browser, server)
- API:er, databaser, frameworks
- Terminal/CLI-flyt
- Arbete i team med kod

**Pedagogisk konsekvens:** År 1 måste börja med fundament. Vi kan inte plöja in arkitekturresonemang förrän studenten har en mental modell av en kodbas som är större än en fil. Det här är hårdvalutan vi måste budgetera mot.

---

## 4. Tidsbudget

| Block | Längd | Anmärkning |
|---|---|---|
| Undervisning på plats | **60 veckor** | ~12 kurser à 5 veckor, alternativt 6 moduler à 10 v |
| LIA (lärande i arbete) | ~20–24 veckor | Halv termin, arbetsgivarförlagt |
| **Totalt** | **~84 veckor** | Standard 2-årig YH |

60 undervisningsveckor är *inte mycket*. En grov fördelning för diskussion:

- **År 1 (~32 v):** Programmeringsfundament, problem­lösning, webbgrunder, frontend (med React/TS som vehikel), Git/CLI/parverkstad
- **År 2 (~28 v + LIA):** Backend, databas, arkitektur, DevOps/cloud, examensarbete, AI-arbetsflöde — det här är där "junior-med-senior-potential"-aspekten levereras

---

## 5. Kompetensfokus — vad analysen ska leta efter

Detta är *omformuleringen* från tidigare arbete. Tidigare letade vi efter verktyg ("React, Node, AWS"). Det räcker inte. Annons­analysen ska istället klassificera kompetenser i sju spår:

### 5.1 Hantverket — programmering som färdighet
Foundation som allt annat vilar på. Att kunna *programmera* — inte bara känna till språkets syntax — är en färdighet som måste tränas tills den är automatiserad. Utan flyt i hantverket går det inte att resonera om arkitektur eller designval, och man kan inte heller granska AI-genererad kod kritiskt.

- **Språkflyt i TypeScript/JavaScript** — idiomatisk användning, inte översatt från Python eller Java. Typsystemet använt som verktyg, inte hinder. Asynk-mönster (promises, async/await) som mental modell.
- **HTML som semantik** — rätt element för rätt syfte, tillgänglighet (a11y), formulär, dokumentstruktur.
- **Modern CSS** — flexbox, grid, custom properties, responsiv design. Förstå *kaskaden* och specificity.
- **Web fundamentals** — HTTP, browser, DOM, hur en sida faktiskt laddas. Vad händer mellan webbläsare och server.
- **Debugging** — metodisk felsökning, läsa stack traces, browser devtools, IDE-debugger, binärsökning i problem.
- **Att läsa andras kod** — navigera obekanta kodbaser, hitta vad som händer var. En av de viktigaste yrkesfärdigheterna och oftast oövad.
- **Refaktorerings­hantverk** — extrahera funktion, byta namn, dela upp ansvar — utan att ändra beteende. Skild från *när* man refaktoriserar (det är metodik, 5.3).

Den här delen kräver mängdträning. AI förstärker behovet snarare än ersätter det.

### 5.2 Arkitektur och systemtänkande
Den största poängen för senior-trajectory. Det här är vad som skiljer en CRUD-skrivare från en ingenjör.

- Systemdesign-principer: separation of concerns, modularity, lagring, kopplingar
- API-design (REST-principer, kontrakter, versionering, gränssnittsdesign)
- Datamodellering (relationsdesign, indexstrategi, transaktioner, evolution)
- Distribuerade system-koncept (asynk, retry, idempotens, eventual consistency)
- Säkerhetsarkitektur (authn/authz, OWASP, datapolicy, secrets management)
- Observabilitet (loggning, metrics, tracing — som *praktik*, inte verktyg)
- Performance & skalning (caching, queries, profilering)
- Cloud-native designprinciper

### 5.3 Metodik och utvecklingsdisciplin
- Agila praktiker som faktiskt fungerar (inte ceremoni för dess egen skull)
- Code review-kultur, pair/mob programming
- Testningsstrategier — unit, integration, e2e, contract
- TDD som disciplin
- CI/CD som arbetssätt
- Trunk-based development, feature flags
- Refaktorering och teknisk skuld
- Incident response, post-mortems

### 5.4 Projektkunnande och samarbete
- Kravarbete och stakeholder-kommunikation
- Estimering och planering
- Teknisk dokumentation
- Tvärfunktionellt samarbete (PM, design, ops, sälj)
- Asynkron kommunikation, skriftlig tydlighet
- Domänförståelse — att förstå *vad* man bygger, inte bara hur

### 5.5 AI-drivet arbetssätt
Detta är **2026-grundkompetens** som inte fanns när Java/.NET-programmen designades. Att inte ha det i kursplanen är en utbildningsskuld från dag ett.

- Effektiv promptning för kod
- Kontextshantering (CLAUDE.md, skills, projektminne, IDE-konfig)
- Agentic workflows (Claude Code, Cursor, Copilot, Aider) — när vilket verktyg
- Kritisk granskning av AI-genererad kod (källkritik på kod)
- Säkerhets- och IP-aspekter — vad man inte skickar till LLM
- När man INTE ska använda AI (säkerhetskritiskt, nya domäner, lärsituationer)
- AI-assisterad code review och dokumentation

### 5.6 Yrkesmässighet och självledning
- Lärautonomi (kunna lära sig nytt utan kurs)
- Problemnedbrytning
- Nyfikenhet och kontinuerligt lärande
- Etik och ansvar (data, AI, säkerhet)

### 5.7 Tekniker (medel, inte mål)
Tracked men inte primärt drivande. Tekniker väljs för att tjäna 5.1–5.6.

- Språk: TypeScript primärt, Python sekundärt
- Frontend: React + Next.js (eller motiverat alternativ)
- Backend: Node.js (eller motiverat alternativ — t.ex. Python/FastAPI)
- Databas: PostgreSQL primärt
- Cloud: AWS eller Vercel
- DevOps: Docker, CI/CD via GitHub Actions

Tekniksiffror från första körningen (svenska annonser, icke-Java/.NET, n=119) stöder dessa val: TypeScript 41%, React 57%, Node.js 43%, PostgreSQL 16%, AWS 40%, CI/CD 40%.

---

## 6. Formativ bedömning som genomgående tråd

Genom hela programmet tillämpas **formativ bedömning** — löpande, lågsanktionerad återkoppling som stödjer lärandet snarare än bara graderar det. Det är en pedagogisk grundprincip, inte en valbar metod.

### Varför formativt

- Studenter får möjlighet att förbättra innan slutleverans → höjer examensgrad och leveranskvalitet
- Lärare upptäcker tidigt om en kohort kämpar med ett specifikt moment → pivot innan det är för sent
- Bygger den **självgranskningsförmåga** som är central för senior-trajectory (kopplar till 5.6 — yrkesmässighet och självledning, och 5.7 — kvalitetssäkringsverktyg i kursmål)
- Matchar evidens från cognitive load theory (Sweller) och deliberate practice — formativ återkoppling är vad som gör övning till lärande

### Mekanismer som tillämpas genom programmet

| Mekanism | Vad det är |
|---|---|
| **Code reviews** (lärare + peer) | Studenter får regelbunden återkoppling på kod under utveckling, inte bara vid slutleverans. Lär dessutom *att granska andras kod* — en av de viktigaste yrkesfärdigheterna. |
| **Worked examples + completion problems** | Inbäddade i undervisningen (se 5.1) — fungerar som formativ träning innan självständig övning |
| **Utkastfeedback** | Inlämningsuppgifter granskas innan slutbedömning, så studenten kan iterera baserat på återkoppling |
| **Lättviktiga checkar** | Korta, icke-graderade förståelse-quizar eller pulskoll för att se var en kohort står |
| **Reflexionsmoment** | Studenten redogör för egna val och resonemang — typiskt kopplat till kompetensmål om självledning |

### Förhållande till summativ bedömning

Formativ bedömning **ersätter inte** "Former för kunskapskontroll" i kursplanerna — den **kompletterar** dem. Summativ bedömning sätter slutbetyg; formativ stöttar resan dit.

I kursplanerna förekommer formativ bedömning *inte* explicit som examinationsmoment (eftersom den är icke-graderad), men den ska genomsyra arbetsformer i samtliga kurser. Den enda kursplan där code review explicit nämns som arbetssätt är **kurs 3** (kursmål 8 — "kodgranskning och refaktorering som arbetsmetoder"), där det också är en yrkesfärdighet att lära ut, inte enbart en pedagogisk metod.

---

## 7. Lärautonomi som genomgående pedagogisk princip

Datasignalen `self_learning` ligger på **91% i SE-niche-annonserna** — högst av alla signaler. För juniors anställningsbarhet och senior-trajectory är förmågan att *själv lära sig nytt* fundamentalt. I FJS26 är detta inte ett enskilt kursmål utan en **genomgående pedagogisk princip** som genomsyrar hur kurserna drivs.

### Vad det innebär konkret

- **Studenten möter nytt material först självständigt** (läsning, video, dokumentation) och sedan i workshop där lärare verifierar förståelse
- **Tekniska val i projekt får inte vara totalt anvisade** — studenten ska göra något val själv (vilket bibliotek, vilken metod) och kunna motivera det
- **Examensprojekt och LIA-uppgifter testar förmågan att möta okända teknologier** — studenten möter material som inte uttryckligen undervisats
- **Lärare modellerar self-learning** — visar hur man söker, läser dokumentation, prövar nytt, värderar källor

### Förhållande till andra principer

Lärautonomi är nära kopplat till:
- **Formativ bedömning** (§6) — feedback-loopen som möjliggör studentens egen utveckling
- **Yrkesmässighet och självledning** (§5.6) — där lärautonomi är listat som signal
- **AI-arbetsflöde** — AI som verktyg för egen utforskning, kompletterar inte bara ersätter studenten

### Riskhantering

Lärautonomi är **inte** att lämna studenten själv. Det är att:
- Tillhandahålla strukturerat material som studenten kan läsa självständigt
- Validera förståelse via worked examples, completion problems och code review
- Stötta när studenten kör fast — utan att lösa problemet åt hen

Studenter som upprepat har svårt att jobba självgående identifieras tidigt via formativ bedömning och får riktat stöd.

---

## 8. Taxonomi för LLM-extraktion (input till Sonnet-prompten)

LLM:n ska för varje annons returnera strukturerad data enligt taxonomin nedan. Detta gör att vi kan aggregera per *kompetensspår*, inte bara per verktyg.

```
{
  "seniority": "junior" | "mid" | "senior" | "unspecified",
  "stack_primary": "java_dotnet" | "javascript_node" | "python" | "other" | "mixed",
  "craft_signals": [
    "language_fluency", "html_semantics", "modern_css",
    "web_fundamentals", "debugging", "code_reading", "refactoring_craft"
  ],
  "architecture_signals": [
    "system_design", "api_design", "data_modeling",
    "distributed_systems", "security_arch", "observability",
    "performance_scaling", "cloud_native"
  ],
  "methodology_signals": [
    "agile_practice", "code_review", "testing_strategy",
    "tdd", "cicd_discipline", "trunk_based",
    "refactoring", "incident_response"
  ],
  "collaboration_signals": [
    "requirements_work", "stakeholder_comm", "estimation",
    "documentation", "cross_functional", "domain_understanding"
  ],
  "ai_workflow_signals": [
    "ai_tools_general", "prompt_engineering", "context_management",
    "ai_code_review", "agentic_workflows"
  ],
  "professional_signals": [
    "self_learning", "problem_decomposition",
    "ethics_responsibility"
  ],
  "tools": ["typescript", "react", ...],
  "is_actually_fullstack": true | false
}
```

LLM:n får också utdrag ur denna brief (avsnitt 5) som context i prompten, så att den vet att t.ex. "äger en feature end-to-end och driver tekniska beslut" ska markeras som `system_design`+`stakeholder_comm`+`requirements_work`, inte bara som "fullstack-arbete".

---

## 9. Risker och förbehåll

- **Annonser ljuger.** "Senior" i annonser betyder ofta "vi vill ha en junior-mid men törs inte säga det". Sonnet hjälper genom att läsa hela texten, men datat är aldrig perfekt.
- **AI-arbetsflöde är underrapporterat i annonser 2026.** Tekniken används överallt men nämns sällan explicit. Detta spår kommer behöva *kuraterat ramverk* utöver annonsdata.
- **Klassificeringen "junior" är osäker.** Mycket få annonser söker explicit juniorer. Vi får mest titta på senior-annonser och *läsa baklänges* vad en junior behöver kunna för att bli kallad.
- **60 v är tajt.** Vi kommer behöva välja bort. Dokumentet får inte landa i en lista på 80 lärandemål — det måste vara *prioriterat*.
- **JobTech har slagsida mot större företag/byråer** med inrapporteringsplikt. Startup-marknaden är underrepresenterad och täcks bättre av HN/RemoteOK-spåret.

---

## 10. Vad ledningsgruppen ska få beslutsunderlag för

Slutleveransen ska besvara minst dessa frågor:

1. **Vad är profileringen?** En mening som differentierar utbildningen mot Java/.NET-programmen.
2. **Vilka kompetensspår är obligatoriska?** Och varför, med datareferens.
3. **Hur fördelar vi 60 v?** Översiktlig kursstruktur med YH-poäng-fördelning.
4. **Hur säkerställer vi senior-trajectory?** Konkreta moment som tränar arkitekt­tänkande och självledning, inte bara verktyg.
5. **Hur hanteras AI-arbetsflödet?** Genomgripande tråd eller egen kurs?
6. **Vad är riskerna?** Och hur mitigeras de.
7. **Hur följer vi upp över tid?** Återkommande körning av denna analys för att fånga marknadsskifte.

---

## 11. Arbetsprocess härifrån

1. ✅ Datapipeline byggd: JobTech + RemoteOK + WWR + HN, 453 annonser totalt
2. ✅ Keyword-baseline kört, gav stack-signaler (TS+React+Node+PG+AWS)
3. ⏳ **Nästa: LLM-extraktion med Sonnet 4.6** mot taxonomin i avsnitt 8
4. Aggregering per kompetensspår (inte per verktyg)
5. Triangulering med Stack Overflow Developer Survey + GitHub/Vercel AI-rapporter
6. Kuraterat AI-arbetsflöde-ramverk (kan inte härledas från annonser)
7. Leveransdokument till ledningsgruppen (6–10 sidor) med kursstruktur
