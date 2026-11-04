# Skrivrapport f_10 (Tunturi/Toorx skivstänger och tillbehör), 2026-11-04

- Butik: BEST OF SPORTS (bestofsports.se), bekräftat med get-shop-info före skrivning.
- Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/f_skriv_10.json` (23 produkter; 10232 och 10237 avvisade och saknas; a_2 nr 2203 skrevs inte, samma produkt som 10246).
- Före-läge: `rapporter/shopify-original-2026-11-04/f_10_fore.json` (23 av 23, kompletta texter, alla ACTIVE, ingen hade taggen texter-klara, ingen titel lika med skrivfilens, så ingen hoppades över).

## Kontroll före skrivning
`kontrollera_produkttext.py` på kopia (html till beskrivning, standardblock markerat, --seo-title-max 43 --seo-suffix " – BEST OF SPORTS"): 14 FEL, alla `meta_langd` (kort sann meta, beslutad 2026-11-03), 26 VARNINGAR (saknar "passar dig som" = känd rubrik "Passar för"; 3 med fler än 3 meningar i första stycket; 10239 36 ord). Inga andra fel.

## Skrivning
- Kanarie 3 (10226, 10227, 10228), därefter batcher om 5 (högst 5 per anrop). Alla mutationer skrevs ut av skript (`json.dumps(ensure_ascii=True)`) och klistrades in; seo skickades alltid med title och description. Alla userErrors tomma.
- Avvikelse: i batchen 10246–10250 klistrades 10250 in med fel (saknade raderna Märke, Retur och Reklamation). Upptäcktes vid egen genomläsning före återläsning; 10250 skrevs om med ny skriptutskrift och verifierades. Den felaktiga versionen låg i Shopify en kort stund.
- Återläsning (högst 4 åt gången, 6 anrop, alla 23) jämförd i python tecken för tecken mot skrivfilen: title, handle (oförändrad mot före), status (ACTIVE), seo.title (null tolkas som titeln), seo.description, descriptionHtml, samt kontroll av osynliga tecken (Cf, Zs, Cc). Resultat: 0 avvikelser på alla 23. Maskinellt: samtliga fält. För hand: bara att rätt produkter ingår och tagglistorna (se nedan).
- "På beställning": taggen finns på 10233, 10239, 10240, 10244 (och endast dessa) och bara dessa har leveranstidsmeningen "Beställningsvaror kan ta upp till en vecka längre".
- Pris, handle och status ändrades inte.

## Taggar
`tagsAdd texter-klara` på alla 23 (inga userErrors). Tagglistorna lästes tillbaka och jämfördes för hand mot före-läget: alla befintliga taggar finns kvar (inklusive Velomarket), enda ändringen är texter-klara.

## Hoppade över
Inga.
