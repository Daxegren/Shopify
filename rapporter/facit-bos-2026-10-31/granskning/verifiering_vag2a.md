# Verifiering våg 2a – BEST OF SPORTS (2026-11-02)

Oberoende kontroll, endast läsning. Inget ändrat i Shopify, inget committat.

## Metod
- `get-shop-info`: BEST OF SPORTS, bestofsports.se, SEK. Rätt butik.
- Live hämtat med `graphql_query` (`nodes(ids)`, två anrop om 16): title, handle, status, seo{title description}, descriptionHtml.
- Jämfört programmatiskt mot `vag2_skriv/a_skriv.json` (sanningen) och handle mot `shopify-original-2026-11-01/vag2a_fore.json`.
  - seo.title förväntas null när seo_title = titel; seo.description null när meta är null.
  - Leveransblocket ersattes vid avskrift av live-svaret med två platshållare (A = standard, B = med "Beställningsvaror kan ta upp till en vecka längre."). Live-texten lästes och var identisk med A/B; B förekommer live på exakt 2210, 2309 och 2414, samma tre som i skrivfilen.
- descriptionHtml matchar även utan normalisering av radbrytningar mellan `<li>` (skrivfilen innehåller redan `\n`).

## Resultat per produkt
| id | nr | titel | seo.title | meta | html | ACTIVE | handle |
|---|---|---|---|---|---|---|---|
| 10411606081802 | 2101 | ja | ja | ja | ja | ja | ja |
| 10411669750026 | 2102 | ja | ja | ja | ja | ja | ja |
| 10411858362634 | 2103 | ja | ja | ja | ja | ja | ja |
| 10461406232842 | 2104 | ja | ja | ja | ja | ja | ja |
| 10462769840394 | 2106 | ja | ja | ja | ja | ja | ja |
| 10470898860298 | 2113 | ja | ja | ja | ja | ja | ja |
| 10470907805962 | 2114 | ja | ja | ja | ja | ja | ja |
| 10462769905930 | 2107 | ja | ja | ja | ja | ja | ja |
| 10462775017738 | 2108 | ja | ja | ja | ja | ja | ja |
| 10462775116042 | 2109 | ja | ja | ja | ja | ja | ja |
| 10468720378122 | 2110 | ja | ja | ja | ja | ja | ja |
| 10468720476426 | 2111 | ja | ja | ja | ja | ja | ja |
| 10588446523658 | 2508 | ja | ja | ja | ja | ja | ja |
| 10588446687498 | 2511 | ja | ja | ja | ja | ja | ja |
| 10588446556426 | 2509 | ja | ja | ja | ja | ja | ja |
| 10472245756170 | 2208 | ja | ja | ja | ja | ja | ja |
| 10472259813642 | 2210 | ja | ja | ja | ja | ja | ja |
| 10472238481674 | 2204 | ja | ja | ja | ja | ja | ja |
| 10472242970890 | 2205 | ja | ja | ja | ja | ja | ja |
| 10472243069194 | 2206 | ja | ja | ja | ja | ja | ja |
| 10472254603530 | 2209 | ja | ja | ja | ja | ja | ja |
| 10472267645194 | 2211 | ja | ja | ja | ja | ja | ja |
| 10472267677962 | 2212 | ja | ja | ja | ja | ja | ja |
| 10472270954762 | 2213 | ja | ja | ja | ja | ja | ja |
| 10472297464074 | 2315 | ja | ja | ja | ja | ja | ja |
| 10472283898122 | 2309 | ja | ja | ja | ja | ja | ja |
| 10472289566986 | 2313 | ja | ja | ja | ja | ja | ja |
| 10472301723914 | 2403 | ja | ja | ja | ja | ja | ja |
| 10472305393930 | 2404 | ja | ja | ja | ja | ja | ja |
| 10475978948874 | 2410 | ja | ja | ja | ja | ja | ja |
| 10472311161098 | 2407 | ja | ja | ja | ja | ja | ja |
| 10494898962698 | 2414 | ja | ja | ja | ja | ja | ja |

**Avvikelser live mot skrivfil: inga.**

## Gränser och dubbletter (skrivfilen = live)
- Titlar 29–58 tecken, högst 2 kommatecken. SEO-titlar högst 43 (2509 = 43). Meta 131–154; null på 2110, 2111, 2208, 2315, 2403, 2407, 2410, 2508, 2511.
- Inga dubbletter av titel, SEO-titel, meta eller effektiv SEO-titel (SEO-titel eller titel när den saknas).
- Tankstreck i alla intervall (11–14 kg, 5–8 arbetsdagar); inga bindestreck i intervall utanför standardblocket. Enheter med gemener. Stor bokstav efter kolon i specifikationer. Beskrivande ord i titlar och SEO-titlar har stor bokstav (bindeord i, och, för, med, om, x gemener).
- `kontrollera_produkttext.py --seo-title-max 43 --seo-suffix " – BEST OF SPORTS"` på kopia (html → beskrivning, standardblocket inom [[STANDARDBLOCK]], fakta = originaltitel + original-html ur före-filen): **32 produkter, 0 FEL, 49 varningar** (36 struktur: rubriken "Passar för" och saknade avsnitt; 13 beskrivning_langd på tunna källor). Utan fakta ger skriptet 32 FEL av typen fakta_saknas, vilket är en indatabrist och inte ett textfel.

## Språkfynd (föreslås, kräver beslut; inget ändrat)
1. **2209 – cirkulärt engelskt typord (bekräftat)**, i både html och meta.
   - html före: `<p>Tunturi Allround Boxing Gloves är boxningshandskar i konstläder, 16 oz. De har mjuk stoppning och bred kardborre.</p>`
   - html efter: `<p>Tunturi Allround är boxningshandskar i konstläder, 16 oz. De har mjuk stoppning och bred kardborre.</p>`
   - meta före (142): `Tunturi Allround Boxing Gloves är boxningshandskar i konstläder, 16 oz. De har mjuk stoppning och en bred kardborre som ger stöd åt handleden.`
   - meta efter (137): `Tunturi Allround är boxningshandskar i konstläder i storlek 16 oz. De har mjuk stoppning och en bred kardborre som ger stöd åt handleden.` (att bara stryka "Boxing Gloves" ger 128 tecken, under 130.)
2. **2213 – genus på gymtalk (bekräftat).** SAOL: talk, talken (en-ord). 2108 och 2109 skriver rätt "en gymtalk"/"talken"; 2213 skriver "ett"/"Talket"/"Det".
   - html före: `<p>Trec Liquid Chalk är ett flytande gymtalk på 250 ml. Talket torkar snabbt mot huden och absorberar fukt.</p>`
   - html efter: `<p>Trec Liquid Chalk är en flytande gymtalk på 250 ml. Talken torkar snabbt mot huden och absorberar fukt.</p>`
   - meta före (134): `Trec Liquid Chalk är ett flytande gymtalk på 250 ml. Talket torkar snabbt mot huden och absorberar fukt. Det passar för styrketräning.`
   - meta efter (133): `Trec Liquid Chalk är en flytande gymtalk på 250 ml. Talken torkar snabbt mot huden och absorberar fukt. Den passar för styrketräning.`
   - Specifikationen "Typ: Flytande talk" är korrekt och behålls.
3. **2210 – verblös mening i meta.**
   - före (150): `Tunturi fristående boxningssäck i svart PVC, 69 x 69 x 170 cm och 9,6 kg. Basen fylls med sand. Säcken passar både nybörjare och avancerade användare.`
   - efter (147): `Tunturi fristående boxningssäck är i svart PVC, väger 9,6 kg och mäter 69 x 69 x 170 cm. Basen fylls med sand. Den passar nybörjare och avancerade.`

Mindre punkter (ingen rättning krävs, för kännedom):
- 2213 titel "Gymtalk Trec Liquid Chalk, Flytande, 250 ml": "Flytande" upprepar "Liquid". Titeländring kräver beslut.
- 2213 påstår utan "enligt tillverkaren" att talken torkar snabbt; 2108 och 2109 har förbehållet. Uppgiften finns i källan.
- 2108 meta "i en förpackning som är lätt att dosera": det är produkten som doseras. Förslag: "i en förpackning som gör den lätt att dosera" (meta 150 → 153).
- 2104: "hemma, på jobbet och utomhus" står både i inledningen och i Passar för (upprepning).
- Ojämn titelform för storlek: 2508, 2511, 2509 har "Storlek S/XS/L", övriga handskar bara "XL"/"XS". SEO-titel 2509 saknar kommatecken ("Gel Shock Svart L") och 2212 saknar "#02".
- Inga påhittade hälso-, miljö- eller ursprungspåståenden hittades; alla egenskaper (kork som inte absorberar fukt, stöd åt handleden, halkfri o.d.) finns i källtexten eller är markerade "enligt tillverkaren". Stavningen "Indiaka" (2410) följer originaltiteln medan källan skriver "Indiaca".

## Slutsats
**32 av 32 produkter matchar skrivfilen exakt** i titel, SEO-titel, meta och beskrivning, alla är ACTIVE och har samma handle som före skrivningen. Tre språkrättningar föreslås (2209, 2213, 2210) med exakt före/efter ovan; de kräver Davids beslut innan något skrivs.
