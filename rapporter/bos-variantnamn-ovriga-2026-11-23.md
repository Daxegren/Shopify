# Hammer, Romet och Toorx: förslag på variantnamn och SKU-rättning (2026-11-23)

Samma metod som för Tunturi och Giant. **Förslag; inget är ändrat i Shopify.** Underlag: Shopify (varianter), synkens databas (`product_syncs`: SKU:er per produkt och Velomarkets produktnamn) och synkens namnregel (färgord översatta till svenska).

Filer: `rapporter/bos-variantnamn-ovriga-forslag-2026-11-23.csv` (71 rader), `rapporter/bos-variantstad-ovriga-2026-11-23/plan.json` (körbar plan, 28 produkter), `rapporter/bos-variantnamn-ovriga-2026-11-23.json` (Shopify-läget, 32 produkter).

## Förslaget

| Märke | Varianter med nytt namn |
|---|---|
| Romet | 26 |
| Hammer | 19 |
| Toorx | 17 |
| **Summa** | **62** (varav 10 SKU-rättningar av "Default Title"-varianter) |

Namnen följer vad som skiljer varianterna: vikt (Hammer hantlar "5 kg" till "40 kg", kettlebells "18 kg" och "22 kg", Toorx kettlebells och handleds-/ankelvikter "2 x 2,5 kg"), längd (Hammer skivstång "183 cm" och "220 cm"), färg (Toorx matta "Grön-Grå" och "Lila-Grå", ficklampa-/gummiband "Gul" och "Röd") och storlek (Romet cyklar, "M / Svart"). Estniska och engelska färgord översätts.

## Manuella fall (9 rader, 4 produkter)

Fyra Romet-produkter har två SKU:er med **samma storlek** i databasen (till exempel `28200712-A` och `28200712-B`, båda L): Art Deco Lux (blå och svart), Art Deco Classic, Vintage Eco D och Rambler R6.0 JR. Vad som skiljer SKU:erna (A/B/C: ram, hjulstorlek eller utförande) står inte i databasen, och Shopify avvisar två varianter med samma namn. De lämnas orörda tills Velomarkets attribut är kända.

## Pris

Variantpriserna rörs inte. Flera produkter har olika priser på varianter som troligen hör till en annan SKU; det tas efter 2026-12-01.

## Beslut som behövs

1. **Godkänn de 62 namnen och 10 SKU-rättningarna** (28 produkter). Kanarie på en produkt, sedan resten, med före-fil och återläsning som för Tunturi och Giant.
2. **De fyra Romet-produkterna:** lämna som de är, eller be Velomarket om attribut för A/B/C?
3. **Övriga märken** (73 av 209 flaggade produkter är nu behandlade eller föreslagna: Tunturi, Giant, Hammer, Romet, Toorx). Resten är mindre märken (Bookman, Christopeit, Liv, Gymstick, Spokey med flera). Ska jag ta dem samlade nästa?
