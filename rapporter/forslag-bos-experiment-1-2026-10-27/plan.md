# Experiment 1 på Best of Sports: SEO-titel och metabeskrivning på produkter (förslag, 2026-10-27)

Ström 2 (Innehåll och sök). Bara förslag. Ingenting är skrivet till Shopify. Alla siffror ur butiken är lästa 2026-10-27 om inte annat anges. Texterna i `utkast_fore_efter.json` är inte granskade av granskaren och är inte godkända av David.

## Sammanfattning
- **Förslag:** pröva om nya SEO-titlar och metabeskrivningar på produkter ger fler klick från Google. Kategori: **Konditionsträning & Fitness** (671 aktiva produkter i butiken i dag, 0 av dem hade SEO-fält före pilotens 10). Efter uteslutning av kosttillskott, hälsoord, produkter utan lager och produkter med för lite data återstår **442** produkter. De bildar **216 matchade par**: **216 i behandlingsgrupp (T)** och **216 i kontrollgrupp (K)**, valda med fast slumpfrö 20261027.
- **Klart att granska:** 39 färdiga före/efter-texter (T), 2 batchdokument för skrivning (20 + 19 produkter) och en kanariebatch (1 produkt), motsvarande återställningsbatchar, sparade original för alla 432 produkter, och en SQL-fil för baslinjen. Resterande 177 texter i T skrivs med en fast mall (se "Utkast och mall") och granskas på samma sätt.
- **Fynd som påverkar designen (code-läst, inte kontrollerat i live-HTML):** temat lägger själv till ` – BEST OF SPORTS` efter sidtiteln om titeln inte innehåller exakt `BEST OF SPORTS` (skiftlägeskänslig jämförelse). Därför föreslår jag att `seo.title` skrivs **utan** ` | Best of Sports` och är högst 43 tecken, så att den renderade titeln blir högst 60. Pilotens 20 titlar slutar på ` | Best of Sports` och får sannolikt varumärket två gånger (hypotes, se Öppna frågor).
- **Det största problemet:** med de volymer vi har går bara mycket stora effekter att upptäcka (ungefär en 2,5-faldig ökning i klick). Effekter på 10–30 % går inte att avgöra med 216 produkter per grupp på 56 dagar. Experimentet ger därför mest lärdom om *skada* och om *stora* effekter; det ska inte förväntas visa små vinster. Siffrorna bygger på en sammanfattning från 2026-10-23, inte på en körd fråga, och ska ersättas av `baseline.sql` innan start.
- **Vad som kräver Davids ja:** se "Risker och återställning". Kort: planen är inom labbramen (reversibel textändring, 216 ≤ 300, svenska grundspråket), men jag rekommenderar ett uttryckligt ja på titelformen, kanariekörningen och att de 177 återstående texterna granskas före skrivning.

## Täckning
**Läst (filer):** `CLAUDE.md`, `LARDOMAR.md`, `arbetsstrommar.md` (hela, inklusive tillägget 2026-10-27 om riskprofil), `standardtester.md` (rutinen för ändringar i Shopify och T30–T40), `rapporter/tackningskarta-2026-10-26.md`, `bos-tema-genomgang-2026-10-26.md`, `shopify-andringar-bestofsports-2026-10-23.md`, `kategoritexter-utkast-2026-10-20.md`, `titlar-lag-ctr.csv` (Gorilla-sidor, används bara som stilreferens), `bestofsports-produkttexter-2026-10-25.md`, `bestofsports-analys-2026-10-23.md` (volymer), pilotfilerna `bestofsports-pilot-20-produkter-2026-10-25.csv` och `shopify-original-2026-10-25/pilot-20-original.json`, `sql/audit/views_sources_bestofsports.sql`, `sql/analys/bos/12_produkter_prioritet_texter.sql` och `scripts/kontrollera_datakallor.sh`.
**Filnamnet i uppdraget** `bestofsports-produkter-titlar-beskrivningar-2026-10-25.csv` finns inte; filen heter `bos-produkter-titlar-beskrivningar-2026-10-25.csv` (3 250 rader, ögonblicksbild 2026-10-25). Jag har använt den.

**Hämtat ur butiken (bara läsande anrop, Best of Sports bekräftad med `get-shop-info`: domän bestofsports.se, SEK):**
1. `productsCount` för status (aktiva 3 547, utkast 1 608, arkiverade 160, totalt 5 315), produkttyper (8 st) och tillverkare (5 st). Ett anrop.
2. **Alla 671 aktiva produkter i typen Konditionsträning & Fitness**, 14 sidor om högst 50: id, lägsta variantpris, `seo.title`, `seo.description`. Allt är läst; id och pris är inskrivna i `verktyg/indata_live_pris_seo_2026-10-27.txt` för hand (671 rader, kontrollerat att alla 671 id:n är unika).
3. Titel, handle, tillverkare, status, `descriptionHtml`, varianter och SEO för **65 produkter** (de 39 utkasten och 26 som föll bort när jag skärpte uteslutningen), i tre anrop.
4. Status och typ för 32 produkter som fanns i ögonblicksbilden men inte längre är aktiva (alla `DRAFT`).
5. SEO-fälten för **100 av 285** aktiva produkter med tillverkare "Gorilla Sports Norden" (två sidor, sorterade på id), för inventeringen av befintliga SEO-fält.
6. Filen `snippets/doc-head-core.liquid` i det publicerade temat (id 195516039434, roll MAIN), läst i sin helhet.
7. Schemat för `productUpdate`, `ProductUpdateInput` (fältet `seo`, fältet `id`) och `SEOInput`.

**Inte gjort:**
- Ingen skrivning av något slag. Inga `graphql_mutation`, `update-product` m.fl.
- **Ingen åtkomst till BigQuery eller Search Console** (jag kan inte köra `bq`). `baseline.sql` är därför skriven men *inte körd*. Tabellen `gorilla-sports-data.site_audit.gsc_combined_bestofsports_se` är en vy (definierad i `views_sources_bestofsports.sql`) och **obekräftad**: den måste verifieras med `scripts/kontrollera_datakallor.sh` (raden "Search Console se") innan baslinjen tas. Alla trafikuppskattningar nedan bygger på en sammanfattning i `bestofsports-analys-2026-10-23.md`, inte på körd data.
- Jag har inte läst alla 3 547 aktiva produkters SEO-fält live. Inventeringen av fält utanför Konditionsträning bygger på ögonblicksbilden 2026-10-25 (3 250 produkter), kompletterad med live-antal.
- Lagret är inte omläst live; uteslutningen "lager ≤ 0" bygger på lagret 2026-10-25.
- Beskrivningstexter för produkter som inte är utkast har inte lästs, så hälsopåståenden i *beskrivningar* är bara sållade på titel och handle (se Kohortdesign).
- Jag kunde inte hämta live-HTML från bestofsports.se (nätverksspärren gav 403) och har inte försökt kringgå den. Hur titeln faktiskt renderas är därför läst ur temakoden, inte sett.
- Översättningar (da, fi) är inte lästa eller berörda. Ahrefs är inte använt. Inga andra kategorier än Konditionsträning har fått samma genomgång som kandidatlistan nedan visar.
- Texterna är inte körda genom T31 (AI-stilkontrollen finns inte byggd); jag har kört en egen kontroll (se Utkast och mall).

**Rättelser till tidigare uppgifter (läggs här, inget gammalt dokument ändrat):**
- `bestofsports-produkttexter-2026-10-25.md` säger "100 % saknar SEO-titel och 92 % saknar metabeskrivning". Ögonblicksbilden visar 15 SEO-titlar och 274 metabeskrivningar på 3 250 produkter, nästan alla på tillverkaren "Gorilla Sports Norden" (285 aktiva produkter, 265 av dem med metabeskrivning). Utanför den tillverkaren och pilotens 20 produkter är SEO-fälten tomma.
- Antalet aktiva produkter är inte stabilt: 3 250 den 25 oktober, 3 547 den 27 oktober. Se Risker.

## Inventering
**Aktiva produkter just nu (live, 2026-10-27): 3 547.** Utkast 1 608, arkiverade 160.

| Produkttyp (live, aktiva) | Antal | SEO-titel satt (ögonblicksbild 25/10) | Metabeskrivning satt (ögonblicksbild 25/10) | Lager > 0 (25/10) |
|---|---|---|---|---|
| Cyklar | 748 | 0 av 585 | 0 av 585 | 298 av 585 |
| Konditionsträning & Fitness | 671 | 0 av 638 (10 satta live efter pilot) | 0 av 638 (10 live) | 570 av 638 |
| Tillbehör | 552 | 3 av 536 | 57 av 536 | 494 av 536 |
| Damcyklar | 158 | 0 av 121 | 0 av 121 | 58 av 121 |
| Professionell utrustning | 111 | 0 av 117 | 0 av 117 | 38 av 117 |
| Kosttillskott | 92 | 0 av 91 | 0 av 91 | 91 av 91 |
| Sparkcyklar | 91 | 0 av 75 | 0 av 75 | 75 av 75 |
| Cykeldelar | 73 | 0 av 68 | 0 av 68 | 68 av 68 |

Typen är tom för 373 produkter i ögonblicksbilden. Antalen är live; SEO-andelarna är från ögonblicksbilden eftersom jag inte skannade alla typer live.

| Tillverkare (live, aktiva) | Antal | SEO satt (ögonblicksbild 25/10, titel / beskrivning) |
|---|---|---|
| Giant | 446 | 0 / 0 |
| Tunturi | 415 | 0 / 0 |
| Gorilla Sports Norden | 285 | 15 / 265 |
| Toorx | 141 | 0 / 0 |
| Hammer | 115 | 0 / 0 |

**Befintliga SEO-fält, kvalitet (de 100 första av 285 "Gorilla Sports Norden", sorterade på id; resten är inte mätt):**
- 6 av 100 saknar båda fälten, 7 har SEO-titel, 94 har metabeskrivning.
- Längd på metabeskrivningarna (94 st): median 136,5, minst 28, störst 160 tecken. 7 under 70 tecken, 19 på 70–119, 62 på 120–155, 6 över 155.
- SEO-titlarna (7 st) är 47, 64, 57, 68, 59, 55 och 55 tecken: 3 av 7 över 60. Två slutar på ` | Best of Sports`, två innehåller marknadsföringsord ("Kundfavorit", "Tillbaka i lager!").
- **Exakta dubbletter: 0.** Nästan-dubbletter: fyra grupper börjar med samma 30 tecken (tre Movit-mattor, två massagestolar, två viktpaket, två curlstångspaket).
- 36 av 94 har inledande eller avslutande blanksteg, 1 innehåller `&nbsp;`, 1 en kvarglömd `&`. Flertalet är leverantörens produktbeskrivning avkortad, och 8 av 94 innehåller ord som "rehab", "rehabilitering", "spänningar" eller "avslappning" (möjliga hälsopåståenden, ej bedömda).
- Dubblettproblem på titelnivå utanför SEO-fälten: 118 produkter delar produkttitel med en annan produkt (enligt `bestofsports-produkttexter-2026-10-25.md`). Det slår igenom i mallen, se "Utkast och mall".

## Val av kategori
**Valt: Konditionsträning & Fitness (produkttyp).** Kravet var två lika stora grupper om minst 100, inte kosttillskott, med svaga eller saknade SEO-fält.

| Kandidat | Aktiva live | I ögonblicksbilden: saknar båda SEO-fält | Kvar efter enkla filter¹ | Kommentar |
|---|---|---|---|---|
| **Konditionsträning & Fitness** | 671 | 638 av 638 | 529 | Valt. 570 av 638 har lager. Få språkproblem (14 engelska beskrivningar). Tydlig specifikationsdata (mått, effekt, maxvikt) som gör faktabaserade texter möjliga. Samma produktfamilj som de kategorisidor (motionscykel, träningsbänk, roddmaskin) som hade flest visningar i 90-dagarsanalysen. |
| Cyklar | 748 | 585 av 585 | 296 | Bara 298 av 585 hade lager; 39 med engelsk text. Annonspengar läcker här (barncyklar, 54 % av kostnaden). En kategori där lagerläget kan förändra utfallet mer än texten. |
| Tillbehör | 552 | 479 av 536 | 379 | Blandkategori (Giant 114, Gorilla Sports Norden 59, AXA 55): svårt att matcha. |
| Professionell utrustning, Damcyklar, Sparkcyklar | 111 / 158 / 91 | alla | 37 / 58 / 70 | För små för 2 × 100. |
| Kosttillskott | 92 | alla | – | Utesluts (nivå C, hälsopåståenden). |

¹ Lager > 0 (25/10), svensk eller engelsk beskrivning, minst 15 ord, inga SEO-fält satta.

**Totalt i kategorin:** 671 aktiva produkter live. **Av dem i ögonblicksbilden 25/10:** 606 (65 har tillkommit som aktiva sedan dess och 32 har gått tillbaka till utkast). Se tratten under Kohortdesign.

**Vad valet inte bygger på:** jag har inte trafik per kategori (ingen BigQuery-åtkomst). Att kategorin är den med flest visningar är en hypotes som kommer från att dess kategorisidor nämns i analysen från 2026-10-23, inte en mätning av produktsidorna. `baseline.sql` svarar på det före start.

## Kohortdesign
**Population (steg för steg, 671 live):**

| Steg | Antal |
|---|---|
| Aktiva i typen live | 671 |
| Samma produkter i ögonblicksbilden 25/10 (för titel, tillverkare, lager, textlängd) | 606 |
| Borta: 65 nya sedan 25/10 (saknar historik, ostabila) | – |
| Uteslutna: 66 utan lager (25/10), 37 med hälsoord¹ i titel/handle, 33 med under 15 ord beskrivning, 18+13 med kort eller osäker språkklassning, 14 Trec (kosttillskott), 10 pilotprodukter med SEO redan satt, 1 med pris 0 | 164 unika (flera orsaker överlappar) |
| **Pool** | **442** |

¹ Ord i regexen (titel och handle): protein, vitamin, kreatin, aminosyra, bcaa, koffein, energi, fettförbränning, tillskott, pre-workout, massage, vibration, våg, hälsa, bränn, viktminsk, detox, rehab, reha, smärta, sjukgymn, collagen, elektrolyt, akupunktur, akupressur, terapi, inversion, smartvåg, body screen, samt estniska titelord (jõu, treening, ujumis). Det är en yta: beskrivningstexterna är inte genomsökta.

**Matchning:** pooler delas i par. Kriterier i prioritetsordning: (1) undertyp (nyckelord i titeln: löpband, cykel, rodd, bänk, viktskivor, hantlar, kettlebell, stång, matta, boll, handskar, rack, band, hopprep, övrigt), tillverkare och prisband; (2) undertyp och prisband; (3) tillverkare och prisband. Prisband: <200, 200–499, 500–1 499, 1 500–4 999, 5 000–14 999, ≥15 000 kr. Inom varje stratum slumpas ordningen med `random.Random("20261027|nivå|stratum")` och produkterna parar ihop två och två; ett slumptal avgör vilken i paret som blir T. Ojämnt antal i ett stratum skickas ner till nästa nivå.
- **Slumpfrö: 20261027.** Koden är `verktyg/kohortval.py`; samma indata ger samma kohorter.
- Resultat: **170 par på nivå 1, 33 på nivå 2, 13 på nivå 3 = 216 par.** 10 produkter fick ingen partner och är utanför experimentet.

**Balans mellan T och K (216 vardera):**

| Mått | T | K |
|---|---|---|
| Prisband <200 / 200–499 / 500–1 499 / 1 500–4 999 / 5 000–14 999 / ≥15 000 | 30 / 43 / 21 / 56 / 49 / 17 | 30 / 43 / 21 / 56 / 49 / 17 |
| Medelpris, median (kr) | 4 652 / 1 884 | 4 603 / 1 864 |
| Tillverkare: Tunturi / Toorx / Hammer / Christopeit / BH Fitness / Finnlo by Hammer / övriga | 108 / 45 / 29 / 14 / 11 / 7 / 2 | 105 / 44 / 29 / 14 / 15 / 3 / 6 |
| Undertyp, största skillnader | band 7, kettlebell 11, stång 11 | band 5, kettlebell 14, stång 9 |
| Median antal ord i beskrivningen (25/10) | 86,5 | 83 |

Prisbanden är identiska eftersom alla nivåer parar inom prisband. Tillverkare och undertyp skiljer några enheter (störst: BH Fitness 11 mot 15, Finnlo by Hammer 7 mot 3). Det är inom vad ett slumpurval ger, men det är **inte kontrollerat mot trafik**. **Kontroll före start:** `baseline.sql` (del 3) visar visningar och klick per grupp de senaste 28 dagarna. Om T och K skiljer mer än 25 % i visningar ska paren dras om med trafik som extra stratum (tre nivåer av visningar) *innan* något skrivs. Det går inte att göra nu eftersom jag saknar trafikdata.

Alla 432 produkter är med i `kohorter.csv` (kolumnerna ber om: produkt-id, handle, URL på .se, tillverkare, typ, pris, kohort, nuvarande `seo.title` och `seo.description`; jag har lagt till prisband, undertyp, par-nr och matchningsnivå). Nuvarande SEO-fält är tomma (butiken svarade `null`) för alla 432.

## Utkast och mall
**Underlag:** `utkast_fore_efter.json` har **39** produkter i T (alla bekräftade i T, handle jämförd mot ögonblicksbilden, `seo` = null före). Fält: `id`, `handle`, `seo_title_fore`, `seo_title_efter`, `seo_description_fore`, `seo_description_efter`, `motivering`, `källfakta`, samt `kohort` och längderna. Utkasten spänner över 15 undertyper (löpband 4, cykel 4, bänk 4, övrigt 6, m.fl.).

**Regler som alla texter följer (och som är kontrollerade med kod i `verktyg/bygg.py`, byggfel stoppar filen):**
- `seo.title`: produktens sökbara namn först (typ på svenska + tillverkare + modell, högst ett nyckelmått), **högst 43 tecken, utan avslutande varumärke.** Renderad titel = `seo.title` + ` – BEST OF SPORTS` som temat lägger till, alltså högst 60 tecken. Faktiskt resultat: 25–43 tecken, 39 av 39 klarar kravet.
- `seo.description`: 130–155 tecken. Faktiskt resultat: 133–155, 39 av 39 klarar kravet. Innehåller inga uppgifter om pris, leverans, garanti, tester eller omdömen.
- Unika: 39 av 39 titlar och 39 av 39 beskrivningar är olika.
- **Fakta:** varje siffra i en text måste stå i `källfakta` (utdrag ur produktens titel och beskrivning) eller i produkttiteln. Kontrollen gav 0 träffar utan källa. Vikt anges aldrig för produkter med flera varianter där vikten inte framgår (Toorx Absolute-kettlebell, Tunturi Platinum Slam Ball, Tunturi Platinum Bumper Plate).
- Förbjudna fraser och tecken (upptäck, perfekt för dig, i dagens snabba, höj din, nästa nivå, oavsett om, toppkvalitet, unik, revolutionerande, utropstecken) och hälsoord (protein, vitamin, rehab, smärta, hälsa m.fl.): 0 träffar.
- **Hälsopåståenden i originaltexterna återanvänds inte.** Exempel: löpbandet T40 ("även lämplig för rehabilitering"), trampolinen ("resultat är garanterade"), mattan HAMMER Puzzlemat Professional ("minskar buller med upp till 80 %"). Orsakerna står i `motivering`.
- Jag har inte lagt fraser i tre led medvetet; uppgiftslistor (till exempel maxvikt, mått, vikt) är separata meningar eller par.

**Rättning av engelska och motstridiga produktdata** (i `motivering`): 5 titlar byter engelska typord ("Treadmill", "Exercise bike") mot de svenska sökorden löpband och motionscykel; beskrivningen till BH i.Hudson kallar den felaktigt "treadmill" och används inte; Hammer Bio Force heter "Power rack" i titeln men beskrivs som multigym, så båda orden används.

**Mall för de övriga 177 i T (generera och granska på samma sätt):**
1. **Hämta** `title`, `vendor`, `descriptionHtml` och varianterna för produkten (läsande). Om produkten har flera varianter med olika pris: skriv aldrig en enskild vikt, storlek eller färg som inte står i produkttiteln.
2. **Titel (högst 43 tecken):** `[Typ på svenska] [Märke i normal skrivning] [Modell][, ett nyckelmått]`. Typ ur nyckelordslistan (Treadmill → Löpband, Exercise bike → Motionscykel, Rowing → Roddmaskin, Weight bench → Viktbänk, Dumbbell → Hantel, Mat → Matta). Märke i normal skrivning (TUNTURI → Tunturi). Om titeln inte ryms: ta bort nyckelmåttet, sedan modifierare. Om två produkter får samma titel: lägg till det som skiljer (färg eller vikt ur produkttiteln) eller markera "manuell".
3. **Metabeskrivning (130–155 tecken):** mening 1: `[Märke Modell] är en/ett [typ] med [de 2 viktigaste egenskaperna]`. Mening 2: `[mått, vikt eller maxvikt som står i datan]`. Egenskaper väljs i den här prioritetsordningen per undertyp (bara de som står i produktdata):
   - löpband: motoreffekt (hk), hastighetsintervall, löpyta, hopfällbar, maxvikt användare
   - motionscykel/spinning: svänghjul (kg), antal nivåer och program, maxvikt användare, mått
   - roddmaskin: motståndstyp, mått, vikt, maxvikt användare
   - bänk: antal lägen för rygg/sits, lastkapacitet, vikt, hopfällbar
   - viktskivor/stänger/hantlar/kettlebells: håldiameter, vikt per styck, antal i set, material, längd
   - mattor: mått, tjocklek, material, antal delar
   - rack och stationer: viktblock, maximalt motstånd, mått, takhöjd
   - tillbehör: vad den passar till (ur beskrivningen), mått, material
4. **Automatisk kontroll** (samma som `bygg.py`): längder; fraslistan; hälsoordslistan; varje siffra i texten finns i produktens titel eller utdragna specifikation; titel och beskrivning är unika inom T; inga uppgifter om pris, leverans, garanti, test eller omdöme.
5. **Manuell läsning** av alla 177 före skrivning (samma granskare som för de 39). En text som faller i kontrollen eller saknar underlag (färre än två fakta) skrivs inte; produkten lämnas orörd och tas bort ur både T och dess K-partner för att behålla balansen (alternativt byts paret).
6. **Skrivs inte av en modell utan granskning:** AI-stilkontrollen T31 är inte byggd, så den manuella läsningen är enda skyddet mot AI-ton.

## Genomförande
Förbereda, inte köra. Alla filer ligger i den här mappen. Ordning för samordnaren, **efter Davids ja**:

0. **Före allt:** kör `scripts/kontrollera_datakallor.sh` (Search Console se, vyn `gsc_combined_bestofsports_se`) och sedan `baseline.sql`. Är källan SAKNAS, TOM eller GAMMAL: avbryt. Är T och K ojämna i visningar (>25 %): dra om paren med trafikstratum (se Kohortdesign). Spara baslinjen som fil.
1. **Granskare** läser de 39 utkasten och mallen mot `källfakta`. Mallen genererar sedan de 177; även de granskas.
2. **Förkontroll (läsning):** `verktyg/forkontroll.graphql` för alla id:n; jämför `seo` mot `shopify-original-2026-10-27/bos-experiment-1-originaler.json`. Skiljer något (nu inte `null`): stoppa, någon annan har ändrat.
3. **Kanariekörning, en produkt:** `utfor_batchar/utfor-00-kanarie.graphql` (Tunturi Mini Resistance Band Set, 5 st). Läs tillbaka; jämför tecken för tecken (`python3 scripts/diff_text.py`) mot `utkast_fore_efter.json`. Kör sedan `aterstall_batchar/aterstall-00-kanarie.graphql` och läs tillbaka: **fälten ska vara `null` igen.** Detta provar återställningen (se Risker); är det inte `null` men tomt eller något annat ändras återställningsbatcharna innan fler körs. Kör `utfor-00-kanarie` igen.
4. **Batcher:** `utfor_batchar/utfor-01.graphql` (20 produkter) och `utfor-02.graphql` (19 produkter), var och en med `userErrors` i svaret. Batcher för de 177 återstående texterna byggs av `verktyg/bygg.py` när deras utkast ligger i `utkast_data.py` (högst 20 alias per dokument). Totalt 216 produkter, under taket 300.
5. **Läs tillbaka alla**, jämför tecken för tecken mot `utkast_fore_efter.json`; rätta och jämför igen tills det stämmer.
6. **Logga** i `ANDRINGSLOGG.md` (samordnaren), `rapporter/shopify-andringar-<datum>.md` (före och efter) och beslutsunderlag.
7. **Testpost (T8):** `site-audit test add` för T-sidorna, mått `gsc_clicks` och `gsc_impressions`, **fönster 56 dagar**, start på skrivdagen, påminnelse. Obekräftat: om `site-audit test add --pages` tar 216 sidor och en separat kontrollista; annars används `baseline.sql` med nya datum som utvärdering (ändra datumen i `DECLARE START/SLUT` överst i filen).
8. **Frys:** inga andra ändringar av titel, beskrivning, pris, status eller SEO på de 432 produkterna under 56 dagar (se Risker).

Filer:
- `utfor_batchar/utfor-00-kanarie.graphql` (1), `utfor-01.graphql` (20), `utfor-02.graphql` (19); `forkontroll-01.graphql` (läsfråga för de första 20).
- `aterstall_batchar/aterstall-00-kanarie.graphql` (1, sätter `null`), `aterstall-01.graphql` (20), `aterstall-02.graphql` (19), alla utan annat än originalen.
- Dokumenten är kontrollerade mot schemat (`productUpdate(product: {id, seo: {title, description}})` finns och `userErrors` ingår i svaret). Valideringsverktyget `validate_graphql_codeblocks` kontrollerar ingenting (det är en tom funktion), så syntaxen är bara läst, inte körd.

## Utvärdering
**Mått (per produkt-URL, Search Console):** klick, visningar, CTR och snittposition. Källa: `gsc_combined_bestofsports_se` (obekräftad). Join på handle ur `/products/<handle>`.
- **Primärt:** CTR (klick / visningar) summerat per grupp, jämfört mot samma grupp de 28 dagarna före (skillnad i skillnad). Sekundärt: klick, visningar och position.
- **Fönster: 56 dagar** (SEO-texter enligt `standardtester.md`: Google omvärderar långsamt). Utvärdera tidigast 4 dagar efter att fönstret slutat (Search Console blir slutgiltig efter cirka 3 dagar), alltså dag 60. Delmätning efter 14 och 28 dagar bara som varningsvakt (skada), inte som resultat.
- **Kontrollgruppens roll:** K är 216 matchade produkter där ingenting ändras. Allt som drabbar båda grupperna lika (säsong inför Black Friday och jul, Googles uppdateringar, temaändringar, prisändringar på hela sortimentet, pausade annonser) tas bort ur jämförelsen. Skillnaden T minus K i förändring är effekten av texterna. Därför är kontrollen viktigare än uppskattade effekter före/efter.
- **Analys:** på parnivå (T-sida minus K-partner), med bootstrap över par (10 000 omdragningar) för ett 95 %-intervall. Summerade CTR-tal är känsliga för enstaka sidor med många visningar, så rapportera både summa och median per par.

**Vad som räknas som lyckat (bestäms nu, före start):** alla fyra villkor:
1. CTR-förändringen i T minus i K är **minst +20 % relativt** och 95 %-intervallet över paren ligger ovanför 0.
2. Totalt minst **150 klick och 3 000 visningar** i fönstret över båda grupperna (annars se nästa punkt).
3. Visningarna i T har inte minskat mer än 10 % relativt K (annars kan CTR-ökningen komma av att dålig trafik försvann).
4. Snittpositionen i T har inte försämrats med mer än 1 plats relativt K.

**Skada (stoppa och återställ):** T har efter 14 eller 28 dagar minst 25 % färre visningar än K *och* intervallet ligger helt under 0, eller att fler än 5 produkter försvinner ur indexet. Då återställs enligt "Risker".

**Vad som är för litet för att avgöra:** om villkor 2 inte uppfylls, eller om intervallet för CTR-skillnaden innehåller både −20 % och +20 % *efter* dag 56. Resultatet noteras då som "inte avgörbart", inte som "ingen effekt". Förläng i så fall till 84 dagar (kostnadsfritt, grupperna ligger kvar) före ett nytt experiment.

**Grov uppskattning av vad som går att upptäcka (hypotes, bygger på sammanfattning och inte på körd fråga):**
- Källa: `bestofsports-analys-2026-10-23.md`, SE, 90 dagar: produktsidor 2 206 sidor med visning, 290 klick, CTR 2,68 %, snittposition 11.
- Härlett: 290 / 0,0268 ≈ **10 800 visningar på 90 dagar** över 2 206 sidor, alltså ≈ 4,9 visningar per sida och 90 dagar, ≈ **3,0 per sida på 56 dagar**.
- Per grupp om 216 produkter: **≈ 660 visningar och ≈ 18 klick på 56 dagar**, om produkterna är som snittet. (Konditionsträning kan vara över eller under snittet; det avgörs av `baseline.sql`.)
- Med ≈ 18 klick per grupp är standardfelet på kvoten T/K ≈ 0,34 på log-skalan. För 80 % styrka och 5 % signifikans kan bara en kvot på ungefär **2,6** (en 2,6-faldig ökning, +160 %) upptäckas.
- Räknat på CTR (baslinje 2,68 %) behövs visningar per grupp för att upptäcka relativ ökning: +10 % ≈ 60 000, +25 % ≈ 10 200, +50 % ≈ 2 800, +100 % ≈ 840, +200 % ≈ 270. Vi har ≈ 660. Alltså kan vi upptäcka en dubblering ungefär, inte mindre.
- **Slutsats:** med 216 produkter per grupp och 56 dagar går det bara att se mycket stora effekter eller tydlig skada. Antagandena är optimistiska (visningar är ojämnt fördelade: ett fåtal sidor står för merparten, vilket gör osäkerheten större).
- **Vad som skulle behövas för att upptäcka +25–50 %:** visningar i storleksordningen 3 000–10 000 per grupp. Alternativ: (a) utvidga till fler kategorier (Cyklar: 296 kandidater, Tillbehör: 379) och köra som ett andra experiment; (b) förlänga fönstret till 84 dagar; (c) välja bara sidor som har visningar i baslinjen (stratifiera på trafik); (d) komplettera med T33-pilotens (20 produkter) utfall. Inget av detta har jag gjort.

**Mått som kan misslyckas:** `baseline.sql` del 5 (antal kohortprodukter helt utan visningar). Om alla 432 saknar visningar är joinen eller URL-formen fel, inte butiken. Samma fråga utan T/K-listan mot en känd sida med trafik rekommenderas före första körningen (till exempel en produkt ur `sql/analys/bos/12_produkter_prioritet_texter.sql`).

## Risker och återställning

| Risk | Hur upptäcks den | Återställning |
|---|---|---|
| **Titeln får varumärket två gånger** (temat lägger till ` – BEST OF SPORTS`, kontrollen `contains shop.name` är skiftlägeskänslig och butikens namn är `BEST OF SPORTS`). Gäller pilotens 20 produkter som slutar på ` | Best of Sports`. | Läs `<title>` i live-HTML på en pilotprodukt (jag kunde inte, nätverksspärr). | Förslaget undviker det genom att skriva `seo.title` utan varumärke. För pilotprodukterna: en separat ändring, inte i det här experimentet. |
| **Googles omskrivning**: Google visar ofta en annan titel och beskrivning än den vi anger. | Jämför SERP-titel och `seo.title` för ett stickprov efter 14 dagar. | Ingen åtgärd (effekten är då svagare, inte skadlig). |
| **Återställningen med `null` fungerar inte som tänkt** (obekräftat om `seo: {title: null}` rensar fältet eller lämnas oförändrat). | Kanariekörningen i steg 3: läs tillbaka efter `aterstall-00`. | Om `null` inte rensar: byt till tomma strängar `""` i återställningsbatcharna och prova igen; sista utväg är att tömma fälten i Shopify admin per produkt. Originalen (alla `null`) ligger i `shopify-original-2026-10-27/`. |
| **Produktsortimentet ändras under experimentet.** Antalet aktiva produkter gick från 3 250 till 3 547 på två dagar och 32 produkter i kategorin blev utkast. | Vecko-kontroll: läs `status` för alla 432 (`forkontroll.graphql`); exkludera ur analysen produkter som varit utkast eller saknat lager i mer än 14 dagar. | Analysen sker på par där båda är aktiva under hela fönstret. |
| **Andra ändringar på T- eller K-produkter** (titel, beskrivning, pris, lager, T33-pilot, temaändringar, annonser) | Läs `updatedAt` för de 432 varje vecka. | Samordnaren stoppar ändringar på dessa produkter; ett par där den ena ändrats utanför experimentet tas bort ur analysen. |
| **Texter som låter som AI eller innehåller fel fakta**, särskilt från leverantörens trasiga data (till exempel "Belastningskapacitet: 11 kg" på en motionscykel eller dubbla uppgifter) | Granskaren läser alla mot `källfakta`; kontrollerna i `bygg.py` fångar siffror utan källa. | `aterstall_batchar/` sätter tillbaka `null` (originalen); kan göras per produkt. |
| **Hälsopåståenden i texterna.** Beskrivningarna sållades inte på hälsoord, bara titlar. | Hälsoordslistan körs över varje text; granskaren läser. | Samma som ovan. Produkter med inneboende hälsonamn (massage, vibration, våg, inversion, kosttillskott) är uteslutna. |
| **Duplicerade titlar och beskrivningar i T** (flera varianter med samma namn) | Unikhetskontroll i `bygg.py` (0 dubbletter bland de 39). | Mallen kräver särskiljare; annars "manuell". |
| **För lite data för att avgöra** (se Utvärdering) | `baseline.sql` före start visar faktiskt antal visningar. | Inget att återställa; byt design (fler kategorier, längre fönster) före skrivning. |
| **Smittoeffekt:** T-sidor kan ta visningar från liknande K-sidor (samma sökord) | Jämför summan T+K med föregående period, inte bara T mot K. | Ingen, men förklarar en skev skillnad. |
| **Dataproblem i poolen:** två produkter har pris 9 kr (10472250933514, 10472251064586) | Granska innan start. | Ta bort ur pool om felaktiga. |

**Vad kräver Davids ja enligt `arbetsstrommar.md`:**
- *Inom labbramen* (ingen ny godkännande per enskild ändring, om alla villkor är uppfyllda): SEO-titel och metabeskrivning på produkter i svenska grundspråket, reversibelt, 216 ≤ 300 objekt, behandlings- och kontrollgrupp, original sparade (klart), skriven text inläst och jämförd, loggning, T8-post med 56 dagars fönster, plan som David har kunnat se (den här).
- *Kräver fortfarande uttryckligt ja:* allt som rör kosttillskott (uteslutet), hälsopåståenden, omdömen och betyg (inga i texterna), pris, lager, status och publicering (rörs inte), rabattkoder, appar, annonser, kunddata, e-post, **tema** (rörs inte).
- **Min rekommendation om ja på tre punkter, trots att ramen räcker:** (1) valet att skriva `seo.title` utan varumärke och högst 43 tecken (avviker från "{Titel} | Best of Sports" i `bestofsports-produkttexter-2026-10-25.md` och pilotens form); (2) kanariekörningen och bytet till `""` om `null` inte återställer; (3) att batcharna för de 177 återstående texterna inte körs förrän granskaren har läst dem.
- Gorilla Sports berörs inte av experimentet.

## Öppna frågor
1. **Titelform:** ska `seo.title` vara utan varumärke (förslaget) eller som pilotens ` | Best of Sports`? Kräver att någon läser `<title>` i live-HTML på en pilotprodukt (jag kommer inte åt bestofsports.se härifrån). Om dubbleringen visar sig stämma bör pilotens 20 titlar också ändras, men det är en egen åtgärd.
2. **Kör `kontrollera_datakallor.sh` och `baseline.sql`:** är `gsc_combined_bestofsports_se` färsk och hur många visningar har kohorterna faktiskt? Utan det är effektuppskattningen en gissning.
3. **Antal par:** vill David hellre ha en bredare design (till exempel Konditionsträning plus Cyklar, 2 × 400+) för att kunna se mindre effekter, eller ett litet "skadeprov" som detta?
4. **Pilotens utfall (T33, 20 produkter, ändrad beskrivning och SEO):** de är uteslutna ur kohorterna; ska deras 56-dagars-fönster (runt 2026-11-22) gå före och lära oss något om titelformen?
5. **Reglerna för K:** ska produkter i K få SEO-text från andra strömmar under experimentet? Förslaget är nej, fryst i 56 dagar.
6. **Hur återställs till `null`:** bekräftas av kanariekörningen. Om tomma strängar fungerar bättre än `null` ska filerna i `aterstall_batchar/` byggas om (en rad i `verktyg/bygg.py`).
7. **Förslag på lärdomspost** (jag får inte skriva i `LARDOMAR.md`): *2026-10-27: Produktuppsättningen i BOS ändras dag för dag (3 250 → 3 547 aktiva på två dagar, 32 produkter gick till utkast). Regel: en ögonblicksbild av produktlistan är bara giltig samma dag; läs om status och lager i butiken före varje kohortdragning och före varje skrivning, och frys de berörda produkterna under experimentet.* Och: *Temat lägger till butiksnamnet efter sidtiteln med en skiftlägeskänslig kontroll; räkna med att renderad titel = `seo.title` + 17 tecken.*

## Filer och återskapande
- `kohorter.csv` (432 rader), `utkast_fore_efter.json` (39), `baseline.sql`, `utfor_batchar/`, `aterstall_batchar/`.
- Original: `/home/user/Shopify/rapporter/shopify-original-2026-10-27/bos-experiment-1-originaler.json` (alla 432, `null`/`null`).
- `verktyg/`: `kohortval.py` (urval, slumpfrö 20261027), `bygg.py` (bygger alla filer och kontrollerar texterna), `utkast_data.py` och `utkast_justeringar.py` (texterna), `indata_live_pris_seo_2026-10-27.txt` (min inskrivning av live-svaret: id, lägsta pris, `S` om SEO redan satt), `indata_gorilla_vendor_seo_100_forsta.tsv`, `forkontroll.graphql`. Kör `python3 verktyg/bygg.py` från den här mappen. Indata om produkter kommer från ögonblicksbilden 2026-10-25 i `rapporter/bos-produkter-titlar-beskrivningar-2026-10-25.csv`.
- **Svaghet i indata:** id och pris är inskrivna för hand ur 14 svar (671 rader). Jag har kontrollerat att alla id:n är unika och att antalet satta SEO-fält (10) stämmer med de 10 svar där fälten var ifyllda, men en felskrivning av enstaka pris kan inte uteslutas; pris används bara för prisband.

## Rättelser och kompletteringar efter granskning och läskontroll (2026-10-27)

Tillägg. Raderna ovan är orörda; där de motsägs gäller detta avsnitt.

**1. DK och FI (granskarens fynd 1, kontrollerat med läsning i Shopify).**
- Butikens språk: sv (grundspråk), da (publicerat), fi (publicerat), en (ej publicerat).
- Läst för två produkter (`translatableResource`, `translations` för da och fi):
  - 10472310931722 (T, SEO null): da och fi har översatt `title`, `body_html` och `product_type`. Fälten `meta_title` och `meta_description` finns inte i det översättningsbara innehållet, eftersom SEO-fälten är null.
  - 10462768038154 (pilotprodukt med SEO satt): svenska `meta_title` och `meta_description` finns, men **da och fi saknar översättning av båda**.
- Slutsats (bevisat om Shopifys data): när vi sätter svensk SEO uppstår ett `meta_title`/`meta_description` att översätta, och ingen översättning finns på da/fi.
- Hypotes (inte sett i live-HTML; jag når inte butikerna härifrån): `.dk` och `.fi` visar då den svenska titeln och beskrivningen i stället för titeln på danska/finska, som de har i dag via produkttiteln. Det vore en försämring mot nuläget och strider mot att `.dk` och `.fi` ska ranka självständigt.
- Konsekvens för planen: **kanariekörningen ska inkludera en kontroll av `<title>` och meta description på `.dk` och `.fi`** för kanarieprodukten. Utfaller hypotesen är experimentet obeslutat till dess en av två vägar är vald: (a) skriva da/fi-översättningar av SEO-fälten i samma batch (kräver översättningstext, ny nivå-B-bedömning), eller (b) avstå från skrivning på produkter som visas på .dk/.fi. Mätningen gäller i båda fallen bara `.se`.
- Samma sak gäller de 10 pilotproduktena som redan har svensk SEO: kontrollera `.dk`/`.fi`-sidorna för dem nu.

**2. Startdatum (fynd 2).** Bara 39 av 216 T-texter finns. Skrivningen får inte starta och 56-dagarsklockan inte börja förrän **alla** T-produkter som ingår är skrivna, annars får produkterna olika startdatum. Om bara 39 skrivs, är experimentet ett 39-mot-39-test och ska beskrivas så (ännu lägre styrka än nedan).

**3. Design och mått (fynd 3).** Rubriken "valid slutsats" får inte användas. Med omkring 36 klick väntade under fönstret går bara en effekt på omkring 2,5 gånger att se. Villkoret +20 % går inte att visa och 150 klick / 3 000 visningar uppnås sannolikt inte; utfallet blir då "inte avgörbart". Skadegränsen (25 % färre visningar) ger falsklarm vid så små tal och används som stoppsignal för samordnaren att titta, inte som bevis. `baseline.sql` avgör före start om experimentet körs alls.

**4. Texter (fynd 4) rättade i `verktyg/utkast_justeringar.py` och filerna byggda om med `verktyg/bygg.py` (alla kontroller passerade, 39 utkast):**
- Hopprep Toorx: "Tillverkat av Toorx i Italien" borttaget (ursprung obekräftat, källan säger "(Italien)").
- Puzzlemat Basic: "dämpar ljud och vibrationer" borttaget; nu "skyddar golvet under dem". Ordet "vibration" ingår i hälsoordslistan, så tidigare "0 träffar" gällde inte denna mening.
- Tunturi ABS Collar: titeln ändrad från "Leverlås" till "Skivstångslås" (källan säger snäppfäste och skivstångslås).
- Plyo Box: den förvirrande uppgiften "Mått 40 x 50 x 60 cm" borttagen.
- Toorx Olympic Barbell: den negativa meningen "Inte lämplig för CrossFit" borttagen; ersatt med uppgifter ur källan.
- Kvarstår för manuell läsning av granskare: de 177 texter som ännu inte finns.

**5. Pris och Sandi (fynd 5).** Medianpriset i tabellen ovan (1 884 / 1 864) stämmer med `kohorter.csv`; granskarens 1 889 i båda grupperna kunde jag inte återskapa, så skillnaden är oförklarad och bör kontrolleras. Däremot stämmer att K-produkten Spokey Sandi (id 10472251064586, pris 9 kr) ligger kvar i par 115 tillsammans med T-produkten 10470997721354 (Spokey Twin gymnastikrulle, 189 kr). Båda ska tas ur kohorterna före start; ingen av dem finns bland de 39 utkasten. Då återstår 215 par. Produkt 10472250933514 (9 kr) finns inte i kohorterna.

**6. Förkontroll (fynd 6).** `verktyg/forkontroll.graphql` hämtar nu `updatedAt`, `title`, `descriptionHtml`, `totalInventory` och `status` och ska köras för alla 432 id:n (50 per anrop) före varje skrivning och varje vecka. `utfor_batchar/forkontroll-01.graphql` fick samma fält.

**7. Titelsuffix (fynd 7).** Att temat lägger till " – BEST OF SPORTS" är läst i `snippets/doc-head-core.liquid` men filen finns inte bland sparade original och `<title>` är inte sedd i live-HTML. Kanariekörningen ska verifiera `<title>` på `.se` innan resten skrivs.
