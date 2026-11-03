# Våg 2b, grupp 15 (25 elcyklar/cyklar), skrivrapport 2026-11-03

Butik: BEST OF SPORTS (bestofsports.se), verifierad med get-shop-info. Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/b_skriv_15.json`.

## Före/efter
- Före-läget (live, före skrivning) sparat i `rapporter/shopify-original-2026-11-03/vag2b_15_fore.json` (25 produkter, alla ACTIVE, seo null, gammal beskrivning).
- Efter skrivning: titel, handle, status, seo.title, seo.description, descriptionHtml och tags lästes tillbaka för alla 25 och jämfördes mot skrivfilen. Tags kontrollerades mot före-läget + "texter-klara" för alla 25.

## Hoppade över
- Inga produkter hoppades över (alla ACTIVE, ingen hade taggen "texter-klara").
- Två produkter (10470907412746, 10472250966282) hade samma titel i live som i skrivfilen. Skippregeln för "redan skrivna" tillämpades inte, eftersom beskrivningen och SEO fortfarande var de gamla. Båda skrevs.

## Kontroll före skrivning
- `kontrollera_produkttext.py` på kopia (`granskning/tmp_kopia_vag2b15/kopia.json`), med `--meta-min 70 --seo-title-max 43 --seo-suffix " – BEST OF SPORTS"`, html mappad till beskrivning, standardblock markerat, källtext = före-läget: **0 FEL, 56 VARNINGAR**. Varningarna är "Passar för"-rubriken (känd, godtagen) och engelska färgnamn i titlar och texter (Green, Grey, Black, Red, Blue). Inget avbröt skrivningen. Resultatet finns i `kontroll.txt` i samma mapp.
- Skrivfilen: inga osynliga tecken (U+00AD, nollbreddstecken).

## Skrivning
- Kanarie 3 produkter, sedan batcher om 5 (den tredje batchen om 2). Varje batch skrevs med `productUpdate` (title, seo{title, description}, descriptionHtml), med variabler ur skriptutskrift (`ensure_ascii=True`). Inga userErrors.
- Seo.title lagras som null när den är lika med titeln. Det är avsett enligt standarden och påverkar inte metabeskrivningen.
- Taggen "texter-klara" lades till sist med `tagsAdd` på alla 25. Inga userErrors. Befintliga taggar finns kvar.

## Verifiering
- Maskinellt (python, tecken för tecken): titel, handle, status, seo.title, seo.description, descriptionHtml och tags för alla 25. Resultat: inga avvikelser, inga osynliga tecken i återläsningen.
- Begränsning: live-data går via min kopiering till filer, så jämförelsen är lika bra som kopieringen av svaren. En felkopiering som råkar bli identisk med skrivfilen skulle inte synas. Avvikelser hade däremot synts.

## Ändrat
- Shopify: ja. 25 produkter (title, seo, descriptionHtml) och taggen "texter-klara" lades till. Handle, status, pris och övriga taggar är oförändrade.
- Filer: `rapporter/shopify-original-2026-11-03/vag2b_15_fore.json` (ny), `rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2b15/` (ny, kopia och kontroll), denna rapport (ny). Inga befintliga filer ändrade, ingen commit.
