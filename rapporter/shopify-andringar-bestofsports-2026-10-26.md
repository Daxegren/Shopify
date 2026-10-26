# Ändringar i Best of Sports publicerade tema, 2026-10-26

**Gjort av:** David, i temaredigeraren (verktyget jag arbetar med blockerar skrivning till det publicerade temat). **Verifierat av:** Claude, genom att läsa filerna ur Shopify (bara läsning) och jämföra rad för rad mot de sparade originalen i `rapporter/shopify-original-2026-10-26/bos-tema/`. Tema: "Kopia av Kopia av Kopia av Uppdaterad kopia av ..." (id 195516039434). Sparat 2026-10-26 19:49–19:50 UTC.

## Resultat av jämförelsen: bara de godkända raderna skiljer
**`layout/theme.liquid`** (29 248 till 29 108 byte)
- Före (6 rader): kommentar och `if request.page_type == 'product'` med `<link rel="canonical" href="{{ shop.url }}{{ product.url }}">`, `else` med `<link rel="canonical" href="{{ shop.url }}{{ request.path }}">`, `endif`.
- Efter (1 rad): `{%- comment -%} Canonical skrivs av snippets/doc-head-core (canonical_url, rätt domän per marknad). Egen override med shop.url borttagen 2026-10-26. {%- endcomment -%}`

**`snippets/breadcrumbs.liquid`** (10 990 till 11 056 byte): `shop.url` blev `request.origin` på alla 11 rader (91, 101, 109, 120, 128, 140, 148, 154, 162, 168, 176).

**`sections/main-product.liquid`** (110 897 till 110 915 byte): `shop.url` blev `request.origin` på rad 23, 31 och 39. Inga andra rader skiljer. Rad 974 är oförändrad.

`snippets/doc-head-core.liquid` är identisk med originalet (den skriver kvarvarande canonical via `canonical_url`).

## Kontroll på de publika sidorna (David körde `schema_kallor.py`)
- bestofsports.fi, produkt: en canonical (`https://bestofsports.fi/products/…`), `og:url` samma, brödsmulor `https://bestofsports.fi`.
- bestofsports.dk, produkt: en canonical (`https://bestofsports.dk/products/…`), brödsmulor `https://bestofsports.dk`.
- Före: två canonical-taggar där den första pekade på bestofsports.se, och brödsmulor på bestofsports.se.

## Fortfarande på bestofsports.se (inte ändrat, inte godkänt)
Organization-blocket i `theme.liquid`, produktschemat (`structured-data-product`: `url` och erbjudandens `url`), omdömessektionens `@id`, `structured-data-header`. Omdömessektionen avvaktar (beslut Davids).

## Utvärdering
- Nästa genomlysning av BOS efter ombyggd avbild: `multiple_canonical_tags` och `canonical_offsite` ska vara 0 på produkt- och kategorisidor.
- Search Console (URL-inspektion, "Google-vald canonical") före och efter, när behörigheten för `bestofsports.*` fungerar. BOS saknar kopplad GA4- och Search Console-data i genomlysningen, så testloggen (T8) kan inte räkna effekten på klick och ordrar.
