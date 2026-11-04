# Våg 2b, grupp 23 (sparkcyklar, hjul och tillbehör): skrivrapport

Butik: BEST OF SPORTS (bestofsports.se, Shopify Basic, SEK). Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/b_skriv_23.json` (45 produkter). Före-läge: `rapporter/shopify-original-2026-11-03/vag2b_23_fore.json`.

## Före och efter
- Före: alla 45 ACTIVE, ingen `seo` satt (title och description null), ingen tagg `texter-klara`, gamla titlar.
- Efter: alla 45 skrivna med `productUpdate` (title, seo{title, description}, descriptionHtml). Alla 45 har taggen `texter-klara` (tagsAdd, sist).
- Hoppade över: 0 (ingen produkt hade redan titeln från filen eller taggen).

## Kontroll före skrivning
- `kontrollera_produkttext.py` på kopia (html som beskrivning, standardblock markerat, `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70`, källtext = före-läget): 16 FEL och 49 VARNINGAR.
- Alla 16 FEL är `tal_utan_kalla` och kontrollerade mot källan: 4 gånger "2" i "V2" (modellnamn, Ethic Incube V2), 2 gånger "180" (0.18 kg i källan), och 10 gånger vikt i gram där källan anger kg eller decimalkomma (0.220/0.223/0.270 kg, 0,223 kg = 220/223/270 g). Inga riktiga fel. Skriptet räknar inte om enheter.
- VARNINGAR: "passar dig som" (avsiktligt, rubriken heter "Passar för") och "Blue" i en produkttitel (färgnamn ur källan).

## Skrivning och återläsning
- Kanarie 3 produkter, sedan batcher om 5 (sista batch 2). Varje mutation skrevs ut av skriptet och klistrades in ordagrant.
- Varje batch lästes tillbaka (4 + 1 produkter per läsning) och jämfördes maskinellt mot skrivfilen och före-läget: titel, handle, status, seo.title (null när den är lika med titeln), seo.description, descriptionHtml tecken för tecken, osynliga tecken, bevarade taggar. Resultat: 0 avvikelser i alla 9 batchar.
- Ingen handskriven rättning gjordes. Inga fel från Shopify (userErrors tomma).

## Så kontrollerades
- Maskinellt: återläst JSON jämfört i python mot skrivfilen. Det maskinella jämförelsen gäller det som klistrats in i python, inte en separat hämtning.
- Handle och status: bekräftat maskinellt mot före-läget (oförändrade).
- Taggar: svaret från tagsAdd visar de befintliga taggarna kvar. Ingen maskinell jämförelse mot före-läget gjordes för taggerna efter tagsAdd, endast visuell kontroll av svaret.

## Att notera
- Före-filen (`vag2b_23_fore.json`) skapades av mig genom att återskriva live-svaren från Shopify-läsningen i filer. Den är inte en rå kopia av svaret från tjänsten. Den bör jämföras mot en ny läsning av före-läget innan den används för återställning.
- Ingen produkt ändrades i Shopify utöver productUpdate (titel, seo, beskrivning) och tagsAdd (`texter-klara`).
- Inget committat.

## Ändrat
- Shopify: ja. 45 produkter fick titel, seo och beskrivning, och taggen `texter-klara`.
- Filer: `rapporter/shopify-original-2026-11-03/vag2b_23_fore.json` (ny), `rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2b23/` (kontrollkopia och kontrollutskrift, ny).
- Denna rapport: `rapporter/facit-bos-2026-10-31/granskning/vag2b_23_skrivrapport.md` (ny).
