# Granskningsutlåtande k_40 (2026-11-07)

Oberoende granskare. Bara läsning i Shopify (`shopify_api.py`, ShopifyKlient; `verifiera_butik` gav BEST OF SPORTS); inget ändrat, inget committat. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.10), BESLUTSLOGG till och med 2026-11-07 (dubbdäck, Gymball, Maca, Gotu Kola och de två revideringarna), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_39fg.md`. Webbkoll: suomityres.fi (Routa-tabellen och Kide W106) samt sökning på Gymballens EAN/artikelnummer.

Alla 9 är ACTIVE med lager och har en enda variant. `skrivfil_kontroll.py`: 0 fel, 0 varningar. Standardblocket är identiskt med det kanoniska (`b_skriv_24.json`) på alla 9. Ingen har taggen På beställning och ingen har leveranstidsmeningen. Titel ≤70 tecken och ≤2 kommatecken, SEO-titel ≤43, meta 91–155 tecken med verb, högst två 'enligt tillverkaren'. Titlar, SEO-titlar och metatexter är unika mot övriga utkast- och skrivfiler (revideringarna träffar bara sig själva i k_39a/k_skriv_39ac) och mot live-titlarna, utom 39081 (se nedan). Inga cirkulära inledningar.

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_40.json`. Inga rättningar behövs, så det finns inga före/efter-par.

## Resultat: 8 GODKÄND, 0 RÄTTA, 1 UNDERKÄND

| nr | id | fil | dom |
|---|---|---|---|
| 39102 | 10472303755530 | k_40_utkast.json | GODKÄND |
| 39103 | 10472304083210 | k_40_utkast.json | GODKÄND |
| 39104 | 10472304902410 | k_40_utkast.json | GODKÄND |
| 39105 | 10472305000714 | k_40_utkast.json | GODKÄND |
| 39081 | 10472265056522 | k_40_utkast.json | UNDERKÄND |
| 39038 | 10470944702730 | k_40_utkast.json | GODKÄND |
| 39090 | 10472270987530 | k_40_utkast.json | GODKÄND |
| 39016 | 10462770987274 | k_40_utkast.json | GODKÄND |
| 39018 | 10462773182730 | k_40_utkast.json | GODKÄND |

## Skäl per produkt

### 39102 (10472303755530): GODKÄND

Live ACTIVE, en variant T506081, EAN 6430020165399, lager 1. Motsägelsen i egen källa ('47-406 (24 tum)') är entydigt löst: ETRTO-måttet 406 mm är standardmåttet för 20-tumshjul, tillverkarens tabell https://suomityres.fi/products/winter/city/routa anger T506081 = 47-406, 20 tum, 176 dubbar, och live-titeln säger '20 x 1.'. Källans '24 tum' är felet och är korrekt utelämnat (R2). Stålsdubbar och reflekterande sidor står i källan och på tillverkarens sida; 'högkvalitativt', 'tillverkade i Finland', grepp, rullmotstånd, punkteringsskydd, slitstark och giftfri är utelämnade. Reflekterande sidor nämns som fakta utan synlighetslöfte (v1.9). Pendlings- och gruscykel ur källan; 'kargcyklar' utelämnat. Format, standardblock och längder rätt; unik mot butikens dubbdäck.

### 39103 (10472304083210): GODKÄND

Live ACTIVE, T600281, EAN 6430020165009, lager 3. Egen källa saknar mått (bara trasigt '106 lbs' och marknadstext med säkerhets- och greppåståenden, allt utelämnat). Mått, dubbantal och användning hämtade från tillverkarens sida https://suomityres.fi/products/winter/city/kide-w106: T600281 = 47-622, 28 tum, 106 dubbar, 'tailored for hybrid and city bikes' (återgivet en gång enligt tillverkaren, v1.6). Inga grepp-, säkerhets- eller prestandalöften. Format och längder rätt.

### 39104 (10472304902410): GODKÄND

Live ACTIVE, T506381, EAN 6430020165603, lager 4. Live-titelns 'Hjul' är ett översättningsfel; källtexten är Routa-seriens och tillverkarens Routa-tabell anger T506381 = 47-507, 24 tum, 106 dubbar, vilket stämmer med W106 i live-titeln och '47-507 (24 tum)' i källan. Modellnamnet Routa W106 är därmed entydigt. Trasiga rader ('grus och karg-hjul', 'för kullersten …') utelämnade; bara pendlingscykel anges. Inga löften. Format och längder rätt.

### 39105 (10472305000714): GODKÄND

Live ACTIVE, T506281, EAN 6430020165597, lager 6. Källans '212 lb' är trasig men W212 i titeln och tillverkarens tabell (T506281 = 47-507, 24 tum, 212 dubbar) ger entydigt 212 dubbar. Pendlings-, grus- och lastcykel står ordagrant i källan. Inga löften. Format och längder rätt.

### 39081 (10472265056522): UNDERKÄND

Live ACTIVE, 14TUSFU334, EAN 8717842035672, lager 10. Färgen är inte entydigt belagd: egen källas specifikation säger 'Färg: grönaktig' medan live-titeln säger 'Off-white'; off-white stöds bara av söksnippets (Decathlon IE, fitnessmarket.ee) vars sidor inte gick att öppna (404/403) för citat. Färgen kan inte heller strykas: utan färg blir titeln 'Gymnastikboll Tunturi Gymball 75 cm', exakt samma som den redan skrivna syskonprodukten 10472277803274 (14TUSFU336, EAN 8717842035696, annan färg, taggen texter-klara), och SEO-titeln krockar likaså (R12). Enligt Davids dubblettbeslut 2026-11-05 ska samma modell i annan färg ha en titel som skiljer dem, och det enda som skiljer är färgen. 'Anti Burst' får inte användas som särskiljare (skyddslöfte, R5). Övriga fakta (75 cm, 1,2 kg, bärförmåga 220 kg som svensk rad, längd 179–190 cm, yoga och stretch) är i sig korrekta. Kan släppas om David bekräftar färgen (förpackning eller leverantör) eller godkänner artikelnummer som särskiljare i titeln.

### 39038 (10470944702730): GODKÄND

Live ACTIVE, SKU 21756, lager 10. Växtextrakt-kosttillskott frisläppt (BESLUTSLOGG 2026-11-05 och 2026-11-07, bara produktfakta). Ingredienslistan står ordagrant i källan (kontrollerat i python). 18 aktiva ingredienser, 10 mg maca rot extrakt per dagsdos, dos 2 kapslar, användning, max 3 månader, förvaring och varningar finns i källan. Fertilitets-, sexual- och energipåståenden är utelämnade; typordet Kosttillskott. 'For Him' står bara som produktnamn. Titel 68 tecken, SEO 42, meta 155. Felaktiga taggar Herrcykel och Trek rörs inte (bör rensas separat).

### 39090 (10472270987530): GODKÄND

Live ACTIVE, SKU 21736, lager 9. Frisläppt som 39038. Ingredienslistan står ordagrant i källan (bara '43%' skrivet som '43 %'). Dos, användning, förvaring och varningar finns i källan; varningen om barn, gravida och ammande finns inte i den här källan och är riktigt utelämnad. Effektpåståendena (cirkulation, matsmältning, kognitiv funktion, sårläkning) är helt utelämnade. Typordet Kosttillskott i stället för 'Vitaminkapslar' är korrekt (inget vitamin). Taggen Trek rörs inte.

### 39016 (10462770987274): GODKÄND

Revidering. Live ACTIVE med texter-klara, lager 4. Titel, SEO-titel och meta är identiska med live. Live-beskrivningen och utkastet skiljer sig bara i en tillagd rad (diff tecken för tecken): '<li>Allergener: Denna produkt kan innehålla allergener som mjölk, soja, vete, korn, havre, ägg, jordnötter och nötter.</li>'. Meningen står ordagrant i produktens ursprungliga källa (rapporter/shopify-original-2026-11-05/k_skriv_39ac_fore_rest.json, kontrollerat för just detta id). Beslut av David 2026-11-07.

### 39018 (10462773182730): GODKÄND

Revidering. Live ACTIVE med texter-klara, lager 11. Titel, SEO-titel och meta är identiska med live. Beskrivningen skiljer sig bara i en tillagd rad: '<li>Varning: Azorubin kan ha negativa effekter på barns aktivitet och uppmärksamhet.</li>'. Meningen efter 'Varning:' står ordagrant i ursprungskällan för just detta id (k_skriv_39ac_fore_rest.json). Beslut av David 2026-11-07. Till David: källan har ingen ingredienslista, så azorubin kan inte kopplas till en ingrediens i texten.

## Till David

1. **39081 Gymball:** färgen behöver bekräftas (förpackning eller leverantör), eller ett annat sätt att skilja produkten från den redan skrivna 75 cm-bollen 10472277803274 (till exempel artikelnumret i titeln). Annars skrivs den inte.
2. **39018:** azorubinvarningen står i källan men ingen ingredienslista; kontrollera gärna förpackningen.
3. **39038 och 39090:** taggarna Herrcykel och Trek är felaktiga och bör rensas separat (rörs inte i textomgången).
