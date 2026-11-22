# Search Console-baslinje för BEST OF SPORTS (bestofsports.se), 2026-11-22

Läsande körning (`gsc_baslinje.py`, egendom `sc-domain:bestofsports.se`). Data 2026-08-22 till 2026-11-19 (90 dagar, 16 veckor). **Det här är läget nu, inte före alla ändringar:** BOS har fått många ändringar sedan oktober (textutrullning, taggar, menyer, intern länkning). De tio kategoritexterna skrevs 2026-11-17, så bara tre dagar efter det ligger i data (17 till 19 november).

**Grupper:** *ändrade* = de tio kollektioner som fick ny text 2026-11-17 (motionscykel, lopband, roddmaskin, cykellas, elcyklar, tunturi, sparkcykel, crosstrainer, hantlar, kettlebell). *Kontroll* = fem kollektioner som inte fick text (cyklar, mountainbike, damcyklar, konditionsutrustning, gravelcykel).

## Hela sajten
- 90 dagar: **526 klick** och **70 572 visningar**, CTR 0,75 %. Det är i snitt cirka 40 klick och 5 000 visningar i veckan.
- Senaste 28 dagarna: 169 klick och 26 271 visningar (CTR 0,64 %). Föregående 28 dagar: 160 klick och 20 050 visningar. Visningarna ökar, men klicken är i stort sett oförändrade.
- Genomsnittlig position: 27 på mobil och 37 på dator, alltså sida tre till fyra i Googles resultat. Sverige står för 163 av 169 klick.
- Per sidtyp (16 veckor): **produktsidor 342 klick (53 %)** men bara 16 % av visningarna; **kollektioner 139 klick (22 %) men 58 % av visningarna** (51 085); blogg 134 klick (21 %); startsidan 23 klick. Av 2 514 produktsidor med data har 244 fått minst ett klick. Den mest klickade produktsidan (en Fiido-elcykel) har 14 klick.

## Ändrade mot kontroll (veckovis, viktad position)
| Vecka (start) | Alla sidor, klick / visningar | Ändrade (10), visningar / position | Kontroll (5), visningar / position |
|---|---|---|---|
| 2026-08-28 | 43 / 5 037 | 213 / 51,4 | 93 / 53,2 |
| 2026-09-25 | 48 / 4 036 | 72 / 54,7 | 15 / 46,5 |
| 2026-10-16 | 37 / 6 601 | 182 / 52,9 | 233 / 39,5 |
| 2026-10-30 | 35 / 6 128 | 91 / 66,2 | 95 / 43,1 |
| 2026-11-06 | 49 / 6 499 | 172 / 74,7 | 84 / 45,2 |
| 2026-11-13 | 43 / 7 942 | 158 / 59,1 | 60 / 46,7 |
Hela tabellen (16 veckor) finns i `vecka_sida.csv`.

## Vad det betyder
- **Organisk sökning är mycket liten idag.** Cirka 40 klick i veckan ger inget underlag för att mäta effekt i klick; vi mäter visningar och position. De tio ändrade kollektionerna ligger i snitt på position 50–75 (sida fem till åtta), och de har i princip noll klick (1 klick på 16 veckor). Att de ligger så djupt förklarar varför det är svårt att lyfta dem med enbart text.
- **Var potentialen finns:** kollektionssidorna har över hälften av visningarna men bara 22 % av klicken, så det är där ett rankinglyft ger mest. Produktsidorna står för över hälften av klicken, vilket är ett skäl att fortsätta med produkttexter, titlar och bilder (alt-text) där.
- Visningarna ökar (28 dagar +31 %), men klicken står still. Det är ett tecken på att sajten syns bredare men på sidor med låg position.
- Jämförelsen mellan ändrade och kontroll är bruten redan före 17 november (kontrollgruppen ligger på position 40–50, de ändrade på 50–75), så titta på förändring över tid, inte på nivå.

## Nästa mätningar
- 2026-12-06 (cirka tre veckor efter texterna) och 2026-12-20 (fem veckor): kör `gsc_baslinje.py` igen med flaggorna i `info.json` och jämför. Alt-text och SEO-ändringar som görs däremellan ska loggas med datum, så att de kan läsas mot kurvan.
- Black Friday (2026-11-27) påverkar visningar och klick på alla sidor.
