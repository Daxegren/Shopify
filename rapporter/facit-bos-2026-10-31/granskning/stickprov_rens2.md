# Stickprov rens2 (k_skriv_rens2.json, 178 produkter), 2026-11-04

Roll: Stickprovare, endast läsning. Inget skrevs till Shopify.

## Urval och metod
- 40 av 178 produkter (22 procent), `random.seed(1)`, `random.sample(skrivfil, 40)`.
- Hämtade live med `shopify_api.hamta_produkter` (4 per anrop, 10 anrop).
- Jämförde tecken för tecken: titel, seo.title (null i Shopify räknat som titeln), seo.description mot `meta`, descriptionHtml mot `html`.
- Kontrollerade att taggen `texter-klara` finns, och att handle, status och tagglista är lika som i `rapporter/shopify-original-2026-11-04/k_skriv_rens2_fore_*.json` (dry-run, 178 poster, är grund; kanarie och rest ger samma poster).

## Resultat
- Avvikelser live mot skrivfil: 0 av 40 (titel, seo.title, meta, html).
- Tagg `texter-klara` saknas: 0. Handle ändrad: 0. Status ändrad: 0 (alla ACTIVE). Tagglista ändrad: 0.
- Alla 40 hittades. Alla har updatedAt 2026-11-04 17:48 till 17:53, alltså skrivna i utrullningen.
- Fler än 2 "enligt tillverkaren": 0 av 178. Fördelning: 127 produkter har 1 och 51 har 2 (max är 2). Eftersom inga har fler än 2 gjordes språkgranskningen på 10 slumpade (seed 1) av de 51 med 2.

## Kontroll av själva ändringen (alla 178, skrivfil mot före-fil)
- Radantalet i descriptionHtml är lika före och efter i alla 178. Varje rad som skiljer sig är exakt före-raden plus " (enligt tillverkaren)". Inga andra ändringar. Titel och meta är oförändrade mot före i alla 178.
- Tillägget finns på 136 rader "Maximal användarvikt", 35 "Lastkapacitet", 3 "Maximal belastning", 3 "Maxlast" och 1 "Maxvikt". Inga lastgränsrader saknar tillägget (enda träffen, "Maximal effekt: 1500 W" i nr 10077, är effekt och ska inte ha det).
- De 51 produkterna med 2 hade redan 1 i före-filen (räckviddsrad eller liknande), så andra förekomsten är inte ny.

## Språkgranskning (10 produkter med 2 förekomster)
Nr 8802, 8918, 10049, 8793, 8806, 8800, 8884, 8878, 8883, 10029.
- Stavning och meningsbyggnad: inga fel. Tillägget står på rätt rad (lastgränsen) och i samma form överallt: "NNN kg (enligt tillverkaren)".
- Inget dubblerat tillägg, inga dubbla mellanslag, ingen trasig HTML.
- Notering, inte fel i denna ändring (fanns redan före): löpbanden 10049 och 10029 har en "Passar för"-rad som slutar ", enligt tillverkaren" (t.ex. "Dig som vill använda apparna Kinomap och Zwift via Bluetooth, enligt tillverkaren"). Det är grammatiskt korrekt men stilistiskt tungt, och 10049 hänför "enligt tillverkaren" till ett dämpningssystem. Påverkar inte rens2. Samma mönster finns i totalt ca 8 rader.

## Begränsningar
- 40 av 178 kontrollerades live. De övriga 138 är kontrollerade bara skrivfil mot före-fil, inte mot live.
- Liveläget kan ha ändrats efter 17:53 av andra processer; jämförelsen gäller läget vid körningen.
- Bilder, varianter, priser och metafält utanför de jämförda fälten ingår inte.
