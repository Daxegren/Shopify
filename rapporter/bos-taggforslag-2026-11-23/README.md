# BOS: taggförslag för att fylla små kollektioner (2026-11-23)

Skapad efter Davids ja ("Ja, ta fram listorna"). **Läsning bara; inget är taggat.** Fil: `taggforslag.csv` (kollektion, tagg att lägga till, produkt-id, titel, märke, lager, om produkten har `price-change-job-active`). Alla produkter är aktiva med lager över 0 och ligger inte redan i kollektionen. Tagg som läggs till är en av kollektionens befintliga regeltaggar, så kollektionsreglerna ändras inte.

| Kollektion | Tagg att lägga till | Köpbara i dag | Förslag | Varav utan prisjobbstagg | Köpbara efter (alla) | Köpbara efter (utan prisjobbsprodukter) |
|---|---|---|---|---|---|---|
| hantelset | fasta hantlar paket | 0 | 15 | 5 | 15 | 5 |
| power-rack | power rack | 3 | 5 | 0 | 8 | 3 |
| wall-ball-1 | wall ball | 3 | 2 | 1 | 5 | 4 |
| battle-rope | battle rope | 2 | 3 | 0 | 5 | 2 |
| plyobox | plyobox | 3 | 5 | 0 | 8 | 3 |
| vattenflaska | vattenflaska | 1 | 4 | 4 | 5 | 5 |
| boxningstillbehor | boxningstillbehör | 2 | 15 | 15 | 17 | 17 |
| staende-boxningssack | stående boxningssäck | 1 | 4 | 0 | 5 | 1 |

(Köpbara i dag enligt fas 1-underlaget. Efter-kolumnerna är beräknade, inte verifierade; en omkörning av underlaget görs före skrivning.)

## Beslut som behövs

**1. Prisjobbstaggen.** De flesta förslagen har `price-change-job-active`. Regeln är att produkter med taggen inte skrivs. David gjorde ett uttryckligt undantag för alt-texten (2026-11-23). Att lägga till en tagg ändrar varken pris eller status, men jag vet inte hur prisjobbet hanterar produktens taggar (rensar det taggar eller bara sin egen?). Utan prisjobbsprodukterna når bara hantelset, vattenflaska och boxningstillbehör fem köpbara; de andra fem gör det inte. Alternativ: (a) tagga alla förslag, med före-fil och återläsning av pris, status och taggar; (b) tagga bara de utan prisjobbstagg och vänta med resten tills jobbet är klart; (c) tagga inget.

**2. Granskning av enskilda produkter** innan skrivning:
- `staende-boxningssack`: "Boxningsdocka Tunturi Free Stand" är en boxningsdocka, inte en säck. Jag rekommenderar att den stryks (då blir kollektionen 4 köpbara och faller under gränsen).
- `power-rack`: "Träningsstation BH Fitness Power Cage och Lat Pull Down" är en kombinerad station.
- `hantelset`: tre produkter är kombinationer av hantel- och skivstångsset.
- `boxningstillbehor`: namnet stämmer nu med innehållet (handskar, tassar, innerhandskar); hopprepen finns kvar.

**3. Inte med i listorna:** `rak-bank` (namn-/regelfall, ska hanteras som träningsbänkar efter kontroll mot den kollektion som redan finns), samt `sandsack`, `bankpress` och `viktskivstall` (för få passande produkter; kandidater för arkivering och omdirigering). Search Console: 14, 7 respektive 31 visningar de senaste 28 dagarna. Interna länkar till dem är inte kontrollerade än.

## Så skrivs det (efter ja)

Kanarie på en kollektion (hantelset), före-fil med tagg, pris, status och handle per produkt, `tagsAdd` per produkt, återläsning (tagg tillagd, pris, status och handle oförändrade), stopp vid första avvikelse, därefter resten i grupper om 5. Ångra: `tagsRemove` med samma lista. Därefter kör jag om underlaget och tar fram texter för de kollektioner som når fem köpbara, med ditt godkännande per text.
