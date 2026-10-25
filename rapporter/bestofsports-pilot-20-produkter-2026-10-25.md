# Best of Sports: pilot på 20 produkter, utkast till titlar och beskrivningar (2026-10-25)

**Status: reviderat utkast efter Davids svar 2026-10-25. Inget är ändrat i Shopify.** Varje produkt har före och efter, och en lista på det som måste bekräftas. Du granskar och säger ja per produkt (eller "alla utom X"). Först därefter skriver jag in texterna enligt rutinen: originalen sparas, ändringen görs, läses tillbaka och loggas.

## Urval
20 aktiva produkter med lager (minst 3), valda för att täcka sortimentet och olika typer av text: kondition (motionscykel, löpband), styrka (bänk, kettlebell, viktskivor), cyklar och cykeltillbehör (elcykel, barncykel, hjälm, lås, pump), kosttillskott och solglasögon. 18 är Velomarket-produkter och 2 är Gorilla Sports Norden-varor (rak träningsbänk och Movit-viktskivor). **Urvalet är inte rangordnat på trafik.** Det görs när prioritetsfrågan (`sql/analys/bos/12_produkter_prioritet_texter.sql`) är körd. Syftet med piloten är att pröva mallen och att se hur mycket i leverantörens text som faktiskt går att lita på.

## Så är utkasten gjorda
- **Bara det som finns i originaltexten.** Inga specifikationer är påhittade. Det som saknas eller är tveksamt står under "Att bekräfta eller rätta".
- **Hälsopåståenden och reklamlöften är borttagna** (till exempel "snabb smärtlindring", effekt av ingredienser och tidsbundet "ledande de senaste 5 åren"). De är riskabla mot marknadsföringsregler och Googles regler.
- **Märkets land och bakgrund** (till exempel "tyskt", "italienskt") är min kunskap och inte hämtad ur butiken. De är markerade och måste bekräftas eller tas bort.
- **Leverans, retur och garanti** ska komma från ett gemensamt standardblock per marknad (se längst ned), så att det ändras på ett ställe. I utkasten står en markör.
- **Titlar** följer formeln Typ, Märke, Modell, nyckelegenskap, färg. Gränserna är titel högst 70 tecken, SEO-titel högst 60 och metabeskrivning 140–155 (kontrollerade, med några korta undantag).

## Mönster som piloten visar
1. **Leverantörstexten innehåller fel:** maskinöversättningar ("Träningsbältet", "Talon 20" på en Liv Tempt 20, upprepade rader hos Tunturi-kettlebellen), motsägelser (titel "2–40 kg" men tabellen visar 1,25–25 kg), orimliga mått, och flera har hälsopåståenden eller reklamlöften som bör bort (bland annat bänken Tricon Flex, pre-workouten, Nutcase-hjälmen och Limar-solglasögonen).
2. **Titlarna är fel i sak i flera fall:** "Koffeinpulver" är en pre-workout, "NorsK" syftar troligen på en norsk variant, och flera titlar saknar modell eller märke.
3. **Det mesta är rätt i grunden:** specifikationerna går att lyfta ur texten och sortera upp. Det är strukturen och språket som saknas, inte fakta.

### Motionscykel CHRISTOPEIT AL 1, svart
Produkt-id: `10462768038154`

**Titel:** Motionscykel Christopeit AL 1, magnetbroms med 8 nivåer, svart  (62 tecken)
**SEO-titel:** Motionscykel Christopeit AL 1, 8 nivåer | Best of Sports  (56 tecken)
**Metabeskrivning:** Christopeit AL 1 är en tyst motionscykel med magnetbroms, 8 motståndsnivåer, pulssensorer i handtagen och plats för surfplatta. Passar längd 155–200 cm.  (152 tecken)

**Beskrivning (utkast):**

Christopeit AL 1 är en tyst motionscykel för hemmaträning med magnetbroms, 8 motståndsnivåer och pulssensorer i handtagen.

**Passar dig som:**
- Du som vill träna konditionen hemma utan buller
- Användare mellan 155 och 200 cm (sadel och handtag justeras)
- Du som vill följa pulsen och träna med surfplatta eller mobil på hållaren

**Specifikationer:**
- Bromssystem: magnetbroms, 8 motståndsnivåer
- Display: stor LCD med beröringskänsliga knappar, pulsmätning via handtagen
- Justering: sadel i höjd och sidled med snabbkoppling, handtag med justerbar lutning
- Pedaler: antiglidpedaler med pedalspärr
- Mått: 96 x 59 x 134 cm, vikt 27 kg
- Maximal användarvikt: 150 kg
- Transporthjul fram och justerbara fötter bak

**Leverans, retur och garanti:** standardblock (se nedan)

**Vanliga frågor:**
- **Vilken längd passar cykeln för?** Den är avsedd för användare mellan 155 och 200 cm.
- **Är den tyst?** Ja, bromssystemet är magnetiskt och cykeln har en platt gummirem, vilket ger tyst gång.

**Om märket:** Christopeit Sport är ett tyskt märke för hemmaträning, grundat 1976 i Velbert.

**Att bekräfta eller rätta:**
- Originaltexten säger "Max. belastning: 9 kg" och "155 till 155 cm". Troligen svänghjulets vikt (9 kg) respektive längdspannet 155–200 cm. Bekräfta svänghjulets vikt innan den nämns.
- "Christopher" finns som tagg (felstavning av märket), bör bort.
- Märkesuppgift verifierad mot två källor (återförsäljarsidor): Tyskland, Velbert, 1976. Källorna är återförsäljare, inte företagets egen sida.

---

### TOORX BRX65 motionscykel med ryggstöd
Produkt-id: `10541370114314`

**Titel:** Motionscykel Toorx BRX 65 Comfort med ryggstöd  (46 tecken)
**SEO-titel:** Motionscykel Toorx BRX 65 Comfort med ryggstöd | Best of Sports  (63 tecken)
**Metabeskrivning:** Toorx BRX 65 Comfort är en liggande motionscykel med ryggstöd, 8 motståndsnivåer och LCD-display. Skonsam mot lederna och tyst. Maxvikt 110 kg.  (143 tecken)

**Beskrivning (utkast):**

Toorx BRX 65 Comfort är en motionscykel med ryggstöd för hemmaträning, med 8 motståndsnivåer och en tydlig LCD-display.

**Passar dig som:**
- Dig som vill ha en bekväm cykel som är skonsam mot lederna
- Nybörjare och vana motionärer som tränar hemma
- Dig som bor i lägenhet och vill ha ett tyst motståndssystem

**Specifikationer:**
- Display: LCD (tid, hastighet, förbrända kalorier)
- Motståndsnivåer: 8, manuellt justerbara
- Bromssystem: PMS, manuellt
- Svänghjulsvikt: 7 kg
- Mått: 130 x 63 x 97 cm, vikt 29,5 kg
- Maximal användarvikt: 110 kg

**Leverans, retur och garanti:** standardblock (se nedan)

**Vanliga frågor:**
- **Går den att ha i lägenhet?** Ja, motståndssystemet är tyst och cykeln är kompakt (130 x 63 x 97 cm).
- **Visar den puls?** Uppgift saknas i produkttexten. Bekräfta med leverantören.

**Om märket:** Toorx är ett italienskt märke för hemmaträning som ägs av Garlando S.p.A.

**Att bekräfta eller rätta:**
- Pulsmätning och montering är inte angivna i texten.
- Märkesuppgift verifierad: Toorx ägs av Garlando S.p.A. (Garlandos egen katalog och företagssida). Toorx lanseringsår är oklart och anges inte.

---

### Spinningcykel HAMMER Speed Race SR
Produkt-id: `10411848532234`

**Titel:** Spinningcykel Hammer Speed Race SR med 10,1-tums pekskärm  (57 tecken)
**SEO-titel:** Spinningcykel Hammer Speed Race SR | Best of Sports  (51 tecken)
**Metabeskrivning:** Hammer Speed Race SR är en spinningcykel med 10,1-tums pekskärm, 16 träningsprogram och 20 kg svänghjul. Maxvikt 150 kg. Beställningsvara.  (138 tecken)

**Beskrivning (utkast):**

Hammer Speed Race SR är en spinningcykel för intensiv hemmaträning med 10,1-tums pekskärm, 16 träningsprogram och 20 kg svänghjul.

**Passar dig som:**
- Dig som vill träna intervaller och program hemma
- Användare upp till 150 kg
- Dig som vill ha en stabil cykel med servostyrd belastning

**Specifikationer:**
- Display: 10,1 tum TFT-pekskärm
- Träningsprogram: 16
- Belastningsintervall: 32
- Bromssystem: PMS, servomotor
- Svänghjul: 20 kg
- Mått: 145 x 51 x 151 cm, vikt 44 kg
- Maximal användarvikt: 150 kg
- Handtagslängd 18 cm, pedalavstånd 17 cm

**Leverans, retur och garanti:** standardblock (se nedan)

**Vanliga frågor:**
- **Hur lång är leveranstiden?** Detta är en beställningsvara och kan ta upp till en vecka längre att leverera.
- **Vem tillverkar den?** Hammer, Tyskland.

**Om märket:** Hammer Sport AG är ett tyskt företag för hemmaträning.

**Att bekräfta eller rätta:**
- Beställningsvara: leveranstiden bör synas högt upp och i Merchant-flödet (tillgänglighet "förbeställning"/leveranstid), annars riskerar vi missnöjda köp.

---

### Treadmill CHRISTOPEIT TM 750S
Produkt-id: `10472280850698`

**Titel:** Löpband Christopeit TM 750S, hopfällbart, 1,75 hk  (49 tecken)
**SEO-titel:** Löpband Christopeit TM 750S, hopfällbart 1,75 hk | Best of Sports  (65 tecken)
**Metabeskrivning:** Christopeit TM 750S är ett hopfällbart löpband, 95 % förmonterat, med 1,75 hk motor, 16 program och 4-punkts stötdämpning. Smal förvaring under sängen.  (151 tecken)

**Beskrivning (utkast):**

Christopeit TM 750S är ett hopfällbart löpband för hemmet, 95 % förmonterat, med 1,75 hk motor, 16 träningsprogram och hastighet upp till 16 km/h.

**Passar dig som:**
- Dig som vill ha ett löpband som går att fälla och förvara under säng eller soffa
- Dig som vill slippa komplicerad montering
- Löpare och joggare som vill ha ledskonande stötdämpning

**Specifikationer:**
- Motor: 1,75 hk
- Hastighet: 1–16 km/h med snabbvalsknappar
- Löpyta: 120 x 45 cm
- Träningsprogram: 16
- Stötdämpning: aktivt system med 4 kuddar
- Hopfällning: Easy Foldable System, höjd 19 cm liggande, djup 34 cm stående
- Smörjsystem integrerat, transporthjul, hållare för surfplatta

**Leverans, retur och garanti:** standardblock (se nedan)

**Vanliga frågor:**
- **Behöver den monteras?** Nej, den är 95 % förmonterad.
- **Hur mycket plats tar den?** Hopfälld är den 19 cm hög (liggande) eller 34 cm djup (stående).

**Om märket:** Christopeit Sport är ett tyskt märke för hemmaträning, grundat 1976 i Velbert.

**Att bekräfta eller rätta:**
- Originalet är längre (461 ord) och innehåller fler specifikationer än vad som visades för mig (maxvikt, mått, vikt). Behåll dem från originalet i den färdiga texten.
- "Treadmill" i titeln är engelska och byts till "Löpband".

---

### Treadmill HAMMER Walk 2.0 NorsK
Produkt-id: `10472307982602`

**Titel:** Gåband Hammer Walk 2.0 Norsk, ekfinish, 1–6 km/h  (48 tecken)
**SEO-titel:** Gåband Hammer Walk 2.0 Norsk, ekfinish | Best of Sports  (55 tecken)
**Metabeskrivning:** Hammer Walk 2.0 är ett kompakt gåband med viskande tyst motor, fjärrkontroll och två lutningar. Passar hemmakontor och vardagsrum. Hastighet 1–6 km/h.  (150 tecken)

**Beskrivning (utkast):**

Hammer Walk 2.0 är ett kompakt gåband med ekfinish och tyst motor, avsett för hemmakontor och vardagsrum, med hastighet 1–6 km/h.

**Passar dig som:**
- Dig som vill gå under arbetsdagen på hemmakontoret
- Dig som vill ha ett tyst alternativ som inte stör andra
- Dig som vill ha ett enkelt gåband med fjärrkontroll

**Specifikationer:**
- Motor: 1,25 hk (max 1,75 hk)
- Hastighet: 1–6 km/h
- Löpyta: 105 x 42 cm
- Lutning: 2 lägen (0 och 2,5 grader)
- Träningsprogram: 13, LED-display och fjärrkontroll
- Mått: 128 x 58 x 16 cm, vikt 28 kg
- Maximal användarvikt: 120 kg

**Leverans, retur och garanti:** standardblock (se nedan)

**Vanliga frågor:**
- **Är det ett löpband?** Nej, hastigheten går till 6 km/h och det är avsett för gång.
- **Hur lång är leveranstiden?** Beställningsvara, kan ta upp till en vecka längre.

**Om märket:** Hammer Sport AG är ett tyskt företag för hemmaträning.

**Att bekräfta eller rätta:**
- JÄMFÖRELSE Walk 2.0 (id 10472289042698, SKU 13007, 6 909 kr) mot Walk 2.0 NorsK (id 10472307982602, SKU 13016, 8 469 kr): identiska specifikationer (LED, 13 program, 1,25 hk, löpyta 105 x 42 cm, 1–6 km/h, lutning 0 och 2,5°, 128 x 58 x 16 cm, 28 kg), men olika artikelnummer och streckkod, olika bilder, NorsK beskrivs med ekfinish och kostar 1 560 kr mer. Slutsats: samma modell i två utföranden, inte en dubblett. Titlarna görs tydliga; sammanslagning till en produkt med två varianter (utförande) är ett separat beslut.
- Max användarvikt 120 kg finns bara i NorsK-texten, inte i den andra.

---

### Löpband TUNTURI Cardio Fit T5 med Bluetooth
Produkt-id: `10472295596298`

**Titel:** Löpband Tunturi Cardio Fit T5 med Bluetooth, hopfällbart  (56 tecken)
**SEO-titel:** Löpband Tunturi Cardio Fit T5 med Bluetooth | Best of Sports  (60 tecken)
**Metabeskrivning:** Tunturi Cardio Fit T5 är ett kompakt löpband med Bluetooth, 14 program och tyst 1,5 hk motor. Hopfällbart och färdigmonterat. Maxvikt 100 kg.  (141 tecken)

**Beskrivning (utkast):**

Tunturi Cardio Fit T5 är ett kompakt, hopfällbart löpband med Bluetooth, 1,5 hk tyst motor och 14 träningsprogram, levereras färdigmonterat.

**Passar dig som:**
- Dig som vill promenera eller jogga hemma på liten yta
- Dig som vill förvara löpbandet under soffa, säng eller bakom garderob
- Användare upp till 100 kg

**Specifikationer:**
- Motor: 1,5 hk, tyst
- Hastighet: 0,8–8 km/h, 14 hastigheter
- Löpyta: 100 x 40 cm
- Träningsprogram: 14, Bluetooth-anslutning
- Display: 3 lysdioder
- Mått: 121,9 x 67,4 x 126,9 cm, hopfälld 27,5 x 61 x 127 cm
- Vikt: 23 kg, maximal användarvikt 100 kg

**Leverans, retur och garanti:** standardblock (se nedan)

**Vanliga frågor:**
- **Behöver den monteras?** Nej, den är färdigmonterad i kartongen.
- **Hur snabbt går det?** Upp till 8 km/h, lämpligt för promenad och lätt jogging.

**Om märket:** Tunturi grundades 1922 i Åbo, Finland.

**Att bekräfta eller rätta:**
- Tunturi: "grundades 1922 i Åbo" stöds av Wikipedia och Yle. Nutida ägande och status är oklart (en finsk nyhet om en konkursansökan för ett Tunturi-bolag, troligen cykelbolaget), därför står inga nutida påståenden som "globalt märke". Bör kontrolleras om leverantören av träningsutrustningen påverkas.

---

### Träningsbänk Tunturi UB70 Utility Bench
Produkt-id: `10541268795658`

**Titel:** Träningsbänk Tunturi UB70 Utility Bench, justerbar, 250 kg  (58 tecken)
**SEO-titel:** Träningsbänk Tunturi UB70, justerbar 250 kg | Best of Sports  (60 tecken)
**Metabeskrivning:** Tunturi UB70 är en stabil, justerbar träningsbänk för hemmagym och gym. Ländryggsstöd, transporthjul och maxbelastning 250 kg. Vikt 25 kg.  (138 tecken)

**Beskrivning (utkast):**

Tunturi UB70 Utility Bench är en stabil och justerbar träningsbänk för hemmaträning och gym, med ländryggsstöd och maxbelastning 250 kg.

**Passar dig som:**
- Dig som bygger hemmagym och vill ha en bänk med justerbar sits och rygg
- Dig som tränar tungt (250 kg maxbelastning)
- Dig som behöver flytta bänken (transporthjul och handtag)

**Specifikationer:**
- Justering: sits- och ryggstödsvinkel
- Ergonomi: extra ländryggsstöd
- Maximal belastning: 250 kg
- Mått: 68 x 135 x 122 cm
- Vikt: 25 kg
- Transporthjul och bärhandtag

**Leverans, retur och garanti:** standardblock (se nedan)

**Vanliga frågor:**
- **Går den att justera?** Ja, både sitsens och ryggstödets vinkel justeras.
- **Hur mycket tål den?** Maximal belastning är 250 kg.

**Om märket:** Tunturi grundades 1922 i Åbo, Finland.

**Att bekräfta eller rätta:**
- Måtten 68 x 135 x 122 cm är ologiska för en bänk i hög position (122 cm). Kolla mot leverantörens datablad.
- Antal justeringslägen saknas.

---

### Träningsbänk Rak Svart
Produkt-id: `10636604932362`

**Titel:** Träningsbänk, rak, svart, 250 kg maxbelastning  (46 tecken)
**SEO-titel:** Rak träningsbänk svart, 250 kg | Best of Sports  (47 tecken)
**Metabeskrivning:** Rak träningsbänk i svart med höjd 40 cm och maxbelastning 250 kg inklusive kroppsvikt. Stabil bänk för hemmagymmet, passar bra med skivstångsställning.  (151 tecken)

**Beskrivning (utkast):**

Rak träningsbänk i svart, 40 cm hög och godkänd för 250 kg inklusive kroppsvikt, avsedd för hemmagymmet.

**Passar dig som:**
- Dig som vill ha en enkel och stabil bänk till bänkpress och hantelövningar
- Dig som kombinerar bänken med skivstångsställning
- Dig som vill ha en lätt bänk (16 kg)

**Specifikationer:**
- Höjd: 40 cm
- Mått inklusive ben (L x B x H): 110 x 58 x 40 cm
- Mått ryggdyna: 110 x 25 x 5 cm
- Maxbelastning: 250 kg inklusive kroppsvikt
- Vikt: 16 kg
- Färg: svart

**Leverans, retur och garanti:** standardblock (se nedan)

**Vanliga frågor:**
- **Går den att justera?** Nej, det är en rak bänk.
- **Passar den till skivstångsställning?** Ja, den kan användas tillsammans med skivstångsställning.

**Att bekräfta eller rätta:**
- Märket "Gorilla Sports Norden" är leverantör, inte konsumentvarumärke. Om produkten har eget varumärke (Movit?) bör det stå i titeln.
- Titeln saknar märke och modell, vilket gör den svår att skilja från andra raka bänkar.

---

### Träningsbänk FINNLO by HAMMER Tricon Flex
Produkt-id: `10507302764810`

**Titel:** Träningsbänk Finnlo by Hammer Tricon Flex, hopfällbar rygg- och stretch  (71 tecken)
**SEO-titel:** Träningsbänk Finnlo Tricon Flex, hopfällbar | Best of Sports  (60 tecken)
**Metabeskrivning:** Finnlo by Hammer Tricon Flex är en hopfällbar bänk för ryggträning, hyperextensions och stretch. Maxbelastning 130 kg. Hopfälld 54 x 51 x 108 cm.  (145 tecken)

**Beskrivning (utkast):**

Finnlo by Hammer Tricon Flex är en hopfällbar bänk för ryggträning, hyperextensions och stretching, med maxbelastning 130 kg.

**Passar dig som:**
- Dig som vill träna ryggen och stretcha benens muskler hemma
- Dig som behöver en bänk som går att fälla ihop och ställa undan

**Specifikationer:**
- Användning: hyperextensions och stretchfunktioner
- Mått: 106 x 51 x 95 cm
- Nödvändig yta vid användning: 164 x 51 x 95 cm
- Mått hopfälld: 54 x 51 x 108 cm
- Vikt: 17 kg
- Maximal belastning: 130 kg

**Leverans, retur och garanti:** standardblock (se nedan)

**Vanliga frågor:**
- **Går den att fälla ihop?** Ja, hopfälld är den 54 x 51 x 108 cm.
- **Är den en medicinsk produkt?** Nej. Den är träningsutrustning.

**Om märket:** Finnlo är premiummärket inom det tyska företaget Hammer Sport AG.

**Att bekräfta eller rätta:**
- Originalet lovar "snabb smärtlindring" och hjälp vid ischias. Sådana hälsopåståenden bör tas bort (marknadsföringsregler och Googles regler), vilket jag har gjort.

---

### Elcykel GIANT Talon E+, 29" Asphalt Green
Produkt-id: `10488326193418`

**Titel:** Elcykel Giant Talon E+ 29", mountainbike, Asphalt Green  (55 tecken)
**SEO-titel:** Elcykel Giant Talon E+ 29" mountainbike | Best of Sports  (56 tecken)
**Metabeskrivning:** Giant Talon E+ är en elcykel med mittmotor (SyncDrive Sport 2, 75 Nm), 430 Wh batteri och räckvidd upp till 115 km. 29" hjul, 9 växlar och hydrauliska bromsar.  (159 tecken)

**Beskrivning (utkast):**

Giant Talon E+ är en elmountainbike med 29"-hjul, mittmotor (Giant SyncDrive Sport 2, 75 Nm) och 430 Wh batteri med räckvidd upp till 115 km.

**Passar dig som:**
- Dig som cyklar skogsstigar, grusvägar eller pendlar
- Dig som vill ha stark trampassistans och enkel terränghantering
- Cyklister mellan 163 och 200 cm (fyra ramstorlekar)

**Specifikationer:**
- Motor: Giant SyncDrive Sport 2, 250 W, 75 Nm, mittmotor
- Batteri: Giant EnergyPak Smart 430 Wh, räckvidd upp till 115 km
- Ram: ALUXX-aluminium
- Växlar: 9, Shimano Cues
- Bromsar: Shimano MT200, hydrauliska skivbromsar
- Gaffel: SR Suntour XCM, 100 mm slaglängd
- Däck: Maxxis Rekon 29 x 2,4"
- Ramstorlekar: S 38,5 cm (163–174 cm), M 43,5 cm (171–182 cm), L 48,5 cm (179–190 cm), XL 53,5 cm (187–200 cm)

**Leverans, retur och garanti:** standardblock (se nedan)

**Vanliga frågor:**
- **Vilken storlek ska jag välja?** Välj efter din längd enligt ramstorlekarna ovan.
- **Går det att montera stänkskärmar?** Ja, cykeln har fästpunkter för stänkskärmar och tillbehör.

**Om märket:** Giant grundades 1972 i Taiwan och är en av världens största cykeltillverkare.

**Att bekräfta eller rätta:**
- Räckvidden upp till 115 km är tillverkarens uppgift under bästa förhållanden, bör stå så.
- Färgen "Asphalt Green" ligger kvar på engelska i titeln, svensk term saknas (oftast behålls färgnamnet).

---

### Hopfällbar elcykel ADO Air 20 Ultra (2026) Grå
Produkt-id: `10656694239498`

**Titel:** Hopfällbar elcykel ADO Air 20 Ultra (2026), grå  (47 tecken)
**SEO-titel:** Hopfällbar elcykel ADO Air 20 Ultra 2026 | Best of Sports  (57 tecken)
**Metabeskrivning:** ADO Air 20 Ultra 2026 är en hopfällbar elcykel med 50 Nm Bafang-motor, 3 automatiska växlar, NFC-display och IPX6. Kompakt stadscykel med pakethållare.  (151 tecken)

**Beskrivning (utkast):**

ADO Air 20 Ultra (2026) är en hopfällbar elcykel för stadsbruk med Bafang H730-motor på 50 Nm, 3 automatiska växlar och momentgivare.

**Passar dig som:**
- Dig som pendlar i stan och vill ha en cykel som går att fälla ihop
- Dig som vill ha jämn assistans efter egen ansträngning (momentgivare)

**Specifikationer:**
- Motor: Bafang H730, 50 Nm (2026 års modell, tidigare 40 Nm)
- Växlar: 3 automatiska
- Display: NFC-aktiverad, startar på 1,7 sekunder
- Vattenbeständighet: IPX6
- Däck: 20 x 2,0 tum med reflexlister
- Främre fjädring: justerbar gaffel
- Pakethållare med MIK-fäste och integrerad baklykta, strålkastare integrerad i ramen

**Leverans, retur och garanti:** standardblock (se nedan)

**Vanliga frågor:**
- **Går cykeln att fälla ihop?** Ja, den är hopfällbar.
- **Hur snabbt ger motorn kraft?** Momentgivaren mäter kraften på pedalerna och justerar assistansen efter din ansträngning.

**Att bekräfta eller rätta:**
- Originalet är längre (225 ord) med fler uppgifter (batteri, räckvidd, vikt) som behålls i den färdiga texten. Batteri och räckvidd måste hämtas därifrån, jag har inte skrivit dem.
- "25 procent mer kraft" bör kunna beläggas (50/40 Nm = 25 %, stämmer).
- Saknas: batterikapacitet, räckvidd, vikt, maxvikt i denna sammanfattning.
- ADO: ursprung ("kinesiskt") finns bara i en källa och anges därför inte.

---

### Barncykel LIV Tempt 20, AI Blue
Produkt-id: `10471131250954`

**Titel:** Barncykel Liv Tempt 20" mountainbike, AI Blue  (45 tecken)
**SEO-titel:** Barncykel Liv Tempt 20" mountainbike | Best of Sports  (53 tecken)
**Metabeskrivning:** Liv Tempt 20 är en barncykel i mountainbikeutförande med främre fjädring, lätt aluminiumram och barnanpassade komponenter. Ramstorlek S för 118–138 cm.  (151 tecken)

**Beskrivning (utkast):**

Liv Tempt 20 är en mountainbike för barn med 20"-hjul, främre fjädring och aluminiumram, anpassad för barn mellan 118 och 138 cm.

**Passar dig som:**
- Barn som cyklar på grusvägar och skogsstigar
- Barn som vuxit ur en mindre cykel och är 118–138 cm långa

**Specifikationer:**
- Ram: ALUXX-aluminium, ramstorlek S (22,5 cm)
- Passar längd: 118–138 cm
- Främre fjädring: ja
- Styre: smalare, 25 mm diameter, bromshandtag med kort räckvidd
- Vevar: kortare för jämn trampning
- Medföljer: stöd, främre stänkskärm och ringklocka

**Leverans, retur och garanti:** standardblock (se nedan)

**Vanliga frågor:**
- **Vilken längd passar cykeln?** Ramstorlek S passar barn mellan 118 och 138 cm.
- **Medföljer stänkskärm och ringklocka?** Ja.

**Om märket:** Liv är ett cykelvarumärke inom Giant-koncernen.

**Att bekräfta eller rätta:**
- Originalet nämner "Talon 20" i texten (felskrivning), använd "Tempt 20".
- Annonskostnad på barncyklar (Tempt 24, Rambler 20) är sedan tidigare en stor del av annonsbudgeten, behåll koppling till annonsdatan.

---

### TUNTURI PE Kettlebell 16kg
Produkt-id: `10588446589194`

**Titel:** Kettlebell Tunturi PE 16 kg, PVC fylld med sand  (47 tecken)
**SEO-titel:** Kettlebell 16 kg Tunturi PE, PVC med sand | Best of Sports  (58 tecken)
**Metabeskrivning:** Tunturi PE-kettlebell 16 kg i PVC fylld med sand. Lätt att rengöra och förvara, för styrka, kondition och rörlighet i hemmaträningen.  (133 tecken)

**Beskrivning (utkast):**

Tunturi PE-kettlebell är en kettlebell på 16 kg i PVC fylld med sand, ett billigare alternativ till gjutjärn för helkroppsträning hemma.

**Passar dig som:**
- Dig som vill träna hela kroppen med en enkel redskap hemma
- Dig som vill ha ett lättskött alternativ till gjutjärn

**Specifikationer:**
- Vikt: 16 kg
- Material: PVC fylld med sand
- Lätt att rengöra och förvara

**Leverans, retur och garanti:** standardblock (se nedan)

**Vanliga frågor:**
- **Är den lika bra som gjutjärn?** Du kan göra samma övningar, den är gjord av PVC med sandfyllning.
- **Vad tränar man med den?** Styrka, koordination, flexibilitet och bålstabilitet.

**Om märket:** Tunturi grundades 1922 i Åbo, Finland.

**Att bekräfta eller rätta:**
- Originalet har en upprepad rad ("Lätt att använda, billigare, lätt att rengöra…") som är tydligt maskinöversättning, den är borttagen.
- Mått och handtagsdiameter saknas.

---

### Kettlebell TUNTURI Platinum Competition, 12 kg
Produkt-id: `10588451635466`

**Titel:** Kettlebell Tunturi Platinum Competition 12 kg, tävlingsstandard  (63 tecken)
**SEO-titel:** Kettlebell Tunturi Platinum Competition 12 kg | Best of Sports  (62 tecken)
**Metabeskrivning:** Tunturi Platinum Competition 12 kg är en kettlebell i stål enligt tävlingsstandard. Samma storlek i alla vikter, färgkodad. För HYROX och gym.  (142 tecken)

**Beskrivning (utkast):**

Tunturi Platinum Competition är en kettlebell i stål (12 kg) tillverkad enligt internationell tävlingsstandard, med samma storlek och form i alla vikter.

**Passar dig som:**
- Dig som tränar HYROX, crossträning eller funktionell träning
- Gym och professionella miljöer som behöver hållbara kettlebells

**Specifikationer:**
- Vikt: 12 kg
- Material: stål
- Mått: 19,4 x 21 x 28 cm
- Ingraverad viktmarkering och färgkod enligt internationell standard
- Samma storlek och form oavsett vikt

**Leverans, retur och garanti:** standardblock (se nedan)

**Vanliga frågor:**
- **Varför samma storlek i alla vikter?** För konsekvent grepp och kroppsposition när du byter vikt.
- **Passar den i ett gym?** Ja, den är designad för kommersiellt bruk.

**Om märket:** Tunturi grundades 1922 i Åbo, Finland.

---

### Viktskivor Movit Gjutjärn 2-40kg
Produkt-id: `10636617875722`

**Titel:** Viktskivor Movit gjutjärn med gummibeläggning, 30/31 mm, 1,25–25 kg  (67 tecken)
**SEO-titel:** Viktskivor Movit gjutjärn 30/31 mm | Best of Sports  (51 tecken)
**Metabeskrivning:** Movit viktskivor i gjutjärn med 4 mm gummibeläggning, håldiameter 31 mm för 30 mm stänger. Tystare och greppvänliga. Säljs parvis, 1,25–25 kg.  (142 tecken)

**Beskrivning (utkast):**

Movit viktskivor i gjutjärn med 4 mm gummibeläggning och håldiameter 31 mm, för skivstänger med 30 mm diameter. Säljs parvis.

**Passar dig som:**
- Nybörjare och vana som bygger hemmagym
- Dig som vill ha tystare skivor än rena gjutjärnsskivor

**Specifikationer:**
- Håldiameter: 31 mm (passar 30 mm stänger)
- Material: gjutjärn med 4 mm gummibeläggning
- Säljs parvis
- Vikter: 1,25, 2,5, 5, 10, 15, 20, 25 kg
- Exempel på mått: 10 kg = 3,4 cm tjock, 28 cm diameter; 20 kg = 4,2 cm, 34,5 cm

**Leverans, retur och garanti:** standardblock (se nedan)

**Vanliga frågor:**
- **Passar de min skivstång?** Ja, om stången har 30 mm diameter på hylsan.
- **Säljs de styckvis?** Nej, de säljs parvis.

**Att bekräfta eller rätta:**
- Titeln säger "2–40 kg", men texten listar 1,25–25 kg (och en tabell med 0,5 kg). Bekräfta vilka vikter som finns, annars blir det fel.
- Produkten har 2 970 i lager och ligger troligen som flera varianter, kontrollera varianttitlar.

---

### Koffeinpulver TREC Boogieman 20g, Candy
Produkt-id: `10472323186954`

**Titel:** Pre-workout Trec Boogieman 20 g, Candy  (38 tecken)
**SEO-titel:** Pre-workout Trec Boogieman 20 g, Candy | Best of Sports  (55 tecken)
**Metabeskrivning:** Trec Boogieman Candy är ett pre-workout-pulver med koffein (150 mg), beta-alanin (2 400 mg) och citrullinmalat (2 500 mg). Godissmak.  (133 tecken)

**Beskrivning (utkast):**

Trec Boogieman Candy är ett pre-workout-pulver med godissmak, avsett att tas före träning. Det innehåller 150 mg koffein, 2 400 mg beta-alanin och 2 500 mg citrullinmalat.

**Passar dig som:**
- Dig som vill ta ett pre-workout före styrke- eller konditionsträning
- Dig som tål koffein (150 mg per portion)

**Specifikationer:**
- Smak: Candy
- Innehåll per portion: koffein 150 mg, beta-alanin 2 400 mg, citrullinmalat 2 500 mg
- Ytterligare ingredienser: L-arginin AKG, taurin, L-tyrosin, vitamin B6 och B12, magnesium, koreansk ginsengextrakt, alfa-liponsyra
- Beta-alanin, citrullin, koffein och taurin är ingredienser som ofta ingår i pre-workout-produkter
- Användning och dosering: enligt etiketten

**Leverans, retur och garanti:** standardblock (se nedan)

**Vanliga frågor:**
- **Hur mycket koffein innehåller en portion?** 150 mg.
- **Vem bör inte använda den?** Se förpackningens varningstexter. Produkten är inte avsedd för barn, gravida eller ammande.

**Om märket:** Trec Nutrition är ett polskt märke för kosttillskott med bas i Gdynia.

**Att bekräfta eller rätta:**
- HÄLSOPÅSTÅENDEN, behöver ditt beslut: du vill beskriva varför man tar tillskottet och inte ta bort allt. Utkastet säger därför syftet (pre-workout, före träning) och vilka ingredienser som ingår och brukar ingå i sådana produkter, utan att påstå effekt. Att mildra språket ("möjliga effekter", "kan bidra till") ändrar inte att det är ett hälsopåstående: i EU får kosttillskott bara marknadsföras med godkända påståenden (förordning 1924/2006), och formuleringar som antyder effekt omfattas även med försiktiga ord. Vill du ha effektbeskrivningar bör vi använda godkända påståenden ordagrant och bara där halten stämmer (till exempel för koffein, magnesium och B-vitaminer), kontrollerat mot EU:s register. Detta är inte juridisk rådgivning.
- Titeln "Koffeinpulver" är ändrad till "Pre-workout".
- "20 g" tolkar jag som portionsstorlek (oklart). Förpackningsstorlek saknas.
- Dosering, varningstext och målgrupp ska hämtas från etiketten.

---

### Cykelhjälm Nutcase Darth Lightnin' Reflective MIPS 56-60 cm
Produkt-id: `10475978981642`

**Titel:** Cykelhjälm Nutcase Darth Lightnin' Reflective MIPS, 56–60 cm  (60 tecken)
**SEO-titel:** Cykelhjälm Nutcase Darth Lightnin' MIPS 56–60 cm | Best of Sports  (65 tecken)
**Metabeskrivning:** Nutcase Darth Lightnin' är en reflekterande cykelhjälm med MIPS, Fidlock-magnetspänne och 11 ventilationsöppningar. Storlek M (56–60 cm), avtagbar skärm.  (153 tecken)

**Beskrivning (utkast):**

Nutcase Darth Lightnin' är en reflekterande cykelhjälm med MIPS-skydd, magnetiskt Fidlock-spänne och 11 ventilationsöppningar, i storlek M (56–60 cm).

**Passar dig som:**
- Dig med huvudomkrets 56–60 cm
- Dig som vill ha en hjälm med MIPS och reflexer för stadscykling

**Specifikationer:**
- Storlek: M (56–60 cm)
- Skydd: MIPS, glidande lager mellan skal och huvud
- Spänne: Fidlock, magnetiskt
- Ventilation: 11 öppningar
- Skal: polykarbonat med ABS-innehåll
- Medföljer: avtagbar skärm i matchande färg

**Leverans, retur och garanti:** standardblock (se nedan)

**Vanliga frågor:**
- **Vilken storlek är det?** M, för huvudomkrets 56–60 cm.
- **Har den reflexer?** Ja, den är reflekterande.

**Om märket:** Nutcase är ett amerikanskt märke med säte i Portland, Oregon.

**Att bekräfta eller rätta:**
- Originalet säger "ledande de senaste 5 åren", tidsbunden marknadsföring, borttagen.
- Testbetyg och certifiering (EN 1078) saknas i texten.

---

### AXA Fold 85 vikbart lås
Produkt-id: `10475621089546`

**Titel:** Vikbart cykellås AXA Fold 85, 85 cm, Sold Secure Bronze  (55 tecken)
**SEO-titel:** Vikbart cykellås AXA Fold 85, Sold Secure Bronze | Best of Sports  (65 tecken)
**Metabeskrivning:** AXA Fold 85 är ett vikbart cykellås, 85 cm långt med 7 mm härdade stållänkar och Sold Secure Bronze. Levereras med hållare och 2 nycklar.  (137 tecken)

**Beskrivning (utkast):**

AXA Fold 85 är ett vikbart cykellås, 85 cm långt, certifierat Sold Secure Bronze, med 7 mm härdade stållänkar och gummiöverdrag.

**Passar dig som:**
- Dig som parkerar cykeln en kortare till medellång tid i områden med måttlig stöldrisk, till exempel vid en skola
- Dig som vill ha ett lås som tar liten plats och inte rasslar

**Specifikationer:**
- Längd: 85 cm
- Länkar: härdat stål, 7 mm, gummiöverdrag som skyddar cykeln mot repor
- Certifiering: Sold Secure Bronze
- Hållare med fäste för flaskhållarfästen eller med två remmar
- Vibrationsdämpning, skyddat cylinderhölje mot fukt och smuts
- Levereras med 2 nycklar

**Leverans, retur och garanti:** standardblock (se nedan)

**Vanliga frågor:**
- **Är det säkert nog för en dyr cykel?** Låset är certifierat Sold Secure Bronze och avsett för måttlig stöldrisk, för dyra cyklar rekommenderas ett högre skyddsklass.
- **Kan jag beställa extranycklar?** Ja, via tillverkarens nyckelbeställningstjänst.

**Om märket:** AXA är ett nederländskt märke för cykelsäkerhet och ingår i Allegion.

**Att bekräfta eller rätta:**
- Lagernivån (29) och beskrivningens längd gör att produkten är en bra kandidat i annonser, men säkerhetsklass bör stå tydligt.

---

### Handpump GIANT CONTROL MINI ROAD+ BLACK
Produkt-id: `10472233566474`

**Titel:** Handpump Giant Control Mini Road+, svart, 160 psi  (49 tecken)
**SEO-titel:** Handpump Giant Control Mini Road+ 160 psi | Best of Sports  (58 tecken)
**Metabeskrivning:** Giant Control Mini Road+ är en kompakt handpump för Presta-ventil med utbyggbar slang, ramfäste och maxtryck 160 psi (11 bar). Passar landsvägscyklar.  (150 tecken)

**Beskrivning (utkast):**

Giant Control Mini Road+ är en kompakt handpump för Presta-ventil med utbyggbar slang och maxtryck 160 psi (11 bar), med ramfäste.

**Passar dig som:**
- Landsvägscyklister som vill ha en liten pump med högt tryck
- Dig som vill ha en pump som går att fästa på ramen

**Specifikationer:**
- Maxtryck: 160 psi / 11 bar
- Ventil: Presta
- Utbyggbar slang
- Ramfäste
- Färg: svart

**Leverans, retur och garanti:** standardblock (se nedan)

**Vanliga frågor:**
- **Passar den bildäck eller andra ventiler?** Den passar Presta-ventil. För andra ventiltyper behövs en adapter.
- **Kan den fästas på cykeln?** Ja, med medföljande ramfäste.

**Om märket:** Giant grundades 1972 i Taiwan och är en av världens största cykeltillverkare.

**Att bekräfta eller rätta:**
- Originalet säger "lämplig för alla typer av cyklar" men anger bara Presta-ventil, motsägelse. Jag har valt den snävare uppgiften.
- Texten innehöll en standardtext om Giant (1972), den ersätts med en kort mening.

---

### Solglasögon Limar F30, vit
Produkt-id: `10411495555338`

**Titel:** Solglasögon Limar F30, vit, rökfärgad lins  (42 tecken)
**SEO-titel:** Solglasögon Limar F30, vit med rökfärgad lins | Best of Sports  (62 tecken)
**Metabeskrivning:** Limar F30 är solglasögon med polykarbonatbåge och rökfärgad lins med Revo-beläggning. Levereras med svart mikrofiberpåse. Italiensk tillverkare.  (144 tecken)

**Beskrivning (utkast):**

Limar F30 är solglasögon i vitt med polykarbonatbåge och rökfärgad polykarbonatlins med Revo-beläggning.

**Passar dig som:**
- Cyklister som vill ha lätta solglasögon från ett italienskt märke

**Specifikationer:**
- Båge: polykarbonat
- Lins: rökfärgad polykarbonat med Revo-beläggning
- Medföljer: svart mikrofiberpåse/rengöringsduk

**Leverans, retur och garanti:** standardblock (se nedan)

**Vanliga frågor:**
- **Är linsen skyddande mot UV?** Uppgift saknas i produkttexten. Bekräfta med leverantören innan det anges.

**Om märket:** Limar är ett italienskt märke för cykelhjälmar och solglasögon, grundat 1986.

**Att bekräfta eller rätta:**
- UV-klass, vikt, linsform och passform saknas. Det är ovanligt tunna uppgifter för solglasögon, be leverantören om datablad.
- Originalet jämför polykarbonat mot vanlig plast (35 % lättare, 12 gånger starkare), generellt påstående som inte gäller just denna produkt. Behålls inte.

---

## Standardblock: leverans, retur och garanti (Sverige)
Hämtat ur butikens egna policyer och fraktprofiler i Shopify (läst 2026-10-25), inte skrivet av mig. Samma text ska ligga på ett ställe (mall eller metafield) så att den inte kopieras in i varje produkt.

**Frakt och leverans:** Normal leveranstid är 5–8 arbetsdagar. Fraktavgiften visas i kassan (inom Sverige 179 kr; löpband och crosstrainers 499 kr). Se sidan Frakt för övriga länder. Beställningsvaror kan ta upp till en vecka längre.
**Retur:** 30 dagars öppet köp. Vid ångrat köp står du för returfrakten. Vid godkänd reklamation står vi för returfrakten, kontakta kundtjänst för instruktioner.
**Reklamation:** Du har reklamationsrätt enligt konsumentlagstiftningen i ditt land. Tillverkarens garanti anges på produkten när uppgiften finns.
**Säljare:** BOS Latitude 60N AB, org.nr 559500-4325, Lindegårdsvägen 33, 746 36 Bålsta, info@bestofsports.se.

**Fakta bakom blocket:** leveranstid 5–8 arbetsdagar (fraktpolicyn och villkoren), 30 dagars öppet köp, kunden betalar returfrakten vid ångrat köp, butiken betalar vid godkänd reklamation (förbetald returetikett), lager i Tyskland, Finland och Estland, fraktpris Sverige 179 kr (fraktprofilen) och 499 kr för löpband och crosstrainers, Danmark 119 DKK, Finland 12 EUR. **Ingen fri frakt** (bekräftat av dig).

## Avvikelser mellan dina policyer som bör rättas (ingen ändring gjord)
1. Fraktpolicyn säger "mellan 199kr", men kassan tar 179 kr i Sverige. Du valde 179 kr i texterna, så fraktpolicyn bör rättas.
2. Fraktprofilen "Löpband Crosstrainer" tar 499 **SEK** även i Danmark och Finland, medan allmän frakt där är 119 DKK och 12 EUR. Kontrollera om det är avsiktligt.
3. Villkoren (punkt 6.2) och återbetalningspolicyn säger "30 dagars ångerrätt", vilket är mer än lagens 14 dagar. Det är butikens egen 30-dagarsregel och stämmer med texterna ovan, men formuleringen "enligt gällande konsumentlagstiftning" i villkoren är missvisande.
4. Villkoren och retur nämner lager i Tyskland, Finland och Estland men ger ingen returadress; den lämnas av kundtjänst. Texten hänvisar till kundtjänst.

## Verifiering av märkesuppgifter (två källor eller flaggad)
| Märke | Uppgift i texterna | Källor | Status |
|---|---|---|---|
| Christopeit | Tyskt, grundat 1976 i Velbert | Kaufland-märkessida, återförsäljarlistning, eBay-säljarsida | Bekräftad (återförsäljarkällor) |
| Toorx | Italienskt, ägs av Garlando S.p.A. | Garlandos katalog och företagssida | Bekräftad |
| Hammer / Finnlo | Tyskt; Finnlo är premiummärket inom Hammer Sport AG | Fitshop, Galaxus, Velomarket, eBay | Bekräftad. Sätet anges olika (Neu-Ulm eller Hockenheim), så ingen ort anges |
| Tunturi | Grundat 1922 i Åbo | Wikipedia, Yle | Bekräftad. Nutida ägande oklart, inga nutida påståenden |
| Giant | Grundat 1972 i Taiwan, en av världens största | Wikipedia, GCN, bike-magazin, Taiwan Today | Bekräftad |
| Liv | Inom Giant-koncernen | Wikipedia, Giant-källor | Bekräftad |
| Trec Nutrition | Polskt, Gdynia | doz.pl, Aflofarm, aplikuj.pl | Bekräftad |
| Nutcase | Amerikanskt, Portland, Oregon | Nutcase egen sida, Ride Review, BikePortland | Bekräftad. Grundår (2000/2006) anges olika, därför inget år |
| AXA | Nederländskt, ägs av Allegion | Allegions sida, återförsäljare | Bekräftad. Grundår varierar, inget år |
| Limar | Italienskt, grundat 1986 | CyclingIndustry, BikeRadar, Bicycle Retailer | Bekräftad |
| ADO | (utelämnat) | Bara en källa (road.cc) | Ej bekräftad, anges inte |

## Beslut som behövs
1. **Kosttillskottet (Trec Boogieman):** godkänn "syfte och ingredienser utan effektpåstående" (utkastet), eller att vi går igenom godkända påståenden ordagrant mot EU:s register.
2. **Hammer Walk 2.0 och Norsk:** de är samma modell i två utföranden, inte dubbletter. Behåll som två produkter med tydliga titlar (utkastet), eller slå ihop till en produkt med två varianter?
3. **Godkänn de reviderade utkasten.** Texterna har ändrats sedan ditt "ja till alla" (standardblocket, märkesuppgifter, tillskottet, Walk 2.0). Säg "kör" så skriver jag in dem enligt rutinen (original sparas, läses tillbaka, loggas).
