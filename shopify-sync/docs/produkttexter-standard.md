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
1. Godkänner David standarden som utgångspunkt?
2. Vem poängsätter blint utöver David?
3. Mått i avsnitt 8: godkända eller ändrade?
4. Hanteringen av da/fi (översätta SEO och beskrivning samtidigt, eller utesluta)?
5. Om märken: vem verifierar märkestexter, eller ska avsnittet utelämnas tills vidare?
