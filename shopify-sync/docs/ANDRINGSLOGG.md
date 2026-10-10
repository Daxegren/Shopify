# Ändringslogg

Den här filen fylls bara på, nya poster överst. Befintliga poster ändras aldrig. Regler: se `CLAUDE.md` i repots rot.

| Datum | Fil | Vad | Varför | Beslut |
|---|---|---|---|---|
| 2026-10-10 | kod, `docs/site-audit.md` (tillägg) | Sex rättelser efter första körningen: avstämning av omdirigeringsmål mot crawl, protokollrelativa bilder, skript per sajt, omdirigering till annan marknad, spårningsparametrar, felorsak vid hämtning, resurstyp PAGE | Kontrollfrågorna visade falsklarm (716 av 892 mål fungerade, 825 bildfynd var protokollrelativa) | David (granskning 2026-10-10) |
| 2026-10-10 | `sql/audit/views.sql` → `views_sources.sql` (ny) + tillägg i `docs/site-audit.md` | De två vyerna `gsc_combined_*` flyttade till egen fil; inget innehåll ändrat | De behövs före första genomlysningen, övriga vyer först efter | David (steg 6) |
| 2026-10-10 | `sites.toml` (ny), `sql/audit/views.sql` (tillägg), kod | Produktionskonfiguration för gorillasports.se och .dk (GA4 320165929, `sc-domain:`-egendomar). Filter på värdnamn (GA4) och valuta (Shopify), eftersom .se och .dk delar GA4-egendom och butik. Ny vy `gsc_combined_gorillasports_dk`. | Utan filter blandas trafik och ordrar från båda domänerna | David (uppgifter 2026-10-10) |
| 2026-10-10 | `CLAUDE.md`, `docs/ANDRINGSLOGG.md` | Regel om att dokumentation inte får skrivas över utan beslut, plus denna logg | Davids krav på kontroll över dokumentationen | David |
| 2026-10-10 | `docs/site-audit.md` | Dokumentet skapat och utökat i samma arbetspass: kontroller, kom igång, uppföljning, historik via API, nattligt jobb, behörigheter, Core Web Vitals | Första versionen av site-audit | David (uppdrag 2026-10-10) |
