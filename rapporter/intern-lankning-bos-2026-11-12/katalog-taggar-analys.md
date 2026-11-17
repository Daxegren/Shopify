# Katalogen: varför 35 % av produkterna saknar ämneslänk i brödsmulan (2026-11-13)

Underlag: kollektionernas definitioner lästa ur Shopify (bara läsning), produkternas medlemskap härlett ur kollektionssidorna i länkmätningen, och titlarna på 1 345 produkter som efter regel v2 saknar ämneslänk. Inget är ändrat i butiken.

## Orsaken
- Kollektionerna är i huvudsak **regelstyrda via produkttaggar**: av 350 kollektioner har 272 enbart taggregler (277 taggvillkor, 18 leverantörsvillkor, 5 titelvillkor, 4 prisvillkor), 78 har andra regler eller är manuella. Exempel: `skivstang` = taggar "skivstång" eller "skivstänger" (42 produkter); `barncyklar` = "Barncyklar", "Barncykel", "kids bikes", "kid bikes" (141 produkter); `hybridcykel` = "hybrid", "hybridcykel" (125); `gummiband` = "gummiband", "motståndsband" (30).
- En produkt hamnar alltså i en kollektion bara om den har rätt tagg. Saknas taggen saknas medlemskapet, och då kan varken brödsmulan, sidomenyn eller kollektionssidan länka dit. Exemplen från de 17 sidorna (en barncykel som bara ligger i "Cyklar", en skivstång som inte ligger i "Skivstång") är därför troligen saknade taggar, inte fel i kollektionen.

## Förslag (att granska, inte att köra)
`brodsmula-sim/forslag-taggar.csv`: för 557 av de 1 345 produkterna innehåller titeln en tagg som en ämneskollektion i menyn använder (minst 5 tecken, ordstart), men produkten ligger inte i kollektionen. Kolumner: produkt, titel, nuvarande huvudgren, föreslagen kollektion, tagg att lägga till. De berör 59 kollektioner; flest: hopfallbara-cyklar 107, barncyklar 64, viktskivor 31, hantlar 26, foam-roller-massageboll 25, cykelhjalmar 24, flaskhallare 22, traningsboll 21, traningsbank 21. För 788 produkter finns ingen träff.

**Förslaget är en grov heuristik.** Titelmatchen kan ge falska träffar: till exempel matchade en bandstrap `kabelmaskin` för att titeln nämner kabelmaskin som användningsområde. Varje rad ska ses över av någon som kan sortimentet innan en tagg läggs till.

## Risker med att lägga till taggar
- Taggar används även av filter, sök, feeds och annonser; en tagg som läggs till flyttar produkten in i kollektionen direkt, inklusive i sidomenyn och på kategorisidan.
- Under Black Friday bör inga massändringar göras av produktdata. Taggar går att ta bort igen (en tagg per produkt per kollektion).
- Rekommendation: en pilot på en kollektion, till exempel `hybridcykel` (10 produkter i förslagen) efter granskning, mät effekten på brödsmula, kollektionens produktantal och länkmätningen, och rulla ut efter kampanjen.

## Ytterligare fynd
Fem kollektionsbeskrivningar har interna länkar med spårningsparametrar (`_pos`, `_psq`, `_ss`, `_v`): `produkter-mot-ryggont`, `lopband-med-lutning`, `lopband-med-skarm`, `hopfallbara-lopband`, `traningsutrustning-for-hemmagym`. Det stämmer med de fem kollektionssidor som länkmätningen räknade i (f). Att rensa dem är en textändring i kollektionens beskrivning.
