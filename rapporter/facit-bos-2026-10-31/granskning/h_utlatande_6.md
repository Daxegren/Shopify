# Granskning faktatext h_6 (Toorx/Tunturi/Hammer: handskar, bälten, vikter, band, västar, boxningshandskar) – BEST OF SPORTS (2026-11-04)

Oberoende granskning, endast läsning. Butiken är bekräftad med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK). Underlag: `h_6_utkast.json` (21 utkast) och `h_6_avvisade.json` (4), lästa från utkastarens scratchpad (`…/scratchpad/h6/`), eftersom de inte fanns i `vag2_skriv/`. Regelbok v1.3 gäller före `c_granskarprompt.md`.

**Metod:** Alla 25 produkter och den redan skrivna 10472305393930 hämtades live (graphql `nodes`). Alla 25 är ACTIVE, productType är oförändrad (Konditionsträning & Fitness) och ingen har html skriven. Bara 10598 har SEO live (från experiment 1, som inte längre hålls) och ersätts helt (R15). Inget id finns i pilotens 20 (`bestofsports-pilot-20-produkter-2026-10-25.csv`) eller i `sparrlista.json`, och inget finns i andra utkast- eller skrivfiler (bara i inventerings- och in-filer). SEO-titlarna jämfördes mot live-titlar och live-SEO (sökning på Power Band, handskar/Gloves, bälte/Belt, väst, vikter, Sliders, Resistance, motståndsband, stretchband, boxningshandskar, viktlyft samt SKU:er): ingen krock, och titlar, SEO-titlar och metor är unika inom batchen.

## Resultat
| Dom | Antal | Nr |
|---|---|---|
| GODKÄND | 15 | 10581, 10582, 10583, 10584, 10585, 10588, 10590, 10592, 10594, 10598, 10600, 10604, 10605, 10606, 10607 |
| RÄTTA | 6 | 10586, 10587, 10593, 10597, 10601, 10602 |
| UNDERKÄND | 0 | – |
| Avvisad (bekräftad) | 4 | 10579, 10580, 10596, 10603 |

## Särskilda kontroller
- **Typordsbyten (R7):** Bicepsfäste (10583), Viktbälte (10584), Träningshandskar (10588), Stretchband (10590/10592), Boxningshandskar (10606) och Vikter (10602) står alla ordagrant i produktens egen källa. Stretchgummiset (10593) är sammansatt av källans 'stretchgummi' och 'satsen' och godtas som gränsfall.
- **Lastgränser (R4):** inga lastgränser i texterna. Motstånd 10–35 och 20–55 kg (10590/10592) och kg per bandfärg (10597, 10598, 10600) anger bandens motstånd, inte en lastgräns, och återges som i källan. 'Upp till 30 kg' (10604) är hur mycket vikt västen rymmer, som redan skrivna 20 kg-västen.
- **Källa/SKU-skillnad:** 10588 (XXL, kod 216 mot SKU 220), 10594 (variant S mot 'andra storlekar S, M, XL', kod 205 mot SKU 203) och 10601 (kod 278 mot SKU 279). Storleken är utelämnad, och inga storlekssyskon finns i butiken. Källtexten är troligen kopierad från ett syskon hos leverantören, men inget i texterna motsäger titeln.
- **Hälsa och säkerhet (R5):** skadeförebyggande, rehab-, effekt- och kvalitetsord är borta överallt. Kvar finns, ordagrant och 'enligt tillverkaren', bara 'halkfri' (10581, 10582, 10587, 10588) och 'stödjer mage och rygg' (10601).
- **'&' → 'och' (10587):** följer R10 även i produktnamnet, godtas.

## Utlåtande per produkt
| Nr | Id | Dom | Fält | Före | Efter | Skäl |
|---|---|---|---|---|---|---|
| 10581 | 10624082968842 | GODKÄND | | | | Styrkeövningar, öglor och halkfri handflata ur källan; 'halkfri' står ordagrant och skrivs 'enligt tillverkaren' (R5). Svart ur titeln. Komfort, säkerhet och Italien borta. SEO skiljer sig från DRAFT-syskonet Viktlyftningshandskar. |
| 10582 | 10472279736586 | GODKÄND | | | | Källan identisk med syskonen; användning (styrketräning), kettlebells/hantlar och halkfri (enligt tillverkaren) ordagrant. Färg ur titeln. |
| 10583 | 10472263221514 | GODKÄND | | | | Typordsbytet Belt → Bicepsfäste har stöd i källan ('Tunturi bicepsfäste', 'bicepsfästet') (R7). 57 cm, 0,72 kg, justerbar, svart, aluminium/snoddrem, nack- och armbågspolstring ordagrant. Isolering, ryggproblem, stark/hållbar borta (R5). |
| 10584 | 10471027507466 | GODKÄND | | | | Viktbälte står i källan ('Tunturi viktbälte', 'extra viktbältet') (R7). Alla mått, läder/stålkedja, en storlek, vaddering och chinsexemplet ordagrant. Muskelutveckling och hållbart borta. Ingen lastgräns i källan. |
| 10585 | 10471027212554 | GODKÄND | | | | Live-ordet Ben- och armvikter behålls, samma som redan skrivna syskonet 10472270266634 (2 x 1,5 kg). Alla specifikationer ordagrant; träningseffekt borta. |
| 10586 | 10472213315850 | RÄTTA | meta | Tunturi EVA Dipping Belt är ett svart bälte i plast (EVA) med metallkedja som väger 529 g. | Tunturi EVA Dipping Belt är ett svart bälte i plast (EVA) som väger 529 g och levereras med en metallkedja för extra vikt. | |
| 10586 | 10472213315850 | (skäl) | | | | Fakta stämmer (EVA, svart, metallkedja ingår, 529 g); oklara mått och 'dykbälte' rätt utelämnade. Metan kan läsas som att kedjan väger 529 g (källan anger produktens vikt). Efter: 122 tecken. |
| 10587 | 10471350534410 | RÄTTA | meta | en halkfri sida för trä | enligt tillverkaren en halkfri sida för trä | |
| 10587 | 10471350534410 | (skäl) | | | | Två entydiga fakta utöver titeln (två sidor; underlag), räcker enligt R3. '&' → 'och' i produktnamnet följer R10. 'Halkfri' är ett R5-ord: i html står det 'enligt tillverkaren', i metan inte. Efter: 144 tecken. Beställningsmening rätt. |
| 10588 | 10462191124746 | GODKÄND | | | | Träningshandskar står i källan (R7). Läder, öppna fingrar, handledsremmar, snöre, par ordagrant; halkfria 'enligt tillverkaren'. Storlek XXL och produktkod 14TUSFU216 (live-SKU 14TUSFU220) rätt utelämnade (R2). Titeln anger ingen storlek och produkten har en variant, så R3 utlöses inte. Inget storlekssyskon finns i butiken (sökt på SKU). Skydd, stukningar, handledsstyrka och Fitkids borta. |
| 10590 | 10472289108234 | GODKÄND | | | | Stretchband står i källan ('stretchbandet') och i redan skrivna syskon (Extra Light). 104 cm, 2,9 cm, latex, grön; motstånd 10–35 kg står två gånger i källan och stämmer med listan (29 mm, grön). Motstånd är inte en lastgräns (R4 gäller inte) och står en gång per fält som 'enligt tillverkaren', godtas. Skräpraden '2,9 cm - 2,9 kg' rätt utelämnad. |
| 10592 | 10468731683082 | GODKÄND | | | | Som 10590: 104 cm, 4,4 cm (44 mm), 20–55 kg, blå, latex. 'Blue' → 'Blå'. SEO (…Heavy) krockar inte med Extra Heavy (Träningsband …, Svart) eller Light (DRAFT). |
| 10593 | 10471026819338 | RÄTTA | meta | Tunturi Resistance Trainer är ett svart set med stretchgummi, träningsstång, dörrankare, säkerhetsrem och förvaringsväska på 2,2 kg. | Tunturi Resistance Trainer är ett svart set på 2,2 kg med stretchgummi, träningsstång, dörrankare, säkerhetsrem och förvaringsväska. | |
| 10593 | 10471026819338 | (skäl) | | | | Innehåll, mått, 2,2 kg, dacron/latex/stål, svart ordagrant; träningseffekter borta. Typordet Stretchgummiset är bildat av källans 'stretchgummi' + 'satsen/set' (syskonet 10472279671050 heter live Stretchgummi), godtas som R7-gränsfall. Metan kan läsas som att väskan väger 2,2 kg. Efter: 132 tecken. |
| 10594 | 10411721392394 | GODKÄND | | | | Läder och nylon, öppna fingrar, kardborreband, parvis, svart ordagrant. Live-varianten heter S medan källan säger 'Finns i andra storlekar (S, M, XL)' och koden 14TUSFU205 (SKU 203): motsägelse, storlek rätt utelämnad (R2). Titeln låser ingen storlek; variantnamnet visas ändå i butiken. 'Intern handske' och blåsor/hygien borta. |
| 10597 | 10472308539658 | RÄTTA | meta | Tunturi Mini Resistance Band Set har fyra motståndsband i olika färger och en liten förvaringspåse. Varje band är 25 x 5 x 0,8 cm. | Tunturi Mini Resistance Band Set har fyra motståndsband i blått, orange, grönt och grått samt en liten förvaringspåse. | |
| 10597 | 10472308539658 | (skäl) | | | | Fyra band, påse, färg och kg per färg ordagrant. Kg per färg är inte en lastgräns och återges som i källan utan tolkning, godtas. 'Varje band är 25 x 5 x 0,8 cm' är en tolkning (källan säger bara 'Mått'); html har bara 'Mått', vilket godtas. Efter: 118 tecken. |
| 10598 | 10472310931722 | GODKÄND | | | | Live-SEO kommer från experiment 1 (forslag-bos-experiment-1), som inte längre hålls (BESLUTSLOGG 2026-11-04); ingen html eller standardblock live, så texten ersätts helt (R15). Fem band, färger, kg och påse ordagrant. Metan tolkar inte måttet. SEO bara versaler ändrade. |
| 10600 | 10472289632522 | GODKÄND | | | | Den maskinöversatta live-titeln är omskriven och behåller live-ordet motståndsbandset (R2/R7), godtas. 5 band med kg per färg, fot-/handledsband, dörrfäste, nätpåse, latex, 513 g ordagrant. 'Längd på rören', fysioterapeuter och rehabiliteringsläkare rätt utelämnade (R5). |
| 10601 | 10411853512970 | RÄTTA | html | \n<li>Finns även i: 100, 110 och 120 cm</li> | (tomt) | |
| 10601 | 10411853512970 | (skäl) | | | | Mått, 417 g, svart, läder, spänne ordagrant. 'Stödjer mage och rygg vid träning med vikter' står ordagrant och har 'enligt tillverkaren' (R5 tillåter); skador och prestation borta. Raden 'Finns även i 100, 110 och 120 cm' stryks: butiken har inga sådana storlekar (sökt på titel och SKU), så raden lovar något kunden inte kan köpa. SKU 14TUSCL279 mot koden 14TUSCL278 i källan: titel och källa säger båda 90 cm, så inget R3-fel. |
| 10602 | 10472289698058 | RÄTTA | html | De fästs på handleden eller ankeln med en snodd, och två vikter ingår. | De fästs på handleden eller ankeln med en snodd. | |
| 10602 | 10472289698058 | (skäl) | | | | 'Innehåll: järnväst' är en egen rad och rätt utelämnad (R2). Mått 40 x 14 x 5 cm och 2 x 2,25 kg står på egna rader, stämmer med titeln och är rimliga för handleds-/ankelvikter, godtas. Typordet Vikter står i källan ('dessa vikter') (R7). Upprepningen 'två vikter … två vikter ingår' i första stycket stryks. |
| 10604 | 10605355172106 | GODKÄND | | | | 'Ökar din kroppsvikt med upp till 30 kg' anger hur mycket vikt västen rymmer, inte en lastgräns för en konstruktion (R4 gäller inte). Samma form som redan skrivna syskonet 10472260665610 ('Maximal vikt: 20 kg'). 1 kg viktblock, en storlek, över huvudet, spänne ordagrant; 'säker passform' borta. |
| 10605 | 10472326660362 | GODKÄND | | | | 8 sandpåsar à 1,25 kg, nylon, justerbara remmar ordagrant; 10 kg ur titeln, och 8 x 1,25 = 10 stämmer. Ingen dubblett av den skrivna Viktväst Tunturi (10470997197066, annan SKU). |
| 10606 | 10472270561546 | GODKÄND | | | | Boxningshandskar står i källan (R7). 12 oz, ventilationshål, handledsstöd, sidostygnad tumme, sparring ordagrant. 'Förhindrar skador' (två gånger), hudvänligt och Tyskland borta, så inget skadeförebyggande påstående finns kvar. SEO skiljer sig från DRAFT-syskonen 10/14 oz. |
| 10607 | 10472279572746 | GODKÄND | | | | Fyra entydiga fakta (endast boxningsträning, polyuretan, tumplatta/rörlighet, S/M), allt 'enligt tillverkaren' där det behövs. SEO med S/M skiljer sig från syskonet Jaguar L/XL (10475517804810). |
| 10579 | 10462783897866 | AVVISAD (bekräftad) | | | | Avvisningen bekräftas. Samma titel, färg, pris (139 kr) och källtext som redan skrivna 10472305393930 (SKU AHF-034 mot AHF-033), ingen storlek i källan. Texten kan inte skilja produkterna åt, och SEO-titeln skulle krocka. Kräver beslut om dubbletten. |
| 10580 | 10472305557770 | AVVISAD (bekräftad) | | | | Avvisningen bekräftas. Titeln säger svart-röd men den enda varianten heter 'M / black' (AHF-087, 119 kr). Källan nämner ingen färg (R3). |
| 10596 | 10472271511818 | AVVISAD (bekräftad) | | | | Avvisningen bekräftas. Titeln säger Medium 105 cm, källan 'Abdominal Power Belt Large' och 'Large 105cm' (R3). Källan består dessutom mest av skadeförebyggande påståenden. |
| 10603 | 10588451471626 | AVVISAD (bekräftad) | | | | Avvisningen bekräftas. Titeln säger 10 kg, men produkten har två varianter med olika pris (1 499 och 739 kr) som bara heter som sin SKU, och källan nämner ingen vikt (R3). |

## Öppna frågor till David
1. 10601 Viktlyftarbälte: R5 tillåter 'stödjer mage och rygg' ordagrant med 'enligt tillverkaren'. Ska stödpåståenden på bälten och handledsstöd ändå strykas (c_granskarprompt räknar 'skydd/stöd' som säkerhetsområde)?
2. 10579 mot 10472305393930: samma produkt (AHF-033/034)? Slå ihop, avaktivera eller skriv med storlek när den är känd?
3. Källor som uppenbart gäller en annan SKU (10588, 10594, 10601): räcker det att utelämna storlek och kod, eller ska de avvisas enligt R3 ('källan stämmer inte')?
4. Ska Stretchgummiset och liknande sammansättningar av källans ord föras in i `godkanda_typord`?

## Oklart i regelboken
- R3 säger 'källan stämmer inte med titeln', men inte vad som gäller när källan inte stämmer med SKU eller variantnamn och titeln är tyst.
- R4 gäller lastgräns. Motstånd i kg, vikt per bandfärg och västens maxvikt nämns inte, så det är oklart om de ska skrivas 'enligt tillverkaren'.
- R7 säger inte om ett typord som bildats av två av källans ord räknas som att 'källan använder ordet'.
- R5 och c_granskarprompt säger olika saker om stödpåståenden (R5 tillåter dem ordagrant, prompten underkänner 'skydd/stöd'), och regelboken säger inte att den andra regeln upphävs.
