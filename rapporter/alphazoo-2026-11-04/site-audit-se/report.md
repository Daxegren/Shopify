# Genomlysning: alphazoo-se

Körning `alphazoo-se-20261104T170745-ae0c90` · 2026-11-04 17:07 UTC

## Sammanfattning

| Kritisk | Hög | Medel | Låg | Info |
|---|---|---|---|---|
| 0 | 113 | 132 | 565 | 251 |

Crawl: 400 URL:er (816 från 27 sitemaps), 400 OK, 0 omdirigerade, 0 4xx, 0 5xx.

## Förbättringar

- 113 × Ingen H1
- 399 × 11 av 21 bilder saknar alt-text
- 90 × Kategori visar 0 produkter
- 13 × Samma titel på 3 sidor (totalt 29 berörda)
- 5 × Identiskt innehåll på 2 indexerbara sidor (totalt 10 berörda)
- 3 × Sidan ska vara på 'da' men texten är mest 'sv'
- 2 × Felstavat varumärke 'alphazoon' i titel/rubrik (totalt 31 berörda)
- 2 × 2 H1 på samma sida
- 1 × Upp till 20 hreflang-varianter per sida
- 1 × 103 av 103 produktsidor
- 118 × Titeln är 79 tecken
- 45 × Metabeskrivning saknas

## Struktur: levande sidor per typ och språk

| Sidtyp | da | en | fi | nb | standard | Totalt |
|---|---|---|---|---|---|---|
| article | 22 | 22 | 21 | 21 | 22 | 108 |
| blog | 1 | 1 | 1 | 1 | 1 | 5 |
| collection | 22 | 22 | 21 | 21 | 22 | 108 |
| home | 1 | 1 | 1 | 1 | 1 | 5 |
| page | 14 | 14 | 14 | 14 | 14 | 70 |
| product | 21 | 21 | 20 | 20 | 21 | 103 |

## Indexering och statuskoder

### Info: robots.txt blockerar inga kända AI-botar (sajten kan läsas av AI-tjänster) (1)

Kontroll: `ai_crawlers_allowed`

| URL | Detaljer |
|---|---|
| https://alphazoo.se/robots.txt | checked: ['gptbot', 'chatgpt-user', 'oai-searchbot', 'claudebot', 'claude-web', 'anthropic-ai', 'perplexitybot', 'google-extended', 'ccbot', 'applebot-extended', 'bytespider'] |

### Info: Crawlen täckte 400 av 816 sitemap-URL:er (höj crawl.max_pages för full täckning) (1)

Kontroll: `crawl_truncated`

| URL | Detaljer |
|---|---|
| https://alphazoo.se | crawled: 400, in_sitemap: 816, max_pages: 400 |

## Marknader, språk och hreflang

### Medel: Sidan ska vara på 'da' men texten är mest 'sv' (3)

Kontroll: `language_mismatch`

| URL | Detaljer |
|---|---|
| https://alphazoo.se/da/blogs/nyheder | expected: da, detected: sv, share: 0.56 |
| https://alphazoo.se/en/blogs/latest-news | expected: en, detected: sv, share: 0.56 |
| https://alphazoo.se/fi/blogs/uutiset | expected: fi, detected: sv, share: 0.56 |

### Medel: Upp till 20 hreflang-varianter per sida (1)

Kontroll: `hreflang_many_variants`

| URL | Detaljer |
|---|---|
| https://alphazoo.se | max: 20, median: 20 |

### Info: 4 språk-/marknadsprefix i crawlen (1)

Kontroll: `locale_inventory`

| URL | Detaljer |
|---|---|
| https://alphazoo.se | locales: ['da', 'en', 'fi', 'nb'], mismatched_pages: {'da': 1, 'en': 1, 'fi': 1} |

## Titlar, rubriker och metadata

### Hög: Ingen H1 (home) (113)

Kontroll: `missing_h1`

| URL | Detaljer |
|---|---|
| https://alphazoo.se/ | page_type: home |
| https://alphazoo.se/da | page_type: home |
| https://alphazoo.se/da/pages/vores-eksperter | page_type: page |
| https://alphazoo.se/da/products/alpha-immun-olie-for-sund-pels-og-velvaere | page_type: product |
| https://alphazoo.se/da/products/alpha-zegg-til-hunde-for-en-vital-hud-og-skinnende-pels | page_type: product |
| https://alphazoo.se/da/products/and-kyllingmaltid-til-kat-laekkert-vadfoder-til-katte | page_type: product |
| https://alphazoo.se/da/products/angusokse-lammesmaltid-laekkert-vadfoder-til-hunde | page_type: product |
| https://alphazoo.se/da/products/barf-olie-til-hund-og-kat | page_type: product |
| … och 105 till | |

### Medel: Samma titel på 3 sidor (13)

Kontroll: `duplicate_title`

| URL | Detaljer |
|---|---|
| https://alphazoo.se/ | title: alpha zoo nordics, count: 3 |
| https://alphazoo.se/da | title: alpha zoo norden, count: 2 |
| https://alphazoo.se/da/blogs/nyheder/beroligende-kosttilskud-til-hunde | title: beroligende kosttilskud til hunde — alpha zoo, count: 2 |
| https://alphazoo.se/da/collections/loppmiddel-for-hundar | title: loppmiddel - for hundar — alpha zoo, count: 2 |
| https://alphazoo.se/da/pages/interview | title: interview — alpha zoo, count: 2 |
| https://alphazoo.se/en/blogs/latest-news | title: nyheter — alpha zoo, count: 2 |
| https://alphazoo.se/en/blogs/latest-news/calming-supplements-for-dogs | title: calming supplements for dogs — alpha zoo, count: 2 |
| https://alphazoo.se/en/pages/about-us | title: about us — alpha zoo, count: 2 |
| … och 5 till | |

### Medel: 2 H1 på samma sida (page) (2)

Kontroll: `multiple_h1`

| URL | Detaljer |
|---|---|
| https://alphazoo.se/nb/pages/byten-og-retur-1 | h1: ['Byten og retur', 'BYTEN OG RETURNER'], page_type: page |
| https://alphazoo.se/nb/pages/personopplysninger | h1: ['Personopplysninger', 'PERSONLIGE DATA'], page_type: page |

### Låg: Titeln är 79 tecken (118)

Kontroll: `title_too_long`

| URL | Detaljer |
|---|---|
| https://alphazoo.se/blogs/news/de-forsta-10-minuterna-kan-radda-ditt-djurs-liv-fastingar-pa-hund-och-katt | title: De första 10 minuterna kan rädda ditt djurs liv – fästingar på djur — Alpha Zoo |
| https://alphazoo.se/blogs/news/fastingar-pa-hund-och-katt-upptack-ta-bort-och-forebygg | title: Fästingar på hund och katt – upptäck, ta bort och förebygg / AlphaZoo — Alpha Zoo |
| https://alphazoo.se/blogs/news/fordelarna-med-fodertillskott-for-hundar-nar-vanlig-kost-inte-racker-till | title: Fördelarna med fodertillskott för hundar – när vanlig kost inte räcker — Alpha Zoo |
| https://alphazoo.se/blogs/news/fordelarna-med-fodertillskott-for-katter-nar-kosten-behover-kompletteras | title: Fördelarna med fodertillskott för katter – när kosten behöver komplett — Alpha Zoo |
| https://alphazoo.se/blogs/news/hunden-blir-nervos-och-skakig-kosttillskott-som-kan-lugna-din-hund | title: Hunden blir nervös och skakig – Kosttillskott som kan lugna din hund — Alpha Zoo |
| https://alphazoo.se/blogs/news/hur-hanterar-man-en-angestfylld-hund | title: Hur hanterar man en ångestfylld hund? / AlphaZoo - Guide! — Alpha Zoo |
| https://alphazoo.se/blogs/news/luftvagsinfektioner-hos-hundar-symtom-orsaker-och-behandling | title: Luftvägsinfektioner hos hundar / Symtom och behandling — Alpha Zoo |
| https://alphazoo.se/blogs/news/min-hund-har-en-orolig-mage-kosttillskott-som-hjalper-mot-magproblem-hos-hundar | title: Min hund har en orolig mage - Kosttillskott som hjälper mot magproblem — Alpha Zoo |
| … och 110 till | |

### Låg: Metabeskrivning saknas (45)

Kontroll: `missing_meta_description`

| URL | Detaljer |
|---|---|
| https://alphazoo.se/blogs/news |  |
| https://alphazoo.se/collections/frontpage |  |
| https://alphazoo.se/da/blogs/nyheder |  |
| https://alphazoo.se/da/collections/hjem |  |
| https://alphazoo.se/da/pages/find-det-rigtige-produkt-til-din-kat |  |
| https://alphazoo.se/da/pages/find-det-rigtige-produkt-til-netop-din-hund |  |
| https://alphazoo.se/da/pages/fortrydelsesret |  |
| https://alphazoo.se/da/pages/interview |  |
| … och 37 till | |

### Låg: Samma metabeskrivning på 2 sidor (1)

Kontroll: `duplicate_meta_description`

| URL | Detaljer |
|---|---|
| https://alphazoo.se/en/products/big-paw-ty-paw-care-for-dogs | count: 2 |

### Info: Metabeskrivningen är 320 tecken (139)

Kontroll: `meta_description_too_long`

| URL | Detaljer |
|---|---|
| https://alphazoo.se/blogs/news/fordelar-med-fiskolja-for-hund-katt |  |
| https://alphazoo.se/blogs/news/fordelarna-med-barf-kost-for-hundar-katter |  |
| https://alphazoo.se/blogs/news/fordelarna-med-hamppulver |  |
| https://alphazoo.se/blogs/news/fordelen-med-lugnande-kosttillskott-for-katter |  |
| https://alphazoo.se/blogs/news/ge-din-hund-en-battre-vardag-med-halsosamt-foder |  |
| https://alphazoo.se/blogs/news/kosttillskott-for-husdjur |  |
| https://alphazoo.se/blogs/news/organisk-hundmat-vad-ar-fordelarna |  |
| https://alphazoo.se/blogs/news/vad-ar-msm-pulver |  |
| … och 131 till | |

## Strukturerad data

### Medel: 103 av 103 produktsidor (100%) saknar shippingDetails i produktschemat (fraktgräns och avgift) (1)

Kontroll: `shipping_details_missing`

| URL | Detaljer |
|---|---|
| https://alphazoo.se | pages: 103, product_pages_with_schema: 103, sample: ['https://alphazoo.se/products/hastfest-delikat-vatfoder-for-hundar', 'https://alphazoo.se/da/products/hestefest-laekkert-vadfoder-til-hunde', 'http |

### Info: Product-schemat saknar aggregateRating (inga omdömen i strukturerad data) (103)

Kontroll: `product_schema_no_rating`

| URL | Detaljer |
|---|---|
| https://alphazoo.se/da/products/alpha-immun-olie-for-sund-pels-og-velvaere |  |
| https://alphazoo.se/da/products/alpha-zegg-til-hunde-for-en-vital-hud-og-skinnende-pels |  |
| https://alphazoo.se/da/products/and-kyllingmaltid-til-kat-laekkert-vadfoder-til-katte |  |
| https://alphazoo.se/da/products/angusokse-lammesmaltid-laekkert-vadfoder-til-hunde |  |
| https://alphazoo.se/da/products/barf-olie-til-hund-og-kat |  |
| https://alphazoo.se/da/products/big-paw-ty-potebehandling-til-hunde |  |
| https://alphazoo.se/da/products/flydende-mavestotte-naturlig-stotte-til-fordojelsen |  |
| https://alphazoo.se/da/products/foder-med-kalv-og-kanin-til-seniorhunde-laekkert-vadfoder-til-hunde |  |
| … och 95 till | |

## Innehåll, dubbletter och tunna sidor

### Medel: Identiskt innehåll på 2 indexerbara sidor (5)

Kontroll: `duplicate_content`

| URL | Detaljer |
|---|---|
| https://alphazoo.se/da/pages/om-os | count: 2 |
| https://alphazoo.se/en/pages/about-us | count: 2 |
| https://alphazoo.se/fi/pages/meista | count: 2 |
| https://alphazoo.se/nb/pages/om-alpha-zoo | count: 2 |
| https://alphazoo.se/pages/om-oss | count: 2 |

### Medel: Felstavat varumärke 'alphazoon' i titel/rubrik (2)

Kontroll: `brand_misspelling`

| URL | Detaljer |
|---|---|
| https://alphazoo.se/fi/collections/kalaoljy-koirille-kissoille | count: 4 |
| https://alphazoo.se/products/laxolja-for-hundar-och-katter | count: 27 |

### Låg: Tunt innehåll (58 ord) (15)

Kontroll: `thin_content`

| URL | Detaljer |
|---|---|
| https://alphazoo.se/collections/frontpage | words: 58, page_type: collection |
| https://alphazoo.se/da/collections/hjem | words: 42, page_type: collection |
| https://alphazoo.se/da/pages/fortrydelsesret | words: 60, page_type: page |
| https://alphazoo.se/da/pages/kontakt | words: 18, page_type: page |
| https://alphazoo.se/en/collections/homehome | words: 42, page_type: collection |
| https://alphazoo.se/en/pages/contact-us | words: 23, page_type: page |
| https://alphazoo.se/en/pages/right-of-withdrawal | words: 59, page_type: page |
| https://alphazoo.se/fi/collections/heme | words: 37, page_type: collection |
| … och 7 till | |

### Info: 399 levande sidor fördelade på 6 sidtyper (1)

Kontroll: `inventory`

| URL | Detaljer |
|---|---|
| https://alphazoo.se | article: {'standard': 22, 'da': 22, 'en': 22, 'fi': 21, 'nb': 21}, blog: {'standard': 1, 'da': 1, 'en': 1, 'fi': 1, 'nb': 1}, collection: {'standard': 22, 'da': 22, 'en': 22, 'fi': 21, 'nb': 21} |

## Produkter och kollektioner

### Medel: Kategori visar 0 produkter (färre än 4) men går att indexera (90)

Kontroll: `collection_few_products`

| URL | Detaljer |
|---|---|
| https://alphazoo.se/collections/aggskalspulver-for-hundar-katter | products_listed: 0, in_sitemap: True |
| https://alphazoo.se/collections/fastingspray-for-hundar | products_listed: 0, in_sitemap: True |
| https://alphazoo.se/collections/frontpage | products_listed: 0, in_sitemap: True |
| https://alphazoo.se/collections/hundschampo | products_listed: 0, in_sitemap: True |
| https://alphazoo.se/collections/hundsnacks-hundgodis | products_listed: 0, in_sitemap: True |
| https://alphazoo.se/collections/kattschampo | products_listed: 0, in_sitemap: True |
| https://alphazoo.se/collections/kattsnacks-kattgodis | products_listed: 0, in_sitemap: True |
| https://alphazoo.se/collections/loppmedel-for-hundar | products_listed: 0, in_sitemap: True |
| … och 82 till | |

## Bilder och alt-texter

### Medel: 11 av 21 bilder saknar alt-text (399)

Kontroll: `images_missing_alt`

| URL | Detaljer |
|---|---|
| https://alphazoo.se/da/products/barf-olie-til-hund-og-kat | missing: 11, total: 21, page_type: product |
| https://alphazoo.se/da/products/big-paw-ty-potebehandling-til-hunde | missing: 11, total: 21, page_type: product |
| https://alphazoo.se/da/products/flydende-mavestotte-naturlig-stotte-til-fordojelsen | missing: 11, total: 21, page_type: product |
| https://alphazoo.se/da/products/laksolie-for-hunde-og-katte | missing: 12, total: 23, page_type: product |
| https://alphazoo.se/da/products/linfroolie-premiumkvalitet-til-hund-og-kat | missing: 11, total: 21, page_type: product |
| https://alphazoo.se/da/products/natlysolie-atbar-vaxtbaseret-hud-og-palskur | missing: 11, total: 21, page_type: product |
| https://alphazoo.se/da/products/pawtable-poteplejestick-til-hunde | missing: 11, total: 21, page_type: product |
| https://alphazoo.se/da/products/pelsglans-spiselig-olie-til-hud-og-pels-hos-hund-og-kat | missing: 11, total: 21, page_type: product |
| … och 391 till | |

## Sidvikt och skript

### Låg: collection: 100% av bilderna saknar bredd och höjd (risk för layoutförskjutning) (2)

Kontroll: `images_without_dimensions`

| URL | Detaljer |
|---|---|
| https://alphazoo.se | page_type: collection, images: 363, without: 363 |
| https://alphazoo.se | page_type: product, images: 2142, without: 2137 |

### Info: home: median 1 externa skriptvärdar per sida (5 sidor) (3)

Kontroll: `third_party_script_hosts`

| URL | Detaljer |
|---|---|
| https://alphazoo.se | page_type: home, median_hosts: 1, pages: 5 |
| https://alphazoo.se | page_type: collection, median_hosts: 1.0, pages: 108 |
| https://alphazoo.se | page_type: product, median_hosts: 1, pages: 103 |

### Info: Samtyckeslösning i HTML: shopify_privacy (1)

Kontroll: `consent_platform_in_html`

| URL | Detaljer |
|---|---|
| https://alphazoo.se | platforms: {'shopify_privacy': 216}, pages_checked: 216 |

### Info: HTML-storlek: median 0.28 MB, max 0.54 MB (1)

Kontroll: `html_size_stats`

| URL | Detaljer |
|---|---|
| https://alphazoo.se | min: 258098, median: 284339, max: 539959 |
