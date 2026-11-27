# Search Console, Workout Brands: första uppföljning 2026-11-27

Källa: `gsc_baslinje.py` (läsande), körd av David i Cloud Shell 2026-11-27, data till och med 2026-11-24. Ändringarna (SEO-titlar på 36 kollektioner) gjordes 2026-11-18 och 2026-11-19. Rådata (`vecka_sida.csv` m.fl.) ligger i Davids Cloud Shell. Fakta = ur exporten, bedömning = tolkning.

## Fakta
Veckovis, alla språkversioner av en kollektion summerade. "Före" = snitt av veckorna 2026-10-14 till 2026-11-17 (5 veckor). "Efter" = veckan 2026-11-18 till 2026-11-24.

| Grupp | Kollektioner | Klick före | Klick efter | Visningar före | Visningar efter |
|---|---|---|---|---|---|
| Ändrade | 36 | 73 | 74 (+2 %) | 5 411 | 5 693 (+5 %) |
| Kontroll | 5 | 8 | 6 (-21 %) | 445 | 334 (-25 %) |

Viktad position, ändrade: 15,7 före (snitt av de fem veckorna: 17,0 / 15,6 / 14,7 / 15,5 / 16,3) mot 18,1 efter. Av 36 ändrade kollektioner fick 16 bättre position, resten sämre eller oförändrad.

Sajten totalt per dag: cirka 13 600 visningar före, 15 400 efter 18 november (+13 %); klick oförändrade (cirka 105 till 110 per dag).

## Bedömning
- **Ingen mätbar effekt ännu, varken positiv eller negativ.** Veckan efter ändringen är för tidig: i indexeringskontrollen 2026-11-19 hade Google läst om bara 6 av 38 ändrade sidor.
- Kontrollgruppen är för liten (6 till 18 klick per vecka) för att vara en jämförelse; en förändring på -21 % är cirka två klick.
- Positionen för ändrade sidor ligger lägre än i september, men nedgången började före 18 november (vecka 14 oktober: 17,0), så den kan inte läggas på titlarna.
- Black Friday (2026-11-27) ligger efter datafönstret.

## Nästa mätning
Kör om efter 2026-12-08 (två veckor efter ändringen, data till 2026-12-05) med `gsc_baslinje.py`, och `gsc_indexering.py` för att se hur många sidor Google har läst om. Jämför mot snittet ovan.
