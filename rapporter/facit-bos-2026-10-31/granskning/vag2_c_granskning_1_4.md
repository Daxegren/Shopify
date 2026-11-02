# Granskning våg 2, utkast c_1–c_4 – BEST OF SPORTS (2026-11-02)

Oberoende granskning. Jag har bara läst i Shopify och inte ändrat någon utkastsfil. Butiken kontrollerades först med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK).

**Underlag:** `vag2_skriv/c_1_utkast.json` (14), `c_2` (13), `c_3` (8), `c_4` (10), totalt 45 utkast, nr 3001–3060. Därtill 15 avvisade (`c_N_avvisade.json`). Standarden (avsnitt 1–11), `LARDOMAR.md` och formatet i `vag2_a_granskning_2.md`.

**Metod:**
- **Källan live:** title, status, productType, vendor, tags, descriptionHtml, seo och variants hämtades med graphql_query (`nodes`) i sju batchar. Alla 45 är ACTIVE och har tom SEO i dag. Fältet `fakta` stämmer med live-källan. Produkttyp är tom på nästan alla (utom 3001 Träningsbollar och 3002–3005 Konditionsträning & Fitness); utkasten rör inte produkttypen. Ingen av de 45 står i `handhavd_ids.txt`.
- **Maskinellt (skript i bash):** längder, kommatecken, standardblocket jämfört med c_1 nr 3001 (alla 45 identiska, utan fraktavgift i kronor), att varje tal i titel, SEO, meta och html (utom standardblocket) finns i `fakta` (0 avvikelser), dubbletter av titel och SEO-titel i alla c_*_utkast.json.
- **För hand:** varje titel, SEO-titel, meta och html lästes mot live-källan och språkgranskades. `kontrollera_produkttext.py` kördes inte i den här granskningen.

## Resultat i korthet

| Kategori | Antal | Nr |
|---|---|---|
| GODKÄND | 19 | 3006, 3007, 3011, 3014, 3017, 3018, 3019, 3021, 3023, 3024, 3026, 3027, 3028, 3030, 3031, 3038, 3039, 3057, 3060 |
| RÄTTA | 16 | 3001, 3004, 3005, 3008, 3010, 3012, 3013, 3015, 3016, 3020, 3025, 3040, 3041, 3055, 3056, 3059 |
| UNDERKÄND | 10 | 3002, 3009, 3034, 3036, 3037, 3047, 3048, 3049, 3051, 3052 |

Totalt 19 + 16 + 10 = 45.

## Regelkontroll
- Titlar 15–54 tecken, högst 2 kommatecken. SEO-titlar 20–42 tecken (≤43). Meta 134–155 tecken där den finns, annars null (tunn källa).
- Enheter med gemener (cm, kg, g, m), tankstreck i 5–8 och 164–180. Stor bokstav efter kolon i specifikationerna.
- Inga priser, omdömen, ursprung eller märkestexter. Hälso-, rehabiliterings- och skadepåståenden har genomgående utelämnats. Varianter med olika pris (3019, 3026, 3041) eller oförklarade namn (3020, 3052, 3055) låses inte.
- **Dubbletter:** titeln på 3008 är identisk med 3057. SEO-titlarna på 3001, 3004 och 3005 är identiska med c_6 nr 3087, c_10 nr 3148 och c_10 nr 3142. Rättningarna nedan löser det från c_1-sidan.
- **Cirkulär engelska i titeln** (som 2209 i våg 2a): 3020, 3055, 3056, 3059.

## Per produkt

| Nr | Id | Dom | Fält | Före | Efter / skäl |
|---|---|---|---|---|---|
| 3001 | 10411728240906 | RÄTTA | seo_title | Träningsboll Gymstick, 65 cm | Träningsboll Gymstick med Pump, 65 cm |
| 3001 | | | skäl | | SEO-titeln är identisk med c_6 nr 3087 (en annan Gymstick-boll). Maxbelastning 120 kg står entydigt i källan; om den ska stå kvar avgör David (öppen fråga). |
| 3002 | 10472257913098 | UNDERKÄND | – | – | Oklar produkttyp: taggen 'hantelstång' och '30 mm' i originaltiteln tyder på en hantelstång för viktskivor (last och lås), inte en fast hantel. Tunn källa (bara titeln). |
| 3004 | 10472282456330 | RÄTTA | seo_title | Medicinboll Gymstick med Handtag | Medicinboll Gymstick med Handtag, 4 kg |
| 3004 | | | skäl | | SEO-titeln är identisk med c_10 nr 3148 (10 kg-bollen). Ny SEO-titel = titeln (lagras tom). |
| 3005 | 10472282489098 | RÄTTA | seo_title | Hopprep Gymstick i Läder | Hopprep Gymstick i Läder, 2,75 m |
| 3005 | | | skäl | | SEO-titeln är identisk med c_10 nr 3142 (Leather Jump Rope). Ny SEO-titel = titeln (lagras tom). |
| 3006 | 10581095743754 | GODKÄND | – | – | Allt spårbart. Varianten 'BB' oförklarad men bara en variant. |
| 3007 | 10581095809290 | GODKÄND | – | – | Allt spårbart; löften om resultat utelämnade. |
| 3008 | 10581095842058 | RÄTTA | titel | Ankel- och Handledsvikter Gymstick, 2 x 1 kg | Ankel- och Handledsvikter Gymstick Aktiv, 2 x 1 kg |
| 3008 | 10581095842058 | RÄTTA | seo_title | Ankel- och Handledsvikter Gymstick | Ankel- och Handledsvikter Aktiv, 2 x 1 kg |
| 3008 | 10581095842058 | RÄTTA | meta | Gymstick ankel- och handledsvikter är ett par på 2 x 1 kg. Enligt tillverkaren ger de extra motstånd vid löpning, promenader och yoga och sitter på plats. | Gymstick Aktiv är två ankel- och handledsvikter på 1 kg vardera. Enligt tillverkaren ger de extra motstånd vid löpning, promenader och yoga. |
| 3008 | 10581095842058 | RÄTTA | html | <p>Gymsticks ankel- och handledsvikter, 2 x 1 kg. Varje vikt väger 1 kg.</p> | <p>Gymstick Aktiv är två ankel- och handledsvikter på 1 kg vardera.</p> |
| 3008 | | | skäl | | Titeln är identisk med c_4 nr 3057 (annan produkt, SKU 61023). 'Aktiv' från originaltiteln ('Aktiva ankel- och handledsvikter') skiljer dem åt. Meta har 'och yoga och sitter på plats' (dubbelt och); 'par' står inte i källan. Introt upprepar vikten. |
| 3009 | 10581095907594 | UNDERKÄND | – | – | Oklar produkttyp: 'tunnrulle' förklaras inte (skumrulle? massagerulle?), och källan består nästan bara av hälso- och skadepåståenden. Utkastaren flaggar själv typen. Kan släppas om David bekräftar typen. |
| 3010 | 10581095940362 | RÄTTA | meta | Gymstick Active Exercise Ball är en träningsboll på 65 cm. Enligt tillverkaren passar den för övningar för kärnstyrka, balans och stretching. | Gymstick Active Exercise Ball är en träningsboll på 65 cm. Enligt tillverkaren passar den för övningar inom kärnstyrka, balans och stretching. |
| 3010 | | | skäl | | 'passar den för övningar för kärnstyrka' (för två gånger). |
| 3011 | 10581095973130 | GODKÄND | – | – | Diameter 75 cm står i källan. Rehabilitering utelämnad. |
| 3012 | 10581096005898 | RÄTTA | meta | Gymstick Active Finger Expander Set innehåller två fingerexpandrar. Enligt tillverkaren är de lätta att använda och transportera, för händer och fingrar. | Gymstick Active Finger Expander Set är två fingerexpandrar för händer och fingrar. Enligt tillverkaren är de lätta att använda och transportera. |
| 3012 | | | skäl | | Metan slutar med det lösa tillägget ', för händer och fingrar.' |
| 3013 | 10581096038666 | RÄTTA | meta | Gymstick Active Foam Hand Grips är handtag i skummaterial med mjuk och greppvänlig yta. Enligt tillverkaren passar de på de flesta skivstänger och hantlar. | Gymstick Active Foam Hand Grips är handtag i skum. Enligt tillverkaren har de mjuk och greppvänlig yta och passar de flesta skivstänger och hantlar. |
| 3013 | | | skäl | | 'Mjuk och greppvänlig yta' står som fakta i metan men som tillverkarpåstående i html; samma tillskrivning i båda. Benämningen 'handtag i skum' bör bekräftas (troligen grepp som träs på stången). |
| 3014 | 10581096104202 | GODKÄND | – | – | Tunn text utan meta, korrekt. |
| 3015 | 10581096169738 | RÄTTA | meta | Gymstick Active Jump Rope är ett hopprep på 275 cm. Enligt tillverkaren passar det för uppvärmning och intervallträning, för både nybörjare och erfarna. | Gymstick Active Jump Rope är ett hopprep på 275 cm. Enligt tillverkaren passar det nybörjare och erfarna utövare för uppvärmning och intervallträning. |
| 3015 | | | skäl | | 'för både nybörjare och erfarna' saknar substantiv. |
| 3016 | 10581096235274 | RÄTTA | meta | Gymstick Active Mini Bands är ett set med två kompakta motståndsband för träning av hela kroppen, enligt tillverkaren. Bandens material är slitstarkt. | Gymstick Active Mini Bands är två kompakta motståndsband. Enligt tillverkaren är de gjorda av slitstarkt material och passar för träning av hela kroppen. |
| 3016 | | | skäl | | 'Bandens material är slitstarkt.' är ett tillverkarpåstående utan 'enligt tillverkaren'. |
| 3017 | 10581096333578 | GODKÄND | – | – | Massageboll är tillåtet produktnamn; inga effektpåståenden. |
| 3018 | 10581096399114 | GODKÄND | – | – | Allt spårbart; 20 cm skrivs som storlek. |
| 3019 | 10581096464650 | GODKÄND | – | – | Varianterna L/M/S (89–259 kr) låses inte. Rätt hanterat. |
| 3020 | 10581096497418 | RÄTTA | titel | Handgrip Gymstick Active Power | Greppstärkare Gymstick Active Power |
| 3020 | 10581096497418 | RÄTTA | seo_title | Handgrip Gymstick Active Power | Greppstärkare Gymstick Active Power |
| 3020 | 10581096497418 | RÄTTA | html | <p>Gymstick Active Power Hand Grip är en handgrip för greppträning, enligt tillverkaren till underarmar, händer och fingrar.</p> | <p>Gymstick Active Power Hand Grip är en greppstärkare för träning av underarmar, händer och fingrar, enligt tillverkaren.</p> |
| 3020 | 10581096497418 | RÄTTA | html_2 | <li>Typ: Handgrip</li> | <li>Typ: Greppstärkare</li> |
| 3020 | | | skäl | | 'Hand Grip är en handgrip' är cirkulär engelska; 3007 i samma serie heter 'Greppstärkare'. Meningen 'enligt tillverkaren till underarmar' är ogrammatisk. Kilouppgiften (30/45) rätt utelämnad. |
| 3021 | 10581096530186 | GODKÄND | – | – | Massageboll, inga effektpåståenden. |
| 3023 | 10581096595722 | GODKÄND | – | – | Inga effektpåståenden. |
| 3024 | 10581096694026 | GODKÄND | – | – | Allt spårbart; stress- och rehabpåståenden utelämnade. |
| 3025 | 10581096759562 | RÄTTA | titel | Träningsmatta Gymstick Active | Träningsmatta Gymstick Aktiv |
| 3025 | 10581096759562 | RÄTTA | seo_title | Träningsmatta Gymstick Active | Träningsmatta Gymstick Aktiv |
| 3025 | 10581096759562 | RÄTTA | meta | Gymstick Active är en träningsmatta för träning från yoga till styrketräning. Enligt tillverkaren är den enkel att rulla ihop och ta med sig. | Gymstick Aktiv är en träningsmatta för allt från yoga till styrketräning. Enligt tillverkaren är den enkel att rulla ihop och ta med sig. |
| 3025 | 10581096759562 | RÄTTA | html | <p>Gymstick Active är en träningsmatta | <p>Gymstick Aktiv är en träningsmatta |
| 3025 | | | skäl | | Källan (titel och text) heter 'Aktiv Träningsmatta'; utkastet byter namnet till 'Active'. Samma serie 3006 behåller 'Aktiv'. Meta: 'träningsmatta för träning' upprepar. |
| 3026 | 10581096923402 | GODKÄND | – | – | Vikten låses inte trots varianter 1/3/5 med olika pris. 'Active' för 'Aktiva vinylhantlar' är en tolkning, se öppen fråga. |
| 3027 | 10581096956170 | GODKÄND | – | – | Tunn text, inga effektpåståenden. |
| 3028 | 10581096988938 | GODKÄND | – | – | Allt spårbart. |
| 3030 | 10581100331274 | GODKÄND | – | – | Bara nät; passform mot mål okänd och flaggad. |
| 3031 | 10581100364042 | GODKÄND | – | – | Källan säger entydigt 'nät'. |
| 3034 | 10581100757258 | UNDERKÄND | – | – | Källan motsäger sig: titeln säger nät, texten ett robust mål som tål hårda skott. Är det ett mål gäller samma säkerhetsbedömning som för 3033 (avvisat). |
| 3036 | 10581100888330 | UNDERKÄND | – | – | Källan motsäger sig: titeln säger nät, texten ett kompakt mål. Oklar produkttyp; minimålet 3035 är avvisat. |
| 3037 | 10581100921098 | UNDERKÄND | – | – | Oklar produkttyp och montering (dörr, vägg eller stativ okänt; 'basketkorg' är en tolkning). Kan vara ställning eller barnprodukt. Utkastaren flaggar själv. |
| 3038 | 10581101084938 | GODKÄND | – | – | Tunn men korrekt. |
| 3039 | 10581101117706 | GODKÄND | – | – | Tunn men korrekt. |
| 3040 | 10581101281546 | RÄTTA | html | passar pilarna både träning och tävling. | passar pilarna för både träning och tävling. |
| 3040 | | | skäl | | Preposition saknas. |
| 3041 | 10581101609226 | RÄTTA | html | <p>Gymstick Hula Hoop med fog. Enligt tillverkaren gör fogen att ringen är enkel att montera och ta med sig.</p> | <p>Gymstick Hula Hoop är en träningsring med fog. Enligt tillverkaren gör fogen ringen enkel att montera och ta med sig.</p> |
| 3041 | | | skäl | | Första meningen saknar verb. Vikten låses rätt inte (varianter 1,2 och 1,5P med olika pris). |
| 3047 | 10581102035210 | UNDERKÄND | – | – | Oklar produkttyp: 'remmar' för crunch-övningar är troligen hängande magremmar på en stång (bär kroppsvikten). Ingen svensk typ i titeln; källan är bara säljtext. |
| 3048 | 10581102067978 | UNDERKÄND | – | – | Oklar produkttyp; utkastaren vet inte om det är matta, stöd eller hjul och sätter inget svenskt typord. |
| 3049 | 10581102199050 | UNDERKÄND | – | – | Den inbyggda räknaren kan vara elektronisk (batteri); källan säger inte. Kan släppas om David bekräftar att räknaren är mekanisk. |
| 3051 | 10581104230666 | UNDERKÄND | – | – | Oklar produkttyp ('justerbart handtag … träningsaccessoar'), oförklarade varianter L/S. |
| 3052 | 10581104427274 | UNDERKÄND | – | – | Uppblåsbart landningsunderlag för gymnastik och cheerleading (fallskydd, används ofta av barn); källan bygger på stötdämpning och ledbelastning. Skydd med skadeförebyggande funktion. Färgvarianter BL/BLU/PI oförklarade, pump okänt. |
| 3055 | 10581104525578 | RÄTTA | titel | Handtränare i Aluminium Gymstick Hand Grip | Handtränare i Aluminium Gymstick |
| 3055 | | | skäl | | 'Handtränare … Hand Grip' är cirkulär engelska. Ny titel = SEO-titeln (lagras tom). |
| 3056 | 10581104558346 | RÄTTA | titel | Ankelfästen Gymstick Ankle Straps PR | Ankelfästen Gymstick PR |
| 3056 | 10581104558346 | RÄTTA | seo_title | Ankelfästen Gymstick Ankle Straps | Ankelfästen Gymstick PR för Benövningar |
| 3056 | | | skäl | | 'Ankelfästen … Ankle Straps' är cirkulär engelska. 'PR' oförklarat, se att bekräfta. |
| 3057 | 10581104591114 | GODKÄND | – | – | Titeldubbletten med 3008 löses genom rättningen av 3008. |
| 3059 | 10581104656650 | RÄTTA | titel | Stressbollar Gymstick Anti-Stress Ball, 3 st | Stressbollar Gymstick, 3 st |
| 3059 | | | skäl | | 'Stressbollar … Anti-Stress Ball' är cirkulär engelska. Ny titel = SEO-titeln. |
| 3060 | 10581104689418 | GODKÄND | – | – | Allt spårbart. |

## Avvisade av utkastarna (15)
Alla 15 avvisningar är rimliga: 3003 (Massager, hälsoord), 3022 (akupressur), 3029, 3032, 3033, 3035 (fristående mål), 3042–3046 (skivstänger och viktset), 3050 och 3054 (lås och last), 3053 (J-Cup, skydd), 3058 (fotledsstöd). Ingen kan släppas.

## Öppna frågor till David
1. **Aktiv eller Active:** leverantören skriver ibland 'Aktiv/Aktiva' (3006, 3008, 3009, 3025, 3026) för Gymsticks Active-serie. Jag har föreslagit att originalets 'Aktiv' behålls (3008, 3025), men 3026 skriver 'Active'. Ska serien heta Active överallt?
2. **3001:** behåll maxbelastning 120 kg och punkten om att sitta på bollen i stället för en stol?
3. **3049:** är räknaren mekanisk? I så fall kan produkten släppas.
4. **3009 och 3013:** vad är en 'tunnrulle', och är 'handtag i skum' rätt benämning för grepp som träs på stången?
5. c_6 nr 3087 och c_10 nr 3142/3148 behöver granskas mot de nya SEO-titlarna här, så att ingen dubblett uppstår igen.
