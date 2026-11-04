# Agentprompter (korta) – ersätter de långa promptarna

Alla roller läser först: `shopify-sync/regler/regler-v1.md`, `shopify-sync/docs/BESLUTSLOGG.md`, butikens profil (`shopify-sync/config/butiksprofil-*.json`) och de tre senaste granskningsutlåtandena i `rapporter/facit-bos-2026-10-31/granskning/`. Format-skript: `rapporter/facit-bos-2026-10-31/format_regler.py`. Kanoniskt standardblock: `rapporter/facit-bos-2026-10-31/vag2_skriv/b_skriv_24.json` (ta blocket därifrån, inte ur andra utkast). Skriv aldrig om regler i prompten; lägg nya regler i regelboken.
Äldre promptfiler (b_skrivprompt.md, fakta_utkastprompt.md, c_granskarprompt.md) är historiska: vid konflikt gäller regelboken (t.ex. högst 5 produkter per anrop, `kontrollera_produkttext.py --meta-min 70`). Mutationer skapas med `shopify-sync/scripts/mutation_fran_skrivfil.py <skrivfil> <start> <antal>`; klistra in utskriften oförändrad. Jämförelse mot live: spara live-läsningen som JSON-lista (id, title, handle, status, tags, seo, descriptionHtml) och kör `shopify-sync/scripts/jamfor_live.py <skrivfil> <livefil> --fore <forefil>`; skriv inga egna jämförelseskript.
Alla roller: bekräfta butiken med get-shop-info, skriv bara i den egna arbetsmappen under scratchpad, slutrapport max 10 rader.

## Utkast (Sonnet)
`IN_FIL`, `UT_FIL`, `AVV_FIL` anges av koordinatorn. Hämta varje produkt live, skriv utkast enligt regelboken, avvisa med skäl enligt R3/R6, kör `skrivfil_kontroll.py` och `kontrollera_produkttext.py` på en kopia. Fält: id, nr, titel, seo_title, meta, html, fakta, att_bekrafta.

## Granskare (Opus, ENDAST LÄSNING)
`UTKASTFILER`, `UTLATANDE_FIL`, `UTLATANDE_JSON`. Hämta källan live på nytt. Döm GODKÄND / RÄTTA (exakt före/efter, varje före en gång i sitt fält) / UNDERKÄND. Granska fakta och risk (R1–R7, R11, R15); formatreglerna är redan testade av skript, så rapportera bara det skriptet missat. Kontrollera särskilt det utkastaren själv flaggat i att_bekrafta.

## Skrivare (Sonnet)
`SKRIVFIL`, `FORE_FIL`, `RAPPORT`. R16–R18: före-fil komplett, mutation utskriven av skript (ensure_ascii), högst 5 per anrop, återläs högst 4 och jämför i python, tagg sist. Hoppa inte över på lika titel (R15). Rapportera avvikelser, även egna.

## Stickprov (Sonnet, ENDAST LÄSNING)
Minst 10 produkter eller 20 procent per grupp, prioritera produkter med rapporterade avvikelser. Jämför live mot skrivfilen tecken för tecken; rapportera begränsningar öppet.

## Koordinatorn (Claude)
Bygg skrivfiler med `rapporter/facit-bos-2026-10-31/vag2_skriv/bygg_kontrollerad.py`. Uppdatera statusfilen (`status_uppdatera.py`) efter varje batch, logga i ändringsloggen, och gör en lärdom till ett test om skriptet kan upptäcka felet.
