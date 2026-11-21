# Genomlysning B You Underwear (byouunderwear.se), 2026-11-04

Fas 1: bara läsning. Inget ändrades i Shopify, tema, Search Console, Analytics eller Google Ads.

## Vad som är undersökt och vad som saknas (läs först)
| Källa | Läge |
|---|---|
| Shopify Admin | **Saknas** (verktyget kräver ny inloggning efter butiksbyte). Siffrorna kommer från publik katalog, publika sidor och site-audit. Publika katalogen visar bara publicerade produkter. |
| Search Console, GA4, Google Ads (Windsor) | **Inte anslutna** (bara Facebook Organic). Länkar i beslutsfilen. |
| Ahrefs | **Ingår inte i planen** ("Insufficient plan"). |
| site-audit (utan admin) | **Klar:** 351 adresser i 27 sitemaps, 1 143 fynd (0 kritiska, 73 höga). Rådata i `rapporter/byouunderwear-2026-11-04/site-audit/`. |

## 1. Inventering (publik katalog, 13 produkter)
- Butik `officialbyou.myshopify.com`, **en domän** (byouunderwear.se) med språk sv, da, fi, de, en som undermappar. Antal marknader/valutor: SEK syns; övriga kräver Admin.
- **Produkter:** 12 trosor (Hipster 6, String 6; i 2-, 5- och 10-pack, färg Beige/Svart) och 1 presentkort. Märke: "BYOU Underwear".
- **Varianter:** 12 produkter med 4 varianter (storlek XS–L), presentkortet med 3.
- **Beskrivningar:** 501–628 tecken, nästan identiska mellan färger. Inga dubblettitlar. Titlar max 37 tecken.
- **Titlar:** använder engelska "Hipster" och "Thong" medan butikens kategorier heter "Hipstertrosor/Stringtrosor" (R7-fråga).
- **Bilder:** 60 produktbilder, **60 utan alt** (100 %).
- **Kollektioner:** 16, alla utan beskrivning, ingen tom.
- **Taggar:** 9 produkter bär en lång hashtagg-sträng (#seamless #lingerie ...) som en enda tagg; övriga 2pack/5pack, Hipstertrosor/Stringtrosor, giftcard.
- **Översättningar:** finns på da, fi, de, en. Översatta produktadresser har suffix (`-dk`, `-fi-1`, `-de-1`, `-eng-1`).
- **Okänt (Admin):** status, SEO-fält, leverantör, översättningsstatus per produkt, valutor/marknader.
- **Oförklarad avvikelse:** publika katalogen anger pris 26,00 på 2-pack, men produktschemat och sidan anger 229,00 SEK. Sannolikt annan valuta eller prisfält i katalogen; ej verifierat. Kontrolleras med Admin före alla prisberoende slutsatser.

## 2. Fynd, rangordnade efter effekt och risk
| # | Fynd | Belägg | Effekt | Risk att åtgärda |
|---|---|---|---|---|
| 1 | **Product-schemat är en `ProductGroup` utan bild på gruppnivå** (varianterna har bild). Verktyget flaggar 65 sidor (13 produkter × 5 språk). Google tolkar normalt varianternas bilder, så effekten kan vara mindre än "hög"; kontrollera i Rich Results-testet innan åtgärd. | site-audit `product_schema_no_image` 65 | Medel | Låg (temakod) |
| 2 | **Dubbletter av title/meta mellan färgvarianter:** 38 sidor med samma titel, meta unik på bara 8 av 13 produkter. Metan är autogenererad ur beskrivningen och blir densamma för Beige/Svart. 9 av 13 metas över 155 tecken (max 477) och avklippta mitt i meningen i og:description. | `produktsidor.json`, site-audit | Hög (klick, utdrag) | Låg: nya SEO-fält per produkt. Gäller trosor, inte hälsokategori. |
| 3 | **Title har radbrytning före varumärket** ("BYOU Seamless Hipster 2-pack - Beige⏎ – BYOU Underwear"). Syns som mellanslag/rad i Google och i delningar. | `produktsidor.json` | Låg–medel | Låg (tema) |
| 4 | **Ingen H1 på 5 sidor** (nyhetsbrev på alla språk m.fl.); produktsidor har 1 H1 (bra). Startsidans H1 är **tom** (`<h1>` utan text). Dubbel H1 på en engelsk sida. | site-audit, `sidor.json` | Medel | Låg |
| 5 | **Alt-text saknas på alla 60 produktbilder** och på 86 bilder i genomsökningen. | `inventering.json` | Medel | Låg |
| 6 | **Dubbel Organization-schema** (två olika block, det andra med fem tomma `sameAs`-poster), sociala länkar skiljer sig (facebook.com/byou, instagram.com/byou mot byou_underwear). Ingen BreadcrumbList på 280 sidor (inkl. kategorier). Ingen frakt/retur i Product-schemat. | site-audit `breadcrumb_schema_missing` 280, `shipping_details_missing` | Medel | Låg |
| 7 | **Trasig intern länk** `/pages/www.byouunderwear.se` (3 språk) från köpvillkoren: 404. | site-audit `broken_internal_link` | Låg–medel | Låg |
| 8 | **Språk:** nyhetsblogg på da/de är på svenska, tysk "US laws compliance" på engelska; hela de/da/fi-sajten ogranskad. 9 sidor flaggade. | `language_mismatch` 9 | Medel | Kräver **modersmålstalare** |
| 9 | **Tunna kategorier:** 53 tunna sidor (40–88 ord), 16 kategorier utan text, `frontpage` med 1 produkt, flera färg×typ-kategorier (beige-hipstertrosor, beige-stringtrosor, beige-trosor-hipster-och-string) som överlappar. Med 12 produkter är 16 kategorier för mycket. | `thin_content`, `collection_few_products` 25 | Medel | Medel (omdirigeringar) |
| 10 | **Översatta adresser med suffix** (`-dk`, `-fi-1`, `-eng-1`) och ogranskade titlar på da/fi/de ("Seamless" kvar på engelska). | hreflang i `sidor.json` | Låg–medel | Låg |
| 11 | **Titlar >60 tecken** på 165 sidor och för lång meta på 217: främst översatta/blogg/kategorisidor. | site-audit | Låg | Låg |
| 12 | **Varumärkesstavning** "byou" i titlar på 3 grupper av sidor; "BYOU" är butikens egen versalskrivning, vilket går emot R8 (se regelbok v1.5, R21). | site-audit `brand_misspelling` | Låg | Låg |

## 3. Risk i innehållet (styr spärrlistan)
Texterna är i huvudsak materialfakta: sömlöst (laserklippt), tunt tyg, stretch, "Inga kliande eller skavande sömmar", "hög träningskvalitet", "bästa möjliga osynlighet". Inga uttryckliga hälso- eller hygienpåståenden hittades, men underkläder kan lätt dra åt hygien/antibakteriellt/material/certifiering. Profilens `utanfor_tills_vidare` föreslår därför att dessa hålls utanför, att material (bomull, polyamid, elastan) och certifieringar endast skrivs om källan anger dem entydigt, och att presentkortet inte får produkttext. Storleksråd ("välj större storlek") och "designad med Jessica Rose" är påståenden att verifiera mot varumärkesägaren, inte gissa (R1).

## 4. GEO (synlighet i AI-svar)
- **Bra:** inga AI-botar blockeras. Shopify publicerar agent-instruktioner, `llms.txt` (standard) och UCP-adress. Product-schema med variantpris och lagerstatus finns. Omdömen i schemat: ett `review`-ord finns i sidkoden men ingen aggregateRating hittades (ej närmare undersökt).
- **Saknas:** entydigt "vad är BYOU"-innehåll (grundat Stockholm 2022 finns på Om oss men inte i schema), dubbel Organization med trasig sameAs, frakt/retur ej i strukturerad data, ingen FAQPage-markup (FAQ-text förekommer i sidkoden, ej närmare undersökt), ingen BreadcrumbList. AI-sök ser främst sidtext, och den är nästan identisk mellan 12 produkter, vilket gör produkter svåra att skilja (färg/antal-pack står bara i titeln).
- **Mätning:** Brand Radar och Search Console kunde inte läsas. Synlighet i AI-sökning är **okänd**.

## 5. Åtgärdsförslag (inget utfört)
1. Unika SEO-titel och meta per produkt (färg, antal i förpackning, typ). 12 trosor + 1 kort är ett litet, välavgränsat första test för pipelinen.
2. Rätta Product-schema (bild på gruppnivå, frakt, retur, ev. omdömen om källa finns), ta bort dubbel Organization, komplettera BreadcrumbList.
3. Fixa title-radbrytningen, tom H1 på startsidan och H1 på sidor som saknar.
4. Alt-text med mall och manuell kontroll.
5. Rätta länken `/pages/www.byouunderwear.se`, och slå ihop överlappande färgkategorier med omdirigering.
6. Granska/översätt blogg och policysidor med modersmålstalare.

## 6. Beslut som krävs av David
A. **Spärr:** godkänn förslaget i `butiksprofil-byouunderwear.json` (`utanfor_tills_vidare`). Rekommendation: ja, det berör få produkter i dag.
B. **Versaler i märket:** får "BYOU" skrivas i versaler (butikens egen stavning)? Rekommendation: ja, som undantag i profilen.
C. **Typord i titel:** "Hipster/Thong" (som nu) eller "Hipstertrosa/Stringtrosa"? Titelbyte påverkar handles aldrig (R12a) men ändrar sökbilden.
D. **Språk:** bara svenska i fas 2 (rekommenderas), da/fi/de/en senare med granskare.
E. **Åtkomst:** Windsor-länkar och Shopify-inloggning för B You (läs).
F. **Marknader:** vilka länder/valutor är aktiva (Admin)?
