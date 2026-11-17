# BEST OF SPORTS: kategorier (kollektioner), inventering och pilotutkast, 2026-11-04

Bara läsning. Inget är skrivet i Shopify (butiken verifierad som `6f2e53-67.myshopify.com` i API-svaren). Maskinläsbart: `kollektioner.json`, `kollektioner.csv`, `faktaunderlag.json`, `prioritering.csv`, `overlappande.json`, `publik_genomlysning.json`, `underlag/`, `pilot/`.

## 1. Inventering (349 kollektioner)
| Mått | Antal |
|---|---|
| Kollektioner totalt | 349 (299 smarta med regler, 50 manuella) |
| Utan en enda köpbar produkt (aktiv + lager) | 112 (varav 110 ligger i sitemap, 92 är smarta) |
| 1–4 köpbara | 103 |
| 5 eller fler köpbara | 134 |
| Utan beskrivningstext | 159 (33 av dem har 5+ köpbara) |
| Med text, median | 324 ord (182 kollektioner har över 200 ord) |
| SEO-titel längre än 43 tecken / saknas | 301 / 45 |
| Meta längre än 155 tecken / saknas | 55 / 43 |
| Med bild | 19 |
| Översättning titel da / fi | 349 / 294 |
| Översättning text da / fi | 197 / 190 |
| Saknas i sitemap men har köpbara | 3 (de tre långa "kopia"-handlarna) |

Att veta:
- **Publicerad ja/nej** går inte att läsa via API (appen saknar `read_publications`); sitemap används som proxy (344 av 349 finns där). **Språk (`read_locales`)** saknas också, men översättningar per språk går att läsa.
- **Antalet i Shopify-admin räknar utkast och arkiverade.** "Köpbar" i denna rapport = aktiv och lager över noll.
- **Dubbletter och överlapp** (samma antal, märken och pris): proteinpulver/proteinpulver-1, aminosyror/-1, tricepsstång/-1, gympaket/-1/viktpaket, ladcyklar/cargobikes, tillbehor/tillbehor-1, `varumarke`/`alla-produkter-best-of-sports`/`all`, konditionsutrustning/traningsutrustning-for-viktnedgang, skivstangspaket/skivstangsset m.fl. (30 kollektioner, `overlappande.json`). Två kollektioner heter "Träningsutrustning för viktnedgång" och en heter "radera" (handle `ddd`).
- **Kollektionerna är blandade.** Löpband innehåller löpbandsolja och silikonspray, sparkcyklar innehåller 26 sparkcykelhjul, elcyklar innehåller cykelhjälm och batteriskydd, Tunturi innehåller akupressurmattor. Ett prisspann över allt blir missvisande (löpband "från 69 kr"). Faktaunderlaget räknar därför bara huvudprodukter (typordet först i titeln).

## 2. Prioritering
Search Console/Analytics är **inte tillgängligt** i denna session: Windsor har bara Facebook ansluten, Ahrefs ingår inte i planen ("Insufficient plan"), och ingen Google Cloud-inloggning finns. Därför prioriterad efter antal köpbara produkter, med tidigare mätningar (2026-10-23: motionscykel position 55, träningsbänk 55, roddmaskin 62, barncykel 8 år 26, kona 16) som stöd. **Be David koppla Search Console** (Windsor `searchconsole`) för en riktig ordning.

| Klass | Antal | Innebörd |
|---|---|---|
| 1 Pilot | 10 | blandade typer, i utkast nedan |
| 2 Våg 2 | 45 | 20+ köpbara (t.ex. cyklar, Giant, Toorx, Hammer, BH Fitness, yoga-pilates, mountainbike) |
| 3 Våg 3 | 44 | 5–19 köpbara |
| 4 Struktur först | 30 | överlappar annan kollektion |
| 5 Tom eller 1–4 köpbara | 177 | ta bort, slå ihop eller fyll på innan text |
| 6 Utanför tills vidare | 43 | kosttillskott, barn m.fl. enligt profilen |

Fyra kollektioner i våg 2 saknar text helt idag (`fria-vikter`, `ovrig-utrustning`, `skidor`, `sportutrustning`); pilotens crosstrainer och sparkcykel har ingen text men har 20 respektive 54 köpbara huvudprodukter.

## 3. Genomlysning av kategorisidor (publikt, 12 sidor)
- **Rubriker:** en H1 (kollektionens titel) och fem H2 i texten ("... för alla nivåer", "Funktioner och komfort", "Kända varumärken", "Varför köpa ... hos Best Of Sports"). Allt ligger **före** produktlistan: på `/collections/lopband` ligger texten ca 44 000 tecken före första produktlänk (HTML). Ingen text under listan.
- **Strukturerad data:** bara Organization/ContactPoint/PostalAddress. **Ingen CollectionPage, BreadcrumbList eller ItemList** hittades på någon av de 12 sidorna.
- **Intern länkning:** inte kartlagd i denna omgång (ej undersökt).
- **Sidtitel:** temat lägger "– BEST OF SPORTS" efter SEO-titeln; flera titlar blir därför långa, och sparkcykelsidan har "Best of Sports – BEST OF SPORTS" (dubbelt).
- **Sidstorlek:** 560–840 kB HTML per kategorisida.
Bara 12 sidor är lästa; övriga antas likadana men är inte kontrollerade.

## 4. Pilotutkast (10 kategorier)
Motionscykel, löpband, roddmaskin, crosstrainer, hantlar, kettlebell, cykellås, elcykel, Tunturi (märke), sparkcykel. Fullständigt i `pilotutkast.md` och `pilot/<handle>.json` (id, titel, nuvarande text, ny text, SEO-titel, meta, faktaunderlag).

**Kontroll mot regelboken (`kategori_kontroll.py`, 0 fel):** R1 (alla tal och märken belagda i underlaget), R2/R5 (inga förbjudna ord: kvalitet, säkerhet, perfekt, hållbar m.fl.), R7 (typord som i kollektionens titlar), R11 (första meningen har verb "säljer", inte cirkulär), R12 (SEO-titel ≤43, meta 120–155, unika mot alla kollektioners SEO).

| Mått | Nuvarande | Nytt |
|---|---|---|
| Ord | 271–406 (crosstrainer, sparkcykel: 0) | 63–84 |
| SEO-titel (tecken) | 46–68 | 27–43 |
| Meta (tecken) | 138–160 | 131–151 |
| Löften/risk (R5) | "slitstark", "robust", "hög brytsäkerhet", "kvalitet", "perfekt", "hållbar", "pålitlig" i 8 av 10 | inga |
| Märken som inte säljs | KETTLER, MAXXUS, Gorilla Sports (löpband, hantlar, kettlebell), Liv/Kona (elcykel, inte bland köpbara elcyklar), Toorx/Finnlo (roddmaskin) | inga |
| Egna påståenden som saknar stöd | "hög brytsäkerhet" (cykellås), "rodd på vatten" och träroddmaskiner (roddmaskin; inga sådana är köpbara) | inga |

Begränsning: texterna blir korta (63–84 ord) eftersom bara det som går att belägga får stå. Se beslut 2 i beslutsfilen.
