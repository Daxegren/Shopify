# Skrivrapport våg 2a, titeländringar – BEST OF SPORTS (2026-11-02)

Butiken kontrollerad med get-shop-info: BEST OF SPORTS (bestofsports.se, SEK). Inget committat.

## Resultat
- 6 produkter skrivna (2301, 2302, 2304, 2308, 2409, 2412), 0 userErrors. Kanarie 2301, därefter de övriga fem i en batch.
- Alla var ACTIVE före och efter. Handles oförändrade (jämförda mot live före). Ingen produkt hoppades över. Ingen av de sex finns i `handhavd_ids.txt` och ingen underkändes av granskarna (`vag2_a_granskning_3_4.md`).
- Före-läge (id, title, handle, status, seo, descriptionHtml, läst live strax före skrivning): `rapporter/shopify-original-2026-11-02/vag2a_titlar_fore.json`. Alla hade seo.title och seo.description = null. Html i före-filen är överförd för hand från live-svaret.
- Skrivdata: `rapporter/facit-bos-2026-10-31/vag2_skriv/a_skriv_titlar.json` (id, nr, titel, seo_title, meta, html). JSON är sanningen.

## Före / efter (titel)
| Nr | Före | Efter | SEO-titel (lagrad) |
|---|---|---|---|
| 2301 | Boxningshandskar TOORX Panther Boxing Gloves 10oz | Boxningshandskar Toorx Panther, Polyuretan, 10 oz | Boxningshandskar Toorx Panther, 10 oz |
| 2302 | Boxningshandskar TOORX Leopard Boxing Gloves 10oz | Boxningshandskar Toorx Leopard, Polyuretan, 10 oz | Boxningshandskar Toorx Leopard, 10 oz |
| 2304 | Flaska TREC SHAKER 050 - 0.7 l BLACK - TREC TEAM | Flaska Trec Shaker 050, 700 ml, Svart | Flaska Trec Shaker 050, 700 ml |
| 2308 | TUNTURI Ankelrem Prof | Ankelrem Tunturi Pro, Läder, Svart | null (lika med titeln) |
| 2409 | Fotsskydd TOORX benskydd med fotsskydd | Benskydd Toorx med Fotskydd | null (lika med titeln) |
| 2412 | Handledd-/ankelvikter CHRISTOPEIT 2x0,50 kg | Handleds- och Ankelvikter Christopeit | null (lika med titeln) |

Metabeskrivning: 2308 (136 tecken) och 2412 (146) har meta, övriga null (tunn källa, tillåtet). Beskrivning ersatt helt enligt utkast med granskarnas rättningar.

## Rättningar som applicerades (ur granskningen)
- 2301 html: "Toorx Panther Boxing Gloves är boxningshandskar i polyuretan. Handskarna är 10 oz." -> "Toorx Panther är boxningshandskar i polyuretan. Handskarna har storleken 10 oz."
- 2302 html: "Toorx Leopard Boxing Gloves är boxningshandskar" -> "Toorx Leopard är boxningshandskar".
- 2308 meta och html: "Tunturi Ankelrem Pro är en svart ankelrem" -> "Tunturi Pro är en svart ankelrem".
- 2304, 2409, 2412: godkända utan rättning. Titlarna 2409 och 2412 är de granskaren pekade ut (2412 utan vikt).

## Kontroller
Maskinellt:
- `kontrollera_produkttext.py --seo-title-max 43 --seo-suffix " – BEST OF SPORTS"` på kopia (html mappad till beskrivning, standardblock inom [[STANDARDBLOCK]]): 6 produkter, 0 FEL, 11 varningar (saknat avsnitt "passar dig som"/"specifikationer" och korta texter på tunna källor, samma som i granskningen och godtagna).
- Längder: titlar 27–49 tecken, högst 2 kommatecken; SEO-titlar 27–37 (≤43); meta 136 och 146.
- Unikhet: titel, SEO-titel och meta jämförda mot de 32 redan skrivna i `a_skriv.json` och inbördes: inga dubbletter.
- Återläsning direkt i svaret från varje productUpdate (title, handle, status, seo.title, seo.description, descriptionHtml) jämförd mot det skickade.

För hand:
- Handle och status lika med före för alla sex.
- seo.title lagrades som null för 2308, 2409, 2412 (lika med titeln, avsett beteende); seo.description återlästes som skickat (null för fyra, text för 2308 och 2412).
- Html jämfört rad för rad mot skickad text; ingen avvikelse (även radbrytning mellan `<li>` bevarad). Stor bokstav på beskrivande ord, enheter med gemener ("oz", "ml", "cm"), inga arbetstermer i kundtext.

## Ej gjort
- Unikhet mot hela sortimentet i live-butiken kontrollerades inte (bara mot våg 2a-filerna).
- Återläsning efter nattens Velomarket-synk (se LARDOMAR 2026-10-30) är inte gjord; titlarna bör läsas om 2026-11-03.
