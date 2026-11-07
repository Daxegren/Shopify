# Regelförslag 2026-11 (granskarregler, G)

Skapad 2026-11-06. **Förslag till David; `regler-v1.md` är inte ändrad.** Underlag: `shopify-sync/status/regeltester-matning.md` (2 496 rättningar i 1 196 produkter, 2 781 bedömningar). Förslagen gäller de rättningstyper som inte går att kodifiera utan att larma på godkända utkast. Varje förslag har en provisorisk beteckning F1–F10 (inte R-nummer, för att inte krocka med regelbokens numrering). Kod G = granskare. Där ett förslag kan bli ett test (T) senare står vad som krävs.

| Förslag | Gäller | Rättningar i facit | Kan bli test (T)? |
|---|---|---:|---|
| F1 Metabeskrivning med verb | R11 | 114 | Ja, om regeln blir entydig |
| F2 Butikens ord i alla fält | R7 | 754 (ordval 468, typord i titel 286) | Delvis, via ordlista i profilen |
| F3 Slutna listor över ord som kräver "enligt tillverkaren" | R5 | 87 + 42 + 23 | Ja, via ordlista |
| F4 "Dig som"-rader | R2, R5 | 41 (rad borttagen) + 52 ("enligt tillverkaren" tillagt eller borttaget) | Delvis |
| F5 Specifikationsrader | R1, R2 | 165 | Delvis |
| F6 Passform och kompatibilitet | R1, R5 | 193 | Nej |
| F7 Tal och mått | R1, R3 | 117 + 32 | Delvis (decimalkomma är redan test) |
| F8 Titel och SEO-titel | R7, R12 | 46 + 32 | Nej |
| F9 Sammansatta ord och en/ett | R7 | 75 | Ja, via ordlista |
| F10 Taggar i utkastfilen | R13 | 12 | Ja, om utkastet bär taggarna |

## F1. Metabeskrivning och första mening ska ha ett verb (förtydliga R11)
- **Förslag:** "R11 (G) gäller även metabeskrivningens första mening: den ska innehålla ett verb (har, ger, väger, mäter, består av, passar …). En ren uppräkning av substantiv ('Hantelstång i svart metall, 35 cm lång med diameter 30 mm') är inte godkänd."
- **Underlag:** 114 rättningar (4,6 %), nästan alla i batcherna k_. Samtidigt godkände granskarna 6,7 % av provdelens godkända utkast (54 av 812) trots att första meningen saknade verb, framför allt metabeskrivningar för hantelstänger och lås. Regeln används alltså olika.
- **Alternativ:** (A) Kräv verb (rekommenderas, enklast att förklara för utkastarna; kontrollen `META_UTAN_VERB` kan då slås på som varning). (B) Tillåt substantivfras i meta men kräv verb i första meningen i texten; då behövs ett undantag i testet.
- **Risk:** Alternativ A ger fler omskrivningar av de ca 6–7 % utkast som i dag godkänns som substantivfras.

## F2. Butikens ord i alla fält (utvidga R7 och profilens `godkanda_typord`)
- **Förslag:** "R7 (G) Typordet i löptext, målgruppsrader och specifikation ska vara samma ord som i titeln. Lånord och engelska typord ersätts med butikens ord enligt profilens `butiksord` (scooter → sparkcykel, power rack → träningsställ, half rack → halvställ, mini bike → minicykel, elliptisk tränare → crosstrainer). Nya ord läggs i profilen, inte i prompter."
- **Underlag:** 754 rättningar (30,2 % av alla) är ordbyten; den största enskilda gruppen är scooter → sparkcykel (ca 175, varav 141 i en batch). Ordlistan finns redan som `butiksord` och `engelska_typord` i `shopify-sync/config/regeltester.json`; testerna `BUTIKSORD` och `ENGELSKT_TYPORD` fångar 148 respektive 62 rättningar och larmar på högst 0,5 % av de godkända.
- **Villkor:** R7 säger att typord bara byts om produktens egen källa använder det nya ordet. Ordlistan ska därför bara innehålla ord där Davids beslut finns; i dag är det ett förslag framtaget ur granskarnas rättningar.
- **Kan bli T:** redan delvis (varning). Läget kan höjas till fel för `BUTIKSORD` när David godkänt ordlistan.

## F3. Slutna listor över ord som kräver "enligt tillverkaren" (förtydliga R5)
- **Förslag:** "R5 (G) Följande ord får bara stå med 'enligt tillverkaren' i samma mening eller rad: slitstark, robust, hållbar, tålig, halkfri, halkskydd, stödjer, skyddar, premium, bekväm, förbättrar, effektiv, BPA-fri, andningsaktiv, fukttransporterande, UPF, ergonomisk, vattentät, smakfri. Ord som inte står i listan men liknar dem utelämnas om källan inte är ordagrann. Listan ligger i profilen och utökas när granskaren hittar nya ord."
- **Underlag:** "enligt tillverkaren" lades till i 87 rättningar och togs bort eller omformulerades i 42; 23 rättningar strök kvalitets- eller säkerhetsord helt. Testet `KVALITETSORD_UTAN_ETV` (18 ord) fångar 55 rättningar med 0,7 % falsklarm som mest.
- **Kan bli T:** redan varning; listan blir facit när David godkänt den. Orden "vattentät", "ergonomisk" och "smakfri" ingår inte i testet i dag (falsklarm 0,5–0,7 % i träningsdelen); de föreslås som G tills fler fall mätts.

## F4. "Dig som"-rader
- **Förslag:** "R2/R5 (G) En 'Dig som'-rad återger bara en uppgift som också står i specifikationen. 'Enligt tillverkaren' sätts på raden bara för kompatibilitet (till exempel 'Dig som har en cykel med 28 tum') eller när uppgiften är ett R5-påstående, aldrig på rena mått. Rader om skydd, hälsa eller prestanda utelämnas."
- **Underlag:** 41 rättningar gäller 'Dig som'-rader som togs bort (i 22 fall hela raden). På sådana rader lade granskarna till "enligt tillverkaren" i 25 rättningar och tog bort det i 27. Rättningarna går alltså åt båda hållen, vilket tyder på att regeln saknas.
- **Kan bli T:** delvis. En kontroll "'Dig som'-rad med kvalitetsord" ingår redan i `KVALITETSORD_UTAN_ETV`.

## F5. Specifikationsrader
- **Förslag:** "R1/R2 (G) Varje rad i specifikationen ska ha en etikett och ett mätbart eller entydigt värde ur en etiketterad rad i källan. Rader vars värde är ett omdöme ('Bekvämt handtag', 'Flexibel, lätt plast'), dubblerar en annan rad ('Finns även i 100, 110 och 120 cm') eller bygger på en trasig eller maskinöversatt källrad utelämnas."
- **Underlag:** 165 rader togs bort (6,6 %). Motiveringarna hänvisar oftast till R2 (trasig eller motsägande källa, ca 41), R4 (lastgräns, ca 24), R7 (ca 15) och R5 (ca 12).
- **Kan bli T:** omdömesvärden i specifikationsrader går att testa med en ordlista (jfr F3); R2 kräver jämförelse mot källan och förblir G.

## F6. Passform och kompatibilitet
- **Förslag:** "R1/R5 (G) Kompatibilitet ('passar Melon-hjälmar', 'passar alla typer av cyklar') skrivs bara om källan anger modell, mått eller storlek; annars utelämnas påståendet. Generella påståenden som 'universell' eller 'passar alla' skrivs aldrig."
- **Underlag:** 193 rättningar (7,7 %) tog bort ett påstående eller en bisats; i granskarnas motiveringar är kompatibilitet och passform en återkommande orsak (ungefär R2 39, R5 20, R4 16 av motiveringarna; räknat före borttagning av dubbletter).
- **Kan bli T:** nej utan jämförelse mot källan; en ordlista ("passar alla", "universell") skulle ge få träffar.

## F7. Tal och mått
- **Förslag:** "R1/R3 (G) Ett tal står likadant i titel, SEO-titel, meta, första meningen och specifikationen, med decimalkomma och enhet med liten bokstav. Hjul-, ram- och däckstorlek anges bara om den finns i källan och gäller alla varianter som säljs (R3). Siffror från syskonprodukter används inte."
- **Underlag:** 117 rättningar ändrade tal eller mått i löptext och 32 i titel eller SEO-titel.
- **Kan bli T:** decimalpunkt och versala enheter är redan test (`DECIMALPUNKT`, `ENHET_FORM`). Att samma tal står på alla ställen går att kontrollera i kod om `fakta`-fältet används; `kontrollera_produkttext.py` har en kontroll (`tal_utan_kalla`) som i dag ger falsklarm (se granskningsutlåtande k_25abcf), så det kräver eget arbete.

## F8. Titel och SEO-titel
- **Förslag:** "R7/R12 (G) Titeln innehåller typord, märke och modellnamn exakt som i källan, och det som skiljer varianten (till exempel 'Forward', 'Aktiv', ', 16 tum,'). SEO-titeln behåller märket om det ryms inom 43 tecken."
- **Underlag:** 78 rättningar kompletterade en titel eller SEO-titel med ord eller mått.
- **Kan bli T:** nej i nuläget. En prototyp "SEO-titeln har tappat märket som titeln har" fångade 0,5 % av rättningarna och larmade på 1,4 % av de godkända i träningsdelen (0 träffar i provdelen) och införs därför inte.

## F9. Sammansatta ord och en/ett
- **Förslag:** "R7 (G) Sammansatta ord skrivs ihop (powerstation, foamroller, universalstorlek, mineralkapslar, stuntsparkcykel) och får rätt genus (en walking pad, ett kosttillskott). Granskaren kontrollerar stavning av alla nya typord mot profilens `godkanda_typord`."
- **Underlag:** 75 rättningar av stavning, böjning eller genus och ytterligare 21 särskrivningar (power station, foam roller, universal storlek, mineral kapslar) bland rättningarna av skiljetecken och mellanslag.
- **Kan bli T:** ja, med en liten ordlista över kända särskrivningar och genus för butikens typord, men underlaget (ca 30 unika fall) räcker inte för att mäta falsklarm på ett tillförlitligt sätt; ordlistan bör byggas först när fler fall samlats.

## F10. Taggar i utkastfilen (processändring för R13)
- **Förslag:** "Utkastfilen får ett fält `taggar` (kopia av produktens taggar vid utkastet). Då kan skrivfil_kontroll.py kontrollera att leveranstidsmeningen finns om och endast om taggen 'På beställning' finns."
- **Underlag:** 12 rättningar gäller leveranstidsmeningen (5 tillagd, 7 borttagen). Skriptet ser i dag inte taggen och kan därför inte testa regeln (regelbokens v1.5 anger att granskaren kontrollerar den).
- **Kan bli T:** ja, direkt när fältet finns.

## Inte föreslaget som regel
- **Stilomskrivning av enskilda meningar** (217 rättningar, 8,7 %): passiv till aktiv, ordföljd, bisatser. Granskarnas motiveringar anger ingen regel; det ser ut som språklig smak. Rekommendation: ingen ny regel, överlåt åt Sonnet-granskaren (billigare än Opus).
- **Versal eller gemen i färgnamn och modellnamn** (EVO/Evo, Orange/orange; 26 rättningar av versal/gemen i löptext och 14 av ord → versaler): rättningarna går åt båda hållen och kan inte reduceras till en regel.

## Beslut som behövs
- F1 (A eller B) och F10 är de två förslag som direkt kan göra ett test till fel eller skapa ett nytt test. F2 och F3 behöver Davids godkännande av ordlistorna innan något test får läget fel. F4–F9 är förtydliganden till granskarna och påverkar inga skript.
