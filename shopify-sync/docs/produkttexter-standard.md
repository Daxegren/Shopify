# Standard för produkttexter (Best of Sports först, sedan Gorilla Sports)

**Status: utkast 2026-10-29. Kräver Davids godkännande innan någon agent skriver till en butik.** Bygger på `rapporter/bestofsports-produkttexter-2026-10-25.md` (förslaget), pilotens utkast (`rapporter/bestofsports-pilot-20-produkter-2026-10-25.md`), granskningen av experiment 1 (`rapporter/forslag-bos-experiment-1-2026-10-27/plan.md`, tillägget efter granskning) och `LARDOMAR.md`. Kontrollskript: `scripts/kontrollera_produkttext.py` (tester i `tests/test_produkttext.py`).

## 1. Syfte och gräns
- Syfte: texter som är korrekta, tydliga och går att hitta, utan påhittade uppgifter.
- Gäller titel, SEO-titel, metabeskrivning och beskrivning. Pris, lager, status, bilder och taggar ändras inte.
- Ordning: Best of Sports är labb (stora reversibla ändringar, se `arbetsstrommar.md`). Gorilla Sports börjar först när David och Claude båda har verifierat att BOS-resultatet håller måttet i avsnitt 8. Gorillas texter behandlas som nivå B med små batchar.
- Piloten med 20 produkter (T33) mäts runt 2026-11-22 och experiment 1 på BOS har låg statistisk styrka (ungefär 36 förväntade klick). Standarden mäts därför mot kvalitet, inte mot ett utlovat försäljningsutfall.

## 2. Faktaregeln (viktigast)
1. **Allt som står i en text ska finnas i källan.** Källan är leverantörens text, produktdata i butiken, originaltiteln och uppgifter från David. Varje utkast ska ha ett fält `fakta` med all källtext, inklusive originaltiteln.
2. **Tal.** Varje tal i titel, SEO-text och beskrivning ska finnas i `fakta` (komma och punkt räknas lika, mellanslag som tusentalsavskiljare ignoreras). Kontrolleras av skriptet.
3. **Ursprung och märkesbakgrund** ("tillverkad i Italien", "tyskt märke") är påståenden som kräver källa. Står landet bara i parentes efter märket räknas det som obekräftat. Utan källa tas det bort. Lärdom från granskningen 2026-10-27.
4. **Leverantörens funktionspåståenden** ("dämpar ljud och vibrationer", "snäppfäste" som blir "leverlås" i titeln) tas bara med om de står ordagrant i källan och är rimliga. Gissa inte vad en detalj heter. Tvekar granskaren: ta bort.
5. **Trasig leverantörsdata** (maskinöversättningar, motsägelser mellan titel och tabell, orimliga mått, dubbla rader) skrivs inte vidare. Det som är osäkert listas under "Att bekräfta" i utkastet och beslutas av David.
6. **Hälsopåståenden** (smärta, rehab, effekt av ingredienser, "vibration", "massage", "behandling") skrivs inte. Kosttillskott är nivå C och ingår inte förrän David beslutat särskilt (EU-förordningarna 1924/2006 och 432/2012).
7. **Inga omdömen, betyg, "testvinnare" eller certifieringar** utan källa. Falska omdömen är förbjudna per se (Omnibus).
8. **Inga priser, rabatter eller kampanjer** i texten (de ändras och hör hemma i butiken). Leverans, retur och garanti kommer från standardblocket per marknad, inte från produkttexten.

## 3. Titel, SEO och metabeskrivning
| Fält | Regel |
|---|---|
| Titel | Typ, Märke, Modell, nyckelegenskap, färg på svenska. Högst 70 tecken, högst 2 kommatecken, inte i versaler, inga engelska typord, märket i normal skrivning, modellnummer behålls. Unik i hela sortimentet. |
| SEO-titel | Högst 60 tecken **inklusive** det varumärkessuffix temat lägger till. På BOS lägger temat själv till ` – BEST OF SPORTS` (läst i `snippets/doc-head-core.liquid`, ej verifierat i live-HTML), så SEO-titeln får då högst 43 tecken utan varumärke (`--seo-title-max 43 --seo-suffix " – BEST OF SPORTS"`). Varumärket ska inte stå två gånger. Unik. |
| Metabeskrivning | 130–155 tecken (mål 140–155): vad produkten är, en nyckelegenskap med källa, ingen uppmaning till köp. Unik. |

## 4. Beskrivningens struktur (samma ordning överallt)
1. **Svar först** (1–2 meningar): vad produkten är, för vem, viktigaste egenskapen. Det är texten Google och AI-tjänster tar som citat.
2. **Passar dig som** (2–3 punkter): användningsfall som följer av specifikationerna.
3. **Specifikationer**: lista eller tabell med mått, vikt, material, maxbelastning, vad som ingår. Bara uppgifter ur källan.
4. **Leverans, retur och garanti**: ett gemensamt standardblock per marknad (SE, DK, FI) inom `[[STANDARDBLOCK]] … [[/STANDARDBLOCK]]`. Siffror i blocket räknas inte som produktpåståenden.
5. **Vanliga frågor** (0–3): bara svar som går att besvara ur källan.
6. **Om märket** (högst 2 meningar): unik, verifierad text. Saknas källa utelämnas avsnittet. Leverantörens standardtext ("grundades 1972…") används inte.

Ton: sakligt, konkret, utan utropstecken och superlativ ("bäst", "ledande", "unik", "perfekt", "oslagbar"), utan uppmaningar som "upptäck". Ord från produktdata får användas, men inga påhittade fördelar.

## 5. Språk och marknader
- Grundspråket är svenska. Danska och finska översättningar av titel och beskrivning finns i butiken (läst 2026-10-27), men **SEO-fälten (`meta_title`, `meta_description`) saknar da/fi-översättning** för produkter där svensk SEO satts. Före skrivning ska vi avgöra om översättningar skrivs samtidigt eller om produkterna utesluts (`plan.md`, tillägget 2026-10-27).
- Ändras svensk beskrivning kan da/fi-översättningen bli inaktuell (`outdated`). Det ska läsas av före första batch och beslutas hur det hanteras.
- `.dk` och `.fi` ska ranka självständigt (David 2026-10-26). Texter för da och fi skrivs och granskas på respektive språk, inte maskinöversatta rakt av. Översättning av länkar och variabler kontrolleras (`{{`, `notranslate`, tomma `href`).

## 6. Processen (varje steg har ett stoppvillkor)
1. **Facit.** Cirka 30 produkter där David och Claude tillsammans godkänner texterna, plus minst 10 dåliga exempel med förklaring (till exempel de fem fynden från granskningen 2026-10-27).
2. **Skriv.** Agenten får standarden, facit och en produkt med källtext, och lämnar utkast i JSON med fälten ovan plus `motivering` och `att_bekräfta`.
3. **Kontrollera med kod.** `python3 scripts/kontrollera_produkttext.py utkast.json`. Alla FEL rättas före granskning.
4. **Granskare.** En separat agent läser utkasten mot källan och rubrikerna i detta dokument och rapporterar fynd med allvarlighet. Granskaren ändrar inget.
5. **Blind poängsättning.** David (och eventuellt fler) poängsätter 20 utkast på produkter agenten inte sett (1–5: korrekthet, begriplighet, ton). Resultatet loggas.
6. **Släpp i batchar** först när måttet i avsnitt 8 är uppnått: originaltexter sparas, kanarie (1 produkt), därefter batchar om högst 20, läs tillbaka, återställningsbatch per skrivbatch.
7. **Mät** enligt experimentdesignen (behandlings- och kontrollgrupp, 56 dagar) och logga utfallet i testloggen.

## 7. Vad skriptet kontrollerar och inte kontrollerar
- **Kontrolleras:** längder, kommatecken, versaler, dubbletter i batch, förbjudna fraser, utropstecken, superlativ, hälsoord, pris/kampanjord, engelska ord, ursprung och nationalitet utan källa, löften utan källa, tal utan källa, varumärket två gånger i SEO-titeln, avsnittsstruktur, första styckets längd.
- **Kontrolleras inte:** fakta som råkar stå felaktigt i källtexten, om texten är bra eller säljande, översättningskvalitet, och om påståenden är lagliga i alla marknader. Det är granskarens och Davids uppgift.
- Skriptets utfall på de 39 utkasten i experiment 1: 0 FEL när originaltiteln ingår i källan; utan titeln flaggas 22 tal ("5", "100"), vilket visar att källfältet måste innehålla originaltiteln.

## 8. Mått för att släppa agenten (förslag, David beslutar)
- 0 allvarliga faktafel (påhittat tal, ursprung, funktion eller hälsopåstående) på 40 utkast.
- 100 % utan FEL från skriptet innan granskning.
- Minst 80 % av utkasten godkända av David utan ändring på produkter agenten inte sett; medelpoäng minst 4 av 5 på korrekthet.
- Granskaren och David är överens (högst 1 av 10 utkast där de bedömer olika på allvarliga fynd).

## 9. Öppna beslut
*Inaktuellt sedan 2026-10-31, se avsnitt 10.*
1. Godkänner David standarden som utgångspunkt?
2. Vem poängsätter blint utöver David?
3. Mått i avsnitt 8: godkända eller ändrade?
4. Hanteringen av da/fi (översätta SEO och beskrivning samtidigt, eller utesluta)?
5. Om märken: vem verifierar märkestexter, eller ska avsnittet utelämnas tills vidare?


## 10. Beslut och erfarenheter 2026-10-31 (tillägg)
Beslut av David: standarden gäller som utgångspunkt; 30 facit-produkter godkända och skrivna; fitness först, därefter övriga Velomarket (steg 1), Gymstick (steg 2), kontroll av Gorilla-texter (steg 3); experiment 1 (432 produkter) och pilotens 20 ändras inte i vågorna.
- **Hellre för lite än för mycket.** Saknas uppgift eller motsäger källan sig: utelämna uppgiften, lägg frågan under "att bekräfta". Tunn källa (bara titel): kort intro, ingen metabeskrivning, ingen påhittad text.
- **Hälsoord i produktnamn.** Massagerulle, massagebollar och massage roller får stå som produktnamn utan effektpåståenden (kontrollskriptet undantar dem). Vibrationsplattor, massagepistoler och akupressurmattor skrivs inte i vågor.
- **Säkerhetsprodukter tas för hand med Davids ja per produkt:** hjälmar, lås, barnprodukter, bänkar/stativ/Smithmaskiner/hantelställ med last, elcyklar, **och allt med batteri, motor eller elektronisk broms** (löpband, crosstrainer, spinningcykel, motionscykel med elektronik, vågor, pulsmätare). Granskarna fann att utkastskrivarna släppte igenom dessa.
- **En agent får aldrig byta produktens namn eller typ för att komma förbi en kontroll.** Produkten lyfts till handläggning.
- **Kundtext får inte innehålla arbetstermer** ("enligt källan", "enligt titeln"). Tillverkarpåstående skrivs "enligt tillverkaren". Säkerhetslöften (till exempel "anti-burst") och belastningsuppgifter tas bort om källan inte är entydig.
- **Varianter.** Har produkten flera varianter med oförklarade namn eller olika pris får titel, SEO och specifikation inte låsa vikt, färg eller antal. Frågan går till "att bekräfta".
- **Standardblocket** anger inte fraktavgift i kronor (kan skilja per produkt). Beställningsvaror får meningen om längre leveranstid.
- **SEO-titel** som är identisk med produkttiteln lagras tom av Shopify (avsett beteende). SEO-titel skrivs högst 43 tecken utan varumärkessuffix; om temat lägger till suffix är fortfarande inte verifierat.
- **Process i vågor (beslutad):** utkast högst 15 produkter per agent; oberoende granskare (annan agent) hämtar källan på nytt och dömer OK/RÄTTA/AVVISA; rättare rättar; David poängsätter ett stickprov (20 i första vågen); skrivning i batchar om högst 25 med kanarie (3) först, återläsning, original sparat och ny kontroll dagen efter nattsynken. Originalet sparas som titel och SEO exakt samt text som ren text.
- **Leverantörssynken (Velomarket3)** ändrar status (aktiv/arkiverad/utkast) och kanaler men inte titlar enligt produkthändelserna. Titlar på 12 pilotprodukter hade ändå gått tillbaka efter 2026-10-25 (orsak ej fastställd). Kontrollfråga: `sql/analys/bos/13_kontroll_skrivna_titlar.sql`.
- **Verktyg och filer:** `rapporter/facit-bos-2026-10-31/` (`bygg_utkast.py` bygger kontrollfiler, `bygg_skriv.py` bygger skrivdata, `handhavd_ids.txt` listar produkter som tas för hand, moduler `vag1_*.py` och `fix_*.py` är utkast, senaste modul vinner vid dubbletter).
- **Formatregler (David 2026-11-01), gäller alla produkter:** (1) stor bokstav direkt efter kolon ("Färg: Svart"); (2) stor bokstav på beskrivande ord i titel och SEO-titel ("Barncykel Tabou Rocket Lite MG, 14 tum, Röd och Vit"). Små ord (och, med, för, i, på, av, till) och enheter (cm, mm, kg, tum, hk, lux) behåller liten bokstav, förkortningar och modellnamn lämnas orörda. Implementerat i `rapporter/facit-bos-2026-10-31/format_regler.py` och anropas av `bygg_utkast.py` och `bygg_skriv.py`.
- **Tunn källa, mer info (David 2026-11-01):** för produkter med bara titel får uppgifter hämtas från flera återförsäljarsidor om de är entydiga (material, yta). De märks "att bekräfta" som sekundärkälla och används inte för mått, vikt eller belastning.

## 11. Tillägg 2026-11-02 (David: ja)
- **Rullskridskor och inlines är säkerhetsprodukter** och skrivs inte i vågor. De tas för hand med Davids ja per produkt. Produkterna med risk för personskada vid fel text eller fel användning (skydd, last, barn) hör hit; id finns i `rapporter/facit-bos-2026-10-31/handhavd_ids.txt`.
- **Gymtalk** är talk för bättre grepp och översätts inte. Namnet får stå kvar i titel och text; genus: en gymtalk, talken.
- **Fitnessmat Pro** (inte "Fitness Mat Pro") är den stavning leverantörskällorna använder.

## 12. Tillägg 2026-11-03 (David)
- **Reflexer och reflexdekaler** behandlas som säkerhetsprodukter (synlighetslöften) och skrivs inte i vågor. De tas för hand med Davids ja per produkt.
- **Framkorgar och bakre korgar utan lastuppgift** får skrivas, om texten inte lovar någon lastgräns. Korgar och väskor med lastgräns i källan skrivs inte.
- **Stänkskärmar/framskärmar** med kompatibilitet "enligt tillverkaren" och **innerslangar** med ETRTO i titeln (ordet "Innerslang") får skrivas.
- **Bartejp heter "Handtagstejp"** (inte "Styretape" eller "Styrlinda").
- **Gymtalk** översätts inte (se avsnitt 11).

## 13. Process och status vid kontextbyte 2026-11-03 (tillägg)
**Processen i vågor (gäller alla grupper):** (1) utkast: Sonnet-agent, 25 produkter per agent, prompt i `rapporter/facit-bos-2026-10-31/vag2_skriv/` (`c_utkastprompt.md` Gymstick, `b_utkastprompt.md` Velomarket-tillbehör, `k_utkastprompt.md` cyklar och cykeldelar, med inbyggda lärdomar); (2) oberoende granskning: Opus-agent hämtar källan live, dömer GODKÄND/RÄTTA/UNDERKÄND med exakt före/efter (`c_granskarprompt.md`); Sonnet som granskare underkändes i test (41 procent av Opus fynd); (3) skrivfil byggs maskinellt av utkast + utlåtanden (`bygg_c_skriv.py`, `bygg_k_skriv.py`; b-grupperna byggdes med samma logik inline): UNDERKÄND utesluts, rättningar appliceras, dubbletter och längder kontrolleras mot allt redan skrivet; (4) skrivning: Haiku-agent enligt `b_skrivprompt.md`, kanarie om 3 först, högst 8 produkter per mutation (6 för cyklar; Shopify avvisar dokument över 16 384 tecken), före-läge sparas först, allt läses tillbaka, taggen `texter-klara` läggs sist; (5) stickprov 20 procent (minst 10) av Sonnet-kontrollant, full kontroll vid avvikelse; (6) nattkontroll av titlar 30 produkter per natt i en vecka.
**Kontrollskriptet** läser fältet `beskrivning`, inte `html`: kör på kopia med html mappad till beskrivning och standardblocket inom `[[STANDARDBLOCK]]…[[/STANDARDBLOCK]]`, med `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS"`. Varningen om rubriken "passar dig som" är avsiktlig (rubriken heter "Passar för"); decimalkomma i mått räknas som kommatecken av skriptet.
**Skyddet mot överskrivning:** Velomarket-synken skriver titel/beskrivning bara vid skapande, rensningen raderar aldrig produkter med taggen `texter-klara`, sammanslagningen av dubbletter är stoppad (torrkörning). Se överlämningsfilen `rapporter/overlamning/overlamning-2026-11-03.md` för status, filer och öppna beslut.


## 14. Korta metabeskrivningar, SEO-skrivning och oklar växelgrupp (beslut 2026-11-03)
- **Kort meta i stället för null (David 2026-11-03):** produkter med tunn källa får en kort, sann metabeskrivning byggd på den godkända inledningen (typ, märke, material, mått). Under 70 tecken läggs "Finns hos BEST OF SPORTS." till. Gränsen 130–155 tecken gäller fortfarande för produkter med tillräcklig källa. Beskrivningen fylls aldrig ut med text som saknar underlag.
- **SEO skickas alltid som `seo{title, description}`** när skrivfilen har en meta, även när SEO-titeln är lika med titeln. Utelämna aldrig seo-objektet, annars försvinner metabeskrivningen. Är meta null skickas bara `seo{title}`.
- **Oklar växelgrupp (David 2026-11-03):** cyklar där källan inte anger om växlingen är mekanisk eller elektronisk (Shimano 105/GRX, SRAM Apex/Eagle) får skrivas. Texten återger växelgruppens namn exakt som källan anger det och säger eller antyder aldrig mekanisk, elektronisk, trådlös eller batteridriven. Elcyklar, motor och batteri enligt källan skrivs inte. Cyklar med motsägande växelsystem i källan skrivs utan växelgrupp och antal växlar.
- **Taggarna Gymstick och Velomarket ändras aldrig** (David 2026-11-03).
- **Skrivning av långa mutationer:** skriptet skriver ut mutation och variabler, huvudagenten klistrar in dem ordagrant. Se LARDOMAR 2026-11-03.

## 15. Vinterprodukter frisläppta (beslut av David 2026-11-03)
- **Pulkor och kälkar** får skrivas med bara produktens egna uppgifter och utan säkerhets- eller barnpåståenden; ålder eller maxvikt återges oförändrat "enligt tillverkaren". Tydliga barn- och babyprodukter hålls utanför.
- **Isskridskor** får skrivas på samma sätt när källan entydigt anger modell, typ och storlek/flex. Rullskridskor, inlines och barn-/juniorprodukter hålls utanför.
- **Isbroddar och liknande grepphjälpmedel hålls utanför** (David: behåll).
- Vinterprodukter prioriteras före övriga Velomarket-grupper under vintersäsongen. Frisläppta ids står i `rapporter/facit-bos-2026-10-31/vag2_skriv/frisläppta_vinter_2026-11-03.txt`.
