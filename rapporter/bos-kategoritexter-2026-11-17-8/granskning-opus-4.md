# Granskning av pilottexter v2: oberoende Opus-granskning 4 (2026-11-17)

**Granskat:** `pilot_texter_v2.py`, tio kategorier med brödtext, SEO-titel och meta. Texterna jämfördes med `underlag/<handle>.json`.
**Regler:** `shopify-sync/docs/kategoritexter-standard.md` (avsnitt 2, 3, 4 och 8) och de fem sista posterna i `shopify-sync/docs/LARDOMAR.md`.
**Metod:** jag kontrollerade varje påstående själv mot `alla_titlar`, `ovriga_titlar` och `marken`. Jag räknade med `python3 -I` och absoluta sökvägar och läste alla titellistor rad för rad. Kontrollskriptet användes inte. Inget skrevs till Shopify och inga nätverksanrop gjordes. Den enda fil jag skrev är den här.

**Begrepp:**
- **FAKTAFEL** betyder att ett påstående inte stämmer med underlaget. Det räknas också som faktafel om en köpbar produkt i kollektionen, även en bland `ovriga_titlar`, gör påståendet osant för den som ser sidan.
- **ANMÄRKNING** gäller stil, precision eller underlaget. Det är valfritt att rätta.
- **Golvat** betyder att antalet avrundas nedåt enligt standarden: till femtal under 30, till tiotal från 30 och till hundratal från 100.

## Kontroller som gäller alla tio texter

| Kontroll | Resultat |
|---|---|
| Brödtext 60–200 ord | 64–100 ord. Alla godkända |
| SEO-titel högst 43 tecken | 27–43 tecken. Alla godkända (crosstrainer har exakt 43) |
| Meta 70–155 tecken (uppdraget), 120–155 (standarden, avsnitt 4) | 137–146 tecken. Alla klarar båda gränserna |
| Första meningen har verb | Alla brödtexter har "säljer" och alla metatexter har "Köp" |
| Prisuppgifter | Inga belopp och inga prisspann. Texterna har bara hänvisningen "Öppna en produkt för att se pris …" (standarden avsnitt 8.3 följs eftersom prisjobbet pågår) |
| Leverantörer som märken (Velomarket, Gorilla Sports Norden) | Nämns inte |
| Löften, superlativ, leveranstid, frakt och ursprung | Inga hittade. "flest" är en räknad jämförelse |
| "produkter" i stället för "modeller" | Används i alla texter. "modell" förekommer inte |
| Exempeltitlar ordagrant i `alla_titlar` | Alla 30 finns ordagrant |
| "bland annat" före uppräkningar som inte är fullständiga | Finns i alla brödtexter och metatexter. Cykellåsmetan använder "till exempel" |
| SEO-titlar unika | Unika sinsemellan och skiljer sig från alla SEO-titlar i `alla_kollektioner_seo_live.json` |
| Rättelser från granskning 3 (R1 och H1) | Båda är införda: "minst fem produkter vardera" och hantlarmetan utan "upp till 50 kg" |

## Resultat per kategori

| Kategori | Utfall | Faktafel | Anmärkningar |
|---|---|---|---|
| motionscykel | godkänd | 0 | 1 |
| lopband | godkänd | 0 | 1 |
| roddmaskin | godkänd | 0 | 2 |
| crosstrainer | godkänd | 0 | 1 |
| hantlar | godkänd | 0 | 1 |
| kettlebell | godkänd | 0 | 1 |
| cykellas | godkänd | 0 | 1 |
| elcyklar | godkänd | 0 | 2 |
| tunturi | godkänd | 0 | 1 |
| sparkcykel | godkänd | 0 | 2 |

---

## 1. motionscykel: godkänd

| Påstående | Underlag | Utfall |
|---|---|---|
| motionscyklar, spinningcyklar och hopfällbara motionscyklar | Titlar som börjar med Spinningcykel: 24. Titlar med Hopfällbar: 4 | godkänd |
| Tunturi, BH Fitness, Toorx, Hammer och Christopeit | marken 28/20/17/11/9. Velomarket nämns inte | godkänd |
| minst 80 produkter | 87 huvudprodukter (84 unika titlar), golvat till 80. Med övriga 93 | godkänd |
| Tunturi och BH Fitness har flest | Titlar 28 och 22. Med övriga 30 och 22. Toorx har 19 med övriga | godkänd |
| minst 20 spinningcyklar | 24, golvat till 20. "Spinning Bike HAMMER HyRace S" bland övriga ökar antalet | godkänd |
| svänghjul, ryggstöd, motståndsnivåer i namnet | Till exempel "med 11 kg Svänghjul", "med Ryggstöd", "med 32 Motståndsnivåer" | godkänd |
| SEO: Tunturi, BH Fitness, Toorx | De tre största märkena | godkänd |
| 3 exempel | Ordagrant | godkänd |

ANMÄRKNING M1 (valfri, kvar från granskning 3): meningen "hopfällbara motionscyklar från bland annat Tunturi …" kan läsas som att Tunturi har en hopfällbar motionscykel. Bland huvudprodukterna är de hopfällbara från BH Fitness, Christopeit och Toorx. "Minicykel Tunturi Hopfällbar med Display" finns bland övriga, men det är en minicykel. Meningen är inte fel som helhet.

## 2. lopband: godkänd

| Påstående | Underlag | Utfall |
|---|---|---|
| Tunturi, BH Fitness, Christopeit, Hammer och Toorx | marken 15/14/9/6/5. Finnlo by Hammer har 2 till | godkänd |
| minst 50 | 52 unika, golvat till 50. En produkt saknar pris (`antal_utan_pris_noll` = 1), men 51 är fortfarande minst 50 | godkänd |
| Tunturi och BH Fitness har flest | Titlar 15 och 14. Med övriga 17 och 15, medan Christopeit och Hammer har 10 vardera | godkänd |
| Flera löpband är hopfällbara | 6 titlar med "Hopfällbart" | godkänd |
| skärm eller träningsprogram i namnet | "5-tums Skärm", "10-tums Display", "44 Träningsprogram" med flera | godkänd |
| 3 exempel | Ordagrant | godkänd |

ANMÄRKNING L1 (underlag): bland övriga finns två köpbara gåband ("Gåband CHRISTOPEIT Walking Pad 4.2" och "Gåband Hammer Walk 2.0 Norsk …"). De gör inget påstående osant.

## 3. roddmaskin: godkänd

| Påstående | Underlag | Utfall |
|---|---|---|
| Tunturi, Hammer, Christopeit och BH Fitness | marken 9/5/5/3 | godkänd |
| minst 20 | 22 (21 unika), golvat till 20. Med roddmaskinerna bland övriga 27 | godkänd |
| Tunturi har flest, bland annat tre i serien Cardio Fit | Tunturi 9 (R20, R25, R30 i Cardio Fit). Med övriga har Christopeit 8 och Hammer 6, så Tunturi har fortfarande flest | godkänd |
| Hammer och Christopeit har minst fem vardera | 5 och 5 bland huvudprodukterna, 6 och 8 med övriga | godkänd |
| Meta: "bland annat i serien Cardio Fit" | Se ovan | godkänd |
| 3 exempel | Ordagrant | godkänd |

ANMÄRKNING R-A1 (underlag): kollektionen innehåller rullskridskor som går att köpa ("Rullskridskor NILS EXTREME NF102"). Texten påstår inget om det, men produkten hör inte hemma i kollektionen. Det bör tas upp separat, utan att texten ändras.
ANMÄRKNING R-A2 (underlag, kvar från granskning 3): titlar som börjar med "Rodd-ergometer", "Rowing ergometer" och "Rowing machine" räknas inte som huvudprodukter. Huvud-regexen bör utökas inför nästa körning.

## 4. crosstrainer: godkänd

| Påstående | Underlag | Utfall |
|---|---|---|
| Christopeit, Hammer, Tunturi, BH Fitness och Gymstick | marken 8/6/6/3/1 | godkänd |
| minst 20 | 24, golvat till 20 | godkänd |
| Christopeit har flest | 8 mot 6 och 6. Med övriga (två hybridtränare) har Christopeit 10 | godkänd |
| En produkt anger 8 nivåer och manuell broms | Bara "Crosstrainer Tunturi Cardio Fit C30, 8 Nivåer, Manuell Broms" | godkänd |
| Christopeit CT 6 är en kombinerad crosstrainer och motionscykel | "Crosstrainer och Motionscykel Christopeit CT 6" | godkänd |
| 3 exempel | Ordagrant | godkänd |

ANMÄRKNING C1 (kvar från granskning 3): märket Gymstick står inte i någon titel ("GX3.0 Crosstrainer"). Det stöds av vendor-fältet, men stavningen som R8 kräver går inte att kontrollera mot en titel.

## 5. hantlar: godkänd

| Påstående | Underlag | Utfall |
|---|---|---|
| hantlar, hantelset och justerbara hantlar | Det finns titlar som börjar med Hantel, Hantelset och Justerbar Hantel | godkänd |
| Tunturi, Gymstick, Toorx, Hammer och Christopeit | marken 26/10/7/5/2. Gorilla Sports Norden nämns inte | godkänd |
| minst 50 | 53 (52 unika, 1 utan pris), golvat till 50 | godkänd |
| Vikterna börjar vid 0,5 kg | "Pro Chrome Hantel 0,5kg - enkel". Inget lägre finns bland övriga | godkänd |
| Hantelset på bland annat 15, 20 och 28 kg | Till exempel "Hantelset Gymstick Vinyl, 15 kg", "Hantelset Toorx Gjutjärn, 20 kg" och "Hantelset Tunturi Vinyl, 28 kg" | godkänd |
| Kombinerade hantel- och skivstångsset på bland annat 20 och 50 kg | "Hantel- och Skivstångsset Christopeit 4-i-1, 20 kg" och "Hantel- och Skivstångsset Tunturi Vinyl 50 kg". Ett set på 60 kg bland övriga täcks av "bland annat" | godkänd |
| Material: gjutjärn, vinyl, neopren och gummi | "Gjutjärn", "Vinyl", "Neopren" samt "Gummibelagd", "gummerad" och "Gummiöverdrag" | godkänd |
| Tunturi har flest | 26 (32 med övriga) | godkänd |
| Meta: Vikter från 0,5 kg. Minst 50 produkter | Se ovan | godkänd |
| 3 exempel | Ordagrant. Zipro finns i marken (1) | godkänd |

ANMÄRKNING H-A1 (underlag): "Snabbkoppling Hantel 22,5kg" och "Hantelset Tunturi Centuri Neopren med Ställ" räknas som huvudprodukter. Det är rimligt. Hantelställ och hantelstänger ligger korrekt bland övriga.

## 6. kettlebell: godkänd

| Påstående | Underlag | Utfall |
|---|---|---|
| Tunturi, Toorx, Hammer, Gymstick och Christopeit | marken 11/11/5/5/3 | godkänd |
| minst 30 | 35, golvat till 30 | godkänd |
| Vikter från 2 till 24 kg (brödtext, SEO och meta) | Lägst "Kettlebell Christopeit, 2 kg" och "Kettlebell Tunturi PE, 2 kg". Högst "Kettlebell Hammer Premium, 24 kg" och "Kettlebell Tunturi, 24 kg". Övriga (12 kg) ligger inom spannet | godkänd |
| gjutjärn, vinyl och gummibotten | "gjutjärn", "Vinyl" och "Gjutjärn med Gummibotten" | godkänd |
| Tunturi och Toorx har flest | 11 och 11 (12 och 12 med övriga) | godkänd |
| 3 exempel | Ordagrant | godkänd |

ANMÄRKNING K1 (underlag): "Kettlebellhandtag Tunturi Rapid Justerbart, 3,5 kg" räknas som huvudprodukt. Utan den finns 34 produkter, vilket fortfarande är minst 30, och Tunturi har 10, vilket fortfarande är bland de två största. Inget påstående ändras.

## 7. cykellas: godkänd

| Påstående | Underlag | Utfall |
|---|---|---|
| vajerlås, kedjelås, vikbara lås, U-lås och kabellås | Alla typer finns som första ord i titlarna (kabellås: 3 plus "Cable lock") | godkänd |
| AXA, Squire och Giant | marken 41/16/5. M-Wave nämns inte, vilket täcks av "bland annat" | godkänd |
| minst 60 | 63 unika, golvat till 60 | godkänd |
| AXA och Squire har flest | 41 och 16 (45 och 18 med övriga, Giant 10 med grepp och handtag) | godkänd |
| nyckel eller kod i namnet, några vikbara | 19 titlar med nyckel eller kod och 9 med vikbar | godkänd |
| 3 exempel | Ordagrant | godkänd |

ANMÄRKNING CL1 (stil, valfri): brödtexten har nu två "bland annat" i samma mening. Metan rättades i förra granskningen men inte brödtexten. Förslag:
- Före: `BEST OF SPORTS säljer cykellås, bland annat vajerlås, kedjelås, vikbara lås, U-lås och kabellås, från bland annat AXA, Squire och Giant. Här finns minst 60 produkter.`
- Efter: `BEST OF SPORTS säljer cykellås från bland annat AXA, Squire och Giant, till exempel vajerlås, kedjelås, vikbara lås, U-lås och kabellås. Här finns minst 60 produkter.` (ordantalet ändras inte)

## 8. elcyklar: godkänd

| Påstående | Underlag | Utfall |
|---|---|---|
| Tenways, ADO, Giant, Fiido och Engwe | marken TENWAYS 25, ADO 17, Giant 11, Fiido 6, Engwe 3. Texten stavar "Tenways" som i titlarna (R8) | godkänd |
| minst 70 | 78, golvat till 70 | godkänd |
| Tenways och ADO har flest | 25 och 17 | godkänd |
| minst 10 hopfällbara elcyklar | 13 titlar börjar med Hopfällbar, golvat till 10 | godkänd |
| minst 10 el-lastcyklar | 12 titlar börjar med El-lastcykel, golvat till 10 | godkänd |
| 3 exempel | Ordagrant | godkänd |

ANMÄRKNING E1 (precision, kvar från granskning 3): Giant och Engwe har varken hopfällbara elcyklar eller el-lastcyklar. Meningen är inte fel som helhet. Det är valfritt att byta Engwe mot Cargobike of Sweden (3, alla el-lastcyklar).
ANMÄRKNING E2 (underlag): kollektionen innehåller en köpbar elsparkcykel, "Elektrisk Sparkcykel Razor Electric Tekno Scooter". Texten påstår inget om den, men den hör inte hemma bland elcyklar. Det bör tas upp separat.

## 9. tunturi: godkänd

| Påstående | Underlag | Utfall |
|---|---|---|
| motionscyklar, löpband, roddmaskiner, träningsbänkar, hantelset, viktskivor, kettlebells och yogamattor | Alla finns bland första orden i titlarna (22/12/9/17/11/11/10/10) | godkänd |
| minst 300 | 381 (379 unika, 1 utan pris), golvat till 300 | godkänd |
| minicyklar och massagerullar | 11 och 8 titlar | godkänd |
| konditionsmaskiner och tillbehör för styrketräning och yoga | Se typerna ovan | godkänd |
| Meta: hantlar | 11 titlar börjar med "Hantlar" | godkänd |
| 3 exempel | Ordagrant | godkänd |

ANMÄRKNING T1 (underlag, kvar från granskning 3): underlaget saknar huvud-regex, så alla 381 produkter räknas. Talet håller ändå.

## 10. sparkcykel: godkänd

| Påstående | Underlag | Utfall |
|---|---|---|
| SOKE, Union, Rideoo, Versatyl och Ethic | marken 30/22/10/8/5 | godkänd |
| minst 80, bland annat stunt- och tricksparkcyklar | 87 unika, golvat till 80. "stunt" finns i 46 titlar och "trick" eller "triks" i 18 | godkänd |
| SOKE och Union har flest | 30 och 22. Med övriga (hjul och griptape) har Union 65, men de två är fortfarande de största | godkänd |
| Delar som hjul och griptape finns som separata produkter | Bland övriga finns många "Sparkcykelhjul …", "Griptape …" och "UNION Griptape …" | godkänd |
| 3 exempel | Ordagrant, bland annat "Stuntsparkcykel SOKE GO, Svart och Rosa" | godkänd |

ANMÄRKNING S1 (underlag): bland huvudprodukterna finns titlar som inte är på svenska, till exempel "Trikitõukeratas Ethic Pandora Complete Pro Scooter L Black" (estniska) och "Ethic Pandora Complete Pro Scooter M Blue". De används inte som exempel. Titlarna bör rättas separat.
ANMÄRKNING S2 (underlag): kollektionen innehåller snöskor ("Snöskor STIGA Snow Kick …") och barnsparkcyklar som inte räknas som huvudprodukter (till exempel "Barnsparkcykel Aest Kids, Svart"). Inget påstående blir osant.

---

## Sammanfattning

Inga faktafel hittades. Båda faktafelen från granskning 3 (R1 för roddmaskin och H1 för hantlarmetan) är rättade, och anmärkning A-H1 om hantlarnas brödtext är införd. Kvar finns bara valfria anmärkningar. Den enda som gäller själva texten är stilen i cykellåsens första mening (CL1). Övriga anmärkningar gäller underlaget eller kollektionernas innehåll: rullskridskor bland roddmaskiner, en elsparkcykel bland elcyklar, snöskor bland sparkcyklar och titlar på andra språk än svenska. De bör tas upp separat och påverkar inte texterna.

Antal faktafel: 0
