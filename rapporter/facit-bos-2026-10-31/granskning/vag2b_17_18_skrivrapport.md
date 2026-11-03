# Skrivrapport våg 2b, skrivfil 17 och 18 (2026-11-03). Klar, verifierad.

## Resultat
- Skrivfil 17: 24 av 24 produkter skrivna och verifierade. Taggen texter-klara satt på alla 24 (kontrollerad mot före-läget: 0 avvikelser).
- Skrivfil 18: 17 av 17 produkter skrivna och verifierade. Taggen texter-klara satt på alla 17 (0 avvikelser).
- Inga produkter hoppades över. De tre produkter i fil 17 där titeln redan var lika skrivfilen (ADO Air 30 Pro x2, ADO Air One Ultra) skrevs om enligt koordinatorns beslut, och verifierades.

## Före-läge
- rapporter/shopify-original-2026-11-03/vag2b_17_fore.json (24 noder).
- rapporter/shopify-original-2026-11-03/vag2b_18_fore.json (17 noder). Skapades från ett sparat svar, med ett dubbelt fält som sedan togs bort.
- Kontroll: alla 41 produkter ACTIVE vid start. Ingen hade taggen texter-klara.

## Kontroll före skrivning
- Kontrollkopior: rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2b17/ (24 produkter, inkl. de tre) och tmp_kopia_vag2b18/ (17 produkter). kontrollera_produkttext.py med --seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70: 0 FEL i båda. Varningar: "passar dig som" (rubriken heter "Passar för") och engelska färgnamn i källan. Godtagna.

## Skrivning och återläsning
- Mutationer genererades med python (ensure_ascii=True) och klistrades in ordagrant. Batcher om 1 (sista), 3 (kanarie) eller 5 produkter.
- Återläsning: skickades i grupper om högst 4 produkter, klistrades in och jämfördes tecken för tecken i python mot skrivfilen. Kontrollerade fält: title, handle (mot före-läget), status, seo.title, seo.description, descriptionHtml, tags (mot före-läget). Osynliga tecken (U+00AD m.fl.) kontrollerades också.
- Resultat: inga avvikelser i någon grupp. Efter varje avvikelsekontroll gjordes ingen rättning med nya handskrivna variabler (det var inte nödvändigt).
- Notering om återläsningens tillförlitlighet: svaren från Shopify kom inline. Pastet in i python är en manuell kopiering av svaret, så en felkopiering skulle ge falsk avvikelse, inte falskt godkännande. Samtliga grupper gav "ALLA OK" vid första försöket.

## Ändrat
- Shopify: ja. Fält title, seo (title och description) och descriptionHtml på 41 produkter. Taggen texter-klara lagd på 41 produkter (tagsAdd). Inga ändringar av handle, status, pris eller andra taggar (verifierat).
- Filer: vag2b_17_fore.json, vag2b_18_fore.json, tmp_kopia_vag2b17/, tmp_kopia_vag2b18/, denna rapport.
- Inget committat.

## Observationer
- Produkten 10476168020234 (Giant Revolt 1, Alpine Green) hade före skrivning ett beskrivningsfält med inklistrad AI-chatt-markup. Ersatt av den godkända texten. Gäller även andra före-lägen; de övriga var rena.
- Det fanns sedan tidigare en svaghet i arbetssättet: skrivprompten hoppar över produkter med lika titel, vilket kan lämna gamla beskrivningar kvar. Koordinatorn beslutade att skriva om dem. Lärdom skrivs in i LARDOMAR (inte gjort i denna körning än, se nedan).

## Nästa steg
- David: beslut om skrivfilerna 17 och 18 kan tas från denna rapport. Fortsatt arbete: nattlig kontroll av titlar (vecka framåt) enligt LARDOMAR 2026-11-03.
