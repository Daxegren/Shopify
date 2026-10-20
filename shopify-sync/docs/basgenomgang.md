# Basgenomgång för varje sajt

Tillägg 2026-10-20. Det här är den standardgenomgång som görs när en sajt läggs till och sedan en gång i kvartalet. Den bygger på en extern tillväxtgenomlysning (Etals-rapporten för gorillasports.se, 2026-10-18) och på det vi redan har. Syftet är att få samma bild för alla butiker utan att köpa en rapport per sajt.

Inget i genomgången ändrar något i Shopify. Alla fynd är förslag som granskas av en människa.

## Steg
1. **Teknisk genomlysning och innehåll:** `site-audit run --site <sajt> --bigquery --search-data` (se `docs/site-audit.md`). Ger fynd, `actions.csv` och `redirects_import.csv`.
2. **Datakvalitet:** `sql/growth/datakvalitet.sql` och `site-audit check-access --site <sajt>` (efter driftsättning), så att siffrorna kan lita på.
3. **Döda sidor med trafik:** `sql/analys/doda_sidor_med_trafik.sql`. Inaktiva eller raderade produktsidor som fortfarande får besök, i prioritetsordning inför omdirigering.
4. **Sökfrågor med lucka:** `sql/analys/sokfragor_luckor.sql`. Frågor och köpguide-sökningar där en sida redan rankar på plats 4–20 men tar få klick.
5. **Sökordsluckor och konkurrenter (manuellt):** sökord som sajten inte rankar på, synlighet mot konkurrenter och länkprofil kräver en extern källa (Ahrefs eller liknande) och automatiseras inte. Sökvolymer är uppskattningar; kontrollera mot Search Console.
6. **Logga åtgärderna** med `site-audit test add` (förväntat utfall och utvärdering efter 28 dagar), så att vi lär oss vad som gav effekt.

## Vad rapporten tog upp och var det täcks
| Fynd i extern rapport | Täckning i basgenomgången |
|---|---|
| Döda URL:er (4xx/5xx), tillgänglighet | `traffic_page_broken`, `redirect_*`, `redirects_import.csv`, `doda_sidor_med_trafik.sql` |
| Saknade H1, för långa eller dubbla titlar och beskrivningar | `missing_h1`, `multiple_h1`, `title_too_long`, `duplicate_title`, `duplicate_seo_title` |
| Tunna sidor och produktbeskrivningar | `thin_page`, `thin_content`, `product_no_description` |
| Kod- eller AI-rester i produkttext (rå HTML, kodstaket, AI-fraser) | **Ny:** `product_text_residue` (heuristik, granskas manuellt) |
| Interna länkar med `?_pos=…&_psq=…` | **Ny:** `internal_links_tracking_params` |
| Product-schema utan omdömen | **Ny:** `product_schema_no_rating` (info) |
| Product- och breadcrumb-schema | `product_schema_*`, `breadcrumb_schema_missing` |
| Orphan-sidor, kanonisering, hreflang | `orphan_page`, `canonical_*`, `hreflang_*` |
| Mobil prestanda (LCP, INP, CLS) | `cwv_*`, `lighthouse_performance` (kräver `--psi N`) |
| Sökordsluckor och sökfrågor | `sokfragor_luckor.sql` (egen data); sökvolymer manuellt |
| Synlighet mot konkurrenter, backlinks | Inte automatiserat |

## Så läser vi en extern rapport
- Uppsidor i procent ("+17–26 %") är verktygets uppskattning, inte en prognos.
- Samma siffra på flera orelaterade poster (till exempel 1 191) tyder på en artefakt i genomsökningen.
- Rekommendationer om FAQ-schema för rich results har liten effekt för de flesta sajter eftersom Google begränsat de utdragen; fyll FAQ för användarnas skull.
- Förändringar i synlighet som sammanfaller med Googles uppdateringar är korrelation, inte bevisad orsak.

## Tillägg 2026-10-20: översatta adresser
`doda_sidor_med_trafik.sql` jämför mot handles i Shopify och fungerar därför bara för domäner där adresserna inte är översatta (gorillasports.se). På marknader med översatta adresser (till exempel gorillasports.dk) ger den falska träffar; där används genomsökningen (`traffic_page_broken` i `site-audit`) i stället. Det första försöket på .dk gav 100 falska träffar innan vi kontrollerade sidorna för hand.

## Tillägg 2026-10-20: sidhastighet och kategorisökord
- `scripts/psi_snapshot.py` mäter fem representativa sidor (startsida, kategori, produkt, blogg) med Googles PageSpeed Insights och listar verkliga besökares LCP/INP/CLS, största element, tyngsta tredjepartsskript och möjliga vinster i millisekunder. Kräver en API-nyckel i miljövariabeln `PSI_API_KEY`; nyckeln läggs aldrig i chatten eller i filer.
- `sql/analys/kategori_sokord.sql` visar för valda sökord vilka sidor som rankar och vilka närliggande frågor besökarna skriver. Underlag för att förbättra en kategorisida.
