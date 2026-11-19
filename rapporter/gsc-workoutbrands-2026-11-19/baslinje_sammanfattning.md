# Search Console-baslinje Workout Brands, körd 2026-11-19 (data till 2026-11-16)

Källa: `gsc_baslinje.py` (läsande) för sc-domain:workoutbrands.com. Rådata (`vecka_sida.csv` m.fl.) ligger i Davids Cloud Shell och i sessionens arbetsyta, inte i repot. Körs om 2026-11-26 för jämförelse. Ändrade kollektioner (36) och kontrollgrupp (5) står i `info.json`.

## Per vecka (alla sidor)
| Vecka (mån) | Klick | Visningar | CTR |
|---|---|---|---|
| 2026-08-31 | 713 | 203 534 | 0,35 % |
| 2026-09-07 | 743 | 208 923 | 0,36 % |
| 2026-09-28 | 800 | 186 829 | 0,43 % |
| 2026-10-12 | 751 | 99 591 | 0,75 % |
| 2026-10-26 | 786 | 83 940 | 0,94 % |
| 2026-11-02 | 852 | 92 679 | 0,92 % |
| 2026-11-09 | 752 | 95 389 | 0,79 % |
(Veckan 2026-11-16 är ofullständig.)

Visningarna föll ca 55 % mellan början av september och oktober, klicken är i stort sett oförändrade (ca 700–850 per vecka), så CTR har fördubblats. Förändringen skedde före våra ändringar (18–19 november).

## Senaste 28 dagarna (3 134 klick, 354 962 visningar)
Per land/språk: sv 572 (18 %), it 245, de 226, en 220 (usa+gbr), pl 184, fi 171, es 170, no 127, fr 124, tr 119, cs 91, da 91, hu 76, nl 70, hr 57, sk 57, pt 47, sl 26, sr 15, is 5. Övriga länder tillsammans 441.
Enhet: mobil 2 283 klick (CTR 1,0 %, position 10,2), dator 801 (0,6 %, position 16,8), surfplatta 50.

## Slutsatser
1. Isländska (5 klick) och serbiska (15 klick) har så lite trafik att översättning inte lönar sig.
2. Turkiska ger 119 klick med hög CTR (3,2 %) men har dålig översättningstäckning (många föråldrade, hälften av kollektionerna). Värd att prioritera.
3. Italienska, tyska, polska, finska och spanska är nästa i trafik och har redan ganska hög täckning men många föråldrade kollektionsbeskrivningar.

## Indexeringsläge 2026-11-19 (`gsc_indexering.py`, URL Inspection API)
Fil: `gsc_indexering_2026-11-19.csv` (43 sidor: 38 ändrade kollektioner, 5 kontroll).
- 42 av 43 "Angiven och indexerad"; Googles canonical = vår canonical på alla 43.
- 1 ändrad kollektion (billiga-t-shirts-herr) är "Genomsökt – inte indexerad för närvarande"; senaste genomsökning 2026-06-20.
- Googles senaste genomsökning är för de flesta sidor före våra ändringar (18–19 november): bara 6 av 38 ändrade sidor har lästs om sedan 18 november. Effekten av nya titlar syns först när Google läst om sidorna.
- present-till-honom indexerades 2026-08-29 och present-till-henne 2026-10-02, båda då tomma; omläsning behövs efter regelfixen.
