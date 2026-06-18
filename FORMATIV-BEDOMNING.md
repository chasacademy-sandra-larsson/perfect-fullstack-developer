# Formativ bedömning i FJS26 — operationell handledning

> Detta dokument operationaliserar pedagogprincipen som dokumenteras i `UPPDRAG.md §6`.
> **UPPDRAG.md säger *varför*; detta dokument säger *hur*.**

---

## 1. Översikt

Formativ bedömning är **löpande, lågsanktionerad återkoppling** som stödjer lärandet snarare än bara graderar det. Den är distinkt från summativ bedömning (slutbetyg), men kan i specifika fall glida över i summativ form — t.ex. när code review körs vid slutleverans (se §5).

Code review är den centrala mekanismen, men inte den enda. Andra mekanismer dokumenteras i §4. Workshops är den primära arenan där formativ bedömning och annan pedagogik faktiskt sker — se §2.

---

## 2. Workshops som arbetsform

Workshops är den primära arbetsformen genom hela programmet — lärar-ledda eller lärar-närvarande tillfällen där studenten arbetar med uppgifter, code-alongs, completion problems och peer-aktiviteter. De fungerar som den arena där formativ bedömning och annan pedagogik (se §3–4) faktiskt sker.

### 2.1 Status: innehållet obligatoriskt, närvaron förväntad

Workshops är inte formellt obligatoriska närvaromässigt — i YH:s mening graderas inte närvaro. Däremot är **innehållet** del av kursen och förväntas läras. Studenten förväntas vara närvarande för att:

- Möta worked examples och code-alongs i nuet (CLT-pedagogiken)
- Få och ge formativ återkoppling (lärare + peer)
- Träna progressionen från noviskt till självständigt arbete (fading)
- Bygga den yrkesmässighet och självledningsförmåga som examineras i kompetensmål

Studenter som upprepat skippar workshops har **betydligt högre risk att inte klara examination**. Detta kommuniceras till studenten vid kursstart.

### 2.2 Vad som händer i workshops

- **Code-alongs** — lärare och student kodar parallellt med narration (worked examples i realtid)
- **Completion problems** — studenten kompletterar förberedda kodfragment
- **Self-directed work** — studenten arbetar med kursuppgifter, lärare finns för stöttning
- **Formativ code review** — lärare och peer granskar kod under utveckling (se §3)
- **Mini-presentationer** — student visar sitt arbete för gruppen

### 2.3 Förhållande till föreläsningar och projektarbete

| Form | Vad det är | Närvaro |
|---|---|---|
| **Föreläsning** | Lärare presenterar, student lyssnar | Förväntad |
| **Workshop** | Aktivt arbete med stöd | Förväntad (innehållet är del av kursen) |
| **Projektarbete** | Studentdrivet team-arbete | Examineras enligt kursplan |

### 2.4 Pedagogisk koppling

Workshops är den primära arenan för:

- **Worked examples → completion problems → fading** (se UPPDRAG.md §5.1)
- **Formativ code review** (se §3)
- **Andra formativa mekanismer** (se §4)

Utan workshops fungerar inte pedagogiken som programmet vilar på. Det är därför *"innehållet är obligatoriskt"* — det går inte att klara kurserna utan att möta innehållet, och workshops är den primära platsen där det möts.

---

## 3. Code review — operationell beskrivning

### 3.1 Frekvens och eskalering över programmet

| Kurs | Frekvens (minst) | Typ |
|---|---|---|
| Kurs 2 — Frontendutveckling | 2 per större inlämning | Lärare → student (formativ) |
| Kurs 3 — Avancerad frontend + TS | 3 per projekt + 1 per inlämningsuppgift | Lärare + peer + studenten lär sig granska (formativ + summativ vid slut) |
| **Kurs 4 och framåt** | **Som etablerad praxis** — frekvens bestäms av kursens innehåll | Peer-driven med lärare som mentor, yrkeslikt PR-flöde |
| LIA | Verkligheten | Real-world företagspraxis |

> **Från och med kurs 4 är code review självklar formativ praxis** och behöver *inte* återintroduceras i varje kursplan. Kursplaner från kurs 4 och framåt nämner code review *endast* när det förekommer som summativt examinationsmoment (t.ex. *bedömd kodgranskning*). Annars är det implicit täckt av detta dokument och UPPDRAG.md §6.

### 3.2 Stages

| Stage | Timing | Fokus | Roll |
|---|---|---|---|
| **Utkast-review** | Tidigt i en uppgift | Struktur, namnval, läsbarhet — innan koden polerats | Formativ — bygg upp |
| **Mid-stage check** | Halvvägs | Progress, blockerare, arkitektur­val | Formativ — kursjustera |
| **Slutfeedback** | Före inlämning | Polish, edge cases, dokumentation | Formativ — finputs |
| **Bedömd kodgranskning** | Vid slutleverans (kurs 3+) | Vilka val gjordes och varför, samt kvalitet | **Summativ — bidrar till betyg** |

### 3.3 Format

- **Skriftlig** (Canvas annotations eller GitHub PR-kommentarer)
- **Inline-kommentarer** + en kort sammanfattande feedback per session
- 5–10 substantiella punkter per review är riktnivå — räcker för att vara meningsfullt, inte så mycket att studenten överväldigas

### 3.4 Rubrik — vad reviewer tittar på

| Område | Vad bedöms |
|---|---|
| **Correctness** | Gör koden vad den ska? Hanteras kantfall? |
| **Readability** | Kan jag förstå koden om 6 månader? Namnval, struktur, kommentarer där relevant. |
| **Structure** | Modul-uppdelning, separation of concerns, loose coupling |
| **Idioms** | Skrivs koden idiomatiskt i språket/ramverket? |
| **Tests** *(där tillämpligt)* | Finns tester? Täcker de relevant beteende? |
| **Security** *(där tillämpligt)* | T.ex. inga secrets i klient-kod, säker hantering av användardata |

### 3.5 Stöttning vs check — två olika syften

- **Stöttning** = lärare eller peer hjälper studenten förstå *varför* något kan förbättras. Didaktisk ton, förklaringar, alternativ. Vanligast i utkast-review.
- **Check** = lärare verifierar status. *"Du är på rätt spår, fortsätt."* Eller: *"Här behöver vi prata innan du går vidare."* Vanligast i mid-stage.

Båda är formativa. Stöttning bygger förståelse, check styr riktning.

### 3.6 Vem reviewar (per kurs)

| Kurs | Lärare | Peer | Studenten lär sig granska |
|---|:---:|:---:|:---:|
| Kurs 2 | ✅ Primärt | — | — |
| Kurs 3 | ✅ Vid utkast + slutbedömning | ✅ Under projekt | ✅ Som kompetens (kursmål 9) |
| Kurs 4+ | Som mentor | ✅ Primärt | ✅ |

---

## 4. Andra formativa mekanismer

### 4.1 Utkastfeedback (text-baserad)

Skriftliga inlämningar (rapporter, projektdokumentation) granskas i utkastform innan slutbedömning. Studenten kan iterera baserat på återkoppling.

### 4.2 Completion problems

Inbäddade i undervisningen (se UPPDRAG.md §5.1). Studenten gör en delvis ifylld kodövning och får direkt återkoppling — fungerar som *mikro-formativ bedömning* i nuet.

### 4.3 Reflexionsmoment

Studenten redogör för egna val i kursarbete. Vanligast kopplat till kompetensmål om självledning. T.ex. den individuella inlämningsuppgiften i kurs 3 (mot kompetensmål 8) är en reflexionsuppgift med summativ kant.

### 4.4 Lättviktiga checkar och quizar

Korta, icke-graderade förståelse­quizar i undervisningen för att se var en kohort står. **Resultat används aldrig för bedömning av enskild student** — endast för lärarens pulskoll.

---

## 5. Gränser mot summativ bedömning

### Vad som ÄR OK

- Formativ feedback är **fri zon** — varken graderad eller betygsatt
- Lärare kan dokumentera att studenten *har svarat* på formativ feedback (utveckling över tid). Detta kan beaktas vid slutbedömning av relaterat kursmål.
- Code review **kan bli summativ** när den körs vid slutleverans (kurs 3+). Då dokumenteras det som examinationsform i kursplanen — t.ex. *"Bedömd kodgranskning av kursmål 9 (vid slutleverans)"*.
- Samma kursmål kan examineras i flera moment — formativt under resan, summativt vid slutet.

### Vad som INTE är OK

- Formativ feedback får aldrig **smyga in betyg**. Om utkastfeedback börjar säga *"detta är VG-värdig kod"* är vi de facto i summativ-zon. Det undergräver tilliten.
- En icke-graderad quiz får aldrig **påverka enskild students bedömning**.
- Code review-anteckningar får aldrig användas **mot** studenten — bara *för* hens utveckling. Om studenten själv ber om att tidigare feedback ska räknas in i slutbedömning är det dock OK.

---

## 6. Dokumentationspraxis

### 6.1 Var feedback bor

- **Canvas annotations** för inlämningar
- **GitHub PR-kommentarer** för projektkod
- Inte spridda i e-post, chatt eller muntligt utan spår — annars går återkopplingen förlorad

### 6.2 Lärarens egen spårning

Lärare för **interna anteckningar** om varje students utveckling under kursens gång. Detta är lärarverktyg, inte studentens dokument. Syftet: ge meningsfull slutbedömning baserad på utveckling och slutprodukt, inte bara slutprodukt.

### 6.3 Vad som BÖR antecknas

- Återkommande mönster (samma fel på tre olika uppgifter)
- Genombrott (student som löst ett tidigare blockerande problem)
- Övergripande utvecklingstendens

### 6.4 Vad som INTE bör antecknas

- Värdeomdömen om personen ("ovillig att lyssna", "lat") — irrelevanta för pedagogik
- Privatpersonliga omständigheter — saknar didaktisk relevans
- Spekulationer om framtida prestanda — orättvist mot studenten

---

## 7. Bedömd kodgranskning — när formativ blir summativ

I kurs 3 och framåt finns *bedömd kodgranskning* som **summativ examinationsform vid slutleverans**. Den följer denna struktur:

1. **Studenten lämnar in slutgiltig kod** för projekt/uppgift
2. **Lärare genomför kodgranskning enligt rubriken i §3.4**
3. **Granskningen dokumenteras** i Canvas eller GitHub PR med inline-kommentarer och sammanfattande omdöme
4. **Bedömning ges** mot relevanta kursmål — typiskt kursmål om kvalitetssäkring, felsökning eller projektarkitektur
5. **Studenten har rätt till omexamination** enligt vanlig YH-praxis

Skillnaden mot formativ code review är att slutbedömningen *räknas* — den bidrar till slutbetyg. Studenten har inte längre möjlighet att iterera baserat på denna feedback (utöver vid omexamination).

---

## 8. Sammanfattning för lärare

- **Workshops är arbetsformen.** Innehållet är del av kursen — närvaro förväntas.
- **Code review är inte valbart.** Det är program-praxis från kurs 2.
- **Code review är *både* metod och färdighet.** Studenten både *får* och *lär sig att ge*.
- **Formativ är fri zon.** Kommentera ärligt utan att gradera.
- **Summativ code review (kurs 3+) finns dokumenterat i kursplanen.** Det är det enda code review-momentet som påverkar betyg.
- **Spåra utveckling.** Anteckna mönster och genombrott — inte personlighetsdrag.
- **Använd rubriken.** Correctness, readability, structure, idioms, tests, security — i den ordningen.
