# Täckningskarta för genomlysningen (2026-10-26)

Underlag: `python3 scripts/audit_tackning.py` (David körde den 2026-10-26 mot nattens körningar). Siffran är antal fynd i senaste körningen; "-" betyder att kontrollen inte gav något fynd **eller** inte kördes. Gorilla SE körde 03:00 och DK 07:30, före dagens sista omdirigeringsändringar och före de fem nya kontrollerna.

## Vad som kördes
- Alla fem jobb gick igenom (COMPLETE 1/1). Fynd: Gorilla SE 7 803, Gorilla DK 10 328, BOS SE 15 962, BOS DK 16 680, BOS FI 35 225.
- Kontroller som bara kan köras med Shopify-adminåtkomst (till exempel `empty_collection`, `product_images_no_alt`, `redirect_table_*`, `partial_translation`) och kontroller som kräver Search Console eller GA4-data (`low_ctr_top10`, `keyword_cannibalization`) ger fynd bara för Gorilla. För BOS visar de "-" på alla rader. Det betyder sannolikt att de inte körs för BOS (bekräftas med `site-audit check-access --site bestofsports-fi`), inte att BOS är felfritt.

## Kritiska och höga fynd
| Sajt | Kritiska | Höga (största poster) |
|---|---|---|
| Gorilla SE | 16 (`redirect_target_missing` 8, `redirect_to_error` 8) | `redirect_chain` 105, `redirect_table_other_domain` 97, `redirect_table_chain` 28, `missing_h1` 7, `redirect_to_other_market` 6, `empty_collection` 5, `duplicate_collection_products` 4, `empty_collection_in_sitemap` 4, `partial_translation` 3 |
| Gorilla DK | 16 (samma 8 + 8) | `redirect_chain` 2 288, `redirect_table_other_domain` 279, `redirect_to_other_market` 249, `redirect_table_chain` 28, `broken_internal_link` 3, `missing_h1` 8 |
| BOS SE | 0 | `missing_h1` 173, `broken_internal_link` 1, `product_schema_bad_image` 1 |
| BOS DK | 1 (`sitemap_url_error`) | `missing_h1` 400, `broken_internal_link` 3 |
| BOS FI | 0 | `missing_h1` 431 |

## Fynd som kontrollerna hittat men som inte diskuterats tidigare
- Gorilla: `redirect_table_other_domain` (97 SE, 279 DK), `redirect_to_other_market` (249 DK), `redirect_target_mismatch` (205), `product_images_no_alt` (855 produktbilder utan alt-text i Shopify), `product_schema_relative_image` (862 och 845), `duplicate_collection_products` (4), `empty_collection` (5), `partial_translation` (3).
- BOS: `multiple_ga4_ids` (flera GA4-mätid i HTML på alla tre), `duplicate_meta_description` (FI 1 196), `duplicate_title` (FI 1 227), `missing_meta_description` (306 SE/DK, 500 FI), `language_mismatch` (FI 78).

## Luckor som kartan visar
- `breadcrumb_schema_missing` (låg) finns redan: 679 till 1 275 fynd per sajt. Det gäller kategorisidor och bloggartiklar, inte produktsidor.
- `product_schema_extra_node` ger fynd på BOS (2 503 till 5 552) men inte på Gorilla. På Gorilla har onsite-kontrollen dock sett två fullständiga Product-noder på 40 av 40 produktsidor; kontrollen flaggar bara extra noder som saknar bild eller pris, så två fullständiga noder upptäcks inte.
- `canonical_offsite` är 0 överallt, men den läste bara den sista canonical-taggen (rättat i koden, inte körd).
- Alla `hreflang_*` är 0 på alla sajter. Det går inte att avgöra av kartan om hreflang är rätt eller saknas helt; en sida utan hreflang ger inga hreflang-fynd.
- `collections_rendered_by_js` gav inget fynd på BOS, vilket tyder på att de flesta kategorisidor har produktlänkar i HTML. Det talar mot hypotesen att `missing_h1` på BOS beror på att allt byggs med JavaScript. Ej verifierat; `rendera_kategorier.py` är inte körd.
- Fynd för `images_missing_alt` (1 565 till 7 985) innehåller dekorativa SVG-ikoner (onsite-kontrollen visade det), så siffran är inte en mätning av produktbilder.

## Nästa steg i genomgången (inget förslag på åtgärd)
1. Bekräfta att BOS saknar adminåtkomst och sökdata i genomlysningen.
2. Kontrollera hreflang på BOS och Gorilla.
3. Hämta exempel på de höga posterna på Gorilla (omdirigeringar, tomma kategorier).
4. Läsa hela temat för BOS (via Shopify-kopplingen) och, för Gorilla, ett exporterat tema.
