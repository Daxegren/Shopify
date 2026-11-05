# Granskningsutlåtande k_31a och k_31b (2026-11-05)

Oberoende granskare, endast läsning. Live-data hämtad med `shopify_api.py` (ShopifyKlient, läsning) 2026-11-05; butiken bekräftad som BEST OF SPORTS (bestofsports.se). Inget ändrat i Shopify, inget committat.

Underlag: CLAUDE.md, regelbok v1.4–v1.9, BESLUTSLOGG (slutet), LARDOMAR (inkl. 2026-11-05 om rättningar), butiksprofilen, `c_granskarprompt.md`, formatet i `k_utlatande_28st.json`.

Maskinkontroller: `skrivfil_kontroll.py` gav 0 FEL och 0 varningar för båda filerna (spärrlistans undantag `undantag_2026-11-05.csv` frisläpper 31001, 31003 och 31006 under "reflex", 31008/31013/31015/31016 under "r3" och 31017 under "elvaxling"). Standardblocket är exakt som i `b_skriv_24.json`, och för 31016 och 31017 (taggen På beställning) står leveranstidsmeningen med som i `k_skriv_07.json`. Titel ≤70 tecken och ≤2 kommatecken, SEO-titel ≤43 tecken och meta 75–138 tecken gäller för alla. Titel, SEO-titel och meta är unika mot alla utkast och alla k_skriv-filer.

## Domar

| nr | id | dom | rättning / skäl |
|---|---|---|---|
| 31001 | 10462853693706 | RÄTTA | meta: "Bookman Reflexband i rosa" → "Bookman reflexband i rosa" |
| 31002 | 10471174832394 | RÄTTA | meta: "Bookman Reflexklistermärken i" → "Bookman reflexklistermärken i"; html: "&lt;p&gt;Bookman Reflexklistermärken är" → "&lt;p&gt;Bookman reflexklistermärken är" |
| 31003 | 10471175192842 | RÄTTA | meta: "Bookman Reflexklistermärken har" → "Bookman reflexklistermärken har"; html: "&lt;p&gt;Bookman Reflexklistermärken har" → "&lt;p&gt;Bookman reflexklistermärken har" |
| 31004 | 10472303067402 | GODKÄND | |
| 31005 | 10472303788298 | RÄTTA | meta: "Bookman Reflexklistermärken har" → "Bookman reflexklistermärken har"; html: "&lt;p&gt;Bookman Reflexklistermärken är" → "&lt;p&gt;Bookman reflexklistermärken är" |
| 31006 | 10665228206346 | RÄTTA | meta: "Bookman Reflexklistermärken har" → "Bookman reflexklistermärken har"; html: "&lt;p&gt;Bookman Reflexklistermärken har" → "&lt;p&gt;Bookman reflexklistermärken har" |
| 31008 | 10462190567690 | GODKÄND | Färgmotsägelsen är löst genom att ingen färg anges. Webbkollen visar att källans utrustning gäller den plommonfärgade årsmodellen. |
| 31013 | 10472297300234 | UNDERKÄND | Det är inte visat att varianterna är samma artikel. Artikelnumren tyder på olika årsmodeller (2020 och 2018). Texten kan släppas oförändrad om butiken bekräftar samma utrustning. |
| 31015 | 10472332099850 | UNDERKÄND | Som 31013: artikelnumren tyder på årsmodell 2023 och 2019, och källan är blandad (växelgruppen anges motsägelsefullt). Texten kan släppas oförändrad om butiken bekräftar samma utrustning. |
| 31016 | 10474079322378 | GODKÄND | |
| 31017 | 10480047325450 | GODKÄND | |

Varje rättning är en enda sammanhängande textbit per fält. Texten förekommer exakt en gång i fältet (kontrollerat i python). Ingen rättning är skarvad med "|".

## Per produkt

**Reflexprodukter (31001–31006).** Alla har en enda variant (Default Title), är ACTIVE och har lager 1–5. Varje uppgift i texten finns i källan: typ, sidoreflexer, mönster eller motiv samt fästplatserna cykel/hjälm respektive arm/ben/väska/barnvagn. Alla synlighets-, säkerhets- och komfortlöften är borta, enligt Davids beslut 2026-11-05 ("360 grader", "säkrare", "ökar synligheten", "syns i mörkret", "bekvämt"). Färgord som bara står i den engelska mönsterbeteckningen (White Leopard, Black Zebra, White Ghost, vit ben) har rätt utelämnats. Rosa (31001) och svart (31004) står i live-titeln, och produkten har en enda variant. Rättningen gäller bara stilen: typordet skrivs med versal mitt i meningen efter märket ("Bookman Reflexklistermärken"). Redan skrivna Bookman-texter skriver gement ("Bookman reflexklistermärken sätts på cykeln …", "Bookmans reflekterande klistermärken …"). 31003 har tunn källa (en mening), men den ger två fakta (motiv och fästplatser), och texten påstår inget mer.

**31008 Fatbike Kona Wo.** Varianterna M, L och XL har färgen purple, artikelnummer B36WO03/05/06 och pris 25569, 25519 och 25519 kr, med 1 i lager vardera. Det är samma cykel i tre ramstorlekar (v1.9). Varje specifikationsrad står i källan. Live-titeln säger Matte Plum, varianterna purple och källan "Färg: orange", och utkastet anger därför ingen färg. Webbkoll (R1 v1.6): https://coloradocyclist.com/products/kona-wo-26-fat-bike-matt-plum (Matt Plum, 2022–23) har exakt källans utrustning: Deore 11 växlar, MT201, RT30 180/160 mm, Jumbo Jim TR 26x4.8", Race Face Ride Fat och Mulefut 80. Utrustningen gäller alltså den plommonfärgade cykeln, och "orange" är en lös felrad. Konas nuvarande Wo (konaworld.com) har Microshift, Tektro och Vee-däck, så texten gäller bara denna årsmodell. Artikelnumren B36… tyder på att butiken säljer just den. 26 tum i titeln följer av däckangivelsen 26x4.8".

**31013 Romet Vintage LTD D och 31015 Romet Wagant 7.** Varianterna har olika pris och olika artikelnummer:

| Produkt | Variant | Artikelnummer | Pris |
|---|---|---|---|
| 31013 | Default Title | 28201899-A | 9979 kr |
| 31013 | M / yellow | 28181898-A | 8679 kr |
| 31015 | Default Title | 28230604-D | 11309 kr |
| 31015 | M / Red | 28190602-C | 9839 kr |

Romets artikelnummer verkar koda hjulstorlek och årsmodell. En polsk återförsäljare (taniaksiazka.pl) har koden RATREWAG3X28231083AB för en Wagant 3 28" 2023. En tidigare granskning (vag2_k_granskning_4_5.md) såg samma mönster för Vintage Classic: 28202517-B mot 28182516-B. Varianterna är alltså troligen olika årsmodeller (2020/2018 och 2023/2019), inte samma artikel i olika storlek. Default Title anger varken storlek eller färg. För 31015 anger källan bara storlek L, fast M säljs, och växelgruppen anges motsägelsefullt, vilket tyder på en blandad källa. v1.9 kräver att varianterna är samma artikel, och det är inte visat här. Texterna i sig stämmer med källan, och format och standardblock är rätt. De kan släppas oförändrade om butiken bekräftar att båda varianterna har samma utrustning, eller om den överblivna varianten tas bort eller delas ut.

**31016 Kona Rove AL 650.** Default Title har artikelnummer B36RV6556 (18719 kr, 1 i lager) och XL / gray har B36RV6558 (16279 kr, 0 i lager). Ändelserna 56 och 58 är ramstorlekarna L och XL i samma serie, så det är samma artikel. Varje uppgift står ordagrant i källan. Användningsområdet anges en gång med "enligt tillverkaren". Shimano Claris finns bara mekanisk. Produkten har taggen På beställning, och leveranstidsmeningen finns.

**31017 Giant TCR Advanced 0 PC.** Default Title har samma artikelnummer som M/L (1096021146), alltså en överbliven Default Title (v1.7), och L (1096021147) ligger i samma serie. Totalt lager är 2. Di2 skrivs enligt v1.7: modellen återges ordagrant, texten säger inte "mekanisk" och nämner inget batteri. Alla uppgifter står i källan, även skivbroms. Prisskillnaden mellan Default Title och M/L (58459 och 49679 kr för samma artikelnummer) är en fråga om butikens data. Texten låser inget pris. Produkten har taggen På beställning, och leveranstidsmeningen finns.

## Avvisade (k_31a_avvisade, k_31b_avvisade)

Ingen avvisning lyfts. 31007, 31011, 31018, 31022 och 31023 är olika vikter och därmed olika artiklar. 31009, 31012, 31020, 31021 och 31024 har varianter med oförklarade namn, olika pris och tunn källa. 31010 är en trampolin med maxvikt och hälsopåståenden. 31014 har en generisk källa, och artikelnumret och handle går isär. 31019 gäller infästning av vikter och har oförklarade varianter.

Obs: posterna 31001, 31003 och 31006 i `k_31a_avvisade.json` (spärrade) är inaktuella. Undantaget "reflex" lades in i commit f8287d3, och produkterna ligger nu i utkastet. Byggskriptet bör inte läsa avvisningsfilen som spärr.

## Öppna frågor till David

1. Romet 31013 och 31015: ska varianter med olika årsmodell under samma annons skrivas? Rekommendation: nej, inte förrän butiken bekräftat att utrustningen är densamma, eller tills annonsen har delats.
2. Kona Wo 31008: live-titeln (Matte Plum) och källans "Färg: orange" går isär. Texten anger ingen färg. Källraden "Färg: orange" bör rättas i butiken vid tillfälle (gäller inte texten).
3. Giant 31017: Default Title och M/L har samma artikelnummer men olika pris (58459 och 49679 kr). Det är en fråga om butikens data, inte om texten.
