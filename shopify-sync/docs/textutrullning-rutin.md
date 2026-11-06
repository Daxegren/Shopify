# Rutin: produkttexter i stor skala (från BEST OF SPORTS, 2026-11)

Skapad 2026-11-04 av Claude på Davids uppdrag: BEST OF SPORTS är första butiken, inte den sista. Filen fylls bara på. Varje butik får lägga till egna rader under "Butiksnoteringar" i stället för att ändra regler som redan gäller.

## 1. Flöde per grupp av produkter

1. **Gruppera** efter produkttyp och risk (en grupp = en typ av fakta, t.ex. växelcyklar, lås, hjälmar).
2. **Spara före-läge** (`*_fore.json`) av titel, seo, beskrivning, tagg, status. Utan före-läge ingen skrivning.
3. **Skriv utkast** från produktens egen källa (aldrig från syskonprodukter). Utkast och avvisade i skilda filer.
4. **Granska** (Opus) mot standarden. Sonnet duger inte som enda granskare (fann bara 41 % av Opus fynd).
5. **Bygg skrivfil** med `bygg_m_skriv.py` (kontroll av dubbletter och längder).
6. **Kontrollera på kopia** med checkern (`--seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70`). 0 fel krävs.
7. **Skriv** i små batcher, **läs tillbaka** (högst 4 produkter per fråga) och jämför tecken för tecken.
8. **Tagga** `texter-klara` sist, först när texten är verifierad.
9. **Stickprov** av Sonnet: minst 10 produkter eller 20 %, endast läsning, rapport i `granskning/`.
10. **Logga** (ändringslogg), **lärdomar**, beslutsfil.

## 2. Den viktigaste lärdomen: skriv inte för hand

Nästan alla fel i BEST OF SPORTS kom från att långa mutationer kopierades som text (av Haiku och av oss): extra mellanslag, mjuka bindestreck, tappade ord. Reglerna som hjälpte: skriptet skriver ut mutationen med `ensure_ascii=True`, återläsning i små delar, jämförelse i python, obligatoriskt stickprov.

**Målläge: skript skriver direkt mot Admin API** så att ingen text kopieras av en modell. Då räcker: skrivfil → skript → återläsning → automatisk jämförelse. Modellen behövs bara för att skriva och granska texterna.

## 3. Krav för API-vägen (att göra en gång per butik)

| Steg | Vem |
|---|---|
| Lägg butikens `*.myshopify.com` under *Allowed domains* i molnmiljöns nätverksinställning | David |
| Skapa en egen app i Shopify (Inställningar → Appar → Utveckla appar) med `read_products` och `write_products` (minsta behörighet). Lägg inte till fler | David |
| Lägg Admin API-token som hemlig miljövariabel (t.ex. `SHOPIFY_ADMIN_TOKEN_<BUTIK>`) i molnmiljön. **Aldrig i chatten eller i repot** | David |
| Ny session; läs en produkt som test innan något skrivs | Claude |
| Skript: dry-run (visa vad som ändras), skriv, återläs, diff, skriv ut avvikelser. Stoppa vid första avvikelse | Claude |
| Dra tillbaka token när arbetet är klart eller vid misstanke | David |

Testat 2026-11-04: utan tillåten adress ger `curl` mot Shopify `CONNECT tunnel failed, response 403`.

## 4. Regler som gäller alla butiker

- Inga uppgifter som inte står entydigt i produktens egen källa. Brutna källtexter stryks.
- Faktatextläge (standard §16) för säkerhetskänsliga kategorier: inga skydds-, stöld-, synlighets-, räckvidds- eller laddningsuttalanden utan "enligt tillverkaren".
- SEO skickas alltid som både `title` och `description`, annars tappas metan.
- Kort sann meta hellre än null. Ingen utfyllnadstext.
- Butikens egna tagg-/leverantörsregler ändras inte (t.ex. Gymstick- och Velomarket-taggar).
- Ingenting dubbleras: parallella skribenter ger dubblerade formuleringar och olika växelregler. Ge en skribent en grupp.
- Tilltrasslade rate limits: återuppta agenter med SendMessage när gränsen återställts.

## 5. Mätetal att följa per butik

Produkter skrivna / totalt, andel med 0 avvikelser i stickprov, antal korrigeringar efter skrivning, tid per 100 produkter, avvisade per orsak. Fyll i vid varje beslutsfil.

## Butiksnoteringar

| Butik | Läge |
|---|---|
| BEST OF SPORTS | Skrivning pågår via MCP (3–5 produkter per mutation). API-väg föreslagen 2026-11-04, väntar på tillåten adress, app och token. |

## Tillägg 2026-11-04: kontroller i kod och beslutslogg

- **Spärrlista:** `shopify-sync/config/sparrlista.json` listar produkter som inte får skrivas (idfil + skäl + beslut). Aktiva spärrar stoppar skrivfiler i `shopify-sync/scripts/skrivfil_kontroll.py`. Bygg alltid inventeringen mot spärrlistan innan batcher delas upp.
- **Skrivfilskontroll:** `python3 shopify-sync/scripts/skrivfil_kontroll.py <skrivfil> [--tillat-kanda]` kontrollerar spärrade produkter, förbjudna uttryck (FAQ, "Om märket", "här kallad", engelska maxviktsrader), märke i versaler, liten bokstav efter kolon, standardblocket, längder, dubbletter, osynliga tecken. Körs automatiskt av `rapporter/facit-bos-2026-10-31/vag2_skriv/bygg_kontrollerad.py` och ska köras före varje skrivning.
- **Beslutslogg:** `shopify-sync/docs/BESLUTSLOGG.md` samlar Davids beslut som styr utrullningen. Läs den före varje ny batch. Nya beslut läggs till överst.
- **Regel:** när något går fel ska vi fråga om ett skript kan upptäcka det, och i så fall lägga in kontrollen i `skrivfil_kontroll.py`, inte bara skriva en lärdom.

## Tillägg 2026-11-04 (kväll): regelbok, profil, status och mätning

- **Regelbok:** `shopify-sync/regler/regler-v1.md` (R1–R19, en kod per regel: T=skript, G=granskare, M=mänskligt beslut). Korta agentprompter i `shopify-sync/regler/agentprompter.md` ersätter de långa promptarna. Nytt granskningsfynd blir en ny regel eller ett nytt test.
- **Butiksprofil:** `shopify-sync/config/butiksprofil-bestofsports.json` (märken, gränsvärden, standardblock, taggar, faktatextkategorier, spärrlista). Ny butik = kopiera profilen, byt värden, behåll pipeline och skript.
- **Status:** `shopify-sync/status/bestofsports-textutrullning.md` genereras av `status_uppdatera.py`; öppna frågor i `shopify-sync/status/oppna_fragor.json`.
- **Mätning:** `python3 shopify-sync/scripts/mat_utbyte.py --md`. Mätt 2026-11-04 över 1 656 utkast: 45 % godkända direkt, 44 % rättas, 11 % underkända. Av enskilda rättningar är bara 12 % format och 88 % innehåll (ordval, påståenden, grammatik). Slutsats: att automatisera format räcker inte för att spara granskning; vinsten ligger i bättre regler till utkastarna och i att automatisera de återkommande innehållsfynden (cirkulär inledning, "N tum skärm", engelska typord).
- **Paketering för fler butiker:** pipelinen (regelbok, profil, kontrollskript, status, mätning) är butiksoberoende. För en ny butik behövs: profil, spärrlista, standardblock, en inventering och en skrivväg (API-token). Det här är underlaget för en tjänst.

## Tillägg 2026-11-04 (API-skript, app "BOS Textutrullning")

- **Åtkomst:** appen använder client credentials. Miljövariablerna `SHOPIFY_CLIENT_ID_BOS` och `SHOPIFY_CLIENT_SECRET_BOS` läses bara ur miljön; åtkomstnyckeln (giltig ca 24 timmar) hålls i minnet och skrivs aldrig till disk, logg eller rapport. Allt som skrivs ut maskeras. Kontrollerat 2026-11-04: nyckel erhållen, butiken är BEST OF SPORTS (`6f2e53-67.myshopify.com`), läsning av produkt fungerar (API-version 2026-07).
- **Bibliotek:** `shopify-sync/scripts/shopify_api.py` (token, `graphql()` med återförsök vid rate limit och serverfel, `hamta_produkter` via `nodes(ids)`, `spara_fore`, `uppdatera_seo` som alltid skickar både title och description, `jamfor_efter`).
- **Rensning av metabeskrivningar:** `python3 -I shopify-sync/scripts/shopify_meta_rensning.py <indata.json> (--dry-run | --kanarie | --rest)`. Indata: lista med id, seo_title, meta_gammal, meta_ny. Före skrivning klassas varje produkt mot live (skriv / redan klar / avviker; spärrlistan respekteras). Ändrar bara `seo.description`. Före-fil och resultatfil sparas i `rapporter/shopify-original-<datum>/`. Stopp vid första avvikelse. Ordning: `--dry-run`, `--kanarie` (3 produkter), `--rest` (resten, i delar om 4, med återläsning efter varje del).
- **Tester utan nätverk:** `python3 -I shopify-sync/scripts/test_shopify_api.py` (23 tester: token i minnet, maskning, återförsök, seo med båda fälten, jämförelse tecken för tecken, klassning).
- **Efter arbetet:** David byter Klienthemligheten i Dev Dashboard och tar bort miljövariablerna.

## Tillägg 2026-11-06: nya regler och daglig kontroll

- **Regelboken** har tillägg v1.7–v1.10 (se `shopify-sync/regler/regler-v1.md`): v1.9 (varianter med olika pris, reflexprodukter) och v1.10 (lastgräns på bärande delar: sök på nätet, annars "Maximal lastgräns: Ej känd").
- **Dubbletter:** Bara exakt samma artikel (modell, färg, storlek, vikt) räknas som dubblett (Davids beslut 2026-11-05). Samma SKU eller streckkod räcker inte som test: i praktiken är många produkter samma artikel under en annan artikelkod.
- **Granskarens rättningar** ska anges som ett sammanhängande före/efter-par per fält. Läs byggskriptets utskrift efter rader med "fore träffar 0" före skrivning (LARDOMAR 2026-11-05).
- **Daglig kontroll:** Kör `shopify-sync/scripts/nattkontroll.py` varje morgon. Den är bara läsande, jämför butiken med senast avsedda text och rapporterar nya avvikelser mot baslinjen (`rapporter/nattkontroll/baslinje.json`). Efter en genomgång av läget skapas en ny baslinje med `--skapa-baslinje`.
- **Leverantörssynken (Velomarket3, jobb 13 kl. 03:22 UTC)** kan arkivera produkter och återställa text. Statusskyddet i Lovable-projektet är införskaffat 2026-11-06; se `rapporter/lovable-prompt-nattsynk-2026-11-06.md`.
