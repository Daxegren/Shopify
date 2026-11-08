# Granskningsutlåtande k_49t3: tom eller tunn källa, v1.12 (2026-11-08)

Granskaren har bara läst i Shopify. Inget har ändrats där och inget har committats. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient; `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.12), BESLUTSLOGG till och med 2026-11-08, LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md`, `k_utlatande_49t1.md` och `k_utlatande_49t2.md` samt formatet i `k_utlatande_43.json`.

Alla 10 utkast och de 3 avvisade produkterna är ACTIVE och har lager. Ingen har taggen På beställning, och inget utkast har leveranstidsmeningen. Standardblocket är exakt rätt på alla. Efter rättning gäller följande: titeln är högst 54 tecken med högst 1 kommatecken, SEO-titeln högst 42 tecken och metatexten 84–126 tecken med verb. Titel, SEO-titel och metatext krockar inte med andra filer i `vag2_skriv`. De enda träffarna gäller samma produkt i äldre in- och utkastfiler. Butikssökningen gav inga krockar (Acadia, Step, Keo, X-Track, Uniplast, Hammer Premium, Christopeit, Bröstbälte, Cykelstöd, bakre, M-Wave, Pedalblock). Varje rättning är ETT sammanhängande före/efter-par per fält, och före-texten förekommer exakt en gång i utkastet (kontrollerat i python). `skrivfil_kontroll.py` på den rättade versionen ger 0 formatfel och 1 spärrfel: 49205 står på `tidigare-avvisade-2026-11-04`.

Tillverkarkällor: granskaren sökte en tillverkarsida för alla tio produkterna. Look har sidor för exakt modell, och 49208 och 49209 stämmer med dem. Hammer, Christopeit, BH Fitness, Toorx, Peltonen, Uniplast och Messingschlager/M-Wave har ingen sida för exakt artikel eller EAN. Där bygger texterna bara på titeln och den egna källan, vilket v1.12 tillåter.

Löften: alla texter genomsöktes efter hälso-, säkerhets-, skydds-, utvecklings-, prestanda- och kvalitetsord. Inget sådant finns kvar. Rätt utelämnat ur källorna: framgångsrik helkroppsträning, säkert grepp, bekvämt, bålstyrka, kroppsstabilitet, perfekt/idealisk, 'liten i storlek men stor i effekt', tyskt märke/god kvalitet och 'lätt träningspass för amatören'. Kvar står 'ergonomiskt utformat handtag' med 'enligt tillverkaren' (49206). Det står ordagrant i källan och följer det skrivna syskonet. Reflex (49205) anges bara som egenskap. Barnprodukten (49210) har inga säkerhets- eller utvecklingspåståenden.

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_49t3.json`.

## Resultat: 1 GODKÄND, 9 RÄTTA, 0 UNDERKÄND

| nr | id | dom | rättade fält |
|---|---|---|---|
| 49201 | 10472324432138 | RÄTTA | meta |
| 49202 | 10472325349642 | RÄTTA | meta |
| 49203 | 10472346190090 | RÄTTA | titel, seo_title, meta, html |
| 49204 | 10475517772042 | RÄTTA | meta |
| 49205 | 10475980882186 | RÄTTA | meta |
| 49206 | 10480054567178 | RÄTTA | meta |
| 49207 | 10494685315338 | RÄTTA | seo_title, meta, html |
| 49208 | 10494695932170 | RÄTTA | meta |
| 49209 | 10494696161546 | GODKÄND | – |
| 49210 | 10494698881290 | RÄTTA | meta |

## Per produkt

### 49201 (10472324432138): RÄTTA

Live ACTIVE, 0191191, EAN 8431284975340, 719 kr, lager 5, taggen step up. Egen källa bara 'Produkten passar för BH Fitness' (länken pekar på en BH-motionscykel) och 'Tillverkaren är BH Fitness'. Ingen BH-sida eller EAN-träff på nätet; texten bygger bara på titel och egen källa (v1.12). Typordet stepbräda finns i profilen. RÄTTA: metatexten hade utfyllnad ('som även är tillverkare. Se specifikationen för märke och modell.', R12).

- **meta**: före `Stepbrädan Step Board kommer från BH Fitness, som även är tillverkare. Se specifikationen för märke och modell.` → efter `Stepbrädan Step Board tillverkas av BH Fitness och har artikelnummer 0191191 och EAN 8431284975340.`

### 49202 (10472325349642): RÄTTA

Live ACTIVE, två varianter med samma SKU 17367 och EAN 4005251173677 (Default Title 1 879 kr och 17367 1 639 kr): överbliven Default Title enligt v1.7, inget pris i texten. Ingen Hammer-sida för 17367 hittades; sortimentet 4–24 kg står i egen källa och i skrivna syskon (14 och 24 kg). Ingen löftesformulering kvar (framgångsrik, helkroppsträning utelämnade). RÄTTA: metatextens första mening saknade verb.

- **meta**: före `Kettlebell Hammer Premium på 22 kg. Den ingår i ett sortiment kettlebells från 4 till 24 kg.` → efter `Kettlebellen Hammer Premium väger 22 kg och ingår i ett sortiment kettlebells med vikter från 4 till 24 kg.`

### 49203 (10472346190090): RÄTTA

Live ACTIVE, SKU 1007, intern EAN 2099900001178, lager 201, pris 0,00 kr. Källa: 'Passar alla 26-29 tums cyklar.' Ingen tillverkarsida (märket oklart: vendor Azimut, taggen Gymstick). RÄTTA: lastgräns enligt v1.10 saknades. Skrivna cykelstöd (Azimut 1001, 1011) har 'Maximal lastgräns: Ej känd' och en mening om det. Intervallet ska skrivas med tankstreck (26–29). Metatexten saknade huvudverb. Obs: priset 0 kr gäller inte texten men bör ses över.

- **titel**: före `Cykelstöd med bakre fäste för 26-29 tum` → efter `Cykelstöd med bakre fäste för 26–29 tum`
- **seo_title**: före `Cykelstöd med bakre fäste 26-29 tum` → efter `Cykelstöd med bakre fäste 26–29 tum`
- **meta**: före `Cykelstöd med bakre fäste som enligt tillverkaren passar cyklar på 26 till 29 tum.` → efter `Cykelstödet har bakre fäste och passar enligt tillverkaren cyklar på 26–29 tum. Maximal lastgräns är inte känd.`
- **html** (sammanhängande del av fältet): före `<p>Cykelstödet har bakre fäste och passar enligt tillverkaren cyklar på 26 till 29 tum.</p><h2>Passar för</h2><ul>
<li>Dig som söker ett cykelstöd med bakre fäste</li>
<li>Dig som har en cykel på 26 till 29 tum</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Cykelstöd</li>
<li>Fäste: Bakre fäste</li>
<li>Cykelstorlek: 26 till 29 tum</li>
<li>Artikelnummer: 1007</li>` → efter `<p>Cykelstödet har bakre fäste och passar enligt tillverkaren cyklar på 26–29 tum. Maximal lastgräns är inte känd.</p><h2>Passar för</h2><ul>
<li>Dig som söker ett cykelstöd med bakre fäste</li>
<li>Dig som har en cykel på 26–29 tum</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Cykelstöd</li>
<li>Fäste: Bakre fäste</li>
<li>Cykelstorlek: 26–29 tum</li>
<li>Maximal lastgräns: Ej känd</li>
<li>Artikelnummer: 1007</li>`

### 49204 (10475517772042): RÄTTA

Live ACTIVE, FC-TOORX, EAN 8029975970295, lager 3. Källa: 'Tillverkare: Toorx (Italien). Frekvens: 5,3 KHz' och en trasig rad om frekvensomfång. Bara frekvensen används; ursprung och omfång är rätt utelämnade. Ingen Toorx-sida för exakt artikel (bara FC-TOORX-3C, som är en annan modell). RÄTTA: metatexten hade utfyllnad ('Se specifikationen ...').

- **meta**: före `Bröstbältet från Toorx har frekvensen 5,3 kHz. Se specifikationen för märke, frekvens och artikelnummer.` → efter `Bröstbältet från Toorx använder frekvensen 5,3 kHz och har artikelnummer FC-TOORX och EAN 8029975970295.`

### 49205 (10475980882186): RÄTTA

Live ACTIVE, 120967, EAN 887539025205, lager 59. Källa: 'En svart reflekterande benfästeklämma' och märkesreklam (rätt utelämnad). Reflex enligt v1.9: bara fakta, inga synlighetslöften, vilket stämmer. Messingschlager (M-Waves tillverkare) har ingen sida för 120967. RÄTTA: metatexten upprepade 'svart' och hade cirkulär utfyllnad. SPÄRRAD: skrivfil_kontroll.py ger FEL (tidigare-avvisade-2026-11-04) och behöver undantagsrad före skrivning. Typordet benfästeklämma är källans eget ord (R7) men ovanligt; se frågor.

- **meta**: före `Benfästeklämman från M-Wave är svart och reflekterande och passar dig som söker en benfästeklämma i svart.` → efter `Benfästeklämman från M-Wave är svart och reflekterande och har artikelnummer 120967.`

### 49206 (10480054567178): RÄTTA

Live ACTIVE, 21-3567, EAN 5704796035677, lager 2. Ingen Christopeit-sida eller EAN-träff. Utelämnat är rätt: säkert grepp, bålstyrka, kroppsstabilitet, perfekt/idealisk och 'bekvämt'. 'Ergonomiskt utformat' står ordagrant i källan, finns med 'enligt tillverkaren' och följer det skrivna syskonet Kettlebell Christopeit 2 kg. RÄTTA: metatexten saknade verb och hade 'enligt tillverkaren' mitt i en ofullständig mening; den nya metatexten anger bara användningen.

- **meta**: före `Kettlebell från Christopeit på 12 kg med ergonomiskt utformat handtag enligt tillverkaren, för hemma, gym eller utomhus.` → efter `Kettlebellen från Christopeit väger 12 kg och är avsedd för svingar, knäböj och bålövningar hemma, på gym eller utomhus.`

### 49207 (10494685315338): RÄTTA

Live ACTIVE, 21AN821200-S00T193, EAN 6417858571158, lager 4. Källan är trasig och maskinöversatt och rätt utelämnad. Peltonens egen sida hittades inte. Återförsäljare anger Acadia Skate i flex Medium och Stiff. Syskonet Längdskidor Peltonen Acadia SK 21 Medium (skrivet) har 'Styvhet: Medium'. RÄTTA: SEO-titeln måste innehålla Stiff för att skilja den från Medium-syskonet (42 tecken). 'Flex' ändras till 'Styvhet', som syskonet. Metatexten hade utfyllnad och 'finns i utförandet', vilket antydde att flera utföranden säljs.

- **seo_title**: före `Skridskoskidor Peltonen Acadia SK 21` → efter `Skridskoskidor Peltonen Acadia SK 21 Stiff`
- **meta**: före `Skridskoskidorna Peltonen Acadia SK 21 finns i utförandet Stiff, det vill säga styv flex. Se specifikationen för modell och märke.` → efter `Skridskoskidorna Peltonen Acadia SK 21 har styvheten Stiff (styv) och artikelnummer 21AN821200-S00T193.`
- **html** (sammanhängande del av fältet): före `<p>Skridskoskidorna Acadia SK 21 från Peltonen har utförandet Stiff, det vill säga styv flex.</p><h2>Passar för</h2><ul>
<li>Dig som söker skridskoskidor från Peltonen</li>
<li>Dig som vill ha modellen Acadia SK 21 i utförandet Stiff</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Skridskoskidor</li>
<li>Märke: Peltonen</li>
<li>Modell: Acadia SK 21</li>
<li>Flex: Stiff (styv)</li>` → efter `<p>Skridskoskidorna Acadia SK 21 från Peltonen har styvheten Stiff (styv).</p><h2>Passar för</h2><ul>
<li>Dig som söker skridskoskidor från Peltonen</li>
<li>Dig som vill ha modellen Acadia SK 21 i utförandet Stiff</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Skridskoskidor</li>
<li>Märke: Peltonen</li>
<li>Modell: Acadia SK 21</li>
<li>Styvhet: Stiff (styv)</li>`

### 49208 (10494695932170): RÄTTA

Live ACTIVE, SKU och EAN 3611720061577, tom källa, lager 7. Tillverkarkälla kontrollerad: lookcycle.com/bg-en/products/pedals/road/cleats/keo-grip (Keo Grip landsvägsklossar, float 0°/4,5°/9° = svart/grå/röd, 6 skruvar 5 x 9 mm och 6 brickor ingår). EAN-kopplingen kommer från wheelandsprocket (röd, 9°). Texten stämmer och följer syskonet Pedalblock Look Keo Grip, 0 grader. RÄTTA: metatextens första mening saknade verb.

- **meta**: före `Pedalblock Look Keo Grip för racercykel med 9 graders vinkelrörelse. Passar Look Keo-pedaler. Artikelnummer 3611720061577.` → efter `Pedalblocken Look Keo Grip är avsedda för racercykel och har 9 graders vinkelrörelse. De passar Look Keo-pedaler.`

### 49209 (10494696161546): GODKÄND

Live ACTIVE, SKU och EAN 3611720144997, tom källa, lager 3. Tillverkarkälla kontrollerad: lookcycle.com/us-en/products/spare-parts/cleat-x-track ('Compatible with all SPD-standard pedals', 2-screw, 'Disengagement is unidirectional', kompatibla med X-TRACK och GEO TREKKING, 6 skruvar och 6 brickor ingår). Allt i texten stämmer. EAN-kopplingen till standardmodellen (inte X-Track Easy) kommer från wheelandsprocket. Ingen dubblett: de övriga X-Track-produkterna är pedaler.


### 49210 (10494698881290): RÄTTA

Live ACTIVE, SKU och EAN 4743128000014, lager 11. Källa: 'Maximal användarvikt 60 kg.' Ingen Uniplast-sida hittades. Barnprodukt: inga säkerhets- eller utvecklingspåståenden. Att användarvikten utelämnats godtas (utelämnande är tillåtet), men skälet 'utan etikett' är fel. Raden har etikett och enhet, och det skrivna syskonet Skidor Uniplast Mini har 'Maximal användarvikt enligt tillverkaren: 30 kg' (se frågor). RÄTTA: metatexten saknade verb.

- **meta**: före `Skidor från Uniplast i utförandet Junior med bindningar för barn, 56 cm. Artikelnummer 4743128000014.` → efter `Skidorna Uniplast Junior levereras med bindningar och är avsedda för barn. Storleken är 56 cm och artikelnumret 4743128000014.`

## Lastgräns (v1.10) och varianter

Cykelstödet 49203 får 'Maximal lastgräns: Ej känd' och en mening om det, som de skrivna cykelstöden. Kettlebell 49202 har en överbliven Default Title med samma SKU och EAN (v1.7). De övriga produkterna har en variant var. Ingen titel låser en variant som inte finns.

## Dubbletter (R12a)

Ingen produkt är en exakt dubblett. Närliggande produkter har annan SKU: Acadia SK 21 Medium (21AN8211…), Keo Grip 0 grader (…560) och 4,5 grader (…553, DRAFT), Hammer Premium 14/16/24/4 kg (17365/17366/17370/17360), Christopeit 2 och 4 kg, Uniplast Mini 41 cm (…021) samt M-Wave Kickstand A26-29C (430720, DRAFT).

## Avvisade (k_49t3_avvisade.json): alla tre avvisningar står fast

- 49211 Fälgskydd M-Wave Ringlock 29-33: vendor Romet, 6 779 kr, SKU 26150015-D, och källan är bara titeln. Det är en motsägelse.
- 49212 Hantelvikter Toorx Spring Locks 30 mm: taggen säger 31 mm, och källan är tom. Det är en motsägelse.
- 49213 Skyddsplåt Uniplast Apple (Pulkor): källan är tom och EAN ger ingen träff. Produkttypen är oklar.

## Frågor till David

1. 49205 (M-Wave byxklämma, 120967) står på spärrlistan `tidigare-avvisade-2026-11-04`. Ska den få en undantagsrad enligt v1.12? Ska typordet vara Byxklämma i stället för källans maskinöversatta Benfästeklämma? Ordet används inte i butiken i dag, så det kräver beslut enligt R7.
2. 49210: ska 'Maximal användarvikt enligt tillverkaren: 60 kg' läggas till, som på det skrivna syskonet Uniplast Mini (30 kg)? R4 tillåter det, eftersom raden är svensk och har etikett och enhet. Utkastet utelämnar uppgiften, och granskaren har godtagit det.
3. 49203 har priset 0,00 kr och 201 i lager, och märket är oklart (Azimut eller Gymstick). Priset bör ses över. Det är ingen textfråga.
4. 49208/49209: syskonet Keo Grip 0 grader har 'Maximal lastgräns: Ej känd'. Granskaren räknar inte pedalklossar som bärande delar enligt v1.10 och har inte lagt till raden. Vill du ha samma rad på alla pedalklossar?
