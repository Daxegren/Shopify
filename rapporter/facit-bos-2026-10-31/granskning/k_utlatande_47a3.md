# Granskningsutlåtande k_47a3: produkter som tidigare avvisats som redan skrivna eller dubbletter (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsning med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan texter-klara får faktatext även i tidigare utanför-kategorier; Giant/Liv-slutsiffran), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md`/`k_utlatande_47a2.md` och formatet i `k_utlatande_43.json`.

Utkastarens påstående att leverantörens original inte finns kvar stämmer inte för 48301–48304: originalen finns i `rapporter/shopify-original-2026-10-31/facit30-original.json` och användes som egen källa. Alla uppgifter i de fyra utkasten stöds av originalen. 48305 och 48306 bygger på leverantörens live-text.

Alla sex utkast är ACTIVE; 48301–48305 har lager > 0, 48306 har lager 0 och taggen På beställning (leveranstidsmeningen finns bara där). Standardblocket är exakt rätt på alla. Titel ≤70 tecken och ≤2 kommatecken, SEO ≤43, meta 117–150 tecken med verb efter rättning, "Passar för" finns. Titel, SEO och meta är unika mot alla andra utkast-/skrivfiler (träffar bara mot samma produkts äldre filer) och mot butiken (sökning på EAN, SKU och Roddhandtag, Glute, Höftband, Miniband, Real Melon, Mini FR, Talon E+ 2 EX). Inga exakta dubbletter (samma EAN/SKU) finns. Inga hälso-, säkerhets-, skydds-, utvecklings-, prestanda- eller kvalitetslöften finns. Varje rättning är ETT sammanhängande före/efter-par per fält och före-texten förekommer exakt en gång i utkastet (kontrollerat i python). `skrivfil_kontroll.py` på de rättade texterna: 0 varningar, 2 FEL (spärrar på 48304 och 48306, se nedan).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_47a3.json`.

## Resultat: 1 GODKÄND, 5 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 48301 | 10636752584970 | k_47a3_utkast.json | RÄTTA | meta, html |
| 48302 | 10636616040714 | k_47a3_utkast.json | RÄTTA | meta |
| 48303 | 10636636782858 | k_47a3_utkast.json | RÄTTA | meta, html |
| 48304 | 10470922682634 | k_47a3_utkast.json | GODKÄND | – |
| 48305 | 10474112975114 | k_47a3_utkast.json | RÄTTA | meta, html |
| 48306 | 10682106085642 | k_47a3_utkast.json | RÄTTA | html |

## Rättningar (före → efter) och skäl

### 48301 (10636752584970): RÄTTA

Live ACTIVE, SKU 100147-00004-0001, EAN 4260200840325, lager 353, ingen På beställning-tagg, ingen annan listning med samma EAN/SKU. Leverantörens originaltext finns i rapporter/shopify-original-2026-10-31/facit30-original.json (tvärtemot att_bekrafta) och användes som egen källa (R3). Originalet (svenskt): parallellt roddhandtag 76 cm, används i kabelrodd och latsdragsmaskin, diameter 2,5 cm, 'Maximal belastning: 200kg' (svensk rad med etikett och enhet, R4: en gång enligt tillverkaren, rätt), roterande, 4,5 kg, krom. Alla uppgifter stöds; 'stärker ryggen' rätt utelämnat. Rättat (R11/meta med verb): första meningen i meta och beskrivning saknade finit verb.

- **meta** före: `'Parallellt roddhandtag på 76 cm i krom, roterande, för kabelrodd och latsdragsmaskin.'`
  efter: `'Det parallella roddhandtaget i krom är 76 cm långt, roterar och används för kabelrodd och latsdragsmaskin.'`
- **html** före: `'<p>Parallellt roddhandtag på 76 cm i krom, avsett för kabelrodd och latsdragsmaskin.'`
  efter: `'<p>Det parallella roddhandtaget i krom är 76 cm långt och avsett för kabelrodd och latsdragsmaskin.'`

### 48302 (10636616040714): RÄTTA

Live ACTIVE, SKU 4407, EAN 4251563244073, lager 80, ingen På beställning-tagg. Leverantörens originaltext finns i rapporter/shopify-original-2026-10-31/facit30-original.json (tvärtemot att_bekrafta) och användes som egen källa (R3). Originalet: set om 3, bärpåse, turkos/mintgrön lätt, rosa medium, grå tung, 65 % polyester/35 % bomull, gummerad insida, omkrets 76 cm, bredd 8 cm, träna hemma eller på gymmet. Alla uppgifter stöds; 'för bättre grepp', 'effektivt', 'perfekta', 'maximera' rätt utelämnade. Inte exakt dubblett av skrivna 10636637503754 (Höftband Hip Glute Band i Tyg, samma mått men annan SKU 101245-00065-0001 och EAN 4250663117263); titel, SEO och meta skiljer sig. Rättat (R11): meta 'Hip Glute Band ... är tre höftband' var nästan cirkulär.

- **meta** före: `"Hip Glute Band från Women's Health är tre höftband i tyg med gummerad insida, i tre motståndsnivåer."`
  efter: `"Höftbanden i setet Hip Glute Band från Women's Health är av tyg med gummerad insida och har tre motståndsnivåer."`

### 48303 (10636636782858): RÄTTA

Live ACTIVE, SKU 101246-00065-0001, EAN 4250663117270, lager 1 405, ingen På beställning-tagg. Leverantörens originaltext finns i rapporter/shopify-original-2026-10-31/facit30-original.json (tvärtemot att_bekrafta) och användes som egen källa (R3). Originalet: fem latexband med påse, olika tjocklek/färg, märkta med motstånd, grön ca 4,5, blå ca 6,8, gul ca 9, röd ca 13,5, svart ca 18 kg (motstånd, inte lastgräns, R4), omkrets 60 cm, bredd 5 cm. Inte dubblett av Miniband TRYM 10636609421578 (annan EAN och andra motståndsvärden). Rättat: meta saknade verb i första meningen; 'hemma' i Passar för står inte i källan (R1).

- **meta** före: `'Miniband i latex, ett set med fem korta gummiband i olika färger och motstånd, från ca 4,5 till ca 18 kg.'`
  efter: `'Setet har fem korta gummiband i latex i olika färger och motstånd, från ca 4,5 till ca 18 kg.'`
- **html** före: `'<li>Dig som vill träna med korta motståndsband hemma</li>'`
  efter: `'<li>Dig som vill träna med korta motståndsband</li>'`

### 48304 (10470922682634): GODKÄND

Live ACTIVE, SKU MUA.G088M.XS, EAN 4260243725184, lager 7, en variant. Leverantörens originaltext finns i rapporter/shopify-original-2026-10-31/facit30-original.json (tvärtemot att_bekrafta) och användes som egen källa (R3). Originalet (engelskt): vattenmelonmönster, 3–7 år, tre tjocklekar på stoppningen, Fidlock magnetisk med en hand, MACS 12 ventilationsöppningar, Spin Dial baktill, XXS/S 46–52 cm, under 300 g, polykarbonat/EPS, vintertäcke tillval, CoolMax, 30 graders maskintvätt. Alla uppgifter stöds. Inga skydds- eller säkerhetslöften: 'adequate ventilation even on hot days', 'comfortable and hygienic', 'fit precisely', 'grow with your child' utelämnade; hjälmar har ingen lastrad (v1.10). Inte dubblett: Hjälm Melon Real Melon 10472261255434 är storlek XL med annan SKU/EAN. OBS: spärrad (utanfor-tills-vidare-2026-11-04); skrivfil_kontroll.py ger FEL tills en undantagsrad läggs till (bara tillägg) med hänvisning till Davids beslut 2026-11-08 om aktiva produkter i tidigare utanför-kategorier.


### 48305 (10474112975114): RÄTTA

Live ACTIVE, SKU TAB25-6830, EAN 5904257311009, lager 1, en variant, ingen På beställning-tagg. Live-texten är leverantörens svenska text (egen källa). Uppgifterna (aluminiumram, hjul och vevparti, 1 växel, V-bromsar, ramstorlek 24,5 cm ur den entydiga delen av en trasig rad, ca 105–115 cm, stödhjul, kedjeskydd, stödstång, 16 tum ur titel och tagg) stöds. 'för flickor', 'maximal säkerhet', 'säkert', 'hållbarhet', 'utmärkt val' och oklar 'hjulvikt 8 kg' rätt utelämnade. Inte dubblett: 10462813225226 är 18 tum (handle), TAB25-6860, EAN 5904257311030, ram 26,5 cm; 10525598023946 är 14 tum. Rättat: upprepningen 'hjul, ram, hjul' i meta; 'ca' föll bort i cyklistlängden (källan säger ca).

- **meta** före: `'Barncykeln Tabou Mini FR har 16-tums hjul, ram, hjul och vevparti i aluminium, 1 växel och V-bromsar. Färg: rosa-lila.'`
  efter: `'Barncykeln Tabou Mini FR i rosa-lila har 16-tums hjul, 1 växel och V-bromsar. Ram, hjul och vevparti är av aluminium.'`
- **html** före: `'<li>Cyklistlängd: 105–115 cm enligt tillverkaren</li>'`
  efter: `'<li>Cyklistlängd: Ca 105–115 cm enligt tillverkaren</li>'`

### 48306 (10682106085642): RÄTTA

Live ACTIVE, SKU 5090005108, EAN 4711291329805, lager 0 med taggen På beställning (leveranstidsmeningen finns, R13/v1.8). Ramstorlek XL ur slutsiffran 8 enligt Davids beslut 2026-11-08 (Giant); källan listar XL 53,5 cm för 187–200 cm. Skrivna syskonet 10682105463050 säljer S/M/L (5090005104/05/07), så XL är egen artikel; titel, SEO och meta skiljer sig. Motor, batteri, gaffel, växlar, bromsar, däck och setets delar stämmer mot källan; räckvidd en gång 'enligt tillverkaren' (praxis), totalt två 'enligt tillverkaren'. Säljfraser ('powerful', 'smoothly', 'world's largest') rätt utelämnade. Rättat (v1.10, praxis k_41c): texten ska också säga att maximal lastgräns inte är känd. OBS: spärrad (titeldubbletter-2026-11-04); skrivfil_kontroll.py ger FEL tills en undantagsrad läggs till (bara tillägg) med hänvisning till beslutet 2026-11-08.

- **html** före: `'samt fram- och bakljus.</p>'`
  efter: `'samt fram- och bakljus. Maximal lastgräns är inte känd.</p>'`

## Avvisade (k_47a3_avvisade.json)

Alla sju avvisningar står sig; ingen lyfts. Kontrollerat live på streckkod: 48307 (G340/8445960014155 delas med skrivna 10656691749130), 48308 och 48309 (25TUPLA033/8717842039038, tre listningar), 48310 (6430062511888 = S/M-varianten i skrivna 10581112783114), 48312 och 48313 (SRX-SPEED-MAG/8029975999371, fyra listningar). 48311 (Rocket Lite MG): originalet säger aluminiumram medan modellnamnet MG och webben anger magnesium, motsägande källa (R2), rätt avvisad.

## Frågor till David

1. 48304 och 48306 står på spärrlistan (utanfor-tills-vidare respektive titeldubbletter, 2026-11-04). En undantagsrad (bara tillägg) med hänvisning till besluten 2026-11-08 behövs innan skrivfilen byggs.
2. Höftband: två aktiva listningar med samma mått och material (Women's Health 10636616040714 och 'i Tyg' 10636637503754) men olika EAN. Enligt regeln 2026-11-05 är de inte dubbletter och får egna texter; säg till om de ska slås ihop.
3. Live-texten på Rocket Lite MG 14 tum (10472330461450) säger aluminiumram men webben anger magnesium. Texten är redan publicerad och kan vara fel.
4. Spinningcykel Toorx SRX Speed Mag finns aktiv i fyra listningar och Tunturi Platinum Hex 37,5 kg i tre (samma EAN); lagret behöver flyttas innan kopiorna arkiveras.
