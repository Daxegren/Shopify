# Granskning våg 2, cyklar k_10–k_12 – BEST OF SPORTS (2026-11-03)

Oberoende granskning, bara läsning. Inget ändrat i Shopify, inga utkastfiler ändrade, inget committat. Butiken bekräftad med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK).

**Underlag:** `vag2_skriv/k_10_utkast.json` (11 poster), `k_11_utkast.json` (10), `k_12_utkast.json` (10), avvisade-filerna k_10–k_12 (45 poster), standarden avsnitt 1–13, `LARDOMAR.md`, granskarprompten, specialreglerna för cyklar i `k_utkastprompt.md`, `k_utlatande_4_5.json` och uppdragets extra skärpa.

**Metod**
- **Live-källa:** title, status, productType, vendor, tags, descriptionHtml, seo och variants (title, sku, price) hämtade med graphql_query (`nodes`) i fyra batchar för alla 31. Alla är ACTIVE och har tomt seo.
- **Maskinellt:** titel ≤70 tecken och ≤2 kommatecken (decimalkomma som i 6119), SEO ≤43, meta 130–155 eller null (7030), standardblocket exakt som c_1 med meningen om beställningsvaror på de 30 produkter som har taggen På beställning och utan den på 7066 (saknar taggen). Dubbletter av titel, SEO-titel och meta, även efter rättning, mot alla a_*, b_*, c_*, k_* utkast- och skrivfiler (1 485 poster): inga. Varje "före" förekommer exakt en gång i sitt fält.
- **För hand:** varje uppgift (växelsystem, antal växlar, bromstyp, hjul- och ramstorlek, däck, gaffel, ram) mot den egna produktens källa, cykeltyp mot titel, produkttyp och taggar, färgnamn mot titel och varianter.

**Extra skärpa som tillämpats**
1. *Elektronisk växling:* SRAM Apex, Apex XPLR och GX Eagle utan angivelse samt Shimano 105 med 24 växlar (12-växlad 105 finns som Di2) → UNDERKÄND. Godkända: Shimano 105 med 22 växlar (11-växlad 105 finns bara mekanisk), SRAM SX Eagle (finns bara mekanisk), Shimano Cues (Di2 bara för elcyklar, ingen motor här), Deore, SLX, XT RD-M8100.
2. Hjulstorlek, ramstorlek, bromstyp och växlar kontrollerade mot den egna källan (inte systerprodukter). Ramstorlek låses aldrig; hjulstorlek utelämnad där den beror på ramstorlek (7013, 7015) eller motsäger sig (7060).
3. Typ: Mountainbike, Damcykel, Herrcykel, Hybridcykel, Fixiecykel och Landsvägscykel stöds av titel eller taggar; 7027 (Road bike/fitnesscykel/Gravel) är dessutom oklar.
4. Färg: Livs och Giants färgnamn behålls; översatt bara Kolgrå, Asfaltsgrön, Metallsvart, Svart, Mörkgrå.
5. Meningen om längre leveranstid finns bara på produkter med taggen På beställning.

## Resultat

| Dom | Antal | Nr |
|---|---|---|
| GODKÄND | 17 | övriga |
| RÄTTA | 5 | 7025, 7032, 7050, 7060, 7071 |
| UNDERKÄND | 9 | 7022, 7027, 7028, 7048, 7056, 7058, 7066, 7067, 7068 |

**Avvisade (45):** elcyklar och el-lastcyklar, barn- och ungdomscyklar, Di2/AXS/eTap/Transmission, GRX RX-820 (7052), ARCHIVED (7054) och dubbletter (7023, 7051, 7053). Alla rätt avvisade, inget "kan släppas".

## Per produkt

| Nr | Id | Dom | Skäl / före → efter |
|---|---|---|---|
| 7005 | 10468767170826 | GODKÄND | Alla uppgifter spårbara (ALUXX, RockShox Paragon Gold RL 50 mm slaglängd, Shimano Cues 11 växlar, hydrauliska skivbromsar, CrossCut 700x42c). Hjulstorlek i tum rätt utelämnad; titeln bär antal växlar i stället. Kolgrå för Charcoal är rimlig översättning (varianten säger dark gray). Shimano Cues: Di2-versionen finns bara för elcyklar och cykeln har ingen motor, så växlingen bedöms som mekanisk. Dubbletten 7023 rätt avvisad. |
| 7006 | 10468767891722 | GODKÄND | Typen Mountainbike stöds av taggen (produkttyp Damcyklar). Deore 12 växlar, BR-MT200 hydrauliska, Maxxis Recon Race 29x2.4 och 29 tum står i källan. Gaffelns 100 mm rätt utelämnad. Asfaltsgrön för Asphalt Green godtas (samma form som i promptens exempel); varianterna säger gray. |
| 7007 | 10468768121098 | GODKÄND | Cues 10 växlar, Tektro HDC TKD 149 hydrauliska, 29x2.4 stämmer. Black Diamond behålls som originalnamn. |
| 7010 | 10468773691658 | GODKÄND | Typen Mountainbike stöds av titeln och taggen (källtexten säger road bike/cyclocross men har Fox 34-gaffel och bakdämpare). Deore XT RD-M8100 är mekanisk. Default Title 71 629 kr mot S/M/L gold 62 279 kr; färg och storlek låses inte. Öppen fråga om källtexten. |
| 7011 | 10468774576394 | GODKÄND | Komposit, Recon Silver RL, SLX 12 växlar, BR-MT500, 29x2.25 stämmer. Default Title 39 309 kr mot M/L/XL white 34 179 kr; storlek låses inte. 'Svart och Shell White' behåller Giants färgnamn. |
| 7012 | 10468774674698 | GODKÄND | 140 mm bak och 150 mm fram, Fox 36 Float Rhythm, Deore 12, BR-MT420, däck 29x2.5/29x2.4 stämmer. Metallsvart för Metallic Black godtas. Default Title 55 199 kr mot L/XL 47 999 kr. |
| 7013 | 10468774969610 | GODKÄND | Hjulstorlek rätt utelämnad i titeln (bakhjulet 27,5 eller 29 tum beroende på ramstorlek). Fox 36 150 mm, Deore 12, BR-MT420 stämmer. Varianter Default Title 55 199 kr och M/purple 55 099 kr, samma SKU. |
| 7014 | 10468775821578 | GODKÄND | En variant. SLX-reglage, 12 växlar, BR-MT520, Fox 36 Float Performance, däck 29x2.5/29x2.4 stämmer. Smoke Metal behålls. |
| 7015 | 10470896402698 | GODKÄND | SRAM SX Eagle finns bara som mekanisk grupp (ingen AXS-version), och nivån SX anges uttryckligen, så regeln om Eagle utan angivelse träffar inte. Antal växlar rätt utelämnat (står inte i källan). RockShox 35 Gold RL 160 mm, Tektro M745 hydrauliska skivbromsar, bakhjul per ramstorlek stämmer. En variant. Lyft till David om han vill tolka Eagle-regeln strängare. |
| 7022 | 10471017414922 | UNDERKÄND | UNDERKÄND. Källan anger två alternativa växelsystem ('Microshift Advent X eller Shimano Deore 11spd') och två bromsalternativ ('SRAM DB8 eller Shimano Deore hydrauliska'). Advent X är en 10-växlad grupp, så '11 växlar' i meta, intro och Passar för är inte entydigt, och bromstypen är inte entydig för båda alternativen. Växlar och bromsar måste stå entydigt i den egna källan. Rammaterial och slaglängd i övrigt stämmer. Fråga leverantören vilken utrustning som levereras. |
| 7024 | 10471092257034 | GODKÄND | Herrcykel stöds av titeln och taggen (källtexten säger mountainbike). Cues 18 växlar, BL-MT200/BR-M200 hydrauliska, Schwalbe Rapid 29x2.25 och 29-tumshjul stämmer. Tre varianter med samma pris; storlek låses inte. Vendor 'Men's' är fel i butiken (öppen fråga). |
| 7025 | 10471123321098 | RÄTTA | Språkfel i metan ('29 tum hjul'); texten skriver redan '29-tumshjul'. 141 tecken efter rättning. Fakta stämmer: komposit, 160 mm Maestro, Fox 38 170 mm, SLX RD-M7100 12 växlar (mekanisk), BR-MT520. Sangria/Carbon mot varianterna Red: originalnamnet behålls. Default Title 79 679 kr mot L/XL 69 289 kr. **meta:** före "med 29 tum hjul" → efter "med 29-tumshjul". |
| 7027 | 10471335461130 | UNDERKÄND | UNDERKÄND. Växelsystem 'SRAM Apex' utan angivelse: Apex finns både mekanisk och som Apex AXS (elektronisk, batteri), och källan visar inte att den är mekanisk. Dessutom oklar typ: originaltiteln säger Road bike, texten fitnesscykel, taggarna Gravelcykel och Racercykel (utkastet skriver neutralt 'Cykel'). |
| 7028 | 10471336116490 | UNDERKÄND | UNDERKÄND. 'SRAM Apex' för både växlar och bromsar utan angivelse om mekanisk eller AXS (elektronisk med batteri). Källan visar inte entydigt mekanisk växling. Källans länk pekar dessutom på FastRoad AR Advanced 1, inte TCX. |
| 7029 | 10471354859786 | GODKÄND | En variant. Komposit, 100 mm FlexPoint Pro, RockShox Sid 110 mm med fjärrlåsning, Deore 12, MT410 hydrauliska, Aspen 29x2.4 stämmer. Sea Sparkle behålls. |
| 7030 | 10472237072650 | GODKÄND | Tunn källa; utkastet skriver bara typ (Fixiecykel enligt originaltiteln) och Kenda 700x26c, ingen meta. Färg, ramstorlek och vikt rätt utelämnade (varianterna green/hõbe, M/L/XL och olika pris). Inga påståenden om bromsar eller växlar. |
| 7032 | 10472248934666 | RÄTTA | Komma saknas före hjulstorleken i titel och SEO-titel (samma rättning som 6119). Titel 48 tecken, SEO 35, unika. Mountainbike stöds av taggen och källtexten ('en stilren mountainbike'), originaltiteln säger Damcykel. 27,5 tum står i originaltiteln och däcket Kenda Booster 27.5. Deore M5100/M4100 mekanisk, BR-MT200 hydrauliska. Gaffelns 80/100 mm rätt utelämnad. Källans länk pekar på Tempt 2 2022 (öppen fråga). **titel:** före "Liv Tempt 1 GE 27,5 tum" → efter "Liv Tempt 1 GE, 27,5 tum". **seo_title:** före "Liv Tempt 1 GE 27,5 tum" → efter "Liv Tempt 1 GE, 27,5 tum". |
| 7043 | 10472291369226 | GODKÄND | Mountainbike stöds av taggen. ALUXX SLR, Crest 34 RRL 100 mm fjärrlåsning, Deore M6100 12 växlar, BR-MT200 hydrauliska, Recon Race 29x2.4 och 29-tumshjul stämmer. Dark Jade behålls; varianten M/sinine (blå) 18 709 kr mot Default Title 21 519 kr (öppen fråga om färgen). |
| 7045 | 10472297070858 | GODKÄND | En variant. Reynolds 520 Cromoly, 1 växel, Tektro HD-M275 hydrauliska, däck 29x2.6 (två alternativ skrivs som i källan). Rolltexten (12 växlar, packning) rätt utelämnad. Brun står i titeln. |
| 7046 | 10472312930570 | GODKÄND | En variant. ALUXX SL, Fox 38 Performance Elite 170 mm, SLX RD-M7100 (mekanisk), Deore BR-M6120 hydrauliska, Contact Switch dropper 30,9 mm, Assegai 29x2.5/DHR II 29x2.4, 29 tum i titeln. Antal växlar rätt utelämnat. |
| 7048 | 10472322138378 | UNDERKÄND | UNDERKÄND. Shimano 105 med 24 växlar (2x12) finns både mekanisk och som 105 Di2 (elektronisk, batteri); källan säger bara 'Shimano 105'. Därutöver: modellåret 2025 står bara i en länk, däckbredden är motsägelsefull (25 mm, 700x25c, 28 mm) och utkastet själv flaggar möjlig dubblett med 6064/6065. Varianter Default Title 39 479 kr och XL/black 40 079 kr med samma SKU. |
| 7050 | 10472324169994 | RÄTTA | 'Lockout utan retur' är en ordagrann översättning av 'lockout without rebound' och blir obegriplig på svenska. Övrigt stämmer: Damcykel (produkttyp och tagg), Cues 20 växlar, Tektro TKD-143 hydrauliska, CrossCut 700x42c, punkteringsskydd rätt struket. En variant. **html:** före "lockout utan retur" → efter "med låsning". |
| 7056 | 10472351400202 | UNDERKÄND | UNDERKÄND. Växelsystem 'SRAM GX-Eagle' utan angivelse: GX Eagle finns både mekanisk och som GX Eagle AXS / Transmission (elektronisk, batteri). Dessutom är rammaterialet tomt i källan och bromsarna (SRAM G2 RS) anges utan bromstyp. |
| 7058 | 10472435056906 | UNDERKÄND | UNDERKÄND. Shimano 105 med 24 växlar (2x12) kan vara 105 Di2 (elektronisk, batteri); källan visar inte entydigt mekanisk. Dessutom typ 'Damcykel för landsväg' och varianterna pink mot titelns RosyBrown/OceanStorm med Default Title 42 989 kr och S/M 37 009 kr (samma SKU som S). |
| 7059 | 10472484700426 | GODKÄND | Shimano 105 med 22 växlar (2x11): 11-växlad 105 finns bara mekanisk (Di2 kom först med 12 växlar), så växlingen är entydigt mekanisk utifrån källans antal. Komposit, 105 hydrauliska, Gavia Fondo 1 700x32c stämmer. Bay Leaf behålls; Default Title 43 409 kr mot XL/green 37 739 kr, samma SKU. |
| 7060 | 10475423629578 | RÄTTA | Punkten var otymplig och 'stöd' är oklart (källan: 'ett praktiskt stöd'). 16 växlar, två fälgbromsar och aluminiumfälgar står i källan. Hjulstorleken rätt utelämnad (titel 28", text 17" fälgar). 'Del Rey' utelämnat, typ neutral 'Cykel'. Källtexten nämner 'Fixiede' (kopierad mall) och ursprung Kalifornien (struket). **html:** före "<li>Dig som vill kunna lägga till tillbehör som lampor, stöd eller korg, vilka kan väljas i butiken</li>" → efter "<li>Dig som vill komplettera cykeln med tillbehör, till exempel lampor eller korg</li>". |
| 7063 | 10476071321866 | GODKÄND | En variant. 29 tum fram och 27,5 tum bak står entydigt i källtexten, Fox 36 160 mm, 145 mm Maestro, Marzocchi Bomber Air, BR-MT420 fyrkolvs med 203/180 mm skivor, Deore 12 (mekanisk). Priset 24 579 kr ser lågt ut (öppen fråga, står inte i texten). |
| 7066 | 10476124012810 | UNDERKÄND | UNDERKÄND. Shimano 105 med 24 växlar (2x12) kan vara 105 Di2 (elektronisk, batteri); källan säger bara 'Shimano 105'. Systerprodukt till 7048 (samma modell). Standardblocket utan beställningsmening är rätt (ingen tagg På beställning). |
| 7067 | 10476126699786 | UNDERKÄND | UNDERKÄND. Bakväxel 'SRAM Apex XPLR' och 'SRAM Apex hydrauliska' utan angivelse: Apex XPLR finns både mekanisk och som AXS (elektronisk, batteri). Källan visar inte entydigt mekanisk. |
| 7068 | 10476128403722 | UNDERKÄND | UNDERKÄND. Samma som 7067: 'SRAM Apex XPLR' utan angivelse om mekanisk eller AXS. Utkastet har dessutom fyra punkter under Passar för (högst tre). |
| 7071 | 10476191285514 | RÄTTA | Samma rättning som 7050. Damcykel stöds av titeln, produkttypen och taggen. Paragon Gold RL 50 mm, Cues 11, BR-MT200 hydrauliska, CrossCut 700x42c, låg ram ('enligt tillverkaren') stämmer. Punkteringsskydd och märkeshistorik rätt strukna. En variant. **html:** före "lockout utan retur" → efter "med låsning". |

## Öppna frågor till David
1. **Växelsystem som kan vara elektroniska** (9 underkända, varav 7 bara av det skälet): ska leverantören bekräfta mekanisk eller AXS/Di2 för SRAM Apex (7027, 7028), Apex XPLR (7067, 7068), GX Eagle (7056) och Shimano 105 12-växlad (7048, 7058, 7066)? Vill du tolka regeln strängare även för SX Eagle (7015) och 105 11-växlad (7059), som är godkända här?
2. **Kona Process 153 (7022):** två alternativa växelsystem och bromsar i källan; vilket levereras?
3. **Butiksdata som ser fel ut:** vendor "Men's" på Romet Mustang (7024); färg Dark Jade mot variant "sinine" (7043); länk till Tempt 2 2022 på Tempt 1 GE (7032); länk till FastRoad på TCX (7028); priset 24 579 kr på Trance X SX (7063); "Default Title" bredvid namngivna varianter med annat pris på många Giant/Liv-produkter.
4. **Möjlig dubblett:** TCR Advanced 2 PC Carbon (7048) mot 6064/6065 enligt utkastaren.
