# Kravspecifikation (utkast): synk av Gorilla Sports produkter till BEST OF SPORTS

Skriven 2026-11-23 efter Davids önskan: "bygga en funktion som synkar Gorilla Sports produkter med Best of Sports, och då lager, pris, titel, beskrivning, bilder, allt". Projektet byggs av David och Claude med **GitHub** (kod, granskning, PR) och **Lovable** (hosting, databas, edge functions), med Cloud Shell för engångsskript. Detta är ett utkast att besluta om; inget är byggt.

## 1. Syfte och avgränsning

Hålla BEST OF SPORTS (bestofsports.se) uppdaterat med Gorilla Sports sortiment från källan, så att produkter, lager, pris, titlar, beskrivningar och bilder följer källan utan manuellt arbete. Gorilla Sports är ett **märke i BOS** (kategorierna ska kunna fyllas med deras produkter), och synken ska inte påverka produkter från Velomarket (`velo-market-api`) eller Gymstick (`ftp-product-sync`).

## 2. Nuläge (läst 2026-11-23)

- BOS har **681 produkter** med märket Gorilla Sports Norden (654) eller Gorilla Sports (27): 290 aktiva (232 med lager), **355 utkast**, 36 arkiverade. 279 har prisjobbstaggen.
- Det finns **ingen dokumenterad synk** för dem. Båda befintliga synkrepona frågar i sin PRODUKT.md (F20/F10) vilken källa de cirka 305 produkterna utan Velomarket- eller Gymstick-tagg har. Gorilla-produkterna kommer alltså från ett okänt flöde (manuell import eller ett äldre verktyg).
- Befintligt mönster att återanvända: ett Lovable-projekt per leverantör (React/Vite, Supabase, edge functions, pg_cron, Vault), `product_syncs` som kärntabell, `PRODUKT.md` som grundlag, `requireCaller`, kill switch, statusskydd, prisspärr.
- Gorillas egen butik (`gs-nordic-production.myshopify.com`) ägs av huvudkontoret. Tillgång har tidigare lösts med en tillfällig token (BigQuery Sync-appen); det får inte bli permanent.
- Möjligt relevanta repon att läsa först: `GorillaSports/shopify-mono`, `GorillaSports/shopify-order-orchestrator`, `GorillaSports/best-of-sports` (tema). Innehållet är inte läst.

## 3. Krav

### 3.1 Källa och åtkomst
- K1. Källan fastställs (Gorillas Shopify-butik via egen app eller HQ:s produktregister/flöde). Skrivåtkomst till Gorillas butik behövs inte; **läsning räcker**.
- K2. Åtkomst via en egen app/token som HQ godkänt och som ligger som secret i Lovable, aldrig i kod eller chatt.

### 3.2 Nyckel och urval
- K3. **SKU är nyckel** mellan butikerna. En tabell `gorilla_syncs` (som `product_syncs`) håller SKU, BOS-produkt-id, Gorilla-produkt-id, status, senaste synk, hash av synkade fält.
- K4. Urvalet styrs av en uttrycklig lista eller regel (alla med lager > 0 eller valda kollektioner), inte "allt". Produkter som redan ligger i BOS och tillhör Velomarket/Gymstick rörs aldrig.

### 3.3 Vad som synkas
| Fält | Regel |
|---|---|
| Lager | Källans lager gäller; lager 0 → utkast, utom beställningsvaror; återpublicering först efter kontroll mot källan (publiceringsvakt som i Velomarket-synken) |
| Pris | Beslut krävs (se 5). Går genom prisspärr (marginal 30–50 %, ±25 % hålls för godkännande). **Inga prisskrivningar före 2026-12-01** |
| Titel och beskrivning | Skrivs bara vid skapande eller när en flagga är på; `texter-klara` och `sync-skydd` skyddas alltid (samma som regel 16 och 19 i Velomarket-synken) |
| Bilder | Laddas upp bara om produkten saknar bilder; produkt utan bild förblir utkast |
| Varianter | Variantnamn byggs av färg, storlek, vikt, längd eller modell (inte SKU), med färgord översatta till svenska; ny delad modul `variant-names` |
| Taggar | Slås bara ihop, tas aldrig bort; taggen `Gorilla Sports-sync` markerar produkter under synk |
| Kategori och attribut | Produktkategori (taxonomi) och kön/attribut som i `playbook` avsnitt 10; skilda lager för kollektion, kanal och filter |
| Metafält för Google Merchant Center | Som i Velomarket-synken, men bara efter beslut |

### 3.4 Säkerhet och skydd (obligatoriskt)
- K5. Dry run är standard; verklig skrivning kräver uttryckligt val.
- K6. Kill switch (som `SYNC_WRITES_ENABLED`) och statusskydd: max 10 automatiska statusändringar per dygn, arkiverade återaktiveras aldrig, status ändras bara efter godkännande där det är riskabelt.
- K7. Ingen radering. Produkter som försvinner i källan hamnar i en granskningslista, som i Velomarket-synken.
- K8. Varje ändring loggas (före/efter) i `gorilla_change_log` och kan ångras för status, pris och text.
- K9. RLS på alla tabeller med admin-roll; anon har inga rättigheter; edge functions kräver `requireCaller`.
- K10. Cron med `x-cron-secret` från Vault; deploy av edge functions via Lovable efter merge, verifierat med ett nekande anrop.

### 3.5 Arbetssätt och leverans
- K11. Egen GitHub-repo och eget Lovable-projekt ("BOS - Gorilla Sports"), `docs/PRODUKT.md` som grundlag, ändringar via PR som David godkänner, tester (vitest) för pris-, lager- och namnregler, `CLAUDE.md` med reglerna ovan.
- K12. Claude skriver koden i repot, kör tester och skript i Cloud Shell; Lovable används för databasmigreringar, deploy av edge functions och cron. Credits används bara för sådant som inte går via GitHub.
- K13. Faser med eget ja: **0** jämförelse per SKU mellan Gorillas butik och BOS (läsning, ingen kod); **1** tabell, dry run och rapport; **2** lager (endast befintliga produkter); **3** titlar, beskrivningar, bilder och varianter; **4** pris (efter 2026-12-01); **5** nya produkter; **6** cron.

## 4. Icke-mål
Orderhantering och leverans (ligger utanför; se fråga 5), Gorillas butiks innehåll, ändringar i Gorillas butik, betalningar, e-post.

## 5. Beslut som behövs innan bygge

1. **Källa:** Gorillas butik, HQ:s register eller ett leverantörsflöde? Vem hos HQ godkänner läsåtkomst och en egen app?
2. **Pris:** ska BOS använda Gorillas pris, en egen marginalregel (som Velomarket-synken) eller ett fast påslag? Har Gorilla ett inköpspris för BOS (internpris) eller bara butikspris?
3. **Texter:** har BOS egna texter på de Gorilla-produkter som redan finns (`texter-klara`)? Rekommendation: skydda dem och synka bara nya produkter.
4. **Utkasten:** varför är 355 av 681 utkast (slutsålt hos Gorilla, medvetet avpublicerade eller ett gammalt flöde)? Ska de aktiveras?
5. **Order och lager:** delar BOS och Gorillas butik lager? Vem skickar BOS-ordrar med Gorilla-produkter? Utan detta finns risk för överförsäljning.
6. **Dubbletter:** samma produkt kan finnas hos Velomarket eller Gymstick och Gorilla. Vilken källa vinner per SKU?
7. **Märkesnamn:** ska BOS visa "Gorilla Sports" som märke (och hur hanteras "Gorilla Sports Norden" som leverantörsnamn)?
8. **Prisjobbet:** vilket verktyg sätter `price-change-job-active` och kommer det i konflikt med en pris-synk?

## 6. Första steget (läsande, ingen kod)

Med en läsning av Gorillas butik (David eller Cloud Shell ger en exportfil): jämför per SKU med BOS, redovisa vilka som finns i båda, vilka som saknas i BOS och vilka av BOS-utkasten som har lager hos Gorilla. Resultatet avgör omfånget och om en egen sync är motiverad.
