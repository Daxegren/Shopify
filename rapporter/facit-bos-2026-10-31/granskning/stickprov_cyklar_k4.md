# Stickprov cyklar k_skriv_4 (växelgrupp utan mekanisk/elektronisk)

Datum 2026-11-03. Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info. Endast läsning, inget skrivet i Shopify.

Stickprov: 10 av 12 (7022, 7027, 7028, 7048, 7056, 7058, 7066, 7067, 7068, 7087). Ej granskade: 7121 (Kona LBF) och 7150 (Liv Avail Advanced 2, Cosmic Dust).

## Metod
Live-läsning via graphql_query (title, handle, status, tags, seo, descriptionHtml) jämförd tecken för tecken i python mot k_skriv_4.json (titel, seo_title, meta, html). Källa: vag2k_4_fore.json (före-läge).

## Resultat
| Kontroll | Utfall |
|---|---|
| Titel, SEO-titel, metabeskrivning, html identiska med skrivfilen | 10 av 10 identiska, inga teckenavvikelser |
| Status ACTIVE | 10 av 10 |
| Tagg texter-klara | 10 av 10 (övriga taggar oförändrade mot före) |
| Mekanisk/elektronisk/trådlös/batteri/Di2/eTap/AXS i text | Förekommer inte i någon av de 10 |
| Längder | Titel 43-63 (max 70), SEO-titel 31-42 (max 43), meta 137-150 (130-155) |
| Tal mot före-filen | Alla tal finns i källan, utom "2025" i 7048 (se nedan) |
| 7022 Kona Process 153 | Växelgrupp och antal växlar utelämnade, som avsett. Källan anger "Microshift Advent X eller Shimano Deore 11spd" (osäker), och texten nämner den inte |
| Påhittade uppgifter | Inga funna. Ord som inte står ordagrant i källan är språkliga omskrivningar (komposit för composite, vikbar/fällbar, 4 kolvar för 4-kolvsbromsar, flaskhållare/pakethållare från källans fästpunkter) |
| Stavning, kolon och versaler | Inga fel funna. Stor bokstav efter kolon och beskrivande ord i titel följer formatreglerna |

## Anmärkningar (ingen kräver rättning, David kan välja)
1. 7048 Giant TCR Advanced 2 PC, 2025, Carbon: "2025" (titel, SEO, meta, Modellår) finns inte i före-titeln eller före-texten, bara i produktens handle (road-bike-giant-tcr-advanced-2-pc-2025-carbon-...). Handle är produktdata i butiken, så det räknas som källa, men det är den svagaste förankringen i stickprovet. 7066 (samma modell, handle innehåller också 2025) har inget årtal i texten, så de två är inte samstämmiga.
2. 7027 Giant FastRoad: titeltypen är "Cykel" medan källan säger fitnesscykel (texten skriver "enligt tillverkaren ... fitnesscykel"). Godtagbart.
3. 7056 SEO-titel "Mountainbike Kona Process 134 DL 27.5" skiljer sig från titeln (saknar färgen), alltså lagras den som skriven. Samma i live.
4. 7066 saknar meningen "Beställningsvaror kan ta upp till en vecka längre" i standardblocket. Före-källan saknar också beställningsvaru-raden, så det är konsekvent.

## Slutsats
Inga avvikelser mellan live och skrivfilen. Inga påhittade uppgifter och inga antydningar om mekanisk/elektronisk växling. Stickprovet godkänt.
