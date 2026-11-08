# Granskningsutlåtande k_47a2: produkter som tidigare avvisats som redan skrivna eller dubbletter (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsning med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan texter-klara får faktatext även i tidigare utanför-kategorier; Giant/Liv-slutsiffran), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och formatet i `k_utlatande_43.json`. Leverantörens ursprungstexter för 48101–48103 finns i `rapporter/shopify-original-2026-10-31/facit30-original.json` och användes som egen källa (live-texten för dessa är vår egen tidigare text och räknas inte som källa, R3).

Alla fyra utkast är ACTIVE med lager > 0; ingen har taggen På beställning och inget utkast har leveranstidsmeningen. Standardblocket är exakt rätt på alla. Titel ≤70 tecken och ≤2 kommatecken, SEO ≤43, meta 138–148 tecken efter rättning, "Passar för" finns. Titel, SEO och meta är unika mot alla andra utkast-/utlåtandefiler i `vag2_skriv` och mot butikens titlar (sökning Union Lite, Niteline, Curlstångspaket, 606 samt streckkoderna). Inga hälso-, säkerhets-, skydds-, prestanda- eller kvalitetslöften finns (synlighet, säkerhet, hållbar, stabil, nybörjare utelämnade). Varje rättning är ETT sammanhängande före/efter-par per fält och före-texten förekommer exakt en gång i utkastet (kontrollerat i python). `skrivfil_kontroll.py` på de rättade texterna: 0 varningar, 1 FEL (spärr på 48101, se nedan).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_47a2.json`.

## Resultat: 0 GODKÄND, 4 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 48101 | 10475431657738 | k_47a2_utkast.json | RÄTTA | meta, html |
| 48102 | 10472332034314 | k_47a2_utkast.json | RÄTTA | seo_title, meta, html |
| 48103 | 10636758286602 | k_47a2_utkast.json | RÄTTA | meta |
| 48104 | 10472232943882 | k_47a2_utkast.json | RÄTTA | meta, html |

## Rättningar (före → efter)

### 48101 (10475431657738)

Live ACTIVE, 92915196SC, EAN 8713249282862, lager 24, ingen På beställning-tagg. Utkastet är live-texten ordagrant. Ursprungskällan finns i rapporter/shopify-original-2026-10-31/facit30-original.json (leverantörens svenska text): standardstrålkastare med inbyggd reflektor, 15 LUX, kan anslutas till dynamon, passar bäst för klassiska och retrocyklar, automatisk ljussensor, Dark Chrome. Alla uppgifter stöds; ljussensorn står i egen källa (R1), webbens splittrade uppgift påverkar inte. 'bättre synlighet' och 'extra säkerhet' rätt utelämnade. Rättat: inledningen 'Namn är en typord' i meta och html (skriptvarning). OBS: produkten står på spärrlistan (tidigare-avvisade-2026-11-04, skäl 'redan skriven, saknar bara taggen'); skrivfil_kontroll.py ger FEL tills en ny undantagsrad läggs till (bara tillägg) med hänvisning till Davids beslut 2026-11-08. Annars bara taggen texter-klara.

- **meta** före: `'AXA LUX 606 AUTO är en LED-strålkastare på 15 lux med inbyggd reflektor och automatisk ljussensor. Kan anslutas till dynamon. Passar klassiska cyklar.'`
  efter: `'LED-strålkastaren AXA LUX 606 AUTO har 15 lux, inbyggd reflektor och automatisk ljussensor och kan anslutas till dynamon. Passar klassiska cyklar.'`
- **html** före: `'<p>AXA LUX 606 AUTO är en LED-strålkastare på 15 lux med inbyggd reflektor och automatisk ljussensor.'`
  efter: `'<p>LED-strålkastaren AXA LUX 606 AUTO har 15 lux, inbyggd reflektor och automatisk ljussensor.'`

### 48102 (10472332034314)

Live ACTIVE, SKU/EAN 2906269724573, lager 3, ingen På beställning-tagg; frisläppt i undantag_2026-11-05 (omprovning-barn) och omfattas av beslutet 2026-11-08. Ursprungskällan (facit30-original.json, svensk) har 'Max. lastkapacitet: 100 kg' med etikett och enhet, så 'enligt tillverkaren' är rätt (R4/v1.10); samma som skrivna syskon Lite S Svart/Neochrome. Användarhöjd 105–125 cm rätt utelämnad (motsägs av scootshop.net 110–145 cm, R2); 'nybörjare', 'hållbar', 'mjuk och stabil' rätt utelämnade. Rättat: SEO-titeln utan färg skiljer inte från skrivna Lite S Svart/Neochrome/Lime, färgen läggs till (30 tecken); särskrivningen 'Total höjd' blir 'Totalhöjd' i meta och html, och raden Färg: Blå läggs till som på syskonen. Inte dubblett: egen EAN/färg.

- **seo_title** före: `'Stuntscooter Union Lite S'`
  efter: `'Stuntscooter Union Lite S, Blå'`
- **meta** före: `'Total höjd 690 mm.'`
  efter: `'Totalhöjd 690 mm.'`
- **html** före: `'<li>Total höjd: 690 mm</li>\n<li>Hjul: 100 mm, 88A</li>\n<li>Kompression: IHC</li>\n<li>Vikt: 3,293 kg</li>\n<li>Lager: ABEC-9</li>'`
  efter: `'<li>Totalhöjd: 690 mm</li>\n<li>Hjul: 100 mm, 88A</li>\n<li>Kompression: IHC</li>\n<li>Vikt: 3,293 kg</li>\n<li>Lager: ABEC-9</li>\n<li>Färg: Blå</li>'`

### 48103 (10636758286602)

Live ACTIVE, 100055-00004-0036, EAN 4260200840851, lager 85, ingen På beställning-tagg. Ursprungskällan (facit30-original.json, Gorilla Sports svenska text) har 'Maximal belastning curlstång: 180kg' med etikett och enhet, så raden med 'enligt tillverkaren' får stå (R4); lastlöftet i metan rätt borttaget. Övriga uppgifter (120 cm, 30 mm, 8 kg, 31 mm, 2 x 1,25/2 x 2,5/4 x 5 kg, två stjärnlås, 35 kg) står ordagrant i källan. Delarna summerar till 35,5 kg mot källans 35 kg; godtas som tidigare (titeln/varunamnet anger 35 kg). Rättat: metans första mening saknade verb. Unik mot andra Curlstångspaket i butiken.

- **meta** före: `'Curlstångspaket med krommade viktskivor och en curlstång på 120 cm, totalt 35 kg.'`
  efter: `'Curlstångspaketet innehåller krommade viktskivor och en curlstång på 120 cm, totalt 35 kg.'`

### 48104 (10472232943882)

Live ACTIVE, 90900495SC, EAN 8713249258706, lager 6, ingen På beställning-tagg. Live-källan är leverantörens svenska text: USB-uppladdningsbara, 4 LED, brinntid 6 h bak och 11 h fram (entydigt i löptexten), 4 ljuslägen, batterilåg indikator, gummiband, mått 110 x 70 x 30 mm. Synlighet 450 m, 'små och kompakta' och AXA:s säkerhetstext rätt utelämnade (belysning frisläppt 2026-11-08, inga säkerhetslöften). Inte exakt dubblett av 10475622400266 (90900495KC, annan EAN), enligt dubblettbeslutet 2026-11-05; titel, SEO och meta skiljer sig. Rättat: 'batterilåg indikator' är otydlig svenska och blir 'indikator för låg batterinivå' i meta och 'Låg batterinivå' i specifikationen.

- **meta** före: `'4 ljuslägen och batterilåg indikator.'`
  efter: `'4 ljuslägen och indikator för låg batterinivå.'`
- **html** före: `'<li>Indikator: Batterilåg</li>'`
  efter: `'<li>Indikator: Låg batterinivå</li>'`

## Spärr som måste hanteras före skrivning

48101 (10475431657738) står i `sparr_tidigare_avvisade.csv` (spärren tidigare-avvisade-2026-11-04) med skälet att den redan är skriven och bara saknar taggen. Den finns inte i `undantag_2026-11-05.csv`, så byggskriptet stoppar den. Produkten omfattas av Davids beslut 2026-11-08 (aktiv, utan texter-klara). Lägg till en ny undantagsrad (bara tillägg, inga befintliga rader ändras) eller hoppa över produkten.

## Avvisade (k_47a2_avvisade.json)

Rätt avvisade: 48202 (tunn och motsägande källa), 48203 och 48208–48210 (exakta dubbletter, samma SKU/EAN), 48204 (källan motsäger sig, varianten M/L har slutsiffra 6 utanför tabellen), 48205 (Kona, slutsiffreregeln gäller inte), 48207 (Romet, storlek okänd).

Avvisningsskälet är föråldrat, kan lyftas till nytt utkast (inte gjort här):
- 48201 (10673180410122, Liv Allure E+ 1, Sunset Ivory, 5600004105): skälet säger att slutsiffran bara räknas som ramstorlek om David beslutat; David beslutade 2026-11-08 att Giant/Liv-slutsiffran gäller (5 = M). Den skrivna 10673177952522 har 5600004104 (4 = S), alltså annan storlek och ingen exakt dubblett (beslut 2026-11-05). Lager 0 och taggen På beställning, så leveranstidsmeningen krävs; titeln måste ange M. Live-källan är säljtext som måste rensas.
- 48206 (10523487240458, Giant XTC SLR 29 1 (2026) Abyss Black, 1119019188): slutsiffra 8 = XL enligt samma beslut; den skrivna 10502528336138 har varianterna M (…185) och L (…187). Annan storlek, ingen exakt dubblett. Lager 0, På beställning. Källan är säljtext.
