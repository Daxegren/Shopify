# Våg 2k 3a: skrivrapport

Datum: 2026-11-03. Butik: BEST OF SPORTS (bestofsports.se), verifierad med get-shop-info.
Skrivfil: rapporter/facit-bos-2026-10-31/vag2_skriv/k_skriv_3a.json (28 cyklar, rättad 2026-11-03: Kona Fire Mountain 10476262064394 utan däckbredd).
Före-läge: rapporter/shopify-original-2026-11-03/vag2k_3a_fore.json (28 produkter, sparat före skrivning).
Kontrollkopia: rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2k3a/kopia.json.

## Före skrivning
- 28 av 28 ACTIVE. Ingen hade taggen texter-klara. Ingen var redan skriven (titlarna var de engelska originalen).
- seo.title och seo.description var null på alla 28.

## Kontroll på kopia (kontrollera_produkttext.py, --seo-title-max 43, --seo-suffix " – BEST OF SPORTS")
- Första körningen: 1 FEL (10476262064394, "2.25" i beskrivningen, källan trasig). Skrivningen avbröts. Inget skrevs.
- Efter rättningen i skrivfilen: 0 FEL, 40 VARNINGAR.
- Varningarna är kända och godtagna: rubriken "Passar för" (27 st), engelska färgord "Black"/"White" (3 st) och 3 kommatecken i titeln på 10472248934666 (decimalkomma i 27,5).

## Skrivning (Shopify productUpdate, ingen alias-fel)
- Batcher: kanarie 3 (7005, 7006, 7007), sedan 6, 6, 6, 6 och 1. Största mutationsdokument 14 165 tecken (under 16 384).
- Mutationstexterna genererades av python (bygg_batcher.py) och klistrades in ordagrant.
- Seo skickades med både title och description. Två specialfall: 10472237072650 saknar meta (skickades med seo.title), 10475423629578 har seo.title lika med titeln (Shopify lagrar null, avsett).
- Inga userErrors i någon batch.

## Återläsning och jämförelse
- Efter varje batch lästes title, handle, status, tags, seo.title, seo.description och descriptionHtml tillbaka.
- Jämförelsen gjordes maskinellt i python (jamfor.py) mot skrivfilen och före-läget, tecken för tecken. Resultat: 28 av 28 produkter, 0 avvikelser.
- Handle, status och befintliga taggar kontrollerades också maskinellt mot före-läget: oförändrade.
- Stickprov manuellt: inget, alla 28 är lästa.

## Tagg
- tagsAdd texter-klara sattes sist, på alla 28, efter att alla fält verifierats. Inga userErrors.
- Återläsning av taggar: alla 28 har texter-klara. De befintliga taggarna finns kvar (kontrollerat för hand, inte i python).

## Avvikelser
- Ingen avvikelse vid skrivning eller återläsning.
- Ett FEL i första kontrollen (10476262064394) löstes genom rättning i skrivfilen, inte i Shopify.

## Hoppade över
- Inga.

## Ändrat i Shopify
- Ja: title, seo.title, seo.description och descriptionHtml på 28 produkter, plus taggen texter-klara på samma 28. Inget annat (pris, lager, status, handle, bilder) ändrades.
