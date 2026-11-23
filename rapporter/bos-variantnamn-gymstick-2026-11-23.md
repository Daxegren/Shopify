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
