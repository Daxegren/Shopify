# Granskningsutlåtande k_46ovr3, aktiva produkter i tidigare utanför-kategorier (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient; `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan text får faktatext även i säkerhets-, barn-, kosttillskotts-, akupressur- och rullskridskokategorierna), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och formatet i `k_utlatande_43.json`. Tidigare granskningar av samma id lästes (30024 i `k_utlatande_28i30cd.json`, 10384 i `g_utlatande_1.json`, 10478 i `g_utlatande_2.json`).

Alla 15 utkast och 9 avvisade är ACTIVE. Standardblocket är exakt rätt på alla; leveranstidsmeningen finns bara på 47205 och 47211, som är de enda med taggen På beställning. Titel ≤70 tecken och ≤2 kommatecken, SEO ≤43, meta 103–153 tecken med verb, "Passar för" finns på alla. Titlar, SEO-titlar och metatexter är unika inom batchen och mot alla andra utkast- och skrivfiler (enda träffen: 47214 mot ett äldre oskrivet utkast för samma produkt). Varje rättning är ETT sammanhängande före/efter-par per fält, och varje före-text förekommer exakt en gång i utkastet (kontrollerat i python); de rättade texterna ger inga fel i `skrivfil_kontroll.py` utöver spärren nedan.

**Obs före skrivfil:** `skrivfil_kontroll.py` stoppar 7 av utkasten (47205, 47206, 47207, 47208, 47209, 47211, 47215) eftersom de står på spärrlistorna `tidigare-avvisade-2026-11-04` och `utanfor-tills-vidare-2026-11-04`. Davids beslut 2026-11-08 släpper dem, men en undantagspost i `sparrlista.json` (som `undantag-2026-11-05`) måste läggas till med beslutet innan skrivfilen byggs. Butiksprofilen listar dessutom fortfarande akupressur, isbroddar och rullskridskor under `utanfor_tills_vidare` (R6 säger att profilen är facit).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_46ovr3.json`.

## Resultat: 4 GODKÄND, 11 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 47201 | 10472280359178 | k_46ovr3_utkast.json | RÄTTA | titel, seo_title, meta, html |
| 47202 | 10472280424714 | k_46ovr3_utkast.json | RÄTTA | titel, seo_title |
| 47203 | 10472280490250 | k_46ovr3_utkast.json | RÄTTA | titel, seo_title, html |
| 47204 | 10472280621322 | k_46ovr3_utkast.json | GODKÄND | – |
| 47205 | 10472282063114 | k_46ovr3_utkast.json | RÄTTA | html |
| 47206 | 10472284520714 | k_46ovr3_utkast.json | RÄTTA | titel |
| 47207 | 10472286257418 | k_46ovr3_utkast.json | RÄTTA | titel, seo_title, html |
| 47208 | 10472287043850 | k_46ovr3_utkast.json | RÄTTA | titel, seo_title |
| 47209 | 10472295694602 | k_46ovr3_utkast.json | GODKÄND | – |
| 47210 | 10472299135242 | k_46ovr3_utkast.json | GODKÄND | – |
| 47211 | 10472301920522 | k_46ovr3_utkast.json | RÄTTA | titel |
| 47212 | 10472301953290 | k_46ovr3_utkast.json | RÄTTA | titel, seo_title |
| 47213 | 10472302051594 | k_46ovr3_utkast.json | RÄTTA | html |
| 47214 | 10472308179210 | k_46ovr3_utkast.json | GODKÄND | – |
| 47215 | 10472314274058 | k_46ovr3_utkast.json | RÄTTA | titel, meta, html |

## Löften och påståenden

Alla texter genomsöktes efter hälso-, säkerhets-, skydds-, utvecklings-, prestanda- och kvalitetsord (immun, celler, trötthet, uthållighet, prestation, rehydrering, testosteron, hud, hår, säker, skyddar, halka, stöld, pålitlig, slitstark, hållbar, avslappning, cirkulation, återhämtning, bekväm, komfort, stöd). Kvar fanns tre subtila fall, som rättas: ingrediensgruppen "Uthållighetsformula" (47213), "isskydd" som benämning på vintergreppen (47215) och azorubinvarningen som påstår ett innehåll som inte finns i ingredienslistan (47201). "Skydd" står kvar i 47207 bara som produktbenämning (knä- och armbågsskydd), utan påstående om vad skydden skyddar mot.

## Mönster

- Uppgifterna hör till exakt artikel: SKU och EAN stämmer mot live på alla. Två källor blandar produkter eller har maskinöversättningar som syntes i titeln: Vit. C (Strong-texten), och "Fuses" (estniska kaitsmed).
- Lastgräns (v1.10): 47210 har svensk etiketterad användarvikt (enligt tillverkaren). 47205 har bara "driftsvikt", och 150 kg finns bara hos återförsäljare, så "Ej känd" skrivs.
- Varianter (v1.8/v1.9): 47208 är samma artikel i två färger med olika pris och lager > 0; inget låses.
- Stor bokstav på beskrivande ord i titeln (R9) saknades i sju titlar.
- Avvisade (9): alla avvisningar är riktiga (tom eller motsägande källa, bara påståenden, olika pris utan lager, motsägelse mellan titel och källa). Ingen lyfts.

## Frågor till David

1. Lägg till undantag i spärrlistan för de 7 spärrade id:na (ditt beslut 2026-11-08) och uppdatera `utanfor_tills_vidare` i butiksprofilen.
2. Finnlo Autark 5.0 (47205): vill du att 150 kg ska stå som maximal användarvikt? Den finns hos återförsäljare (Gigantti, Ha3654) och på det skrivna syskonet Hammer Autark 5.0, men inte i produktens egen källa eller på en tillverkarsida som gick att läsa.
3. Fila Legacy QF Lady (47214): storleken framgår bara av artikelnumret (troligen 38,5). Vill du att storleken ska stå i titeln?
4. Paw Patrol-handskarna: rosa (Default Title) kostar 129 kr och blå 109 kr med samma SKU och EAN; troligen ett prisfel i butiken.
5. Hammer Autark 5.0 och Finnlo by Hammer Autark 5.0 har samma mått men olika SKU och EAN; båda är aktiva. Behåll båda?

## Skäl och rättningar per produkt

### 47201 (10472280359178): RÄTTA

Live ACTIVE, SKU 11664, EAN 5902114018443, 109 kr, lager 6. Källan blandar två produkter: löptexten gäller 'Vit. C Strong 1000' (tablett, bioflavonoider, zink, 1000 mg), medan live-titeln, ingredienslistan och 90 kapslar gäller Vit. C 1000 i kapslar (samma bedömning som k_utlatande_28i30cd, nr 30024). Rättning: produktnamnet följer live-titeln ('Vit. C 1000', som skrivna syskonet Trec Vit. C + L-Lysin); '1000 mg' utan bas (per kapsel eller dag) och bara ur Strong-texten stryks (R2); azorubinvarningen stryks eftersom azorubin inte finns i ingredienslistan (motsägelse, R2; samma praxis som 30024). Inga hälsopåståenden kvar.

**titel**

Före:
```
Vitaminkapslar Trec Vitamin C 1000, 90 kapslar
```
Efter:
```
Vitaminkapslar Trec Vit. C 1000, 90 kapslar
```

**seo_title**

Före:
```
Vitaminkapslar Trec Vitamin C 1000
```
Efter:
```
Vitaminkapslar Trec Vit. C 1000
```

**meta**

Före:
```
Kosttillskottet Trec Vitamin C 1000 innehåller 1000 mg C-vitamin i 90 kapslar. Dosen är 1 kapsel per dag med 300 ml vatten, helst efter en huvudmåltid.
```
Efter:
```
Kosttillskottet Trec Vit. C 1000 innehåller C-vitamin i 90 kapslar. Dosen är 1 kapsel per dag med 300 ml vatten, helst efter en huvudmåltid.
```

**html**

Före:
```
<p>Kosttillskottet Trec Vitamin C 1000 innehåller 1000 mg C-vitamin i kapselform. Förpackningen har 90 kapslar och rekommenderad daglig dos är 1 kapsel.</p><h2>Passar för</h2><ul>
<li>Dig som söker C-vitamin i kapselform</li>
<li>Dig som vill ha ett kosttillskott med fast dos om 1 kapsel per dag</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Kosttillskott i kapslar</li>
<li>Innehåll: C-vitamin, 1000 mg</li>
<li>Förpackning: 90 kapslar</li>
<li>Ingredienser: C-vitamin, kapselkropp (hydroxipropylmetylcellulosa), klumpförebyggande medel (magnesiumstearat)</li>
<li>Rekommenderad daglig dos: 1 kapsel</li>
<li>Användning: 1 kapsel med 300 ml vatten, helst efter en huvudmåltid</li>
<li>Förvaring: Burken stängd på en torr plats, 15–25 °C, och utom räckhåll för barn</li>
<li>Obs: Överskrid inte den dagliga mängden. Använd inte som ersättning för en varierad kost. Enligt tillverkaren är produkten inte avsedd för barn, gravida eller ammande kvinnor. Produkten kan innehålla allergener som mjölk, soja, vete, korn, havre, ägg, jordnötter och nötter.</li>
<li>Varning: Azorubin kan ha negativa effekter på barns aktivitet och uppmärksamhet.</li>
</ul>
```
Efter:
```
<p>Kosttillskottet Trec Vit. C 1000 innehåller C-vitamin i kapselform. Förpackningen har 90 kapslar och rekommenderad daglig dos är 1 kapsel.</p><h2>Passar för</h2><ul>
<li>Dig som söker C-vitamin i kapselform</li>
<li>Dig som vill ha ett kosttillskott med fast dos om 1 kapsel per dag</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Kosttillskott i kapslar</li>
<li>Förpackning: 90 kapslar</li>
<li>Ingredienser: C-vitamin, kapselkropp (hydroxipropylmetylcellulosa), klumpförebyggande medel (magnesiumstearat)</li>
<li>Rekommenderad daglig dos: 1 kapsel</li>
<li>Användning: 1 kapsel med 300 ml vatten, helst efter en huvudmåltid</li>
<li>Förvaring: Burken stängd på en torr plats, 15–25 °C, och utom räckhåll för barn</li>
<li>Obs: Överskrid inte den dagliga mängden. Använd inte som ersättning för en varierad kost. Enligt tillverkaren är produkten inte avsedd för barn, gravida eller ammande kvinnor. Produkten kan innehålla allergener som mjölk, soja, vete, korn, havre, ägg, jordnötter och nötter.</li>
</ul>
```

### 47202 (10472280424714): RÄTTA

Live ACTIVE, SKU 13094, EAN 5902114019631, lager 2. Alla uppgifter finns ordagrant i källans ingredienslista, dos och varning; L-karnitin, taurin och B-vitaminer (finns bara i påståendetexten, inte i ingredienslistan) rätt utelämnade. Inga effektord (rehydrering, uthållighet, trötthet utelämnade). Rättning: stor bokstav på beskrivande ord i titel och SEO-titel (R9, format_regler.py).

**titel**

Före:
```
Isotoniskt pulver Trec Isotonic Sport Citron, 400 g
```
Efter:
```
Isotoniskt Pulver Trec Isotonic Sport Citron, 400 g
```

**seo_title**

Före:
```
Isotoniskt pulver Trec Isotonic Sport
```
Efter:
```
Isotoniskt Pulver Trec Isotonic Sport
```

### 47203 (10472280490250): RÄTTA

Live ACTIVE, SKU 14286, EAN 5902114041687, lager 10. Ingredienser, dos, 3-månadersgräns och varningar stämmer; alla funktionspåståenden (celler, immunförsvar, testosteron, elektrolytbalans) utelämnade. Fel: källan anger kapselskal av gelatin (parti B) ELLER hydroxipropylmetylcellulosa (parti C) beroende på parti; utkastet skrev bara gelatin, vilket är fel för hälften av partierna. Rättning av ingrediensraden och stor bokstav på 'Män' (R9).

**titel**

Före:
```
Multivitamin för män Trec, 90 kapslar
```
Efter:
```
Multivitamin för Män Trec, 90 kapslar
```

**seo_title**

Före:
```
Multivitamin för män Trec
```
Efter:
```
Multivitamin för Män Trec
```

**html**

Före:
```
kapselskal (gelatin), multivitaminkomplex
```
Efter:
```
kapselskal (gelatin eller hydroxipropylmetylcellulosa beroende på parti), multivitaminkomplex
```

### 47204 (10472280621322): GODKÄND

Live ACTIVE, SKU 21337, EAN 5902114046668, lager 7. Typordet Antioxidant (effektbeteckning) byts mot Kosttillskott, som källans varningsrad använder (R7). Källans felaktiga 'lakritsrotsextrakt' för Berberis aristata utelämnat, bara latinska namnet används (R2). Ingredienser, halter (40 %, 2 % berberin, 95 % curcumin), dos och förvaring stämmer. Alla effektpåståenden (antiinflammatorisk, immunstärkande, blodsocker) utelämnade. Inga subtila löften.

### 47205 (10472282063114): RÄTTA

Live ACTIVE, lager 0, tagg På beställning (meningen finns i standardblocket). SKU 3654, EAN 4005251365409. Mått, fritt utrymme, takhöjd och maximalt motstånd 120 kg stämmer; totalvikten (80 och 255 kg) rätt utelämnad som motsägelse. Typord Kraftstation följer skrivna syskon (Finnlo Autark 600/2200). Inte exakt dubblett av skrivna 'Powerstation Hammer Autark 5.0' (10589703241994): annan SKU (14003) och EAN, och David 2026-11-05 räknar bara samma SKU/EAN som dubblett. Kraftstationen bär användaren och källan har bara 'Maximal driftsvikt: 150 kg', som inte får tolkas (R4). v1.10: webbsökning ger 150 kg bara hos återförsäljare (gigantti.fi 'Max. kapasiteetti 150 kg' för Ha3654, velomarket.ee för Hammer-varianten), inte på tillverkarens sida (hammer.de gick inte att läsa), så uppgiften är inte entydig från tillverkaren: 'Maximal lastgräns: Ej känd' läggs in i specifikationen och i texten. Dessutom tas dubblerat 'hemma' bort.

**html**

Före:
```
<p>Finnlo by Hammer Autark 5.0 är ett hemmagym för styrketräning hemma. Det mäter 200 x 143 x 217 cm, kräver ett fritt utrymme på 200 x 160 x 217 cm och en takhöjd på minst 220 cm.</p><h2>Passar för</h2><ul>
<li>Dig som söker ett hemmagym för styrketräning</li>
<li>Dig som har en takhöjd på minst 220 cm</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Kraftstation (hemmagym)</li>
<li>Märke: Finnlo by Hammer</li>
<li>Modell: Autark 5.0</li>
<li>Mått: 200 x 143 x 217 cm</li>
<li>Nödvändigt fritt utrymme: 200 x 160 x 217 cm</li>
<li>Minsta takhöjd: 220 cm</li>
<li>Maximalt motstånd: 120 kg</li>
<li>Artikelnummer: 3654</li>
```
Efter:
```
<p>Finnlo by Hammer Autark 5.0 är ett hemmagym för styrketräning. Det mäter 200 x 143 x 217 cm, kräver ett fritt utrymme på 200 x 160 x 217 cm och en takhöjd på minst 220 cm. Maximal lastgräns är inte känd.</p><h2>Passar för</h2><ul>
<li>Dig som söker ett hemmagym för styrketräning</li>
<li>Dig som har en takhöjd på minst 220 cm</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Kraftstation (hemmagym)</li>
<li>Märke: Finnlo by Hammer</li>
<li>Modell: Autark 5.0</li>
<li>Mått: 200 x 143 x 217 cm</li>
<li>Nödvändigt fritt utrymme: 200 x 160 x 217 cm</li>
<li>Minsta takhöjd: 220 cm</li>
<li>Maximalt motstånd: 120 kg</li>
<li>Maximal lastgräns: Ej känd</li>
<li>Artikelnummer: 3654</li>
```

### 47206 (10472284520714): RÄTTA

Live ACTIVE, SKU 2050, EAN 4250969220506, lager 1. Aluminiumram, 12-tums luftfyllda däck, 3,4 kg och sadelhöjd 32–44 cm stämmer; 'snabbaste och lättaste', 'säkra', 'hållbara' utelämnade. Inga säkerhets- eller utvecklingslöften. Åldern finns bara i live-titeln och behålls där som förut. Rättning: tankstreck i intervallet 2–4 år (som skrivna 'Flickcykel Bobbin Gingersnap för 4–6 år').

**titel**

Före:
```
Springcykel S'cool X Magnesium, 12 tum, 2-4 år
```
Efter:
```
Springcykel S'cool X Magnesium, 12 tum, 2–4 år
```

### 47207 (10472286257418): RÄTTA

Live ACTIVE, SKU 9062, EAN 5902308590625, lager 4. 'Fuses' är en maskinöversättning (estniska 'kaitsmed' = både säkringar och skydd), inget modellnamn; det tas bort ur titel och text (R2). Kvar är bara källans fakta: skydd för knän och armbågar, avsedda för barn, vaddering, Avengers-design, blå. 'Skyddar vid fall' och 'utmärkt skydd' rätt utelämnade; ordet skydd står bara som produktbenämning. Antal delar och storlek anges inte i källan och skrivs inte. Rättningar: titel (utan Fuses, R9), SEO (R9) och inledningen.

**titel**

Före:
```
Skydd för knän och armbågar Fuses Avengers, Blå
```
Efter:
```
Skydd för Knän och Armbågar Avengers, Blå
```

**seo_title**

Före:
```
Skydd för knän och armbågar Avengers
```
Efter:
```
Skydd för Knän och Armbågar Avengers
```

**html**

Före:
```
<p>Fuses Avengers är skydd för knän och armbågar avsedda för barn. De har Avengers-design och är vadderade.</p>
```
Efter:
```
<p>Avengers-skydden för knän och armbågar är avsedda för barn. De har vaddering och Avengers-design i blått.</p>
```

### 47208 (10472287043850): RÄTTA

Live ACTIVE, två varianter (Default Title 129 kr, lager 5; blue 109 kr, lager 2) med samma SKU 34011 och EAN: samma artikel i två färger med olika pris och lager > 0 (v1.9); titel, SEO och text låser varken färg eller pris. Storlek S och ålder 4–6 år gäller båda. Skydd mot stötar och repor och 'bekväm' utelämnade; trasig måttrad utelämnad. Rättning: stor bokstav på 'Barn' (R9).

**titel**

Före:
```
Handskar Paw Patrol för barn, Storlek S
```
Efter:
```
Handskar Paw Patrol för Barn, Storlek S
```

**seo_title**

Före:
```
Handskar Paw Patrol för barn
```
Efter:
```
Handskar Paw Patrol för Barn
```

### 47209 (10472295694602): GODKÄND

Live ACTIVE, SKU 59051595KS, EAN 8713249347189, lager 7. Kedjelås, 150 cm, 5 mm och fästa cykeln i olika objekt står i källan; 'pålitlig', 'bra säkerhet', 'slitstark' och 'motstå stöld' utelämnade. Typord Kedjelås ur källan (live-titelns norska 'Kettlukk'). AXA i versaler följer alla skrivna AXA-titlar. Inga säkerhetslöften.

### 47210 (10472299135242): GODKÄND

Live ACTIVE, SKU SRX-80EVO, EAN 8029975999623, lager 1. Remdrift, precisionsfriktionsbroms, justerbar sadel och styre, LCD, mått, 51 kg stämmer; svänghjulet (20 kg i text, 24 kg i specifikation) rätt utelämnat. 'Maximal användarvikt: 140 kg' är en svensk rad med etikett och enhet och står en gång med 'enligt tillverkaren' (R4). 'Hållbar', 'intensiva', 'realistisk' utelämnade. Inte dubblett av skrivna SRX-modeller.

### 47211 (10472301920522): RÄTTA

Live ACTIVE, lager 0, tagg På beställning (meningen finns i standardblocket). SKU 14TUSYO095, EAN 8717842038451. Mått, kokosfiberfyllning, linne och bomull, bärväska, tvättbart överdrag och 2,4 kg stämmer. Alla effektord (koppla av, spänningar, cirkulation, nervändar, återhämtning, hudvänliga) och OCS-certifiering utelämnade. Beige syskon 10462850449674 är annan SKU/färg, ingen dubblett. Rättning: stor bokstav på 'Kudde' i titeln (R9).

**titel**

Före:
```
Akupressurmatta med kudde Tunturi Pro, Svart
```
Efter:
```
Akupressurmatta med Kudde Tunturi Pro, Svart
```

### 47212 (10472301953290): RÄTTA

Live ACTIVE, SKU=EAN 5902114041694, lager 12. Ingredienser, dos och alla varningar (tom mage, grönt te-extrakt, 800 mg EGCG) stämmer; källans 'ECGC' och 'linolensyra' är uppenbara stavfel och ändras till EGCG respektive bara CLA (bekräfta mot förpackningen). Påståenden om celler, immunförsvar, hud och hår utelämnade. Typord följer live-titeln på syskonet för män. Rättning: stor bokstav på 'Kvinnor' (R9).

**titel**

Före:
```
Multivitamin för kvinnor Trec, 90 kapslar
```
Efter:
```
Multivitamin för Kvinnor Trec, 90 kapslar
```

**seo_title**

Före:
```
Multivitamin för kvinnor Trec
```
Efter:
```
Multivitamin för Kvinnor Trec
```

### 47213 (10472302051594): RÄTTA

Live ACTIVE, SKU=EAN 5902114019624, lager 10. Ingredienser, dos 50 g (8 skopor), portion 25 g (4 skopor) i 500 ml, förvaring och varningar stämmer; alla prestanda- och trötthetspåståenden utelämnade. Ett subtilt prestandaord fanns kvar: ingrediensgruppens namn 'Uthållighetsformula' (källans 'PRO uthållighetssportformula'). Rättning: 'Formula', i linje med 'mineralformula' och 'vitaminformula'; innehållet i gruppen är oförändrat.

**html**

Före:
```
<li>Ingredienser: Uthållighetsformula [maltodextrin
```
Efter:
```
<li>Ingredienser: Formula [maltodextrin
```

### 47214 (10472308179210): GODKÄND

Live ACTIVE, SKU 010622085-38-5, lager 2. Engelsk källa: soft fitness roller skate, AirFlow-foder, hög stövel, spak, kardborre och ATOP-hjul, aluminiumram, 4 x 84 mm, ABEC 7, färg Black/Violet; allt återgivet utan komfort-, stöd- eller säkerhetsord. Titel och SEO sammanfaller med ett äldre oskrivet utkast (a_4_utkast.json, nr 2406) för samma produkt, som aldrig nådde butiken; ingen krock mot skrivna texter. Storlek nämns inte i källan; syskonet Legacy Pro 80 Lady har SKU-suffixen -37, -37-5 och -38-5 som storlekar, så detta par är troligen storlek 38,5 (se frågor). Ingen rättning.

### 47215 (10472314274058): RÄTTA

Live ACTIVE, SKU WNT09633540, EAN 8716404237301, lager 8. Gummitaggar, elastisk gummisula, passar de flesta skor och stövlar och köldbeständighet ner till -20 grader står i källan; 'säkra', 'säker promenad', 'säkert stöd' och 'minskar risken för halka och fall' rätt utelämnade. Single är modellnamn (syskonet heter Double), inte antal. Rättningar: ordet 'isskydd' (skyddsord) tas bort ur text och specifikation; 'vinterskor' (finns inte i källan) ersätts med källans skor och stövlar; tankstreck i storleksintervallet 35–40 i titel, meta och text.

**titel**

Före:
```
Vintergrepp Winter-Grip Anti Skid Sole Single, 35-40
```
Efter:
```
Vintergrepp Winter-Grip Anti Skid Sole Single, 35–40
```

**meta**

Före:
```
i storlek 35-40.
```
Efter:
```
i storlek 35–40.
```

**html**

Före:
```
<p>Winter-Grip Anti Skid Sole Single är vintergrepp, även kallade isskydd, för vinterskor. De har gummitaggar och en elastisk gummisula och passar enligt tillverkaren de flesta skor, stövlar och träningsskor.</p><h2>Passar för</h2><ul>
<li>Dig som söker vintergrepp till vinterskor</li>
<li>Dig som söker vintergrepp i storlek 35-40</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Vintergrepp (isskydd)</li>
<li>Märke: Winter-Grip</li>
<li>Modell: Anti Skid Sole Single</li>
<li>Storlek: 35-40</li>
<li>Taggar: Gummi</li>
<li>Sula: Elastisk gummisula</li>
<li>Passar till: Skor, stövlar och träningsskor</li>

```
Efter:
```
<p>Winter-Grip Anti Skid Sole Single är vintergrepp med gummitaggar och en elastisk gummisula. De passar enligt tillverkaren de flesta skor, stövlar och träningsskor.</p><h2>Passar för</h2><ul>
<li>Dig som söker vintergrepp till skor och stövlar</li>
<li>Dig som söker vintergrepp i storlek 35–40</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Vintergrepp</li>
<li>Märke: Winter-Grip</li>
<li>Modell: Anti Skid Sole Single</li>
<li>Storlek: 35–40</li>
<li>Taggar: Gummi</li>
<li>Sula: Elastisk gummisula</li>
<li>Passar till: Skor, stövlar och träningsskor</li>

```
