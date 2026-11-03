# Våg 2b, grupp 6 (Velomarket-tillbehör): skrivrapport

Datum: 2026-11-03. Butik: BEST OF SPORTS (bestofsports.se), verifierad med get-shop-info. Skrivfil: `vag2_skriv/b_skriv_6.json` (40 produkter). Före-läge: `rapporter/shopify-original-2026-11-03/vag2b_6_fore.json`. Ingen commit.

## Före och efter
- Live-läge före skrivning: 40 av 40 ACTIVE, ingen med taggen `texter-klara`, ingen med titel lika med skrivfilen. Inga hoppades över.
- Efter skrivning: 40 av 40 skrivna (kanarie 3, sedan batcher om 8, 8, 8, 8 och 5), ingen användarfel i productUpdate.
- Tagg `texter-klara` lagd på alla 40 sist. Befintliga taggar kvar (kontrollerat för hand mot före-läget).

## Kontroll före skrivning
- `kontrollera_produkttext.py` på kopia i `granskning/tmp_kopia_vag2b6/` (html mappad till beskrivning, standardblocket inom `[[STANDARDBLOCK]]`, `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS"`, källtext = före-läget): **0 FEL, 52 VARNINGAR**. Varningarna är "passar dig som" (rubriken heter "Passar för", godkänt), korta beskrivningar under 40 ord (fem produkter) och engelska ordet "Red" i produktnamnet "Dryckesflaska Elite Vintage Red" (färgnamn, ej ändrat).

## Återläsning och jämförelse
- Efter varje batch lästs title, handle, status, tags, seo.title, seo.description och descriptionHtml tillbaka.
- Jämförelsen mot skrivfilen (titel, SEO-titel där Shopify lagrar null när den är lika med titeln, metabeskrivning, html, handle, status, taggar) gjordes maskinellt i python: 0 avvikelser i alla sex batcher.
- Ett begränsat förbehåll: återläsningen klistrades in av mig från MCP-svaret till en fil, och python jämförde filen. Själva MCP-svaret går inte att skicka till bash. Felaktig inklistring hade gett avvikelse, inte tyst godkännande.
- Ingen avvikelse i descriptionHtml: Shopify lade inte till radbrytningar mellan `<li>`.

## Metabeskrivning vid SEO-titel lika med titel
- Fem produkter har SEO-titel lika med titeln och en metabeskrivning: nr 8118, 8135, 8138, 8147, 8155. Skriptet skickade först inte `seo` för dessa, vilket skulle ha tappat metabeskrivningen. Rättat före batch 0 (`bygg_mutation.py`): `seo{title: titel, description: meta}`. Shopify lagrar titeln som null, metan sparas. Alla fem återlästa med metabeskrivning kvar. Ingen omskrivning behövdes.
- Två produkter (8136, 8157) har SEO-titel lika med titeln och ingen meta. De skickades utan `seo`, enligt regeln. Live-SEO-titel är null där.

## Hoppade över
- Inga.

## Avvikelser
- Ingen avvikelse i skrivningen eller återläsningen.
- Taggen `texter-klara` lades bara efter att alla 40 var verifierade.
- Process: productUpdate tar ett produkt-id per anrop, så en batch är ett dokument med åtta alias (`p1`–`p8`) och ett anrop per dokument. Dokumenten är under 16 384 tecken.

## Ändrat
- Shopify: ja. productUpdate (title, seo, descriptionHtml) på 40 produkter, tagsAdd `texter-klara` på 40 produkter. Handle, status och pris ändrades inte.
- Filer: nya filer i `rapporter/shopify-original-2026-11-03/vag2b_6_fore.json` och `rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2b6/` (kopia, mutationer, återläsningar, jämförelse). Ingen befintlig fil ändrad.
