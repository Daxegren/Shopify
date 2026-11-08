# Granskningsutlåtande k_47b3: Gymstick-trampolin, kinesiologitejp och fotledsstöd (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsning med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan texter-klara får faktatext även i tidigare utanför-kategorier, bland annat trampoliner och rehab; inga hälso-, säkerhets-, prestanda- eller kvalitetslöften; lastgräns v1.10), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och `k_utlatande_47b1.md`, formatet i `k_utlatande_43.json`. Tillverkarsidorna på gymstick.com lästes av granskaren för alla tre; SKU och EAN stämmer.

Alla tre utkast och alla elva avvisade är ACTIVE med lager > 0. Ingen av de tre har taggen På beställning och inget utkast har leveranstidsmeningen. Standardblocket är exakt rätt (jämfört med `b_skriv_24.json`). Titel 24–37 tecken och högst ett kommatecken, SEO 24–37 tecken, meta 124–135 tecken med verb, "Passar för" finns. Titel, SEO och meta krockar inte med andra filer i `vag2_skriv` eller med butikens titlar (sökning Kinesiolog, tejp, Fotled, Trampolin och de tre streckkoderna). Inga cirkulära inledningar. Varje rättning är ETT sammanhängande före/efter-par per fält, och före-texten förekommer exakt en gång i utkastet (kontrollerat i python). `skrivfil_kontroll.py` på de rättade texterna: 0 innehållsfel; 48502 och 48503 stoppas av spärren `tidigare-avvisade-2026-11-04` tills en undantagsrad (bara tillägg) med hänvisning till Davids beslut 2026-11-08 läggs in (R14).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_47b3.json`.

## Resultat: 1 GODKÄND, 2 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 48501 | 10581106524426 | k_47b3_utkast.json | RÄTTA | html |
| 48502 | 10581108228362 | k_47b3_utkast.json | GODKÄND | – |
| 48503 | 10581104623882 | k_47b3_utkast.json | RÄTTA | html |

## Bedömning per produkt

### 48501 (10581106524426): RÄTTA

Live ACTIVE, två varianter 61026 (EAN 6430016908283, lager 105) och 61026-SC (utan EAN, lager 44), båda 1 149 kr, taggar Gymstick och Trampoliner, ingen På beställning-tagg. https://www.gymstick.com/fitness-trampoline.html (SKU och EAN stämmer, läst av granskaren): hopfällbar 'for easy storage', 32 steel springs, 102 x 102 x 125 cm, Iron 76 %/PVC 8 %/PE 10 %/EPE 5 %/NBR 1 %, Max user weight (kg): 100. Allt i texten stämmer. Trampoliner är frisläppta 2026-11-08 med lastgräns enligt v1.10: etiketterad rad med enhet på tillverkarsidan för exakt SKU/EAN får stå en gång 'enligt tillverkaren'. Löfteskonst ur live-texten och tillverkarsidan (rolig och effektiv, kompakt och stabil, kondition/koordination/balans, skonsam mot lederna, 'wellbeing of respiratory and circulatory system') rätt utelämnad; inga hälso-, säkerhets- eller stabilitetsord. RÄTTA: användarvikten stod två gånger (löptext och specifikation); R4/R5 säger en gång, praxis k_47b1 är bara specifikationsraden. Titel/SEO unika mot butiken och alla vag2-filer (Tunturi 4-folding, Toorx, Hammer JumpStep är andra artiklar); ingen dubblett på EAN. Spärrlistan: 0 fel i skrivfil_kontroll. Fråga: 61026-SC saknas hos tillverkaren; texten låser inte varianten men anger Artikelnummer 61026.

- **html** före: `'Måtten är 102 x 102 x 125 cm, och enligt tillverkaren är maximal användarvikt 100 kg.</p>'`
  efter: `'Måtten är 102 x 102 x 125 cm.</p>'`

### 48502 (10581108228362): GODKÄND

Live ACTIVE, titel 'Kinesiology Tape (beige)' men sex färgvarianter 63026-BE/BL/CAM/FIN/PI/TU med egna EAN, 99 kr (FIN 79 kr), lager 12 909, ingen På beställning-tagg. https://www.gymstick.com/kinesiology-tape.html (SKU 63026, EAN 6430016901994 = CAM-varianten, läst av granskaren): 97 % Cotton/3 % Spandex, 500 x 5 x 0,1 cm, 0,08 kg, latex-free, max stretch 75 %, instructions for use, 'Available in several different colors'. Allt i texten stämmer. v1.9: samma artikel i olika färg med lager; titel, SEO och text låser ingen färg eller pris (beige ur live-titeln rätt borttaget). Alla smärtlindrings-, läknings-, skadeförebyggande-, stöd-, prestanda- och kvalitetsord ur källan (pain relief, healing, prevent/treat injuries, supports muscles, 7 dagar, vatten, medical grade/does not irritate skin, högkvalitativ) rätt utelämnade; 'latexfri' och 'max töjning' är materialuppgifter. Typordet Kinesiology Tape följer titelns ord (R7). Ingen annan kinesiologitejp i butiken; unik titel/SEO/meta. Spärr: produkten står i tidigare-avvisade-2026-11-04 och skrivfil_kontroll ger FEL tills en undantagsrad (bara tillägg) med hänvisning till Davids beslut 2026-11-08 läggs in (R14). Fråga: FIN kostar 79 kr; att den är samma tejp i annan färg kan inte styrkas på tillverkarsidan.

### 48503 (10581104623882): RÄTTA

Live ACTIVE, en variant 63060, EAN 6430062510744, 79 kr, lager 453, ingen På beställning-tagg. https://www.gymstick.com/ankle-support-1-0-one-size.html (SKU och EAN stämmer, läst av granskaren): justerbart elastiskt band, Rubber 30 %/Polyester 35 %/Nylon 35 %, Grey-White, 21,5 x 50,5 x 1 cm, 0,05 kg. Specifikationen stämmer; stabiliserings-, värme-, komfort- och skadeförebyggande löften rätt utelämnade. RÄTTA: 'andas och leder bort fukt' är funktions-/prestandaegenskaper på en stöd-/rehabprodukt och tas bort enligt uppdraget (inga subtila löften; praxis k_utlatande_4x utelämnar fukt- och andningsegenskaper på skyddsprodukter); 'i storleken En storlek' blir 'i en storlek' (språk). Inte dubblett: Fotledsstöd 2.0 (10593407500554) är annan modell; unik titel/SEO/meta. Spärr: tidigare-avvisade-2026-11-04, skrivfil_kontroll ger FEL tills en undantagsrad (bara tillägg) med hänvisning till beslutet 2026-11-08 läggs in (R14).

- **html** före: `'<p>Fotledsstödet 1.0 från Gymstick har ett justerbart elastiskt band. Enligt tillverkaren är det elastiskt, andas och leder bort fukt. Materialet är gummi, polyester och nylon, och stödet finns i storleken En storlek.</p>'`
  efter: `'<p>Fotledsstödet 1.0 från Gymstick har ett justerbart elastiskt band. Materialet är gummi, polyester och nylon, och stödet finns i en storlek.</p>'`

## Avvisade (k_47b3_avvisade.json)

Alla elva avvisningar står sig; ingen är uppenbart fel. 48505 Knästöd 1.0 (63062): tillverkarsidan säger både knee och ankle support, och live-texten består bara av löften; motsägande källa (R2, beslutet 2026-11-08). 48511 har redan texter-klara. Övriga saknar egen källa och tillverkarsida för exakt artikel, har motsägande produkttyp (48506, 48508) eller oförklarade varianter (48507, 48513).

## Löften (beslutet 2026-11-08)

Alla tre texterna genomsöktes efter hälso-, säkerhets-, skydds-, utvecklings-, prestanda- och kvalitetsord, även subtila (stöd, stabil, skydd, lindring, återhämtning, förebygga, komfort, bekväm, andas, fukt, hållbar, slitstark, kvalitet, skonsam, kondition, balans). Efter rättning finns inget sådant. "Fotledsstöd" och "Kinesiology Tape" är produktnamn och typord, inte löften. "Latexfri" och "max töjning 75 %" är materialuppgifter. "Hopfällbar för enkel förvaring" är ordagrant ur källan och beskriver bara förvaring.

## Frågor till David

1. Trampolinen har en extra variant 61026-SC (utan EAN, lager 44, samma pris) som inte finns hos tillverkaren. Är det samma trampolin (till exempel ett annat lager)? Texten anger Artikelnummer 61026.
2. Kinesiologitejpens variant FIN kostar 79 kr mot 99 kr för övriga färger. Tillverkarsidan visar inte färgkoderna. Om FIN är en annan längd eller annan artikel stämmer inte "5 m" i titeln för den.
3. Spärren: 48502 och 48503 behöver undantagsrader i spärrlistans undantagsfil (bara tillägg) innan skrivfilen byggs.
