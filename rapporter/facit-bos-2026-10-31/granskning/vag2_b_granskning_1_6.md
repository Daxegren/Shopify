# Granskning våg 2, utkast b_1–b_6 (Velomarket-cykeltillbehör) – BEST OF SPORTS (2026-11-03)

Det här är en oberoende granskning. Jag har bara läst i Shopify och har inte ändrat någon utkastsfil. Butiken kontrollerades först med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK).

**Underlag:** `vag2_skriv/b_1_utkast.json`–`b_6_utkast.json` (54 utkast, nr 5002–5088), `b_1_avvisade.json`–`b_6_avvisade.json` (36 avvisade), standarden (`produkttexter-standard.md`, avsnitt 1–11), `LARDOMAR.md` och granskarprompten `c_granskarprompt.md`. Extra regler för gruppen: kompatibilitet bara om källan är entydig. Underkänn produkter där fel passform eller fel uppgift kan ge en säkerhetsrisk (däck och slangar med oklara mått, delar till växlar, bromsar och hjul, fästen med lastgräns, belysning, lås och barnprodukter). Där en engelsk butikstitel har översatts har jag kontrollerat typordet.

**Metod:**
- **Källan live:** title, status, productType, vendor, tags, descriptionHtml, seo och variants hämtades med graphql_query (`nodes`) i sex omgångar, en per utkastsfil. Alla 54 är ACTIVE och har tom SEO i dag. Endast 5007 har flera varianter (Default 49 kr, must/hall 79 kr). Endast 5087 har tre varianter (520/521/522, samma pris). Taggen "På beställning" finns på 5007 och 5047, och båda har rätt beställningsmening i standardblocket.
- **Maskinellt:** standardblocket jämfördes tecken för tecken mot `c_1_utkast.json`. 52 är identiska, och 5007 och 5047 har bara den tillåtna meningen om beställningsvaror. Längder, kommatecken och antalet "enligt tillverkaren" per html kontrollerades före och efter rättning. Dubbletter av titel, SEO-titel och meta kontrollerades mot alla `b_*_utkast.json`, `c_*_utkast.json`, `a_*_utkast.json` och `a_skriv.json`. Kontrollskriptet `kontrollera_produkttext.py --seo-title-max 43 --seo-suffix " – BEST OF SPORTS"` kördes på en kopia av de 44 godkända och rättade utkasten efter rättning, med html mappat till `beskrivning` och standardblocket inom `[[STANDARDBLOCK]]`. Resultat: **0 FEL och 48 VARNINGAR** (rubriken "Passar för" i stället för "passar dig som", som i alla facit, och korta texter på tunna källor). Ändringarna i JSON-utlåtandet testades: varje `fore` träffar exakt en gång i utkastet.
- **För hand:** varje titel, SEO-titel, meta och html lästes mot live-källan och språkgranskades.

## Resultat i korthet

| Dom | Antal | Nr |
|---|---|---|
| GODKÄND | 21 | 5009, 5014, 5018, 5019, 5020, 5022, 5026, 5030, 5031, 5032, 5039, 5040, 5043, 5044, 5047, 5052, 5054, 5059, 5063, 5082, 5084 |
| RÄTTA | 23 | 5007, 5011, 5013, 5015, 5016, 5017, 5027, 5029, 5035, 5036, 5045, 5050, 5051, 5060, 5061, 5062, 5064, 5065, 5069, 5075, 5081, 5085, 5086 |
| UNDERKÄND | 10 | 5002, 5006 (slangar med oklara mått), 5003, 5010 (oklar typ, troligen stödben eller växeldel), 5070, 5080 (möjliga dubbletter), 5071, 5077 (väskor med lastgräns 5 kg), 5087 (reflexdekaler med oförklarade varianter), 5088 (husdjursgaller med säkerhetslöfte) |

Totalt: 21 + 23 + 10 = 54.

## Mönster
- **"Enligt tillverkaren" upprepas** i 17 utkast (2–4 gånger per html, ofta både i "Passar för" och i specifikationen). Det var den vanligaste rättningen. Efter rättningen står det högst en gång per html.
- **Typord:** "Pakväska" (från källan) är inte svenska och ska vara "packväska". Framskärmar hade tre olika namn ("Främre Stänkskärm", "Stänkskärm Fram", "Framskärm") och har gjorts lika. ToolShed 6 hade två olika typord i titel och SEO-titel. Engelska butikstitlar är i övrigt rätt översatta: Fender set → Stänkskärmset, Skirt protector → Kjolskydd, Saddle cover → Sadelöverdrag, Bottle holder → Flaskhållare, Bicycle watch → Cykelklocka (ringklocka; måttet 60 mm bekräftar det), Front fender → Framskärm, Tool Kit → Verktygssats, Inner tube → Innerslang.
- **Specifikationsrader med egenskaper i stället för fakta** ("Material: Vattenavvisande", "Material: Stålmaskor", "Handtag: Bekvämt handtag", "Material: Flexibel, lätt plast").
- **Lastgränser som tagits bort i stället för att produkten lyfts:** två väskor (5071, 5077) har "Bärkapacitet 5 kg" i källan. Utkastaren tog bort uppgiften och skrev ändå, medan samma utkastare avvisade 5038 (styrväska 2,5 kg). Det är inkonsekvent, så båda är underkända tills David har beslutat.
- **Dubbletter i butiken:** tre "Proway, Svart/Neongrön" (5054, 5070, 5080). 5070 och 5080 har identisk källa. Utkasten gav alla tre samma titel.
- Inga påhittade tal, ursprung, märkeshistorier, hälsopåståenden eller FAQ. Trasiga källor ("borrmaskin", "puderbräda", "110 cm bred", "linsen") har inte skrivits vidare. Fältet `fakta` har inte jämförts rad för rad. Bedömningen bygger på live-källan.

## Avvisade (b_N_avvisade.json)
Alla 36 avvisningar är rimliga: lås, belysning, barnprodukter, stödben, pedaler, lastbärande korgar och fästen, cykeldator samt produkter som inte är ACTIVE (5004, 5028, 5034 ARCHIVED; 5058, 5072 DRAFT). **Kan släppas:** 5033 (cykelhandskar Liv Energize LF för vuxna, ingen säkerhetsprodukt). Produkten stoppades bara av att kontrollskriptet flaggade modellnamnet "Energize" som ett hälsoord, vilket är falskt positivt. Den behöver ett undantag i skriptet eller Davids ja, eftersom namnet inte får ändras. 5038 (styrväska 2,5 kg) hör ihop med beslutet om 5071 och 5077.

## Öppna frågor till David
1. **Innerslangar:** 5015 och 5060 har entydiga mått och är godkända med rättning. 5002 och 5006 är underkända på grund av motsägande mått. Ska alla slangar ändå tas för hand? Ska typordet vara "Innerslang" eller "Innerdäck" (butiken använder båda)?
2. **Framkorgar utan angiven maxlast** (5011, 5014, 5019, 5020, 5031, 5043) är godkända, eftersom källan inte anger någon last. Korgar och fästen med 5 kg avvisades (5001, 5056). Är en korg på styret en säkerhetsprodukt även när lasten inte anges?
3. **Väskor med lastgräns** (5071, 5077, 5038): ska de släppas med lastuppgiften kvar?
4. **Modellspecifika stänkskärmar** (5065, 5069, Giant Defy/Contend/Avail) och framskärmar som fästs i gaffeln (5030, 5064, 5081) är godkända med passform enligt källan. Vill David ta skärmar som kan komma åt hjulet för hand?
5. **Butiksdata:** möjliga dubbletter 5070 och 5080 (och 5054), SKU och handtag som korsar varandra (5003/5010, 5065/5069), samt priset 1 629 kr på flaskhållaren 5059.

## Tabell
| Nr | Id | Fil | Dom |
|---|---|---|---|
| 5002 | 10470898827530 | b_1_utkast.json | UNDERKÄND |
| 5003 | 10494699372810 | b_1_utkast.json | UNDERKÄND |
| 5006 | 10472186380554 | b_1_utkast.json | UNDERKÄND |
| 5007 | 10472266334474 | b_1_utkast.json | RÄTTA |
| 5009 | 10470929760522 | b_1_utkast.json | GODKÄND |
| 5010 | 10494699340042 | b_1_utkast.json | UNDERKÄND |
| 5011 | 10472293695754 | b_1_utkast.json | RÄTTA |
| 5013 | 10472254439690 | b_1_utkast.json | RÄTTA |
| 5014 | 10475362418954 | b_1_utkast.json | GODKÄND |
| 5015 | 10472256602378 | b_1_utkast.json | RÄTTA |
| 5016 | 10472246739210 | b_2_utkast.json | RÄTTA |
| 5017 | 10472281473290 | b_2_utkast.json | RÄTTA |
| 5018 | 10472243167498 | b_2_utkast.json | GODKÄND |
| 5019 | 10471080296714 | b_2_utkast.json | GODKÄND |
| 5020 | 10472293761290 | b_2_utkast.json | GODKÄND |
| 5022 | 10589582655754 | b_2_utkast.json | GODKÄND |
| 5026 | 10472245199114 | b_2_utkast.json | GODKÄND |
| 5027 | 10472245297418 | b_2_utkast.json | RÄTTA |
| 5029 | 10470899810570 | b_2_utkast.json | RÄTTA |
| 5030 | 10470902890762 | b_2_utkast.json | GODKÄND |
| 5031 | 10472225734922 | b_3_utkast.json | GODKÄND |
| 5032 | 10472249393418 | b_3_utkast.json | GODKÄND |
| 5035 | 10461971480842 | b_3_utkast.json | RÄTTA |
| 5036 | 10472254570762 | b_3_utkast.json | RÄTTA |
| 5039 | 10472246051082 | b_3_utkast.json | GODKÄND |
| 5040 | 10472252834058 | b_3_utkast.json | GODKÄND |
| 5043 | 10475401085194 | b_3_utkast.json | GODKÄND |
| 5044 | 10494701109514 | b_3_utkast.json | GODKÄND |
| 5045 | 10588446392586 | b_3_utkast.json | RÄTTA |
| 5047 | 10472231207178 | b_4_utkast.json | GODKÄND |
| 5050 | 10472246083850 | b_4_utkast.json | RÄTTA |
| 5051 | 10472249983242 | b_4_utkast.json | RÄTTA |
| 5052 | 10472253980938 | b_4_utkast.json | GODKÄND |
| 5054 | 10530129051914 | b_4_utkast.json | GODKÄND |
| 5059 | 10494699241738 | b_4_utkast.json | GODKÄND |
| 5060 | 10411714740490 | b_4_utkast.json | RÄTTA |
| 5061 | 10472246378762 | b_5_utkast.json | RÄTTA |
| 5062 | 10515742753034 | b_5_utkast.json | RÄTTA |
| 5063 | 10462053237002 | b_5_utkast.json | GODKÄND |
| 5064 | 10472231928074 | b_5_utkast.json | RÄTTA |
| 5065 | 10472232681738 | b_5_utkast.json | RÄTTA |
| 5069 | 10472232124682 | b_5_utkast.json | RÄTTA |
| 5070 | 10541369721098 | b_5_utkast.json | UNDERKÄND |
| 5071 | 10472251392266 | b_5_utkast.json | UNDERKÄND |
| 5075 | 10541369655562 | b_5_utkast.json | RÄTTA |
| 5077 | 10472218034442 | b_6_utkast.json | UNDERKÄND |
| 5080 | 10541369622794 | b_6_utkast.json | UNDERKÄND |
| 5081 | 10462177558794 | b_6_utkast.json | RÄTTA |
| 5082 | 10470893584650 | b_6_utkast.json | GODKÄND |
| 5084 | 10472224686346 | b_6_utkast.json | GODKÄND |
| 5085 | 10472264990986 | b_6_utkast.json | RÄTTA |
| 5086 | 10507217633546 | b_6_utkast.json | RÄTTA |
| 5087 | 10665228173578 | b_6_utkast.json | UNDERKÄND |
| 5088 | 10462755356938 | b_6_utkast.json | UNDERKÄND |
## Per produkt (exakt före/efter för RÄTTA)

### 5002 – 10470898827530 – UNDERKÄND
- Utkast: "Innerslang Continental MTB 27,5 tum, Presta-Ventil 42 mm" (b_1_utkast.json)
- Skäl: UNDERKÄND. Innerslang med motsägande mått: originaltiteln anger ETRTO 47/60-584, beskrivningen (47-62x584). Gruppens regel: innerslang med oklara mått underkänns (fel passform kan ge punktering eller att slangen spricker). Behöver entydigt ETRTO från leverantören.

### 5003 – 10494699372810 – UNDERKÄND
- Utkast: "Stöd för Giant Direct Mount KSA, 24–29 tum, 18 mm" (b_1_utkast.json)
- Skäl: UNDERKÄND. Oklar produkttyp. 'Stöd för Giant Direct Mount KSA' med 18 mm bultavstånd ser ut att vara ett stödben (kickstand) som monteras på ramen, och det bär cykelns vikt. Samma serie som 5025 (stödben) och 5042 (KSA 40 mm), som utkastaren själv avvisade. Typordet 'Stöd' är inte begripligt för kunden. Kan inte skrivas säkert utan bekräftad typ och passform.

### 5006 – 10472186380554 – UNDERKÄND
- Utkast: "Innerslang Continental MTB, 26 tum, Presta-Ventil 42 mm" (b_1_utkast.json)
- Skäl: UNDERKÄND. Innerslang med motsägande mått: ETRTO-listan (47–62-559) stämmer med titeln, men de engelska storlekarna omfattar 26x1.375 (smalare än 47 mm) och 'innerbensbredd 1,75 tum' är trasig text. Metan hänvisar dessutom till 'specifikationen'. Oklara mått, så underkänd enligt gruppens regel.

### 5007 – 10472266334474 – RÄTTA
- Utkast: "Flaskhållare Giant Gateway" (b_1_utkast.json)
- Skäl: Variantlåsningen är rätt undviken (Default 49 kr, must/hall 79 kr). Beställningsmeningen i standardblocket stämmer (taggen 'På beställning'). 'Enligt tillverkaren' står två gånger i html: strykt i 'Passar för'. Intervallet skrivs med tankstreck.
- **html 1** före: `Den rymmer flaskor på 500 till 750 ml`
  efter: `Den rymmer flaskor på 500–750 ml`
- **html 2** före: `<li>Dig som cyklar i terräng, enligt tillverkaren</li>`
  efter: `<li>Dig som cyklar i terräng</li>`

### 5009 – 10470929760522 – GODKÄND
- Utkast: "Däcklagningskit Giant" (b_1_utkast.json)
- Skäl: Tunn källa och korrekt hanterad (ingen meta, inget påhittat).

### 5010 – 10494699340042 – UNDERKÄND
- Utkast: "Stöd för Bakväxel Giant Direct Mount KSA, 24–29 tum, 18 mm" (b_1_utkast.json)
- Skäl: UNDERKÄND. Samma oklara produkt som 5003, men butikstiteln säger 'Stöd för bakväxel' (troligen maskinöversättning) medan texten säger stöd för bakhjul. Om det är en del till växeln gäller gruppens regel om växeldelar. Om det är ett stödben är det lastbärande. 'Giant för Giant' är trasig text. SKU 500000012 och handtaget 500000013 överlappar med 5003 (SKU 500000013).

### 5011 – 10472293695754 – RÄTTA
- Utkast: "Framkorg Basil Bilbao FM, utan Handtag, Svart" (b_1_utkast.json)
- Skäl: 'Material: Stålmaskor' anger form, inte material. 'För inköp' är styltigt. Källan anger ingen maxlast (se öppen fråga om framkorgar).
- **html 1** före: `<li>Material: Stålmaskor</li>`
  efter: `<li>Material: Stål</li>`
- **html 2** före: `<li>Dig som vill ha en korg i stålmaskor för inköp</li>`
  efter: `<li>Dig som handlar mat eller går på marknaden</li>`

### 5013 – 10472254439690 – RÄTTA
- Utkast: "Kjolskydd Selle Monte Grappa, Svart, Plast" (b_1_utkast.json)
- Skäl: Kjolskydd är rätt typord för 'Skirt protector'. 'Enligt tillverkaren' står två gånger i html.
- **html** före: `<li>Dig som vill skydda kjol, kappa eller andra lösa plagg från kedjan, enligt tillverkaren</li>`
  efter: `<li>Dig som vill skydda kjol, kappa eller andra lösa plagg från kedjan</li>`

### 5014 – 10475362418954 – GODKÄND
- Utkast: "Cykelkorg Fram Basil Bremen Alu, Löstagbar" (b_1_utkast.json)
- Skäl: Stämmer mot källan. 'Alu' behålls som en del av modellnamnet utan att materialet påstås.

### 5015 – 10472256602378 – RÄTTA
- Utkast: "Innerslang Continental, 29 tum, Presta-Ventil 42 mm" (b_1_utkast.json)
- Skäl: Måtten är entydiga: ETRTO 47/62-622 i titeln stämmer med 28/29 x 1.90/2.40 (47–62 mm). Därför godkänd mot gruppens regel, med rättning. ETRTO är den uppgift som avgör passformen, så den ska stå i titeln. Metan hade UNI-nummer och arbetsfrasen 'anges som'. Ändringen från 'Innerdäck' till 'Innerslang' är godtagbar (båda är svenska, och produkttypen är oförändrad).
- **titel** före: `Innerslang Continental, 29 tum, Presta-Ventil 42 mm`
  efter: `Innerslang Continental 29 tum, 47/62-622, Presta-Ventil 42 mm`
- **meta** före: `Continental innerslang för 29 tum är svart och har Presta-ventil på 42 mm. Modellen anges som 28/29 x 1,90/2,40 och har UNI-nummer CO0182181.`
  efter: `Continental innerslang för 29 tum har ETRTO 47/62-622 och Presta-ventil på 42 mm. Slangen är svart och avsedd för storleken 28/29 x 1,90–2,40.`
- **html** före: `Modellen anges som 28/29 x 1,90/2,40.`
  efter: `Slangen har ETRTO 47/62-622 och storleken 28/29 x 1,90–2,40.`

### 5016 – 10472246739210 – RÄTTA
- Utkast: "Stänkskärmset Hebie Taipan, 24 tum, Svart" (b_2_utkast.json)
- Skäl: 'Enligt tillverkaren' står tre gånger i html. Kvar står det en gång, i inledningen.
- **html 1** före: `<li>Dig som söker stänkskärmar till 24-tums hjul, enligt tillverkaren</li>`
  efter: `<li>Dig som söker stänkskärmar till 24-tums hjul</li>`
- **html 2** före: `<li>Hjulstorlek: 24 tum (enligt tillverkaren passar setet nästan alla 24-tums hjul)</li>`
  efter: `<li>Hjulstorlek: 24 tum</li>`

### 5017 – 10472281473290 – RÄTTA
- Utkast: "Stänkskärmset Hebie Viper, 26–29 tum, Svart" (b_2_utkast.json)
- Skäl: 'Enligt tillverkaren' står fyra gånger i html. 'Stänkskärmset för mountainbikes i plast' kan läsas som att cykeln är av plast. Hjulstorleken 26–29 tum är en specifikation och behöver ingen hänvisning till tillverkaren.
- **html 1** före: `Hebie Viper är ett svart stänkskärmset för mountainbikes i plast. Enligt tillverkaren är det designat för 26–29-tums hjul och fästs nära däcket.`
  efter: `Hebie Viper är ett svart stänkskärmset i plast för mountainbikes. Det är designat för 26–29-tums hjul och fästs nära däcket.`
- **html 2** före: `<li>Dig som söker stänkskärmar till mountainbikes med 26–29-tums hjul, enligt tillverkaren</li>`
  efter: `<li>Dig som har en mountainbike med 26–29-tums hjul</li>`
- **html 3** före: `<li>Dig som vill ha ett skydd mot vatten och smuts, enligt tillverkaren</li>`
  efter: `<li>Dig som vill ha ett skydd mot vatten och smuts</li>`

### 5018 – 10472243167498 – GODKÄND
- Utkast: "Stänkskärmset Hebie Viper X MTB, 24–28 tum, Svart" (b_2_utkast.json)
- Skäl: Stämmer. 24–28 tum och MTB kommer från originaltiteln. Vikten 210 g för bakskärmen bekräftas av 5022.

### 5019 – 10471080296714 – GODKÄND
- Utkast: "Framkorg Basil Bilbao BE för Styrstam, med Handtag, Svart" (b_2_utkast.json)
- Skäl: Stämmer. Ingen maxlast i källan (öppen fråga om framkorgar).

### 5020 – 10472293761290 – GODKÄND
- Utkast: "Framkorg Basil Bilbao KF, med Handtag, Svart" (b_2_utkast.json)
- Skäl: Stämmer mot titeln. Brödtexten är kopierad från FM-modellen, men måtten (28 cm) och fästena som säljs separat skiljer sig från FM (5011) och är rimliga för KF.

### 5022 – 10589582655754 – GODKÄND
- Utkast: "Bakskärm Hebie Viper X för Sadelstolpe" (b_2_utkast.json)
- Skäl: Stämmer. Den trasiga titeln ('26"-') är rätt utelämnad.

### 5026 – 10472245199114 – GODKÄND
- Utkast: "Stänkskärmset Hebie Taipan Trekking, 28 tum, Svart" (b_2_utkast.json)
- Skäl: Stämmer.

### 5027 – 10472245297418 – RÄTTA
- Utkast: "Stänkskärmset Hebie Viper S, 26–29 tum, Svart" (b_2_utkast.json)
- Skäl: 'Enligt tillverkaren' står två gånger i html. Det oklara måttet (90 cm/65 mm) är rätt utelämnat.
- **html** före: `<li>Dig som söker stänkskärmar till cyklar i storlekarna 26–29 tum, enligt tillverkaren</li>`
  efter: `<li>Dig som söker stänkskärmar till cyklar i storlekarna 26–29 tum</li>`

### 5029 – 10470899810570 – RÄTTA
- Utkast: "Stänkskärmset Hebie Viper X Stealth, 26–29 tum, MTB" (b_2_utkast.json)
- Skäl: 'Enligt tillverkaren' står två gånger i html. Trasiga uppgifter ('110 cm bred', 'borrsats') är rätt utelämnade.
- **html** före: `<li>Dig som vill ha ett set med ett extra brett skyddsområde, enligt tillverkaren</li>`
  efter: `<li>Dig som vill ha stänkskärmar med extra brett skyddsområde</li>`

### 5030 – 10470902890762 – GODKÄND
- Utkast: "Framskärm Hebie Viper X med Adaptrar" (b_2_utkast.json)
- Skäl: Stämmer mot titeln trots 'borrmaskin' i källan (maskinöversättning). Bredden 56–70 mm med adaptrar och den oklara klämraden är rätt hanterade.

### 5031 – 10472225734922 – GODKÄND
- Utkast: "Cykelkorg Fram Basil Bremen Rattan Look KF, Seagrass" (b_3_utkast.json)
- Skäl: Stämmer. Den motsägande färgen (ljusbrun/havsgrå), den oklara storleken och 'linsen' är rätt utelämnade.

### 5032 – 10472249393418 – GODKÄND
- Utkast: "Cykelklocka Basil Noir, Silverfärgad" (b_3_utkast.json)
- Skäl: 'Bicycle watch' är en maskinöversättning av cykelklocka (ringklocka). Måttet 60 mm stämmer med det, och typordet är rätt.

### 5035 – 10461971480842 – RÄTTA
- Utkast: "Sadelöverdrag Basil GO" (b_3_utkast.json)
- Skäl: 'Enligt tillverkaren' står två gånger i html. Det motsägande materialet (gummi/polyester) är rätt utelämnat.
- **html** före: `<li>Skydd: Mot regn, smuts och damm, enligt tillverkaren</li>`
  efter: `<li>Skydd: Regn, smuts och damm</li>`

### 5036 – 10472254570762 – RÄTTA
- Utkast: "Sadel Selle Monte Grappa Feliz, Grå" (b_3_utkast.json)
- Skäl: Specifikationsraden innehöll en hel mening om bilden. Den blir en kort anmärkning.
- **html** före: `<li>Färg: Grå. Bilden är illustrativ och färgen kan variera.</li>`
  efter: `<li>Färg: Grå (färgen kan variera)</li>`

### 5039 – 10472246051082 – GODKÄND
- Utkast: "Flaskhållare Giant Airway Sport, Vit och Blå" (b_3_utkast.json)
- Skäl: Tunn källa och korrekt hanterad. Källan anger nylon och 41 g, vilket hade kunnat stå med, men utelämningen är försiktig och godtas.

### 5040 – 10472252834058 – GODKÄND
- Utkast: "Flaskhållare Giant Airway Sport, Vit och Röd" (b_3_utkast.json)
- Skäl: Tunn källa och korrekt hanterad.

### 5043 – 10475401085194 – GODKÄND
- Utkast: "Cykelkorg Fram Basil Bremen Rattan Look KF, Löstagbar" (b_3_utkast.json)
- Skäl: Stämmer. 'Fästs i styrstammen' är rätt utelämnat (osäkert).

### 5044 – 10494701109514 – GODKÄND
- Utkast: "Regnskydd för Cykelväska Basil Keep Dry & Clean" (b_3_utkast.json)
- Skäl: Stämmer. Synlighetspåståendet och det orimliga måttet är rätt utelämnade.

### 5045 – 10588446392586 – RÄTTA
- Utkast: "Verktygssats Giant ToolShed 6" (b_3_utkast.json)
- Skäl: Typordet var inkonsekvent: titeln sade 'Verktygssats', SEO-titeln och texten 'multiverktyg'. Källtexten kallar produkten multiverktyg med sex tillbehör, och det stämmer med produkten. 'Enligt tillverkaren' stod två gånger. SEO-titeln blir identisk med titeln (lagras tom, avsett beteende).
- **titel** före: `Verktygssats Giant ToolShed 6`
  efter: `Multiverktyg Giant ToolShed 6`
- **html** före: `<li>Yta: Nickelpläterad, enligt tillverkaren korrosionsbeständig</li>`
  efter: `<li>Yta: Nickelpläterad</li>`

### 5047 – 10472231207178 – GODKÄND
- Utkast: "Sadelöverdrag Basil Noir" (b_4_utkast.json)
- Skäl: Stämmer. Beställningsmeningen är rätt (taggen 'På beställning').

### 5050 – 10472246083850 – RÄTTA
- Utkast: "Flaskhållare Giant Airway Sport, Röd och Blanksvart" (b_4_utkast.json)
- Skäl: 'Passar för' hade två fragment som saknade 'Dig som' och tre förekomster av 'enligt tillverkaren'.
- **html 1** före: `<li>Cyklar med små ramar, enligt tillverkaren</li>`
  efter: `<li>Dig som har en cykel med liten ram</li>`
- **html 2** före: `<li>Terrängcykling, enligt tillverkaren</li>`
  efter: `<li>Dig som cyklar i terräng</li>`

### 5051 – 10472249983242 – RÄTTA
- Utkast: "Pakväska Basil Kavan Eco Classic, 68 l, Svart" (b_4_utkast.json)
- Skäl: 'Pakväska' (från källan) är inte svenska. Det svenska ordet är 'packväska'. Rättas i titel, SEO-titel, meta och html. Garantin på 10 år och 'Eco' är rätt utelämnade.
- **titel** före: `Pakväska Basil Kavan Eco Classic, 68 l, Svart`
  efter: `Packväska Basil Kavan Eco Classic, 68 l, Svart`
- **seo_title** före: `Pakväska Basil Kavan Eco Classic`
  efter: `Packväska Basil Kavan Eco Classic`
- **meta** före: `är en dubbel pakväska på 68 liter`
  efter: `är en dubbel packväska på 68 liter`
- **html 1** före: `är en dubbel pakväska med en kapacitet`
  efter: `är en dubbel packväska med en kapacitet`
- **html 2** före: `<li>Typ: Dubbel pakväska</li>`
  efter: `<li>Typ: Dubbel packväska</li>`

### 5052 – 10472253980938 – GODKÄND
- Utkast: "Sadel Selle Monte Grappa Venice i Retrostil" (b_4_utkast.json)
- Skäl: Stämmer. Den motsägande färgen och 'Tillverkad i Italien' är rätt utelämnade.

### 5054 – 10530129051914 – GODKÄND
- Utkast: "Flaskhållare Giant ProWay, Svart och Neongrön" (b_4_utkast.json)
- Skäl: Stämmer ('Bottle holder' är rätt översatt). Titeln blir unik när 5070 och 5080 är underkända.

### 5059 – 10494699241738 – GODKÄND
- Utkast: "Flaskhållare Giant AirWay Lite i Kolfiber, Svart" (b_4_utkast.json)
- Skäl: Stämmer. Priset 1 629 kr har flaggats (troligen fel pris i butiken).

### 5060 – 10411714740490 – RÄTTA
- Utkast: "Innerdäck Continental Compact 18, 18 tum, Autoventil" (b_4_utkast.json)
- Skäl: Måtten är entydiga (32-355 till 47-400 i både titel och text). Godkänd mot gruppens regel, men David kan välja att ta alla slangar för hand. 'Auto/chrader' är en felstavning i källan och skrivs 'autoventil'. 'Hög motståndskraft mot punkteringar' är ett säkerhetslöfte utan entydig källa (standarden avsnitt 10) och tas bort ur 'Passar för' och specifikationen. Typordet 'Innerdäck' här och 'Innerslang' i 5002, 5006 och 5015 bör enhetliggöras (David väljer).
- **html 1** före: `och ventilen är av typen auto/chrader, 40 mm lång.`
  efter: `och ventilen är en autoventil på 40 mm.`
- **html 2** före: `<li>Dig som söker ett innerdäck med autoventil (auto/chrader)</li>`
  efter: `<li>Dig som söker ett innerdäck med autoventil</li>`
- **html 3** före: `⏎<li>Dig som vill ha ett innerdäck med hög motståndskraft mot punkteringar, enligt tillverkaren</li>`
  efter: *(tas bort)*
- **html 4** före: `<li>Ventiltyp: Auto/Chrader</li>`
  efter: `<li>Ventiltyp: Autoventil</li>`
- **html 5** före: `⏎<li>Egenskap enligt tillverkaren: Hög motståndskraft mot punkteringar</li>`
  efter: *(tas bort)*

### 5061 – 10472246378762 – RÄTTA
- Utkast: "Flaskhållare Giant Airway Sport, Blå och Blanksvart" (b_5_utkast.json)
- Skäl: Metan slutade med ett verblöst fragment ('Vikt 41 g.'). 'Enligt tillverkaren' stod två gånger i html, och 'cyklar på en cykel' är en upprepning.
- **meta** före: `Giant Airway Sport är en flaskhållare i nylon i blått och blanksvart. Enligt tillverkaren passar den cyklar med små ramar och terrängcykling. Vikt 41 g.`
  efter: `Giant Airway Sport är en flaskhållare i nylon i blått och blanksvart som väger 41 g. Enligt tillverkaren passar den små ramar och terrängcykling.`
- **html 1** före: `<li>Dig som cyklar på en cykel med liten ram, enligt tillverkaren</li>`
  efter: `<li>Dig som har en cykel med liten ram, enligt tillverkaren</li>`
- **html 2** före: `<li>Dig som terrängcyklar och vill ha en flaskhållare i nylon, enligt tillverkaren</li>`
  efter: `<li>Dig som cyklar i terräng och vill ha en flaskhållare i nylon</li>`

### 5062 – 10515742753034 – RÄTTA
- Utkast: "Cykelklocka Giant Ding-a-Ling, Silver" (b_5_utkast.json)
- Skäl: 'Enligt tillverkaren' står två gånger i html.
- **html** före: `<li>Funktion: Ringer två gånger vid ett tryck på spaken, enligt tillverkaren</li>`
  efter: `<li>Funktion: Ringer två gånger vid ett tryck på spaken</li>`

### 5063 – 10462053237002 – GODKÄND
- Utkast: "Verktygssats Giant Toolshed 12" (b_5_utkast.json)
- Skäl: Stämmer. Måttet markerat (TBC) är rätt utelämnat.

### 5064 – 10472231928074 – RÄTTA
- Utkast: "Främre Stänkskärm Giant Speedshield Clip-On" (b_5_utkast.json)
- Skäl: Typordet var inte enhetligt i gruppen: 'Främre Stänkskärm' här, 'Stänkskärm Fram' i 5081 och 'Framskärm' i 5030 (Hebie). Framskärm används överallt. 'Enligt tillverkaren' stod tre gånger. Tillverkarens materialpåståenden flyttas från specifikationen till inledningen.
- **titel** före: `Främre Stänkskärm Giant Speedshield Clip-On`
  efter: `Framskärm Giant Speedshield Clip-On`
- **seo_title** före: `Främre Stänkskärm Giant Speedshield`
  efter: `Framskärm Giant Speedshield Clip-On`
- **html 1** före: `Giant Speedshield Clip-On är en stänkskärm som monteras med kardborreband. Den är gjord i PP-material och är enligt tillverkaren avsedd för mountainbikes och hybridcyklar.`
  efter: `Giant Speedshield Clip-On är en framskärm i PP-plast som monteras med kardborreband. Den är avsedd för mountainbikes och hybridcyklar, och materialet är enligt tillverkaren UV-beständigt, värmebeständigt och flexibelt.`
- **html 2** före: `<li>Dig som har en mountainbike eller hybridcykel, enligt tillverkaren</li>`
  efter: `<li>Dig som har en mountainbike eller hybridcykel</li>`
- **html 3** före: `<li>Material: PP-plast, UV-beständigt, värmebeständigt och flexibelt, enligt tillverkaren</li>`
  efter: `<li>Material: PP-plast</li>`

### 5065 – 10472232681738 – RÄTTA
- Utkast: "Stänkskärmar Giant Speedshield Defy & Contend Disc" (b_5_utkast.json)
- Skäl: 'Enligt tillverkaren' står fyra gånger i html. Källan säger 'hjul' och 'skivor' (maskinöversättning), men titeln är entydig: stänkskärmar. Passformen per Giant-modell står entydigt i källan. Se öppen fråga om modellspecifika skärmar.
- **html 1** före: `är stänkskärmar för hjul med skivbromsar. Enligt tillverkaren är de lämpliga för 700c x 23–25 mm.`
  efter: `är stänkskärmar för hjul i 700c x 23–25 mm med skivbromsar. Enligt tillverkaren passar de Giant-modellerna Defy, Contend och Avail.`
- **html 2** före: `<li>Dig som har en Giant Defy, Contend eller Avail, enligt tillverkaren</li>`
  efter: `<li>Dig som har en Giant Defy, Contend eller Avail med skivbromsar</li>`
- **html 3** före: `<li>Hjulstorlek: 700c x 23–25 mm, enligt tillverkaren</li>`
  efter: `<li>Hjulstorlek: 700c x 23–25 mm</li>`
- **html 4** före: `<li>Passar Giant-modeller: Defy, Contend och Avail, enligt tillverkaren</li>`
  efter: `<li>Passar Giant-modeller: Defy, Contend och Avail</li>`

### 5069 – 10472232124682 – RÄTTA
- Utkast: "Stänkskärmar Giant Speedshield Defy & Contend Caliper" (b_5_utkast.json)
- Skäl: Samma rättning som 5065. Handtaget slutar på 530000035, som är Disc-produktens SKU. Det bör kontrolleras.
- **html 1** före: `är stänkskärmar för hjul med Caliper-bromsar. Enligt tillverkaren är de lämpliga för 700c x 23–28 mm.`
  efter: `är stänkskärmar för hjul i 700c x 23–28 mm med Caliper-bromsar. Enligt tillverkaren passar de Giant-modellerna Defy, Contend och Avail.`
- **html 2** före: `<li>Dig som har en Giant Defy, Contend eller Avail, enligt tillverkaren</li>`
  efter: `<li>Dig som har en Giant Defy, Contend eller Avail med Caliper-bromsar</li>`
- **html 3** före: `<li>Hjulstorlek: 700c x 23–28 mm, enligt tillverkaren</li>`
  efter: `<li>Hjulstorlek: 700c x 23–28 mm</li>`
- **html 4** före: `<li>Passar Giant-modeller: Defy, Contend och Avail, enligt tillverkaren</li>`
  efter: `<li>Passar Giant-modeller: Defy, Contend och Avail</li>`

### 5070 – 10541369721098 – UNDERKÄND
- Utkast: "Flaskhållare Giant Proway, Svart och Neongrön" (b_5_utkast.json)
- Skäl: UNDERKÄND (möjlig dubblett). Live-källan är ordagrant identisk med 5080 (samma titel 'Flaskhållare GIANT Proway, Svart/Neongrön', samma text, samma pris 109 kr; SKU 490000071 mot 490000074). Utkastets titel är identisk med 5054 och 5080. Titeln ska vara unik i sortimentet, men produkterna går inte att skilja åt utan nya uppgifter. David eller leverantören avgör vilken som är rätt produkt.

### 5071 – 10472251392266 – UNDERKÄND
- Utkast: "Handväska Basil Bloom Field, 8–11 L, Blå och Blommig" (b_5_utkast.json)
- Skäl: UNDERKÄND. Väska som fästs på styret eller pakethållaren och har bärkapaciteten 5 kg i källan (fäste med lastgräns). Utkastet har tagit bort lastuppgiften, vilket döljer en säkerhetsrelevant gräns. Samma kategori som 5038 (styrväska 2,5 kg), som utkastaren avvisade. Kan släppas om David bedömer att väskor med lastuppgift inte räknas som säkerhetsprodukter. I så fall ska 'Bärkapacitet: Upp till 5 kg' stå med, och titelns '8–11 L' ska skrivas med liten bokstav ('8–11 l').

### 5075 – 10541369655562 – RÄTTA
- Utkast: "Flaskhållare Giant Proway, Svart och Neongul" (b_5_utkast.json)
- Skäl: 'Material: Flexibel, lätt plast' innehåller egenskaper, inte bara material.
- **html** före: `<li>Material: Flexibel, lätt plast</li>`
  efter: `<li>Material: Plast</li>`

### 5077 – 10472218034442 – UNDERKÄND
- Utkast: "Cykelväska Basil Sport Design Commuter Bag, 18 l" (b_6_utkast.json)
- Skäl: UNDERKÄND. Väska som hängs på cykelramen eller pakethållaren, med bärkapaciteten 5 kg i källan. Lastuppgiften är bortplockad. Samma bedömning och villkor för att släppa den som 5071.

### 5080 – 10541369622794 – UNDERKÄND
- Utkast: "Flaskhållare Giant Proway, Svart och Neongrön" (b_6_utkast.json)
- Skäl: UNDERKÄND (möjlig dubblett). Se 5070: identisk källa och samma titel, färg och pris. Titeln dubblerar 5054 och 5070.

### 5081 – 10462177558794 – RÄTTA
- Utkast: "Stänkskärm Fram Giant Swift, 28 tum, Aluminium" (b_6_utkast.json)
- Skäl: Typordet blir 'Framskärm' (se 5064). 'Passar för' hade ett fragment utan 'Dig som' och två förekomster av 'enligt tillverkaren'.
- **titel** före: `Stänkskärm Fram Giant Swift, 28 tum, Aluminium`
  efter: `Framskärm Giant Swift, 28 tum, Aluminium`
- **seo_title** före: `Stänkskärm Fram Giant Swift, 28 tum`
  efter: `Framskärm Giant Swift, 28 tum`
- **html 1** före: `<li>Stads- och touringcyklister, enligt tillverkaren</li>`
  efter: `<li>Dig som cyklar i stan eller på långtur</li>`
- **html 2** före: `<li>Typ: Främre stänkskärm</li>`
  efter: `<li>Typ: Framskärm</li>`

### 5082 – 10470893584650 – GODKÄND
- Utkast: "Verktygssats Giant Toolshed 13, 13 Delar" (b_6_utkast.json)
- Skäl: Stämmer. Verktygslistan ger 13 delar.

### 5084 – 10472224686346 – GODKÄND
- Utkast: "Sadelväska Basil Discovery 365D, M, 1 l" (b_6_utkast.json)
- Skäl: Stämmer. Den motsägande färgen och det trasiga 'vattentät x3' är rätt utelämnade.

### 5085 – 10472264990986 – RÄTTA
- Utkast: "Golvpump Giant Control Tower Pro 2 Stage" (b_6_utkast.json)
- Skäl: 'Handtag: Bekvämt handtag' är en värdering och ingen specifikation. 'Stage' är rätt lämnat oförklarat.
- **html** före: `⏎<li>Handtag: Bekvämt handtag</li>`
  efter: *(tas bort)*

### 5086 – 10507217633546 – RÄTTA
- Utkast: "Sadelväska Basil Mada, 1–1,5 l" (b_6_utkast.json)
- Skäl: 'Material: Vattenavvisande' är en egenskap och inget material. Kapacitetsraden upprepade sig.
- **html 1** före: `<li>Kapacitet: 1–1,5 l, kan utökas upp till 1,5 l</li>`
  efter: `<li>Kapacitet: 1 l, kan utökas till 1,5 l</li>`
- **html 2** före: `<li>Material: Vattenavvisande</li>`
  efter: `<li>Egenskap: Vattenavvisande material</li>`

### 5087 – 10665228173578 – UNDERKÄND
- Utkast: "Reflekterande Klistermärken för Cykel Bookman, Black Flames" (b_6_utkast.json)
- Skäl: UNDERKÄND. Reflexdekaler: köparen väljer dem för synligheten (närliggande belysning; synlighetspåståendet har rätt utelämnats). Tre varianter, 520, 521 och 522, har samma pris men oförklarade namn, och titeln låser 'Black Flames'. Källan säger att dekalerna kan sättas på hjälmen (utelämnat, men risken bör David känna till). Antal, mått och material saknas. Metans andra mening ('sidodekaler som enligt tillverkaren sätts på cykeln') säger ingenting. Kan släppas om varianterna förklaras och David godtar reflexer i vågor.

### 5088 – 10462755356938 – UNDERKÄND
- Utkast: "Korggaller Basil Pluto XL, Stål" (b_6_utkast.json)
- Skäl: UNDERKÄND. Galler till cykelkorgen för husdjur. Enligt källan hindrar det djuret från att hoppa ur korgen under färden, vilket är ett säkerhetslöfte om djuret och cyklisten. Det framgår inte vilken korg gallret passar, och måtten 13 x 23 x 20 cm förklaras inte. Ett säkerhetslöfte utan entydig passform tas bort enligt standarden avsnitt 10, och då blir texten för tunn.
