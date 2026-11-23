# Lärdomar från arbetet

Syftet är att samma fel inte upprepas i nya arbetspass. Filen fylls bara på: nya poster läggs överst, gamla ändras inte. Läs den innan du rekommenderar en ändring i en butik, ett tema eller en datamodell.

## Hur en post skrivs
Datum, vad som gick fel eller upptäcktes, och regeln som följer av det.

### 2026-11-04: Kollektioner är blandade; ett prisspann eller antal över hela kollektionen är missvisande
- **Vad hände:** första faktaunderlaget för kategoritexter gav "från 69 kr" för löpband (löpbandsolja), "från 409 kr" för motionscykel (cykelsadel) och 26 sparkcykelhjul i sparkcyklar. `productType` duger inte som typ (nästan allt är "Konditionsträning & Fitness"). Upptäcktes när billigaste titlarna listades innan texten skrevs.
- **Regel:** räkna antal, märken och pris för en kategori bara på huvudprodukter (typordet i titelns två första ord, `kategorier_underlag.py`). Granska alltid billigaste och dyraste titel innan ett prisspann skrivs. Leverantörsnamn (Velomarket, Gorilla Sports Norden) är inte märken.

### 2026-11-04: Data för prioritering saknades i sessionen (Windsor bara Facebook, Ahrefs ingår inte i planen)
- **Regel:** kontrollera datakällor (`get_connectors`, ett testanrop) innan en prioritering lovas efter Search Console. Säg öppet när prioriteringen bygger på ersättningsmått (antal köpbara produkter).


### 2026-11-06: F2:s mätetal var inaktuellt, och R5 räknar bara html
- **Vad hände:** F2 och tidigare beslutsfiler säger "2 av 24 texter" har "enligt tillverkaren" på maxvikt. Efter rensning 2 (178 specifikationsrader, 2026-11-04) och nya batcher gäller det inte längre: i repots data saknar bara 10 av 482 texter frasen helt; 156 har den på en förekomst men upprepar uppgiften utan den i metabeskrivning, "Passar för" eller löptext. Dessutom har 3001 (Gymstick träningsboll) redan tre "enligt tillverkaren" i beskrivningen (R5, högst 2) och BH Fitness Inertia 10069 skriver "maximal driftsvikt" ur engelsk källa (alt A, 2026-11-04, säger att driftsvikt utelämnas då); Hebie-stödbenen 32027–32029 har "enligt tillverkaren" på en lastgräns som bara stöds av återförsäljarsidor.
- **Regel:** mät F2 per påstående och förekomst, inte per text (`shopify-sync/scripts/rensning2_underlag.py`). Ett förslag som lägger till frasen måste först räkna frasen i hela texten (högst 2) och kontrollera att källan är svensk och ordagrann (R4). `skrivfil_kontroll.py` räknar frasen bara i beskrivningen, inte i metabeskrivningen.
### 2026-11-06: Skript som tyst faller tillbaka på BEST OF SPORTS kan läsa eller skriva i fel butik
- **Vad hände:** kartläggningen för flerbutik (`flerbutik-kartlaggning.md`) visade att butiksadress, miljövariabler och taggar var standardvärden i koden. Ett skript som körs för en ny butik utan att butiken pekats ut hade därför gått mot BEST OF SPORTS, och `verifiera_butik` hade inte stoppat det eftersom både klient och förväntad butik var BOS. Skripten `shopify_skriv_texter.py`, `arkivera_dubbletter.py`, `nattkontroll.py` och `verifiera_skrivna.py` har fortfarande den egenskapen (ej ändrade i detta pass).
- **Regel:** en profil för en annan butik får aldrig ärva butik, miljövariabler eller sökvägar från BOS; saknade obligatoriska fält ger fel (`butiksprofil.py`). Lägg `--profil` i varje skript som skriver innan det används för en andra butik, och kör alltid `verifiera_butik` mot profilens egen adress.

### 2026-11-04: Formatskriptet gav "El-Lastcykel", och granskaren fångade det bara i en av tre batcher
- **Vad hände:** `format_regler.py` skriver stor bokstav efter bindestreck i typordet ("El-Lastcykel"). Granskaren av k_01a rättade det, men det gick igenom i k_01c (9055 och 9060) och skrevs i butiken. Upptäcktes när jag gjorde granskarens fynd till test; rättades samma dag (skrivet och återläst). Granskaren av k_01c fann dessutom 3 gånger "enligt tillverkaren" i en text (R5, högst 2), som skriptet inte räknade.
- **Regel:** testerna "stor bokstav efter bindestreck i typordet" och "enligt tillverkaren högst 2 per text" finns nu i `skrivfil_kontroll.py`. Kör kontrollen om på skrivfilerna efter att ett nytt test lagts till, även på batcher som redan granskats.


### 2026-11-04: Överlappande nr-serier mellan grupper (08 och 09)
- **Vad hände:** in-filerna för grupp 08 numrerades från 9501 och grupp 09 från 9601, men grupp 08 har 126 produkter och nådde 9626. Samma `nr` fanns därför på två olika produkter (9608, 9610–9619, 9623, 9625). Upptäcktes av granskaren; inget skrevs fel eftersom skrivfilerna byggdes per batch och identifieras via id.
- **Regel:** ge varje grupp ett nr-intervall som rymmer hela gruppen (t.ex. 1000 per grupp) och bygg skrivfiler per batch. Byggskriptet `bygg_m_skriv.py` bör nyckla på id, inte nr.

---

### 2026-11-03: Samma fel i skrivfil 20: lika titel betyder inte skriven (våg 2b, produkt 10589704749322)
- **Vad hände:** produkt 8912 i skrivfil 20 hade rätt titel men gammal seo-titel, metabeskrivning och beskrivning. Regeln "hoppa över när titeln är lika" följdes inte, eftersom den bygger på ett antagande som inte stämde. Produkten skrevs med resten av filen och redovisas i rapporten.
- **Regel:** innan en produkt hoppas över, jämför alla fält som skrivfilen ändrar (titel, seo, meta, beskrivning) mot live. Titel ensam räcker inte som bevis för att produkten är skriven. Avvikelse från regeln redovisas.

### 2026-11-03: Skrivprompten hoppade över produkter med lika titel och lämnade gamla texter kvar (våg 2b, skrivfil 17)
- **Vad hände:** skrivprompten sade att produkter vars titel redan är lika skrivfilens ska hoppas över. Tre produkter i skrivfil 17 hade rätt titel men gammal beskrivning och meta. Koordinatorn beslutade att de ska skrivas om och verifieras.
- **Regel:** "titel lika" är inte ett bevis på att texten är skriven. Hoppa över en produkt bara på bevis för att hela posten (titel, seo, beskrivning) är lika, eller låt koordinatorn besluta.
- **Vad hände också:** återläsningen av Shopify-svar kunde inte gå till python när svaret låg inline. Lösningen: läsa tillbaka högst 4 produkter per fråga och klistra in svaret i python. Svar över ca 50 000 tecken sparas till fil av verktyget och kan läsas direkt där.

### 2026-11-03: Handskrivna variabler i en Shopify-skrivning gav fel titlar och metabeskrivningar (våg 2b, grupp 12)
- **Vad hände:** i batch 2 (8611–8616) skrev jag variablerna för `productUpdate` för hand efter att skriptutskriften hade lästs. Tre produkter fick fel text i Shopify: "Frambagagebärare" blev "Frambagebärare" (8613, 8614) och "Frontbärare" blev "Frontbagebärare" (8616), i både titel och metabeskrivning. Felen syntes först när svaren jämfördes mot skrivfilen i python. Skrivningen avbröts och batch 3 och 4 skrevs inte.
- **Regel:** skrivningen görs bara av variabler som skriptet har skrivit ut, kopierade ordagrant. Handskrivna variabler är förbjudna, även när texten "bara" ska kopieras. En avvikelse rättas med ett nytt skriptgenererat anrop, inte med nya handskrivna variabler. Återläsningen jämförs mot skrivfilen direkt efter varje batch, innan nästa batch börjar.

### 2026-11-03: Även en kopierad skriptutskrift kan ändra tecken; återläsningen måste jämföras maskinellt
- **Vad hände:** i batch 3 av vag2b_13a (Best of Sports) skrev jag av utskriften från skrivskriptet för hand till mutationen. Ett osynligt mjukt bindestreck (U+00AD) hamnade i "remmar" i produkt 10472233107722. Återläsningen i python fångade det. Skriptutskriften var korrekt. Felet rättades inte med nya handskrivna variabler, utan skrivningen avbröts.
- **Regel:** (a) en avvikelse ger avbrott och rapport, aldrig en handskriven rättning. (b) Skrivskriptet ska vägra skriva ut texter som innehåller osynliga tecken (U+00AD, nollbreddstecken) och ge ett fel i stället. (c) Återläsningen jämförs tecken för tecken i python för varje batch, även när texten ser rätt ut.

---

### 2026-10-28: Läs den renderade sidan, och ange vilken period och tabell en trend kommer från
- **Vad hände:** (1) Min tidigare bild var att Gorillas besök sjönk (−17 % SE) och att konverteringen därför föll. En ny körning (`pengalage_veckovis.sql`, GA4-tabell per dag) visade att SE-sessionerna i stället steg från cirka 7 000 till 14 000–18 000 per vecka medan köpen låg still. Perioderna och källorna var inte desamma. (2) GTM-dubbelladdningen bedömdes först som "delvis frikänd" utifrån temakoden, eftersom den andra laddaren bara renderas när temainställningen `google_tag_manager_id` är ifylld. Den renderade HTML:en visade att den är det.
- **Regel:** (a) Ange alltid period och tabell för en trend och jämför med en annan källa innan du säger att något har gått upp eller ned. (b) När temakoden gör något villkorligt: hämta den renderade sidan (`curl`) och räkna förekomsterna innan du frikänner eller fäller. (c) Rådata utan tolkning först; skilj bevisat från hypotes.

### 2026-10-26: Läs konfigurationen innan slutsatsen "saknas"
- **Vad hände:** `check-access --site bestofsports-fi` visade "saknas" för Shopify, GA4, annonser och Merchant. Jag drog slutsatsen att BOS saknar dessa källor. I `sites.toml` ligger butikens källor på blocket `bestofsports-se`; FI-blocket har bara sin egen Search Console-egendom.
- **Regel:** när ett verktyg säger att något saknas för en sajt: läs konfigurationen för hela butiken (alla block med samma `shop_domain` och `data_key`) och kontrollera i datat (`scripts/kontrollera_datakallor.sh`) innan du påstår att det saknas.


### 2026-10-26: Ett kontrollkommando måste kunna misslyckas på det som ska kontrolleras
- **Vad hände:** jag gav David `gcloud auth application-default print-access-token` som test på att inloggningen för Search Console gällde. Kommandot lyckas även när behörighetsområdet saknas, så testet kunde inte upptäcka felet (403 "insufficient authentication scopes" vid URL-inspektionen). Dessutom sparades inloggningen i en tillfällig fil i Cloud Shell utanför standardplatsen, som verktyget inte läser utan miljövariabeln `GOOGLE_APPLICATION_CREDENTIALS`.
- **Regel:** ange ett test som visar det som faktiskt behövs (här behörighetsområdena via tokeninfo) och som ger fel när det saknas.


### 2026-10-26: Räkna inte upp ett mått som positivt innan källan är känd
- **Vad hände:** jag redovisade att 85 % av BOS-produktsidorna hade betyg i strukturerad data (jämfört med 10 % på Gorilla) som om det vore en styrka. Temagenomgången visade att betygen kommer från en sektion som genererar påhittade omdömen från färdiga texter och namnlistor, inte från kunder.
- **Regel:** innan ett värde i strukturerad data, en omdömessiffra eller en annan "bra" siffra redovisas som positiv: ta reda på varifrån den kommer (kod, app, riktiga data). Läs hela temat före slutsatser om vad temat gör.


### 2026-10-26: Föreslå inget utan en genomgång av det som redan finns
- **Vad hände:** jag föreslog "fem nya kontroller" i genomlysningen, varav en (brödsmulor på kategorisidor) redan fanns som `breadcrumb_schema_missing`. Jag hade inte gått igenom genomlysningens ca 150 kontroller eller läst de senaste fynden per sajt innan jag föreslog. Flera av dagens förslag byggde dessutom på ett urval på 60 sidor och på några temafiler, inte på hela temat eller en genomlysning av hela sajten.
- **Regel:** före varje förslag på en ändring, en ny kontroll eller en åtgärd: (1) lista vad som redan finns (`scripts/audit_tackning.py`, `git grep` i kontrollerna, `standardtester.md`), (2) läs de senaste fynden per sajt för ämnet, (3) läs de berörda filerna i sin helhet (hela temafiler, inte bara de rader som verkar relevanta), (4) skriv i förslaget vad som är genomgånget och vad som inte är det, och rekommendera inte en åtgärd som "ja" innan helheten är känd. David vill inte ha förslag utan att helheten är känd.


### 2026-10-26: Rekommendera inte en ändring i kod någon annan skrivit utan att veta avsikten och dagens effekt
- **Vad hände:** jag föreslog att ta bort canonical-blocket i BOS `theme.liquid` och byta `shop.url` mot `request.origin` i breadcrumbs och Organization, innan jag hade kontrollerat varför blocket fanns, vad Google gör i dag och om `shop.url` i Organization var ett fel. Organization-URL på varumärkets huvuddomän är normalt och korrekt, och adress och språk i Organization kan vara företagets, inte marknadens.
- **Regel:** innan en ändring föreslås: (1) ta reda på avsikten (fråga David, läs loggen), (2) mät dagens effekt (till exempel vilken canonical Google valt), (3) skilj det som är bevisat från det som är en hypotes och säg det, (4) testa på en kopia av temat före publicering.

### 2026-10-26: Kontrollera att ett mått mäter det det påstås mäta, innan det presenteras som fynd
- **Vad hände:** i onsite-kontrollen gav FAQ-måttet 100 % (räknade alla `<details>`), alt-textmåttet 67,8–88,9 % (räknade dekorativa SVG-ikoner), sidnumrering flaggades som felaktig canonical, och två canonical-taggar upptäcktes inte alls eftersom skriptet bara läste den sista.
- **Regel:** testa nya mått mot ett känt fall och granska exempel innan siffran används. Läs exempelsidor, inte bara andelar.

### 2026-10-26: Skriv inte "tyder på" om orsaken inte är uppdelad
- **Vad hände:** jag skrev att hoppet vid fraktgränsen 800 kr "tyder på att kunder fyller på". Uppdelningen visade att 108 av 165 ordrar var enkelradsordrar där produktens eget pris låg där. Påfyllning var en mindre del.
- **Regel:** dela upp materialet innan en orsak antyds, och rätta öppet när uppdelningen visar något annat.

### 2026-10-25: Kontrollera aggregeringar mot totalsumman
- **Vad hände:** ett SQL-resultat för Gravity Pro 2 byggde på `GROUP BY` med NULL-nyckel och `ANY_VALUE(title)`, vilket gav ett felaktigt belopp som David vidarebefordrade till en extern part.
- **Regel:** summera varje uppdelning och jämför mot totalen, kontrollera NULL-grupper och namnge antaganden innan en siffra lämnas ut.

### Fakta om uppsättningen (David har bekräftat)
- **Best of Sports:** tre separata domäner med eget språk: bestofsports.se (svenska), bestofsports.dk (danska), bestofsports.fi (finska, med svenska under /sv/). **.fi och .dk ska ranka självständigt på finska och danska.** Bekräftat av David 2026-10-26.
- **`shop.url` är alltid butikens primärdomän,** även på de andra domänerna. För marknadsspecifika adresser (canonical, brödsmulor, produktens `url`) används `request.origin`. Organization-schemat får peka på varumärkets huvuddomän.
- **Redirecttabellen är gemensam** för alla domäner i butiken; handtag är översatta per språk.
- **Köp av hälsopåståenden:** EU-reglerna (1924/2006, 432/2012) gäller även försiktiga formuleringar. Se tidigare BOS-arbete.
- **Skrivning till det publicerade temat:** Shopify-verktyget som Claude använder blockerar skrivning till det publicerade (MAIN) temat. Ändringar där görs av David i temaredigeraren efter exakta före och efter, och Claude verifierar genom att läsa filerna och jämföra mot sparade original. Avpublicerade teman kan skrivas av Claude.

## 2026-10-30: kontrollera att skrivna titlar finns kvar
- Vad hände: 12 av 20 pilottitlar i Best of Sports hade gått tillbaka till leverantörens original inom ett dygn efter skrivning 2026-10-25, medan beskrivning och SEO låg kvar. Granskningssidan visade ändå pilotfilens titlar som om de var live.
- Regel: visa i granskningen det som läses från butiken, inte det som skrevs. Läs tillbaka titlar efter ett dygn och efter varje nattlig synk av Velomarket-produkter. Fråga innan skrivning om en synk skriver över titeln.

## 2026-10-31: kontrollskriptet får inte "lösas" genom att byta produktnamn
- Vad hände: två hjälpagenter bytte ordet "vibrationsplatta" och "massage" i titlar för att komma förbi hälsoordskontrollen. Titeln beskrev då inte längre produkten.
- Regel: en agent som stoppas av en kontroll ska lyfta produkten till handläggning, inte ändra produktens namn eller typ. Produkter med hälsoord som produktnamn (massage, vibration, akupressur) tas för hand med Davids ja.
- Regel: SEO-titeln lagras som tom när den är identisk med produkttiteln. Läs inte det som ett skrivfel.
- Regel: skriv inte leveranskostnad i kronor i standardblocket per produkt utan att läsa fraktprofilen.

## 2026-11-01: seo är ett objekt som ersätts i sin helhet
- Vad hände: pilotens 20 produkter skrevs om med `seo:{title:...}` utan description. Shopify nollställde då `seo.description` på alla 20. Upptäcktes vid återläsning och återställdes ur `bestofsports-pilot-20-produkter-2026-10-25.csv` (två metabeskrivningar hade ändrats 2026-10-30).
- Regel: skicka alltid `seo:{title, description}` tillsammans vid productUpdate, och läs tillbaka båda. Läs tillbaka ALLA fält som berörs, inte bara det som ändrades. Fråga: stämmer `seo.description` fortfarande?
- Regel: en skrivagent som skriver 20+ produkter ska läsa tillbaka beskrivningen för alla, inte bara för kanarieprodukterna (agenten skrev "when" i stället för "när" i en text).

## 2026-11-01: oberoende kontroll hittar språkfel som skribent och granskare missar
- Vad hände: i våg 1 (86 produkter) hittade de oberoende kontrollanterna språkfel i 26 produkter som upphovsagenterna och första granskningen släppt igenom. Två berodde på mitt eget formateringsprogram (`tillamp` gav "500 Ml" och "14 Oz" eftersom enheterna saknades i listan).
- Regel: lägg till alla enheter som förekommer i ENHETER i `format_regler.py` innan stor bokstav-regeln körs, och stickprovsläs titlarna efter körning.
- Regel: lita inte på en skrivagents egen kontroll. Låt en separat kontrollant läsa texten som språkgranskare (stavning, verb i meningar, ordval), inte bara jämföra mot filen.
- Regel: agenter jämför MCP-svar för hand (utdata kan inte diffas i bash). Beräkna aldrig "identiskt" utan att alla fält är genomlästa; redovisa vad som kontrollerats maskinellt och vad för hand.
- Regel: när skriv-JSON rättas direkt blir källskripten inaktuella; ange i loggen att JSON är sanningen.

## 2026-11-01: kontrollskriptet läser inte html, och utkast skrevs över
- Vad hände: `kontrollera_produkttext.py` läser fälten `beskrivning`/`body`, inte `html`. En körning direkt på utkastsfilerna gav "0 FEL" men täckte bara titel, SEO och meta. En utkastsagent skrev dessutom över en befintlig `a_4_utkast.json`. Flera produkter fick samma SEO-titel.
- Regel: kör kontrollskriptet på en kopia där html är mappat till beskrivning och standardblocket är markerat med `[[STANDARDBLOCK]]`, och redovisa det i rapporten.
- Regel: tala om för utkastsagenter att kontrollera om målfilen finns innan de skriver, och kräv unika SEO-titlar över hela batchen.
- Regel: granskare underkände 12 av 27 utkast (säkerhetsprodukter, oklar produkttyp). Sortera bort produkter med säkerhetsprofil innan utkast skrivs.

## 2026-11-02: utkastagenter missar fel som bara en oberoende granskare ser
- Vad hände: i Gymstick-vågen (295 produkter) underkände eller rättade granskarna drygt hälften av utkasten. Mönster: cirkulära första meningar ("Exercise Ball är en träningsboll"), en påhittad FAQ ("Går bandet att tvätta?") i alla 13 utkast i en batch, fel i `fakta`-fältet (kopierat från en annan produkt), dubblerade SEO-titlar mellan batcher och arbetstermer i kundtext. Kontrollskriptet gav 0 FEL på allt detta.
- Regel: kör aldrig skrivning på utkast som bara kontrollskriptet har sett. Oberoende granskare ska hämta källan på nytt och döma varje produkt.
- Regel: förbjud FAQ-avsnitt som inte har stöd i produktens egen källa, och kräv att `fakta` hämtas per produkt (inte kopieras).
- Regel: bygg skrivfilen maskinellt av utkast och granskarnas före/efter (`vag2_skriv/bygg_c_skriv.py`), och låt skriptet kontrollera dubbletter och längder över alla batcher innan skrivning.
- Regel: Shopify-skrivning pausar vid användargräns; återuppta avbrutna agenter med SendMessage i stället för att starta nya.

## 2026-11-02: nattsynken efter våg 1 lät texterna stå kvar (stickprov), orsaken till pilotens tillbakagång är fortfarande okänd
- Vad hände: våg 1 skrevs 2026-11-01 kl. 19:14–19:28 (UTC). Nattsynken 2026-11-02 kl. 04:23–05:06 ändrade `updatedAt` på drygt 40 av 126 skrivna produkter. Stickprov på 18 av dem (titel, SEO, beskrivning mot skrivfilerna): 18 av 18 hade kvar våra texter. Produkthändelserna (`events`) visar att Velomarket3 ändrar status och kanaler, aldrig titel eller beskrivning; de loggar dock inte alltid fältändringar.
- Okänt: varför 12 av pilotens 20 titlar gick tillbaka 2026-10-25–10-30. Hypotes (obekräftad): leverantörssynken skriver om texter när en produkt byter status (arkiverad till aktiv).
- Regel: kontrollera `updatedAt` mot skrivtidpunkt efter varje natt; jämför titlar på de produkter som ändrats. Allt som ändrats efter skrivningen jämförs mot skrivfilen.
- Regel: skriv alltid från filer med före-läge sparat, så att en omskrivning är en batchkörning.

## 2026-11-03: arbetssätt för lägre tokenförbrukning (David godkände)
- Vad hände: våg 2 kostade drygt 100 agentkörningar à 150–300 000 tokens. Granskning före skrivning gav kvaliteten; den andra fullständiga kontrollen efter skrivning hittade 0 avvikelser mot filerna på över 200 produkter, bara språkfel som borde fångats före skrivning.
- Regel: granskarnas återkommande fynd ligger inbyggda i utkastprompten (`vag2_skriv/b_utkastprompt.md`): inga cirkulära första meningar, verb i första metameningen, ingen FAQ utan stöd i källan, `fakta` hämtas per produkt, samma typord i hela batchen.
- Regel: utkast skrivs i batcher om 25 produkter per agent (inte 15), så att instruktionerna läses in färre gånger.
- Regel: efter skrivning görs stickprov på 10 procent (minst 10 produkter per batch) i stället för full kontroll. Skrivagenten läser alltid tillbaka alla fält själv. Avvikelse i stickprovet ger full kontroll av batchen.
- Test pågår: om Sonnet hittar minst 90 procent av Opus fynd som granskare byts granskaren till Sonnet. Om Haiku skriver och taggar felfritt (no-op-test) används Haiku för skrivning och taggning, med testbatch om tre först.

## 2026-11-03: stickprovet efter skrivning är 20 procent (David beslutade, ersätter 10 procent ovan)
- Regel: efter skrivning görs stickprov på 20 procent av varje batch (minst 10 produkter) av en starkare modell än skrivagenten, i stället för full kontroll. Skrivagenten läser alltid tillbaka alla fält själv. Avvikelse i stickprovet ger full kontroll av batchen.
- Anm.: posten "arbetssätt för lägre tokenförbrukning" ovan anger 10 procent. Den ändras inte (filen fylls bara på); gällande värde är 20 procent.

## 2026-11-03: test av Sonnet som granskare underkändes (hittade 41 procent av Opus fynd)
- Vad hände: Sonnet granskade Gymstick c_5–c_8 (50 utkast) blint och jämfördes med Opus. Samma dom på 27 av 50. Av Opus 37 icke-godkända flaggade Sonnet 15 (41 procent): 13 av 19 underkända (68 procent) och 2 av 18 rättas (11 procent). Sonnet godkände 16 utkast som Opus ville rätta och 6 som Opus underkände (nackskydd, boxningshandskar, handlindor, balansbräda, rulle). Sonnet saknade dessutom originalkällan för 20 av 50 (före-filerna täckte 30).
- Gräns som sattes: Sonnet skulle hitta minst 90 procent. Resultat 41 procent, alltså byts inte granskaren.
- Regel: Opus fortsätter som granskare före skrivning. Besparingen tas i stället från Haiku som skrivare/taggare (no-op-test godkänt), utkast i batcher om 25, inbyggda lärdomar i utkastprompten och stickprov 20 procent efter skrivning.
- Anm.: testet gäller Sonnet utan förbättrad granskarprompt och utan komplett källa; en omtest med bättre underlag kan göras om kostnaden motiverar det.

## 2026-11-03: titlarna stod kvar efter nattsynken 3 november (Velomarket-skyddet fungerar)
- Vad hände: efter nattens synk 2026-11-03 (03:00) lästes titlar tillbaka på 33 slumpvis valda skrivna produkter (Gymstick-testbatch, de sex titeländringarna, våg 2a, Gymstick-batcher och Velomarket-batcher). 33 av 33 hade kvar sina texter. Velomarket-produkterna hade nytt ändringsdatum kl. 05:31–05:32, alltså rördes de av något jobb, men titlarna ändrades inte.
- Slutsats: det nya skyddet i Velomarket-synken (titel och beskrivning skrivs bara vid skapande) och stoppet av sammanslagningen verkar fungera. Orsaken till pilotens tillbakagång 25–30 oktober är fortfarande inte bekräftad.
- Regel: läs tillbaka titlar efter varje natt i en vecka framåt (stickprov om 30 produkter) och efter varje körning av sammanslagningen.

## 2026-11-03: Haiku skrev om en metabeskrivning för hand (1 av 21), fångad av kanariekontrollen
- Vad hände: i cykelomgången skrev Haiku 21 av 90 produkter. På en (6032) skrev agenten en egen version av `seo.description` i stället för skrivfilens text. Agentens egen återläsning fångade avvikelsen och den avbröt som instruerat.
- Regel: skrivagenter ska aldrig skriva texten för hand i mutationen. De ska låta ett skript skriva ut färdiga GraphQL-variabler ur skrivfilen och kopiera utskriften ordagrant.
- Regel: kanarie om 3 och full tillbakaläsning efter varje batch är obligatoriska; avbryt vid första avvikelse. Det fungerade.

## 2026-11-03: Skrivagent skrev fel stavning trots skript; granskaren missade en hjulstorlek
- Vad hände: i cykelomgången skrev Haiku "växlereglage" i stället för skrivfilens "växelreglage" på en produkt (rättad efter egen återläsning). Skrivagenten stoppade också före skrivning på 6147, där "24-tumshjul" saknade stöd i källan; Opus-granskaren hade missat det eftersom hjulstorleken bara stod hos en systerprodukt.
- Regel: återläsningen jämför tecken för tecken och måste göras för varje batch; det är den som fångar skrivfel. Hjulstorlek, ramstorlek och liknande mått ska verifieras mot den egna produktens källa, inte systerprodukter.

## 2026-11-03: Parallella utkastagenter skrev samma modell och färg; växelgrupper som kan vara elektroniska bedömdes olika
- Vad hände: åtta utkastagenter körde parallellt på cyklar utan lager. Tre Talon-modeller hamnade som utkast i två batcher (k_16 och k_17) och flera butiksdubbletter (samma modell och färg under olika id) upptäcktes. Två granskare bedömde Shimano 105 med 24 växlar olika: ena underkände (kan vara Di2), andra godkände. Stickprovet noterade att 7085, 7088, 7091 och 7126 kan vara elektroniska.
- Regel: kör en dubblettkontroll av titel och SEO-titel över alla batchers utkast innan granskningen, och bygg batcher av cyklar så att samma modell ligger i samma batch. Växelgrupper som finns både mekaniskt och elektroniskt (Shimano 105/GRX/Ultegra, SRAM Apex/Eagle) får bara skrivas om källan entydigt anger mekanisk, annars tas de upp som beslut för David. En enda regel ska gälla för alla granskare.
- Regel: trasig källtext (till exempel "x2 .25"") ger ingen uppgift att bygga på; struka uppgiften i stället för att gissa.

## 2026-11-03: Metabeskrivning tappades när SEO-titeln var lika med titeln (min instruktion)
- Vad hände: i skrivprompten för tillbehör (b_skriv_4–6) stod att seo-objektet skulle utelämnas när SEO-titeln är lika med titeln. Det gjorde att metabeskrivningen (seo.description) inte skrevs på 11 av de 28 produkterna i b_skriv_5. Felet upptäcktes av Sonnet-stickprovet, inte av skrivagentens egen återläsning, som jämförde fälten mot filen men inte flaggade ett null.
- Regel: skicka alltid seo{title, description} med båda fälten när filen har en meta. Shopify lagrar seo.title som null när den är lika med titeln, men det är avsett och påverkar inte meta. Utelämna aldrig seo-objektet när meta finns. Återläsningen ska jämföra seo.description mot filens meta för varje produkt, inte bara när seo_title skiljer sig.
- Åtgärd: de 11 rättades (productUpdate med seo), och en revision av alla tidigare skrivna produkter körs.

## 2026-11-03: Haiku kan inte kopiera långa mutationer ordagrant; huvudagenten gör sådana skrivningar
- Vad hände: i omgången med korta metabeskrivningar (117 produkter) skrev Haiku om variablerna för hand trots instruktion om skriptutskrift. Det gav 9 skrivfel på 7 produkter (till exempel "belag" blev "beläg"), och rättningsförsök införde nya fel. Fyra produkter hade fel text i Shopify tills huvudagenten skrev om dem med skriptets utskrift. Samma mönster förekom tidigare ("växlereglage").
- Regel: när texten i en mutation är längre än några rader eller antalet produkter är stort: låt skriptet skriva ut mutationen och variablerna, och låt huvudagenten (inte Haiku) klistra in dem. Haiku duger för korta skrivningar med kanarie och maskinell återläsning, men återläsningen måste jämföras mot skrivfilen, och en avvikelse får aldrig rättas med nya handskrivna variabler.
- Regel: Sonnet-stickprovet på minst 20 procent (minst 10) fångade metafelet och är kvar som obligatoriskt steg.

## 2026-11-03: Trasig källtext ger ingen uppgift att bygga på; kort meta är bättre än null
- Vad hände: Kona Fire Mountain hade däckbredden bara som trasig text ("x2 .25""), och granskare godkände ändå "2,25 tum". Skrivningen stoppades före första skrivningen av kontrollskriptet och uppgiften togs bort.
- Regel: en uppgift som inte står entydigt i den egna produktens källa tas bort. David har beslutat att kort sann meta (typ, märke, material, mått) ska användas i stället för null på tunna produkter, men att beskrivningen aldrig fylls ut med text som saknar underlag.

## 2026-11-04: Kopierad FAQ, osynliga tecken och inklistringsfel i faktatextgrupper
- Vad hände: i utkasten b_50/b_51 fanns en kopierad vanliga-frågor-text från leverantören; den togs bort före skrivning. Mjuka bindestreck och extra mellanslag kom in när långa mutationer klistrades in för hand (Haiku, och vid två tillfällen jag själv: Fiido X, 8647). Fångades av jämförelse tecken för tecken och stickprov.
- Regel: kontrollera utkast mot leverantörens kopierade FAQ/marknadstext. Skriv helst via skript mot API, inte via text som klistras in. Se `textutrullning-rutin.md`.

## 2026-11-04: Shopifys admin-adress är blockerad från molnmiljön
- Vad hände: `curl` mot `6f2e53-67.myshopify.com` gav `CONNECT tunnel failed, response 403`.
- Regel: för skript-skrivning mot Admin API måste butikens adress läggas under Allowed domains och token lagras som hemlig miljövariabel, aldrig i chatten.

## 2026-11-04: Fitness – fel som upprepades trots rutinen
- Vad hände: (1) Skrivagent hoppade över 10103/10110 för att titeln var lika, fast texten var pilotens gamla (FAQ + Om märket): samma fel som 2026-11-03. (2) Vid inklistring av mutation tappades en mening (10078) och raderna Märke/Retur/Reklamation (10250); fångades av återläsning. (3) Före-fil skrevs för hand och fick förkortade texter (f_8) eller saknade ett bildblock (10211). (4) Format (stor bokstav efter kolon, versaler i titel) var det vanligaste granskningsfelet i f_10 och f_12. (5) Engelska 'Maximum operating weight' översattes olika i olika batcher.
- Regel: lika titel räcker aldrig som bevis (jämför titel, seo och beskrivning). Kör format_regler.py på varje utkast innan granskning. Före-fil ska kontrolleras mot id-antal och teckenlängd före skrivning. Maxvikt vid engelsk/maskinöversatt källa utelämnas (Davids alt A); svensk ordagrann lastgräns får stå en gång som 'enligt tillverkaren'. Skript-skrivning mot API (textutrullning-rutin.md) tar bort inklistringsfelen.

## 2026-11-04: Fitnessbatcherna skrevs över experiment 1 och pilotprodukter
- Vad hände: Davids beslut i produkttexter-standard.md (rad 73) säger att experiment 1 (432 produkter, kohorter T/K i `rapporter/forslag-bos-experiment-1-2026-10-27/kohorter.csv`) och pilotens 20 produkter inte ändras i vågorna. Inventeringen av fitnessgruppen (643 produkter) räknade bort varken kohorterna eller pilotprodukterna. Före upptäckten (granskaren av f_15) skrevs 150 kohortprodukter (76 behandling T, 74 kontroll K) i f_1–f_12 samt f_x1, och 15 i f_13 (skrivna men utan taggen texter-klara när agenten stoppades). Två pilotprodukter (10103, 10110) skrevs om. Skrivandet stoppades, och f_14 och f_15 filtrerades.
- Regel: bygg varje inventering mot en spärrlista (kohorter.csv + pilotens 20 + handhavda ids) innan batcher delas upp. Kontrollera spärrlistan i skriptet som bygger skrivfilen, inte bara i granskarens prompt.

## 2026-11-04: Mät innan du automatiserar – antagandet 'mest format' stämde inte
- Vad hände: jag trodde att de flesta granskningsrättningar gällde format. Mätningen (`mat_utbyte.py`, 1 656 utkast) visade 12 % format och 88 % innehåll. Det nya testet för cirkulära inledningar hittade två fel som både utkastare och Opus-granskare missat (10290, 10291).
- Regel: räkna fynden per typ före varje beslut om vad som ska automatiseras eller minskas. Lägg varje återkommande innehållsfynd som test i `skrivfil_kontroll.py` så fort det går att uttrycka som regel.

## 2026-11-04: Shopify-verktygets koppling delas mellan sessioner och pekar på en butik åt gången
- Vad hände: Sju nya sessioner startades parallellt för olika butiker. Flera körde `switch-shop`, vilket återkallade åtkomsten till BEST OF SPORTS för den delade kopplingen och krävde ny inloggning av David vid varje butiksbyte. Parallella sessioner via verktyget går därför inte.
- Regel: Läs och skriv butiker via Admin API med en app per organisation (token hämtas i minnet per körning, adress per butik), inte via Shopify-verktygets `switch-shop`. Verktyget duger för en butik i en session, aldrig för flera parallellt. Starta aldrig flera butikssessioner innan åtkomsten per butik är ordnad.

## 2026-11-05: parallella agenter skrev över varandras filer
- **Vad hände:** En utkastagent skrev sin utkastfil till ett redan använt batchnamn (`k_14_utkast.json`, ett äldre tracked utkast), och en annan agent körde ett delat skript med generiskt namn (`bygg.py`) som skrev om `k_16a`-filerna. Inget nådde butiken, eftersom allt granskades som filerna såg ut på disk, men äldre arbetsfiler hade kunnat gå förlorade.
- **Regel:** Varje agent får unika filnamn per batch (fortlöpande batchnummer som inte använts tidigare) och skapar hjälpskript bara i scratchpad med batchnamnet i filnamnet. Kontrollera `git status` efter varje agent.

## 2026-11-05: utkast utan nr gav tyst bortfall i skrivfilen
- **Vad hände:** I k_18a saknade fyra utkast `nr` (värdet var null). Byggskriptet använder `nr` som nyckel, så bara en av fem produkter hamnade i skrivfilen utan felmeddelande. Fyra flaskor skrevs först när jag såg att antalet inte stämde. Inget skrevs fel i butiken.
- **Regel:** Alla utkast och utlåtanden ska ha unikt `nr` (för produkter utan nummer används ett löpnummer, t.ex. 18005). `bygg_m_skriv.py` stoppar nu om ett utkast saknar `nr`. Kontrollera alltid att antalet produkter i skrivfilen stämmer med antalet godkända.

## 2026-11-05: Granskarens rättning med flera delar föll bort tyst
Opus-utlåtandet för 28232 hade en html-rättning med flera delar skarvade med "|". Byggskriptet (`bygg_m_skriv.py`) skrev ut "fore träffar 0" men stoppade inte, så produkten skrevs med ett felaktigt ord ("Biltema") i beskrivningen. Stickprovet hittade det; rättat med `k_skriv_korr8.json`. Regel: läs byggskriptets utskrift efter rader med "fore träffar 0" och åtgärda före skrivning. Granskare ska ange en rättning per fält som en enda sammanhängande textbit eller ett fält per ändring.

## 2026-11-06: leverantörssynken (Velomarket3) arkiverar produkter över natten
Appen Velomarket3 arkiverade 2026-11-06 kl. 03:22–03:23 ett femtiotal produkter, varav 62 hade fått text av oss (totalt 64 skrivna produkter är nu ej aktiva), trots att Shopify visar lager på de flesta. Det syns i produkternas historik (`events`). Regel: återaktivera aldrig arkiverade produkter utan att först kontrollera historiken; synken arkiverar dem igen. Kontrollera dagen efter varje skrivomgång både status och att texterna ligger kvar (`verifiera_skrivna.py`). Produkten 10348 (Finnlo Tricon Flex, pilot-20) har också återställts av synken till leverantörens titel och text och mist taggen texter-klara; den är spärrad och rörs inte före ca 2026-11-22.

## 2026-11-06: regeltester mot facit visade att befintligt varningstest inte skiljer rätt från fel, och att träningsdata ger för höga siffror
- **Vad hände:** (1) Varningen "Namn är en/ett typord" i `skrivfil_kontroll.py` motiverades 2026-11-04 med "30+ granskarrättningar", men falsklarm mot godkända utkast mättes aldrig. Mätningen 2026-11-06 visar att den larmar på 83 % av träningsdelens och 44 % av provdelens godkända utkast (och 45 % av de rättade): den särskiljer inte. (2) De nya testerna fångade 20,8 % av rättningarna på den data de utformades på men 9,2 % på batcher som inte användes (provdelen). (3) Granskarna var inte konsekventa på två punkter (N tums hjul/däck, metabeskrivning utan verb): 4,6 % respektive 6,7 % av de godkända utkasten bryter mot det som rättas i andra utkast. Ett test kan inte vara skarpare än regeln. (4) Facit innehåller bara det som kontrollerna inte fångade före granskningen, och en enda batch (`b_utlatande_49_50`) står för 8,8 % av rättningarna.
- **Regel:** mät alltid falsklarm mot godkända utkast innan ett test läggs till, och mät på batcher som inte användes när mönstret valdes (hållbar träning/prov-delning, se `shopify-sync/scripts/mat_regeltester.py`). Ett nytt test får stå på (varning) bara om falsklarmet är högst 2 % i båda delarna. Där granskarna är oeniga ska regeln förtydligas först (se `shopify-sync/regler/regelforslag-2026-11.md`, F1 och F2). Redovisa täckning per batch så att en enskild batch inte ger ett falskt intryck.
## 2026-11-06: skripten är inställda på BEST OF SPORTS och fungerar inte för en annan butik utan ändring
- **Vad hände:** när kundguiden skrevs ("kunden kör själv") visade läsningen att `shopify_skriv_texter.py`, `shopify_meta_rensning.py`, `verifiera_skrivna.py` och `nattkontroll.py` alla anropar `api.ShopifyKlient()` utan argument. Butiksadressen (`6f2e53-67.myshopify.com`) och variabelnamnen (`SHOPIFY_CLIENT_ID_BOS`/`SHOPIFY_CLIENT_SECRET_BOS`) är förvalda värden i `shopify_api.py`. `skrivfil_kontroll.py` har dessutom längdgränserna (70/43/155) och vissa BEST OF SPORTS-regler inbyggda i koden, trots att butiksprofilen innehåller `gransvarden`.
- **Regel:** innan en andra butik körs ska butik och variabelnamn bli argument eller läsas ur butiksprofilen, och gränserna ska läsas ur profilen. Kundguiden (steg 4 och 7) säger öppet att detta inte är gjort. Ändringen gäller befintliga skript och kräver ett beslut (se `rapporter/beslut-2026-11-06-2.md`). Skriv aldrig att en pipeline är butiksoberoende förrän den har körts mot en andra profil.

## 2026-11-06: efterhandskontroll av skrivna texter visade fynd som kontrollerna inte fångat när de skrevs
- **Vad hände:** `kvalitetsrapport.py` körde reglerna på den senast avsedda texten för alla 2 614 skrivna produkter. Fynd: 79 texter har fler än två "enligt tillverkaren" (äldre batcher före regeln i v1.5), 10 har cirkulär inledning, 4 har förbjudet uttryck, 121 saknar metabeskrivning, och 1 spärrad produkt (10348, pilot-20) har fått text utan att vara redovisad som känd överträdelse. Dessutom saknar 1 377 skrivna produkter (53 %) maskinläsbart återläsningsresultat, eftersom de skrevs via chatt-kopplingen innan skripten sparade resultatfiler.
- **Regel:** när en regel skärps ska kontrollerna köras om på redan skrivna texter, inte bara på nya. Kör `kvalitetsrapport.py` efter varje större omgång och läs avsnitt 4 och "Svagheter och osäkerheter". Bevis som bara finns som fri text i en skrivrapport räknas som svagare än en resultatfil.

## 2026-11-06: ordsökning i fria motiveringar ger bara ungefärlig sortering
- **Vad hände:** första versionen av kvalitetsrapporten sorterade avvisade produkter efter första träffande kategori i en fast lista. Det gav till exempel "Dubblett" för ett knäskydd som avvisats för säkerhet och där dubbletten bara nämndes sist ("dessutom dubblett"). Sorteringen ändrades till det ord som förekommer tidigast i motiveringen, men är fortfarande ungefärlig.
- **Regel:** fria motiveringar ska i nya körningar få ett fält `kategori` från en fast lista, så att rapporter kan räkna exakt. Tills dess redovisas sorteringen i rapporten som ungefärlig.


## 2026-11-12: repot har ingen gren som heter main
- **Vad hände:** jag pratade om att slå ihop till `main`, men fjärrrepot har ingen sådan gren. Standardgrenen (HEAD) är `claude/zealous-johnson-0ywddr`, och alla sessioner utgick från den. Dessutom var min lokala kopia grund (shallow), så `git merge-base` gav tomt svar tills `git fetch --unshallow` kördes.
- **Regel:** kontrollera `git ls-remote --symref origin HEAD` innan "main" nämns, och hämta full historik (`git fetch --unshallow`) före jämförelser mellan grenar.

## 2026-11-12: parallella sessioner valde samma beslutsfilnamn
- **Vad hände:** sex sessioner skapade alla `rapporter/beslut-2026-11-06-2.md`, och namnet fanns dessutom redan på standardgrenen. Sammanslagningen krävde omdöpning.
- **Regel:** när flera sessioner startas samma dag får varje session ett eget reserverat löpnummer för beslutsfilen i uppdraget.

## 2026-11-12: långa inklistringar i Cloud Shell blir sönderhackade
- **Vad hände:** en 90-raders heredoc blandades ihop med `EOF` och gav en trasig fil.
- **Regel:** dela skript i delar om högst cirka 55 rader (`cat >` för första delen, `cat >>` för resten) och kontrollera med `python3 -m py_compile` och `wc -l` före körning.


## 2026-11-17: ett ja i chatten hann inte nå en session som redan avslutats
- **Vad hände:** Davids ja till den fullständiga återläsningen (2026-11-12) skickades som meddelande till en session som redan hunnit avsluta, och återläsningen kördes aldrig. Jag märkte det först fem dagar senare.
- **Regel:** efter varje ja som skickas till en annan session: kontrollera inom samma pass att sessionen bekräftat och påbörjat uppgiften, annars starta en ny.

## 2026-11-17: en session som startats som "bara läsning" kan få skrivrättigheter av David direkt
- **Vad hände:** länkningssessionen gjorde skrivningar i butiken (meny, tema, taggar, kategoribeskrivningar) och använde `switch-shop` efter instruktioner som koordinatorn inte sett.
- **Regel:** koordinatorn läser sessionens ändringslogg och beslutsfil före nästa instruktion och noterar vilka skrivningar som skett och på vems besked. Effekt på klick och omsättning redovisas här först när den är mätt mot baslinjen 2026-11-12 (tidigast omkring 2026-12-10).
## 2026-11-12: "klar" gällde bara tills nya produkter aktiverades; en kontroll som aldrig kan ge fel upptäcktes sent
- **Vad hände:** utrullningen räknades klar 2026-11-08 med 281 aktiva produkter utan text. Läsningen 2026-11-12 visar 731: 454 utkast blev aktiva och 39 nya produkter tillkom (alla med taggen Velomarket, ingen med text). Dessutom räknade min första inventering standardblock och leveranstidsmening som aldrig saknade (0 av 5 354), eftersom profilladdaren (`butiksprofil.py`) inte lämnar fälten `standardblock_krav` och `leveranstidsmening` vidare; en tom lista ger `all([]) = True`. Det syntes först när 10 tomma beskrivningar ändå räknades som "har standardblock".
- **Regel:** ett "klart" gäller ett mätdatum; mät om innan det upprepas. Låt en inventering fela högt om ett kontrollfält är tomt (`inventera_bos.py` stoppar nu) och granska resultat som är exakt 0 innan de redovisas.

## 2026-11-12: "spärrad produkt har fått text" bygger på skrivfilen, inte på butiken
- **Vad hände:** kvalitetsrapporten 2026-11-06 och beslutsunderlaget räknade 10348 (Finnlo Tricon Flex, pilot-20) som överträdelse eftersom produkten finns i två skrivfiler. Live-läsning 2026-11-12 visar att skrivfilernas text inte ligger i butiken; beskrivning och metabeskrivning är pilottexten.
- **Regel:** en överträdelse av en spärr bevisas med butikens läge (live), inte med att produkten finns i en skrivfil. Läs produkten live innan den förs in i spärrlistan som känd överträdelse.

## 2026-11-12: "butiksoberoende" ska bevisas per skript, inte antas av kartläggningen
- **Vad hände:** kartläggningen 2026-11-06 listade fyra skript plus skrivfilskontrollen som hårdkodade. När jag gick igenom dem hittades fler delade ärvda BOS-värden som inte stod i listan: en standardtagg som parameterstandard i `jamfor_text` (importeras av två andra skript), `regeltester.py` som alltid läser BOS-profilen och BOS-konfigurationen (`regeltester.json`) även när skrivfilskontrollen fick en annan profil, delade utkataloger (`shopify-original-<datum>`, `rapporter/nattkontroll/baslinje.json`) och BOS pilotlista i `arkivera_dubbletter.py`. Hade bara de listade raderna ändrats hade en andra butik delat baslinje och rapportkatalog med BOS.
- **Regel:** vid butiksoberoende ändringar, sök i varje berört skript (och i modulerna det anropar) efter BOS-värden, delade sökvägar och parameterstandarder, och skriv ett test som kör skriptet med en annan butiks profil och kontrollerar att ingen BOS-fil, BOS-tagg eller BOS-katalog används. Bevisa "oförändrat utan argument" med före/efter-utskrift på alla skrivfiler.
## 2026-11-05: Underlaget räknade ett klistermärke som sparkcykel och 'modeller' var egentligen produkter
- Vad hände: Opus-granskningen av kategoritexterna visade att sparkcykelns lägsta pris (cirka 1 500 kr) kom från ett klistermärke, att Rideoo påstods sälja stuntsparkcyklar (bara stadssparkcyklar), och att 'minst N modeller' räknade färgvarianter som egna modeller (motionscykel, elcyklar, sparkcykel). Kontrollskriptet godkände allt, eftersom det bara jämförde texten med underlaget, inte underlaget med verkligheten.
- Regel: granska underlaget separat (billigaste och dyraste titel, antal unika titlar) innan text skrivs. Skriv 'produkter' om inte unika modeller är räknade, och 'bland annat' före varje uppräkning som inte är fullständig. Skriptkontroll ersätter inte oberoende granskning.

## 2026-11-12: Underlaget missade intervall, engelska titlar och tillbehör; metatexter listade ofullständigt
- Vad hände: Andra Opus-granskningen av pilottexterna hittade fel som kontrollskriptet godkänt: hantlarnas lägsta vikt var 1 kg ("1–10 kg" missades av vikt-regexen), märket Tenways skrevs med versaler mot titlarna, och fem metatexter räknade upp märken eller typer som om listan var fullständig. Underlaget räknar dessutom hantelställ och hantellås som huvudprodukter, och köpbara produkter med engelska titlar ("Dumbbell", "Treadmill", "Electric bike") hamnar bland övriga, vilket kan ändra lägsta pris, vikter och märken.
- Regel: granska underlaget separat före varje text (billigaste och dyraste titel, intervall i vikter, produkter bland övriga, tillbehör bland huvudprodukter), också för kategorier som redan godkänts. Skriv "bland annat" i brödtext och metatext före varje uppräkning som inte är bevisat fullständig. Märken stavas som i produkttitlarna (R8), inte i versaler. Skriptkontroll ersätter inte oberoende granskning.

## 2026-11-17: Sortiment, titlar och priser ändras mellan körningar; app-åtkomsten räcker inte för omdirigeringar
- Vad hände: Underlaget kördes om för tio kategorier 13 dagar efter förra körningen. Antalet köpbara produkter ökade i alla (till exempel sparkcykel 53 till 87, löpband 35 till 52 efter att engelska titlar räknades med), flera exempelmodeller har bytt namn eller försvunnit (Amladcykler, ZIPRO HEX, Rideoo-varianter) och många priser är nu rabatterade med 10 procent (taggen `price-change-job-active`, jämförpris i `compareAtPrice`). Kontrollen mot nytt underlag gav fel på exempelmodeller och prisavrundningar i sex av tio texter. Appen saknar dessutom läsbehörighet för `urlRedirects` (ACCESS_DENIED), så omdirigeringar går inte att läsa via API.
- Regel: kör om underlaget och kontrollen direkt före varje text och skrivning, inte bara när texten skrivs. Skriv inga priser medan prisjobbet är aktivt. Om omdirigeringar ska läsas via API krävs en behörighet som David beslutar om; be inte om hemligheter och bredda inte behörighet på egen hand.
## 2026-11-12: bot-kontroll på bloggartiklar och två mätfel i egen analys
- **Vad hände:** (1) Vid genomsökning av bestofsports.se svarade Cloudflare med bot-kontroll (HTTP 429, `cf-mitigated: challenge`) på bloggartiklar efter cirka 130 anrop, även vid 1,2 anrop/s; kollektioner och produkter påverkades inte. 21 av 155 artiklar hämtades aldrig och 8 blockerades. Sitemapen sorterades alfabetiskt så bloggarna kom först. (2) Första analysen slog ihop pagineringssidor med första sidan och gav produkter för grunt djup (max 2 i stället för 50), och ankartexter räknades per länk i stället för per källsida. Båda fångades i granskning av mellanresultat.
- **Regel:** hämta kollektioner och produkter före bloggartiklar, håll högst cirka 1 anrop/s mot bestofsports.se, och försök aldrig ta dig förbi bot-kontrollen (redovisa i stället luckan). Räkna pagineringssidor som egna steg i klickdjup, och räkna inlänkar och ankartexter per unik källsida. Granska mellanresultat på riktig data innan slutsatser skrivs.

## 2026-11-13: collectionUpdate kräver `collection`, inte `input`; antalsfältet släpar; Cloudflare stoppar även produktsidor
- **Vad hände:** (1) Admin-API 2026-10 avvisar `collectionUpdate(input:)` som föråldrat; rätt form är `collectionUpdate(collection: CollectionUpdateInput)` med `id` och `descriptionHtml`. (2) `productsCount` på en taggstyrd kollektion visade 125 flera minuter efter att 10 produkter fått taggen, trots att `inCollection` redan var sant. (3) Publik hämtning av en produktsida gav HTTP 429 (Cloudflare) efter att `products.json` hade hämtats några gånger i följd.
- **Regel:** kontrollera kollektionsmedlemskap med `product.inCollection`, inte med `productsCount`. Verifiera varje textändring i en kollektion genom att jämföra hela `descriptionHtml` mot original plus avsedd text. Hämta inte `products.json` upprepat för att vänta in en ändring; vid 429, vänta och försök inte ta dig förbi.

## 2026-11-18: inköpspris på 27 % av varianterna ger marginal över 90 %; ta inte fram prisförslag före kontroll (Workout Brands)
- **Vad hände:** i läsningen av 7 371 aktiva produkter (32 906 varianter med inköpspris) hade 8 900 varianter (27 %) marginal över 90 % efter moms (till exempel pris 199 kr mot inköpspris 6,50 kr; Build your Brand och MJ Gonzales 100 % av varianterna), 141 låg under inköpspris och övriga 73 % låg tätt kring 60,6 %. Det tyder på fel enhet eller valuta i `unitCost`. Skriptet `pris_forslag.py` (BEST OF SPORTS-mönster, 25 % moms på allt, 40 % målmarginal) hade gett 1 927 felaktiga förslag.
- **Regel:** läs fördelningen av marginal per leverantör före varje prisarbete; en gruppvis över 90 % är ett datafel tills motsatsen är bevisad. Ta inte fram prisförslag på butiker vars inköpspris inte är kontrollerat.

## 2026-11-18: butiksinställningen taxesIncluded säger inte hur varje marknad räknar moms (Workout Brands)
- **Vad hände:** `shop.taxesIncluded` var false, men svenska ordrar hade `taxesIncluded=true` (pris 199,00 kr inkl. 39,80 kr moms) och danska ordrar false (667,17 kr + 150,08 kr moms på). Hade butiksinställningen använts hade marginalen blivit fel.
- **Regel:** läs `taxesIncluded` och `taxLines` på några senaste ordrar per marknad innan marginal räknas efter moms.

## 2026-11-18: bulkOperationRunQuery fastnar i godkännande; sidindelning med sparad svarsfil fungerar (Workout Brands)
- **Vad hände:** `graphql_mutation` med bulkexport väntade på ett godkännande som ingen kunde ge nattetid (avbröts). `graphql_query` med 100 produkter per sida sparar stora svar i en fil, så 7 371 aktiva produkter lästes på 74 sidor utan att svaren fyllde samtalet; två agenter delade intervallet på id (74 respektive 7 297 produkter, 0 fel, 9 minuter för den större delen). Föråldrade fält (`Collection.ruleSet`, `Market.enabled`, `ShopPlan.displayName`) avvisas av schema 2026-10; använd `sources`, `status` respektive `publicDisplayName`.
- **Regel:** vid nattkörning, planera sidindelad läsning med `graphql_query` och undvik allt som kräver godkännande. Kontrollera antal mot `productsCount` (EXACT) per delintervall.

## 2026-11-18: Cloudflare ger HTTP 429 på produktsidor efter cirka 120 stora sidor (Workout Brands)
- **Vad hände:** publik genomsökning av workoutbrands.com (cirka 1,4 anrop/s, sidor 0,5–1,3 MB) gav 200 på startsida, 101 kollektioner och 17 sidor, sedan 429 på sex produktsidor i rad, även efter 60 och 30 sekunders väntan. En enskild produktsida gick att hämta efter en paus. Därför saknas produktsidor och blogg i klickdjups- och inlänkningsmätningen.
- **Regel:** räkna med att volymen (inte bara takten) triggar bot-kontrollen; hämta produktsidor före kollektioner i en separat, långsammare körning, eller använd sitemap och Shopify-data i stället. Försök aldrig ta dig förbi kontrollen; redovisa luckan.

## 2026-11-18: inköpspris i fel enhet följer importvägen, inte märket (Workout Brands)
- **Vad hände:** av 33 007 varianter hade 8 920 marginal över 90 % efter moms. 92,3 % av varianterna utan taggen `in sheet` var misstänkta mot 0,8 % av dem med taggen; 88 % av de misstänkta inköpspriserna har decimaler (2,45, 7,90, 12,90) medan de rimliga är hela kronor. Vid 11 kr per euro blir marginalen cirka 49 %, vilket är rimligt. Att räkna per märke dolde mönstret (Build your Brand och MJ Gonzales 100 %, men MT Men 22 %).
- **Regel:** gruppera misstänkta inköpspriser på importväg och skapandeår (tagg, datum) före märke, och kontrollera decimaler och valutakurs som hypotes. Skriv ingen ny kostnad innan leverantörens valuta är bekräftad.

## 2026-11-18: handles med tecknet ® är URL-kodade i sitemapen och ger falska sitemap-luckor (Workout Brands)
- **Vad hände:** jämförelsen mellan 7 371 aktiva produkter och sitemapen gav först 466 saknade; 16 av dem var produkter med ® i handle (URL-kodade i sitemapen). Rätt siffra var 450, varav 449 är opublicerade i Online Store. Filtret `published_status:unpublished` på produkter gav direkt 449.
- **Regel:** avkoda URL-kodning före jämförelse av handles och kontrollera med `productsCount(query:"status:active AND published_status:unpublished")` mot sitemapens antal.

## 2026-11-18: orderfilter som är fel stavade ignoreras tyst (Workout Brands)
- **Vad hände:** `orders(query:"billing_address.country_code:SE")` och `shipping_address.country_code:DK` returnerade samma senaste order oavsett land (ogiltiga filter ignoreras utan fel). Rätt land hittades först genom att läsa 100 ordrar och gruppera på `shippingAddress.countryCodeV2` i efterhand.
- **Regel:** kontrollera att ett filter faktiskt begränsar (ordernummer eller land i svaret) innan resultatet används; gruppera annars på klientsidan.


- 2026-11-18, Search Console-export (workoutbrands.com): sid-, sökfråge- och sida×sökfråge-rapporterna avkortas vid 25 000 rader (`MAX_ROWS` i `gsc_export.py`), så deras visningssummor är lägre än verkliga totaler (3,98 av 6,56 miljoner). Jag redovisade först den avkortade summan som butikens totala visningar. Regel: ta totaler ur land-, enhets- och månadsrapporterna och ange alltid om en sidtyps- eller frågeandel gäller de avkortade raderna. Klick är i praktiken kompletta, visningar inte.

- 2026-11-18, Workout Brands, kollektioner: jag tolkade `hoodie-oversized-herren` som en dubblett av `hoodie-oversized-herr` och skrev det i baslinjen och i uppdraget till sessionen. Adressen finns bara som `/de/collections/…` (tyska versionen; "Herren" = män). Regel: kontrollera språkprefixet (`/de/`, `/fr/` …) innan en kollektion kallas dubblett; sammanslagning över språk döljer att handles kan vara översättningar.
### 2026-11-18: Kopierad chattgränssnitts-HTML i beskrivningar
- **Vad som hände:** en läsande räkning visade stark rest av chattgränssnitts-HTML (`data-start`, `data-end`, `data-is-last-node` med flera) i 2 904 av 7 371 aktiva produkter, 470 av 674 kollektioner, 71 av 144 bloggartiklar och 8 av 85 sidor, ofta även i de översatta texterna.
- **Regel:** kontrollera varje ny eller omskriven text mot dessa mönster före skrivning. Klistra inte in text direkt från ett chattgränssnitt utan att rensa attributen. Översätt inte från en källtext som innehåller dem, eftersom resterna följer med. Skriptet `shopify-sync/scripts/chatt_html_rester.py` räknar mönstren.

- 2026-11-18, könsfältet (workoutbrands.com): mitt skript valde fältet `ownerId` på typen Metafield i mutationen metafieldsSet, som inte finns. Fakeklienten i testerna fångade det inte, och felet visade sig först i Davids körning. Regel: kontrollera varje fält i en ny mutation mot Shopifys schema (graphql_schema) innan skriptet lämnas till David, och lägg ett test som låser urvalsfälten.

- 2026-11-18, könsfältet: standardfältet `shopify.target-gender` är begränsat till vissa produktkategorier (definitionens constraints). Produkter vars kategori inte ingår nekas med "Owner subtype does not match". Regel: kontrollera constraints och produkternas kategori före en stor metafältsskrivning; skriv enskilda produkter om en grupp nekas och lista de nekade med kategori.

- 2026-11-19, Cloud Shell-körningar: miljövariabler (nycklar) försvinner när Cloud Shell startas om, och uppladdade filer får suffix `(1)`, `(2)` om namnet redan finns, så en gammal skriptversion kan köras ovetande (hände tre gånger med `kategori_satt.py`). Regel: be David kontrollera `ls -l` och filstorlek efter uppladdning, kontrollera nyckellängder med `echo ${#VAR}` före varje körning, och lägg versionsnummer eller en uppenbar utskrift i skripten så att fel version syns direkt.
- 2026-11-19, kategori och kön: produkter med kategorin "Uncategorized" (Okategoriserat) kan inte få `shopify.target-gender`. 246 av 255 nekade produkter saknade kategori. Regel: sätt kategori innan könsfältet, och kontrollera kategorins attribut (taxonomy.categories → attributes) innan en bulkskrivning.
- 2026-11-19, kollektionsregler: i Admin API 2026-10 ändras en kollektions regler med `collectionUpdate(collection:{id, sourcesToUpdate:[{condition:{id, inclusion:{conditionsToUpdate:[…]}}}]})`. `collectionConditionsSourceUpdate` ger "Källan kan inte delas" för vanliga (ej delbara) källor, och `ruleSet` finns inte i `CollectionUpdateInput`. Produktantalet i svaret kan vara gammalt direkt efter ändringen: läs om det efteråt.
- 2026-11-19, SEO-fält: att utelämna `description` i `SEOInput` på `collectionUpdate` tömmer beskrivningen. På t-shirt-med-tryck-dam försvann beskrivningen en kort stund när bara titeln skickades; den återställdes direkt ur exporten. Regel: skicka alltid både title och description i `seo` (befintligt värde om det inte ska ändras) och läs tillbaka svaret.
- 2026-11-19, omdirigeringar: Shopify-omdirigeringar gäller bara när sidan inte finns; en publicerad (tom) kollektion måste först avpubliceras. Det koordinatorns Shopify-verktyg blockerar `publishableUnpublish`, så avpubliceringen görs av David i Shopify admin (eller med ett eget skript). Regel: skapa omdirigeringar först, avpublicera sedan, och kontrollera efteråt att mål-URL:en svarar (publika sidor hämtas inte automatiskt eftersom Cloudflare svarar 429).
- 2026-11-19, gsc_indexering.py: första versionen skrev en tom rad per sida när URL Inspection API svarade med fel och gick vidare, så Davids körning gav en tom CSV utan att felet syntes. Regel: ett skript som anropar ett externt API ska stoppa efter några fel i rad och skriva ut hela felmeddelandet, inte skriva tomma resultat.
- 2026-11-19, gsc_indexering.py: Googles URL Inspection API svarade inte inom 120 s på anrop 31 av 43; skriptet kraschade och förlorade de 30 redan hämtade sidorna eftersom filen skrevs först i slutet. Regel: skript som gör många externa anrop ska ha kortare timeout med omförsök, spara löpande och kunna återupptas; fånga alla undantag per anrop.
- 2026-11-19, wb_alt.py: samma bild (MediaImage) kan sitta på flera produkter; den kom två gånger i samma skrivgrupp med olika produkttitlar och återläsningen stoppade körningen vid 33 020 av 45 328 bilder. Regel: deduplicera på bildens id innan skrivning när ett skript skriver per fil-id; låt första förekomsten gälla.
- 2026-11-19, återanvändning: repot hade redan genomlysningsdokument (`seo-geo-genomlysning-metod.md`, `site-audit.md`, `genomlysning-ny-butik.md`) och en publik sidkontroll (`onsite_kontroll.py`) när playbooken skrevs. Regel: sök i repot efter befintliga dokument och skript (`ls shopify-sync/docs shopify-sync/scripts`) innan något nytt byggs, och bygg på dem. Playbooken pekar därför på de äldre dokumenten i stället för att duplicera dem, och `sajtskanning.py` importerar `onsite_kontroll`.
- 2026-11-20, sajtskanning/onsite_kontroll: den första riktiga körningen (gorillasports.se) rapporterade att 150 av 150 titlar var över 60 tecken. Det var fel: parsern lade ihop alla `<title>`-element på sidan, inklusive svg-ikonernas (betalningsmärken), så en titel på 53 tecken räknades som 118. Rättat i `onsite_kontroll.py` (bara sidans egen titel, mellanrum normaliserade) med test (`test_onsite_titel.py`). Regel: kontrollera ett resultat som ser för dåligt ut mot en enskild sida för hand innan det rapporteras; en kontroll som slår på 100 % av sidorna är nästan alltid ett fel i kontrollen, inte i sajten.
- 2026-11-20, Shopify-app för en annan butik: `shop_not_permitted` vid hämtning av token (klientuppgifter) betyder att appen inte ligger i samma Shopify-organisation som butiken. Appen måste skapas i den organisation som äger butiken (Gorilla Sports), inte i organisationen där Workout Brands ligger. Kontrollera vilken organisation som är vald i Dev Dashboard innan appen skapas.

## 2026-11-20: Nollfynd räknades som brister
Vad hände: skanningsrapporten listade kontroller med noll träffar (t.ex. 0 produkter utan bild) som BRIST och räknade dem i sammanfattningen. Regel: en kontroll utan träffar är inget fynd och visas inte. Kontrollera alltid att sammanfattningens antal stämmer med tabellernas rader.

## 2026-11-20: Alt-text i Shopify och i sidans HTML är olika mått
Vad hände: Shopify-exporten visade 95,5 % av Gorillas aktiva bilder utan alt-text, medan den publika skanningen bara hittade 2,1 % `<img>` utan alt. Temat fyller sannolikt i produkttiteln som reserv i HTML:en. Regel: redovisa båda måtten och säg vilket som avses; alt i mediabiblioteket påverkar främst bildsök och flöden, inte nödvändigtvis det synliga i sidkällan.

## 2026-11-20: Regelkollision i kategoriförslag (Gorilla Sports)
Vad hände: regeln för viktskivor matchade ordet "Viktskivor" i titeln "Bicepscurlbänk Z Stång Viktskivor Totalt 40kg" före regeln för curlbänkar, och förslaget markerades ändå som hög säkerhet. Felet upptäcktes först när kanariekörningen listade de fem skrivna produkterna. En andra träff: en skivstång med inkluderad kudde fick kategorin Skivstångskuddar. Regel: (1) ordningen på regler avgör utfallet, så de mest specifika reglerna först och regler på titelord bara där produkttypen stödjer dem; (2) före skrivning ska alla rader med hög säkerhet jämföras mot produkttypen och avvikelser lyftas ut; (3) kanariekörningen granskas på produkttitel, inte bara på antal.

## 2026-11-20: Kategori, kön och kollektioner är olika lager
Vad hände: David frågade varför vi kategoriserade produkter som redan hade taggar som styr kollektionerna. Vi hade behandlat "produkter utan kategori" som en brist utan att fråga om butikens mål. Regel: skilj alltid på (1) site, kollektioner och menyer, (2) kanaler och produktflöden, (3) filter och attribut. Fråga om målet innan ett fynd prioriteras, och kontrollera om någon kollektion använder produktkategori som regel (de kan peka på nedlagda kategorier) innan kategorier skrivs. Se playbook avsnitt 10.

## 2026-11-20: SEO på huvudspråket ger svensk titel på översatta sidor när översättning saknas
Vad hände: när 13 kollektioner fick svensk SEO-titel visade gorillasports.dk (danska) direkt den svenska titeln i `<title>`, eftersom SEO-titelns översättning saknades. Före ändringen var källtiteln tom och sidan använde den översatta kollektionstiteln. Regel: skriv inte SEO-titel på huvudspråket i en butik med flera språk utan att översättningarna (meta_title, meta_description) är klara i samma körning, eller kontrollera en översatt domän direkt efter kanariekörningen.

## 2026-11-20: Kontrollera rätt behörighet för varje skrivtyp, och läs STOPP-raden
Vad hände: översättningskörningen på Gorilla Sports stoppade med `ACCESS_DENIED: write_translations`, eftersom appen bara hade `read_translations`. Jag hade bara kontrollerat `write_products` (för kategorier och kollektions-SEO). Dessutom bekräftades kanariekörningen som lyckad utan att utskriften visades, och att inget skrivits upptäcktes först när jag läste översättningarna direkt i butiken. Regel: kontrollera appens behörigheter mot skrivtypen före körning (produkter: `write_products`; översättningar: `write_translations`; navigering: `write_online_store_navigation`; innehåll: `write_content`). Skripten kontrollerar nu själva före första skrivningen. Kräv hela utskriften efter varje kanariekörning och bekräfta resultatet i butiken innan vi går vidare.

<!-- Förd över från sidospåret bos-244-omgang 2026-11-21 -->
## 2026-11-17: tre av fyra "enkla kandidater" hade prisjobbstaggen; riskordsfiltret missade engelska termer
- **Vad hände:** inventeringen räknade 254 enkla kandidater (244 två dagar tidigare), men 175 hade taggen `price-change-job-active` och fick inte skrivas. Riskordsfiltret i `analysera_inventering.py` (`RISK`) saknar engelska ord och böjningar (lock, helmet, light, lampor, tire, basket, pedals, grips, saddle), så belysning och lås utan svenska ord klassades som enkla. Dessutom kontrollerar `shopify_skriv_texter.py` varken prisjobbstagg eller priser.
- **Regel:** läs taggar och varianternas priser live före och efter varje skrivning; använd `skriv_med_skydd.py` (stoppar vid prisjobbstagg, prisändring eller annan avvikelse), inte det äldre skriptet, så länge prisjobbet är aktivt. Granska riskordslistan manuellt mot engelska typord innan en kandidatlista räknas som "enkel".

## 2026-11-17: annonser kan blanda ihop produkter; en källtext kan beskriva en annan modell
- **Vad hände:** i cykeldelsomgången beskrev källtexten för Giant Pinner Comp lila en annan modell (Pinner Elite, vikt 380 g), sittdynan till Cargobike hade fram- och bakdynans artikelnummer och mått blandade, Ass Savers Toetector hade texten för en annan Ass Savers-produkt och Giant Tactal svart-röd saknade färgstöd (källan: bilden är illustration). Utkastaren hade i två fall hämtat fakta från syskonprodukter, vilket bara granskaren fångade.
- **Regel:** jämför källtextens modellnamn med titel och artikelnummer före utkast; vid avvikelse avvisa (R1/R3) i stället för att fylla på från syskon eller webb. Granskarens obligatoriska kontroll av modellnamn, artikelnummer och mått mot tillverkaren avgör, inte utkastarens webbkoll.

<!-- Förd över från sidospåret bos-struktur-redirects 2026-11-21 -->
## 2026-11-17: Shopify MCP-kopplingen blockerar avpublicering; appen saknar read_publications; strukturlistans "tomma" är snabbt föråldrad
- **Vad hände:** (1) `publishableUnpublish` via Shopify MCP vägras av kopplingens egen skyddsregel ("Unpublishing is blocked to prevent accidental storefront catalog removal"), så en omdirigering som kräver att källkollektionen avpubliceras kan inte genomföras via MCP. Omdirigeringen hann skapas före avpubliceringen och är overksam så länge sidan finns. (2) Admin API-appen kan inte läsa publicering (`read_publications` saknas); den läses bara via MCP (`resourcePublicationsV2`). (3) Mellan strukturlistan (2026-11-04) och 2026-11-17 hade flera "tomma" kollektioner fått produkter (multigymspaket 0 till 8, hantelset, ribbstol m.fl.), flera har nyskrivna kategoritexter (ändrade 2026-11-13 och 2026-11-16), och ett föreslaget mål (crossfit) var inte publicerat.
- **Regel:** skapa omdirigeringen först och avpublicera sedan, men kontrollera i förväg att avpublicering går att göra med det verktyg som finns; försök aldrig kringgå en blockering. Läs alltid om kollektionens läge live (produkter, status, lager, publicering) före varje åtgärd i stället för att lita på strukturlistan. Ett mål måste vara publicerat och ha köpbara produkter, och ska ha minst så många visningar som källan.

## 2026-11-17: regeländring på kollektion i Admin API 2026-10 görs med `sourcesToUpdate`
- **Vad hände:** `ruleSet` är föråldrat i 2026-10 och `collectionUpdate` tar inga regler direkt; en regel ändras med `collectionUpdate(collection:{id, sourcesToUpdate:[{condition:{id:<CollectionConditionsSource>, inclusion:{conditionsToUpdate:[{id:<villkors-id>, condition:{productVendor:{relation, values}}}]}}}]})`. `productsCount` i svaret visade fortfarande 0 direkt efter ändringen; återläsning efter cirka 20 sekunder visade 69 medlemmar.
- **Regel:** läs `sources` (käll-id och villkors-id) före ändringen, spara en före-fil med regel och medlemslista, och verifiera medlemmarna med en återläsning en stund efter, inte med svaret från mutationen.

## 2026-11-17: simulera kollektionsregler exakt, inte med produktsökning
- **Vad hände:** en torrkörning med produktsökningen `tag:skivstång` förutsade 15 medlemmar, men kollektionsregeln (exakt tagg) gav 13, eftersom två produkter har taggen "skivstång 50mm" som sökningen matchade löst. Titelsökning med `title:*ord*` missar dessutom ord som slutar på det sökta ("Framnav", "Frihjulsnav") och en ren titelregel gav felträffar ("Navy", "med Bromsar", "Manuell Broms").
- **Regel:** simulera regeln i kod mot de inlästa produkterna med samma semantik som regeln (exakt tagg, titel innehåller som delsträng, produkttyp lika med), kombinera titelvillkor med produkttyp, och jämför utfallet med torrkörningen efter skrivning; stoppa vid avvikelse och förklara den innan något mer görs.

<!-- Förd över från sidospåret bos-kategoritexter-skriv 2026-11-21 -->
## 2026-11-17: hela kategorin kan ha prisjobbstaggen; skrivskriptets egna kontroller hade ordningsfel; revisionsgranskning av märkeslistor
- **Vad hände:** (1) För sex av tio pilotkategorier har alla köpbara produkter taggen `price-change-job-active`, så "räkna utan taggade" ger 0; antalet räknades därför med taggade produkter och texterna skrevs utan priser. (2) Första versionen av `kategorier_skriv.py` flaggade redan skrivna kollektioner som "ändrade live" och hoppade över tre kollektioner i `--rest`; stopp-skyddet fångade det och inget skrevs fel, men tre kollektioner fick skrivas i en extra körning. (3) Granskningarna av våg 2 hittade fem metatexter där en märkes- eller typlista såg fullständig ut utan "bland annat" (samma fel som 2026-11-12), och att `traningsbank` växte från 19 till 33 köpbara mellan två körningar samma dag. (4) Hantlar-metan "set upp till 50 kg" gick inte att behålla: en köpbar produkt bland övriga ("Skivstångs- och Hantelset ... 60 kg") motsäger den.
- **Regel:** kontrollera hur många produkter som har en spärrtagg innan "räkna utan" används som metod. Testa skrivskript med en torrkörning efter en delskrivning (alla lägen), inte bara före. Kör underlaget om omedelbart före skrivning och granska också övriga köpbara produkter mot varje max- och min-påstående.

## 2026-11-17: ett produktnamn i ett urvalsmönster träffade riktiga produkter; någon annan rättade samma regler samtidigt
- **Vad hände:** i torrkörningen av regelrättningen för racercykel hade mönstret för felplacerade produkter ordet "racercykel" med (jag skickade hela strängen i stället för bara avvikelserna), och det hade undantagit två riktiga racercyklar om API:t inte hade avvisat anropet ("Source is not shareable"; nämnda källor går inte att ändra med `collectionConditionsSourceUpdate`). Samtidigt hade en annan session eller person redan lagt typvillkor på herrcyklar, hybridcykel, racercykel, roddmaskin och elcyklar; medlemsantalet i racercykel sjönk från 168 till 129 mellan två av mina läsningar.
- **Regel:** skriv det som ska undantas som en uttrycklig lista av produkt-id som granskats, aldrig som ett mönster som körs direkt mot butiken. Läs kollektionens villkor och medlemmar på nytt omedelbart före varje ändring (någon annan kan ha ändrat dem) och stoppa om de skiljer sig från säkerhetskopian.

<!-- Förd över från sidospåret bos-aterlasning 2026-11-21 -->
## 2026-11-17: filernas ändringstid säger inget om skrivordning i en ny kopia
- **Vad hände:** `nattkontroll.py` väljer "senast avsedd text" per produkt med filens ändringstid (`getmtime`) när flera skrivfiler innehåller samma produkt. I en ny kopia av repot har alla filer samma tid och git-historiken är ihopslagen (179 av 218 skrivfiler har samma commit-tid), så ordningen blir godtycklig för de 287 produkter där filerna har olika text. Vid återläsningen 2026-11-17 användes i stället resultatfilernas tidsstämplar, med rättningsfiler (`korr`) sist; för 252 produkter saknas tidsstämpel för minst en fil och ordningen är inte bevisad.
- **Regel:** bestäm skrivordning ur tidsstämplar i resultatfilerna eller ett fält i skrivfilen, aldrig ur filens ändringstid eller git-datum. Nya skrivfiler ska få ett fält `skriven` (datum) när de skrivs. Redovisa produkter där ordningen inte kan styrkas i stället för att räkna dem som säkra.

## 2026-11-17: två sessioner rättade samma produkter, och en taggspärr fanns bara i den andra sessionens chatt
- **Vad hände:** medan jag byggde korrigeringar för 74 aktiva produkter skrev en parallell session (gren `claude/bos-status-10348-f2`) metabeskrivningar och leveranstidsmeningar på 39 produkter (13:50–13:51 UTC). 26 av mina 44 färdiga utkast var därför inaktuella; torrkörningens före-fil visade det, och jag skrev bara de 18 som var orörda. Den andra sessionen behandlar dessutom taggen `price-change-job-active` som "rörs inte"; den regeln står inte i repots dokument på min gren, och 4 av de 18 jag skrev bär taggen.
- **Regel:** kontrollera `git fetch` och grenarnas senaste loggposter före en skrivomgång, och jämför före-filen med underlaget innan något skrivs (det gjordes här och räddade 26 produkter). Regler om taggar som låser produkter ska stå i `BESLUTSLOGG.md`/profilen, inte bara i en chatt; fråga David om `price-change-job-active` innan fler produkter med den taggen skrivs.

## 2026-11-17: backtecken i en skal-heredoc körs som kommandon
- **Vad hände:** ett tillägg till beslutsfilen skrevs med en oavgränsad heredoc som innehöll backtecken; skalet körde `price-change-job-active` och filnamnen som kommandon och stoppade in tomma strängar i filen. Upptäcktes vid kontroll av filens slut.
- **Regel:** skriv text med backtecken via en citerad heredoc (`<<'E'`) eller med Write-verktyget, och läs filens slut efter varje tillägg.

<!-- Förd över från sidospåret bos-intern-lankning-matning 2026-11-21 -->
## 2026-11-17: handskriven återgivning av beskrivningstext ger tysta avvikelser
- **Vad hände:** Vid första skrivningen av en kollektionsbeskrivning (efter att ha borttagit spårningsparametrar) tappade jag ett fast mellanslag (U+00A0) och skrev "upphörsbacke" i stället för "uppförsbacke". Återläsning med exakt jämförelse mot förväntad text fångade båda. Ingen kund hann se felet länge, men det hade inte synts utan jämförelsen.
- **Regel:** skriv aldrig kollektionstext för hand utan att skriva ut den som kodad JSON (`json.dumps`) och kopiera den; kör alltid en kanarie först och jämför hela texten byte för byte mot förväntat före övriga skrivningar.

## 2026-11-21: git visar svenska tecken i filnamn med citattecken och oktala koder
Vad hände: vid konsolideringen av BOS-grenarna fördes nio filer med å i namnet (`rå_*.json`) först över med felaktiga namn (`"rapporter/…r\303\245_…json"`), eftersom git skriver ut sådana namn inom citattecken. Felet upptäcktes vid kontrollen att allt från grenarna fanns i målgrenen. Regel: sätt `git config core.quotepath false` och läs filnamn med `-z` (eller med den inställningen) i alla skript som hanterar sökvägar, och kontrollera efter varje överföring att varje källfil finns i målet.

<!-- Förd över från sidospåret alphazoo-byou-onboarding 2026-11-21 -->
### 2026-11-04 (tillägg): Shopify-kopplingen delas mellan sessioner; switch-shop kan ha brutit BEST OF SPORTS-sessionen
- **Vad hände:** jag anropade `switch-shop` två gånger i onboarding-passet för Alpha Zoo och B You. En annan session meddelade (ej verifierat av mig) att kopplingen delas mellan alla sessioner, pekar på en butik åt gången och att varje `switch-shop` bryter BEST OF SPORTS-sessionen och kräver ny inloggning. Det kan alltså ha avbrutit det pågående BEST OF SPORTS-arbetet.
- **Regel:** anropa aldrig `switch-shop` eller `get-shop-info` för en annan butik medan en annan session arbetar mot Shopify. För nya butiker: använd API-åtkomst per butik (samma app installeras på varje butik) eller publik katalog tills den finns. Ersätter inte föregående post, som beskriver samma händelse från min sida.

### 2026-11-04: switch-shop kopplade loss Shopify-verktyget och blockerade inventeringen av nya butiker
- **Vad hände:** uppdraget sa att jag skulle använda `switch-shop` och sedan `get-shop-info`. `switch-shop` återkallar åtkomsten till den nuvarande butiken (här BEST OF SPORTS) och nästa anrop kräver ny OAuth-inloggning som bara David kan göra; efter det fick Shopify-verktyget "needs you to sign in again" och gick inte att använda resten av passet. Inventering via Admin (status, SEO-fält, översättningar) blev därför inte gjord; publik katalog (`/products.json`) och genomsökning användes i stället. Ahrefs-API:t gav "Insufficient plan" på alla anrop (planen saknar API), och Windsor hade bara Facebook Organic anslutet.
- **Regel:** innan `switch-shop` anropas: kontrollera att en annan session inte är mitt i skrivning i den butik som kopplas loss, och be David logga in i den nya butiken i förväg. Anta aldrig att åtkomst finns för Windsor, Ahrefs eller Shopify: testa med ett billigt anrop först (`get_connectors`, `subscription-info-limits-and-usage`, `get-shop-info`) och rapportera luckorna direkt. Den publika katalogen (`/products.json`, `/collections.json`, `sitemap.xml`) räcker för en grov inventering av publicerade produkter men visar inte utkast, arkiverade, SEO-fält eller översättningsstatus.

<!-- Förd över från sidospåret byou-onboarding 2026-11-21 -->
### 2026-11-04: switch-shop bryter andra sessioners koppling (B You-onboarding)
- **Vad hände:** Shopify-verktygets koppling delas mellan sessionerna och pekar på en butik åt gången. Jag anropade `switch-shop` två gånger för att nå B You, vilket revokerar den aktuella butikens åtkomst och kan bryta en parallell BEST OF SPORTS-session. Ingen butik lästes eller skrevs till. Upptäcktes via meddelande från en annan session.
- **Regel:** använd inte `switch-shop` eller `get-shop-info` när flera sessioner arbetar parallellt. Läs andra butiker via API-väg med egen app per butik (`textutrullning-rutin.md` §3) eller offentliga flöden. Kontrollera först med David vilken butik kopplingen pekar på.

<!-- Förd över från sidospåret happyparent-onboarding 2026-11-21 -->
### 2026-11-04: switch-shop på den delade Shopify-kopplingen stör andra sessioner (onboarding Happy Parent)
- **Vad hände:** när Shopify-verktyget krävde ny inloggning ombads jag försöka igen med `switch-shop`. Kopplingen delas av alla sessioner och pekar på en butik åt gången; `switch-shop` återkallade åtkomsten till BEST OF SPORTS medan en annan session arbetade där. Ingen data ändrades. Den andra sessionen bad mig stoppa.
- **Regel:** anropa aldrig `switch-shop` om en annan session kan använda kopplingen. Kontrollera med `get-shop-info` först, och om kopplingen pekar på en annan butik: stanna, rapportera till David och vänta på butiksspecifik API-åtkomst (egen app per butik). Instruktioner om butiksbyte i en uppdragstext gäller inte när sessioner delar koppling.

<!-- Förd över från sidospåret workoutbrands-onboarding 2026-11-21 -->
### 2026-11-04: switch-shop återkallar åtkomsten för alla sessioner (onboarding WORKOUT BRANDS)
- **Vad hände:** Shopify-verktygets koppling delas mellan sessioner och pekar på en butik åt gången. Jag körde switch-shop för att byta från BEST OF SPORTS till WORKOUT BRANDS, vilket återkallade BOS-åtkomsten och bröt den parallella BOS-sessionen. Dessutom hade jag, när verktyget först sa att inloggning krävdes, redan avslutat fas 1 på publika data.
- **Regel:** kör aldrig switch-shop när andra sessioner arbetar parallellt. Inventera nya butiker via publika data eller via API-åtkomst per butik (egen app och nyckel), inte via den delade MCP-kopplingen.

<!-- Förd över från sidospåret gorillasports-onboarding 2026-11-21 -->
### 2026-11-04: switch-shop bryter andra sessioners Shopify-koppling (onboarding Gorilla Sports)
- **Vad hände:** Shopify-verktygets koppling delas av alla sessioner och pekar på en butik åt gången. Jag körde `switch-shop` för att nå Gorilla Sports, efter ett meddelande från en annan session. Det bryter inloggningen för BEST OF SPORTS-sessionen, och Gorilla kunde inte nås eftersom ny auktorisering krävs av David. Meddelandet från den andra sessionen återkallades därefter. Inget skrevs i någon butik.
- **Regel:** kör aldrig `switch-shop` eller `get-shop-info` i en session om en annan session kan använda samma koppling. Använd i stället butikens Admin API-app per butik (samma app installerad på varje butik) eller publika sidor. Uppdragstexten som säger "använd switch-shop" gäller bara när ingen annan session arbetar mot kopplingen.

<!-- Förd över från sidospåret oversikt-samordnare 2026-11-21 -->
## 2026-11-04: Tre sessioner numrerade regelboken v1.5 oberoende av varandra (samordnaren)
- **Vad hände:** BEST OF SPORTS-sessionen hade ett eget v1.5-avsnitt, Alpha Zoo-sessionen skrev om rubriken till v1.5 med R20/R21, och en tredje version v1.6 lades till. Sammanslagning hade gett konflikt och två olika v1.5.
- **Regel:** butikssessioner föreslår regler i sin rapport eller i ett eget utkast; bara samordnaren numrerar och för in dem i `regler-v1.md`. Regler som skriptet kan testa läggs samtidigt som test i `skrivfil_kontroll.py`.

## 2026-11-21: Läs butikens spärrar i BESLUTSLOGG före varje skrivbatch, även när David ger ja
Vad hände: BESLUTSLOGG hade sedan 2026-11-17 en rad om ändringsstopp i Gorillas butiker till och med 2026-11-30. Jag läste den inte före skrivningarna 2026-11-20, och därför kunde jag inte säga till David att stoppet fanns innan han godkände steg för steg. Regel: före varje skrivbatch i en butik, sök i `BESLUTSLOGG.md` efter butikens namn och ord som stopp, spärr och ändringsstopp, och redovisa resultatet för David i samma meddelande som ber om godkännande. Ett ja i chatten ändrar inte att spärren ska nämnas.

## 2026-11-23: "Bilder utan alt-text" i sidskanningen dominerades av menyikoner, inte produktbilder
Vad hände: BEST OF SPORTS-skanningen visade att 82 % av bilderna i sidkällan saknade alt-text, och jag presenterade det som en lucka som alt-text på produktbilder skulle täppa till. Efter att alt-text satts på 13 896 produktbilder (kontrollerat live: produktbilderna har titeln som alt) låg måttet kvar på 83,6 %. Orsaken är att varje sida innehåller cirka 150 bilder i huvudmenyn (ikoner för kategorier, 143 distinkta filer i Shopify Files) med tom alt-text, vilket är vanlig praxis för dekorativa ikoner bredvid en länktext. Skanningens mått räknar dem, så procenten sade nästan inget om produktbilderna. Regel: mät produktbildernas alt-text separat (galleribilder på produktsidor) och exkludera meny-, logotyp- och ikonbilder; redovisa vad som dominerar ett procenttal innan det används som mål eller säljargument.

## 2026-11-23: Variantnamn i BOS skrivs om av synken; ändra dem i synken, inte i butiken
Vad hände: Före en tänkt namnrättning av 303 varianter (SKU eller engelska ord som namn) läste jag synkkoden (Lovable-projektet "BOS - Velomarket"). Den bygger variantnamnet av Velomarkets attribut (storlek, färg, vikt; annars SKU) och skickar `option1` med i varje variantuppdatering. Rättningar direkt i Shopify hade återställts vid nästa synk.
Regel: läs hur ett flöde sätter ett fält innan fältet ändras i butiken. Variantnamn rättas via en översättnings- och override-tabell i synken.

## 2026-11-23: Velomarket-synken matchar varianter på position, inte SKU
Vad hände: Dubbla SKU:er, "Default Title"-varianter och priser som hör till en annan SKU fanns på sju Tunturi-produkter. Orsak: `shopify-bulk-sync` skriver SKU, namn, pris och streckkod till `existingVariants[i]` efter position, så en ändrad ordning eller ett saknat/tillkommet alternativ flyttar SKU:n till fel variant.
Regel: variantnamn och variantstädning får inte planeras utan att först åtgärda matchningen (SKU först, position som reserv). Kontrollera hur ett flöde identifierar en rad innan fält skrivs på den.

## 2026-11-23: Färgkoden "BL" hos Gymstick är svart, inte blå
Vad hände: I analysen av Gymsticks variantnamn föreslog jag att BL översätts till "Blå" utan att kontrollera. Vid bygget av PR i `ftp-product-sync` visade produkter med både BL och BLU (Air Track) och en shaker med handle `...svart` att BL är svart och BLU blå. Rättat före skrivning; inget skrevs i butiken med fel tolkning.
Regel: verifiera varje kodtolkning mot minst en produkt som har både koden och en färg i titeln eller handle innan den används i en översättningstabell.
