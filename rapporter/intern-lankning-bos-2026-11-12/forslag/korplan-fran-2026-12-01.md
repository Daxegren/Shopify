# Körplan: intern länkning, att göra från 2026-12-01 (förberedd 2026-11-17)

Underlag: Davids beslut 2026-11-17 via Översikt (se `shopify-sync/docs/BESLUTSLOGG.md`). Till och med 2026-11-30: inga strukturella liveändringar och inga skrivningar på produkter med taggen `price-change-job-active`. Varje skrivning: torrkörning, kanarie (en post först), återläsning, stopp vid första avvikelse. Avvikelse läggs under "Behöver Davids ja".

## Före 2026-12-01 (får förberedas nu, bara läsning/filer)
1. Search Console: David eller medarbetaren kör `gsc_export.py` (Cloud Shell, bara läsning). Därefter sorterar jag de 108 föräldralösa kategorierna i grupper med visningar och föreslår beslut per grupp i `108-foraldralosa-kategorier.csv` (kolumnen `beslut_david` fylls av David).
2. Brödsmula: test på en produkttyp i en opublicerad temakopia (inte publicerat tema). Publicering först från 2026-12-01 efter mätning.
3. Kategoritexter: länkar i de fem källkategorier som saknar beskrivningstext förbereds som text; skrivs inte före beslut om huvudkategori för PWO.
4. Spårningslänkar (169 st, 5 kategoribeskrivningar och bloggartiklar): lista färdig, låg prioritet.

## Från 2026-12-01 (i den här ordningen)
1. Kontrollera att taggen `price-change-job-active` är borta eller att prisjobbet är klart på de 10 cyklarna.
2. Pre-workout-pwo mot pwo-energipulver: huvudkategori blir den med flest visningar i Search Console (hämta siffror, besluta, genomför).
3. Tränings T-shirt Dam (0 produkter): finns matchande produkter, fyll via taggar; annars omdirigering.
4. 108 föräldralösa: genomför bara grupper som David granskat och godkänt.
5. Taggning av fler cyklar (Hybridcykel): bara när punkt 1 är uppfylld.
6. Publicera brödsmula efter mätning i temakopian.
7. Ommätning med `intern_lankning_mat.py`, därefter Search Console 4–6 veckor efter ändringarna (Black Week stör jämförelsen; jämför mot samma period året innan).

## Redan gjort
- Länken /collections/kona → kona-1 (2026-11-13).
- Hybridcykel-pilot på 10 produkter, brödsmula bekräftad 2026-11-13.
- Länkmeningar i 13 kategoritexter (2026-11-13).
