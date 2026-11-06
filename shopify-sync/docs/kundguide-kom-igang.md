# Kom igång själv: bättre produkttexter med kvalitetsrapport

Den här guiden är till dig som driver en webbutik på Shopify och vill köra produkttexterna själv. Du behöver ingen teknisk bakgrund. Du gör en sak i taget, och varje steg säger vad du ska göra och hur du ser att det gick bra.

Skapad 2026-11-06. Guiden bygger på det som gjordes och gick snett i den första butiken, BEST OF SPORTS. Allt som står här finns belagt i repots filer; källan anges. Det som vi **inte** har kunnat kontrollera är markerat **Ej verifierat**. Läs de punkterna som en varning, inte som ett löfte.

## Läs det här först: tre regler som aldrig bryts

1. **Skriv aldrig en nyckel, ett lösenord eller en "hemlighet" i chatten.** Inte heller i en fil i repot. Nycklar ligger bara i miljöns hemliga inställningar (steg 4). Om du råkat klistra in en nyckel någonstans: byt den direkt (steg 14).
2. **En butik i taget.** Använd inte Shopify-kopplingen i chatten för att växla mellan butiker (se "Det som var krångligt" nedan). Varje butik får sin egen app och sina egna inställningar.
3. **Ingenting skrivs i butiken förrän du har sett en provkörning.** Provkörningen kallas *dry-run* (steg 10). Den visar vad som skulle ändras, utan att ändra något.

## Ordlista (förklaras också första gången de används)

| Ord | Betyder |
|---|---|
| **Shopify Admin API** | Shopifys dörr för program. Ett program kan läsa och ändra produkter där, om det har nyckel och behörighet. |
| **App** | Det "program" du skapar i Shopify för att ge åtkomst. Appen är nyckeln till butiken. |
| **Behörighet (scope)** | Vad appen får göra. Vi ger bara `read_products` (läsa produkter) och `write_products` (ändra produkter). Inget mer. |
| **Klient-ID och Klienthemlighet** | Appens användarnamn och lösenord. Hemligheten är det som aldrig får läcka. |
| **Åtkomstnyckel** | En tillfällig nyckel som programmet hämtar med Klient-ID och Klienthemlighet. Den gäller ungefär ett dygn (24 timmar) och sparas bara i datorns minne. |
| **Miljö** | Den dator i molnet där arbetet körs. Den har egna inställningar för nätverk och hemligheter. |
| **Butiksprofil** | En liten fil med din butiks regler: märken, längdgränser, standardtext, taggar. |
| **Spärrlista** | En lista med produkter som aldrig får få ny text, hur mycket man än vill. |
| **Inventering** | En lista över alla produkter i butiken och deras läge, innan något görs. |
| **Batch** | En liten grupp produkter som körs tillsammans (högst 25 hos oss). |
| **Dry-run** | Provkörning. Visar vad som skulle ändras. Ändrar inget. |
| **Kanarie** | De tre första produkterna i en skarp körning. Går något fel upptäcks det på tre, inte på hundra. |
| **Återläsning** | Efter skrivning läser programmet tillbaka produkten från butiken och jämför den tecken för tecken med det som skulle skrivas. |
| **Stickprov** | En oberoende läsning av ett urval (minst 10 produkter eller 20 %) för att hitta fel som kontrollerna missat. |
| **Kvalitetsrapport** | Ett dokument som visar vad som gjordes, vad som kontrollerades och var det finns svagheter (steg 13). |

---

## Del A. Åtkomst till butiken

### Steg 1. Bestäm vad som ska ingå

Skriv ner tre saker: butikens adress på formen `något.myshopify.com` (den finns i Shopify under Inställningar), vilka produktgrupper som ska med först, och vilka som inte får röras. Du behöver inte göra något mer än så i det här steget.

*Hur du ser att det gick bra:* du har butikens `.myshopify.com`-adress nedskriven.

### Steg 2. Skapa appen i Shopify

Du skapar en egen app i Shopify. Vi använder **Dev Dashboard** (Shopifys sida för appar som byggs av butiksägare och utvecklare).

1. Öppna Dev Dashboard och välj att skapa en ny app (*Create app*). Källa: `shopify-sync/README.md`, avsnitt 2.
2. Ge appen ett tydligt namn, till exempel "Textutrullning" och butikens namn.
3. Välj behörigheter. Välj **bara** `read_products` och `write_products`. Lägg inte till något annat. Källa: `shopify-sync/docs/textutrullning-rutin.md`, avsnitt 3.
4. Spara en version av appen.

Varför bara dessa två? En app med färre rättigheter kan göra mindre skada om nyckeln läcker. Det har också en baksida som är bra att känna till: i BEST OF SPORTS gick det inte att flytta lagersaldo mellan dubbletter, eftersom appen inte har rätt att ändra lager (`rapporter/beslut-2026-11-05-7.md`). Det är avsiktligt.

**En app per butik, och ibland en per organisation.** Appen måste ligga i samma Shopify-organisation som butiken. I BEST OF SPORTS gick det inte att dela en app som skapats i en annan organisation: därför skapades en ny app i butikens egen organisation (`shopify-sync/docs/ANDRINGSLOGG.md`, 2026-10-23). Äger du flera butiker i olika organisationer behöver du alltså en app i varje.

*Ej verifierat:* Shopifys exakta menynamn och adressen till Dev Dashboard. De ändras av Shopify och står inte nedskrivna i repot. Äldre anteckningar (`textutrullning-rutin.md`, avsnitt 3) nämner menyvalet *Inställningar → Appar → Utveckla appar* i butiken; om det finns kvar är **Ej verifierat**. Vår första butik använde Dev Dashboard.

*Hur du ser att det gick bra:* appen finns i listan över dina appar och visar behörigheterna `read_products` och `write_products`.

### Steg 3. Installera appen i butiken

1. Installera appen i just den butik den ska arbeta i.
2. Öppna **Inställningar för appen** och leta upp **Klient-ID** och **Klienthemlighet**. Titta på dem, men **kopiera dem inte in i chatten** (se steg 4).

**Om installationslänken inte går att använda.** Appar kan ha så kallad *anpassad distribution* (Custom distribution), där appen delas ut med en särskild installationslänk till en butik. Länken fungerar bara för en butik, och bara om appen och butiken hör ihop. Vår logg säger att anpassad distribution bara gäller butiker i samma organisation (`ANDRINGSLOGG.md`, 2026-10-23). Får du ett meddelande om att länken inte kan användas är det därför troligast att du försöker installera appen i en butik i en *annan* organisation. Lösning: skapa en ny app i den butikens egen organisation (steg 2) i stället för att försöka dela den gamla.

*Ej verifierat:* Shopifys exakta felmeddelandetext. Den finns inte nedskriven i repot, så vi kan inte garantera att orsaken alltid är den ovan.

*Hur du ser att det gick bra:* appen står som installerad i butikens appförteckning.

### Steg 4. Ge åtkomst utan att klistra in nycklar i chatten

Programmet behöver Klient-ID och Klienthemlighet. De ska ligga som **hemliga inställningar i miljön**, inte i chatten och inte i någon fil.

1. Öppna miljöns inställningar (i Claude Code på webben: menyn för molnmiljön i sessionens titelrad, sedan *Edit*). Källa: miljödokumentationen i verktyget, läst 2026-11-06.
2. Lägg till två variabler med de namn programmet läser. För en butik som du kallar `MINBUTIK` blir det `SHOPIFY_CLIENT_ID_MINBUTIK` och `SHOPIFY_CLIENT_SECRET_MINBUTIK`. Klistra in värdena **i inställningsfältet**, aldrig i chatten. Om inställningarna också har en rubrik "Network secrets" (nätverkshemligheter) är den till för nycklar som skickas direkt till en viss adress. Våra skript läser vanliga miljövariabler, så lägg värdena som miljövariabler.
3. Starta en **ny session**. Nya variabler syns först då.

Det säkra formuläret: i vissa miljöer kan Claude öppna ett säkert formulär där du själv skriver in en nyckel, utan att den hamnar i chatten. **Ej verifierat** att det formuläret fungerar för vårt flöde. Skripten i repot läser Klient-ID och Klienthemlighet ur miljövariabler (`shopify-sync/scripts/shopify_api.py`), och ett formulär som lägger nyckeln i ett nätverkshuvud är något annat. Använd miljövariablerna tills vidare.

**Viktigt om butiken i skripten.** Skripten i repot är i dag inställda på BEST OF SPORTS: butiksadress och variabelnamn är förvalda värden i `shopify_api.py` och kan inte ändras med ett kommandoradsval. Programmet kan peka på en annan butik (`ShopifyKlient(butik=..., id_var=..., secret_var=...)`), men skripten som skriver och läser anropar det utan argument. **För en ny butik krävs alltså en liten ändring i skripten innan steg 6 och framåt går att köra.** Det är inte gjort ännu och är ett öppet beslut (se `rapporter/beslut-2026-11-06-2.md`).

*Hur du ser att det gick bra:* i den nya sessionen finns variablerna (Claude kan kontrollera att de *finns* utan att visa dem).

### Steg 5. Tillåt butikens adress i nätverksinställningen

Miljön får som standard inte nå vilka adresser som helst. När vi testade 2026-11-04 utan tillstånd gav Shopify felet `CONNECT tunnel failed, response 403` (`textutrullning-rutin.md`, avsnitt 3 och `LARDOMAR.md`).

1. Öppna miljöns inställningar igen.
2. Under nätverksåtkomst: lägg butikens `något.myshopify.com` under **Allowed domains** (tillåtna domäner). Lägg bara butikens adress, inte hela internet. Källa: miljödokumentationen, läst 2026-11-06.
3. Starta en ny session.

*Hur du ser att det gick bra:* ett läsande testanrop (steg 6) ger ett svar i stället för felet 403.

### Steg 6. Testa att läsa en enda produkt

Innan något skrivs: läs en produkt. Det visar att nyckeln, adressen och behörigheten fungerar. Programmet kontrollerar dessutom att svaret kommer från rätt butik och stannar om det inte gör det (`verifiera_butik` i `shopify_api.py`).

*Hur du ser att det gick bra:* programmet skriver butikens namn och en produkts titel. Inget har ändrats i butiken.

Får du fel:

| Du ser | Troligaste orsak | Gör så här |
|---|---|---|
| `CONNECT tunnel failed, response 403` | Butikens adress är inte tillåten | Steg 5 |
| "Miljövariablerna … måste finnas" | Variablerna saknas eller sessionen är gammal | Steg 4, starta ny session |
| "Token-anrop misslyckades: HTTP 4xx" | Fel Klient-ID eller Klienthemlighet, eller appen ligger i fel organisation | Kontrollera i Dev Dashboard; se steg 2–3 |
| "Fel butik" | Variablerna hör till en annan butik | Rätta variablerna; fortsätt inte |
| Väntar länge och försöker om | Shopify begränsar antal anrop (rate limit) | Programmet väntar och försöker igen av sig självt; låt det vara |

(Felmeddelandena kommer från `shopify_api.py`.)

---

## Del B. Butikens egna regler

### Steg 7. Gör butiksprofilen

Butiksprofilen är en fil som talar om hur *din* butik ska skrivas. Börja med att kopiera BEST OF SPORTS profil: `shopify-sync/config/butiksprofil-bestofsports.json`. Den är medvetet gjord som mall ("kopiera filen, byt butik, märken, standardblock, taggar och spärrlista").

Byt dessa saker:

- `butik` och `myshopify`: din butiks adresser.
- `marken`: de varumärken du säljer, skrivna som de ska se ut i texten.
- `gransvarden`: längder för titel, SEO-titel (rubriken som syns i Google) och metabeskrivning (texten under rubriken i Google). Förvalen är 70, 43 och 70–155 tecken.
- `standardblock_krav`: de rader som alltid ska finnas i slutet av varje text (leverans, retur, garanti, säljare). Skriv in de rubriker och ord som finns i *ditt* block.
- `klartagg`: taggen som sätts på en produkt när texten är färdig och kontrollerad. Hos oss `texter-klara`.
- `taggar_som_inte_far_roras`: taggar som andra system, till exempel en leverantörssynk, bygger på.
- `utanfor_tills_vidare`: produktgrupper du vill hålla utanför (till exempel kosttillskott eller barnprodukter, där påståenden kan vara känsliga).

Butiksspecifika saker hör till profilen. Regelboken (`shopify-sync/regler/regler-v1.md`) gäller alla butiker och ska inte skrivas om per butik.

*Hur du ser att det gick bra:* filen går att läsa som JSON, och alla fält pekar på din butik, inte på BEST OF SPORTS.

*Ej verifierat:* skriptet `skrivfil_kontroll.py` har längdgränserna (70/43/155) och vissa BEST OF SPORTS-specifika regler inbyggda i koden i stället för att läsa dem ur profilen. Kvalitetsrapporten (steg 13) läser gränserna ur profilen, men själva skrivkontrollen före skrivning gör det inte fullt ut. Se beslutsfilen.

### Steg 8. Gör spärrlistan

Spärrlistan skyddar produkter. Hos oss: de 20 produkter som ingår i ett pågående test, och grupper som ägaren beslutat hålla utanför.

1. Gör en CSV-fil med en kolumn `produkt_id` och ett id per rad.
2. Lägg en post i `shopify-sync/config/sparrlista.json` med namn, `aktiv`, sökväg till filen, kolumnnamn, skäl och vem som beslutat. Se hur befintliga poster ser ut.
3. En spärr hävs genom att sätta `aktiv` till `false` och ange datum och beslut. Poster tas aldrig bort.

*Hur du ser att det gick bra:* ett försök att skriva en spärrad produkt stoppas av `skrivfil_kontroll.py` med meddelandet att produkten är spärrad (och av `shopify_skriv_texter.py`, som hoppar över den).

---

## Del C. Första körningen

### Steg 9. Första inventeringen

En inventering är listan över alla produkter. Den gör att du vet hur många som finns, vilka som är aktiva, och vilka som ska med i första batchen.

I BEST OF SPORTS lästes alla 5 315 produkter via Admin API till en fil (`rapporter/inventering-bos-2026-11-04/alla_produkter.json`) med fälten id, titel, handle, status, tillverkare, produkttyp, taggar, lagersaldo och skapad-datum. Sedan delades de upp i batcher om högst 25, med spärrlistan inräknad (`plan_batcher.csv`).

**Ej verifierat:** det finns ingen färdig inventeringsmodul i repot. Programmet `shopify_api.py` kan läsa produkter om man redan har deras id (`hamta_produkter`), men inte lista *alla* produkter i butiken, och skriptet som gjorde BEST OF SPORTS inventering sparades inte som fil. För en ny butik behöver inventeringen byggas (öppet beslut).

*Regel som kostade oss dyrt:* bygg alltid inventeringen mot spärrlistan *innan* batcherna delas upp. I BEST OF SPORTS skrevs 150 produkter som skulle ha stått utanför, eftersom spärren inte fanns med från början (`LARDOMAR.md`, 2026-11-04).

### Steg 10. Första lilla batchen, med provkörning

Börja med en grupp om 10–25 produkter av samma typ. Flödet är detsamma varje gång (`textutrullning-rutin.md`, avsnitt 1):

1. **Spara före-läget.** Produktens titel, SEO, beskrivning, taggar och status sparas i en fil *innan* något ändras. Utan före-fil skrivs ingenting.
2. **Skriv utkast** utifrån produktens egen källtext. Aldrig från liknande produkter.
3. **Låt en andra, starkare granskare** döma varje utkast: godkänd, rättas (med exakt före/efter) eller underkänd. Använd kortprompterna i `shopify-sync/regler/agentprompter.md`.
4. **Bygg skrivfilen** och kör `python3 -I shopify-sync/scripts/skrivfil_kontroll.py <skrivfil>`. Noll fel krävs.
5. **Provkör**: `python3 -I shopify-sync/scripts/shopify_skriv_texter.py <skrivfil> --dry-run`. Programmet läser butiken och visar vad som skulle skrivas, vad som redan är lika och vad som avviker. Det ändrar inget.
6. **Kanarie**: samma kommando med `--kanarie` skriver de tre första produkterna, läser tillbaka dem och jämför. Stämmer allt fortsätter du.
7. **Resten**: `--rest` skriver övriga i delar om fyra, läser tillbaka efter varje del och **stoppar vid första avvikelse**. Taggen för färdig text sätts först efter lyckad återläsning.

Du bestämmer när du går från ett steg till nästa. Skrivningen ändrar titel, SEO och beskrivning, men aldrig pris, status eller handle (den webbadress som produkten har). Programmet kontrollerar att handle och status är oförändrade.

Skripten lägger före-fil och resultatfil i `rapporter/shopify-original-<datum>/`. Det är dina bevis. Ta bort dem aldrig.

*Hur du ser att det gick bra:* resultatfilen visar 0 avvikelser, och alla produkter i batchen har färdigtaggen.

Skriv aldrig texten för hand in i butiken. De flesta fel i BEST OF SPORTS kom av att långa texter kopierades för hand: extra mellanslag, mjuka bindestreck, tappade ord (`LARDOMAR.md`, flera poster). Programmet skriver direkt, och då uppstår inte de felen.

### Steg 11. Kontroll och återläsning

Återläsningen är redan inbyggd i steg 10. Du behöver bara läsa resultatet:

- **Skrivna och verifierade**: hur många som lästes tillbaka och stämde.
- **Avvikelser**: ska vara 0. Om inte: stanna, läs avvikelsen och fråga innan du kör vidare.
- **Redan lika / hoppade över**: produkter som inte behövde skrivas eller som programmet av säkerhetsskäl lät vara.

Dagen efter ska du köra en ny läsning (`shopify-sync/scripts/verifiera_skrivna.py <skrivfil>`, endast läsning). Skälet är att andra system kan skriva över texten. I BEST OF SPORTS hade en leverantörsapp arkiverat produkter över natten: när vi kontrollerade 2026-11-06 var 62 produkter med text från oss arkiverade (`rapporter/arkiverade-av-synk-2026-11-06.md`, `LARDOMAR.md` 2026-11-06). Det upptäcks bara om man tittar dagen efter. Återaktivera aldrig arkiverade produkter utan att först ta reda på varför de arkiverades.

### Steg 12. Stickprov

Ett stickprov är en separat läsning av minst 10 produkter eller 20 % av gruppen, gjord av en annan modell än den som skrev, och **bara läsande**. Be stickprovet:

1. jämföra butiken mot skrivfilen tecken för tecken,
2. leta efter påståenden som saknar stöd i källan,
3. rapportera allvarlighet: A (rätta före publik trafik), B (rätta), C (smaklig anmärkning),
4. skriva en rapport i `rapporter/…/granskning/` som börjar med antal lästa av antal och antal avvikelser.

I BEST OF SPORTS hittade stickproven fel som både utkastaren och granskaren missat, till exempel en metabeskrivning som aldrig skrevs (`LARDOMAR.md`, 2026-11-03). Hoppa inte över det steget.

Vill du att kvalitetsrapporten ska kunna räkna stickprovet exakt: spara också en liten JSON-fil bredvid rapporten (format i bilaga 2).

### Steg 13. Kvalitetsrapporten

Kvalitetsrapporten samlar allt i ett dokument du kan läsa och visa upp: omfattning (skrivna, totalt, avvisade), före/efter-exempel, vilka regler som tillämpats, kontrollresultat, granskning, återläsning, stickprov, mätetal, avvisade produkter och varför, vad som kräver ditt beslut och en ärlig lista över svagheter.

1. Gör ett manifest: en JSON-fil som pekar ut körningens filer. Utgå från `shopify-sync/config/kvalitetsrapport-bestofsports.json` (format i bilaga 2).
2. Kör:
   ```
   python3 -I shopify-sync/scripts/kvalitetsrapport.py --manifest <manifest.json> --ut rapporter/kvalitetsrapport-<butik>-<datum>.md --html
   ```
3. Öppna Markdown-filen eller den fristående HTML-filen (`.html`, går att öppna i vilken webbläsare som helst).

Rapporten läser bara filer. Den ansluter inte till Shopify, läser inga hemligheter och ändrar inga indatafiler. E-postadresser, telefonnummer och allt som liknar en nyckel tas bort ur rapporten.

Ett riktigt exempel finns i `rapporter/kvalitetsrapport-bestofsports-2026-11-06.md`. Läs gärna avsnittet "Svagheter och osäkerheter" först: det visar vad rapporten *inte* bevisar.

*Hur du ser att det gick bra:* filen innehåller alla avsnitt och siffrorna går ihop (skrivna + avvisade + övriga = totalt).

---

## Del D. När arbetet är klart

### Steg 14. Dra tillbaka åtkomsten

Appen kan ändra produkter så länge nyckeln finns. Därför ska åtkomsten dras tillbaka när du är klar, eller direkt om du misstänker att en nyckel läckt.

1. Byt **Klienthemligheten** i Dev Dashboard (genererar en ny; den gamla slutar fungera).
2. Ta bort variablerna `SHOPIFY_CLIENT_ID_…` och `SHOPIFY_CLIENT_SECRET_…` ur miljöns inställningar.
3. Ta bort butikens adress ur Allowed domains om den inte behövs mer.

Källa: `textutrullning-rutin.md`, avsnitt 3 och "Efter arbetet". Åtkomstnyckeln (24 timmar) tar slut av sig själv, men Klienthemligheten gör det inte.

**Ej verifierat:** om du även vill avinstallera appen från butiken. Stegen för det finns inte nedskrivna i repot; gör det i butikens appförteckning om du vill ha bort den helt.

*Hur du ser att det gick bra:* ett nytt läsförsök ger ett fel om saknade variabler eller en nekad åtkomst.

*Anmärkning om BEST OF SPORTS:* ägaren valde 2026-11-05 att avvakta med bytet (`BESLUTSLOGG.md`). Hemligheten är alltså inte bytt, och appen kan fortfarande skriva produkter. Det är ett medvetet, öppet beslut.

---

## Det som var krångligt i BEST OF SPORTS (och hur du undviker det)

**1. Den delade Shopify-kopplingen i chatten.** Claude kan i chatten använda en färdig Shopify-koppling. Den delas mellan alla sessioner och pekar på **en** butik åt gången. När sju sessioner startades för olika butiker körde flera `switch-shop`. Det återkallade åtkomsten till BEST OF SPORTS för alla, och ägaren fick logga in på nytt vid varje byte (`LARDOMAR.md`, 2026-11-04). Regeln: använd kopplingen för en butik i en session, **byt aldrig butik med switch-shop** i en delad koppling, och starta aldrig flera butikssessioner innan varje butik har sin egen app (steg 2–4).

**2. Dev Dashboard och Klient-ID/Klienthemlighet.** Appar som skapats i Dev Dashboard hämtar åtkomstnyckeln själva med Klient-ID och Klienthemlighet (metoden heter *client credentials*). Nyckeln gäller ungefär 24 timmar, hålls bara i minnet och skrivs aldrig till disk eller logg. Det fungerar bara när appen och butiken ligger i samma organisation. Äger ett partnerkonto appen (annan organisation) fungerar metoden inte; då hämtas en permanent nyckel i stället via en engångsinstallation (`shopify-sync/README.md`, avsnittet om partnerkonto). Den vägen kräver en installationslänk och mer handpåläggning; undvik den om du kan skapa appen i butikens egen organisation.

**3. "Installationslänken kan inte användas".** Se steg 3. Orsaken är i regel att en app med anpassad distribution försöker installeras i en butik utanför sin egen organisation. Lösningen är en ny app per organisation. Meddelandets exakta text är **Ej verifierat**.

**4. Nycklar i chatten.** Det händer lätt när något inte fungerar och man vill "bara visa nyckeln". Gör det aldrig. Nyckeln läggs i miljöns hemliga inställningar. Om en nyckel hamnat i chatten eller i en fil: byt den (steg 14). Rapporter och loggar ska aldrig innehålla nycklar; kvalitetsrapporten och `shopify_api.py` maskerar sådant automatiskt, men det är ett skyddsnät, inte en ursäkt.

**5. Leverantörssynken skriver över.** Appar som synkar produkter från en leverantör kan ändra eller arkivera produkter efter att du skrivit. Kontrollera dagen efter (steg 11) och lägg skyddstaggar på produkter som inte får röras. Detaljer: `rapporter/lovable-prompt-nattsynk-2026-11-06.md`.

**6. Skriv aldrig för hand.** Se steg 10.

## Äldre uppsättning med Google Cloud och Partner

Det finns en äldre och större uppsättning som handlar om *analys*: att samla försäljning, besök, Search Console och annonser i en databas (BigQuery) och göra nattliga granskningar. Den har egna steg för en ny butik och har inget med själva textskrivningen att göra.

- `shopify-sync/docs/ny-sajt.md`: lägga till en ny sajt (Google Cloud-projekt, Shopify, Search Console, Google Analytics, nattlig granskning). Steg 1 där beskriver en installationslänk via **Partners → Appar → Distribution**. Det är en annan väg än Dev Dashboard i den här guiden. Om den stämmer med Shopifys nuvarande meny är **Ej verifierat**; den lästes bara som text i repot.
- `shopify-sync/docs/tillvaxtdata.md`: tillväxtdata från Shopify, Google Analytics 4, Google Ads och Meta i BigQuery. Två stycken där är märkta som inaktuella (se markeringen i filen).
- `shopify-sync/docs/flera-sajter.md`: hur flera butiker hanteras tillsammans.

Du behöver inte göra något av detta för att komma igång med produkttexter.

---

## Bilaga 1. Snabbkommandon (vad som körs, och att inget ändras om du inte säger det)

| Vad | Kommando | Ändrar butiken? |
|---|---|---|
| Kontrollera en skrivfil | `python3 -I shopify-sync/scripts/skrivfil_kontroll.py <skrivfil>` | Nej |
| Provkörning | `python3 -I shopify-sync/scripts/shopify_skriv_texter.py <skrivfil> --dry-run` | Nej |
| Kanarie (3 produkter) | samma med `--kanarie` | **Ja** |
| Resten | samma med `--rest` | **Ja** |
| Läs tillbaka dagen efter | `python3 -I shopify-sync/scripts/verifiera_skrivna.py <skrivfil>` | Nej |
| Daglig kontroll | `python3 -I shopify-sync/scripts/nattkontroll.py` | Nej |
| Kvalitetsrapport | `python3 -I shopify-sync/scripts/kvalitetsrapport.py --manifest <fil> --ut <rapport.md> --html` | Nej (läser bara filer) |
| Tester utan nätverk | `python3 -I shopify-sync/scripts/test_kvalitetsrapport.py` | Nej |

Skripten som skriver är i dag inställda på BEST OF SPORTS (se steg 4).

## Bilaga 2. Filformat för kvalitetsrapporten

**Manifest** (en JSON-fil; sökvägar räknas från repots rot, `*` fungerar):

| Fält | Innehåll |
|---|---|
| `namn`, `butik` | Rubrik och butikens namn i rapporten |
| `profil`, `sparrlista`, `regelbok` | Butiksprofilen, spärrlistan och regelboken |
| `inventering` | Filer med listor av `{id, nr}`: alla produkter som ingick |
| `utkast` | Filer med listor av `{id, …}`: skrivna utkast |
| `avvisade` | Filer med listor av `{id, nr, skäl}`: avvisade produkter |
| `utlatanden` | Filer med listor av `{id, dom, rattningar, skal}`: granskningar. `dom` är `GODKÄND`, `RÄTTA`, `UNDERKÄND` eller `AVVISA` |
| `skrivfiler` | Filer med listor av `{id, nr, titel, seo_title, meta, html}`: det som skrevs |
| `korrigeringsmonster` | Del(ar) av filnamn som betyder "rättning, väger tyngst", till exempel `["korr", "fix"]` |
| `fore` | Före-filer: Shopify-poster `{id, title, tags, seo{title,description}, descriptionHtml}` |
| `resultat` | Resultatfiler från skrivningen: `{datum, skrivna_taggade_verifierade, redan_lika, avvikelser, hoppade_over, anrop}` |
| `skrivrapporter`, `stickprov` | Textrapporter (`.md`). Stickprov kan också vara `.json`: `{"namn","lasta","jamforda","avvikelser","fynd":{"A":0,"B":0,"C":0},"skrivfiler":["…"]}` |
| `oppna_fragor` | JSON-lista med `{id, datum, fraga, status}` |
| `efterkontroll` | Textfiler från kontroller efter skrivning |
| `totalt_i_butiken` | `{antal, kalla}`: uppgivet antal aktiva produkter |
| `exempel` | `{antal, fro}`: hur många före/efter-exempel och vilket frö som styr urvalet |

Allt utom `skrivfiler` är valfritt. Saknas något skriver rapporten det som en svaghet i stället för att gissa.

## Bilaga 3. Det som är Ej verifierat, samlat

1. Shopifys nuvarande menynamn och adress till Dev Dashboard (steg 2).
2. Om menyvalet *Inställningar → Appar → Utveckla appar* finns kvar (steg 2).
3. Den exakta texten i meddelandet om att installationslänken inte kan användas (steg 3).
4. Om ett säkert formulär för nätverkshemligheter fungerar för Shopify-flödet (steg 4).
5. Att skripten fungerar för en annan butik än BEST OF SPORTS utan ändring: det gör de **inte** (steg 4). Butiken är förvald i koden.
6. Att `skrivfil_kontroll.py` kan styras helt av butiksprofilen (steg 7).
7. En färdig inventeringsmodul för "alla produkter" (steg 9).
8. Hur appen avinstalleras (steg 14).
9. Att Partners → Distribution-vägen i `ny-sajt.md` stämmer med Shopifys nuvarande meny.
