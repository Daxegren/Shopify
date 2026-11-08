# Granskningsutlåtande k_46sak2: hjälmar, belysning, reflexer och bromsdelar (2026-11-08)

Granskaren har bara läst i Shopify, inte ändrat något där och inte committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter i tidigare utanför-kategorier får faktatext), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och formatet i `k_utlatande_43.json`.

Alla 12 utkast är ACTIVE med lager > 0. Ingen har taggen På beställning och inget utkast har leveranstidsmeningen (rätt). Standardblocket är tecken för tecken lika med kanoniska `b_skriv_24.json` på alla. Titel ≤70 tecken och ≤2 kommatecken, SEO ≤43, meta 89–144 tecken, "Passar för" finns på alla, högst två "enligt tillverkaren" per text. Titlar, SEO-titlar och metatexter är unika inom batchen, mot alla andra utkast- och skrivfiler i `vag2_skriv` och mot butiken (sökning på Adventure, Nutty, Lena, Pnut, Chiru, Bob, TS+, TX500, RT64, RT86, 203, R400 samt varje EAN/SKU). Ingen exakt dubblett finns. Numren 46101–46112 är unika. Varje rättning är ETT sammanhängande före/efter-par per fält, och varje före-text förekommer exakt en gång i utkastet (kontrollerat i python).

**Spärrlistan:** `skrivfil_kontroll.py` ger 0 formatfel men 5 FEL för spärrade produkter: 46102 och 46107 (utanfor-tills-vidare-2026-11-04) samt 46103, 46105 och 46111 (tidigare-avvisade-2026-11-04). Alla spärrades eller avvisades bara på grund av kategori (barn, hjälm, bromsdel), och de omfattas av beslutet 2026-11-08. Före skrivning måste en undantagspost (som `undantag-2026-11-05`) läggas in i `sparrlista.json` med hänvisning till beslutet; annars stoppar skriptet skrivfilen. Inget annat FEL finns, inte heller på de rättade texterna.

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_46sak2.json`.

## Resultat: 7 GODKÄND, 5 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 46101 | 10471175520522 | k_46sak2_utkast.json | RÄTTA | titel, seo_title, meta, html |
| 46102 | 10472193655050 | k_46sak2_utkast.json | GODKÄND | – |
| 46103 | 10472234123530 | k_46sak2_utkast.json | RÄTTA | meta, html |
| 46104 | 10472235270410 | k_46sak2_utkast.json | RÄTTA | meta, html |
| 46105 | 10472237367562 | k_46sak2_utkast.json | GODKÄND | – |
| 46106 | 10472237596938 | k_46sak2_utkast.json | RÄTTA | meta, html |
| 46107 | 10472237629706 | k_46sak2_utkast.json | GODKÄND | – |
| 46108 | 10472238743818 | k_46sak2_utkast.json | GODKÄND | – |
| 46109 | 10472242249994 | k_46sak2_utkast.json | RÄTTA | titel, meta, html |
| 46110 | 10472242446602 | k_46sak2_utkast.json | GODKÄND | – |
| 46111 | 10472242512138 | k_46sak2_utkast.json | GODKÄND | – |
| 46112 | 10472243200266 | k_46sak2_utkast.json | GODKÄND | – |

## Löften och säkerhetsord

Alla texter genomsöktes efter säkerhets-, skydds-, hälso-, utvecklings-, prestanda- och kvalitetsord, även subtila (säker, skydd, skyddande, absorbera, stöt, slagkraft, synlig, synlighet, trafik, bromskraft, prestanda, kraftfull, jämn, kylning, sval, bekväm, komfort, slitstark, hållbar, kvalitet, certifierad, antibakteriell, lätt/lättare som fördel). Kvar efter rättning finns bara: "Standarder enligt tillverkaren: CE, CPSC och AS" (ordagrant i egen källa på 46102, 46106, 46107, återgivet som fakta utan skyddslöfte, R5), MIPS och KinetiCore som namn på system utan effekt, "lätt yttre skal" (46102, ordagrant ur källan som materialbeskrivning) och "lätta att ta bort enligt tillverkaren" (46101). "Antibakteriell" (46103, 46104) är ett hälsopåstående och stryks, i linje med tidigare praxis (Giant Doublespring). Reflexen (46101) och bakljuset (46108) har inga synlighetslöften (v1.9). Bromsdelarna har inga bromsprestandapåståenden. Lastgräns (v1.10) är inte aktuell för någon av produkterna: hjälmar och bromsdelar är undantagna i v1.10 och ingen text anger last.

## Mönster

- Varianter (v1.7–v1.9): alla utom 46101 har en variant. 46101 har två varianter med samma SKU och EAN där den ena är en överbliven Default Title (v1.7); titeln låser inget pris.
- R12a: Bookman Adventure Stickers finns aktiv i tre färger (Green, Yellow, Vit) med olika EAN och utkast i 46301 och 46408. 46101 saknade färg i titeln och hade då inte skilts från syskonen; rättat till Grön.
- Uppgifter som inte är entydiga för exakt artikeln stryks: vikten på Chiru (300 g gäller storlek S, exemplarets storlek är okänd) och växeluppgiften på frihjulsnavet (motsägande 8/9 mot 11/10/9/8).
- Typordsbyten (Bakdäck → Frihjulsnav bak, Bromslänk → Bromshandtag) har stöd i egen källtext (R7) och godtas.
- Grammatik: "nav" är neutrum (46109).

## Avvisade (k_46sak2_avvisade.json)

Alla 12 avvisningar (46201–46212) står sig: tunn eller tom källa (46201, 46206, 46207, 46208, 46210), oklar produkttyp (46202, 46205), motsägelse mellan titel och källa eller inom källan (46203, 46204, 46211, 46212) och vag källa (46209). Beslutet 2026-11-08 säger uttryckligen att produkter med motsägande eller tom källa inte skrivs. Ingen lyfts ur.

## Frågor till David

1. Spärrlistan behöver en undantagspost för 46102, 46103, 46105, 46107 och 46111 enligt ditt beslut 2026-11-08 innan skrivfilen kan byggas (ändringen är ett tillägg, inte en ändring av befintliga poster).
2. Lazer Chiru (10472237596938) säljs utan storlek, men modellen finns i S, M och L. Vet du vilken storlek som ligger i lager? Texten nämner ingen storlek eller vikt tills det är känt.
3. Bookman Adventure Stickers Green har två varianter med samma SKU och EAN men olika pris (69 och 59 kr). Troligen bör den överblivna Default Title tas bort (texten berörs inte).
4. Samma serie heter Reflexklistermärken (Yellow, 46301) och Reflekterande klistermärken (Green, Vit) i live-titlarna. Varje produkt behåller sitt live-ord enligt R7; säg till om du vill ha ett gemensamt ord.

## Skäl och rättningar per produkt

### 46101 (10471175520522, k_46sak2_utkast.json): RÄTTA

Live ACTIVE, Bookman, två varianter med samma SKU 491 och EAN 7350051864919 (Default Title 69 kr lager 4, "491" 59 kr lager 3): överbliven Default Title, v1.7 gäller. Källan stämmer (cykelramar, styren, hjälmar, lätta att ta bort, kombinera färger och mönster); "säkerhet", "mer synlig i trafiken" och vidhäftning i regn/snö/hagel är rätt utelämnade (v1.9, inga synlighets- eller skyddslöften). RÄTTA: samma serie finns aktiv i Yellow (10472303198474, EAN …4896, utkast 46301) och Vit (10548248215818, EAN …4889, utkast 46408), så titeln måste skilja färgerna (David 2026-11-05: samma modell, annan färg får egen titel som skiljer dem). Färgen Green står i live-titeln och översätts till Grön i titel, SEO och specifikation; "Reflective" stryks i titeln så att den ryms (60 tecken). Meta: "lätta att ta bort" får "enligt tillverkaren" som i beskrivningen.

**titel**

Före:
```
Reflekterande klistermärken Bookman Reflective Adventure Stickers
```
Efter:
```
Reflekterande klistermärken Bookman Adventure Stickers, Grön
```

**seo_title**

Före:
```
Klistermärken Bookman Adventure Stickers
```
Efter:
```
Klistermärken Bookman Adventure Grön
```

**meta**

Före:
```
Klistermärkena är lätta att ta bort.
```
Efter:
```
Klistermärkena är enligt tillverkaren lätta att ta bort.
```

**html**

Före:
```
<li>Modell: Reflective Adventure Stickers</li>
```
Efter:
```
<li>Modell: Reflective Adventure Stickers</li>
<li>Färg: Grön</li>
```

### 46102 (10472193655050, k_46sak2_utkast.json): GODKÄND

Live ACTIVE, Nutcase, en variant 10001789, EAN 194521007843, 2059 kr, lager 3. Allt ur egen källa: XS 48–52 cm, MIPS, polykarbonatskal, EPS-skum, Fidlock magnetspänne, CE/CPSC/AS. Standarderna står ordagrant i källan och återges som "Standarder enligt tillverkaren" utan skyddslöfte; "ledande inom säkerhet", "skyddande", "absorbera kraft", att MIPS minskar stöten och "maximal komfort" är utelämnade. Ingen dubblett (övriga Little Nutty har andra EAN och mönster). Typord Hjälm följer live-titeln (syskonen i 46307/46308 heter Barnhjälm i live). Spärrlistan (utanfor-tills-vidare) stoppar produkten i skriptet tills undantag läggs in enligt beslutet 2026-11-08.

### 46103 (10472234123530, k_46sak2_utkast.json): RÄTTA

Live ACTIVE, vendor Liv, live-titel GIANT Lena, en variant 800002260, EAN 4713250839424, 479 kr, lager 6. Storlek 46–51 cm, visir i skum, TransTextura Plus-vaddering och justerbara vadderade band stämmer med källan; "säker passform" och Giants märkestext utelämnade. RÄTTA: "antibakteriell" är ett hälsopåstående (praxis: Giant Doublespring 418 m.fl. strök ordet) och tas bort i meta, brödtext och specifikation. Spärrad som tidigare avvisad (barnhjälm), behöver undantag enligt beslutet 2026-11-08.

**meta**

Före:
```
har antibakteriell vaddering,
```
Efter:
```
har TransTextura Plus-vaddering,
```

**html**

Före:
```
Den har antibakteriell TransTextura Plus-vaddering och justerbara, vadderade fästband av typen Textura-Transflex.</p><h2>Passar för</h2><ul>
<li>Dig som söker en cykelhjälm i storlek 46–51 cm</li>
<li>Dig som vill ha en cykelhjälm med integrerat visir</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Cykelhjälm</li>
<li>Märke: Giant</li>
<li>Modell: Lena</li>
<li>Färg: Gloss Coral</li>
<li>Storlek: 46–51 cm</li>
<li>Vaddering: Antibakteriell TransTextura Plus</li>
```
Efter:
```
Den har TransTextura Plus-vaddering och justerbara, vadderade fästband av typen Textura-Transflex.</p><h2>Passar för</h2><ul>
<li>Dig som söker en cykelhjälm i storlek 46–51 cm</li>
<li>Dig som vill ha en cykelhjälm med integrerat visir</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Cykelhjälm</li>
<li>Märke: Giant</li>
<li>Modell: Lena</li>
<li>Färg: Gloss Coral</li>
<li>Storlek: 46–51 cm</li>
<li>Vaddering: TransTextura Plus</li>
```

### 46104 (10472235270410, k_46sak2_utkast.json): RÄTTA

Live ACTIVE, vendor Liv, en variant 800002259, EAN 4713250839417, 459 kr, lager 4. Egen källa: 46–51 cm, skärm i skum, insektsnät, vaddering, band. Egen artikel (annan färg och EAN än 46103), titlarna skiljer färgerna. RÄTTA: "antibakteriell" stryks i meta, brödtext och specifikation (hälsopåstående).

**meta**

Före:
```
har insektsnät, antibakteriell vaddering och
```
Efter:
```
har insektsnät, TransTextura Plus-vaddering och
```

**html**

Före:
```
insektsnät och antibakteriell TransTextura Plus-vaddering.</p><h2>Passar för</h2><ul>
<li>Dig som söker en cykelhjälm med insektsnät</li>
<li>Dig som vill ha en cykelhjälm i storlek 46–51 cm</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Cykelhjälm</li>
<li>Märke: Giant</li>
<li>Modell: Lena</li>
<li>Färg: Gloss Aqua</li>
<li>Storlek: 46–51 cm</li>
<li>Vaddering: Antibakteriell TransTextura Plus</li>
```
Efter:
```
insektsnät och TransTextura Plus-vaddering.</p><h2>Passar för</h2><ul>
<li>Dig som söker en cykelhjälm med insektsnät</li>
<li>Dig som vill ha en cykelhjälm i storlek 46–51 cm</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Cykelhjälm</li>
<li>Märke: Giant</li>
<li>Modell: Lena</li>
<li>Färg: Gloss Aqua</li>
<li>Storlek: 46–51 cm</li>
<li>Vaddering: TransTextura Plus</li>
```

### 46105 (10472237367562, k_46sak2_utkast.json): GODKÄND

Live ACTIVE, Lazer, en variant BLC2227891160, EAN 5400974014747, 689 kr, lager 1. Egen källa: KinetiCore, automatiskt EZ Fit-system, 46–52 cm, barn från 1 år. Viktraden är delvis trasig ("240 g 240 g 240 cm - 240 lbs"); den entydiga delen 240 g bekräftas av https://lazersport.com/products/pnut-kineticore (240 g, Toddler uni-size 46–52 cm), R2. "Starkare material", "absorberar slagkraft", "mer skydd", "bättre ventilerad" utelämnade; CE-CPSC ur live-titeln utelämnat. Ingen dubblett (Pnut 2.0 KC 10472298348810 är annan modell och DRAFT). Spärrad som tidigare avvisad, behöver undantag.

### 46106 (10472237596938, k_46sak2_utkast.json): RÄTTA

Live ACTIVE, Lazer, en variant BLC2207887978, EAN 5420078879875, 1699 kr, lager 3. Limar-stycket är rätt utelämnat; Turnfit plus, 15-luftventilationssystem (15 ventiler bekräftas av återförsäljare, t.ex. https://www.99bikes.com.au/helmet-lazer-chiru-matte-red) och CE/CPSC/AS är entydiga. RÄTTA: källan listar storlekarna S, M och L och sedan "Vikt: 300g", men produkten säljs som en variant utan storlek; återförsäljare anger 300 g bara för storlek S (M 340 g, L 370 g), så vikten är inte entydig för just denna artikel (R1/R2) och stryks i meta, brödtext, Passar för och specifikation. Kvar finns tre entydiga fakta utöver titeln. Storleken på exemplaret är okänd, se frågor.

**meta**

Före:
```
 Hjälmen väger 300 g.
```
Efter:
```

```

**html**

Före:
```
 Hjälmen väger 300 g.</p><h2>Passar för</h2><ul>
<li>Dig som söker en cykelhjälm på 300 g</li>
<li>Dig som söker en cykelhjälm med Turnfit plus-system</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Cykelhjälm</li>
<li>Märke: Lazer</li>
<li>Modell: Chiru</li>
<li>Färg: Röd</li>
<li>System: Turnfit plus</li>
<li>Ventilation: 15 öppningar</li>
<li>Vikt: 300 g</li>

```
Efter:
```
</p><h2>Passar för</h2><ul>
<li>Dig som söker en cykelhjälm med 15 ventilationsöppningar</li>
<li>Dig som söker en cykelhjälm med Turnfit plus-system</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Cykelhjälm</li>
<li>Märke: Lazer</li>
<li>Modell: Chiru</li>
<li>Färg: Röd</li>
<li>System: Turnfit plus</li>
<li>Ventilation: 15 öppningar</li>

```

### 46107 (10472237629706, k_46sak2_utkast.json): GODKÄND

Live ACTIVE, Lazer, en variant BLC2167880917, EAN 5420078809179, 729 kr, lager 2. Egen källa: Comfit3-spännsystem, 6 ventilationsöppningar, vikt 260 g, CE/CPSC/AS. Det maskinöversatta stycket ("Bob Bobs Bobs …") och alla säkerhetsformuleringar ("säkerställer säkerheten", "bekvämt och säkert", "svalt") är utelämnade. 6 ventiler och Comfit3 stämmer med återförsäljare; vikten varierar mellan återförsäljare (260–277 g), men egen källa anger entydigt 260 g (R1). Spärrad (utanfor-tills-vidare), behöver undantag.

### 46108 (10472238743818, k_46sak2_utkast.json): GODKÄND

Live ACTIVE, Lazer, tagg Cykelbelysning, en variant PLZ2167881921, EAN 5420078819222, 159 kr, lager 31. Bara tekniska uppgifter ordagrant ur källan (CR2032, 37 h, 4 lumen, 12 g); "göra dig synlig" och "ett av de bästa sätten" utelämnade. Inga synlighets- eller säkerhetslöften. Titel 43 tecken, unik.

### 46109 (10472242249994, k_46sak2_utkast.json): RÄTTA

Live ACTIVE, Shimano, en variant VMAFHTX5008AZBL, ingen EAN, 219 kr, lager 18. Typbytet Bakdäck → Frihjulsnav bak har stöd i egen källtext (R7) och är rätt; FH-TX5008-QR används av återförsäljare för QR-versionen. O.L.D. 135 och flänsdiameter 53,8 mm stämmer med återförsäljardata. RÄTTA: (1) växeluppgiften är motsägande i egen källa ("8/9-delat" i rubriken, "Bakre hastigheter: 11/10/9/8" i specifikationen; återförsäljare anger 8/9/10) och "8/9-delat" är dessutom en maskinöversättning av 8/9-speed, så den stryks i titel, meta, brödtext, Passar för och specifikation (R2, R4-praxis för motsägande värden). (2) Nav är neutrum: "Frihjulsnaven" → "Frihjulsnavet", "en frihjulsnav" → "ett frihjulsnav". (3) Metans första mening saknade verb. Färg Svart ur live-titeln enligt praxis.

**titel**

Före:
```
Frihjulsnav bak Shimano FH-TX5008-QR, 8/9-delat
```
Efter:
```
Frihjulsnav bak Shimano FH-TX5008-QR för V-broms
```

**meta**

Före:
```
Frihjulsnav bak Shimano FH-TX5008-QR för mountainbikes med V-broms. Navet har snabbkoppling, är 8/9-delat och har O.L.D. 135 mm.
```
Efter:
```
Frihjulsnavet Shimano FH-TX5008-QR monteras bak på mountainbikes med V-broms. Navet har snabbkoppling och O.L.D. 135 mm.
```

**html**

Före:
```
<p>Frihjulsnaven Shimano FH-TX5008-QR monteras bak på mountainbikes med V-broms. Navet har snabbkoppling och är 8/9-delat.</p><h2>Passar för</h2><ul>
<li>Dig som söker en frihjulsnav bak till en mountainbike med V-broms</li>
<li>Dig som söker ett 8/9-delat nav med snabbkoppling</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Frihjulsnav bak</li>
<li>Märke: Shimano</li>
<li>Modell: FH-TX5008-QR</li>
<li>Bromstyp: V-broms</li>
<li>Fastsättning: Snabbkoppling</li>
<li>Delning: 8/9-delat</li>

```
Efter:
```
<p>Frihjulsnavet Shimano FH-TX5008-QR monteras bak på mountainbikes med V-broms. Navet har snabbkoppling och O.L.D. 135 mm.</p><h2>Passar för</h2><ul>
<li>Dig som söker ett frihjulsnav bak till en mountainbike med V-broms</li>
<li>Dig som söker ett nav med snabbkoppling och O.L.D. 135 mm</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Frihjulsnav bak</li>
<li>Märke: Shimano</li>
<li>Modell: FH-TX5008-QR</li>
<li>Bromstyp: V-broms</li>
<li>Fastsättning: Snabbkoppling</li>

```

### 46110 (10472242446602, k_46sak2_utkast.json): GODKÄND

Live ACTIVE, Shimano, en variant VMESMRT64SEC (S = 160 mm), EAN 4550170451974, 469 kr, lager 5. 160 mm och Center Lock ur live-titeln; källans serietext med 220/203 mm och alla bromsprestandapåståenden ("kraftfull", "10 % mer bromskraft", "jämn bromsning") är utelämnade. Kompatibilitet harts/metall står ordagrant i källan. Skild från SM-RT64 180 mm (46005, annan EAN 4550170451967). Bromsdel skrivs enligt beslutet 2026-11-08.

### 46111 (10472242512138, k_46sak2_utkast.json): GODKÄND

Live ACTIVE, Shimano, en variant VMISMRT86L2, EAN 4524667744689, 1639 kr, lager 9. EAN är SM-RT86 L 203 mm 6-bult (https://nanobike.de/en/bike-parts/brakes/discs/8576/shimano-disc-sm-rt86-ice-tech-6-loch-203-mm). ICE TECHNOLOGY och tre lager rostfritt stål/aluminium/rostfritt stål ur egen källa; "jämn prestanda", "kylteknik", "värmebeständighet", "mindre blekning", "längre livslängd" och "certifierad" utelämnade. Modellbeteckningen kan läggas till senare (v1.6, EAN-träff) men krävs inte. Skild från SM-RT86 180 mm (10472240349450, avvisad 46208). Spärrad som tidigare avvisad (bromsdel), behöver undantag.

### 46112 (10472243200266, k_46sak2_utkast.json): GODKÄND

Live ACTIVE, Shimano, en variant BLR400RL, ingen EAN, 259 kr, lager 7. Källan är delvis maskinöversatt; de entydiga delarna används: "SHIMANO SORA BL-R400 bromshandtag … droppformade styren", klämma 23,8–24,2 mm (Shimanos klämdiameter för droppstyre), kompatibel med Dual-Pivot-bromssystem; höger ur live-titeln och SKU (BLR400RL). Typbytet Bromslänk → Bromshandtag har stöd i källtexten (R7). "Aerodynamisk", "fjädring", "SUPER SLR" och "bekväm skyddande ringform" utelämnade.
