# Skanning av Gorilla Sports Nordics (gorillasports.se), 2026-11-20

Läsande. Källor: Shopify-kopplingen (butiksinfo, ShopifyQL, antal, kollektioner) och `sajtskanning.py` mot publika sidor (150 av 1 479 sidor i sitemap). Djupexporten (`wb_export.py`) är inte körd än (se nedan).

## Butiken
Gorilla Sports Nordics, Shopify Plus, SEK. 12 månader: 14,5 miljoner kr brutto, 625–999 ordrar per månad. 1 309 produkter (885 aktiva, 378 utkast, 46 arkiverade), 216 kollektioner, språk sv/da/no. Besök 90 dagar: 201 000, varav SE 112 000 (1,04 % konvertering) och DK 59 000 (1,34 %); ca 15 % kommer från länder med nästan noll konvertering (USA 0,04 %, Frankrike 0,02 % m.fl.), vilket liknar Workout Brands och kan vara botar (misstanke, ej styrkt).

## Sajtskanningen (rättad version, `rapport_2`)
0 brister och 4 varningar. Fynden har kontrollerats för hand mot enskilda sidor:
- Metabeskrivningar över 160 tecken: 16 av 150 (10,7 %).
- Sidor utan exakt en H1: 5 av 150 (3,3 %). Bekräftat: `collections/hantelset` och `collections/staende-boxningssack` har två H1 (andra H1 ligger i kollektionens beskrivningstext), och `pages/gorilla-sports` har ingen H1.
- Bilder utan alt-text: 68 av 3 264 (2,1 %).
- Titlar över 60 tecken: 1 av 150 (0,7 %).
Den första körningen visade 150 av 150 titlar över 60 tecken. Det var ett fel i skannern (SVG-ikoners `<title>` räknades med) och är rättat; se `LARDOMAR.md` 2026-11-20.

Extrapolering från urvalet är osäker: 5 av 150 sidor utan exakt en H1 motsvarar grovt 20–100 av 1 479 sidor.

## Kollektioner (första 100 av 216, via kopplingen)
Tre saknar SEO-titel och -beskrivning (frontpage, skivstangspaket-30-31mm, skivstang-120-200cm-30mm); bara frontpage är tom. Många SEO-beskrivningar delar samma fraser. De återstående 116 är inte granskade.

## Slutsats
Gorilla Sports har en teknisk och metadatamässig nivå som är bra, och skanningen hittar få och små fynd. Katalogdelen (alt-text per produkt, kategorier, översättningar) är inte mätt förrän exporten körts.

## Öppet
Exporten stoppade med `shop_not_permitted`: appen GS Scan måste skapas i den Shopify-organisation som äger Gorilla-butiken (samma som Gorilla BigQuery Sync).
