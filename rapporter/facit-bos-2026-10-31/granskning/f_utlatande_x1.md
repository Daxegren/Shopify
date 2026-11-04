# Granskning f_x1 (motionscyklar och löpband efter Davids beslut alt A, faktatextläge) – BEST OF SPORTS (2026-11-04)

Oberoende granskning, bara läsning. Butiken bekräftad med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK). Underlag: `vag2_skriv/f_x1_utkast.json` (7 utkast: 10085, 10087, 10093, 10094, 10100 från f_4 och 10034, 10044 från f_2; `f_x1_avvisade.json` är tom). Regler: standarden §1–17 (faktatextläge §14–17 och `fakta_utkastprompt.md` har företräde), LARDOMAR.md, meta 70–155 tecken (§17), standardblocket enligt `b_skriv_24.json`. Davids beslut alt A (2026-11-04): maxvikt/användarvikt/driftsvikt utelämnas helt när den engelska källan bara anger "Maximum operating weight".

**Metod:** alla 7 hämtade live (graphql `nodes`): alla ACTIVE, en variant var (Default Title), SEO tom. Varje titel, SEO-titel, meta och html lästes mot den egna produktens live-text; tidigare skäl i `f_utlatande_2.md` och `f_utlatande_4.md` jämfördes. Maskinellt: längder, kommatecken, sökning efter max/användarvikt/driftsvikt/load/nivå/rehab/äldre/säker/stabil/belastning, gemen efter kolon, osynliga tecken, unikhet mot alla övriga `*_utkast*.json`/`*_skriv*.json`, standardblocket.

## Resultat
| Dom | Antal | Nr |
|---|---|---|
| GODKÄND | 4 | 10085, 10093, 10100, 10034 |
| RÄTTA | 3 | 10087, 10094, 10044 |
| UNDERKÄND | 0 | – |

## Särskilt kontrollerat
- **Maxvikt (alt A):** ingen text innehåller max-, användar- eller driftsvikt. Enda "max" är motoreffekten "2,75 hk (max 5,5 hk)" på 10034, som står så i källan.
- **Load range/capacity, nivåer:** finns inte i någon text. "Lutning: 12" på 10034 står utan "nivåer", som i rättningarna i f_2. "Gymnivå" på 10085 betyder "gym-level", inte nivåer.
- **Tolkningar och översättningar:** inga tolkade värden. Typorden (spinningcykel, motionscykel, liggande motionscykel, löpband) och raderna i specifikationen är raka översättningar av källans egna rader. Tillverkarpåståenden (gymnivå på 10085, svänghjul på 10093, Kinomap/Zwift på 10034) står med "enligt tillverkaren".
- **Rehab, äldre och säkerhet:** borta från 10044 och 10100, och komfort och säkerhet är borta från 10034.
- **Live-titlar:** "NorsK" (10034, 10094) och "Walking Pad" (10044) stämmer exakt med live-titlarna.
- **Format:** titlar och SEO-titlar 29–38 tecken, inga kommatecken, och ingen gemen efter kolon. Meta 111–129 tecken efter rättning (kort meta enligt §17, ingen utfyllnad). Titel, SEO-titel och meta krockar bara med de tidigare underkända utkasten av samma id i f_2/f_4, inte med andra produkter. Inga osynliga tecken.
- **Standardblocket:** identiskt i alla 7. Det är `b_skriv_24.json` plus beställningsmeningen, i exakt samma form som i tidigare skrivfiler. Alla 7 har taggen "På beställning" live.
- **Syskonläckage:** inget. Duke och Duke Magnetic, och Spheris 4.0 och NorsK, jämfördes rad för rad.

## Per produkt
| Nr | Id | Dom | Före → efter / skäl |
|---|---|---|---|
| 10085 | 10468768284938 | GODKÄND | Stämmer mot live (104 x 63 x 117 cm, 53 kg, SKU H920). Maxvikt (Maximum operating weight 115 kg) utelämnad enligt alt A; motsägande bromssystem (friction/hydraulic) utelämnat. 'Gymnivå … hemmabruk' är källans egen text och står som 'enligt tillverkaren'. Kort meta (111 tecken) enligt §14/§17; suffixet har godtagits tidigare (10032). |
| 10087 | 10472323383562 | RÄTTA | Stämmer mot live (LCD, PMS manual, 104 x 64 x 123 cm, 53 kg). Maxvikt och 'Load capacity 20 kg' utelämnade; Duke-texten om gymnivå rätt utelämnad. Grammatik: 'Mått är' → 'Måtten är', och 'bromssystemet PMS, manuellt' skrivs som i rättningen av 10089 i f_4.<br>**meta**: `med LCD-skärm och bromssystemet PMS, manuellt.` → `med LCD-skärm och bromssystem av typen PMS, manuellt.`<br>**html**: `med LCD-skärm och bromssystemet PMS, manuellt. Mått är 104 x 64 x 123 cm` → `med LCD-skärm och bromssystem av typen PMS, manuellt. Måtten är 104 x 64 x 123 cm` |
| 10093 | 10472325513482 | GODKÄND | Stämmer mot live (10 tum pekkänslig, 17 program, EMS induktion, 116 x 60 x 139 cm, 50 kg). Svänghjulet 10 kg står i källans brödtext ('10 kg flywheel'). 'Load range 40' och 'Load capacity' tolkas inte; maxvikt utelämnad enligt alt A. Titelns namn Spheris används (källtexten: Sphere). Not: handle slutar 10015 men SKU är 10014 (10094 har SKU 10015). |
| 10094 | 10471334084874 | RÄTTA | Stämmer mot live; 'NorsK' står exakt som i live-titeln. 'Difficulty levels 40', 'Load capacity' och trämarknadsföring utelämnade; maxvikt utelämnad enligt alt A. Grammatik: 'Mått är' → 'Måtten är', 'bromssystemet EMS, induktion' → 'bromssystem av typen EMS, induktion' (samma form som 10087).<br>**meta**: `med 10-tums pekskärm och bromssystemet EMS, induktion.` → `med 10-tums pekskärm och bromssystem av typen EMS, induktion.`<br>**html**: `med 10-tums pekskärm och bromssystemet EMS, induktion. Mått är 116 x 60 x 139 cm` → `med 10-tums pekskärm och bromssystem av typen EMS, induktion. Måtten är 116 x 60 x 139 cm`<br>**html**: `<li>Dig som vill ha en motionscykel med bromssystemet EMS, induktion</li>` → `<li>Dig som vill ha en motionscykel med bromssystem av typen EMS, induktion</li>` |
| 10100 | 10472324595978 | GODKÄND | Stämmer mot specifikationen live (10 tum pekkänslig, 17 program, EMS induktion, 159 x 74 x 121 cm, 77 kg). Den maskinöversatta brödtexten (rehabilitering, ledvänlig, 'backpack pedal trance') och '10 workout levels'/'Load capacity 14 kg' används inte; maxvikt utelämnad enligt alt A. Underkännandet i f_4 byggde på maxvikten; utan den kan produkten skrivas säkert. |
| 10034 | 10472334262538 | GODKÄND | Stämmer mot live (LED/LCD, 2,75 hk (max 5,5 hk), 1–24 km/h, lutning 12 utan 'nivåer', 152 x 50 cm, 181 x 83 x 130 / 124 x 83 x 154 cm, 82 kg, 95 % monterad, Kinomap/Zwift med 'enligt tillverkaren'). 'NorsK' stämmer med live-titeln. Komfort/säkerhet/Pro Solid och maxvikt utelämnade. Beställningsmeningen: taggen 'På beställning' finns (källtexten saknar ⏳-raden). |
| 10044 | 10472300118282 | RÄTTA | Stämmer mot live; 'Walking Pad' står i live-titeln och produkttypen är oförändrad. Rehabilitering, äldre, återhämtning, grepp och säker design är borta; maxvikt utelämnad enligt alt A. Genus: walking pad används som utrum i svenska ('en walking pad').<br>**meta**: `är ett walking pad med` → `är en walking pad med`<br>**html**: `är ett walking pad med` → `är en walking pad med`<br>**html**: `<li>Dig som vill ha ett walking pad med hastighet` → `<li>Dig som vill ha en walking pad med hastighet`<br>**html**: `<li>Dig som vill ha ett walking pad med 12` → `<li>Dig som vill ha en walking pad med 12` |

## Öppna frågor till David
1. "Walking Pad" står kvar som typord på 10044, eftersom det följer live-titeln. På 10037 (f_2) byttes samma typord till "Löpband (walking pad)". En regel bör gälla för båda.
2. 10093 och 10094: handle för 10093 slutar på 10015, men SKU är 10014. 10094 har SKU 10015. Inget fel i texten, men kontrollera att produkterna inte är förväxlade i butiken.
