# Skrivrapport vag2k_1 (Velomarket, Best of Sports)

Status: **klar 2026-11-03.** Alla 90 produkter skrivna, återlästa och taggade "texter-klara".

## Underlag
- Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_skriv_1.json` (90 produkter, sanningen enligt David).
- Före-läge (sparat före första skrivning): `rapporter/shopify-original-2026-11-03/vag2k_1_fore.json` (90 poster: id, title, handle, status, tags, seo, descriptionHtml).
- Butik: BEST OF SPORTS (bestofsports.se), verifierad med get-shop-info.

## Före-läge och urval
- Alla 90 produkter ACTIVE. Ingen hade taggen "texter-klara" eller skrivfilens titel före skrivning. Hoppade över: 0.
- Live-id-mängden identisk med skrivfilens (90 unika id).

## Kontroll på kopia (kontrollera_produkttext.py)
- Kopia: html som beskrivning, standardblocket mellan [[STANDARDBLOCK]] och [[/STANDARDBLOCK]] (alla 90 har rubriken "Leverans, retur och garanti"), fakta = före-läget som ren text, `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS"`.
- Första körningen: 2 FEL, båda nr 6075 (`tal_utan_kalla`, 2.4). Källan skriver "29x2 .4" med mellanslag, så talet finns i källan. Felet rättades i kontrollkopian, inte i skrivfilen.
- Efter rättningen: **0 FEL**, 103 VARNINGAR, alla godtagna enligt instruktionen eller kända:
  - 90 `struktur` (skrivfilen använder "Passar för", inte "Passar dig som").
  - 12 `engelska_ord` (färgnamnen Tiger Red 6056, Gunmetal Black 6071, Abyss Black 6054; tillverkarens namn, lämnas kvar).
  - 1 `titel_kommatecken` (10468709138698, 3 kommatecken; decimalkomma i mått, godtaget).

## Skrivning
- `productUpdate(product: {...})` med id, title, seo{title, description} och descriptionHtml. Max 6 produkter per mutation. Handle och status ändrades inte.
- Textinnehållet kopierades från utskrifter av skrivfilen (script `mut.py` i scratchpad, utskriften klistrades in ordagrant).
- **Avvikelse 6032 (id 10530156347658), rättad:** under första batchen skrevs en egen metabeskrivning i stället för skrivfilens. Rättades enligt David 2026-11-03 med skrivfilens värde. Återläst: OK.

## Återläsning och taggar
- Återläsning av alla 90 produkter via Shopify-API, sparad till fil, jämförd i Python exakt mot skrivfilen och före-läget. Fält: title, handle, status, seo.title, seo.description, descriptionHtml (exakt strängjämförelse), tags (före-taggar kvar), "texter-klara" finns.
- Resultat: **alla 90 OK**, 0 avvikelser i sista läsningen.
- Taggen "texter-klara" satt via `tagsAdd` på alla 90 produkter (21 först, 69 efter batchavstämning). Befintliga taggar finns kvar (kontrollerat i jämförelsen).
- Maskinell kontroll: all jämförelse är Python-strängar. Ingen manuell jämförelse används i slutresultatet.

## Ändrat
- Shopify: productUpdate på 90 produkter (title, seo, descriptionHtml); tagsAdd "texter-klara" på 90 produkter. Inget annat fält ändrat.
- Filer: `vag2k_1_fore.json` (ny), denna rapport (ny).
- Inga commits.

## Att notera
- Inline-läsningar av Shopify blev för stora för att spara; jag tvingade sparade utdata genom att upprepa alias i frågan. Det påverkar inte resultatet men är ett omständligt arbetssätt.
