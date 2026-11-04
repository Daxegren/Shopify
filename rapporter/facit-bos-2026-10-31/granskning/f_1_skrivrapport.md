# Skrivrapport f_1 (BH Fitness löpband, Velomarket), 2026-11-04

Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info.
Skrivfil: vag2_skriv/f_skriv_1.json (24 produkter). Före-läge: rapporter/shopify-original-2026-11-04/f_1_fore.json (sparat före skrivning).

## Före / efter
- Före: alla 24 ACTIVE, ingen med taggen texter-klara, SEO-titel och meta null, titlar på formen "Löpband/Treadmill BH FITNESS ...", flera beskrivningar på engelska eller med trasig specifikation (t.ex. 16", x10 på RS1200).
- Efter: titel, seo.title, seo.description och descriptionHtml identiska med skrivfilen på 24 av 24. handle, status (ACTIVE) och pris orörda.
- Hoppade över: 0 (alla ACTIVE, ingen redan skriven).

## Kontrollskript (på kopia, html mappad till beskrivning, standardblock markerat, fakta = före-text)
24 produkter, 6 FEL, 0 övriga än kända. De 6 felen är falska: "tal_utan_kalla" 0,5 / 0,8 (10001, 10002, 10008) eftersom källan har "0<strong>,5" som splittras av taggen i skriptets textrensning. Varningen "passar dig som" känd och godtagen. Inga riktiga fel.

## Skrivning
Kanarie 3 (0-3), därefter 5+5+5+5+1. Varje mutation skrevs ut av python-skript (json.dumps ensure_ascii=True) och klistrades in. Alla userErrors tomma. Seo skickades alltid med title och description.

## Återläsning
Alla 24 återlästa (högst 4 åt gången) och jämförda i python (titel, seo.title, seo.description, descriptionHtml, status) mot skrivfilen, plus kontroll av osynliga tecken (Cf/Zs utom vanligt mellanslag): 24 av 24 identiska, 0 osynliga tecken. Obs: återläsningen klistrades in i skriptet för hand, då MCP-svar inte kan nås från bash; felkopiering skulle ge falsk avvikelse, inte falsk överensstämmelse. Ingen avvikelse uppstod, ingen omskrivning behövdes. Handtaggar/statusfält jämfördes inte mot före-filen maskinellt.

## Taggar
texter-klara lades till på alla 24 med tagsAdd; svaret visar att övriga taggar (BH Fitness, Löpband, Velomarket m.fl.) finns kvar.
"På beställning": 18 produkter har taggen och 18 har meningen "Beställningsvaror kan ta upp till en vecka längre" i html; de 6 utan taggen (10005, 10013, 10014, 10018, 10019, 10020) saknar meningen. Matchar exakt (kontrollerat i python mot skrivfilen och i tagsAdd-svaret).

## Avvikelser
Inga. Notering: scratchpad delas med annan agent (kopia.json skrevs över); jag bytte till egen mapp scratchpad/f1.
