# Granskningsutlåtande k_47a1: aktiva produkter utan texter-klara (cyklar, elcyklar, lås, belysning, innerslang) (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan text får faktatext även i tidigare utanför-kategorier; Giant/Liv-storlek ur slutsiffra), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och formatet i `k_utlatande_43.json`.

Fem av utkasten (48001, 48002, 48003, 48005, 48007) har redan vår egna text live men saknar taggen texter-klara. Vår egen text räknas inte som källa (R3), så de jämfördes mot leverantörens original i `rapporter/shopify-original-2026-10-31/facit30-original.json`. Innerslangen (48004) har ingen originalbeskrivning; uppgifterna kontrollerades på nätet för exakt EAN. Elcyklarna bygger på egen svensk källa live.

Alla 11 utkast är ACTIVE. Standardblocket är exakt som i `b_skriv_24.json` på alla. Leveranstidsmeningen finns på exakt de sex produkterna med taggen På beställning (48002, 48008, 48009, 48012, 48013, 48014) och på ingen annan. Titlarna har 42–68 tecken och högst 2 kommatecken, SEO-titlarna 31–41 tecken och metatexterna 95–150 tecken, alla med verb. "Passar för" finns på alla. Titlar, SEO-titlar och metatexter krockar inte med andra utkast- eller skrivfiler. Butiken söktes på modellnamn och streckkod (R12a). `skrivfil_kontroll.py` ger inga formatfel men 7 spärrfel: 48002, 48007, 48008, 48009, 48012, 48013 och 48014 står i den aktiva spärren `tidigare-avvisade-2026-11-04`. De stoppas tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14, samma som i k_46). Varje rättning är ETT sammanhängande före/efter-par per fält, och före-texten finns exakt en gång i fältet (kontrollerat i python).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_47a1.json`.

## Resultat: 9 GODKÄND, 2 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 48001 | 10472250474762 | k_47a1_utkast.json | GODKÄND | – |
| 48002 | 10468773232906 | k_47a1_utkast.json | GODKÄND | – |
| 48003 | 10471057719562 | k_47a1_utkast.json | RÄTTA | titel |
| 48004 | 10472237957386 | k_47a1_utkast.json | RÄTTA | meta, html |
| 48005 | 10523488190730 | k_47a1_utkast.json | GODKÄND | – |
| 48007 | 10462752997642 | k_47a1_utkast.json | GODKÄND | – |
| 48008 | 10605383909642 | k_47a1_utkast.json | GODKÄND | – |
| 48009 | 10624088244490 | k_47a1_utkast.json | GODKÄND | – |
| 48012 | 10650209747210 | k_47a1_utkast.json | GODKÄND | – |
| 48013 | 10650209845514 | k_47a1_utkast.json | GODKÄND | – |
| 48014 | 10656692207882 | k_47a1_utkast.json | GODKÄND | – |

## Löften och påståenden

Alla titlar, SEO-titlar, metatexter och beskrivningar har sökts igenom efter hälso-, säkerhets-, skydds-, prestanda-, kvalitets-, räckvidds- och synlighetsord, även subtila (säker, trygg, stabil, kontroll, bekväm, hållbar, pålitlig, kraftfull, självförtroende, skyddar, synlighet, räckvidd, laddtid). Inget sådant finns. Låset (48001) och bakljuset (48007) beskrivs bara med mått, nycklar, ljuskälla, laddning och passform. Cyklarna anger bara komponenter och storlek; räckvidd, Aegis/larm/spårning och påståenden om hantering är utelämnade. Lastgränsen skrivs "Ej känd" på alla cyklar (v1.10, praxis från k_41). Uppgiften "30 kg bagage" på Amiti är rätt utelämnad.

## Avvisade (k_47a1_avvisade.json)

- 48010 Revolt Advanced 2 (slutsiffra 6) och 48011 Kona Ouroboros: rätt avvisade. Regeln för storlek ur slutsiffran gäller inte dem, och texten skulle bli identisk med det skrivna syskonet.
- 48006 Peltonen Skinpro 22 Med+ 181/188: dubblettskälet stämmer inte. Längderna 181/188 har egna EAN och samma pris (5 869 kr), och enligt beslutet 2026-11-05 behålls samma modell i annan storlek. Avvisningen lyfts ändå inte här, eftersom källan bara är engelsk marknadsföring och produkten inte har lager. Den kan släppas till en ny batch om David vill.

## Frågor till David

1. Sju produkter står i spärren `tidigare-avvisade-2026-11-04`. En undantagspost som bygger på ditt beslut 2026-11-08 behövs innan skrivfilen byggs.
2. 48003 TCR Advanced 2 PC: de två varianterna har samma artikelnummer och EAN men olika pris (Default Title 39 479 kr, M/L 40 089 kr). Troligen är Default Title en överbliven variant. Ska den tas bort? Texten berörs inte.
3. Fem produkter har redan rätt text live men saknar taggen texter-klara (48001, 48002, 48003, 48005, 48007). Skrivningen sätter taggen.
4. 48006 Peltonen: vill du att den skrivs i en ny batch (se ovan)?

## Skäl och rättningar per produkt

### 48001 (10472250474762, k_47a1_utkast.json): GODKÄND

Live ACTIVE, en variant 230950, EAN 887539022594, lager 21, ingen På beställning. Live-texten är vår egen; jämfört mot leverantörens original (facit30-original.json): kedjelås, 10 mm tjockt, 900 mm långt, två nycklar. 'Säkert' och tillverkarland rätt utelämnade. Inga säkerhets- eller skyddsord. Cirkulär inledning rättad till verb-först. Ingen dubblett (EAN unik i butiken).

### 48002 (10468773232906, k_47a1_utkast.json): GODKÄND

Live ACTIVE, fyra varianter XS/S/M/L beige, SKU 1032014183/84/85/87, samma pris 29 689 kr, lager 3, tagg På beställning; leveranstidsmeningen finns i standardblocket. Mot leverantörens engelska original: ALUXX-aluminium, kompositgaffel, flip-chip, Shimano Cues 20 växlar, hydrauliska, CrossCut Grip 1 700x45C, ramstorlekar och längder, fästpunkter: allt stämmer. Prestandapåståendena om hjulbas (styrning, acceleration, grepp) och 'durable', 'comfortable' utelämnade. v1.8 uppfyllt (storlekar med samma pris och färg). Lastgräns Ej känd enligt v1.10 och praxis för cyklar (k_41). Spärrlistan: produkten står i den aktiva spärren tidigare-avvisade-2026-11-04; skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt.

### 48003 (10471057719562, k_47a1_utkast.json): RÄTTA

Live ACTIVE, Default Title (39 479 kr, lager 3) och M/L black (40 089 kr, lager 5), samma SKU 1096036146 och EAN 4711291080720: samma artikel, v1.9 uppfyllt (lager > 0, priset låses inte). Original: ram/gaffel Advanced-Grade Composite, Shimano 105 24 växlar, hydrauliska, M/L 50 cm ca 177–187 cm; texten rätt begränsad till M/L (v1.5); motsägande dubbla däckrader och CFD/vindtunnel-, 'snabb och effektiv' utelämnade. R12a: samma modell och färg (Carbon) finns skriven i andra storlekar, 10471084556554 (1096036147, L) och 10472322138378 (1096036148, XL); titeln måste skilja dem (beslut 2026-11-05), därför läggs storlek M/L in i titeln som i k_skriv_41g. SEO-titeln är redan unik. Carbon är Giants färgnamn (samma som syskonen), därför behålls det.

- **titel** före: `'Landsvägscykel Giant TCR Advanced 2 PC, Carbon'`
- **titel** efter: `'Landsvägscykel Giant TCR Advanced 2 PC storlek M/L, Carbon'`

### 48004 (10472237957386, k_47a1_utkast.json): RÄTTA

Live ACTIVE, CO0181671, EAN 4019238556728, lager 42. Leverantörens original saknar beskrivning (bara titeln), så webbkoll (v1.6, beslut 2026-11-05): all4bikes.be bekräftar för exakt EAN 4019238556728 och tillverkarnummer 0181671: 47-559/62-559, Presta, 60 mm. Texten innehåller bara dessa uppgifter. Syskonen (Presta 42 mm, Autoventil, Tour) har egna titlar och EAN. Rättning: '26 tums hjul' skrivs '26-tumshjul' (R10, samma form som '29-tumshjul' i batchen).

- **meta** före: `'passar 26 tums hjul'`
- **meta** efter: `'passar 26-tumshjul'`

- **html** före: `'<p>Continental-innerslangen för 26 tums hjul har en Presta-ventil (PV) på 60 mm och dimensionen 47/62-559.</p><h2>Passar för</h2><ul>\n<li>Dig som söker en innerslang till 26 tums hjul</li>'`
- **html** efter: `'<p>Continental-innerslangen för 26-tumshjul har en Presta-ventil (PV) på 60 mm och dimensionen 47/62-559.</p><h2>Passar för</h2><ul>\n<li>Dig som söker en innerslang till 26-tumshjul</li>'`

### 48005 (10523488190730, k_47a1_utkast.json): GODKÄND

Live ACTIVE, M/blue 28171674-A och L/blue 28191676-A, samma pris 8 949 kr, lager 6, ingen På beställning. Mot leverantörens original: aluminium, M 17" 155–170, L 19" 165–180, Shimano Altus/Tourney 21 växlar, V-bromsar, 17 kg, set med stöd, kedjeskydd, stänkskärmar, pakethållare, ljus, upprätt sittställning, vardagscykling på asfalt och skogsstigar: allt stämmer. 'Bekväm åktur och god kontroll' utelämnat. v1.8 uppfyllt. Turkos står i leverantörens titel; variantens 'blue' är leverantörens grovfärg, ingen motsägelse i texten (färg anges inte där). Inte dubblett av Gazela 0 Grafit eller Turkos och Guld (andra SKU/EAN).

### 48007 (10462752997642, k_47a1_utkast.json): GODKÄND

Live ACTIVE, PLZ2207888489, EAN 5420078885883, lager 39. Mot leverantörens original: uppladdningsbart LED-bakljus via USB för Lazer Gekko, Lil' Gekko och Lizard. Märkeshistorik, 'säkerhet' utelämnade; inga synlighets- eller säkerhetslöften (belysning, v1.9 reflexregel). Titel 68 tecken, 2 kommatecken. Spärrlistan: produkten står i den aktiva spärren tidigare-avvisade-2026-11-04; skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt.

### 48008 (10605383909642, k_47a1_utkast.json): GODKÄND

Live ACTIVE, Default Title 5300001104, EAN 4711291252226, lager 0, tagg På beställning (meningen finns i standardblocket). Slutsiffra 4 = S (Giant-regeln 2026-11-08); källans S (40 cm) ca 163–174 cm. Alla tekniska uppgifter (SyncDrive Pro3X 250 W 100 Nm, EnergyPak 800 Wh, ALUXX SL 140 mm, Fox 36 Rhythm Air 150 mm, Fox Float X 185x52,5, Deore XT 11 växlar, BR-M8120, Minion DHF/Dissector) står i egen svensk källa. Räckvidd 245 km, 'mer kraft/självförtroende', 'stabil', 'full kontroll' utelämnade. Syskonet 10593839644938 säljer M/L; titel/SEO med storlek S är unika (R12a enligt beslut 2026-11-05). Spärrlistan: produkten står i den aktiva spärren tidigare-avvisade-2026-11-04; skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt.

### 48009 (10624088244490, k_47a1_utkast.json): GODKÄND

Live ACTIVE, Default Title 5060020105, EAN 4711291201200, lager 0, På beställning (meningen i standardblocket). Slutsiffra 5 = M; källans M (43,5 cm) 169–179 cm. SyncDrive Sport 2 250 W 75 Nm, EnergyPak Smart 625 Wh, Gen 4 ALUXX, XCR34 100 mm, Deore 10 växlar, Tektro HD-M280, Crosscut Gravel 2 700x57c, set med stöd/kedjeskydd/stänkskärmar/pakethållare/ljus: allt ur egen källa. Räckvidd, 'hållbarheten garanteras', 2 300 laddcykler, Aegis/larm/radar/synlighet, 'säkerheten säkerställs' utelämnade. Syskonet 10589706780938 är S; unik titel/SEO. Spärrlistan: produkten står i den aktiva spärren tidigare-avvisade-2026-11-04; skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt.

### 48012 (10650209747210, k_47a1_utkast.json): GODKÄND

Live ACTIVE, Default Title 5600003105, EAN 4711291152892, lager 0, På beställning (meningen i standardblocket). Slutsiffra 5 = M; källans M (46 cm) 168–176 cm. SyncDrive Sport 2 250 W 75 Nm, 430 Wh, ALUXX, Enviolo (källans 'Växelreglage'), Deore BR-MT420, Marathon E Plus 622x55, set med stöd, stänkskärmar, båda pakethållarna, kedjeskydd, ljus: allt ur egen källa. Räckvidd 115 km, 'stabil och bekväm', 'pålitlighet', 'säker cykelupplevelse', GPS/E-Lock utelämnade. Syskonet 10588450881802 är S; unik titel/SEO. Spärrlistan: produkten står i den aktiva spärren tidigare-avvisade-2026-11-04; skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt.

### 48013 (10650209845514, k_47a1_utkast.json): GODKÄND

Live ACTIVE, Default Title 5230005104, EAN 4711291201552, lager 0, På beställning (meningen i standardblocket). Slutsiffra 4 = S; källans S (41 cm) 158–169 cm. Motor 250 W 75 Nm, EnergyPak Smart 500 Wh, färgdisplay, Gen 3 ALUXX, XCM34 100 mm, Cues 9 växlar, HD-M275, Crosscut Gravel 2 700x57, set: allt ur egen källa. 'Bära upp till 30 kg bagage' (lastuppgift utan etikett, R4) och 'trygg', 'skyddar mot smuts', 'högkvalitativt' utelämnade; lastgräns Ej känd (v1.10). Syskonet 10598564757770 säljer XS och M; unik titel/SEO. Spärrlistan: produkten står i den aktiva spärren tidigare-avvisade-2026-11-04; skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt.

### 48014 (10656692207882, k_47a1_utkast.json): GODKÄND

Live ACTIVE, Default Title 5332003185, EAN 4711291327894, lager 0, På beställning (meningen i standardblocket). Slutsiffra 5 = M; källans M (42 cm) 169–179 cm. SyncDrive Pro 3X 250 W 100 Nm, EnergyPak Smart 800 Wh, ALUXX-grade 148x12, STL 36 Air 130 mm, Cues LinkGlide 10 växlar, Tektro Orion, Maxxis Rekon 29x2,4 (raden 'XCT 29 … 25mm' är fälgen och rätt utelämnad, som på det skrivna syskonet). 'Utmärkt hantering och stabilitet', 'självförtroende', laddtid, räckvidd utelämnade. Syskonet 10635806900490 är XL; unik titel/SEO. Spärrlistan: produkten står i den aktiva spärren tidigare-avvisade-2026-11-04; skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt.
