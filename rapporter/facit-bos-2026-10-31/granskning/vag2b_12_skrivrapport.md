# Skrivrapport våg 2b, grupp 12 (24 pakethållare, bagagebärare och fästen) – AVBRUTEN

Butik: BEST OF SPORTS (bestofsports.se), verifierad med get-shop-info.
Skrivfil: rapporter/facit-bos-2026-10-31/vag2_skriv/b_skriv_12.json (24 produkter).
Före-läge: rapporter/shopify-original-2026-11-03/vag2b_12_fore.json (24 produkter, alla ACTIVE, ingen med taggen texter-klara, ingen med titel lika skrivfilen).

## Status
- Skrivningen avbröts efter batch 2 på grund av avvikelser. Batch 3 (8617–8622) och batch 4 (8623–8625) är inte skrivna.
- Taggen "texter-klara" är inte satt på någon produkt.

## Avvikelser (ska rättas av David-beslut, inte handskrivet)
Mina handskrivna variabler i batch 2 avvek från skrivfilen. Felen fångades vid jämförelse mot skrivfilen i python. Shopify har följande fel nu:
- 10494698488074 (nr 8613): titel "Frambagebärare Giant Rackit Metro Front" i stället för "Frambagagebärare Giant Rackit Metro Front". Metabeskrivningen har "frambagebärare" i stället för "frambagagebärare".
- 10494699438346 (nr 8614): titel "Frambagebärare Basil Front Carrier L, 40 x 28 x 96 cm" i stället för "Frambagagebärare ...". SEO-titeln "Frambagebärare Basil Front Carrier L" i stället för "Frambagagebärare Basil Front Carrier L". Metabeskrivningen har samma fel.
- 10507287265546 (nr 8616): titel "Frontbagebärare Basil Front Carrier L, Svart" i stället för "Frontbärare Basil Front Carrier L, Svart". Metabeskrivningen har "frontbagebärare" i stället för "frontbärare".
- Beskrivningen (descriptionHtml) för batch 2 är inte återläst och jämförd. Den kan innehålla fler fel.

Batch 1 och kanariebatchen (8601–8607 och 8609, 9 produkter) är verifierade: titel, status, SEO-titel, metabeskrivning och beskrivning matchar skrivfilen tecken för tecken.

## Vad som är kontrollerat
- Kontrollskriptet (kopia med html mappad till beskrivning, standardblock markerat, --seo-title-max 43, --seo-suffix " – BEST OF SPORTS", --meta-min 70) på 24 produkter: 0 FEL, 28 VARNINGAR. Varningarna är de godtagna ("passar dig som"-rubriken) och tre korta beskrivningar.
- Kopian ligger i rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2b12/kopia_vag2b12.json.
- Återläsning och jämförelse är gjord mot mina egna kopior av Shopifys svar, inte mot en maskinell export. Jämförelsen är därför bara så bra som kopian.

## Vad som ändrats i Shopify
- Batch kanarie (8601, 8602, 8603) och batch 1 (8604, 8605, 8606, 8607, 8609, 8610): titel, SEO-titel, metabeskrivning och beskrivning ändrade via productUpdate.
- Batch 2 (8611–8616): titel, SEO och beskrivning ändrade. Tre produkter har fel enligt ovan.
- Handle, status, pris och andra taggar är oförändrade enligt återläsningen.

## Nästa steg (kräver ett besked från David)
1. Rätta 8613, 8614 och 8616 med ett skriptgenererat productUpdate från skrivfilen, inte med handskrivna variabler.
2. Läs tillbaka beskrivningen för batch 2 (8611–8616).
3. Skriv batch 3 och 4 med skriptutskrift, med återläsning efter varje batch.
4. Sätt taggen texter-klara först när allt är verifierat.

Lärdom: LARDOMAR.md har fått en ny post.
