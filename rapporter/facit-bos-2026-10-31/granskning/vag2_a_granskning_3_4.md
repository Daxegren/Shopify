# Granskning våg 2, utkast a_3 och a_4 – BEST OF SPORTS (2026-11-01)

Oberoende granskning. Bara läsning i Shopify, ingenting skrevs. Inga utkastsfiler ändrades.

**Butik:** kontrollerad med get-shop-info: BEST OF SPORTS (bestofsports.se, SEK).
**Underlag:** `vag2_skriv/a_3_utkast.json` (9 produkter) och `vag2_skriv/a_4_utkast.json` (10 produkter).
**Metod:** title, status, vendor, productType, descriptionHtml, tags, seo och varianter hämtades live via graphql_query (`nodes`) i tre batchar (8, 8, 3). Fältet `fakta` jämfördes för hand mot live-källan; det stämmer för alla 19 (på 2406 saknas meningen "Want the perfect balance…" i fakta, utan betydelse). Längder, kommatecken och enheter räknades med skript. `scripts/kontrollera_produkttext.py --seo-title-max 43` gav 0 FEL och 0 varningar på båda filerna. Språket lästes för hand.
**Live-läge:** alla 19 är ACTIVE och har `seo.title` och `seo.description` = null. Ingen av produkterna finns i `handhavd_ids.txt`.

## Sammanställning

| Kategori | Antal | Nr |
|---|---|---|
| GODKÄND | 7 | 2304, 2315, 2403, 2404, 2409, 2410, 2412 |
| GODKÄND MED SMÅ RÄTTNING | 7 | 2301, 2302, 2308, 2309, 2313, 2407, 2414 |
| UNDERKÄND | 5 | 2310, 2314, 2406, 2411, 2415 |

Totalt 19 produkter.

## Regelkontroll (alla 19)
- Titel ≤70 tecken (längst 57) och ≤2 kommatecken: alla uppfyller.
- SEO-titel ≤43 (längst 42, nr 2404): alla uppfyller. Där SEO-titeln är lika med titeln (2308, 2409, 2410, 2412, 2414) lagras den som tom av Shopify. Det är avsett.
- Meta: de 9 som har meta ligger inom 130–155 (131–149). 10 har meta null på grund av tunn källa, vilket är tillåtet.
- Enheter: ml, oz, cm, mm, kg och g står med gemener överallt. "Ml", "Oz", "Cm", "Mm" och "Kg" förekommer inte.
- Inga intervall med bindestreck i texterna. Det enda talparet med bindestreck är org.nr i standardblocket, och det är rätt.
- Ingen titel har kolon. Beskrivande ord har versal i titel och SEO-titel.
- Standardblocket är identiskt i alla 19 och anger ingen fraktavgift i kronor. Meningen om beställningsvaror finns på 2309 och 2414, som båda har taggen "På beställning" (på 2414 står det även i källtexten).
- Inga utropstecken, superlativ, priser, ursprungsland eller märkeshistoria. "Italien" (2404) och Tunturis märkestext (2309, 2411) är borttagna.

## Per produkt

### a_3

**2301 – Boxningshandskar Toorx Panther (10472279539978) – GODKÄND MED SMÅ RÄTTNING**
- Live-titel: "Boxningshandskar TOORX Panther Boxing Gloves 10oz". Ny titel: "Boxningshandskar Toorx Panther, Polyuretan, 10 oz". Den engelska delen "Boxing Gloves" är borttagen och materialet tillagt ur källan.
- Fakta: alla uppgifter går att spåra till källan. Rubriken "Storlek" är antagen, vilket står under att bekräfta.
- Språk: "Toorx Panther Boxing Gloves är boxningshandskar" upprepar typordet på engelska och svenska.
- Rättning (html): före "Toorx Panther Boxing Gloves är boxningshandskar i polyuretan. Handskarna är 10 oz." → efter "Toorx Panther är boxningshandskar i polyuretan. Handskarna har storleken 10 oz." (samma formulering som 2302).

**2302 – Boxningshandskar Toorx Leopard (10472279605514) – GODKÄND MED SMÅ RÄTTNING**
- Live-titel: "Boxningshandskar TOORX Leopard Boxing Gloves 10oz". Ny titel: "Boxningshandskar Toorx Leopard, Polyuretan, 10 oz", ändrad på samma sätt som 2301.
- Rättning (html): före "Toorx Leopard Boxing Gloves är boxningshandskar i polyuretan." → efter "Toorx Leopard är boxningshandskar i polyuretan."

**2304 – Flaska Trec Shaker 050 (10472280391946) – GODKÄND**
- Live-titel: "Flaska TREC SHAKER 050 - 0.7 l BLACK - TREC TEAM". Ny titel: "Flaska Trec Shaker 050, 700 ml, Svart". "TREC TEAM" är borttaget (står under att bekräfta), och 0.7 l är omräknat till 700 ml, som också står i källtexten.
- Språk: korrekt. Formuleringen "en flaska med en kapacitet på 700 ml" kunde vara kortare, men den är inte fel.

**2315 – Flaska Trec Endurance 002 (10472297464074) – GODKÄND**
- Live-titel: "Flaska TREC Endurance 002, orange". Ny titel: "Flaska Trec Endurance 002, Orange", bara skrivsättet är ändrat. Källan är tom, och texten innehåller bara det som står i titeln. Det är korrekt.

**2308 – Ankelrem Tunturi Pro (10472283832586) – GODKÄND MED SMÅ RÄTTNING**
- Live-titel: "TUNTURI Ankelrem Prof". Ny titel: "Ankelrem Tunturi Pro, Läder, Svart". "Prof" är ändrat till "Pro", eftersom källtexten två gånger skriver "Ankelrem(men) Pro". Färg och material kommer från källan.
- Fakta: utkastet utelämnar fästet (källan anger både spänne/krok och "Kardborrefästning") och längdjusteringen. Det är korrekt hanterat. 35,5 cm finns i källan.
- Språk: "Tunturi Ankelrem Pro är en svart ankelrem" har versal mitt i meningen (samma fel som nr 502 i våg 1) och upprepar "ankelrem".
- Rättning (meta, 145 → 136 tecken): före "Tunturi Ankelrem Pro är en svart ankelrem i läder, 35,5 cm lång." → efter "Tunturi Pro är en svart ankelrem i läder, 35,5 cm lång."
- Rättning (html): före "<p>Tunturi Ankelrem Pro är en svart ankelrem i läder som används" → efter "<p>Tunturi Pro är en svart ankelrem i läder som används".

**2309 – Stretchband Tunturi Power Band Light (10472283898122) – GODKÄND MED SMÅ RÄTTNING**
- Live-titel: "Stretch band Tunturi Power Band Light Yellow". Ny titel: "Stretchband Tunturi Power Band Light, 104 cm, Gul".
- Fakta: motstånd (5–20 kg) och bredd är utelämnade, eftersom källan motsäger sig. Det är rätt. Hälsofraserna är borttagna.
- Språk: den andra punkten under Passar för, "Dig som vill ha ett band i latex som är 104 cm långt", upprepar bara specifikationen.
- Rättning (html): ta bort `<li>Dig som vill ha ett band i latex som är 104 cm långt</li>`, så att bara den första punkten står kvar.
- Not: den femte punkten under att bekräfta motsäger sig själv ("texten saknar raden … finns i leveransblocket"). Meningen finns i blocket, så inget behöver ändras i texten.

**2310 – Viktplatta Spokey (10472289075466) – UNDERKÄND**
- Live-titel: "Viktplatta SPOKEY Blå, 30 mm, 10 kg". Ny titel: "Viktplatta Spokey, Järn, Borrdiameter 29 mm". Vikten (10 kg) och färgen (Blå) är borttagna, eftersom produkten har fem varianter (59–439 kr) som bara har artikelnummer som namn. Det följer variantregeln. Men titeln har fått ett nytt mått ur brödtexten.
- Skäl:
  1. Källan motsäger sig: titeln anger 30 mm och texten "Borrdiameter: 29 mm". Enligt avsnitt 10 i standarden ("motsäger källan sig: utelämna uppgiften") får 29 mm inte stå i titel, SEO-titel eller specifikation. Utkastet skriver det på alla tre ställena. Det är inte heller säkert att hålet är lika stort på alla fem varianterna.
  2. Materialet "järn" kommer bara från skräpraden "Spokey: Spokey Spokes: 29 mm Material: järn".
  3. Efter en rättning skulle det bara stå "Viktplatta Spokey, Järn" utan vikt. Produktnamnet förlorar då sin viktigaste uppgift. Variantnamnen behövs först.
- Förslag: lyft produkten till David (variantnamn och borrdiameter). Om den ändå ska skrivas: titeln "Viktplatta Spokey, Järn", SEO-titeln "Viktplatta Spokey, Järn" och html utan 29 mm.

**2313 – Gymnastikboll Christopeit 75 cm (10472289566986) – GODKÄND MED SMÅ RÄTTNING**
- Live-titel: "Gymnastikboll CHRISTOPEIT 75 cm, blå". Ny titel: "Gymnastikboll Christopeit, 75 cm, Blå", bara skrivsättet är ändrat.
- Fakta: bärförmågan 100 kg och bäckenbotten är utelämnade, vilket är rätt. Inget löfte om att bollen är sprängsäker.
- Språk: "Enligt tillverkaren tränar bollen balans" säger att bollen tränar (samma fel som nr 302 i våg 1). "med diameter 75 cm" saknar en artikel.
- Rättning (meta, 144 → 150): före "Christopeit gymnastikboll är en blå boll i PVC med diameter 75 cm. Pump ingår. Enligt tillverkaren tränar bollen balans och olika muskelgrupper." → efter "Christopeit gymnastikboll är en blå boll i PVC, 75 cm i diameter. Pump ingår. Med bollen tränar du enligt tillverkaren balans och olika muskelgrupper."
- Rättning (html): före "Christopeit gymnastikboll är en blå boll i PVC med diameter 75 cm. Enligt tillverkaren tränar bollen balans och olika muskelgrupper, till exempel mage, ben, säte och rygg." → efter "Christopeit gymnastikboll är en blå boll i PVC, 75 cm i diameter. Med bollen tränar du enligt tillverkaren balans och olika muskelgrupper, till exempel mage, ben, säte och rygg."
- Notering: en gymnastikboll bär kroppsvikt. Den finns inte i listan över produkter som tas för hand, och ingen belastningsuppgift skrivs. Godtagbart.

**2314 – Viktskivor för Christopeit SP 5000 (10472296808714) – UNDERKÄND**
- Live-titel: "Viktskivor för CHRISTOPEIT SP 5000". Ny titel: "Viktskivor för Christopeit SP 5000, 2 x 5 kg" (vikten är tillagd ur källtexten "2x5 kg").
- Skäl: viktskivor till en maskin med last tas för hand enligt uppdraget och avsnitt 10. Utkastet säger det självt under att bekräfta. Källan består av tre tecken, och det är oklart om "2 x 5 kg" betyder två skivor på 5 kg.
- Språk (om produkten tas för hand): "angivna som 2 x 5 kg" läses konstigt. Förslag: "Två viktskivor på 5 kg till Christopeit SP 5000", men först när David har bekräftat vikten.

### a_4

**2403 – Gymnastikgummi Toorx Elastic (10472301723914) – GODKÄND**
- Live-titel: "Gymnastikgummi TOORX Elastic med handtag, medium, blå". Ny titel: "Gymnastikgummi Toorx Elastic med Handtag, Medium, Blå", bara skrivsättet är ändrat. Måttet står utan benämningar, vilket är rätt hanterat. Språket är korrekt.

**2404 – Träningshandskar Toorx Professional Gloves (10472305393930) – GODKÄND**
- Live-titel: "Träningshandskar TOORX Professional Gloves, svart-grå". Ny titel: "Träningshandskar Toorx Professional Gloves, Svart och Grå".
- Fakta: "Italien" är borttaget och "maximal komfort och säkerhet" likaså. Allt annat finns i källan.
- Notering, ingen rättning krävs: metan skriver "De rekommenderas för styrketräning" utan "enligt tillverkaren" (html har det). Specifikationsraden "Öglor mellan fingrarna för enkel borttagning" har inte formen "Rubrik: Värde". "Gloves" är engelska, men ordet ingår i modellnamnet.

**2406 – Rullskridskor Fila Legacy QF Lady (10472308179210) – UNDERKÄND**
- Live-titel: "Rulluisud FILA Legacy QF Lady, Black/Violet" (estniskt typord). Ny titel: "Rullskridskor Fila Legacy QF Lady, Svart och Violett".
- Skäl: rullskridskor ska tas för hand (säkerhet). Pris 3 379 kr. Storleken är okänd: varianten heter "Default Title" och artikelnumret slutar på "-38-5". Källan är på engelska, så hela texten är en översättning som behöver granskas av en människa (stängningssystemet "Velcro straps on the leg arch and a buckle button on the stirrups").
- Inga påhittade uppgifter hittades. Hjul 4 × 84 mm, ABEC 7, aluminium, AirFlow och anvisningen om tungan finns i källan.

**2407 – Gymnastikgummiband Toorx Fabric Bands Medium (10472311161098) – GODKÄND MED SMÅ RÄTTNING**
- Live-titel: "Gymnastikgummiband set TOORX Fabric Bands Medium". Ny titel: "Gymnastikgummiband Set Toorx Fabric Bands Medium".
- Språk: "Gymnastikgummiband Set" har ett fristående "Set" med versal mitt i titeln och läses som en felöversättning.
- Rättning (titel, 48 → 54 tecken, 1 kommatecken): före "Gymnastikgummiband Set Toorx Fabric Bands Medium" → efter "Gymnastikgummiband Toorx Fabric Bands Medium, Set om 5" (5 finns i källan).
- Rättning (SEO-titel, 41 → 37): före "Gymnastikgummiband Set Toorx Fabric Bands" → efter "Gymnastikgummiband Toorx Fabric Bands".
- Html är korrekt. "Fabric" kan betyda att banden är av tyg, och då är "gummiband" i namnet missvisande. Den frågan står redan under att bekräfta.

**2409 – Benskydd Toorx med Fotskydd (10475517870346) – GODKÄND (titeländringen kräver Davids bekräftelse)**
- Live-titel: "Fotsskydd TOORX benskydd med fotsskydd". Ny titel: "Benskydd Toorx med Fotskydd". Typordet är flyttat ("Benskydd" först, det dubbla "Fotsskydd" i början borttaget) och stavfelet "fotsskydd" är rättat till "fotskydd". Ändringen följer källan och byter inte typ av produkt.
- Fakta: "avsedda för boxare" står i källan. Inget skyddspåstående görs. Notering: det är skyddsutrustning för kampsport. Den finns inte i listan över produkter som tas för hand, men texten får inte byggas ut med skyddslöften.

**2410 – Reservfjädrar Tunturi Indiaka (10475978948874) – GODKÄND**
- Live-titel: "Reservfjädrar TUNTURI Indiaka". Ny titel: "Reservfjädrar Tunturi Indiaka", bara skrivsättet är ändrat.
- Fakta: "passar i alla Indiaca-Playballs" står i källan ("passar perfekt i alla Indiaca®-Playballs") och är skrivet som tillverkarens uppgift. Den motsägelsefulla uppgiften om "4 plastbollar" och antalet skrivs inte. Det är rätt.
- Notering: "Indiaka" (titeln) och "Indiaca" (varumärket) står i samma mening. Det följer källan, men en läsare kan uppfatta det som ett stavfel.

**2411 – Boxningssäcksfäste Tunturi Swivel Chrome (10475982520586) – UNDERKÄND**
- Live-titel: "Boxningssäcksfäste Tunturi Swivel Chrome med kullager". Ny titel: "Boxningssäcksfäste Tunturi Swivel Chrome med Kullager", bara skrivsättet är ändrat.
- Skäl:
  1. Titel och text beskriver olika produkter. Titeln säger fäste för boxningssäck (en lastbärande upphängning), medan texten och källan beskriver en pivot till speedboll som skruvas fast i en speedballplattform. Motsägelsen mellan titel och källa skrivs vidare i titeln. Agenten får inte byta namn på produkten, så den ska lyftas till David (utkastet säger samma sak under att bekräfta).
  2. Specifikationen "Material: Krom" motsäger "krompläterad" i samma text. Bör vara "Material: Krompläterad" eller tas bort.
  3. Språk: "speedball" och "speedboll" blandas ("mellan speedbollen och speedballplattformen", "speedballpivot").
- Det övriga går att spåra: mått, 358 g (från "358 gr"), fyra skruvar, grå, produktkod och FAQ-svaret ("lämplig för alla boxnings- eller speedbollar", skrivet som tillverkarens uppgift).

**2412 – Handleds- och Ankelvikter Christopeit (10494691344650) – GODKÄND (titeländringen kräver Davids bekräftelse)**
- Live-titel: "Handledd-/ankelvikter CHRISTOPEIT 2x0,50 kg". Ny titel: "Handleds- och Ankelvikter Christopeit". Stavfelet "Handledd-" är rättat och **vikten 2x0,50 kg är borttagen**, eftersom källtexten säger "0,50 kg (par)". Det följer regeln om motsägelser. Konsekvensen är att produktsidan inte anger någon vikt alls förrän David har bekräftat den.
- Fakta: par, armar och ben, justerbart remfäste, aerobics, gymnastik, promenader, uthållighetssporter och "öka intensiteten" finns alla i källan. "(Utan matta, löpband)" är utelämnat.
- Språk: korrekt.

**2414 – Tricepsrep Tunturi Revolving Triceps Rope (10494898962698) – GODKÄND MED SMÅ RÄTTNING**
- Live-titel: "Tricepsrep TUNTURI Revolving Triceps Rope". Ny titel: "Tricepsrep Tunturi Revolving Triceps Rope", bara skrivsättet är ändrat.
- Språk: "kan läggas till en viktstation" är en ordagrann översättning och låter konstigt på svenska.
- Rättning (meta, 149 → 150): före "Det kan läggas till en viktstation." → efter "Det kan användas med en viktstation."
- Rättning (html, första stycket): före "ett tricepsrep som kan läggas till en viktstation." → efter "ett tricepsrep som kan användas med en viktstation."
- Rättning (html, Passar för): före "Dig som har en viktstation och vill lägga till ett tricepsrep" → efter "Dig som har en viktstation och vill komplettera den med ett tricepsrep".
- Notering: repet används med kabel under last, men texten har inga belastningsuppgifter. Godtagbart på samma sätt som ankelremmen 2308.

**2415 – Rullskridskor Fila Legacy Pro 80 (10494939595018) – UNDERKÄND**
- Live-titel: "Rullskridskor LEGACY PRO 80, svart-röd-grå". Ny titel: "Rullskridskor Fila Legacy Pro 80, Svart, Röd och Grå" (märket är tillagt ur märkesfältet).
- Skäl:
  1. Rullskridskor ska tas för hand.
  2. Färgen är motsägelsefull: den enda varianten heter "42.5 / black", medan titeln anger svart-röd-grå. Enligt variantregeln får titel och specifikation då inte låsa färgen, men utkastet skriver "Svart, Röd och Grå" både i titeln och i specifikationen.
  3. Språk: "rullskridskor för vuxna med ABEC 5-lager" kan läsas som "vuxna med lager". Bättre: "… för vuxna. De har ABEC 5-lager." Raden "Lämplig för" i specifikationen upprepar Passar för.

## Alla rättningar i korthet
| Nr | Fält | Före | Efter |
|---|---|---|---|
| 2301 | html | Toorx Panther Boxing Gloves är boxningshandskar i polyuretan. Handskarna är 10 oz. | Toorx Panther är boxningshandskar i polyuretan. Handskarna har storleken 10 oz. |
| 2302 | html | Toorx Leopard Boxing Gloves är boxningshandskar | Toorx Leopard är boxningshandskar |
| 2308 | meta | Tunturi Ankelrem Pro är en svart ankelrem | Tunturi Pro är en svart ankelrem |
| 2308 | html | Tunturi Ankelrem Pro är en svart ankelrem | Tunturi Pro är en svart ankelrem |
| 2309 | html | `<li>Dig som vill ha ett band i latex som är 104 cm långt</li>` | (tas bort) |
| 2313 | meta | … i PVC med diameter 75 cm. Pump ingår. Enligt tillverkaren tränar bollen balans och olika muskelgrupper. | … i PVC, 75 cm i diameter. Pump ingår. Med bollen tränar du enligt tillverkaren balans och olika muskelgrupper. |
| 2313 | html | … i PVC med diameter 75 cm. Enligt tillverkaren tränar bollen balans och olika muskelgrupper, | … i PVC, 75 cm i diameter. Med bollen tränar du enligt tillverkaren balans och olika muskelgrupper, |
| 2407 | titel | Gymnastikgummiband Set Toorx Fabric Bands Medium | Gymnastikgummiband Toorx Fabric Bands Medium, Set om 5 |
| 2407 | seo_title | Gymnastikgummiband Set Toorx Fabric Bands | Gymnastikgummiband Toorx Fabric Bands |
| 2414 | meta | Det kan läggas till en viktstation. | Det kan användas med en viktstation. |
| 2414 | html | som kan läggas till en viktstation. | som kan användas med en viktstation. |
| 2414 | html | vill lägga till ett tricepsrep | vill komplettera den med ett tricepsrep |

## Titeländringar som David bör se (namnet ändrat mer än skrivsättet)
- 2301 och 2302: "Boxing Gloves" borttaget, "Polyuretan" tillagt.
- 2304: "TREC TEAM" borttaget, 0.7 l skrivet som 700 ml.
- 2308: "Prof" ändrat till "Pro".
- 2310: "Blå" och "10 kg" borttagna, "30 mm" ersatt med "Järn, Borrdiameter 29 mm" (underkänd).
- 2314: "2 x 5 kg" tillagt (underkänd).
- 2406: estniska "Rulluisud" ersatt med "Rullskridskor" (underkänd).
- 2407: se rättningen ovan.
- 2409: "Fotsskydd TOORX benskydd med fotsskydd" ändrad till "Benskydd Toorx med Fotskydd" (typordet flyttat, stavfelet rättat).
- 2412: "Handledd-/ankelvikter … 2x0,50 kg" ändrad till "Handleds- och Ankelvikter Christopeit" (vikten borttagen, stavfelet rättat).
- 2415: "Fila" tillagt (underkänd).
