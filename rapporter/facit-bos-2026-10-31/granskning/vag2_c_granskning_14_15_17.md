# Granskning våg 2, utkast c_14, c_15 och c_17 – BEST OF SPORTS (2026-11-02)

Oberoende granskning. Jag har bara läst i Shopify och har inte ändrat någon utkastsfil. Butiken kontrollerades först med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK).

**Underlag:** `vag2_skriv/c_14_utkast.json` (11 poster), `c_15_utkast.json` (11) och `c_17_utkast.json` (12), alltså 34 utkast, samt avvisade-filerna (4 + 4 + 3). Standarden (`produkttexter-standard.md`, avsnitt 1–11), `LARDOMAR.md` och `granskning/vag2_a_granskning_2.md` som formatmall.

**Metod:**
- **Källan live:** title, handle, status, productType, vendor, tags, descriptionHtml, seo och variants hämtades med graphql_query (`nodes`) i tre batchar. Alla 34 är ACTIVE, vendor Gymstick, produkttyp tom (oförändrad i utkasten), seo.title och seo.description är null. `fakta` stämmer med live-källan. Live-texterna har ofta en extra avslutande säljmening som inte finns i `fakta`; den innehåller bara omdömen, så inget faktum försvinner.
- **Maskinellt:** längder (titel ≤70, SEO-titel ≤43, meta 130–155 eller null), antal kommatecken, standardblocket jämfört tecken för tecken med `c_1_utkast.json` (identiskt i alla 34), dubbletter av titel och SEO-titel mot alla `c_*_utkast.json` (inga i mina filer, inte heller för de föreslagna nya SEO-titlarna), och överlapp mot `handhavd_ids.txt` (inget). Kontrollskriptet kördes inte (granskaren ändrar inget och skapar inga kontrollfiler).
- **För hand:** varje titel, SEO-titel, meta och html lästes mot live-källan och språkgranskades.

## Resultat i korthet

| Kategori | Antal | Nr |
|---|---|---|
| GODKÄND | 14 | 3196, 3198, 3203, 3207, 3209, 3210, 3212, 3219, 3223, 3245, 3248, 3249, 3250, 3251 |
| RÄTTA | 13 | 3197, 3199, 3205, 3211, 3214, 3215, 3217, 3221, 3224, 3241, 3244, 3246, 3252 |
| UNDERKÄND | 7 | 3204, 3206, 3213, 3225, 3243, 3253, 3254 |

Totalt 14 + 13 + 7 = 34.

## Regelkontroll (alla utkast)
- Titlar 18–48 tecken, högst 1 kommatecken. SEO-titlar 18–43 tecken (3217 exakt 43). Meta 130–155 där den finns; null på 3204 och 3253 (tunn källa).
- Varianter med olika pris eller oförklarade namn är inte låsta: 3209 (4/8/12/16), 3206 (7 vikter), 3217 (Default/TELE), 3221 (XS–L), 3224 (S–L), 3241 (S/M, L/XL), 3249 (65/75). Live-titlarnas 'extra små', 'Large', 'L/XL', '12kg' och '65cm' förs rätt inte vidare.
- Inga priser, omdömen, ursprung eller miljöpåståenden ('miljövänligt' i 3223 och 3246 rätt utelämnat). Tillverkarpåståenden skrivs 'enligt tillverkaren'. Inga arbetstermer.
- Återkommande språkfel: 'en träningsutrustning' (3214, 3215, 3225), 'X är handskar' (3221, 3224) och engelsk plural 'minibands' (3252).

## Per produkt

| Nr | Id | Utkastets titel | Dom | Rättning (före → efter) eller skäl |
|---|---|---|---|---|
| 3196 | 10581110817034 | Handtag Gymstick Pulley Handles PR | GODKÄND |  |
| 3197 | 10581110882570 | Boxningstassar Gymstick Punching Mitts | RÄTTA | **html**: "<li>Dig som vill träna allmän fitness med tassar</li>" → "<li>Dig som vill använda tassar i allmän fitnessträning</li>"<br>Skäl: Språk: 'träna allmän fitness' är inte idiomatiskt. |
| 3198 | 10581110915338 | Armhävningshandtag Gymstick Push Up Bars | GODKÄND |  |
| 3199 | 10581110948106 | Träningsmattor Gymstick Puzzle Mat Set | RÄTTA | **meta**: "Gymstick Puzzle Mat Set är ett set träningsmattor med pusseldesign. Enligt tillverkaren har de en stötdämpande yta och går att lägga ut efter utrymmet." → "Gymstick Puzzle Mat Set är ett set träningsmattor med pusseldesign. Enligt tillverkaren har de en stötdämpande yta och kan anpassas efter utrymmet."<br>Skäl: Språk: 'går att lägga ut efter utrymmet' är oklart. Ny meta 147 tecken. |
| 3203 | 10581111144714 | Reaktionsboll Gymstick Reaction Ball, 7 cm | GODKÄND |  |
| 3204 | 10581111177482 | Isbadkar Gymstick RecoPod Ice Bath | UNDERKÄND | Isbadkar: kallbad har hälsorisker, och källan består bara av hälsopåståenden (muskelömhet, cirkulation, mental klarhet). Inga mått, volym, material eller bruksanvisning. Tas för hand med Davids ja. |
| 3205 | 10581111210250 | Massageboll Gymstick Recovery Twin Ball | RÄTTA | **html**: "<li>Material enligt tillverkaren: Slitstarkt material</li>" → "<li>Material: Slitstarkt, enligt tillverkaren</li>"<br>Skäl: Tautologi i specifikationen ('Slitstarkt material' som material); samma form som övriga utkast. |
| 3206 | 10581111243018 | Gummerad Viktskiva Gymstick | UNDERKÄND | Viktskivor är last. Sju varianter (1,25–25) med olika pris, hålets diameter (vilken stång de passar) saknas och det är oklart om priset gäller en skiva. Konsekvent med avvisade Z-Bar och Quick-Lock-hantlar. Om David släpper den: titel 'Viktskiva Gymstick, Gummerad' (typ först) och 'Material: Gummerad' → 'Yta: Gummerad'. |
| 3207 | 10581111275786 | Handtag Gymstick Single Handle | GODKÄND |  |
| 3209 | 10581111374090 | Träningsboll Gymstick Slam Ball | GODKÄND |  |
| 3210 | 10581111406858 | Träningskoner Gymstick Speed Discs, 20 st | GODKÄND |  |
| 3211 | 10581111439626 | Hopprep Gymstick Speed Rope | RÄTTA | **meta**: "Gymstick Speed Rope är ett hopprep. Enligt tillverkaren har det ergonomiskt handtag och justerbar längd och är designat för snabba rotationer." → "Gymstick Speed Rope är ett hopprep. Enligt tillverkaren har det ett ergonomiskt handtag och justerbar längd och är designat för snabba rotationer."<br>**html**: "har det ergonomiskt handtag" → "har det ett ergonomiskt handtag"<br>Skäl: Grammatik: obestämd artikel saknas. Meta blir 146 tecken. |
| 3212 | 10581111472394 | Hopprep Gymstick Speed Rope Pro | GODKÄND |  |
| 3213 | 10581111537930 | Tejp Gymstick Sports Tape, 2 Rullar | UNDERKÄND | Sporttejp: källan bygger på stöd, skydd av musklerna och att 'minimera risken för skador' (skydd/stöd med skadeförebyggande påståenden). Tejpens typ (kinesio eller stel) framgår inte. |
| 3214 | 10581111570698 | Pressboll Gymstick Squeeze Ball | RÄTTA | **titel**: "Pressboll Gymstick Squeeze Ball" → "Handträningsboll Gymstick Squeeze Ball"<br>**seo_title**: "Pressboll Gymstick Squeeze Ball" → "Handträningsboll Gymstick Squeeze Ball"<br>**meta**: "Gymstick Squeeze Ball är en träningsutrustning för grepp och handstyrka. Enligt tillverkaren är den gjord av slitstarkt material för långvarig användning." → "Gymstick Squeeze Ball är en boll för träning av grepp och handstyrka. Enligt tillverkaren är den gjord av slitstarkt material för långvarig användning."<br>**html**: "är en träningsutrustning för grepp och handstyrka. Enligt tillverkaren är den tillverkad av slitstarkt material." → "är en boll för träning av grepp och handstyrka. Enligt tillverkaren är den gjord av slitstarkt material."<br>Skäl: 'Pressboll' är inget etablerat svenskt typord; 'en träningsutrustning' är ogrammatiskt (oräknebart ord); 'tillverkaren ... tillverkad' upprepas. Typordet är ett språkval som David kan ändra (alternativ: Stressboll undviks eftersom det anknyter till källans hälsopåstående). Meta 151 tecken; SEO-titel = titel lagras tom. |
| 3215 | 10581111603466 | Balanskudde Gymstick Stability Air Pad | RÄTTA | **html**: "<p>Gymstick Stability Air Pad är en träningsutrustning för balans och bålstyrka, enligt tillverkaren. Den fungerar som träningsyta för balansövningar.</p>" → "<p>Gymstick Stability Air Pad är en balanskudde som enligt tillverkaren används för att träna balans och bålstyrka.</p>"<br>Skäl: 'En träningsutrustning' är ogrammatiskt, och andra meningen upprepar den första. |
| 3217 | 10581111701770 | Stretchingredskap Gymstick Stretching Stick | RÄTTA | **html**: "<p>Gymstick Stretching Stick är ett träningsredskap för stretchövningar. Enligt tillverkaren är det tillverkat för hållbarhet.</p>" → "<p>Gymstick Stretching Stick är ett träningsredskap som enligt tillverkaren används för djupgående stretchövningar.</p>"<br>Skäl: 'Enligt tillverkaren är det tillverkat' upprepar ordet och är ett kvalitetspåstående (källan: 'högkvalitativt material för att säkerställa hållbarhet'). Varianterna Default (149 kr) och TELE (269 kr) är rätt olåsta; skillnaden bör bekräftas av David. |
| 3219 | 10581111767306 | Tatamimatta Gymstick, 105 x 105 x 2 cm | GODKÄND |  |
| 3221 | 10581111931146 | Träningshandskar Gymstick, Svart-Grå | RÄTTA | **meta**: "Gymstick träningshandskar är handskar i svart-grå färg. Enligt tillverkaren är de designade för komfort under träningspass och förbättrar greppet." → "Träningshandskar från Gymstick i svart-grå färg, i storlekarna XS, S, M och L. Enligt tillverkaren är de designade för komfort och förbättrar greppet."<br>Skäl: Cirkulärt ('träningshandskar är handskar'). Storlekarna finns som varianter live med samma pris. Ny meta 150 tecken. Live-titeln 'extra små' är fel mot varianterna, rätt att den inte förs vidare. |
| 3223 | 10581111996682 | Träningsmatta Gymstick Training Mat Cork | GODKÄND |  |
| 3224 | 10581112029450 | Träningshandskar Gymstick, Rosa-Svart | RÄTTA | **meta**: "Gymstick träningshandskar är handskar i rosa-svart färg. Enligt tillverkaren är de designade för komfort och stöd under intensiva träningspass." → "Träningshandskar från Gymstick i rosa-svart färg, i storlekarna S, M och L. Enligt tillverkaren är de designade för komfort och stöd under träningspass."<br>Skäl: Cirkulärt ('träningshandskar är handskar'). Storlekarna S, M, L finns live med samma pris. Ny meta 152 tecken. |
| 3225 | 10581112160522 | Tricepsstång Gymstick Triceps Full Extension Bar | UNDERKÄND | Oklar produkttyp: källan säger inte om stången är ett kabelfäste eller en stång som lastas med vikter (möjlig last). 'Tricepsstång' är en tolkning; inga mått, material eller maxbelastning. Dessutom 'en träningsutrustning' (ogrammatiskt). |
| 3241 | 10581112783114 | Träningshandskar Gymstick Workout Gloves | RÄTTA | **meta**: "Gymstick Workout Gloves är träningshandskar som enligt tillverkaren ger bättre grepp och skyddar händerna under träningspass. Finns i S/M och L/XL." → "Gymstick Workout Gloves är träningshandskar som enligt tillverkaren ger bättre grepp och komfort under träningspass. Finns i storlekarna S/M och L/XL."<br>**html**: "ger bättre grepp och skyddar händerna under träningspass.</p>" → "ger bättre grepp och komfort under träningspass.</p>"<br>**html_2**: "<li>Dig som vill skydda händerna under träningspass, enligt tillverkaren</li> " → "(tas bort)"<br>Skäl: Skyddslöftet tas bort, i linje med 3221 och 3224 där skydd utelämnats (skydd/stöd-regeln). Ny meta 150 tecken. |
| 3243 | 10581112848650 | Handledsstöd Gymstick Wrist Support 1.0 | UNDERKÄND | Handledsstöd: skydd/stöd med skadeförebyggande påstående i källan ('minskar risken för skador', 'lyfta tyngre'). Samma bedömning som avvisade Tennis Elbow Support (c_15). Gäller också 3289 Handledsstöd 2.0 i c_20. |
| 3244 | 10581112881418 | Svettband för Handled Gymstick, 2 st | RÄTTA | **titel**: "Svettband för Handled Gymstick, 2 st" → "Svettband Gymstick för Handled, 2 st"<br>**seo_title**: "Svettband för Handled Gymstick, 2 st" → "Svettband Gymstick för Handled, 2 st"<br>Skäl: Ordningen Typ, Märke ska följas (jfr 'Träningshandskar Trec #24 för Dam'). 36 tecken. |
| 3245 | 10581112914186 | Yogablock Gymstick | GODKÄND | Godkänd. Notering: källan skriver 'Dessa block' (plural) medan titeln är singular; utkastet säger 'ett yogablock'. Antal bör bekräftas av David. |
| 3246 | 10581112946954 | Yogablock av Kork Gymstick | RÄTTA | **titel**: "Yogablock av Kork Gymstick" → "Yogablock Gymstick i Kork"<br>**seo_title**: "Yogablock av Kork Gymstick" → "Yogablock Gymstick i Kork"<br>Skäl: Ordningen Typ, Märke (jfr 'Massageboll Spokey Double Oak i Kork'). 25 tecken. |
| 3248 | 10581118976266 | Pannbandsset Gymstick Vivid Head Band Set | GODKÄND |  |
| 3249 | 10581119009034 | Träningsboll Gymstick Vivid Fitness Ball | GODKÄND |  |
| 3250 | 10581119041802 | Massageboll Gymstick Vivid | GODKÄND |  |
| 3251 | 10581119074570 | Hopprep Gymstick Vivid Jump Rope | GODKÄND |  |
| 3252 | 10581119172874 | Minibandset Gymstick Vivid Mini Band Set, 3 st | RÄTTA | **titel**: "Minibandset Gymstick Vivid Mini Band Set, 3 st" → "Minibandset Gymstick Vivid, 3 st"<br>**meta**: "Gymstick Vivid Mini Band Set är ett set med tre minibands med olika motståndsnivåer, för uppvärmning och styrkeövningar enligt tillverkaren." → "Gymstick Vivid Mini Band Set är ett set med tre miniband med olika motståndsnivåer, för uppvärmning och styrkeövningar enligt tillverkaren."<br>**html**: "innehåller tre minibands med" → "innehåller tre miniband med"<br>**html_2**: "värma upp med minibands," → "värma upp med miniband,"<br>Skäl: 'Mini Band Set' upprepar typordet på engelska (jfr 2209). 'Minibands' är engelsk pluralform; svensk plural är 'miniband'. Titeln blir lika med SEO-titeln (lagras tom). Meta 139 tecken. |
| 3253 | 10581119205642 | Myo Ball Gymstick Vivid | UNDERKÄND | Oklar produkttyp: 'Myo Ball' är inget svenskt typord, och källan består bara av effekt- och rehabpåståenden (triggerpunkter, ömhet). Texten blir innehållslös ('en boll för träning'). |
| 3254 | 10581119238410 | Viktset Gymstick Vivid Pump Set, 20 kg | UNDERKÄND | Viktset 20 kg med justerbara vikter: last och troligen lås (stång, skivor, lås), men vad som ingår och om 20 kg är totalvikten framgår inte. Konsekvent med avvisade Quick-Lock-hantlar. |

## Avvisade av utkastaren (11)
Alla elva avvisningar håller: 3200, 3201, 3202 (snabblåshantlar och kettlebell: last och lås), 3208 Slant Board och 3216 Step Board (bär kroppsvikt, ingen maxbelastning), 3218 Fit Walker (gånghjälp, rehab), 3220 och 3222 Tennis Elbow Support (smärt- och skadepåståenden i namnet), 3242 Plyobox (last, varianter S/Default med olika pris), 3247 Z-Bar (last) och 3255 Spike Mat (akupressur). Ingen kan släppas.

## Att bekräfta för David
- 3214: typordet 'Handträningsboll' (utkastets 'Pressboll' är inte etablerat).
- 3217: vad varianten TELE är (269 kr mot 149 kr).
- 3245: om Yoga Block säljs styckvis eller som par (källan: 'Dessa block').
- 3206 och 3254: om viktskivor och viktset ska räknas som last som tas för hand (jag har underkänt dem för att följa avvisningen av Z-Bar och snabblåshantlar).
- 3241: att skyddslöftet tas bort också för handskar, i linje med 3221 och 3224.
