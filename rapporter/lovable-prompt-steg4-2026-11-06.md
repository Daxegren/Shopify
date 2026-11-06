# Kort Lovable-prompt: rätta orsakerna till felaktiga arkiveringar (steg 4)

Skicka bara om du vill bygga bort orsaken. Omkontrollen av de 400 görs utanför Lovable (Cloud Shell-skriptet), och jobb 13 står kvar i `dry_run: true`.

```
Rätta orsakerna till att produkter felaktigt kan markeras som borttagna hos Velomarket. Följ CLAUDE.md och uppdatera docs/PRODUKT.md. Ändra inga priser, texter eller lager i Shopify, och lämna jobb 13 i dry_run = true.

a) velo_status = not_found får bara sättas efter två negativa kontroller, på både SKU och produkt-id, på olika dagar.
b) velo_status_checked_at får inte skrivas över vid tillfälliga fel (timeout, 5xx, nätverksfel).
c) Lägg till en kolumn för när not_found först sågs och använd den för "dagar som saknas" i stale-cleanup.
d) shopify-price-retry och shopify-price-recalc ska slå upp på SKU som reserv, inte bara på Velomarkets produkt-id.
e) Lägg till tester för a till d.
f) Deploya de ändrade edge functions och kör ett testanrop per funktion med dry_run = true. Visa svaren.

Rapportera kort vad som ändrats och vad som deployats.
```
