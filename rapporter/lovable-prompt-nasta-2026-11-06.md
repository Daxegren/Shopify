# Lovable-prompt: nästa steg efter statusskyddet (2026-11-06)

```
Tack för statusskyddet. Nästa steg, i den här ordningen. Följ CLAUDE.md, uppdatera docs/PRODUKT.md och lämna jobb 13 i dry_run = true. Ändra inga priser, texter eller lager i Shopify.

1. RÄTTA ORSAKERNA till felaktiga "borttagna hos Velomarket"-markeringar:
   a) velo_status = not_found får bara sättas efter två negativa kontroller, på både SKU och Velomarkets produkt-id, på olika dagar.
   b) velo_status_checked_at får inte skrivas över vid tillfälliga fel (timeout, 5xx, nätverksfel).
   c) Lägg till en kolumn för när not_found först sågs och använd den för "dagar som saknas" i stale-cleanup.
   d) shopify-price-retry och shopify-price-recalc ska slå upp på SKU som reserv, inte bara på produkt-id.
   e) Tester för a till d.

2. WEBBLÄSARTEST: öppna sidan Statusskydd i en riktig webbläsare (inloggad) och verifiera flikarna Förslag, Statusändringar, Textändringar, Arkiverade och Varningar, knapparna Godkänn, Ångra, CSV-export och kill switchen. Rätta det som inte fungerar och visa en skärmbild per flik.

3. IMPORT AV OMKONTROLL: lägg till en flik "Omkontroll" där man kan ladda upp en CSV (kolumner: sku, velo_product_id, namn, klass, lager_velomarket med klasserna FINNS_MED_LAGER, FINNS_UTAN_LAGER, BORTTAGEN, OSAKER). Visa raderna tillsammans med nuvarande Shopify-status, Shopify-lager, taggen "texter-klara" och "sync-skydd", med CSV-export. Lägg till åtgärden "Återaktivera" för rader i klassen FINNS_MED_LAGER (valda rader, max 25 åt gången): kräver inloggad användare, sätter status ACTIVE, loggar i status_change_log med ångra, återställer velo_status till aktiv med nytt kontrolldatum. Gör ingen automatisk återaktivering och inga anrop mot Velomarket i den här fliken.

4. DEPLOYA de ändrade edge functions, kör ett testanrop per funktion med dry_run = true och visa svaren. Rapportera kort vad som ändrats och vad som deployats, och vänta på vår bekräftelse innan något annat ändras.
```

Bakgrund: steg 3 flyttar omkontrollen (som görs i Cloud Shell, utan krediter) in i appen så att återaktiveringen loggas och kan ångras. Prompten ersätter `lovable-prompt-steg4-2026-11-06.md`.
