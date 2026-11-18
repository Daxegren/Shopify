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

## Rättelse 2026-11-18, kollektionerna (tillägg; texten ovan är oförändrad)
`hoodie-oversized-herren` är **inte** en dubblett av `hoodie-oversized-herr`. Sidrapporten visar att adressen bara finns som `/de/collections/hoodie-oversized-herren` (tyska versionen; "Herren" är tyska för män): 25 klick, 37 485 visningar, position 41. Avsnittet ovan som föreslår att undersöka den som dubblett är fel och ska inte följas. URL-inspektionen visar dessutom att den svenska adressen `/collections/hoodie-oversized-herren` är okänd för Google. Den tyska hoodie-kollektionen med 37 485 visningar på position 41 är i stället en möjlig förbättringspost i sig.

## Tillägg 2026-11-18: indexering, sitemap, Kärnvärden och oktoberfallet
Källor: skärmbilder och täckningsexport ur Search Console (`indexering/`, fyra CSV-filer), samt `gsc_brandit_dag.py` och `gsc_index.py` körda av David i Cloud Shell (bara läsning).

**Fakta**
- **Indexering (alla kända sidor, 2026-11-10):** 139 tusen indexerade och 872 tusen inte indexerade (13 orsaker). Antalet kända, ej indexerade sidor föll i ett enda steg 2026-09-22 från 1 969 457 till 908 913; indexerade sidor ändrades då inte (155 257 till 158 280). Indexerade sidor har därefter sjunkit från 158 280 (2026-09-22) till 138 692 (2026-11-10).
- **Orsaker (sidor):** utesluten av noindex 373 085; alternativ sida med korrekt kanonisk tagg 332 215; genomsökt men inte indexerad 146 442; upptäckt men inte indexerad 7 475; hittades inte (404) 5 833; blockerad av robots.txt 3 532; sida med omdirigering 1 802; serverfel (5xx) 1 759 (verifiering misslyckades); soft 404 41; Google valde annan kanonisk 165; dubblett utan vald kanonisk 11.
- **Webbplatskarta:** `https://workoutbrands.com/sitemap.xml`, inskickad 2025-01-02, senast läst 2026-11-14, status lyckades, 125 011 upptäckta webbsidor och 113 362 bilder, inga fel eller varningar. Kolumnen indexerade visar 0 (fältet fylls inte av API:et).
- **Viktiga webbvärden (Chrome-användardata):** mobil och desktop var för sig 1 008 bra webbadresser, 0 behöver förbättras, 0 dåliga.
- **URL-inspektion, stickprov om nio produkter ur de 449 som saknas i sitemapen:** alla nio "URL is unknown to Google". Kollektionerna `/collections/hoodie-oversized-herr` (senast genomsökt 2026-11-11) och `/collections/rocawear-herr` (2026-10-23) är indexerade och skickade via sitemapen, och Google valde samma kanoniska adress.
- **Oktoberfallet, dag för dag (visningar):** alla sökfrågor låg på 20 000–28 000 per dag till och med 2026-10-07, föll 2026-10-08 till 21 151 och 2026-10-09 till 16 439, och ligger sedan på cirka 10 500–14 500 per dag. Klick per dag är oförändrade, cirka 80–150, genom hela perioden. Sökfrågor som innehåller "brandit" hade 2 400–4 700 visningar per dag fram till 2026-10-07, 982 den 2026-10-08 och 88 den 2026-10-09, och därefter cirka 10–100 per dag. Brandit-frågorna gav 0–2 klick per dag även före fallet.

**Bedömning**
- Oktoberfallet är ett tydligt avbrott 2026-10-08/09 i visningar men inte i klick, och Brandit-frågorna förklarar bara cirka 2 500–3 000 av de cirka 12 000 visningar per dag som försvann. Orsaken är inte fastställd. Det som bör kontrolleras: om andra egendomar (till exempel BOS) har samma fall samma dagar (då är det sannolikt Google-gemensamt), och vad som ändrades i Workout Brands-butiken eller dess appar 2026-10-08/09.
- Eftersom klicken inte påverkades är den direkta affärseffekten på sökklick liten.
- Steget 2026-09-22 i antalet kända sidor stämmer inte med någon förändring i indexerade sidor eller visningar; det ser ut som en omräkning eller rensning av kända adresser (till exempel parameter- eller filteradresser), inte ett index som försvann.
- 705 000 av de 872 000 oindexerade sidorna är noindex eller korrekt kanoniska alternativ (förväntat för en butik med 21 språk, filter och varianter). Intressantast för försäljning är de 146 442 genomsökta men inte indexerade sidorna (kvalitet eller dubbletter) och 1 759 serverfel.
- De nio produkterna ur sitemap-gapet är okända för Google; det bekräftar att 362 produkter med lager i praktiken inte syns i sökmotorn.

## Tillägg 2026-11-18: vad de oindexerade sidorna är (stickprov om 1 000 adresser per orsak)
Källa: Search Console, Indexering, Sidor, export per orsak (Davids filer, sex stycken). Varje fil innehåller de första 1 000 adresserna av orsakens totala antal; procentandelar gäller alltså stickprovet, inte hela antalet. **Fakta** om stickproven, **bedömning** om slutsatser.

| Orsak (sidor totalt) | Vad stickprovet visar |
|---|---|
| Utesluten av noindex (373 085, upp från 309 210 den 2026-08-21) | Alla 1 000 är Shopifys tekniska adresser `/web-pixels@…/sandbox/…`. |
| Alternativ sida med korrekt kanonisk tagg (332 215) | 95 % produktadresser på många språk; 53 % har parametrarna `_pos`/`_ss`/`_fid` (söksidor och rekommendationer), 43 % `pr_prod_strat` (rekommendationsmodul). Alla genomsöktes i november. |
| Genomsökt – inte indexerad (146 442) | Ingen exportfil mottagen än. |
| Hittades inte, 404 (5 833, 6 592 den 2026-08-21) | 97 % produktadresser; 46 % saknar parametrar (till exempel `/products/veloce-shorts-blue`, `/it/products/a-euphoria-top-bianco-crema`) och är alltså riktiga produktadresser som inte finns längre; de flesta på andra språk än svenska (svenska 10 %). Några enstaka `/upload/…` och `/public/video/…`. |
| Blockerad av robots.txt (3 532, 4 319 den 2026-08-21) | 971 av 1 000 är kollektionsflöden som slutar på `.atom` (till exempel `/is/collections/mossa.atom`), resten inloggnings- och kontosidor. Det är avsiktlig blockering och inget fel. 983 av 1 000 genomsöktes senast i augusti. |
| Sida med omdirigering (1 802, 2 365 den 2026-08-21) | 91 % utan parametrar: 47 % produkter, 30 % kollektioner, 11 % sidor, 10 % bloggartiklar. Riktiga omdirigeringar, genomsökta över hela sommaren och hösten. |
| Serverfel 5xx (1 759; 83 den 2026-08-21 och 1 838 från 2026-09-05) | 97 % franska produktadresser med `q=` och `pr_prod_strat` (rekommendationsmodulens parametrar); 999 av 1 000 genomsöktes senast i september. Antalet hoppade från 83 till 1 838 mellan 2026-09-04 och 2026-09-05. Verifiering har misslyckats. |

**Bedömning.** (1) Noindex, alternativ kanonisk och robots-blockeringen är i huvudsak väntat beteende för en Shopify-butik med 21 språk och rekommendationsparametrar, och de påverkar inte intäkter. (2) 404-adresserna med rena produktadresser är riktiga döda produktsidor; en sidotäckande omdirigering till närmaste kollektion är en strukturändring och görs tidigast 2026-12-01. (3) Serverfelen på franska rekommendationsadresser började 2026-09-05 och hör till parameteradresser, inte till produktsidorna själva; orsaken är inte fastställd, men de har inte genomsökts om sedan september. Det ger inget bevis för att riktiga produktsidor felar. (4) Den intressantaste gruppen för sökbarhet är "Genomsökt – inte indexerad" (146 442), men exempel saknas.

## Tillägg 2026-11-18: jämförelse med BOS för oktoberfallet
Källa: `gsc_bos_okt.py` (Davids körning i Cloud Shell, bara läsning), dag för dag 2026-10-01 till 2026-10-15.
- **bestofsports.se** (visningar per dag): 613, 650, 623, 677, 829, 816, 735, 624 (10-08), 688 (10-09), 633, 746, 664, 690, 665, 645. Klick 2–9 per dag. Inget fall 2026-10-08/09.
- **workoutbrands.com** (visningar per dag): 25 125 (10-07), 21 151 (10-08), 16 439 (10-09), cirka 15 300–17 550 därefter.
- **Bedömning.** BOS visar ingen motsvarande förändring, så fallet verkar inte vara en ändring som drabbar alla Davids sajter. BOS är dock liten (cirka 600–800 visningar per dag), bara svenskspråkig och har inte Workout Brands språkversioner, så jämförelsen utesluter inte en ändring som bara drabbar flerspråkiga produktsidor. Nästa steg är att se vilka länder och enheter som föll.

## Tillägg 2026-11-18: "Genomsökt – inte indexerad" och stickprov om inköpspris
**Fakta (Search Console, export med 1 000 adresser av 146 442).** Antalet föll i ett enda steg 2026-09-22 från 1 200 311 till 145 617. Det är samma steg som minskade "inte indexerat" från 1 969 457 till 908 913 samma dag. Stickprovet: 91 % produkter, 8 % kollektioner, 75 % utan parametrar (riktiga sidor), och 98,5 % på andra språk än svenska (pl 147, it 134, nl 108, fr 102, es 102, en 71, de 46; svenska 15 av 1 000). Alla genomsöktes i november.
**Bedömning.** Det stora steget 2026-09-22 är i praktiken Googles rensning av genomsökta men ej indexerade adresser (cirka 1,05 miljoner); det är inte ett index som försvann. Det som återstår är framför allt översatta produkt- och kollektionssidor på mindre språk som Google har läst men valt att inte indexera. Svenska sidor är i stort sett indexerade. Det förklarar varför utländska versioner har många visningar men få klick för vissa sökord och är en tänkbar kvalitetsfråga för maskinöversatta texter (inte undersökt).

## Tillägg 2026-11-18: leverantörsfaktura bekräftar att inköpspriserna är i euro
Källa: faktura 5018457 daterad 2026-11-17 från TB International GmbH (Urban Classics) till Davids bolag, i EUR, med nollmoms (EU-leverans); fakturan sparas inte i repot.
**Fakta.** Styckpriser på fakturan: BY027 Ladies Sweat College Jacket 14,95 EUR, BY058 Ladies Oversize Crewneck 10,95 EUR, BY191 Acid Washed Oversized Hoody 17,95 EUR (storlek L). I Shopify står `unitCost` till exakt 14,95 (alla lästa BY027-varianter), 10,95 (alla lästa BY058-varianter) och 17,95–18,95 (BY191, beroende på storlek). Försäljningspriserna är 429, 329 och 479 kr (BY191 med jämförpris 529).
**Slutsats.** Inköpspriset i Shopify är leverantörens eurobelopp, oomräknat och registrerat som kronor. Med en växelkurs på cirka 11 kr per euro (antagande, kursen är inte kontrollerad) blir marginalen efter 25 % moms cirka 52 % (BY027), 54 % (BY058) och 48 % (BY191); den visade marginalen var över 90 %. Fakturans belopp är exklusive frakt (19 EUR i extra kostnad på fakturan) och tull/fraktkostnader per styck är inte inräknade.

## Tillägg 2026-11-18: indexeringskontroll av svenska sidor (URL-inspektion, 1 825 adresser)
Källa: `gsc_inspect_par.py` körd av David i Cloud Shell mot Search Console (bara läsning), resultat i `indexeringskontroll_sv_1825.csv`. Urval: alla 670 svenska kollektioner och var sjätte svensk produkt ur sitemapen (1 155 av cirka 6 900), alltså inte slumpmässigt men jämnt fördelat i sitemapens ordning.
**Fakta.**
- Kollektioner (670): 594 indexerade (88,7 %), 50 genomsökta men inte indexerade (7,5 %), 18 okända för Google (2,7 %), 8 upptäckta men inte indexerade (1,2 %).
- Produkter (1 155): 1 098 indexerade (95,1 %), 44 okända för Google (3,8 %), 13 genomsökta men inte indexerade (1,1 %).
- Google valde samma kanoniska adress som den inskickade i samtliga fall. Senaste genomsökning: de flesta produkter i september–november 2026 (1 092 av 1 155); 19 genomsöktes senast i april–augusti.
- De 76 kollektioner som inte är indexerade (svenska adresser) har tillsammans cirka 19 956 visningar i Search Console (alla språk sammanräknade per handle). Störst: `t-shirt-oversized-herr` 6 343 visningar och 54 klick, `billiga-t-shirts-herr` 3 134 och 11, `hoodies-med-tryck-man` 1 142 och 13, `vandringsklader-herr` 888 och 4, `fleece-trojor-kvinna` 854 (okänd för Google), `klader-till-kontoret-dam` 779, `billiga-byxor-dam` 696, `basplagg-dam` 621 (upptäckt men inte indexerad).
**Bedömning.** (1) Svenska sidor är i huvudsak välindexerade; omfattningen av indexeringsproblem ligger i andra språk (98,5 % av "genomsökt, inte indexerad") och i de 449 produkter som inte är publicerade i Online Store. (2) Extrapolerat till alla svenska produkter är cirka 260 okända för Google och cirka 75 genomsökta men inte indexerade (osäkert, eftersom urvalet är var sjätte). (3) De cirka 76 svenska kollektionerna som inte är indexerade är en avgränsad lista att arbeta med efter 2026-12-01 (titel, text, intern länkning), med `t-shirt-oversized-herr` och `billiga-t-shirts-herr` först.
