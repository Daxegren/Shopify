# Åtgärdsförslag för beslut 1 och 2 (godkända av David 2026-11-12)

Inget av detta är utfört. Ingen skrivning till Shopify har gjorts (se "Hinder" längst ned).

## Beslut 1: döda länken `/collections/kona`
- **Var:** kollektionssidan `/collections/varumarke`, textblocket (sektionen `rich_text_k7w9xd`, hopfällbar text) med meningen "Vi samarbetar med välkända och pålitliga tillverkare som Tunturi - Christopeit Sport Germany - ... - Liv - Kona".
- **Före:** `<a href="/collections/kona" title="Kona">Kona</a>`
- **Efter:** `<a href="/collections/kona-1" title="Kona">Kona</a>`
- **Konsekvens:** länken slutar ge 404; kona-1 (2 887 visningar, position 17) får sin första innehållslänk. Inget annat ändras. Efter ändringen: hämta `/collections/varumarke` och kontrollera att länken svarar 200.

## Beslut 2: länkar till de nio svagast länkade synliga kollektionerna
Förslag på var en länk (ankartext = kollektionens namn) bör läggas. Källorna är valda på handle-namn och är förslag att bedöma, inte mätt relevans. Länkarna läggs i kategoritexterna via kategorisessionen (texter är ett eget beslut per källa).

| Mål (innehållskällor idag) | Föreslagna källkollektioner |
|---|---|
| kona-1 (0) | varumarke (se beslut 1), mountainbike, gravelcykel, cyklar |
| cykelsolglasogon (0) | cykeltillbehor, cykelhjalmar |
| traningsutrustning-for-hemmagym (0, inte i meny) | hemmagym, gymutrustning, multigymspaket, skivstangspaket |
| skivstangsset (0) | skivstang, skivstangspaket, olympisk-skivstang-50mm |
| pre-workout-pwo (1, inte i meny) | kosttillskott, kreatin, bcaa |
| tranings-t-shirt-dam (1) | tranings-t-shirt-herr |
| romet (1) | herrcyklar, damcyklar |
| benmaskiner (1, inte i meny) | benpress, traningsmaskin, gymutrustning |
| skyddsutrustning-cykel (1) | cykeltillbehor, cykelhjalmar |

Mätning före: `gsc-svagast-lankade.csv`. Mät om med samma skript efter ändring.

## Hinder
Ändringen i beslut 1 är en innehållsändring i Shopify (sidsektion i temat/sidan). Den här sessionen har ingen godkänd skrivväg: ingen API-token finns i miljön, och Shopify-verktyget används inte (uppdragets begränsning, och lärdomen 2026-11-04 om delad koppling). David kan göra ändringen i temaredigeraren på någon minut, eller ge en skrivväg via Admin API-appen.
