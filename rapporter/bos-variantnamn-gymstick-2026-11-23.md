# Gymstick: variantnamn (analys och förslag, 2026-11-23)

Gymstick-produkterna hanteras av `ftp-product-sync` (inte Velomarket-synken). **Inget är ändrat.**

## Orsak (kod läst)

`sync-products` sätter variantnamnet till **SKU-suffixet** (`option1: v.suffix`, rad ~902 och ~1062): "BL", "PI", "WH", "10", "5", "S/M". Befintliga varianters namn skrivs inte om vid vanlig uppdatering (bara nya varianter får suffixet), så namn rättade i Shopify står kvar, men **nya varianter får fortfarande rå kod**.

## Läge

335 aktiva Gymstick-produkter, 94 med flera varianter och 447 varianter med kod eller tal som namn. Vanligaste namn: bara tal ("10", "5", "4", "20"), färgkoder ("BL" = blå, "PI" = rosa, "WH" = vit, "BLU", "TU"), storlekar ("S", "M/L", redan rätt) och andra koder ("MS", "WM", "GB", "LI", "AB", "FB").

## Förslag (`rapporter/bos-variantnamn-gymstick-forslag-2026-11-23.csv`)

- **Färgkoder** översätts säkert (BL → Blå, PI → Rosa, WH → Vit ...).
- **Tal** ("10", "15") får enhet ur produkttiteln (kg, cm, mm) som *förslag att granska*: enheten kan bara läsas ur titeln och blir fel ibland (till exempel "01 mm" för ett halsband). Dessa kräver granskning per produkt.
- **Okända koder** ("MS", "WM", "GB", "LI") och "Default" lämnas till manuell hantering; Gymsticks produktinformation (XLSX) har rätt namn.

## Rekommendation

1. Ändra `sync-products` så att suffixet översätts via en tabell (färgkoder) och så att tal får enhet ur Gymsticks produktinformation (XLSX), i en PR i `ftp-product-sync` (kräver `PRODUKT.md`-uppdatering, tester och deploy via Lovable).
2. Först därefter rätta befintliga varianter i butiken, med samma metod som för Velomarket-produkterna (före-fil, kanarie, återläsning).

## Beslut som behövs

1. Ska jag göra synkändringen (PR i `ftp-product-sync`) och ta fram en granskningsbar lista per produkt för talen?

## Rättelse 2026-11-23 (tillägg; ursprungstexten ovan är oförändrad)

I analysen ovan står "BL = blå". Det är fel: **BL är svart och BLU är blå**. Båda finns på samma produkt (Air Track har varianterna BL, BLU och PI), och shakern med BL, PI och WH har handle `shakerflaska-600ml-svart`. Övriga koder som kunde verifieras: PI = rosa, WH = vit, TU = turkos (Cohesive Tape heter "Turkos"), BE = beige, CAM = kamouflage. CSV-filen `bos-variantnamn-gymstick-forslag-2026-11-23.csv` har den felaktiga tolkningen av BL och ska inte användas för skrivning. PR i `ftp-product-sync` använder de rättade koderna.

## Gymstick-lista efter deploy (2026-11-23)

Deployen av `sync-products` (PR 26) är gjord, så nya varianter får svenska namn. För **befintliga** varianter: `rapporter/bos-variantnamn-gymstick-forslag-2026-11-23.csv` (447 varianter i 94 produkter, rättad tolkning: BL = Svart) och `rapporter/bos-variantstad-gymstick-2026-11-23/plan.json` (körbar plan).

| | Antal |
|---|---|
| Varianter med säkert förslag | **97** (28 produkter) |
| varav färgkoder (BL → Svart, BLU → Blå, PI → Rosa, WH → Vit, TU → Turkos, BE → Beige, CAM → Kamouflage) | 31 |
| varav tal + kg i viktprodukter (hantlar, viktskivor, bumper plates, aerobic bar m.fl.) och tal + cm som står i titeln (Core Roller 45 och 90 cm) | 66 |
| Manuella (ingen säker tolkning) | 350 |

Manuella är bland annat tal där enheten inte går att läsa ur titeln (Gummigolv "6", "8", "30", "40" är tjocklek i mm, inte cm; jag har uteslutit dem) och koder som "MS", "WM", "GB", "03BL", "1,25PU". Rätt namn finns i Gymsticks produktinformation (XLSX), som jag inte kan läsa härifrån. Variantvikterna i Shopify är 0 kg och kan inte användas som kontroll.

Pris rörs inte.

## Beslut som behövs

1. **Godkänn de 97 namnen** (28 produkter): kanarie på en produkt, sedan resten, med före-fil och återläsning.
2. **De 350 manuella:** de kräver Gymsticks XLSX. Ska jag lägga till en funktion i `ftp-product-sync` som läser variantnamn ur produktinformationen (PR), eller lämnar vi dem?
