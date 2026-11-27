# Förslag: SEO-titel och metabeskrivning för vinterjackorna (Workout Brands), 2026-11-27

Bara SEO-titel och metabeskrivning på tre kollektioner. Beskrivningstexter, produkter, taggar och priser rörs inte. Ej skrivet i Shopify; väntar på Davids ja. Titlarna slutar inte med butiksnamn (beslut 2026-11-18). Före-läge: båda fälten saknas på alla tre.

Se `forslag.csv` (med teckenantal) och `skrivplan.json`.

## Fynd som inte ingår i förslaget
- `vinterjacka-kvinna` och `vinterjacka-man-och-kvinna` har beskrivningstexter som nämner **Under Armour** ("jackor från Under Armour och Urban Classics"). Under Armour fylls inte på (BESLUTSLOGG 2026-11-19), och produkterna i kollektionerna är Urban Classics, Brandit och Build your Brand. Texten stämmer alltså inte. Texten för herr är ok i sak men har brutna meningar och två interna länkar med sökparametrar.
- `vinterjacka-man-och-kvinna` (124 produkter) innehåller även barnjackor (t.ex. "UC Boys Basic Bubble Jacket") och överlappar de två andra. Dubbletter i övrigt: se jackor-herr/jacka-herr.

## Uppdatering 2026-11-27 (efter Davids ja)
- **Skrivet:** SEO-titel och metabeskrivning på alla tre (kanarie `vinterjacka-herr` först, därefter de två andra). Återläst i Shopify: exakt som i `forslag.csv`. Beskrivningstexterna oförändrade. Före-läge: `fore_seo.json` (båda fält saknades). Ångra: sätt seo.title och seo.description till null.
- **Utkast till nya beskrivningar** för `vinterjacka-kvinna` och `vinterjacka-man-och-kvinna`: `forslag_texter.json` (HTML, bara `<p>`, inga länkar, inga rubriker, inga pris- eller leveransuppgifter). Ej skrivet. Fakta ur kollektionernas produkter: dam har minst 30 köpbara jackor (Urban Classics flest, Brandit fyra parkas, Forvert en); märkena är hämtade ur produkternas vendor-fält.
- **Fynd:** `vinterjacka-kvinna` innehåller två sweatshirts med namnet "Parka" (UC Sweat Parka, Ladies Sweat Parka) som inte är vinterjackor. De är inte räknade i texten.
- Texten för herr är oförändrad (stämmer i sak men har brutna meningar).
- Före skrivning behövs enligt standarden en oberoende granskning av påståendena mot produkterna.
