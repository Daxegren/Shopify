# Granskningsutlåtande k_16a

Datum: 2026-11-05. Granskare: Opus. Granskningen gjordes bara genom läsning, och ingenting skrevs i Shopify. Butiken bekräftades som BEST OF SPORTS (6f2e53-67.myshopify.com). Källtext, varianter, SKU (artikelnummer), priser och syskonprodukter hämtades live via `shopify_api`.
Utkastfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_16a_utkast.json` (9 cyklar). Maskinläsbart utlåtande: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_16a.json`.
Förutsättningar: regler v1.5–v1.7. Elektronisk växling får skrivas när källan anger modellen ordagrant. En överbliven Default Title med samma SKU ignoreras (R3). Faktakoll på nätet är tillåten mot alla webbplatser.

## Resultat

| nr | id | Produkt | Dom |
|---|---|---|---|
| 7003 | 10468733223178 | Giant TCR Advanced Pro 0 Di2 | GODKÄND |
| 7004 | 10468733321482 | Giant TCR Advanced SL 1, Blue Dragonfly | GODKÄND |
| 7033 | 10472249032970 | Liv EnviLiv Advanced SL LTD, Blanc | GODKÄND |
| 7038 | 10472255488266 | Giant TCR Advanced Pro 1-AXS, Carbon | GODKÄND |
| 7039 | 10472259322122 | Giant TCR Advanced SL 0 Disc, Raw Carbon | RÄTTA (1) |
| 7040 | 10472276492554 | Giant TCR Advanced SL 0 DA | GODKÄND |
| 7041 | 10472282587402 | Kona Process 134 CR/DL G3, 29 tum | RÄTTA (1) |
| 6061 | 10472290124042 | Giant TCR Advanced 1 PC, Mars Dust | GODKÄND |
| 7044 | 10472293171466 | Liv Pique Advanced 29 1, Raw Carbon | RÄTTA (1) |

Totalt: 6 godkända, 3 att rätta och 0 underkända. `skrivfil_kontroll.py` på en kopia av utkastet gav 0 fel och 0 varningar. Ingen av de nio är en dubblett (R12a). Ingen produkt med samma modell och färg har taggen texter-klara.

## Rättningar (varje "före" förekommer exakt en gång i fältet html)

**7039 (R2).** Källans gaffelrad har fått "integrerad sadelstolpe" kopierat från ramraden. En gaffel har ingen sadelstolpe.
- Före: `<li>Gaffel: Advanced SL-Grade Composite, integrerad sadelstolpe, skivbroms</li>`
- Efter: `<li>Gaffel: Advanced SL-Grade Composite, skivbroms</li>`

**7041 och 7044 (R1).** Källorna säger bara att bromsarna är hydrauliska ("SRAM G2 RSC hydrauliska" och "Shimano XT, hydrauliska"). Ordet "skiv" finns inte i någon av de två källorna.
- Före: `<li>Dig som vill ha hydrauliska skivbromsar</li>`
- Efter: `<li>Dig som vill ha hydrauliska bromsar</li>`

## Fokuspunkter

- **Modellnamn ordagrant.** Alla modellnamn står i live-titeln. De flesta står också i källtexten eller i tillverkarlänken i källan. Pro 1-AXS (7038) står bara i titeln. Källtexten säger där "TCR Advanced", och det stämmer med titeln.
- **7004, Pro 0 eller SL 1.** Inledningen i källan är en ordagrann kopia av inledningen till 7003 (Pro 0). Ram, gaffel och tillverkarlänken (`giant-bicycles.com/gb/tcr-advanced-sl-1-2025`) anger SL 1. Webbkoll på den adressen bekräftar SL 1 2025 med SL-ram, integrerad sadelstolpe, Ultegra Di2, Giant Power Pro, SLR 0 40-hjul och CADEX Race GC 700x28. Utkastet utelämnar inledningen och följer SL 1. Det är rätt enligt R2 och v1.6.
- **7039, 22 växlar.** Utelämnandet är rätt. Källan anger Dura-Ace Di2 ST-R9250, som är en växelgrupp med 2x12 växlar, alltså 24. Länken gäller 2023 års modell med 12-växlad Dura-Ace. Uppgiften "22 växlar" motsäger modellen och utelämnas enligt R2.
- **7041, R3. Produkten får skrivas.** Default Title (B36134CD06, 107 459 kr) har samma SKU som XL / gray. Det är alltså en överbliven Default Title enligt v1.7, och den ignoreras. Kvar finns M, L och XL. De har olika SKU men samma pris (93 439 kr) och samma färg. Olika SKU är här vanliga storleksvarianter. Det är inte det fall som v1.7 avvisar, nämligen en Default Title med egen SKU. Den ursprungliga R3 avvisar bara när titeln anger en variant och varianterna har olika pris. Titeln anger varken storlek eller färg. Live-titelns "Satin Metallic Charcoal (Purple)" står inte med, och varianterna säger "gray". "29 tum" gäller alla storlekar som säljs: bakhjulet på 27,5 tum gäller bara storlek S, som inte säljs. Storlekarna M, L och XL i texten stämmer med källan (R3 v1.5).
- **7044, landsväg och cyklocross mot mountainbike.** Inledningen i källan kallar cykeln landsvägscykel och cyklocrosscykel. Taggen Mountainbike, live-titeln och specifikationerna visar entydigt en heldämpad mountainbike: Fox 34-gaffel med 120 mm slaglängd, Fox Float-bakdämpare, 115 mm FlexPoint Pro och Maxxis Aspen 29x2.4. Utkastet utelämnar inledningen men behåller den entydiga uppgiften att Liv är "designat för kvinnor" (R2). Det är rätt.
- **Priser, färger och storlekar som inte säljs.** Ingen titel, SEO-titel eller meta innehåller ett pris. På 7003, 7040 och 7041 med överbliven Default Title är färgen borttagen från titeln. Där en färg står kvar (7004, 7033, 7038, 7039, 6061, 7044) har produkten antingen bara en variant eller samma färg på alla varianter. Storlekar nämns bara där de säljs som varianter (7041 M–XL, 6061 M–XL, 7044 S).
- **6061, däckraden "700x25c (28 mm)".** Raden ser motsägelsefull ut, men webbkoll på tillverkarlänken visar att den är Giants egen formulering: "700x25c (28mm)". Modellnamnet 1 PC och färgen Mars Dust bekräftas också där.
- **Elektronisk växling (v1.7).** Di2, eTap AXS och AXS T-Type återges bara som modellnamn. Ingen text påstår mekanisk växling eller nämner batteri.

## Anmärkningar utan rättning

- För 7033 och 7038 står det "Di2" i fältet att_bekrafta, men växlingen är SRAM eTap AXS respektive SRAM AXS. Det är kopierad text. Kundtexten är korrekt.
- Lagersaldot är 0 på alla varianter utom 6061 (M, M/L och L har 1 var). Default Title på 7003, 7040 och 7041 kostar 11 640–20 680 kr mer än de verkliga varianterna. Textutrullningen ändrar inte priser eller varianter. Det här är en iakttagelse för David.
