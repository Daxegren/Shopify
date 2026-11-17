# Granskning av pilottexter v2: oberoende Opus-granskning 3 (2026-11-17)

**Granskat:** `pilot_texter_v2.py` (tio kategorier: brödtext, SEO-titel och meta) mot `underlag/<handle>.json` (omkört 2026-11-17).
**Regler:** `shopify-sync/docs/kategoritexter-standard.md` (avsnitt 2, 3, 4 och 8) och de fem senaste posterna i `LARDOMAR.md`.
**Metod:** jag har kontrollerat varje påstående själv mot `alla_titlar`, `ovriga_titlar` och `marken`. Jag räknade med python3 (`-I`, absoluta sökvägar) och läste titellistorna rad för rad. Kontrollskriptet har inte använts. Inget har skrivits till Shopify och inga nätverksanrop har gjorts.

**Begrepp:**
- **FAKTAFEL** = ett påstående som inte stämmer med underlaget. Det gäller också när en köpbar produkt i kollektionen (även bland `ovriga_titlar`) gör påståendet osant för den som tittar på sidan.
- **ANMÄRKNING** = stil eller precision. Valfritt att rätta.

## Kontroller som gäller alla tio texter (godkända)

| Kontroll | Resultat |
|---|---|
| Längd brödtext 60–200 ord | 64–89 ord, alla godkända |
| SEO-titel högst 43 tecken | 27–43 tecken, alla godkända (crosstrainer exakt 43) |
| Meta 120–155 tecken (standarden) | 137–146 tecken, alla godkända |
| Första meningen har verb | "säljer" i alla brödtexter och "Köp" i alla metatexter |
| Prisuppgifter | Inga belopp eller prisspann. Bara hänvisningsmeningen "se pris" |
| Leverantörsnamn som märken (Velomarket, Gorilla Sports Norden) | Nämns inte |
| Löften, superlativ, frakt och ursprung | Inga hittade ("flest" är en räknad jämförelse) |
| "produkter" i stället för "modeller" | Används överallt |
| Exempeltitlar ordagrant i `alla_titlar` | Alla 30 finns ordagrant |
| SEO-titlar unika sinsemellan | Ja |

---

## 1. motionscykel (godkänd)

| Påstående | Underlag | Utfall |
|---|---|---|
| motionscyklar, spinningcyklar och hopfällbara motionscyklar | Typorden motionscykel 56, spinningcykel 24, hopfällbar 4 | godkänd |
| Märkena Tunturi, BH Fitness, Toorx, Hammer och Christopeit | marken: 28/20/17/11/9 | godkänd |
| minst 80 produkter | 87 (84 unika titlar); golvat till tiotal = 80 | godkänd |
| Tunturi och BH Fitness har flest | 28 och 20 (titlar 28 och 22). Toorx 17 (19 med två TOORX BRX R300 bland övriga) | godkänd |
| minst 20 spinningcyklar | 24 titlar börjar med "Spinningcykel"; golvat till femtal = 20 | godkänd |
| svänghjul, ryggstöd, motståndsnivåer i namnet | t.ex. "med 11 kg Svänghjul", "med Ryggstöd", "med 32 Motståndsnivåer" | godkänd |
| 3 exempel | alla ordagrant | godkänd |

ANMÄRKNING (valfri): "hopfällbara motionscyklar från bland annat Tunturi …". Tunturi har ingen hopfällbar motionscykel bland huvudprodukterna (de hopfällbara är från BH Fitness, Christopeit och Toorx). Meningen är allmän och inte fel, men den kan läsas som att Tunturi har en sådan.

## 2. lopband (godkänd)

| Påstående | Underlag | Utfall |
|---|---|---|
| Märkena Tunturi, BH Fitness, Christopeit, Hammer och Toorx | marken 15/14/9/6/5 | godkänd |
| minst 50 | 52, golvat till 50 | godkänd |
| Tunturi och BH Fitness har flest | 15 och 14 (titlar 15 och 14) | godkänd |
| Flera löpband är hopfällbara | 6 med "Hopfällbart" (+1 "Infällbart") | godkänd |
| skärm eller träningsprogram i namnet | "5-tums Skärm", "10-tums Skärm", "44 Träningsprogram", "47 Träningsprogram" | godkänd |
| Meta: Hopfällbara löpband finns | se ovan | godkänd |
| 3 exempel | ordagrant | godkänd |

## 3. roddmaskin (1 faktafel)

| Påstående | Underlag | Utfall |
|---|---|---|
| Märkena Tunturi, Hammer, Christopeit och BH Fitness | marken 9/5/5/3 | godkänd |
| minst 20 | 22 (21 unika), golvat till 20 | godkänd |
| Tunturi har flest, tre i serien Cardio Fit | Tunturi 9; Cardio Fit R20, R25, R30 = 3 | godkänd |
| **Hammer och Christopeit har fem produkter vardera** | Bland huvudprodukterna 5 och 5. Bland `ovriga_titlar` finns dock fler köpbara roddmaskiner av samma märken: "Rodd-ergometer CHRISTOPEIT Cambridge II Black Edition", "Rowing ergometer CHRISTOPEIT Vico", "Rowing machine CHRISTOPEIT Colorado" (Christopeit totalt **8**), "Rowing ergometer HAMMER AquaFold" (Hammer **6**, plus "Rodd-ergometer Finnlo by Hammer Aquon Evolution") | **FAKTAFEL** |
| 3 exempel | ordagrant | godkänd |

**FAKTAFEL R1.** Det exakta talet "fem" stämmer inte med vad kunden ser i kollektionen: Christopeit har 8 köpbara roddmaskiner och Hammer 6. Talet bryter också mot standarden, där antal ska anges som "minst N" (avsnitt 2).
- Före: `Tunturi har flest produkter, bland annat tre i serien Cardio Fit, och Hammer och Christopeit har fem produkter vardera.`
- Efter: `Tunturi har flest produkter, bland annat tre i serien Cardio Fit, och Hammer och Christopeit har minst fem produkter vardera.`
- Underlag: `ovriga_titlar` i `underlag/roddmaskin.json` (se titlarna ovan). Ordantalet efter rättelsen är 65.

Påståendet "Tunturi har flest" håller också med övriga inräknade (9 mot 8).

ANMÄRKNING: underlaget räknar inte titlar som börjar med "Rodd-ergometer", "Rowing ergometer" eller "Rowing machine" som huvudprodukter. Huvud-regexen bör utökas inför nästa körning (jfr LARDOMAR 2026-11-12 om engelska titlar).

## 4. crosstrainer (godkänd)

| Påstående | Underlag | Utfall |
|---|---|---|
| Märkena Christopeit, Hammer, Tunturi, BH Fitness och Gymstick | marken 8/6/6/3/1 (Gymstick = "GX3.0 Crosstrainer", den enda titeln utan annat märke) | godkänd |
| minst 20 | 24, golvat till 20 | godkänd |
| Christopeit har flest | 8 (titlar 8). Med två hybridtränare från Christopeit bland övriga: 10 | godkänd |
| En produkt anger 8 nivåer och manuell broms | "Crosstrainer Tunturi Cardio Fit C30, 8 Nivåer, Manuell Broms" (en enda) | godkänd |
| Christopeit CT 6 kombinerad crosstrainer och motionscykel | "Crosstrainer och Motionscykel Christopeit CT 6" | godkänd |
| 3 exempel | ordagrant | godkänd |

ANMÄRKNING: "Gymstick" står inte i någon produkttitel ("GX3.0 Crosstrainer"). Det är tillåtet enligt vendor-fältet, men R8 (stavning som i titlarna) går inte att kontrollera för märket.

## 5. hantlar (1 faktafel)

| Påstående | Underlag | Utfall |
|---|---|---|
| hantlar, hantelset och justerbara hantlar | Typorden hantel 18, hantelset 11, justerbar 8 | godkänd |
| Märkena Tunturi, Gymstick, Toorx, Hammer och Christopeit | marken 26/10/7/5/2 (Gorilla Sports Norden nämns inte) | godkänd |
| minst 50 | 53 (52 unika), golvat till 50 | godkänd |
| Vikterna börjar vid 0,5 kg | "Pro Chrome Hantel 0,5kg - enkel" är lägsta vikten. Inget lägre bland övriga | godkänd |
| hantelset på bland annat 15 och 20 kg | "Hantelset Gymstick Vinyl, 15 kg", "Hantelset Tunturi Vinyl, 15 kg", "Hantelset Toorx Gjutjärn, 20 kg", "Hantelset Tunturi, 20 kg" | godkänd |
| hantelset på … 50 kg | Den enda 50 kg-produkten är "Hantel- och Skivstångsset Tunturi Vinyl 50 kg", alltså ett set men ett kombinerat hantel- och skivstångsset. Rena hantelset går upp till 28 kg ("Hantelset Tunturi Vinyl, 28 kg") | godkänd med anmärkning (se A-H1) |
| Material gjutjärn, vinyl, neopren och gummi | "Gjutjärn", "Vinyl", "Neopren", "Gummibelagd/gummerad/Rubber" | godkänd |
| Tunturi har flest | 26 | godkänd |
| 3 exempel | ordagrant | godkänd |
| **Meta: "hantelset upp till 50 kg"** | Bland `ovriga_titlar` finns en köpbar produkt "Skivstångs- och Hantelset Gymstick, Vinyl, 60 kg" (pris finns i `ovriga_med_pris`), alltså samma slags kombinerade set som 50 kg-produkten men tyngre. Räknas bara rena hantelset är maxvikten 28 kg. Med båda definitionerna stämmer "upp till 50 kg" inte | **FAKTAFEL** |

**FAKTAFEL H1 (meta).**
- Före: `Köp hantlar, hantelset och justerbara hantlar från bland annat Tunturi, Gymstick, Toorx och Hammer. Vikter från 0,5 kg, hantelset upp till 50 kg.`
- Efter: `Köp hantlar, hantelset och justerbara hantlar från bland annat Tunturi, Gymstick, Toorx och Hammer. Vikter från 0,5 kg. Minst 50 produkter.` (139 tecken)
- Underlag: `ovriga_titlar` i `underlag/hantlar.json`: "Skivstångs- och Hantelset Gymstick, Vinyl, 60 kg". `alla_titlar`: det tyngsta rena hantelsetet är "Hantelset Tunturi Vinyl, 28 kg".

**ANMÄRKNING A-H1 (brödtext, rekommenderas).** "hantelset finns på bland annat 15, 20 och 50 kg". 50 kg-produkten är ett set, men ett kombinerat hantel- och skivstångsset, och 50 kg är totalvikten med stång. Butikens egen titel "… 2-i-1 Hantelset 15kg" använder "hantelset" lika brett, så påståendet är inte direkt fel. Det kan ändå ge intrycket av ett rent hantelset på 50 kg. Förslag:
- Före: `Vikterna i produktnamnen börjar vid 0,5 kg, och hantelset finns på bland annat 15, 20 och 50 kg.`
- Efter: `Vikterna i produktnamnen börjar vid 0,5 kg. Hantelset finns på bland annat 15, 20 och 28 kg, och kombinerade hantel- och skivstångsset på bland annat 20 och 50 kg.` (stöd: "Hantelset Tunturi Vinyl, 28 kg"; "Hantel- och Skivstångsset Christopeit 4-i-1, 20 kg"; "Hantel- och Skivstångsset Tunturi Vinyl 50 kg"). Brödtexten får då 96 ord.

ANMÄRKNING (underlag): bland huvudprodukterna räknas "Hantelset Tunturi Centuri Neopren med Ställ" (set med ställ, godtagbart). Hantelställ och hantelstänger ligger korrekt bland övriga. Engelska titlar ("Active 10kg Vinyl Dumbbell Set", "Adjustable Dumbbell Set 15kg") räknas nu som huvudprodukter. Det är rätt.

## 6. kettlebell (godkänd)

| Påstående | Underlag | Utfall |
|---|---|---|
| Märkena Tunturi, Toorx, Hammer, Gymstick och Christopeit | marken 11/11/5/5/3 | godkänd |
| minst 30 | 35, golvat till 30 (34 utan "Kettlebellhandtag", fortfarande minst 30) | godkänd |
| Vikter 2–24 kg | Lägst "Kettlebell Christopeit, 2 kg" och "Kettlebell Tunturi PE, 2 kg"; högst "Kettlebell Hammer Premium, 24 kg" och "Kettlebell Tunturi, 24 kg". Övriga (12 kg) ligger inom spannet | godkänd |
| gjutjärn, vinyl, gummibotten | "gjutjärn", "Vinyl", "Gjutjärn med Gummibotten" | godkänd |
| Tunturi och Toorx har flest | 11 och 11 (titlar 11 och 11) | godkänd |
| 3 exempel | ordagrant | godkänd |

## 7. cykellas (godkänd)

| Påstående | Underlag | Utfall |
|---|---|---|
| vajerlås, kedjelås, vikbara lås, U-lås och kabellås | Typorden 17/16/8/7/3 | godkänd |
| Märkena AXA, Squire och Giant | marken 41/16/5 (stavning som i titlarna: "AXA", "Squire") | godkänd |
| minst 60 | 63 unika, golvat till 60 | godkänd |
| AXA och Squire har flest | 41 och 16 | godkänd |
| nyckel eller kod i namnet; några vikbara | t.ex. "Nyckel", "med Kod", "Vikbart Lås …" | godkänd |
| 3 exempel | ordagrant | godkänd |

ANMÄRKNING (stil): metan har två "bland annat" i samma mening ("Köp cykellås, bland annat vajerlås … från bland annat AXA …"). Den är korrekt men tung. Förslag: `Köp cykellås från bland annat AXA, Squire och Giant, till exempel vajerlås, kedjelås, vikbara lås, U-lås och kabellås. Minst 60 produkter.` (136 tecken).
ANMÄRKNING (underlag): "Köp AXA Fold Lite 80" bland övriga är ett lås med felaktig titel (börjar med "Köp"). Det påverkar inga påståenden.

## 8. elcyklar (godkänd)

| Påstående | Underlag | Utfall |
|---|---|---|
| Märkena Tenways, ADO, Giant, Fiido och Engwe | marken TENWAYS 25, ADO 17, Giant 11, Fiido 6, Engwe 3. Texten stavar "Tenways" som i 24 av 25 titlar (R8) | godkänd |
| minst 70 | 78, golvat till 70 (färgvarianter räknas, därför "produkter") | godkänd |
| Tenways och ADO har flest | 25 och 17 (titlar 25 och 18) | godkänd |
| minst 10 hopfällbara elcyklar | 13, golvat till femtal = 10 | godkänd |
| minst 10 el-lastcyklar | 12, golvat till 10 | godkänd |
| 3 exempel | ordagrant | godkänd |

ANMÄRKNING (precision): "elcyklar, hopfällbara elcyklar och el-lastcyklar från bland annat Tenways, ADO, Giant, Fiido och Engwe". Giant och Engwe har varken hopfällbara elcyklar eller el-lastcyklar. Hopfällbara finns från ADO, Fiido, Coast, Italwin och Romet; el-lastcyklar från bland annat Cargobike of Sweden, Fiido och Tenways. Meningen är inte fel som helhet, men märket med flest el-lastcyklar (Cargobike of Sweden, 3) nämns inte medan Engwe (3) gör det. Valfritt: byt Engwe mot Cargobike of Sweden.

## 9. tunturi (godkänd)

| Påstående | Underlag | Utfall |
|---|---|---|
| motionscyklar, löpband, roddmaskiner, träningsbänkar, hantelset, viktskivor, kettlebells, yogamattor | Första ord: motionscykel 22, löpband 12, roddmaskin 9, träningsbänk 17, hantelset 11, viktskiva 11 (+viktskivor 9), kettlebell 10, yogamatta 10 | godkänd |
| minst 300 | 381 (379 unika), golvat till hundratal = 300 | godkänd |
| minicyklar och massagerullar | minicykel 11, massagerulle 8 | godkänd |
| konditionsmaskiner och tillbehör för styrketräning och yoga | se typerna ovan | godkänd |
| 3 exempel | ordagrant | godkänd |
| Meta: "hantlar" | hantlar 11, hantel 7 | godkänd |

ANMÄRKNING: underlaget saknar huvud-regex, så alla 381 räknas, bland dem akupressurmattor och vibrationsplattor (kategorier "utanför tills vidare"). Texten nämner dem inte, och talet håller ändå.

## 10. sparkcykel (godkänd)

| Påstående | Underlag | Utfall |
|---|---|---|
| Märkena SOKE, Union, Rideoo, Versatyl och Ethic | marken 30/22/10/8/5 (titlar 30/22/10/8/6) | godkänd |
| minst 80 | 87 unika, golvat till 80 | godkänd |
| bland annat stuntsparkcyklar och tricksparkcyklar | stuntsparkcykel 34, tricksparkcykel 16 | godkänd |
| SOKE och Union har flest | 30 och 22 | godkänd |
| Delar som hjul och griptape finns som separata produkter | Bland övriga (köpbara): många "Sparkcykelhjul …", "Griptape …" | godkänd |
| 3 exempel | ordagrant | godkänd |

Rideoo kopplas inte längre till stuntsparkcyklar (felet från 2026-11-05 är borta).

---

## Sammanställning

| Kategori | Utfall | Faktafel | Anmärkningar |
|---|---|---|---|
| motionscykel | godkänd | 0 | 1 |
| lopband | godkänd | 0 | 0 |
| roddmaskin | fel | 1 (R1) | 1 |
| crosstrainer | godkänd | 0 | 1 |
| hantlar | fel | 1 (H1, meta) | 2 |
| kettlebell | godkänd | 0 | 0 |
| cykellas | godkänd | 0 | 2 |
| elcyklar | godkänd | 0 | 1 |
| tunturi | godkänd | 0 | 1 |
| sparkcykel | godkänd | 0 | 0 |

Antal faktafel: 2
