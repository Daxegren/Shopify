# Granskningsutlåtande k_36a och k_36b (2026-11-06)

Granskaren har bara läst i Shopify och inte ändrat något där. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient) mot BEST OF SPORTS på bestofsports.se. Underlaget är `regler-v1.md` (R1, R3, R4, R12a, v1.5–v1.10), LARDOMAR, butiksprofilen, BESLUTSLOGG (dubblettdefinitionen från 2026-11-05 och slutomgången 2026-11-06), formatet i `k_utlatande_35cd.json` och `skrivfil_kontroll.py`, som gav 0 fel på båda utkasten.

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_36ab.json`.

## Resultat

| nr | id | fil | dom |
|---|---|---|---|
| 36002 | 10530213921034 | k_36a_utkast | RÄTTA |
| 36102 | 10636737184010 | k_36b_utkast | GODKÄND |
| 36001 | 10665228173578 | k_36a_avvisade | Avvisningen står |
| 36003 | 10565633638666 | k_36a_avvisade | Avvisningsskälet är fel (ingen dubblett), men produkten kräver beslut |
| 36004 | 10682105987338 | k_36a_avvisade | Avvisningsskälet är fel (ingen dubblett), men produkten kräver beslut |
| 36005 | 10682106052874 | k_36a_avvisade | Avvisningsskälet är fel (ingen dubblett), men produkten kräver beslut |
| 36006 | 10656688341258 | k_36a_avvisade | Avvisningen står (exakt dubblett) |
| 36007 | 10665225978122 | k_36a_avvisade | Avvisningen står (exakt dubblett) |
| 36008 | 10665226010890 | k_36a_avvisade | Avvisningen står (exakt dubblett) |
| 36009 | 10656691618058 | k_36a_avvisade | Avvisningen står (elektronik) |
| 36101 | 10636706349322 | k_36b_avvisade | Avvisningen står (varianterna är olika artiklar) |

## 36002 Gravelcykel Kona Libre 2026: RÄTTA

Live: ACTIVE, en variant (B37LBGYSHFA52), 38 019 kr, lager 0, med taggen På beställning. Alla fakta står i egen källa. Leveranstidsmeningen finns och standardblocket är exakt. Meta är 140 tecken. Produkten är ingen dubblett: syskonet 10488282251530 har andra storlekar (FA48/50/54/56/58).

| fält | före | efter |
|---|---|---|
| titel | Gravelcykel Kona Libre 2026, 700c, Blank Metallic Kolgrå | Gravelcykel Kona Libre 2026, 700x45c, Gloss Metallic Charcoal |
| seo_title | Gravelcykel Kona Libre 2026, Kolgrå | Gravelcykel Kona Libre, Metallic Charcoal |
| html | `<li>Färg: Blank Metallic Kolgrå</li>` | `<li>Färg: Gloss Metallic Charcoal</li>` |

Skäl: Konas färgnamn behålls i alla 40 skrivna Kona-titlar, till exempel "Gloss Metallic Charcoal (Grå)" och "Libre, 700x45c, Winter Sky". Den halvöversatta formen "Blank Metallic Kolgrå" bryter mot det. "700c" står inte i källan, men "700x45c" gör det. Efter rättningen har titeln 61 tecken och 2 kommatecken och SEO-titeln 41 tecken. Båda är unika.

## 36102 Viktskivor Trigrip 51 mm, 6 x 5 kg: GODKÄND

Alla uppgifter står ordagrant i leverantörens originaltext (`facit30-original.json`). Texten har ingen FAQ, ingen lastgräns och ingen leveranstidsmening, vilket stämmer eftersom produkten saknar På beställning. Standardblocket är exakt. Meta är 145 tecken och har verb. Den gamla live-texten med "Vanliga frågor" ersätts helt (R15). Syskonen med 31 mm håldiameter och syskonet med lösa vikter är andra artiklar.

## Avvisade som granskades särskilt

- **36003 Rove AL/DL, Gloss Aragorn:** samma modell och färg, men SKU och streckkod är **...SHIN52**, medan det skrivna syskonet har **...SHIN54** (M/L). Det är alltså inte exakt samma artikel, och skälet "dubblett" är fel. Suffixet motsvarar sannolikt ramstorlek M (52 cm), men egen källa säger inte vilken storlek annonsen gäller, och webbkollen hittade inte exakt SKU. Utan storleken blir titel, SEO och meta lika syskonets.
- **36004 och 36005 Kona Dew, Peridot och Fancy Karman:** samma färg som de skrivna syskonen, men **inte samma storlek**. Syskonen har S/M/L (SKU 01/03/05), och deras text säger S, M och L. 36004 och 36005 har SKU ...06, rimligen XL (57 cm). Det stöds av mönstret hos hibike.com, där Dew XL 2022 har MPN B22DWGR06, men det är inte verifierat för exakt SKU. Skälet "dubblett" är alltså fel.
- **36006 Tunturi 37,5 kg:** samma SKU (25TUPLA033) och samma EAN som den skrivna produkten 10656688275722 och som 10656688308490. Det är en exakt dubblett, och avvisningen står.
- **36007 och 36008:** samma SKU och EAN som den skrivna 10665225912586. Avvisningen står.
- **36001** (reflex, varianterna oförklarade och frågan stängd av David), **36009** (elektronik) och **36101** (fem vikter som är olika artiklar) står.

## Beslut som behövs (David)

1. **36003, 36004 och 36005:** ska slutsiffrorna i artikelnumret få räknas som ramstorlek? I så fall blir 36003 52 cm och 36004/36005 XL (57 cm). Vid ja kan de tre skrivas med storleken i titeln, på samma sätt som Sutra LTD 56 cm. Vid nej lämnas de utan text. Rekommendation: ja. Mönstret stämmer med varje syskon i butiken (48–58 för Libre och Rove, 01/03/05 för S/M/L hos Dew). Risken är att en storlek blir fel om Velomarket har en annan kodning.

Webbkällor: [velomarket.ee Rove AL/DL Gloss Aragorn](https://velomarket.ee/en/products/gravel-bike-kona-rove-aldl-2026-gloss-aragorn/), [Kona Rove AL/DL](https://en-eu.konaworld.com/products/rove-al-dl-37), [hibike Dew XL 2022](https://hibike.com/bicycles/city-trekkingbikes/kona-dew-27-5-bike-xl-mint-green-2022-p38faa0d37b1da2dd6f7a02ae1d76275e).
