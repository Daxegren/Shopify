# Stickprov k_09b–k_12 (live mot skrivfil)

Datum: 2026-11-04. Roll: Stickprov (endast läsning). Inget skrevs till Shopify. Inga nycklar skrevs ut.

## Metod och begränsningar
- 40 av 172 produkter (23 procent) hämtades live via `shopify_api.hamta_produkter` (4 anrop à 10). Fördelning: 09b 4, 10 8, 11a 6, 11bc 7, 11d 6, 11efg 4, 12 5 (minst 4 per fil).
- Urval: alla produkter som granskaren rättade prioriterades. Där en fil hade färre rättade än kvoten fylldes den med jämnt spridda godkända (09b 2 rättade + 2 godkända, 12 2 rättade + 3 godkända). I 11efg finns 4 rättade, de övriga i utlåtandet är underkända och ersatta, så de ingår inte.
- Jämfört tecken för tecken: titel, seo.title (null räknas som titeln), seo.description, descriptionHtml. Kontrollerat: taggen `texter-klara`, handle och status mot `_fore_`-filerna i `rapporter/shopify-original-2026-11-04/`, samt U+00AD, U+200B, U+FEFF.
- Begränsning: handle och status jämförs bara mot före-läget. Ändringar mellan före-läget och skrivningen av annan part, eller senare, fångas bara om värdet skiljer sig från före-filen. Källsanningen i språkgranskningen är kontrollerad mot före-texten i `shopify-original` (9635, 9726, 9842, 9804, 9881), inte mot tillverkarnas webbsidor.

## Resultat av live-jämförelsen
- Avvikelser i titel, seo.title, meta eller descriptionHtml: 0 av 40.
- Taggen `texter-klara` saknas: 0 av 40.
- Handle ändrad: 0. Status ändrad: 0.
- Osynliga tecken (U+00AD, U+200B, U+FEFF): 0.
- Rensning 2 (` (enligt tillverkaren)`): ingen av de 40 ingår i rensning 2 (178 produkter, ingen överlappning), så inget väntat tillägg observerades. 9730 och 9739 har redan ` (enligt tillverkaren)` i själva skrivfilen (se fynd 9).

## Urval
| Fil | Produkt-id | Nr | Rättad av granskaren |
|---|---|---|---|
| 09b | 10468721983754 | 9631 | ja |
| 09b | 10472281211146 | 9632 | ja |
| 09b | 10472277836042 | 9626 | nej |
| 09b | 10636736299274 | 9635 | nej |
| 10 | 10636624822538 | 9704 | ja |
| 10 | 10636714901770 | 9726 | ja |
| 10 | 10636605587722 | 9727 | ja |
| 10 | 10636605391114 | 9728 | ja |
| 10 | 10636649431306 | 9729 | ja |
| 10 | 10636649234698 | 9730 | ja |
| 10 | 10636671385866 | 9739 | ja |
| 10 | 10636609421578 | 9746 | ja |
| 11a | 10612578812170 | 9803 | ja |
| 11a | 10523474592010 | 9804 | ja |
| 11a | 10572432736522 | 9806 | ja |
| 11a | 10636733448458 | 9809 | ja |
| 11a | 10636724732170 | 9810 | ja |
| 11a | 10636746817802 | 9811 | ja |
| 11bc | 10636669780234 | 9829 | ja |
| 11bc | 10636730499338 | 9833 | ja |
| 11bc | 10636682658058 | 9838 | ja |
| 11bc | 10636743672074 | 9842 | ja |
| 11bc | 10636602048778 | 9847 | ja |
| 11bc | 10636680429834 | 9848 | ja |
| 11bc | 10636731056394 | 9855 | ja |
| 11d | 10636646809866 | 9876 | ja |
| 11d | 10636723945738 | 9879 | ja |
| 11d | 10636758450442 | 9881 | ja |
| 11d | 10636603064586 | 9882 | ja |
| 11d | 10581102067978 | 9885 | ja |
| 11d | 10581102199050 | 9887 | ja |
| 11efg | 10411494244618 | 9943 | ja |
| 11efg | 10636622725386 | 9947 | ja |
| 11efg | 10472226521354 | 9949 | ja |
| 11efg | 10472247001354 | 9953 | ja |
| 12 | 10581100921098 | 10015 | ja |
| 12 | 10636632621322 | 10024 | ja |
| 12 | 10581106983178 | 10001 | nej |
| 12 | 10581110391050 | 10006 | nej |
| 12 | 10636630622474 | 10020 | nej |
## Språkgranskning (10 texter), fynd per produkt-id

Granskade: 10581102067978, 10636758450442, 10612578812170, 10636630622474, 10636680429834, 10636731056394, 10581106983178, 10411494244618, 10636649234698, 10636733448458.

1. **10581102067978 (9885 Ab Mat Gymstick)**. Grammatik i meta: "...och är gjort av PU och EPE." Ab Mat är en-ord, ska vara "gjord".
2. **10636758450442 (9881 Viktväst med viktpåsar)**. Meningsbyggnad i HTML: "Den finns för 10, 20 och 30 kg, där varje vikt väger 0,5 kg, 1,0 kg respektive 1,5 kg." Oklart att "varje vikt" är en viktpåse, och att västen väger 10/20/30 kg kan läsas som att den är summan av de små vikterna. Samma oklarhet i specifikationsraderna "Varje vikt i 10 kg-västen". Förslag: "varje viktpåse".
3. **10612578812170 (9803 BikeFinder Gen2)**. Meningsbyggnad i HTML: "GPS-tjänsten erbjuds mot en månadsavgift för en månad, 12 månader eller 24 månader." Upprepning av "månad" och otydligt vad som avses. Samma i specifikationsraden "Mot månadsavgift för en månad, 12 månader eller 24 månader". Förslag: "kan tecknas för 1, 12 eller 24 månader mot avgift".
4. **10636630622474 (10020 Viktskivor gummi gjutjärn)**. Meta: första meningen "Viktskivor i gjutjärn med 4 mm gummibeläggning och håldiameter 31 mm." saknar verb (fragment). Verbet kommer först i mening två ("Finns..."). Regeln "meta med verb" uppfylls bara delvis.
5. **10636680429834 (9848 Lifting Hooks)**. Meningsbyggnad: meta blandar plural och singular ("två svarta stålkrokar ... Krokens bredd är 6,8 cm och måtten är 15,8 x 9,5 x 4,8 cm") utan att säga att måtten gäller en krok. HTML: "med kardborrefäste med neoprenvaddering" (dubbelt "med") och "Kroken hakas fast" efter plural. Stilfel, inget faktafel.
6. **10636731056394 (9855 Power Hooks)**. Ordval i HTML: "används för att konvertera hantlar" är en anglicism. Bättre "göra om hantlar så att de kan användas som viktskivor".
7. **10581106983178 (10001 Promenadstavar Go Walker 105 cm)**. Cirkulär/tom information: meta och HTML-ingress är samma mening ("Promenadstavarna ... är avsedda för promenader") och upprepar bara typordet. "har färgen svart och vit" är stelt (bättre "är svarta och vita"). Påståendet "avsedda för promenader" saknar angiven källa i texten, och granskarens skäl hänvisar till Gigantti "kävelysauvat" (stavgång), vilket är en annan användning än promenad.
8. **10411494244618 (9943 Limar Argo)**. Meta är teckenidentisk med första stycket i HTML (duplicerat innehåll, ingen regelöverträdelse bekräftad). "näskudde med högt grepp" är svårbegripligt.
9. **10636649234698 (9730 Gymmattor med mattstativ)**. Format: lastgränsen står som "Stativ, maximal belastning: 20 kg (enligt tillverkaren)", medan övriga produkter använder "Belastning enligt tillverkaren: ...". Inkonsekvent formulering, samma sakuppgift. Samma parentesform finns i 10636671385866 (9739, färg- och motståndsrad).
10. **10636733448458 (9809 Situpskudde Ab Mat GS)**. Stavning: "sit-ups-träning" (tre led, ovanligt) och blandning av "Situpskudde" (titel, typord) och "sit-ups" i brödtext. Förslag "träning av sit-ups", eller konsekvent "situps".

Övriga iakttagelser i hela stickprovet (inte bland de tio):
- Cirkulär inledning (typordet i titeln upprepas som "X är en X"): 10468721983754 (9631 Träningsrulle Elite Roller Arion) och 10472281211146 (9632 Träningsrulle Elite Roller Quick Motion) börjar meta och HTML med "Elite Arion/Quick Motion är en hopfällbar träningsrulle". Mild form (modellnamn + typord), men värd att notera.
- 10523474592010 (9804 Cairn Flake): "är avsedda för sport" står utan "enligt tillverkaren". Källan säger "sport och stil går hand i hand", stödet är svagt.
- Stöds av före-texten, ingen anmärkning: 9635 (benböj med ett ben), 9726 (stretching), 9842 (svingas i mönster), 9881 (neopren/nylon, vikter).
- Inga andra stavfel hittades. Meta-längder 101–145 tecken.
