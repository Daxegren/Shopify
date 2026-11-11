# Egen genomgång av kategorier och sidor, 2026-11-11

Metod: hämtade HTML för alla 230 adresser i butikens sitemaps för kategorier och sidor (208 kategorier, 21 informationssidor, 1 bloggindex). Produkter och enskilda blogginlägg ingår inte. Resultat per sida: `crawl-kategorier-sidor-2026-11-11.csv`. Det är en avgränsad genomgång av sidornas egen kod, inte en ersättning för Etals fullständiga kontroll.

| Mätning | Resultat | Kopplas till |
|---|---|---|
| Svarskod | 230 av 230 svarar 200 | W07 (404-felen finns på andra adresser än sitemapen) |
| Titlar med emoji | 69 av 230 | W03, textregler |
| Metabeskrivningar med emoji | 74 av 230 | W03 |
| Titlar över 60 tecken utan butiksnamn | 36 | W03 |
| Titlar över 70 tecken inklusive butiksnamn | 131 | W03 |
| Metabeskrivningar över 155 tecken | 31 | W03 |
| Dubblettitel | 1 par ("Bästsäljare") | – |
| Sidor utan H1 | 7, alla informationssidor (`/pages/gorilla-sports`, `kontakta-oss`, `foretags-gym`, `intervju-med-vd`, `bygga-paket`, `showroom`, `om-vart-showroom`) | W02 |
| Sidor med två H1 | 6 kategorier (`parallettes`, `foam-roller-massageboll`, `fot-o-handledsvikt`, `staende-boxningssack`, `hantelset`, `massagestol`) | W02 |
| Kategorier med strukturerad data | 201 har bara ItemList; ingen har BreadcrumbList eller FAQPage | W10 |
| Canonical som skiljer sig från adressen | 1 (`/collections/v-grepp-…` med emoji i adressen) | W06/W13 |
| Synliga ord per kategori | lägst 154, median cirka 382 | W03 |

Anmärkningar: titlarna innehåller en radbrytning före butiksnamnet, vilket tyder på en mallrad i temat. Etals siffra om 505 titlar över gränsen gäller fler sidor (produkter ingår) än den här genomgången.
