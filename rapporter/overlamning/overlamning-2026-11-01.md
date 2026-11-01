# Överlämning 2026-11-01 (produkttexter i Best of Sports)

Läs först: `shopify-sync/docs/produkttexter-standard.md` (avsnitt 10), `rapporter/facit-bos-2026-10-31/process-vagor.md`, `shopify-sync/docs/LARDOMAR.md` (senaste två posterna), `CLAUDE.md`. Läs inte hela `ANDRINGSLOGG.md` (94 kB): sök på datum.

## Läge
- **Skrivet i BEST OF SPORTS (bestofsports.se):** pilotens 20 produkter (2026-10-25, titlar och sorterade specifikationer rättade 2026-10-30) och facit 30 (2026-10-31). Original: `rapporter/shopify-original-2026-10-25|30|31/`.
- **Våg 1 (fitness, Tunturi/Toorx/BH/Hammer):** 113 utkast skrevs av hjälpagenter, 4 oberoende granskare dömde (59 OK, 29 RÄTTA, 15 AVVISA), 3 rättare rättade. **86 utkast klara, 0 FEL**, ingenting skrivet. Lista: `rapporter/facit-bos-2026-10-31/vag1_klara_ids.json`. Skrivdata byggs med `python3 bygg_skriv.py vag1_01 ... vag1_09 fix_1 fix_2 fix_3`.
- **Stickprov:** 20 produkter (`stickprov1_ids.json`) ligger i artefakten https://claude.ai/artifact/JJZR5YVvGvAmfcaqyyAC3f. Davids kommentarer sparas bara i hans webbläsare. Han ska klicka "Kopiera sammanställning" och klistra in tabellen.
- **Handläggning (inte i vågen):** `handhavd_ids.txt` (massage/vibration/akupressur kvar, batteri/motor, avvisade, hållna).

## Nästa steg
1. Få Davids stickprovstabell. Rätta utkast efter kommentarerna (ny modul `fix_4.py`, senaste vinner). Kör `python3 bygg_utkast.py <alla moduler>` (0 FEL).
2. Kanarie 3 produkter, återläs, skriv i batchar om högst 25 (mutation per produkt: titel, seo, descriptionHtml). Spara original först (`rapporter/shopify-original-<datum>/`). Logga i `ANDRINGSLOGG.md`, beslutsfil `rapporter/beslut-<datum>.md`.
3. Dagen efter: kör kontrollfrågan (13_kontroll_skrivna_titlar.sql) och återläs titlar.
4. Våg 2: resterande fitness (cirka 79 kandidater kvar av 199), därefter övriga Velomarket, Gymstick (369), Gorilla Norden (cirka 285, ta bort showroomadress Vanadisvägen 2).
5. Pilotens effekt mäts tidigast 2026-11-22 (ingen kontrollgrupp; Black Month stör).

## Öppet för David
Pullbuoy (svenskt ord?), bärförmåga 220 kg på gymbollar, Platinum Hex/SmartLock-varianter (olika priser), AL 1 arkiverad, SEO-suffix i temat (sidkälla på en pilotprodukt), ska experiment 1 vara kvar utanför (ja, beslutat), annonsbeslut i `rapporter/beslut-2026-10-30.md` (Rude).

## Tekniska anteckningar
- Shopify-kopplingen måste visa BEST OF SPORTS (`get-shop-info`); den hamnade en gång på Gorilla. Byte: `switch-shop` och Davids ny inloggning.
- Hjälpagenter: utkast och rättning går med sonnet, oberoende granskning med opus (stoppades en gång av 5-timmarsgräns, kom tillbaka). Agenterna får aldrig skriva till butiken.
- Webbåtkomst från sessionen till tunturi.com/velomarket.ee är blockerad.
