# Granskningsutlåtande k_46barn1, barnprodukter och barntransport (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan text får faktatext även i tidigare utanför-kategorier), LARDOMAR, butiksprofilen, standarden §16, `c_granskarprompt.md`, praxis i `k_utlatande_43.md`/`k_utlatande_46sak*.md` och formatet i `k_utlatande_43.json`.

Alla 15 utkast är ACTIVE med en variant (Default Title). Titel ≤70 tecken och ≤2 kommatecken, SEO ≤43, meta 112–144 tecken med verb, "Passar för" på alla. Standardblocket är exakt som i `b_skriv_24.json`; leveranstidsmeningen finns på exakt de sex produkter som har taggen På beställning (46607, 46611, 46612, 46622, 46623, 46624). Titlar, SEO-titlar och metatexter är unika inom batchen och mot alla andra utkast- och skrivfiler (enda träffen är 46611 mot sitt eget oskrivna utkast i k_20a). Butiken söktes på SKU, streckkod och modellord: inga exakta dubbletter (R12a); Stiga Cruiser svart/rosa/grön och Cruiser Eco har olika SKU/EAN, Cargobike Classic/Delight Kindergarten/Dog är olika artiklar. Varje rättning är ETT sammanhängande före/efter-par per fält, och före-texten förekommer exakt en gång i fältet (kontrollerat i python). `skrivfil_kontroll.py` ger 0 formatfel och 0 varningar på både utkasten och de rättade texterna.

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_46barn1.json`.

## Resultat: 4 GODKÄND, 11 RÄTTA, 0 UNDERKÄND

| nr | id | dom | rättade fält |
|---|---|---|---|
| 46601 | 10411887165706 | GODKÄND | – |
| 46602 | 10462150525194 | GODKÄND | – |
| 46603 | 10462224417034 | GODKÄND | – |
| 46604 | 10462806212874 | RÄTTA | html, meta |
| 46606 | 10468708843786 | GODKÄND | – |
| 46607 | 10468710711562 | RÄTTA | html, meta |
| 46610 | 10470902333706 | RÄTTA | html |
| 46611 | 10470905282826 | RÄTTA | meta, html |
| 46612 | 10470906659082 | RÄTTA | html |
| 46613 | 10470985138442 | RÄTTA | seo_title |
| 46615 | 10472233664778 | RÄTTA | seo_title |
| 46620 | 10472248213770 | RÄTTA | html, meta |
| 46622 | 10472249688330 | RÄTTA | html |
| 46623 | 10472249852170 | RÄTTA | html |
| 46624 | 10472250212618 | RÄTTA | html |

## Löften och säkerhetsord

Alla texter genomsöktes efter säkerhets-, skydds-, hälso-, utvecklings-, prestanda- och kvalitetsord (säker, säkerhet, skydd, skyddar, trygg, stabil, slitstark, hållbar, kvalitet, punkteringsfri/-skyddad, bekväm, utveckling, motorik, väderbeständig, kraftfull). Kvar efter rättning: bälten, sele och reflex/reflektor som ren utrustning, "tillverkad i Sverige enligt tillverkaren" (ordagrant i källan), åldersuppgifter ur källan. Två subtila löften rättas: lastgränsen utan "enligt tillverkaren" i inledningen på 46610 och i metan på 46611, och "punkteringsfria" på 46610. Räckvidd på fem lastcyklar saknade "enligt tillverkaren" (§16.2).

## Per produkt

### 46601 (10411887165706): GODKÄND

Live ACTIVE, SKU 214072, EAN 4511890214072, 269 kr, lager 9. Ramfästet: allt ur egen källa (extra fäste för Urban Iki barnstolar, ramar 28–38 mm). Den otydliga raden om "två hjul omväxlande" rätt utelämnad (R2). Inga säkerhetsord. Fäste, inte bärande del med lastuppgift i källan; v1.10 undantar barntransport. Spärrad (utanfor-tills-vidare), behöver undantag enligt beslutet 2026-11-08.

### 46602 (10462150525194): GODKÄND

Live ACTIVE, SKU E26703-ZWART, EAN 8719636019981, 70789 kr, lager 1. Allt ur egen källa; trasiga rader ("12,5A, 12,5Wh …", "Shiflex", "Shimano 4x4") och marknadsord ("torra och säkra") rätt utelämnade. Hjulstorlek 12"/26" bekräftad för exakt SKU E26703-ZWART på https://velomarket.ee/en/products/electric-cargo-bike-cangoo-buzz-black (leverantörens sida, ej tillverkarens). Lastgräns hittades inte på nätet; "Maximal lastgräns: Ej känd" och meningen i texten följer v1.10. Bälten bara som utrustning.

### 46603 (10462224417034): GODKÄND

Live ACTIVE, SKU 7462-5601-00, EAN 7318686256011, 529 kr, lager 5. Allt ur egen källa: hög rygg, återvunnen plast, bälte, vadderad rygg och sits, från ca 6 månader, tillverkad i Sverige (ursprung ordagrant, "enligt tillverkaren", två gånger totalt). "Bekväm", "grönare val" och säkerhetsbälte rätt utelämnade. Annan SKU/EAN än Cruiser svart/rosa/grön. Spärrad (utanfor-tills-vidare), behöver undantag.

### 46604 (10462806212874): RÄTTA

Live ACTIVE, SKU 9044, EAN 5902308590441, 129 kr, lager 3. Uppgifterna stämmer (S, 4–6 år, 15 cm, inre vaddering, justerbar); skyddslöftet och "linsen" rätt utelämnade. RÄTTA (R11): inledningen och metan är cirkulära ("Handskarna Cars är handskar/barnhandskar"). Rättningen behåller samma fakta.

- **html** före: `<p>Handskarna Cars är handskar för barn i storlek S, avsedda för ålder 4–6 år. De har inre vaddering och är justerbara.</p>`
- **html** efter: `<p>Handskarna Cars är gjorda för barn i åldern 4–6 år och har inre vaddering. De finns i storlek S och är justerbara.</p>`

- **meta** före: `Handskarna Cars är barnhandskar i storlek S för ålder 4–6 år och omkrets 15 cm, med inre vaddering. Artikelnummer 9044.`
- **meta** efter: `Handskarna Cars har inre vaddering och är gjorda för barn 4–6 år, i storlek S med omkrets 15 cm. Färg röd, artikelnummer 9044.`

### 46606 (10468708843786): GODKÄND

Live ACTIVE, SKU 0756E, EAN 4021834756013, 109 kr, lager 103. Tunn men entydig källa: barnhjul 16 tum, bredd 55 mm (två fakta utöver titeln, R3). Längdraderna rätt utelämnade (felaktiga etiketter). Typord Stänkskärmar enligt tagg och syskon. Inga löften.

### 46607 (10468710711562): RÄTTA

Live ACTIVE, SKU 1521-23, EAN saknas, 509 kr, lager 1. Fakta ur egen källa (mjuk, handtag, hopfällbar, två sitsar bredvid varandra, passar även andra märken). RÄTTA: "i lådan" är otydligt för kunden (kan läsas som förpackningen); produkten är tillbehör till lastcykel (taggen Lastcykel, Cargobike of Sweden), så "i lastcykelns låda". Taggen På beställning finns och leveranstidsmeningen finns. Spärrad (utanfor-tills-vidare), behöver undantag.

- **html** före: `<p>Barnsitsen Kids Seat Soft från Cargobike of Sweden har mjuk sits och handtag. Den är hopfällbar, och två sitsar får plats bredvid varandra i lådan.</p>`
- **html** efter: `<p>Barnsitsen Kids Seat Soft från Cargobike of Sweden har mjuk sits och handtag. Den är hopfällbar, och två sitsar får plats bredvid varandra i lastcykelns låda.</p>`

- **meta** före: `Barnsitsen Kids Seat Soft från Cargobike of Sweden är mjuk och hopfällbar med handtag. Två sitsar får plats bredvid varandra i lådan.`
- **meta** efter: `Barnsitsen Kids Seat Soft från Cargobike of Sweden är mjuk och hopfällbar med handtag. Två sitsar får plats bredvid varandra i lastcykelns låda.`

### 46610 (10470902333706): RÄTTA

Live ACTIVE, SKU AC_DELUXE, EAN saknas, 41169 kr, lager 1. Specifikationen stämmer med egen källa. RÄTTA: (1) lastgränsen står två gånger (inledning utan "enligt tillverkaren" och specifikation); R4 tillåter en gång, så meningen i inledningen tas bort. (2) "punkteringsfria" är ett kvalitets-/prestandalöfte (källan: "inte behöver oroa dig för punkteringar"); utelämnas som för "punkteringsskyddade" i 46622/46624. (3) Räckvidd är ett räckviddspåstående (standard §16.2, praxis "Räckvidd: Upp till X km enligt tillverkaren") och får "enligt tillverkaren"; texten har då två (lastkapacitet och räckvidd).

- **html** före: `<p>El-lastcykeln Deluxe från Amladcykler har lastlåda, motor på 250 W och Shimano Tourney med 6 växlar. Cykeln levereras med digital LCD-display och har en lastkapacitet på 150 kg.</p><h2>Passar för</h2><ul>
<li>Dig som söker en el-lastcykel med lastlåda</li>
<li>Dig som vill ha en el-lastcykel med sele och stolar för fyra barn</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: El-lastcykel</li>
<li>Märke: Amladcykler</li>
<li>Modell: Deluxe</li>
<li>Display: Digital LCD</li>
<li>Motor: 250 W</li>
<li>Batteri: 36 V, 9 Ah (litiumjon)</li>
<li>Räckvidd: Upp till 40 km</li>
<li>Växelsystem: Shimano Tourney (SiS), 6 växlar</li>
<li>Bromsar: Tektro/Bengal hydrauliska skivbromsar (fram), V-broms (bak)</li>
<li>Däck: 20 tum (fram), 26 tum (bak), punkteringsfria enligt tillverkaren</li>`
- **html** efter: `<p>El-lastcykeln Deluxe från Amladcykler har lastlåda, motor på 250 W och Shimano Tourney med 6 växlar. Cykeln levereras med digital LCD-display.</p><h2>Passar för</h2><ul>
<li>Dig som söker en el-lastcykel med lastlåda</li>
<li>Dig som vill ha en el-lastcykel med sele och stolar för fyra barn</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: El-lastcykel</li>
<li>Märke: Amladcykler</li>
<li>Modell: Deluxe</li>
<li>Display: Digital LCD</li>
<li>Motor: 250 W</li>
<li>Batteri: 36 V, 9 Ah (litiumjon)</li>
<li>Räckvidd: Upp till 40 km enligt tillverkaren</li>
<li>Växelsystem: Shimano Tourney (SiS), 6 växlar</li>
<li>Bromsar: Tektro/Bengal hydrauliska skivbromsar (fram), V-broms (bak)</li>
<li>Däck: 20 tum (fram), 26 tum (bak)</li>`

### 46611 (10470905282826): RÄTTA

Live ACTIVE, SKU 1970, EAN saknas, 50499 kr, lager 0. Fakta ur egen källa; "vädertåligt", "höghållfasta", "kraftfullt" rätt utelämnade. RÄTTA: metan återger lastgränsen en andra gång utan "enligt tillverkaren" (R4); ersätts med artikelnummer. Räckvidd är ett räckviddspåstående (standard §16.2, praxis "Räckvidd: Upp till X km enligt tillverkaren") och får "enligt tillverkaren"; texten har då två (lastkapacitet och räckvidd). Krocken med k_20a_utkast.json gäller samma produkt (oskrivet utkast 21064) och är ingen dubblett. På beställning-meningen finns.

- **meta** före: `El-lastcykeln Svensson Family har en låda för upp till 4 barn, 250 W motor och 12,8 Ah batteri. Lastkapacitet lådan 100 kg plus förare 100 kg.`
- **meta** efter: `El-lastcykeln Svensson Family har en låda för upp till 4 barn, 250 W motor och 12,8 Ah batteri. Artikelnummer 1970.`

- **html** före: `<li>Räckvidd: 20–40 km</li>`
- **html** efter: `<li>Räckvidd: 20–40 km enligt tillverkaren</li>`

### 46612 (10470906659082): RÄTTA

Live ACTIVE, SKU 1273, EAN saknas, 75979 kr, lager 0. Fakta ur egen källa; trasiga raden "210 x 210 kg …" och marknadsord rätt utelämnade. Egen produkt (SKU 1273), skild från Delight Kindergarten. RÄTTA: Räckvidd är ett räckviddspåstående (standard §16.2, praxis "Räckvidd: Upp till X km enligt tillverkaren") och får "enligt tillverkaren"; texten har då två (lastkapacitet och räckvidd). På beställning-meningen finns.

- **html** före: `<li>Räckvidd: 20–40 km</li>`
- **html** efter: `<li>Räckvidd: 20–40 km enligt tillverkaren</li>`

### 46613 (10470985138442): RÄTTA

Live ACTIVE, SKU 74-6250-01, EAN 7318686250019, 469 kr, lager 6. Fakta ur egen källa (bälte, vadderad rygg och sits, reflex på baksidan, tillverkad i Sverige); "så säkert som möjligt" och skyddsrekommendationen rätt utelämnade, reflexen bara som fakta (v1.9). RÄTTA (R9): beskrivande ord med stor bokstav i SEO-titeln, som i titeln. Spärrad (tidigare-avvisade), behöver undantag.

- **seo_title** före: `Babykälke Stiga Cruiser svart`
- **seo_title** efter: `Babykälke Stiga Cruiser Svart`

### 46615 (10472233664778): RÄTTA

Live ACTIVE, SKU 74-6250-07, EAN 7318686250071, 469 kr, lager 11. Som 46613, egen SKU 74-6250-07/EAN. RÄTTA (R9): "Rosa" med stor bokstav i SEO-titeln. Spärrad (utanfor-tills-vidare), behöver undantag.

- **seo_title** före: `Babykälke Stiga Cruiser rosa`
- **seo_title** efter: `Babykälke Stiga Cruiser Rosa`

### 46620 (10472248213770): RÄTTA

Live ACTIVE, SKU 59359, EAN 5902308593596, 129 kr, lager 12. Uppgifterna stämmer (S, 4–6, 15 cm, inre vaddering, justerbara manschetter); skyddslöftet rätt utelämnat. RÄTTA (R11): cirkulär inledning och meta ("Handskarna Wish är handskar/barnhandskar").

- **html** före: `<p>Handskarna Wish är handskar för barn i storlek S, avsedda för ålder 4–6 år. De har inre vaddering och justerbara manschetter.</p>`
- **html** efter: `<p>Handskarna Wish är gjorda för barn i åldern 4–6 år och har inre vaddering. De finns i storlek S och har justerbara manschetter.</p>`

- **meta** före: `Handskarna Wish är barnhandskar i storlek S för ålder 4–6 år och omkrets 15 cm, med inre vaddering. Artikelnummer 59359.`
- **meta** efter: `Handskarna Wish har inre vaddering och justerbara manschetter och är gjorda för barn 4–6 år, storlek S. Artikelnummer 59359.`

### 46622 (10472249688330): RÄTTA

Live ACTIVE, SKU 1153, EAN saknas, 84119 kr, lager 0. Fakta ur egen källa; "garantera barnens säkerhet", "punkteringsskyddade" och trasiga raden rätt utelämnade. RÄTTA: grammatik "klar plexiglas" → "klart plexiglas" (två ställen) och Räckvidd är ett räckviddspåstående (standard §16.2, praxis "Räckvidd: Upp till X km enligt tillverkaren") och får "enligt tillverkaren"; texten har då två (lastkapacitet och räckvidd). Rättningen är ett sammanhängande stycke från inledningen till räckviddsraden. På beställning-meningen finns.

- **html** före: `<p>El-lastcykeln Delight Kindergarten från Cargobike of Sweden har en låda för upp till sex barn, med sex individuella bälten och en öppningsbar front av klar plexiglas.</p><h2>Passar för</h2><ul>
<li>Dig som söker en el-lastcykel med låda för upp till sex barn</li>
<li>Dig som vill ha en låda med öppningsbar front</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: El-lastcykel</li>
<li>Märke: Cargobike of Sweden</li>
<li>Modell: Delight Kindergarten</li>
<li>Låda: Upp till sex barn, sex individuella bälten, öppningsbar front av klar plexiglas</li>
<li>Motor: Ananda centralmotor, 250 W, 110 Nm</li>
<li>Batteri: 16 Ah, 36 V</li>
<li>Räckvidd: 30–50 km</li>`
- **html** efter: `<p>El-lastcykeln Delight Kindergarten från Cargobike of Sweden har en låda för upp till sex barn, med sex individuella bälten och en öppningsbar front av klart plexiglas.</p><h2>Passar för</h2><ul>
<li>Dig som söker en el-lastcykel med låda för upp till sex barn</li>
<li>Dig som vill ha en låda med öppningsbar front</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: El-lastcykel</li>
<li>Märke: Cargobike of Sweden</li>
<li>Modell: Delight Kindergarten</li>
<li>Låda: Upp till sex barn, sex individuella bälten, öppningsbar front av klart plexiglas</li>
<li>Motor: Ananda centralmotor, 250 W, 110 Nm</li>
<li>Batteri: 16 Ah, 36 V</li>
<li>Räckvidd: 30–50 km enligt tillverkaren</li>`

### 46623 (10472249852170): RÄTTA

Live ACTIVE, SKU 1272, EAN saknas, 68909 kr, lager 0. Fakta ur egen källa (SKU 1272, 55 kg, lådmått 91,5 x 61,5 x 49,5 cm). RÄTTA: Räckvidd är ett räckviddspåstående (standard §16.2, praxis "Räckvidd: Upp till X km enligt tillverkaren") och får "enligt tillverkaren"; texten har då två (lastkapacitet och räckvidd). På beställning-meningen finns.

- **html** före: `<li>Räckvidd: 20–40 km</li>`
- **html** efter: `<li>Räckvidd: 20–40 km enligt tillverkaren</li>`

### 46624 (10472250212618): RÄTTA

Live ACTIVE, SKU 1162, EAN 7350097566105, 82669 kr, lager 0. Fakta ur egen källa (SKU 1162, EAN 7350097566105); "sitta säkert" och "punkteringsskyddade" rätt utelämnade, inga bromsar i källan. RÄTTA: Räckvidd är ett räckviddspåstående (standard §16.2, praxis "Räckvidd: Upp till X km enligt tillverkaren") och får "enligt tillverkaren"; texten har då två (lastkapacitet och räckvidd). På beställning-meningen finns.

- **html** före: `<li>Räckvidd: 30–50 km</li>`
- **html** efter: `<li>Räckvidd: 30–50 km enligt tillverkaren</li>`

## Avvisade (k_46barn1_avvisade.json)

Alla nio avvisningar står sig och lyfts inte: 46605 Aest (fyra färgvarianter, 2269 mot 729 kr, trasig källa), 46608 Fiido T2 (titel staket, källa stänkskärm), 46609 Liv Tempt 0 (titel ungdomscykel, källa damcykel), 46614 Peltonen Delta Step JR (olika pris, lager 0), 46616 Tempish Dasty (37–40 mot 40–43), 46617–46619 FILA (titel rullskridskor, källa isskridskoblad), 46621 Winnie the Pooh (vantar mot handskar). Live-kontrollen bekräftar skälen.

## Före skrivning

1. Spärrlistan: `skrivfil_kontroll.py` ger 5 FEL för spärrade produkter: 46601, 46603, 46607, 46615 (utanfor-tills-vidare-2026-11-04) och 46613 (tidigare-avvisade-2026-11-04). De spärrades bara på grund av kategori (barn, barnstol, barntransport) och omfattas av beslutet 2026-11-08. En undantagspost med hänvisning till beslutet måste läggas in i `sparrlista.json` (tillägg, R14) innan skrivfilen byggs.
2. 46602: lastgränsen kunde inte hittas på nätet; "Ej känd" står kvar (v1.10).
