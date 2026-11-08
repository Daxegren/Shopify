# Granskningsutlåtande k_46sak5: aktiva produkter i tidigare utanför-kategorier (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan texter-klara får faktatext även i säkerhets-, barn- och övriga tidigare utanför-kategorier), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och k_46sak2–4 samt formatet i `k_utlatande_43.json`.

Alla 11 utkast och alla 13 avvisade är ACTIVE. Standardblocket är exakt rätt på alla; leveranstidsmeningen finns på exakt de tre som har taggen På beställning (46401, 46403, 46409). Efter rättning: titel ≤70 tecken och ≤2 kommatecken, SEO ≤43, meta 117–155 tecken med verb, "Passar för" på alla, högst ett "enligt tillverkaren" per text. Titlar, SEO-titlar och metatexter jämfördes mot alla JSON-filer under `rapporter/` och mot butiken (sökning på Rideoo, AnyTour, Allure, Relay, Holler, Sunny, Kid Pro, Bookman, Bormio, GB3, Minnie samt SKU/EAN). `skrivfil_kontroll.py` på de rättade texterna ger bara 4 FEL: 46404–46407 står i spärren `utanfor-tills-vidare-2026-11-04` (hjälm/barn) och behöver en undantagspost med beslutet 2026-11-08 innan de skrivs (R14). Varje rättning är ETT sammanhängande före/efter-par per fält, och varje före-text förekommer exakt en gång i utkastet (kontrollerat i python).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_46sak5.json`.

## Resultat: 4 GODKÄND, 7 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 46401 | 10494941692170 | k_46sak5_utkast.json | GODKÄND | – |
| 46402 | 10515754516746 | k_46sak5_utkast.json | RÄTTA | titel, seo_title, meta, html |
| 46403 | 10523488387338 | k_46sak5_utkast.json | RÄTTA | titel, seo_title, html |
| 46404 | 10530129477898 | k_46sak5_utkast.json | RÄTTA | meta, html |
| 46405 | 10541372277002 | k_46sak5_utkast.json | GODKÄND | – |
| 46406 | 10554353910026 | k_46sak5_utkast.json | RÄTTA | html |
| 46407 | 10577688527114 | k_46sak5_utkast.json | RÄTTA | seo_title, html |
| 46408 | 10548248215818 | k_46sak5_utkast.json | RÄTTA | seo_title, meta, html |
| 46409 | 10548295368970 | k_46sak5_utkast.json | GODKÄND | – |
| 46410 | 10581106917642 | k_46sak5_utkast.json | GODKÄND | – |
| 46411 | 10624081527050 | k_46sak5_utkast.json | RÄTTA | titel, meta, html |

## Löften (hälsa, säkerhet, skydd, utveckling, prestanda, kvalitet)

Alla texter genomsöktes efter tydliga och subtila löften (säker, skydd, synlig, trafik, trygg, stabil, pålitlig, robust, hållbar, komfort, bekväm, antibakteriell, antimikrobiell, fukt, lukt, kylning, vidhäftning, räckvidd, effektiv, uthållighet, perfekt). Efter rättning finns inget kvar: antibakteriell/antimikrobiell (46406, 46407), fukt- och lukttransport (46404) och vidhäftning i regn, snö och hagel (46408) stryks. Kvar står bara ordagranna fakta: MIPS och Direct Flow Cooling som systemnamn, reflekterande element och reflexrand som utrustning, lastgräns som svensk rad med etikett (46402 70 kg, 46410 120 kg, en gång enligt tillverkaren) och "Ej känd" för Bormio (v1.10).

## Avvisade (k_46sak5_avvisade.json)

Alla 13 avvisningar står; ingen är uppenbart fel. 46501 och 46513 har redan vår text (texter-klara saknas på 46501, se frågor). 46502 (Ding-A-Ling Flick) och 46509 (shaker) har tom källa. 46503 (ryggstöd) och 46504 (trampolin) har bara löften och oklara varianter. 46505–46508 och 46510–46512 har varianter som är olika artiklar eller motsägande SKU (R3, v1.9).

## Frågor till David

1. Spärrlistan: 46404–46407 (hjälmar/barn) stoppas av `utanfor-tills-vidare-2026-11-04`. En undantagspost med beslutet 2026-11-08 behövs innan skrivfilen byggs (samma som för k_46sak2–4).
2. Rideoo 46402: färgen Rosa bygger på en återförsäljare (scootshop.net) som kopplar EAN 4751036030139 till Pink; övriga EAN på samma sida stämmer med butikens skrivna färger. Säg till om du hellre vill att produkten väntar.
3. Minnie Flowers Retro 46411: egen källa säger diameter 55 mm, medan syskonet Minnie Retro anger 80 mm diameter och 55 mm höjd. Bör kontrolleras mot den fysiska varan.
4. Damcykel Romet Gazela 0 (10523488190730, avvisad 46501) har redan vår text men saknar taggen texter-klara.
5. Giant AnyTour CS 2 GB (46403) och Liv Allure CS 2 GB (46401) har varianter med olika pris för samma eller närliggande artikel (22 399/19 479 kr för samma SKU). Troligen prisfel i butiken; texten berörs inte.

## Skäl och rättningar per produkt

### 46401 (10494941692170, k_46sak5_utkast.json): GODKÄND

Live ACTIVE, lager 2, tagg På beställning (leveranstidsmeningen finns). Två varianter: Default Title 3005010114/EAN …0460 22 889 kr och M / purple 3005010115/EAN …0477 19 909 kr; enligt Giant/Liv-regeln 2026-11-08 är det S och M i olika färg av samma modell, så v1.9 gäller (lager > 0) och titel, SEO och text låser varken färg, storlek eller pris. Alla uppgifter (ALUXX-aluminium, Gates remdrift, Nexus 8, MT200 hydrauliska, P-X3 700x45C, stöd/stänkskärmar/pakethållare/ramlås/ljus, stadskörning och lättare turer) står i egen källa; pålitlig, stabil, underhållsfri, säkerhet och trygghet rätt utelämnade. Pakethållaren nämns bara som ingående del, ingen lastuppgift. Ingen dubblett (Liv Allure RS 2 GB är annan modell).

### 46402 (10515754516746, k_46sak5_utkast.json): RÄTTA

Live ACTIVE, lager 2, en variant SKU 4751036030139 (inget EAN-fält). Uppgifterna (hopfällbar, justerbart styre, PU-hjul 120 mm, ABEC-9, 3,4 kg, 4–7 år) står i egen källa; 'Maximal belastning: upp till 70 kg' är svensk rad med etikett och enhet och står en gång enligt tillverkaren i texten (R4, som de skrivna syskonen). LED-belysning rätt struken. RÄTTA: (1) Samma serie finns skriven i Turkos, Svart, Salmon, Blå och Lila som 'Sparkcykel Rideoo 120 City, <färg>' från samma typ av live-titel ('Scooter Rideoo 120 City Scooter …'), så typordet görs enhetligt (R7) och titeln måste skilja färgen (David 2026-11-05). EAN 4751036030139 är enligt scootshop.net (https://www.scootshop.net/mestske-kolobezky/folding-scooters/rideoo/) 'Rideoo 120 City Scooter Pink' (kod 101070); samma sida anger Blue 4751036030122, Turquoise 4751036030733 och Purple 4751036030740, vilket stämmer med butikens skrivna syskon, så färgen Rosa är entydig för exakt artikeln (v1.6/v1.7, återförsäljare). Ingen rosa variant finns skriven, ingen dubblett. (2) 'styrehöjd' ändras till syskonens 'höjdjusterbart styre' (stavning).

**titel**

Före:
```
Scooter Rideoo 120 City, Hopfällbar
```
Efter:
```
Sparkcykel Rideoo 120 City, Rosa
```

**seo_title**

Före:
```
Scooter Rideoo 120 City
```
Efter:
```
Sparkcykel Rideoo 120 City, Rosa
```

**meta**

Före:
```
Rideoo 120 City Scooter är hopfällbar, har justerbar styrehöjd och polyuretanhjul på 120 mm. Den är lämplig för åldrarna 4–7 år och väger 3,4 kg.
```
Efter:
```
Sparkcykeln Rideoo 120 City i rosa är hopfällbar, har höjdjusterbart styre och polyuretanhjul på 120 mm. Den är för åldrarna 4–7 år och väger 3,4 kg.
```

**html**

Före:
```
<p>Rideoo 120 City Scooter fälls ihop och har justerbar styrehöjd och polyuretanhjul på 120 mm. Den väger 3,4 kg och är lämplig för åldrarna 4–7 år. Enligt tillverkaren är maximal belastning 70 kg.</p><h2>Passar för</h2><ul>
<li>Dig som söker en hopfällbar scooter för barn i åldern 4–7 år</li>
<li>Dig som vill ha en scooter med justerbar styrehöjd</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Scooter</li>
<li>Märke: Rideoo</li>
<li>Modell: 120 City Scooter</li>
<li>Hopfällbar: Ja</li>
<li>Styrehöjd: Justerbar</li>
```
Efter:
```
<p>Sparkcykeln Rideoo 120 City i rosa är hopfällbar och har höjdjusterbart styre och polyuretanhjul på 120 mm. Den väger 3,4 kg och är lämplig för åldrarna 4–7 år. Enligt tillverkaren är maximal belastning 70 kg.</p><h2>Passar för</h2><ul>
<li>Dig som söker en hopfällbar sparkcykel för barn i åldern 4–7 år</li>
<li>Dig som vill ha en sparkcykel med höjdjusterbart styre</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Sparkcykel</li>
<li>Märke: Rideoo</li>
<li>Modell: 120 City Scooter</li>
<li>Färg: Rosa</li>
<li>Hopfällbar: Ja</li>
<li>Styre: Höjdjusterbart</li>
```

### 46403 (10523488387338, k_46sak5_utkast.json): RÄTTA

Live ACTIVE, lager 0, tagg På beställning (leveranstidsmeningen finns). Båda varianterna har SKU 3009011118 och EAN 4711291230408 (samma artikel, olika pris); slutomgången 2026-11-06 och beslutet 2026-11-08 tillåter skrivning, titel och text låser inte färg eller pris. Uppgifterna står i egen källa; perfekt, pålitlig, säkerställer, högkvalitativ rätt utelämnade. RÄTTA: syskonet 10581606629642 (SKU 3009011117, texter-klara) har samma live-titel och skrevs som 'Stadscykel Giant AnyTour CS 2 GB, 700x45, Stealth Chrome' med SEO 'Stadscykel Giant AnyTour CS 2 GB'. Typordet görs enhetligt med syskonet (R7, källtexten säger stadscykel) och titeln måste skilja produkterna (David 2026-11-05). Skillnaden är ramstorleken: slutsiffra 8 = XL enligt Giant-regeln 2026-11-08, och varianten heter 'XL / gray'; källan anger 'XL (60 cm)'. Storleken låses inte fel eftersom båda varianterna är samma SKU.

**titel**

Före:
```
Cykel Giant AnyTour CS 2 GB med remdrift
```
Efter:
```
Stadscykel Giant AnyTour CS 2 GB med remdrift, XL
```

**seo_title**

Före:
```
Cykel Giant AnyTour CS 2 GB
```
Efter:
```
Stadscykel Giant AnyTour CS 2 GB XL
```

**html**

Före:
```
<li>Typ: Cykel (stadscykel)</li>
<li>Märke: Giant</li>
<li>Ram: ALUXX-aluminium</li>
```
Efter:
```
<li>Typ: Stadscykel</li>
<li>Märke: Giant</li>
<li>Ramstorlek: XL (60 cm)</li>
<li>Ram: ALUXX-aluminium</li>
```

### 46404 (10530129477898, k_46sak5_utkast.json): RÄTTA

Live ACTIVE, lager 5, 800002576, EAN 4713250018218. Live-titeln säger Barnhjälm men källan beskriver en cykelhjälm för landsväg och terräng i S/M 49–57 cm; bytet till källans typord Cykelhjälm följer R7 och de skrivna Relay-syskonen. Ingen dubblett: skrivna Gloss White 10530129510666 är M/L (800002577), och titeln skiljer storleken. Maximalt skydd, sidokollisioner, komfort och Robust rätt utelämnade; MIPS bara som systemnamn. RÄTTA: '(fukt- och lukttransporterande)' är ett funktionslöfte (prestanda) och stryks; 'en innerfoder' → 'ett innerfoder'; 'Direct Flow Cooling ventilationssystem' får bindestreck (sammansättning). Spärrlistan: produkten står i aktiv spärr (utanfor-tills-vidare-2026-11-04); skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt.

**meta**

Före:
```
Direct Flow Cooling ventilationssystem
```
Efter:
```
Direct Flow Cooling-ventilationssystem
```

**html**

Före:
```
Direct Flow Cooling ventilationssystem och en innerfoder av TransTextura.</p><h2>Passar för</h2><ul>
<li>Dig som söker en cykelhjälm för landsväg och terräng</li>
<li>Dig som behöver en hjälm i storlek S/M, 49–57 cm</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Cykelhjälm</li>
<li>Märke: Giant</li>
<li>Modell: Relay MIPS</li>
<li>Storlek: S/M (49–57 cm)</li>
<li>System: 360° Cinch One MIPS</li>
<li>Ventilation: Direct Flow Cooling</li>
<li>Innerfoder: TransTextura (fukt- och lukttransporterande)</li>
```
Efter:
```
Direct Flow Cooling-ventilationssystem och ett innerfoder av TransTextura.</p><h2>Passar för</h2><ul>
<li>Dig som söker en cykelhjälm för landsväg och terräng</li>
<li>Dig som behöver en hjälm i storlek S/M, 49–57 cm</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Cykelhjälm</li>
<li>Märke: Giant</li>
<li>Modell: Relay MIPS</li>
<li>Storlek: S/M (49–57 cm)</li>
<li>System: 360° Cinch One MIPS</li>
<li>Ventilation: Direct Flow Cooling</li>
<li>Innerfoder: TransTextura</li>
```

### 46405 (10541372277002, k_46sak5_utkast.json): GODKÄND

Live ACTIVE, lager 5, 030012955XS, EAN 3267654944181. Storlek XS 48–52 cm, insektsnät, reflekterande element, justering och användning på springcykel/cykel/cykelstol står i egen källa; säkerhet, synlighet, bekväm passform och lekfulla designer rätt utelämnade (reflekterande element bara som fakta, v1.9). Ingen annan Cairn Sunny i butiken. Spärrlistan: produkten står i aktiv spärr (utanfor-tills-vidare-2026-11-04); skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt.

### 46406 (10554353910026, k_46sak5_utkast.json): RÄTTA

Live ACTIVE, lager 1, 800002244, EAN 4713250839264. Under 5 år, EPS, 46–51 cm och inbyggt insektsnät står i egen källa; ålder en gång enligt tillverkaren. Lime-syskonet (800002243) är DRAFT och annan färg. RÄTTA: 'antimikrobiell' är hälsopåstående och stryks i brödtext och specifikation (praxis 46103/46104/46210). Spärrlistan: produkten står i aktiv spärr (utanfor-tills-vidare-2026-11-04); skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt.

**html**

Före:
```
Hjälmen har EPS-konstruktion, inbyggt insektsnät och vaddering av TransTexture med antimikrobiell behandling.</p><h2>Passar för</h2><ul>
<li>Dig som söker en barnhjälm i storlek 46–51 cm</li>
<li>Dig som vill ha en hjälm med inbyggt insektsnät</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Barnhjälm</li>
<li>Märke: Giant</li>
<li>Modell: Holler</li>
<li>Ålder: Under 5 år</li>
<li>Storlek: 46–51 cm</li>
<li>Konstruktion: EPS</li>
<li>Vaddering: TransTexture, antimikrobiell</li>
```
Efter:
```
Hjälmen har EPS-konstruktion, inbyggt insektsnät och TransTexture-vaddering.</p><h2>Passar för</h2><ul>
<li>Dig som söker en barnhjälm i storlek 46–51 cm</li>
<li>Dig som vill ha en hjälm med inbyggt insektsnät</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Barnhjälm</li>
<li>Märke: Giant</li>
<li>Modell: Holler</li>
<li>Ålder: Under 5 år</li>
<li>Storlek: 46–51 cm</li>
<li>Konstruktion: EPS</li>
<li>Vaddering: TransTexture</li>
```

### 46407 (10577688527114, k_46sak5_utkast.json): RÄTTA

Live ACTIVE, lager 1, HCKIDSCEGVS, EAN 8055186667686. 195 g, insektsnät, tvättbar stoppning och Monoshell in-mould Superlight står i egen källa; storleken rätt utelämnad (46-52 cm och 46 - 46 cm motsäger varandra, R2). RÄTTA: 'antibakteriell' stryks (hälsopåstående, praxis 46103/46211). SEO 'Barnhjälm Limar Kid Pro S' krockar med utkastet för Ghost Blue (10472252244234, k_46sak3_utkast.json); färgen läggs till (R12). Spärrlistan: produkten står i aktiv spärr (utanfor-tills-vidare-2026-11-04); skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt.

**seo_title**

Före:
```
Barnhjälm Limar Kid Pro S
```
Efter:
```
Barnhjälm Limar Kid Pro S Space Blue
```

**html**

Före:
```
insektsnät och antibakteriell, tvättbar stoppning.</p><h2>Passar för</h2><ul>
<li>Dig som söker en barnhjälm med insektsnät</li>
<li>Dig som vill ha en hjälm med tvättbar stoppning</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Barnhjälm</li>
<li>Märke: Limar</li>
<li>Modell: Kid Pro S</li>
<li>Färg: Space Blue</li>
<li>Vikt: 195 g</li>
<li>Teknik: Monoshell in-mould (Superlight)</li>
<li>Stoppning: Antibakteriell och tvättbar</li>
```
Efter:
```
insektsnät och tvättbar stoppning.</p><h2>Passar för</h2><ul>
<li>Dig som söker en barnhjälm med insektsnät</li>
<li>Dig som vill ha en hjälm med tvättbar stoppning</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Barnhjälm</li>
<li>Märke: Limar</li>
<li>Modell: Kid Pro S</li>
<li>Färg: Space Blue</li>
<li>Vikt: 195 g</li>
<li>Teknik: Monoshell in-mould (Superlight)</li>
<li>Stoppning: Tvättbar</li>
```

### 46408 (10548248215818, k_46sak5_utkast.json): RÄTTA

Live ACTIVE, lager 3, 488, EAN 7350051864889. Montering på ram/styre/hjälm, lätta att ta bort och kombinera färger/mönster står i egen källa; 'för barn' i live-titeln saknar stöd och är rätt struket. RÄTTA: (1) Första meningen i html och meta är cirkulär engelska ('Bookman Reflective Adventure Stickers är reflekterande klistermärken', R11). (2) Raden om vidhäftning i regn, snö och hagel är ett hållbarhetslöfte och utelämnades på syskonen Grön (46101) och Gul (46301); den stryks här också. (3) SEO 'Reflekterande klistermärken Bookman' krockar med b_6_utkast.json (Black Flames) och skiljer inte färgen från syskonen; färgen läggs till. Titeln skiljer redan färgen.

**seo_title**

Före:
```
Reflekterande klistermärken Bookman
```
Efter:
```
Reflekterande klistermärken Bookman, Vit
```

**meta**

Före:
```
Bookman Reflective Adventure Stickers är reflekterande klistermärken i vitt som kan sättas på cykelramar, styren och hjälmar.
```
Efter:
```
De vita reflekterande klistermärkena Bookman Reflective Adventure Stickers kan sättas på cykelramar, styren och hjälmar och kombineras med andra färger.
```

**html**

Före:
```
<p>Bookman Reflective Adventure Stickers är reflekterande klistermärken som kan sättas på cykelramar, styren och hjälmar. Klistermärkena kan kombineras i olika färger och mönster, och enligt tillverkaren är de lätta att ta bort.</p><h2>Passar för</h2><ul>
<li>Dig som söker reflekterande klistermärken till cykel</li>
<li>Dig som vill kombinera olika färger och mönster</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Reflekterande klistermärken</li>
<li>Märke: Bookman</li>
<li>Modell: Reflective Adventure Stickers</li>
<li>Färg: Vit</li>
<li>Användning: Cykelramar, styren och hjälmar</li>
<li>Vidhäftning: Enligt tillverkaren tappar de inte sin vidhäftning i regn, snö eller hagel</li>

```
Efter:
```
<p>De vita reflekterande klistermärkena Bookman Reflective Adventure Stickers kan sättas på cykelramar, styren och hjälmar. Klistermärkena kan kombineras i olika färger och mönster, och enligt tillverkaren är de lätta att ta bort.</p><h2>Passar för</h2><ul>
<li>Dig som söker reflekterande klistermärken till cykel</li>
<li>Dig som vill kombinera olika färger och mönster</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Reflekterande klistermärken</li>
<li>Märke: Bookman</li>
<li>Modell: Reflective Adventure Stickers</li>
<li>Färg: Vit</li>
<li>Användning: Cykelramar, styren och hjälmar</li>

```

### 46409 (10548295368970, k_46sak5_utkast.json): GODKÄND

Live ACTIVE, lager 0, tagg På beställning (leveranstidsmeningen finns). Varianterna white K25/5/23/2 och black K25/5/23/1 har samma pris; v1.8: färgen är rätt struken ur titeln och texten. Motor, batteri, ram, växlar, bromsar, däck, vikt, förarlängd och ingående delar står ordagrant i egen källa; räckvidd 70 km rätt utelämnad (prestanda), likaså perfekt, prisvärd, stabil, trygg. Lastgräns saknas i egen källa; webbsökning hittade ingen uppgift för Bormio (velomarket.ee nekar åtkomst, övriga träffar gäller andra trehjulingar), så 'Maximal lastgräns: Ej känd' i specifikation och text följer v1.10. Ingen annan Bormio i butiken.

### 46410 (10581106917642, k_46sak5_utkast.json): GODKÄND

Live ACTIVE, lager 37, EB-GB3.0-WH, EAN 6430016905060. Elektronik är frisläppt 2026-11-08. Egen källa är bara löften; uppgifterna kommer ur tillverkarens svenska manual för EB-GB3.0 (https://hefitness.se/produktfiler/eb-gb3.0exercisebike-manualse.pdf, text kontrollerad: 'Max användarvikt: 120 kg', 'Välj mellan 10 förinställda träningsprogram', 'Visa hastighet (RPM), TIME, DIST., CAL., WATT, PULS, LEVEL', 'Omfång: 1–16', inomhus- och hemmabruk, manuellt program och wattkontrollprogram). Maxvikten står en gång enligt tillverkaren (R4, svensk rad med etikett). Pulskontrollprogram, Bluetooth/appar och mått rätt utelämnade. Manualen gäller modellen EB-GB3.0 utan färgsuffix; Galaxus säljer GB3.0 i vit och svart som samma modell, så uppgifterna godtas för WH. Ingen annan GB3.0 i butiken.

### 46411 (10624081527050, k_46sak5_utkast.json): RÄTTA

Live ACTIVE, lager 1, 9136, EAN 5902308591363. Barncykelklocka, Minnie-tema, metall och diameter 55 mm står i egen källa (fyra fakta, R3 uppfylld); säkerhetslöftet och 'linsdiameter' rätt utelämnade. Skriven Minnie Retro Vit (9139) är annan artikel. RÄTTA: titelns beskrivande ord får stor bokstav (R9, praxis 'Cykelklocka Minnie Retro, Vit'); inledningen i html och meta är cirkulär ('Minnie … har Minnie-tema') och skrivs om enligt praxis 46209. 55 mm är egen källas 'diameter'; syskonet 9139 anger 80 mm diameter och 55 mm höjd, se fråga till David.

**titel**

Före:
```
Cykelklocka Minnie Flowers Retro, vit blommig
```
Efter:
```
Cykelklocka Minnie Flowers Retro, Vit Blommig
```

**meta**

Före:
```
Barncykelklockan Minnie Flowers Retro är av metall, har 55 mm i diameter och Minnie-tema i vit blommig design. Artikelnummer 9136.
```
Efter:
```
Den här cykelklockan för barn är av metall och har en diameter på 55 mm. Den har Minnie-tema i vit blommig design och artikelnummer 9136.
```

**html**

Före:
```
<p>Barncykelklockan Minnie Flowers Retro har Minnie-tema i vit blommig design.
```
Efter:
```
<p>Den här cykelklockan för barn har Minnie-tema i vit blommig design.
```
