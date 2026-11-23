# BOS: prisjämförelse efter variantstädningen (2026-11-23)

Läsande jämförelse mellan Shopifys variantpriser och synkens databas (`product_syncs.shopify_price` per SKU) för 275 av de städade Velomarket-SKU:erna (Tunturi, Giant, Hammer, Romet, Toorx och resterande märken). **Inga priser är ändrade.** Underlag: `rapporter/bos-priser-shopify-2026-11-23.json`.

## Resultat

- De flesta **Giant-varianter ligger 10 till 24 % under** databasens pris (till exempel TCR Advanced SL 0 DA: 124 046 kr mot 158 169 kr). Mönstret stämmer med kampanjpriser: produkterna har taggen `price-change-job-active` och Black Friday pågår. Jämförelsen blir rättvisande först efter kampanjen, därför körs den om 2026-12-01 (påminnelse inlagd).
- **Avvikande rader** som inte går att förklara med kampanjen:
  - `1031003247` Defy Advanced 2 (L): 38 690 kr mot 19 589 kr (+98 %).
  - `1082008385` Roam 1 (M): 16 631 kr mot 9 369 kr (+78 %).
  - `5028032107` Trance X Advanced E+ Elite 2 (L): 72 179 kr mot 106 479 kr (-32 %).
  - `24TCFT3000` Löpband Cardio Fit T30, den nyare modellen: **0,00 kr** mot 9 109 kr (-100 %). Lager 1, lagerpolicy DENY, alltså går den att köpa för 0 kr så länge lagret finns.
- Tunturi, Hammer, Toorx, Gymstick och de mindre märkena visar få eller inga avvikelser över 5 % i urvalet.

## Löpbandet (Cardio Fit T30)

Utredning ur öppna källor (butiker och Tunturis egen sida): modellen finns i två versioner, 16TCFT3000 (äldre) och 24TCFT3000 (nyare, EAN 8717842036730), och uppgifterna om motor, maxvikt och program skiljer mellan butiker. Variantnamnen sattes därför efter version: "Äldre modell" (SKU 16TCFT3000) och "Nyare modell" (SKU 24TCFT3000). Streckkoden på den äldre varianten står fortfarande på den nyares EAN och rättas av synken vid nästa uppdatering. **0-kronorspriset är inte rättat** (pris före 2026-12-01 kräver ditt ja): jag rekommenderar att sätta det till databasens 9 109 kr nu, eftersom varianten går att köpa för 0 kr.

## Beslut som behövs

1. **Löpbandets 0 kr:** sätta 9 109 kr nu (rekommenderas), eller vänta till 2026-12-01.
2. **Avvikande Giant-rader (+98 %, +78 %, -32 %):** kontrolleras mot Velomarket den 1 december och rättas efter ditt ja.
