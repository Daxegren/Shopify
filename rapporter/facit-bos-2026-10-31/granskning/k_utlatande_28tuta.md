# Granskningsutlåtande k_28tuta: cykeltutor (28238, 28244, 28246)

Granskare: oberoende (Opus), 2026-11-05. Bara läsning: inget har ändrats i Shopify och inget har committats.
Utkast: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_28tuta_utkast.json`. Maskinläsbart: `vag2_skriv/k_utlatande_28tuta.json`.

## Resultat

**3 godkända, 0 att rätta, 0 underkända.**

Underlag: regelbok v1.8, LARDOMAR (även posten från 2026-11-05 om rättningar i flera delar), butiksprofilen (`godkanda_typord.cykeltuta`, Davids beslut 2026-11-05) samt de tidigare utlåtandena `k_utlatande_28st.md` och `k_utlatande_28uv.md`.

## Kontroller

- **Butik och källa:** live via Admin API (`shopify_api.py`, bara läsning). Butiken är BEST OF SPORTS (bestofsports.se). Alla tre produkterna är ACTIVE och har en variant (Default Title, 129 kr). Ingen har taggen "På beställning", så leveranstidsmeningen ska inte finnas, och den finns inte.
- **Spärrlista och maskinkontroll:** `skrivfil_kontroll.py` gav 0 fel och 0 varningar. Ingen av produkterna står på spärrlistan.
- **Standardblock:** tecken för tecken lika med `b_skriv_24.json`.
- **Längder:** titlarna har 26, 36 och 22 tecken och ett kommatecken var. SEO-titlarna är lika med titlarna och högst 36 tecken. Metatexterna har 133, 137 och 107 tecken och innehåller verb.
- **Unikhet:** titel, SEO-titel och meta krockar inte med något annat utkast, någon `k_skriv_*.json` eller med live-butiken. En sökning på "tuta" och "Cykeltuta" gav inga träffar.
- **Produkttyp:** webbkällan bekräftar producentkoderna. På centrumrowerowe.pl (hämtad 2026-11-05) heter 34062 "Trąbka PSI PATROL Girls", 9156 "Trąbka DISNEY Frozen 2" och 9129 "Trąbka DISNEY Minnie". Alla tre är tutor. Typordet Cykeltuta är godkänt av David.
- **Påståenden:** inga påståenden om ljud, uppmärksamhet, säkerhet, kvalitet, ålder eller enkel montering finns kvar. Mallens "högt ljud", "högkvalitativa komponenter" och "enkel installation" är borttagna.
- **Disney:** ordet står bara på 28244. Live-texten "Disney-figurer" är en mallmening som också står på Paw Patrol och räcker därför inte ensam. Webbkällan för exakt produktkod 9156 heter "Trąbka DISNEY Frozen 2", och adressen anges i `att_bekrafta` (R1 v1.6/v1.7). På 28238 (Paw Patrol är inte Disney) och 28246 (live-källan säger bara "Musse-inspirerad") är Disney rätt utelämnat.

## Tabell

| nr | id | dom | skäl |
|---|---|---|---|
| 28238 | 10541366968586 | GODKÄND | Live: 'Paw Patrol trumpet, pink', 34062. Måtten 6,5 cm och 14 cm, att installationsdelarna ingår och tillverkaren Seven Polska stämmer ordagrant. Paw Patrol och rosa kommer från live-titeln. Disney och alla omdömen är utelämnade. |
| 28244 | 10548282753290 | GODKÄND | Live: 'Trombone Frozen 2, green-purple', 9156. Mått, installationsdelar och Seven Polska stämmer. Disney stöds av webbkällan för just 9156. Färgen grön-lila kommer från live-titeln. |
| 28246 | 10561327956234 | GODKÄND | Live: 'Trumpet Minnie, pink', 9129. Metall och plast, 6,5 cm och 14 cm stämmer. Disney och tillverkare saknas i källan och är rätt utelämnade (webbsidan anger Seven 1, inte Seven Polska). "Bekväm" och "rolig" är borttagna. |

## Anmärkningar (inga rättningar)

1. **Gamla utkast med samma id:** `k_28t_utkast.json` (28238) och `k_28u_utkast.json` (28244, 28246) innehåller de tidigare underkända utkasten för samma produkter, med typordet Cykelklocka eller Trumpet. Byggskriptet får bara använda `k_28tuta_utkast.json`, annars får produkterna två texter. Kontrollera att skrivfilen har tre produkter och att varje id förekommer en gång.
2. **Frozen 2 eller Frost 2:** den redan skrivna syskonklockan 28013 heter "Cykelklocka Frost 2" (filmens svenska namn). 28244 följer live-titelns "Frozen 2". Det stämmer med R1 och behöver inte rättas, men David kan välja en gemensam form för framtida Frozen-produkter.
3. **Syskonprodukt:** 'Paw Patrol trumpet, blue' (10541366739210) är inte skriven. Får den ett utkast senare skiljer den sig från 28238 genom färgen.
