# Skrivrapport våg 2, cyklar (k_skriv_3b), 2026-11-03

## Före/efter
- Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_skriv_3b.json`, 27 produkter (nr 7091–7167).
- Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info (plan Basic, SEK).
- Före-läge (live, innan skrivning): `rapporter/shopify-original-2026-11-03/vag2k_3b_fore.json`. Alla 27 var ACTIVE, ingen hade taggen `texter-klara`, ingen var redan skriven (titel var lika med leverantörens original).
- Efter: alla 27 har ny titel, SEO-titel, SEO-metabeskrivning och beskrivning enligt skrivfilen. Handle, status och pris är oförändrade. Taggen `texter-klara` är satt på alla 27. Befintliga taggar finns kvar på alla 27.

## Kontroll före skrivning
- `shopify-sync/scripts/kontrollera_produkttext.py` kördes på kopia (`granskning/tmp_kopia_vag2k3b/kopia.json`): html mappad till beskrivning, standardblocket (leverans, retur, garanti) inom `[[STANDARDBLOCK]]`, `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS"`, källtext = före-läget.
- Resultat: 0 FEL, 50 VARNINGAR. Varningarna är:
  - 27 st "saknar avsnittet 'passar dig som'": avsiktligt, rubriken heter "Passar för".
  - 21 st engelska färgord (Blue, Yellow, White, Grey, Green): alla finns i källan, maskinellt kontrollerat.
  - 2 st kommatecken i mått (decimalkomma i "Liv Tempt 3 XS, 27,5 tum" och "Giant Talon 3" m.fl.): känt beteende i skriptet.

## Skrivning och kontroll
- Mutation: `productUpdate`, sex produkter per anrop (kanarie: tre produkter först). Texterna togs ur skrivfilen med ett python-skript (`scratchpad/s3b/bygg.py`), som skrev ut variablerna; utskriften kopierades in i anropet.
- Efter varje batch lästes alla fält tillbaka (title, handle, status, seo.title, seo.description, descriptionHtml, tags). Jämförelsen gjordes maskinellt i python mot skrivfilen och före-filen (`scratchpad/s3b/jamfor.py`). Ingen avvikelse i någon batch. Inga userErrors.
- Slutkontroll: alla 27 lästes tillbaka i en fråga och jämfördes maskinellt (`scratchpad/s3b/slutkontroll.py`): 27 av 27 utan avvikelse, taggen finns på alla, befintliga taggar finns kvar.
- Teckenlängder för beskrivningens html stämmer exakt mot skrivfilen för alla 27.
- Shopify ändrar seo.description och descriptionHtml exakt som skickats (ingen radbrytning mellan li-taggar förändrades i detta fall).

## Avvikelser från instruktionen
- Den första live-läsningen gjordes i ett anrop för alla 27 i stället för i grupper om 25. Svaret blev för stort för direktvisning och sparades som fil; datan lästes maskinellt.
- Batchernas readback kopierades till JSON-filer för jämförelse (kopieringssteget är därmed mänskligt); jämförelsen i sig är maskinell, och varje fel i kopieringen hade syns som avvikelse. Inga avvikelser uppstod.

## Hoppat över
- Inga produkter. Ingen av de 27 hade status annat än ACTIVE, taggen eller skriven titel.

## Ändrat
- Shopify (BEST OF SPORTS): titel, SEO-titel, SEO-metabeskrivning, beskrivning och taggen `texter-klara` på 27 produkter.
- Filer: `vag2k_3b_fore.json` (ny), `tmp_kopia_vag2k3b/kopia.json` (ny), denna rapport (ny). Inga andra filer ändrade. Inget committat.
