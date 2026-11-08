# Granskningsutlåtande k_46barn2: barnprodukter, lastcyklar och barnstolar (2026-11-08)

Granskaren har bara läst i Shopify. Inget har ändrats där och inget har committats. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient; `verifiera_butik` gav BEST OF SPORTS). `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan text får faktatext även i tidigare utanför-kategorier), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md`/`k_utlatande_42.json`/`k_utlatande_46sak*.md` och formatet i `k_utlatande_43.json`.

Alla 16 utkast och 8 avvisade är ACTIVE. Standardblocket är exakt som i `b_skriv_24.json` på alla 16. Leveranstidsmeningen finns på exakt de fem produkterna med taggen På beställning (46702, 46706, 46707, 46714, 46716) och saknas på övriga. Titel ≤70 tecken och ≤2 kommatecken, SEO ≤43 och meta 106–150 tecken gäller också efter rättning, och "Passar för" finns på alla. Titlar, SEO-titlar och metatexter är unika inom batchen och mot övriga utkast- och skrivfiler. Butiken söktes på modellnamnen (Cruiser, Fiido, Rocket, Bookman, Amladcykler, Urban Iki, Prinsessa, Musse, X-One, Tekno, Cangoo, Joy, Cykelstöd). Ingen exakt dubblett finns (R12a). Tre SEO-titlar krockar nästan med en skriven produkt eller riskerar att krocka med oskrivna färgsyskon (46715, 46705, 46718). De rättas. Varje rättning är ETT sammanhängande före/efter-par per fält, och före-texten förekommer exakt en gång i fältet (kontrollerat i python). `skrivfil_kontroll.py` ger 0 formatfel både på utkasten och på de rättade texterna, men 4 FEL för spärrade produkter (se nedan).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_46barn2.json`.

## Resultat: 3 GODKÄND, 13 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 46702 | 10472253718794 | k_46barn2_utkast.json | RÄTTA | html |
| 46703 | 10472255848714 | k_46barn2_utkast.json | RÄTTA | titel, seo_title, meta, html |
| 46705 | 10472281800970 | k_46barn2_utkast.json | RÄTTA | titel, seo_title, meta, html |
| 46706 | 10472282784010 | k_46barn2_utkast.json | RÄTTA | meta, html |
| 46707 | 10472282980618 | k_46barn2_utkast.json | GODKÄND | – |
| 46708 | 10472284487946 | k_46barn2_utkast.json | RÄTTA | titel, html |
| 46711 | 10472286322954 | k_46barn2_utkast.json | RÄTTA | titel, meta, html |
| 46712 | 10472286552330 | k_46barn2_utkast.json | RÄTTA | titel, seo_title, meta |
| 46713 | 10472289468682 | k_46barn2_utkast.json | RÄTTA | titel, seo_title |
| 46714 | 10472291205386 | k_46barn2_utkast.json | GODKÄND | – |
| 46716 | 10472295072010 | k_46barn2_utkast.json | RÄTTA | meta |
| 46715 | 10472291238154 | k_46barn2_utkast.json | RÄTTA | titel, seo_title |
| 46718 | 10472303296778 | k_46barn2_utkast.json | RÄTTA | seo_title, meta |
| 46719 | 10472308211978 | k_46barn2_utkast.json | GODKÄND | – |
| 46722 | 10475361206538 | k_46barn2_utkast.json | RÄTTA | titel, seo_title |
| 46723 | 10475369562378 | k_46barn2_utkast.json | RÄTTA | titel, seo_title, meta |

## Löften (hälsa, säkerhet, skydd, utveckling, prestanda, kvalitet)

Alla texter genomsöktes efter både tydliga och subtila löften: säker, säkerhet, skydd, skyddar, trygg, stabil, robust, slitstark, hållbar, pålitlig, bekväm, komfort, ergonomi, utveckling, lära sig cykla, synlighet, synas, kraftfull, smidig, idealisk och perfekt. Inget sådant finns i någon titel, SEO-titel, meta eller beskrivning. Kvar finns bara rena fakta: bälte och 3-punktsbälte ("säkerhets-" struket), reflex på baksidan (utan synlighetslöfte), vaddering, kedjekåpa ("skyddande" struket), "lätt att ta bort" (källans "lätt borttagbar" om funktionen) och räckvidd en gång enligt tillverkaren (praxis för elcyklar). EN14344, UL2271, tippskydd och elektroniskt bromssystem är utelämnade.

## Mönster

- **Lastgräns (R4/v1.10):** de svenska raderna med etikett och enhet (Lastkapacitet 150/200/15 kg, Maximal lastkapacitet 50 kg, Kapacitet 22 kg) står med "enligt tillverkaren". I 46706, 46708 och 46711 stod "enligt tillverkaren" två gånger för samma värde (text och specifikation). I 46706 och 46711 stod lasten i meta utan tillskrivning. Båda felen rättas enligt praxis 42401. Cangoo och cykelstödet saknar lastgräns i källan. Ingen träff på nätet, så de får "Ej känd".
- **Exakt artikel:** Urban Iki 212665 bekräftades som framsits i färgen Bincho Black. "Modell: Bincho Black" var alltså fel och rättas till Färg. Polisport Joy-EAN:et hittades inte, men modellens 22 kg stämmer med Polisports sida för Joy FF. Övriga uppgifter står i egen live-källa.
- **R9:** färg- och beskrivningsord i titel och SEO-titel saknade stor bokstav i nio produkter (praxis: skrivna "Handskar Liv Supreme SF, Svart" och "Barncykel Tabou Rocket FR, 14 tum, Röd-Gul"). El-lastcykel behåller liten bokstav efter bindestrecket (v1.5).
- **R11:** cirkulära inledningar i 46703 (html och meta) och 46718 (meta) skrivs om.
- **Varianter (v1.9):** 46719 har varianter med olika pris men är samma artikel i olika storlek och har lager. Titel och text låser varken storlek, färg eller pris.
- **Avvisade (8):** alla avvisningar står sig. 46721 är redan skriven i vår mall och saknar bara taggen. 46717 har tom källa. 46704 har en titel som motsäger källan (mountainbike för 160–175 cm). 46701, 46709, 46720 och 46724 har för tunn källa med bara kvalitets- och skyddsord, och 46710 har oklar produkttyp. Ingen lyfts ur.

## Frågor till David

1. Spärrlistan stoppar 46708, 46711, 46712 (utanfor-tills-vidare, barnstolar) och 46719 (rullskridskor). De spärrades bara på grund av kategori och omfattas av ditt beslut 2026-11-08. Före skrivning behövs en undantagspost i `sparrlista.json` med hänvisning till beslutet (R14). Det är ett tillägg, inte en ändring.
2. Fila X-One 46719 har en överbliven Default Title-variant med samma SKU som M/black men 1889 kr i stället för 1639 kr. Den bör troligen tas bort (texten berörs inte).
3. Polisport Joy 46711: vill du att "Kapacitet upp till 22 kg" står kvar? Polisport anger 22 kg som barnets maxvikt för Joy FF, men butikens EAN kunde inte kopplas till en sida.
4. Butiksprofilen har kvar "barnstolar och säten" under fortfarande utanför (frislappta_2026_11_05), trots beslutet 2026-11-08. Profilen behöver uppdateras med ditt beslut.

## Skäl och rättningar per produkt

### 46702 (10472253718794, k_46barn2_utkast.json): RÄTTA

Live ACTIVE, en variant CB07U2400100MEN1, EAN 8719636019523, lager 0, tagg På beställning; leveranstidsmeningen finns. Uppgifterna (aluminium, 250 W 95 Nm mittmotor, Enviolo Stepless, hydrauliska skivbromsar, 26 tum, räckvidd upp till 60 km en gång enligt tillverkaren, EPP och trä, 4 magnetiska trepunktsbälten, Lådcykelvikt 50 kg) står i egen källa; batteriraden (700 Wh mot 48 V 2 Ah) och skräpdelen '50 kg: 50 lb' rätt utelämnade (R2). Lastgräns saknas i källan och hittades inte på nätet (sökning på modell/artikelnummer gav ingen träff): 'Ej känd' (v1.10). Robust/säkerhet/stark/bekväm utelämnade. RÄTTA: 'lådan fram' står inte i källan (R1), byts mot källans 'låda i EPP och trä'.

- **html** före: `<li>Dig som söker en el-lastcykel med lådan fram</li>`
  efter: `<li>Dig som söker en el-lastcykel med låda i EPP och trä</li>`

### 46703 (10472255848714, k_46barn2_utkast.json): RÄTTA

Live ACTIVE, 59092, EAN 5902308590922, lager 8. Storlek S, ålder 4–6, omkrets 15 cm, inre vaddering och justerbara manschetter ur egen källa; skyddslöftet 'skydda händerna från stötar och repor', 'bekväm' och trasiga raden '5 - 15 cm - 15 cm' rätt utelämnade. RÄTTA: cirkulär inledning i html och meta ('Prinsesshandskarna är handskar', 'Handskar Prinsessa är barnhandskar', R11); färgordet i titel och SEO får stor bokstav (R9, praxis 'Handskar Liv Supreme SF, Svart').

- **titel** före: `Handskar Prinsessa, rosa`
  efter: `Handskar Prinsessa, Rosa`
- **seo_title** före: `Handskar Prinsessa, rosa`
  efter: `Handskar Prinsessa, Rosa`
- **meta** före: `Handskar Prinsessa är barnhandskar i storlek S för åldern 4–6 år, med inre vaddering och justerbara manschetter. Omkrets 15 cm.`
  efter: `Handskar Prinsessa i storlek S är gjorda för barn i åldern 4–6 år och har inre vaddering och justerbara manschetter. Omkrets 15 cm.`
- **html** före: `<p>Prinsesshandskarna är handskar för barn i storlek S, avsedda för åldern 4–6 år.`
  efter: `<p>Handskarna Prinsessa är gjorda för barn i storlek S och avsedda för åldern 4–6 år.`

### 46705 (10472281800970, k_46barn2_utkast.json): RÄTTA

Live ACTIVE, 74-6250-09, EAN 7318686250095, lager 6. Bälte, vadderad rygg och sits, reflex på baksidan och 'Tillverkad i Sverige' (ordagrant, ursprung enligt tillverkaren, R5) ur egen källa; 'säkerhetsbälte' skrivet som 'bälte', 'så säkra som möjligt' och skyddsutrustningsråd rätt utelämnade. RÄTTA: R9 i titeln (Grön); SEO får färgen eftersom syskonen Cruiser rosa (74-6250-07), black (74-6250-01) och Cruiser Eco är aktiva och oskrivna (R12, praxis 46001); 'av kälken' upprepas i meta; 'enligt tillverkaren' stod två gånger för samma ursprungspåstående (text och specifikation, R5, praxis 42401).

- **titel** före: `Babykälke Stiga Cruiser, grön`
  efter: `Babykälke Stiga Cruiser, Grön`
- **seo_title** före: `Babykälke Stiga Cruiser`
  efter: `Babykälke Stiga Cruiser Grön`
- **meta** före: `Kälken har dessutom en reflex på baksidan av kälken.`
  efter: `Kälken har dessutom en reflex på baksidan.`
- **html** före: `<li>Tillverkningsland enligt tillverkaren: Sverige</li>`
  efter: `<li>Tillverkningsland: Sverige</li>`

### 46706 (10472282784010, k_46barn2_utkast.json): RÄTTA

Live ACTIVE, AM_CLASSICCARGO, lager 1, tagg På beställning; leveranstidsmeningen finns. Typordet Lastcykel står i egen källa (R7). Alla tekniska rader ur egen källa; 'Lastkapacitet: 150 kg' är svensk rad med etikett och enhet (R4). 'Slitstarkt stål och aluminium' (motsäger ramraden), 'hög säkerhetsnivå', 'slitstarka fotbromsar' rätt utelämnade. RÄTTA: 'enligt tillverkaren' stod två gånger för lastkapaciteten (text och specifikation, R5); i meta stod lastkapaciteten utan 'enligt tillverkaren' (R4).

- **meta** före: `Lastkapacitet 150 kg.`
  efter: `Lastkapacitet 150 kg enligt tillverkaren.`
- **html** före: `<li>Lastkapacitet enligt tillverkaren: 150 kg</li>`
  efter: `<li>Lastkapacitet: 150 kg</li>`

### 46707 (10472282980618, k_46barn2_utkast.json): GODKÄND

Live ACTIVE, AM_ULTIMATEHARMONY, lager 1, tagg På beställning; leveranstidsmeningen finns. Alla uppgifter står i egen källa (36 V x 14 Ah = 504 Wh stämmer). Räckvidd och lastkapacitet 150 kg (svensk rad med etikett och enhet) under ett 'enligt tillverkaren'. Tippskydd och elektroniskt bromssystem rätt utelämnade. Inga löften. El-lastcykel med liten bokstav efter bindestreck (v1.5). Ingen dubblett (Deluxe, Ultimate Curve är andra modeller).


### 46708 (10472284487946, k_46barn2_utkast.json): RÄTTA

Live ACTIVE, 212665, EAN 4511890212665, lager 3. EAN motsvarar Urban Iki framsits i färgen Bincho Black (https://www.cyclesuk.com/product/132342/urban-iki-front-seat-take/, https://www.urbaniki.com/en-dk/front-seat-in-bincho-black-bincho-black/): ramfäste framtill, 9 månader–3 år och 15 kg stämmer; källans 'bakre säten' är generell sortimentstext. EN14344, 'höga säkerhetsstandarder' och 'ultimat komfort' rätt utelämnade. RÄTTA: Bincho Black är färgnamnet, inte modellen (specifikationsraden); 'enligt tillverkaren' stod två gånger för lastkapaciteten (R5); R9 i titeln. Spärrlistan (utanfor-tills-vidare) stoppar produkten i skriptet tills undantag läggs in enligt beslutet 2026-11-08 (R14).

- **titel** före: `Barnstol Urban Iki Bincho Black, med ramfäste framtill`
  efter: `Barnstol Urban Iki Bincho Black, med Ramfäste Framtill`
- **html** före: `<li>Modell: Bincho Black</li>
<li>Montering: Ramfäste framtill</li>
<li>Rammonteringsdiameter: 22–28 mm</li>
<li>Ålder: 9 månader till 3 år</li>
<li>Lastkapacitet enligt tillverkaren: Upp till 15 kg</li>`
  efter: `<li>Färg: Bincho Black</li>
<li>Montering: Ramfäste framtill</li>
<li>Rammonteringsdiameter: 22–28 mm</li>
<li>Ålder: 9 månader till 3 år</li>
<li>Lastkapacitet: Upp till 15 kg</li>`

### 46711 (10472286322954, k_46barn2_utkast.json): RÄTTA

Live ACTIVE, 4838, EAN 5604415085406, lager 4. Egen källa: lätt borttagbar, rammonterad, ljusgrå, 'Kapacitet upp till 22 kg'. EAN hittades inte på nätet, men Polisport anger för Joy FF (rammonterad) högst 22 kg för barnet (https://www.polisport.com/en/move/child-bike-seats/rear-frame-mounting-system/joy-ff-frame-mounted-bicycle-child-seat_p4728.html); värdet återges ordagrant utan tolkning, vilket godtas. Tunn men räcker (två fakta utöver titeln). RÄTTA: 'enligt tillverkaren' två gånger för kapaciteten (R5); meta hade kapaciteten utan 'enligt tillverkaren' (R4) och utfyllnaden 'Artikelnummer 4838'; R9 i titeln. Spärrlistan stoppar produkten tills undantag läggs in (R14).

- **titel** före: `Barnstol Polisport Joy med ramfäste, ljusgrå`
  efter: `Barnstol Polisport Joy med Ramfäste, Ljusgrå`
- **meta** före: `Kapacitet upp till 22 kg. Artikelnummer 4838.`
  efter: `Kapaciteten är enligt tillverkaren upp till 22 kg.`
- **html** före: `<li>Kapacitet enligt tillverkaren: Upp till 22 kg</li>`
  efter: `<li>Kapacitet: Upp till 22 kg</li>`

### 46712 (10472286552330, k_46barn2_utkast.json): RÄTTA

Live ACTIVE, S123-0024, EAN 4009208000245, lager 1. Barn 9–15 kg, runda och ovala ramrör, 3-punktsbälte, justerbara fotstöd och tvättbart överdrag ur egen källa; viktintervallet står även i live-titeln och är produktens målgrupp. Märke utelämnat (vendor Polisport, men EAN-prefixet pekar inte på Polisport): rätt. RÄTTA: metans första mening saknade huvudverb; R9 i titel och SEO. Spärrlistan stoppar produkten tills undantag läggs in (R14).

- **titel** före: `Barnstol 9–15 kg, svart-grå, med ramfäste fram`
  efter: `Barnstol 9–15 kg, Svart-Grå, med Ramfäste Fram`
- **seo_title** före: `Barnstol 9–15 kg, svart-grå`
  efter: `Barnstol 9–15 kg, Svart-Grå`
- **meta** före: `Barnstol för barn som väger 9–15 kg, med ramfäste fram, justerbara fotstöd och tvättbart överdrag.`
  efter: `Barnstolen är avsedd för barn som väger 9–15 kg och har ramfäste fram, justerbara fotstöd och tvättbart överdrag.`

### 46713 (10472289468682, k_46barn2_utkast.json): RÄTTA

Live ACTIVE, 9016, EAN 5902308590168, lager 12. Cykelhandskar, bild av Disneys tecknade figurer, kardborreband, vadderad handflata och handflatans bredd 7–8 cm ur egen källa; 'slitstarkt material' och 'perfekt passform' rätt utelämnade. RÄTTA: R9 i titel och SEO (Blå).

- **titel** före: `Handskar Musse, blå`
  efter: `Handskar Musse, Blå`
- **seo_title** före: `Handskar Musse, blå`
  efter: `Handskar Musse, Blå`

### 46714 (10472291205386, k_46barn2_utkast.json): GODKÄND

Live ACTIVE, FIIDOT2, lager 1, tagg På beställning; leveranstidsmeningen finns. Alla tekniska rader i egen svensk källa; cyklistlängd 155–200 cm är den entydiga delen av den trasiga ramraden (R2). Lastkapacitet 200 kg (svensk rad med etikett och enhet) och räckvidd under ett 'enligt tillverkaren'. 'Kraftfull', 'tar hand om dig' och barntransport rätt utelämnade. Annan färg än 46716, inte dubblett. El-lastcykel enligt v1.5.


### 46716 (10472295072010, k_46barn2_utkast.json): RÄTTA

Live ACTIVE, FIIDOT2-GREY, lager 1, tagg På beställning; leveranstidsmeningen finns. Samma tekniska data som 46714 ur egen källa (fjädringsväg här, slaglängd i den gröna, båda ordagrant). Annan färg, inte dubblett. RÄTTA: '250 W motor' ska skrivas '250 W-motor' i meta.

- **meta** före: `drivs av en 250 W motor`
  efter: `drivs av en 250 W-motor`

### 46715 (10472291238154, k_46barn2_utkast.json): RÄTTA

Live ACTIVE, TAB25-6680, EAN 5904257310859, lager 7. 16 tum, stålram, kedjekåpa och 4–6 år beroende på längd ur egen källa; robust, pålitlig, skyddande och 'ökad säkerhet' rätt utelämnade. RÄTTA (R12): den skrivna 10486810575114 (Rocket FR 16 tum Blå-Turkos) har SEO 'Barncykel Tabou Rocket FR, 16 tum', som bara skiljer sig med ett kommatecken; färgen läggs till. R9 i titeln (Röd-Gul, som skrivna syskon).

- **titel** före: `Barncykel Tabou Rocket FR, 16 tum, röd-gul`
  efter: `Barncykel Tabou Rocket FR, 16 tum, Röd-Gul`
- **seo_title** före: `Barncykel Tabou Rocket FR 16 tum`
  efter: `Barncykel Tabou Rocket FR 16 tum Röd-Gul`

### 46718 (10472303296778, k_46barn2_utkast.json): RÄTTA

Live ACTIVE, 484B, EAN 7350051864841, lager 2. Enkla geometriska former, fästs med klämma eller snodd på kläder, ryggsäckar och barnvagnar ur egen källa; synlighets- och säkerhetslöften rätt utelämnade (v1.9). RÄTTA: meta var cirkulär ('… Reflector … är en reflex', R11); SEO får färgen eftersom rosa syskonet 485B (10665226895626) är aktivt och oskrivet (R12).

- **seo_title** före: `Reflex Bookman Soft Adventure`
  efter: `Reflex Bookman Soft Adventure Fox Red`
- **meta** före: `Bookman Soft Adventure Reflector, Fox Red, är en reflex i enkla geometriska former som fästs med klämma eller snodd.`
  efter: `Reflexen Bookman Soft Adventure Reflector i färgen Fox Red har enkla geometriska former och fästs med klämma eller snodd.`

### 46719 (10472308211978, k_46barn2_utkast.json): GODKÄND

Live ACTIVE, lager 5. Varianter Default Title (010623130-M35, 1889 kr), M/black (samma SKU, 1639 kr) och XL/black (1639 kr): samma artikel i olika storlek med lager, v1.9 uppfylld; titel och text låser varken storlek, färg eller pris. Alla uppgifter ur egen källa; storlekstabellen S–XL rätt utelämnad, robust/säker/stabil/ergonomi rätt utelämnade. Spärrlistan (rullskridskor) stoppar produkten tills undantag läggs in (R14). Till David: Default Title-varianten har samma SKU som M/black men 250 kr högre pris.


### 46722 (10475361206538, k_46barn2_utkast.json): RÄTTA

Live ACTIVE, 1011, EAN 2099900001208 (butiksintern kod), lager 176. Centrerat, aluminium, 16–20 tum ur egen källa. Lastgräns saknas; EAN är internt och ingen tillverkarsida hittas, så 'Ej känd' enligt v1.10. Märke utelämnat (taggar Azimut/Azimuth). RÄTTA: R9 i titel och SEO ('Cyklar').

- **titel** före: `Cykelstöd för 16–20 tums cyklar`
  efter: `Cykelstöd för 16–20 tums Cyklar`
- **seo_title** före: `Cykelstöd för 16–20 tums cyklar`
  efter: `Cykelstöd för 16–20 tums Cyklar`

### 46723 (10475369562378, k_46barn2_utkast.json): RÄTTA

Live ACTIVE, 13173809, lager 1. Alla tekniska rader ordagrant ur egen källa; 'Maximal lastkapacitet: 50 kg' är svensk rad med etikett och enhet, en gång enligt tillverkaren (R4). UL2271, 'mjuk acceleration, lämplig för barn', 'slitstarkt' och Razors märkestext rätt utelämnade. RÄTTA: R9 i titel och SEO (Sparkcykel, praxis 'Liggande Motionscykel'); '80 W motor' ska skrivas '80 W-motor' i meta.

- **titel** före: `Elektrisk sparkcykel Razor Electric Tekno Scooter`
  efter: `Elektrisk Sparkcykel Razor Electric Tekno Scooter`
- **seo_title** före: `Elektrisk sparkcykel Razor Tekno`
  efter: `Elektrisk Sparkcykel Razor Tekno`
- **meta** före: `drivs av en 80 W motor`
  efter: `drivs av en 80 W-motor`
