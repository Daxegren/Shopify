# Skrivrapport våg 2b-4 (Velomarket, tillbehör), 2026-11-03

Skrivfil: rapporter/facit-bos-2026-10-31/vag2_skriv/b_skriv_4.json (34 produkter). Butik verifierad: BEST OF SPORTS (bestofsports.se).

## Före och efter
- Live-läge före skrivning: 34 produkter, alla ACTIVE, ingen med taggen texter-klara, ingen med titel lika med skrivfilen. Inga hoppade över.
- Före-läge sparat i rapporter/shopify-original-2026-11-03/vag2b_4_fore_skriv34.json (34 poster).
- Efter skrivning: 34 av 34 har titel, seo.title, seo.description (där skrivfilen har meta), descriptionHtml och taggen texter-klara. Handle och status oförändrade.

## Kontroll före skrivning
- kontrollera_produkttext.py på kopia (rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2b4/kopia.json), html som beskrivning, standardblocket markerat, --seo-title-max 43, --seo-suffix " – BEST OF SPORTS", källtext = före-läget: 0 FEL, 47 VARNINGAR (kända: "passar dig som" saknas i 34, korta beskrivningar från tunn källa i 12, engelskt ord "Black" i ett produktnamn).

## Skrivning och återläsning
- Kanarie 3 (8001, 8002, 8005), sedan batcher om 8, 8, 8, 8, 7. Ingen batch över 12 000 tecken.
- Mutationerna genererades av skript (bygg.py), inte för hand.
- Återläsning efter varje batch med separat läsning av alla fält. Jämförelse i python mot skrivfil och före-läge. Tecken-för-tecken-jämförelsen gjordes maskinellt på återläsningen; själva återläsningen överfördes till JSON för hand, så en transkriptionsfel är inte utesluten men skulle synas som avvikelse.
- Avvikelser: 2 st, båda rättade (se nedan).

## Avvikelse och rättelse
- 8042 Grepptejp och 8044 Golvpump: SEO-titeln var lika med produkttiteln och metabeskrivning fanns. Mitt skript utelämnade då hela seo-objektet, så metabeskrivningen skrevs inte. Återläsningen fångade det. Rättat: seo{title, description} skickas nu i sådana fall. Verifierat: description lika med skrivfilen, title lagrad som null.
- Inga andra produkter berördes av detta. Ingen annan produkt har både lika titel och metabeskrivning i skrivfilen.

## Taggen texter-klara
- Lagd per batch efter verifiering. Befintliga taggar kvar (kontrollerat i återläsningen).

## Ej gjort och avvikelser från prompten
- Prompten sa att före-läget skulle sparas till vag2b_4_fore.json. Den filen finns redan med tre andra produkter (Basil/Giant/LIV) som inte ingår i skrivfilen. Enligt CLAUDE.md ändras inte befintliga filer i rapporter/ utan David. Därför skrevs före-läget till en ny fil (se ovan).
- Vag2b_4_skrivrapport.md finns redan och skrevs inte över. Denna rapport är ny.
- Beslutsfil rapporter/beslut-2026-11-03.md enligt CLAUDE.md skrevs inte; den och commit/push väntar på besked, eftersom prompten sa "committa inte".
- Metabeskrivning "" (8033 Sadel Selle Monte Grappa 156): behandlades som saknad. Shopify har description null före och efter.

## Ändrat
- Shopify: 34 produkter, fälten title, seo, descriptionHtml och tagsAdd texter-klara. Handle, status och pris ändrades inte.
- Filer: fore-fil (ny), kopia för kontroll (ny), denna rapport (ny). Inga befintliga filer ändrades.

## Nästa steg
- Nattlig titelkontroll enligt standarden (avsnitt 13): stickprov 30 produkter per natt under en vecka.
- Beslut från David: vilken fil som ska gälla som före-läge, samt om beslutsfilen ska committas.
