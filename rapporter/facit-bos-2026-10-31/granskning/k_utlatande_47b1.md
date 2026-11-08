# Granskningsutlåtande k_47b1: tidigare avvisade produkter (barn, Disney/Seven Polska, cykelstöd, pakethållare) (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsning med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan texter-klara får faktatext även i tidigare utanför-kategorier; produkter med motsägande eller tom källa och exakta dubbletter skrivs inte), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md`, `k_utlatande_46barn3.md` och `k_utlatande_47a2.md`, formatet i `k_utlatande_43.json`. Webbkällorna (centrumrowerowe.pl, fahrrad.de, tormino.com) lästes av granskaren; EAN stämmer på alla tre.

Alla fyra utkast och alla tio avvisade är ACTIVE. Ingen av de fyra utkastprodukterna har taggen På beställning och inget utkast har leveranstidsmeningen. Standardblocket är exakt rätt. Titel ≤70 tecken och ≤2 kommatecken, SEO ≤43, meta 92–124 tecken efter rättning med verb, "Passar för" finns. Titel, SEO och meta krockar inte med någon annan fil i `vag2_skriv` eller med butikens titlar (sökning Stitch, Comoa, SP-Quick, Cykelstöd, Knä, Academy, Seven Polska och streckkoderna). Inga hälso-, säkerhets-, skydds-, utvecklings-, prestanda- eller kvalitetslöften finns i de godkända och rättade texterna. Spärren: alla fyra har undantagsrader i `undantag_2026-11-05.csv`; `skrivfil_kontroll.py` gav 0 fel och 0 varningar på utkasten och på de rättade texterna. Varje rättning är ETT sammanhängande före/efter-par per fält, och före-texten förekommer exakt en gång i utkastet (kontrollerat i python).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_47b1.json`.

## Resultat: 1 GODKÄND, 2 RÄTTA, 1 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 48301 | 10530130854154 | k_47b1_utkast.json | UNDERKÄND | – |
| 48302 | 10530130886922 | k_47b1_utkast.json | RÄTTA | titel, html |
| 48303 | 10472250835210 | k_47b1_utkast.json | GODKÄND | – |
| 48304 | 10472293433610 | k_47b1_utkast.json | RÄTTA | meta, html |

## Bedömning per produkt

### 48301 (10530130854154): UNDERKÄND

Live ACTIVE, en variant 59232, EAN 5902308592322, 99 kr, lager 15, ingen På beställning-tagg. Live-beskrivningen är helt tom; alla fakta kommer från en enda återförsäljarsida (tormino.com, exakt EAN), ingen tillverkarsida. Beslutet 2026-11-08 säger uttryckligen att produkter med tom källa inte skrivs och att källkravet är egen källa eller entydig tillverkarsida; praxis i k_46sak2/k_46sak4/k_46sak5 (tom källa avvisas). Därtill motsägelser i återförsäljarens egna uppgifter: material både plast och PVC, färgen pink mot live-titelns mörkrosa (R2). Fakta på sidan (20 x 13 x 13 cm, styrmontering med remmar, Minnie Mouse) stämmer i sig, men räcker inte mot beslutet. Lämnas som tidigare avvisning.


### 48302 (10530130886922): RÄTTA

Live ACTIVE, en variant 59295, EAN 5902308592957, 209 kr, lager 4, ingen På beställning-tagg. Egen källa är en mening (skydd för knän och armbågar); övriga fakta från centrumrowerowe.pl med exakt EAN och producentkod 59295 (Seven 1 Sp. z o.o.), läst av granskaren: Marka DISNEY, niebieski, one size, knä 13,5x11 cm, armbåge 13x9,5 cm, regulowane rzepy och elastyczne paski. Allt i texten stämmer. Skyddslöften på sidan (bezpieczeństwo, chroni przed urazami, komfort, mjuk vaddering) rätt utelämnade; inga hälso-, säkerhets-, skydds- eller utvecklingslöften i texten. Typordet Knä- och armbågsskydd följer egen källa och skrivna syskon Cars/Frozen 2 (R7). 'Fuses' rätt struket (maskinöversättning, praxis k_46barn3). Inte dubblett (egen EAN; Barnhandskar/Frontkorg/Cykelklocka Stitch är andra artiklar). RÄTTA: färgen i titeln med stor bokstav som syskonen (R9, praxis 46809/46810); 'regleringsbara kardborrband' är en ordagrann kalk av polskans regulowane rzepy och blir 'justerbara kardborreband' i löptext och specifikation. Spärr: undantag omprovning-barn finns, skrivfil_kontroll 0 fel.

- **titel** före: `'Knä- och armbågsskydd Disney Stitch, blå'`
  efter: `'Knä- och armbågsskydd Disney Stitch, Blå'`
- **html** före: `'Skydden har regleringsbara kardborrband och elastiska band.</p><h2>Passar för</h2><ul>\n<li>Dig som söker knä- och armbågsskydd med Stitch-motiv</li>\n<li>Dig som vill ha ett set i en storlek</li>\n</ul><h2>Specifikationer</h2><ul>\n<li>Typ: Knä- och armbågsskydd</li>\n<li>Märke: Disney</li>\n<li>Motiv: Stitch</li>\n<li>Färg: Blå</li>\n<li>Storlek: One size</li>\n<li>Mått knäskydd: 13,5 x 11 cm</li>\n<li>Mått armbågsskydd: 13 x 9,5 cm</li>\n<li>Fästen: Regleringsbara kardborrband och elastiska band</li>'`
  efter: `'Skydden har justerbara kardborreband och elastiska band.</p><h2>Passar för</h2><ul>\n<li>Dig som söker knä- och armbågsskydd med Stitch-motiv</li>\n<li>Dig som vill ha ett set i en storlek</li>\n</ul><h2>Specifikationer</h2><ul>\n<li>Typ: Knä- och armbågsskydd</li>\n<li>Märke: Disney</li>\n<li>Motiv: Stitch</li>\n<li>Färg: Blå</li>\n<li>Storlek: One size</li>\n<li>Mått knäskydd: 13,5 x 11 cm</li>\n<li>Mått armbågsskydd: 13 x 9,5 cm</li>\n<li>Fästen: Justerbara kardborreband och elastiska band</li>'`

### 48303 (10472250835210): GODKÄND

Live ACTIVE, en variant 1672, EAN 4250969216721, 299 kr, lager 2, ingen På beställning-tagg. Egen källa: stativ för Academy-cyklar, avstånd 40 mm; titeln KSA 40. fahrrad.de (exakt EAN, läst av granskaren): ACADEMY COMOA Hinterbauständer L, KSA 40-Aufnahme, montering på insidan av strebe, skruvar ingår, Einbein-/Seitenständer. Hjulstorleken rätt utelämnad (egen källa 24-27,5 tum, fahrrad.de 24-26 tum, R2); 'robust' rätt utelämnat. Bärande del utan funnen lastgräns: raden 'Maximal lastgräns: Ej känd' och meningen i löptext finns (v1.10), som syskonet Stödben Academy KSA 40, 20 tum. Typordet Cykelstöd är godkänt i profilen; syskonets Stödben bygger på ett annat live-ord, så R7 kräver inte samma ord. Inga lastlöften eller stabilitetsord. Unikt mot butikens Cykelstöd- och Academy-titlar. Spärr: undantag omprovning-pass4 finns.


### 48304 (10472293433610): RÄTTA

Live ACTIVE, en variant 440170 (ingen EAN), 219 kr, lager 6, ingen På beställning-tagg. Live-texten är vår egen; leverantörens original (facit30-original.json): 'Lastkapacitet: 9 kg. Aluminium. med sadelstolpsfäste.' Ordagrann svensk lastgräns med etikett och enhet, så den får stå (R4/v1.10). Lastgränsen stod tre gånger (meta, löptext och specifikationsraden, där utan 'enligt tillverkaren'). R4 säger en gång; praxis (48102, 48103, k_05a) är en specifikationsrad 'Lastkapacitet enligt tillverkaren: …' och ingen lastuppgift i meta. RÄTTA: lastgränsen ur meta och löptext, specifikationsraden med 'enligt tillverkaren'; Typ, Märke och Modell läggs till ur titeln som i batchens övriga texter. Titel utan ', 9 kg' och SEO-titel godtas; ingen annan SP-Quick i butiken (ingen dubblett). Spärr: undantag distinkt-artikel-ej-dubblett finns.

- **meta** före: `'Pakethållaren M-Wave SP-Quick i aluminium monteras på sadelstolpen med ett sadelstolpsfäste. Lastkapacitet 9 kg enligt tillverkaren.'`
  efter: `'Pakethållaren M-Wave SP-Quick i aluminium monteras på sadelstolpen med ett sadelstolpsfäste.'`
- **html** före: `' Lastkapacitet 9 kg enligt tillverkaren.</p><h2>Passar för</h2><ul>\n<li>Dig som vill ha en pakethållare som fästs på sadelstolpen</li>\n<li>Dig som söker en pakethållare i aluminium</li>\n</ul><h2>Specifikationer</h2><ul>\n<li>Fäste: Sadelstolpsfäste</li>\n<li>Lastkapacitet: 9 kg</li>'`
  efter: `'</p><h2>Passar för</h2><ul>\n<li>Dig som vill ha en pakethållare som fästs på sadelstolpen</li>\n<li>Dig som söker en pakethållare i aluminium</li>\n</ul><h2>Specifikationer</h2><ul>\n<li>Typ: Pakethållare</li>\n<li>Märke: M-Wave</li>\n<li>Modell: SP-Quick</li>\n<li>Fäste: Sadelstolpsfäste</li>\n<li>Lastkapacitet enligt tillverkaren: 9 kg</li>'`

## Avvisade (k_47b1_avvisade.json)

Alla tio avvisningar kontrollerades live och står sig; ingen lyfts ur. 48311 frontkorg ADO (källan säger hjälm, lager 0), 48312 Squire Folda Mini (vredeslås/hjullås/vikbart lås och 69 cm mot 650 mm), 48313 och 48314 (monteringstjänster, inga produkter), 48315 Kindad Frozen 2 och 48320 Uniplast skyddsplåt (tom källa), 48316 Gloves Mickey (färg och storlek motsäger sig), 48317/48318 Kapellställning Long Lite (exakta dubbletter med samma SKU 1521-28 och EAN, lager 0) och 48319 Stiga Snow Kick (live-titeln Snow boots, källan "snödörr"; produkten är sannolikt en snösparkcykel och källan har en svensk lastrad, men typordet saknar stöd i egen källa och i profilen, så avvisningen är inte uppenbart fel).

## Frågor till David

1. 48301 Framkorg Minnie: fakta finns bara hos en återförsäljare (tom egen källa). Beslutet 2026-11-08 säger att tom källa inte skrivs. Vill du göra undantag när en återförsäljare med exakt EAN har tydliga fakta? Samma fråga gäller 48319 Stiga Snow Kick om typordet Snösparkcykel godkänns.
2. Typordet "Knä- och armbågsskydd" används nu i tre Seven Polska-produkter men står inte i profilens godkända typord (fråga 2 i k_46barn3 är fortfarande öppen).
