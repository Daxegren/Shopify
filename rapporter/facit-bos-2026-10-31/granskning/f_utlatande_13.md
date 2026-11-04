# Granskning faktatext f_13 (Tunturi-, Hammer- och Toorx-hantlar och kettlebells) – BEST OF SPORTS (2026-11-04)

Oberoende granskning, endast läsning. Butiken bekräftad med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK).

**Underlag:** `vag2_skriv/f_13_utkast.json` (18 poster, nr 10301–10325), `f_13_avvisade.json` (7). FAKTATEXTLÄGE (§14–17, `fakta_utkastprompt.md`); meta 70–155 (§17); standardblocket jämfört med `b_skriv_24.json`.

**Metod:** alla 25 hämtade live (graphql `nodes`), alla ACTIVE, produkttyper oförändrade, alla 18 utkast har en variant (Default Title). Maskinellt: titlar 32–59 tecken (högst 2 komman utöver decimalkomman), SEO 32–43, meta 118–152, inga dubbletter inom batchen eller mot övriga `*_utkast.json`/`*skriv*.json`, inga osynliga tecken. Standardblocket identiskt med `b_skriv_24.json`; beställningsmeningen finns exakt på de fyra med taggen 'På beställning' (10304, 10306, 10313, 10315) och saknas på övriga 14. `format_regler.py`: inga fel (kolon och titelversaler). Vikt kontrollerad i titel, SEO, meta, text och specifikation mot källan och enheten (per hantel, par, set); serier kontrollerade mot SKU och pris (Hammer 1736x, Toorx KCAE/KPCE). Inget läckt från syskonprodukter; inga säkerhets-, hälso-, träningseffekt- eller belastningspåståenden.

## Resultat
| Dom | Antal | Nr |
|---|---|---|
| GODKÄND | 9 | 10305, 10306, 10309, 10310, 10314, 10315, 10318, 10324, 10325 |
| RÄTTA | 9 | 10301, 10302, 10303, 10304, 10308, 10312, 10313, 10319, 10320 |
| UNDERKÄND | 7 | 10307, 10311, 10316, 10317, 10321, 10322, 10323 |

## De särskilda kontrollerna
- **Vikten:** samma tal och enhet i alla fält på samtliga 16 med vikt. Per hantel: 10303, 10309–10315 ('Setet innehåller en hantel'); par: 10306, 10308 ('2 hantlar som väger … var'); set: 10302, 10304 (par per vikt; 132 kg = summan av tio par), 10318 (totalvikt). Kettlebells en per produkt.
- **Utelämnade vikter 10301 och 10305:** rätt. 10301 har bara en trasig källrad ('… x 1,3 kg (2 x 3 kg)'), 10305 bara '1.0kg' i namnet utan antal. Se fråga 1.
- **Utelämnade luckor:** rätt på alla: MX30 steg 1,12 kg, MX85/MX55 räfflad längder i 'kg' och 3,6 kg-intervallet, 10302 PVC/neopren, 10318 Ø 25 mm (taggen säger 30 mm), 10325 material (bara tagg).
- **SEO MX85 utan 'Select':** godtas (MX85 är modellen, Tunturi ryms inte). Däremot har 10301, 10308 och 10312 tappat märket fast det ryms – rättas.
- **Toorx 10324:** handlen '…-kcae-20' mot SKU KCAE-18 och titeln 18 kg. Alla Olympic EVO-handlar är förskjutna två steg (16 kg …-kcae-18, 20 kg …-kcae-22, och 12 kg-produkten har SKU KCAE-14); titel, SKU och prisordning stöder 18 kg. Godkänd.
- **Format:** inga kolon- eller versalfel denna gång. **Typord:** 'Hantelset' för flera par (som f_12) i 10302 och 10304; upprepat typord i 10308; engelska 'Dumbbell' i 10303 mot syskonet 10293. **Utfyllnad:** 'Finns hos BEST OF SPORTS.' på metor över 70 tecken (10303, 10319, 10320) tas bort. Inga cirkulära inledningar som säger noll.

## Per produkt
| Nr | Id | Dom | Skäl / före → efter |
|---|---|---|---|
| 10301 | 10462774231306 | RÄTTA | Vikten utelämnad med rätta: källraden '9,1 x 9,1 x 9,1 x 1,3 kg (2 x 3 kg)' är trasig och antalet framgår inte. Mått, material, färg och 'lätt textur' (enligt tillverkaren) ordagrant. SEO-titeln har tappat märket fast det ryms.<br>seo_title: `Hantlar Neoprene Dumbbells, Lila` → `Hantlar Tunturi Neoprene Dumbbells, Lila` |
| 10302 | 10475374248202 | RÄTTA | 3 par (2 x 1, 2 x 2, 2 x 3 kg), 12,3 kg inkl. ställ, ställmått och gjutjärn ordagrant; PVC/neopren rätt utelämnade (motsägande). Typord: flera par heter 'Hantelset' i batchen och i f_12 (jfr 10296).<br>titel: `Hantlar Tunturi Neoprenhantlar, 3 Par med Ställ` → `Hantelset Tunturi Neoprenhantlar med Ställ, 3 Par`<br>seo_title: `Hantlar Neoprenhantlar, 3 Par med Ställ` → `Hantelset Neoprenhantlar med Ställ, 3 Par` |
| 10303 | 10471350665482 | RÄTTA | En hantel, 6 kg, gummiöverdrag ordagrant; golvskydd som 'enligt tillverkaren'. Titeln ska följa syskonet 10293 ('Hantel Tunturi Platinum Hex Rubber, 10 kg') utan engelska 'Dumbbell'. 'Finns hos BEST OF SPORTS.' är utfyllnad när metan redan är över 70 tecken (§14).<br>titel: `Hantel Tunturi Platinum Hex Rubber Dumbbell, 6 kg` → `Hantel Tunturi Platinum Hex Rubber, 6 kg`<br>seo_title: `Hantel Platinum Hex Rubber Dumbbell 6 kg` → `Hantel Tunturi Platinum Hex Rubber 6 kg`<br>meta: `Tunturi Platinum Hex Rubber Dumbbell är en hantel med gummiöverdrag. Setet innehåller en hantel som väger 6 kg. Finns hos BEST OF SPORTS.` → `Tunturi Platinum Hex Rubber Dumbbell är en hantel med gummiöverdrag. Setet innehåller en hantel som väger 6 kg.` |
| 10304 | 10472283996426 | RÄTTA | 10 par, vikterna, 132 kg (= ett par per vikt), svart/krom, polyuretan ordagrant; systerprodukter, Fitkids och träningspåståenden borta. Beställningsmening rätt. Typord 'Hantelset' för flera par (jfr 10297).<br>titel: `Hantlar Tunturi PU Pro, 10 Par, 2–12 kg` → `Hantelset Tunturi PU Pro, 10 Par, 2–12 kg`<br>seo_title: `Hantlar Tunturi PU Pro, 10 Par, 2–12 kg` → `Hantelset Tunturi PU Pro, 10 Par, 2–12 kg` |
| 10305 | 10462778753290 | GODKÄND | Vikt och antal utelämnade med rätta (1.0kg bara i namnet, oklart per hantel eller par). Plastbelagda och aerobics/träning hemma som 'enligt tillverkaren'. Tunn källa, kort meta godtas (§17). |
| 10306 | 10472290091274 | GODKÄND | 2 hantlar à 5 kg, gummibeläggning på ovansidan, vinklad form, lätt att rengöra (enligt tillverkaren) ordagrant; ljud-, skydds- och muskelpåståenden borta. Beställningsmening rätt. |
| 10307 | 10462794776842 | UNDERKÄND | Avvisningen bekräftas live: tre varianter Red/blue/green (14TUSFU111/112/110) med olika pris (339/449/249 kr); titelns röd 3.0 kg gäller bara en. |
| 10308 | 10462778917130 | RÄTTA | 2 x 0,5 kg, gummilager, vinklad form ordagrant. Titeln upprepar typordet ('Hantlar … Vinylhantlar'); SEO-titeln saknar märket.<br>titel: `Hantlar Tunturi Vinylhantlar 2 x 0,5 kg, Rosa` → `Hantlar Tunturi Vinyl 2 x 0,5 kg, Rosa`<br>seo_title: `Hantlar Vinylhantlar 2 x 0,5 kg, Rosa` → `Hantlar Tunturi Vinyl 2 x 0,5 kg, Rosa` |
| 10309 | 10472281145610 | GODKÄND | Intervall, en hantel, längder i cm, grepp 3,27 cm och stål ordagrant. Stegen 1,12 kg rätt utelämnade (går inte jämnt upp). Säkerhets- och låspåståenden borta. |
| 10310 | 10472295661834 | GODKÄND | 10 viktlägen ordagrant, en hantel, 3,27 cm, stål/härdat stål. Längder angivna i 'kg' och '3,6 kg intervall' rätt utelämnade. SEO utan 'Select' godtas: MX85 identifierar modellen och Tunturi ryms inte inom 43. |
| 10311 | 10471139213578 | UNDERKÄND | Avvisningen bekräftas live: titeln 12,8–45,5 kg och 'Justerbar hantel', texten 12,7–45,3 kg och ett skivstångsset med rak och EZ-stång och bas; två motsägande längdrader (högsta/tyngsta vikt 141,3/110,5 cm). |
| 10312 | 10472505934090 | RÄTTA | Intervall, steg 2,25 kg, en hantel, längder i cm, grepp ordagrant. SEO-titeln har tappat märket fast titeln (41) ryms.<br>seo_title: `Justerbar Hantel MX55 4,5–24,9 kg` → `Justerbar Hantel Tunturi MX55 4,5–24,9 kg` |
| 10313 | 10472296775946 | RÄTTA | 10 viktlägen, 2,25 kg, en hantel, härdat stål ordagrant; kg-längder rätt utelämnade; beställningsmening rätt. 'Räfflad' skrivs som modellnamn med versal i löptext; skriv som egenskap som i 10310.<br>meta: `Tunturi MX55 Räfflad är en justerbar hantel av stål med viktintervallet 4,5–24,9 kg. En hantel ingår och handtaget är av härdat stål.` → `Tunturi MX55 är en räfflad, justerbar hantel av stål med viktintervallet 4,5–24,9 kg. En hantel ingår och handtaget är av härdat stål.`<br>html: `<p>Tunturi MX55 Räfflad är en justerbar hantel med` → `<p>Tunturi MX55 är en räfflad, justerbar hantel med` |
| 10314 | 10472249065738 | GODKÄND | 12,5 kg, handtag 2,5 kg, 1,25 kg/styck, mått och röd knapp/bas ordagrant; basen påstås inte ingå. |
| 10315 | 10472349237514 | GODKÄND | 25 kg, tio viktlägen 2,5–25 kg, mått ordagrant; beställningsmening rätt. |
| 10316 | 10472298086666 | UNDERKÄND | Avvisningen bekräftas live: titeln säger hantlar, texten Rapid skivstång eller kettlebell; lastbärande fästdel med träningsbelastningspåstående. |
| 10317 | 10472289861898 | UNDERKÄND | Avvisningen bekräftas live: två varianter 14TUSCL454/455 (639/1 479 kr) med oförklarade namn; '4 viktplattor på 1,5 kg med 1,5 kg kapacitet', 'Mått: 114 x 114 cm - 114,5 cm', delarna summerar inte till 20 kg. |
| 10318 | 10472260075786 | GODKÄND | 16 skivor (6 x 5, 4 x 2,5, 6 x 1,25 kg), 149,5 cm, två 45 cm, 6 klämmor, 50 kg, svart vinyl ordagrant; Ø 25 mm mot taggen 30 mm rätt utelämnad; golv- och snabbytespåståenden borta; 'kan kompletteras' enligt tillverkaren utan lastuppgift. |
| 10319 | 10650169475338 | RÄTTA | 14 kg i namnet, en variant, SKU 17365 i serien (17366 = 16 kg) och priset stämmer. 'Finns hos BEST OF SPORTS.' är utfyllnad över 70 tecken; 'dessa kettlebells' i en enstaka produkt skrivs 'modellen' (som 10277).<br>meta: `Hammer Premium är en kettlebell på 14 kg. Enligt tillverkaren finns dessa kettlebells i vikter från 4 till 24 kg. Finns hos BEST OF SPORTS.` → `Hammer Premium är en kettlebell på 14 kg. Enligt tillverkaren finns modellen i vikter från 4 till 24 kg.`<br>html: `Enligt tillverkaren finns dessa kettlebells i vikter från 4 till 24 kg.</p>` → `Enligt tillverkaren finns modellen i vikter från 4 till 24 kg.</p>` |
| 10320 | 10650210435338 | RÄTTA | Som 10319 med 24 kg (SKU 17370).<br>meta: `Hammer Premium är en kettlebell på 24 kg. Enligt tillverkaren finns dessa kettlebells i vikter från 4 till 24 kg. Finns hos BEST OF SPORTS.` → `Hammer Premium är en kettlebell på 24 kg. Enligt tillverkaren finns modellen i vikter från 4 till 24 kg.`<br>html: `Enligt tillverkaren finns dessa kettlebells i vikter från 4 till 24 kg.</p>` → `Enligt tillverkaren finns modellen i vikter från 4 till 24 kg.</p>` |
| 10321 | 10650210468106 | UNDERKÄND | Avvisningen bekräftas live: varianterna 17360 (409 kr) och 17368 (1 949 kr); 17368 är inte 4 kg. |
| 10322 | 10472325349642 | UNDERKÄND | Avvisningen bekräftas live: två varianter med samma SKU 17367 (1 879/1 639 kr), handle …17369; vikten går inte att låsa. |
| 10323 | 10411923276042 | UNDERKÄND | Avvisningen bekräftas live: tre varianter AKCA-10/12/14 (779/1 609/1 789 kr); titelns 12 kg gäller bara en. |
| 10324 | 10472328757514 | GODKÄND | 18 kg och lila i titeln, SKU KCAE-18 och pris (1 979 kr mellan 16 kg 1 869 och 20 kg 2 099) stöder 18 kg. Handlen '…-kcae-20' avviker men alla Olympic EVO-handlar ligger två steg fel (16 kg …-kcae-18, 20 kg …-kcae-22) och nämns inte. Material ('högkvalitativa') rätt utelämnat. |
| 10325 | 10472299462922 | GODKÄND | 12 kg, SKU KPCE-12 och handle stämmer; material rätt utelämnat (bara taggen 'Kettlebell Järn'). |

## Öppna frågor till David
1. **10301 och 10305 utan vikt:** får titelns vikt (3 kg resp. 1 kg) återges som i originalnamnet, eller ska leverantören bekräfta vikt och antal (per hantel eller par) först?
2. **MX30 (10309):** källans steg 1,12 kg går inte jämnt upp – bekräfta om steget ska stå (MX55 behåller 2,25 kg som står i källan och stämmer med viktlägena).
3. **Variantprodukterna 10307, 10317, 10321, 10322, 10323:** behöver delas upp per vikt/färg i butiken eller få förklarade variantnamn innan de kan skrivas. 10311 och 10316 behöver ny källa.
4. **Toorx Olympic EVO:** handlar och SKU är förskjutna i hela serien (12 kg-produkten har SKU KCAE-14) – värt att kontrollera i leverantörsdatan.
