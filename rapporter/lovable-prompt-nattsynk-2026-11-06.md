# Prompt till Lovable: kontroll på nattsynken (velo-market-api)

Bygger på läsning av repot Daxegren/velo-market-api (commit 25a84d6, 2026-11-06) och Shopifys produkthistorik. Inget i repot har ändrats.

## Vad koden visar

- Jobb 13 `shopify-stale-cleanup-daily` kör `shopify-stale-cleanup` varje dag 03:22 UTC. Det är exakt tiden då Velomarket3 arkiverade ett femtiotal produkter i natt.
- Funktionen arkiverar (eller sätter utkast på) alla produkter där `velo_status = 'not_found'` i minst 7 dagar. `dry_run` är sant som standard, men cron-anropets body är okänd (öppen fråga F7 i `docs/PRODUKT.md`), och produkterna arkiverades faktiskt, så cron skickar uppenbarligen `dry_run: false`.
- Funktionen kontrollerar varken taggen `texter-klara`, lager i Shopify eller försäljning. (Taggen `texter-klara` skyddas bara i `shopify-orphan-cleanup` och i sammanslagningsplanen.)
- `shopify-inventory-sync` sätter produkter till utkast vid lager 0.
- Textskyddet är en global inställning (`sync_metadata.overwrite_texts_on_existing`, standard falsk) i `_shared/text-protection.ts`. Det skyddar inte per produkt, och det täcker inte taggar eller status.
- Edge functions deployas inte automatiskt från GitHub (se `CLAUDE.md`).

## Prompt att klistra in i Lovable

```
Vi har gått igenom koden och Shopifys historik. Natten mot 2026-11-06 kl. 03:22 arkiverade jobb 13 (shopify-stale-cleanup-daily) ett femtiotal produkter som vi hade lagt manuellt skrivna texter på, de flesta med lager kvar i Shopify. Vi vill ha full kontroll över vilka produkter synken får arkivera, avpublicera och skriva text på. Ändra bara det som anges här, och uppdatera docs/PRODUKT.md (funktionskarta, avsnitt 4 och öppna frågor) i samma ändring. Följ CLAUDE.md.

STEG 1: ÄNDRA INGET, SVARA FÖRST
a) Visa den exakta bodyn och schemat för cron-jobb 13 (och alla andra cron-jobb som anropar shopify-stale-cleanup, shopify-inventory-sync, shopify-orphan-cleanup och shopify-merge-cleanup). Är dry_run false?
b) Lista de produkter som shopify-stale-cleanup arkiverade eller satte till utkast under de senaste 14 dagarna: SKU, namn, Shopify-id, tidpunkt, velo_status och när velo_status sattes till not_found. Exportera som CSV i appen.
c) Visa vad sync_metadata.stale_cleanup_action och overwrite_texts_on_existing är satta till just nu.
d) Förklara hur velo_status = 'not_found' sätts (vilket svar från Velomarket-API:t, hur många kontroller i rad) och om ett tillfälligt fel kan ge not_found.

STEG 2: REGLER SOM SKA GÄLLA FRAMÅT (efter vår bekräftelse av steg 1)
A. Stoppa riktig arkivering i cron. Sätt jobb 13 till dry_run = true (eller pausa jobbet) tills vidare. Lägg i stället resultatet i en granskningslista i appen: "Förslag: arkivera/avpublicera" med SKU, namn, Shopify-id, lager i Shopify, senaste försäljning, dagar som not_found och skäl. Status i Shopify ändras bara när en inloggad person godkänner.
B. Skyddsregler som alltid gäller, även efter godkännande, i alla funktioner som ändrar status (stale-cleanup, inventory-sync, merge-cleanup, orphan-cleanup, unpublish-imageless):
   1. Produkter med taggen "texter-klara" ändras aldrig automatiskt (status, text, taggar). De hamnar på granskningslistan med markering "har text".
   2. Produkter med taggen "sync-skydd" ändras aldrig automatiskt.
   3. Max 10 statusändringar per körning och dygn utan manuell överstyrning. Överskrids gränsen: avbryt och skicka en varning.
   4. Produkter med lager i Shopify > 0 eller med försäljning de senaste 90 dagarna arkiveras inte automatiskt.
C. Textskydd per produkt. Utöver den globala inställningen: skriv aldrig title, body_html, seo_title eller seo_description på en produkt med taggen "texter-klara", oavsett overwrite_texts_on_existing, och ta aldrig bort den taggen. Taggar ska slås ihop (lägg till, ersätt inte hela listan).
D. Logga allt som ändras. product_text_change_log finns redan för texter; lägg till en motsvarande status_change_log (produkt-id, SKU, gammal/ny status, funktion som gjorde ändringen, körnings-id, tid) och visa båda i appen med CSV-export.
E. Ångra. Från loggen i appen ska en enskild statusändring kunna återställas med ett klick (sätter tillbaka föregående status och tar bort ev. sync-taggar vi inte vill ha).
F. Morgonrapport. Efter nattens sista jobb, skicka en rapport (mejl till david.axegren@gmail.com) med antal ändrade produkter per funktion och en lista på alla statusändringar och alla produkter på granskningslistan.
G. Kill switch. En knapp i appen och en secret (SYNC_WRITES_ENABLED) som stoppar alla skrivningar till Shopify från cron men låter läsning och rapporter fortsätta.

STEG 3: TESTER
1. En produkt med "texter-klara" och velo_status = not_found: status ändras inte, den hamnar på granskningslistan.
2. En produkt med lager > 0: arkiveras inte automatiskt.
3. En produkt med "sync-skydd": ingen funktion skriver något på den.
4. Mer än 10 kandidater i en körning: ingen ändras, en varning skickas.
5. Taggar slås ihop och texter-klara finns kvar efter en full synk.
6. Kill switch av: inga skrivanrop mot Shopify.

Börja med steg 1 och vänta på vår bekräftelse innan steg 2. Edge functions deployas inte automatiskt från GitHub: deploya och verifiera med ett riktigt anrop efteråt.
```

## Beslut åt David innan prompten skickas

1. Ska produkter utan lager som Velomarket inte längre listar fortsätta arkiveras automatiskt (B.4 gör att de då går igenom utan mänsklig granskning)? Rekommendation: ja, men med taket 10 per dygn.
2. Taggen "sync-skydd": på vilka produkter ska den sättas (pilotprodukterna, ca 20)? Rekommendation: pilotprodukterna.
3. Mejladressen i punkt F.
