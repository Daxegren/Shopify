# Genomlysning WORKOUT BRANDS (fas 1, 2026-11-04)

Underlag: offentliga data (workoutbrands.com/products.json, sitemap, robots.txt, fyra sidor) hämtade skrivskyddat. **Ej gjort:** Shopify-verktyget kräver ny inloggning (ingen get-shop-info, ingen butiksverifiering, inga marknader/kollektioner/status), Windsor har inget anslutet för Search Console, GA4 eller Google Ads, Ahrefs svarade "Insufficient plan" på gränskontrollen och användes därför inte. Allt nedan är alltså offentlig syn, inte kontorsdata.

## Butiken
- Streetwear och mode, inte träningsutrustning: Urban Classics, Mister Tee, Brandit, Flexfit, Merchcode m.fl. 53 värden i vendor, 86 produkttyper (T-shirt 2 125, Hoodie 877, Jacka 457, Keps 390).
- 6 920 publicerade produkter, 104 356 varianter (median 9 per produkt), 4 958 med lagerstatus tillgänglig. Skapade 2025 (6 381), 2026 (465).
- 21 språkversioner via hreflang/sitemap; sidan visar SEK. Flera valutor ej bekräftat.

## Fynd, rangordnade efter effekt och risk (förslag, inget utfört)
| # | Fynd | Omfattning | Effekt | Risk | Förslag |
|---|---|---|---|---|---|
| 1 | Bilder utan alt-text i produktdata | 66 514 av 66 514 | Hög (sök, tillgänglighet, GEO) | Låg | Generera alt ur titel + variant, via kontrollerat skript |
| 2 | Titel anger en enskild variant men produkten har flera (t.ex. "UC Shaped Long Tee NAVY XL", variant Black/XS) | 127 titlar slutar på storlek, 44 har engelsk färg | Hög (felaktig titel i sök och feeds) | Medel | Rensa titel till modellnamn; handle ändras ej (R12a) |
| 3 | Dubbla titlar | 145 titlar, 311 produkter | Medel | Medel | Gruppera, besluta om sammanslagning |
| 4 | Engelska titlar kvar | cirka 350 med engelska småord | Medel | Låg | Typordslista i profilen |
| 5 | Fältet vendor blandar märkeslinje och status ("Out of stock", "outlet") | 53 vendor-värden | Medel (märkesfilter, schema "brand") | Medel | David beslutar märkesmodell |
| 6 | Produkttyp saknas eller är status | 61 tomma, 34 "Out of stock" | Låg–medel | Låg | Fyll i / flytta |
| 7 | Taggar: 442 olika, många dubbletter i skiftläge och språk (Hoodie/Hoodies/Huvtröja, "in sheet" 5 155) | 442 | Medel (kollektionsregler, filter) | Medel | Taggstädning efter beslut; "in sheet" verkar vara importmarkör |
| 8 | Produktsida 1,65 MB HTML, startsida 0,68 MB | stickprov 1 | Medel (hastighet) | Medel | Mät med PSI innan prioritering (LÄRDOMAR 2026-10-20) |
| 9 | Startsidans H1 saknar text, 28 av 193 bilder utan alt | startsida | Medel | Låg | Tema, kräver beslut |
| 10 | Produkt-SEO-titel och og:title skiljer sig; metabeskrivningar finns | stickprov 1 | Låg | Låg | Mäta SEO-täckning med Shopify-data |
| 11 | Strukturerad data finns: Product, BreadcrumbList, Organization, WebSite, FAQPage; saknar offer/review-kontroll | stickprov | Medel för GEO | Låg | Validera med Rich Results-test (ej gjort) |
| 12 | Kanoniska adresser och hreflang (21 st) finns och ser konsekventa ut; sitemap per språk | 4 sidor | Positivt | – | Kontrollera större urval med site-audit |
| 13 | 33 färgnamn/gamla importrester, 83 outlet-produkter | – | Låg | Låg | Beslut om utrensning |

Beskrivningar: 0 tomma, 1 under 30 ord, median 90 ord, 6 887 svenska och 80 med mestadels engelsk text. Texterna ser alltså ut att vara skrivna (troligen AI/leverantör); källbindning enligt R1 går inte att kontrollera utan leverantörens originaltext.

## GEO (offentlig syn, otestad mot AI-sökmotor)
Positivt: Organization, FAQPage, Product och Breadcrumb finns. Okänt: tydlighet kring leverans/retur/betalning, om varumärkesidor finns, om märkena nämns i AI-svar (Brand Radar kräver Ahrefs-plan som inte gick att läsa).

## Att göra för fullständig genomlysning
Logga in Shopify-verktyget; koppla Search Console/GA4/Ads (David, i Windsor eller BigQuery enligt `ny-sajt.md`); bekräfta Ahrefs-plan.
