# Intern länkning på bestofsports.se: mätning 2026-11-12

Bara mätning. Inget har byggts eller ändrats i Shopify, temat, Search Console, Analytics eller Ads. Alla siffror kommer från körningen och står i `matvarden.md` (genererad av skriptet). Detaljfiler: `sidor.csv` (en rad per sitemapsida: typ, djup, inlänkar, orsak/typ av länk), `kollektioner.csv`, `ankartexter.csv`, `lankproblem.csv`, `tvillingar.csv`, `gsc-svagast-lankade.csv`, `kosttillskott-barn-junior.csv`.

## Metod och täckning
- `site-audit` kan enligt koden köras utan BigQuery och utan Google Cloud (`--no-admin`, utan `--bigquery` och `--search-data`), men den sparar varken ankartexter eller var på sidan en länk sitter, och genomsöker hela domänen. Den kördes inte. I stället byggdes `shopify-sync/scripts/intern_lankning_mat.py` (återanvänder `fetch.py`, `sitemap.py`, `html_parse.py`, `crawler.py`), med 33 nätverksfria tester (`python3 -I shopify-sync/scripts/test_intern_lankning_mat.py`).
- Mätt: alla 4 375 adresser i sitemapen utom bloggartiklar (3 860 produkter, 344 kollektioner, 13 sidor, startsida, bloggindex) samt 1 055 pagineringssidor (`?page=N`), 15 sonderingar av `-se`-adresser och ett länkmål utanför sitemapen. Totalt 5 425 hämtade sidor, 4 451 sekunder. Alla produkter mättes, inget stickprov.
- Robots.txt följdes, neutral User-Agent utan e-post, aldrig över 3 anrop/s (sista omgången 1,2/s).
- **Bloggartiklar: 126 av 155 hämtades.** Cloudflare svarade med en bot-kontroll (HTTP 429, "Verifying your connection") på artiklar redan efter cirka 130 anrop, även vid 1,2 anrop/s. 8 artiklar blockerades och 21 hämtades aldrig. Jag försökte inte ta mig förbi kontrollen. Kollektioner och produkter påverkades inte (enstaka 429 löstes med kort väntan). Länkar från bloggen är därför en underkant.
- Mätt är HTML som servern levererar. Länkar som läggs till med JavaScript, och om menyn/sidomenyn syns på mobil, ingår inte.

## Fakta (mätvärden)
**(a) Föräldralösa sidor** (i sitemap, svarar 200, ingen inlänk från någon hämtad sida, inte ens menyn): 108 av 344 kollektioner, sidan `/pages/contact`, 0 produkter, 0 av de hämtade artiklarna. Ytterligare 37 kollektioner, 10 sidor och bloggindexet länkas bara från meny/sidfot/sidomeny.

**(b) Klickdjup från startsidan** (pagineringssidor räknas som egna steg):

| Sidtyp | Alla länkar | Utan meny/sidfot/sidomeny |
|---|---|---|
| Kollektioner | 234 nåbara, 110 onåbara, median 1, max 7 | 157 nåbara, 187 onåbara, median 3, max 7 |
| Produkter | alla nåbara, median 3, medel 5,6, 876 på djup 5 eller mer, max 50 | median 4, 1 897 på djup 5 eller mer, max 52 |
| Bloggartiklar (126) | median 4 | onåbara (bloggindexet länkas bara från sidfoten) |

2 406 av 3 860 produkter länkas bara från pagineringssidor.

**(c) Inlänkar till kollektioner.** 165 av 344 kollektioner finns i huvudmenyn, och exakt samma 165 finns i sidomenyn som visas på varje kollektionssida. Sidfoten länkar inga kollektioner. Innehållskällor (unika sidor som länkar, utan meny/sidfot/sidomeny/paginering):

| | 0 | 1 | 2-4 | 5-9 | 10+ |
|---|---|---|---|---|---|
| I meny (165) | 36 | 38 | 39 | 22 | 30 |
| Inte i meny (179) | 109 | 37 | 26 | 4 | 3 |

Innehållslänkar kommer från kollektionssidor (192 kollektioner får minst en), bloggartiklar (45), startsidan (19), produktbrödsmulor (6) och övriga sidor (1). **Produktsidornas brödsmula länkar bara till sex breda kollektioner**: varumarke 2 142, cyklar 770, konditionsutrustning 670, gymutrustning 129, kosttillskott 104, ovrig-utrustning 45. Ingen produktsida länkar till sin egen specifika kollektion.

**(d) Ankartexter.** Alla 5 058 innehållslänkar till kollektioner (räknat per källsida) har textankare, inga tomma eller bara bild. Generiska ankare: en ("se alla", på traningsmatta). Ankartexterna är beskrivande, oftast kollektionens namn i plural eller singular. Per kollektion: `kollektioner.csv`, `ankartexter.csv`.

**(e) Länkar till omdirigerade, saknade eller icke-indexerbara sidor.** En: `/collections/kona` ger 404 och länkas från `/collections/varumarke`. Inga omdirigerade adresser, noindex eller avvikande canonical bland länkmålen (0 omdirigeringar bland alla hämtade sidor). 0 felformade länkadresser.

**(f) Spårningsparametrar.** 169 innehållslänkar på 57 källsidor (52 bloggartiklar, 5 kollektionssidor): `_pos`, `_psq`, `_ss` (168 vardera), `_v` (120), `_psid` (52), `shpxid` (2). Ingen i meny eller sidfot.

**(g) Tvillingkollektioner med ändelsen -se.** Alla 15 uppräknade `-se`-adresser ger 404 på bestofsports.se. Ingen finns i sitemapen, ingen länkas från någon hämtad sida, ingen finns i menyn. De 13 basadresserna svarar 200, ligger i sitemapen och har canonical till sig själva. Sitemapen innehåller två adresser som slutar på -se, men det är produkter. Var `-se`-kollektionerna finns (utkast, annan marknad, annan domän) kan inte avgöras härifrån.

**(h) Mest synliga men svagast länkade** (Search Console-siffror från uppdraget/baslinjen; `kollektioner.csv` från kategorisessionen fanns inte på grenen). Av de 24: fyra har 0 innehållskällor (kona-1, cykelsolglasogon, traningsutrustning-for-hemmagym, skivstangsset), fem till har 1 (pre-workout-pwo, tranings-t-shirt-dam, romet, benmaskiner, skyddsutrustning-cykel). Fem ligger inte i menyn: traningsutrustning-for-hemmagym, pre-workout-pwo, benmaskiner, boxningssack, hybridcykel. Mest synliga enskilt: pre-workout-pwo (4 102 visningar, position 67) har ingen menylänk och en innehållslänk. kona-1 (2 887 visningar, position 17) har bara menylänk, och varumärkessidan länkar i stället till den döda `/collections/kona`. Hela tabellen: `matvarden.md` (h).

Kosttillskott (urval på handle-ord): 13 av 25 kollektioner har 0 innehållskällor. Barn/junior: 3 av 9 har 0. Se `kosttillskott-barn-junior.csv`.

## Bedömning (inte mätt)
1. Länkningen bärs av menyn: 165 kollektioner får en länk från varje sida, medan resten är nästan osynliga för intern länkning. De 108 föräldralösa är sannolikt tomma eller överlappande, och det är ett strukturbeslut som kategorisessionen förbereder. De ska inte länkas in före det beslutet.
2. Största enskilda hävstången är produktsidornas brödsmula (3 860 sidor som länkar till bara sex hubbar). Det är en temaändring som David gör.
3. De högt synliga men svagt länkade kollektionerna är billigast att förbättra, eftersom sidorna redan har visningar.
4. Att Google rankar dem på position 30–70 beror på flera saker; länkning är en möjlig faktor, inte en bevisad orsak.

## Föreslagen ordning (inget byggt)
1. Rätta den döda länken `/collections/kona` på varumärkessidan (till kona-1).
2. Länka de nio svagaste av de 24 synliga kollektionerna från relevanta kollektioner och kategoritexter (kategorisessionen), inte från menyn först.
3. Testa brödsmula till specifik kollektion på en produkttyp, mät, rulla ut.
4. Besluta struktur för de 108 föräldralösa.
5. Rensa spårningsparametrarna (låg prioritet).
6. Mät om med samma skript och Search Console minst 4–6 veckor efter ändring.

## Köra om
Rådata ligger i `ra-data/` (komprimerat). `python3 -I shopify-sync/scripts/intern_lankning_mat.py analysera --bas https://bestofsports.se --ut rapporter/intern-lankning-bos-2026-11-12/ra-data --rapport <ny katalog> --gsc rapporter/intern-lankning-bos-2026-11-12/gsc-underlag.csv` ger identiska filer (kontrollerat). Ny hämtning: kommandot `crawl` i skriptet.
