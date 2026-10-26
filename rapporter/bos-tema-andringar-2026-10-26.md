# BOS-temat: godkända ändringar att göra i det publicerade temat (2026-10-26)

**Beslut (David):** 1. Omdömessektionen: avvakta. 2. Canonical och brödsmulor: ändra i det publicerade temat. Verktyget jag arbetar med blockerar skrivningar till det publicerade temat, så ändringarna görs i temaredigeraren (Teman, Åtgärder, Redigera kod) av David, och jag verifierar efteråt.

Originalfilerna är sparade i `rapporter/shopify-original-2026-10-26/bos-tema/` (exakta kopior, storlek jämförd mot Shopify: 29 248, 10 990 och 110 897 byte).

## Ändring 1: `layout/theme.liquid`
**Före** (rad 6–11, direkt efter `<head>`):
```liquid
  {%- comment -%} Optimized AI SEO Canonical & Crawl Budget Rules (Enterprise Theme) {%- endcomment -%}
  {%- if request.page_type == 'product' -%}
    <link rel="canonical" href="{{ shop.url }}{{ product.url }}">
  {%- else -%}
    <link rel="canonical" href="{{ shop.url }}{{ request.path }}">
  {%- endif -%}
```
**Efter:**
```liquid
  {%- comment -%} Canonical skrivs av snippets/doc-head-core (canonical_url, rätt domän per marknad). Egen override med shop.url borttagen 2026-10-26: den gav en andra canonical till primärdomänen. {%- endcomment -%}
```
Raderna under (robots-regeln för `sort_by` och `filter.`) ska stå kvar.

## Ändring 2: `snippets/breadcrumbs.liquid`
Byt `shop.url` mot `request.origin` på alla 11 ställen (rad 91, 101, 109, 120, 128, 140, 148, 154, 162, 168, 176). Exempel:
- Före: `"item": {{ shop.url | append: collection.url | json }}`
- Efter: `"item": {{ request.origin | append: collection.url | json }}`

## Ändring 3: `sections/main-product.liquid` (brödsmulorna i produktschemat, rad 23, 31 och 39)
| Före | Efter |
|---|---|
| `"item": {{ shop.url \| json }}` | `"item": {{ request.origin \| json }}` |
| `"item": {{ shop.url \| append: b1.url \| json }}` | `"item": {{ request.origin \| append: b1.url \| json }}` |
| `"item": {{ shop.url \| append: product.url \| json }}` | `"item": {{ request.origin \| append: product.url \| json }}` |

Rad 974 (`contact[Product URL]` i kontaktformuläret) ändras **inte**.

## Ändras inte (inte godkänt)
Omdömessektionen `bos-auto-reviews`, Organization i `theme.liquid`, `structured-data-product` och `structured-data-header` (alla med `shop.url`), hälsoetiketterna och GTM.

## Verifiering efter ändringen
1. Jag läser de tre filerna ur Shopify (bara läsning) och jämför mot originalen: bara de godkända raderna får skilja.
2. Du kör `python3 scripts/schema_kallor.py --base-url https://bestofsports.fi` (och `.dk`, `.se`). Förväntat: en canonical per sida på sidans egen domän, och brödsmulornas adresser på sidans domän. Produktschemat och Organization pekar fortfarande på bestofsports.se (inte ändrat).
3. Nästa nattliga genomlysning (kräver ombyggd avbild för de nya kontrollerna) visar `multiple_canonical_tags` och `canonical_offsite` på BOS.
