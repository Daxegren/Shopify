# Granskningsutlåtande k_47b9, barnstol och vindskydd för barnstol (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där. Inget har committats. Produkterna lästes live med `shopify_api.py` (ShopifyKlient); `verifiera_butik` gav BEST OF SPORTS. `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan text får faktatext även i barn- och säkerhetskategorier), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och `k_utlatande_46barn2.md` (samma produktfamiljer) samt formatet i `k_utlatande_43.json`.

Alla tre utkasten är ACTIVE med lager > 0 och saknar taggen På beställning. Tillverkarsidorna lästes (polisport.com och två urbaniki.com-sidor, alla 200). `skrivfil_kontroll.py` gav på utkasten 3 FEL (spärrade, utanfor-tills-vidare-2026-11-04) och 1 varning (cirkulär inledning 49101). Efter rättning återstår bara spärr-FEL, 0 varningar; `format_regler.py` utan anmärkning. Standardblocket är exakt det kanoniska efter rättning. Titel ≤45 tecken och ≤2 kommatecken, SEO-titel ≤32, meta 116–142 tecken med verb, "Passar för" finns i alla. Titlar, SEO-titlar och metatexter är unika mot alla utkast-/skrivfiler och mot butiken (sökning Vindskydd, Urban Iki, Polisport Joy). Varje rättning är ETT sammanhängande före/efter-par per fält, och varje före-text förekommer exakt en gång i utkastet (kontrollerat i python).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_47b9.json`.

## Resultat: 0 GODKÄND, 3 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 49101 | 10605358121226 | k_47b9_utkast.json | RÄTTA | titel, meta, html |
| 49102 | 10472284619018 | k_47b9_utkast.json | RÄTTA | titel, html |
| 49103 | 10475402330378 | k_47b9_utkast.json | RÄTTA | titel, html |

## Löften (hälsa, säkerhet, skydd, utveckling, prestanda, kvalitet)

Texterna genomsöktes efter säker, säkerhet, skydd/skyddar, trygg, stabil, robust, slitstark, hållbar, slagtålig, stark, UV, bländning, synlighet, bekväm, komfort, utveckling och liknande. Inget finns kvar. "3-punktsbälte" (källans "säkerhetsbälte") och "reflexdekal" står som ren fakta utan synlighetslöfte. Ordet "vindskydd" är produktens typord ur live-titeln; texten säger inte att det skyddar mot något.

## Mönster

- **Leveranstidsmeningen** ("Beställningsvaror kan ta upp till en vecka längre.") stod i alla tre fast ingen har taggen På beställning (R13). Skriptet ser inte taggen; samma sak bör kontrolleras i k_47b4 (10 förekomster).
- **Barnets vikt 9–22 kg (R4/v1.10):** barntransport ingår inte i v1.10:s webbrutin, men live-raden är en ren svensk rad med enhet som entydigt anger vad vikten gäller, och Polisport anger samma värde. Står en gång med "enligt tillverkaren" i texten och i meta, utan tillskrivning i specifikationen (praxis 46711).
- **R8/R9:** "URBAN IKI" i versaler och "mörkgrå" med liten bokstav i titlarna.
- **Avvisade (10):** alla avvisningar står sig, ingen lyfts ur. 49104, 49106 och 49111 har tom källa utan entydig tillverkarsida. 49105 och 49110 har titel/typ som motsäger källan (isskridsko respektive roddmaskinens SKU och EAN). 49109 och 49112 har för tunn eller motsägande källa. 49107 har oklar funktion och nästan bara säkerhetslöften. 49108 (melatonin) är uttryckligen undantagen 2026-11-06 och nämns inte 2026-11-08. 49113 är exakt dubblett av 10656690274570 (samma SKU 1521-30 och EAN, båda aktiva).

## Frågor till David

1. Spärrlistan stoppar alla tre (utanfor-tills-vidare-2026-11-04). De spärrades bara på grund av kategori och omfattas av ditt beslut 2026-11-08. Före skrivning behövs en undantagspost i `sparrlista.json` med hänvisning till beslutet (R14); det är ett tillägg.
2. Live-titeln stavar färgen "Seiboku Grey", tillverkaren "Suiboku Grey". Texten följer live-titeln. Vill du att stavningen rättas till tillverkarens?
3. Sittdynan CARGOBIKE of Sweden Flex/Delight finns aktiv två gånger med samma SKU och EAN: 10656690307338 kostar 529 kr och 10656690274570 bara 9 kr. 9 kr är troligen ett felaktigt pris, och en av annonserna bör arkiveras när lagret flyttats.

## Skäl och rättningar per produkt

### 49101 (10605358121226, k_47b9_utkast.json): RÄTTA

Live ACTIVE, en variant 4837, ingen EAN, lager 5, ingen tagg På beställning. Egen källa (maskinöversatt men rena svenska rader): barn som väger 9-22 kg, höjdjusterbara fotstöd, 3-punkts säkerhetsbälte, hjulstorlek 26''-28'', ramdiameter 28-40 mm, mörkgrå, 3,2 kg, reflexdekal. Polisports sida för Joy FF Dark Grey (ref 8406500004) bekräftar Maximum Child Weight 9-22 kg, 28-40 mm och 3-punktsbälte; den anger 26-29 tum, så texten 26-28 tum (egen källa) är inte fel. Artikelnummer 4837 kan inte knytas till tillverkarens referens; modell och färg stämmer. Inte dubblett: den skrivna Joy 10472286322954 är ljusgrå med annan SKU och EAN. Inga säkerhets-, skydds- eller utvecklingslöften (säkerhetsbälte skrivet som 3-punktsbälte, reflexdekal utan synlighetslöfte). RÄTTA: cirkulär inledning (R11, skriptvarning); 'enligt tillverkaren' två gånger för barnets vikt i html och vikten utan tillskrivning i meta (R4/R5, praxis 46711); leveranstidsmeningen står utan taggen På beställning (R13); R9 och intervall i titeln (praxis 'Barncykel Tabou Rocket FR, 14 tum, Röd-Gul').

- **titel**
  - Före: `Barnstol Polisport Joy FF 26"-28", mörkgrå`
  - Efter: `Barnstol Polisport Joy FF, 26–28 tum, Mörkgrå`
- **meta**
  - Före: `och är avsedd för barn som väger 9–22 kg.`
  - Efter: `och är enligt tillverkaren avsedd för barn som väger 9–22 kg.`
- **html**
  - Före: `<p>Barnstolen Polisport Joy FF är en rammonterad barnstol i mörkgrått för cyklar med 26–28 tums hjul. Enligt tillverkaren är den avsedd för barn som väger 9–22 kg.</p><h2>Passar för</h2><ul>
<li>Dig som söker en rammonterad barnstol till cykel med 26–28 tums hjul</li>
<li>Dig som vill ha en barnstol med höjdjusterbara fotstöd</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Barnstol</li>
<li>Märke: Polisport</li>
<li>Modell: Joy FF</li>
<li>Montering: Rammonterad, för cykelram med diameter 28–40 mm</li>
<li>Hjulstorlek på cykeln: 26–28 tum</li>
<li>Barnets vikt enligt tillverkaren: 9–22 kg</li>
<li>Fotstöd: Höjdjusterbara</li>
<li>Bälte: 3-punktsbälte</li>
<li>Reflex: Med reflexdekal</li>
<li>Färg: Mörkgrå</li>
<li>Artikelnummer: 4837</li>
</ul><h2>Leverans, retur och garanti</h2><p><strong>Frakt och leverans:</strong> Normal leveranstid är 5–8 arbetsdagar. Fraktavgiften visas i kassan. Se sidan Frakt för övriga länder. Beställningsvaror kan ta upp till en vecka längre.`
  - Efter: `<p>Polisport Joy FF monteras på cykelramen och passar cyklar med 26–28 tums hjul. Barnstolen är mörkgrå, och enligt tillverkaren är den avsedd för barn som väger 9–22 kg.</p><h2>Passar för</h2><ul>
<li>Dig som söker en rammonterad barnstol till cykel med 26–28 tums hjul</li>
<li>Dig som vill ha en barnstol med höjdjusterbara fotstöd</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Barnstol</li>
<li>Märke: Polisport</li>
<li>Modell: Joy FF</li>
<li>Montering: Rammonterad, för cykelram med diameter 28–40 mm</li>
<li>Hjulstorlek på cykeln: 26–28 tum</li>
<li>Barnets vikt: 9–22 kg</li>
<li>Fotstöd: Höjdjusterbara</li>
<li>Bälte: 3-punktsbälte</li>
<li>Reflex: Med reflexdekal</li>
<li>Färg: Mörkgrå</li>
<li>Artikelnummer: 4837</li>
</ul><h2>Leverans, retur och garanti</h2><p><strong>Frakt och leverans:</strong> Normal leveranstid är 5–8 arbetsdagar. Fraktavgiften visas i kassan. Se sidan Frakt för övriga länder.`

### 49102 (10472284619018, k_47b9_utkast.json): RÄTTA

Live ACTIVE, 218438, EAN 4511890218438, lager 3, ingen tagg På beställning. Egen källa har bara kvalitets- och skyddsord (rätt utelämnade). Alla fakta finns på https://www.urbaniki.com/en-dk/windscreen-suiboku-grey/ (200): transparent med ljus gråblå ton, Mounting method On the Urban Iki front seat, två ledpunkter och lutbar skärm, Package contents Windscreen and allen key, Mounting material included, Product weight 0,9 kg. EAN står inte på tillverkarsidan; färg och artikelkod (EAN slutar på 218438) avgör matchningen, godtas (v1.6/v1.7). Inga löften: UV-filter, 'skyddar mot regn och vind', hållbar och slagtålig utelämnade. Inte dubblett (annan färg och EAN än 49103; inget skrivet Urban Iki-vindskydd i butiken). RÄTTA: märket i versaler i titeln (R8, praxis 'Ramfäste Urban Iki'); leveranstidsmeningen utan taggen På beställning (R13); 'Ingår'-raden omformulerad.

- **titel**
  - Före: `Vindskydd för barnstol URBAN IKI Seiboku Grey`
  - Efter: `Vindskydd för barnstol Urban Iki Seiboku Grey`
- **html**
  - Före: `<li>Ingår: Vindskydd och insexnyckel, monteringsmaterial</li>
<li>Vikt: 0,9 kg</li>
<li>Artikelnummer: 218438</li>
</ul><h2>Leverans, retur och garanti</h2><p><strong>Frakt och leverans:</strong> Normal leveranstid är 5–8 arbetsdagar. Fraktavgiften visas i kassan. Se sidan Frakt för övriga länder. Beställningsvaror kan ta upp till en vecka längre.`
  - Efter: `<li>Ingår: Vindskydd, insexnyckel och monteringsmaterial</li>
<li>Vikt: 0,9 kg</li>
<li>Artikelnummer: 218438</li>
</ul><h2>Leverans, retur och garanti</h2><p><strong>Frakt och leverans:</strong> Normal leveranstid är 5–8 arbetsdagar. Fraktavgiften visas i kassan. Se sidan Frakt för övriga länder.`

### 49103 (10475402330378, k_47b9_utkast.json): RÄTTA

Live ACTIVE, 218933, EAN 4511890218933, lager 5, ingen tagg På beställning. Egen källa har bara kvalitets- och skyddsord (rätt utelämnade). Alla fakta finns på https://www.urbaniki.com/en-gb/windscreen-asahi-gold/ (200): transparent med ljust gyllene ton, Urban Ikis framsäte, två ledpunkter och lutbar skärm, vindskydd och insexnyckel, monteringsmaterial ingår, 0,9 kg. EAN-matchning via färg och artikelkod, godtas. Inga löften. Unik mot 49102. RÄTTA: märket i versaler i titeln (R8); leveranstidsmeningen utan taggen På beställning (R13); 'Ingår'-raden omformulerad.

- **titel**
  - Före: `Vindskydd för barnstol URBAN IKI Asahi Gold`
  - Efter: `Vindskydd för barnstol Urban Iki Asahi Gold`
- **html**
  - Före: `<li>Ingår: Vindskydd och insexnyckel, monteringsmaterial</li>
<li>Vikt: 0,9 kg</li>
<li>Artikelnummer: 218933</li>
</ul><h2>Leverans, retur och garanti</h2><p><strong>Frakt och leverans:</strong> Normal leveranstid är 5–8 arbetsdagar. Fraktavgiften visas i kassan. Se sidan Frakt för övriga länder. Beställningsvaror kan ta upp till en vecka längre.`
  - Efter: `<li>Ingår: Vindskydd, insexnyckel och monteringsmaterial</li>
<li>Vikt: 0,9 kg</li>
<li>Artikelnummer: 218933</li>
</ul><h2>Leverans, retur och garanti</h2><p><strong>Frakt och leverans:</strong> Normal leveranstid är 5–8 arbetsdagar. Fraktavgiften visas i kassan. Se sidan Frakt för övriga länder.`
