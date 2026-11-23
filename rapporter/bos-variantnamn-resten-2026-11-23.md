# Resterande märken: förslag på variantnamn och SKU-rättning (2026-11-23)

Samma metod som för Tunturi, Giant, Hammer, Romet och Toorx, samlat för de 31 övriga märkena (97 produkter). **Förslag; inget är ändrat i Shopify.** Underlag: Shopify, synkens databas (`product_syncs`: SKU, storlek, färg, vikt per produkt) och synkens namnregel (svenska färgord).

Filer: `rapporter/bos-variantnamn-resten-forslag-2026-11-23.csv` (rader per variant), `rapporter/bos-variantstad-resten-2026-11-23/plan.json` (körbar plan, 62 produkter), `rapporter/bos-variantnamn-resten-2026-11-23.json` (Shopify-läget).

## Förslaget

- **163 varianter får nytt namn** i 62 produkter, varav **30 SKU-rättningar** av "Default Title"-varianter som bar en annan variants SKU.
- Märken med flest: Liv (cyklar), Kona, Bookman, Stiga, Fila (skor, storlekar 37 till 44), Christopeit, TENWAYS, Spokey, AXA, Excelsior med flera.
- Exempel: Fila-skor "40" och "40,5" (ur SKU-suffix), Christopeit/Gymstick-vikter "1 kg" till "10 kg", Liv-cyklar "S / Lila" i stället för "S / purple", Bookman-lyktor "Svart" och "Blå".
- Pris rörs inte (tas efter 2026-12-01).

## Manuella fall (utan förslag)

- **Gorilla Sports Norden (12 produkter)** och **Gymstick (5 produkter)** finns inte i Velomarket-databasen, så deras SKU:er och attribut kan inte avgöras där. Gorillas varianter heter redan "Orange" och "Silver" (giltig svenska) och är inte fel. Gymsticks koder ("BL", "PI", "WH") hör till `ftp-product-sync` och behöver ett eget förslag.
- **Cirka 45 rader** där databasen inte skiljer SKU:erna åt (samma färg eller storlek på flera SKU:er, eller attribut saknas): TENWAYS (elcyklar), BLB (fixiecykel), SOKE (stunt), AXA (vajerlås), Basil, Tabou, Lazer, Kona, Trec, Liv Tempt E+, Christopeit hantlar och kettlebell, Selle Monte Grappa, Bookman reflexer, Bottecchia. De lämnas orörda tills Velomarkets attribut är kända.

## Beslut som behövs

1. **Godkänn de 163 namnen och 30 SKU-rättningarna** (62 produkter). Kanarie på en produkt, sedan resten, med före-fil och återläsning.
2. **Manuella fall:** lämna som de är, eller be Velomarket om attribut för TENWAYS, BLB, SOKE, AXA med flera?
3. **Gymstick (`ftp-product-sync`):** ta ett eget förslag för deras variantkoder (BL/PI/WH osv.) och en liknande översättning i deras synk?
