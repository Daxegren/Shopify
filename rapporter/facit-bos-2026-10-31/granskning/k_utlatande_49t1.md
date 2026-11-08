# Granskningsutlåtande k_49t1: tom eller tunn källa, v1.12 (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.12), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan text får faktatext även i tidigare utanför-kategorier; tom/tunn källa skrivs enligt v1.12), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och formatet i `k_utlatande_43.json`.

Alla elva utkast och båda avvisade är ACTIVE med lager > 0. Ingen har taggen På beställning, och inget utkast har leveranstidsmeningen. Standardblocket är exakt rätt på alla. Titel ≤70 tecken och ≤2 kommatecken, SEO ≤43, meta 96–126 tecken med verb, "Passar för" finns på alla. Titel, SEO och meta krockar inte med någon annan utkast- eller skrivfil i `vag2_skriv` eller med butikens titlar (sökning på Ride Tour, Pacer, Fix 18, Classic Bell, Lifetime, Solely, SM-MA, Primo, Sticker, Stödben, Cykelstöd, Ytterdäck m.fl.). Efter rättning ger `skrivfil_kontroll.py` 0 varningar och bara två FEL: spärrarna på 49009 (utanfor-tills-vidare, rullskridskor) och 49010 (tidigare-avvisade). Båda omfattas av Davids beslut 2026-11-08 men behöver undantagsrader i spärrlistan innan de skrivs. Tillverkar- eller EAN-källa söktes för varje produkt; många tillverkarsidor gav 403/404 eller saknade exakt artikel, och då bygger texten bara på titel och egen källa, vilket v1.12 tillåter. Varje rättning är ETT sammanhängande före/efter-par per fält (hela fältet där flera ord ändras), och före-texten förekommer exakt en gång i utkastet (kontrollerat i python).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_49t1.json`.

## Resultat: 3 GODKÄND, 7 RÄTTA, 1 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 49001 | 10462767284490 | k_49t1_utkast.json | RÄTTA | titel, seo_title, meta, html |
| 49002 | 10462780424458 | k_49t1_utkast.json | RÄTTA | titel, seo_title |
| 49003 | 10472232419594 | k_49t1_utkast.json | RÄTTA | titel |
| 49004 | 10472238678282 | k_49t1_utkast.json | RÄTTA | titel, seo_title, meta, html |
| 49005 | 10472239366410 | k_49t1_utkast.json | GODKÄND | – |
| 49006 | 10472239956234 | k_49t1_utkast.json | GODKÄND | – |
| 49007 | 10472240021770 | k_49t1_utkast.json | RÄTTA | html |
| 49008 | 10472240382218 | k_49t1_utkast.json | UNDERKÄND | – |
| 49009 | 10472241791242 | k_49t1_utkast.json | RÄTTA | titel, meta, html |
| 49010 | 10472241987850 | k_49t1_utkast.json | GODKÄND | – |
| 49011 | 10472245330186 | k_49t1_utkast.json | RÄTTA | titel, seo_title, meta, html |

## Löften och belägg

Alla texter genomsöktes efter hälso-, säkerhets-, skydds-, utvecklings-, prestanda- och kvalitetsord (robust, stark, pålitlig, säker, skydd, punktering, grepp, slitstark, bekväm, lätt, stabil, hög kvalitet). Inget sådant finns. Det enda tveksamma är 'som gillar fart' (49009), som står ordagrant i egen källa som målgrupp och inte är ett löfte. Lastgräns förekommer bara på stödbenet 49011 som 'Ej känd' (v1.10), eftersom återförsäljarna anger 25 eller 50 kg.

## Per produkt

### 49001 (10462767284490): RÄTTA

Live ACTIVE, CO0101157, EAN 4019238693478, 329 kr, lager 13, tom beskrivning. EAN-träff (reifen.com, galaxus) = Continental Ride Tour 42-622 (28 x 1.60), svart; titelns uppgifter stämmer. Ingen tryck-, punkterings- eller kvalitetsuppgift i texten. RÄTTA: 'Utomhusdäck' är en maskinöversättning (R2) av ytterdäck; samma modell Ride Tour 32-630 är skriven som 'Ytterdäck' (butikens live-ord), så typordet blir Ytterdäck i alla fält. SEO-titeln 'Ytterdäck Continental Ride Tour' skulle krocka med syskonet, därför med dimension (38 tecken).

- **titel**: före `Utomhusdäck Continental Ride Tour 42-622, 28 x 1,60` → efter `Ytterdäck Continental Ride Tour 42-622, 28 x 1,60`
- **seo_title**: före `Utomhusdäck Continental Ride Tour` → efter `Ytterdäck Continental Ride Tour 42-622`
- **meta**: före `Utomhusdäcket Continental Ride Tour har däckstorlek 42-622 (28 x 1,60). Artikelnummer CO0101157, EAN 4019238693478.` → efter `Ytterdäcket Continental Ride Tour har däckstorlek 42-622 (28 x 1,60). Artikelnummer CO0101157, EAN 4019238693478.`
- **html** (hela fältet i JSON-filen; skillnad): före `…<p>Utomhusdäcket Ride Tour från Continental har däckstorlek 42-622, vilket motsvarar 28 x 1,60.</p><h2>Passar för</h2><ul>
<li>Dig som söker ett utomhusdäck i storlek 42-622</li>
<li>Dig som vill ha ett däck i dimensionen 28 x 1,60</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Utomhusdäck</li>
<li>Märke:…` → efter `…<p>Ytterdäcket Ride Tour från Continental har däckstorlek 42-622, vilket motsvarar 28 x 1,60.</p><h2>Passar för</h2><ul>
<li>Dig som söker ett ytterdäck i storlek 42-622</li>
<li>Dig som vill ha ett däck i dimensionen 28 x 1,60</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Ytterdäck</li>
<li>Märke:…`

### 49002 (10462780424458): RÄTTA

Live ACTIVE, 104912, ingen EAN, lager 3. Egen källa: märke Union, vikt 0,0100 kg; allt i texten stämmer. Ingen tillverkarkälla funnen (sökning på 104912 och Union scooter sticker gav ingen träff), så texten bygger bara på titel och egen källa (v1.12). Typordet 'Scooter stickers' behålls från titeln (R7). RÄTTA: stor bokstav på beskrivande ord i titel och SEO (R9). Obs till David: priset 1 459 kr för ett klistermärke på 0,01 kg ser fel ut (ingen textfråga).

- **titel**: före `Scooter stickers Union Sticker` → efter `Scooter Stickers Union Sticker`
- **seo_title**: före `Scooter stickers Union Sticker` → efter `Scooter Stickers Union Sticker`

### 49003 (10472232419594): RÄTTA

Live ACTIVE, 580901, EAN 4718905933137, 49 kr, lager 29. Leverantörens sida velomarket.ee (SKU 580901, Giant Classic Bell svart) stämmer; Giants egen sida hittades inte. Marknadsföringsord (snygg, unik design, hög kvalitet, bra ljud) och märkestexten rätt utelämnade. RÄTTA: färgen med stor bokstav i titeln som skrivna syskon (Cykelklocka Giant Ding-A-Ling, Svart; R9).

- **titel**: före `Cykelklocka Giant Classic Bell, svart` → efter `Cykelklocka Giant Classic Bell, Svart`

### 49004 (10472238678282): RÄTTA

Live ACTIVE, S103-647869, EAN 8711252647869, 29 kr, lager 9, tom beskrivning. Märket Prophete finns bara i vendor och tagg, inte i live-titeln; EAN gav ingen träff på nätet (8711252 är ett nederländskt företagsprefix), så märket kan inte bekräftas mot tillverkare. Godtas eftersom vendor är produktens egen data, men David bör veta att märket i titeln bygger på vendorfältet. Inga storleks-, material- eller vattentäthetsuppgifter, inga löften. RÄTTA: stor bokstav på beskrivande ord i titel och SEO (R9, format_regler.py) och modellnamnet 'Lifetime Travel' enhetligt i meta och beskrivning.

- **titel**: före `Regnjacka Prophete Lifetime travel, med huva, blå` → efter `Regnjacka Prophete Lifetime Travel, med Huva, Blå`
- **seo_title**: före `Regnjacka Prophete Lifetime travel` → efter `Regnjacka Prophete Lifetime Travel`
- **meta**: före `Regnjackan Prophete Lifetime travel har huva och är blå. Artikelnummer S103-647869, EAN 8711252647869.` → efter `Regnjackan Prophete Lifetime Travel har huva och är blå. Artikelnummer S103-647869, EAN 8711252647869.`
- **html** (hela fältet i JSON-filen; skillnad): före `…Regnjackan Lifetime travel från Prophete har huva och är blå.</p><h2>Passar för</h2><ul>
<li>Dig som söker en regnjacka med huva</li>
<li>Dig som vill ha en blå regnjacka</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Regnjacka</li>
<li>Märke: Prophete</li>
<li>Modell: Lifetime travel</li>
<li>Huva:…` → efter `…Regnjackan Lifetime Travel från Prophete har huva och är blå.</p><h2>Passar för</h2><ul>
<li>Dig som söker en regnjacka med huva</li>
<li>Dig som vill ha en blå regnjacka</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Regnjacka</li>
<li>Märke: Prophete</li>
<li>Modell: Lifetime Travel</li>
<li>Huva:…`

### 49005 (10472239366410): GODKÄND

Live ACTIVE, SOLELYJR350, ingen EAN, 119 kr, lager 3, tagg Barncykel men ingen På beställning. Egen källa: passar mindre ramar ~10–12 tum (ZERO 20 och ZERO 24), 350 ml. mtbiker.shop (Beany Solely.Jr 350 ml) bekräftar ZERO 20 (10 tum) och ZERO 24 (11 tum); Beanys egen sida hittades inte. 'Enligt tillverkaren' en gång i beskrivningen och en i meta. Inga säkerhets- eller utvecklingslöften (barnprodukt, beslut 2026-11-08). Ingen dubblett.

### 49006 (10472239956234): GODKÄND

Live ACTIVE, VMISMMA90R160PS, EAN 4524667430513, 189 kr, lager 24. Befintlig kort text och SEO-titel ersätts med samma fakta (modell, 160 mm, Post/Standard). SKU (…PS) stämmer med titelns Post/Standard. Ingen tillverkarsida eller EAN-träff hittades; Shimanos återförsäljarsidor ger 403. Inget användningsområde påstås utöver titeln, rätt enligt v1.12. Annan modell än 49008 (MA90-R160 mot MA-F160), inte dubblett.

### 49007 (10472240021770): RÄTTA

Live ACTIVE, VMISMMAF180PSA, EAN 4524667108146, 179 kr, lager 13, tom beskrivning. SKU (…PSA) stämmer med Post/Standard; 'F' i Shimanos modellbeteckning SM-MA-F180 anger framadapter och 180 mm gäller bromsskivan (samma namngivning i återförsäljarlistor för SM-MA-F160P/S). Shimanos sida (dealers.bike.shimano.com) gav 403 för granskaren; utkastarens källa godtas för fram/180 mm-skiva. EAN-träff saknas på nätet men EAN är produktens egen streckkod. RÄTTA: 'Enligt Shimanos återförsäljarsida' är en källhänvisning i kundtext (R11); ersätts med 'Enligt tillverkaren' (en gång i texten).

- **html** (hela fältet i JSON-filen; skillnad): före `…st/Standard. Enligt Shimanos återförsäljarsida är den en framadapter.</p><h2>Passar för<…` → efter `…st/Standard. Enligt tillverkaren är den avsedd för framhjulet.</p><h2>Passar för<…`

### 49008 (10472240382218): UNDERKÄND

Live ACTIVE, VMKSMMAF160PZA, ingen EAN, 99 kr, lager 40. Motsägelse: titeln och live-texten säger Post/Standard (P/S, som på 49007 där SKU slutar på PSA), men SKU slutar på PZA. Shimano har en separat variant SM-MA-F160P/Z (front 160 mm, P/Z) enligt återförsäljare (rodalink.com), så artikeln kan vara P/Z och inte P/S. Adapterns utförande är det enda belagda faktumet och det går inte att avgöra entydigt (R2, v1.12 punkt 5: motsägelse). Live-textens 'montera en 160 mm bromsskiva' är dessutom tekniskt oklart (adaptern fäster bromsoket). Skrivs inte förrän utförandet är bekräftat mot Shimano eller leverantören.

### 49009 (10472241791242): RÄTTA

Live ACTIVE, FILA-PRIMOLX90-BLKBLUYLW-41, streckkod = SKU-text, 2 429 kr, lager 2. Egen källa: rullskridsko för herrar, avancerade åkare som gillar fart; 'lätta', 'bekväma', 'trevlig upplevelse' rätt utelämnade. sportisimo.com listar Fila Primo LX 90 (90 mm hjul m.m.); Filas egen sida hittades inte, och tekniska uppgifter tas inte med eftersom de inte är kontrollerade mot exakt artikel. Storlek anges inte (SKU -41 och handle -40 motsäger varandra), rätt. RÄTTA: färgerna med stor bokstav i titeln (R9, som skrivna Fila-syskon); 'är herrmodeller' blir en icke-cirkulär inledning i beskrivning och meta (skrivfil_kontroll varnade för 'Namn är en …'); metans 'finns i svart, blått och gult' antydde tre färgval fast det är en färgkombination. Spärrad (utanfor-tills-vidare, rullskridskor): behöver undantagsrad enligt beslutet 2026-11-08 innan skrivning.

- **titel**: före `Rullskridskor Fila Primo LX 90, svart, blå och gul` → efter `Rullskridskor Fila Primo LX 90, Svart, Blå och Gul`
- **meta**: före `Rullskridskorna Fila Primo LX 90 är herrmodeller för avancerade åkare och finns i svart, blått och gult.` → efter `Rullskridskorna Fila Primo LX 90 riktar sig till herrar som är avancerade åkare och har färgerna svart, blått och gult.`
- **html** (hela fältet i JSON-filen; skillnad): före `…imo LX 90 från Fila är herrmodeller för avancerade åkare som gillar fart.</p><h2…` → efter `…imo LX 90 från Fila riktar sig till herrar som är avancerade åkare och gillar fart.</p><h2…`

### 49010 (10472241987850): GODKÄND

Live ACTIVE, tre färgvarianter 74-6263-01/-07/-09, samma pris 339 kr, EAN 7318686263019/-071/-095, lager 26. Samma artikel i tre färger med samma pris (v1.8/v1.9): titeln låser rätt inte färg. Egen källa: passar både barn och vuxna; 'robust', 'tåla tuffa tag', 'pålitlig' rätt utelämnade. Velomarket.ee och galaxus (74-6263-01/-09) bekräftar Stiga Pacer i dessa färger; stiga.com gav 404. Inte dubblett: skriven 'Kälke Stiga Pacer med Bromsar' är annan artikel (74-6273) och skiljs i titel och SEO. Inga säkerhetslöften (barn). Spärrad (tidigare-avvisade): behöver undantagsrad enligt beslutet 2026-11-08.

### 49011 (10472245330186): RÄTTA

Live ACTIVE, 066329E, EAN 4021834066327, 319 kr, lager 47. Egen källa: hålavstånd 18 mm; titeln: Fix 18 I, 29 tum, svart. Webb: Hebie 0663 29 E, Fix 18 i överlängd för 29 tum, KSA 18 (fahrrad.de, bike-components.de). Lastgränsen anges olika (25 och 50 kg), så 'Maximal lastgräns: Ej känd' och meningen i texten är rätt (v1.10). 'Robust och stark' och raden '18 mm Ø 18 mm' rätt utelämnade. RÄTTA: typordet. 'Cykelstöd' finns inte i produktens egen källa; egen tagg och handle säger 'stödben (för bakmontering)', och det skrivna syskonet Fix 18 (0663E) heter 'Stödben' (R7). Färgen med stor bokstav (R9). SEO unik mot syskonet 'Stödben Hebie Fix 18, Svart'.

- **titel**: före `Cykelstöd Hebie Fix 18 I, 29 tum, svart` → efter `Stödben Hebie Fix 18 I, 29 tum, Svart`
- **seo_title**: före `Cykelstöd Hebie Fix 18 I, 29 tum` → efter `Stödben Hebie Fix 18 I, 29 tum`
- **meta**: före `Cykelstödet Hebie Fix 18 I monteras bak, har 18 mm hålavstånd och är avsett för 29 tum. Artikelnummer 066329E.` → efter `Stödbenet Hebie Fix 18 I monteras bak, har 18 mm hålavstånd och är avsett för 29 tum. Artikelnummer 066329E.`
- **html** (hela fältet i JSON-filen; skillnad): före `…<p>Cykelstödet Fix 18 I från Hebie monteras bak på cykeln och har ett hålavstånd på 18 mm. Det är avsett för 29 tum. Maximal lastgräns är inte känd.</p><h2>Passar för</h2><ul>
<li>Dig som söker ett cykelstöd för bakmontering</li>
<li>Dig som söker ett cykelstöd med 18 mm hålavstånd</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Cykelstöd</li>
<li>Märke: Heb…` → efter `…<p>Stödbenet Fix 18 I från Hebie monteras bak på cykeln och har ett hålavstånd på 18 mm. Det är avsett för 29 tum. Maximal lastgräns är inte känd.</p><h2>Passar för</h2><ul>
<li>Dig som söker ett stödben för bakmontering</li>
<li>Dig som söker ett stödben med 18 mm hålavstånd</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Stödben</li>
<li>Märke: Heb…`

## Avvisade (k_49t1_avvisade.json)

- 49901 (10462785896714, Kork Start NATURAL): avvisningen står kvar. Källan är en maskinöversatt mening och produkttypen (vad korken används till) är oklar (v1.12 punkt 5).
- 49902 (10472237170954, Cykelklocka Azimut Mini 5 mm): avvisningen står kvar. Titeln säger 5 mm och källan diameter 35 mm, en motsägelse.

## Frågor till David

1. Spärrlistan saknar undantag för 49009 och 49010 enligt beslutet 2026-11-08; de kan skrivas först när undantagsrader lagts till.
2. 49004: märket Prophete i titeln bygger bara på vendorfältet (EAN och märke kunde inte bekräftas på nätet). Godtas, eller ska titeln vara utan märke?
3. 49002: priset 1 459 kr för ett klistermärke ser fel ut.
4. 49008: utförandet (P/S eller P/Z) behöver bekräftas mot Shimano eller leverantören innan produkten skrivs.
