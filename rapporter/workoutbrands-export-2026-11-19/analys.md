# Export Workout Brands 2026-11-19 (steg 1: produkter och kollektioner)

Källa: `wb_export.py` (bulkoperation, läsande) körd av David i Cloud Shell 2026-11-19. Rådata (`produkter.csv`, `kollektioner.csv`) ligger i Davids Cloud Shell och i sessionens arbetsyta, inte i repot.

## Produkter (15 664)
- Status: 7 380 aktiva, 8 156 utkast, 125 arkiverade, 3 olistade.
- Aktiva utan SEO-titel: 6 997 (Shopify faller tillbaka på produkttiteln). Utan SEO-beskrivning: 3 068.
- Aktiva utan könsfält ("Avsett för"): 802 (grupp utan könssignal, ca 819 i `kon_ingen_signal_819.csv`).
- Aktiva utan kategori: 26.
- Bilder utan alt-text: 46 013 av 70 475 bilder på aktiva produkter (65 %); 4 733 produkter har minst en sådan bild.
- Dubblettitlar: 161 titlar används på 346 aktiva produkter (t.ex. UC Boxer Shorts 3-Pack ×6, ZY Highbridge ×5).
- SEO-titlar över 60 tecken: 34 av 383. SEO-beskrivningar över 160 tecken: 141 av 4 312.

## Kollektioner (674)
- Utan SEO-titel: 524 (490 av dem med visningar i Search Console, tillsammans 179 660 visningar, utöver de 35 vi redan gjort).
- Utan SEO-beskrivning: 328. Med mycket kort beskrivning (<50 tecken): 85.
- Tomma kollektioner: 42, varav ca 26 har visningar (gavelo-alla-produkter 1 174, present-till-honom 543, traningsskor-kvinna 384, southpole-herr 326, db-journey 267 m.fl.).
- Misstänkt feltyp liksom hoodie-kvinna: tights-man (2 produkter, 3 092 visningar).

## Öppet
- Steg 2 (översättningstäckning) stoppade på saknad behörighet `read_locales` (+ `read_translations`); körs efter ny appversion.
