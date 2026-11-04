# Stickprov fitness f_1–f_15 och f_x1 (2026-11-04)

Kontrollant: Sonnet, endast läsning. Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info. Inget skrevs till Shopify.
Urval: 64 produkter, 4 per batch (f_1–f_15 och f_x1), alla prioriterade ids ingår (10078, 10250, 10103, 10110, 10021, 10024, 10025, 10211), övriga slumpade (seed 7). Där flera filer täcker samma produkt gäller den senaste (10021/10024/10025 = f_skriv_1fix, 10103/10110 = f_skriv_5fix; 14ok, 14rest, 15ok, 15rest används där produkten finns i dem). Live-läsning via graphql_query nodes(ids), 4 produkter åt gången (id, handle, status, tags, title, seo.title, seo.description, descriptionHtml), jämförelse i python mot skrivfilen (script i scratchpad).

## Resultat: 0 avvikelser (64 av 64 kontrollerade)

Kolumnen Tagg/mening visar om live har taggen På beställning och om beställningsmeningen står i skrivfilen; de stämmer överens i alla 64.

| Skrivfil | Nr | Produkt | Meta (tecken) | seo.title live | Tagg/mening | Prioriterad | Avvikelser |
|---|---|---|---|---|---|---|---|
| f_skriv_1 | 10011 | Löpband BH Fitness RCM Pro TFT, 16-tums Pekskärm | 146 | satt | ja/ja |  | 0 |
| f_skriv_1fix | 10021 | Löpband BH Fitness RCM Pro MED | 104 | satt | ja/ja | prio: omskriven (1fix) | 0 |
| f_skriv_1fix | 10024 | Löpband BH Fitness RS2000, LED-skärm | 122 | satt | ja/ja | prio: omskriven (1fix) | 0 |
| f_skriv_1fix | 10025 | Löpband BH Fitness RS2000 Multimedia, 16-tums Pekskärm | 121 | satt | ja/ja | prio: omskriven (1fix) | 0 |
| f_skriv_2 | 10027 | Löpband BH Fitness RS800 Multimedia | 148 | NULL | -/- |  | 0 |
| f_skriv_2 | 10030 | Löpband BH Fitness RX3 | 130 | NULL | -/- |  | 0 |
| f_skriv_2 | 10039 | Löpband Toorx City Compact, Rose Gold | 133 | NULL | -/- |  | 0 |
| f_skriv_2 | 10049 | Löpband Tunturi Platinum TR20 | 137 | NULL | ja/ja |  | 0 |
| f_skriv_3 | 10053 | Löpband Tunturi T60 med 47 Träningsprogram | 149 | satt | ja/ja |  | 0 |
| f_skriv_3 | 10054 | Löpband Tunturi Signature T80 med 10-tums Skärm | 145 | satt | ja/ja |  | 0 |
| f_skriv_3 | 10062 | Löpbandsolja Tunturi T-Lube 200 ml | 138 | satt | -/- |  | 0 |
| f_skriv_3 | 10068 | Räckesförlängning för Tunturi T80, T85 och T90 Löpband | 106 | satt | -/- |  | 0 |
| f_skriv_4 | 10077 | Motionscykel BH Fitness EC01 Exercycle med 11 kg Svänghjul | 126 | satt | -/- |  | 0 |
| f_skriv_4 | 10078 | Motionscykel BH Fitness Ergo EMS med 12 Träningsprogram | 130 | satt | ja/ja | prio: avvikelse rapporterad (kanarie, tappad mening) | 0 |
| f_skriv_4 | 10083 | Motionscykel BH Fitness XTB MED, Maximal Användarvikt 180 kg | 129 | satt | ja/ja |  | 0 |
| f_skriv_x1 | 10085 | Spinningcykel BH Fitness Duke | 111 | NULL | ja/ja |  | 0 |
| f_skriv_x1 | 10087 | Spinningcykel BH Fitness Duke Magnetic | 122 | NULL | ja/ja |  | 0 |
| f_skriv_x1 | 10093 | Motionscykel Hammer Spheris 4.0 | 115 | NULL | ja/ja |  | 0 |
| f_skriv_4 | 10098 | Motionscykel Hammer Maximum Presidio med 41 Nivåer | 134 | satt | -/- |  | 0 |
| f_skriv_x1 | 10100 | Liggande Motionscykel Hammer RB 8000 | 120 | NULL | ja/ja |  | 0 |
| f_skriv_5 | 10102 | Spinningcykel Hammer Speed PRO med 36 Nivåer | 117 | satt | -/- |  | 0 |
| f_skriv_5fix | 10103 | Spinningcykel Hammer Speed Race SR med 10,1-tums Pekskärm | 123 | satt | ja/ja | prio: omskriven (5fix) | 0 |
| f_skriv_5 | 10104 | Spinningcykel Hammer Speed Race X med 20 kg Svänghjul | 111 | satt | ja/ja |  | 0 |
| f_skriv_5fix | 10110 | Motionscykel Toorx BRX 65 Comfort med Ryggstöd | 120 | satt | -/- | prio: omskriven (5fix) | 0 |
| f_skriv_6 | 10128 | Motionscykel Tunturi Fitcycle 40i | 141 | NULL | -/- |  | 0 |
| f_skriv_6 | 10133 | Motionscykel Tunturi Signature E40 | 138 | NULL | ja/ja |  | 0 |
| f_skriv_6 | 10139 | Motionscykel Tunturi Star Fit X100 X-Bike | 112 | satt | ja/ja |  | 0 |
| f_skriv_6 | 10144 | Minicykel Toorx Everfit Welly-M | 128 | NULL | -/- |  | 0 |
| f_skriv_7 | 10152 | Minicykel Tunturi Hopfällbar med Display | 149 | NULL | ja/ja |  | 0 |
| f_skriv_7 | 10154 | Minicykel Tunturi Cardio Fit M35 Magnetic | 145 | NULL | ja/ja |  | 0 |
| f_skriv_7 | 10166 | Crosstrainer BH Fitness Movemia ERV1000 LED | 127 | NULL | ja/ja |  | 0 |
| f_skriv_7 | 10171 | Crosstrainer Hammer SpeedMotion II | 150 | NULL | -/- |  | 0 |
| f_skriv_8 | 10177 | Stepbräda Tunturi Aerobic Step Easy | 123 | NULL | -/- |  | 0 |
| f_skriv_8 | 10183 | Roddmaskin BH Fitness Cardiff | 136 | NULL | -/- |  | 0 |
| f_skriv_8 | 10194 | Roddmaskin Toorx Rower Master | 134 | NULL | ja/ja |  | 0 |
| f_skriv_8 | 10196 | Roddmaskin Tunturi FitRow 70 WTR | 126 | NULL | -/- |  | 0 |
| f_skriv_9 | 10202 | Roddmaskin Tunturi FitRow 50 | 144 | NULL | ja/ja |  | 0 |
| f_skriv_9 | 10211 | Roddmaskin Tunturi Star Fit R100 | 137 | NULL | ja/ja | prio: före-fil saknade bildblock | 0 |
| f_skriv_9 | 10214 | Skivstångsskydd Hammer för Axlar | 142 | NULL | -/- |  | 0 |
| f_skriv_9 | 10220 | Skivstång Hammer Olympic Barbell, 50 mm | 124 | satt | -/- |  | 0 |
| f_skriv_10 | 10227 | Viktskiva Toorx Bumper Plate Challenge, Blå, 20 kg | 106 | satt | -/- |  | 0 |
| f_skriv_10 | 10234 | Skivstång Tunturi 30 mm, 165 cm, Nedre Huvud | 122 | satt | -/- |  | 0 |
| f_skriv_10 | 10245 | Hantelstång Tunturi, 36 cm, med Skruvfästen | 112 | satt | -/- |  | 0 |
| f_skriv_10 | 10250 | Viktskiva Tunturi Olympic Rubber Plate, 50 mm, 20 kg | 122 | satt | -/- | prio: avvikelse rapporterad (saknade Märke/Retur/Reklamation) | 0 |
| f_skriv_11 | 10256 | Viktskiva Tunturi Rubber Plate, 30 mm, 20 kg | 124 | satt | -/- |  | 0 |
| f_skriv_11 | 10263 | Viktskivor Tunturi Olympic Rubber Plates, 50 mm, 2 x 1,25 kg | 119 | satt | -/- |  | 0 |
| f_skriv_11 | 10268 | Viktskivor Tunturi Skivor Svart, 30 mm, 2 x 2,5 kg | 130 | satt | -/- |  | 0 |
| f_skriv_11 | 10275 | Hantel Hammer Compact Dumbbell PU, 32,5 kg | 108 | satt | ja/ja |  | 0 |
| f_skriv_12 | 10281 | Hantel Hammer Dumbbell Set, 10 kg, Krom | 129 | satt | -/- |  | 0 |
| f_skriv_12 | 10285 | Hantelset Toorx Gjutjärn, 20 kg | 124 | satt | -/- |  | 0 |
| f_skriv_12 | 10289 | Hantlar Tunturi Neoprene 2 x 0,5 kg, Rosa | 125 | satt | -/- |  | 0 |
| f_skriv_12 | 10298 | Hantelset Tunturi Platinum Hex Rubber, 2,5–20 kg | 110 | satt | ja/ja |  | 0 |
| f_skriv_13 | 10302 | Hantelset Tunturi Neoprenhantlar med Ställ, 3 Par | 136 | satt | -/- |  | 0 |
| f_skriv_13 | 10304 | Hantelset Tunturi PU Pro, 10 Par, 2–12 kg | 151 | NULL | ja/ja |  | 0 |
| f_skriv_13 | 10308 | Hantlar Tunturi Vinyl 2 x 0,5 kg, Rosa | 118 | NULL | -/- |  | 0 |
| f_skriv_13 | 10314 | Justerbar Hantel Tunturi Selector Dumbbell 12,5 kg | 136 | satt | -/- |  | 0 |
| f_skriv_14 | 10327 | Kettlebell Toorx Olympic EVO, Lila, 20 kg | 151 | NULL | -/- |  | 0 |
| f_skriv_14 | 10328 | Kettlebell Toorx Vinyl, 12 kg | 140 | NULL | -/- |  | 0 |
| f_skriv_14 | 10342 | Inversionsbänk BH Fitness Zero | 139 | NULL | -/- |  | 0 |
| f_skriv_14 | 10350 | Träningsbänk Hammer Force 2.0 | 135 | NULL | -/- |  | 0 |
| f_skriv_15 | 10357 | Inversionsbänk Toorx Inversion Bench, Hopfällbar | 123 | satt | -/- |  | 0 |
| f_skriv_15 | 10367 | Träningsbänk Tunturi UB80 Utility Bench, Justerbar | 102 | satt | -/- |  | 0 |
| f_skriv_15 | 10369 | Träningsbänk Tunturi WB20 Basic Weight Bench | 149 | satt | -/- |  | 0 |
| f_skriv_15 | 10373 | Rack BH Fitness Power Rack | 145 | NULL | -/- |  | 0 |

## Vad som kontrollerades (alla 64)

- **Tecken för tecken live mot skrivfilen:** title, seo.title (null när lika med titeln, avsett: 29 produkter), seo.description och descriptionHtml (produktdelen före `<h2>Leverans, retur och garanti</h2>` jämförd med kod; standardblocket jämfört med kod i skrivfilen och med blick mot live, se begränsningar). Alla identiska.
- **Osynliga tecken, dubbla mellanslag, inledande/avslutande blanksteg, kontrolltecken** (soft hyphen, nollbreddstecken, hårda mellanslag, BOM): inga i skrivfilens fyra fält.
- **Standardblocket:** rubriken samt styckena Frakt och leverans, Retur, Reklamation och Säljare (org.nr och adress) finns i alla 64. Endast två varianter förekommer (med och utan beställningsmeningen), identiska mellan produkterna.
- **Status och taggar:** status ACTIVE i alla 64, taggen texter-klara finns i alla. Handle: se begränsningar.
- **Beställningsmeningen** "Beställningsvaror kan ta upp till en vecka längre." står på exakt de produkter som har taggen På beställning live och på inga andra.
- **Förbjudna uttryck:** inga träffar på driftsvikt, "Maximum operating weight" (varken engelskt eller översatt), "Vanliga frågor", "Om märket", ursprungsland, "tillverkad i/Made in" som ursprung. Enda träffen är "tillverkad i ett stycke" i 10304 (Tunturi PU Pro, hantlarnas konstruktion enligt tillverkaren, inte ursprung). Texterna för 10021, 10024 och 10025 (omskrivna efter frågan om "Maximum operating weight") innehåller ingen användarvikt alls, bara Produktvikt. Inga säkerhets-, hälso-, effekt-, stabilitets- eller omdömespåståenden; träffar på "säker" är "Säkerhetsrem" (10342, källans utrustning), "skydd" är produkttypen Skivstångsskydd (10214), "effekt" är "Maximal effekt 1500 W" (10077, specifikation), "tål" är bara en delsträng i "stål" (10068, 10152).
- **Maxvikt och lastgräns:** förekommer i 24 av 64 texter. I alla 24 finns värdet ordagrant som svensk uppgift i produktens källa (fältet fakta i f_N_utkast.json: "Maximal användarvikt: X kg" eller "Maximal belastning: X kg"); inga tolkade eller översatta värden. Endast 10350 ("Enligt tillverkaren är maximal belastning 200 kg" i inledningen) och 10373 ("Maximal användarvikt enligt tillverkaren: 140 kg") har kvalificeringen vid vikten; i 10083 står vikten även i den ursprungliga titeln. Se punkten att avgöra nedan.
- **Märket i versaler i titlar:** inga (BH Fitness, Toorx, Tunturi, Hammer skrivs i normal skrivning).
- **Specifikationsrader:** stor bokstav efter kolon i alla rader i alla 64.
- **Längder:** titel högst 70, seo.title högst 43, metabeskrivning 70–155 tecken (kort meta enligt §14 och §17).
- **Prioriterade produkter:** 10078 (tappad mening i Retur vid första skrivningen) har nu fullständigt Retur-stycke. 10250 (saknade Märke/Retur/Reklamation vid första skrivningen) har hela blocket (Frakt, Retur, Reklamation, Säljare). 10103 och 10110 saknar pilotens FAQ, "Om märket", "stabil" och tillverkningsland. 10021, 10024, 10025 saknar användarvikt. 10211 (Roddmaskin Tunturi Star Fit R100, hela texten finns live; före-filen saknade ett bildblock men skrivfilen och live är lika).

## Punkt att avgöra (ingen avvikelse mot standard §16.3, men mot en strikt läsning av uppdraget)

Maxvikt står som "Maximal användarvikt: X kg" i specifikationer, meta och "Passar för", ordagrant ur svensk källa, men **utan** "enligt tillverkaren" vid själva vikten i 22 av de 24 texterna: 10011, 10027, 10030, 10039, 10049, 10054, 10077, 10078, 10083, 10098, 10102, 10103, 10104, 10110, 10128, 10133, 10139, 10166, 10171, 10183, 10194, 10202. (I flera av dem, till exempel 10027, 10030, 10049, 10077, 10098 och 10102, står "enligt tillverkaren" vid andra uppgifter i samma text.) Standard §16.3 säger att maxvikt återges oförändrat om källan anger den; kravet "enligt tillverkaren" gäller enligt §16.2 påståenden om bärförmåga och liknande. Om kravet ska gälla all maxvikt behövs en ändring i 22 av 64 sampeltexter, och sannolikt i motsvarande andel av alla f-batcher. Beslut hör hemma hos David.

## Begränsningar

- Jämförelsen av live-text gjordes genom att kopiera live-svaret från graphql_query till en fil och köra python mot skrivfilen. Osynliga tecken som bara skulle finnas i live (inte i skrivfilen) går inte att se på det sättet; skrivfilens fält är kontrollerade och live-texten är identisk med dem i de synliga tecknen.
- Standardblocket i live jämfördes visuellt mot den kanoniska texten (alla 64 identiska), och i kod i skrivfilen.
- Handle: det finns ingen före-fil med handle att jämföra mot. Alla handles är i det mönster Shopify bildar av originaltiteln (till exempel treadmill-bh-fitness-rx3-g6478-1), inga innehåller de nya titlarna, vilket tyder på att de är oförändrade. Status är ACTIVE.
- Befintliga taggar som inte rör texterna men ser fel ut (ändrades inte av texterna): 10039 har taggen Hybridcykel, 10373 har Pakethållare, 10285 (hantelset) har Mineraler. Skrivagenterna noterade 10039 och 10373 själva.
