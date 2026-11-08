# Granskningsutlåtande k_46ovr2: övriga tidigare utanför-kategorier (2026-11-08)

Granskaren har bara läst i Shopify och har inte ändrat något där eller committat något. Live-läsningen gjordes med `shopify_api.py` (`verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlaget var CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter får faktatext även i tidigare utanför-kategorier), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och formatet i `k_utlatande_43.json`. Webbkoll gjordes för Christopeit Vibro 3000 (120 kg bekräftat), FILA Houdini Pro, Start Wax Remover och Hammer Body Screen TX (ingen träff).

Alla tio utkast är ACTIVE. Standardblocket är exakt som i den kanoniska filen. Leveranstidsmeningen finns bara på 47105 och 47120, som är de enda med taggen På beställning. Alla titlar är högst 70 tecken med högst 2 kommatecken, alla SEO-titlar högst 43 tecken, och alla metatexter är 101–136 tecken med verb. "Passar för" finns överallt, och "enligt tillverkaren" står högst 2 gånger per text. Inga cirkulära inledningar. Titel, SEO och meta är unika mot alla andra utkast- och skrivfiler, utom 47106 vars SEO-titel finns i det äldre, oskrivna utkastet a_2 för samma id. `skrivfil_kontroll.py` ger bara spärrfel (47105, 47123, 47106, 47118), både före och efter rättning. Varje rättning är ETT sammanhängande före/efter-par per fält, och före-texten förekommer exakt en gång i utkastet (kontrollerat i python).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_46ovr2.json`.

## Resultat: 3 GODKÄND, 6 RÄTTA, 1 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 47101 | 10470932807946 | k_46ovr2_utkast.json | RÄTTA | html |
| 47102 | 10470937755914 | k_46ovr2_utkast.json | GODKÄND | – |
| 47105 | 10471019020554 | k_46ovr2_utkast.json | RÄTTA | titel |
| 47123 | 10472276721930 | k_46ovr2_utkast.json | RÄTTA | titel |
| 47124 | 10472276984074 | k_46ovr2_utkast.json | RÄTTA | titel |
| 47106 | 10471232602378 | k_46ovr2_utkast.json | RÄTTA | html |
| 47116 | 10472253227274 | k_46ovr2_utkast.json | UNDERKÄND | – |
| 47118 | 10472257323274 | k_46ovr2_utkast.json | RÄTTA | html |
| 47120 | 10472265351434 | k_46ovr2_utkast.json | GODKÄND | – |
| 47121 | 10472269611274 | k_46ovr2_utkast.json | GODKÄND | – |

## Löften (hälsa, säkerhet, skydd, prestanda, kvalitet)

Alla texter genomsöktes efter både tydliga och subtila löftesord: hälsa, säker, skydd, stöd, dämpning, stabil, hållbar, slitstark, robust, effektiv, avslappning, smärta, cirkulation, återhämtning, koncentration, energi, sömn, prestanda och kvalitet. Inga sådana ord finns kvar. OBS- och varningsrader (akupressur, kosttillskott) återger bara tillverkarens kontraindikationer och användningsbegränsningar som upplysning. 47118 hade en subtil överdrift om materialet ("gjorda i mikrofiber"), som är rättad.

## Avvisade (k_46ovr2_avvisade.json)

Alla 14 avvisningar står sig, och ingen lyfts ur. Kälken STIGA Pacer (47111) skulle kunna skrivas efter webbkoll, men live-texten anger svart medan varianterna är svart, rosa och grön och källan i övrigt bara innehåller löftesord, så avvisningen är inte uppenbart fel. Shimano MF-TZ500-7 (47109) är enligt modellbeteckningen ett frihjul, men live-texten säger kassett, så motsägelsen finns. 47122 (Vibrating Duo) har redan texter-klara.

## Frågor till David

1. Spärrlistan: 47105, 47123, 47106 och 47118 behöver en undantagspost i `sparrlista.json` med hänvisning till beslutet 2026-11-08 (R14) innan skrivfilen byggs.
2. Rhodiola (47121) var markerad "väntar tills David svarat särskilt" 2026-11-07. Omfattas den av beslutet 2026-11-08?
3. Start Wax Remover (47116): vill du ha ett nytt utkast med typordet Vallaborttagning? Ordet bygger på återförsäljarnas engelska namn och står inte i den egna källan. Farovarningen bör i så fall stämmas av mot säkerhetsdatabladet.
4. Typordet Kroppsanalysvåg (47101) kommer från profilens kategorinamn, inte från källan. Ska det godkännas i `godkanda_typord`?
5. Tunturi-akupressurmattorna har olika titelordning i k_46ovr1 ("med kudde Tunturi") och k_46ovr2 ("Tunturi med Kudde"). Välj en form för alla.

## Skäl och rättningar per produkt

### 47101 (10470932807946, k_46ovr2_utkast.json): RÄTTA

Live ACTIVE, 75000, EAN 4005251750007, lager 2. Alla uppgifter står i egen svensk källa (4+4 sensorer, DSM-BIA/SMFIM, 43 parametrar, Bodypedia, 200 kg, mått, vikt, 4 x AA). Hälsorelaterade, exakta, hälsopoäng, patenterade och hälsa/träningsresultat är rätt utelämnade. 200 kg är en svensk rad med etikett och enhet och står en gång med "enligt tillverkaren" (R4/v1.10). "Enligt tillverkaren" står 2 gånger. Rättning: källan säger inte "fötter"; "Passar för" använder nu källans ord (R1). Ingen tillverkarsida hittades (webbsökning på SKU/EAN gav ingen träff), så texten bygger bara på egen källa. Typordet Kroppsanalysvåg följer profilens kategorinamn (live-titeln är "Weight"). Kategorin omfattas av beslutet 2026-11-08 (elektronik, tidigare utanför).

- **html** före: `Dig som söker en kroppsanalysvåg med sensorer för både fötter och händer`
- **html** efter: `Dig som söker en kroppsanalysvåg med viktsensorer och handsensorer`

### 47102 (10470937755914, k_46ovr2_utkast.json): GODKÄND

Live ACTIVE, 5534, EAN 5902114011758, lager 1. Ingredienser, dos, användning, varning och förvaring finns ordagrant i egen källa. Metabolismaktivatorer, stress/kost/träning, lättassimilerade och hälsosam livsstil är utelämnade; inga hälsopåståenden. Texten är konsekvent med det skrivna syskonet 60 kapslar (10470937788682, SKU 5533, egen EAN) men har egen titel, SEO och meta, så det är ingen dubblett. Gemena "kapslar" följer praxis i skrivna Trec-titlar. Ett äldre utkast för samma id (k_30a) är inte skrivet; produkten saknar texter-klara.

### 47105 (10471019020554, k_46ovr2_utkast.json): RÄTTA

Live ACTIVE, 14TUSYO068, EAN 8717842035245, lager 0. Taggen På beställning finns och leveranstidsmeningen står i standardblocket (R13/v1.8). Mått, vikter, set med väska och avtagbart tvättbart överdrag finns i egen källa. Alla hälsopåståenden (avslappning, sömn, smärta, stress, cirkulation, energi) är utelämnade. OBS-raden återger bara de entydiga delarna av tillverkarens kontraindikationer, som upplysning och inte som löfte; det svarta setet saknar "gravid" i källan, vilket är rätt. Färgen står i live-titeln. Rättning R9: stor bokstav på beskrivande ord i titeln (Kudde, som i skrivna titlar "med Främre Korg"). Akupressur omfattas av beslutet 2026-11-08. Spärrlistan: produkten står i en aktiv spärr i sparrlista.json; skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt.

- **titel** före: `Akupressurmatta Tunturi med kudde, Svart`
- **titel** efter: `Akupressurmatta Tunturi med Kudde, Svart`

### 47123 (10472276721930, k_46ovr2_utkast.json): RÄTTA

Live ACTIVE, 14TUSYO094, EAN 8717842037256, lager 3, ingen På beställning och ingen leveranstidsmening (rätt). Uppgifterna och OBS-raden (inklusive gravid) finns i egen källa; hälsopåståendena är utelämnade. Annan färg och EAN än 47105/47124, så ingen dubblett (beslut 2026-11-05). Rättning R9: Kudde i titeln. Spärrlistan: produkten står i en aktiv spärr i sparrlista.json; skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt.

- **titel** före: `Akupressurmatta Tunturi med kudde, Roséguld`
- **titel** efter: `Akupressurmatta Tunturi med Kudde, Roséguld`

### 47124 (10472276984074, k_46ovr2_utkast.json): RÄTTA

Live ACTIVE, 14TUSYO092, EAN 8717842037232, lager 5, ingen På beställning. Samma bedömning som 47123. Rättning R9: Kudde i titeln. Spärrlistan stoppar inte denna. Obs: syskonet Ljusblå i k_46ovr1 har titelordningen "Akupressurmatta med kudde Tunturi, Ljusblå". Båda formerna är tillåtna, men titlarna bör göras enhetliga när skrivfilen byggs.

- **titel** före: `Akupressurmatta Tunturi med kudde, Mintgrön`
- **titel** efter: `Akupressurmatta Tunturi med Kudde, Mintgrön`

### 47106 (10471232602378, k_46ovr2_utkast.json): RÄTTA

Live ACTIVE, totalInventory 7. Storlekarna 40–44 är alla black: 44 kostar 3 059 kr och de övriga 3 519 kr. Default Title delar SKU med 44. Titel, SEO och text låser varken storlek, pris eller färg (v1.7/v1.9), och färgen är rätt utelämnad eftersom live-titeln Svart/Vit inte stämmer med varianterna. Ram, hjul, lager, stövel, innersula och vaddering finns i egen källa och stämmer med återförsäljares uppgifter (3x110, ABEC 9). Löftesord (säkert, stabilitet, dämpning, hållbara, högpresterande) är utelämnade. Rättning R2: raden om fästsystemet ("remmar, klämma och knappar på fotvalvet") är maskinöversatt och går inte att verifiera, eftersom återförsäljarna anger snörning, spänne och rem olika. Den tas bort ur inledningen och specifikationen. Ett äldre utkast för samma id (a_2) har samma SEO-titel men är inte skrivet; produkten saknar texter-klara. Spärrlistan: produkten står i en aktiv spärr i sparrlista.json; skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt.

- **html** före: `Innersulan Zero-Shock sitter i hälområdet, och fästsystemet har remmar, klämma och knappar på fotvalvet.</p><h2>Passar för</h2><ul>
<li>Dig som söker rullskridskor med tre hjul på 110 mm</li>
<li>Dig som vill ha rullskridskor med aluminiumram och ABEC 9-lager</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Rullskridskor</li>
<li>Märke: Fila</li>
<li>Modell: Houdini Pro</li>
<li>Ram: Aluminium, 6000-serien</li>
<li>Hjul: 3 x 110 mm</li>
<li>Lager: ABEC 9</li>
<li>Stövel: Hög</li>
<li>Innersula: Zero-Shock i hälområdet</li>
<li>Vaddering: Förformad och anatomisk (Performance-fit)</li>
<li>Fästsystem: Remmar, klämma och knappar på fotvalvet</li>`
- **html** efter: `Innersulan Zero-Shock sitter i hälområdet.</p><h2>Passar för</h2><ul>
<li>Dig som söker rullskridskor med tre hjul på 110 mm</li>
<li>Dig som vill ha rullskridskor med aluminiumram och ABEC 9-lager</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Rullskridskor</li>
<li>Märke: Fila</li>
<li>Modell: Houdini Pro</li>
<li>Ram: Aluminium, 6000-serien</li>
<li>Hjul: 3 x 110 mm</li>
<li>Lager: ABEC 9</li>
<li>Stövel: Hög</li>
<li>Innersula: Zero-Shock i hälområdet</li>
<li>Vaddering: Förformad och anatomisk (Performance-fit)</li>`

### 47116 (10472253227274, k_46ovr2_utkast.json): UNDERKÄND

Live ACTIVE, 15MW503200-U00T000, EAN 6418016050324, lager 2. Källan är maskinöversatt (finskt "voide", alltså valla, översatt som "fett"). Enligt återförsäljarna är Start-produkten en vallaborttagare (Start Ski Wax Remover 1000 ml). Typordet Fettlösare och uppgiften "främst för att ta bort underhållsfett" är därför fel, och källan motsäger sig själv (fettlösare eller glidvallningsborttagning) (R2/R3). Ett korrekt typord (vallaborttagning) har inget stöd i den egna källtexten (R7). Kemikalien har en ofullständig farovarning som bör stämmas av mot säkerhetsdatabladet. Kan inte rättas säkert.

### 47118 (10472257323274, k_46ovr2_utkast.json): RÄTTA

Live ACTIVE. S/M/L är alla blue och kostar 379/379/389 kr; totalInventory 24. Samma artikel i olika storlekar (v1.9). Färgen får stå eftersom alla varianter är blå (v1.8), och storlekarna S, M och L säljs som varianter. TransTextura, 4-vägs stretchtyg, mikrofiber och fingertoppar för smartphone finns i egen källa. Skyddslöftet (skavsår vid fall), fukt- och torkegenskaper och "andningsbart, krymper inte" är rätt utelämnade. Rättning R1: källan säger "Mjukt mikrofibermaterial", inte att handskarna är gjorda av mikrofiber. Därför står nu "har ... mikrofibermaterial" och "handskar med mikrofiber". Ingen sport anges, vilket är rätt. Spärrlistan: produkten står i en aktiv spärr i sparrlista.json; skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt.

- **html** före: `Liv Energize LF har TransTextura-tyg samt 4-vägs stretchtyg på baksidan och i panelerna, och handskarna är gjorda i mjukt mikrofibermaterial. Fingertopparna är avsedda för smartphoneanvändning.</p><h2>Passar för</h2><ul>
<li>Dig som söker handskar med fingertoppar för smartphoneanvändning</li>
<li>Dig som vill ha handskar i mikrofiber och stretchtyg`
- **html** efter: `Liv Energize LF har TransTextura-tyg, 4-vägs stretchtyg på baksidan och i panelerna samt mjukt mikrofibermaterial. Fingertopparna är avsedda för smartphoneanvändning.</p><h2>Passar för</h2><ul>
<li>Dig som söker handskar med fingertoppar för smartphoneanvändning</li>
<li>Dig som vill ha handskar med mikrofiber och stretchtyg`

### 47120 (10472265351434, k_46ovr2_utkast.json): GODKÄND

Live ACTIVE, 30-1970, EAN 4044163019703, lager 6. Taggen På beställning finns och leveranstidsmeningen står i standardblocket. Bara tekniska uppgifter ur egen svensk källa. Regenerativ/förebyggande effekt, muskelgrupper och frekvensernas effekter är utelämnade; inga hälso- eller träningseffektlöften. 120 kg är en svensk rad med etikett och enhet och står en gång med "enligt tillverkaren". Det stöds av flera återförsäljare (BAUR, Kaufland) och av bruksanvisningen för best.-nr 1970; en enstaka eBay-uppgift om 150 kg bedöms som avvikande. 0,3 kW och 500 W återges som i källan med separata etiketter. Vibrationsplattor omfattas av beslutet 2026-11-08.

### 47121 (10472269611274, k_46ovr2_utkast.json): GODKÄND

Live ACTIVE, 12127, EAN 5902114019006, lager 5. Ingredienser, dos, användning, varning och förvaring finns ordagrant i egen källa. Alla hälsopåståenden (trötthet, stress, koncentration, sexuella funktioner, fysik) är utelämnade, liksom den motsägande raden om "3 mg per dag" (R2). Typordet Adaptogen (ett påståendeord) är bytt mot Kosttillskott enligt butikens tagg och de skrivna Trec-syskonen. Obs: Rhodiola markerades 2026-11-07 som "väntar tills David svarat särskilt". Beslutet 2026-11-08 omfattar kosttillskott generellt; David bör bekräfta att Rhodiola ingår.
