# LG-diskussion — kurs 8: Avancerad fullstackutveckling, Cloud och DevOps

> **Syfte:** beslutsunderlag inför ledningsgruppens diskussion om kurs 8 i FJS26.
> **Status:** Kursplanen är skapad (`kursplaner-fjs26/8. Avancerad fullstackutveckling, Cloud och DevOps.md`) i en första version. Detta dokument samlar **öppna frågor och datasignaler** som ledningsgruppen bör ta ställning till.

---

## Sammanfattning av kursen idag

**Namn:** Avancerad fullstackutveckling, Cloud och DevOps
**Omfattning:** 65 YHp / 13 v
**Placering:** HT2 (efter kurs 7 AI inom fullstackutveckling)
**Antal kursmål:** 16 (8 kunskap + 6 färdighet + 2 kompetens)

### Vad kursen är en sammanslagning av

| FJS25-kurs | YHp | Status |
|---|---|---|
| Kurs 8 (Cloud, CI/CD och arbetsmetodik) | 20 | Sammanslagen till FJS26 kurs 8 |
| Kurs 9 (Avancerad fullstackutveckling) | 50 | Sammanslagen till FJS26 kurs 8 |
| **FJS25 totalt** | **70** | → **FJS26 kurs 8 = 65 YHp** |

(Reduceringen på 5 YHp beror på att innehåll som redan täckts i tidigare kurser tagits bort.)

### Vad som tagits bort (redan täckt i tidigare kurser)

| Innehåll | Var det redan finns |
|---|---|
| NoSQL-databaser | Kurs 4 |
| Docker / containerisering | Kurs 4 |
| TypeScript som fullstack-språk | Kurs 3, 4 |
| OWASP säkerhet | Kurs 4 |
| Datalagring (SQL/NoSQL implementation) | Kurs 4 |
| Testning / teststrategier | Kurs 6 |
| AI-verktyg generellt | Kurs 7 + tråd genom hela programmet |

### Vad kursen täcker — kärnan

- Cloud hosting (AWS, Azure, GCP eller motsvarande) + serverless
- CI/CD pipelines och DevOps-metoder
- Avancerad Git
- GraphQL
- Valbart JavaScript-ramverk (Vue, Svelte, Angular — utöver React i kurs 4)
- Routing, state management, rendering, prestanda och skalbarhet i valt ramverk
- Headless CMS

---

## Öppna frågor till ledningsgruppen

### Fråga 1: Observability — ska den med explicit?

**Datasignal:** `observability` ligger på **44%** i svensk niche-marknad (monitorering, loggning, tracing).

**Status:** Saknas i kursplanen just nu. Är **dokumenterad i memory** (`project_deferred-from-kurs4.md`) som något som "ska in i kurs 8" — men har inte landat i kursmålen.

**Pedagogisk fråga:** Är observability en distinkt kompetens som kräver eget mål, eller är den implicit i CI/CD och DevOps?

**Två förslag:**
- **A. Integrera i befintligt kursmål 2 (CI/CD + DevOps)** — utvidga med "observability (monitorering, loggning, tracing)"
- **B. Lägg till som eget kursmål** + matchande färdighet (totalt 18 mål istället för 16)

**LG-perspektiv:** Marknadssignalen är stark (44%). Risk att försumma — junior-utvecklare som inte vet vad observability är blir snabbt off-balance i drift­situationer.

---

### Fråga 2: Backend-prestanda och caching

**Datasignal:** `performance_scaling` ligger på **59%** i svensk niche-marknad — bred signal som täcker frontend OCH backend OCH skalning.

**Status:** Kursmål 7 är *frontend-fokuserat* ("rendering, prestanda och skalbarhet inom valt ramverk"). Backend-aspekter (database query optimization, caching, connection pooling) är *inte* explicit.

**Vad som finns implicit:** Cloud + serverless (kursmål 1) ger viss skalning, men inte caching eller query-optimering.

**Pedagogisk fråga:** Räcker frontend-prestanda för junior-nivå, eller behöver vi backend-prestanda också?

**Två förslag:**
- **A. Behåll som det är** — frontend-prestanda räcker; backend-performance lärs ut i jobb
- **B. Utvidga kursmål 1 eller lägg till nytt mål** för backend-prestanda (caching, index-strategier, query-optimering)

**LG-perspektiv:** En *avancerad fullstack-kurs* utan backend-prestanda är pedagogiskt ofullständigt. Men det är också svårt material för junior.

---

### Fråga 3: Avancerad infrastruktur (Kubernetes, IaC)

**Datasignaler:**
- `kubernetes`: 17% i SE-niche
- `terraform` / IaC: 16% i SE-niche

**Status:** Inte explicit i kursen. Eventuellt för avancerat för en HT2-junior?

**LG-perspektiv:** Det här är *senior-territory* — troligen rimligt att skjuta till LIA / yrkeslivet. Men värt att åtminstone *nämna* så studenten är medveten om att det finns.

---

### Fråga 4: Distribuerade system

**Datasignal:** `distributed_systems` ligger på **48%** i SE-niche.

**Status:** Delvis täckt av cloud + serverless (kursmål 1), men inte explicit.

**Pedagogisk fråga:** Bör konceptet *distribuerade system* (event-driven, queues, eventual consistency) finnas explicit som kunskap?

**LG-perspektiv:** 48% är högt. Men distribuerade system är konceptuellt tungt för junior — kanske bättre som introduktion än djup?

---

### Fråga 5: Valbar JS-ramverk vs React-fördjupning

**Nuvarande val:** Studenten lär sig ett *annat* JS-ramverk än React (Vue, Svelte eller Angular).

**Datasignaler i SE-niche:**
- React: 65% (primärt — täcks i kurs 4)
- Angular: 13%
- Vue: 11.6%
- Svelte: 1.4%

**Pedagogiskt argument:** Att möta ett *annat* ramverk visar studenten att ramverksmönster generaliserar — bygger transfer learning och senior-trajectory.

**Marknadsargument:** Studenten kan möta Angular eller Vue på riktiga arbetsplatser. Att bara kunna React begränsar.

**Alternativ för LG-diskussion:** Vill ni:
- **A. Behålla "valbart ramverk"** (nuvarande) — transfer learning prioriteras
- **B. Skifta till "fördjupad React"** — mer marknads-fokuserat (React har 65% av annonserna)

---

## Bestämt / inte under omprövning

- Kursnamn: "Avancerad fullstackutveckling, Cloud och DevOps"
- Omfattning: 65 YHp / 13 v (HT2)
- Borttaget innehåll (NoSQL, Docker, testning, OWASP, TS, generell AI) — repeteras inte
- Kursen ligger efter kurs 7 AI i HT2
- Examinations­struktur: skriftlig inlämning (kunskaper), laborationer (cloud/CI/DevOps), projekt med muntlig presentation (GraphQL, JS-ramverk, headless CMS, kompetenser)
- VG-kriterier: kursmål 15 + 16 (argumentera + motivera lösningar)

---

## Förslag till LG-beslut

1. **Observability** — A (integrera) eller B (eget mål)?
2. **Backend-prestanda** — A (behåll som är) eller B (utvidga)?
3. **Infrastruktur (Kubernetes/Terraform)** — nämna kort eller helt utelämna?
4. **Distribuerade system** — explicit kursmål eller implicit?
5. **JS-ramverk** — valbart (nuvarande) eller fördjupad React?

---

## Datasignaler för referens

Från `output/report.md` — SE-niche (n=69, icke-Java/.NET fullstack-annonser):

| Signal | % | Status i kurs 8 |
|---|:---:|---|
| `cloud_native` | 78% | ✅ Kursmål 1 |
| `cicd_discipline` | 73% | ✅ Kursmål 2 |
| `api_design` | 65% | (täckt i kurs 4 + GraphQL i kursmål 4 här) |
| `performance_scaling` | 59% | ⚠️ Frontend ja, backend nej |
| `system_design` | 48% | (täckt i kurs 4) |
| `distributed_systems` | 48% | ⚠️ Delvis (serverless) |
| `testing_strategy` | 46% | (täckt i kurs 6) |
| `observability` | **44%** | ❌ Saknas — diskussionspunkt |
| `security_arch` | 39% | (täckt i kurs 4) |
| AWS | 42% | ✅ Implicit i kursmål 1 |
| Docker | 33% | (täckt i kurs 4) |
| Kubernetes | 17% | ❌ Inte explicit — diskussionspunkt |
| Terraform | 16% | ❌ Inte explicit — diskussionspunkt |

---

## Datadriven gap-analys mot anställningssignaler

> **Frågeställning:** Vad i perfect-fullstack-datan finns *inte* i nuvarande FJS26 — och var ligger störst risk att studenten missar inträdesbarriärerna för junior-anställning?

### Hårda gap — inträdesbarriärer ≥40% som ej är explicit täckta

Dessa är annonsfrekvens-prioriterade och påverkar direkt sannolikheten att studenten klarar intervjuer och får LIA-platser:

| Signal | % SE niche | Status nu | Konsekvens om vi inte täcker |
|---|:---:|---|---|
| **observability** | 44 | ❌ Saknas helt | Studenten kan inte felsöka i drift, vet inte vad logs/metrics/tracing är — direkt rödflagg i intervju |
| **distributed_systems** | 48 | ⚠️ Endast implicit via serverless | Studenten saknar mental modell för queues, event-driven, eventual consistency |
| **performance_scaling** (backend) | 59 | ⚠️ Bara frontend täckt | Studenten saknar caching, query-optimering, indexstrategi — vanlig junior-fråga |

**Total signalmassa som annars är gap:** ~151 procentenheter över 3 inträdesbarriärer.

### Mjuka gap — differentierare bara implicit täckta

Dessa är edge mot andra juniorer men inte avgörande. De är "trevliga att stärka" snarare än anställningskritiska:

| Signal | % SE niche | Status nu |
|---|:---:|---|
| problem_decomposition | 78 | Implicit i projektarbete — inget eget mål |
| debugging | 22 | Implicit — inget eget mål |
| refactoring_craft | 22 | Implicit — inget eget mål |
| documentation | 19 | Implicit — inget eget mål |
| Kubernetes | 17 | ❌ Ej med — diskussionspunkt 3 ovan |
| Terraform | 16 | ❌ Ej med — diskussionspunkt 3 ovan |

### Rekommendation från datan

De tre hårda gapen ligger **alla naturligt i kurs 8** och motsvarar uppskattningsvis 1–2 v innehåll = 5–10 YHp. Detta sammanfaller med de 10 YHp som idag fattas mellan FJS26 (420 YHp) och FJS25 (430 YHp).

**Datadrivet förslag på allokering:**

- **Alt A (datadriven, max anställnings-ROI):** Allt 10 YHp till kurs 8 — 65 → 75 YHp / 13 v → 15 v. LIA kvar på 110 YHp. Adresserar samtliga tre hårda gap.
- **Alt B (kompromiss):** 5 YHp till kurs 8 (70 YHp, observability + 1 av övriga) + 5 YHp till LIA (115 YHp).
- **Alt C (LIA-tung):** Allt 10 YHp till LIA (120 YHp). Hårda gap förblir täckta endast inom befintliga 65 YHp.

Marknadssignalerna stödjer **Alt A** för anställningschans. **Alt B** balanserar mot LG-mötets tidigare intention att kunna utöka LIA med 1–2 v.
