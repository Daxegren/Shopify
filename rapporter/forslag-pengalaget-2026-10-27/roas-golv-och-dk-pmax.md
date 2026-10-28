# ROAS-golv och Performance Max DK (förslag, ström 3, 2026-10-27)

**Status:** analys och förslag (nivå A). Ingenting är ändrat i något annonskonto, någon butik, något tema eller Google Cloud. Varje ändring i annonskontot som beskrivs här är **nivå C och kräver Davids och Rudes uttryckliga ja** före genomförande. Jag har inte kunnat köra något mot BigQuery eller Google Ads; alla siffror kommer ur tidigare resultatfiler med fil och datum angivna. Skilj genomgående mellan **bevisat** (siffra ur en körd fråga) och **hypotes** (min tolkning).

## Sammanfattning
- Vilken ROAS som är break-even beror helt på marginalen, och marginalen är inte säkerställd. Med Net Profit version 1 (arkets kostnader, frakten överskattad) blir break-even-ROAS på rörlig bidragsmarginal ungefär **2,7 (SE) och 2,9–3,0 (DK)** om plattformens värde är inklusive moms, och 2,2–2,4 om det är exklusive moms. Med bruttomarginalen ur Shopifys inköpspris (som är överskattad) blir den 1,8–1,9. Det är en skattning med stora förbehåll (avsnitt 1).
- Performance Max DK hade ROAS 2,94 de senaste 30 dagarna (`beslut-2026-10-26.md` §13). Det ligger **vid** den uppskattade break-even-nivån, inte klart över. Det betyder att fler annonskronor i samma kampanj sannolikt inte ger mer vinst om de ger samma ROAS som i dag, och att tillräckligt lågt ROAS-mål kan göra saken sämre.
- Hypotesen att ett för högt mål (5) bromsar volymen är **delvis stödd** (målet ligger långt över utfallet, budgeten används till ca 22 %, visningarna föll 80 %) men **inte avgjord**: ROAS föll först och värdet per klick halverades samtidigt på Meta DK, vilket pekar på att något i konverteringen på Danmark försämrats, inte bara att Google budar försiktigt (avsnitt 2).
- Jag föreslår ett billigt **steg 0** utan ändring (kolla vad som ändrats och vilka produkter som är slut) och därefter ett begränsat test (avsnitt 3) med lägre budgettak och tydliga stoppregler. Utfallet kan lika gärna bli att målet inte var begränsningen.

## Täckning
Genomläst i sin helhet: `beslut-2026-10-26.md` (avsnitt 7–20, plus 21–31 översiktligt), `trafik-konvertering-resultat-2026-10-13.txt`, `omsattning-30d-resultat-2026-10-12.txt`, `annonser-resultat-2026-10-14.txt`, `beslut-2026-10-14.md` (avsnitt om annonser, N och O), `beslut-2026-10-18-7.md` (månadsanalys), SQL-filerna `cos_30d.sql`, `marginal_30d.sql`, `marginal_stickprov.sql`, `net_profit_ordrar.sql`, `annonser_kampanjer_30d.sql`, `annonser_vecka.sql`. **Inte tillgängligt och därför inte analyserat:** Google Ads gränssnitt (ändringshistorik, budgivningsstrategins historik, andel förlorade visningar, auktionsinsikter, sökordsrapport), Shopify admin, arket "SWE - Net Profit" i sin helhet (jag litar på hur det är återgivet i `beslut-2026-10-26.md` §17–18), och DK-fliken.

---

## 1. Break-even-ROAS från bidragsmarginalen

### Definition
- **ROAS** = plattformens konverteringsvärde / annonskostnad (samma som i `cos_30d.sql`: `conversions_value / cost`).
- **M** = bidragsmarginal efter alla rörliga kostnader som hör till en order (varor, frakt, betalavgifter), före annonskostnad, som andel av det belopp plattformen räknar som värde.
- En annonskrona ger ROAS × M kronor i bidrag. **Break-even-ROAS = 1 / M** (annonsen betalar sig precis). För ett krav på vinst efter fasta kostnader behövs ett högre ROAS (se "Fullt belastad").

### Vilka marginaler finns, och hur säkra är de
| Underlag (fil, datum) | Siffra | Omräknad till M (andel av plattformens värde, om värdet är inklusive 25 % moms) | Break-even-ROAS | Förbehåll |
|---|---|---|---|---|
| Bruttomarginal ur Shopifys `unit_cost` (`marginal_30d.sql`, resultat i `beslut-2026-10-26.md` §14, 30 dagar, täckning 98 %) | Break-even-COS exklusive moms: **54,3 % (SE), 52,9 % (DK)** | 54,3 % / 52,9 % | **1,84 / 1,89** | **Överskattad.** Frakt, betalavgifter och returer ingår inte. Shopifys inköpspris avviker från arket (§18: Kettlebell GS Vinyl 253 mot ca 158, Viktskivor PRO 62 mot ca 104). Antaget att priser är inklusive 25 % moms (§14) |
| Net Profit version 1 (`net_profit_ordrar.sql`, §18, 30 dagar) | Bidrag (contribution) **46,2 % (SE), 43,3 % (DK)** av nettoförsäljning exklusive moms | 46,2 / 1,25 = **37,0 %**; 43,3 / 1,25 = **34,6 %** | **2,71 / 2,89** | Frakten är **överskattad** (summa per produkt, inte per paket), vilket pressar bidraget nedåt (konservativt); kurserna avviker från arkets; täckning 96,5 % (SE), 97,1 % (DK); version 2 med vikter är inte körd |
| Samma, DK-siffran baklänges ur nettovinsten i §18 | 6,2 % nettovinst + 22,0 % annonser + 13 % personal och övrigt = **41,2 %** | 41,2 / 1,25 = **33,0 %** | **3,03** | §18 anger 43,3 % som bidrag men nettovinsten 6,2 % går inte ihop med det (43,3 − 22,0 − 13 = 8,3). SE går ihop (6,7 + 24,4 + 15 = 46,1). Skillnaden är **oförklarad** (troligen olika urval eller fraktvariant) och DK:s bidrag ligger därför mellan 41 och 43 % |
| Om plattformens värde är **exklusive** moms (oklart) | Bidrag av nettoförsäljning direkt | 46,2 % / 43,3 % | 2,16 / 2,31 | Se "Moms" nedan |

**Bevisat:** siffrorna ovan är de som redovisades. **Hypotes:** att ingen av dem är den sanna marginalen. Davids egna ark är den källa som ska gälla (§18), men `Contribution_Model_GorillaSports` används inte (§17) och Net Profit version 1 är en första körning.

### Känslighet: break-even-ROAS för ett intervall av marginaler
| M (andel av plattformens värde) | Break-even-ROAS |
|---|---|
| 25 % | 4,00 |
| 30 % | 3,33 |
| 33 % (≈ DK baklänges) | 3,03 |
| 35 % | 2,86 |
| 37 % (≈ SE, Net Profit v1 inkl. moms) | 2,71 |
| 40 % | 2,50 |
| 45 % | 2,22 |
| 50 % | 2,00 |
| 54 % (bruttomarginal exkl. moms, överskattad) | 1,85 |
| 60 % | 1,67 |

(§15 i `beslut-2026-10-26.md` redovisar samma känslighet: M 54 % ger 1,85; 45 % ger 2,2; 35 % ger 2,9; 30 % ger 3,3.)

### Fullt belastad (hypotes om vad målet 5 kan bygga på)
- Arkens plan (SWE, återgiven i §17–18): personal 10 % och övrigt 5 % av nettoförsäljningen i SE, 8 % och 5 % i DK. Om även de ska täckas av varje order blir kravet SE 1 / ((46,2 − 15) / 1,25) = **4,01** och DK 1 / ((43,3 − 13) / 1,25) = **4,13** (4,43 med DK-bidraget 41,2 %).
- Arkets marknadsföringsandel är 30 % (SE) och 25 % (DK) av nettoförsäljningen. 25 % av nettoförsäljningen motsvarar 20 % av intäkten inklusive moms, alltså **ROAS 5, vilket är DK:s mål**. 30 % motsvarar 24 %, ROAS 4,17; SE:s mål är 4,55 (22 %). Detta är en **hypotes** som redan står i §16–17 (att målen är härledda ur planen); den är inte bekräftad av Rude eller David.
- Konsekvens: ROAS-målet 5 kan vara en *planeringsnivå* (hela kostnadsstrukturen täckt), medan det relevanta kravet för frågan "ska vi köpa mer volym" är den **rörliga** break-evenpunkten (ca 2,7–3,0), under förutsättning att personal och övriga kostnader i praktiken är fasta. Om de inte är fasta (t.ex. mer volym kräver mer kundtjänst och logistik) ligger rätt nivå däremellan. **Det avgörs av David, inte av data.**

### Plattformens värde är inte butikens omsättning
- Plattformens värde är Googles respektive Metas egen tillskrivning och överlappar (`tillvaxtdata.md`). I `cos_30d` (§12, 30 dagar) var Google + Metas värde tillsammans 450 230 SEK mot butikens omsättning 623 874 SEK i SE (72 %), och 167 141 DKK mot 271 880 DKK i DK (61 %). Det visar att summan inte uppenbart överstiger butiken, men det säger inget om hur mycket som hade sålts ändå.
- Shopifys egen kanaluppgift (senaste besök, `omsattning_30d`, 2026-10-13, P1 12 sep–11 okt) tillskriver Facebook-etiketterade ordrar i SE 17 607 SEK (+ 0 för "Facebook"), medan Metas eget värde för SE var 202 455 SEK i samma period (`annonser-resultat-2026-10-14.txt`). Tillskrivningsmodellerna är olika (senaste klick mot Metas fönster och visningar), så siffrorna kan inte jämföras rakt av, men gapet visar att **ROAS som plattformen rapporterar kan ligga väl över det annonserna faktiskt orsakar**. Hur mycket är okänt.
- Om endast andelen *i* av plattformens värde är verklig merförsäljning blir den effektiva break-evenpunkten **1 / (M × i)**:

| Inkrementell andel i | SE (M 37,0 %) | DK (M 34,6 %) |
|---|---|---|
| 100 % | 2,71 | 2,89 |
| 80 % | 3,38 | 3,61 |
| 60 % | 4,51 | 4,81 |

  Varumärkessökning har sannolikt låg inkrementalitet (kunden hade hittat butiken ändå); det är en hypotes, inte uppmätt.

### Moms
Det är inte verifierat om Google/Meta-värdet inkluderar moms. Kontroll: jämför konverteringsvärdet för en känd order med orderns summa (nivå A, läsning; David eller Rude). Fram till dess används **inklusive moms** som huvudfall eftersom Shopifys `total_price` och butiksomsättningen i `cos_30d.sql` är inklusive moms, och flaggar exklusive moms som alternativ (ROAS 2,2–2,3).

### Övriga förbehåll
- Returer och ersättningar ingår inte. Återbetalt var ca 1,2 % (SE) och 0,9 % (DK) av ordervärdet i P0 (`trafik-konvertering-resultat-2026-10-13.txt`, kolumnen `aterbetalt`), så effekten är liten men riktad nedåt.
- 30 dagar är kort och brusigt per kampanj (§12 anger själv det).
- Täckning: produktnivån täcker bara 76 % (SE) och 56 % (DK) av Googles kostnad (§12). Kampanjnivån (§13) stämmer med totalen.
- Annonshantering och bolagets övriga kostnader ingår inte.

### Vad det innebär per kampanj (illustration, inte prognos)
Bidrag efter annonskostnad = värde × M − kostnad, med Net Profit v1 (SE M 37,0 %, DK M 34,6 %), 30 dagar (`beslut-2026-10-26.md` §13, SEK för SE och DKK för DK). **Förutsätter att plattformens värde är verklig, inkrementell försäljning**, vilket sannolikt överskattar.

| Marknad | Kampanj | Kostnad | Värde | ROAS | Bidrag efter annons | % av värdet |
|---|---|---|---|---|---|---|
| SE | Performance Max (Rude) | 59 998 | 221 249 | 3,69 | +21 776 | 9,8 |
| SE | Search Brand - Mixed | 7 261 | 6 394 | 0,88 | **−4 898** | −76,6 |
| SE | Search Brand Exact | 2 999 | 33 201 | 11,07 | +9 272 | 27,9 |
| SE | Search Non-Brand (Rude) | 1 522 | 7 541 | 4,96 | +1 265 | 16,8 |
| SE | Meta Prospecting | 43 746 | 136 346 | 3,12 | +6 647 | 4,9 |
| SE | Meta Remarketing | 13 637 | 45 501 | 3,34 | +3 180 | 7,0 |
| DK | Performance Max (Rude) | 16 743 | 49 289 | 2,94 | **+331** | 0,7 |
| DK | Search (Finch, juni 2022) | 7 663 | 52 266 | 6,82 | +10 442 | 20,0 |
| DK | Meta Adv+ Sales | 25 281 | 65 585 | 2,59 | **−2 562** | −3,9 |

Med DK-bidraget 41,2 % (M 33,0 %) blir DK Performance Max −497 och Meta DK −3 664. Läsning: SE Performance Max och Meta SE ligger över break-even på de här antagandena; **DK Performance Max ligger på noll och Meta DK under**; Search Brand - Mixed SE förlorar pengar i alla antaganden (ROAS 0,88 ligger under varje break-even i tabellen ovan).

---

## 2. Hypotesen: Performance Max DK är begränsad av ett för högt ROAS-mål

**Hypotes (H1):** kampanjens mål-ROAS 5 ligger så långt över det kampanjen faktiskt uppnår (2,94) att Google bara byter in en bråkdel av auktionerna, och det är därför visningarna föll cirka 80 %. Ett lägre mål skulle då öka volymen.

### Underlag som stöder H1
| # | Uppgift | Källa |
|---|---|---|
| S1 | Mål-ROAS 5, dagsbudget 2 500 (DKK), status LIMITED, budgivning "maximera konverteringsvärde" (synk 2026-10-14). Faktisk ROAS 2,94 (30 dagar) | `annonser-resultat-2026-10-14.txt` avsnitt 2; `beslut-2026-10-26.md` §13 |
| S2 | Budgeten är inte begränsningen: kostnad 16 743 / 30 dagar ≈ 558 per dag = 22 % av dagsbudgeten (SE: 59 998 / 30 ≈ 2 000 per dag = 15 % av 13 565) | §13 och `annonser-resultat-2026-10-14.txt`; samma slutsats i `beslut-2026-10-14.md` ("cirka 800 DKK mot 2 500") |
| S3 | Google DK per vecka, första till sista veckan (3 aug till 19 okt): kostnad 15 107 → 3 669 (−76 %), visningar 142 306 → 28 490 (−80 %), CTR 1,64 → 3,02 %, kostnad per klick 6,47 → 4,26 | `beslut-2026-10-26.md` §10 (från `annonser_vecka.sql`) |
| S4 | Mönstret "färre visningar, högre CTR, lägre klickpris" passar med att Google väljer färre och bättre auktioner | samma; tolkning (hypotes) |
| S5 | Google Ads DK totalt hade ROAS 5,21 (juli), 5,62 (augusti) när det låg nära målet och normal volym (augusti 58 124 DKK, +12 % mot augusti 2025), men 3,78 (september) och 3,42 (oktober, 17 dagar) med kostnad 42 564 i september | `beslut-2026-10-18-7.md` månadstabellerna (alla Google-kampanjer, inte bara Performance Max) |
| S6 | Performance Max DK: kostnad 43 568 → 24 273 (−44 %), klick 6 314 → 3 774 (−40 %), värde 221 086 → 69 561 (−69 %), ROAS 5,07 → 2,87 (egen uträkning ur siffrorna) | `annonser-resultat-2026-10-14.txt` avsnitt 2 (P0 13 aug–11 sep, P1 12 sep–11 okt) |

### Underlag som talar emot, eller förklarar volymen på annat sätt
| # | Uppgift | Betydelse |
|---|---|---|
| M1 | **ROAS föll samtidigt som volymen föll.** Om ett för högt mål var den enda orsaken skulle Google strypa volymen *så att ROAS närmar sig målet*; här gick ROAS ifrån målet (5,07 → 2,87) | Värdet per klick halverades: Performance Max DK 35,0 → 18,4 DKK per klick (−47 %, egen uträkning ur S6), medan kostnaden per klick var i stort sett lika (6,90 → 6,43). Ett lägre mål reparerar inte ett halverat värde per klick |
| M2 | **Meta DK**, som saknar ROAS-mål som stryper, tappar likadant: konverteringsvärde per klick 16,6 → 6,3 DKK (−62 %); ROAS 7,37 → 2,37 (lägst 1,76); Meta DK kostnad, visningar och klick stabila | `beslut-2026-10-26.md` §10. Pekar på en orsak som drabbar *Danmark* oavsett kanal (konvertering, sortiment, pris, tillgänglighet, spårning), inte bara Googles budgivning |
| M3 | GA4-konvertering DK 1,08 → 0,97 % (−10 %) och sessioner −24 %, Shopify-ordrar DK −31 % (412 → 285) mellan perioderna | `trafik-konvertering-resultat-2026-10-13.txt`. Både färre besök och lägre andel som köper |
| M4 | Storsäljaren *Kombinerad Chinsstång och Dipsställning Vägg* (DK 26 → 1 sålda; −48 035 SEK) är slut i lager och Google slutade visa den (445 → 27 klick; värde 13 953 → 732). Den ensam står för ca **8,7 %** av Performance Max DK:s värdetapp (151 525 DKK; antaget att produktens hela värde ligger i Performance Max) | `omsattning-30d-resultat-2026-10-12.txt` avsnitt 5; `annonser-resultat-2026-10-14.txt` avsnitt 3; `beslut-2026-10-12-2.md` (lager 0 är dagens lager, ingen lagerhistorik). Fler produkter kan vara slut; `storsaljare_tapp.sql` kan visa det |
| M5 | Ordrar märkta "direct" föll mindre än Google-märkta i DK (42 → 37 mot 150 → 96) | `omsattning-30d-resultat-2026-10-12.txt` avsnitt 4. Talar för att annonsvolymen har betydelse (stöder H1 på så vis), men förklarar inte *varför* volymen minskade |
| M6 | **Break-evenpunkten.** ROAS 2,94 ligger vid den rörliga break-evenpunkten (2,89–3,03). Även om ett lägre mål ger mer volym kan vinsten vara oförändrad eller negativ | avsnitt 1 |

### Bedömning
- **Mekanismen är rimlig** (att ett mål långt över utfallet begränsar visningar är så målstyrd budgivning i allmänhet beskrivs fungera; detta är inte verifierat i repots data). **Men den skillnad som hypotesen behöver, att målet är *den* begränsningen, är inte visad.** Den sannolikaste tolkningen enligt filerna är att *andelen besökare som köper sjunkit* (så skrev jag redan i `beslut-2026-10-14.md`) och att målet då förstärker nedgången. Den tolkningen ligger närmast M1–M3.
- H1 är därför **delvis stödd, inte avgjord**. Följden: ett test av ROAS-målet utan att samtidigt förstå *varför värdet per klick föll* riskerar att köpa mer trafik av samma slag.
- **Tidigare förslag, för jämförelse:** `beslut-2026-10-14.md` beslut N föreslog 5 → 4 i DK i två veckor, men rekommenderade att annonsansvarig bedömer först. Utfallet av den frågan finns inte i filerna. Det här förslaget bygger vidare med break-even och ett fast stoppvillkor.

---

## 3. Testförslag (kräver Davids och Rudes ja, nivå C)

> **Märkning:** *Allt i detta avsnitt är ändringar i Gorillas annonskonto (Google Ads) och kräver Davids och Rudes ja, nivå C.* Jag ändrar ingenting; Rude eller David utför och anger själva värdena. Siffrorna är förslag att diskutera.

### Steg 0: diagnostik utan ändring (nivå A, kan göras av David, Rude eller Claude med läsrätt)
1. Rude/Ads-gränssnittet: ändringshistorik för Performance Max DK sedan juli (har mål-ROAS, budget, tillgångsgrupp eller produktflöde ändrats), och för Gorillas kontot i stort (konverteringsåtgärder, värdemoms-inställning).
2. Vilken andel av visningarna som förloras på grund av rank respektive budget (Ads-gränssnittet; finns inte i BigQuery).
3. Kör `sql/analys/storsaljare_tapp.sql` och `annonser_pa_slutsalda.sql` (rättad 2026-10-26): hur många storsäljare och annonserade produkter är slut eller inaktiva? Om ett fåtal produkter i DK förklarar mycket av tappet är målet inte huvudfrågan.
4. Ta reda på om konverteringsvärdet är inklusive eller exklusive moms (en känd order).
5. Bekräfta marginalen: Davids ark/Net Profit version 2 (kräver vikter, `hamta_vikter.py`) eller en av David godkänd siffra för rörlig bidragsmarginal i DK.

**Rekommendation:** gör steg 0 först. Det kostar inget och kan visa att testet inte behövs.

### Själva testet (om steg 0 inte förklarar tappet)
| Del | Förslag | Skäl och osäkerhet |
|---|---|---|
| Vad ändras | Mål-ROAS i kampanjen "RUDE: Performance Max - Denmark - All Products" (DK). **Inget annat**: inga nya tillgångar, ingen annan budgivningsstrategi, ingen produktfeed-ändring | En variabel åt gången. Andra ändringar suddar ut effekten |
| Startvärde | **4,0** (från 5,0, −20 %) | Under planeringsnivån men över den rörliga break-evenpunkten (ca 2,9–3,0), med marginal. Alternativ: 4,5 (försiktigare, liten effekt) eller 3,5 (närmare break-even, större risk). Branschpraxis är att inte ändra mål mer än ca 15–20 % per steg för att inte störa inlärningen; det är **inte verifierat här**, Rude bedömer |
| Spärr för budget | Sänk dagsbudgeten från 2 500 till **1 000 DKK** under testet | 1 000 är ca 1,8 × dagens genomsnitt (558 per dag). Största möjliga kostnad över 21 dagar blir ca 21 000 DKK, merkostnad mot dagens nivå ca **9 300 DKK** (skattning; Google kan enstaka dagar spendera upp till dubbla dagsbudgeten men ska hålla sig inom budget över månaden). Budgetändringen är en andra ändring men är ett skyddstak som bara slår till om kampanjen reagerar kraftigt |
| Om budgeten blir bindande | Om kostnaden når ≥ 90 % av dagsbudgeten på 3 dagar: stanna, utvärdera, höj inte automatiskt | Då har kampanjen reagerat starkt och beslutet om nästa steg är ett nytt ja |
| Stoppregler (förslag; David och Rude sätter gränserna) | (1) Efter **7 dagar** med minst 3 000 DKK testkostnad: om plattformens ROAS för testdagarna är **under 2,5** → återställ målet till 5,0. (2) Total testkostnad når **15 000 DKK** → stoppa och utvärdera. (3) Någon av de två andra DK-kanalerna (Search, Meta) eller sortimentet ändras väsentligt under testet (kampanj, pris, slutsåld storsäljare) → avbryt eller förläng och notera det | 2,5 är ca 15 % under dagens 2,94 och under break-even 2,9, med utrymme för att Googles konverteringar kommer i efterhand (dag-7-siffran är lägre än slutsiffran). Det är en tolerans, inte en vinstgräns |
| Mätfönster | **Baslinje:** 28 dagar före ändringen. **Inlärning:** dag 1–7 efter ändringen, räknas inte. **Mätperiod:** dag 8–28 (21 dagar). **Slutläsning:** dag 35, så att sena konverteringar (Googles konverteringsfördröjning, jfr `tillvaxtdata.md`) hunnit komma | Utfallsfönster för annonser är 14–28 dagar enligt `standardtester.md`; jag föreslår längre eftersom Performance Max är trögt och DK har få ordrar |
| Kontroll | **Performance Max SE** (mål 4,55, oförändrat) som kontroll för marknadsövergripande skiften (säsong, sajt, tracking) | SE och DK delar sajt men inte alla orsaker (M2). Differens-i-differens: ändringen i DK minus ändringen i SE |
| Mått, annonsplattform | Kostnad, visningar, klick, CTR, kostnad per klick, konverteringar, konverteringsvärde, ROAS, andel förlorade visningar på grund av rank | Per vecka, för testkampanjen |
| Mått, butik (facit) | DK-ordrar och omsättning totalt (Shopify), varav Google-märkta (kanal i `omsattning_30d.sql`); GA4-sessioner och konvertering DK; **MER** = DK-omsättning / (Google- + Metakostnad DK) | `pengalage_veckovis.sql` ger veckoserierna; annonsplattformens värde ensamt räcker inte (avsnitt 1) |
| Primärt utfallsmått | **Marginalbidrag** = (DK-omsättning × M) − (Google + Meta kostnad), jämfört med baslinjen, med M från avsnitt 1 som intervall (33–35 %) | Visar om extra volym är lönsam. Annonsplattformens ROAS visar det inte |
| Marginellt ROAS | (Δ värde) / (Δ kostnad) mot baslinjen, plattform och butik | Brusigt; se nedan |

**Vad en extra annonskrona är värd (skattning, M 34,6 % och 33,0 %):** bidrag per 1 000 DKK merkostnad = 1 000 × (marginellt ROAS × M − 1).

| Marginellt ROAS | M 34,6 % | M 33,0 % |
|---|---|---|
| 2,0 | −307 | −341 |
| 2,5 | −134 | −176 |
| 2,94 | +19 | −31 |
| 3,5 | +213 | +154 |
| 4,0 | +386 | +318 |
| 5,0 | +733 | +648 |

Det är marginellt ROAS som avgör, inte genomsnittet, och marginellt ROAS är nästan alltid lägre än genomsnittet. Detta är en uträkning på antagandena i avsnitt 1, inte ett löfte om utfall.

**Statistisk styrka (grov):** DK hade 285 ordrar på 30 dagar (12 sep–11 okt, `trafik-konvertering-resultat-2026-10-13.txt`), alltså ca 200 på 21 dagar. Slumpspridningen (Poisson) är ca ±7 % (en standardavvikelse), och veckovariationen är större (58–118 ordrar per vecka). **En skillnad på under ca 15–20 % i DK-ordrar går inte att skilja från slumpen** på ett 21-dagars fönster. Testet kan därför bara avgöra stora effekter, och annonsplattformens egna siffror (klick, visningar, kostnad) är känsligare än butikens ordrar.

### Vem gör vad
- **Rude:** ändrar mål och budget, rapporterar ändringshistoriken (steg 0), sätter konverteringsvärde-inställning.
- **David:** beslutar (Gorillas ja, nivå C), bekräftar marginalen, godkänner stoppreglerna.
- **Claude:** löpande uppföljning med läsfrågor (inget skrivs i Ads), veckosammanställning, stoppsignal enligt reglerna.

---

## 4. Vad som skulle falsifiera hypotesen

H1 (målet är den begränsande faktorn och ett lägre mål är lönsamt) **förkastas** om någon av följande gäller. Gränserna är förslag och ska fastställas före testet:

1. **Volymen svarar inte.** Efter mål 4,0 ökar inte kostnaden eller visningarna med minst ca 30 % jämfört med baslinjens sista 14 dagar (på nivå med den spridning som ses i veckodata). Då är målet inte den bindande begränsningen; det finns en annan orsak (konvertering, sortiment, flöde).
2. **Volymen svarar, men inte lönsamt.** Marginellt ROAS (Δ värde / Δ kostnad) understiger break-even för vald marginal (ca 2,9–3,0, eller 3,6–4,8 om endast 80–60 % av värdet är inkrementellt, avsnitt 1). Då fungerar mekanismen men affären gör det inte.
3. **Plattformen och butiken säger emot varandra.** Annonsplattformens värde ökar men DK-omsättningen (särskilt Google-märkta ordrar och MER) ökar inte i motsvarande mån jämfört med kontrollen (SE). Då är den extra "försäljningen" sannolikt tillskrivning av köp som skulle ha skett ändå.
4. **Orsaken visar sig ligga utanför kampanjen** (steg 0): t.ex. att ett fåtal storsäljare är slut (M4), att konverteringsåtgärden eller värdet ändrats, eller att en ändring i augusti/september ändrade kampanjens förutsättningar.

H1 **stärks** om volymen ökar tydligt, marginellt ROAS ligger över break-even och butiken följer med. Även då är det ett resultat för *en marknad under tre veckor* och ska inte generaliseras till SE utan eget test.

---

## 5. Vad som inte är känt

- **Verklig marginal.** Vilket av 54 %, 46/43 % eller 41 % (eller något annat) som gäller. Vad `unit_cost` i Shopify är (leverantörspris, internpris, inklusive frakt?) är fortfarande obesvarat (§15, §17). Net Profit version 2 (vikter) är inte körd. DK-bidragets 43,3 mot 41,2 % är oförklarat.
- **Moms i plattformens värde** (inklusive eller exklusive).
- **Vilken kostnadsdel som är fast.** Om personal (SE 10 %, DK 8 %) och övrigt (5 %) är fasta eller rörliga avgör om break-even är ca 2,9 eller ca 4,1.
- **Inkrementalitet.** Hur stor del av Googles och Metas värde som är verklig merförsäljning. Ingen holdout- eller geotest finns.
- **Ändringshistoriken.** Om mål-ROAS, budget, tillgångsgrupper, konverteringsåtgärder eller produktflöde ändrats sedan juli ("Ändringshistorik finns inte i datan", `annonser-resultat-2026-10-14.txt`). Ingen av filerna redovisar att Rude svarat på frågan i beslut N i `beslut-2026-10-14.md`.
- **Andel förlorade visningar** på grund av rank eller budget, och auktionsinsikter (konkurrens). Finns bara i Ads-gränssnittet.
- **Lagerhistorik.** Dagens lager är en ögonblicksbild (`omsattning_tapp_per_produkt.sql`). När produkter tog slut och hur länge vet vi inte.
- **Vad som hände i DK i slutet av augusti och början av september** (tema, pris, frakt, appar, kassa, kampanjer, produktflöde): fråga (1) i `beslut-2026-10-26.md` §10 är obesvarad. GTM-containern laddas två gånger (§22), men påverkan på mätningen är inte verifierad.
- **Hur Rude räknar COS** (28,44 %, §11–12). Om målen 22 % och 5 faktiskt bygger på planens marknadsföringsandel är en hypotes (§16–17).
- **Hur stor del av tappet som är säsong.** Fjolårsdata för ordrar saknas (GA4 börjar mars 2026; Shopify-ordrar 60 dagar). Shopifys egen analys säger att totalförsäljningen i perioden var 2,8 % lägre än i fjol (`beslut-2026-10-14.md`; Davids rapport, ej kontrollerad), vilket talar för att nedgången mot förra månaden delvis är säsongsmässig.

## Källor (fil, datum, avsnitt)
`beslut-2026-10-26.md` §7, §9–§18, §22 (2026-10-26) · `trafik-konvertering-resultat-2026-10-13.txt` (körd 2026-10-13, P1 2026-09-12–10-11, P0 2026-08-13–09-11) · `omsattning-30d-resultat-2026-10-12.txt` (2026-10-12) · `annonser-resultat-2026-10-14.txt` (2026-10-14; Cockpit X; synk 2026-10-14 03:00) · `beslut-2026-10-14.md` (2026-10-14) · `beslut-2026-10-18-7.md` (2026-10-18) · `beslut-2026-10-12-2.md` (2026-10-12) · SQL: `cos_30d.sql`, `marginal_30d.sql`, `marginal_stickprov.sql`, `net_profit_ordrar.sql`, `annonser_kampanjer_30d.sql`, `annonser_vecka.sql`.

## Uppdatering 2026-10-28: marginal per variant ur arket (körd av David)

Källa: `sql/analys/marginal_per_variant.sql`, orderrader senaste 90 dagarna (orderdata sedan 2026-08-10), täckning 96,4 % (SE) och 95,3 % (DK) av nettointäkten. Tillägg; avsnitten ovan är orörda, och där de bygger på en äldre marginal gäller siffrorna här.

| | SE | DK |
|---|---|---|
| GM1 (före frakt och avgifter), arket | 67,8 % | 76,5 % |
| GM2 (efter fraktkostnad och betalavgift, utan fraktintäkt), arket | 42,9 % | 58,4 % |
| GM1 med Shopifys `unit_cost` | 67,2 % | 75,9 % |

**Break-even ROAS** (1 / marginal; "inkl. moms" är × 1,25 och gäller om plattformens värde inkluderar moms, vilket inte är verifierat):

| Marginalmått | SE exkl. moms | SE inkl. moms | DK exkl. moms | DK inkl. moms |
|---|---|---|---|---|
| GM1 | 1,47 | 1,84 | 1,31 | 1,63 |
| GM2 | 2,33 | 2,91 | 1,71 | 2,14 |
| GM2 minus personal och övrigt enligt arket (15 % SE, 13 % DK) | 3,58 | 4,48 | 2,20 | 2,75 |

- GM2 är en nedre gräns: fraktkostnaden är med, men fraktintäkten från kunder under fraktgränsen är inte med. Fraktintäkten gör att verkligt GM2 ligger högre.
- Siffrorna är utan returer, reklamationer och tullar. Arkets inköpspris är inte verifierat mot fakturor.
- Slutsatser som följer av datan (inte hypoteser): DK har cirka 15 procentenheter högre GM2 än SE; DK:s break-even ROAS är därmed klart lägre (cirka 2,1–2,8 inkl. moms mot cirka 2,9–4,5 för SE). Mot PMax DK:s mål-ROAS 5 och uppmätta 2,94 stärker det hypotesen i avsnitt (b) att målet är för högt, men det visar inte att en sänkning ger lönsam volym.
- Aggregatet stämmer mellan arket och Shopifys `unit_cost` (inom 1 procentenhet), men enskilda SKU avviker kraftigt åt båda håll: AirBike MAXXUS Pro SE 41,8 % (arket) mot 85,1 % (Shopify), Viktskivor PRO 31 mm 47–52 % mot 67–72 %, Skivstångspaket MOVIT 30 kg 71,3 % mot 36,5 %. Använd arket för beslut per produkt.
- Fynd 3 i körningen (negativ GM2 på Gummiband, Viktskivor, Miniband) ska inte tolkas som förlust: arkets fraktkostnad är per SKU som skickas separat, och småprodukter går normalt i samma paket eller ger kunden fraktavgiften. Den listan behöver fraktintäkt per order för att läsas.
- Tidigare redovisad bruttomarginal (72,9 % DK, 74,3 % SE, `marginal_30d.sql`) avser en annan period och inköpskälla; skillnaden mot dagens SE-siffra (67,8 %) är inte avstämd.

## Uppdatering 2026-10-28 (2): med fraktintäkt, GM3

Källa: `sql/analys/marginal_per_variant.sql` (version med `total_shipping` fördelad på orderrader efter varuvärde), 90 dagar, täckning 96,4 % SE och 95,3 % DK. Tillägg; ändrar inte avsnitten ovan.

| | SE | DK |
|---|---|---|
| GM2 (efter fraktkostnad och betalavgift) | 42,9 % | 58,4 % |
| GM3 (GM2 plus betald frakt exkl. moms) | 44,8 % | 60,8 % |
| Fraktintäkt som andel av varuvärdet | 1,9 % | 2,3 % |

- Fraktintäkten är liten (cirka 2 % av varuvärdet) och ändrar marginalen med 2 procentenheter. De stora säljarna har samma GM2 och GM3, eftersom de i stort sett skickas utan fraktavgift.
- **GM3 är en nedre gräns och GM1 en övre gräns.** Arkets `shipping_eur` är per enhet, så en order med flera enheter räknas med full frakt per enhet. Verkligheten ligger däremellan: SE 44,8–67,8 %, DK 60,8–76,5 %.
- Break-even ROAS med GM3 (exkl. moms / inkl. moms): SE 2,23 / 2,79, DK 1,65 / 2,06. Efter personal och övrigt (15 % SE, 13 % DK): SE 3,36 / 4,19, DK 2,09 / 2,61. Övre gräns (GM1, inkl. moms): SE 1,84, DK 1,63.
- Listan över varianter med negativ marginal (Viktskivor, Gummiband, Miniband) kvarstår efter fraktintäkten men ska inte tolkas som förlust. Orsak: arket räknar 13 EUR frakt per enhet, och fördelningen av fraktintäkt efter värde ger de billiga varorna nästan ingen intäkt. Sådana varor skickas i regel tillsammans med andra. För att läsa dem behövs fraktkostnad per order (vikt och paket), se `net_profit_ordrar.sql`.
- Vad som är bevisat: marginalen före frakt (GM1) per variant och de stora säljarnas GM3 på 41–70 %. Vad som är osäkert: arkets inköpspris (inte verifierat mot fakturor) och fraktkostnaden per order.
