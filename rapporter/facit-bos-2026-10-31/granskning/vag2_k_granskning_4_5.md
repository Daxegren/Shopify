# Granskning våg 2, cyklar k_4–k_5 – BEST OF SPORTS (2026-11-03)

Oberoende granskning, bara läsning. Inget ändrat i Shopify, inga utkastfiler ändrade, inget committat. Butiken bekräftad med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK).

**Underlag:** `vag2_skriv/k_4_utkast.json` (22 poster, 6076–6100) och `k_5_utkast.json` (22 poster, 6101–6125), avvisade-filerna k_4/k_5 (6 poster), standarden avsnitt 1–12, `LARDOMAR.md`, granskarprompten och uppdragets extra regler för cyklar.

**Metod**
- **Live-källa:** title, status, productType, tags, descriptionHtml, seo och variants (title, sku, price) hämtade med graphql_query (`nodes`) i fyra batchar för alla 44 utkast och för 6122. Alla 44 är ACTIVE; seo är tomt på alla. `fakta` stämmer med live-källan.
- **Maskinellt:** titel ≤70 tecken och ≤2 kommatecken, SEO ≤43, meta 130–155, inga FAQ-avsnitt, standardblocket (exakt som c_1, eller med meningen "Beställningsvaror kan ta upp till en vecka längre." på exakt de 7 produkter som har taggen På beställning: 6078, 6079, 6080, 6083, 6086, 6089, 6123; samma mening som i a_*/b_*-filerna). Dubbletter av titel, SEO-titel och meta mot varandra och mot alla k_*, b_*, c_*, a_*-utkast, b_skriv*.json, c_skriv_resten_*.json och a_skriv.json: **inga dubbletter**. Alla rättningar har kontrollerats så att "före"-texten finns exakt en gång.
- **För hand:** varje uppgift (växlar, ram, broms, hjul, däck, vikt, ramstorlek, utrustning) jämförd mot live-texten och varianterna; cykeltyp mot productType och taggar; färg och färgöversättning; språk.

## Resultat

| Dom | Antal | Nr |
|---|---|---|
| GODKÄND | 33 | övriga |
| RÄTTA | 9 | 6080, 6086, 6089, 6100, 6103, 6111, 6119, 6124, 6125 |
| UNDERKÄND | 2 | 6079, 6083 |

**Avvisade (6):** 6081 (ARCHIVED), 6084 och 6085 (ungdomscykel), 6117 och 6118 (barncykel), 6122 (dubblett av 6121, live bekräftad: samma titel, text och pris 6 969 kr). Alla rätt avvisade, inget "kan släppas". Status för 6081 har inte hämtats om.

**Extra regler:** inga elcyklar, barncyklar, lastcyklar eller lösa delar bland utkasten. Ramstorlek låses aldrig i titel eller SEO (bara som lista av varianter i specifikationen på 6080, 6087, 6095, 6096). Vikt bara på produkter med en enda variant. Inga komfort-, säkerhets- eller kvalitetslöften kvar efter rättning (punkteringsskydd struket på 6080). Korg, pakethållare och belysning nämns som utrustning utan lastgräns. Ursprung (PL, "tillverkad i Polen") och märkeshistorik är strukna överallt. Färgnamn: svenska färger rätt översatta (turkos-guld, grafit, silvergrå, mörkgrå, champagne, "sinine" = blå); Livs egna färgnamn (Ocean Wave, Purple Ash, Golden Wheat, Tyrian Purple) står kvar som namn.

## Per produkt

| Nr | Id | Dom | Skäl / före → efter |
|---|---|---|---|
| 6076 | 10472261845258 | GODKÄND | Alla uppgifter spårbara (ALUXX, SF22-X1 100 mm slaglängd, Alivio/Deore, BR-MT200, Kenda 29x2.4). 'Mugghållare' står så i källan (troligen flaskhållare). |
| 6077 | 10472261910794 | GODKÄND | Hjulstorlek (titel 27.5", däck 29x2.2") och bromsskivor rätt utelämnade. Färg: titeln Purple Ash, texten Metallic Black; titelns färg används. Öppen fråga. |
| 6078 | 10460947120394 | GODKÄND | Gaffelns 100 mm (styrrör) rätt utelämnad; enda varianten 'S / gold' låses inte. |
| 6079 | 10488246796554 | UNDERKÄND | UNDERKÄND. Varianterna motsäger titeln: 'Default Title' 26 209 kr och 'S / white' 22 789 kr har samma SKU (1017035184), och variantfärgen vit stämmer inte med titelns Lavender Blush. Färgen kan då varken låsas i titel och SEO (regel 5) eller utelämnas (regel 3). Taggen säger Racercykel, texten damcykel. Behöver rättade varianter från leverantören innan text skrivs. |
| 6080 | 10471302660362 | RÄTTA | Typen Damcykel följer produkttypen Damcyklar (taggen säger Gravelcykel). 'Punkteringsskydd' är en skyddsegenskap från tillverkaren och stryks enligt regeln om inga skydds- och kvalitetslöften. Punkten i Passar för var otymplig; fästena står redan i specifikationen. Ramstorlekarna XS, S och M motsvarar varianterna (beskrivningen listar även L). **html 1:** före "<li>Däck: Giant CrossCut 700 x 42c, med punkteringsskydd</li>" → efter "<li>Däck: Giant CrossCut 700 x 42c</li>". **html 2:** före "<li>Dig som vill montera pakethållare eller stänkskärmar, för det finns fästen för båda</li>" → efter "<li>Dig som vill montera pakethållare eller stänkskärmar</li>". |
| 6082 | 10476230541578 | GODKÄND | Godkänd under förutsättning att 6083 inte skrivs med samma titel (se 6083). |
| 6083 | 10476252692746 | UNDERKÄND | UNDERKÄND. Möjlig dubblett av 6082 (10476230541578): samma titel 'Women's bike LIV Tempt 3. 29" Tyrian Purple', samma källtext och samma pris 11 919 kr; skillnaden är SKU (1101019185/-187 mot 1101019184), varianterna M och L mot Default Title och taggen På beställning. Utkastet gör titeln unik genom att lägga 'M och L' i titeln ('Tempt 3 M och L'), vilket läses som ett modellnamn och låser storlekarna. Samma hantering som 6122 (avvisad dublett): David avgör vilken produkt som ska finnas kvar. |
| 6086 | 10472332329226 | RÄTTA | Omständlig formulering kortas. Korg, pakethållare och belysning står i källan och nämns utan lastgräns (godtaget). Antal växlar (7/5/7) och 'wheel weight' rätt utelämnade. Varianter Default Title 10 239 kr och 'L / sinine' 9 509 kr (sinine = blå på estniska, så färgen stämmer). **html 1:** före "<li>Dig som söker en cykel för stadsmiljö, eftersom tillverkaren beskriver modellen som designad för stadslivet</li>" → efter "<li>Dig som söker en cykel för stadsmiljö, enligt tillverkaren</li>". |
| 6087 | 10656692142346 | GODKÄND | Ramstorlekarna M och L motsvarar båda varianterna (samma pris). Korg och belysning nämns utan lastgräns. |
| 6088 | 10523488256266 | GODKÄND | Stämmer mot live-källan. |
| 6089 | 10471179649290 | RÄTTA | Samma rättning som 6086. Ramens material saknas i källan (tom rad) och är rätt utelämnat. Varianter Default Title och 'M / beige' har samma SKU men olika pris. **html 1:** före "<li>Dig som söker en cykel för stadsmiljö, eftersom tillverkaren beskriver modellen som designad för stadslivet</li>" → efter "<li>Dig som söker en cykel för stadsmiljö, enligt tillverkaren</li>". |
| 6090 | 10472332984586 | GODKÄND | Stämmer mot live-källan. |
| 6091 | 10523488354570 | GODKÄND | Stämmer mot live-källan. |
| 6092 | 10460950626570 | GODKÄND | Stämmer mot live-källan. |
| 6093 | 10494944182538 | GODKÄND | Stämmer mot live-källan. |
| 6094 | 10526100291850 | GODKÄND | Stämmer mot live-källan. |
| 6095 | 10526100390154 | GODKÄND | Källtexten nämner 'hybridcykeln Gazela 4' och bara storlek L; modellnamn enligt titeln, vikt rätt utelämnad. Öppen fråga. |
| 6096 | 10526100455690 | GODKÄND | Som 6095. |
| 6097 | 10486668296458 | GODKÄND | Stämmer mot live-källan. |
| 6098 | 10472332525834 | GODKÄND | Stämmer mot live-källan. |
| 6099 | 10507443208458 | GODKÄND | Stämmer mot live-källan. |
| 6100 | 10588447605002 | RÄTTA | Källan säger 'fjädring fram', inte 'fjädrande framgaffel'. Metan skrivs som texten och specifikationen (151 tecken). **meta:** före "Hybridcykel Romet Orkan 1 M i svart och rött har aluminiumram, fjädrande framgaffel, 21 växlar från Shimano Acera och däck i 700 x 45C." → efter "Hybridcykel Romet Orkan 1 M i svart och rött har aluminiumram, fjädring fram, 21 växlar från Shimano Acera, mekaniska skivbromsar och däck i 700 x 45C.". |
| 6101 | 10472333738250 | GODKÄND | Varianter med olika SKU och pris (8 959/7 789 kr); vikt rätt utelämnad. |
| 6102 | 10507442815242 | GODKÄND | Stämmer mot live-källan. |
| 6103 | 10523487994122 | RÄTTA | Metan slutade 'har fästpunkter.' utan att säga för vad. Ny meta 147 tecken. **meta:** före "Cykel Romet Orkan 1.0 M i svart och silver har aluminiumram, 14 växlar med Shimano Tourney och V-bromsar. Cykeln väger 14,6 kg och har fästpunkter." → efter "Cykel Romet Orkan 1.0 M i svart och silver väger 14,6 kg och har aluminiumram, 14 växlar från Shimano Tourney, V-bromsar och fästpunkter för tillbehör.". |
| 6104 | 10472236777738 | GODKÄND | Stämmer mot live-källan. |
| 6105 | 10472334328074 | GODKÄND | Varianter med samma SKU och olika pris (9 579/8 329 kr); vikt rätt utelämnad. |
| 6106 | 10526097834250 | GODKÄND | Stämmer mot live-källan. |
| 6107 | 10507233493258 | GODKÄND | Stämmer mot live-källan. |
| 6108 | 10523487895818 | GODKÄND | Stämmer mot live-källan. |
| 6109 | 10523488125194 | GODKÄND | Stämmer mot live-källan. |
| 6110 | 10523487764746 | GODKÄND | Stämmer mot live-källan. |
| 6111 | 10471111622922 | RÄTTA | Källan anger bara 'Gaffel: Suntour NEX RL 63mm', inte att den är fjädrande. Texten säger redan 'Suntour-gaffel'; metan rättas till samma (141 tecken). **meta:** före "Damcykel Romet Orkan 7 D i mörkgrått är en hybridcykel med aluminiumram, Suntour-fjädergaffel, 30 växlar med Shimano Deore och hydrauliska bromsar." → efter "Damcykel Romet Orkan 7 D i mörkgrått är en hybridcykel med aluminiumram, Suntour-gaffel, 30 växlar med Shimano Deore och hydrauliska bromsar.". |
| 6112 | 10472333508874 | GODKÄND | Stämmer mot live-källan. |
| 6113 | 10526097735946 | GODKÄND | Varianter Default Title 6 799 kr och 'L / purple' 5 909 kr, samma SKU; ramstorlek och vikt rätt utelämnade. |
| 6114 | 10526097899786 | GODKÄND | Stämmer mot live-källan. |
| 6115 | 10656692175114 | GODKÄND | Stämmer mot live-källan. |
| 6116 | 10486812442890 | GODKÄND | Stämmer mot live-källan. |
| 6119 | 10468709138698 | RÄTTA | Komma saknades före hjulstorleken (samma mönster som övriga titlar). 2 kommatecken, 47 tecken. **titel:** före "Cykel Romet Rambler R7.0 27,5 tum, Grå och Röd" → efter "Cykel Romet Rambler R7.0, 27,5 tum, Grå och Röd". |
| 6120 | 10656692371722 | GODKÄND | Stämmer mot live-källan. |
| 6121 | 10523488157962 | GODKÄND | Möjlig dubblett 6122 (10635810144522) är rätt avvisad; live samma titel, text och pris, SKU 28182516-B mot 28202517-B. |
| 6123 | 10472435122442 | GODKÄND | Stämmer mot live-källan. |
| 6124 | 10472335900938 | RÄTTA | SEO-titeln saknade komma före färgen ('1.0 M Grön'). Med komma blir den 44 tecken, därför typordet 'Cykel' (butikens produkttyp Cyklar) i SEO-titeln; 39 tecken och unik i alla filer. **seo_title:** före "Stadscykel Romet Vintage Classic 1.0 M Grön" → efter "Cykel Romet Vintage Classic 1.0 M, Grön". |
| 6125 | 10472332427530 | RÄTTA | 'Parkeringsbroms' på en cykel med V-bromsar ser ut som en felöversättning (troligen stöd) och stryks. Källtexten nämner 'Vintage Classic 1.0 D' trots titeln 2.0 D; Nexus 7 och 7 växlar skiljer sig från 1.0 D (Tourney, 6 växlar) och följs. **html 1:** före "<li>Ingår: Kedjeskydd, stänkskärmar, bakre stänkskydd, parkeringsbroms samt fram- och bakljus</li>" → efter "<li>Ingår: Kedjeskydd, stänkskärmar, bakre stänkskydd samt fram- och bakljus</li>". |

## Öppna frågor till David (butiksdata som ser fel ut)
1. **Möjliga dubbletter:** 6082/6083 (Liv Tempt 3 Tyrian Purple, samma titel och text, SKU 1101019184 mot 1101019185/-187) och 6121/6122 (Romet Vintage Classic 1.0 D grön, SKU 28202517-B mot 28182516-B). Vilken ska finnas kvar, eller är det olika årsmodeller?
2. **Varianter med samma SKU men olika pris:** 6079 (26 209/22 789 kr, dessutom vit mot Lavender Blush), 6089 (8 179/7 719 kr), 6105 (9 579/8 329 kr), 6113 (6 799/5 909 kr). Varianter med olika SKU och pris: 6086 (10 239/9 509 kr), 6101 (8 959/7 789 kr). "Default Title" bredvid en namngiven variant tyder på att leverantörsdata blandats.
3. **Titel mot däck/text:** 6077 titel 27.5" men däck 29x2.2" och texten säger Metallic Black; 6076 titeln "Tempt 29 2 GE"; 6095/6096 texten nämner "Gazela 4" och bara storlek L; 6125 texten nämner "Vintage Classic 1.0 D".
4. **Ramstorlek mot varianter:** 6080 (varianter XS–M, text XS–L), 6078 (variant S, text S–L), 6087 (variant-SKU 2821OEM207-A och 2820OEM171-A, kan vara olika årsmodeller).
5. **Cykeltyp för Romet Orkan 1.0 M, 2 M, 4 M Lite och Rambler R7.0:** källan anger ingen typ, så titeln börjar med "Cykel" och första meningen blir svag ("är en cykel med …"). Vill du att Orkan-modellerna får "Hybridcykel" (som Orkan 1 M, 7 M och M) om leverantören bekräftar?
6. **Trasig leverantörstext** på Art Deco Lux/Classic ("front helmet", "Nex Nex Nexus", "hjulvikt 16,5 kg", tom rad för ram) och Orkan 1 M ("Aluminiumramen med framskärm", "Stötdämpare: 13,5 mm, 5,5 mm"). Våra texter utelämnar det, men källan i butiken är fel.
