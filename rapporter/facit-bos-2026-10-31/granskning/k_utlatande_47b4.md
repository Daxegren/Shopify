# Granskningsutlåtande k_47b4: Giant-cyklar med ramstorlek ur artikelnumret (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (Giant/Liv: ramstorlek ur artikelnumrets slutsiffra; aktiva produkter utan text får faktatext), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och `k_utlatande_47a1.md`, och formatet i `k_utlatande_43.json`.

Alla tio utkast är ACTIVE, har en variant (Default Title), lager 0 och taggen På beställning. Leveranstidsmeningen finns i standardblocket på alla, och standardblocket är i övrigt exakt som i `b_skriv_24.json`. Titlarna har 49–68 tecken och 2 kommatecken, SEO-titlarna 36–42 tecken och metatexterna 125–138 tecken med verb. "Passar för" finns på alla, och ingen text har mer än en "enligt tillverkaren". Ramstorleken är härledd ur slutsiffran (3=XS, 4=S, 5=M, 7=L, 8=XL). I alla tio stämmer den med storleken och längdintervallet i produktens egen storlekstabell, och ingen text nämner andra storlekar. Varje produkts SKU och EAN söktes i butiken. Ingen annan produkt har samma SKU eller streckkod, så ingen är exakt dubblett (R12a, beslut 2026-11-05). Titel, SEO och meta är unika inom batchen, mot alla andra utkast- och skrivfiler i `vag2_skriv` och mot butikens titlar (sökning på Trinity, Defy Advanced, Propel Advanced, Anthem Advanced, Talon och XTC Advanced). Det finns inga cirkulära inledningar. Varje rättning är ETT sammanhängande före/efter-par per fält, och före-texten förekommer exakt en gång i utkastet (kontrollerat i python).

**Löften:** alla texter genomsöktes efter prestanda-, säkerhets-, kvalitets-, komfort- och hållbarhetsord (lätt, snabb, styv, aerodynamisk, bekväm, trygg, pålitlig, hållbar, effektiv, minskar trötthet, kontroll). Inget sådant finns. Elektronisk växling anges bara som modellnamn (SRAM Rival AXS (D2), Shimano 105 Di2) eller som "elektronisk växling", vilket v1.7 tillåter. Ingen text påstår mekanisk växling eller nämner batteri eller räckvidd.

**Lastgräns (v1.10):** ingen av de tio texterna nämner lastgräns. Samma dag skrev batch k_47a1 raden "Maximal lastgräns: Ej känd" och meningen "Maximal lastgräns är inte känd." på alla cyklar (praxis från k_41; till exempel 48003 Giant TCR). Därför är alla tio RÄTTA och får samma tillägg.

**Spärrlistan:** `skrivfil_kontroll.py` på de rättade texterna gav 0 formatfel men 8 spärrfel. 48601, 48602, 48605, 48606, 48607, 48608, 48609 och 48610 står i den aktiva spärren `tidigare-avvisade-2026-11-04` men inte i `undantag-2026-11-05`. De stoppas tills en undantagsrad med hänvisning till Davids beslut 2026-11-08 läggs till (bara tillägg; R14, samma som i k_47a1–k_47b3). 48603 och 48604 finns redan i undantaget och släpps.

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_47b4.json`.

## Resultat: 0 GODKÄND, 10 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 48601 | 10488318427402 | k_47b4_utkast.json | RÄTTA | html |
| 48602 | 10494910431498 | k_47b4_utkast.json | RÄTTA | html |
| 48603 | 10502528106762 | k_47b4_utkast.json | RÄTTA | html |
| 48604 | 10565633769738 | k_47b4_utkast.json | RÄTTA | html |
| 48605 | 10507440783626 | k_47b4_utkast.json | RÄTTA | html |
| 48608 | 10530216771850 | k_47b4_utkast.json | RÄTTA | html |
| 48606 | 10523486880010 | k_47b4_utkast.json | RÄTTA | html |
| 48607 | 10530215559434 | k_47b4_utkast.json | RÄTTA | html |
| 48609 | 10561347748106 | k_47b4_utkast.json | RÄTTA | html |
| 48610 | 10561355907338 | k_47b4_utkast.json | RÄTTA | html |

## Rättningar

Alla tio får i `html` meningen "Maximal lastgräns är inte känd." sist i inledningen och raden `<li>Maximal lastgräns: Ej känd</li>` före artikelnumret. 48601 och 48602 får dessutom "i ramen" struket i Passar för. Det står inte i källan, som bara säger "det integrerade vätskesystemet och förvaringsfacket" (R1). Före och efter står ordagrant i JSON-filen. Varje par börjar vid `</p><h2>Passar för</h2>` och slutar med `<li>Artikelnummer: …</li>`.

## Avvisade (k_47b4_avvisade.json)

Alla fyra avvisningar står sig, och ingen lyfts ur.

- 48612 (10472323023114, hunddörr Amladcykler): live-källan är en enda mening om en dörrpanel för Ultimate Curve och Deluxe. Varken hund eller sidöppning styrks. Rätt avvisad (R3, tunn källa).
- 48613 (10462767284490, Continental Ride Tour 42-622): live-beskrivningen är tom och återförsäljarna motsäger varandra. Rätt avvisad.
- 48614 (10494696161546, Look X-Track): live-beskrivningen är tom, EAN-kopplingen finns bara hos återförsäljare och typordet saknas ("Pedal blocks"). Rimligt avvisad; den kan skrivas om David godkänner typordet "Pedalklossar".
- 48611 (10561356398858, Propel Advanced 2 Vit, SKU 1074031103): slutsiffran 3 betyder XS, men källans tabell har bara S–XL. Rätt avvisad (gissa aldrig).

## Mönster

- Storlekarna är rätt härledda och stämmer med produktens egen tabell. De skrivna syskonen (7074, 7075, 6057, 7091, 7101, 6028, 7086) är andra storlekar, och titlarna skiljer sig genom storleken.
- Lastgränsraden saknas i hela batchen, trots att praxis sedan k_41/k_47a1 är "Ej känd" på cyklar.
- Ett påhittat tillägg: "i ramen" om vätskesystem och förvaringsfack på Trinity (48601, 48602).
- Färgnamnen kommer från live-titeln. 48609 har Metallicblå i titeln (som 6028) och Metallic Blue i texten. Det rättas inte.
- Utkastarens notering om 7057 stämmer inte live. 7057 (10472435024138, SKU 1074029107) heter fortfarande "Road bike …" och saknar texter-klara. Det påverkar inte 48604.

## Frågor till David

1. Åtta produkter står i spärren `tidigare-avvisade-2026-11-04`. En undantagsrad som bygger på ditt beslut 2026-11-08 behövs innan skrivfilen byggs.
2. Trinity Advanced SL 2 i samma färg har olika pris i olika storlekar (L 100 669 kr, S 117 969 kr, XS 134 719 kr). Texten påverkas inte, men priserna kan behöva kontrolleras.
3. Look X-Track (48614): godkänner du typordet "Pedalklossar"?

## Skäl per produkt

### 48601 (10488318427402): RÄTTA

Live ACTIVE, en variant (Default Title), lager 0, tagg På beställning; leveranstidsmeningen finns i standardblocket. SKU 1138002107, EAN 4711291140318, 100 669 kr. Slutsiffra 7 = L (Giant-regeln 2026-11-08); källans L (56,5 cm) ca 181–191 cm. Ram/gaffel Advanced SL-klassad komposit 12x142/12x100, SRAM Rival AXS (D2) 24, SRAM S-900 Aero hydrauliska, CADEX Aero 700x25c (26,5 mm) fällbart, fyra sadelstolpspositioner och 24 styrinställningar: allt ur egen svensk källa. 'SL-grade' följer det skrivna syskonet 7074. Elektronisk växling bara som modellnamn (v1.7). 558 g, 5,9 W, aerodynamik, 'pålitlig bromskraft', 'skräddarsys perfekt', 'världens största' rätt utelämnade. (R1): källan säger 'det integrerade vätskesystemet och förvaringsfacket' men inte att de sitter i ramen; 'i ramen' stryks. Inte dubblett: XS (1138002103) är skriven som 7074, M (…105) är DRAFT; SKU/EAN finns inte på någon annan produkt. Unik titel/SEO/meta. Spärrlistan: produkten står i den aktiva spärren tidigare-avvisade-2026-11-04; skrivfil_kontroll.py stoppar den tills en undantagsrad (bara tillägg) med hänvisning till Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt. RÄTTA (v1.10, praxis k_41/k_47a1 för cyklar): egen källa saknar lastgräns och utkastet anger ingen webbkälla för exakt artikelnummer/EAN, så raden Ej känd krävs (samma som 48003 m.fl. i k_47a1); meningen 'Maximal lastgräns är inte känd.' läggs sist i inledningen och raden 'Maximal lastgräns: Ej känd' före artikelnumret. De två ändringarna står i ETT sammanhängande före/efter-par.

### 48602 (10494910431498): RÄTTA

Live ACTIVE, en variant (Default Title), lager 0, tagg På beställning; leveranstidsmeningen finns i standardblocket. SKU 1138002104, EAN 4711291140295, 117 969 kr. Slutsiffra 4 = S; källans S (50,8 cm) ca 166–176 cm. Övriga uppgifter som 48601 och stämmer mot egen källa ('vikbart', '24 olika styreinställningar'). Samma RÄTTA (R1): 'i ramen' finns inte i källan. Inte dubblett (annan storlek än 48601 och 7074; SKU/EAN unika i butiken). Spärrlistan: produkten står i den aktiva spärren tidigare-avvisade-2026-11-04; skrivfil_kontroll.py stoppar den tills en undantagsrad (bara tillägg) med hänvisning till Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt. RÄTTA (v1.10, praxis k_41/k_47a1 för cyklar): egen källa saknar lastgräns och utkastet anger ingen webbkälla för exakt artikelnummer/EAN, så raden Ej känd krävs (samma som 48003 m.fl. i k_47a1); meningen 'Maximal lastgräns är inte känd.' läggs sist i inledningen och raden 'Maximal lastgräns: Ej känd' före artikelnumret. De två ändringarna står i ETT sammanhängande före/efter-par.

### 48603 (10502528106762): RÄTTA

Live ACTIVE, en variant (Default Title), lager 0, tagg På beställning; leveranstidsmeningen finns i standardblocket. SKU 1031021144, EAN 4711291228078, 55 579 kr. Slutsiffra 4 = S; källans S (44,5 cm) ca 166–174 cm. Komposit av Advanced-kvalitet 12x142/12x100, OverDrive-styrrör, Shimano 105 Di2 24, Shimano 105 hydrauliska, SLR 2 40 Carbon Disc, Gavia Fondo 0 700x32c (33,5 mm), fästpunkter för vattenflaska och tillbehör: allt ur egen källa. 'Elektronisk växling' i Passar för är tillåtet enligt v1.7 (Di2 ordagrant, ingen mekanisk växling, inget batteri). 'Lätt', 'bekväm', 'jämnar ut', 'minskar trötthet' rätt utelämnade. Syskonet 7075 (M, …145) är skrivet; 147 är ARKIVERAD. Unik titel/SEO/meta. Spärrlistan: står i tidigare-avvisade-2026-11-04 men även i undantag-2026-11-05; skrivfil_kontroll.py släpper den. RÄTTA (v1.10, praxis k_41/k_47a1 för cyklar): egen källa saknar lastgräns och utkastet anger ingen webbkälla för exakt artikelnummer/EAN, så raden Ej känd krävs (samma som 48003 m.fl. i k_47a1); meningen 'Maximal lastgräns är inte känd.' läggs sist i inledningen och raden 'Maximal lastgräns: Ej känd' före artikelnumret. De två ändringarna står i ETT sammanhängande före/efter-par.

### 48604 (10565633769738): RÄTTA

Live ACTIVE, en variant (Default Title), lager 0, tagg På beställning; leveranstidsmeningen finns i standardblocket. SKU 1074029108, EAN 4711291264656, 67 389 kr. Slutsiffra 8 = XL; källans XL (59,5 cm) ca 189–199 cm. Advanced-grade composite 12x142/12x100, OverDrive Aero, Shimano 105 Di2 24, 105 Di2 hydrauliska, SLR 2 50 Carbon Disc [F]50/[R]50, Gavia Course 0 700x28c vikbart, fästpunkter: allt ur egen källa. All aero-, hastighets-, styvhets- och komfortmarknadsföring utelämnad. Skrivna syskonet 6057 (…106) har titel utan storlek; 7057 (…107) är inte skriven live ('Road bike …'), 10488318329098 (…104/105) oskriven. Unik titel/SEO/meta. Spärrlistan: står i tidigare-avvisade-2026-11-04 men även i undantag-2026-11-05; skrivfil_kontroll.py släpper den. RÄTTA (v1.10, praxis k_41/k_47a1 för cyklar): egen källa saknar lastgräns och utkastet anger ingen webbkälla för exakt artikelnummer/EAN, så raden Ej känd krävs (samma som 48003 m.fl. i k_47a1); meningen 'Maximal lastgräns är inte känd.' läggs sist i inledningen och raden 'Maximal lastgräns: Ej känd' före artikelnumret. De två ändringarna står i ETT sammanhängande före/efter-par.

### 48605 (10507440783626): RÄTTA

Live ACTIVE, en variant (Default Title), lager 0, tagg På beställning; leveranstidsmeningen finns i standardblocket. SKU 1074031104, EAN 4711291264892, 47 559 kr. Slutsiffra 4 = S; källans S (50,5 cm) ca 165–175 cm. Advanced-grade composite, OverDrive Aero, Shimano 105 24, 105 hydrauliska, P-A1 Disc legering, Gavia Course 0 700x28c fällbart, fästpunkter för flaskhållare: allt ur egen källa. Marknadsföring utelämnad. Skrivna syskonet 7091 (L, …107) har annan titel; …105 ARKIVERAD; …103 rätt avvisad (48611). Unik titel/SEO/meta. Spärrlistan: produkten står i den aktiva spärren tidigare-avvisade-2026-11-04; skrivfil_kontroll.py stoppar den tills en undantagsrad (bara tillägg) med hänvisning till Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt. RÄTTA (v1.10, praxis k_41/k_47a1 för cyklar): egen källa saknar lastgräns och utkastet anger ingen webbkälla för exakt artikelnummer/EAN, så raden Ej känd krävs (samma som 48003 m.fl. i k_47a1); meningen 'Maximal lastgräns är inte känd.' läggs sist i inledningen och raden 'Maximal lastgräns: Ej känd' före artikelnumret. De två ändringarna står i ETT sammanhängande före/efter-par.

### 48608 (10530216771850): RÄTTA

Live ACTIVE, en variant (Default Title), lager 0, tagg På beställning; leveranstidsmeningen finns i standardblocket. SKU 1074031108, EAN 4711291264939, 47 559 kr. Slutsiffra 8 = XL; källans XL (59,5 cm) ca 189–199 cm. Samma uppgifter som 48605, alla i egen källa ('Växelförare: Shimano 105', 'vikbart'). Unik mot 48605 och 7091. Spärrlistan: produkten står i den aktiva spärren tidigare-avvisade-2026-11-04; skrivfil_kontroll.py stoppar den tills en undantagsrad (bara tillägg) med hänvisning till Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt. RÄTTA (v1.10, praxis k_41/k_47a1 för cyklar): egen källa saknar lastgräns och utkastet anger ingen webbkälla för exakt artikelnummer/EAN, så raden Ej känd krävs (samma som 48003 m.fl. i k_47a1); meningen 'Maximal lastgräns är inte känd.' läggs sist i inledningen och raden 'Maximal lastgräns: Ej känd' före artikelnumret. De två ändringarna står i ETT sammanhängande före/efter-par.

### 48606 (10523486880010): RÄTTA

Live ACTIVE, en variant (Default Title), lager 0, tagg På beställning; leveranstidsmeningen finns i standardblocket. SKU 1008012107, EAN 4711291210561, 88 749 kr. Slutsiffra 7 = L; källans L (46,5 cm) ca 179–188 cm. Advanced SL-klass komposit fram- och baktriangel, 120 mm FlexPoint Pro, flip chip, 12x148, Sid Select+ 3P 120 mm fjärrlåsning, SidLuxe Select+, Eagle 90 mekanisk 12, SLX BR-M6220 hydrauliska, Aspen 29x2.4 vikbara slanglösa: allt ur egen källa; 'kolfiberram' i meta står i källan. Typordet Mountainbike stöds av källan ('en mountainbike') och det skrivna syskonet 7101 (R7). 'Exceptionell lätthet', 'maximal kraftöverföring', 'tävlingsklar', 'pålitlig bromskraft' utelämnade. Syskonet 7101 (XL) skrivet; unik titel/SEO/meta. Spärrlistan: produkten står i den aktiva spärren tidigare-avvisade-2026-11-04; skrivfil_kontroll.py stoppar den tills en undantagsrad (bara tillägg) med hänvisning till Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt. RÄTTA (v1.10, praxis k_41/k_47a1 för cyklar): egen källa saknar lastgräns och utkastet anger ingen webbkälla för exakt artikelnummer/EAN, så raden Ej känd krävs (samma som 48003 m.fl. i k_47a1); meningen 'Maximal lastgräns är inte känd.' läggs sist i inledningen och raden 'Maximal lastgräns: Ej känd' före artikelnumret. De två ändringarna står i ETT sammanhängande före/efter-par.

### 48607 (10530215559434): RÄTTA

Live ACTIVE, en variant (Default Title), lager 0, tagg På beställning; leveranstidsmeningen finns i standardblocket. SKU 1008012105, EAN 4711291210554, 88 749 kr. Slutsiffra 5 = M; källans M (42 cm) ca 171–180 cm. Samma uppgifter som 48606 (källan skriver 'SL-grade'; texten 'SL-klass' som 7101). Unik mot 48606 och 7101. Spärrlistan: produkten står i den aktiva spärren tidigare-avvisade-2026-11-04; skrivfil_kontroll.py stoppar den tills en undantagsrad (bara tillägg) med hänvisning till Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt. RÄTTA (v1.10, praxis k_41/k_47a1 för cyklar): egen källa saknar lastgräns och utkastet anger ingen webbkälla för exakt artikelnummer/EAN, så raden Ej känd krävs (samma som 48003 m.fl. i k_47a1); meningen 'Maximal lastgräns är inte känd.' läggs sist i inledningen och raden 'Maximal lastgräns: Ej känd' före artikelnumret. De två ändringarna står i ETT sammanhängande före/efter-par.

### 48609 (10561347748106): RÄTTA

Live ACTIVE, en variant (Default Title), lager 0, tagg På beställning; leveranstidsmeningen finns i standardblocket. SKU 1095008284, EAN 4711291189768, 15 169 kr. Slutsiffra 4 = S; källans S (38 cm) ca 163–172 cm. ALUXX-grade aluminium, SXC32-3 RL spiralfjäder 15x110 stålstyrrör 100 mm slaglängd, Shimano Cues 10, Tektro HDC M275 hydrauliska, Rekon Race 29x2.4 med stålwire, fästpunkter för stänkskärmar: allt ur egen källa; 'fjädergaffel' stöds av 'fjädring fram'. 'Lättare och mer hållbar', 'trygg cykling', 'bättre grepp' utelämnade. Syskonet 6028 (…285/…287) skrivet; unik titel/SEO/meta. Anmärkning utan rättning: titeln har Metallicblå (som 6028) och texten Metallic Blue (live-färgnamnet). Spärrlistan: produkten står i den aktiva spärren tidigare-avvisade-2026-11-04; skrivfil_kontroll.py stoppar den tills en undantagsrad (bara tillägg) med hänvisning till Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt. RÄTTA (v1.10, praxis k_41/k_47a1 för cyklar): egen källa saknar lastgräns och utkastet anger ingen webbkälla för exakt artikelnummer/EAN, så raden Ej känd krävs (samma som 48003 m.fl. i k_47a1); meningen 'Maximal lastgräns är inte känd.' läggs sist i inledningen och raden 'Maximal lastgräns: Ej känd' före artikelnumret. De två ändringarna står i ETT sammanhängande före/efter-par.

### 48610 (10561355907338): RÄTTA

Live ACTIVE, en variant (Default Title), lager 0, tagg På beställning; leveranstidsmeningen finns i standardblocket. SKU 1119022145, EAN 4711291235984, 39 649 kr. Slutsiffra 5 = M; källans M (43,1 cm) ca 171–180 cm. Komposit av avancerad kvalitet 12x148, Crest SL 100 mm fjärrlåsning 44 mm offset 15x110, Shimano SLX 12, BR-MT500 hydrauliska, Rekon Race 29x2.4/29x2.25 vikbara TLR EXO: allt ur egen källa. 'Responsiv', 'maximal effektivitet', 'mjukare åktur' utelämnade. Syskonet 7086 (…144/…147) skrivet; unik titel/SEO/meta. Spärrlistan: produkten står i den aktiva spärren tidigare-avvisade-2026-11-04; skrivfil_kontroll.py stoppar den tills en undantagsrad (bara tillägg) med hänvisning till Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt. RÄTTA (v1.10, praxis k_41/k_47a1 för cyklar): egen källa saknar lastgräns och utkastet anger ingen webbkälla för exakt artikelnummer/EAN, så raden Ej känd krävs (samma som 48003 m.fl. i k_47a1); meningen 'Maximal lastgräns är inte känd.' läggs sist i inledningen och raden 'Maximal lastgräns: Ej känd' före artikelnumret. De två ändringarna står i ETT sammanhängande före/efter-par.
