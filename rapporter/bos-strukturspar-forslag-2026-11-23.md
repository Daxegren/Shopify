# BOS strukturspåret: förslag efter fas 1 (2026-11-23)

Skapad efter Davids ja ("Ja på alla fyra", 2026-11-23). Detta är förslag och underlag. **Inget är ändrat i Shopify.** Varje ändring kräver ett separat ja, och avpublicering görs av David i admin.

## A. Fel i kollektioner som fick text i fas 1

| Kollektion | Fel | Förslag |
|---|---|---|
| skivstang-30-mm | Toorx Olympic Barbell (50 mm) ligger i kollektionen (taggstyrd) | ta bort taggen som släpper in den, eller lägg ett undantag i regeln; kontrollera att den ligger i skivstang-50-mm |
| skidor | skridskor (Alpina T 40), isskor/broddar (ANTi SKid Sole, Winter-Grip) och cykelstänkskärmar (SKS Bluemels) | ta bort felaktiga taggar så att de hamnar i rätt kollektioner (skridskor, broddar, cykeltillbehör); texten påstår inget fel tack vare "bland annat" |
| skidstavar | Rex-skidstavar ("Skidstav Rex Omega i Glasfiber", "Barnskidstavar Rex Apollo, Glasfiber") ligger i skidor men inte i skidstavar | lägg till taggen så att de når skidstavar; därefter kan skidstavar få text |

## B. Namn och innehåll stämmer inte

| Kollektion | Läge | Förslag |
|---|---|---|
| hopfallbar-gymutrustning | 9 hopfällbara cyklar och elcyklar (ADO, Romet, COAST, Fiido) | byt namn/handle (med omdirigering) till hopfällbara cyklar eller slå ihop med cykelkollektionen |
| pjaxor | 9 produkter: pjäxor, skidor och skridskor | begränsa regeln till pjäxor; skidor och skridskor till egna kollektioner |
| boxningstillbehor | 13 i kollektionen, bara 2 köpbara (hopprep) | byt namn (hopprep) eller lägg rätt produkter i; flera boxningsprodukter är utkast |

## C. Små kollektioner (läst live 2026-11-23: status och lager)

"Köpbar" = aktiv med lager över 0.

| Kollektion | Läge | Slutsats |
|---|---|---|
| hantelset | 5 aktiva Hexagonhantlar, alla lager 0 | slutsålda; text efter påfyllning (kräver minst 5 köpbara) |
| power-rack | 3 aktiva Tunturi i lager (1, 2 och 3 st), 3 utkast | vänta; lagret är mycket litet |
| boxningstillbehor | se B | namnfråga |
| viktskivstall | 1 köpbar, 2 utkast, 2 aktiva utan lager | vänta eller slå ihop med viktskivor |
| wall-ball-1 | 3 köpbara, flera utkast | vänta; flera utkast kan aktiveras om de är avsedda att säljas |
| battle-rope | 2 köpbara, 3 utkast | slå ihop med närliggande kollektion |
| staende-boxningssack | 1 köpbar (Toorx), 3 utkast, 2 arkiverade | slå ihop med boxningssäckar |
| sandsack | 2 köpbara, 3 utkast | slå ihop med viktsäckar |
| plyobox | 3 köpbara, 1 aktiv utan lager | vänta |
| bankpress | 1 köpbar, 4 utkast | slå ihop med bänkar |
| rak-bank | 3 köpbara, kabelstänger inräknade, 5 utkast | rensa regeln (kabelstänger hör inte hit) och slå ihop med träningsbänkar |
| vattenflaska | 1 köpbar (shaker), 2 aktiva utan lager | slå ihop med shakers/flaskor |

Gemensamt mönster: många produkter är **utkast (DRAFT)** med lager 0. Om utkasten är avsedda att säljas igen räcker det att aktivera dem för att nå fem köpbara. Det är ett affärsbeslut för David (inte något jag ändrar).

Avpublicering eller omdirigering av en kollektion görs av David i admin. Innan dess ska varje kandidat kontrolleras mot Search Console (position och visningar) och interna länkar.

## D. fria-vikter

Bred överkategori (172 köpbara). Vänta till fas 3 (intern länkning) och skriv navigeringstext då.

## E. Tillägg efter Davids besked (2026-11-23): fyll kollektionerna innan något arkiveras

David: Gorilla Sports-produkter hör hemma i BOS och kan ligga i kategorierna; arkivera och omdirigera bara när inga andra produkter, från något varumärke, passar. Jag har därför sökt i hela butiken (läsning, aktiva produkter med lager över 0) efter produkter som passar varje kollektion men inte når den. Kollektionerna styrs av taggar, så produkter med passande titel saknas när taggen inte finns. Det här är **förslag**: att lägga till taggar är en produktändring som kräver eget ja, och produkter med `price-change-job-active` ska behandlas enligt gällande regel.

| Kollektion | I kollektionen i dag (köpbara) | Passande aktiva produkter med lager i butiken (urval) | Förslag |
|---|---|---|---|
| hantelset | 0 | minst 12 produkter med "Hantelset" i titeln: Tunturi (flera), Toorx, Gymstick och Gorilla Sports Norden ("Skivstång och Hantelset, 23 kg") | fyll via tagg; når med god marginal 5 |
| power-rack | 3 | Tunturi Half Rack, BH Fitness (Power Rack, Power Cage, Power Cage med Lat Pull Down); Gorilla Sports Norden har 7 racks men alla är utkast med lager 0 | fyll via tagg (4 till, med BH Fitness och Half Rack); GS-racks aktiveras först om de ska säljas |
| wall-ball-1 | 3 | Tunturi Väggboll 10 kg och Wall Ball 6 kg, Gymstick Wall Ball, Gorilla Sports Norden Wall Ball Paket | fyll via tagg |
| battle-rope | 2 | Tunturi (3 rep, väggfäste, markankare), Gymstick Battle Rope Mount | fyll via tagg; avgör om tillbehör ska med |
| plyobox | 3 | Tunturi (3), Gymstick (2) | fyll via tagg; når 8 |
| sandsack | 2 | 3 Gorilla Sports Norden (Powerbag, Bulgarian Bag), inga andra märken | **för få**: slå ihop med viktsäckar/ta bort, om inte fler produkter aktiveras |
| staende-boxningssack | 1 | Tunturi, Toorx, MAXXUS, Gorilla Sports Norden (Body Opponent Bag, E-Series); flera hänger | fyll via tagg, men håll isär stående och hängande säckar; granska titel för titel |
| rak-bank | 3 | 30+ träningsbänkar (Tunturi, Hammer, Finnlo, Christopeit, BH Fitness m.fl.) | kollektionen är i praktiken **träningsbänkar**; byt regel/namn (kolla mot den befintliga träningsbank-kollektionen först så att de inte dubblerar varandra) |
| bankpress | 1 | 2 Tunturi-bänkar | **för få**: slå ihop med träningsbänkar och omdirigera |
| viktskivstall | 1 | 2 Gorilla Sports Norden-viktställ (varav ett redan i kollektionen) | **för få**: slå ihop med hantel-/skivställ eller aktivera utkast |
| vattenflaska | 1 | Gymstick (3 flaskor, mycket lager), Trec, Nils Extreme, Elite, GS Shaker | fyll via tagg; cykelflaskhållare ska inte med |
| boxningstillbehor | 2 | ca 30 boxningsprodukter (handskar, tassar, innerhandskar, väggfäste m.m.) från Tunturi, Toorx, Hammer, Gymstick | fyll via tagg; når med god marginal |

Slutsats: av 12 kollektioner kan **9** fyllas så att de når fem köpbara, och **3** (sandsack, bankpress, viktskivstall) har för få passande produkter och är kandidater för arkivering/omdirigering enligt Davids regel (efter kontroll av Search Console och interna länkar). `rak-bank` är ett namn-/regelfall.

Nästa steg: ett tagg-förslag per kollektion (lista över exakta produkter att tagga) som David godkänner före skrivning. Ingen ändring är gjord.
