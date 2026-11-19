# Översättningstäckning Workout Brands (2026-11-19)

Källa: `wb_export.py --bara oversattning` (läsande), 19 språk, produkter (15 664 inkl. utkast) och kollektioner (674). Siffrorna är antal översatta fält, inom parentes antal föråldrade (källtexten ändrad efter översättningen). Rådata: `oversattning_sammanfattning.csv` (i Davids Cloud Shell).

## Produkter
- Titel: 8 200–10 500 av 15 664 översatta per språk (pl bäst 10 487, is sämst 6 736). Föråldrade: ca 600–850 per språk, men sr och tr ca 2 300.
- Beskrivning (body_html, källa 10 758): 5 170 (is) till 8 698 (en) översatta. Föråldrade: ca 450–650, sr och tr ca 1 325.
- SEO-titel (källa 409): 14–279 översatta; de bäst (279), is/sl/sr sämst (14–17).
- SEO-beskrivning (källa 4 362): en 4 116, pl/da/fi ca 2 950; sr 398 och tr 336 sämst.

## Kollektioner
- Titel: en 623, pl 591, de 495; **is bara 4 av 674**; sr 327, tr 318.
- Beskrivning (källa 665): en 566 men 335 föråldrade (59 %); övriga språk 60–70 % föråldrade; is 4.
- SEO-titel (källa 171): en 165, de 74, fr 22, sr/tr 6, is 4.
- SEO-beskrivning (källa 355): en 328, da 264, pl 246; is/sr/tr 4.

## Slutsatser
1. Isländska kollektioner (och till stor del sr och tr) är i praktiken oöversatta.
2. Cirka 60–70 % av kollektionsbeskrivningarna är föråldrade på alla språk, och ca 5 % av produkttitlarna (sr/tr 15 %).
3. Procenten för produkter gäller alla 15 664 produkter inklusive utkast; täckningen för de 7 380 aktiva är sannolikt högre.
4. Prioritering bör följa trafik per land (Search Console-baslinjen, `land.csv`) innan något översätts.
