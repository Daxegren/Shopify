# Granskningsutlåtande k_15

Datum: 2026-11-05. Granskare: Opus, endast läsning mot Shopify. Butiken bekräftades som BEST OF SPORTS (6f2e53-67.myshopify.com). Källan, varianterna och syskonprodukterna hämtades live via `shopify_api`.
Utkastfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_15_utkast.json`. Maskinläsbart utlåtande: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_15.json`.
Förutsättning: Davids beslut 2026-11-05. Varianten Default Title har samma SKU (28200712-B) som L / valge, räknas som överbliven och ignoreras (R3). Produkten skrivs utan färg i titeln.

## Resultat

| nr | id | Produkt | Dom |
|---|---|---|---|
| 10113 | 10471064273162 | Romet Vintage Eco D | GODKÄND |

`skrivfil_kontroll.py` på en kopia av utkastet gav 0 fel och 0 varningar.

## Faktakontroll mot live-källan (R1, R2)

| Påstående i utkastet | Live-källa |
|---|---|
| Stålram | "Ram: stål" |
| Shimano Tourney, 6 växlar | "Shimano Tourney växel", "Antal växlar: 6" |
| Stänkskärmar, pakethållare, kedjeskydd, stödben samt fram- och bakljus ingår | Står ordagrant i den fetstilta raden under listan |

- **Hjulvikt 15,3 kg** är rätt utelämnad. Etiketten säger hjul, men värdet passar en hel cykel, så uppgiften är inte entydig (R2).
- **"Shimano Touring - Shimano Touring"** är rätt utelämnad. Raden är trasig och det framgår inte vilken del den gäller (R2).
- **Marknadsföringen** ("kvalitet", "pålitligt", "säkerhet och komfort", "designad för kvinnor") är utelämnad. Det följer R5.
- Syskonen Eco D Grafit och Turkos anger V-bromsar i sina egna källor. Det står inte i den här källan och har med rätta inte tagits med (R1).

## Fokuspunkter

- **Ingenting bygger på den ignorerade varianten.** Texten nämner varken pris (6 749 kr för Default Title, 5 869 kr för L / valge), färg eller storlek. Titel, SEO-titel och meta saknar färg, som David beslutat. Handtaget (handle) innehåller fortfarande "vit". Det får inte ändras (R12a) och motsäger inget, eftersom valge betyder vit.
- **Motiveringen i `att_bekrafta` punkt 2 är fel, men texten påverkas inte.** Utkastaren skriver att ramstorlek L bara säljs som den ignorerade varianten. Det är tvärtom: Default Title ignoreras och L / valge är den variant som finns kvar. Ramstorlek L (20 tum, 165–185 cm) står entydigt i källan och hade fått nämnas enligt R3 v1.5. Att utelämna den är ändå inget faktafel, så någon rättning krävs inte. Punkt 1 är också otydligt formulerad och kan läsas som att båda varianterna ignoreras.
- **Typord och titel (R7, R12).** Typordet "Cykel" kommer från live-titeln. Syskonen heter Damcykel och Stadscykel, men varje produkt behåller sitt eget ord. Den färglösa titeln "Cykel Romet Vintage Eco D" är unik i butiken. De andra Eco D-produkterna (Grafit, Röd, Turkos) har färg i titeln. Meta och SEO-titel krockar inte med dem. Ingen annan produkt har artikelkoden 28200712, så det finns ingen dubblett (R12a).
- **R11 och R15.** Första meningen har verb och är inte cirkulär. Live-SEO saknas och den gamla beskrivningen ersätts helt.
- **Standardblocket** är identiskt med `b_skriv_24.json`. Leveranstidsmeningen saknas, vilket är rätt eftersom produkten inte har taggen "På beställning".

## Iakttagelse för David (inte ett textfel)

Lagersaldot 1 ligger på den ignorerade varianten Default Title. L / valge har saldo 0. Tas Default Title bort senare kan produkten visas som slutsåld. Den varianten kostar dessutom 880 kr mer. Textutrullningen ändrar varken pris, varianter eller lager.

## Rättningar

Inga.
