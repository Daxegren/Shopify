# Granskningsutlåtande k_46ovr5: övriga tidigare utanför-kategorier, aktiva produkter (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan text får faktatext även i säkerhets-, barn-, elektronik-, rullskridsko- och akupressur/rehab-kategorier), `beslut-2026-11-08.md`, LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och formatet i `k_utlatande_43.json`. Tillverkarsidorna på gymstick.com lästes för alla tio Gymstick-produkter (alla 200; SKU och EAN stämmer utom för PRO-550M-HPB).

Alla 19 utkast och alla 5 avvisade är ACTIVE. Standardblocket är exakt som i `b_skriv_24.json` på alla; leveranstidsmeningen finns bara på 47606 och 47607, som är de enda med taggen På beställning. Titel ≤70 tecken och ≤2 kommatecken, SEO ≤43, meta 115–148 tecken med verb, "Passar för" på alla, inga cirkulära inledningar. Titlar, SEO-titlar och metatexter är unika inom batchen och mot alla andra filer i `vag2_skriv/`; butiken söktes på modellord (Talon, Bookman, Boom, Aero, Legacy, Vibrationsplatta, Spike, Knästöd, Patella, Neck, Straps, Elbow, Hållning, Akupressur, Knäskydd, Light Stick, Rullskridsk, Stuntspark). `skrivfil_kontroll.py` ger 0 formatfel och 0 varningar på utkasten och på de rättade texterna. De enda FEL är spärrlistan för 15 produkter (alla utom 47611, 47616, 47617, 47618), som spärrades bara på grund av kategori eller tidigare avvisning och omfattas av beslutet 2026-11-08; en undantagspost behövs i `sparrlista.json` (tillägg, R14) innan skrivfilen byggs. Varje rättning är ETT sammanhängande före/efter-par per fält, och före-texten förekommer exakt en gång i fältet (kontrollerat i python).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_46ovr5.json`. I tabellerna nedan står ⏎ för radbrytning; JSON-filen har de exakta före/efter-texterna.

## Resultat: 13 GODKÄND, 5 RÄTTA, 1 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 47601 | 10507390091530 | k_46ovr5_utkast.json | RÄTTA | titel, seo_title, html |
| 47602 | 10515754352906 | k_46ovr5_utkast.json | GODKÄND | – |
| 47603 | 10515754451210 | k_46ovr5_utkast.json | GODKÄND | – |
| 47604 | 10554365903114 | k_46ovr5_utkast.json | GODKÄND | – |
| 47605 | 10554365935882 | k_46ovr5_utkast.json | GODKÄND | – |
| 47606 | 10561341620490 | k_46ovr5_utkast.json | RÄTTA | html |
| 47607 | 10561341718794 | k_46ovr5_utkast.json | GODKÄND | – |
| 47608 | 10565607850250 | k_46ovr5_utkast.json | RÄTTA | html |
| 47609 | 10574017691914 | k_46ovr5_utkast.json | RÄTTA | titel, seo_title |
| 47610 | 10581096562954 | k_46ovr5_utkast.json | GODKÄND | – |
| 47611 | 10581107933450 | k_46ovr5_utkast.json | UNDERKÄND | – |
| 47612 | 10581108326666 | k_46ovr5_utkast.json | GODKÄND | – |
| 47613 | 10581109211402 | k_46ovr5_utkast.json | GODKÄND | – |
| 47614 | 10581109244170 | k_46ovr5_utkast.json | GODKÄND | – |
| 47615 | 10581109375242 | k_46ovr5_utkast.json | GODKÄND | – |
| 47616 | 10581109571850 | k_46ovr5_utkast.json | GODKÄND | – |
| 47617 | 10581110259978 | k_46ovr5_utkast.json | RÄTTA | meta |
| 47618 | 10581110718730 | k_46ovr5_utkast.json | GODKÄND | – |
| 47619 | 10581111898378 | k_46ovr5_utkast.json | GODKÄND | – |

## Löften (hälsa, säkerhet, skydd, utveckling, prestanda, kvalitet)

Alla titlar, SEO-titlar, metatexter och beskrivningar söktes efter både tydliga och subtila ord (lindrar, smärta, spänning, stöd/stödjer, skyddar, säker, trygg, stabil, förebygger, återhämtning, cirkulation, hållning, rörlighet, komfort, bekväm, hållbar, slitstark, kvalitet, effektiv, prestation, synlighet, utveckling, stimulering). Ett subtilt påstående fanns kvar: "magnetisk benstimulering" på vibrationsplattan 47606 (tas bort). I övrigt står sådana ord bara som produktnamn eller typord ur live-titeln eller tillverkaren (Knäskydd, Knästöd, Nackstöd, Hållningskorrigerare, Patella Brace, Tennis Elbow Support, Underarmsstöd), aldrig som påstående om effekt. Lastgränser: 47602/47603 (100 kg), 47606 (120 kg) och 47607 (150 kg) är svenska rader med etikett och enhet i egen källa och står en gång med "enligt tillverkaren" (R4); 47611 hade "Ej känd" (v1.10) men underkänns av annat skäl.

## Avvisade (k_46ovr5_avvisade.json)

Alla fem avvisningar är riktiga och lyfts inte: Bottecchia Gravel Monster (olika pris M/L, lager 0, titelns C48 och färg stämmer inte med varianterna), Leader Fox Ema (olika SKU och pris, lager 0, storlek ej belagd, undantagen från slutsiffre-regeln), Fiido T2 fotstöd (en rad källa, bärande del, ingen tillverkarsida, lager 0), Knästöd 1.0 (tillverkaren kallar den ankle support: motsägande källa, R2) och Telescopic Fit Walker (SKU 28000/EAN 6430016901895 mot tillverkarens 28000BL/6430062513363).

## Frågor till David

1. Spärrlistan: 15 utkast stoppas av `skrivfil_kontroll.py` (utanfor-tills-vidare och tidigare-avvisade). En undantagspost med hänvisning till beslutet 2026-11-08 behövs (tillägg). Butiksprofilen har också kvar rullskridskor, akupressur och vibrationsplattor under `utanfor_tills_vidare`; R6 säger att profilen är facit, så raderna behöver markeras som hävda för aktiva produkter.
2. Horisontell stång PRO-550M-HPB (47611): bekräfta att butikens streckkod 6430016904520 avser samma artikel som tillverkarens 6430016901963. Då kan texten skrivas (fakta finns redan i utkastet).
3. Fila Legacy Comp Lady finns aktiv två gånger utan text: storlek 42,5 (10507390091530, denna) och storlek 42 (10472237891850). Titeln skiljer dem nu på storlek, som står i artikelnumret.
4. Nya engelska typord behålls som produktnamn: Neck Traction Device, Patella Brace, Knee Straps, Wrist Straps, Tennis Elbow Support (svenskt beskrivande ord i texten). Nya svenska typord: Akupressurmatta, Nackstöd, Hållningskorrigerare, Underarmsstöd, Bärbar lampa. Godkänn eller ange andra ord, och lägg de godkända i `godkanda_typord`.
5. Produktnamn som i sig antyder effekt (Hållningskorrigerare, Tennis Elbow Support) behålls enligt praxis 2026-11-06 för varunamn. Säg till om de ska ersättas.

## Skäl och rättningar per produkt

### 47601 (10507390091530, k_46ovr5_utkast.json): RÄTTA

Live ACTIVE, en variant (Default Title) FILA-LEGCOMPLADY-BLKBLU-42.5, lager 1. Fakta (komposittram, Air Flow, 80 mm hjul, ABEC 5, fritidsbruk) finns i egen svensk källa; löftesord (pålitliga, slitstarkt, ultralätt, torra fötter, åkkapacitet, komfort och säkerhet) korrekt utelämnade. Rättning R12a/beslut 2026-11-05: en annan aktiv annons utan text, 10472237891850 'Rullskridskor FILA Legacy Comp Lady, svart' (SKU ...-42), är samma modell i storlek 42. Titeln måste skilja dem; storleken 42,5 står entydigt i artikelnumret (samma mönster som butikens Fila-varianter). Färgen lämnas utanför (BLKBLU mot 'svart'). Spärrlistan (utanfor-tills-vidare) kräver undantag enligt beslutet 2026-11-08.

| fält | före | efter |
|---|---|---|
| titel | Rullskridskor Fila Legacy Comp Lady | Rullskridskor Fila Legacy Comp Lady, Storlek 42,5 |
| seo_title | Rullskridskor Fila Legacy Comp Lady | Rullskridskor Fila Legacy Comp Lady 42,5 |
| html | <li>Modell: Legacy Comp Lady</li> | <li>Modell: Legacy Comp Lady</li>⏎<li>Storlek: 42,5</li> |

### 47602 (10515754352906, k_46ovr5_utkast.json): GODKÄND

Live ACTIVE, 105557, EAN 2909452639647, lager 3. Varje uppgift finns i den svenska specifikationen (förare 115–130 cm, 4–9 år, nybörjare, ståplatta och styre i aluminium med mått, IHC, ABEC-9, 110 mm, 2,48 kg, svart/grå). Lastgräns 'Lastkapacitet: upp till 100 kg' är svensk med etikett och enhet och står en gång med 'enligt tillverkaren' (R4). Live-titelns 'Rå' mot källans 'grå': texten följer källan, som skrivna syskonet Union DOT L Svart/Grå. Inga säkerhets- eller utvecklingslöften. Skild från 47603 genom färg, SKU och EAN. Spärrlistan kräver undantag.

### 47603 (10515754451210, k_46ovr5_utkast.json): GODKÄND

Live ACTIVE, 105556, EAN 2909698309939, lager 2. Samma kontroll som 47602; färg svart enligt källan. Lastgräns en gång enligt tillverkaren (R4). Titel och SEO unika mot 47602 och mot skrivna Union Lite/DOT. Spärrlistan kräver undantag.

### 47604 (10554365903114, k_46ovr5_utkast.json): GODKÄND

Live ACTIVE, SKU 480, EAN 7350051864803, lager 1. USB-laddning, fast sken/blinkande, fästen hand/väska/cykel och användningsområde finns i egen källa. 'Reflexlampa', synlighet, säkerhet, 'i alla väder' och 'idealisk' utelämnade (v1.9, inga synlighets- eller säkerhetslöften). Typordet Bärbar lampa finns i live-titeln på Bookman Eclipse (R7). Skild från 47605 genom färg, SKU och EAN. Spärrlistan kräver undantag.

### 47605 (10554365935882, k_46ovr5_utkast.json): GODKÄND

Live ACTIVE, SKU 509, EAN 7350051865091, lager 1. Samma kontroll som 47604; egen källas ordval (laddningsbar, kontinuerligt, daglig pendling) följs. Inga synlighets- eller säkerhetslöften. Spärrlistan kräver undantag.

### 47606 (10561341620490, k_46ovr5_utkast.json): RÄTTA

Live ACTIVE, 24TCFV3000, EAN 8717842037287, lager 14, taggen På beställning: leveranstidsmeningen finns i standardblocket. Alla effektpåståenden (fettförbränning, muskeluppbyggnad, bentäthet, cirkulation, balans) korrekt utelämnade, men 'magnetisk benstimulering' står kvar i löptext och specifikation. 'Stimulering' av ben (ben = skelett eller ben) är ett subtilt hälsopåstående i en källa som samtidigt lovar förbättrad bentäthet; tas bort (2026-11-08: inga hälsolöften). Maximal användarvikt 120 kg är svensk rad med etikett och enhet, en gång enligt tillverkaren (R4). Spärrlistan kräver undantag; profilen har kvar vibrationsplattor under utanfor_tills_vidare.

| fält | före | efter |
|---|---|---|
| html | Den har 99 hastigheter, 10 program, magnetisk benstimulering och LED-display. Stretchbollar och en sladdlös fjärrkontroll följer med, och hastighet och program justeras med fjärrkontrollen.</p><h2>Passar för</h2><ul>⏎<li>Dig som söker en vibrationsplatta med 99 hastigheter och 10 program</li>⏎<li>Dig som vill ha en vibrationsplatta med fjärrkontroll</li>⏎</ul><h2>Specifikationer</h2><ul>⏎<li>Typ: Vibrationsplatta</li>⏎<li>Märke: Tunturi</li>⏎<li>Modell: Cardio Fit V30</li>⏎<li>Motor: 200 W</li>⏎<li>Hastigheter: 99</li>⏎<li>Program: 10</li>⏎<li>Benstimulering: Magnetisk</li> | Den har 99 hastigheter, 10 program och LED-display. Stretchbollar och en sladdlös fjärrkontroll följer med, och hastighet och program justeras med fjärrkontrollen.</p><h2>Passar för</h2><ul>⏎<li>Dig som söker en vibrationsplatta med 99 hastigheter och 10 program</li>⏎<li>Dig som vill ha en vibrationsplatta med fjärrkontroll</li>⏎</ul><h2>Specifikationer</h2><ul>⏎<li>Typ: Vibrationsplatta</li>⏎<li>Märke: Tunturi</li>⏎<li>Modell: Cardio Fit V30</li>⏎<li>Motor: 200 W</li>⏎<li>Hastigheter: 99</li>⏎<li>Program: 10</li> |

### 47607 (10561341718794, k_46ovr5_utkast.json): GODKÄND

Live ACTIVE, 24TCFV4000, EAN 8717842037294, lager 0, en variant, taggen På beställning: leveranstidsmeningen finns. Uppgifterna stämmer med egen källa (99 hastigheter, 10 program, 200 W, LED, 68 x 39 x 14 cm, 11 kg, stretchbollar, sladdlös kontroll). 'Max. brukarvikt: 150 kg' en gång enligt tillverkaren (R4). Inga effektpåståenden. Skriven utan lager enligt beslutet 2026-11-06 (en variant, v1.9 berörs inte). Spärrlistan kräver undantag.

### 47608 (10565607850250, k_46ovr5_utkast.json): RÄTTA

Live ACTIVE, varianter S/pink 105810 och L/pink 105808, båda 279 kr, lager 1+1 (v1.8: samma pris och färg, titeln låser ingen storlek). Vadderad insida, viktintervall, färg, användning och målgrupp finns i källan; kvalitets-, slitage- och komfortlöften samt 'Skyddsnivå: Extreme' korrekt utelämnade. Rättning R1: 'beroende på storlek' står inte i källan (bara intervallet 0.2330–0.2450). Boom Solid Knee Pads är annan modell. Spärrlistan kräver undantag.

| fält | före | efter |
|---|---|---|
| html | De är rosa och väger 0,233–0,245 kg, beroende på storlek. | De är rosa och väger 0,233–0,245 kg. |

### 47609 (10574017691914, k_46ovr5_utkast.json): RÄTTA

Live ACTIVE (tidigare DRAFT), 1094009283, EAN 4711291189409, lager 1. Alla uppgifter finns i egen specifikation (ALUXX, XS 34,5 cm för 155–166 cm, SXC32-3 RL 80 mm, Microshift Advent 9 växlar, Tektro HDC M275, Maxxis Rekon 27,5 x 2,2 tum, fästpunkter). 'Trygg', 'hållbar', 'bättre grepp' utelämnade. Rättning R12a/beslut 2026-11-05: butiken har flera Talon 2 (skrivna 29 tum Asfaltsgrön och Dried Matcha, oskriven aktiv 29 tum Pure Red, utkast 27,5 XS Dried Matcha); titeln ska skilja på storlek och färg som syskonet 'Mountainbike Giant Talon 3 XS 27,5 tum, Beeswax'. Färgen Pure Red står i live-titeln. Spärrlistan kräver undantag.

| fält | före | efter |
|---|---|---|
| titel | Mountainbike Giant Talon 2, 27,5 tum | Mountainbike Giant Talon 2 XS 27,5 tum, Pure Red |
| seo_title | Mountainbike Giant Talon 2, 27,5 tum | Mountainbike Giant Talon 2 XS, Pure Red |

### 47610 (10581096562954, k_46ovr5_utkast.json): GODKÄND

Live ACTIVE, 72041, EAN 6430062511482, lager 301. https://www.gymstick.com/active-spike-mat.html (SKU och EAN stämmer): 6 210 piggar, 64 x 40 x 3 cm, 0,52 kg, svart-blå, material bomull/skumplast/PP (tabell), länk till träningsvideo. Motsägelsen om piggarnas material (ABS i text) hanterad genom att bara tabellen återges. All text om cirkulation, spänningar, smärta, stress och avslappning utelämnad. Akupressur/rehab frisläppt för aktiva produkter 2026-11-08; typordet Akupressurmatta finns i butikens Tunturi-titlar. Spärrlistan kräver undantag.

### 47611 (10581107933450, k_46ovr5_utkast.json): UNDERKÄND

UNDERKÄND. Live ACTIVE, PRO-550M-HPB, lager 17, men EAN i butiken (6430016904520) skiljer sig från tillverkarsidans (6430016901963) för samma SKU, och produkten är uttryckligen hållen i beslutsunderlaget 2026-11-08 punkt 7 ('streckkoden skiljer') utan att David har svarat. Uppdraget kräver att SKU och EAN stämmer mot källan, och den avvisade Telescopic Fit Walker avvisades på samma grund. Dessutom är det en bärande del (pull-ups) där mått 230 x 95 x 220 cm, vikt 215 kg och 86 kg viktstapel på tillverkarsidan läses som hela stationens och inte entydigt som tilläggets. Skrivs när David bekräftat streckkoden; utkastets fakta kan då återanvändas (jämför 42216 i k_utlatande_42).

### 47612 (10581108326666, k_46ovr5_utkast.json): GODKÄND

Live ACTIVE, 63063, EAN 6430062510812, lager 195. https://www.gymstick.com/knee-support-2-0-one-size.html (SKU och EAN stämmer): 3 mm neopren, tre kardborrband, justerbar, material 15/45/34/6 % (spandex = elastan), 20,5 x 60 x 1 cm, 0,12 kg, svart. Stabilisering, patellaposition, knäsmärta, artrit, prestation och skydd utelämnade. Knästöd är live-titelns ord. Spärrlistan kräver undantag.

### 47613 (10581109211402, k_46ovr5_utkast.json): GODKÄND

Live ACTIVE, 61262, EAN 6430016903813, lager 911. https://www.gymstick.com/neck-relaxer.html (SKU och EAN stämmer): mjukt EVA, ergonomisk form, manual, 22,5 x 21 x 13 cm, 0,23 kg, svart. Användningsområdet anges bara som område (nacke, axlar, övre rygg); lindring, spänning, smärta, ryggradsställning och rörlighet utelämnade. 'Ergonomisk form' är ordagrann formbeskrivning (praxis k_utlatande_43). Nackstöd är egen källas ord. Spärrlistan kräver undantag.

### 47614 (10581109244170, k_46ovr5_utkast.json): GODKÄND

Live ACTIVE, 61240, EAN 6430016901048, lager 100. https://www.gymstick.com/neck-traction-device.html (SKU och EAN stämmer, enhet SET): enhet med fast hängrem, justerbara mitt- och sidokuddar, ögonmask, bärpåse, material 65/15/10/5/5 %, 0,18 kg, svart. Användningen (huvudet vilar, remmen hängs ovanifrån) är ordagrann; 'svävar', 'helt avslappnade', sträckning till naturligt läge, lindring och hållning utelämnade. Engelskt typord behålls (R7). Spärrlistan kräver undantag.

### 47615 (10581109375242, k_46ovr5_utkast.json): GODKÄND

Live ACTIVE, 63072, EAN 6430016909594, lager 733. https://www.gymstick.com/patella-brace-2-0.html (SKU och EAN stämmer): kompressionsdesign, justerbart kardborrband, strax under knäskålen, öppen rygg, PU, 13 x 5,5 x 3 cm, 0,032 kg, svart, smal profil under sportkläder. Smärta, stabilitet, patellastyrning, belastning, diagnoser, andning och 'sitter säkert' utelämnade. Engelskt typord behålls (R7). Spärrlistan kräver undantag.

### 47616 (10581109571850, k_46ovr5_utkast.json): GODKÄND

Live ACTIVE, varianter L/XL (lager 146) och S/M (lager 0), båda 199 kr och svarta (v1.8: titeln låser ingen storlek; live-titelns 'Stor/Extra stor' tas bort). https://www.gymstick.com/posture-corrector.html (SKU 63069-X, EAN för L/XL stämmer): polyester 85/PU 10/PP 5 %, svart, två storlekar med justering. Mått och vikt korrekt utelämnade (storlek ej angiven). Alla hållnings- och smärtpåståenden utelämnade; 'Hållningskorrigerare' står bara som produktnamn/typord (live-titeln, praxis 2026-11-06 för varunamn). Inte på spärrlistan.

### 47617 (10581110259978, k_46ovr5_utkast.json): RÄTTA

Live ACTIVE, 61137, EAN 6430016906296, lager 113. https://www.gymstick.com/pro-knee-straps.html (SKU och EAN stämmer): elastiska remmar, kardborre, polyester, svart-röd-vit, 162 x 8 x 0,4 cm, 0,4 kg, par, för styrketränare och lyftare. Skydd, stöd, skadeförebyggande och 'secure fit' utelämnade. Rättning: metan använder det engelska namnet som gemen svensk substantivfras ('elastiska knee straps'); svenska 'remmar' som i beskrivningen. Inte på spärrlistan.

| fält | före | efter |
|---|---|---|
| meta | Gymstick Pro Knee Straps är elastiska knee straps av polyester med kardborrstängning. De är 162 cm långa och säljs som par. | Gymstick Pro Knee Straps är elastiska remmar av polyester med kardborrstängning. De är 162 cm långa och säljs som par. |

### 47618 (10581110718730, k_46ovr5_utkast.json): GODKÄND

Live ACTIVE, 61138, EAN 6430016906302, lager 562. https://www.gymstick.com/pro-wrist-straps.html (SKU och EAN stämmer): polyester och gummi, kardborre, svart-röd-vit, 40 x 8 x 0,4 cm, 0,128 kg, par; kategori Weightlifting Gear. Stöd, belastning, prestation, grepp och skydd utelämnade. Engelskt typord behålls (R7). Inte på spärrlistan.

### 47619 (10581111898378, k_46ovr5_utkast.json): GODKÄND

Live ACTIVE, 63067, EAN 6430062510881, lager 115. https://www.gymstick.com/tennis-elbow-support-2-0.html (SKU och EAN stämmer): 'Forearm support', justerbart kardborrband, material 50/10/34/6 %, svart, 0,02 kg, 5 x 45 x 0,9 cm. Längden korrekt utelämnad (42 cm i text, 45 cm i tabell). Smärta, tendontryck, kompression och prestation utelämnade; 'Tennis Elbow' står bara som produktnamn. Spärrlistan kräver undantag.

