# Granskning k_03a (hjälmar) och k_04a (belysning), 2026-11-04

Granskare: Opus, endast läsning. Källan hämtades live via Admin API (23 produkter plus 4 redan skrivna produkter för dubblettkontroll). Regler: regler-v1 (v1.6), standard §12 och §16, beslutsloggen, butiksprofilen och LARDOMAR. Maskinläsbart utlåtande: `vag2_skriv/k_utlatande_03_04.json`. Alla rättningarnas före-text träffar exakt en gång (kontrollerat i python).

## Resultat
14 utkast: 10 GODKÄND, 4 RÄTTA, 0 UNDERKÄND. Alla 9 avvisningar är motiverade.

| Nr | Produkt | Dom | Kort skäl |
|---|---|---|---|
| 9302 | Giant Relay MIPS, Gloss Black | GODKÄND | MIPS bara som systemnamn ur källan; skyddsord utelämnade |
| 9303 | Lazer Maze KC, Copper | RÄTTA | ASTM står i källan, men "enligt tillverkaren" stod två gånger för samma påstående (R5); tas bort i specifikationen |
| 9304 | Limar Air Stratos, Midnight Black Bronze | RÄTTA | Källan säger bara att AirFit "ger komfort", inte att det är ett justeringssystem (R1); dubbelt "och" i meta |
| 9305 | Limar Delta, Matt Electric Blue | GODKÄND | NTA 8776 ordagrant, en gång som tillverkarens uppgift; storlekarna säljs som varianter |
| 9306 | Limar Tonale, Matt Amaranth | GODKÄND | "extra skydd" utelämnat |
| 9308 | Melon E-Series, Metropolis | RÄTTA | Typordet saknades i SEO-titeln fast det ryms (R7). Synlighetsmeningen är ordagrann och står en gång som tillverkarens uppgift (§16.2) |
| 9309 | AXA Juno Batteri 80 mm | GODKÄND | Webbkällan gäller exakt modellen, se nedan |
| 9310 | AXA Juno E-Bike 50 mm | GODKÄND | "garanterar säkerhet" utelämnat |
| 9311 | AXA Juno E-Bike 80 mm | GODKÄND | Som 9310 |
| 9313 | AXA Nox Sport 12 Lux | GODKÄND | Ljusomfånget återges ordagrant som tillverkarens uppgift |
| 9317 | Bookman Monocle pannlampa | GODKÄND | Hör till belysning, se nedan |
| 9318 | Giant Recon+ HL1200 | RÄTTA | Varningsfunktionen stod som fakta; etiketten "Helljus" motsäger tillverkaren |
| 9319 | M-Wave Cobra III | GODKÄND | Spårbart |
| 9322 | SP Connect All-Round 200 lm | GODKÄND | Typordet "cykellampa" finns i källtexten (R7) |

## Särskilda kontroller
- **Standarder för hjälmar:** ingen text påstår EN 1078. Bara ASTM (9303) och NTA 8776 (9305) nämns, och båda står ordagrant i källan. MIPS (9302) nämns bara som systemnamn. Bobbin (9301), där EN1078 står, är avvisad.
- **9304, W&B:** W&B är Limars serienamn "White & Black series" (limar.com/collections/white-and-black-series). Att ta bort det ur titeln ger ingen felaktig uppgift, och handtaget (produktens webbadress) ändras inte. SEO-titeln saknar typord eftersom den annars blir 46 tecken. Det har gjorts likadant för Limar i tidigare batcher.
- **9309, webbkällan:** sidan gäller entydigt den här modellen. axabikesecurity.com/product/axa-juno-battery-80-mm/ har artikel 93929595KB, och butikens SKU är 93929595SC (samma artikelnummer, olika förpackningssuffix). Sidans förpackningsbild heter "juno-batt-on-off-b-l-80mm", vilket motsvarar butikens live-titel "AXA JUNO BATT ON-OFF BL/80MM". Sidan anger baklykta, 80 mm, 2 AAA, på/av-knapp, indikator för låg batterinivå och 50 timmar.
- **9318 (underkänd i b_51):** utkastet är bättre men inte tillräckligt. "Varningslampor för döda vinkeln" är en säkerhetsfunktion som kräver en bakre radar, och det framgår inte att radarn ingår. Funktionen stod ändå som fakta i första meningen, i meta och i Passar för. Rättningen gör att den står en gång, som tillverkarens uppgift. Dessutom kallar butikens källa lägena 800, 400 och 200 lm "Helljus", medan tillverkarsidan (giant-bicycles.com/se/reconplus-hl1200-2024) kallar dem "Low Beam" (halvljus). Det är en motsägelse (R2), så etiketten stryks. Övriga värden stämmer med tillverkarsidan.
- **9317 (pannlampa):** den hör till belysning. Standard §16 och profilen frisläpper "belysning", inte bara cykelbelysning, och taggen avgör inte gruppen. Felen från b_51 är åtgärdade: arbetstermen är borta och det finns inga löften om synlighet eller säker passform. "Uppladdningsbar" står i leverantörens live-titel. **David kan ändå vilja bekräfta att pannlampor ska ingå.**

## Avvisningar (alla motiverade)
- **9301 Bobbin Starling:** butiken har en variant men källan anger två storlekar (S/M 48–54 cm kan vara barnstorlek). Källan har trasig text ("justerbar, justerbar och justerbar") och vikter som inte går ihop. R2, R3 och R6.
- **9307 Giant/Liv Lena:** 46–51 cm är en barnhjälm (R6).
- **9312:** dubblett av 10472255455498 (aktiv, texter-klara, Compactline Front 20 lux, 12 h, 40 m).
- **9314:** källan motsäger sig, kontrollerat live (Compactline mot Greenline, 6 h mot 4 h, 35 m mot 300 m).
- **9315:** dubblett av 10475622400266 (aktiv, texter-klara, Niteline 44-R).
- **9316 Bookman Eclipse:** säljs som "säkerhetslampa" för synlighet och saknar lumen och batteriuppgifter. Konservativt i linje med §12; David avgör.
- **9320:** färgvalet görs i kommentarsfältet vid beställning; beslut från David behövs.
- **9321:** sparkcykel för barn, 4–7 år (R6), och inte belysning.
- **9323:** elcykel med fel tagg. Färgen Ljusgrå går inte att skilja från de redan skrivna Pebble Grey och Willow Mist (båda aktiva och texter-klara).

## Ändrat
Inget i Shopify (endast läsning). Två nya filer skapades: den här och `k_utlatande_03_04.json`.
