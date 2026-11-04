# Skrivrapport f_5 (Velomarket, motionscyklar), 2026-11-04

Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/f_skriv_5.json` (25 produkter). Före-läge: `rapporter/shopify-original-2026-11-04/f_5_fore.json` (de 23 som skrevs). Butik bekräftad: BEST OF SPORTS (bestofsports.se).

## Hoppade över (2)
- 10411848532234 (nr 10103, Hammer Speed Race SR) och 10541370114314 (nr 10110, Toorx BRX 65 Comfort): live-titeln var redan lika med skrivfilens (pilotprodukter, redan skrivna). Inget ändrat. Ingen tagg lades på dem.

## Kontroll före skrivning
`kontrollera_produkttext.py` på kopia (`--seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70`): 23 produkter, 0 FEL, 24 VARNINGAR (23 x rubriken "passar dig som" saknas, avsiktligt; 1 x 10472220197130 kort beskrivning, 34 ord, tunn källa). Med standardgränsen 130–155 för meta gav 18 produkter meta_langd-fel; gäller kort meta enligt standard §14 (min 70).
'På beställning'-kontroll: de 9 skrivna produkterna med taggen har leveranstidsmeningen, de 14 utan taggen saknar den (maskinellt kontrollerat före skrivning).

## Skrivning
Kanarie 3 + batcher om 5 (3+5+5+5+5 = 23), alla via `productUpdate(product:)` med seo{title, description} och variabler utskrivna av skript (`json.dumps(..., ensure_ascii=True)`) och inklistrade ordagrant. 0 userErrors. Handle, status och pris orörda.

## Återläsning (maskinellt i python, tecken för tecken)
Alla 23 återlästa (högst 4 per fråga) och jämförda mot skrivfilen: title, seo.title (null tolkat som lika med titeln, 10108), seo.description, descriptionHtml, handle (mot före), status ACTIVE, taggar oförändrade, samt kontroll av osynliga tecken (Cf/Cc/nbsp) och dubbla mellanslag. Resultat: 0 avvikelser, ingen omskrivning behövdes. Inget jämfördes för hand.

## Taggar
`tagsAdd texter-klara` på de 23. Återläst: varje produkt har exakt sina tidigare taggar plus texter-klara (0 avvikelser); Velomarket-taggen och 'På beställning' orörda.

## Anmärkningar
- FORE_FIL är överförd till fil genom inklistring av live-läsningen (ingen API-väg från sandlådan), inte exportad maskinellt; den användes bara som referens för handle och taggar.
- Ingenting committat.
