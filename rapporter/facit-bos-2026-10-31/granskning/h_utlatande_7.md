# Granskning faktatext h_7 (Toorx/Tunturi: boxningshandskar, boxboll, boxningssäck, boxningsdocka) – BEST OF SPORTS (2026-11-04)

Oberoende granskning, endast läsning. Butiken bekräftad med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK). Underlag: `vag2_skriv/h_7_utkast.json` (5 utkast), `h_7_avvisade.json` (tom). Regelbok v1.3 gäller före `c_granskarprompt.md`.

**Metod:** Alla 5 hämtades live (graphql `nodes`): ACTIVE, productType oförändrad (Konditionsträning & Fitness), en variant var, ingen SEO live. Inget id finns i pilotens 20 (`rapporter/bestofsports-pilot-20-produkter-2026-10-25.csv`) eller i `sparrlista.json`. SEO-titlar jämförda mot live (sökning boxning/boxboll/Boxing/Punch, 40 träffar) och mot alla utkast- och skrivfiler i `vag2_skriv/`: ingen krock. Syskonen 16 oz (10472254603530), Jaguar S/M (10472279572746) och Slam Man (10462758469898) lästa live.

## Resultat
| Dom | Antal | Nr |
|---|---|---|
| GODKÄND | 2 | 10608, 10614 |
| RÄTTA | 3 | 10610, 10611, 10616 |
| UNDERKÄND | 0 | – |

## Särskilda kontroller
- **Lastgräns/fyllning (R4):** 10610 '15 liter vatten eller 15 kg sand' är svensk, ordagrann fyllnadsmängd – står kvar. 10616 '110 kg sand/130 kg vatten' är engelsk, felciterad ('upp till' på båda) och fysiskt udda – stryks.
- **Skydd och effekt (R5):** 'skyddar ... från skador' (10611), 'står stadigt', 'stabil', 'hållbar', 'minskar belastningen på leder' (10614), 'tål de hårdaste slagen' (10616), 'reflexträning' (10610) är borta. Kvar som 'enligt tillverkaren': endast boxningsträning/tumplatta (10608), ingen installation/krokar/kedjor (10614).
- **Typord (R7):** 10608/10611 Boxningshandskar, 10610 Stående boxboll, 10614 Fristående boxningssäck är live-ord. 10616 Boxningsdocka saknas i egen källa och profil men är entydig översättning och butikens live-ord (godtas, se oklarhet).
- **Taggar:** felaktig 'Cykelväska' på 10610 och 10614 rörs inte (beslutslogg 2026-11-03); utkasten ändrar inga taggar.
- **Utanför batchen:** live-meta på 10472254603530 (16 oz, texter-klara) säger 'ger stöd åt handleden' utan 'enligt tillverkaren' (R5) – bör prövas separat.

## Utlåtande per produkt
| Nr | Id | Dom | Fält | Före | Efter | Skäl |
|---|---|---|---|---|---|---|
| 10608 | 10475517804810 | GODKÄND | | | | Fyra entydiga fakta ur egen källa (endast boxningsträning, polyuretan, tumplatta/god rörlighet, L/XL); Italien utelämnat. 'Enligt tillverkaren' en gång i html och en gång i meta, inleder meningen och täcker båda påståendena (R5). Samma text som godkända syskonet S/M (10607). SEO skiljer sig från S/M. |
| 10610 | 10472299954442 | RÄTTA | html | `med justerbar höjd, 120 eller 160 cm.` | `med justerbar höjd på 120/160 cm.` | Källan anger '120/160 cm' (även i 'Mått: 48 x 120/160 cm'); det kan vara två lägen eller ett intervall, så '120 eller 160' är en tolkning (R2). Övrigt stämmer: 'Bolltstorlek' → 'Bollens storlek' är entydigt (R2 entydig del), 15 L vatten/15 kg sand är basens fyllnadsmängd ordagrant på svenska, inte en lastgräns (R4). Reflexträning borta (R5). Taggen Cykelväska rörs inte. |
| 10611 | 10472268824842 | RÄTTA | meta | `Tunturi Allround Boxing Gloves är universella` | `Tunturi Allround är universella` | R11: 'Allround Boxing Gloves är universella boxningshandskar' är cirkulärt engelskt; syskonet 16 oz skriver 'Tunturi Allround är'. Fakta (universella, syntetiskt läder, mjuk stoppning, bred kardborre, 12 oz ur titeln, en variant) stämmer. Handledsstöd utelämnat är tillåtet (utelämna är alltid säkert, R5); syskonet har det och stödpåståendet kunde stå som 'enligt tillverkaren' (jfr 10606 Hammer i h_6) – beslut för enhetlighet, inget fel. Skyddar mot skador borta. |
| 10611 | 10472268824842 | RÄTTA | html | `<p>Tunturi Allround Boxing Gloves är universella` | `<p>Tunturi Allround är universella` | Se raden ovan. |
| 10614 | 10650165772554 | GODKÄND | | | | Typordet Fristående boxningssäck är live-ordet (R7). 180 cm och 18 kg ur källans lista; titeltillägget 180 cm har stöd. 'Enligt tillverkaren' en gång (ingen installation/krokar/kedjor, kan flyttas). PU-skum på slagytan och vatten/sand/grus ordagrant. Dämpar energi, avlastar leder, står stadigt, stabil, hållbar, intensiv användning, effektiv träning borta (R5). SEO skiljer sig från live 'Boxningssäck Tunturi Fristående' (10472259813642). Taggen Cykelväska rörs inte. |
| 10616 | 10472302575882 | RÄTTA | html | `<li>Fyllning: Upp till 110 kg sand eller 130 kg vatten</li>` | `<li>Fyllning: Sand eller vatten</li>` | Fyllvolymen stryks: källan är engelsk, säger '110kg of sand or up to 130kg of water' (utkastet flyttar 'upp till' till båda), siffrorna är fysiskt udda (sand är tätare än vatten i samma bas) och står i en stabilitetsmening ('maximum stability'); vid tvivel stryk (R2/R4). Typordet Boxningsdocka godtas: entydig översättning av källans 'boxing dummy' och butikens eget live-ord (Slam Man), men det står inte i godkanda_typord – se oklarhet. Mått, tre höjder upp till 185 cm, 18 kg stämmer. Tål hårda slag/sparringpartner borta (R5). Leveranstidsmeningen finns (tagg På beställning). |

## Oklart i regelboken
1. R7: får en entydig översättning av en engelsk källas typord ('boxing dummy' → boxningsdocka) användas när ordet inte står i `godkanda_typord`? Förslag: lägg till 'boxningsdocka' i profilen (M).
2. R4/R5: fyllnadsmängd i en bas (sand/vatten i kg) är varken lastgräns eller ordagrant undantagen; skilj på fyllnadsmängd (får stå om svensk och ordagrann) och lastgräns.
3. R5: 'en gång per påstående' – räcker en inledande 'Enligt tillverkaren' för två påståenden i samma mening (10608)? Räknas meta och html som samma text?
4. R5: stödpåståenden ('stöd åt handleden') nämns inte uttryckligen; utkastare har behandlat dem olika (10606 kvar, 10611 utelämnat, 16 oz utan 'enligt tillverkaren').
