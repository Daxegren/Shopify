# Granskning k_35c och k_35d (2026-11-05)

Oberoende granskare, endast läsning. Live läst via `shopify_api.py` (ShopifyKlient) mot BEST OF SPORTS (bestofsports.se). Inget ändrat i Shopify, inget committat. Davids beslut 2026-11-05 tillämpat: dubblett = exakt samma artikel (modell, färg, storlek, vikt).

## Sammanfattning

- Utkast: 2 produkter, båda **RÄTTA** (små språkfel). Inget påstående har smugit in; skillnaden mot syskonet står i egen källa i båda fallen.
- Avvisade som kontrollerades: 35037, 35038, 35039, 35044 och 'samma artikel' 35014, 35015, 35017, 35018, 35019, 35023, 35031, 35034. **Ingen lyfts ur.** 35044 har fel skäl (se nedan) och är en fråga till David.
- Båda utkasten: ACTIVE, lager > 0 (1 respektive 211). `skrivfil_kontroll.py`: 0 fel. Titel, SEO och meta unika mot alla `*utkast*.json` och `k_skriv_*.json`.

## Utkast

| nr | id | dom |
|---|---|---|
| 35036 | 10523488321802 | RÄTTA |
| 35042 | 10636651233546 | RÄTTA |

### 35036 (10523488321802): RÄTTA

**meta**

Före:

```
Cykel Romet Vintage Eco M har stålram, 6 växlar med Shimano Tourney, V-bromsar och 700 x 35C-däck. Stöd, pakethållare och stänkskärmar ingår.
```

Efter:

```
Cykeln Romet Vintage Eco M har stålram, 6 växlar med Shimano Tourney, V-bromsar och 700 x 35C-däck. Stöd, pakethållare och stänkskärmar ingår.
```

**html**

Före:

```
ingår i setet.</p><h2>Passar för</h2><ul>
<li>Dig som söker en cykel för dagliga turer till jobbet, affären och utflykter, enligt tillverkaren</li>
<li>Dig som vill ha 6 växlar med Shimano Tourney och stålram</li>
<li>Dig som vill ha pakethållare, stänkskärmar och belysning i samma set</li>
```

Efter:

```
ingår.</p><h2>Passar för</h2><ul>
<li>Dig som söker en cykel för dagliga turer till jobbet, affären och utflykter, enligt tillverkaren</li>
<li>Dig som vill ha 6 växlar med Shimano Tourney och stålram</li>
<li>Dig som vill att pakethållare, stänkskärmar och belysning ska ingå</li>
```

Skäl: Live: BEST OF SPORTS, ACTIVE, 'Cykel ROMET Vintage Eco M, turkos', en variant (Default Title, SKU 28181056-B, EAN 5904803191437, 6 789 kr), lager 1. Egen källa anger modellen Vintage Eco M fyra gånger; syskonet 10472291008778 (SKU 28181056-A, lager 7, texter-klara) hade i originalkällan (rapporter/shopify-original-2026-11-03/vag2k_2_fore.json) Vintage Eco D, 'designad för kvinnor', med hjulvikt 15,3 kg. Olika modell, alltså inte exakt samma artikel enligt Davids beslut 2026-11-05. Webben (velomarket.ee, sportano.com) bekräftar att Eco M (herr) och Eco D (dam) är två modeller och att Eco M finns i turkos; EAN 5904803191437 gav ingen träff. Risk att notera: samma artikelkod 28181056 och samma pris; suffixen -A/-B förekommer både på Eco D och Eco M i butiken (28181054-A D grafit, 28200714-A M grön), så koden avgör inget och tolkas inte. Allt i texten finns i egen källa: stål, Tourney, 6 växlar, V-bromsar, 700 x 35C, ingår-listan; färg ur live-titeln. Ramstorlekarna M/L rätt utelämnade (en variant). Ingen lastuppgift för pakethållaren, inga marknadsföringsord. Format: titel 33 tecken/1 komma, SEO 33, meta 141 (142 efter rättning) med verb, Passar för, standardblocket exakt, en 'enligt tillverkaren', ingen På beställning-tagg. Unik mot alla utkast och k_skriv_* (Eco M Grön 10472290713866 har egen titel/SEO/meta). skrivfil_kontroll.py: 0 fel. Rättning: 'setet' (direktöversatt 'Setet inkluderar', förväxlas med sätet) i två meningar, och meta 'Cykel ... har' till bestämd form.

### 35042 (10636651233546): RÄTTA

**seo_title**

Före:

```
Curlstångspaket E Series Plastbelagda
```

Efter:

```
Curlstångspaket E Series med Plastskivor
```

**html**

Före:

```
<li>Curlstång: Går att demontera för förvaring</li>
```

Efter:

```
<li>Förvaring: Curlstången går att demontera</li>
```

Skäl: Live: ACTIVE, 'Curlstångspaket E Series 30kg', en variant (SKU GN002-00006-0032, 1 319 kr), lager 211. Egen källa: SZ-curlstång 120 cm, 25 mm, två skivor 7,5 kg, två 5 kg, plastbelagda, två stjärnlås, kan demonteras för förvaring; allt i texten stämmer. Syskonet 10636650938634 (GN019-00002-0032, 2 819 kr, lager 0) har enligt sin originalkälla åtta skivor 2,5 kg och fyra 1,25 kg i gjutjärn med håldiameter 26 mm: annan vikt och annat material, alltså egen artikel. Totalvikt 30 kg och utökning till 45 kg nämns inte (kontrollerat i titel, SEO, meta och html), ingen lastuppgift, 'högkvalitativa' och 'repor på golv' borta, ingen håldiameter påhittad. Format: titel 52 tecken/0 komma, meta 134 med verb, Passar för, standardblocket exakt, ingen 'enligt tillverkaren' behövs. Unik mot alla utkast och k_skriv_*. skrivfil_kontroll.py: 0 fel. Rättningar: SEO-titeln slutade på ett adjektiv utan substantiv ('Plastbelagda'); ny SEO 40 tecken, unik, ordet plast är leverantörens ('SZ-Curlset 25mm plast'). Specifikationen hade två rader med etiketten 'Curlstång:'.

## Avvisade som kontrollerades

| nr | id | fil | slutsats |
|---|---|---|---|
| 35037 | 10541369622794 | k_35d_avvisade.json | Avvisningen står. Egen källa: plast, 45 g, Giant; färg Svart/Neongrön bara i live-titeln. Syskonet 10530129051914 (texter-klara): ProWay, plast, 45 g, svart/neongrön. Ingen källa anger annan modell, färg, storlek eller vikt. Skälet är något fel i detaljen: '500–750 ml' står bara i syskonets källa, inte i 35037:s egen. SKU 490000074 mot 490000072, 109 mot 59 kr. |
| 35038 | 10541369721098 | k_35d_avvisade.json | Avvisningen står: samma som 35037 (plast, 45 g, Svart/Neongrön i titeln), SKU 490000071, 109 kr, lager 14. Tre listningar med olika EAN men samma färg i alla titlar; om titlarna är fel (olika kulörer i verkligheten) kan bara David/leverantören reda ut det. |
| 35039 | 10548290978058 | k_35d_avvisade.json | Avvisningen står: egen källa och syskonets originalkälla (10472332067082) är ord för ord lika i allt som avgör artikeln: Wagant 8, svart, aluminium, L (21"), Alivio, 27 växlar, BL-MT200/BR-MT200, VeeTire 700x42C, hjulvikt 18,2 kg. Samma pris 12 359 kr. Exakt dubblett. |
| 35044 | 10636715163914 | k_35d_avvisade.json | Avvisningen står tills vidare, men skälet 'endast SKU, streckkod och pris skiljer' är fel. Syskonets originalkälla (10636691013898, rapporter/shopify-original-2026-11-04/k_skriv_07d08a_fore_rest.json) heter 'Ankelband Vristband Läder 2x34cm' och säger 'Säljs i par' (949 kr). Den här källan heter '34cm', talar om 'bandet' i singular och säger inget om par (449 kr). Modell, material, färg, längd och 120 kg är samma; antalet troligen inte. Egen källa säger inte ordagrant 'styck', så en skillnad kan inte skrivas ut utan att gissa. Fråga till David: räknas ett band och ett par som olika artiklar? Om ja kan den skrivas utan antalsuppgift, med 'Maximal belastning enligt tillverkaren: 120 kg' en gång och utan rehabpåståendet. |
| 35014 | 10472305950986 | k_35b_avvisade.json | Avvisningen 'samma artikel' står: egen live-källa och syskonets (10472305885450) originalkälla anger samma modell, färg och storlek/vikt (110 mm, lila/svart, 0,270 kg, pris per hjul, 1 669 kr i båda). Ingen källa anger någon skillnad; endast SKU/EAN skiljer, och artikelnummer tolkas inte. Ingen lyfts ur. |
| 35015 | 10472332230922 | k_35b_avvisade.json | Avvisningen 'samma artikel' står: egen live-källa och syskonets (10507259478282) originalkälla anger samma modell, färg och storlek/vikt (Wagant 0 grågrön, XL (23"), 17 kg, 21 växlar, 8 949 kr i båda). Ingen källa anger någon skillnad; endast SKU/EAN skiljer, och artikelnummer tolkas inte. Ingen lyfts ur. |
| 35017 | 10472333607178 | k_35b_avvisade.json | Avvisningen 'samma artikel' står: egen live-källa och syskonets (10507443044618) originalkälla anger samma modell, färg och storlek/vikt (Jolene 7.2 mörkröd-orange, M (17"), 24 växlar, ca 15 kg; 8 679 mot 8 699 kr). Ingen källa anger någon skillnad; endast SKU/EAN skiljer, och artikelnummer tolkas inte. Ingen lyfts ur. |
| 35018 | 10472333639946 | k_35b_avvisade.json | Avvisningen 'samma artikel' står: egen live-källa och syskonets (10472295006474) originalkälla anger samma modell, färg och storlek/vikt (Excelsior Dandy svart, M 52 och L 56 cm listade, 10,9 kg, en variant, 8 909 kr i alla tre). Ingen källa anger någon skillnad; endast SKU/EAN skiljer, och artikelnummer tolkas inte. Ingen lyfts ur. |
| 35019 | 10472372338954 | k_35b_avvisade.json | Avvisningen 'samma artikel' står: egen live-källa och syskonets (10656692175114) originalkälla anger samma modell, färg och storlek/vikt (Orkan M grå-röd, L (19") och XL (21") listade, 14,5 kg, 21 växlar, 6 549 kr i båda). Ingen källa anger någon skillnad; endast SKU/EAN skiljer, och artikelnummer tolkas inte. Ingen lyfts ur. |
| 35023 | 10476185125130 | k_35b_avvisade.json | Avvisningen 'samma artikel' står: egen live-källa och syskonets (10460948398346) originalkälla anger samma modell, färg och storlek/vikt (Revolt 2 Ocean Storm, S–XL listade, en variant, 18 växlar, 25 439 kr i båda). Ingen källa anger någon skillnad; endast SKU/EAN skiljer, och artikelnummer tolkas inte. Ingen lyfts ur. |
| 35031 | 10507442946314 | k_35c_avvisade.json | Avvisningen 'samma artikel' står: egen live-källa och syskonets (10472332919050) originalkälla anger samma modell, färg och storlek/vikt (Jolene 7.1 vit-blå, M (17"), 21 växlar, mekaniska skivbromsar, ca 15 kg; 7 529 mot 7 519 kr). Ingen källa anger någon skillnad; endast SKU/EAN skiljer, och artikelnummer tolkas inte. Ingen lyfts ur. |
| 35034 | 10523486585098 | k_35c_avvisade.json | Avvisningen 'samma artikel' står: egen live-källa och syskonets (10472295006474) originalkälla anger samma modell, färg och storlek/vikt (Excelsior Dandy svart (live black), samma källtext som 35018, 8 909 kr). Ingen källa anger någon skillnad; endast SKU/EAN skiljer, och artikelnummer tolkas inte. Ingen lyfts ur. |

## Frågor till David

1. **35036 Eco M Turkos**: Egen källa och webben (velomarket.ee, sportano.com) säger att det är modellen Vintage Eco M, och syskonet är Eco D (dam). Men båda har samma artikelkod 28181056 (suffix -A/-B) och samma pris, 6 789 kr. Enligt ditt beslut tolkas koden inte, och därför rekommenderar jag att texten skrivs. Bekräfta.
2. **35044 Ankelband**: Syskonet säljs i par (2x34 cm, 949 kr). Det här är troligen ett band (34 cm, 449 kr), men egen källa säger inte 'styck'. Räknas par och styck som olika artiklar? Om ja kan produkten skrivas utan att antalet anges.
3. **35037/35038 Flaskhållare**: tre listningar med olika EAN och priser (59, 109 och 109 kr) har alla färgen svart/neongrön i titeln. Om färgerna i verkligheten är olika är det titlarna som är fel. Det är en datafråga, inte en textfråga.

Källor för webbkontrollen: [velomarket.ee Vintage Eco M](https://velomarket.ee/en/products/bicycle-arkus-romet-vintage-eco-m-28-green/), [sportano.com Vintage Eco D](https://sportano.com/p/81422/women-s-bicycle-romet-vintage-eco-d-white-2228571).
