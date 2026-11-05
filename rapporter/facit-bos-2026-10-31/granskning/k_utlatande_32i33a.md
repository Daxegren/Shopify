# Granskningsutlåtande k_32i och k_33a (2026-11-05)

**Granskare:** oberoende Opus-granskare, endast läsning. Inget ändrades i Shopify och inget committades. Live-data lästes via `shopify_api.py` (BEST OF SPORTS, bestofsports.se bekräftad). Alla 15 produkter är ACTIVE med lager > 0 och har en variant.

**Underlag:** CLAUDE.md, regelbok v1.4–v1.10 (R1, R2, R4, R7, R12, v1.9, v1.10), BESLUTSLOGG (slutet: kosttillskott skrivs utan förhandsfråga, bara fakta; klosspedaler tillåtna), LARDOMAR, butiksprofilen, kosttillskott-exempel-2026-11-05.md och praxis i k_utlatande_30ab/28jk30e/32cde.

**Resultat:** 3 godkända, 9 att rätta, 3 underkända. Efter rättningarna ger `skrivfil_kontroll.py` 0 fel och 0 varningar för de 12 som går vidare. `kontrollera_produkttext.py` ger bara känd falsklarm: 'halsa' på ingrediensordet koffein och metalängd under 130 (profilens gräns är 70–155). Titel, SEO och meta är unika mot alla `*_utkast.json` och `k_skriv_*.json`.

## Sammanställning

| nr | id | dom | fält som rättas |
|---|---|---|---|
| 32019 | 10472241168650 | GODKÄND | - |
| 32036 | 10472294940938 | RÄTTA | html |
| 32037 | 10475424284938 | GODKÄND | - |
| 32040 | 10494687805706 | GODKÄND | - |
| 33001 | 10411849646346 | UNDERKÄND | - |
| 33002 | 10462770135306 | RÄTTA | meta, html |
| 33003 | 10462770299146 | RÄTTA | meta, html |
| 33004 | 10462773641482 | UNDERKÄND | - |
| 33005 | 10462777770250 | RÄTTA | meta, html |
| 33006 | 10462778458378 | RÄTTA | titel, seo_title, meta, html |
| 33007 | 10462778589450 | RÄTTA | meta, html |
| 33008 | 10462791991562 | UNDERKÄND | - |
| 33009 | 10470944768266 | RÄTTA | meta, html |
| 33010 | 10471287783690 | RÄTTA | meta, html |
| 33011 | 10472269873418 | RÄTTA | meta, html |

## Viktiga fynd

1. **33001 Melatonin underkänns.** Läkemedelsverket säger på sin egen frågetjänst (fragor.lakemedelsverket.se, svar 2025-09-16): *"Melatonin är klassat som läkemedel i Sverige och får inte säljas som kosttillskott. Det får endast säljas på apotek."* Läkemedelsverkets pressmeddelande 2025-03-24 (via.tt.se/pressmeddelande/3839885) talar om "olaglig försäljning av melatonin som kosttillskott" och om säljförbud. lakemedelsverket.se gick inte att läsa direkt (inloggningssida). Produkten säljs just nu med live-texten "främjar snabbare insomning". Det som behöver beslutas är försäljningen, inte texten.
2. **Produktnamn som är påståenden (förordning 1924/2006 art. 1.3).** Ett handelsnamn som kan uppfattas som ett hälsopåstående kräver ett godkänt påstående bredvid sig. "Appetite Control" (33008) och "Beauty Body Shaper" (33004) är bokstavliga viktlöften och kan inte tas bort utan att produkten blir oidentifierbar: de underkänns. 33004 har dessutom synefrin (bitter apelsin) tillsammans med koffein, utan angiven synefrinmängd. Livsmedelsverket anger hälsorisk över 40 mg per dag och även lägre doser vid kombination med koffein. "Tribido Max" (33006, tribulus + libido) rättas genom att namnet tas bort ur titel, SEO, meta och text. Vill David behålla namnet ska produkten underkännas.
3. **Osäkra mängder.** I 33002 och 33003 tas mängderna 2400/2500/150 mg bort: de saknar portion, och tillverkarens sida (trecnutrition.com/brands/trec/trec-core/boogieman-shot/) anger 2500/1000/200 mg per 50 ml för en annan receptur. I 33010 tas dosen 15 ml bort: tillverkaren anger 50 ml (en halv flaska) för exakt denna receptur, och en koffeindos som är tre gånger för låg får inte stå (R2).
4. **Inga effektord kvar** i titel, SEO, meta, Passar för, typ eller specifikation i någon av de 12 som går vidare. Live-typorden Adaptogen, Antioxidant, Viktminskningskapslar, Energishot och Koffeindrink är ersatta av Kosttillskott, vilket källorna stöder (R7). Ginseng, rosenrot, taurin, koffein och synefrin står bara som ingredienser.
5. **Cirkulär inledning** ("Namn är ett kosttillskott") i meta och första meningen i alla kosttillskott är rättad enligt praxis i k_30ab.
6. **Cykeldelar:** lastgränsen följer v1.10. Basil 5 kg kommer från Basils egen sida för exakt EAN 8715019701832. Övriga lastgränser är "Ej känd", eftersom ingen lastgräns hittades. I 32036 tas vikten 355 g bort (oklart om den gäller en pedal eller paret, samma skäl som i 32040), och singular rättas till plural. 32037 kräver att typordet **Styrstamshållare** läggs till i profilens godkanda_typord.

## Öppna frågor till David

- **Melatonin 33001:** avpublicera i den svenska butiken? Rekommendation: ja. Om inget görs fortsätter försäljning av något som Läkemedelsverket klassar som läkemedel.
- **33004 och 33008:** avpublicera, eller skriva med namnen och medveten risk? Rekommendation: avpublicera. Om inget görs ligger live-texterna med viktlöften kvar.
- **33006:** godkänner du att "Tribido Max" tas bort ur vår text? Rekommendation: ja.
- **Boogieman-familjen:** k_33c (33027–33031) har nyare Boogieman Shot-varianter med andra EAN-nummer, alltså inte dubbletter, och använder typordet "Energishot". k_33a använder "Kosttillskott". Typordet bör vara samma i hela familjen (R7). Rekommendation: Kosttillskott, eftersom "energi" ligger nära ett energilöfte.
- **Styrstamshållare** in i godkanda_typord?

## Utlåtande per produkt

### 32019 (10472241168650): GODKÄND

Live: ACTIVE, 'Center chain Shimano BSA 115mm/68mm BB-UN300 Square', VMEBBUN300B15B/EAN 4550170619183, 269 kr, lager 6, tom beskrivning. BSA, 68 mm skal och 115 mm axel står i live-titeln. Stålaxel och Square Taper (JIS) gäller hela BB-UN300-serien enligt bike-components p76645 ('Axle Material: Steel', 'Square Taper (JIS)') och bekräftas för exakt 68x115 (EBBUN300B15B) av bl.a. materiel-velo.com och bicyclewarehouse.com. Vevbultar är rätt utelämnade (återförsäljarna säger emot varandra). Ingen lastgräns finns någonstans: 'Ej känd' enligt v1.10. Första meningen är inte cirkulär. Typordet vevlager är bekräftat av David 2026-11-05.

### 32036 (10472294940938): RÄTTA

Live: ACTIVE, 'Pedaler GIANT Combo Touring Pedal', 230000095/EAN 4713250014166, 1589 kr, lager 4. Klosspedaler är tillåtna (David 2026-11-05). Dubbelsidig, vanliga skor och SPD-pedalkloss står i live-källan. Aluminiumkropp, Cr-Mo-axel, förseglade lager och 104x64x28 mm står på Giants egen sida (giant-bicycles.com/se/combo-touring-pedal-2022, där 230000095 syns i bildnamnen) och är godtagbara enligt v1.6. Ingen lastgräns hittades: 'Ej känd' (v1.10). Rättning: första meningen i singular ('Pedalen ... är dubbelsidig') stämmer inte med titel och meta (pedaler, ett par) och skrivs i plural. Vikten 355 g tas bort: Giant anger inte om den gäller en pedal eller paret, och i 32040 utelämnades vikten av exakt samma skäl (R2, enhetlighet).

- **html** före: `<p>Pedalen Giant Combo Touring är dubbelsidig. Ena sidan är lämplig för vanliga skor och den andra sidan för skor med SPD-pedalkloss. Maximal lastgräns är inte känd.</p><h2>Passar för</h2><ul>
<li>Dig som söker dubbelsidiga pedaler</li>
<li>Dig som använder både vanliga skor och skor med SPD-pedalkloss</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Dubbelsidiga pedaler</li>
<li>Ena sidan: Vanliga skor</li>
<li>Andra sidan: Skor med SPD-pedalkloss</li>
<li>Kropp: Aluminium</li>
<li>Axel: Cr-Mo</li>
<li>Lager: Förseglade kullager</li>
<li>Mått: 104 x 64 x 28 mm</li>
<li>Vikt: 355 g</li>
`
- **html** efter: `<p>Pedalerna Giant Combo Touring är dubbelsidiga. Ena sidan är lämplig för vanliga skor och den andra sidan för skor med SPD-pedalkloss. Maximal lastgräns är inte känd.</p><h2>Passar för</h2><ul>
<li>Dig som söker dubbelsidiga pedaler</li>
<li>Dig som använder både vanliga skor och skor med SPD-pedalkloss</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Dubbelsidiga pedaler</li>
<li>Ena sidan: Vanliga skor</li>
<li>Andra sidan: Skor med SPD-pedalkloss</li>
<li>Kropp: Aluminium</li>
<li>Axel: Cr-Mo</li>
<li>Lager: Förseglade kullager</li>
<li>Mått: 104 x 64 x 28 mm</li>
`

### 32037 (10475424284938): GODKÄND

Live: ACTIVE, 'BASIL 22-25,4 mm fästes på den främre korgen', 70183/EAN 8715019701832, 169 kr, lager 57. Live-källan: 'Fixed Mounted Stem Holder', 22–25,4 mm. Basils egen produktsida för exakt EAN 8715019701832 (basil.com/en/p/8715019701832/basil-fixed-mounted-stem-holder-black/) anger 'Max. 5 kg', stål, svart, 'suitable for stems of 22-25.4 mm' och FM-korgar. Lastgränsen är alltså tillverkarens egen för exakt artikeln och står en gång med 'enligt tillverkaren' i löptexten (v1.10). Mått är rätt utelämnade (live 15 x 9 x 8 cm, Basil 9,5 x 2 x 2,5 cm: motsägelse). Texten undviker motsägelsen styre/stam genom att bara ange diametern. Villkor: typordet Styrstamshållare finns inte i godkanda_typord och måste läggas till i profilen (översättning av 'stem holder', R7) innan skrivning.

### 32040 (10494687805706): GODKÄND

Live: ACTIVE, 'Landsvägscykels-pedaler Giant Road Comp, utan klossar', 230000082/EAN 4713250012971, 719 kr, lager 10. Klosspedaler tillåtna (David 2026-11-05). Look KEO-klossar, aluminiumstomme, inkapslade lager, 86,5 x 77,5 mm och 'utan klossar' står i live-källan. 'Slitstark', 'underhållsfria' och Giants märkeshistorik är rätt borta. Vikten 325 g är rätt utelämnad (oklart om per pedal eller par). Ingen lastgräns hittades: 'Ej känd' (v1.10). Titeln 'utan klossar' med liten bokstav avviker något från praxis i 'Framkorg Basil Bilbao FM, utan Handtag, Svart', men skriptet godtar den; ingen rättning.

### 33001 (10411849646346): UNDERKÄND

Melatonin är läkemedel i Sverige. Verifierat på Läkemedelsverkets egna kanaler: Läkemedelsverkets frågeforum (fragor.lakemedelsverket.se/org/lakemedelsverket/d/vem-far-salja-melatonin/, svar 2025-09-16): 'Melatonin är klassat som läkemedel i Sverige och får inte säljas som kosttillskott. Det får endast säljas på apotek.' Läkemedelsverkets pressmeddelande 2025-03-24 (via.tt.se/pressmeddelande/3839885/risk-att-melatonin-anvands-alltfor-lattvindigt, avsändare Läkemedelsverket): 'Läkemedelsverket ser även fler signaler om olaglig försäljning av melatonin som kosttillskott' och 'Myndigheten har fattat förbud om försäljning för flera melatonininnehållande produkter.' Livsmedelsverkets Kontrollwiki (artikel 82, Närliggande produkter till kosttillskott) listar melatonin bland ämnen som ofta klassas som läkemedel. Kosttillskottstext får inte skrivas. Dessutom är produkten fortfarande ute till försäljning (ACTIVE, lager 4) med live-texten 'främjar snabbare insomning', vilket är ett medicinskt påstående. Beslut för David: avpublicera eller arkivera produkten i den svenska butiken (texten är inte problemet, försäljningen är det).

### 33002 (10462770135306): RÄTTA

Live: ACTIVE, 'Koffeindrink TREC BOOGIEMAN SHOT FOREST FRUIT 100ml', 21553/EAN 5902114047320, 29 kr, lager 10. Inga påståenden eller effektord i titel, SEO, meta, Passar för eller specifikation; alla effektfraser ur källan är borta. Typbytet till Kosttillskott är tillåtet (källan säger 'kosttillskott i flytande form', R7). Koffein, taurin, ginseng och rosenrot står bara som ingredienser, inga effekter (skriptets 'halsa' på 'koffein' är falsklarm). Rättning 1: mängderna 2400/2500/150 mg tas bort. Källan anger inte om de gäller 50 ml eller hela flaskan, och tillverkarens sida (trecnutrition.com/brands/trec/trec-core/boogieman-shot/) anger andra värden per 50 ml (beta-alanin 2500 mg, citrullinmalat 1000 mg, koffein 200 mg) för en receptur utan ginseng och rosenrot. Mängden är alltså inte entydig (R1, R2). Raden med 'portionsstorlek anges inte' är inte korrekt formulerad kundtext. Rättning 2: cirkulär inledning i meta och första meningen (skriptvarning, praxis k_30ab). Dosen 50 ml stämmer med både live och tillverkaren. Obs: ingredienslistan i live (med ginseng och rosenrot) skiljer sig från tillverkarens nuvarande receptur; det är troligen en äldre version (eget EAN), så live-listan behålls men bör kontrolleras mot förpackningen. Nyare Boogieman-varianter med andra EAN finns i k_33c (33027–33031) med typordet Energishot: typorden bör samordnas (se utlåtandet).

- **meta** före: `Trec Boogieman Shot Forest Fruit är ett flytande kosttillskott med skogsbärssmak och koffein i en flaska på 100 ml. Dosen är 50 ml.`
- **meta** efter: `Trec Boogieman Shot Forest Fruit innehåller beta-alanin, citrullinmalat, taurin och koffein och har skogsbärssmak. Flaskan rymmer 100 ml, dosen är 50 ml.`
- **html** före: `<p>Trec Boogieman Shot Forest Fruit är ett flytande kosttillskott med skogsbärssmak i en flaska på 100 ml. Det innehåller bland annat beta-alanin, citrullinmalat, taurin och koffein.</p><h2>Passar för</h2><ul>
<li>Dig som vill ha ett flytande kosttillskott med koffein, beta-alanin och citrullinmalat</li>
<li>Dig som vill ha ett kosttillskott med skogsbärssmak</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Flytande kosttillskott</li>
<li>Smak: Skogsbär (Forest Fruit)</li>
<li>Förpackning: 100 ml</li>
<li>Innehåll: Enligt tillverkaren beta-alanin 2400 mg, citrullinmalat 2500 mg och koffein 150 mg (portionsstorlek för mängderna anges inte)</li>
`
- **html** efter: `<p>Trec Boogieman Shot Forest Fruit har skogsbärssmak och levereras i en flaska på 100 ml. Det flytande kosttillskottet innehåller bland annat beta-alanin, citrullinmalat, taurin och koffein.</p><h2>Passar för</h2><ul>
<li>Dig som vill ha ett flytande kosttillskott med koffein, beta-alanin och citrullinmalat</li>
<li>Dig som vill ha ett kosttillskott med skogsbärssmak</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Flytande kosttillskott</li>
<li>Smak: Skogsbär (Forest Fruit)</li>
<li>Förpackning: 100 ml</li>
`

### 33003 (10462770299146): RÄTTA

Live: ACTIVE, 'Koffeindryck TREC BOOGIEMAN SHOT GRAPEFRUIT-LIME 100ml', 16723/EAN 5902114017675, 29 kr, lager 9. Samma bedömning som 33002: inga påståenden kvar, typbytet till Kosttillskott är tillåtet, ingrediensorden är falsklarm. Rättning 1: mängderna utan portion tas bort (oklart om per 50 ml eller per flaska, och tillverkarens sida anger 2500/1000/200 mg per 50 ml för en annan receptur, R1/R2). Rättning 2: cirkulär inledning i meta och första meningen. Dosen 50 ml står kvar i specifikationen (stämmer med live och tillverkaren). SEO-titeln 'Kosttillskott Trec Boogieman Grapefruit' är unik.

- **meta** före: `Trec Boogieman Shot Grapefruit-Lime är ett flytande kosttillskott med koffein och smak av grapefrukt och lime. Flaskan rymmer 100 ml, dosen är 50 ml.`
- **meta** efter: `Trec Boogieman Shot Grapefruit-Lime innehåller beta-alanin, citrullinmalat, taurin och koffein och har smak av grapefrukt och lime. Flaskan rymmer 100 ml.`
- **html** före: `<p>Trec Boogieman Shot Grapefruit-Lime är ett flytande kosttillskott med smak av grapefrukt och lime i en flaska på 100 ml. Det innehåller bland annat beta-alanin, citrullinmalat, taurin och koffein.</p><h2>Passar för</h2><ul>
<li>Dig som vill ha ett flytande kosttillskott med koffein, beta-alanin och citrullinmalat</li>
<li>Dig som vill ha ett kosttillskott med smak av grapefrukt och lime</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Flytande kosttillskott</li>
<li>Smak: Grapefrukt och lime (Grapefruit-Lime)</li>
<li>Förpackning: 100 ml</li>
<li>Innehåll: Enligt tillverkaren beta-alanin 2400 mg, citrullinmalat 2500 mg och koffein 150 mg (portionsstorlek för mängderna anges inte)</li>
`
- **html** efter: `<p>Trec Boogieman Shot Grapefruit-Lime har smak av grapefrukt och lime och levereras i en flaska på 100 ml. Det flytande kosttillskottet innehåller bland annat beta-alanin, citrullinmalat, taurin och koffein.</p><h2>Passar för</h2><ul>
<li>Dig som vill ha ett flytande kosttillskott med koffein, beta-alanin och citrullinmalat</li>
<li>Dig som vill ha ett kosttillskott med smak av grapefrukt och lime</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Flytande kosttillskott</li>
<li>Smak: Grapefrukt och lime (Grapefruit-Lime)</li>
<li>Förpackning: 100 ml</li>
`

### 33004 (10462773641482): UNDERKÄND

Live: ACTIVE, 'Vitamin kapslar TREC TBL BEAUTY BODY SHAPER 90 kapslar', 17593, 169 kr, lager 6. Texten i sig har inga påståenden, men två skäl stoppar den. (1) Bitter apelsinextrakt (10 % synefrin) tillsammans med vattenfritt koffein. Livsmedelsverkets sida 'Risker med kosttillskott' (livsmedelsverket.se/livsmedel-och-innehall/kosttillskott/risker-med-kosttillskott/) säger att mer än 40 mg synefrin per dag kan innebära en hälsorisk, och att kombinationen synefrin och koffein kan innebära en hälsorisk även vid lägre doser. Synefrin per dos anges inte i källan, så vi kan inte visa att produkten ligger under någon gräns. (2) Produktnamnet 'Body Shaper' är i sig ett indirekt löfte om formad kropp eller viktminskning. Enligt förordning 1924/2006 art. 1.3 får ett handels- eller fantasinamn som kan uppfattas som ett hälsopåstående bara användas tillsammans med ett godkänt påstående, och vi har inget sådant. Namnet kan inte tas bort utan att produkten blir oidentifierbar (titel, etikett och bild säger Beauty Body Shaper). Dessutom består nästan hela live-texten av otillåtna påståenden ('Uppnå den perfekta figuren', 'gå ner i vikt'), vilket gäller tills produkten skrivs om eller tas bort. Beslut för David: avpublicera, eller skriva ändå med medveten risk.

### 33005 (10462777770250): RÄTTA

Live: ACTIVE, 'Adaptogen TREC ESSENSEY KOREAN GINSENG 90 kapslar', SKU 21770/EAN 5902114047535, 209 kr, lager 7. Alla påståenden ('uthållighet', 'vitalitet', 'stimulerande', 'träna längre') är borta. Typbytet från 'Adaptogen' (ett effektord) till Kosttillskott är rätt; källan säger 'tillskott'. 79 % extrakt och 10 % ginsenosider, 1 kapsel, 'helst före frukost' och varningarna stämmer. Ingen mängd per kapsel påstås. Rättning: cirkulär inledning i meta och första meningen. Metalängden 126 tecken (skriptets 130-gräns) ligger inom profilens 70–155.

- **meta** före: `Trec Essensey Korean Ginseng är ett kosttillskott med extrakt av koreansk ginsengrot i 90 kapslar. Dosen är 1 kapsel dagligen.`
- **meta** efter: `Trec Essensey Korean Ginseng innehåller extrakt av koreansk ginsengrot med 10 % ginsenosider. Burken har 90 kapslar och dosen är 1 kapsel dagligen.`
- **html** före: `<p>Trec Essensey Korean Ginseng är ett kosttillskott i kapselform som innehåller extrakt av koreansk ginsengrot (Panax ginseng).`
- **html** efter: `<p>Trec Essensey Korean Ginseng innehåller extrakt av koreansk ginsengrot (Panax ginseng) i kapselform.`

### 33006 (10462778458378): RÄTTA

Live: ACTIVE, 'Adaptogen TREC ESSENSEY TRIBIDO MAX TRIBULUS 90 kapslar', 21155/EAN 5902114046309, 109 kr, lager 11. Alla libido-, potens- och hälsopåståenden ur källan är borta, och 42 % extrakt, 95 % saponiner, dosen och varningarna stämmer. Men namnet 'Tribido' är en sammandragning av tribulus och libido och fungerar som ett indirekt potenslöfte (David: inga potenspåståenden; förordning 1924/2006 art. 1.3 om fantasinamn som kan uppfattas som påståenden). Rättning: 'Tribido Max' tas bort ur titel, SEO-titel, meta och första meningen. Produkten är ändå entydigt identifierad av Trec Essensey, tribulus, 90 kapslar och EAN. Handle ändras inte (R12a). Samtidigt rättas den cirkulära inledningen. Om David hellre vill behålla tillverkarens namn ska produkten i stället underkännas.

- **titel** före: `Kosttillskott Trec Essensey Tribido Max Tribulus, 90 kapslar`
- **titel** efter: `Kosttillskott Trec Essensey Tribulus, 90 kapslar`
- **seo_title** före: `Kosttillskott Trec Essensey Tribido Max`
- **seo_title** efter: `Kosttillskott Trec Essensey Tribulus`
- **meta** före: `Trec Essensey Tribido Max Tribulus är ett kosttillskott med tribulusextrakt (95 % saponiner) i 90 kapslar. Dosen är 1 kapsel dagligen.`
- **meta** efter: `Trec Essensey Tribulus innehåller tribulusextrakt (Tribulus terrestris) standardiserat till 95 % saponiner. Burken har 90 kapslar och dosen är 1 kapsel.`
- **html** före: `<p>Trec Essensey Tribido Max Tribulus är ett kosttillskott i kapselform som innehåller extrakt av tribulus`
- **html** efter: `<p>Kapslarna i Trec Essensey Tribulus innehåller extrakt av tribulus`

### 33007 (10462778589450): RÄTTA

Live: ACTIVE, 'Antioxidant TREC ESSENSEY MILK THISTLE 90 kapslar', 21766, 109 kr, lager 4. 'Antioxidant' (effektord) är rätt ersatt, och lever-, matsmältnings- och 'oxidativ stress'-påståendena är borta. 78 % extrakt, dosen 1 kapsel och de entydiga delarna av den trasiga varningsraden stämmer (R2). Ingen barn- eller gravidrad är påhittad. Rättning: cirkulär inledning i meta och första meningen.

- **meta** före: `Trec Essensey Milk Thistle är ett kosttillskott med extrakt av mariatistelfrö (78 %) i 90 kapslar. Dosen är 1 kapsel dagligen.`
- **meta** efter: `Trec Essensey Milk Thistle innehåller extrakt av mariatistelfrö (Silybum marianum). Burken har 90 kapslar och dosen är 1 kapsel dagligen.`
- **html** före: `<p>Trec Essensey Milk Thistle är ett kosttillskott i kapselform som innehåller extrakt av mariatistelfrö (Silybum marianum).`
- **html** efter: `<p>Trec Essensey Milk Thistle innehåller extrakt av mariatistelfrö (Silybum marianum) i kapselform.`

### 33008 (10462791991562): UNDERKÄND

Live: ACTIVE, 'Viktminskningskapslar TREC TBL APPETITE CONTROL 90 kapslar', 17595, 149 kr, lager 13. Texten har inga påståenden, men produktnamnet 'Appetite Control' är i sig ett påstående om aptitkontroll, alltså ett viktminskningslöfte. Det står i titel, SEO-titel, meta och löptext. Enligt förordning 1924/2006 art. 1.3 får ett handelsnamn som kan uppfattas som ett hälsopåstående bara användas tillsammans med ett godkänt påstående, och det finns inget godkänt påstående om aptit för Garcinia cambogia eller vita bönor. Namnet kan inte tas bort utan att produkten blir oidentifierbar. Dessutom innehåller källan en motsägelse (OA-extrakt och L-karnitin i texten finns inte i ingredienslistan, R2). Utkastets egen notering om franskt Garcinia-förbud är inte verifierad på svensk myndighetssida. Live-texten med 'gå ner i vikt' och 'bekämpa hunger' ligger kvar i butiken. Beslut för David: avpublicera, eller skriva med medveten risk.

### 33009 (10470944768266): RÄTTA

Live: ACTIVE, 'Vitamin Kapslar TREC ESSENSEY NIACIN FORTE 120 kapslar', 21341, 109 kr, lager 2. Energi-, trötthets- och hudpåståendena är borta, och 'effektivt' finns inte med. 500 mg niacin per kapsel står entydigt i källan ('Innehåller 500 mg niacin per kapsel!'), och ingredienslistan anger nikotinamid. Den trasiga sista ingrediensraden är rätt utelämnad. 500 mg nikotinamid ligger under EU:s (SCF/EFSA) övre gräns på 900 mg per dag för vuxna; Sverige har inga nationella maxhalter. Rättning: cirkulär inledning i meta och första meningen. 'i samband med måltid' sammanfattar källans 'med eller omedelbart efter måltid'.

- **meta** före: `Trec Essensey Niacin Forte är ett kosttillskott med 500 mg niacin per kapsel i 120 kapslar. Dosen är 1 kapsel dagligen.`
- **meta** efter: `Trec Essensey Niacin Forte innehåller 500 mg niacin (nikotinamid) per kapsel. Burken har 120 kapslar och dosen är 1 kapsel dagligen i samband med måltid.`
- **html** före: `<p>Trec Essensey Niacin Forte är ett kosttillskott i kapselform med niacin (nikotinamid).`
- **html** efter: `<p>Trec Essensey Niacin Forte innehåller niacin (nikotinamid) i kapselform.`

### 33010 (10471287783690): RÄTTA

Live: ACTIVE, 'Energishot TREC Boogieman Shot 100ml, Bubble Gum', EAN 5902114046781, 29 kr, lager 18. Energi-, fokus- och uthållighetspåståendena är borta. Typbytet från Energishot till Kosttillskott är tillåtet (källan säger 'flytande kosttillskott'). Rättning 1: dosen 15 ml tas bort ur meta och specifikation. Live anger 15 ml, men tillverkarens sida för Boogieman Shot (trecnutrition.com/brands/trec/trec-core/boogieman-shot/), vars ingredienser (inosin, AAKG, taurin, citrullinmalat, koffein) stämmer med just denna produkt, anger 'Single serving of the product ‒ 50 ml (1/2 bottle)'. Det är en motsägelse, och en tre gånger för låg dos med koffein får inte stå (R2). Användningsraden '30 minuter före träning' och alla varningar står kvar. Rättning 2: metan börjar med 'Namn är ett' (cirkulär). Samma cirkulära form i första meningen rättas. Koffeinmängd anges inte (tillverkaren: 200 mg per 50 ml), och det är rätt så länge dosen är oklar.

- **meta** före: `Trec Boogieman Shot Bubble Gum är ett flytande kosttillskott med koffein i en flaska på 100 ml. Den rekommenderade dagliga dosen är 15 ml.`
- **meta** efter: `Trec Boogieman Shot Bubble Gum innehåller bland annat beta-alanin, taurin, L-citrullinmalat och koffein. Flaskan rymmer 100 ml och skakas före användning.`
- **html** före: `<p>Trec Boogieman Shot Bubble Gum är ett flytande kosttillskott i en flaska på 100 ml. Det innehåller bland annat beta-alanin, taurin, L-citrullinmalat och vattenfritt koffein.</p><h2>Passar för</h2><ul>
<li>Dig som vill ha ett flytande kosttillskott med koffein, beta-alanin och taurin</li>
<li>Dig som vill ha ett kosttillskott med smaken Bubble Gum</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Flytande kosttillskott</li>
<li>Smak: Bubble Gum</li>
<li>Förpackning: 100 ml</li>
<li>Ingredienser: Vatten, äppeljuice från koncentrerad äppeljuice (17 %), beta-alanin, citronjuice från koncentrerad citronjuice (3 %), L-arginin alfa-ketoglutarat, taurin, L-citrullinmalat, vattenfritt koffein, inosin, smakämnen, sötningsmedel (acesulfam K, sukralos, neotam), maltodextrin, konserveringsmedel (kaliumsorbat, natriumbensoat)</li>
<li>Rekommenderad daglig dos: 15 ml</li>
`
- **html** efter: `<p>Trec Boogieman Shot Bubble Gum levereras i en flaska på 100 ml. Det flytande kosttillskottet innehåller bland annat beta-alanin, taurin, L-citrullinmalat och vattenfritt koffein.</p><h2>Passar för</h2><ul>
<li>Dig som vill ha ett flytande kosttillskott med koffein, beta-alanin och taurin</li>
<li>Dig som vill ha ett kosttillskott med smaken Bubble Gum</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Flytande kosttillskott</li>
<li>Smak: Bubble Gum</li>
<li>Förpackning: 100 ml</li>
<li>Ingredienser: Vatten, äppeljuice från koncentrerad äppeljuice (17 %), beta-alanin, citronjuice från koncentrerad citronjuice (3 %), L-arginin alfa-ketoglutarat, taurin, L-citrullinmalat, vattenfritt koffein, inosin, smakämnen, sötningsmedel (acesulfam K, sukralos, neotam), maltodextrin, konserveringsmedel (kaliumsorbat, natriumbensoat)</li>
`

### 33011 (10472269873418): RÄTTA

Live: ACTIVE, 'Aminosyrat TREC TYROSINE 60 kapslar', 13344, 109 kr, lager 9. Prestations-, fettförbrännings-, nedstämdhets- och sköldkörtelpåståendena är borta. 83 %, 3 kapslar per dag, 1 kapsel 3 gånger med cirka 300 ml vatten och läkarvarningen stämmer. Den obegripliga raden '300 mg per 300 mg' är rätt utelämnad (R2). Rättning: cirkulär inledning i meta och första meningen.

- **meta** före: `Trec Tyrosine är ett kosttillskott med L-tyrosin (83 %) i 60 kapslar. Den dagliga dosen är 3 kapslar, 1 kapsel 3 gånger dagligen.`
- **meta** efter: `Trec Tyrosine innehåller L-tyrosin, 83 % av innehållet, i 60 kapslar. Den dagliga dosen är 3 kapslar, 1 kapsel 3 gånger dagligen med vatten.`
- **html** före: `<p>Trec Tyrosine är ett kosttillskott i kapselform som innehåller L-tyrosin.`
- **html** efter: `<p>Trec Tyrosine innehåller L-tyrosin i kapselform.`

## Källor

- https://fragor.lakemedelsverket.se/org/lakemedelsverket/d/vem-far-salja-melatonin/
- https://via.tt.se/pressmeddelande/3839885/risk-att-melatonin-anvands-alltfor-lattvindigt (avsändare Läkemedelsverket)
- https://kontrollwiki.livsmedelsverket.se/artikel/82/narliggande-produkter-till-kosttillskott
- https://www.livsmedelsverket.se/livsmedel-och-innehall/kosttillskott/risker-med-kosttillskott/
- https://trecnutrition.com/brands/trec/trec-core/boogieman-shot/
- https://www.basil.com/en/p/8715019701832/basil-fixed-mounted-stem-holder-black/
- https://www.giant-bicycles.com/se/combo-touring-pedal-2022
- https://www.bike-components.de/en/Shimano/BB-UN300-Square-Taper-Bottom-Bracket-p76645/
