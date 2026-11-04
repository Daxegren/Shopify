# Granskning väg 2, elcyklar och cyklar k_01a (2026-11-04)

Oberoende granskning (Opus), endast läsning mot Shopify. Underlag: `vag2_skriv/k_01a_utkast.json` (21 utkast) och `vag2_skriv/k_01a_avvisade.json` (4 avvisade). Regelbok v1.4, BESLUTSLOGG, butiksprofil BEST OF SPORTS, standard §16, lärdomen 2026-11-03 om växelgrupper och de senaste utlåtandena (k_16_17, k_01c) som praxis. Alla 25 produkter hämtades live på nytt via Admin API (`shopify_api.hamta_produkter` + variantfråga); alla är ACTIVE och har ännu inte någon SEO-titel eller meta. Inget ändrat i Shopify.

Formatreglerna är redan testade av skript. Kontrollerat här: varje påstående mot produktens egen källa, varianter och pris (R3), färg mot SKU och variantnamn, lastgräns, räckvidd och batteri (R4, §16), typord (R7), dubbletter mot andra batcher (R12a). Beställningsmeningen finns på exakt de 15 produkter som har taggen "På beställning". "Enligt tillverkaren" högst två gånger per text i alla utkast. Rättningarna har provkörts med `bygg_m_skriv.py` (till scratchpad): 0 problem, varje "före" träffar en gång.

**Resultat:** 16 GODKÄND, 4 RÄTTA, 1 UNDERKÄND. Alla 4 avvisningar är motiverade.

| nr | id | dom | före → efter / skäl |
|---|---|---|---|
| 9001 | 10472281080074 | GODKÄND | Allt spårbart i egen källa. Blå stöds av SKU (ADO-A20PRO-BLUE). 18 kg står i egen källa; 28,5 kg i 9003/9004 är syskondata (R1) – tas upp som fråga. "Automatiskt växelval via motorn" motsäger inte "Antal växlar: 1". Inte dubblett av 9003 (annan SKU, 40 mot 50 Nm). |
| 9002 | 10472307065098 | GODKÄND | Bromsraden: "Bromsar: hydrauliska skivbromsar" är entydig del av en trasig rad (R2). "150 kg" i skräpraden är ett eko av längdraden, inte en etiketterad lastuppgift; den rena raden "Lastkapacitet: 120 kg" får stå (R4). Meteor Grey stöds av SKU (GREY). |
| 9003 | 10665232105738 | GODKÄND | Spårbart, modellår 2026 i källan, Blå stöds av SKU. |
| 9004 | 10612594475274 | GODKÄND | Som 9003, SKU GREY. Separat produkt, inte dubblett. |
| 9005 | 10656694272266 | GODKÄND | Spårbart; IPX6 och 1,7 s rätt utelämnade. Polar Blue stöds av SKU. |
| 9007 | 10487987011850 | GODKÄND | Spårbart. SRAM SX utelämnad – försiktigt och tillåtet. Två varianter, samma pris. Antracit/Röd mot "gray": ingen motsägelse. |
| 9008 | 10472304771338 | GODKÄND | Gravelbike → Gravelcykel tillåtet (R7): entydig översättning, butikens live-ord (9010/9011) och produktens egen tagg. Sora finns bara mekaniskt. |
| 9010 | 10472304541962 | GODKÄND | GRX610 rätt utelämnad (lärdom 2026-11-03). Grigio Opaco = "gray". |
| 9011 | 10472304804106 | GODKÄND | GRX610 rätt utelämnad, fyra varianter samma pris. Inte dubblett av 9012. |
| 9012 | 10475622007050 | GODKÄND | "SRAM Rival AXS" är elektroniskt; att grupp och bromsmodell utelämnas är rätt. |
| 9014 | 10468708614410 | RÄTTA | **titel:** `El-Lastcykel` → `El-lastcykel`; **seo_title:** `El-Lastcykel` → `El-lastcykel`. Typordet är ett ord (som live-titeln och metan). Fakta och lastkapacitet 100 kg (låda) + 100 kg (förare) spårbara och rätt återgivna. |
| 9015 | 10472348188938 | RÄTTA | **html:** `<li>Dig som behöver en lastcykel för företag eller familj</li>` → `<li>Dig som vill ta med ditt husdjur på vardagsresorna</li>`. R1-fel: "företag och familjer" står bara i syskonet 9014:s källa; Flex Dogs egen källa talar om "din fyrbenta vän" och "ditt husdjur". **titel/seo_title:** `El-Lastcykel` → `El-lastcykel` som 9014. |
| 9017 | 10494946312458 | UNDERKÄND | R3: titeln säger Gem Blue men enda varianten har SKU ENGWE_E26-GREEN och källan nämner ingen färg. Övrigt spårbart; kan skrivas oförändrat om färgen bekräftas. |
| 9018 | 10502527910154 | GODKÄND | Spårbart, Svart stöds av SKU. |
| 9019 | 10541371752714 | GODKÄND | "Elcykel" står i källtexten, så bytet från "Electric bike" är tillåtet (R7). Två varianter samma pris, ingen färg/storlek låst. |
| 9020 | 10472292778250 | GODKÄND | Spårbart; IP-klassning rätt utelämnad. Grön bara i titeln, enda variant (praxis). |
| 9021 | 10472296251658 | RÄTTA | **html:** `<li>Antal växlar: 1</li>` + radbrytning → (tas bort). R2: "Shimano E5" och "Antal växlar: 1" går inte ihop entydigt; namnet står kvar. **meta:** `SR Suntour-luftgaffel, Shimano BR-MT410 och däck` → `SR Suntour-luftgaffel, hydrauliska bromsar och däck` (metan sade inte att BR-MT410 är bromsar; 143 tecken). |
| 9022 | 10472295956746 | GODKÄND | Shimano Deore Shadow+ får stå: Deore finns inte elektroniskt, står inte på lärdomens lista och texten påstår inget om mekanik (praxis 7147). |
| 9023 | 10472250769674 | GODKÄND | Spårbart; 25 km/h och "under ideala förhållanden" står ordagrant i källan. |
| 9024 | 10676722008330 | RÄTTA | **html:** `, 800 W toppeffekt` → (tas bort). Toppeffekten står bara i säljande löptext; specifikationen anger 250 W. Bredvid 250 W kan den läsas som ett påstående om effektklass (§16.4). Eagle 90 Transmission rätt utelämnad. Mars Dust mot "Red": samma kulör, originalnamnet behålls. |
| 9025 | 10470923141386 | GODKÄND | Spårbart; laddtid står i källan och har "enligt tillverkaren". Pakethållarens 20 kg i löptext rätt utelämnad (R4). |

## Avvisningar (k_01a_avvisade.json)

| nr | id | bedömning |
|---|---|---|
| 9006 | 10472250343690 | **Motiverad.** Titeln säger "centrumbatteri", källan säger skydd för "mittmotor" (R3). Koordinatorn bör rätta titeln före text. |
| 9009 | 10541368377610 | **Motiverad.** Två varianter med olika pris (28 919 kr och 25 149 kr) och variantfärgen "green" mot titelns Grigio Opaco (R3). |
| 9013 | 10462150525194 | **Motiverad.** Barntransport med säkerhetsbälten (R6, "barn" i `utanfor_tills_vidare`) och trasig, maskinöversatt källa (R2). |
| 9016 | 10502527877386 | **Motiverad.** Källan beskriver E26, inte E26 ST (genomstegsram), och ST-specifikationerna går inte att belägga (R3). |

## Kontroll av utkastarens att_bekrafta-punkter
- **Växelgrupper utelämnade (9007, 9010–9012, 9024):** rätt. GRX610, Rival AXS och Eagle 90 Transmission finns som eller är elektroniska; SRAM SX hade kunnat stå, men att utelämna den är tillåtet.
- **9017 (GREEN mot Gem Blue):** underkänd, se ovan.
- **9024 (Red mot Mars Dust, 800 W):** färgen godtas; 800 W stryks.
- **9001 mot 9003/9004 (18 mot 28,5 kg):** båda står i respektive egen källa och får stå; frågan går till David.
- **9022 (Deore Shadow+):** godkänd.
- **9021 (Shimano E5, "1 växel"):** antalet stryks.
- **9002 (bromsrad):** godkänd.
- **9008 (Gravelbike → Gravelcykel):** godkänd.

## Sammanställning av återkommande fynd
1. **Fakta från syskonprodukt (R1):** 9015 lånade "företag eller familj" från 9014, och utkastarens att_bekrafta påstod att det stod i källan. Lika källtexter i en produktfamilj gör att utkastaren kopierar mellan dem. Förslag: låt kontrollskriptet varna när en "Passar för"-punkt har ord som saknas i produktens egen källa.
2. **Färg som bara finns i titeln:** fungerar när SKU eller variantnamn stöder färgen (9001–9005, 9018). Vid motsägelse mellan SKU och titel (9017) underkänns produkten. SKU-jämförelsen kan automatiseras.
3. **Växelgrupper:** utkastaren följde lärdomen konsekvent. Tidigare skrivna produkter följde den inte: 8832 har "GRX610" i titeln och 8899 "SRAM 90 Eagle Transmission" i texten. Tas upp som fråga.
4. **Prestandauppgifter ur löptext** (800 W toppeffekt) bör strykas när specifikationsraden säger något annat.
5. **"Enligt tillverkaren" på sammanslagna rader** ("Räckvidd, vikt och lastkapacitet: …") håller gränsen på två per text. Raderna blir dock långa. Det är godtagbart, men det är en stilfråga för David.

## Öppna frågor till David
1. **ADO Air 20 PRO:** 9001 anger 18 kg och 9003/9004 (2026) anger 28,5 kg för i övrigt liknande cyklar. 9005 anger också 28,5 kg. Ska vikten stå kvar så som den står i varje produkts källa, eller strykas tills leverantören bekräftat den?
2. **9017 Engwe E26:** är varianten Gem Blue eller grön (SKU GREEN)?
3. **Växelgrupper i redan skrivna texter (8832 GRX610, 8899 Eagle 90 Transmission):** ska de rättas så att de följer lärdomen 2026-11-03?
