# Granskning k_52b (14 utkast, 2 avvisade), Opus, 2026-11-17

Källa: live-läsning 2026-11-17 (`rapporter/shopify-original-2026-11-17/k_52b_kalla_live_granskning.json`), butikens titlar (`rapporter/inventering-bos-2026-11-17/alla_produkter.json`) och webbkoll mot tillverkare och återförsäljare. JSON-utlåtandet finns i `vag2_skriv/k_utlatande_52b.json`. Varje ändring (före → efter) är kontrollerad i python: texten som ändras finns exakt en gång i sitt fält. Efter ändringarna är metabeskrivningarna (texten under länken i sökresultaten) högst 145 tecken. Standardblocket är identiskt med `b_skriv_24.json` på alla utkast. Leveranstidsmeningen finns bara på 52110, som är den enda produkten med taggen "På beställning". Ingenting har ändrats i Shopify.

**Resultat:** 10 GODKÄND, 3 RÄTTA, 1 UNDERKÄND. Båda avvisningarna är rätt.

| nr | Produkt | Dom | Kort skäl |
|---|---|---|---|
| 52101 | Bakskärm SKS X-Blade Dark 26/27,5 | RÄTTA | "Monteras på sadeln" är fel. Skärmen sitter på sadelstolpen med snabbfäste (R2). |
| 52102 | Sittdyna framsäte Cargobike of Sweden Flex/Delight | UNDERKÄND | Framdynan har ca 25 cm ryggstöd och bakdynan 18 cm. Handle och artikelnummer pekar på olika dynor (1521-32 och 1521-31). |
| 52103 | Pedaler Look Trail Fusion Lime | GODKÄND | Frankrike och 100 kg står i källan och är skrivna en gång var med "enligt tillverkaren" (två totalt). Tillverkaren bekräftar ursprunget. |
| 52104 | Dricksflaska Giant ARX 400 ml, Blå | GODKÄND | "För barncyklar" är källans ord. Flaskan har ingen säkerhetsfunktion. Texten följer de skrivna syskonen. |
| 52105 | Sadel Giant Approach | GODKÄND | Lastgränsen är skriven enligt v1.10. Det finns inga komfort- eller tryckpåståenden. |
| 52106 | Stänkskärmset Giant Revolt 2019+ | GODKÄND | Stavningen följer tolv skrivna syskon (se beslut 2). |
| 52108 | Stänkskärmset Academy 24 tum | GODKÄND | Kort text med källans enda mening. |
| 52110 | Framskärm SKS Mudrocker Front | GODKÄND | Taggen "På beställning" finns, och leveranstidsmeningen är med. |
| 52111 | Sadel Giant Romero, Svart | RÄTTA | "Elastisk dämpning" stryks, eftersom det är en del av källans komfortpåstående. |
| 52112 | Knä- och armbågsskydd Boom Basic Double Pad Set | RÄTTA | Texten är sann med bara fakta. "Boards" blir "brädor", och raden "söker skydd för" skrivs om. |
| 52113 | Träningsboll Tunturi Gymball 65 cm, Ljusblå | GODKÄND | "Anti Burst" och "220 kg" är rätt utelämnade (R4). |
| 52107 | Handtag Liv Sole-O, Svart/Vit | GODKÄND | Typordet Handtag är butikens eget ord för grips (R7). |
| 52114 | Handtag Liv Sole-O, Svart | GODKÄND | "Designat för kvinnor" står en gång med "enligt tillverkaren". |
| 52116 | Handtag Ethic Grips Transparent | GODKÄND | Ordet "handtag" står i källan. Alla löften är utelämnade. |
| 52951 | Grips Giant Tactal svart-röd (avvisad) | Avvisning rätt | Färgen motsäger källan. Utan färg skulle titeln krocka med syskonet svart-gul. |
| 52952 | Tire milk Giant (avvisad) | Avvisning rätt | Produkttypen är oklar och det finns inget godkänt typord (v1.12 punkt 5). |

## Viktigaste fynden
1. **52102, Cargobike-dynan:** Källan säger "framsäte" och ryggstödshöjden 18 cm. Den tyska återförsäljaren lucky-bike.de säljer samma Flex/Delight-dyna i två versioner: Front med ca 25 cm och Rear med ca 18 cm. Handle slutar på 1521-32 men varianten har 1521-31. Annonsen blandar troligen ihop fram- och bakdynan. Det går inte att skriva en sann text innan leverantören har rättat annonsen. Dynan sitter dessutom i lådan där barn transporteras.
2. **52103, Look:** LOOK:s egen sida bekräftar "Made in France" (Nevers), 324 g, 18 mm, 8 piggar och färgen Lime. Fotavtrycket 107 x 105 mm stämmer med LOOK:s pressmaterial, medan produktsidan anger 104 x 104 mm. Därför behålls källans värde. Uppgiften 100 kg kommer från en svensk rad med etikett och enhet, och lime-säljare anger samma vikt. Bike24 kallar samma EAN (streckkod) "Trail Roc Fusion", men någon sådan modell finns inte hos LOOK, och alla data passar Trail Fusion. Krocken bedöms därför vara ett namnfel hos återförsäljaren.
3. **52101:** Källan har både "snabbfäste för sadelstolpe" och "montering på sadeln". Tillverkaren och återförsäljarna anger sadelstolpe, så "på sadeln" tas bort.
4. **52112, Boom:** Davids krav är att texten ska vara sann med bara fakta. Det uppfylls av typ, märke, modell, målgruppen vuxna, användning, vikt, artikelnummer och EAN. "Skyddsnivå: extrem" är utelämnad. Produkten har två varianter med samma artikelnummer men olika pris (349 och 329 kr). Den får skrivas enligt v1.7/v1.9 eftersom texten inte anger färg, storlek eller pris.
5. **Sadlarna 52105/52111:** Raden "Maximal lastgräns: Ej känd" står i specifikationen, och meningen "Maximal lastgräns är inte känd." står i texten (v1.10). Ingen annan lastuppgift finns. Texterna har inga komfort-, ergonomi- eller hälsoeffekter efter rättningen av 52111.
6. Det finns inga ursprungspåståenden utom 52103, som är tillåtet. Det finns inga kvalitets-, skydds- eller hälsopåståenden. Titlar och SEO-titlar (titeln som visas i sökmotorer) är unika mot butikens 5 377 produkter.

## Beslut för David
1. **52102, Cargobike-dynan:** Alternativ A (rekommenderas): skriv inte nu, och be Velomarket bekräfta om 1521-31 är fram- eller bakdynan. Alternativ B: skriv en text utan ordet "framsäte" och utan ryggstödsmåttet. Risk med B: kunden kan få fel dyna. Om inget beslutas lämnas produkten utan ny text.
2. **Stavningen Stänkskärmset/Stänkskärmsset:** Live-titlar och källor skriver "Stänkskärmsset", vilket är den vanliga svenska formen (jämför butikens "Stänkskärmsfäste"). De skrivna syskonen har "Stänkskärmset". Alternativ A (rekommenderas nu): behåll "Stänkskärmset" för att butiken ska vara enhetlig. Alternativ B: byt alla till "Stänkskärmsset" i en senare rättningsomgång. Om inget beslutas gäller A.
3. **52951 och 52952:** De avvisade produkterna kan skrivas om David godkänner skrivning utan färg för Tactal (med titelkrock mot svart-gul som risk) eller typordet "däcktätningsvätska" för Tire milk. Rekommendation: avvakta.

## Webbkällor
- https://lookcycle.com/uk-en/products/dh-dirt/trail-fusion
- https://www.lookcycle.com/download/press-room/trail-this/trail-fusion/press-book-trail-fusion-en.pdf (enligt sökresultat)
- https://www.bike24.com/p2527093.html (enligt utkastaren, 403 vid hämtning)
- https://www.bike-discount.de/en/index.php/detail/018d1689bace7299a5ef1332d00df4bd
- https://www.bowcycle.com/product/sks-x-blade-26-27.5-inch-336066-1.htm
- https://nanobike.de/en/SKS-X-Blade-Dark-Rear-Wheel-Mudguard-26-27.5-Inch-black
- https://www.lucky-bike.de/Ausruestung/Transport/Lastenfahrraeder-Zubehoer/Cargobike-of-Sweden-Flex-Delight-Sitzkissen-Front.html
- https://www.lucky-bike.de/Ausruestung/Transport/Lastenfahrraeder-Zubehoer/Cargobike-of-Sweden-Flex-Delight-Sitzkissen-Rear.html
- https://velomarket.ee/en/products/grips-giant-tactal-double-lock-on-grip-black-red/
- https://www.ebike24.com/giant-tactal-double-lock-on/3246-003
- https://www.giant-bicycles.com/nz/tactal-double-lock-on-grip
