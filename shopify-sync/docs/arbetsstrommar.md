# Arbetsströmmar: så delas arbetet mellan flera agenter

Tillägg 2026-10-26. Beslutat av David samma dag: tre arbetsströmmar, en samordnare och en granskare. Syftet är att flera saker kan göras samtidigt utan att en enda session blir överlastad, och att fel fångas innan de når David. Dokumentet är ett arbetssätt, inget är byggt eller automatiserat.

## Roller
| Roll | Gör | Gör inte |
|---|---|---|
| **David** | Beslutar, kör kommandon i Cloud Shell, gör ändringar i det publicerade temat, ger behörigheter | |
| **Samordnare** (huvudsessionen) | Delar ut uppdrag, tar emot resultat, för över loggar till `ANDRINGSLOGG.md`, skriver beslutsunderlag, sköter temaarbete och beslut som kräver Davids manuella steg, löser konflikter mellan strömmar | |
| **Ström 1, Drift och mätning** | Se nedan | Ändrar inte i butikerna |
| **Ström 2, Innehåll och sök** | Se nedan | Ändrar inte kod i `src/` (beställer av ström 1) |
| **Ström 3, Lönsamhet och annonser** | Se nedan | Ändrar inte annonskonton eller priser |
| **Granskare** | Läser varje slutsats och förslag mot data och kod innan David ser det. Skrivskyddad | Skriver inga ändringar, utom sitt eget utlåtande |

## Gemensamma regler (gäller alla)
1. **Ingen ändring i någon butik, något tema, något annonskonto eller någon Google Cloud-tjänst utan Davids ja.** Godkännandenivåerna A, B och C i `standardtester.md` (T30–T40) gäller.
2. **Ingen kan köra `gcloud`, `bq` eller `site-audit` mot Google Cloud, och ingen kan skriva till det publicerade temat.** Det görs av David i Cloud Shell och temaredigeraren. Agenter skriver kommandon och planer, och läser resultat som David klistrar in eller som Shopify-kopplingen läser.
3. **Hemligheter läggs aldrig i chatten eller i filer.** Det gäller nycklar, token, koder och inloggningsfiler.
4. **Läs först:** `CLAUDE.md`, `shopify-sync/docs/LARDOMAR.md`, `shopify-sync/docs/standardtester.md`, `rapporter/tackningskarta-2026-10-26.md` (kör `python3 scripts/audit_tackning.py` för färskt läge) och senaste beslutsfilen i `rapporter/`.
5. **Innan ett förslag lämnas:** lista vad som redan finns (`git grep`, `audit_tackning.py`), läs de berörda filerna i sin helhet, och skriv i förslaget **Täckning:** vad som är genomgånget och vad som inte är det. Skilj bevisat från hypotes. Rekommendera inte "ja" innan helheten är känd.
6. **Mått och tester** ska kunna misslyckas på det de ska kontrollera, och testas mot ett känt fall.
7. **Ingen agent skapar kundomdömen, betyg, citat eller "verifierad"-märken.** Inga hälsopåståenden utöver de EU-godkända (förordning 1924/2006, 432/2012). Kosttillskott går på nivå C.
8. **Original sparas** (`rapporter/shopify-original-<datum>/`), skriven text läses tillbaka och jämförs, och allt loggas.

## Filer, grenar och loggar
- **Ägande:** varje ström äger de filer som anges nedan. Vill en ström ändra en annan strömmens fil beställer den det via samordnaren.
- **Hjälpagenter i huvudsessionen** committar inte. De lämnar filer och text till samordnaren, som committar på sessionens gren.
- **Egna sessioner** arbetar på en egen gren (`claude/ström-1-drift`, `claude/ström-2-innehall`, `claude/ström-3-lonsamhet`) som David godkänner när sessionen startas, och David mergar.
- **Loggar:** varje ström skriver sina ändringar i `rapporter/logg/<ström>-<datum>.md` (en rad per ändring: datum, fil, vad, varför, beslutad av). Samordnaren för över raderna till `ANDRINGSLOGG.md` samma dag, så att den gemensamma loggen inte får sammanslagningskonflikter. Gamla poster ändras aldrig.
- **Beslutsunderlag:** varje session som avslutar ett arbetspass skriver `rapporter/beslut-ÅÅÅÅ-MM-DD-<n>.md` enligt `CLAUDE.md`, med exakt de fem rubrikerna.
- **Överlämning mellan strömmar:** `rapporter/overlamning/<från>-<till>-<datum>.md` med: vad som behövs, varför, vilka filer, och när.

## Ström 1: Drift och mätning
**Uppdrag:** att genomlysningen, datakällorna och verktygen fungerar, och att åtgärder kan utföras säkert.
- **Testkatalog:** T1, T2, T11, T27, T38, T39 (och utför-ramverket).
- **Äger:** `shopify-sync/src/site_audit/**`, `shopify-sync/deploy/**`, `shopify-sync/tests/**`, `shopify-sync/sites.toml`, `scripts/audit_*`, `scripts/kontrollera_datakallor.sh`, `scripts/onsite_kontroll.py`, `scripts/schema_kallor.py`.
- **Startuppgifter:**
  1. Bekräfta att den ombyggda avbilden körs och läs nattens resultat med `audit_tackning.py` (nya kontroller: `multiple_canonical_tags`, `schema_url_other_domain`, `gtm_container_loaded_twice`, `shipping_details_missing`, `collections_without_breadcrumb_schema`).
  2. Kör `scripts/kontrollera_datakallor.sh` och reda ut vad som faktiskt finns och är färskt för BOS (Search Console per domän, GA4, Shopify, annonser, Merchant). Rätta det som i dokumenten sagts om BOS datakällor om fynden säger annat.
  3. `site-audit test due` och valbart utvärderingsfönster (T38).
  4. Utför-ramverket (T39): designa först, bygg sedan, på mönstret i `scripts/redirects_gorilla_apply.py`.
  5. Leveransen av `tracking`-kontrollerna (GTM dubbelladdad) mot nätverksmätning i webbläsare.
- **Behöver från David:** köra deploy, Search Console- och GA4-behörigheter, Cloud Shell-körningar.

## Ström 2: Innehåll och sök
**Uppdrag:** förslag som gör att sidor och artiklar syns och konverterar, byggda på egen data. Bara förslag och analys.
- **Testkatalog:** T4, T5, T31 (spec), T32, T33, T34, T35, T36, T37.
- **Äger:** `shopify-sync/sql/analys/{longtail_blogg,sokfragor_luckor,kategori_sokord,ai_hanvisningar,produktdata_kvalitet}.sql`, `rapporter/forslag-*`, `rapporter/kategoritexter-utkast-*`, `rapporter/titlar-lag-ctr.csv`.
- **Startuppgifter:**
  1. Grupperade förslag ur `longtail_blogg.sql` (Gorilla SE först: 137 frågor, 80 % har redan en artikel som bästa sida): vilka artiklar som ska förbättras och vilka ämnen som saknar artikel. Fönstret kan utökas till 365 dagar.
  2. FAQ-förslag för kategorisidor från riktiga sökfrågor.
  3. Förslag på titlar och metabeskrivningar för sidor med låg CTR.
  4. Specifikation av AI-stilkontrollen (T31); koden beställs av ström 1.
  5. Vänta med T33 (produktbeskrivningar) till pilotens utvärdering runt 2026-11-22; T36 börjar med Search Console (beslut), Ahrefs kräver köpt åtkomst.
- **Öppna frågor:** vad "tyskarna" avser (T37, möjligen Gorillas huvudkontor), Reddit som organisk plattform (T40).

## Ström 3: Lönsamhet och annonser
**Uppdrag:** förstå vad som är lönsamt, och vilka åtgärder i pris, frakt och annonser som är värda att pröva. Bara analys och förslag.
- **Testkatalog:** T23, T24, T25, T26, T30, T40.
- **Äger:** `shopify-sync/sql/analys/{frakt_*,net_profit_ordrar,priser_strax_under_gransen,cos_30d,marginal_*,annonser_*,omsattning_*,portfolio_30d,matintegritet,merchant_avvisade}.sql`, `shopify-sync/data/net_profit_sku.csv`, `shopify-sync/scripts/hamta_vikter.py`.
- **Startuppgifter:**
  1. Net Profit version 2 (kräver vikter ur Shopify och tabellerna `net_profit_sku` och `gorilla_vikter`); frågan är skriven men inte körd.
  2. Priser strax under fraktgränsen (`priser_strax_under_gransen.sql`, inte körd), inklusive Pull Up Bar Multi Dörr (799 kr).
  3. Fraktgränsen: konvertering per varukorgsvärde i GA4 (kräver att GA4-händelserna ligger i BigQuery).
  4. Performance Max-analys för DK (ROAS 2,94 mot mål 5).
  5. Prisrådgivare (T30): design med golv för marginal och tak för ändring per dag. Aldrig automatisk prisändring.
- **Öppna frågor:** vad som avses med COS 22 % (vilken nämnare), och fraktprislista per vikt.

## Granskaren
Läser varje slutsats, förslag eller siffra som ska nå David. Skrivskyddad. Lämnar ett utlåtande: godkänt, godkänt med anmärkning eller underkänt, med bevis. Kontrollerar:
1. Är det som redan finns genomgånget (kontroller, senaste fynd, berörda filer i sin helhet)? Står **Täckning** med?
2. Är varje siffra spårbar till sin källa? Är aggregeringar avstämda mot totalen?
3. Är påståenden märkta som bevisade eller som hypotes?
4. Kan testet misslyckas på det det ska kontrollera? Är mätet testat mot ett känt fall?
5. Är butikens hela konfiguration läst innan "saknas" påstås (alla block med samma butik)?
6. Är urvalets storlek angiven?
7. Stämmer godkännandenivån (A, B, C)? Är regeln om hälsopåståenden och omdömen följd?
8. Rättar uppdraget sådant som tidigare sagts fel?
9. Står det något som kräver ett manuellt steg som agenten inte kan göra?

## Hur ett uppdrag formuleras (mall)
```
Uppdrag: <en mening>
Ström: <1, 2 eller 3>
Läs först: CLAUDE.md, LARDOMAR.md, standardtester.md, tackningskarta, <relevanta filer>
Du äger: <filer>
Du får inte: <regler>
Leverans: <fil och format>, med avsnittet Täckning
Klart när: <kriterium>
```

## Start och uppföljning
- **Start:** högst två strömmar aktiva samtidigt tills vi sett hur det fungerar, eftersom du är flaskhalsen. Förslag: ström 1 och ström 2 först (ström 2 kan börja med Gorilla-data som redan finns).
- **Uppföljning efter en vecka:** antal sammanslagningskonflikter, antal fel som granskaren fångade, hur mycket tid det tagit för David, och om uppdragen blev tydligare.
- **Inaktuellt:** om strömmarna ändras ska det göras som ett nytt avsnitt med datum, inte genom att skriva om det här.

## Tillägg 2026-10-27: riskprofil per butik och start av hjälpagenter
**Beslut (David, 2026-10-27):** hjälpagenter är en bra början. Starta nu. **Best of Sports (BOS) är labbet:** stora förändringar för att lära. **Gorilla Sports ska bara få förändringar som är 99,9 % säkra.**

### Så tolkas beslutet (säg till om något ska vara annorlunda)
**BOS, labb.** Tillåtet inom ramen nedan utan ett nytt ja per enskild ändring, så länge varje omgång dokumenteras i en plan före skrivning och alla villkor är uppfyllda:
- Gäller **reversibla innehållsändringar** i Shopify: SEO-titel, metabeskrivning och beskrivning på produkter, kategorier, sidor och artiklar (grundspråket svenska; översättningar rörs inte), FAQ-text i kategoribeskrivning, alt-text på bilder, och nya omdirigeringar med verifierat mål.
- **Kohortdesign:** en behandlingsgrupp och en lika stor, matchad kontrollgrupp som lämnas orörd. Högst 300 objekt per omgång.
- **Villkor per omgång:** originalen sparade i `rapporter/shopify-original-<datum>/`, skriven text inläst och jämförd tecken för tecken, loggad (`ANDRINGSLOGG.md`, `shopify-andringar-*.md`, beslutsunderlag), testpost i testloggen (T8) med utvärderingsfönster (56 dagar för SEO-texter), och en plan som David har kunnat se.
- **Kräver fortfarande Davids uttryckliga ja per ändring:** pris, lager, publicering, avpublicering eller radering av produkter och kategorier, allt som rör kosttillskott, hälsopåståenden, omdömen och betyg, rabattkoder, appar, annonser, kunddata, e-post och tema. Temat kan inte skrivas av Claude och ändras av David.

**Gorilla, säkert.** Bara förändringar där alla dessa gäller:
1. Beviset är entydigt och bygger på hela genomsökningen, inte ett urval.
2. Ändringen är exakt reversibel och en återställningsfil är klar före körning.
3. Ändringen rör inte rankingkänsligt innehåll (rubriker, texter), pris, annonser, spårning eller mallar.
4. Resultatet kontrolleras efteråt mot ett mått som kan misslyckas.
5. Skadan om något ändå går fel är liten och synlig.
- Exempel som uppfyller kraven: omdirigeringar där målet är verifierat som 200, och objektivt felaktiga tekniska värden.
- Gorillas butik når Claude inte; ändringar görs av David med skript (torrkörning är standard) och verifieras efteråt.
- Allt annat blir förslag på nivå A och B, med David som beslutar.

### Hjälpagenter: vad som startade 2026-10-27
- **Ström 1 (kod):** `site-audit test due` och valbart utvärderingsfönster (T38), kontroll av att `scripts/kontrollera_datakallor.sh` använder rätt tabell- och kolumnnamn, och en designskiss för utför-ramverket (T39).
- **Ström 2 (BOS-labb):** plan för experiment 1 på BOS: kohorter, utkast på titlar och metabeskrivningar för behandlingsgruppen, sparade original, utvärderingsplan. Bara förslag; ingenting skrivs till Shopify förrän planen är granskad.
- Hjälpagenterna committar inte. De lämnar filer, och samordnaren granskar och committar. Ström 3 startar inte än (högst två strömmar samtidigt).
