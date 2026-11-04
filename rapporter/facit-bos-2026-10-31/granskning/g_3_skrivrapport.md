# Skrivrapport g_3 (Hammer JumpStep, Tunturi tillbehör, Velomarket), 2026-11-04

Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info före skrivning.
Skrivfil: `vag2_skriv/g_skriv_3.json` (6 produkter; passerade `skrivfil_kontroll.py` på nytt före skrivning: 6 produkter, 0 FEL, 0 varningar). Övriga produkter i g_3 är avvisade/underkända och saknas i filen.
Före-fil: `rapporter/shopify-original-2026-11-04/g_3_fore.json` (6 av 6 id, sparad före första skrivning).

## Före / efter
- Före: alla 6 ACTIVE, ingen med texter-klara, ingen med taggen "På beställning" (kontrollerat live), SEO-titel och meta null på alla. Titlarna skilde sig från skrivfilen på alla 6 (t.ex. "Trampoline HAMMER JumpStep", "Ujumispoi TUNTURI Pullbuoy Medium"), så ingen hoppades över. Beskrivningarna var leverantörens originaltext (flera med brutna rader, t.ex. 10526 "Ø: 55 cm* 811 vinylfärg..." och 10549 "33,5 cm - vikt: 33,5 kg - 45,5 cm").
- Efter: title, seo.title (null när lika med titeln, vilket gäller 10543 och 10554), seo.description och descriptionHtml identiska med skrivfilen på 6 av 6. Handle, status och tagg-lista (före + texter-klara) oförändrade. Priset rördes inte.
- Leveranstidsmeningen ("Beställningsvaror kan ta upp till en vecka längre") finns inte i någon text och ska inte finnas, eftersom ingen produkt har taggen "På beställning".
- Bildblock (figure/img/Trix) i originalbeskrivningarna: inga hittades i någon av de 6.

## Kontrollskript
`kontrollera_produkttext.py` på kopia (`g3work/kopia.json`, html mappad till beskrivning, standardblocket i [[STANDARDBLOCK]], källtext = före-titel + före-text, `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70 --meta-max 155`): 0 FEL, 8 VARNINGAR. Sex är den kända "passar dig som" (rubriken heter "Passar för"). Två är nya och inte tidigare godtagna: "första stycket har fler än 3 meningar" för 10511 och 10554. Texterna är redan skrivna och verifierade; varningen är ingen blockering men bör bedömas (förstastycket har 2 resp. 2 meningar vid manuell räkning, så det kan vara skriptets meningsräkning som tar "+" eller förkortningar som meningsslut).

## Skrivning
Kanarie 3 (10493, 10511, 10526), återläst och verifierad, därefter 3 (10543, 10549, 10554). Varje mutation genererades av `g3work/bygg.py` (json.dumps ensure_ascii=True, kontroll mot osynliga tecken) och klistrades in ordagrant. userErrors tomma i alla anrop. seo skickades alltid med både title och description.

## Återläsning
Alla 6 återlästa (3 åt gången) med title, handle, status, tags, seo.title, seo.description och descriptionHtml. Jämförelse i python (`g3work/jamfor.py`) mot skrivfilen och före-filen: 6 av 6 OK, 0 avvikelser, 0 osynliga tecken (Cf/Zs). Maskinellt: alla fält ovan. För hand: själva återläsningsfilerna (`g3work/aterlas_1.json`, `aterlas_2.json`) och före-filen är avskrifter av tool-svar (verktygen sparar inte till fil); en felkopiering skulle ge falsk avvikelse, inte falsk överensstämmelse. Före-filen är en avskrift som inte kontrollerats mot en andra läsning.

## Taggar
texter-klara tillagd sist på alla 6 med tagsAdd, tomma userErrors. Svaret visar att befintliga taggar (Hammer, Utomhusträning, Tunturi, Fell, Träningsbollar, Tillbehör, Crosstrainers, puls, pulsklocka, pulsmätare, Konditionsträning & Fitness, Velomarket) finns kvar.

## Avvikelser
Inga i skrivningen. Handles innehåller gamla ord ("trampoline", "ujumispoi", "gymboll-verdrag") och rördes inte, enligt uppdraget.

## Oklart eller saknat i regler och prompt
- Prompten b_skrivprompt.md nämner "högst 8 produkter per anrop" och "Velomarket-produkter"; R16 säger högst 5 och återläs högst 4. Jag följde R16 (3 per anrop).
- b_skrivprompt.md anger inte `--meta-min 70`; skriptets standard är 130 och ger FEL på kort sann meta (R12/§14 tillåter 70). Utan flaggan hade kontrollen stoppat felaktigt.
- b_skrivprompt.md hänvisar till rot-CLAUDE.md och `produkttexter-standard.md`; i denna körning låg `/home/user/Shopify/CLAUDE.md` i sessionens instruktioner, och rapporten följer regelboken v1.2. Standard §10–11 och LARDOMAR.md lästes inte separat.
- Sparrlistan lästes inte manuellt; spärrkontrollen (R14) gjordes av `skrivfil_kontroll.py` (0 FEL).
- Taggens namn är "texter-klara" (profilens `klartagg`), inte "texter-klar".
- Nya skriptvarningen "första stycket har fler än 3 meningar" saknas i listan över godtagna varningar (se ovan).
- CLAUDE.md kräver `rapporter/beslut-ÅÅÅÅ-MM-DD.md` efter varje arbetspass samt post i ändringsloggen. Jag har inte skrivit någon av dem (uppdraget var skrivning + RAPPORT; ändringsloggen är bara-tillägg och beslutsfilen ska sammanställas av koordinatorn). Behöver göras.

## Ändrat
- Shopify (BEST OF SPORTS): 6 produkter fick ny title, seo.title/seo.description och descriptionHtml samt taggen texter-klara. Handle, status, pris och övriga taggar oförändrade.
- Filer: `rapporter/shopify-original-2026-11-04/g_3_fore.json` (ny), denna rapport (ny), arbetsfiler i scratchpad `g3work/` (kopia.json, kontroll.txt, bygg.py, jamfor.py, aterlas_1.json, aterlas_2.json). Inget committat.
