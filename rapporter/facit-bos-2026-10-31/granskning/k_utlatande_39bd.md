# Granskningsutlåtande k_39b och k_39d (2026-11-07)

Granskaren har bara läst i Shopify och inte ändrat något där. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient) mot BEST OF SPORTS (`verifiera_butik` gav BEST OF SPORTS). Underlaget är CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.10), BESLUTSLOGG (till och med 2026-11-07), LARDOMAR (bland annat posten 2026-11-05 om rättningar med flera delar), butiksprofilen, `c_granskarprompt.md`, formatet i `k_utlatande_38a.json` och praxis i `k_utlatande_36ab.md`. Alla 34 produkter är ACTIVE och har lager. Ingen annan produkt i butiken har samma SKU. `skrivfil_kontroll.py` gav 0 fel och 0 varningar både på utkasten och på de rättade texterna. `kontrollera_produkttext.py` larmade 'halsa' på 'vitamin' i 39034 och 39036; det är det kända falsklarmet på produktnamn och ingredienser. Standardblocket är exakt som i `b_skriv_24.json` på alla 34. Leveranstidsmeningen finns på exakt de fem som har taggen På beställning (39074, 39075, 39076, 39085 och 39086). Titlar, SEO-titlar och metatexter är unika mot alla `*_utkast*.json`, `*skriv*.json` och live-titlarna.

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_39bd.json`. Varje rättning är ETT sammanhängande före/efter-par per fält, och varje före-text förekommer exakt en gång i utkastet (kontrollerat i python).

## Resultat: 23 GODKÄND, 11 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom |
|---|---|---|---|
| 39027 | 10470924222730 | k_39b_utkast | RÄTTA |
| 39030 | 10470925697290 | k_39b_utkast | GODKÄND |
| 39031 | 10470926156042 | k_39b_utkast | RÄTTA |
| 39033 | 10470934741258 | k_39b_utkast | GODKÄND |
| 39034 | 10470937788682 | k_39b_utkast | RÄTTA |
| 39036 | 10470944014602 | k_39b_utkast | GODKÄND |
| 39037 | 10470944440586 | k_39b_utkast | RÄTTA |
| 39039 | 10471008665866 | k_39b_utkast | GODKÄND |
| 39040 | 10471167623434 | k_39b_utkast | GODKÄND |
| 39041 | 10471170998538 | k_39b_utkast | RÄTTA |
| 39042 | 10471175258378 | k_39b_utkast | GODKÄND |
| 39043 | 10471198490890 | k_39b_utkast | RÄTTA |
| 39044 | 10472213971210 | k_39b_utkast | RÄTTA |
| 39045 | 10472216559882 | k_39b_utkast | GODKÄND |
| 39046 | 10472216985866 | k_39b_utkast | GODKÄND |
| 39048 | 10472226586890 | k_39b_utkast | GODKÄND |
| 39073 | 10472263155978 | k_39d_utkast | GODKÄND |
| 39074 | 10472263287050 | k_39d_utkast | GODKÄND |
| 39075 | 10472263614730 | k_39d_utkast | GODKÄND |
| 39076 | 10472263778570 | k_39d_utkast | GODKÄND |
| 39078 | 10472264106250 | k_39d_utkast | GODKÄND |
| 39079 | 10472264532234 | k_39d_utkast | GODKÄND |
| 39080 | 10472264958218 | k_39d_utkast | GODKÄND |
| 39082 | 10472265384202 | k_39d_utkast | RÄTTA |
| 39083 | 10472265449738 | k_39d_utkast | GODKÄND |
| 39084 | 10472265580810 | k_39d_utkast | RÄTTA |
| 39085 | 10472265875722 | k_39d_utkast | GODKÄND |
| 39086 | 10472268366090 | k_39d_utkast | GODKÄND |
| 39088 | 10472269709578 | k_39d_utkast | RÄTTA |
| 39089 | 10472270037258 | k_39d_utkast | GODKÄND |
| 39092 | 10472282292490 | k_39d_utkast | GODKÄND |
| 39093 | 10472282358026 | k_39d_utkast | GODKÄND |
| 39094 | 10472282718474 | k_39d_utkast | RÄTTA |
| 39096 | 10472285602058 | k_39d_utkast | GODKÄND |

## Rättningar

### 39027 (10470924222730)

Live ACTIVE, lager 8, varianter L/brown 16 679 kr, XL/brown 14 499 kr och en överbliven Default Title med samma SKU/streckkod som XL (2201130288) men pris 16 679 kr och lager 2. v1.9: samma cykel i olika storlek, titel/SEO/text låser varken storlek, färg (Hematite i titel, brown i varianter, utelämnad) eller pris. Alla fakta står i egen källa (ALUXX SL-Grade, SXC32-2 luft, 100 mm, Deore M5100/M4100, 22 växlar, BR-MT200 hydrauliska, Kenda Booster 29x2.4, fästpunkter); Deore är mekanisk. Rättning R7: samma live-ord och taggar (Mountainbike) som 39073 och de skrivna Talon 0/3/4 ('Mountainbike Giant Talon …'); typordet ska vara enhetligt. Modellnamnet enligt källan är 'Talon 1 GE' (29 = hjulstorlek). Till David (ej textfel): Default Title-varianten säljs utan storlek och till XL:s SKU med annat pris; bör rensas i butiken.

| fält | före | efter |
|---|---|---|
| titel | Cykel Giant Talon 29 1 GE | Mountainbike Giant Talon 1 GE, 29 tum |
| seo_title | Cykel Giant Talon 29 1 GE | Mountainbike Giant Talon 1 GE |
| meta | Cykeln Giant Talon 29 1 GE har aluminiumram, 29-tumshjul, 22 växlar med Shimano Deore, hydrauliska skivbromsar och en luftfjädrad gaffel. | Mountainbiken Giant Talon 1 GE har aluminiumram, 29-tumshjul, 22 växlar med Shimano Deore, hydrauliska skivbromsar och en luftfjädrad gaffel. |
| html | sammanhängande bit, 491 tecken (se JSON) | samma bit med ändringen i skälet ovan |

### 39031 (10470926156042)

Live ACTIVE, en variant, lager 6. Fakta i egen källa (80 x 30 x 10/15/20 cm, justerbar i 3 höjder, extra lång, 4 kg, syntetiskt, 'Maxvikt: 100 kg' ordagrann svensk rad). Rättning R4: lastgränsen stod tre gånger (meta, löptext, specifikation); ska stå en gång med 'enligt tillverkaren'. Strukes ur meta och löptext, specifikationsraden får 'enligt tillverkaren'. Meta efter: 108 tecken med verb.

| fält | före | efter |
|---|---|---|
| meta | Stepbrädan Tunturi Aerobic Step Compact mäter 80 x 30 cm och går att justera i tre höjder: 10, 15 och 20 cm. Maxvikt enligt tillverkaren är 100 kg. | Stepbrädan Tunturi Aerobic Step Compact mäter 80 x 30 cm och går att justera i tre höjder: 10, 15 och 20 cm. |
| html | sammanhängande bit, 438 tecken (se JSON) | samma bit med ändringen i skälet ovan |

### 39034 (10470937788682)

Live ACTIVE, lager 1, en variant. Kosttillskott frisläppta (BESLUTSLOGG 2026-11-05: även växtextrakt skrivs med bara fakta); ginseng- och citrusbioflavonoidextrakt står bara som ingredienser. Alla källans påståenden (stress, ökat behov, lättassimilerade) är borta. Rättning: 'metabolismaktivatorer' är ett funktionspåstående (aktiverar ämnesomsättningen) utan godkänt påstående; ersatt i meta, inledning och Innehåll-raden med de faktiska ingredienserna, och gruppnamnet i ingredienslistan ersatt med 'övriga ingredienser'. SEO-titeln får '60 kapslar' så att den inte krockar med syskonet Multipack 120 kapslar (10470937755914, oskrivet). Kontrollskriptets 'halsa' på 'vitamin' är falsklarm (ingrediens).

| fält | före | efter |
|---|---|---|
| seo_title | Kosttillskott Trec Multipack | Kosttillskott Trec Multipack 60 kapslar |
| meta | Trec Multipack innehåller vitaminer, mineraler och metabolismaktivatorer i 60 kapslar. Rekommenderad daglig dos är 2 kapslar. | Trec Multipack innehåller vitaminer, mineraler, ginsengextrakt och citrusbioflavonoidextrakt i 60 kapslar. Rekommenderad daglig dos är 2 kapslar. |
| html | sammanhängande bit, 764 tecken (se JSON) | samma bit med ändringen i skälet ovan |

### 39037 (10470944440586)

Live ACTIVE, lager 5. Fakta: L-tryptofan, 78 %, kapselskal, 2 kapslar, varningar. Källans sömn-, humör- och serotoninbudskap är utelämnat. Rättning: tidpunkten 'helst 30–60 minuter före sänggåendet' i meta och Användning-raden signalerar indirekt sömneffekt för tryptofan (sömnbudskapet i källan); strukes så att inget påstående syns. Meta efter 102 tecken med verb.

| fält | före | efter |
|---|---|---|
| meta | Trec Essensey L-Tryptophan innehåller L-tryptofan i 90 kapslar. Dosen är 2 kapslar dagligen, helst 30–60 minuter före sänggåendet. | Trec Essensey L-Tryptophan innehåller L-tryptofan i 90 kapslar. Rekommenderad daglig dos är 2 kapslar. |
| html | sammanhängande bit, 105 tecken (se JSON) | samma bit med ändringen i skälet ovan |

### 39041 (10471170998538)

Live ACTIVE, lager 1. Två entydiga fakta (höjder 15/20/25 cm, 89 x 39 cm). Rättning R7: egen källa skriver 'Stepbänk' och alla skrivna Toorx-syskon heter 'Stepbänk Toorx …' (Training Step, Advance Step, Active Step); profilens 'stepbräda' gäller bara när källan saknar svenskt ord. Typordet byts i titel, SEO, meta och html (en sammanhängande bit). Unik mot live.

| fält | före | efter |
|---|---|---|
| titel | Stepbräda Toorx Step Pro | Stepbänk Toorx Step Pro |
| seo_title | Stepbräda Toorx Step Pro | Stepbänk Toorx Step Pro |
| meta | Stepbrädan Toorx Step Pro kan användas i tre olika höjder: 15, 20 och 25 cm. Brädan är 89 x 39 cm. | Stepbänken Toorx Step Pro kan användas i tre olika höjder: 15, 20 och 25 cm. Bänken är 89 x 39 cm. |
| html | sammanhängande bit, 287 tecken (se JSON) | samma bit med ändringen i skälet ovan |

### 39043 (10471198490890)

Live ACTIVE, lager 5. Barnprodukt (frisläppt 2026-11-05): bara fakta; aluminium ram/fälgar/vevarmar, V-bromsar, 1 växel, medföljande delar, 12 tum ur titeln, entydig del 'ca 80–100 cm' ur trasig rad som tillverkarens uppgift. Säkerhetsord utelämnade. Rättning R12: SEO-titeln utan storlek blir identisk med den framtida texten för Miss FR 16 tum rosa-lila (10472307458314, oskriven); storleken läggs till som i det skrivna syskonet 'Barncykel Tabou Miss FR 14 tum Rosa-Lila'. 40 tecken.

| fält | före | efter |
|---|---|---|
| seo_title | Barncykel Tabou Miss FR, Rosa-Lila | Barncykel Tabou Miss FR 12 tum Rosa-Lila |

### 39044 (10472213971210)

Live ACTIVE, lager 1. Fakta i egen källa (108 x 41 x 10/15/20 cm, syntetiskt, svart med grönt och grått, 'Maxvikt: 100 kg'). Trasiga materialrader utelämnade. Rättning R4 som 39031: lastgränsen en gång, i specifikationen med 'enligt tillverkaren'; strukes ur meta och löptext. Meta efter 108 tecken.

| fält | före | efter |
|---|---|---|
| meta | Stepbrädan Tunturi Aerobic Power Step har storleken 108 x 41 x 10/15/20 cm och är svart med grönt och grått. Maxvikt enligt tillverkaren är 100 kg. | Stepbrädan Tunturi Aerobic Power Step har storleken 108 x 41 x 10/15/20 cm och är svart med grönt och grått. |
| html | sammanhängande bit, 400 tecken (se JSON) | samma bit med ändringen i skälet ovan |

### 39082 (10472265384202)

Live ACTIVE, lager 3. Fakta i egen källa; maxvikt 120 kg svensk rad en gång. Rättning R1: 'sensorer i handtagen' och 'fungerar även med' står inte i källan, som säger 'Puls mätning via handtagen. Även kompatibel med Bluetooth pulsbälte'.

| fält | före | efter |
|---|---|---|
| html | sammanhängande bit, 90 tecken (se JSON) | samma bit med ändringen i skälet ovan |

### 39084 (10472265580810)

Live ACTIVE, lager 3. Fakta i egen källa; motstridigt antal motståndsnivåer (24/10), '7 kg' och 'Maximal driftsvikt' korrekt utelämnade. Rättning R1: källan säger att sadeln justeras 'i höjdled vertikalt och horisontellt', inte 'i sidled' (sidled vore fel funktion); rättat i löptext och specifikation (en sammanhängande bit).

| fält | före | efter |
|---|---|---|
| html | sammanhängande bit, 662 tecken (se JSON) | samma bit med ändringen i skälet ovan |

### 39088 (10472269709578)

Live ACTIVE, lager 10. Bara produktfakta: BCAA 2:1:1, cola, ingredienser, dosering, varningar. 'Optimalt för kroppen att absorbera' och 'snabb absorption' borta. Rättning R12: SEO-titeln utan smak krockar med kommande texter för syskonen CITRON (10472269250826) och CACTUS (10472269316362); smaken läggs till. 39 tecken.

| fält | före | efter |
|---|---|---|
| seo_title | Kosttillskott Trec BCAA High Speed | Kosttillskott Trec BCAA High Speed Cola |

### 39094 (10472282718474)

Live ACTIVE, lager 5. Barnprodukt: bara fakta; 'Ultralätt' struken ur titeln (löfte), produkttypen oförändrad. Ram, mått och längd 105–115 cm 'enligt tillverkaren' som i skrivna 16 tum Röd-Vit. Rättning R10-format: '16 tums hjul' i meta saknar bindestreck ('16-tums hjul').

| fält | före | efter |
|---|---|---|
| meta | Barncykeln Tabou Rocket Lite MG har ram i magnesium, 16 tums hjul och V-bromsar. Gaffel, fälgar och vevarmar är i aluminium. Stödhjul ingår. | Barncykeln Tabou Rocket Lite MG har ram i magnesium, 16-tums hjul och V-bromsar. Gaffel, fälgar och vevarmar är i aluminium. Stödhjul ingår. |

## Godkända: kort skäl

- **39030**: Live ACTIVE, en variant 14TUSCL249, lager 3. Alla fakta i egen källa (5 kg, svart med grå neopren, justerbara remmar, ventilerande tyg nedre ryggen, ficka för telefon/mp3). Tillagd vikt är ingen lastgräns (R4). Inga löftesord. Unik mot syskonet 10 kg (10472326660362).
- **39033**: Live ACTIVE, lager 1. Alla fakta i egen källa (6–13 tum, 360 grader, stål, 45 x 10 x 10 cm, 1,06 kg, kompatibla modeller). Ingen elektronik. 'enligt tillverkaren' 2 gånger (gräns 2). Inga löften ('ultimata racingspasset' utelämnat).
- **39036**: Live ACTIVE, lager 5. Fakta i egen källa (4000 enheter D3, ingredienser, 1 kapsel, 300 ml vatten, förvaring, inom 3 månader). Källans hälsopåståenden (immunsystem, muskler, ben, tänder, kalcium) och den trasiga raden '300 mg per dag' är utelämnade. Inget påstående syns. 'halsa'-larmet på 'Vitamin' i titel/SEO/meta är falsklarm (produktnamn).
- **39039**: Live ACTIVE, varianter 190/200 samma pris 3 629 kr, lager 2; ingen längd låst. Fakta i egen källa (skinn, PRG 3600/mohair 100 %, airchannel CAP, NIS-platta från fabrik). Trasig bredd '44 m' utelämnad. Typordet följer taggen och skrivna syskon Stiff/Med. Unik SEO (Soft).
- **39040**: Live ACTIVE, en variant MV-2, lager 5. Tunn egen källa (styckvis, Toorx); 2 kg, röd och vinyl står i live-titeln och bekräftas för EAN 8029975992396 hos MediaMarkt BE/NL ('Toorx Fitness Vinyl Dumbbell - per Piece - 2 kg red') och moyo.ua (MV-2). Webbkoll enligt Davids beslut 2026-11-05. Inga löften (golvskydd, rullar inte) tagna från webben.
- **39042**: Live ACTIVE, en variant (525), lager 5. Reflexprodukt (v1.9): bara fakta (sidoreflexklistermärken, ram och fälgar, barnvagn eller hjälm, gula ränder ur titeln). Synlighets- och 'sticker ut'-löften utelämnade. Ingen belysning eller skyddsfunktion.
- **39045**: Live ACTIVE, lager 1. Typordet Hantelstång står i källan ('krompläterad hantelstång'); 38 cm ur live-titeln (värdet saknas i källans tekniska rad). Ø 30 mm, 2 skruvlås, krom, metall i källan. Lastgräns saknas; ingen rad tillagd, i linje med de skrivna Tunturi-hantelstängerna (10472210956554, 10588448129290) som inte behandlats som bärande delar. Vill David räkna hantelstänger som bärande delar läggs 'Maximal lastgräns: Ej känd' till på alla, inte bara här.
- **39046**: Live ACTIVE, lager 5. Fakta i egen källa (parallella stänger, per par, svart/grå, metall, 520 g, plana ytor). Oklara mått (P/L/K) och alla effektord utelämnade. Typordet som skrivna Toorx Push-Up Bars.
- **39048**: Live ACTIVE, 4 längdvarianter samma pris 4 359 kr, lager 5; ingen längd låst. Fakta i egen källa (44/44/44 mm, Aircell Honeycomb, PRG-3600 Grafit, universal, klassisk teknik). Unik mot skrivna Acadia CL Medium.
- **39073**: Live ACTIVE, L/gray och M/gray samma pris 14 679 kr, lager 4. Alla tekniska fakta står i egen källa (ALUXX SL-Grade, GX03V, X1 Coil 100 mm, MT101-2 22/36, Alivio M3120, Deore M592, 18 växlar, BR-MT200, RT-26 180/160, Kenda Booster 29x2,2). Typordet Mountainbike: tagg och skrivna Talon-syskon; produkttypen oförändrad. Knight Shield (live-titel) är Giants gråtonade färgnamn och motsäger inte 'gray'.
- **39074**: Live ACTIVE, lager 1, tagg På beställning, leveranstidsmeningen finns och blocket är exakt. Fakta i egen källa; trasig 'Tunductuator-diameter' och 'skyddar golvet' utelämnade. 'Hålavstånd 50 mm' återges som i det skrivna syskonet 2 x 1,25 kg. Titeln saknar kommat efter 'Plates' jämfört med syskonet, men med kommat blir det 3 kommatecken (decimalkommat räknas av skriptet); lämnas.
- **39075**: Live ACTIVE, lager 1, På beställning: meningen finns. Fakta: 8 mm, 100 % TPE, bärväska och gratis app. Färgen: egen källa har både 'Färg: mint' och den trasiga raden 'MATERIAL: TPEPE FÄRG: PINK'; titel och SKU 14TUSYO077 säger Mint och webbkollen för EAN 8717842035375 kopplar mint-versionen till 14TUSYO077 (tunturi.com, aio.lv, Decathlon), så Mint står. Halkfri, miljö- och ledlöften utelämnade.
- **39076**: Live ACTIVE, lager 2, På beställning: meningen finns. Löpband med elektronik: Davids pilotbeslut tillåter faktatext; varje elektronisk funktion står entydigt i källan (geststyrning via sensorer, knappar, LED, 16 program, puls via handtag eller Bluetooth-pulsbälte, Kinomap med månadsavgift efter provperiod, hållare). Hälso- och effektord utelämnade, liksom hopfällt mått och trasig rad. Ingen användarvikt i källan.
- **39078**: Live ACTIVE, lager 4. Typordet Stuntscooter står i källan. Fakta i källan (aluminiumram, 49 x 11 cm, 110 mm hjul, 3,8 kg); 'Maximal användarvikt: 100 kg' svensk rad en gång. Hållbarhets- och proffsord utelämnade.
- **39079**: Live ACTIVE, lager 3, ingen På beställning-tagg och ingen mening. Fakta i egen källa (95 % monterat, 2,0 hk max 4,5, 0,8–20 km/h, 26 program, Easy-Fold, LED/LCD, 3 manuella lutningar, mått, 54 kg). 'Viskande tyst', halkfri, dämpning och ursprung utelämnade.
- **39080**: Live ACTIVE, lager 3. Typordet Rodd-ergometer behålls (live och källa). Fakta i specifikationsraderna; 'Maximal användarvikt: 150 kg' svensk ordagrann rad, en gång med 'enligt tillverkaren'. Robust/avancerad/ursprung utelämnade.
- **39083**: Live ACTIVE, lager 1. Bänk i faktatextläge (profilen). 'Maximal belastningsvikt: 100 kg' svensk rad med etikett; samma värde i löptexten; återges en gång med 'enligt tillverkaren'. Kvalitets- och stödord utelämnade. Typordet Träningsbänk står i källan.
- **39085**: Live ACTIVE, lager 4, På beställning: meningen finns. Engelsk källa översatt rad för rad; 'Maximum user weight' utelämnad (engelsk lastrad, R4). Modellen C20-R och EAN 8717842036693/23TCR20000 bekräftade i webbsök (velomarket.ee, fitnessmarket.ee, mediamarkt.nl). '+ Tunturi app' struken ur titeln: appen står inte i källan; produkttypen oförändrad. Typordet Crosstrainer: tagg och produkttyp 'Crosstrainers'.
- **39086**: Live ACTIVE, lager 4, På beställning: meningen finns. Titeln 'Löpband Hammer FlyRun 4.0, 24 km/h' skiljer den från skrivna FlyRun 4.0 NorsK (10472334262538, SKU 13017); krocken med oskrivet f_2-utkast räknas inte. Elektronik (LED/LCD, 31 program, elektronisk lutning, Kinomap/Zwift) står i källan. Maxvikt 150 kg svensk rad en gång. 'Bekvämt och säkert', 'förblir stabila' utelämnade.
- **39089**: Live ACTIVE, lager 6. 'Antioxidant' struken ur titeln: påstående, produkttypen (kosttillskott) oförändrad. Fakta i egen källa (30 % NAC, 150 mg per dagsmängd, 1 kapsel, kan innehålla, varningar). 'Ren', 'stabilare form', 'för fysiskt aktiva' utelämnade.
- **39092**: Live ACTIVE, L/green 35 979 kr och M/L/green 35 909 kr, lager 2: v1.9, ingen storlek eller pris låst. Färg och 700x45c som i skrivna Libre-titlar. SRAM Apex utan mekanisk/elektronisk (v1.7). Trasig storleksrad och 'Mekanisk / Hydraulisk' utelämnade. Engelska-varningen 'Green' är Konas färgnamn (praxis k_36a).
- **39093**: Live ACTIVE, lager 1. Fakta i egen källa (2x2 kg, 28,5 x 12,5 x 3 cm, svart/röd, neopren, kardborre, ankel eller handled). 'Bekväm', 'stark och hållbar' utelämnade. Butikens tagg Gymstick rörs inte.
- **39096**: Live ACTIVE, lager 4. Tre entydiga fakta (gelvaddering, 260 x 230 mm, halkskyddsbeläggning på insidan). Halkskydd står ordagrant och återges med 'enligt tillverkaren' (R5, 2 gånger i texten). Komfort- och vibrationslöften utelämnade.

## Avvisade (k_39b_avvisade, k_39d_avvisade)

| nr | id | produkt | bedömning |
|---|---|---|---|
| 39025 | 10470888243466 | Leverlås Tunturi ABS Collar | Avvisningen står: skivstångslås som håller viktskivor på plats räknas som lås och säkerhetsprodukt enligt uppdraget. |
| 39026 | 10470922944778 | Barnhjälm Melon Little Pirate | Avvisningen står: hjälm. |
| 39028 | 10470925074698 | Fjäderklämmor Tunturi Spring Collar | Avvisningen står: lås. Vikten anges både i gram och i liter i källan. |
| 39029 | 10470925238538 | Tunturi PE Kettlebell 12 kg | Avvisningen står: källan säger 16 kg och 12 kg, PVC mot titelns PE och produktkoden 14TUSCL183 mot SKU 14TUSCL182. |
| 39032 | 10470929334538 | Pedaler Giant Pinner Comp | Avvisningen står, men skälet är delvis fel. Pedaler är tillåtna som bärande delar enligt v1.10 (raden 'Ej känd', klosspedaler godkända 2026-11-05). Det som hindrar är varianterna: Default Title (SKU 230000103, 629 kr) och 'sinine' (blå, SKU 230000104, 489 kr). Det går inte att se att Default Title är samma pedal i en annan färg (v1.9). Kan släppas om färgen för 230000103 bekräftas. |
| 39035 | 10470943621386 | Trec S.A.W. ('Vitaminpulver') | Avvisningen står: titeln säger vitaminpulver medan texten beskriver pre-workout med koffein, och ingredienslistan stämmer inte med texten. Profilskälet 'koffein utanför' gäller inte längre (BESLUTSLOGG 2026-11-05), men motsägelsen räcker. |
| 39038 | 10470944702730 | Essensey Multivit for Him + Maca | **Avvisningsskälet är fel, och produkten kan släppas.** BESLUTSLOGG 2026-11-05 säger att potens- och växtextraktprodukter skrivs med bara produktfakta, och Tribido Max släpptes 2026-11-06. Källan har en full ingredienslista, 10 mg macaextrakt per dagsdos, dos och varningar. Nytt utkast med bara fakta: 'fertilitet' och 'sexuell aktivitet' utelämnas, och de felaktiga taggarna Herrcykel och Trek rörs inte i textskrivningen. |
| 39047 | 10472221802762 | Löpband Tunturi Cardio Fit T30 | Avvisningen står, men skälet är delvis fel: löpband med elektronik får skrivas med faktatext. Hindret är varianten 'must' (SKU 24TCFT3000) som har priset **0,00 kr** och lager 1. Priset måste rättas i butiken innan produkten skrivs. Taggen Gymstick ser felaktig ut. |
| 39077 | 10472263844106 | Viktskivor Tunturi Aerobic Plates 0,5 kg | Avvisningen står: varianterna 14TUSCL290 (69 kr) och 14TUSCL291 (149 kr) är olika artiklar (v1.9). |
| 39081 | 10472265056522 | Gymnastikboll Tunturi Gymball 75 cm | **Avvisningen kan hävas.** Egen källa säger 'grönaktig' och titeln Off-white, men webbkollen för exakt EAN 8717842035672 och SKU 14TUSFU334 ([Decathlon IE](https://www.decathlon.ie/sku/cc7b37d7-05de-41b8-8bfe-f6dea79cb931.html)) anger off-white, 75 cm, PVC, 1,2 kg och 220 kg. Färgen Off-white gäller alltså (R1 v1.6/v1.7). 'Bärförmåga: 220 kg' är en ordagrann svensk rad och skrivs en gång med 'enligt tillverkaren'. 'Anti Burst' ska bort ur titeln, eftersom 'sprängsäker' är ett säkerhetsord (R4/R5). Bara 75 cm säljs, så storlekstabellen utelämnas. Nytt utkast behövs. |
| 39087 | 10472269611274 | Trec Rhodiola Rosea ('Adaptogen') | **Avvisningsskälet är fel.** Växtextrakt skrivs med bara fakta (BESLUTSLOGG 2026-11-05), och bara ashwagandha är uttryckligen pausad. Kan släppas med ingredienser (3 % rosaviner, 1 % salidrosid), 1 kapsel och förvaring. 'Adaptogen' stryks ur titeln, och alla påståenden om trötthet, stress, koncentration och sexuell funktion utelämnas. Den oklara raden '3 mg per dag' utelämnas. Rekommendation: låt David bekräfta, eftersom produkten är ett adaptogen av samma slag som ashwagandha. |
| 39090 | 10472270987530 | Trec Essensey Gotu Kola | **Avvisningsskälet är fel.** Produkten kan släppas med bara fakta: 43 % Centella asiatica-extrakt, 1 kapsel och varningar. Påståendena om cirkulation, matsmältning, kognitiv funktion och sårläkning utelämnas. Typordet blir Kosttillskott i stället för live-ordet 'Vitaminkapslar' (produkten innehåller inga vitaminer). |
| 39091 | 10472276984074 | Tunturi Akupressurmadrass | Avvisningen står: akupressur (R6, utanför tills vidare). |
| 39095 | 10472285569290 | Sadelöverdrag Azimut THIN gel | Avvisningen står: beskrivningen är tom, och webbkollen gav ingen sida för exakt modell (R3). |

## Frågor till David

1. **39087 Rhodiola och 39038 Maca:** ska de skrivas med bara fakta enligt linjen från 2026-11-05/06? Rekommendation: ja för Maca och Gotu Kola. För Rhodiola bör David svara uttryckligen, eftersom ashwagandha är pausad.
2. **39027 Talon 1 GE:** varianten Default Title har samma SKU som XL men ett annat pris (16 679 mot 14 499 kr). Den bör tas bort i butiken. Texten påverkas inte.
3. **39047 T30:** varianten 'must' har priset 0 kr. Rätta priset innan produkten skrivs.
4. **Hantelstänger (39045):** ska de räknas som bärande delar med raden 'Maximal lastgräns: Ej känd'? Skrivna syskon har inte raden. Rekommendation: nej, behåll nuvarande praxis.

Webbkällor: [MediaMarkt NL MV-2](https://www.mediamarkt.nl/en/product/_mv-2-149439121.html), [MediaMarkt BE MV-2](https://www.mediamarkt.be/en/product/_toorx-mv-2-dumbbell-149439121.html), [moyo.ua MV-2](https://www.moyo.ua/gantel_dlya_fitnesa_toorx_vinyl_2kg_mv-2_/645008.html), [velomarket.ee C20-R](https://velomarket.ee/en/products/elliptical-trainer-tunturi-signature-c20-r), [fitnessmarket.ee C20-R](https://fitnessmarket.ee/en/shop/elliptical-trainer-tunturi-signature-c20-r), [aio.lv Yogamat 8 mm Mint 14TUSYO077](https://aio.lv/en/product--tunturi-14tusyo077--12240961.md), [Decathlon IE Gymball 75 cm off-white](https://www.decathlon.ie/sku/cc7b37d7-05de-41b8-8bfe-f6dea79cb931.html).
