# Granskningsutlåtande k_46ovr1, övriga tidigare utanför-kategorier (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan text får faktatext även i tidigare utanför-kategorier), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och formatet i `k_utlatande_43.json`.

Alla 10 utkast är ACTIVE. Standardblocket är exakt som i `b_skriv_24.json` på alla. Leveranstidsmeningen finns på exakt de tre produkterna med taggen På beställning (47005, 47007, 47009). Titel 28–51 tecken och ≤2 kommatecken, SEO 27–42 tecken, meta 114–136 tecken med verb, och "Passar för" finns på alla, även efter rättning. Inga cirkulära inledningar. Titel, SEO och meta är unika inom batchen, mot övriga utkast- och skrivfiler och mot butikens titlar (sökning på Roam, Legacy, Mizar, SC30, Akupress/Akupunktur, Parma, M8000, SKid, Isskor, Kassett, SKU 14TUSYO*). Ingen exakt dubblett (R12a). `skrivfil_kontroll.py` ger 0 formatfel både på utkasten och på de rättade texterna, men 6 FEL för spärrade produkter (se frågor). Varje rättning är ETT sammanhängande före/efter-par per fält, och före-texten förekommer exakt en gång i fältet (kontrollerat i python).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_46ovr1.json`.

## Resultat: 5 GODKÄND, 5 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 47001 | 10411495817482 | k_46ovr1_utkast.json | RÄTTA | seo_title |
| 47002 | 10411850432778 | k_46ovr1_utkast.json | GODKÄND | – |
| 47003 | 10411932647690 | k_46ovr1_utkast.json | RÄTTA | html |
| 47004 | 10462778392842 | k_46ovr1_utkast.json | RÄTTA | html |
| 47005 | 10460947054858 | k_46ovr1_utkast.json | RÄTTA | html |
| 47006 | 10462155473162 | k_46ovr1_utkast.json | GODKÄND | – |
| 47007 | 10462850449674 | k_46ovr1_utkast.json | GODKÄND | – |
| 47008 | 10468719493386 | k_46ovr1_utkast.json | GODKÄND | – |
| 47009 | 10469226512650 | k_46ovr1_utkast.json | RÄTTA | html |
| 47010 | 10470896173322 | k_46ovr1_utkast.json | GODKÄND | – |

## Löften (hälsa, säkerhet, skydd, utveckling, prestanda, kvalitet)

Alla texter genomsöktes efter tydliga och subtila löftesord (säkert, grepp, halka, skydd, stabil, komfort, bekväm, slitstark, hållbar, effektiv, exakt, prestanda, stötdämpning, hälsa, smärta, cirkulation, återhämtning, avslappning, sömn, energi, certifierad, godkänd). Inget finns kvar. Det enda subtila fyndet var vågarnas lista med kroppsparametrar (fettprocent, intraabdominellt fett, kroppsålder), som stod som egen sakuppgift; den attribueras nu till tillverkaren (47003, 47004). Köldbeständighet (47002) och belastningsvikt 180 kg (47003, 47004) står ordagrant ur svensk källa och med "enligt tillverkaren" i löptext respektive specifikation.

## Per produkt

### 47001 (10411495817482): RÄTTA

Live ACTIVE, Fila, varianter 45.5/46/47 (2429/2119/2119 kr), samma färg BLKRED, lager 3: v1.9 uppfylld, titel/SEO/text låser varken storlek eller pris. Fakta ur egen källa (Air-Flow, nybörjare och avancerade, justerbar bromsvinkel och intensitet); 'enligt tillverkaren' två gånger. 'Stötdämpning och prestanda', 'stabila hjul', 'bekväma' rätt utelämnade. RÄTTA: SEO-titeln angav bara 'Röd' fast färgen är svart-röd; full färg behövs också för att skilja från oskrivna Legacy Pro 84 svart-grå (10494941495562) och 84 Lady. Spärrlistan stoppar produkten i skrivfil_kontroll.py (utanfor-tills-vidare-2026-11-04) tills undantag läggs in enligt beslutet 2026-11-08 (R14).

- **seo_title** före:

```
Rullskridskor Fila Legacy Pro 84 Röd
```

  efter:

```
Rullskridskor Fila Legacy Pro 84 Svart-Röd
```

### 47002 (10411850432778): GODKÄND

Live ACTIVE, WNT096441/46, EAN 8716404237332, 209 kr, lager 21. Uppgifter ur egen källa (gummitaggar, elastisk gummisula, 41-46, de flesta skor och stövlar, köldbeständighet -20 grader). Säkerhetsorden 'säkert', 'fast grepp', 'minskar risken att halka och falla', 'slitstarka' rätt utelämnade. Märket Winter-Grip kommer ur produktens vendor-fält och tagg (egen live-data), godtas. Inga löften. Ingen dubblett (ensam i butiken). Inte i spärrlistan.

### 47003 (10411932647690): RÄTTA

Live ACTIVE, 14TUSSP002, EAN 8717842037669, 259 kr, lager 6. Mätlista, mått, vikt, batterier ordagrant ur källan; 'Maximal belastningsvikt: 180 kg' är svensk ordagrann rad med etikett och enhet, en gång 'enligt tillverkaren' (R4). Hälsoformuleringar ('överblick över din hälsa', 'förbättra sin hälsa') utelämnade. RÄTTA (subtilt): listan med kroppsparametrar (fettprocent, intraabdominellt fett, kroppsålder m.fl.) stod som egen sakuppgift 'Mäter:'; den attribueras nu till tillverkaren så att texten inte själv utlovar mätningar av hälsoparametrar (2 'enligt tillverkaren' totalt). Typordet Våg följer live-titeln, svarta syskonet behåller Smartvåg (R7). Spärrlistan stoppar produkten i skrivfil_kontroll.py (tidigare-avvisade-2026-11-04) tills undantag läggs in enligt beslutet 2026-11-08 (R14).

- **html** före:

```
<li>Mäter: Vikt,
```

  efter:

```
<li>Mätvärden enligt tillverkaren: Vikt,
```

### 47004 (10462778392842): RÄTTA

Live ACTIVE, 14TUSSP001, EAN 8717842035467, 269 kr, lager 6. Annan SKU/EAN och färg än 47003, ingen dubblett. Samma bedömning och samma rättning av 'Mäter:' som 47003. Typord Smartvåg ur live-titeln. Inte i spärrlistan.

- **html** före:

```
<li>Mäter: Vikt,
```

  efter:

```
<li>Mätvärden enligt tillverkaren: Vikt,
```

### 47005 (10460947054858): RÄTTA

Live ACTIVE, varianter S/gray 1082009184 och L/gray 1082009187, båda 16849 kr, lager 1+1, tagg På beställning (leveranstidsmeningen finns). Bara S och L nämns (v1.5/v1.8). Specifikationerna stämmer med egen källa och med https://www.giant-bicycles.com/ee/roam-2-2025 (ALUXX, SR Suntour NEX HLO 63 mm, Tektro TKD-143, CrossCut 700x42c, Shimano CUES 2x10 = 20 växlar). Giant anger bara färgerna Asphalt Green och Black för Roam 2; svarta syskonet 10460947087626 (1082009285/287) är redan skrivet, så denna är Asphalt Green; variantnamnet 'gray' är leverantörens förenkling, färgen står bara i titeln som i live. RÄTTA: 'raka styren' (felaktig plural, två ställen) blir 'rakt styre', och specifikationsraden 'Ram: ALUXX-aluminium, skivbroms' är otydlig och blir 'för skivbroms'. Rättningen ges som ett sammanhängande stycke. Spärrlistan stoppar produkten i skrivfil_kontroll.py (tidigare-avvisade-2026-11-04) tills undantag läggs in enligt beslutet 2026-11-08 (R14).

- **html** före:

```
<p>Giant Roam 2 har raka styren, ram av ALUXX-aluminium och 20 växlar med Shimano Cues. Cykeln har fästpunkter för pakethållare och stänkskärmar.</p><h2>Passar för</h2><ul>
<li>Dig som söker en hybridcykel med raka styren</li>
<li>Dig som vill kunna montera pakethållare och stänkskärmar</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Hybridcykel</li>
<li>Märke: Giant</li>
<li>Modell: Roam 2</li>
<li>Ram: ALUXX-aluminium, skivbroms</li>
```

  efter:

```
<p>Giant Roam 2 har rakt styre, ram av ALUXX-aluminium och 20 växlar med Shimano Cues. Cykeln har fästpunkter för pakethållare och stänkskärmar.</p><h2>Passar för</h2><ul>
<li>Dig som söker en hybridcykel med rakt styre</li>
<li>Dig som vill kunna montera pakethållare och stänkskärmar</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Hybridcykel</li>
<li>Märke: Giant</li>
<li>Modell: Roam 2</li>
<li>Ram: ALUXX-aluminium, för skivbroms</li>
```

### 47006 (10462155473162): GODKÄND

Live ACTIVE, VMICSM8000142, EAN 4524667322238, 2099 kr, lager 9. EAN bekräftad som Shimano Deore XT CS-M8000 11-växlad 11-42T (ICSM8000142, https://www.bike24.com/p2124061.html, https://bike.shimano.com/en-SG/product/component/grx-di2/CS-M8000.html). DYNA-SYS11, drevbärare i legering, aluminium- och ståldrev ur egen källa. Viktminskning, hållbarhet, exakt växling och effektivitet rätt utelämnade. Drivlina, ej bärande med lastuppgift. Inte i spärrlistan.

### 47007 (10462850449674): GODKÄND

Live ACTIVE, 14TUSYO096, EAN 8717842038468, 699 kr, lager 2, tagg På beställning (meningen finns). Bara material, innehåll och vikt; alla effektlöften (spänningar, cirkulation, nervändar, återhämtning, avslappning) och OCS utelämnade. Motsägande måttrader och oklar kuddfyllning rätt utelämnade (R2). Annan SKU än svarta Pro (47211) och övriga färger; SEO unik. Spärrlistan stoppar produkten i skrivfil_kontroll.py (tidigare-avvisade-2026-11-04) tills undantag läggs in enligt beslutet 2026-11-08 (R14).

### 47008 (10468719493386): GODKÄND

Live ACTIVE, 14TUSYO091, EAN 8717842037225, 319 kr, lager 3. Mått, vikter, överdrag och innehåll ur egen källa; alla effektlöften utelämnade. Källans medicinska varningstext är utelämnad; den innehåller själv ett medicinskt påstående (oxytocin, sammandragningar) och tas därför inte in utan Davids besked (se frågor). Unik mot färgsyskonen i k_46ovr2. Spärrlistan stoppar produkten i skrivfil_kontroll.py (tidigare-avvisade-2026-11-04) tills undantag läggs in enligt beslutet 2026-11-08 (R14).

### 47009 (10469226512650): RÄTTA

Live ACTIVE, 4199, lager 0, tagg På beställning (meningen finns; beställningsvara, skrivs enligt beslutet 2026-11-08). Egen källa är engelsk och delvis trasig; bara entydiga rader används (R2). v1.10: lastgränsen i egen källa är engelsk och artikelnumret kunde inte knytas till tillverkarens Parma 4-sida, därför 'Maximal lastgräns: Ej känd' i spec och text, vilket är tillåtet. Typgodkännande och 'mest ekonomiska' rätt utelämnade. RÄTTA: stavfel 'ställer' blir 'stället'. Inte i spärrlistan.

- **html** före:

```
när ställer är monterat.
```

  efter:

```
när stället är monterat.
```

### 47010 (10470896173322): GODKÄND

Live ACTIVE, Default Title (överbliven) och 40.5/black med samma SKU, lager 1+1: v1.7, färg, storlek och pris utelämnade. Fakta ur egen källa (damer, fritidsåkning, mjuk sko med nät, fästning, Air Flow, aluminiumchassi, 4 hjul 80 mm 82A, ABEC 5). 'Hög komfort', 'stabil gång', 'håller fötterna torra' rätt utelämnade. Ensam Mizar i butiken. Spärrlistan stoppar produkten i skrivfil_kontroll.py (utanfor-tills-vidare-2026-11-04) tills undantag läggs in enligt beslutet 2026-11-08 (R14).

## Avvisade (k_46ovr1_avvisade.json, 14 st)

Alla 14 avvisningar står sig; ingen lyfts. Kontrollerat: 47011 (V20 i titeln, V10 i texten), 47013 (mörkbrun mot havsgrön), 47014 (oklart vad som ingår), 47015 och 47016 (tunn eller oklar källa), 47017 och 47018 (monteringstjänster, ingen produktfakta), 47019 (storlek kan inte styrkas, text blir identisk med skriven syskon), 47020 (olika pris, lager 0, v1.9), 47021 (olika artiklar 2,5–40 kg), 47022 (Pro 2 mot Pro 1), 47024 (PE mot PVC, 12 mot 16 kg). 47012 melatonin: undantogs uttryckligen 2026-11-06 och melatonin är läkemedelsklassat i Sverige; kräver särskilt besked. 47023 Liv Devote 1: live bekräftar att vår text, SEO och meta finns (R15); bara taggen texter-klara saknas.

## Frågor till David

1. Spärrlistan stoppar 47001 och 47010 (utanfor-tills-vidare, rullskridskor) och 47003, 47005, 47007, 47008 (tidigare-avvisade på grund av kategori eller tidigare DRAFT-status). De omfattas av beslutet 2026-11-08. Före skrivning behövs en undantagspost i `sparrlista.json` med hänvisning till beslutet (R14). Det är ett tillägg, inte en ändring.
2. Akupressurmattan 47008: källan har en varningstext (kontakta specialist vid hjärtproblem, blodtrycksproblem, blodförtunnande medel och graviditet). Den är utelämnad eftersom den själv innehåller ett medicinskt påstående (oxytocin). Ska en kort neutral rad tas med, till exempel "Tillverkaren rekommenderar att du rådgör med vårdpersonal före användning vid hjärt- eller blodtrycksproblem eller graviditet"? Rekommendation: ja, som produktfakta, på samma sätt som allergenraden 2026-11-07.
3. Peruzzo Parma 47009: tillverkarens sida för Parma 4 anger 60 kg totalt, och egen källa säger samma sak på engelska. Artikelnummer 4199 kunde inte knytas till sidan. Utkastet skriver "Ej känd" (v1.10). Vill du hellre ha 60 kg "enligt tillverkaren"?
4. 47023 Liv Devote 1 har redan text men saknar taggen texter-klara. Taggen bör läggas till i ett separat steg.
