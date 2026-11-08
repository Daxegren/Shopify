# Granskningsutlåtande k_46ovr6, aktiva produkter i tidigare utanför-kategorier (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient; `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan text får faktatext även i tidigare utanför-kategorier), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och `k_utlatande_46ovr3.md`, formatet i `k_utlatande_43.json`. Tidigare avvisningar av samma id lästes (b_25: reflexer, k_11a: kallbadtunna, k_19c: suspensionstränare).

Alla 9 utkast och 15 avvisade är ACTIVE. Ingen av de 9 har taggen På beställning, och ingen har leveranstidsmeningen. Standardblocket är exakt rätt på alla. Titel ≤70 tecken och ≤2 kommatecken, SEO ≤43, meta 106–137 tecken med verb, "Passar för" finns på alla. Titlar, SEO-titlar och metatexter är unika inom batchen och mot övriga utkast- och skrivfiler. De enda träffarna gäller äldre oskrivna utkast för samma produkt (a_5). De är också unika mot butikens titlar (sökning på Isbadkar, Kallbad, Lifeplate, Vibrationsplatta, Foam Roller, Nacksträckare, Argon, Legacy, Suspension och Reflex). Varje rättning är ETT sammanhängande före/efter-par per fält, och varje före-text förekommer exakt en gång i utkastet (kontrollerat i python). De rättade titlarna klarar `format_regler.titel_versaler`.

**Obs före skrivfil:** `skrivfil_kontroll.py` stoppar 7 utkast (47501, 47502, 47504, 47506, 47507, 47508, 47509), eftersom de står på spärrlistorna `utanfor-tills-vidare-2026-11-04` och `tidigare-avvisade-2026-11-04`. Davids beslut 2026-11-08 släpper dem, men en undantagspost i `sparrlista.json` måste läggas till innan skrivfilen byggs. Butiksprofilen listar fortfarande rullskridskor och vibrationsplattor under `utanfor_tills_vidare`. Annars ger skriptet 0 fel och 0 varningar, både före och efter rättning.

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_46ovr6.json`.

## Resultat: 4 GODKÄND, 5 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 47501 | 10588451897610 | k_46ovr6_utkast.json | GODKÄND | – |
| 47502 | 10588451930378 | k_46ovr6_utkast.json | GODKÄND | – |
| 47503 | 10636609224970 | k_46ovr6_utkast.json | RÄTTA | titel, seo_title |
| 47504 | 10636622168330 | k_46ovr6_utkast.json | RÄTTA | titel, seo_title |
| 47505 | 10636624331018 | k_46ovr6_utkast.json | RÄTTA | titel |
| 47506 | 10636632817930 | k_46ovr6_utkast.json | GODKÄND | – |
| 47507 | 10636662571274 | k_46ovr6_utkast.json | RÄTTA | titel |
| 47508 | 10636663521546 | k_46ovr6_utkast.json | RÄTTA | titel |
| 47509 | 10612579139850 | k_46ovr6_utkast.json | GODKÄND | – |

## Löften och påståenden

Alla texter genomsöktes efter hälso-, säkerhets-, skydds-, utvecklings-, prestanda- och kvalitetsord: stabilitet, säker, synlig, skyddar, halkfri, robust, hållbar, slitstark, komfort, effektiv, återhämtning, avslappning, spänning, hållning, rörlighet, cirkulation, stress, sömn, kalorier, tyst, leder och ergonomisk. Inget sådant finns i titel, SEO, meta eller beskrivning. Kvar finns bara ord som står ordagrant i källan och beskriver produkten: "vadderad och andningsbar" (sko), "isolerande lock" och "vadderade fjädrar/handtag". Ingen av dem anger en effekt. Hjärtfelsvarningen på kallbadtunnan är en varning, inget löfte.

## Mönster

- Uppgifterna hör till exakt artikel: SKU och EAN stämmer mot live på alla. Ingen tillverkarsida behövdes för fakta. TRYM-lastgränsen söktes på nätet på SKU och EAN utan entydigt resultat, så "Ej känd" står kvar (v1.10).
- Lastgräns: Lifeplate 1.0 och 4.0 har svenska etiketterade rader (Maximal belastning/användarvikt: 100kg), som återges en gång enligt tillverkaren.
- Varianter: Argon (v1.7 Default Title och v1.8) och Legacy Pro (v1.9, olika pris och lager > 0). Ingen storlek eller färg är låst.
- R9: "med + beskrivande ord" i fyra titlar saknade stor bokstav; "450 liter" ändras till "450 l".
- Avvisade (15): alla avvisningar är riktiga. Skälen är AI-text utan verifierbar tillverkarkälla (Tennis Elbow, Vivid Spike Mat, Fotledsstöd, Ryggstöd), exakta dubbletter (Centuri E100, Kona Ouroboros, Boom Knee Pads x2), oklar produkttyp (NILS/ROWER-COMPACT), tom källa (Zefal), olika pris utan lager eller motsägelse (Giant Defy, Fathom E+), motsägelse i färg (Roddhandtag BLACK/Krom) och massagestolar som inte går att skilja åt. Ingen lyfts.

## Frågor till David

1. Lägg till undantag i spärrlistan för de 7 spärrade id:na (ditt beslut 2026-11-08) och uppdatera `utanfor_tills_vidare` i butiksprofilen.
2. Fila Argon 84 Lady har en överbliven Default Title-variant med samma SKU som 37,5 men 2669 kr (mot 2319 kr). Den bör städas i Shopify. Båda Fila-produkterna har dessutom taggen Damcykel.
3. Kallbadtunnan: hjärtfelsvarningen och vattenvikten (cirka 450 kg) står som Obs-rad ur källan. Godtas det, eller ska de bort?

## Skäl och rättningar per produkt

### 47501 (10588451897610): GODKÄND

Live ACTIVE, Velomarket, lager 10. Sju storleksvarianter 37,5–41 (010621215-xx) à 2319 kr plus en överbliven Default Title med samma SKU som 37,5 (2669 kr), som ignoreras enligt v1.7; samma artikel i storlekar, inget låst (v1.8). Hjul 84 mm/83 A, ABEC 7, chassi 6000-serie aluminium, broms, vadderad och andningsbar sko, klassiskt fästsystem och målgrupp stämmer ordagrant. 'Större stabilitet', 'enklare hantering' och 'lätta' utelämnade. Färg utelämnad (titeln Svart/Magenta, varianterna black). Inte dubblett: 10472238153994 (Argon 84 Lady svart-rosa) är DRAFT med annan SKU.

### 47502 (10588451930378): GODKÄND

Live ACTIVE, lager 6. Fyra storlekar 37–40 med 2319/2309 kr, lager > 0, samma artikel (v1.9); ingen storlek eller färg låst. Ram, high-cut manschetter, spänne/snören/kardborreband, Fila Air Flow-vaddering, 80 mm/82A, ABEC 5, metallaxlar och aluminiumdistanser stämmer. Robust, komfort, stabilitet, kalorier och träningseffekter utelämnade. Övriga Legacy-produkter i butiken är andra modeller (Pro 80 utan Lady, Pro 84, QF, Comp) med andra SKU.

### 47503 (10636609224970): RÄTTA

Live ACTIVE, T000164, EAN 4250663123349, lager 0. Uppgifterna stämmer; 'förbättrar styrka, balans och rörlighet', 'halkfria', 'ergonomiskt', 'stabila', 'supereffektivt' utelämnade. Hängande produkt: ingen lastgräns i källan; granskarens webbsökning på SKU/EAN gav ingen entydig uppgift för exakt modellen (samma utfall som k_19c), så 'Maximal lastgräns: Ej känd' i specifikation och text är rätt enligt v1.10. Rättning: stor bokstav på beskrivande ord i titel och SEO-titel (R9).

**titel**

Före:
```
Suspensionstränare TRYM med dörrankare
```
Efter:
```
Suspensionstränare TRYM med Dörrankare
```

**seo_title**

Före:
```
Suspensionstränare TRYM med dörrankare
```
Efter:
```
Suspensionstränare TRYM med Dörrankare
```

### 47504 (10636622168330): RÄTTA

Live ACTIVE, 101321-00019-0001, EAN 4250663126012, lager 1280. Material, C-kurva, massagepunkter, mått, vikt och färg stämmer. Alla effektord (spänningar, avslappning, hållning, 'känner dig bättre') utelämnade; inga subtila löften. Typordet finns i live-titeln. Rättning: stor bokstav på beskrivande ord (R9).

**titel**

Före:
```
Nacksträckare GS med massagepunkter
```
Efter:
```
Nacksträckare GS med Massagepunkter
```

**seo_title**

Före:
```
Nacksträckare GS med massagepunkter
```
Efter:
```
Nacksträckare GS med Massagepunkter
```

### 47505 (10636624331018): RÄTTA

Live ACTIVE, GSMX-600419-00019-0001, EAN 4250663125879, lager 367. Kapacitet, mått, material/tjocklekar, fem lager, innehåll, vikt 3,8 kg, 1 års garanti och färg stämmer. Hälsopåståenden (muskelvärk, stress, sömn, motståndskraft), 'håller temperaturen', 'hållbart' och badtider utelämnade. Obs-raden (vattenvikt cirka 450 kg och hjärtfel/läkare) är en varning ur källan, inget löfte; behålls i linje med praxis för varningsrader (allergen/azorubin). Ej dubblett: RecoPod (63085) är annan artikel. Rättning: enheten skrivs 'l' som på skrivna syskonet (Isbadkar Gymstick RecoPod, 420 l), så att formatregeln inte gör 'Liter' versal (R9).

**titel**

Före:
```
Kallbadtunna Maxxus Isbadkar XL, 450 liter
```
Efter:
```
Kallbadtunna Maxxus Isbadkar XL, 450 l
```

### 47506 (10636632817930): GODKÄND

Live ACTIVE, T000196, EAN 4250663124346, lager 0. Användningsområden, intensitet via kroppsvikt, EPP, 15 x 30 cm och ca 240 g stämmer. Effektpåståenden (muskelspänningar, rörlighet, näringsämnen, balans/stabilitet) utelämnade enligt v1.11. Typordet Foam Roller ur live-titeln; massagerulle i specifikationen. Ingen annan aktiv TRYM-rulle.

### 47507 (10636662571274): RÄTTA

Live ACTIVE, GSMX-600164-00019-0001, EAN 4260244711070, lager 0. Platta, frekvens, två styrkesteg, 3 program plus manuellt, två LED-skärmar, panel/fjärrkontroll, fyra vadderade fjädrar, gummiband, mått och vikt stämmer. Lastgräns: svensk etiketterad rad 'Maximal belastning: 100kg', en gång enligt tillverkaren (R4). 'Tyst drift', 'bra vibrationer' och effekter utelämnade. Övriga Lifeplate-modeller är DRAFT med annan SKU. Rättning: stor bokstav på beskrivande ord (R9).

**titel**

Före:
```
Vibrationsplatta Lifeplate 1.0 med två gummiband
```
Efter:
```
Vibrationsplatta Lifeplate 1.0 med Två Gummiband
```

### 47508 (10636663521546): RÄTTA

Live ACTIVE, GSMX-600184-00019-0001, EAN 4260244716044, lager 0. Motor DC 200 W plus 40 W, frekvensområden, platta, tre program plus manuellt, display/radiosändare, två träningsband, mått och vikt stämmer. 'Maximal användarvikt: 100kg' är svensk etiketterad rad, en gång enligt tillverkaren. Uppvärmning, återhämtning, 'snäll mot leder' och 'effektiv' (även i nuvarande SEO-titel) utelämnade. Rättning: stor bokstav på beskrivande ord (R9).

**titel**

Före:
```
Vibrationsplatta Lifeplate 4.0 med radiosändare
```
Efter:
```
Vibrationsplatta Lifeplate 4.0 med Radiosändare
```

### 47509 (10612579139850): GODKÄND

Live ACTIVE, Velomarket, SKU 427, EAN 7350051864278, lager 1. Fästning på arm, ben, väska och barnvagn och vit färg stämmer; synlighets- och säkerhetsord (360 grader, säkrare, syns i mörkret) utelämnade enligt v1.9. Tunn källa men samma nivå som skrivna syskon 426 (svart) och 428 (rosa), som har andra EAN; ingen dubblett. Titel och SEO är unika mot syskonen. Tidigare avvisad i b_25 som säkerhetsprodukt; släppt av beslutet 2026-11-08.
