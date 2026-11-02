# Skrivrapport våg 2a – BEST OF SPORTS (2026-11-02)

Butiken kontrollerad med get-shop-info: BEST OF SPORTS (bestofsports.se, SEK). Inget committat.

## Sammanfattning
- **32 produkter skrivna, 0 userErrors.** Kanarie (2101, 2108, 2110), därefter batchar om 8, 8, 8 och 5.
- Alla 32 var ACTIVE före skrivning och är ACTIVE efter. Handles oförändrade (jämförda mot live före). Inga hoppades över.
- Återläst alla fält (title, handle, status, seo.title, seo.description, descriptionHtml) efter varje batch och jämfört med det som skickades: inga avvikelser utöver det avsedda Shopify-beteendet (seo.title lagras som null när den är lika med titeln: 2108, 2109, 2114, 2205, 2208, 2410, 2414).
  - Produkter utan meta (skickades utan description, livevärdet var tomt, återlästes som null): 2110, 2111, 2208, 2315, 2403, 2407, 2410, 2508, 2511.
- Original (före) sparade i `rapporter/shopify-original-2026-11-01/vag2a_fore.json` (title, handle, status, seo, descriptionHtml för alla 32, läst live strax före första skrivningen; alla hade seo.title och seo.description = null). Obs: html-texterna i före-filen är överförda för hand från live-svaret.
- Byggd skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/a_skriv.json` (32 produkter, fälten id, nr, titel, seo_title, meta, html). JSON är sanningen.

## Skrivna produkter (nr)
2101, 2102, 2103, 2104, 2106, 2113, 2114, 2107, 2108, 2109, 2110, 2111, 2508, 2511, 2509, 2208, 2210, 2204, 2205, 2206, 2209, 2211, 2212, 2213, 2315, 2309, 2313, 2403, 2404, 2410, 2407, 2414.

## Rättningar som applicerades (före -> efter, ur granskningsrapporterna)
- **2107** SEO-titel "Träningshandskar Trec #02 Gel Shock" -> "Träningshandskar Trec #02 Gel Shock, Röd" (40 tecken).
- **2108** meta och html: "ett flytande gymtalk" -> "en flytande gymtalk"; meta "torkar det snabbt" -> "torkar den snabbt"; spec "Förpackning: Enkel att dosera" -> "Förpackning: Gör produkten enkel att dosera".
- **2109** meta och html: "torkar talket snabbt" -> "torkar talken snabbt".
- **2110, 2111** html: "Toorx Leopard/Panther Boxing Gloves är boxningshandskar" -> "Toorx Leopard/Panther är boxningshandskar"; hela avsnittet "Passar för" (en punkt) borttaget. Titel, SEO och specifikationer oförändrade.
- **2509** SEO-titel "Träningshandskar Trec #02 Gel Shock" -> "Träningshandskar Trec #02 Gel Shock Svart L" (exakt 43 tecken).
- **2204** html: "Användning efter träning" -> "Efter träning".
- **2205** html: punkten "Dig som vill ha en massageboll i kork" borttagen.
- **2206** meta och html: "är en gymnastikmatta på 183 x 61 cm och 4 mm tjocklek." -> "är en gymnastikmatta som mäter 183 x 61 cm och är 4 mm tjock."; FAQ "Enligt uppgifterna rengörs mattan..." -> "Mattan rengörs för hand med en fuktig trasa."
- **2209** titel -> "Boxningshandskar Tunturi Allround, 16 oz, Konstläder".
- **2211** meta: "multisydd, utsidan" -> "multisydd. Utsidan".
- **2212** SEO-titel -> "Träningshandskar Trec Gel Shock, Svart, XL" (42 tecken); meta "Gelkuddar finns inuti och öglor mellan fingrarna." -> "Inuti finns gelkuddar och mellan fingrarna sitter öglor."
- **2213** meta: "Det passar styrketräning." -> "Det passar för styrketräning." Titeln behölls (ingen frivillig ändring).
- **2309** html: punkten "Dig som vill ha ett band i latex som är 104 cm långt" borttagen.
- **2313** meta och html: "i PVC med diameter 75 cm ... Enligt tillverkaren tränar bollen" -> "i PVC, 75 cm i diameter ... Med bollen tränar du enligt tillverkaren".
- **2407** titel -> "Gymnastikgummiband Toorx Fabric Bands Medium, Set om 5"; SEO-titel -> "Gymnastikgummiband Toorx Fabric Bands".
- **2414** meta och html: "läggas till en viktstation" -> "användas med en viktstation"; "vill lägga till ett tricepsrep" -> "vill komplettera den med ett tricepsrep".

## Kontroller före skrivning
- `kontrollera_produkttext.py --seo-title-max 43` på kopia där html -> `beskrivning` och standardblocket markerat med [[STANDARDBLOCK]]: **32 produkter, 0 FEL**, 49 varningar (rubriken heter "Passar för" i stället för "Passar dig som", korta texter, saknade avsnitt på tunna källor; samma som i granskningen och godtagna).
- Dubblettkontroll över hela a_skriv.json: inga dubbletter av titel, SEO-titel eller meta; heller inga dubbletter av effektiv SEO-titel (SEO-titel eller titel när SEO saknas).
- Längder: titlar högst 70 och högst 2 kommatecken, SEO-titlar högst 43 (2509 = 43), meta 120–155: inga avvikelser.
- Språkgenomläsning av de rättade texterna (verb, stavning, upprepningar, enheter med gemener, tankstreck i intervall): inga fel i det som rättades.

## Observationer för Davids beslut (ändrades inte, utanför uppdraget)
1. **2209** html och meta säger fortfarande "Tunturi Allround Boxing Gloves är boxningshandskar" (samma cirkulära engelska typord som rättades på 2110, 2111, 2301, 2302). Granskningen rättade bara titeln.
2. **2213** använder "ett flytande gymtalk" och "Talket", medan 2108 och 2109 nu skriver "en flytande gymtalk" och "talken". Genus är inte enhetligt mellan 2108, 2109 och 2213 (granskaren bad bara om att SAOL kontrolleras).
3. **2212** har fått SEO-titel utan "#02" ("Träningshandskar Trec Gel Shock, Svart, XL") enligt granskarens exakta förslag.
4. Produkter med null-meta (tunn källa, enligt standarden) skrevs utan `seo.description`; livevärdet var tomt.

## Ej skrivet (enligt uppdraget)
2301, 2302, 2304, 2308, 2409, 2412 (titeländringar väntar på David) samt alla underkända/handhavda enligt uppdragets lista. Inget av dem rördes.

## Ej gjort
- Ingen post i ANDRINGSLOGG.md och ingen beslutsfil `rapporter/beslut-ÅÅÅÅ-MM-DD.md` (ingen commit begärd; detta är en skrivrapport).
- Kontroll dagen efter nattsynken (Velomarket) av att titlarna ligger kvar: se LARDOMAR 2026-10-30. Rekommenderas: läs tillbaka titlar för de 32 efter nästa nattliga synk.
