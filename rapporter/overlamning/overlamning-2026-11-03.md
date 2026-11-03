# Överlämning 2026-11-03 (nytt kontextfönster)

Läs först: `CLAUDE.md` (rot), `shopify-sync/docs/produkttexter-standard.md` (avsnitt 10–13), `shopify-sync/docs/LARDOMAR.md`, `rapporter/beslut-2026-11-03.md`. Butiken som ska skrivas i är **BEST OF SPORTS (bestofsports.se)**: verifiera alltid med `get-shop-info` (annars `switch-shop`). Skriv med `productUpdate(product: ProductUpdateInput)`; `seo` skickas alltid med både `title` och `description`. Black Month började 2026-11-01.

## Status (2026-11-03)
- **Skrivet och verifierat i Shopify** (alla med taggen `texter-klara`, före-lägen i `rapporter/shopify-original-2026-11-0*/`): pilot 20, facit 30, våg 1 (86) + rättningar 1b/1c, våg 2a (fitness Velomarket, 32 + sex titeländringar + rättningar), **Gymstick 173** (språkrättat), **Velomarket tillbehör 83** (`b_skriv.json` 30, `b_skriv_hold_frisläppta.json` 13, `b_skriv_2.json` 37, `b_skriv_3.json` 3).
- **Cyklar och cykeldelar (214 med lager, nio batcher `k_1`–`k_9`):** utkast klara (118 utkast). Granskning k_1–k_3 och k_4–k_5 klar (`k_utlatande_1_3.json`, `k_utlatande_4_5.json`). `k_skriv_1.json` (90 cyklar) SKRIVEN och stickprovad (0 avvikelser), tidigare skriven av en Haiku-agent (rapport `granskning/vag2k_1_skrivrapport.md`). Cyklar utan lager (k_10–k_17, 187 st): 55 skrivna (k_skriv_3a/3b), stickprovade utan avvikelser. Granskning k_6–k_9 klar (`k_utlatande_6_9.json`); `k_skriv_2.json` (34) SKRIVEN och stickprovad (0 avvikelser), skriven av en Haiku-agent (rapport `granskning/vag2k_2_skrivrapport.md`).
- **Nattkontroll:** titlar var intakta efter synken 3 nov (33 av 33). Läs tillbaka stickprov om 30 produkter varje natt i en vecka (och efter varje körning av sammanslagningen).

## Nästa steg i ordning
1. Vänta in Haiku-rapporten för `k_skriv_1` och kör stickprov 20 procent (18 produkter, Sonnet, read-only, samma upplägg som `granskning/stickprov_velomarket_*.md`).
2. `k_skriv_2.json` (34 st, byggd av `bygg_k_skriv.py` minus nr i `k_skriv_1.json`) skrivs med Haiku (kanarie 3, högst 6 per mutation); kör sedan stickprov 20 procent (minst 10) på den.
3. Resterande Velomarket: cyklar/delar utan lager (187), pakethållare, cykelkläder, solglasögon, vinterutrustning/skidor; samma process. Pakethållare med lastgräns är säkerhetsprodukter.
4. Steg 3 i Davids plan: kontrollera Gorilla Norden-texterna (vendor "Gorilla Norden", cirka 285–301 på BOS) och ta bort showroomadressen Vanadisvägen 2.
5. Uppdatera `ANDRINGSLOGG.md` (ny rad överst per skrivning), `LARDOMAR.md` och skriv `rapporter/beslut-2026-11-03-2.md` (fem rubriker enligt CLAUDE.md) efter cykelomgången; committa och pusha.

## Beslut redan tagna av David (gäller)
Säkerhetsprodukter skrivs inte (hjälmar, lås, barn, last/belastning, bänkar/ställningar, el/batteri/elektronik, kosttillskott, rullskridskor, reflexer, bromsar, hjul, gafflar, kedjor, pedaler/vevar/vevlager, belysning, väskor/korgar med lastgräns, nackskydd/stöd med skadelöften). Gymtalk översätts inte. Fitnessmat Pro. Handtagstejp (inte Styrlinda). Innerslang med ETRTO i titeln. Framkorgar/bakre korgar utan lastuppgift, stänkskärmar med kompatibilitet "enligt tillverkaren" är tillåtna. Fitnessboll i titeln med träningsboll i beskrivningen; Motståndsband med "korta gummiband" i beskrivningen; sammanfogbar. Stickprov efter skrivning: 20 procent. Opus granskar före skrivning; Haiku skriver; Sonnet gör utkast och stickprov.

## Öppet / väntar på David eller leverantör
- Lovable (Velomarket-projektet): behörigheterna `read_orders`, `read_online_store_navigation`, `write_online_store_navigation` ska läggas till och appen installeras om; godkänn nya produktdokumentet; sammanslagningen byggs om först efter Black Month (behåll en produkt, övriga som varianter, hoppa över `texter-klara`). Rensningen är skyddad. Gymstick-skyddet är byggt men otestat (FTP-servern svarade inte); frontend ej publicerad.
- Butiksdata att rätta hos Velomarket/Rude: dubbletter (5054/5070/5080, 6006/6007/6008, 6066/6067, 6082/6083, 6121/6122, 6133/6134, 6144/6145), handle≠SKU (5213, 5234, 5244), priser (5211 1 569 kr, 5273 1 589 kr, Attend RS 1 12 469 kr), varianter med samma SKU men olika pris (6026, 6035, 6051, 6054, 6068, 6079, 6089, 6105, 6113), prisfel 0 kr på Gymstick-varianter, Talon 3 titel 27,5″ mot text 29″, inklistrad chatt-HTML (6014), Fila Houdini Pro (2201), estniska/tjeckiska variantnamn.
- Hållna produkter: 5054 (möjlig dubblett); stegbrädor och balansbräda i trä (Gymstick 3191, 3192, 3257, 3240); 3087 (möjlig dubblett av 3001). Öppna säkerhetsfrågor: nackskydd, boxningshandskar, handlindor, balansbräda.
- BigQuery-inloggning saknas (ingen trafikprioritering).

## Filer och verktyg
- Data: `rapporter/facit-bos-2026-10-31/vag2_skriv/` (`*_in.json` indata, `*_utkast.json`, `*_avvisade.json`, `*_utlatande_*.json`, `*_skriv*.json` slutlig skrivdata; JSON är sanningen), `rapporter/facit-bos-2026-10-31/granskning/` (rapporter), `rapporter/shopify-original-2026-11-0*/` (före-lägen), `rapporter/facit-bos-2026-10-31/handhavd_ids.txt`.
- Indata skapades ur `vag2_plan/b_ovriga_velomarket.csv` (kolumner: id, nr, titel, status_live, vendor, typ, kategori, skal, lager_2026_10_25, beskr_ord). Filen är en ögonblicksbild från 25 oktober.
- Kontrollskript: `shopify-sync/scripts/kontrollera_produkttext.py` (se standarden avsnitt 13).
- Användargränsen (5 timmar) har slagit till flera gånger; avbrutna agenter återupptas med SendMessage. Containern har startats om; allt är committat och pushat på grenen `claude/zealous-johnson-0ywddr`.

## Beslut av David efter cykelomgången (2026-11-03)
1. **Växelgrupper som kan vara elektroniska (7085, 7088, 7091, 7126 m.fl.):** låt de skrivna texterna stå (alternativ a). Leverantören bekräftar mekanisk växling i efterhand.
2. **Dubbletter (samma modell och färg under flera id):** slå ihop nu. Plan tas fram i `rapporter/facit-bos-2026-10-31/granskning/sammanslagningsplan.md` (arkivera dubbletter med taggen "sammanslagen", behåll den med taggen texter-klara). Osäkra grupper slås inte ihop.
3. **Väntelista, underkända för växlingen:** de skrivs inte nu men ska kommas ihåg (`rapporter/facit-bos-2026-10-31/vag2_skriv/vantelista_underkanda.json`: 7022, 7027, 7028, 7048, 7056, 7058, 7066, 7067, 7068, 7080, 7087, 7121, 7124, 7150, 7163). Webbsökning på tillverkarens specifikationer pågår (`granskning/vaxelsystem_webbsok.md`); skrivs bara de där tillverkaren entydigt anger mekanisk växling.
4. **Gorilla Sports-texter:** först på GorillaSports.se, sedan över till Best of Sports.
