# Granskningsutlåtande k_46ovr4, aktiva produkter i tidigare utanför-kategorier, omgång 4 (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan text får faktatext även i tidigare utanför-kategorier), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och formatet i `k_utlatande_43.json`. Webbkoll: tunturi.com (V10, SKU och EAN stämmer), återförsäljarsidor för Stiga SnowSkate 75-1116-06, Christopeit AL 2 och Fila Legacy Pro 80/84.

Alla 11 utkast och alla 13 avvisade är ACTIVE. `skrivfil_kontroll.py` ger inga formatfel men 5 spärrträffar (se fråga 1). Standardblocket är exakt rätt på alla; leveranstidsmeningen finns på 47305, 47306 och 47309, som är de enda med taggen På beställning. Titel ≤70 tecken och ≤2 kommatecken, SEO ≤43, meta 111–155 tecken med verb och "Passar för" finns på alla. Titlar och metatexter är unika mot alla andra utkast- och skrivfiler. En SEO-krock hittades (47310). Butiken söktes på Legacy, Tempt, Defy, SnowSkate, Cardiff, Catania, Lyon, Cardio Fit och Essensey. Varje rättning är ETT sammanhängande före/efter-par per fält, och varje före-text förekommer exakt en gång i utkastet (kontrollerat i python).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_46ovr4.json`.

## Resultat: 5 GODKÄND, 6 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 47301 | 10472324399370 | k_46ovr4_utkast.json | RÄTTA | html |
| 47302 | 10472349597962 | k_46ovr4_utkast.json | GODKÄND | – |
| 47303 | 10472435187978 | k_46ovr4_utkast.json | GODKÄND | – |
| 47304 | 10472522055946 | k_46ovr4_utkast.json | GODKÄND | – |
| 47305 | 10476166807818 | k_46ovr4_utkast.json | RÄTTA | html |
| 47306 | 10476252692746 | k_46ovr4_utkast.json | RÄTTA | titel, html |
| 47307 | 10480045523210 | k_46ovr4_utkast.json | RÄTTA | html |
| 47308 | 10480045850890 | k_46ovr4_utkast.json | GODKÄND | – |
| 47309 | 10486629597450 | k_46ovr4_utkast.json | RÄTTA | html |
| 47310 | 10494939595018 | k_46ovr4_utkast.json | RÄTTA | seo_title |
| 47311 | 10494939627786 | k_46ovr4_utkast.json | GODKÄND | – |

## Löften och påståenden

Alla texter söktes igenom efter tydliga och subtila löften: hälsa (energimetabolism, hår och hud, kalorier, muskler, ryggkotor, avslappning), säkerhet och skydd (säker hantering, stabil, halk, broms), prestanda (snabbare, längre, vibrationsdämpning, trötthet, lättast i klassen, hastighet) och kvalitet (slitstark, robust, högkvalitativ, slitagefri). Inget sådant finns kvar. Kosttillskottets grönt teextrakt, CLA och natriumhyaluronat står bara i ingredienslistan. Vibrationsplattan har bara specifikation. Rullskridskornas broms beskrivs bara som justerbar.

## Detaljer per produkt

### 47301 (10472324399370): RÄTTA

Live ACTIVE, Default 75-1116-06, EAN 7318681116068, 1719 kr, lager 4. Plast och glasfiber, EVA-skum på ovansidan, 85 x 23,5 cm ur egen källa; återförsäljare bekräftar 75-1116-06 = blå, 85 x 23,5 cm. Slitstark, bättre balans och 'för mindre berg' rätt utelämnade; lastgräns 'Ej känd' enligt v1.10. RÄTTA (R1): 'kort' i Passar för är en egen värdering som inte står i källan.

- **html** före: `<li>Dig som söker en kort snowboard i plast och glasfiber</li>`
- **html** efter: `<li>Dig som söker en snowboard i plast och glasfiber</li>`

### 47302 (10472349597962): GODKÄND

Live ACTIVE, 21372, EAN 5902114046835, 109 kr, lager 10. Ingredienser, dos, användning, varning och förvaring ordagrant ur egen källa; 'bidrar till korrekt energimetabolism', 'friskt hår och frisk hud' och livsstilsmeningen rätt utelämnade. Grönt teextrakt, CLA och natriumhyaluronat står bara som ingredienser utan effekt. Två 'enligt tillverkaren' (dos, varning). Kosttillskott omfattas av beslutet 2026-11-08 för aktiva produkter. Typordet Multivitamin är live-titelns ord (R7).

### 47303 (10472435187978): GODKÄND

Live ACTIVE, 11055, EAN 8715019110559, 489 kr, lager 17. Hopfällbar, tätt vävt stål, svart, pakethållare, tre monteringsklämmor och instruktioner ur egen källa. Måtten rätt utelämnade (33 x 23 x 20 mot 33 x 32 x 20 i samma källa, R2). Unik, idealisk och 'mobila bagageutrymme' utelämnade. Spärrlistan (tidigare-avvisade, DRAFT-status 2026-11-04) stoppar produkten tills undantag läggs in (R14).

### 47304 (10472522055946): GODKÄND

Live ACTIVE, 11057, EAN 8715019110573, 279 kr, lager 13. Pakethållare, svart, avtagbar, plastbelagda handtag och mått 19 x 27 x 32 cm ur egen källa. Avlastning av rygg och axlar, säker hantering, högkvalitativ och prisvärd rätt utelämnade. Ingen lastuppgift. Spärrlistan (tidigare-avvisade, DRAFT-status) stoppar produkten tills undantag läggs in (R14).

### 47305 (10476166807818): RÄTTA

Live ACTIVE, en variant M/L / gray, SKU 1031022146, EAN 4711291228443, 56709 kr, lager 2, tagg På beställning; leveranstidsmeningen finns. Storleken står i varianttiteln, ingen härledning ur slutsiffra behövs. Skriven syskonprodukt 10476178669834 (SKU 1031022144, 48929 kr) är annan storlek, alltså inte exakt dubblett (beslut 2026-11-05); titeln skiljer dem med M/L. Di2 enligt v1.7 utan batteri. Vibrationsdämpning, trötthet och 'lättaste i sin klass' utelämnade. SEO börjar med märket som syskonen (Giant-praxis). RÄTTA (R5): längden enligt tillverkaren stod två gånger (Passar för och specifikation); behålls bara i specifikationen.

- **html** före: `<li>Dig som är ca 178–186 cm lång (storlek M/L enligt tillverkaren)</li>`
- **html** efter: `<li>Dig som är ca 178–186 cm lång (storlek M/L)</li>`

### 47306 (10476252692746): RÄTTA

Live ACTIVE, M / purple 1101019185 (lager 1) och L / purple 1101019187 (lager 0), samma pris 11919 kr och färg: v1.8 uppfylld. Slutsiffror 5=M och 7=L stämmer med Giant/Liv-regeln. Tagg På beställning; leveranstidsmeningen finns. Skriven syskonprodukt 10476230541578 (Mountainbike Liv Tempt 3, 29 tum, Tyrian Purple, SKU 1101019184 = S) har samma modell och färg; beslutet 2026-11-05 kräver titel som skiljer dem. Damcykel är entydig översättning av live-ordet Women's bike och används på andra Liv Tempt. RÄTTA: titeln får 'M och L' så att den skiljer sig från syskonet (låser ingen enskild storlek); '100 mm' i gaffelraden är oklart i den engelska källan ('steel steerer 100mm', troligen fjäderväg) och stryks (R2).

- **titel** före: `Damcykel Liv Tempt 3 29 tum, Tyrian Purple`
- **titel** efter: `Damcykel Liv Tempt 3 29 tum, Tyrian Purple, M och L`

- **html** före: `<li>Gaffel: SR Suntour XCE, snabbspänne, styrrör av stål, 100 mm</li>`
- **html** efter: `<li>Gaffel: SR Suntour XCE, snabbspänne, styrrör av stål</li>`

### 47307 (10480045523210): RÄTTA

Live ACTIVE, H9115, EAN 8445960018313, 12129 kr, lager 4. Magnetisk broms, 16 kg svänghjul, 32 nivåer, LCD, 3 program, mått, vikt och användarvikt ur egen svensk källa. Spinningcykel är live-titelns typord (R7). RÄTTA (R5): användarvikten stod med 'enligt tillverkaren' både i inledningen och i specifikationen; en gång räcker (praxis k_41c).

- **html** före: `<li>Maximal användarvikt enligt tillverkaren: 110 kg</li>`
- **html** efter: `<li>Maximal användarvikt: 110 kg</li>`

### 47308 (10480045850890): GODKÄND

Live ACTIVE, 30-11072B, EAN 4044163110721, 6699 kr, lager 1. Uppgifterna finns i egen källa. Lastraderna motsäger varandra (Lastkapacitet 24, Max. belastning 9 kg, Maximal användarvikt 150 kg) och 'Ej känd' är godtagbart enligt R4/v1.5. Återförsäljare (baur.de, otto.de) anger 150 kg för AL 2 men ingen tillverkarsida knyter 150 kg till exakt 30-11072B; därför står 'Ej känd' kvar. Tyst, slitagefri och användarvänlig utelämnade; '9 kg broms' utelämnad.

### 47309 (10486629597450): RÄTTA

Live ACTIVE, 19TCFV1000, EAN 8717842033135, 4439 kr, lager 10, tagg På beställning; leveranstidsmeningen finns. Vibrationsplattor omfattas av beslutet 2026-11-08 (tidigare utanför-kategorier, aktiva produkter). https://www.tunturi.com/en/tunturi-cardio-fit-v10-vibration-plate.html (SKU och EAN stämmer): oscillation, 58 x 35 x 33 cm inkl. sits, 11 kg, max användarvikt 150 kg, ingår två gummiband med handtag, fjärrkontroll och push-up-handtag. Alla effektpåståenden (balans, muskler, ryggkotor, avslappning) utelämnade. RÄTTA: 'handtag för armförlängningar' är maskinöversättning av push-up-handtag (tillverkarsidan) och blir 'handtag för armhävningar'; 'en stång' finns inte hos tillverkaren och stryks (R2); dubbelt 'enligt tillverkaren' om användarvikten tas bort i specifikationen (R5). Obs: vissa återförsäljare anger 120 kg, men egen källa och tillverkaren anger 150 kg. Spärrlistan (tidigare-avvisade) stoppar produkten tills undantag läggs in (R14).

- **html** före: `Vibrationsplattan har en avtagbar sits och levereras med två träningsgummiband med handtag, en stång och handtag för armförlängningar. Enligt tillverkaren är maximal användarvikt 150 kg.</p><h2>Passar för</h2><ul>
<li>Dig som söker en vibrationsplatta med oscillation</li>
<li>Dig som vill ha en platta med avtagbar sits och gummiband med handtag</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Vibrationsplatta</li>
<li>Märke: Tunturi</li>
<li>Modell: Cardio Fit V10</li>
<li>Funktion: Oscillation</li>
<li>Mått: 58 x 35 x 33 cm (inklusive sits)</li>
<li>Produktvikt: 11 kg</li>
<li>Maximal användarvikt enligt tillverkaren: 150 kg</li>
<li>Ingår: Avtagbar sits, två träningsgummiband med handtag, en stång och handtag för armförlängningar</li>`
- **html** efter: `Vibrationsplattan har en avtagbar sits och levereras med två träningsgummiband med handtag samt handtag för armhävningar. Enligt tillverkaren är maximal användarvikt 150 kg.</p><h2>Passar för</h2><ul>
<li>Dig som söker en vibrationsplatta med oscillation</li>
<li>Dig som vill ha en platta med avtagbar sits och gummiband med handtag</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Vibrationsplatta</li>
<li>Märke: Tunturi</li>
<li>Modell: Cardio Fit V10</li>
<li>Funktion: Oscillation</li>
<li>Mått: 58 x 35 x 33 cm (inklusive sits)</li>
<li>Produktvikt: 11 kg</li>
<li>Maximal användarvikt: 150 kg</li>
<li>Ingår: Avtagbar sits, två träningsgummiband med handtag och handtag för armhävningar</li>`

### 47310 (10494939595018): RÄTTA

Live ACTIVE, en variant 42.5 / black, SKU/EAN 8026473412241, 2329 kr, lager 1. Vuxna, ABEC 5-lager och användningsområden ur egen källa; ABEC 5 bekräftas för Legacy Pro 80 hos återförsäljare (decathlon.it, galaxus). Högkvalitativa, stabilitet, robust och 'nybörjare och avancerade' rätt utelämnade. RÄTTA (R12): SEO-titeln 'Rullskridskor Fila Legacy Pro 80' finns redan i a_5_utkast.json för den andra aktiva Legacy Pro 80 (10494939660554, EAN 8026473464257); storleken (enda varianten) skiljer dem. Spärrlistan (utanfor-tills-vidare, rullskridskor) stoppar produkten tills undantag läggs in (R14).

- **seo_title** före: `Rullskridskor Fila Legacy Pro 80`
- **seo_title** efter: `Rullskridskor Fila Legacy Pro 80, 42,5`

### 47311 (10494939627786): GODKÄND

Live ACTIVE, en variant 38 / black, SKU/EAN 8026473451097, 2709 kr, lager 1. Air-Flow och justerbar bromsvinkel/intensitet ur egen källa; Air-Flow bekräftas för Legacy Pro 84 hos återförsäljare. Källtexten delas med Legacy Pro 84 svart-grå, men de två uppgifterna gäller modellserien och inga löften återges (stötdämpning, prestanda, ventilation, nybörjare utelämnade). Tunn men minst två fakta utöver titeln (R3). SEO-träffen i a_5_utkast.json gäller samma produkt-id och är ingen krock. Spärrlistan (utanfor-tills-vidare, rullskridskor) stoppar produkten tills undantag läggs in (R14).

## Avvisade (k_46ovr4_avvisade.json)

Alla 13 avvisningar kontrollerades live. Ingen är uppenbart fel och ingen lyfts. 47401 Ice cats (engelsk titel, maskinöversatt källa, bara löften om säkert stöd och halka kvar), 47402 AXA LUX 606 (har redan strukturtext, SEO och meta; saknar bara taggen texter-klara), 47403 Toorx bröstbälte (bara frekvensen, som redan står i titeln), 47404 M-Wave byxklämma (en mening), 47405, 47406, 47408, 47411 och 47412 (olika pris och dubblerad SKU, lager 0, v1.9), 47407 Kona Lava Dome och 47413 Revolt Advanced 2 (skillnaden mot skriven produkt går inte att fastställa; Kona och slutsiffra 6 omfattas inte av storleksregeln), 47409 Fila Legacy Pro 80 (färglistan anger både svart och blå, i övrigt bara hälsolöften) och 47410 Legacy Pro 84 svart-grå (Default Title 2589 kr mot 44/black 2249 kr med olika EAN).

## Frågor till David

1. Spärrlistan stoppar 47303 och 47304 (tidigare-avvisade på grund av DRAFT-status), 47309 (tidigare-avvisade, vibrationsplatta) och 47310–47311 (utanfor-tills-vidare, rullskridskor). Alla spärrades bara på grund av kategori eller tidigare status och omfattas av ditt beslut 2026-11-08. Före skrivning behövs en undantagspost i `sparrlista.json` med hänvisning till beslutet (R14). Det är ett tillägg, inte en ändring. Profilen har också kvar vibrationsplattor och rullskridskor under `utanfor_tills_vidare` (R6).
2. Christopeit AL 2 (47308): egen källa har "Maximal användarvikt: 150 kg" men också motstridiga lastrader. Återförsäljare anger 150 kg; texten säger nu "Ej känd". Vill du ha 150 kg, krävs tillverkarens manual för 30-11072B.
3. Giant Defy Advanced 1 Thundercloud: M/L kostar 56709 kr och den skrivna S-varianten 48929 kr. Kontrollera priset (texten berörs inte).
4. AXA LUX 606 (47402) har text men saknar taggen texter-klara. Ska taggen sättas efter kontroll?
5. Trec Multivit For Her har taggen Damcykel, och Legacy Pro 84 Lady har också taggen Damcykel. Taggarna är fel men rörs inte.
