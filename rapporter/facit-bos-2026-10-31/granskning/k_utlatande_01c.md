# Granskning väg 2, elcyklar och styrväska k_01c (2026-11-04)

Det här är en oberoende granskning av 7 utkast i `vag2_skriv/k_01c_utkast.json` och 4 avvisningar i `k_01c_avvisade.json`. Granskaren har bara läst, inget har ändrats i Shopify. Underlaget är regelbok v1.4, agentprompter (Granskare), BESLUTSLOGG, butiksprofil-bestofsports.json och standard §16. Formatet följer `vag2k_utlatande_10_12`, `_13_15` och `_16_17`.

**Metod:** alla 11 produkter hämtades live via `shopify_api` (title, handle, status, tags, seo, descriptionHtml, varianter med SKU, pris och options). Alla är ACTIVE och ingen har SEO satt. Typord och märkesskrivning kontrollerades med titelsökning i butiken (Styrväska, El-lastcykel, vendor PRO). Utlåtandet provkördes med `bygg_m_skriv.py` mot en scratchpad-fil: 7 skrivbara, alla 'fore' träffar exakt en gång, inga dubbletter och inga längdfel. Antalet "enligt tillverkaren" räknades per text.

**Resultat:** 5 GODKÄND, 2 RÄTTA, 0 UNDERKÄND. Alla 4 avvisningar är motiverade.

| nr | id | dom | före → efter / skäl |
|---|---|---|---|
| 9051 | 10676717453578 | GODKÄND | Allt spårbart. Svart stöds av varianterna (XS/M/L / black, samma pris), inte bara av titeln. Räckvidden står ordagrant från raden 'Räckvidd: upp till 100 km' med "enligt tillverkaren" en gång. |
| 9053 | 10503245529354 | GODKÄND | Alla rader spårbara (SyncDrive Pro 2, 400 Wh, 130 km, Advanced-kolfiber/Aluxx SL, Bomber Z2 150 mm, Float 185x52,5, Deore 12, MT420, AM30, DHF/Dissector). Shoreline finns bara i titeln men det finns en enda variant och källan säger inte emot (praxis från k_16). Ramstorlekar och kvalitetsord är rätt utelämnade. |
| 9054 | 10682105430282 | RÄTTA | **html:** `<li>Däck: Maxxis Rekon Tanwall 2,4 tum, 27,5 tum på storlek XS och S, 29 tum på storlek M och L</li>` → `<li>Däck: Maxxis Rekon Tanwall 2,4 tum, 27,5 tum på storlek XS och S, 29 tum på storlek L</li>`. Varianterna är bara XS, S och L, och M ska inte nämnas. Den engelska källan är korrekt översatt. Elcykel är butikens live-ord (R7). E-Lock och Find My är rätt utelämnade. Räckvidden 'Range: up to 115 km' är en etiketterad rad, se fråga 1. |
| 9055 | 10471119159562 | GODKÄND | Lastgränsen är rätt utelämnad: 164 kg i löptexten motsäger 'Lastkapacitet: 200 kg' (R2, §16.3). Rammaterialet är rätt utelämnat: 'ALUXX Aluminium' står under etiketten '1,5-tums LCD-skärm:', och att det gäller ramen är en tolkning utanför källan (R1). Övrigt spårbart. Svart finns bara i titeln, med en variant. Taggen 'På beställning' saknas, så leveranstidsmeningen saknas med rätta. |
| 9056 | 10471065026826 | GODKÄND | Spårbart. Ramstorlek M är den entydiga delen av den trasiga raden (R2). 'Växellåda' blir Växelsystem, vilket är rätt eftersom Tourney inte är en växellåda. Grafit finns bara i titeln, med en variant. |
| 9060 | 10488308203786 | GODKÄND | 'Lastkapacitet upp till 100 kg' och 'tre till fyra barn' står i löptext utan etikett och är rätt utelämnade (R4). Säkerhetsbelysning och 'säker resa' är rätt utelämnade. 'Steglöst' står i löptexten. Ingen färg, en variant. |
| 9061 | 10472239137034 | RÄTTA | **html:** `en stor vattentät ficka enligt tillverkaren och snabbfäste` → `en stor ficka och snabbfäste`. "Enligt tillverkaren" stod 3 gånger, varav 2 för samma påstående (R5). Efter rättningen står det 2 gånger. Bytet Styckväska → Styrväska godtas: 'Handlebar Bag' har en entydig översättning och Styrväska är butikens live-ord (Basil Mali, Giant Scout Burrito Bar Bag). 'Bredd: 275–640 mm' återges ordagrant och är ingen riskuppgift, så den får stå. '5000 mm vattenslang' och 'ökad synlighet' är rätt utelämnade. |

## Avvisningar (k_01c_avvisade.json)

| nr | id | bedömning |
|---|---|---|
| 9052 | 10676720173322 | **Motiverad.** Titeln säger Svart men varianterna är black och green (samma pris). Titeln stämmer alltså inte med produkten (R3). Utkastarens extra skäl att 'Shimano Claris med 7 växlar' är en motsägelse bygger på kunskap utanför källan (R1) och bör inte användas som skäl. Färgen räcker. |
| 9057 | 10471092093194 | **Motiverad.** Titeln säger silver-red, alla fyra varianter är silver och priset skiljer sig (15 249 / 15 279 kr). Det är R3. |
| 9058 | 10494834245898 | **Motiverad.** Titeln säger röd, källan säger 'Färg: grön' och handle 'r-d'. Löptexten säger 'kedjebromsar', specifikationen 'mekaniska skivbromsar'. Texten är maskinöversatt ('något på en stålram', 'pegboards'). Det är R2 och R3. |
| 9059 | 10472304935178 | **Motiverad.** Källan har bara titelns fakta. Raderna '244 pounds' och '74.01' saknar etikett, och resten är säkerhets- och kvalitetslöften. Det ger mindre än två entydiga fakta utöver titeln (R3, tunn källa). Dubbdäck har också samma säkerhetsprofil som 6209, som fortfarande är en öppen fråga. |

## Återkommande fynd (för regelbok och test)
1. **"Enligt tillverkaren" upprepas för samma påstående i inledning och specifikation** (9061: 3 gånger). R5 säger högst två per text, men skriptet räknar inte. Förslag på test: räkna förekomster per text och larma om fler än 2.
2. **Ramstorlekar och storleksberoende uppgifter som inte finns som variant** (9054: storlek M nämns trots att bara XS, S och L säljs). Förslag på regel: storleksberoende uppgifter får bara nämna storlekar som finns bland produktens varianter.
3. **Felmärkta specifikationsrader** ('1,5-tums LCD-skärm: ALUXX Aluminium', 'Växellåda: Tourney', 'Tillverkare: Romet, Ltd: M (17")'). Utkastaren hanterade alla rätt enligt R2. Värt ett exempel i regelboken: värdet får bara användas om det är entydigt utan kunskap utanför källan.
4. **Lastgräns i både löptext och tabell med olika värden** (9055: 164 eller 200 kg). R4 täcker inte uttryckligen motsägelse mellan löptext och tabell. Förslag: lägg till "vid olika värden för lasten i samma källa → utelämna".
5. **Avvisningsskäl hämtade från minnet** (9052: Claris har inte 7 växlar). R1 bör gälla även skälen för en avvisning.
6. **Formatskriptet gör "El-lastcykel" till "El-Lastcykel"** (titel_versaler versaliserar varje del efter bindestreck). Butikens live-ord är 'El-lastcykel' överallt. Samma sak gäller tidigare 'Dips-Handtag'. Det är inte rättat här eftersom det följer Davids formatbeslut 2026-11-01, se fråga 2.
7. **Märket PRO med versaler** strider mot R8 men har redan skrivits så ('Handpump PRO Minipump …'). Skriptet släpper igenom det. Märket bör få ett uttryckligt undantag i profilen eller rättas överallt, se fråga 3.

## Öppna frågor till David
1. Räckvidd från en engelsk källa (9054, 'Range: up to 115 km'): Alt A gäller bara lastgränser. Ska räckvidd och batteriuppgifter från engelsk källa också utelämnas? I det här utlåtandet får raden stå.
2. Ska typordet efter bindestreck ha liten bokstav ("El-lastcykel", som live) och skriptets regel ändras?
3. Märket PRO: ska det skrivas "PRO" som i butiken, eller "Pro" enligt R8?
4. "Styckväska" används live även för andra väskor (Basil Magnolia City Bag, Giant H2Pro, PRO Gravel Discover). Ska de få rätt typord i kommande batcher?
