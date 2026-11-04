# Beslutslogg för produkttexter (BEST OF SPORTS)

Skapad 2026-11-04. Filen fylls bara på; nya beslut läggs överst i tabellen, gamla rader ändras aldrig (en hävd spärr ändras genom en ny rad). **Läs den här filen och `shopify-sync/config/sparrlista.json` före varje ny batch.** Spärrarna läses dessutom av `shopify-sync/scripts/skrivfil_kontroll.py`, som stoppar skrivfiler med spärrade produkter.

| Datum | Beslut | Gäller | Vem | Källa |
|---|---|---|---|---|
| 2026-11-04 | Onboarding av WORKOUT BRANDS startad (fas 1, bara läsning). Profil och spärrlista är utkast; inga beslut taget om kategorier. Fas 2 startar när David godkänt profil, spärrar och åtgärdsförslag | WORKOUT BRANDS | David (uppdrag), Claude | `rapporter/beslut-2026-11-04-7.md` |
| 2026-11-04 | Produktdata-AI med kvalitetsrapport är riktningen; det byggs så att kunden kör det själv (självbetjäning). Nästa sajter: Alpha Zoo (alphazoo.se/.dk/.fi) och B You Underwear (byouunderwear.se), med genomlysning av SEO, metadata, struktur och GEO utifrån Search Console, Google Ads och Google Analytics | Alla framtida butiker | David | Chatt 2026-11-04 |
| 2026-11-04 | Riktning: kunskapen och pipelinen från BEST OF SPORTS ska kunna bli ett PIM-/produktdatasystem som säljs till andra e-handlare. Allt som byggs ska därför vara butiksoberoende (profil, regelbok, kontroller, status, mätning). Inget säljbeslut taget än | Hela textutrullningen | David | Chatt 2026-11-04 |
| 2026-11-04 | Punkt 3–6 byggs: regelbok i stället för långa prompter, butiksprofil per sajt, statusfil per utrullning, mätning av granskningsutbytet. Få korta filer som läses vid start via CLAUDE.md, och tester som tvingar fram reglerna | Alla butiker | David | Chatt 2026-11-04 |
| 2026-11-04 | Experiment 1 (432 produkter, kohorter T/K) hålls inte längre utanför. Skäl: låg trafik på .se/.dk/.fi och Google Ads avstängt, så experimentet går inte att lita på. Nya tester schemaläggs när allt är genomgånget | Alla produkter i kohorter.csv | David | Chatt 2026-11-04; `sparrlista.json` (aktiv=false) |
| 2026-11-04 | Pilotens 20 produkter hålls kvar tills David säger annat (mäts runt 2026-11-22). Två skrevs av misstag (10103, 10110) | `rapporter/bestofsports-pilot-20-produkter-2026-10-25.csv` | Claude föreslog, David har inte hävt | `sparrlista.json` (aktiv=true) |
| 2026-11-04 | "Alt A": maxvikt, användarvikt och driftsvikt utelämnas när källan bara är engelsk eller maskinöversatt. Ordagrann svensk lastgräns med enhet i produktens egen källa får stå en gång som "enligt tillverkaren" | Fitnessgruppen och andra faktatextgrupper | David | Chatt 2026-11-04 ("Kör på A") |
| 2026-11-04 | Fitnessprodukterna (Tunturi, Toorx, BH Fitness, Hammer) skrivs i faktatextläge, batch för batch, med Opus-granskning och Sonnet-stickprov | Fitnessgruppen | David | Chatt 2026-11-04 ("Kör nästa grupp") |
| 2026-11-04 | API-vägen (skript mot Admin API) görs senare samma dag; token läggs som hemlig variabel i miljön, aldrig i chatten | Alla butiker | David | Chatt 2026-11-04 |
| 2026-11-03 | Faktatextläge (standard §16) för pakethållare, solglasögon, lås, hjälmar, elcyklar, sparkcyklar och belysning. Kids och kosttillskott hålls utanför | Dessa grupper | David | `produkttexter-standard.md` §16 |
| 2026-11-03 | Kort sann meta (≥70 tecken) i stället för null; ingen utfyllnadstext i beskrivningen | Alla produkter | David | `produkttexter-standard.md` §14, §17 |
| 2026-11-03 | Gymstick- och Velomarket-taggar får aldrig ändras; felaktiga cykeltaggar rörs inte utan beslut | Alla produkter | David | Chatt 2026-11-03 |
| 2026-11-03 | Vinterprodukter frisläppta (pulkor, kälkar, skridskor), isbroddar hålls utanför | Vintergruppen | David | `produkttexter-standard.md` §15 |
| 2026-10-30 | Experiment 1 och pilotens 20 ändras inte i vågorna | Se ovan | David | `produkttexter-standard.md` rad 73 (hävd för experiment 1 2026-11-04) |
