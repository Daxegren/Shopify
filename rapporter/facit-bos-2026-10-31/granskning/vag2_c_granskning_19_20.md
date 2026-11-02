# Granskning våg 2, utkast c_19 och c_20 – BEST OF SPORTS (2026-11-02)

Oberoende granskning. Jag har bara läst i Shopify och inte ändrat något i butiken eller i utkastsfilerna, och jag har inte committat något. Butiken kontrollerades först med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK).

**Underlag:** `vag2_skriv/c_19_utkast.json` (9 utkast) och `c_20_utkast.json` (8 utkast), alltså 17 utkast. Dessutom `c_19_avvisade.json` (6) och `c_20_avvisade.json` (2). Jag har läst standarden (`produkttexter-standard.md` avsnitt 1–11), `LARDOMAR.md` och `granskning/vag2_a_granskning_2.md`.

**Metod:**
- **Källan live:** title, handle, status, productType, vendor, tags, descriptionHtml, seo och variants hämtades med graphql_query (`nodes`) i två batchar (9 + 8). Alla 17 är ACTIVE, produkttypen är tom ("") och leverantören är Gymstick. Live-SEO är tom på alla 17. Fältet `fakta` stämmer med live-källan för alla 17 (beskrivning, taggar, varianter och SKU).
- **Maskinellt:** längder på titel, SEO-titel och meta. Standardblocket jämfördes tecken för tecken med `c_1_utkast.json`, och alla 17 är identiska. Titlar och SEO-titlar kontrollerades mot alla `c_*_utkast.json` och `a_skriv.json`, både utkastens och mina föreslagna: inga dubbletter. Ingen av de 17 finns i `handhavd_ids.txt`. Före-texterna i JSON-filen har kontrollerats mot utkasten (de finns ordagrant).
- **För hand:** varje titel, SEO-titel, meta och html lästes mot live-källan och språkgranskades. Typorden jämfördes med de övriga Gymstick-utkasten i c_1–c_18.

## Resultat i korthet

| Dom | Antal | Nr |
|---|---|---|
| GODKÄND | 2 | 3282, 3287 |
| RÄTTA | 14 | 3271, 3272, 3273, 3274, 3280, 3283, 3284, 3285, 3290, 3291, 3292, 3293, 3294, 3295 |
| UNDERKÄND | 1 | 3289 |

Avvisade av utkastaren (8 st: 3275, 3276, 3277, 3278, 3279, 3281, 3286, 3288): **alla avvisningar är riktiga.** Det är hantlar, viktstång, viktskiva, multigym, plyobox och viktväst (last), och Comfort Seat har oklar produkttyp (sju varianter från 449 till 12 999 kr med SKU-prefix SB). Ingen av dem kan släppas.

## Regelkontroll (alla 17)
- Titlar: 20–43 tecken och högst 2 kommatecken. Kommat i decimaltalet "45,7 m" (3282) räknas av skriptet men är ett tal, inte en avskiljare.
- SEO-titlar: 20–38 tecken (≤43), unika. Flera är identiska med titeln, och de lagras då tomma (avsett beteende).
- Meta: 131–155 tecken där den finns. Null på 3274, 3282 och 3287 (tunn källa), vilket godtas.
- Enheter med gemener (cm, ml, m), inga intervall med bindestreck, stor bokstav efter kolon.
- Inga priser, omdömen, ursprung eller märkestexter. Alla "ultimata", "perfekt", "högkvalitativ", rehab-, blodcirkulations- och skadepåståenden är utelämnade. Miljöpåståendet i 3293 är utelämnat.
- Varianter: 3280 (Default/MS 0 kr), 3282 (1–6, 1 109–1 959 kr) och 3284 (BL/PI/WH, WH 0 kr) låser inte färg, nivå eller variant. Det är rätt.
- **Mönster:** (1) cirkulära engelska förstameningar ("Speed Cones är koner", "Vivid Foam Roller är en foam roller", "Yoga Block är ett yogablock", "Wrist Trainer är en handledstränare") i 8 utkast. (2) Typord som avviker från resten av vågen: Skumrulle och Foam Roller i stället för Foamroller, Myofasciaboll och Återhämtningsboll i stället för Massageboll, Flytande Krita i stället för Gymtalk (avsnitt 11) och Koner i stället för Träningskoner. (3) "Återhämtning" står kvar som effekt i 3271 och 3283, fast alla andra utkast i vågen stryker det. (4) Specifikationsrader av typen "Material: Slitstarkt" anger en egenskap, inte ett material.

## Per produkt

| Nr | Id | Dom | Fält | Före | Efter |
|---|---|---|---|---|---|
| 3271 | 10598114197770 | RÄTTA | titel | Skumrulle Gymstick Active Compact, 30 cm | Foamroller Gymstick Active Compact, 30 cm |
| 3271 | 10598114197770 | RÄTTA | seo_title | Skumrulle Gymstick Active Compact | Foamroller Gymstick Active Compact |
| 3271 | 10598114197770 | RÄTTA | meta | Gymstick Active Compact är en kompakt skumrulle på 30 cm. Enligt tillverkaren är den avsedd för återhämtning och rörlighetsträning. | Gymstick Active Compact är en kompakt foamroller på 30 cm. Enligt tillverkaren är den avsedd för rörlighetsträning och regelbunden användning. |
| 3271 | 10598114197770 | RÄTTA | html intro | Gymstick Active Compact är en kompakt skumrulle på 30 cm, enligt tillverkaren avsedd för återhämtning och rörlighetsträning. | Gymstick Active Compact är en kompakt foamroller på 30 cm, enligt tillverkaren avsedd för rörlighetsträning. |
| 3271 | 10598114197770 | RÄTTA | html passar 1 | <li>Dig som vill ha en kompakt skumrulle</li> | <li>Dig som vill ha en kompakt foamroller</li> |
| 3271 | 10598114197770 | RÄTTA | html passar 2 | <li>Dig som vill använda en rulle till återhämtning och rörlighetsträning, enligt tillverkaren</li> | <li>Dig som vill använda en rulle i rörlighetsträning, enligt tillverkaren</li> |
| 3271 | 10598114197770 | RÄTTA | html spec | <li>Typ: Skumrulle</li> | <li>Typ: Foamroller</li> |
| 3272 | 10598117802250 | RÄTTA | meta | Gymstick Fot- och Handmassagerulle är | Gymstick Fot- och handmassagerulle är |
| 3272 | 10598117802250 | RÄTTA | html intro | <p>Gymstick Fot- och Handmassagerulle är | <p>Gymstick Fot- och handmassagerulle är |
| 3273 | 10598117900554 | RÄTTA | titel | Flytande Krita Gymstick | Gymtalk Gymstick Liquid Chalk |
| 3273 | 10598117900554 | RÄTTA | seo_title | Flytande Krita Gymstick för Grepp | Gymtalk Gymstick Liquid Chalk för Grepp |
| 3273 | 10598117900554 | RÄTTA | meta | Gymstick Flytande Krita är en krita i flytande form. Enligt tillverkaren förstärker den greppet vid styrkelyft, klättring och andra aktiviteter. | Gymstick Liquid Chalk är en flytande gymtalk. Enligt tillverkaren förstärker den greppet vid styrkelyft, klättring och andra aktiviteter. |
| 3273 | 10598117900554 | RÄTTA | html intro | Gymstick Flytande Krita är en krita i flytande form som enligt tillverkaren förstärker greppet. | Gymstick Liquid Chalk är en flytande gymtalk som enligt tillverkaren förstärker greppet. |
| 3273 | 10598117900554 | RÄTTA | html spec | <li>Typ: Flytande krita</li> | <li>Typ: Flytande gymtalk</li> |
| 3274 | 10604622086410 | RÄTTA | titel | Myofasciaboll Gymstick Active | Massageboll Gymstick Active Myofascia Ball |
| 3274 | 10604622086410 | RÄTTA | seo_title | Myofasciaboll Gymstick Active | Massageboll Gymstick Active Myofascia Ball |
| 3274 | 10604622086410 | RÄTTA | html intro | Gymstick Active Myofascia Ball är en myofasciaboll som enligt tillverkaren används efter träning. | Gymstick Active Myofascia är en massageboll som enligt tillverkaren används efter träning. |
| 3274 | 10604622086410 | RÄTTA | html passar 1 | <li>Dig som vill ha en myofasciaboll</li>  | (tas bort) |
| 3274 | 10604622086410 | RÄTTA | html spec modell | <li>Modell: Active</li> | <li>Modell: Active Myofascia Ball</li> |
| 3274 | 10604622086410 | RÄTTA | html spec typ | <li>Typ: Myofasciaboll</li> | <li>Typ: Massageboll</li> |
| 3280 | 10611430850826 | RÄTTA | meta | kan användas för övningar för ben | kan användas i övningar för ben |
| 3282 | 10611433832714 | GODKÄND | – | – | – |
| 3283 | 10611438027018 | RÄTTA | titel | Återhämtningsboll Gymstick Recovery, 10 cm | Massageboll Gymstick Recovery Ball, 10 cm |
| 3283 | 10611438027018 | RÄTTA | seo_title | Återhämtningsboll Gymstick Recovery | Massageboll Gymstick Recovery Ball |
| 3283 | 10611438027018 | RÄTTA | meta | Gymstick Recovery Ball är en återhämtningsboll på 10 cm. Enligt tillverkaren används den efter träningspass som komplement till träningsrutinen. | Gymstick Recovery är en massageboll på 10 cm. Enligt tillverkaren används den efter träningspass och som komplement till träningsrutinen. |
| 3283 | 10611438027018 | RÄTTA | html intro | Gymstick Recovery Ball är en återhämtningsboll på 10 cm som enligt tillverkaren används efter träningspass. | Gymstick Recovery är en massageboll på 10 cm som enligt tillverkaren används efter träningspass. |
| 3283 | 10611438027018 | RÄTTA | html passar 1 | <li>Dig som vill ha en liten boll till återhämtning efter träning</li> | <li>Dig som vill ha en liten boll att använda efter träning</li> |
| 3283 | 10611438027018 | RÄTTA | html spec | <li>Typ: Återhämtningsboll</li> | <li>Typ: Massageboll</li> |
| 3284 | 10611438420234 | RÄTTA | meta | Gymstick Shakerflaska är en shakerflaska på 600 ml. | Shakerflaskan från Gymstick rymmer 600 ml. |
| 3284 | 10611438420234 | RÄTTA | html intro | <p>Gymstick Shakerflaska är en shakerflaska på 600 ml.</p> | <p>Shakerflaskan från Gymstick rymmer 600 ml.</p> |
| 3285 | 10611438616842 | RÄTTA | titel | Koner Gymstick Speed | Träningskoner Gymstick Speed |
| 3285 | 10611438616842 | RÄTTA | seo_title | Koner Gymstick Speed | Träningskoner Gymstick Speed |
| 3285 | 10611438616842 | RÄTTA | meta | Gymstick Speed Cones är koner som enligt tillverkaren används för agilityträning, intervallpass och hinderbanor, både inomhus och utomhus. | Gymstick Speed är träningskoner som enligt tillverkaren används för agilityträning, intervallpass och hinderbanor, både inomhus och utomhus. |
| 3285 | 10611438616842 | RÄTTA | html intro | Gymstick Speed Cones är koner för träning av snabbhet, smidighet och koordination, enligt tillverkaren. | Gymstick Speed är träningskoner för träning av snabbhet, smidighet och koordination, enligt tillverkaren. |
| 3285 | 10611438616842 | RÄTTA | html spec | <li>Typ: Koner</li> | <li>Typ: Träningskoner</li> |
| 3287 | 10611438911754 | GODKÄND | – | – | – |
| 3289 | 10611442450698 | UNDERKÄND | – | – | – |
| 3290 | 10611453886730 | RÄTTA | meta | Gymstick Vivid Core Ball är en rosa träningsboll | Gymstick Vivid Core är en rosa träningsboll |
| 3290 | 10611453886730 | RÄTTA | html intro | <p>Gymstick Vivid Core Ball är en rosa träningsboll | <p>Gymstick Vivid Core är en rosa träningsboll |
| 3290 | 10611453886730 | RÄTTA | html spec | <li>Material: Slitstarkt, enligt tillverkaren</li> | <li>Slitstarkt material, enligt tillverkaren</li> |
| 3291 | 10611454050570 | RÄTTA | meta | Gymstick Vivid Exercise Band Set är ett set med 3 träningsband. | Gymstick Vivid är ett set med 3 träningsband. |
| 3291 | 10611454050570 | RÄTTA | html intro | <p>Gymstick Vivid Exercise Band Set är ett set med 3 träningsband.</p> | <p>Gymstick Vivid är ett set med 3 träningsband.</p> |
| 3291 | 10611454050570 | RÄTTA | html spec | <li>Material: Hållbart, enligt tillverkaren</li>  | (tas bort) |
| 3292 | 10611454181642 | RÄTTA | titel | Foam Roller Gymstick Vivid, 60 cm | Foamroller Gymstick Vivid, 60 cm |
| 3292 | 10611454181642 | RÄTTA | seo_title | Foam Roller Gymstick Vivid, 60 cm | Foamroller Gymstick Vivid, 60 cm |
| 3292 | 10611454181642 | RÄTTA | meta | Gymstick Vivid Foam Roller är en foam roller på 60 cm. Enligt tillverkaren gör längden den mångsidig för övningar över hela kroppen. | Gymstick Vivid är en foamroller med längden 60 cm. Enligt tillverkaren gör den generösa längden den mångsidig för övningar över hela kroppen. |
| 3292 | 10611454181642 | RÄTTA | html intro | <p>Gymstick Vivid Foam Roller är en foam roller på 60 cm.</p> | <p>Gymstick Vivid är en foamroller på 60 cm.</p> |
| 3292 | 10611454181642 | RÄTTA | html passar 1 | Dig som vill ha en foam roller för övningar för hela kroppen | Dig som vill ha en foamroller för övningar för hela kroppen |
| 3292 | 10611454181642 | RÄTTA | html passar 2 | Dig som vill ha en foam roller med längden 60 cm | Dig som vill ha en foamroller med längden 60 cm |
| 3293 | 10611454771466 | RÄTTA | meta | Gymstick Vivid Yoga Block är ett yogablock. | Gymstick Vivid är ett yogablock. |
| 3293 | 10611454771466 | RÄTTA | html intro | <p>Gymstick Vivid Yoga Block är ett yogablock för yoga.</p> | <p>Gymstick Vivid är ett yogablock för stöd och stabilitet i olika positioner, enligt tillverkaren.</p> |
| 3293 | 10611454771466 | RÄTTA | html spec | <li>Material: Slitstarkt, enligt tillverkaren</li> | <li>Slitstarkt material, enligt tillverkaren</li> |
| 3294 | 10634245669130 | RÄTTA | meta | Gymstick Court Dartboard Surround är en darttavleomslutning. Enligt tillverkaren är den slagtålig och skyddar väggen mot missade pilar runt standardtavlor. | Gymstick Court är en darttavleomslutning. Enligt tillverkaren är den slagtålig och skyddar väggen mot missade pilar runt standarddarttavlor. |
| 3294 | 10634245669130 | RÄTTA | html intro | <p>Gymstick Court Dartboard Surround är en darttavleomslutning | <p>Gymstick Court är en darttavleomslutning |
| 3294 | 10634245669130 | RÄTTA | html spec | <li>Egenskaper enligt tillverkaren: Slagtålig</li> | <li>Egenskaper, enligt tillverkaren: Slagtålig</li> |
| 3295 | 10634331783434 | RÄTTA | meta | Gymstick Wrist Trainer är en handledstränare för träning av handleder och underarmar. Enligt tillverkaren har den kompakt design | Gymstick Wrist Trainer är ett träningsredskap för handleder och underarmar. Enligt tillverkaren har det kompakt design |
| 3295 | 10634331783434 | RÄTTA | html intro | <p>Gymstick Wrist Trainer är en handledstränare för handleder och underarmar.</p> | <p>Gymstick Wrist Trainer är ett träningsredskap för handleder och underarmar.</p> |

## Skäl per produkt

- **3271 (10598114197770) – RÄTTA:** Typordet följer övriga godkända Gymstick/Toorx-utkast (Foamroller: 3027, 3226, 3259, Toorx Grid i våg 1). "Återhämtning" behandlas som effektpåstående i alla andra utkast i vågen och tas bort.
- **3272 (10598117802250) – RÄTTA:** Versal mitt i ordet hör bara hemma i titel och SEO-titel, inte i löptext. Massagerulle får stå som produktnamn (avsnitt 10); inga effektpåståenden. Meta 145 tecken.
- **3273 (10598117900554) – RÄTTA:** Avsnitt 11: Gymtalk är typordet för talk (jfr 2108, 2213 Gymtalk Trec Liquid Chalk). Utkastet byter dessutom produktnamnet "Liquid Chalk" mot en egen översättning och sätter märket sist (ordning Typ, Märke, Modell). Meta 137 tecken.
- **3274 (10604622086410) – RÄTTA:** "Myofasciaboll" är inget etablerat svenskt typord; övriga Gymstick-utkast använder Massageboll (3154 MyoFascia Ball, 3156, 3157). Modellnamnet ska vara helt (Active Myofascia Ball). Punkten "Dig som vill ha en myofasciaboll" är cirkulär och tas bort. SEO-titel lika med titel lagras tom (avsett).
- **3280 (10611430850826) – RÄTTA:** Upprepningen "för övningar för". Meta 139 tecken. Variant MS (SKU 62005-MS) har pris 0 kr och är oförklarad; texten låser ingen variant, så frågan går till David men stoppar inte texten.
- **3282 (10611433832714) – GODKÄND:** Längden 45,7 m finns i originaltitel och beskrivning. Motståndsnivån ("Extra Heavy") är rätt inte låst eftersom varianterna 1–6 (1 109–1 959 kr) är oförklarade. Rehabilitering utelämnad. Meta null godtas. Att bekräfta: vad varianterna 1–6 är, och att titeln "Extra Heavy" i butiken motsäger varianterna.
- **3283 (10611438027018) – RÄTTA:** "Återhämtningsboll" är en direktöversättning av Recovery Ball (cirkulärt) och bär ett effektpåstående. Övriga utkast för samma slags boll heter Massageboll (3021 Active Recovery, 3205 Recovery Twin Ball). Källan nämner självmassage. Meta 137 tecken.
- **3284 (10611438420234) – RÄTTA:** Cirkulär mening ("Shakerflaska är en shakerflaska"). Meta 131 tecken. Färgen är rätt inte låst (varianter BL, PI, WH; WH 0 kr). Kosttillskott är rätt utelämnat.
- **3285 (10611438616842) – RÄTTA:** "Speed Cones är koner" är just det cirkulära engelska mönstret. Typordet följer 3210 (Träningskoner Gymstick Speed Discs). Meta 140 tecken. Antal koner i förpackningen saknas i källan (att bekräfta); "för barn" rätt utelämnat.
- **3287 (10611438911754) – GODKÄND:** Massagebollar som produktnamn är tillåtet (avsnitt 10); alla effekt- och behandlingspåståenden utelämnade. Meta null godtas (tunn källa). Antal och storlek saknas i källan.
- **3289 (10611442450698) – UNDERKÄND:** Handledsstöd/"handledsortos" med skadeförebyggande påstående i källan ("minimerar risken för skador", "optimalt stöd" vid tunga lyft). Skydd/stöd med skadeförebyggande påståenden tas för hand med Davids ja. Texten i sig är försiktig, men storlek, material och hand saknas. Obs: syskonprodukten 3243 Wrist Support 1.0 (c_17) bör bedömas likadant.
- **3290 (10611453886730) – RÄTTA:** "Core Ball är en träningsboll" är cirkulärt. "Slitstarkt" är inget material, så raden skrivs som egenskap. Meta 147 tecken. Storlek saknas; pris 89 kr och syskonet 3174 (22 cm) tyder på en liten boll, inte en sittboll med last, men det bör bekräftas.
- **3291 (10611454050570) – RÄTTA:** "Exercise Band Set är ett set med träningsband" är cirkulärt. Materialraden saknar material och bygger bara på kvalitetspåståendet "högkvalitativt material för maximal hållbarhet"; tas bort. Meta 133 tecken. Antalet 3 finns i originaltiteln (3pcs).
- **3292 (10611454181642) – RÄTTA:** Typordet skrivs Foamroller i ett ord som i 3027, 3226, 3259 och våg 1 (engelskt tvåordsuttryck annars). "Vivid Foam Roller är en foam roller" är cirkulärt. Meta 137 tecken (utkastets 132 blir för kort när upprepningen tas bort; "generösa längd" står i källan). Unik mot 3259 (33 cm).
- **3293 (10611454771466) – RÄTTA:** "Yoga Block är ett yogablock för yoga" är cirkulärt och upprepar. Miljöpåståendet rätt utelämnat. Meta 144 tecken. Källan säger "dessa block" (plural): antal i förpackningen ska bekräftas.
- **3294 (10634245669130) – RÄTTA:** "Dartboard Surround är en darttavleomslutning" är cirkulärt. Kommatecken för att följa mönstret "X, enligt tillverkaren:" i övriga utkast. Meta 140 tecken. Ingen säkerhetsprodukt. Mått och material saknas i källan.
- **3295 (10634331783434) – RÄTTA:** "Wrist Trainer är en handledstränare" är cirkulärt (och "handledstränare för handleder" upprepar). Titeln "Handledstränare Gymstick" behålls som typord. Meta 144 tecken. Hur redskapet fungerar (fjäder, gyro, rulle) saknas; om det visar sig ha motor eller elektronik ska det tas för hand.

## Att bekräfta för David
1. **3289 Wrist Support 2.0** är underkänd som stöd med skadeförebyggande påstående. Ska syskonet 3243 Wrist Support 1.0 (c_17) också tas för hand?
2. **Varianter med pris 0 kr:** 3280 Pilatesring (MS) och 3284 Shakerflaska (WH). 3282 Träningsband Pro: vad betyder varianterna 1–6, och stämmer butikens "Extra Heavy" i titeln?
3. **Typord:** Foamroller (ett ord, som i tidigare vågor) i stället för det svenska "skumrulle". Jag har rättat till Foamroller för enhetlighetens skull. Säg till om skumrulle ska gälla överallt i stället.
4. **3295 Wrist Trainer:** funktionen är okänd. Om den har motor eller elektronik ska den tas för hand.
5. **3290 Vivid Core Ball:** storleken saknas. Om den är en sittboll (last) ska den tas för hand.
