# Granskningsutlåtande k_46sak1: säkerhets- och barnprodukter efter Davids beslut 2026-11-08

Granskaren har bara läst i Shopify och har inte ändrat något där eller committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS). `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan text får faktatext även i tidigare utanför-kategorier), LARDOMAR, butiksprofilen, `c_granskarprompt.md` samt praxis och format i `k_utlatande_43.md` och `k_utlatande_43.json`.

Alla 13 utkast är ACTIVE, har lager > 0 och har en enda variant (Default Title). Ingen av dem har taggen På beställning, och ingen leveranstidsmening finns. Standardblocket är exakt likadant som i `b_skriv_24.json`. "Passar för" finns på alla. Titlarna är 25–46 tecken med högst 2 kommatecken, SEO-titlarna 18–35 tecken och metatexterna 131–154 tecken med verb. Titlar, SEO-titlar och metatexter krockar inte med andra utkast- eller skrivfiler. Butiken söktes på modellnamn och streckkod: inga exakta dubbletter (R12a), men SEO-titeln för 46001 skiljs från det skrivna färgsyskonet. Varje rättning är ett sammanhängande före/efter-par per fält, och före-texten finns exakt en gång i fältet (kontrollerat i python). `skrivfil_kontroll.py` på de rättade texterna ger inga fel utöver spärrarna nedan.

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_46sak1.json`.

## Resultat: 6 GODKÄND, 7 RÄTTA, 0 UNDERKÄND

| nr | id | dom | rättning (före → efter) |
|---|---|---|---|
| 46001 | 10411860394250 | RÄTTA | seo_title: `Styrkälke Stiga Snowpower` → `Styrkälke Stiga Snowpower, Rosa` |
| 46002 | 10411907940618 | RÄTTA | titel: `Vikbart lås Axa Fold Lite C100 med kod` → `Vikbart Lås Axa Fold Lite C100 med Kod`; seo_title: `Vikbart lås Axa Fold Lite C100` → `Vikbart Lås Axa Fold Lite C100` |
| 46003 | 10460948234506 | RÄTTA | html: `<li>Modell: Frozen Lake</li>` → `<li>Modell: Mosaique</li> <li>Utförande: Frozen Lake, matt</li>` |
| 46004 | 10462148722954 | GODKÄND | – |
| 46005 | 10462155407626 | GODKÄND | – |
| 46006 | 10462175101194 | RÄTTA | titel: `Baklykta Axa Go Steady för skärm` → `Baklykta Axa Go Steady för Skärm` |
| 46007 | 10462188503306 | GODKÄND | – |
| 46016 | 10468736925962 | RÄTTA | html: `<li>Modell: Venice</li>` → `<li>Modell: Posh</li> <li>Utförande: Venice, matt</li>` |
| 46022 | 10470922944778 | GODKÄND | – |
| 46018 | 10470888243466 | GODKÄND | – |
| 46019 | 10470898237706 | RÄTTA | titel: `Bromsskiva Shimano SM-RT66, 160 mm, 6 bultar` → `Bromsskiva Shimano SM-RT66, 160 mm, 6 Bultar`; html: `<li>Belägg: Harts och metall</li>` → `<li>Belägg: Harts och metall (med bromsoken BR-S700 och BR-S7000 bara harts)</li>` |
| 46020 | 10470900597002 | RÄTTA | titel: `Bromsskiva Shimano SM-RT66, 180 mm, 6 bultar` → `Bromsskiva Shimano SM-RT66, 180 mm, 6 Bultar`; html: `<li>Belägg: Metall och harts</li>` → `<li>Belägg: Metall och harts (med bromsoken BR-S700 och BR-S7000 bara harts)</li>` |
| 46023 | 10470925074698 | GODKÄND | – |

## Skäl per produkt

- **46001** (RÄTTA): Live ACTIVE, en variant 74-7122-07, EAN 7318687122070, lager 6, ingen På beställning. Alla uppgifter (ratt som styr två skidor, broms, reflektor fram och bak, plast, 5+) står i egen källa; 'hållbar', 'slitstark', 'säker åktur', 'dragkontrollkabel' rätt utelämnade. Rosa står i live-titeln. R12a: syskonet 10472281899274 (Svart och Grön, 74-7122-19, annan EAN) är skrivet med SEO 'Stiga SnowPower Styrkälke'; ingen dubblett men SEO-titeln skiljs med färgen. Spärrlistan: produkten står i en aktiv spärr i sparrlista.json; skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt nedan.
- **46002** (RÄTTA): Live ACTIVE, 59842095KB, EAN 8713249350073, lager 22. Allt i texten står i egen källa (100 cm, flexibla ben, stållänkar 5 mm med gummihölje, fyrsiffrig kod, hållare på flaskhållaren eller med remmar). 'Säkerhet: 7/15', 'härdade', stöldrisk, 'skydda hjulet' och anti-rattle rätt utelämnade. Typordet Vikbart lås ur källan; skrivna syskon heter 'Vikbart Lås'. Rättning: formatregeln för versaler i titel/SEO (format_regler.py). Inte dubblett av skrivna Fold Lite 100 (59841095KB, nyckel) eller Fold Lite 80.
- **46003** (RÄTTA): Live ACTIVE, MUA.M103M.XL, EAN 4260243725924, lager 7. Storlek XL/XXL 58–63 cm verifierad för exakt EAN och artikelnummer: https://meinhartje.com/en/melon-helmet-mosaique/08655119 (sökträff: MUA.M103M.XL, EAN 4260243725924, frozen lake matt, XL-XXL 58-63 cm). Tillverkarens modell är Mosaique och Frozen Lake är utförandet (syskon MUA.M103M.ML/.XS heter 'Mosaique frozen lake matt', https://meinhartje.com/en/print/product/4028973e81ba228101821bfae88e145f), så specifikationsraden 'Modell: Frozen Lake' rättas. Övriga uppgifter står i egen källa; 'perfekt skydd', 'stark', 'säkerhet' utelämnade. Vikt 'under 300 g' ur egen källa (återförsäljarens 0,32 kg gäller ML och troligen med förpackning). Titeln behåller live-namnet. Ej spärrad.
- **46004** (GODKÄND): Live ACTIVE, BLC2207888207, EAN 5420078882165, lager 4. Enda storlek i källan 46–50 cm, 280 g, 12 ventilationshål, Autofit, rem nära örat, lång skärm: allt ur egen källa. 'Extra skydd', 'skyddar ögon och ansikte', 'förhindra nyp' och märkeshistorik rätt utelämnade; 'automatisk passform' är källans funktionsbeskrivning, inget skyddslöfte. Pony ur live-titeln. Fox-syskonet (BLC2207888204) är DRAFT och annan EAN. Spärrlistan: produkten står i en aktiv spärr i sparrlista.json; skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt nedan.
- **46005** (GODKÄND): Live ACTIVE, VMESMRT64MEC, EAN 4550170451967, lager 25. 180 mm och CL ur live-titeln, Center Lock med spår och låsring, harts/metall ur källan; 'kraftfull', '10 % mer bromskraft' och 220 mm-jämförelsen rätt utelämnade. Bromsdel: ingen lastgräns (v1.10). Syskonet SM-RT64 160 (10472242446602) är annan EAN och oskrivet. Spärrlistan: produkten står i en aktiv spärr i sparrlista.json; skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt nedan.
- **46006** (RÄTTA): Live ACTIVE, 93913095SC, EAN 3379939130957, lager 7. Bakskärmsmontering, 4 min stå-ljus, inbyggd reflektor, dynamo ('Dünamo', entydigt), 6 V elcykelbatteri, 100 x 45 x 45 mm, 70 g, vitt matt hölje: allt ur egen källa; LED framgår av källans LED-rader. 'Synlig upp till 500 m', LED-livslängd och 'fantastisk design' rätt utelämnade (inga synlighetslöften). Rättning: formatregeln för versaler i titel.
- **46007** (GODKÄND): Live ACTIVE, 8A501521, EAN 8716808152118, lager 24. 375 mm, vevaxelöppning 120 mm, ABS svart, enkel-/trippeldrev, montering med vev och bakdrev ur egen källa. Skyddspåståendena (kläder, smuts, fukt) och den motsägande tandantalsraden rätt utelämnade (R2). Kedjeskydd är typordet och källans ord, inget löfte. Engelsk live-titel ersatt med källans svenska ord.
- **46016** (RÄTTA): Live ACTIVE, MUA.P108M.ML, EAN 4260243725436, lager 5. Storleken M/L 52–58 cm är nu verifierad för exakt EAN: https://meinhartje.com/en/melon-helmet-posh/08655100 (Venice matt, size M-L (52-58cm), Supplier Article Number MUA.P108M.ML, EAN 4260243725436). Tillverkarens modell är Posh och Venice är utförandet; specifikationsraden rättas. Övrigt ur egen källa (Fidlock med en hand, 12 lufthål, Spin Dial, PC/EPS, under 300 g, vinteröverdrag tillval); 'moderiktig', 'hållbar konstruktion' utelämnade. Ej spärrad.
- **46022** (GODKÄND): Live ACTIVE, MUA.K003M.XS, EAN 4260243722015, lager 11. Källan anger bara XXS/S 46–52 cm (3 till 7 år), som stämmer med artikelnumrets XS. Motiv, tre tjocklekar stoppning, Fidlock, MACS 12 hål, Spin Dial, PC/EPS, under 300 g ur egen källa. 'Växa med ditt barn', 'skydda dem', 'extra säkert EPS', 'sprider stötkrafter', 'hygienisk' rätt utelämnade. Inte dubblett av skrivna Real Melon (10470922682634, annan EAN). Spärrlistan: produkten står i en aktiv spärr i sparrlista.json; skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt nedan.
- **46018** (GODKÄND): Live ACTIVE, 14TUSCL158, EAN 8717842026984, lager 2. 2-delat set, Ø 30 mm, snäppfäste, 53 g, svart, syntetiskt ur egen källa. Typord Skivstångslås ur källan ('ABS-skivstångslåsen'); live-ordet Leverlås och taggen Cykellås är fel men taggen rörs inte. 'Säkert', 'starka lås som sitter stadigt' och 'perfekt' utelämnade; 'används för att hålla viktskivorna på stången' är avsedd användning, inget löfte. Kettlebell i källan rätt utelämnat ur Passar för. Spärrlistan: produkten står i en aktiv spärr i sparrlista.json; skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt nedan.
- **46019** (RÄTTA): Live ACTIVE, SMRT66-S, EAN 4550170598334, lager 24. SM-RT66, 6 bultar, 160 mm, låsplattor, harts/metall ur egen källa; 'pålitlig', 'jämn bromskraft', 'säker installation' utelämnade. Rättningar: formatregeln för versaler i titel; samma modellbegränsning som syskonet 46020 (egen källa där och https://www.bike-components.de/en/Shimano/SM-RT66-6-bolt-Brake-Rotor-p81603/: med BR-S700/BR-S7000 bara hartsbelägg) läggs till så att beläggsraden inte blir för vid. Ingen lastgräns (v1.10). Spärrlistan: produkten står i en aktiv spärr i sparrlista.json; skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt nedan.
- **46020** (RÄTTA): Live ACTIVE, SMRT66-M, EAN 4524667299554, lager 24. 6 bultar, 180 mm, rostfritt stål, ca 140 g, metall/harts ur egen källa. Källans rad 'endast med BR-S700 och BR-S7000 hartser!' är entydig i sak och bekräftas av https://www.bike-components.de/en/Shimano/SM-RT66-6-bolt-Brake-Rotor-p81603/ (med BR-S700 och BR-S7000 fungerar bara organiska/hartsbelägg); utkastet utelämnade den men påstod obegränsad beläggskompatibilitet, så begränsningen läggs till i specifikationen. Bromsoklistan rätt utelämnad. Rättning även av versaler i titel. Spärrlistan: produkten står i en aktiv spärr i sparrlista.json; skrivfil_kontroll.py stoppar den tills en undantagspost med Davids beslut 2026-11-08 läggs in (R14). Innehållet är granskat och dömt nedan.
- **46023** (GODKÄND): Live ACTIVE, 14TUSCL159, EAN 8717842026991, lager 6. Säljs i par, Ø 30 mm, 9 x 8 x 1,7 cm, 39 g, svart/krom, metall/syntetisk och fästsättet ur egen källa. 'Vikt: 39 ltr' är en trasig enhet på samma värde; 39 g står entydigt (R2, entydig del). 'Starkt grepp', 'säkert träningspass' utelämnade. Typord Fjäderklämmor ur källan; skrivna syskonet Olympic Spring Collars 50 mm (10472212463882) är annan artikel. Taggen Cykellås är fel men rörs inte.

## Löften och säkerhet

Titel, SEO, meta och beskrivning har genomsökts efter säkerhets-, skydds-, hälso-, utvecklings-, prestanda- och kvalitetsord, även dolda (säker, skydd, stabil, hållbar, slitstark, synlig, stark, robust, perfekt, pålitlig, grepp, stadig, förhindra, växer, komfort och liknande). Det enda som finns kvar är typordet Kedjeskydd. Utkastaren har tagit bort leverantörens löften genomgående: synlighet på 500 m, LED-livslängd, "10 % mer bromskraft", "extra skydd", "växer med barnet", säkerhetsklass 7/15 och "starkt grepp". Hjälmarna nämner ingen standard och inget skydd. Bromsdelarna och hjälmarna har ingen lastgräns, eftersom de undantas i v1.10.

## Spärrlistan: åtgärd före skrivning (R14)

`skrivfil_kontroll.py` stoppar 5 av utkasten. Det beror på aktiva spärrar i `shopify-sync/config/sparrlista.json`, inte på innehållet:
- 46001, 46005, 46019 och 46020 står i spärren `tidigare-avvisade-2026-11-04`.
- 46004 står i spärren `utanfor-tills-vidare-2026-11-04`.

De avvisades tidigare bara på grund av kategori (kälke, bromsdel, barnhjälm). Davids beslut 2026-11-08 släpper de kategorierna. Innan skrivfilen kan godkännas måste en undantagspost läggas till i spärrlistan, med `typ: undantag`, en id-fil och beslutet 2026-11-08. Det ska göras på samma sätt som `undantag-2026-11-05`. Domarna ovan gäller innehållet.

## Avvisade (k_46sak1_avvisade.json)

Alla 11 avvisningar stämmer. Ingen lyfts ur.
- 46008 och 46009: storleken som säljs går inte att avgöra, och vikterna motsäger varandra.
- 46010 och 46021: produkterna har redan text.
- 46011 och 46014: källan är tom.
- 46015: källan motsäger sig själv.
- 46012, 46013, 46017 och 46024: varianterna är olika artiklar med olika pris och artikelnummer.

## Att notera för David

- Melon-hjälmarna heter hos tillverkaren Mosaique (Frozen Lake) och Posh (Venice). Butikens titlar använder namnet på utförandet, och det behålls.
- Taggen Cykellås är fel på viktlåsen 46018 och 46023. Live-titlarna är dessutom felöversatta ("Leverlås", "Lever springlås"). Taggar rörs inte av textutrullningen.
- Bromsskivorna SM-RT66 får en beläggsbegränsning (med bromsoken BR-S700 och BR-S7000 bara harts). Den står ordagrant i 46020:s egen källa och på bike-components.de.
