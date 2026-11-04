# Skrivrapport våg 2b, skrivfil 21 och 22 (Best of Sports, Velomarket: elcyklar och cyklar)

Datum: 2026-11-04. Butik: BEST OF SPORTS (bestofsports.se), verifierad med get-shop-info.
Ingen commit gjord (enligt skrivprompt).

## Fil 21 (24 produkter, nr 8915–8942)

- Före-läge: `rapporter/shopify-original-2026-11-03/vag2b_21_fore.json` (24 produkter, sparat från live-läsning innan skrivning). Alla ACTIVE, ingen hade taggen "texter-klara", ingen hade titel lika med skrivfilen, seo var null.
- Hoppade över: inga.
- Kontrollskript (kopia, `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70`, källtext = före-läget): 0 FEL, 40 VARNINGAR. Varningarna är kända och godtagna: "passar dig som" (rubriken heter "Passar för") och engelska färgord (Green, Black, White) som kommer från källan.
- Skrivning: kanarie 3, sedan batcher om 5, 5, 5, 5, 1. Alla productUpdate utan userErrors.
- Återläsning: alla 24 jämförda tecken för tecken mot skrivfilen (titel, handle/status, seo.title, seo.description, descriptionHtml) med python. 0 avvikelser. Seo.title är null där SEO-titeln är lika med titeln (avsett).
- Taggen "texter-klara" lagd på alla 24 efter verifiering. Befintliga taggar kontrollerade mot före-läget: alla kvar.

## Fil 22 (13 produkter, nr 8948–8970)

- Före-läge: `rapporter/shopify-original-2026-11-03/vag2b_22_fore.json` (13 produkter). Obs: inte en maskinell dump. Live-svaret klistrades in i filer och sammanfogades med python. Titel, status och taggar stämmer mot live-svaret, men texten är en inklistring och bör ses som mindre säker än fil 21:s före-läge.
- Hoppade över: inga.
- Kontrollskript: 0 FEL, 13 VARNINGAR (samma kända "passar dig som").
- Skrivning: kanarie 3, sedan batcher om 5 och 5. Inga userErrors.
- Återläsning: alla 13 jämförda tecken för tecken mot skrivfilen. 0 avvikelser.
- Live-kontroll före taggning: titlar och metabeskrivningar stämde för alla 13. Taggen "texter-klara" lagd på alla 13. Befintliga taggar kontrollerade: alla kvar.

## Noterat till David (ej ändrat)

- Produkt 8928 (Bottecchia BE20 Richmond, Blå Blank): "Ingår" i skrivfilen nämner pakethållare två gånger ("Främre pakethållare, ..., pakethållare"). Texten är skriven som den står i skrivfilen. Ingen ändring gjord för hand.
- Engelska färgord i titlar och text (Green, Black, White) är källans färgnamn och kvarstår.

## Ändrat i Shopify

Ja. productUpdate (title, seo, descriptionHtml) för 37 produkter och tagsAdd "texter-klara" för 37 produkter. Handle, status, pris och övriga taggar är inte ändrade.

## Lokala filer

- `rapporter/shopify-original-2026-11-03/vag2b_21_fore.json`
- `rapporter/shopify-original-2026-11-03/vag2b_22_fore.json`
- `rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2b21/kopia.json`
- `rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2b22/kopia.json`
