# Genomgång av BOS-temat (publicerat tema, id 195516039434), 2026-10-26

Bara läsning. Inget är ändrat i Shopify.

## Täckning (vad som är läst och inte)
- **Hämtat:** alla 552 textfiler utanför `assets/`: 5 blocks, 3 config, 2 layout, 11 locales, 87 sektioner, 108 snippets och 330 mallar (306 kategorimallar, 24 övriga).
- **Läst i sin helhet:** `layout/theme.liquid`, `snippets/doc-head-core`, `doc-head-social`, `structured-data-header`, `structured-data-product`, `structured-data-article`, `breadcrumbs`, `free-shipping-notice`, `rating`, `sections/bos-auto-reviews` (alla 442 rader; långa rader visades avkortade), `sections/main-collection-banner`, `config/markets.json`, `product.json`, `collection.json`.
- **Genomsökt med mönster, inte läst rad för rad:** övriga sektioner och snippets (canonical, JSON-LD, `shop.url`, spårning, noindex, hälsopåståenden, FAQ). `sections/main-product.liquid` (111 KB) är bara läst delvis (rad 1–45 och träffar).
- **Inte läst:** `assets/` (JS och CSS, cirka 120 filer, bland annat `custom.js` och `main.js`), appars inbäddningar och det Shopify själv lägger i sidan via `content_for_header`.

## 1. Påhittade kundomdömen på alla produktsidor (allvarligt)
Sektionen `sections/bos-auto-reviews.liquid` ingår i `templates/product.json` (`bos_auto_reviews_4ndGHx`) och visas på produktsidor utom tillbehör och delar.
- **Omdömena är inbyggda i koden**, inte hämtade från kunder: några färdiga texter per produktkategori och språk (sv, da, fi, en), till exempel "Bästa proteinet jag testat, löser sig perfekt." Texterna handlar inte om den enskilda produkten.
- **Författarna är påhittade:** förnamn och initial väljs ur namnlistor utifrån produktens ID. Kommentaren i koden lyder "DYNAMISKA NAMN-POOLER (Förhindrar fotspår hos Google)".
- **Betyget är framräknat:** `ratingValue` 4,4–5,0 väljs utifrån produkt-ID, `reviewCount` är fast "6" och alla sex omdömen har betyg 5.
- **Det visas för besökaren** som omdömeskort med stjärnor, författare och "verifierad ✓"-text, och skrivs som `Product`, `aggregateRating` och `Review` i strukturerad data.
- **Följd för tidigare siffror:** de 85 % av BOS-produktsidor som har betyg i strukturerad data (onsite-kontrollen) kommer från den här sektionen och inte från riktiga kunder. Jag redovisade siffran som något positivt i ett tidigare svar; det var fel.
- **Risker (bedömning, inte juridiskt utlåtande):** Googles regler för strukturerad data förbjuder omdömen som inte kommer från riktiga användare och kan ge manuell åtgärd mot hela sajten. Falska konsumentomdömen är förbjudna enligt konsumentskyddsreglerna i EU (Omnibus-direktivet, i Sverige marknadsföringslagen), med sanktionsavgifter. Annonsplattformarnas policyer kan också beröras. Frågan bör bedömas av en jurist.

## 2. Flera källor till samma schema, alla med `shop.url`
- **Product:** `snippets/structured-data-product` (renderas av `main-product.liquid` rad 1466) plus `bos-auto-reviews`. Båda använder `shop.url`, alltså primärdomänen bestofsports.se, även på .fi och .dk.
- **Organization:** `layout/theme.liquid` (url `shop.url`, `availableLanguage` Swedish, land SE hårdkodat) och `structured-data-header` (header-sektionen, url `shop.url` plus sidans adress).
- **BreadcrumbList:** `main-product.liquid` (rad 15–40) och `snippets/breadcrumbs` skriver varsin lista, båda med `shop.url`.
- **`shop.url` förekommer 40 gånger i 12 filer** (`breadcrumbs`, `structured-data-*`, `bos-auto-reviews`, `main-product`, `theme.liquid`, `doc-head-social`, `social-share`, `main-gift-card`).
- **Samma kod som Gorilla:** `structured-data-product` är i praktiken identisk med Gorillas `json-linked-data-product` (samma text och samma Yotpo/Stamped-logik). Gorillas tema har jag inte läst i sin helhet; om Gorilla också har en sektion för automatiska omdömen vet jag inte.

## 3. Två canonical-taggar
`layout/theme.liquid` rad 26 och 28 skriver `{{ shop.url }}{{ product.url }}` respektive `{{ shop.url }}{{ request.path }}`. `snippets/doc-head-core` skriver `{{ canonical_url }}`. Resultat: två taggar där den första pekar på bestofsports.se. `og:url` använder `canonical_url`.

## 4. H1 på kategorisidor: temat förklarar inte felen
- **Temat renderar H1 i Liquid** (inte med JavaScript): `main-collection-banner` skriver `<h1>` när `show_collection_title` är sant, och det är det i 305 av 306 kategorimallar och i standardmallen.
- Två mallar avviker: `collection.flash-sale` (rubriken avstängd) och `collection.skivstang-25mm.context.danmark` (ingen banner).
- Alltså förklarar temat **inte** de 173/400/431 `missing_h1` i genomlysningen eller att 15 av 20 kategorier saknade H1 i onsite-kontrollen. Min tidigare hypotes (JavaScript-byggda kategorier) stämmer inte. Orsaken är inte hittad och kräver att den faktiska HTML:en för en flaggad kategori läses.
- 143 av kategorimallarna har dessutom en egen `<h1>` i rich-text-innehållet, utöver bannerns. Möjliga dubbla rubriker; inte verifierat.

## 5. Övrigt som framkom
- **Hälsopåståenden:** en JavaScript i `theme.liquid` lägger på produktsidor för kosttillskott etiketter ("Muskler & Styrka", "Energi & Fokus", "Viktminskning", "Hälsa & Mående") utifrån nyckelord i produkttexten. Menyn har en post "Viktminskning / fettförbränning" och en kategorimall med kosttillskott för viktminskning. Det kan vara hälsopåståenden i EU:s mening (förordning 1924/2006) och bör granskas.
- **Spårning:** inget GTM, Facebook-pixel eller liknande i temat (`custom_html_head` och GTM-ID är tomma). Spårningen ligger alltså i appar och pixlar. `multiple_ga4_ids` i genomlysningen kommer därför inte från temat.
- **Fri frakt:** `free_shipping_minimum` är `SE:800` och `DK:700` (ingen rad för FI), och aviseringen `show_free_shipping_notice` är avstängd.
- **hreflang** finns inte i temat. Taggarna som syns i sidan (inklusive `fi-DK` och `da-FI`) skrivs av Shopify.
- **Tillgänglighetsverktyget accessiBe** laddas från `theme.liquid`.
- **Mark-up:** `theme.liquid` har två `</head>`.
- **Redigerat med AI-verktyg:** fem `blocks/ai_gen_block_*` har kvar sina prompts. Det säger inget om innehållet.
