# Granskning våg 2, utkast b_7–b_9 (Velomarket-cykeltillbehör) – BEST OF SPORTS (2026-11-03)

Det här är en oberoende granskning. Jag har bara läst i Shopify och har inte ändrat någon utkastsfil. Butiken kontrollerades först med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK).

**Underlag:** `vag2_skriv/b_7_utkast.json`, `b_8_utkast.json`, `b_9_utkast.json` (54 utkast, nr 5201–5275), `b_7_avvisade.json`–`b_9_avvisade.json` (21 avvisade), standarden (`produkttexter-standard.md`, avsnitt 1–11), `LARDOMAR.md`, granskarprompten `c_granskarprompt.md` och det förra utlåtandet `vag2_b_granskning_1_6.md`, så att bedömningarna blir lika. Beslut av David som gäller: framkorgar utan lastuppgift, stänkskärmar och framskärmar med kompatibilitet "enligt tillverkaren" och innerslangar med ETRTO i titeln är tillåtna. Belysning, lås, barnprodukter, bromsar och växeldelar, pedaler och vevar samt väskor och korgar med lastgräns underkänns. Kompatibilitet får bara stå om källan är entydig.

**Metod:**
- **Källan live:** title, handle, status, productType, vendor, tags, descriptionHtml, seo och variants hämtades med graphql_query (`nodes`) i fyra omgångar. Alla 54 är ACTIVE och har tom SEO. Flera varianter: 5205 (269/299 kr), 5209 (273/275), 5215 (520–522), 5240 (black/black (0784)). Taggen "På beställning" finns på 5205, 5239 och 5262.
- **Maskinellt:** standardblocket jämfördes tecken för tecken mot `c_1_utkast.json`. 52 är identiska, och 5239 och 5262 har bara den tillåtna meningen om beställningsvaror. **5205 saknar meningen fast den har taggen** (rättas). Varje `fore` i JSON-utlåtandet träffar exakt en gång i utkastet. Efter rättning kontrollerades längder (titel högst 70 tecken och 2 kommatecken, SEO-titel högst 43, meta 130–155 eller null) och dubbletter av titel, SEO-titel och meta mot alla `b_*_utkast.json`, `c_*_utkast.json`, `b_skriv.json`, `b_skriv_hold_frisläppta.json`, `c_skriv_resten_*.json` och `a_skriv.json`. Resultat: inga dubbletter och inga längdfel. Kontrollskriptet `shopify-sync/scripts/kontrollera_produkttext.py --seo-title-max 43 --seo-suffix " – BEST OF SPORTS"` kördes på en kopia av de 40 godkända och rättade utkasten efter rättning, med html mappat till `beskrivning` och standardblocket inom `[[STANDARDBLOCK]]`. Resultat: **0 FEL och 43 VARNINGAR** (rubriken "Passar för" i stället för "passar dig som", som i facit, och två korta texter på tunna källor, 5270 och 5275).
- **För hand:** varje titel, SEO-titel, meta och html lästes mot live-källan och språkgranskades. Fältet `fakta` har inte jämförts rad för rad, eftersom bedömningen bygger på live-källan.

## Resultat i korthet

| Dom | Antal | Nr |
|---|---|---|
| GODKÄND | 21 | 5202, 5203, 5214, 5216, 5219, 5221, 5222, 5224, 5226, 5227, 5240, 5245, 5250, 5251, 5262, 5263, 5265, 5266, 5269, 5270, 5274 |
| RÄTTA | 19 | 5201, 5204, 5205, 5208, 5210, 5211, 5212, 5213, 5234, 5235, 5236, 5239, 5244, 5246, 5248, 5249, 5259, 5268, 5275 |
| UNDERKÄND | 14 | 5206, 5209, 5215, 5238, 5252, 5253, 5254, 5255, 5256, 5257, 5258, 5264, 5267, 5273 |

Totalt: 21 + 19 + 14 = 54.

## Mönster
- **Utkastaren tog med produkter som Davids beslut underkänner**, och var inkonsekvent mot sina egna avvisningar: pedaler 5267 och 5273 (5217 och 5241 avvisades), barnprodukter 5252 och 5253 (barnkorg 5247 och klockor 5228–5229 avvisades) och 5256 (flaska "designad för barncyklar"), samt Hebie Alumee 5257 och 5258, där lastuppgiften 8 kg per sida togs bort i stället för att produkten lyftes (5233 avvisades av samma skäl).
- **Reflexer** (5209, 5215, 5254, 5255, 5264) är underkända på samma sätt som 5087 i b_1–b_6. Källorna lovar säkerhet och synlighet ("ökar säkerheten", "syns i mörkret") och nämner hjälm eller barnvagn. Davids beslut nämner inte reflexer, så frågan behöver ett beslut.
- **Djurgaller** 5206 har samma säkerhetslöfte som 5088, och lådan för pakethållare 5238 har en motsägelsefull källa och omfattas inte av beslutet om framkorgar.
- **Språk:** "Selle Monte Grappa är ett kjolskydd" (märket i stället för produkten, 5248 och 5249), genus som växlar ("ett styretape … Tapen", 5268), upprepningar ("skydd … ger skydd", "snabbt avtagbar, så den går att ta av") och "27,5 tum … hjul". Stavningen "stänkskärmsset"/"Stänkskärmset" växlade inom samma utkast (5204).
- **Kompatibilitet som inte är entydig** togs bort: "passar alla typer av cyklar" (5275), "25–27 tums hjul" där källan bara säger "25–27 tums stadscyklar" (5248, 5249) och "cykeln ryms i måtten" (5235).
- **Engelska och trasiga butikstitlar är rätt översatta:** Bicycle at → Cykelklocka (ringklocka enligt text och tagg), Saddle bag → Sadelväska, Rear Fender → Bakskärm, Fender set → Stänkskärmset, Bicycle Cover → Cykelskydd, Fatbike fenders → Stänkskärmar för fatbike, Fenders → Stänkskärmar, Skirt protector → Kjolskydd, Floor pump → Golvpump, Front fender → Framskärm, Scraper acrylic → Skrapa i akryl. Undantag: "Styckväska" (5211) blev det för allmänna "Väska" och rättas till Cykelväska.
- Inga påhittade tal, ursprung, märkeshistorier, hälsopåståenden eller FAQ. Trasiga källor ("rullstolssadel", "Lens Bag", "doktorförslutning", "grepp om linsen", "front porch", chattkod i 5274) har inte skrivits vidare. Variantlåsning är rätt undviken i 5205 och 5240.

## Avvisade (b_N_avvisade.json)
Alla 21 avvisningar är rimliga enligt Davids beslut: barnprodukter (5207, 5220, 5228, 5229, 5230, 5247, 5260, 5272), pedaler (5217, 5241), väskor och korgar med lastgräns (5218, 5225, 5232, 5237), stänkskärmset med last 8 kg (5233), lås (5231) och belysning (5223, 5242, 5243, 5261, 5271). Ingen avvisad produkt kan släppas.

## Öppna frågor till David
1. **Reflexer** (5209, 5215, 5254, 5255, 5264 och tidigare 5087): ska reflexdekaler och reflexband räknas som säkerhetsprodukter (som belysning) eller släppas utan synlighetslöften? 5209 och 5215 har dessutom oförklarade varianter.
2. **Bakre korgar och lådor på pakethållaren utan lastuppgift** (5275 rättad och godkänd, 5238 underkänd): gäller beslutet om framkorgar även dem?
3. **Typord för styrlinda:** "Handtagstejp" (5245) och "Styretape" (5268) är samma produkttyp. Ska båda heta "Styrlinda"?
4. **Butiksdata att kontrollera:** handtag som inte stämmer med SKU (5213 mot 750 ml-flaskan, 5234, 5244), priserna 1 569 kr (5211) och 1 589 kr (5273), felaktiga taggar "Cykelbelysning" (5214, 5249), chattkod i källtexten till 5274, och 5224 (skidskrapa) bland cykeltillbehören.

## Tabell
| Nr | Id | Fil | Dom |
|---|---|---|---|
| 5201 | 10472284422410 | b_7_utkast.json | RÄTTA |
| 5202 | 10472292647178 | b_7_utkast.json | GODKÄND |
| 5203 | 10472347042058 | b_7_utkast.json | GODKÄND |
| 5204 | 10589571744010 | b_7_utkast.json | RÄTTA |
| 5205 | 10461953425674 | b_7_utkast.json | RÄTTA |
| 5206 | 10462230970634 | b_7_utkast.json | UNDERKÄND |
| 5208 | 10470936740106 | b_7_utkast.json | RÄTTA |
| 5209 | 10471174668554 | b_7_utkast.json | UNDERKÄND |
| 5210 | 10472232059146 | b_7_utkast.json | RÄTTA |
| 5211 | 10472249524490 | b_7_utkast.json | RÄTTA |
| 5212 | 10475415044362 | b_7_utkast.json | RÄTTA |
| 5213 | 10494699208970 | b_7_utkast.json | RÄTTA |
| 5214 | 10541370212618 | b_7_utkast.json | GODKÄND |
| 5215 | 10665228075274 | b_7_utkast.json | UNDERKÄND |
| 5216 | 10470910624010 | b_7_utkast.json | GODKÄND |
| 5219 | 10472253358346 | b_7_utkast.json | GODKÄND |
| 5221 | 10472485519626 | b_7_utkast.json | GODKÄND |
| 5222 | 10565562007818 | b_7_utkast.json | GODKÄND |
| 5224 | 10472217477386 | b_7_utkast.json | GODKÄND |
| 5226 | 10472232091914 | b_8_utkast.json | GODKÄND |
| 5227 | 10472246771978 | b_8_utkast.json | GODKÄND |
| 5234 | 10494689411338 | b_8_utkast.json | RÄTTA |
| 5235 | 10635765743882 | b_8_utkast.json | RÄTTA |
| 5236 | 10472224653578 | b_8_utkast.json | RÄTTA |
| 5238 | 10472293957898 | b_8_utkast.json | UNDERKÄND |
| 5239 | 10475364909322 | b_8_utkast.json | RÄTTA |
| 5240 | 10475428872458 | b_8_utkast.json | GODKÄND |
| 5244 | 10468721033482 | b_8_utkast.json | RÄTTA |
| 5245 | 10470908264714 | b_8_utkast.json | GODKÄND |
| 5246 | 10472249753866 | b_8_utkast.json | RÄTTA |
| 5248 | 10472253653258 | b_8_utkast.json | RÄTTA |
| 5249 | 10472254177546 | b_8_utkast.json | RÄTTA |
| 5250 | 10472254669066 | b_8_utkast.json | GODKÄND |
| 5251 | 10472254898442 | b_9_utkast.json | GODKÄND |
| 5252 | 10472256143626 | b_9_utkast.json | UNDERKÄND |
| 5253 | 10472286224650 | b_9_utkast.json | UNDERKÄND |
| 5254 | 10472303067402 | b_9_utkast.json | UNDERKÄND |
| 5255 | 10472303788298 | b_9_utkast.json | UNDERKÄND |
| 5256 | 10475418452234 | b_9_utkast.json | UNDERKÄND |
| 5257 | 10487987765514 | b_9_utkast.json | UNDERKÄND |
| 5258 | 10487987798282 | b_9_utkast.json | UNDERKÄND |
| 5259 | 10515739705610 | b_9_utkast.json | RÄTTA |
| 5262 | 10462768595210 | b_9_utkast.json | GODKÄND |
| 5263 | 10470902857994 | b_9_utkast.json | GODKÄND |
| 5264 | 10471174832394 | b_9_utkast.json | UNDERKÄND |
| 5265 | 10472224915722 | b_9_utkast.json | GODKÄND |
| 5266 | 10472233435402 | b_9_utkast.json | GODKÄND |
| 5267 | 10472250376458 | b_9_utkast.json | UNDERKÄND |
| 5268 | 10472252375306 | b_9_utkast.json | RÄTTA |
| 5269 | 10472254013706 | b_9_utkast.json | GODKÄND |
| 5270 | 10472257388810 | b_9_utkast.json | GODKÄND |
| 5273 | 10472294940938 | b_9_utkast.json | UNDERKÄND |
| 5274 | 10475978653962 | b_9_utkast.json | GODKÄND |
| 5275 | 10475980161290 | b_9_utkast.json | RÄTTA |

## Per produkt (exakt före/efter för RÄTTA)

### 5201 – 10472284422410 – RÄTTA
- Utkast: "Styrväska Basil Mali, 8 liter" (b_7_utkast.json)
- Skäl: Stämmer mot källan, ingen lastgräns i källan. Löftet att tillhörigheterna hålls torra är ett tillverkarpåstående och markeras.
- **html** före: `Materialet är vattenavvisande, så tillhörigheterna hålls torra även i regnigt väder.`
  efter: `Materialet är vattenavvisande och ska enligt tillverkaren hålla tillhörigheterna torra även i regnigt väder.`

### 5202 – 10472292647178 – GODKÄND
- Utkast: "Ramväska Basil Navigator Storm S, 0,8 liter" (b_7_utkast.json)
- Skäl: Stämmer. IPX3 skrivs enligt tillverkaren, den obegripliga meningen om vad väskan rymmer är rätt utelämnad.

### 5203 – 10472347042058 – GODKÄND
- Utkast: "Cykelklocka Basil Portland" (b_7_utkast.json)
- Skäl: Butikstiteln 'Bicycle at Basil Portland' är trasig; källtexten och taggen 'ringklocka' bekräftar typordet Cykelklocka. Tunn källa rätt hanterad (ingen meta).

### 5204 – 10589571744010 – RÄTTA
- Utkast: "Stänkskärmset Hebie Swap Set, 26–29 tum, Kamouflage" (b_7_utkast.json)
- Skäl: Stavningen skiljer sig mellan titeln (Stänkskärmset, som i övriga godkända Hebie-set) och meta/html (stänkskärmsset). Metan påstod att skärmen fästs med snabbkoppling; enligt källan fästs den med 4 skruvar och snabbkopplingen används för att ta av skärmen. Hjulstorleken 26–29 tum står i butikstiteln och skrivs enligt tillverkaren (Davids beslut om stänkskärmar).
- **meta** före: `Hebie Swap Set är ett stänkskärmsset med bak- och framskärm. Bakskärmen är ca 57 cm lång, 13 cm bred och fästs på sadelstolpen med snabbkoppling.`
  efter: `Hebie Swap Set är ett stänkskärmset med bak- och framskärm. Bakskärmen är ca 57 cm lång och 13 cm bred och går snabbt att ta av med snabbkopplingen.`
- **html** före: `Hebie Swap Set är ett stänkskärmsset med bakskärm och framskärm.`
  efter: `Hebie Swap Set är ett stänkskärmset med bakskärm och framskärm.`

### 5205 – 10461953425674 – RÄTTA
- Utkast: "Sadelväska Giant Shadow DX" (b_7_utkast.json)
- Skäl: Produkten har taggen 'På beställning' men standardblocket saknar meningen om beställningsvaror. Variantlåsningen är rätt undviken (269 kr Default, 299 kr black (0064)); mått och kapacitet rätt utelämnade.
- **html** före: `Normal leveranstid är 5–8 arbetsdagar. Fraktavgiften visas i kassan. Se sidan Frakt för övriga länder.</p>`
  efter: `Normal leveranstid är 5–8 arbetsdagar. Fraktavgiften visas i kassan. Se sidan Frakt för övriga länder. Beställningsvaror kan ta upp till en vecka längre.</p>`

### 5206 – 10462230970634 – UNDERKÄND
- Utkast: "Galler Basil Buddy Space Frame för Husdjurskorg, Svart" (b_7_utkast.json)
- Skäl: UNDERKÄND. Galler till husdjurskorg med säkerhetslöfte i källan (hindrar hunden från att hoppa ur, 'fullständigt skydd för din hund'); utkastet behåller 'avsett att hindra hunden från att hoppa ur korgen'. Samma bedömning som 5088 (Korggaller Basil Pluto XL) i b_1–b_6. 'Kapacitet: 0 l' i källan.

### 5208 – 10470936740106 – RÄTTA
- Utkast: "Flaskhållare Giant Airway Sport, Matt Svart och Blank Blå" (b_7_utkast.json)
- Skäl: SEO-titeln hade omvänd ordning (märke före typord) och är nästan identisk med 5050 ('Flaskhållare Giant Airway Sport i Nylon', b_4). Ny SEO-titel 43 tecken, unik. Övrigt stämmer (nylon, 41 g); '41,5 %' rätt utelämnat.
- **seo_title** före: `Giant Airway Sport Flaskhållare i Nylon`
  efter: `Flaskhållare Giant Airway Sport, Matt Svart`

### 5209 – 10471174668554 – UNDERKÄND
- Utkast: "Reflexklistermärken för Cykel Bookman" (b_7_utkast.json)
- Skäl: UNDERKÄND. Reflexklistermärken som enligt källan sätts på cykel eller hjälm och 'ökar säkerheten'; två varianter (273, 275) med oförklarade namn medan titeln anger 'vita prickar'. Samma bedömning som 5087 i b_1–b_6 (reflexer räknas som synlighet/belysning tills David beslutat). Kan släppas om David godtar reflexer och varianterna förklaras.

### 5210 – 10472232059146 – RÄTTA
- Utkast: "Bakskärm Giant Uniclip Fender, Fästs på Sadeln" (b_7_utkast.json)
- Skäl: Metans andra mening upprepade sig ('snabbt avtagbar, så den går att ta av'). 'Fender' behålls som del av modellnamnet Uniclip Fender.
- **meta** före: `Giant Uniclip Fender är en bakre stänkskärm för mountainbikes. Den fästs vid sadeln och är snabbt avtagbar, så den går att ta av och sätta på igen.`
  efter: `Giant Uniclip Fender är en bakre stänkskärm för mountainbikes som fästs vid sadeln. Skärmen är snabbt avtagbar och går att sätta på igen när den behövs.`

### 5211 – 10472249524490 – RÄTTA
- Utkast: "Väska Basil City MIK, Svart" (b_7_utkast.json)
- Skäl: Butikstitelns 'Styckväska' är trasig och källtexten säger 'Lens Bag' (felöversättning). 'Väska' är för allmänt; väskan fästs på cykeln med MIK-systemet, så typordet blir Cykelväska (samma som 5077). Den motsägande kapaciteten (8–11 l mot 9–11 l) är rätt utelämnad. Priset 1 569 kr bör kontrolleras.
- **titel** före: `Väska Basil City MIK, Svart`
  efter: `Cykelväska Basil City MIK, Svart`
- **seo_title** före: `Väska Basil City MIK`
  efter: `Cykelväska Basil City MIK`

### 5212 – 10475415044362 – RÄTTA
- Utkast: "Dricksflaska Giant Doublespring, 750 ml, Transparent Röd/Svart" (b_7_utkast.json)
- Skäl: Färger skrivs med 'och' som i övriga godkända utkast ('Svart och Neongrön'). 750cc skrivs rätt som 750 ml. 'Giftfritt' rätt utelämnat; BPA-fritt enligt tillverkaren.
- **titel** före: `Dricksflaska Giant Doublespring, 750 ml, Transparent Röd/Svart`
  efter: `Dricksflaska Giant Doublespring, 750 ml, Transparent Röd och Svart`

### 5213 – 10494699208970 – RÄTTA
- Utkast: "Dricksflaska Giant Doublespring, 600 ml, Transparent Röd/Svart" (b_7_utkast.json)
- Skäl: Samma rättning som 5212. Handtaget slutar på 480000351 (750 ml-flaskans SKU) medan SKU är 480000350; bör kontrolleras i butiken.
- **titel** före: `Dricksflaska Giant Doublespring, 600 ml, Transparent Röd/Svart`
  efter: `Dricksflaska Giant Doublespring, 600 ml, Transparent Röd och Svart`

### 5214 – 10541370212618 – GODKÄND
- Utkast: "Framkorg Basil Rattan Look FM, Sjögräs" (b_7_utkast.json)
- Skäl: Stämmer. Framkorg på styret utan lastuppgift i källan (tillåten enligt Davids beslut). Taggen 'Cykelbelysning' i butiken är felaktig men påverkar inte texten.

### 5215 – 10665228075274 – UNDERKÄND
- Utkast: "Reflekterande Klistermärken för Cykel Bookman, Flammönster" (b_7_utkast.json)
- Skäl: UNDERKÄND. Reflexdekaler, systerprodukt till 5087 (underkänd i b_1–b_6): tre varianter (520, 521, 522) med oförklarade namn, sätts enligt källan på hjälm, och metan lovar 'ökar synligheten i trafiken, både dag och natt' utan 'enligt tillverkaren'. Kan släppas om David godtar reflexer och varianterna förklaras.

### 5216 – 10470910624010 – GODKÄND
- Utkast: "Sadel Selle Monte Grappa MYO, Svart" (b_7_utkast.json)
- Skäl: Stämmer (stålram, 290 x 160 mm, 460 g). 'Black Technology System' rätt utelämnat.

### 5219 – 10472253358346 – GODKÄND
- Utkast: "Sadel Selle Monte Grappa Ramona, Svart" (b_7_utkast.json)
- Skäl: Stämmer. 'Tillverkad i Italien' rätt utelämnat.

### 5221 – 10472485519626 – GODKÄND
- Utkast: "Golvpump Giant Control Tower Elite med Analog Mätare" (b_7_utkast.json)
- Skäl: Stämmer (3,5 tums analog mätare, V-format gummihandtag, rostfritt stål). Den oklara meningen om slanglösa tillbehör rätt förenklad.

### 5222 – 10565562007818 – GODKÄND
- Utkast: "Handpump Beto Alu CCO-018AG med Tryckmätare" (b_7_utkast.json)
- Skäl: Stämmer. 'Exakt övervakning' rätt utelämnat; ventiltyperna står i källan.

### 5224 – 10472217477386 – GODKÄND
- Utkast: "Skrapa för Skidbas Start, Akryl, 3 mm" (b_7_utkast.json)
- Skäl: Butikstiteln 'Scraper Start acrylic 3 mm' är engelsk; 'Skrapa för Skidbas Start, Akryl, 3 mm' är rätt översatt och stämmer med källan (skidvalla, inte cykel). Produkttypen Tillbehör är oförändrad.

### 5226 – 10472232091914 – GODKÄND
- Utkast: "Bakskärm Giant Speedshield Clip-On" (b_8_utkast.json)
- Skäl: Butikstiteln 'Giant Speedshield Clip-On Rear Fender' är rätt översatt till Bakskärm. Stämmer mot källan; UV-/värmebeständighet rätt utelämnad.

### 5227 – 10472246771978 – GODKÄND
- Utkast: "Stänkskärmset Hebie Viper F, 26–29 tum, Svart" (b_8_utkast.json)
- Skäl: Butikstiteln 'Fender set HEBIE Viper F, 26"-29", black' är rätt översatt (Stänkskärmset, Svart). Hjulstorlek och mått entydiga i källan; den otydliga monteringsraden rätt utelämnad.

### 5234 – 10494689411338 – RÄTTA
- Utkast: "Framskärm XLC MG-C05 för Hjul 26–29 tum" (b_8_utkast.json)
- Skäl: 'Endast' är värderande och 'lätt att montera' är ett tillverkarpåstående som saknade markering i metan. Ursprung (Tyskland) och miljöpåståenden rätt utelämnade. Handtag 2502501007 mot SKU 2502501005 bör kontrolleras.
- **meta** före: `XLC MG-C05 är en genomskinlig, flexibel framskärm för hjul på 26–29 tum och däck som är 1,5–2 tum breda. Skärmen väger endast 75 g och är lätt att montera.`
  efter: `XLC MG-C05 är en genomskinlig, flexibel framskärm för 26–29-tums hjul och 1,5–2 tum breda däck. Den väger 75 g och är enligt tillverkaren lätt att montera.`

### 5235 – 10635765743882 – RÄTTA
- Utkast: "Cykelskydd Oxford Aquatex" (b_8_utkast.json)
- Skäl: Upprepning 'skydd ... ger skydd' i meta och html. 'Passar för'-punkten om att cykeln ryms i måtten bygger på en tolkning av måtten som källan inte ger (utkastaren noterar själv att det är oklart vad måtten avser) och tas bort. Butikstiteln 'Bicycle Cover' rätt översatt.
- **meta** före: `Oxford Aquatex är ett cykelskydd för en cykel, avsett för både inomhus- och utomhusbruk. Skyddet ger skydd mot smuts och regn och mäter 200 x 80 x 110 cm.`
  efter: `Oxford Aquatex är ett cykelskydd för en cykel som kan användas både inomhus och utomhus. Det skyddar mot smuts och regn och mäter 200 x 80 x 110 cm.`
- **html 1** före: `Oxford Aquatex är ett cykelskydd som ger skydd mot smuts och regn.`
  efter: `Oxford Aquatex är ett cykelskydd mot smuts och regn.`
- **html 2** före: `⏎<li>Dig som har en cykel som ryms i måtten 200 x 80 x 110 cm</li>`
  efter: *(tas bort)*

### 5236 – 10472224653578 – RÄTTA
- Utkast: "Sadelväska Basil Discovery 365D S, 0,5 l" (b_8_utkast.json)
- Skäl: SEO-titeln görs lik systerprodukten 5084 ('Sadelväska Basil Discovery 365D, 1 l'). Titeln behålls, eftersom ett kommatecken till (som i 5084) ger tre kommatecken med decimalkommat. Den motsägande färgen (grå/svart melange) och vattentätheten är rätt utelämnade.
- **seo_title** före: `Sadelväska Basil Discovery 365D S`
  efter: `Sadelväska Basil Discovery 365D, 0,5 l`

### 5238 – 10472293957898 – UNDERKÄND
- Utkast: "Framkorg och Bagagekorg Basil Crate S, Svart" (b_8_utkast.json)
- Skäl: UNDERKÄND. Låda för både fram- och bakre pakethållare (Davids beslut gäller framkorgar utan lastuppgift, inte lådor på pakethållare). Källan är motsägelsefull: 17,5 l i titeln mot 17 l, 'fästas permanent på cykelsitsen' och 'lämplig för förskolebarn' (oklart om barnprodukt). Typordet 'Bagagekorg' är ovanligt. Kan släppas om David godtar bakre korgar utan lastuppgift och barnfrågan klaras ut.

### 5239 – 10475364909322 – RÄTTA
- Utkast: "Stänkskärmar SKS Fatboard för Fatbike" (b_8_utkast.json)
- Skäl: 'Enkla att installera' är ett tillverkarpåstående utan markering. Beställningsmeningen i standardblocket stämmer (taggen 'På beställning'). Butikstiteln 'Fatbike fenders' rätt översatt. Ursprung rätt utelämnat; tunn källa, ingen meta.
- **html 1** före: `Skärmarna är enkla att installera.`
  efter: `Skärmarna är enligt tillverkaren enkla att installera.`

### 5240 – 10475428872458 – GODKÄND
- Utkast: "Strumpor Liv Short N Snug, Dam" (b_8_utkast.json)
- Skäl: Stämmer. Två varianter (black, black (0784), samma pris) är inte låsta; storleken XS/S är rätt utelämnad.

### 5244 – 10468721033482 – RÄTTA
- Utkast: "Stänkskärmar SKS Speedrocker för 27,5–28 tum" (b_8_utkast.json)
- Skäl: Grammatik ('27,5 tum ... hjul') och en punkt som upprepade sig. Hjulstorlek och däckbredd är entydiga i källan; '42 mm' i butikstiteln är rätt tolkad som största däckbredd. Handtag 11568 mot SKU 11567 bör kontrolleras.
- **html 1** före: `<li>Dig som har 27,5 tum (650b) eller 28 tum hjul med däckbredd 23–42 mm</li>`
  efter: `<li>Dig som har 27,5-tums (650b) eller 28-tums hjul med däckbredd 23–42 mm</li>`
- **html 2** före: `<li>Dig som har skivbromsar, eftersom skärmarna enligt tillverkaren är lämpliga för cyklar med skivbromsar</li>`
  efter: `<li>Dig som har en cykel med skivbromsar, enligt tillverkaren</li>`

### 5245 – 10470908264714 – GODKÄND
- Utkast: "Handtagstejp Giant Connect Gel, Vit och Röd" (b_8_utkast.json)
- Skäl: Stämmer. Vibrationspåståendet rätt utelämnat; 'skyddsplatta' (felöversättning) rätt skrivet som handtagstejp. Se öppen fråga om typord (Handtagstejp/Styretape).

### 5246 – 10472249753866 – RÄTTA
- Utkast: "Väska med Pakethållarfäste Basil Grand Bicycle Shopper, 23 l" (b_8_utkast.json)
- Skäl: 'För inköp' är styltigt (samma rättning som 5011). Källan anger ingen lastgräns. Maskinöversatta termer ('doktorförslutning', 'medicinsk låsning') rätt utelämnade.
- **html** före: `<li>Dig som vill ha en väska på 23 l för inköp på cykeln</li>`
  efter: `<li>Dig som handlar på cykeln och behöver 23 l utrymme</li>`

### 5248 – 10472253653258 – RÄTTA
- Utkast: "Kjolskydd Selle Monte Grappa, Svart, Läder" (b_8_utkast.json)
- Skäl: Första meningen sade att märket är ett kjolskydd ('Selle Monte Grappa är ett kjolskydd'). Källan säger '25–27 tums stadscyklar' utan att ange att det gäller hjulen, så 'hjul' tas bort (kompatibilitet bara om källan är entydig). Butikstiteln 'Skirt protector ..., black, leather' rätt översatt.
- **meta** före: `Selle Monte Grappa är ett kjolskydd i svart läder som hindrar`
  efter: `Kjolskyddet från Selle Monte Grappa i svart läder hindrar`
- **html 1** före: `<p>Selle Monte Grappa är ett kjolskydd i svart läder som skyddar`
  efter: `<p>Kjolskyddet från Selle Monte Grappa är i svart läder och skyddar`
- **html 2** före: `<li>Dig som har en stadscykel med 25–27 tums hjul, enligt tillverkaren</li>`
  efter: `<li>Dig som har en stadscykel i storleken 25–27 tum, enligt tillverkaren</li>`

### 5249 – 10472254177546 – RÄTTA
- Utkast: "Kjolskydd Selle Monte Grappa, Ljusbrun, Läder" (b_8_utkast.json)
- Skäl: Samma rättning som 5248. Butikstiteln 'Skirt protector ..., light brown, made of leather' rätt översatt.
- **meta** före: `Selle Monte Grappa är ett kjolskydd i ljusbrunt läder som hindrar`
  efter: `Kjolskyddet från Selle Monte Grappa i ljusbrunt läder hindrar`
- **html 1** före: `<p>Selle Monte Grappa är ett kjolskydd i ljusbrunt läder som skyddar`
  efter: `<p>Kjolskyddet från Selle Monte Grappa är i ljusbrunt läder och skyddar`
- **html 2** före: `<li>Dig som har en stadscykel med 25–27 tums hjul, enligt tillverkaren</li>`
  efter: `<li>Dig som har en stadscykel i storleken 25–27 tum, enligt tillverkaren</li>`

### 5250 – 10472254669066 – GODKÄND
- Utkast: "Sadel Selle Monte Grappa Corvetta, Grå" (b_8_utkast.json)
- Skäl: Stämmer (stålram, 260 x 210 mm, 410 g). Oklar formulering 'sadel för Monte Grappa Corvetta' rätt hanterad.

### 5251 – 10472254898442 – GODKÄND
- Utkast: "Sadel Selle Monte Grappa 07F, Svart" (b_9_utkast.json)
- Skäl: Stämmer. 'Rullstolssadel' (felöversättning) och 'designad i Italien' rätt utelämnade; 'Ram: Fjädrar' rimligt tolkat som fjädrar.

### 5252 – 10472256143626 – UNDERKÄND
- Utkast: "Frontkorg Wish för Barn, Lila" (b_9_utkast.json)
- Skäl: UNDERKÄND. Barnprodukt: 'Cykelkorg för barn med Wish-tema' (Davids beslut: barnprodukter underkänns). Utkastaren avvisade själv barncykelklockan med samma tema (5229) och barnkorgen 5247. Måttraden i källan är dessutom trasig.

### 5253 – 10472286224650 – UNDERKÄND
- Utkast: "Cykeldekorationer Stitch, Färgglad" (b_9_utkast.json)
- Skäl: UNDERKÄND. Barnprodukt: dekorationer för 'ditt barns cykel' som fästs på handtagen (Davids beslut: barnprodukter underkänns). Antal och vad diametern avser framgår inte.

### 5254 – 10472303067402 – UNDERKÄND
- Utkast: "Reflexer Bookman Snap Bands för Arm och Ben, Svart" (b_9_utkast.json)
- Skäl: UNDERKÄND. Reflexband att bära på arm och ben och fästa på barnvagn; källan är helt inriktad på säkerhet och synlighet i mörker ('säkrare på vägen', 'säkerställer att du syns'). Personlig säkerhetsprodukt i samma kategori som reflexdekalerna (5087). Kan släppas om David godtar reflexer i vågor.

### 5255 – 10472303788298 – UNDERKÄND
- Utkast: "Reflexklistermärken Bookman Black Zebra för Cykel" (b_9_utkast.json)
- Skäl: UNDERKÄND. Reflexdekaler (sätts enligt källan på cykel eller hjälm), samma bedömning som 5087, 5209 och 5215. Kan släppas om David godtar reflexer.

### 5256 – 10475418452234 – UNDERKÄND
- Utkast: "Dricksflaska Giant ARX 400 ml, Orange" (b_9_utkast.json)
- Skäl: UNDERKÄND. Barnprodukt: flaskan är enligt källan 'designad för barncyklar' och har taggen Barncykel; källan har dessutom ett hygienpåstående (antimikrobiell). Davids beslut: barnprodukter underkänns.

### 5257 – 10487987765514 – UNDERKÄND
- Utkast: "Stänkskärmsset Hebie Alumee 52 mm" (b_9_utkast.json)
- Skäl: UNDERKÄND. Källan anger att bakskärmen bär högst 8 kg per sida (fästen för sidoväskor). Utkastaren har tagit bort lastuppgiften och skrivit ändå, medan samma utkastare avvisade 5233 av exakt det skälet. Lastuppgift som tas bort döljer en säkerhetsrelevant gräns (samma bedömning som 5071, 5077). Måttet 52 mm förklaras inte.

### 5258 – 10487987798282 – UNDERKÄND
- Utkast: "Stänkskärmsset Hebie Alumee 62 mm" (b_9_utkast.json)
- Skäl: UNDERKÄND. Samma som 5257 (bakskärmen bär 8 kg per sida, lastuppgiften bortplockad). Måttet 62 mm förklaras inte.

### 5259 – 10515739705610 – RÄTTA
- Utkast: "Flaskhållare Giant Airway Composite, Svart/Orange/Rosa" (b_9_utkast.json)
- Skäl: Färger skrivs med 'och' som i övriga utkast (två kommatecken, 59 tecken). Kolfiberkomposit och 34 g stämmer.
- **titel** före: `Flaskhållare Giant Airway Composite, Svart/Orange/Rosa`
  efter: `Flaskhållare Giant Airway Composite, Svart, Orange och Rosa`

### 5262 – 10462768595210 – GODKÄND
- Utkast: "Golvpump SKS Air-X-Press 8.0, Svart och Orange" (b_9_utkast.json)
- Skäl: Stämmer (8 bar/115 PSI, AV/SV/DV, 600 mm, stålrör). Butikstiteln 'Floor pump' rätt översatt; 'passar alla typer av ventiler' rätt ersatt med de listade. Beställningsmeningen finns (taggen 'På beställning').

### 5263 – 10470902857994 – GODKÄND
- Utkast: "Framskärm Hebie Swap Front Adrenaline, 320 x 140 mm" (b_9_utkast.json)
- Skäl: Butikstiteln 'Front fender HEBIE Swap Front "Adrenaline", 26"-' och den engelska källan är rätt översatta (Framskärm). Bara mått, vikt och monteringsdelar används; den oklara '26"-' är rätt utelämnad.

### 5264 – 10471174832394 – UNDERKÄND
- Utkast: "Reflexklistermärken Bookman White Leopard för Cykel" (b_9_utkast.json)
- Skäl: UNDERKÄND. Reflexdekaler i leopardmönster (sätts enligt källan på cykel eller hjälm), samma bedömning som 5087, 5209, 5215 och 5255. Källans 'set med 10' är oklart. Kan släppas om David godtar reflexer.

### 5265 – 10472224915722 – GODKÄND
- Utkast: "Sadelväska Basil Navigator Storm M, 1,5 l" (b_9_utkast.json)
- Skäl: Stämmer (1,5 l, 10 x 9 x 29 cm, polyester, snodd). Motsägande vattentäthet (IPX3/IP68) och 'kommer hem säkert' rätt utelämnade.

### 5266 – 10472233435402 – GODKÄND
- Utkast: "Handpump Liv Control Mini+, Silver" (b_9_utkast.json)
- Skäl: Tunn, trasig källa rätt hanterad: bara slang med utdragbar ventil, ingen meta.

### 5267 – 10472250376458 – UNDERKÄND
- Utkast: "Pedaler Giant Pinner Elite, Lila" (b_9_utkast.json)
- Skäl: UNDERKÄND. Pedaler (Davids beslut: pedaler och vevar underkänns). Utkastaren avvisade själv 5217 och 5241 (pedaler) men tog med denna.

### 5268 – 10472252375306 – RÄTTA
- Utkast: "Styretape Liv Contact SL, Vit" (b_9_utkast.json)
- Skäl: Genus växlade: 'ett vitt styretape' följt av 'Tapen'. Rättas till neutrum. Stötdämpning skrivs enligt tillverkaren. Se öppen fråga om typordet.
- **meta** före: `Tapen är 2,5 mm tjock och ändpluggar`
  efter: `Det är 2,5 mm tjockt och ändpluggar`
- **html** före: `Tapen är 2,5 mm tjock och levereras`
  efter: `Det är 2,5 mm tjockt och levereras`

### 5269 – 10472254013706 – GODKÄND
- Utkast: "Sadel Selle Monte Grappa Ramona, Brun" (b_9_utkast.json)
- Skäl: Stämmer, som 5219 (Ramona svart). 'Tillverkad i Italien' rätt utelämnat.

### 5270 – 10472257388810 – GODKÄND
- Utkast: "Handskar Liv Supreme SF, Svart" (b_9_utkast.json)
- Skäl: Tunn källa rätt hanterad: bara polyester, inga skydds- eller säkerhetslöften ('säker', grepp 'om linsen' utelämnade). Cykelhandskar för vuxna är ingen säkerhetsprodukt.

### 5273 – 10472294940938 – UNDERKÄND
- Utkast: "Pedaler Giant Combo Touring Pedal" (b_9_utkast.json)
- Skäl: UNDERKÄND. Pedaler (Davids beslut). Dessutom tunn källa och priset 1 589 kr bör kontrolleras.

### 5274 – 10475978653962 – GODKÄND
- Utkast: "Flaskhållaradapter SKS för Sadelstolpe" (b_9_utkast.json)
- Skäl: Stämmer. Monteringen på 'vevarm eller vilken annan del som helst' och 'tillverkad i Tyskland' rätt utelämnade. Källans html innehåller kopierad chattkod som bör rensas i butiken.

### 5275 – 10475980161290 – RÄTTA
- Utkast: "Cykelkorg Basil Cairo Luxe för Pakethållare" (b_9_utkast.json)
- Skäl: Kompatibilitet får bara stå om källan är entydig; 'passar alla typer av cyklar' är ett generellt påstående utan underlag och tas bort. Ingen lastgräns i källan. Bakre korg på pakethållare omfattas inte uttryckligen av Davids beslut om framkorgar (öppen fråga).
- **html 1** före: ` Korgen är universell och passar enligt tillverkaren alla typer av cyklar.`
  efter: *(tas bort)*
- **html 2** före: `⏎<li>Dig som söker en universell bakre korg</li>`
  efter: *(tas bort)*
- **html 3** före: `⏎<li>Passform: Universell</li>`
  efter: *(tas bort)*
