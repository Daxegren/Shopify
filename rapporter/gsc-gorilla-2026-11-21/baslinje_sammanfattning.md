# Search Console-baslinje för Gorilla Sports (gorillasports.se), 2026-11-21

Läsande körning (`gsc_baslinje.py`, egendom `sc-domain:gorillasports.se`). Data till och med 2026-11-18. Jämförelsepunkt före SEO-ändringarna som gjordes 2026-11-20 och -21 (se `info.json` och BESLUTSLOGG).

**Grupper:** *ändrade* = 13 innehållskollektioner som fick SEO-titel och översättningar (skivstangspaket-30-31mm, skivstang-120-200cm-30mm, roddhandtag, skivstangspaketet-hantlar-30mm, viktskivor-31mm-gummi, rehabilitering-aterhamtning, bentraning, benspark, tyst-traningsutrustning-for-hemmet, excalibur, maxxus, gyronetics-gs, presentkort). *Kontroll* = 5 kollektioner som redan hade SEO och inte ändras (skivstenger, hopprep, kabelhandtag, dipshandtag, brosttraning). De fem kampanjkollektionerna som ändrades 2026-11-21 ingår inte i någon grupp.

## Hela sajten
- 90 dagar (21 augusti till 18 november): 14 006 klick, 1 040 128 visningar, CTR 1,35 %.
- Senaste 28 dagarna: 4 065 klick och 314 099 visningar; föregående 28 dagar 4 424 klick och 330 246 visningar.
- Mobil 2 873 klick, dator 1 126, platta 66 (28 dagar). Sverige står för 3 918 av drygt 4 000 klick.
- **Veckan 2026-11-12 till -18 är ovanligt låg:** 653 klick och 74 162 visningar mot 1 121 klick och 104 012 visningar veckan före (−42 % klick). Orsaken är okänd och har inget med våra ändringar att göra (data före 2026-11-20). Kan vara Black Week-effekter, förändringar i annonsering eller ofullständiga sista dagar i Search Console. Kontrolleras vid nästa körning.

## Veckovis, ändrade mot kontroll (klick / visningar / viktad position)
| Vecka (start) | Alla sidor | Ändrade (13) | Kontroll (5) |
|---|---|---|---|
| 2026-07-30 | 1 540 / 117 082 | 2 / 255 / 4,1 | 20 / 1 434 / 8,4 |
| 2026-08-13 | 1 580 / 119 303 | 6 / 281 / 4,2 | 14 / 641 / 10,2 |
| 2026-08-27 | 1 192 / 99 228 | 0 / 194 / 5,3 | 7 / 488 / 11,8 |
| 2026-09-10 | 1 032 / 84 388 | 2 / 143 / 4,4 | 6 / 427 / 10,5 |
| 2026-09-24 | 1 210 / 94 421 | 6 / 155 / 7,6 | 5 / 452 / 8,2 |
| 2026-10-08 | 1 162 / 95 301 | 5 / 201 / 5,0 | 7 / 549 / 8,6 |
| 2026-10-22 | 1 132 / 97 169 | 4 / 210 / 7,4 | 7 / 615 / 10,3 |
| 2026-11-05 | 1 121 / 104 012 | 2 / 277 / 7,8 | 12 / 638 / 8,7 |
| 2026-11-12 | 653 / 74 162 | 1 / 109 / 10,4 | 4 / 264 / 13,3 |
Hela veckotabellen (16 veckor) finns i `vecka_sida.csv`.

## Vad det betyder för mätningen
- De 13 ändrade kollektionerna ger tillsammans bara cirka 150–280 visningar och 0–9 klick i veckan, ungefär 0,2 procent av sajtens visningar. En förändring i klick blir därför svår att skilja från vanlig variation (±5 klick per vecka). Det som går att jämföra över tid är visningar och viktad position för ändrade mot kontroll, inte absoluta klick.
- Kontrollgruppen är större i visningar (cirka 450–650 per vecka) och bör följa samma allmänna trend. Jämför förändringen i ändrade mot förändringen i kontroll, inte enskilda veckor.
- Största enskilda sidor 28 dagar före ändringen (visningar): skivstenger 820, kabelhandtag 774, hopprep 450 (alla kontroll), därefter roddhandtag 205, skivstangspaketet-hantlar-30mm 145, maxxus 140, skivstangspaket-30-31mm 122 (ändrade).
- Black Friday (2026-11-27) och Black Week påverkar jämförelsen; det gör också den låga veckan 2026-11-12. Redovisa det när resultatet läses.

## Nästa mätningar
- 2026-12-05 (två veckor efter första ändringen): kör `gsc_baslinje.py` igen med samma flaggor och jämför ändrade mot kontroll.
- 2026-12-19 (fyra veckor): slutlig jämförelse. Räkna med att effekten på de här små sidorna kan bli omöjlig att utläsa; då är resultatet "ingen mätbar effekt, ingen skada".
