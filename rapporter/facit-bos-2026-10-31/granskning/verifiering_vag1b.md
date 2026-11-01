# Verifiering våg 1b – BEST OF SPORTS (2026-11-01)

Oberoende kontroll, bara läsning. Inget skrevs till Shopify och inga andra filer ändrades.

- Butik: get-shop-info gav **BEST OF SPORTS** (bestofsports.se, SEK, Sverige).
- Hämtat live med `graphql_query` (`nodes(ids:)`: title, status, handle, updatedAt, seo{title description}, descriptionHtml) i tre batchar: 8 + 8 + 3 (de två pilotprodukterna och 105).
- Jämfört mot `vag1_skriv/skriv_1..4.json` (matchat på `nr`) och `vag1_skriv/pilot_1b.json`. Före-läget hämtades ur `shopify-original-2026-11-01/vag1b_fore.json`, status före ur `vag1_skriv_1..4_fore.json` och handles ur exporten `bos-produkter-titlar-beskrivningar-2026-10-25.csv`.

## 1. Live jämfört med skrivfilerna

**Resultat: 18 av 18 är identiska** i titel, SEO-titel, meta och html, tecken för tecken. Html stämmer exakt, också radbrytningarna (`\n`) mellan `<li>`, så ingen normalisering behövdes.

| nr | Produkt-id | Status | Handle oförändrad | seo.title | Ändrat jämfört med före |
|---|---|---|---|---|---|
| 106 | 10588447539466 | ACTIVE | ja | egen | meta |
| 107 | 10588447473930 | ACTIVE | ja | egen | meta, html |
| 115 | 10486654075146 | ACTIVE | ja | null (= titel) | html |
| 302 | 10472215347466 | ACTIVE | ja | egen | html |
| 303 | 10472303689994 | **DRAFT** | ja | egen | html |
| 315 | 10472270266634 | ACTIVE | ja | egen | html |
| 401 | 10475978916106 | ACTIVE | ja (`…-indiaka-…`) | egen | titel, SEO, meta, html |
| 408 | 10472300314890 | ACTIVE | ja | null (= titel) | html |
| 414 | 10472271184138 | ACTIVE | ja | egen | html |
| 502 | 10472279965962 | **DRAFT** | ja | egen | meta |
| 601 | 10472279638282 | ACTIVE | ja | egen | titel, SEO |
| 702 | 10480045752586 | ACTIVE | ja | null (= titel) | html |
| 704 | 10650210402570 | ACTIVE | ja | egen | titel |
| 812 | 10462778818826 | ACTIVE | ja | null (= titel) | html |
| 903 | 10472216363274 | ACTIVE | ja | egen | meta (tidigare null) |
| 909 | 10494680563978 | ACTIVE | ja | null (= titel) | meta, html |
| AXA | 10475621089546 | ACTIVE | ja | egen | SEO, html |
| KB | 10588446589194 | ACTIVE | ja | egen | SEO, html |

- **Avvikelser: 0.** Inget fält skiljer sig mellan live och fil.
- **Status:** oförändrad för alla 18. Före-filerna anger DRAFT för 303 och 502 och ACTIVE för de övriga 14. Pilotprodukterna saknar status i före-filerna; live är ACTIVE, vilket stämmer med skrivrapporten.
- **Handle:** alla 18 handles finns ordagrant i exporten från 2026-10-25, så de är oförändrade. 401 behåller `indiaka` i handle, som avsett.
- **Tidpunkter:** alla 18 har `updatedAt` mellan 21:43:19 och 21:45:22 (2026-11-01 UTC). 401 skrevs först, som kanarieprodukt (testprodukten som skrivs före resten). 105 har 19:15:29 och rördes alltså inte i våg 1b.
- **Borttagen text är borta live:** "(inom Sverige 179 kr)" finns inte i AXA eller KB. Inte heller "Indiaka" (utom i 401:s handle), "Set: 2 per set" (107), "Set om 2" eller "…annan vikt, eftersom…" (315), "Storlek: L 30,5…" (414), "många poser" eller "yin yoga" (702 och 812).

## 2. Regler

| Regel | Utfall |
|---|---|
| Titel ≤ 70 | OK. Längst är 704 med 59 tecken. |
| SEO-titel ≤ 43 | OK. Längst är 107 med 42 och KB med 41. |
| Meta 130–155 där den finns | OK. 106: 150, 107: 153, 909: 136, 302: 140, 303: 150, 903: 132, 315: 155 (på gränsen), 401: 145, 414: 141, 502: 149, 702: 146, 704: 146, 812: 144, AXA: 137, KB: 133. Meta saknas (null) på 115, 408 och 601, som rapporten redovisar. |
| Enheter med gemener | OK. Inga träffar på KG, Cm, ML och liknande. |
| Tankstreck i intervall | OK. Inga intervall med bindestreck (siffra-siffra); enda träffen är org.nr 559500-4325. 303 och 502 har 166–178 och så vidare. |
| Stor bokstav efter kolon | **1 brott: 903 meta** slutar "Material och färg: **k**ork." Övriga skriver "Färg: Mint." (303) och i html "Material och färg: Kork" (903 och 909). |
| Versaler på beskrivande ord i titel och SEO-titel | OK. Bara prepositioner, konjunktioner och enheter har gemener (i, för, med, och, kg, cm, g, ml, oz). 704 "Vrid-och-lås-mekanism" har stor bokstav på första ledet, vilket stämmer med regeln. |

## 3. Språkgranskning

### Ändringarna i skrivrapporten
- **401 Indiaca:** stavningen är konsekvent i titel, SEO-titel, meta, ingress, specifikation och FAQ ("Indiaca Tennis" och "Indiaca Play-boll"). OK.
- **601 titel:** "Mobilhållare Toorx för Arm, Armband för Smartphone" läses bättre än tidigare. "för" står två gånger, men det är godtagbart. SEO-titeln "Mobilhållare Toorx för Arm" är OK.
- **704 "Vrid-och-lås-mekanism":** titeln stämmer med meta och html ("vrid-och-lås-mekanism", med gemener i löptext). OK. Ingress, specifikation och meta upprepar dock nästan ordagrant "vikten väljs med vrid-och-lås-mekanism på handtaget" och "viktskivor(na) som inte används förvaras på basen", så samma två fakta står tre gånger.
- **414:** "Mått (L x B x H): 30,5 x 16 x 12,5 cm" och "Dig som vill ha handskar på 14 oz" är OK. "Bred kardborre" står fyra gånger: ingress, passar för, specifikation och meta.
- **107:** "Set: 2 per set" är borta. Den nya andra meningen i meta är OK. **Den första meningen i meta saknar verb:** "Tunturi handleds- och fotvikter i neopren, 2 x 0,5 kg per set." Meta slutar också med fragmentet "En storlek."
- **909:** "Tunturi massagerulle är gjord i kork och väger 680 g." är grammatiskt OK, men "Tunturis massagerulle" eller "Massagerullen från Tunturi" hade varit idiomatiskt bättre. Samma mönster finns i 107 ("Tunturi handleds- och fotvikter är…"), så det är en stilfråga och inget fel.
- **903 (ny meta):** brott mot kolonregeln (se avsnitt 2). Ordet kork upprepas: "korkmassagebollar … två bollar i kork … Material och färg: kork." Ingressen i html skriver "har **diametern** 5 och 6,5 cm", där det bör stå "diametrarna" (två bollar), som i meta. Den raden ändrades inte i våg 1b men syns nu bredvid den nya metan. Passar för-punkten "Dig som vill ha massagebollar i kork" säger inget nytt (cirkulär).
- **106:** meta "väger 1 kg och är i svart och grönt syntetmaterial" är OK.
- **115 och 408:** "Det här är en …" har verb och är OK, men texterna är mycket tunna (en mening).
- **302:** "Med hjulet tränar du överkropp och bål." är OK. Passar för-punkterna upprepar ingressen: "träna överkropp och bål" och "dubbelhjuldesign och breda handtag".
- **303 och 502:** tankstrecken är rätt. I 502 saknar båda meningarna i meta verb: "Tunturi gymnastikboll med diameter 65 cm och vikt 1,1 kg." och "Röd, lämplig för …". 303:s meta "avsedd för längd över 190 cm" är stel; "för personer som är längre än 190 cm" vore bättre.
- **315:** borttagningarna är korrekta. Meta slutar med två verblösa fragment: "Finns även i andra vikter. En storlek."
- **702 och 812:** "positioner" och "yinyoga" är rätt, och texterna är identiska bortsett från färgen. Däremot är "utför många positioner" ett ovanligt uttryck; "intar" eller "gör många övningar" vore bättre. Meta har fragment utan verb: "Halkfri och lätt att rengöra, med bärväska. Finns i 7 färger, här svart/grå."
- **Pilot AXA:** fraktparentesen är borta. "under en kortare till medellång tid" och "Hållare som monteras på flaskhållarfästen eller med två remmar" är OK. SEO-titeln "Vikbart Cykellås AXA Fold 85, 85 cm" upprepar 85 och läses som en dubblering. Metan, som inte ändrades i våg 1b, har "…stållänkar och Sold Secure Bronze", där det saknas ett verb för certifieringen ("och är certifierat enligt Sold Secure Bronze").
- **Pilot KB:** fraktparentesen är borta. Den nya FAQ:n och specifikationsraderna är OK. Som tidigare noterat skiljer sig metan ("styrka, kondition och rörlighet") från FAQ-svaret ("Styrka, koordination, flexibilitet och bålstabilitet"). Metans båda meningar saknar verb ("Tunturi PE-kettlebell 16 kg i PVC fylld med sand." och "Lätt att rengöra …"). Ingressen upprepar ordet: "PE-kettlebell är en kettlebell".

### Sammanfattning av språkfynd
- **Regelbrott:** 1, kolonregeln i 903:s meta.
- **Språkfel som bör rättas:** 903 html "diametern", som ska vara "diametrarna".
- **Meningar utan verb i meta:** 107, 315, 414, 502, 702, 812 och KB, samt delvis AXA. Det är ett mönster i metatexterna (kortfattad stil), inte något som infördes i våg 1b, utom 107:s och 903:s nya meta. Om regeln "verb i varje mening" ska gälla även meta behövs en egen rättningsomgång.
- **Upprepningar:** 704, 414, 302, 903 och KB, enligt ovan.
- **Stavfel:** inga hittades.

## 4. Nr 105 – inkonsekvent produktnamn (inget ändrat)

Live för produkt 10461917741322, senast uppdaterad 19:15:29, alltså inte i våg 1b:
- Titel: "Gymnastikmatta Tunturi **Fitnessmat Pro**, 140 cm, Blå"
- SEO-titel: "Gymnastikmatta Tunturi **Fitnessmat Pro**"
- Meta: "Tunturi **Fitness Mat Pro** är en blå gymnastikmatta i gummi, …"
- Brödtext: "Tunturi **Fitness Mat Pro** är en blå gymnastikmatta i gummi som mäter 140 x 60 x 1,5 cm, …"

Titel och SEO-titel säger "Fitnessmat Pro", medan meta och brödtext säger "Fitness Mat Pro". Skrivrapporten beskriver samma läge och lämnar valet till David: tillverkarens stavning "Fitnessmat Pro" överallt, vilket rapporten rekommenderar, eller "Fitness Mat Pro" överallt.

## Slutsats
- 18 av 18 produkter stämmer live med skrivfilerna. Status och handles är oförändrade, och 0 fält avviker.
- Ett regelbrott: 903:s meta har gemen efter kolon. Ett språkfel: 903:s html har "diametern" där det ska vara "diametrarna". Därutöver finns stilanmärkningar: verblösa metameningar och upprepningar.
- 105 är fortfarande inkonsekvent och väntar på Davids besked.
