# Granskningsutlåtande k_46barn3, barnprodukter (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan text får faktatext även i tidigare utanför-kategorier), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och `k_utlatande_46barn1.md`/`46barn2.md` samt formatet i `k_utlatande_43.json`.

Alla 13 utkast är ACTIVE med lager > 0 och saknar texter-klara. 12 har en variant (Default Title); 46802 har nio längdvarianter (v1.9). Standardblocket är exakt som i `b_skriv_24.json` på alla utom 46815, där leveranstidsmeningen stod dubbelt (rättas). Leveranstidsmeningen finns bara på 46815, den enda med taggen På beställning. Efter rättning: titel 36–60 tecken och ≤2 kommatecken, SEO 24–43, meta 113–146 med verb, "Passar för" på alla. Titlar, SEO-titlar och metatexter är unika inom batchen och mot alla andra filer i `vag2_skriv/` (enda träffarna är 46812/46813 mot sina egna, aldrig skrivna a_5-utkast). Butiken söktes på SKU, streckkod och modellord: inga exakta dubbletter (R12a). Varje rättning är ETT sammanhängande före/efter-par per fält, och före-texten förekommer exakt en gång i fältet (kontrollerat i python). `skrivfil_kontroll.py` ger 0 formatfel och 0 varningar på utkasten och på de rättade texterna; de enda FEL är spärrlistan för 46804, 46805 och 46815 (utanfor-tills-vidare-2026-11-04), som behöver undantag enligt beslutet 2026-11-08.

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_46barn3.json`.

## Resultat: 2 GODKÄND, 11 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 46802 | 10494685348106 | k_46barn3_utkast.json | RÄTTA | titel |
| 46804 | 10494941823242 | k_46barn3_utkast.json | RÄTTA | titel |
| 46805 | 10494941888778 | k_46barn3_utkast.json | RÄTTA | seo_title |
| 46808 | 10530126332170 | k_46barn3_utkast.json | RÄTTA | titel |
| 46809 | 10530129445130 | k_46barn3_utkast.json | RÄTTA | titel, seo_title, meta, html |
| 46810 | 10530129838346 | k_46barn3_utkast.json | RÄTTA | titel, seo_title, html |
| 46812 | 10541367263498 | k_46barn3_utkast.json | GODKÄND | – |
| 46813 | 10541367492874 | k_46barn3_utkast.json | GODKÄND | – |
| 46815 | 10561353187594 | k_46barn3_utkast.json | RÄTTA | html |
| 46816 | 10572637012234 | k_46barn3_utkast.json | RÄTTA | html, meta |
| 46818 | 10612579041546 | k_46barn3_utkast.json | RÄTTA | titel, html |
| 46819 | 10612579074314 | k_46barn3_utkast.json | RÄTTA | titel |
| 46821 | 10665226895626 | k_46barn3_utkast.json | RÄTTA | titel, html, meta |

## Löften och säkerhetsord

Alla titlar, SEO-titlar, metatexter och beskrivningar genomsöktes efter säkerhets-, skydds-, hälso-, utvecklings-, prestanda- och kvalitetsord (säker, säkerhet, trygg, skydda/skyddar, stabil, slitstark, hållbar, kvalitet, bekväm, komfort, UV-skydd, synlig, utveckling, växer med, perfekt, effektiv). Inget löfte finns kvar. "Skydd" förekommer bara som produktnamn (knä- och armbågsskydd, stänkskydd) och som innehåll i Fila-setet (hjälm och skydd), aldrig som funktion. Kategori 4 och antireflex står som ren linsdata utan UV- eller siktlöfte. "Lätt" på discen (46813) står ordagrant i källan. Reflektorn har inga synlighets- eller säkerhetslöften (v1.9). Lastuppgiften "barn som väger upp till 100 kg" (46804) är rätt utelämnad (R4); stödhjulen har "Maximal lastgräns: Ej känd" enligt v1.10.

## Mönster

- **"Fuses" är maskinöversättning.** Seven Polska-skydden heter "Fuses …" i Velomarkets titlar; det är estniska "kaitsmed" (skydd, men också säkringar) översatt fel. Syskonet 10541367394570 heter "Frozen protectors". Ordet stryks i 46809 och 46810. Samma fel finns i utkastet 47207 (k_46ovr3, "Fuses Avengers") som ännu inte har granskats här.
- **R9:** färgord i titeln saknade stor bokstav på sju produkter (praxis "Handskar Cars för barn, Röda" och 46barn2).
- **Typord (R7):** SEO-titeln avvek från titelns typord på 46805 och var halv ("Armbågsskydd") på 46809/46810.
- **Artikelentydighet:** Cairn-titlarna angav bara första halvan av färgen; Bookman-reflektorn beskrevs med seriens djurformer och i plural, men tillverkaren anger "Ghost Pink" och 1 st.

## Per produkt

### 46802 (10494685348106): RÄTTA

Live ACTIVE, nio storleksvarianter 70–120 med olika SKU/EAN (21ARAH03AP-T03T…), 199 kr utom 115 (169 kr), lager 20. v1.9: samma artikel i olika längd, lager > 0; titel, SEO och text låser varken längd eller pris. Glasfiber, barn och de två stavlängdsformlerna står ordagrant i egen källa; enhet för längderna saknas och anges rätt inte. Inga löften. RÄTTA (R9): beskrivande ord i titeln med stor bokstav (praxis 46barn2). Obs: varianterna 70 och 80 har SKU-slut 670/680; påverkar inte texten.

- **titel** före: `Barnskidstavar Rex Apollo, glasfiber`
- **titel** efter: `Barnskidstavar Rex Apollo, Glasfiber`

### 46804 (10494941823242): RÄTTA

Live ACTIVE, SKU 010619147, EAN 8026473412692, 2009 kr, lager 1. Modell J-One 2020, 70–72 mm 82A PU-hjul och ABEC 5 ur egen källa; storlek S29–32 och färg ur live-titeln. 'Hållbar', 'bekväm', 'säkerheten', 'stabilitet' och 'barn som väger upp till 100 kg' (lastuppgift i löptext, R4) rätt utelämnade. Inga dubbletter (J-One G Rosa/Magenta är annan artikel och DRAFT). RÄTTA (R9): färgen i titeln med stor bokstav. Spärrlistan (utanfor-tills-vidare-2026-11-04) stoppar produkten i skriptet tills undantag läggs in enligt beslutet 2026-11-08 (R14).

- **titel** före: `Barnrullskridskor Fila J-One, S29–32, svart och röd`
- **titel** efter: `Barnrullskridskor Fila J-One, S29–32, Svart och Röd`

### 46805 (10494941888778): RÄTTA

Live ACTIVE, SKU 010616150, EAN 8026473364489, 2739 kr, lager 2. Justerbara, nybörjare ('tillverkaren riktar'), hjälm och skydd för knän/armbågar/handleder som innehåll, upp till fyra storlekar, 70–72 mm, ABEC 5 och fästsystem ur egen källa; storlek och färg ur live-titeln. 'Nödvändig skyddsutrustning', 'bekväm och stabil', 'säkert', 'jämn och kontrollerad' rätt utelämnade; hjälm och skydd utan funktionslöfte. RÄTTA (R7): SEO-titeln började med 'Rullskridskor' när titeln har typordet 'Barnrullskridskor'. Spärrlistan (utanfor-tills-vidare-2026-11-04) stoppar produkten i skriptet tills undantag läggs in enligt beslutet 2026-11-08 (R14).

- **seo_title** före: `Rullskridskor Fila J-One Combo`
- **seo_title** efter: `Barnrullskridskor Fila J-One Combo`

### 46808 (10530126332170): RÄTTA

Live ACTIVE, SKU 9059, EAN 5902308590595, 129 kr, lager 12. Barn, Avengers-stil, inre vaddering, storlek S/ålder 4–6 och justerbara manschetter ur egen källa; färg ur live-titeln. Skyddslöftet ('skydda händerna från stötar och repor'), 'bekväm' och den trasiga raden rätt utelämnade. Ingen dubblett (Handskar Cars 9044 och Prinsessa 59092 är andra artiklar). RÄTTA (R9): färgen i titeln med stor bokstav, som praxis 'Handskar Cars för barn, Röda'.

- **titel** före: `Handskar för barn Seven Polska Avengers, blå`
- **titel** efter: `Handskar för barn Seven Polska Avengers, Blå`

### 46809 (10530129445130): RÄTTA

Live ACTIVE, SKU 9006, EAN 5902308590069, 209 kr, lager 5. Källan är en mening med skyddslöften; entydiga fakta är knän och armbågar, barn, bilstil och vaddering, plus Cars och röd ur live-titeln (räcker enligt R3). 'Skyddar', 'vid fall', 'utmärkt skydd' rätt utelämnade. RÄTTA: (1) 'Fuses' är ingen serie utan maskinöversättning (estniska 'kaitsmed' = skydd/säkringar; syskonet 10541367394570 heter 'Frozen protectors') och stryks ur titel, SEO och text (R2); (2) SEO-titeln 'Armbågsskydd …' beskrev bara halva produkten och avvek från titelns typord (R7); (3) 'vadderingen som beskrivs av tillverkaren' är en arbetsformulering (R11); (4) metan 'bil-motiv från Cars' antyder en licens som källan inte nämner. Färgen i titeln med stor bokstav (R9).

- **titel** före: `Knä- och armbågsskydd Seven Polska Fuses Cars, röd`
- **titel** efter: `Knä- och armbågsskydd Seven Polska Cars, Röd`

- **seo_title** före: `Armbågsskydd Seven Polska Fuses Cars`
- **seo_title** efter: `Knä- och armbågsskydd Seven Polska Cars`

- **meta** före: `Knä- och armbågsskydd för barn med bil-motiv från Cars och vaddering. Färgen är röd och artikelnumret 9006.`
- **meta** efter: `Seven Polska Cars är vadderade knä- och armbågsskydd för barn med bilmotiv. Färgen är röd och artikelnumret är 9006.`

- **html** före: `<p>Fuses Cars från Seven Polska är knä- och armbågsskydd för barn i bil-stil. Skydden har vadderingen som beskrivs av tillverkaren.</p><h2>Passar för</h2><ul>\n<li>Dig som söker knä- och armbågsskydd till barn</li>\n<li>Dig som vill ha skydd med bil-motiv</li>\n</ul><h2>Specifikationer</h2><ul>\n<li>Typ: Knä- och armbågsskydd för barn</li>\n<li>Märke: Seven Polska</li>\n<li>Serie: Fuses Cars</li>`
- **html** efter: `<p>Cars från Seven Polska är vadderade knä- och armbågsskydd för barn med bilmotiv.</p><h2>Passar för</h2><ul>\n<li>Dig som söker knä- och armbågsskydd till barn</li>\n<li>Dig som vill ha skydd med bil-motiv</li>\n</ul><h2>Specifikationer</h2><ul>\n<li>Typ: Knä- och armbågsskydd för barn</li>\n<li>Märke: Seven Polska</li>\n<li>Modell: Cars</li>`

### 46810 (10530129838346): RÄTTA

Live ACTIVE, SKU 9061, EAN 5902308590618, 209 kr, lager 2. Anatomiskt formade, barn, användning med rullskridskor/skridskor/inlines/sparkcyklar, Disney-figurer, breda elastiska band, två armbågs- och två knäskydd ur egen källa. 'Slitstarkt', 'perfekt passform', 'minska skador vid fall' rätt utelämnade; EN 14120 utelämnad (godtas, ingen säkerhetsuppgift i texten). RÄTTA: 'Fuses' är maskinöversättning, inte serienamn (R2, se 46809), stryks ur titel, SEO och text; SEO-titeln 'Armbågsskydd …' ändras till titelns typord (R7, exakt 43 tecken); färgen i titeln med stor bokstav (R9).

- **titel** före: `Knä- och armbågsskydd Seven Polska Fuses Frozen 2, grön`
- **titel** efter: `Knä- och armbågsskydd Seven Polska Frozen 2, Grön`

- **seo_title** före: `Armbågsskydd Seven Polska Fuses Frozen`
- **seo_title** efter: `Knä- och armbågsskydd Seven Polska Frozen 2`

- **html** före: `<p>Setet Fuses Frozen 2 från Seven Polska innehåller två armbågsskydd och två knäskydd för barn. Delarna är anatomiskt formade och dekorerade med Disney-figurer.</p><h2>Passar för</h2><ul>\n<li>Dig som söker knä- och armbågsskydd till barn</li>\n<li>Dig som åker rullskridskor, skridskor, inlines eller sparkcykel</li>\n</ul><h2>Specifikationer</h2><ul>\n<li>Typ: Knä- och armbågsskydd för barn</li>\n<li>Märke: Seven Polska</li>\n<li>Serie: Fuses Frozen 2</li>`
- **html** efter: `<p>Setet Frozen 2 från Seven Polska innehåller två armbågsskydd och två knäskydd för barn. Delarna är anatomiskt formade och dekorerade med Disney-figurer.</p><h2>Passar för</h2><ul>\n<li>Dig som söker knä- och armbågsskydd till barn</li>\n<li>Dig som åker rullskridskor, skridskor, inlines eller sparkcykel</li>\n</ul><h2>Specifikationer</h2><ul>\n<li>Typ: Knä- och armbågsskydd för barn</li>\n<li>Märke: Seven Polska</li>\n<li>Modell: Frozen 2</li>`

### 46812 (10541367263498): GODKÄND

Live ACTIVE, SKU 59542, EAN 5902308595422, 99 kr, lager 5. Två plastracketar och en liten boll, Disney-figurer, lek på stranden/parken/trädgården och inomhus, Seven Polska ur egen källa; Frozen och lila ur live-titeln. 'Roligt' och 'perfekt' rätt utelämnade. Titel och SEO finns bara i det aldrig skrivna a_5-utkastet för samma produkt. Ingen dubblett.

### 46813 (10541367492874): GODKÄND

Live ACTIVE, SKU 59497, EAN 5902308594975, 39 kr, lager 3. Lätt (ordagrant), Disney-figurer, 23 cm, utomhuslek, Seven Polska ur egen källa; Frozen och lila ur live-titeln. 'Idealisk' och 'roliga' rätt utelämnade. Titel och SEO finns bara i det aldrig skrivna a_5-utkastet för samma produkt.

### 46815 (10561353187594): RÄTTA

Live ACTIVE, SKU 12153, EAN 4002556159092, 359 kr, lager 3, tagg På beställning. Rowdy 2.0, 20–24 tum, mountainbikes för barn och ungdomar, plast, mattsvart ur egen källa. 'Slitstarkt', 'hållbar', 'effektivt skydd mot lera och vatten', 'lätt', 'enkel installation' rätt utelämnade. Ingen dubblett (SKS Rowdy 10078 är annan EAN och DRAFT). RÄTTA (R13): leveranstidsmeningen stod två gånger, i inledningen och i standardblocket; den i inledningen stryks så att blocket är exakt som i profilen. Spärrlistan (utanfor-tills-vidare-2026-11-04) stoppar produkten i skriptet tills undantag läggs in enligt beslutet 2026-11-08 (R14).

- **html** före: `Skydden är gjorda av plast och har mattsvart finish. Beställningsvaror kan ta upp till en vecka längre.</p>`
- **html** efter: `Skydden är gjorda av plast och har mattsvart finish.</p>`

### 46816 (10572637012234): RÄTTA

Live ACTIVE, SKU AR-1220-M, ingen EAN, 229 kr, lager 5. 12/14/16/18/20 tum, plast med svart gummi, stålfästen silver, alla monteringsdelar, enkelväxel/navväxel, ej utanpåliggande växlar ur egen källa. Bärande del utan lastgräns i källan; 'Maximal lastgräns: Ej känd' och meningen i texten följer v1.10. 'Reservhjul' (motsäger resten) rätt utelämnat. RÄTTA: inledningen 'stödhjul är cykelsidohjul' är cirkulär (R11); metan sade 'plasthjul i svart gummi', men källan anger plasthjul täckta med svart gummi (R1).

- **html** före: `<p>Polaver stödhjul är cykelsidohjul för barn och passar cyklar med 12, 14, 16, 18 och 20 tums hjul.`
- **html** efter: `<p>Polaver stödhjul passar barncyklar med 12, 14, 16, 18 och 20 tums hjul.`

- **meta** före: `Passar barncyklar med hjul på 12 till 20 tum: Polaver stödhjul med plasthjul i svart gummi och monteringsfästen i stål.`
- **meta** efter: `Polaver stödhjul passar barncyklar med 12–20 tums hjul. Hjulen är av plast täckt med svart gummi och fästena av silverfärgat stål.`

### 46818 (10612579041546): RÄTTA

Live ACTIVE, SKU JSPLAY812TU, EAN 3267654914276, 179 kr, lager 1. Ålder 4–8, kategori 4, antireflex, flexibla bågar och glasbredd 54 mm ur egen källa. 'Pålitligt skydd', 'helt skyddade från UV', 'säker sikt', 'tål stötar' rätt utelämnade. Tillverkarsidan gick inte att nå. RÄTTA: (1) 'Ögonavstånd 116 mm' är orimligt som ögonavstånd och troligen maskinöversatt (ram- eller bågmått), och 'Bredd på tinningen 16 mm' är oklar; båda stryks (R2), samma bedömning som utkastaren gjorde för Bloom; (2) titeln angav bara 'matt svart' men live-färgen är Matt Svart Fluo Rosa; hela färgen och stor bokstav (R1, R9).

- **titel** före: `Barnsolglasögon Cairn Play, 4–8 år, matt svart`
- **titel** efter: `Barnsolglasögon Cairn Play, 4–8 år, Matt Svart och Fluo Rosa`

- **html** före: `<li>Ögonavstånd: 116 mm</li>\n<li>Bredd på tinningen: 16 mm</li>\n`
- **html** efter: (tomt)

### 46819 (10612579074314): RÄTTA

Live ACTIVE, SKU JLBLOOM02TU, EAN 3267654930092, 209 kr, lager 1. Ålder 8–12, kategori 4, antireflex, (super)flexibla bågar, glasbredd 51 mm ur egen källa; de otydliga måttraderna rätt utelämnade. 'Säkerhet', 'maximalt skydd mot UV', 'säker sikt', 'oöverträffad bärkomfort' rätt utelämnade. RÄTTA: titeln angav bara 'matt svart' men live-färgen är Matt Svart Ljus Röd; hela färgen och stor bokstav (R1, R9).

- **titel** före: `Barnsolglasögon Cairn Bloom, 8–12 år, matt svart`
- **titel** efter: `Barnsolglasögon Cairn Bloom, 8–12 år, Matt Svart och Ljusröd`

### 46821 (10665226895626): RÄTTA

Live ACTIVE, SKU 485B, EAN 7350051864858, 89 kr, lager 1. Tillverkarsidan https://bookman.se/products.json (produkt 'Hanging Reflectors Adventure', handle soft-adventure-reflectors) visar varianten 485 'Ghost Pink' och 'Contents: 1 x Hanging Reflectors Adventure'. Utkastets 'reflektorer i form av små djur' och 'Form: Små djur' gäller serien (Fox Red 484 är räv), inte exakt denna artikel, och plural motsäger tillverkarens innehåll (en reflektor). Löften om skydd, säkerhet och certifierad reflektion rätt utelämnade (v1.9). RÄTTA: formen stryks, innehållet anges som 1 reflektor (R1, artikelentydighet); färgen i titeln med stor bokstav (R9). Ingen dubblett (Fox Red 484B är annan EAN).

- **titel** före: `Reflektor för barn Bookman Soft Adventure, rosa`
- **titel** efter: `Reflektor för barn Bookman Soft Adventure, Rosa`

- **html** före: `<p>Bookman Soft Adventure är reflektorer i form av små djur, gjorda för barn. De fästs med klämma eller snöre.</p><h2>Passar för</h2><ul>\n<li>Dig som söker en reflektor till barnets kläder eller ryggsäck</li>\n<li>Dig som vill fästa en reflektor på en barnvagn</li>\n</ul><h2>Specifikationer</h2><ul>\n<li>Typ: Reflektor för barn</li>\n<li>Märke: Bookman</li>\n<li>Modell: Soft Adventure</li>\n<li>Form: Små djur</li>\n`
- **html** efter: `<p>Bookman Soft Adventure är gjord för barn och fästs med klämma eller snöre. Förpackningen innehåller en reflektor.</p><h2>Passar för</h2><ul>\n<li>Dig som söker en reflektor till barnets kläder eller ryggsäck</li>\n<li>Dig som vill fästa en reflektor på en barnvagn</li>\n</ul><h2>Specifikationer</h2><ul>\n<li>Typ: Reflektor för barn</li>\n<li>Märke: Bookman</li>\n<li>Modell: Soft Adventure</li>\n<li>Innehåll: 1 reflektor</li>\n`

- **meta** före: `Bookman Soft Adventure är reflektorer i form av små djur för barn. De fästs på kläder, ryggsäck eller barnvagn med klämma eller snöre.`
- **meta** efter: `Den rosa reflektorn Bookman Soft Adventure är gjord för barn och fästs på kläder, ryggsäck eller barnvagn med klämma eller snöre.`

## Avvisade (k_46barn3_avvisade.json)

Alla elva avvisningar kontrollerades live och står sig; ingen lyfts. 46801 FILA X-One Ice G (titeln säger rullskridskor, källan beskriver skridskoblad i hockeystål för is), 46803 Uniplast-skidor (enda källraden är en lastuppgift i löptext), 46806 Giant träningshjul och 46814 Hamax regnskydd (tom källa), 46807 Tabou Rocket Alu (har redan strukturerad text och SEO; avvisad på samma grund i k_28s, se fråga 3), 46811 Fuses Stitch (en mening, inga fakta utöver titeln), 46817 Polisport Joy barnstol (barntransport, lastuppgift 9–22 kg utan etikett; inte uppenbart fel att lyfta till David), 46820 sittdyna (pris 9 kr, ett faktum), 46822/46823 (exakta dubbletter, samma SKU 1521-22 och EAN, lager 0) och 46824 skyddsram 1580-5 (dubblettpar med 10676715553034, redan hanterat med utkast och fråga i k_utlatande_46barn4).

## Frågor till David

1. Spärrlistan: 46804, 46805 och 46815 behöver undantag (utanfor-tills-vidare-2026-11-04) innan de kan skrivas, enligt beslutet 2026-11-08.
2. Typordet för Seven Polska-skydden: den här batchen använder "Knä- och armbågsskydd", k_46ovr3 (47207) "Skydd för knän och armbågar". Rekommendation: "Knä- och armbågsskydd" (kortare, ryms i SEO-titeln) i båda, och ordet läggs i profilens godkända typord.
3. 46807 Tabou Rocket Alu har en strukturerad text med avsnittet "Vanliga frågor" men saknar taggen texter-klara. Ska den räknas som klar (lägg taggen), eller skrivas om utan FAQ enligt beslutet 2026-11-08?
