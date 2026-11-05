# Stickprov omprövning, BEST OF SPORTS, 2026-11-05

Roll: Stickprov (Sonnet, endast läsning). Butik bekräftad som BEST OF SPORTS via `verifiera_butik`. Inget skrevs i Shopify.

## Urval och metod
- Skrivfiler: k_skriv_16a, 16b, 16c, 16d, 16e, 17ab, 17cd, 17ef, 17i (totalt 49 produkter).
- Kravet var minst 15 produkter med minst en per fil. Eftersom en enda live-läsning (nodes, 5 anrop) var lika billig lästes och jämfördes **alla 49** (alla filer, alla produkter).
- Jämfört live mot skrivfilen tecken för tecken: title, seo.title (null = title), seo.description, descriptionHtml, samt att taggen `texter-klara` finns.
- Språkgranskning: jag läste titel, seo-titel, meta, brödtext och specifikationer för alla 49, plus sökning på "mekanisk", "gjort/gjord/görs", dubbla mellanslag, upprepade ord och metalängd (70-160 tecken).

## Resultat jämförelse live mot skrivfil
- Avvikelser: **0 av 49** i title, seo.title, seo.description och descriptionHtml.
- Tagg `texter-klara`: finns på **49 av 49**.
- Status: alla ACTIVE.
- Metalängd: alla inom 70-160 tecken.

| Fil | Produkter | Avvikelser |
|---|---|---|
| 16a | 9 | 0 |
| 16b | 7 | 0 |
| 16c | 6 | 0 |
| 16d | 6 | 0 |
| 16e | 3 | 0 |
| 17ab | 4 | 0 |
| 17cd | 6 | 0 |
| 17ef | 2 | 0 |
| 17i | 6 | 0 |

## Språkgranskning: fynd

### Meningar utan verb i meta (seo.description)
- **9474** (17cd, Bakväxel Shimano Altus RD-M370 SGS): "Bakväxel i silver från Shimano för 9 växlar." (första meningen saknar verb; andra meningen har verb).
- **9944** (17cd, Spegel M-Wave Spy Mini Short): "Spegel från M-Wave med 46 mm parabolisk spegel som är tredimensionellt justerbar och monteras på styret utan verktyg." (ingen huvudsats, bara bisats) och "Färg: svart." (inget verb, etikettformat).
- **10117** (17cd, Herrcykel Tabou Kinetic 1.0): "Herrcykel Tabou Kinetic 1.0 med aluminiumram, 28-tums däck, 18 växlar från Shimano Tourney och V-bromsar." (första meningen saknar verb).
- **9655** (17ab, Tunturi Exercise Wheel Deluxe): "Mått 26 x 23 x 60 cm, vikt 0,65 kg och knämatta ingår." Har verb men säger att mått och vikt "ingår", vilket är missvisande (bara knämattan ingår).

### Felaktig eller ovanlig svenska
- **9620** (17i, Kettlebellrack) html: "Det är svart, görs av stål och gummi och mäter 60 x 120 x 75 cm" ("görs av" är ovanligt, "är tillverkat av" eller "är gjort av" är normalt).
- **10011** (17i, Universal Paw) html: "Gymstick Universal Paw görs av svart TPR och sitter på stavar." (samma "görs av").
- **9941** (17i, Handledsstöd) meta: "har justerbar rem och är grå-vitt." Bindestrecket är oväntat, normalt "gråvitt". Specifikationen har "Grå-vit".
- **10117** (17cd) html: "Shimano Tourney växelsystem" ska vara "Shimano Tourney-växelsystem" (bindestreck vid sammansättning med egennamn).
- **7074** (16c) spec: "Gaffel: ... helt komposit styrrör" ska vara "helt kompositstyrrör" (särskrivning). Lika mönster: "helt komposit OverDrive Aero-styrrör" i 7040, 7109, 7128, 7134, 7152, "helt kolfiber OverDrive Aero-styrrör" i 7110 och 7180, samt "helt komposit, OverDrive-styrrör" i 7070 och 7075. "helt komposit" är ofullständigt, "helt i komposit" vore korrekt.
- **7033** (16a, Damcykel Liv EnviLiv Advanced SL LTD): titel och meta säger "Damcykel/Damcykeln" men brödtext och spec säger "Landsvägscykeln ..." / "Cykeltyp: Landsvägscykel" och "Dig som vill ha en landsvägscykel med ram i komposit". Inkonsekvent produkttyp.
- **7041** (16a, Kona Process 134) Passar för: "Dig som vill kunna välja mellan två 29-tumshjul och en mullet-inställning med flip-chip" är svårbegripligt (ett val mellan "två 29-tumshjul" och en "mullet-inställning" går inte ihop).
- **6052** (16b) spec: "Gaffel: Avancerad komposit, helt kompositstyrrör" (svenskt "Avancerad" där övriga filer har "Advanced-Grade"; inkonsekvent).
- **7179** (16e) spec: "Advanced SL-klassad komposit" (övriga har "Advanced SL-grade"); "bento-låda" mot "bento box" i 7055/7074.
- Inkonsekvent term "tubeless" i spec för 7047, 7052 och 7055 medan resten av texterna säger "slanglös/slanglösa".
- **7038** (16a) spec: "Växelsystem: SRAM Rival AXS" men "Bromsar: SRAM Rival eTap" i samma produkt (eTap/AXS blandas; fakta ej kontrollerad mot källa).
- Särskrivning av metastil i flera 16b/16c-metas: "Landsvägscykel Giant TCR Advanced 1 PC i Dreamy Blue har ..." (obestämd form som subjekt, ej fel men avviker från "Landsvägscykeln ..." i 16a/16d). Berör 6052, 6060, 7047, 7052, 7055, 7062, 7065, 6057, 7070, 7072, 7074, 7075, 7084, 7179.

### Gjort/gjord
- **9006** (17cd, Basil Mid Engine Cover): "är gjort av 4,5 mm tjock neopren" (rätt genus för "skydd", neutrum). Inget fel.
- **9474** (17cd): "Bakväxeln är silverfärgad och gjord för 9 växlar" (rätt genus, "bakväxel" är utrum). Inget fel.

### Pluralis/singularis
- Inga tydliga fel funna. "hantlar" (9621, 9626) är korrekt pluralform.

### Mekanisk växling på elektroniska cyklar
- Sökning på "mekanisk" gav **0 träffar** i alla 49 texter. Ingen text påstår mekanisk växling på en cykel med elektronisk växling (Di2/eTap/AXS).
- 7109, 7110 och 7134 anger uttryckligen "elektronisk växling". Elcykeln Engwe E26 (9016) anger "7 växlar med Shimano" utan att kalla den mekanisk eller elektronisk.

## Begränsningar
- Jämförelsen mot skrivfilen är fullständig (49 av 49), men språkgranskningen är en manuell läsning av en enda granskare (jag), inte ett skript, och kan ha missat enstaka fel. Jag läste texterna ur skrivfilerna, som är tecken för tecken lika med live.
- Fakta (specifikationer, ramstorlekar, komponenter) har inte kontrollerats mot tillverkarens källor; det ingick inte i uppdraget. Påståendet om 7038 (eTap/AXS) är därför en inkonsekvens i texten, inte en verifierad felaktighet.
- Hela standardblocket "Leverans, retur och garanti" jämfördes tecken för tecken men lästes inte språkligt i varje produkt (identiskt block enligt jämförelsen mot kanoniska skrivfilen, ej separat kontrollerat mot b_skriv_24.json).
- Inga ändringar gjorda, varken i Shopify eller i texter. Alla fynd ovan är förslag som kräver beslut.
