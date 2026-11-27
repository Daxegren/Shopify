# Förslag: SEO-titlar för jackkollektioner (Workout Brands), 2026-11-27

Ej skrivet i Shopify; väntar på Davids ja. Sju kollektioner utan SEO-titel. Titlar utan butiksnamn. Metabeskrivning föreslås bara där den saknas (kamouflage-jackor-herr och brandit-vinterjacka-herr har redan en och behåller den). Märken och jacktyper ur kollektionernas bäst säljande produkter (vendor-fältet). "Dunjacka" i kollektionsnamnet kvarstår men produkterna är puffer-jackor och västar; titeln påstår därför inte dunfyllning.

Se `forslag.csv`.

## Inte med (och varför)
- **Dubbletter, väntar på strukturbeslut:** `jackor-herr`, `jacka-herr`, `jackor-herr-dam`, `jackor-dam`, `jacka-dam`, `vinterklader-herr`, `vinterklader-herr-1`, `vinterklader-herr-dam` och `vinterklader-dam`.
- **För få köpbara produkter:** `parkasjackor-herr` (10 varav cirka 5 köpbara; har meta, saknar titel), `lader-konstlader-jacka-kvinna` (4), `brandit-vinterjacka-dam` (5), `brandit-britannia-jacket-herr-dam-1` (5).
- **Barn:** `jacka-pojke`, `jacka-flicka`: ej granskade här.
- **Homepage-kollektionerna** (`vinterjacka-herr-homepage`, `vintertillbehor-homepage`): tekniska, rörs inte.

## Skrivet 2026-11-27 (efter Davids ja)
Alla sju skrivna: `var-jacka-herr` först som kanarie, därefter övriga sex i ett anrop. Återläst: titel och metabeskrivning exakt som i `forslag.csv`; `kamouflage-jackor-herr` och `brandit-vinterjacka-herr` behöll sina befintliga metabeskrivningar oförändrade. Före-läge: `fore_seo.json`. Ångra: sätt seo.title (och där den saknades före, seo.description) till null.
