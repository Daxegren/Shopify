# Prompt till Lovable: omkontroll och återaktivering av de 400 arkiverade produkterna

Bygger på Lovables rapport 2026-11-06 (800 arkiveringar på 400 artikelnummer under 14 dagar, alla markerade not_found 27/4–5/5 utan omkontroll). David har godkänt: (1) omkontroll mot Velomarket innan något återaktiveras, (2) jobb 13 till `dry_run: false` (skriver bara förslag, inga Shopify-ändringar), (3) Shopify-behörigheterna `read_orders` och `read_all_orders` läggs till av David.

## Prompt att klistra in i Lovable

```
Tack för arbetet med statusskyddet. Nästa uppdrag gäller de 400 artikelnummer som arkiverades de senaste 14 dagarna (listan "stale-cleanup-arkiverade-14d.csv"). Vi vill veta vilka som fortfarande finns hos Velomarket och sedan kunna återaktivera dem på ett kontrollerat sätt. Följ CLAUDE.md och uppdatera docs/PRODUKT.md. Ändra inga priser, texter eller lager i Shopify. Shopify-skrivningar får bara ske via den godkännande-åtgärd som beskrivs i steg 3.

STEG 1: Sätt jobb 13 till dry_run = false (vi har godkänt det). Med den nya koden skriver det bara förslag till granskningslistan och ändrar inget i Shopify. Bekräfta med ett testanrop att inget skrivanrop mot Shopify görs, och att kill switchen fortfarande stoppar allt.

STEG 2: Omkontroll av de 400. För varje artikelnummer i listan, kontrollera live mot Velomarket-API:t, utan att skriva till Shopify:
 a) slå upp på artikelnummer (SKU) och, separat, på Velomarkets produkt-id;
 b) gör två kontroller med minst 10 minuters mellanrum (eller på två olika körningar) och kräv att båda ger samma svar;
 c) kör i omgångar om 25, med paus mellan omgångarna, så att Velomarkets gränser respekteras, och att körningen kan återupptas efter ett avbrott.
Klassa varje produkt som:
 1. FINNS_MED_LAGER: finns i Velomarket med lager > 0.
 2. FINNS_UTAN_LAGER: finns men lager 0.
 3. BORTTAGEN: saknas på både SKU och id i båda kontrollerna.
 4. OSÄKER: kontrollerna ger olika svar eller fel.
Visa resultatet på sidan Statusskydd i en ny flik "Omkontroll" med kolumnerna: SKU, namn, Shopify-id, nuvarande Shopify-status, lager i Shopify, lager i Velomarket, har text (taggen "texter-klara"), har sync-skydd, klass, förslag. Lägg till CSV-export och en sammanfattning med antal per klass och antal med "texter-klara".

STEG 3: Kontrollerad återaktivering. Lägg till en åtgärd "Återaktivera" i fliken Omkontroll som bara finns för klass FINNS_MED_LAGER (för enskilda rader och för valda rader, max 25 åt gången). Den kräver en inloggad person, sätter status till ACTIVE (inte utkast), loggar i status_change_log (med ångra) och återställer velo_status till aktiv med nytt kontrolldatum så att rensningen inte föreslår dem igen. Inget återaktiveras automatiskt. Kontrollera att nattens övriga jobb inte sätter tillbaka dem direkt (särskilt lagersynken och utkastsättningen av produkter utan bild) och beskriv i så fall vad som krävs.

STEG 4: Rätta orsakerna så att det inte upprepas (implementera, testa och deploya efter att steg 2 är redovisat):
 a) velo_status = not_found får bara sättas efter två negativa kontroller på både SKU och produkt-id, på olika dagar;
 b) velo_status_checked_at får inte skrivas över vid tillfälliga fel (timeout, 5xx);
 c) lägg till en kolumn för när not_found först sågs och använd den för "dagar som saknas";
 d) shopify-price-retry och shopify-price-recalc ska slå upp på SKU som reserv, inte bara på produkt-id;
 e) lägg till tester för a–d.

STEG 5: Rapportera: antal per klass, hur många av klass FINNS_MED_LAGER som har "texter-klara", vad dry_run = false på jobb 13 har lagt på granskningslistan, och vad som återstår. Vänta på vår bekräftelse innan du återaktiverar något i steg 3 (bygg bara åtgärden) och innan du deployar steg 4.
```

## Efter Lovables svar

1. David granskar fliken Omkontroll och godkänner vilka rader som ska återaktiveras (jag föreslår att börja med de som har "texter-klara").
2. Jag kontrollerar efteråt i Shopify att texterna ligger kvar på de återaktiverade produkterna.
3. David lägger till Shopify-behörigheterna `read_orders` och `read_all_orders` i appen (görs i Shopify).
