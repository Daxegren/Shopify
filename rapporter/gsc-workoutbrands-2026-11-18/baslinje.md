# Search Console-baslinje: workoutbrands.com (2026-11-18)

Källa: `gsc_export.py sc-domain:workoutbrands.com --months 16` (2025-07-17 till 2026-11-15) samt `gsc_sammanfatta.py` och `gsc_sep_okt.py`, körda av David i Cloud Shell med egen inloggning (bara läsning). Rådata ligger i Davids Cloud Shell (`~/gsc_out/workoutbrands.com`, `~/gsc_workoutbrands.tgz`), inte i repot. **Fakta** = ur exporten. **Bedömning** = tolkning.

## Fakta
- 42 545 klick och 3 983 347 visningar på 16 månader. Mobil 31 388 klick (74 %), klickfrekvens 1,0 % mot desktop 0,3 %.
- Länder (klick): Sverige 11 247, USA 2 662, Italien 2 574, Polen 2 561, Finland 2 459, Tyskland 2 385.
- Månader: visningar 92 133 (2025-07) till 783 287 (2026-09), snittposition 26,2 till 5,9, klick 2 500–3 350 per månad, klickfrekvens 1,1 % till 0,4 %. Oktober 2026: 511 592 visningar, position 8,7.
- Sidtyper (klick / visningar): produkt 14 019 / 496 908; blogg 13 607 / 2 085 144; kollektion 10 237 / 937 295; annat (bl.a. språkens startsidor) 3 507 / 77 925; sidor 598 / 116 833; startsida 577 / 269 242. Sidrapporten är avkortad vid 25 000 rader.
- September till oktober (sidrapporten, avkortad; täcker bara cirka 61–73 % av månadens visningar): produkt visningar 204 204 till 112 796 (klick 944 till 1 065), blogg 175 982 till 160 323 (klick 1 041 till 890), kollektion 69 417 till 72 621 (klick 1 056 till 1 065). Störst visningsfall på sökfrågenivå: många Brandit-frågor (t.ex. "men brandit t-shirt" 2 160 till 459, "men brandit lumber jacket" 1 775 till 382, "brandit m65 giant veste homme" 1 197 till 4).
- Sökfrågor: "workout brand" 422 klick, "workout brands" 319, "forgotten faces" 237, "uc hoodie" 234, "träningskläder" 176, "rocawear" 164 (74 863 visningar, position 11,3).
- Vilken sida som rankar för frågan (visningar, klick, position):
  - rocawear: startsidan 58 864, 17, 11,1 (kollektionen /de/collections/rocawear-herr 2 161, 7, 13,9)
  - träningskläder: startsidan 39 876, 176, 11,7
  - zoo york shoes: startsidan 7 698, 5, 8,8 (produktsidan /en/products/zy-highbridge-en-gum-1 position 1,7–2,5 med 35–39 klick)
  - astani: /en/collections/astani-wear-women-and-men 6 994, 8, 5,8
  - relode: /collections/relode 5 681, 4, 12,7 och /en/collections/relode-en 5 507, 3, 8,3
  - ecko unltd: /fr/collections/ecko-unltd-herr 3 052, 47, 9,3
  - uc hoodie: /en/products/uc-vintage-heavy-hoodie-en 6 828, 8, 7,1
  - forgotten faces: /en/collections/forgotten-faces-eng 3 988, 224, 6,2
- Produktadresser med parametrar (?variant=…&currency=USD&utm_source=…) syns som egna sidor i exporten.

## Bedömning
- Märkessökningar besvaras ofta av startsidan i stället för märkets kollektion (Rocawear, Zoo York shoes): klickfrekvens 0,03 % respektive 0,06 %. Att göra märkeskollektionen till bästa träff är sannolikt den största enskilda SEO-möjligheten.
- Bloggen står för hälften av visningarna och en tredjedel av klicken men är informationssökning (CrossFit, styrka) med låg köpavsikt.
- Visningsfallet i oktober ligger i svansen av produktsidor och blogg; klicken föll inte. Orsaken är inte fastställd (kontrollera dag för dag och Brandit-produkternas lager/publicering).
- Språkversionerna ger riktig trafik (utom Sverige 74 % av klicken); tyska startsidan ligger på position 30,9.

## Saknas
Sidindexering, Sitemaps (inskickade mot indexerade) och Kärnvärden ur Search Console-gränssnittet.

## Rättelse 2026-11-18 (tillägg; texten ovan är oförändrad)
Efter omkörning av exporten visar totalerna per land, enhet och månad (inte avkortade): **42 266 klick och 6 556 547 visningar**, klickfrekvens 0,64 %. Sidrapporten, sökfrågerapporten och rapporten sida × sökfråga är avkortade vid 25 000 rader och summerar bara 3 983 347 visningar (cirka 61 % av totalen) men 42 545 klick (klickdelen är i praktiken komplett).
- Uppgiften "3,98 miljoner visningar" ovan är alltså sidrapportens avkortade summa, inte butikens totala visningar.
- Andelar av visningar per sidtyp (blogg cirka 52 %) gäller de 3,98 miljoner som ingår i sidrapporten. Räknat på alla 6,56 miljoner är bloggens synliga andel högst cirka 32 %; resten av visningarna ligger på sidor utanför de 25 000 raderna och kan inte fördelas per typ med den här exporten.
- Klickandelar per sidtyp (produkt 33 %, blogg 32 %, kollektion 24 %) påverkas knappt, eftersom klicken är i stort sett kompletta.
- Månadssiffrorna (visningar, klick, position) kommer från den fullständiga månadsrapporten och står kvar.
- September mot oktober per sidtyp bygger på avkortade sidrapporter (täckning 61–73 % av månadens visningar).

## Tillägg 2026-11-18: kollektioner (språk sammanslagna per handle)
Källa: `kollektioner_prioritet.csv` (alla språkversioner av en kollektion summerade, frågetecken-parametrar borttagna), skapad med `shopify-sync/scripts/gsc_kollektioner.py` ur sidrapporten (avkortad vid 25 000 rader; visningar är därför lägre än verkligt). Rådata: `gsc_workoutbrands_radata.tgz`.

**Fakta**
- 1 616 kollektionshandles syns i sidrapporten. Mest visningar: `hoodie-oversized-herr` 44 048 (449 klick, position 16,1, 21 sidor på 10 språk), `hoodie-oversized-herren` 37 691 (28 klick, position 41,0), `ecko-unltd-herr` 19 126 (305 klick), `vendors` 17 393 (440 klick, 291 filtersidor `/collections/vendors?…` per märke), `klader-till-examen-herr` 16 432, `relode` 15 677 (20 klick), `klader-till-dop-herr` 13 400 och `-dam` 10 258, `starter-black-label-man` 12 026, `present-till-18-arig-kille` 11 960, `rocawear-herr` 11 138 (172 klick).
- Mest klick: `forgotten-faces-eng` 474 (4,9 %), `hoodie-oversized-herr` 449, `vendors` 440, `dangerous-dngrs-herr` 396 (6,7 %), `ecko-unltd-herr` 305, `cayler-sons-man` 294 (4,4 %), `dangerous-dngrs-man` 200.
- `hoodie-oversized-herr` och `hoodie-oversized-herren` är två kollektioner med nästan samma namn och konkurrerar om samma sökord.
- Kollektioner med många visningar och nästan inga klick: `oversized-clothing-man` 10 497 visningar och 4 klick, `long-sleeve-kvinna` 10 176 och 3, `relode` 15 677 och 20, `astani-wear-women-and-men` 9 145 och 20.

**Bedömning**
- Märkena sköts delvis av filtersidor (`/collections/vendors?q=…`) i stället för egna märkeskollektioner; ändra inte det utan beslut.
- Tillfällesktioner (examen, dop, present till 18-åring) får många visningar men är osäkra som köpavsikt för streetwear; bedöm mot försäljning innan de prioriteras.
- Dubblettkollektionen `hoodie-oversized-herren` bör undersökas (omdirigering eller sammanslagning); ändring tidigast 2026-12-01.
