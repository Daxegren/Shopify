# Flerbutik: vad som var hårdkodat för BEST OF SPORTS

Skapad 2026-11-06 av Claude på Davids uppdrag (butiksoberoende textutrullning inför Alpha Zoo och BYOU Underwear). Filen fylls bara på.

## 1. Kartläggning (läget före ändringen)

### Skripten som omfattades av uppdraget

| Skript | Hårdkodat för BOS | Nu |
|---|---|---|
| `shopify_api.py` | Butiksadress `6f2e53-67.myshopify.com` (konstanten `BUTIK`); miljövariabelnamn `SHOPIFY_CLIENT_ID_BOS` / `SHOPIFY_CLIENT_SECRET_BOS` som standardargument; `verifiera_butik` jämförde med `BUTIK`; maskningen av hemligheter täckte bara variabler som börjar på `SHOPIFY_CLIENT_` | `klient_fran_profil(profil)`; `verifiera_butik` jämför med klientens egen adress; variabelnamn från profilen maskas också. `BUTIK` och standardargumenten finns kvar (oförändrat beteende utan profil) |
| `shopify_meta_rensning.py` | `ShopifyKlient()` utan argument (BOS); spärrlistans sökväg | `--profil`; klient och spärrlista från profilen |
| `status_uppdatera.py` | Arbetskatalog `rapporter/facit-bos-2026-10-31/vag2_skriv`; granskningskatalog `.../granskning`; statusfilens namn `bestofsports-textutrullning.md`; filprefix `f`, `g`, `h` (regex `[fgh]`, sorteringsordning, särbehandling av skrivfilernas namn); ersatta batcher f_16–f_25; delade skrivfiler f_14/f_15 (ok + rest); rubriken "BEST OF SPORTS"; ordet "Fitnessgruppen"; sökvägarna till profil, regelbok och beslutslogg i sidhuvudet; öppna frågor i `oppna_fragor.json` | `--profil`; allt ovan från profilen |
| `mutation_fran_skrivfil.py` | Taggen `texter-klara` | Taggen `klartagg` ur profilen (`--profil`) |
| `mat_utbyte.py` | Standardkatalog `rapporter/facit-bos-2026-10-31/vag2_skriv` (relativ till arbetskatalogen) | Profilens arbetskatalog (`--profil`); uttryckligt katalogargument går före |
| `jamfor_live.py` | Inget butikspecifikt (jämför mot skrivfil). Meddelandet om taggen `texter-klara` är enda BOS-kopplingen | Ingen ändring |
| `mutation_meta.py` | Inget butikspecifikt | Ingen ändring |
| `test_shopify_api.py` | Testerna använder BOS-variablernas namn som testdata | Oförändrad (28 tester) |

### Hårdkodat i skript utanför uppdraget (ändrades inte)

| Skript | Vad | Behov inför nästa butik |
|---|---|---|
| `skrivfil_kontroll.py` | Profilsökvägen `butiksprofil-bestofsports.json` (rad 118), standardblockets krav, märkeslistor, utfyllnadstexten "Finns hos BEST OF SPORTS." (rad 92–93), SEO-suffix | **Rörs inte nu** (annan session arbetar i filen). Önskad ändring beskrivs i beslutsfilen |
| `shopify_skriv_texter.py` | `ShopifyKlient()` (BOS), `KLARTAGG = 'texter-klara'` | Behöver `--profil` innan Alpha Zoo skrivs. Tills dess skriver den alltid mot BOS (och `verifiera_butik` stoppar inte, eftersom både klient och förväntad butik är BOS) |
| `arkivera_dubbletter.py` | `ShopifyKlient()`, pilotlistans sökväg, `texter-klara` | Som ovan |
| `nattkontroll.py`, `verifiera_skrivna.py` | `ShopifyKlient()`, `vag2_skriv`-katalogen, `texter-klara` | Som ovan |
| Övriga (audit, rendera, samtycke m.fl.) | Exempel-URL:er i hjälptexten | Ingen åtgärd |

### Filprefix och namnmönster

`f_`, `g_` och `h_` är BOS batchprefix (fitness, sedan nya batcher efter spärrhanteringen 2026-11-04). Filerna heter `<prefix>_<nr>_in.json`, `<prefix>_<nr>_utkast.json`, `<prefix>_<nr>_avvisade.json`, `<prefix>_utlatande_<nr>.json`, `<prefix>_skriv_<nr>.json` och `<granskningskatalog>/<prefix>_<nr>_*skrivrapport.md`. Mönstret är oförändrat; prefixen och katalogerna väljs nu i profilen. Batcherna `k_*` (cykel och övrigt) räknas inte av `status_uppdatera.py` (gäller före som efter ändringen).

## 2. Hur en butik väljs

Alla skripten i tabellen ovan tar `--profil <sökväg>`. Utan argument används `shopify-sync/config/butiksprofil-bestofsports.json`. Mallen för en ny butik är `shopify-sync/config/butiksprofil-mall.json`; modulen `shopify-sync/scripts/butiksprofil.py` läser och kontrollerar profilen.

| Profilfält | Betydelse | BOS-värde om fältet saknas |
|---|---|---|
| `myshopify` | butikens `*.myshopify.com` | `6f2e53-67.myshopify.com` |
| `butiksnamn` | rubriker | BEST OF SPORTS |
| `api.klient_id_var`, `api.klient_hemlighet_var` | NAMNEN på miljövariablerna | `SHOPIFY_CLIENT_ID_BOS`, `SHOPIFY_CLIENT_SECRET_BOS` |
| `gransvarden.seo_suffix` | SEO-suffix | ` – BEST OF SPORTS` |
| `klartagg` | tagg när texten är verifierad | `texter-klara` |
| `sparrlista`, `regelbok`, `beslutslogg` | sökvägar | oförändrade BOS-sökvägar |
| `arbetskatalog`, `granskningskatalog` | batchfiler och skrivrapporter | `rapporter/facit-bos-2026-10-31/{vag2_skriv,granskning}` |
| `filprefix` | batchprefix i ordning | `["f","g","h"]` |
| `ersatta_batcher`, `delade_skrivfiler` | batcher som utgår / delas i ok+rest | f_16–f_25 / f_14, f_15 |
| `statusfil`, `oppna_fragor`, `statusgrupp` | statusfilens sökväg, öppna frågor, ordet i sammanfattningen | BOS-filerna / "Fitnessgruppen" |

**Säkerhetsregel:** fallbacken gäller bara BOS-profilen. En annan butiks profil får inte ärva något från BOS: saknas ett obligatoriskt fält, står `<...>` kvar från mallen, eller pekar profilen på BOS miljövariabler eller BOS adress med annan butik, stoppar skriptet med ett fel innan något anrop görs. Skälet är att ett ofullständigt Alpha Zoo-underlag annars tyst kunde läsa eller skriva i BOS.

## 3. Så startar nästa butik (Alpha Zoo)

1. Kopiera `butiksprofil-mall.json` till `butiksprofil-alphazoo.json` och fyll i alla fält (adress, namn, variabelnamn, suffix, kataloger, prefix, statusfil). Skapa spärrlistan.
2. David: tillåt butikens `*.myshopify.com` i molnmiljön, skapa appen, lägg klient-id och hemlighet som miljövariabler med de namn som står i profilen (aldrig i chatten).
3. Kör `python3 -I shopify-sync/scripts/status_uppdatera.py --profil shopify-sync/config/butiksprofil-alphazoo.json` och `shopify_meta_rensning.py ... --profil ...` (dry-run först; skriptet verifierar att API-svaret kommer från profilens butik).
4. Före skrivning med `shopify_skriv_texter.py`: `--profil` måste först läggas till där (se tabellen ovan).
