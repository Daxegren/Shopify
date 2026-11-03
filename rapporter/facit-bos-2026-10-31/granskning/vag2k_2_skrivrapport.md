# Våg 2k-2 (cyklar och cykeldelar): skrivrapport

Datum: 2026-11-03. Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_skriv_2.json` (34 produkter). Före-läge: `rapporter/shopify-original-2026-11-03/vag2k_2_fore.json`.

## Status: AVBRUTEN före skrivning

Ingen produkt skrevs i Shopify. Inga taggar lades till. Skrivningen avbröts enligt regeln "avbryt vid riktiga fel" i kontrollsteget.

## Butik

Shopify-butiken är BEST OF SPORTS (bestofsports.se). Kontrollerad med get-shop-info.

## Steg 1: live-läge

- Alla 34 produkter hittades och är ACTIVE. Ingen hoppades över.
- Ingen produkt har taggen "texter-klara".
- Ingen live-titel är lika med skrivfilens titel. Alla 34 har leverantörens originaltitel.
- Alla 34 har `seo.title = null` och `seo.description = null` live.
- Före-läget (titel, handle, status, taggar, seo, descriptionHtml) sparades i `rapporter/shopify-original-2026-11-03/vag2k_2_fore.json`. Filen är kontrollerad att den är giltig JSON med 34 poster, samma id-ordning som skrivfilen och alla ACTIVE. Innehållet är överfört för hand från läsningen. Den är inte maskinellt jämförd mot svaret från Shopify.

## Steg 2: kontroll på kopia

Kopia: `rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2k2/kopia.json`. Html är mappad till beskrivning. Standardblocket (från `<h2>Leverans, retur och garanti</h2>` till slutet) är markerat med `[[STANDARDBLOCK]]`. Källtext för `fakta` är före-läget (titel och descriptionHtml utan taggar). Körning: `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS"`.

Resultat: 34 produkter, 2 FEL, 37 VARNINGAR.

**Riktigt FEL (avbrott):**

- `10572695503114` (Hopfällbar Cykel Romet Jubilat ECO, Svart, nr 6147). Texten nämner "24-tumshjul" i meta och i beskrivningen. Källan för just den här produkten (före-läget) anger bara "Rammstorlek: 15\"" och ingen hjulstorlek. Siffran 24 finns i källan för systerprodukten 10548235239690 (blå), inte för den svarta. Kontrollen flaggar talet som ett påstående utan stöd i källan.
- Rättning krävs före skrivning. Rekommendation: ta bort "24-tumshjul" i meta och i beskrivningen, eller bekräfta att 24 tum gäller även svarta modellen. Det är en ändring i skrivfilen, och skrivfilen är inte ändrad av mig.

**VARNINGAR (godtagna enligt instruktionen):**

- "saknar avsnittet 'passar dig som'". Rubriken heter "Passar för". Känd och godtagen varning.
- Kort beskrivning på `10515736723722`, `10472238612746` och `10472287535370` (13, 13 och 27 ord). Källtexten är tunn, och texten är bara intro och specifikation. Ingen påhittad text. Godtagen som varning.

Övriga 31 produkter gav inga FEL.

## Steg 3–5: skrivning, återläsning och taggen "texter-klara"

Ej utförda. Kanarie (3 produkter) och resten skrevs inte, eftersom kontrollen gav ett riktigt fel.

## Avvikelser

- Ingen skrivning i Shopify. Butiken är oförändrad.
- Kopian `tmp_kopia_vag2k2/kopia.json` är ett arbetsunderlag. Den innehåller bara text, inte skrivfilen.

## Nästa steg

1. Rätta `10572695503114` i skrivfilen (ta bort "24-tumshjul" eller bekräfta måttet med källa). Kör kontrollen om på kopian.
2. Kör sedan skrivningen: kanarie om tre, återläsning av alla fält och jämförelse mot skrivfilen, därefter taggen "texter-klara".
