# Genomlysning: byouunderwear

Körning `byouunderwear-20261104T171120-c6113b` · 2026-11-04 17:11 UTC

## Sammanfattning

| Kritisk | Hög | Medel | Låg | Info |
|---|---|---|---|---|
| 0 | 73 | 58 | 722 | 290 |

Crawl: 394 URL:er (351 från 27 sitemaps), 391 OK, 0 omdirigerade, 3 4xx, 0 5xx.

## Förbättringar

- 65 × Product-schemat saknar bild
- 5 × Ingen H1
- 3 × Interna länkar pekar på en sida som ger 404
- 38 × Samma titel på 2 sidor (totalt 160 berörda)
- 9 × Sidan ska vara på 'da' men texten är mest 'sv'
- 4 × Identiskt innehåll på 2 indexerbara sidor (totalt 11 berörda)
- 3 × Felstavat varumärke 'byou' i titel/rubrik (totalt 376 berörda)
- 1 × 2 H1 på samma sida
- 1 × Samma inline-skript (totalt 390 berörda)
- 1 × 85 av 85 kategorisidor
- 1 × 65 av 65 produktsidor
- 280 × BreadcrumbList saknas

## Struktur: levande sidor per typ och språk

| Sidtyp | da | de | en | fi | standard | Totalt |
|---|---|---|---|---|---|---|
| article | 26 | 26 | 26 | 26 | 26 | 130 |
| blog | 6 | 6 | 6 | 6 | 6 | 30 |
| collection | 17 | 17 | 17 | 17 | 17 | 85 |
| collection_list | 1 | 1 | 1 | 1 | 1 | 5 |
| home | 1 | 1 | 1 | 1 | 1 | 5 |
| page | 13 | 13 | 13 | 13 | 13 | 65 |
| policy | 1 | 1 | 1 | 1 | 1 | 5 |
| product | 13 | 13 | 13 | 13 | 13 | 65 |

## Indexering och statuskoder

### Låg: 25 paginerade sidor har canonical till sida 1 (produkter på sida 2 och framåt hittas då bara via sitemapen) (1)

Kontroll: `paginated_canonical_to_first`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se/blogs/nyheter?page=2 | count: 25, sample: ['https://byouunderwear.se/blogs/nyheter?page=2', 'https://byouunderwear.se/blogs/nyheter?page=3', 'https://byouunderwear.se/blogs/nyheter?page=5', 'https://byouunderwear.se/da/blog |

### Info: robots.txt blockerar inga kända AI-botar (sajten kan läsas av AI-tjänster) (1)

Kontroll: `ai_crawlers_allowed`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se/robots.txt | checked: ['gptbot', 'chatgpt-user', 'oai-searchbot', 'claudebot', 'claude-web', 'anthropic-ai', 'perplexitybot', 'google-extended', 'ccbot', 'applebot-extended', 'bytespider'] |

## Marknader, språk och hreflang

### Medel: Sidan ska vara på 'da' men texten är mest 'sv' (9)

Kontroll: `language_mismatch`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se/da/blogs/nyheter | expected: da, detected: sv, share: 0.6 |
| https://byouunderwear.se/de/blogs/nyheter | expected: de, detected: sv, share: 0.6 |
| https://byouunderwear.se/de/pages/us-laws-compliance-de | expected: de, detected: en, share: 0.71 |
| https://byouunderwear.se/en/blogs/nyheter | expected: en, detected: sv, share: 0.6 |
| https://byouunderwear.se/fi/blogs/uutiset | expected: fi, detected: sv, share: 0.6 |
| https://byouunderwear.se/pages/appi-compliance | expected: sv, detected: en, share: 0.7 |
| https://byouunderwear.se/pages/ccpa-compliance | expected: sv, detected: en, share: 0.71 |
| https://byouunderwear.se/pages/gdpr-compliance | expected: sv, detected: en, share: 0.72 |
| … och 1 till | |

### Info: 4 språk-/marknadsprefix i crawlen (1)

Kontroll: `locale_inventory`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se | locales: ['da', 'de', 'en', 'fi'], mismatched_pages: {'da': 1, 'fi': 1, 'de': 2, 'en': 1, 'rot': 4} |

## Titlar, rubriker och metadata

### Hög: Ingen H1 (page) (5)

Kontroll: `missing_h1`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se/da/pages/nyhetsbrev | page_type: page |
| https://byouunderwear.se/de/pages/nyhetsbrev | page_type: page |
| https://byouunderwear.se/en/pages/nyhetsbrev | page_type: page |
| https://byouunderwear.se/fi/pages/nyhetsbrev | page_type: page |
| https://byouunderwear.se/pages/nyhetsbrev | page_type: page |

### Medel: Samma titel på 2 sidor (38)

Kontroll: `duplicate_title`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se/ | title: byou - trosorna du glömmer att du har på dig
 – byou underwear, count: 2 |
| https://byouunderwear.se/blogs/nyheter | title: nyheter
 – byou underwear, count: 2 |
| https://byouunderwear.se/blogs/nyheter/bambu-vs-ekologisk-bomull-trosor-kanslig-hy | title: bambu vs ekologisk bomull: vilket material är bäst för känslig hy och 
 – byou underwear, count: 5 |
| https://byouunderwear.se/blogs/nyheter/bygg-en-kapselgarderob-for-underklader-hur-manga-trosor-behover-du | title: bygg en kapselgarderob för underkläder: hur många trosor behöver du eg
 – byou underwear, count: 5 |
| https://byouunderwear.se/blogs/nyheter/farglara-underklader-osynliga-under-vitt | title: färglära för underkläder: så väljer du osynliga underkläder under vitt
 – byou underwear, count: 5 |
| https://byouunderwear.se/blogs/nyheter/flexibla-trosor-kroppsforandringar | title: flexibla trosor för livets alla kroppsförändringar
 – byou underwear, count: 5 |
| https://byouunderwear.se/blogs/nyheter/hallbara-underklader-kvalitetstrosor-som-haller | title: hållbara underkläder i praktiken: så känner du igen kvalitetstrosor so
 – byou underwear, count: 5 |
| https://byouunderwear.se/blogs/nyheter/modal-i-underklader-silkesmjuka-trosor-trafiber | title: modal i underkläder: därför är träfiber det mest silkesmjuka valet för
 – byou underwear, count: 5 |
| … och 30 till | |

### Medel: 2 H1 på samma sida (page) (1)

Kontroll: `multiple_h1`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se/en/pages/delivery-information-eng | h1: ['DELIVERY INFORMATION', 'DELIVERY INFORMATION'], page_type: page |

### Låg: Titeln är 62 tecken (165)

Kontroll: `title_too_long`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se/ | title: BYOU - Trosorna du glömmer att du har på dig
 – BYOU Underwear |
| https://byouunderwear.se/blogs/nyheter/bambu-vs-ekologisk-bomull-trosor-kanslig-hy | title: Bambu vs Ekologisk bomull: Vilket material är bäst för känslig hy och 
 – BYOU Underwear |
| https://byouunderwear.se/blogs/nyheter/bygg-en-kapselgarderob-for-underklader-hur-manga-trosor-behover-du | title: Bygg en kapselgarderob för underkläder: Hur många trosor behöver du eg
 – BYOU Underwear |
| https://byouunderwear.se/blogs/nyheter/den-perfekta-presenten-till-flickvannen-eller-frun-eleganta-underklader-som-visar-omtanke | title: Present till flickvän eller fru – eleganta underkläder - Tips!
 – BYOU Underwear |
| https://byouunderwear.se/blogs/nyheter/farglara-underklader-osynliga-under-vitt | title: Färglära för underkläder: Så väljer du osynliga underkläder under vitt
 – BYOU Underwear |
| https://byouunderwear.se/blogs/nyheter/flexibla-trosor-kroppsforandringar | title: Flexibla trosor för livets alla kroppsförändringar
 – BYOU Underwear |
| https://byouunderwear.se/blogs/nyheter/hallbara-underklader-kvalitetstrosor-som-haller | title: Hållbara underkläder i praktiken: Så känner du igen kvalitetstrosor so
 – BYOU Underwear |
| https://byouunderwear.se/blogs/nyheter/modal-i-underklader-silkesmjuka-trosor-trafiber | title: Modal i underkläder: Därför är träfiber det mest silkesmjuka valet för
 – BYOU Underwear |
| … och 157 till | |

### Låg: Metabeskrivning saknas (70)

Kontroll: `missing_meta_description`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se/blogs/nyheter |  |
| https://byouunderwear.se/collections/all |  |
| https://byouunderwear.se/collections/beige-hipstertrosor |  |
| https://byouunderwear.se/collections/beige-stringtrosor |  |
| https://byouunderwear.se/collections/beige-trosor-hipster-och-string |  |
| https://byouunderwear.se/collections/frontpage |  |
| https://byouunderwear.se/collections/svarta-hipstertrosor |  |
| https://byouunderwear.se/collections/svarta-stringtrosor |  |
| … och 62 till | |

### Låg: Samma metabeskrivning på 4 sidor (42)

Kontroll: `duplicate_meta_description`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se/ | count: 4 |
| https://byouunderwear.se/blogs/nyheter/bambu-vs-ekologisk-bomull-trosor-kanslig-hy | count: 5 |
| https://byouunderwear.se/blogs/nyheter/bygg-en-kapselgarderob-for-underklader-hur-manga-trosor-behover-du | count: 5 |
| https://byouunderwear.se/blogs/nyheter/farglara-underklader-osynliga-under-vitt | count: 5 |
| https://byouunderwear.se/blogs/nyheter/flexibla-trosor-kroppsforandringar | count: 5 |
| https://byouunderwear.se/blogs/nyheter/hallbara-underklader-kvalitetstrosor-som-haller | count: 5 |
| https://byouunderwear.se/blogs/nyheter/modal-i-underklader-silkesmjuka-trosor-trafiber | count: 5 |
| https://byouunderwear.se/blogs/nyheter/nattunderklader-och-somnkomfort-ratt-trosor-for-god-somn | count: 5 |
| … och 34 till | |

### Info: Metabeskrivningen är 320 tecken (217)

Kontroll: `meta_description_too_long`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se/blogs/nyheter/bambu-vs-ekologisk-bomull-trosor-kanslig-hy |  |
| https://byouunderwear.se/blogs/nyheter/bygg-en-kapselgarderob-for-underklader-hur-manga-trosor-behover-du |  |
| https://byouunderwear.se/blogs/nyheter/farglara-underklader-osynliga-under-vitt |  |
| https://byouunderwear.se/blogs/nyheter/flexibla-trosor-kroppsforandringar |  |
| https://byouunderwear.se/blogs/nyheter/hallbara-underklader-kvalitetstrosor-som-haller |  |
| https://byouunderwear.se/blogs/nyheter/modal-i-underklader-silkesmjuka-trosor-trafiber |  |
| https://byouunderwear.se/blogs/nyheter/nattunderklader-och-somnkomfort-ratt-trosor-for-god-somn |  |
| https://byouunderwear.se/blogs/nyheter/osynliga-underklader-guide-somlosa-trosor |  |
| … och 209 till | |

## Strukturerad data

### Hög: Product-schemat saknar bild (65)

Kontroll: `product_schema_no_image`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se/da/products/byou-seamless-hipster-10-pack-beige |  |
| https://byouunderwear.se/da/products/byou-seamless-hipster-10-pack-svart |  |
| https://byouunderwear.se/da/products/byou-seamless-hipster-2-pack-beige-dk |  |
| https://byouunderwear.se/da/products/byou-seamless-hipster-2-pack-sort |  |
| https://byouunderwear.se/da/products/byou-seamless-hipster-5-pabyou-seamless-hipster-5-pack-sortck-sort |  |
| https://byouunderwear.se/da/products/byou-seamless-hipster-5-pack-beige-dk |  |
| https://byouunderwear.se/da/products/byou-seamless-thong-10-pak-beige |  |
| https://byouunderwear.se/da/products/byou-seamless-thong-10-pak-sort |  |
| … och 57 till | |

### Medel: 85 av 85 kategorisidor (100%) saknar BreadcrumbList (mallen skriver ingen) (1)

Kontroll: `collections_without_breadcrumb_schema`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se | pages: 85, collections: 85, sample: ['https://byouunderwear.se/collections/frontpage', 'https://byouunderwear.se/da/collections/frontpage', 'https://byouunderwear.se/fi/collections/frontpage-fi', 'htt |

### Medel: 65 av 65 produktsidor (100%) saknar shippingDetails i produktschemat (fraktgräns och avgift) (1)

Kontroll: `shipping_details_missing`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se | pages: 65, product_pages_with_schema: 65, sample: ['https://byouunderwear.se/products/byou-underwear-presentkort-2', 'https://byouunderwear.se/da/products/byou-underwear-presentkort-2', 'https://byouu |

### Låg: BreadcrumbList saknas (article) (280)

Kontroll: `breadcrumb_schema_missing`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se/blogs/nyheter/bambu-vs-ekologisk-bomull-trosor-kanslig-hy |  |
| https://byouunderwear.se/blogs/nyheter/bygg-en-kapselgarderob-for-underklader-hur-manga-trosor-behover-du |  |
| https://byouunderwear.se/blogs/nyheter/den-perfekta-presenten-till-flickvannen-eller-frun-eleganta-underklader-som-visar-omtanke |  |
| https://byouunderwear.se/blogs/nyheter/farglara-underklader-osynliga-under-vitt |  |
| https://byouunderwear.se/blogs/nyheter/flexibla-trosor-kroppsforandringar |  |
| https://byouunderwear.se/blogs/nyheter/hallbara-underklader-kvalitetstrosor-som-haller |  |
| https://byouunderwear.se/blogs/nyheter/modal-i-underklader-silkesmjuka-trosor-trafiber |  |
| https://byouunderwear.se/blogs/nyheter/nattunderklader-och-somnkomfort-ratt-trosor-for-god-somn |  |
| … och 272 till | |

### Info: Product-schemat saknar aggregateRating (inga omdömen i strukturerad data) (65)

Kontroll: `product_schema_no_rating`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se/da/products/byou-seamless-hipster-10-pack-beige |  |
| https://byouunderwear.se/da/products/byou-seamless-hipster-10-pack-svart |  |
| https://byouunderwear.se/da/products/byou-seamless-hipster-2-pack-beige-dk |  |
| https://byouunderwear.se/da/products/byou-seamless-hipster-2-pack-sort |  |
| https://byouunderwear.se/da/products/byou-seamless-hipster-5-pabyou-seamless-hipster-5-pack-sortck-sort |  |
| https://byouunderwear.se/da/products/byou-seamless-hipster-5-pack-beige-dk |  |
| https://byouunderwear.se/da/products/byou-seamless-thong-10-pak-beige |  |
| https://byouunderwear.se/da/products/byou-seamless-thong-10-pak-sort |  |
| … och 57 till | |

## Innehåll, dubbletter och tunna sidor

### Medel: Identiskt innehåll på 2 indexerbara sidor (4)

Kontroll: `duplicate_content`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se/pages/appi-compliance | count: 2 |
| https://byouunderwear.se/pages/gdpr-compliance | count: 2 |
| https://byouunderwear.se/pages/intervju | count: 5 |
| https://byouunderwear.se/pages/us-laws-compliance | count: 2 |

### Medel: Felstavat varumärke 'byou' i titel/rubrik (3)

Kontroll: `brand_misspelling`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se/ | count: 365 |
| https://byouunderwear.se/de/pages/kaufbedingungen | count: 1 |
| https://byouunderwear.se/fi/products/byou-seamless-thong-5-pack-beige-fi-1 | count: 10 |

### Låg: Tunt innehåll (56 ord) (53)

Kontroll: `thin_content`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se/collections/beige-hipstertrosor | words: 56, page_type: collection |
| https://byouunderwear.se/collections/beige-stringtrosor | words: 40, page_type: collection |
| https://byouunderwear.se/collections/beige-trosor-hipster-och-string | words: 88, page_type: collection |
| https://byouunderwear.se/collections/frontpage | words: 22, page_type: collection |
| https://byouunderwear.se/collections/svarta-hipstertrosor | words: 55, page_type: collection |
| https://byouunderwear.se/collections/svarta-stringtrosor | words: 55, page_type: collection |
| https://byouunderwear.se/collections/svarta-trosor-hipster-och-string | words: 102, page_type: collection |
| https://byouunderwear.se/da/collections/beige-hipstertrosor | words: 49, page_type: collection |
| … och 45 till | |

### Info: 390 levande sidor fördelade på 8 sidtyper (1)

Kontroll: `inventory`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se | article: {'standard': 26, 'da': 26, 'fi': 26, 'de': 26, 'en': 26}, blog: {'standard': 6, 'da': 6, 'fi': 6, 'de': 6, 'en': 6}, collection: {'standard': 17, 'da': 17, 'fi': 17, 'de': 17, 'en': 17} |

## Produkter och kollektioner

### Låg: Kategori visar 3 produkter (färre än 4) men går att indexera (25)

Kontroll: `collection_few_products`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se/collections/beige-hipstertrosor | products_listed: 3, in_sitemap: True |
| https://byouunderwear.se/collections/beige-stringtrosor | products_listed: 2, in_sitemap: True |
| https://byouunderwear.se/collections/frontpage | products_listed: 1, in_sitemap: True |
| https://byouunderwear.se/collections/svarta-hipstertrosor | products_listed: 3, in_sitemap: True |
| https://byouunderwear.se/collections/svarta-stringtrosor | products_listed: 3, in_sitemap: True |
| https://byouunderwear.se/da/collections/beige-hipstertrosor | products_listed: 3, in_sitemap: True |
| https://byouunderwear.se/da/collections/beige-stringtrosor | products_listed: 2, in_sitemap: True |
| https://byouunderwear.se/da/collections/frontpage | products_listed: 1, in_sitemap: True |
| … och 17 till | |

## Bilder och alt-texter

### Låg: 7 av 18 bilder saknar alt-text (86)

Kontroll: `images_missing_alt`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se/ | missing: 7, total: 18, page_type: home |
| https://byouunderwear.se/collections | missing: 16, total: 19, page_type: collection_list |
| https://byouunderwear.se/da | missing: 7, total: 18, page_type: home |
| https://byouunderwear.se/da/collections | missing: 16, total: 19, page_type: collection_list |
| https://byouunderwear.se/da/pages/baeredygtighed | missing: 1, total: 4, page_type: page |
| https://byouunderwear.se/da/pages/nyhetsbrev | missing: 1, total: 4, page_type: page |
| https://byouunderwear.se/da/pages/om-os | missing: 1, total: 4, page_type: page |
| https://byouunderwear.se/da/products/byou-seamless-hipster-10-pack-beige | missing: 6, total: 14, page_type: product |
| … och 78 till | |

## Sidvikt och skript

### Medel: Samma inline-skript (upp till 325 KB) på 390 sidor – tema eller app, åtgärdas på ett ställe (1)

Kontroll: `large_inline_script_sitewide`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se/ | pages: 390, starts_with: // 检查是否有class为shopify-design-mode的元素(区分是不是在shopify设计模式下) if , sample: ['https://byouunderwear.se/', 'https://byouunderwear.se/pages/contact', 'https://byouunderwear.se/collect |

### Info: home: median 2 externa skriptvärdar per sida (5 sidor) (3)

Kontroll: `third_party_script_hosts`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se | page_type: home, median_hosts: 2, pages: 5 |
| https://byouunderwear.se | page_type: collection, median_hosts: 2, pages: 85 |
| https://byouunderwear.se | page_type: product, median_hosts: 2, pages: 65 |

### Info: Samtyckeslösning i HTML: shopify_privacy (1)

Kontroll: `consent_platform_in_html`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se | platforms: {'shopify_privacy': 155}, pages_checked: 155 |

### Info: HTML-storlek: median 0.57 MB, max 0.82 MB (1)

Kontroll: `html_size_stats`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se | min: 553882, median: 572997, max: 816383 |

## Interna länkar

### Hög: Interna länkar pekar på en sida som ger 404 (3)

Kontroll: `broken_internal_link`

| URL | Detaljer |
|---|---|
| https://byouunderwear.se/da/pages/www.byouunderwear.se | linked_from: ['https://byouunderwear.se/da/pages/handelsbetingelser'], count: 1 |
| https://byouunderwear.se/en/pages/www.byouunderwear.se | linked_from: ['https://byouunderwear.se/en/pages/kopvillkor'], count: 1 |
| https://byouunderwear.se/pages/www.byouunderwear.se | linked_from: ['https://byouunderwear.se/pages/kopvillkor'], count: 1 |
