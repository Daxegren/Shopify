# Granskningsutlåtande k_02e (Romet-cyklar och SOKE City), 2026-11-04

Granskare: Opus, bara läsning. Källan hämtades live via Admin API (`hamta_produkter` och varianter) för alla 25 produkter i `k_02e_in.json` och för de skrivna jämförelseprodukterna 10656692175114, 10507259478282, 10507443044618 och 10462192173322. Jag sökte också i butiken på titel (Jubilat, City, Orkan, Wagant, Jolene). Ingenting skrevs till Shopify.

Underlag: `vag2_skriv/k_02e_utkast.json` (8 utkast), `vag2_skriv/k_02e_avvisade.json` (17). Domarna i maskinläsbar form finns i `vag2_skriv/k_utlatande_02e.json`. Rättningarna har tillämpats på en kopia. Varje före-text träffar exakt en gång. `skrivfil_kontroll.py` gav 0 fel och `kontrollera_produkttext.py --meta-min 70` gav 0 fel och 0 varningar.

## Domar (8 utkast)

| Nr | Id | Dom | Kort |
|---|---|---|---|
| 9201 | 10472332919050 | GODKÄND | Allt finns i källan. Se dubblettnoten nedan om 10507442946314. |
| 9202 | 10472294580490 | GODKÄND | Allt finns i källan (Altus, 21 växlar, skivbromsar, 13,7 kg, fästpunkter). |
| 9203 | 10494855971082 | GODKÄND | Varianten S / purple stöder både S och lila. Ingen dubblett av Orkan D "Vit och Lila", som har annan färg, SKU och pris. |
| 9210 | 10472294514954 | GODKÄND | "Wagant 0" i källan är kopierad från Wagant 0-texten. Utkastet använder bara live-titelns "Wagant" och påstår inget modellnummer, vilket är rätt. |
| 9211 | 10471091470602 | GODKÄND | SEO-titeln utan färg godtas. Med ", Grön" blir den 44 tecken, och märket ska vara kvar (R12). Butiken har ingen annan Jubilat Classic, så SEO-titeln krockar inte med någon annan. |
| 9214 | 10472281932042 | RÄTTA | Metan: "21 växlar med Shimano Acera" ändras till "21 växlar, Shimano Acera-bakväxel". Bara bakväxeln är Acera; framväxeln FD-TY510 är Tourney. |
| 9224 | 10515741245706 | RÄTTA | Typordet "scooter" ändras till "sparkcykel" i alla fält. Etiketten "Maximal ryttarbelastning" ändras till "Maximal belastning". |
| 9225 | 10572593824010 | RÄTTA | Typordet "scooter"/"stadsscooter" ändras till "sparkcykel (för stadskörning)". Lastgränsen tas bort ur metan och står kvar en gång i specifikationen. |

### Särskilda frågor

- **Typord för SOKE City (9224/9225).** Sparkcykel ska gälla. Frågan avgjordes redan i `vag2b_utlatande_49_50.md`: "scooter" betyder på svenska normalt en moped och ersattes med sparkcykel i alla fält. Det stämmer med produkttypen och taggen Sparkcyklar och med alla redan skrivna SOKE-texter i `b_skriv_23.json` (Tricksparkcykel och Stuntsparkcykel SOKE EVO). Enligt R7 får en entydig översättning av ett engelskt typord användas när butikens live-ord har den, och "Sparkcyklar" finns i butiken. Produkterna väger 3,9–3,96 kg och har handbroms, så de är inte motordrivna.
- **Märket SOKE eller Soke (R8).** Jag behåller "SOKE" som i de cirka 20 redan skrivna SOKE-texterna, i live-titlarna och i taggen. Att bara dessa två skulle få "Soke" skulle splittra märkesfamiljen i butiken. R8 säger ordagrant "aldrig versaler", och källtexten skriver "Soke City". Det är därför ett beslut för David (se nedan). Skriptet kontrollerar inte SOKE, eftersom märket saknas i profilens `marken`.
- **"Unga och vuxna" (9224).** Det är ingen barnprodukt. Källan säger "både unga och vuxna", lasten är 100 kg och styrhöjden 88–98 cm. 9225 anger en förarhöjd upp till 185–190 cm. R6 gäller alltså inte.
- **Lastgräns (R4).** Båda produkterna har en ren svensk rad med etikett och enhet, så värdet får stå en gång med "enligt tillverkaren". Ordet "ryttarbelastning" är maskinöversatt och kortas till "Maximal belastning" med samma värde och enhet. Värdet ska inte upprepas i metan, som i praxis från 49_50.
- **Faktakoll på nätet (v1.6).** Inget utkast lägger till uppgifter från webben, så det fanns ingen webbkälla att granska. Ingen uppgift behövde hämtas för att texterna ska stämma.
- **Leveranstidsmeningen (R13).** Ingen av de åtta har taggen "På beställning", och ingen har meningen. Det är rätt.

## Avvisade (17): alla avvisningar är motiverade

- **9204–9206 Panda (R6).** Källan säger själv "barncykel", "barn mellan 125/135 och 155 cm" och "barnsäkerhet".
- **9215–9222 ungdomscyklar (R6).** Källorna säger "mountainbike för unga" och "ungdoms-mountainbike" (Jolene 6.0, ramstorlek från 148 cm), "mountainbike för pojkar" och "första cykel" (Rambler R6.0 blå-grön), "ditt barns första riktiga mountainbike" (R6.0 svart-orange-röd) och "Rambler R6.1/R6.2 ungdomscykel" (9218–9222, ramstorlek från 140 cm). Barn- och ungdomscyklar avvisades på samma sätt i k_4_5, k_6_9 och k_10_12. Profilens `utanfor_tills_vidare: barn` omfattar dem tills David beslutar annat. 9221 och 9222 är dessutom samma modell, färg och pris (26170271-A och -E, 7 419 kr).
- **9207 Orkan M grå-röd (R12a).** Live har SKU 28190093-A för 6 549 kr. Den skrivna och aktiva 10656692175114 har 28190093-B, "Grå och Röd" och samma pris. Det är en dubblett.
- **9212 Wagant 0 grågrön (R12a).** Live har 28210558-A för 8 949 kr. Den skrivna och aktiva 10507259478282 har 28190557-A, är grågrön och kostar lika mycket. Det är samma modell och färg; bara ramstorleken skiljer. Det är en dubblett.
- **9223 Jolene 7.2 mörkröd-orange (R12a).** Live har 27170076-A för 8 679 kr. Den skrivna och aktiva 10507443044618 har 27190075-A, "Mörkröd och Orange" och kostar 8 699 kr. Det är samma modell och färg. Källan och live-titeln är dessutom på engelska. Det är en dubblett.
- **9208 Orkan M svart-guld (R3).** Varianterna är L / black och XL / black, och ingen guldfärg finns i källan. Titeln stämmer alltså inte med källan. Avvisningen räcker på R3. "Trolig dubblett av 9214" är inte belagd (andra SKU:er), men den påverkar inte domen.
- **9209 Wagant 7 och 9213 Wagant 1 (R3).** Varianterna har olika pris (11 309/9 839 kr och 8 549/7 439 kr), vilket jag har bekräftat live.

## Observation till koordinatorn

- Butiken har en andra aktiv **"Damcykel ROMET Jolene 7.1, 27.5" vit-blå"** (10507442946314, SKU 27190282-B, 7 529 kr). Den finns inte i någon batch. Det är samma modell och färg som 9201. Skrivs 9201 ska den andra avvisas som dubblett när den dyker upp (R12a). Den andra har en renare källa (Tourney/Altus, "Cykels vikt: ca 15 kg"), men enligt R1 får de uppgifterna inte föras över till 9201.
- SOKE City finns också i vitt, rosa och grönt som utkast i butiken (DRAFT, inte aktiva). Färgen i SEO-titeln behövs därför för att titlarna ska vara unika.

## Beslut för David

1. **Märkesstavning SOKE eller Soke.** R8 säger att versaler aldrig ska användas, men cirka 20 skrivna texter, live-titlarna och taggen använder SOKE.
   - Alternativ A: lägg till SOKE som undantag i profilen. **Rekommenderas**, eftersom det inte kräver någon omskrivning och ger en enhetlig märkesfamilj.
   - Alternativ B: skriv om alla SOKE-texter till Soke.
   - Om inget beslutas står SOKE kvar, vilket avviker från R8 men är enhetligt.
