# Skrivrapport g_4 (Tunturi tillbehör och boxning, Velomarket), 2026-11-04

Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info före skrivning.
Skrivfil: `vag2_skriv/g_skriv_4.json` (7 produkter; `skrivfil_kontroll.py` på nytt före skrivning: 7 produkter, 0 FEL, 0 varningar). Övriga produkter i g_4 är avvisade och saknas i filen.
Före-fil: `rapporter/shopify-original-2026-11-04/g_4_fore.json` (7 av 7 id, sparad före första skrivning; avskrift av tool-svar).

## Före / efter
- Före: alla 7 ACTIVE, ingen med texter-klara, ingen med taggen "På beställning" (kontrollerat live), SEO-titel och meta null på alla. Titlarna skilde sig från skrivfilen på alla 7, så ingen hoppades över. 10612 (10541114491146) hade den trasiga live-titeln "Boxningssäck TUNTURI Speedball är ett stativ", ersatt med "Speedball Tunturi Free Standing". Övriga live-titlar var t.ex. "Stretch elastic TUNTURI Textile Light yellow", "TUNTURI Sauna Smoke", "Tunturi Skyddshjälm Head Guard L/XL". Beskrivningarna var leverantörens originaltext, flera med upprepade/brutna rader (10595 "Kompakt och lätt, lätt att bära ...", "Färg: Svart/vit; PVC; PVC: PVC") och tre med "Om Tunturi"-block.
- Efter: title, seo.title (null när lika med titeln: 10612, 10615, 10617), seo.description och descriptionHtml identiska med skrivfilen på 7 av 7. Handle, status och tagg-lista (före + texter-klara) oförändrade. Pris och övriga fält rördes inte.
- Leveranstidsmeningen ("Beställningsvaror kan ta upp till en vecka längre") finns inte i någon text, eftersom ingen produkt har taggen "På beställning".
- Bildblock (figure/img/Trix) i originalbeskrivningarna: inga hittades i någon av de 7.
- Observera: Swivel Chrome (10613) har live-taggen "Cykelväska" och 10612 likaså, 10591 "Cykelbelysning"; felaktiga cykeltaggar rörs inte utan beslut (beslutsloggen 2026-11-03) och rördes inte.

## Kontrollskript
`kontrollera_produkttext.py` på kopia (`g4work/kopia.json`, html mappad till beskrivning, standardblocket i [[STANDARDBLOCK]], källtext = före-titel + före-text, `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70 --meta-max 155`): 0 FEL, 7 VARNINGAR, alla den kända "saknar avsnittet 'passar dig som'" (rubriken heter "Passar för").

## Skrivning
Kanarie 3 (10591, 10595, 10599), återläst och verifierad, därefter 4 (10612, 10613, 10615, 10617). Mutationerna skrevs ut av `mutation_fran_skrivfil.py` (0 3 respektive 3 4) och klistrades in ordagrant. userErrors tomma i alla anrop. seo skickades alltid med både title och description.

## Återläsning
Alla 7 återlästa (3 + 4) med title, handle, status, tags, seo.title, seo.description och descriptionHtml. Jämförelse i python (`g4work/jamfor.py`, anpassad från g3work) mot skrivfilen och före-filen: 7 av 7 OK, 0 avvikelser, 0 osynliga tecken (Cf/Zs). Maskinellt: alla fält ovan inklusive tagg-lista. För hand: återläsningsfilerna (`g4work/aterlas_1.json`, `aterlas_2.json`) och före-filen är avskrifter av tool-svar (verktygen sparar inte till fil); en felkopiering ger falsk avvikelse, inte falsk överensstämmelse. Före-filen kontrollerades inte mot en andra läsning. Jag gjorde ett eget avskriftsfel i före-filen för 10613 (Material-raden) och rättade det mot tool-svaret innan skrivning.

## Taggar
texter-klara tillagd sist på alla 7 med tagsAdd (5 + 2), tomma userErrors. Läst tillbaka efteråt: alla 7 har texter-klara och alla tidigare taggar (Velomarket, Tunturi, Fell m.fl.) finns kvar; handle och status oförändrade.

## Avvikelser
Inga i skrivningen. Handles innehåller gamla ord ("stretch-elastic", "boxningss-ck-...-ett-stativ") och rördes inte.

## Oklart eller saknat i regler, prompt och skript
- Prompten b_skrivprompt.md säger "högst 8 produkter per anrop" och gäller Velomarket; R16 säger högst 5 och återläs högst 4. Jag följde R16/agentprompter (3 + 4 för skrivning, 3 + 4 för återläsning, taggar 5 + 2).
- b_skrivprompt.md anger inte `--meta-min 70`; skriptets standard är 130 och ger FEL på kort sann meta. Jag använde flaggan enligt R12/§14.
- b_skrivprompt.md hänvisar till rot-CLAUDE.md, `produkttexter-standard.md` och LARDOMAR.md; jag läste regelboken, beslutsloggen, agentprompter och b_skrivprompt enligt uppdraget, men inte standard §10–11 eller LARDOMAR.md separat. Sparrlistan lästes inte manuellt; R14 kontrollerades av `skrivfil_kontroll.py` (0 FEL).
- `mutation_fran_skrivfil.py` skriver inte ut `seo.title` som null när den är lika med titeln; den skickar alltid titeln, och Shopify lagrar då null. Fungerar, men jämförelsen måste förvänta null (gör `jamfor.py`).
- `jamfor.py` från g3work förutsätter att före-filen har numeriska id; min före-fil har gid-id (rått tool-svar) och skriptet fick justeras. Ett gemensamt jämförelseskript med fast format vore bättre.
- Taggens namn är "texter-klara" (profilens `klartagg`), inte "texter-klar".
- CLAUDE.md kräver `rapporter/beslut-ÅÅÅÅ-MM-DD.md` och post i ändringsloggen efter arbetspass; jag har inte skrivit någon av dem (uppdraget var skrivning + RAPPORT). Koordinatorn behöver göra det.

## Ändrat
- Shopify (BEST OF SPORTS): 7 produkter fick ny title, seo.title/seo.description och descriptionHtml samt taggen texter-klara. Handle, status, pris och övriga taggar oförändrade.
- Filer: `rapporter/shopify-original-2026-11-04/g_4_fore.json` (ny), denna rapport (ny), arbetsfiler i scratchpad `g4work/` (fore_a.json, fore_b.json, kopia_raw.json, kopia.json, kontroll.txt, jamfor.py, aterlas_1.json, aterlas_2.json). Inget committat.
