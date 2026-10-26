# Förslag: BOS-temat (ingen ändring gjord)

Bara ett underlag för beslut. Inget är ändrat i Shopify. Gäller det publicerade temat "Kopia av Kopia av Kopia av Uppdaterad kopia av ..." (id 195516039434).

## 1. Ta bort canonical-blocket i `layout/theme.liquid`
Tas bort (raderna direkt efter `<head>`):
```liquid
  {%- comment -%} Optimized AI SEO Canonical & Crawl Budget Rules (Enterprise Theme) {%- endcomment -%}
  {%- if request.page_type == 'product' -%}
    <link rel="canonical" href="{{ shop.url }}{{ product.url }}">
  {%- else -%}
    <link rel="canonical" href="{{ shop.url }}{{ request.path }}">
  {%- endif -%}
```
Kvar: robots-regeln (noindex för `sort_by` och `filter.`) och `snippets/doc-head-core.liquid`, som redan skriver `<link rel="canonical" href="{{ canonical_url }}">` med rätt domän per marknad.
- **Varför:** två motstridiga canonical-taggar, där den första pekar på bestofsports.se med ett finskt eller danskt handtag. Bekräftat i utdata för en .fi-produkt.
- **Konsekvens:** Google kan inte längre få en motstridig signal. Sidorna kanoniseras på sin egen adress via Shopifys `canonical_url`.
- **Att veta före beslut:** vad Google har valt i dag (kräver Search Console-inspektion) och om blocket är ett medvetet beslut. David har bekräftat att .fi och .dk ska ranka självständigt.

## 2. `snippets/breadcrumbs.liquid`: `shop.url` till `request.origin`
Sju ställen i `crumbs_structured_data` (rot, samlingar, produkt, blogg):
```liquid
"item": {{ shop.url | append: routes.root_url | json }}      ->  {{ request.origin | append: routes.root_url | json }}
"item": {{ shop.url | append: collection.url | json }}       ->  {{ request.origin | append: collection.url | json }}
"item": {{ shop.url | append: product.url | json }}          ->  {{ request.origin | append: product.url | json }}
... samma för routes.collections_url, blog.url, blog_tag_url, article.url, item_url
```
- **Varför:** brödsmulorna på .fi och .dk pekar på .se.
- **Konsekvens:** brödsmulornas adresser stämmer med sidans egen domän.

## 3. Organization i `layout/theme.liquid`: ingen ändring föreslås
`url` på varumärkets huvuddomän på alla domäner är normalt. Adress SE och språk Swedish kan vara företagets uppgifter. Det som kan vara fel är en andra Organization-block från annat håll (dubblett). Källan är inte hittad.

## Så testas det
1. Duplicera temat (Teman, Duplicera). Ändringen görs i kopian.
2. Förhandsgranska med `?preview_theme_id=<kopians id>` och kör `scripts/schema_kallor.py --url <adress>?preview_theme_id=...`. Förväntat: exakt en canonical per sida, rätt domän; brödsmulor med rätt domän.
3. Publicera först när det stämmer. Originalfilerna sparas före ändring.
