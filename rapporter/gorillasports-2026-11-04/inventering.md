# Inventering GORILLA SPORTS (2026-11-04), fas 1, bara läsning

**Källa:** butikens publika produktflöde (`/products.json`), sitemap och offentliga sidor på gorillasports.se och .dk. Shopify-verktyget (get-shop-info) kunde inte användas: det krävde ny inloggning, så butiken kunde inte verifieras via verktyget. Inga nycklar användes och inget skrevs. Följande kräver Admin API/verktyg och saknas därför: status (utkast/arkiverad), SEO-fält som egna värden, marknader/språkinställningar, kollektionernas regler, lager.

| Mått | Värde | Anm. |
|---|---|---|
| Publicerade produkter | 869 (.se och .dk har samma 869 id) | Utkast/arkiverade syns inte i flödet |
| Kollektioner (sitemap) | 208 | |
| Sidor (sitemap) | 21 | Bl.a. delivery, returning, payments, bygga-hemmagym |
| Leverantörsfält | Gorilla Sports Norden 777, Gorilla Sports Nordics 45, Gorilla Sports 35, MAXXUS 12 | Fyra värden för i praktiken samma märke |
| Produkttyper | Gympaket 82, Tillbehör 78, Träningsbänkar 56, Viktskivor 30 mm 50, Skivstångspaket 30 mm 47, Kabelhandtag 45, Justerbara hantelset 42, Kettlebells 32 m.fl.; 17 utan typ | |
| Taggar | 790 olika; vanligast "all products" 717, "paket" 124 | Stort taggträd; behöver rensas/klassas före taggregler |
| Beskrivning, ord | median 121; 22 under 50 ord; 18 över 400; inga tomma | |
| Beskrivningen börjar med titeln som rubrik | 815 av 869 (h2 i texten, 864 har h2) | Titeln upprepas, och sidan har redan en h1 |
| FAQ i beskrivningstexten | 0 | FAQPage finns i strukturerad data på 31 av 120 sidor (från tema/app) |
| Titeldubbletter (exakt, skiftlägesokänsligt) | 12 titlar, 13 överskjutande produkter | `sparr_titeldubbletter.csv`; kan vara avsiktliga varianter |
| Titlar >70 tecken | 0 | |
| Titlar med VERSALER (≥5 i rad) | 210 | Märke i versaler (MAXXUS, EXCALIBUR, TRIGRIP) och ord som GJUTJÄRN, PREMIUM |
| Bilder utan alt-text (flödet) | 8 140 av 8 140 | Ingen produktbild har alt-text i butiken |
| Produkter utan bild | 0 | |
| Engelska titlar | Få: "Set", "Pack", "Pull up bar", "Soft Plyo Box" | Blandade svensk-engelska ord |
| .dk-titlar identiska med .se | 25 av 869 | .dk är översatt |
| Produkter med bara leverantörens text | Går inte att avgöra utan Admin API/leverantörsfil | TODO |
| Hälsorelaterade/utanför-kandidater | 8 av 869 (vibrationsplattor 2, massagestolar 2, pulsmätare 2, barnhandskar 2) | `sparr_utanfor_tills_vidare_forslag.csv` |

Rådata: `produkter_se.json`, `produkter_dk.json`, `sidor_produkter_se.json` (120 slumpade produktsidor), `sidor_produkter_dk.json` (25), `sidor_ovriga_se.json` (start, 40 kollektioner, 6 sidor).
