# Lärdomar från arbetet

Syftet är att samma fel inte upprepas i nya arbetspass. Filen fylls bara på: nya poster läggs överst, gamla ändras inte. Läs den innan du rekommenderar en ändring i en butik, ett tema eller en datamodell.

## Hur en post skrivs
Datum, vad som gick fel eller upptäcktes, och regeln som följer av det.

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
