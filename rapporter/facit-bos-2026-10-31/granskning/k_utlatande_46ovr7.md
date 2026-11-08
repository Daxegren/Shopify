# Granskningsutlåtande k_46ovr7, aktiva produkter i tidigare utanför-kategorier (2026-11-08)

Granskaren har bara läst i Shopify och har inte ändrat något där. Inget har committats. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient; `verifiera_butik` gav BEST OF SPORTS). `mcp__Shopify__*` användes inte. Underlaget var CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11) och BESLUTSLOGG till och med 2026-11-08. Enligt det beslutet får aktiva produkter utan text faktatext även i tidigare utanför-kategorier. Dessutom lästes LARDOMAR, butiksprofilen och `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och `k_utlatande_46ovr6.md` och formatet i `k_utlatande_43.json`. Tidigare avvisningar av samma id lästes också: b_25 (reflexer, kedjestagsskydd), k_16/k_19f (STP 26) och k_2 (Roam 3, då DRAFT).

Alla 8 utkast är ACTIVE. Taggen På beställning finns på 47602, 47603 och 47604. Bara de tre har leveranstidsmeningen, och den finns på alla tre. Standardblocket är exakt detsamma som i `b_skriv_24.json` på alla 8. Titlarna har 29–59 tecken och högst 2 kommatecken. SEO-titlarna har 28–41 tecken. Metatexterna har 112–146 tecken och har verb. Alla har avsnittet "Passar för". Inga cirkulära inledningar finns.

Titlar, SEO-titlar och metatexter är unika inom batchen och mot övriga utkast- och skrivfiler. Den enda träffen är äldre oskrivna utkast för samma id (k_02a, k_16). De är också unika mot butiken. Butiken söktes på Soft Reflector, Reflexband, Hängande, spikmatta, kedjestagsskydd/kedjeskydd, Tygklistermärken, Fabric Stickers, Roam 3 och STP 26, och på varje SKU och EAN. Ingen SKU eller EAN finns på någon annan produkt.

Varje rättning är ETT sammanhängande före/efter-par per fält. Varje före-text förekommer exakt en gång i utkastet (kontrollerat i python).

**Obs före skrivfil:** `skrivfil_kontroll.py` stoppar 6 utkast (47602, 47604–47608), eftersom de står på spärrlistan `tidigare-avvisade-2026-11-04`. Davids beslut 2026-11-08 släpper dem, men en undantagspost i `sparrlista.json` måste läggas till innan skrivfilen byggs. I övrigt ger skriptet 0 fel och 0 varningar, både före och efter rättning.

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_46ovr7.json`.

## Resultat: 5 GODKÄND, 3 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 47601 | 10636681773322 | k_46ovr7_utkast.json | RÄTTA | meta |
| 47602 | 10650167640330 | k_46ovr7_utkast.json | RÄTTA | meta, html |
| 47603 | 10650208993546 | k_46ovr7_utkast.json | GODKÄND | – |
| 47604 | 10656692044042 | k_46ovr7_utkast.json | GODKÄND | – |
| 47605 | 10665226797322 | k_46ovr7_utkast.json | GODKÄND | – |
| 47606 | 10665226862858 | k_46ovr7_utkast.json | GODKÄND | – |
| 47607 | 10665226928394 | k_46ovr7_utkast.json | RÄTTA | html |
| 47608 | 10665228402954 | k_46ovr7_utkast.json | GODKÄND | – |

## Löften och påståenden

Alla texter genomsöktes efter hälso-, säkerhets-, skydds-, utvecklings-, prestanda- och kvalitetsord. Sökningen gällde bland annat säker, synlig/syns, mörker, skyddar, halk, robust, hållbar, slitstark, stabil, komfort, bekväm, effektiv, kontroll, perfekt, stark, lätt, snabb, avslappning, cirkulation, smärta, lindring, hälsa, akupressur och stress.

Den enda träffen är "skydd" i artikelnamnet kedjestagsskydd (47602). Det är produktens namn och inget skyddslöfte. Följande källpåståenden är rätt utelämnade:
- spikmattans blodcirkulation, smärtlindring och avslappning
- reflexernas synlighet och säkerhet
- STP 26:s kontroll, hållbarhet och självförtroende vid hopp
- Roams punkteringsskydd och stabilitet
- kedjestagsskyddets "förhindrar skador och repor"

## Rättningar

### 47601 (10636681773322), fält `meta`

Före:

```
har 6 210 plastspikar, kudden 1 971.
```

Efter:

```
har 6 210 spikar, kudden 1 971.
```

### 47602 (10650167640330), fält `meta`

Före:

```
och har en förlängd fästanordning med snoddfäste.
```

Efter:

```
och har en längre fästanordning.
```

### 47602 (10650167640330), fält `html`

Före:

```
Det har en längre fästanordning med snoddfäste.</p><h2>Passar för</h2><ul>
<li>Dig som söker ett kedjestagsskydd i neopren</li>
<li>Dig som vill ha ett kedjestagsskydd med snoddfäste</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Kedjestagsskydd</li>
<li>Märke: SKS</li>
<li>Material: Flexibelt neopren</li>
<li>Fäste: Längre fästanordning med snoddfäste</li>
```

Efter:

```
Det har en längre fästanordning.</p><h2>Passar för</h2><ul>
<li>Dig som söker ett kedjestagsskydd i neopren</li>
<li>Dig som vill ha ett kedjestagsskydd med längre fästanordning</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Kedjestagsskydd</li>
<li>Märke: SKS</li>
<li>Material: Flexibelt neopren</li>
<li>Fäste: Längre fästanordning</li>
```

### 47607 (10665226928394), fält `html`

Före:

```
<li>Material: Elastiska band</li>
```

Efter:

```
<li>Band: Elastiska</li>
```

## Skäl per produkt

- **47601** (RÄTTA): Live ACTIVE, Gorilla Sports Norden, sju färgvarianter 101043-000xx-0001 (EAN 42506631035xx), alla 549 kr, totalInventory 794 (v1.9: samma artikel i olika färg, ingen färg låst). Akupressur/rehab frisläppt för aktiva produkter 2026-11-08. Alla mått, antal knoppar/spikar, material och innehåll stämmer ordagrant mot egen källa. Effektord (blodcirkulation, smärta, avslappning, akupressur) rätt utelämnade. Rättning: meta 'plastspikar' har inget stöd (källan anger bara att knopparna är av plast). Inga dubbletter (EAN/SKU bara här).
- **47602** (RÄTTA): Live ACTIVE, SKU 10994, EAN 4002556440633, lager 0, tagg På beställning; leveranstidsmening finns. Typordet stöds av live-titeln och av bike-components.de (SKS Chainstay Protector, tillverkarnr 10994) och bike24 (EAN 4002556440633, neopren). Skyddslöften (förhindrar skador och repor, tillförlitligt skydd, slitstarkt) rätt utelämnade. Rättning: 'snoddfäste' är sannolikt maskinöversättning och motsägs av återförsäljarnas kardborreband (R2: utelämna); kvar står neopren, flexibelt material och längre fästanordning.
- **47603** (GODKÄND): Live ACTIVE, SKU 1090029180, EAN 4711291240063, lager 0, tagg På beställning; leveranstidsmening finns. Tidigare underkänd som möjlig säkerhetsprodukt (7163, 20059); släppt av Davids beslut 2026-11-08. Alla specifikationer stämmer mot egen källa och mot giant-bicycles.com/ee/stp-26 (2026, Quicksilver): [F] mekanisk skivbroms 180 mm, [R] Shimano MT500 hydraulisk 160 mm, Marzocchi Bomber DJ 36 mm/GRIP/20x110/100 mm, Kenda Booster 26x2.25, Contact TR35. (bike24 med samma artikelnummer anger MT501/MT500 runt om, men tillverkarsidan och egen källa är samstämmiga.) Användningsområdet står en gång som 'enligt tillverkaren'; hopp-, kontroll- och hållbarhetslöften utelämnade. SEO lika titeln, unik mot butiken (äldre utkast k_02a/k_16 för samma id ersätts).
- **47604** (GODKÄND): Live ACTIVE, totalInventory 3; L 1082011287 13 989 kr (lager 2), XL 1082011288 13 999 kr, plus överbliven Default Title med samma SKU/EAN som XL (v1.7: ignoreras). v1.9: samma artikel i två storlekar med olika pris och lager > 0; titel/SEO/meta låser varken storlek eller pris, och specifikationen nämner bara sålda storlekar L och XL (v1.5). Typord och format följer skrivna syskon (Roam 3 Metall, Ultra Navy). Fakta stämmer mot egen källa; punkteringsskydd och komfort/stabilitetsord utelämnade. Tagg På beställning: leveranstidsmening finns.
- **47605** (GODKÄND): Live ACTIVE, SKU 418, EAN 7350051864186, lager 2. Reflex frisläppt 2026-11-08 (tidigare b_25). Bara fakta: form (källans 'Rektangel'), fäste på dragkedja, färg från live-titeln. Inga synlighets- eller säkerhetslöften. Titeln unik mot 47606 och butikens Soft Reflector-produkter (barnvarianterna heter Soft Adventure). Ingen dubblett.
- **47606** (GODKÄND): Live ACTIVE, SKU 423, EAN 7350051864230, lager 1. Bara fakta ur källan (rund form, fäste på dragkedja, färg vit ur live-titeln). Synlighets- och säkerhetsord utelämnade. Unik titel, SEO och meta. Ingen dubblett.
- **47607** (RÄTTA): Live ACTIVE, SKU 531, EAN 7350051865312, lager 4. Fakta stämmer (elastiska band, justerbart spänne, runt ben eller arm, byxor borta från kedja och drev som användning). Säkerhets- och synlighetsord utelämnade, färg saknas i källan och anges inte. Skiljer sig från skrivna Reflexband Bookman för Arm och Ben (SKU 428). Rättning: 'Material: Elastiska band' anger inget material; skrivs som bandets egenskap.
- **47608** (GODKÄND): Live ACTIVE, SKU 492, EAN 7350051864926, lager 3. Fakta stämmer (mönstrade klistermärken för kläder och väskor, även ytterkläder och sportkläder, ljusreflekterande yta). 'Syns bra i mörker', 'mer synlig', 'starka limmet', 'lätta att ta bort' rätt utelämnade. Unik mot Adventure Silver/Leopard Silver (andra SKU, DRAFT).

## Avvisade (k_46ovr7_avvisade.json, 16 st)

Ingen avvisning lyfts ur. Skälen är tunn eller motsägande källa (10636716376330, 10676714111242, de två ER1000R19 som beskriver en roddmaskin under crosstrainertitel) och exakta dubbletter av aktiva annonser med delat SKU/EAN, där lagret måste flyttas först (R12a och beslutet 2026-11-08). Boogieman Shot 10656694173962 har ett annat EAN än den skrivna, men samma modell, smak och ingredienslista. Ingen skiljande titel har stöd i källan. Ingen av avvisningarna är uppenbart fel.

## Frågor till David

1. Lägg till ett undantag i spärrlistan för de 6 spärrade id:na (ditt beslut 2026-11-08).
2. Roam 3 Shell White (10656692044042) har en överbliven Default Title med samma SKU och EAN som XL, men med ett annat pris (13 989 mot 13 999 kr) och lager 1. Den bör städas i Shopify.
