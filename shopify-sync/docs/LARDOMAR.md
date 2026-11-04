# Lärdomar från arbetet

Syftet är att samma fel inte upprepas i nya arbetspass. Filen fylls bara på: nya poster läggs överst, gamla ändras inte. Läs den innan du rekommenderar en ändring i en butik, ett tema eller en datamodell.

## Hur en post skrivs
Datum, vad som gick fel eller upptäcktes, och regeln som följer av det.


### 2026-11-04: Formatskriptet gav "El-Lastcykel", och granskaren fångade det bara i en av tre batcher
- **Vad hände:** `format_regler.py` skriver stor bokstav efter bindestreck i typordet ("El-Lastcykel"). Granskaren av k_01a rättade det, men det gick igenom i k_01c (9055 och 9060) och skrevs i butiken. Upptäcktes när jag gjorde granskarens fynd till test; rättades samma dag (skrivet och återläst). Granskaren av k_01c fann dessutom 3 gånger "enligt tillverkaren" i en text (R5, högst 2), som skriptet inte räknade.
- **Regel:** testerna "stor bokstav efter bindestreck i typordet" och "enligt tillverkaren högst 2 per text" finns nu i `skrivfil_kontroll.py`. Kör kontrollen om på skrivfilerna efter att ett nytt test lagts till, även på batcher som redan granskats.


### 2026-11-04: Överlappande nr-serier mellan grupper (08 och 09)
- **Vad hände:** in-filerna för grupp 08 numrerades från 9501 och grupp 09 från 9601, men grupp 08 har 126 produkter och nådde 9626. Samma `nr` fanns därför på två olika produkter (9608, 9610–9619, 9623, 9625). Upptäcktes av granskaren; inget skrevs fel eftersom skrivfilerna byggdes per batch och identifieras via id.
- **Regel:** ge varje grupp ett nr-intervall som rymmer hela gruppen (t.ex. 1000 per grupp) och bygg skrivfiler per batch. Byggskriptet `bygg_m_skriv.py` bör nyckla på id, inte nr.

---

### 2026-11-04 (tillägg): Shopify-kopplingen delas mellan sessioner; switch-shop kan ha brutit BEST OF SPORTS-sessionen
- **Vad hände:** jag anropade `switch-shop` två gånger i onboarding-passet för Alpha Zoo och B You. En annan session meddelade (ej verifierat av mig) att kopplingen delas mellan alla sessioner, pekar på en butik åt gången och att varje `switch-shop` bryter BEST OF SPORTS-sessionen och kräver ny inloggning. Det kan alltså ha avbrutit det pågående BEST OF SPORTS-arbetet.
- **Regel:** anropa aldrig `switch-shop` eller `get-shop-info` för en annan butik medan en annan session arbetar mot Shopify. För nya butiker: använd API-åtkomst per butik (samma app installeras på varje butik) eller publik katalog tills den finns. Ersätter inte föregående post, som beskriver samma händelse från min sida.

### 2026-11-04: switch-shop kopplade loss Shopify-verktyget och blockerade inventeringen av nya butiker
- **Vad hände:** uppdraget sa att jag skulle använda `switch-shop` och sedan `get-shop-info`. `switch-shop` återkallar åtkomsten till den nuvarande butiken (här BEST OF SPORTS) och nästa anrop kräver ny OAuth-inloggning som bara David kan göra; efter det fick Shopify-verktyget "needs you to sign in again" och gick inte att använda resten av passet. Inventering via Admin (status, SEO-fält, översättningar) blev därför inte gjord; publik katalog (`/products.json`) och genomsökning användes i stället. Ahrefs-API:t gav "Insufficient plan" på alla anrop (planen saknar API), och Windsor hade bara Facebook Organic anslutet.
- **Regel:** innan `switch-shop` anropas: kontrollera att en annan session inte är mitt i skrivning i den butik som kopplas loss, och be David logga in i den nya butiken i förväg. Anta aldrig att åtkomst finns för Windsor, Ahrefs eller Shopify: testa med ett billigt anrop först (`get_connectors`, `subscription-info-limits-and-usage`, `get-shop-info`) och rapportera luckorna direkt. Den publika katalogen (`/products.json`, `/collections.json`, `sitemap.xml`) räcker för en grov inventering av publicerade produkter men visar inte utkast, arkiverade, SEO-fält eller översättningsstatus.
### 2026-11-04: switch-shop bryter andra sessioners koppling (B You-onboarding)
- **Vad hände:** Shopify-verktygets koppling delas mellan sessionerna och pekar på en butik åt gången. Jag anropade `switch-shop` två gånger för att nå B You, vilket revokerar den aktuella butikens åtkomst och kan bryta en parallell BEST OF SPORTS-session. Ingen butik lästes eller skrevs till. Upptäcktes via meddelande från en annan session.
- **Regel:** använd inte `switch-shop` eller `get-shop-info` när flera sessioner arbetar parallellt. Läs andra butiker via API-väg med egen app per butik (`textutrullning-rutin.md` §3) eller offentliga flöden. Kontrollera först med David vilken butik kopplingen pekar på.

---

### 2026-11-04: switch-shop bryter andra sessioners Shopify-koppling (onboarding Gorilla Sports)
- **Vad hände:** Shopify-verktygets koppling delas av alla sessioner och pekar på en butik åt gången. Jag körde `switch-shop` för att nå Gorilla Sports, efter ett meddelande från en annan session. Det bryter inloggningen för BEST OF SPORTS-sessionen, och Gorilla kunde inte nås eftersom ny auktorisering krävs av David. Meddelandet från den andra sessionen återkallades därefter. Inget skrevs i någon butik.
- **Regel:** kör aldrig `switch-shop` eller `get-shop-info` i en session om en annan session kan använda samma koppling. Använd i stället butikens Admin API-app per butik (samma app installerad på varje butik) eller publika sidor. Uppdragstexten som säger "använd switch-shop" gäller bara när ingen annan session arbetar mot kopplingen.
---

### 2026-11-04: switch-shop på den delade Shopify-kopplingen stör andra sessioner (onboarding Happy Parent)
- **Vad hände:** när Shopify-verktyget krävde ny inloggning ombads jag försöka igen med `switch-shop`. Kopplingen delas av alla sessioner och pekar på en butik åt gången; `switch-shop` återkallade åtkomsten till BEST OF SPORTS medan en annan session arbetade där. Ingen data ändrades. Den andra sessionen bad mig stoppa.
- **Regel:** anropa aldrig `switch-shop` om en annan session kan använda kopplingen. Kontrollera med `get-shop-info` först, och om kopplingen pekar på en annan butik: stanna, rapportera till David och vänta på butiksspecifik API-åtkomst (egen app per butik). Instruktioner om butiksbyte i en uppdragstext gäller inte när sessioner delar koppling.

### 2026-11-04: switch-shop återkallar åtkomsten för alla sessioner (onboarding WORKOUT BRANDS)
- **Vad hände:** Shopify-verktygets koppling delas mellan sessioner och pekar på en butik åt gången. Jag körde switch-shop för att byta från BEST OF SPORTS till WORKOUT BRANDS, vilket återkallade BOS-åtkomsten och bröt den parallella BOS-sessionen. Dessutom hade jag, när verktyget först sa att inloggning krävdes, redan avslutat fas 1 på publika data.
- **Regel:** kör aldrig switch-shop när andra sessioner arbetar parallellt. Inventera nya butiker via publika data eller via API-åtkomst per butik (egen app och nyckel), inte via den delade MCP-kopplingen.

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

## 2026-11-04: Tre sessioner numrerade regelboken v1.5 oberoende av varandra (samordnaren)
- **Vad hände:** BEST OF SPORTS-sessionen hade ett eget v1.5-avsnitt, Alpha Zoo-sessionen skrev om rubriken till v1.5 med R20/R21, och en tredje version v1.6 lades till. Sammanslagning hade gett konflikt och två olika v1.5.
- **Regel:** butikssessioner föreslår regler i sin rapport eller i ett eget utkast; bara samordnaren numrerar och för in dem i `regler-v1.md`. Regler som skriptet kan testa läggs samtidigt som test i `skrivfil_kontroll.py`.
