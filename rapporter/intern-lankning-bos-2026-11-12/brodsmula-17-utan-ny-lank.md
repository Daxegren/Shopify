# De 17 av 48 testprodukter som inte fick en ny brödsmulelänk (2026-11-13)

Underlag: produkternas kollektionstillhörighet och huvudmenyns uppbyggnad, båda lästa ur Shopify (bara läsning, BEST OF SPORTS) 2026-11-13. Orsaken är bedömd av Claude utifrån det underlaget; reglerna bakom kollektionerna (manuella eller regelstyrda) kunde inte läsas (anslutningen föll).

## Hur koden väljer
Brödsmulan väljer först den första av de sju huvudgrenarna i menyn (Cyklar, Gymutrustning, Kondition, Kosttillskott, Övrig utrustning, Träningskläder, Varumärken) som produkten är medlem i, och letar sedan efter en underkollektion **bara under den grenen**. Det går fel när produkten är medlem i en specifik kollektion (till exempel Träningsbänk) men inte i huvudkollektionen ovanför (Gymutrustning), eller när mellannivån (Protein) saknar medlemskap.

## Orsak A: produkten tillhör en specifik menykollektion, men koden hittar den inte (5 av 17)
Kan rättas i temakoden utan att röra katalogen.
| Produkt | Medlem i (urval) | Menykollektion som missas |
|---|---|---|
| Ljussats AXA Niteline T1 | varumarke, tillbehor | Cykelbelysning (under Cyklar) |
| Boxningshandskar Toorx Jaguar | konditionsutrustning, boxning | Boxning (under Gymutrustning > Funktionellt) |
| Proteinbar Trec Peanut Caramel | kosttillskott, proteinbars | Proteinbars (under Kosttillskott > Protein; mellannivån Protein saknas) |
| Solglasögon Shimano S23X | varumarke, cykelsolglasogon, solglasogon | Cykelglasögon, Solglasögon |
| Träningsbänk Finnlo by Hammer Tricon | konditionsutrustning, traningsbank, hemmagym | Träningsbänk (under Gymutrustning > Hemmagym) |

## Orsak B: bara en varumärkeslänk skulle visas (3 av 17)
Kona Dew, Giant AnyTour RS 3 och Giant Roam 2 är hybridcyklar. Kollektionen `hybridcykel` finns men är inte i menyn; Kona och Giant finns under Varumärken. Med en bättre kodregel skulle de få varumärkeslänken, men ingen ämneslänk förrän `hybridcykel` läggs i menyn.

## Orsak C: produkten saknas i den specifika kollektion den uppenbart hör till (9 av 17)
Rättas i katalogen (eller i reglerna för kollektionerna), inte i koden.
| Produkt | Medlem i | Saknas i |
|---|---|---|
| Barncykel Academy Grade 2, 14" | cyklar | Barncykel (barncyklar, barncyklar-2-4-ar-12-14) |
| Skivstång Hammer Maximum PRO | konditionsutrustning, hammer | Skivstång (skivstang) |
| Minicykel Tunturi Cardio Fit M35 | konditionsutrustning, tunturi | Motionscykel |
| Träningsstation Toorx CSX-2000 | konditionsutrustning, toorx | Träningsmaskin |
| Gymnastikgummi Toorx Elastic | konditionsutrustning, toorx | Gummiband |
| Golvskyddsmatta BH Fitness | konditionsutrustning, bh-fitness | Gymgolv |
| Styrkepaket Explosiv | gymutrustning, gympaket-1 | Gympaket (menyn länkar `gympaket`, produkten ligger i `gympaket-1`) |
| Knäskydd Boom Basic | tillbehor, varumarke | en passande skydds-/barnkollektion |
| Chinsgrepp till Tunturi RC20 Pro | konditionsutrustning, **pakethallare-cykel** | Chins & Dips; **felaktigt medlem i en cykelkollektion** |

## Slutsats (bedömning)
- Stickprovet är jämnt fördelat över huvudkategorierna och inte representativt för hela katalogen, så andelen (17 av 48) kan inte räknas upp till hela sortimentet. Men 9 av 48 produkter (19 %) i stickprovet saknar sin uppenbara specifika kollektion, och minst en är felplacerad.
- Förslag i ordning: (1) kodregel version 2 som söker i hela menyträdet och hanterar saknad mellannivå: löser orsak A och ger varumärkeslänk vid B; (2) katalogkontroll av medlemskap för orsak C (mät först hur många produkter per specifik kollektion som saknas, bygg ingenting förrän David beslutat); (3) lägg `hybridcykel` i menyn eller besluta om strukturen.
