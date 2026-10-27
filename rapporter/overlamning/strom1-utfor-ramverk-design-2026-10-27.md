# Utför-ramverk (T39): designskiss

Datum: 2026-10-27. Ström 1 (Drift och mätning). Status: **bara design, ingenting är byggt**. Skriven av en hjälpagent; samordnaren och David beslutar. Inga nätverksanrop mot Shopify eller Google gjordes; allt nedan om Shopifys API är skrivet från kunskap och kodens egna frågor, inte verifierat mot Shopifys dokumentation i det här passet (markerat **Obekräftat**).

## 1. Mönstret som redan finns i `scripts/redirects_gorilla_apply.py`

| Delmoment | Vad skriptet gör | Fil:rad |
|---|---|---|
| Torrkörning som standard | `--apply` är en `store_true`-flagga; utan den skrivs bara rapport och "Torrkörning: inget ändrat" | `redirects_gorilla_apply.py:144`, `:200-202` |
| Planen byggs av läsning | Befintliga omdirigeringar hämtas (`fetch_redirects`) och jämförs mot den granskade filen; varje rad blir SKAPA, ÄNDRA eller OFÖRÄNDRAD (idempotent: redan rätt rör inte butiken) | `:78-89`, `:130-137`, `:153-155` |
| Kontrollera mål före skrivning | Målet måste finnas (produkt ACTIVE, kollektion, artikel); annars "STOPPAD" och hoppas över. Källa som är en levande sida stoppas | `:103-127`, `:166-178` |
| Rapport-CSV | En rad per åtgärd med nuvarande mål, nytt mål och målkontroll; skrivs både vid torrkörning och körning | `:182-190` |
| Återställningsfil före skrivning | JSON med id, sökväg och `target_innan` för varje rad som ändras, skriven **före** första mutationen | `:204-207` |
| Skriv rad för rad | En mutation per rad, `userErrors` räknas, 0,3 s paus, felkod 1 om något misslyckades | `:208-221` |
| Token | Läses ur miljön (`ShopifyConfig.from_env`), aldrig som argument | `:6-8`, `:148-151` |

Det som **saknas** i skriptet och som T39 kräver enligt rutinen i `standardtester.md` ("Rutin för ändringar i Shopify", steg 1–7):
1. **Ingen läsning tillbaka efter skrivning och ingen jämförelse.** Skriptet litar på att mutationen svarade utan `userErrors` (`:216`).
2. **Ingen testpost** i testloggen (T8).
3. **Återställningsfilen har ingen återställare.** SKAPA-rader har `id: None` i filen (`:84`, `:205`), så de kan inte återställas utan att leta upp dem via sökvägen.
4. **Ingen loggfil** (`shopify-andringar-<datum>.md`, rad till `ANDRINGSLOGG.md`).
5. **Bara omdirigeringar.** Inga textfält.
6. **Ingen batch-hantering och ingen kohort** (behandlings-/kontrollgrupp, krav för BOS-labbet enligt `arbetsstrommar.md`, tillägget 2026-10-27).
7. Klienten `ShopifyClient.graphql` kastar fel för hela svaret om `errors` finns på toppnivå (`shopify_client.py:73-88`); ett delvis svar med både `data` och `errors` kastas alltså bort. Det spelar roll för aliasbatchar (avsnitt 2.4).

## 2. Förslag: `site-audit apply --plan <fil>`

Rekommendation: ett underkommando i `site-audit` (`src/site_audit/apply.py` plus ren logik i en testbar modul), inte ett fristående skript. Skäl: testloggen (`growth_tests.py`) finns där och måste anropas, och ren logik (planvalidering, batchning, jämförelse) blir enhetstestbar utan nätverk. `redirects_gorilla_apply.py` lämnas orörd tills det nya verktyget är bevisat; det kan sedan ersättas av en plan med typ `redirect`.

### 2.1 Planfilens format (JSON)
```json
{
  "format": 1,
  "plan_id": "bos-exp1-2026-11-02",
  "site": "bestofsports-se",
  "shop_domain": "6f2e53-67.myshopify.com",
  "skapad": "2026-11-02",
  "beslutad_av": "David, 2026-11-02 (ref: beslutsfil eller ANDRINGSLOGG)",
  "niva": "B",
  "test": { "kind": "seo_text", "metric": "gsc_clicks", "channel": "site", "market": null,
            "hypothesis": "...", "what": "...", "expect": 10, "start": "2026-11-03" },
  "objekt": [
    { "rad": 1, "typ": "product", "id": "gid://shopify/Product/123", "handle": "gravity-pro-2",
      "falt": "seo.title", "fore": "Gammal titel", "efter": "Ny titel", "kohort": "behandling" },
    { "rad": 2, "typ": "product", "id": "gid://shopify/Product/456", "handle": "annan-produkt",
      "falt": "seo.title", "fore": "Annan titel", "efter": null, "kohort": "kontroll" },
    { "rad": 3, "typ": "redirect", "id": null, "handle": "/gammal-sida",
      "falt": "redirect.target", "fore": null, "efter": "/collections/ny-sida", "kohort": "behandling" }
  ]
}
```
- `typ`: `product`, `collection`, `page`, `article`, `image` (alt-text), `redirect`.
- `falt` (stängd lista, allt annat avvisas vid validering): `seo.title`, `seo.description`, `descriptionHtml` (produkt, kategori, sida, artikel), `image.altText`, `redirect.target` (och `redirect.path` vid skapande).
- `fore` är värdet planen utgår från. Vid körning läses nuvärdet och **måste vara lika med `fore`**; annars är raden "föråldrad" och hoppas över (skyddar mot att någon ändrat fältet efter att planen skrevs). För nya omdirigeringar är `fore` `null` och källan får inte finnas.
- `kohort`: `behandling` eller `kontroll`. Kontrollrader har `efter: null` och skrivs aldrig; de finns i planen så att kohorterna är fastlåsta före körning och kan läsas av testutvärderingen. Verktyget ska vägra körning om antalet behandlings- och kontrollobjekt inte är lika (regeln i `arbetsstrommar.md`: lika stor, matchad kontrollgrupp, högst 300 objekt per omgång) eller om `objekt` överstiger 300 behandlingsrader.
- `efter` ska komma från ett skript som bygger texten ur originalfilen (rutinens steg 3), inte skrivas för hand.

### 2.2 Obligatoriska steg (ingen kan hoppas över; verktyget har ingen flagga för det)
0. **Validera planen** utan nätverk: format, stängd fältlista, kohortbalans, högst 300, inga dubbletter av (id, falt), `efter` inte tomt för behandling, titel- och metalängd (varning, inte stopp), inga förbjudna fält (avsnitt 3), inget `typ` som rör kosttillskott (se avsnitt 3 och 4), spärrlista för hälsopåståenden och omdömesord (hård lista, T31 när den finns).
1. **Läs nuvärden** från Shopify (bara läsning; här slutar en torrkörning) och jämför med `fore`. Skriv `plan-rapport-<plan_id>.csv` med status per rad: SKRIV, OFÖRÄNDRAD (nuvärde redan = `efter`), FÖRÅLDRAD (nuvärde skiljer från `fore`), STOPPAD (mål saknas osv.), KONTROLL (rörs inte).
2. **Spara original** för alla SKRIV-rader i `rapporter/shopify-original-<datum>/<typ>-<handle>-<falt>.txt` (exakt kopia, inklusive HTML) samt en samlad `aterstall-<plan_id>.json` med id, typ, fält och `fore`. Filerna skrivs och läses tillbaka (kontrollsumma) **före** första mutationen; kan de inte skrivas avbryts körningen.
3. **Skriv** i batchar (2.4), bara med `--apply` och bara om `plan_id` anges en gång till i `--bekrafta <plan_id>` (skydd mot att peka på fel fil).
4. **Läs tillbaka** varje skriven rad med en separat läsfråga (inte mutationens eget svar) och **jämför tecken för tecken** mot `efter`, med samma jämförelse som `scripts/diff_text.py` (`changes`). Rader som inte stämmer markeras AVVIKER; ingenting rättas automatiskt tyst.
5. **Logga**: en rad per rad i `rapporter/logg/strom1-<datum>.md` (datum, fil/objekt, vad, varför, beslutad av), `rapporter/shopify-andringar-<datum>.md` med före och efter, och utskrift av vad som ska föras till `ANDRINGSLOGG.md` (verktyget skriver inte i den; samordnaren för över, enligt `arbetsstrommar.md`).
6. **Skapa testpost** i `growth_tests` (via `add_test`, med `kind`, fönster från åtgärdstypen, `pages` = behandlingsobjektens adresser för `gsc_*`-mått). Kontrollgruppens adresser sparas i planen/rapporten; i dag finns ingen kolumn för dem i `growth_tests` (se öppna frågor).
7. **Slutrapport**: antal SKRIV/lyckades/AVVIKER/FÖRÅLDRAD/STOPPAD, sökväg till återställningsfil, exakt återställningskommando, och `site-audit test due`-datum.

Torrkörning (utan `--apply`) gör steg 0–1 och skriver rapporten; den skriver inga original, inga loggar och ingen testpost.

### 2.3 Gorilla kontra BOS
`arbetsstrommar.md` (tillägget 2026-10-27) tillåter BOS som labb men Gorilla bara vid 99,9 % säkra, exakt reversibla ändringar. Verktyget bör därför kräva `niva` och `site` i planen och vägra `site = gorillasports-*` för alla typer utom `redirect` med verifierat mål (200) och objektivt felaktiga tekniska värden, tills David säger annat. Claude når inte Gorillas butik; där körs verktyget av David (torrkörning som standard).

### 2.4 Batchning och fel
- **Aliasbatch:** flera mutationer i ett GraphQL-dokument via alias, t.ex. `m1: productUpdate(product: {...}) { product { id seo { title description } } userErrors { field message } } m2: ...`. **Obekräftat:** exakta mutationsnamn och indatatyper per typ (`productUpdate`, `collectionUpdate`, `pageUpdate`, `articleUpdate`, filuppdatering för alt-text) och att API-versionen `2026-07` (`config.py:48`) har dem som jag skriver; kontrollera med schemaverktyget innan bygget. `urlRedirectCreate`/`Update`/`Delete` och deras `userErrors` är däremot använda i `redirects_gorilla_apply.py:51-62`.
- **Batchstorlek:** förslag **10 alias per dokument** för textfält (långa `descriptionHtml` gör dokumenten stora), upp till 25 för korta fält som SEO-titel och -beskrivning, justerbart med `--batch`. Skäl: Shopifys kostnadsbegränsning (hink med poäng som fylls på per sekund) och att ett fel i ett dokument drabbar hela dokumentet. **Obekräftat:** exakta kostnadspoäng per mutation och planens fyllnadstakt; verktyget ska läsa `extensions.cost` ur svaret och dra ned takten själv, inte förlita sig på mitt tal.
- **Fel i en rad:** `userErrors` är per alias. Raden markeras FEL med meddelandet, övriga rader i samma dokument påverkas inte, och körningen fortsätter. Kör man mot en felgräns (till exempel fler än 5 FEL eller 10 % av raderna) stoppas körningen och slutrapporten säger vad som redan skrivits, så att det kan återställas.
- **Fel på hela dokumentet:** i dag kastar `ShopifyClient.graphql` om `errors` finns på toppnivå (`shopify_client.py:84-86`) och kastar då bort eventuell `data`. Ramverket behöver en variant som returnerar både `data` och `errors` så att man kan se vilka alias som gick igenom. Efter ett sådant fel läser verktyget **alltid** tillbaka alla rader i dokumentet (steg 4) innan något körs om; omkörning är trygg eftersom raden jämförs mot `fore`/`efter` (idempotent).
- **Takt och återförsök:** `_request` har redan återförsök på RETRY_STATUS med väntan (`shopify_client.py:53-71`). Mellan dokument en paus och respekt för kostnadshinken.
- **Ordning:** behandlingsrader i fast ordning (rad-nummer), så att en avbruten körning kan återupptas med `--fortsatt` (hoppar över rader vars nuvärde redan är `efter`).

### 2.5 Återställning
- `site-audit apply --aterstall aterstall-<plan_id>.json [--apply]`: läser nuvärde, jämför mot det som planen skrev (`efter`); rader där någon annan ändrat fältet sedan dess markeras KONFLIKT och rörs inte utan `--tvinga-rad N`. Skriver tillbaka `fore`, läser tillbaka, jämför, loggar (egen rad i loggen: "återställd") och sätter testet till avbrutet (kräver ett nytt fält/status i testloggen, öppen fråga).
- Torrkörning är standard även här.
- **Omdirigeringar:** återställning av SKAPA = radering av den skapade omdirigeringen. Därför sparas det nya id:t som mutationen returnerar i återställningsfilen efter skrivningen (i dag sparas inget id för SKAPA, `redirects_gorilla_apply.py:205`). Radering är annars utanför ramverket (avsnitt 3), men *återställning av egen skapad omdirigering* är ett undantag som ska vara uttryckligt och loggas.
- Originalfilerna i `rapporter/shopify-original-<datum>/` är den andra, oberoende återställningsvägen (manuell, via admin).
- **Gräns:** Shopify har ingen ångra-funktion för texter (`standardtester.md`, rutinens steg 1). Återställning bygger helt på våra sparade original; därför är steg 2 ett hårt krav.

## 3. Vad som INTE ska ingå
- **Tema** (Liquid, mallar, sektioner, tema-inställningar): Claude kan inte skriva det publicerade temat och ändrar det inte; David gör det (`LARDOMAR.md`, sista raden i "Fakta om uppsättningen").
- **Pris, jämförpris, lager, kostnad**: nivå C, kräver Davids ja per ändring. Inget `falt` för dem i den stängda listan.
- **Publicering, avpublicering, status, radering** av produkter, kategorier, sidor, artiklar (undantag: återställning av en omdirigering ramverket själv skapat, se 2.5).
- **Översättningar** (finska, danska): rörs inte. Verktyget skriver bara grundspråket (svenska).
- **Kosttillskott, hälsopåståenden, omdömen, betyg, citat, "verifierad"-märken**: nivå C och aldrig genererade av agent. Verktyget ska stoppa objekt vars produkttyp/kollektion är kosttillskott om inte planen har `niva: "C"` med Davids uttryckliga ja per rad. Hur kosttillskott identifieras (taggar, produkttyp, kollektion) är **inte undersökt**.
- **Rabattkoder, appar, annonser, kunddata, e-post.**
- **Befintliga omdirigeringar som ändras eller tas bort** i Gorillas butik utom enligt 99,9 %-villkoret.
- Metafält, schema/strukturerad data i temat, canonical (ligger i temat).

## 4. Risker och öppna frågor

Risker:
1. **Skrivning av fel text i stor skala.** Motmedel: `fore`-kontroll, torrkörning, max 300, avbryt vid felgräns, läs tillbaka. Lärdomar 2026-10-26 gäller: texten byggs ur originalfilen, inte för hand; mät inte "tyder på" utan kontrollgrupp.
2. **Kohortfel.** En dåligt matchad kontrollgrupp (annan säsong, annan trafiknivå) ger falska slutsatser. Matchningen är inte lösbar i skrivverktyget; den måste designas av ström 2 och granskas. Verktyget kan bara kontrollera storlek, överlapp (inget objekt i båda grupperna) och att kontrollobjekten inte ändras.
3. **Sidor i kontrollgruppen ändras av annat** under testet (andra åtgärder, temaändringar). Verktyget kan varna om samma `handle` finns i en annan aktiv testpost.
4. **Utvärderingsmåttet kan inte misslyckas som det är byggt.** `evaluate_pages` använder "övriga sidor med samma första led" som kontroll (`growth_tests.py`, funktionen `evaluate_pages`), inte en fastlåst kontrollkohort. Ett riktigt kohortdesign kräver en ny utvärderingsväg som läser kontrollsidorna ur planen. Det är ett eget arbetspaket.
5. **API-versionen** (`2026-07`) och mutationernas form är inte verifierade här; fel mutationsnamn upptäcks först vid första riktiga körning. Motmedel: bygg mot en fake-klient, och kör första riktiga torrkörningen (läsning) på BOS, sedan ett batchat skrivtest på en (1) behandlingsrad.
6. **Token och scopes.** Skrivning kräver skrivrätter (`write_products`, `write_content`, `write_online_store_navigation` för omdirigeringar enligt `redirects_gorilla_apply.py:11-12`; övriga scopes obekräftade). BOS-token är `BESTOFSPORTS_SHOPIFY_TOKEN` (`sites.toml:100`); om den har skrivrätt är **inte undersökt**. Skrivrättigheter i Shopify-kopplingen bör stå på "fråga" (`standardtester.md`, rutinen).
7. **Ändringar som Shopify själv gör** (till exempel att `seo.title` tomt faller tillbaka på produkttiteln) kan göra "läs tillbaka och jämför" tvetydigt: ett tomt `efter` läses tillbaka som null. Planen bör förbjuda tomma `efter`-värden för SEO-fält.
8. **Teckenkodning och HTML-normalisering.** Shopify kan normalisera HTML i `descriptionHtml` vid sparande. Då avviker tillbakaläsningen från `efter` fast inget är fel. Mät i ett litet test (en rad) innan bulk och bestäm om jämförelsen ska ske mot normaliserad text.

Öppna frågor till David/samordnaren:
- Ska ramverket vara ett underkommando (`site-audit apply`) eller ett skript i `scripts/` som `redirects_gorilla_apply.py`? Mitt förslag: underkommando.
- Behövs nya kolumner i `growth_tests`: `plan_id`, `control_pages` (kontrollkohortens adresser), och en statusväg "avbruten/återställd"? Det är en ändring i `growth_tests.py` (ström 1:s fil) men påverkar tolkningen av testerna.
- Ska en plan kunna blanda typer, eller en plan per åtgärdstyp (enklare att utvärdera, ett fönster per plan)? Förslag: en åtgärdstyp per plan eftersom fönstret (`kind`) är per test.
- Hur identifieras kosttillskott maskinellt?
- Vilken nivå (B) gäller för titlar på BOS inom labbet: räcker planens ja från David utan ett ja per rad (så står det i `arbetsstrommar.md`), och i så fall hur dokumenteras det (fältet `beslutad_av`)?

## 5. Testplan (utan nätverk, med fake-klient)
Alla tester i `shopify-sync/tests/`, mönstret från `test_site_audit.py` (fakes för BigQuery och HTTP).
1. **Plan-validering:** godkänd plan; okänt fält; saknad kohort; obalans behandling/kontroll; >300; dubblett (id, fält); tomt `efter` på SEO-fält; förbjuden typ (pris, tema); Gorilla-sajt med textfält avvisas.
2. **Torrkörning skriver inget:** fake-klienten registrerar anrop; inga mutationer, inga originalfiler, ingen testpost.
3. **`fore`-kontroll:** nuvärde skiljer från `fore` ger FÖRÅLDRAD och ingen mutation för raden.
4. **Original före skrivning:** om originalkatalogen inte går att skriva (skrivskyddad temp-katalog) görs ingen mutation. Ordning verifieras genom anropslistan: original-fil skriven < första mutation.
5. **Batchning:** 23 rader med `--batch 10` ger tre dokument (10, 10, 3), alias unika, rätt ordning.
6. **Fel i en rad:** fake-klienten returnerar `userErrors` på alias 4 av 10; övriga 9 skrivs, rad 4 loggas FEL, körningen fortsätter; felgräns stoppar efter N fel.
7. **Fel på hela dokumentet** (`errors` utan `data`, och `errors` med partiell `data`): ingen krasch, tillbakaläsning av alla rader, ingen dubbelskrivning vid omkörning.
8. **Tillbakaläsning och jämförelse:** fake-butik som lagrar `efter` korrekt ger OK; fake som ändrar ett tecken ger AVVIKER och ett icke-nollskilt returvärde; test som kan misslyckas: en fake som tyst ignorerar skrivningen (läser tillbaka `fore`) **måste** ge AVVIKER (regel 6 i `arbetsstrommar.md`).
9. **Idempotens:** kör samma plan två gånger mot fake-butiken; andra gången OFÖRÄNDRAD för alla rader, inga mutationer.
10. **Återställning:** kör plan, kör `--aterstall`; fake-butiken är tillbaka till originalet tecken för tecken; en rad som ändrats av annan efter planen ger KONFLIKT och rörs inte; SKAPA-omdirigering raderas via sparat id.
11. **Testpost:** efter lyckad körning har `add_test` anropats med rätt `kind`, fönster (56 för `seo_text`), `pages`; inte vid torrkörning eller återställning.
12. **Loggfiler:** rad per ändring i `rapporter/logg/…`, före/efter i `shopify-andringar-…`; inga hemligheter i någon utfil (sök efter tokenmönster i alla utfiler).
13. **Skyddsflaggor:** `--apply` utan `--bekrafta <plan_id>` eller med fel id gör ingenting.
14. **Förstakörning mot riktig butik (manuellt, David):** torrkörning mot BOS (läsning), därefter en rad med `--apply`, kontrollera i admin, därefter hela omgången.

## Täckning

Läst i sin helhet: `/home/user/Shopify/CLAUDE.md`, `shopify-sync/docs/LARDOMAR.md`, `shopify-sync/docs/arbetsstrommar.md`, `shopify-sync/docs/tillvaxtarbete.md`, `scripts/redirects_gorilla_apply.py` (alla 225 rader), `src/site_audit/growth_tests.py`, `scripts/diff_text.py` (de första 30 raderna).
Läst delvis: `shopify-sync/docs/standardtester.md` (rutinen rad 27–37, tillägget rad 145–213 och T8-raden; resten av filen inte), `src/site_audit/main.py` (kommandot `test` och hjälpfunktioner, inte hela filen), `src/shopify_sync/shopify_client.py` (rad 50–90).
**Inte läst:** `src/site_audit/shopify_admin.py` (läsning via Admin API finns där och kan återanvändas, inte undersökt), `src/site_audit/actions.py` (förslagsformat, `actions.csv`), `scripts/audit_*`, temat, Shopifys dokumentation och schema (ingen åtkomst), BOS-tokenens scopes, tidigare `rapporter/shopify-andringar-*.md` (hur loggformatet faktiskt ser ut), hur ström 2:s plan för experiment 1 ser ut. Inget har körts mot Shopify.
