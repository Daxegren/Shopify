# Granskningsutlåtande k_47b7, lyfta Gymstick- och övriga produkter (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där. Inget har committats. Produkterna lästes live med `shopify_api.py` (ShopifyKlient). `verifiera_butik` gav BEST OF SPORTS. `mcp__Shopify__*` användes inte. Underlaget var CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08, LARDOMAR, butiksprofilen, `c_granskarprompt.md` samt praxis och format från `k_utlatande_43`.

Båda utkasten är ACTIVE med lager > 0, och ingen av dem har taggen På beställning. Före rättning gav `skrivfil_kontroll.py` 0 fel och 1 varning: den cirkulära inledningen i metatexten för 48902. Efter rättning gav den 0 fel och 0 varningar. Standardblocket är exakt rätt i båda utkasten. Titlarna har högst 42 tecken och högst 1 kommatecken. SEO-titlarna har högst 35 tecken. Metatexterna är 130–144 tecken och innehåller verb. Avsnittet "Passar för" finns i båda. Varje rättning är ETT sammanhängande före/efter-par per fält, och varje före-text förekommer exakt en gång i utkastet (kontrollerat i python).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_47b7.json`.

## Resultat: 0 GODKÄND, 1 RÄTTA, 1 UNDERKÄND

| nr | id | fil | dom | rättade fält / skäl |
|---|---|---|---|---|
| 48901 | 10581106000138 | k_47b7_utkast.json | UNDERKÄND | Exakt dubblett, se nedan |
| 48902 | 10581104853258 | k_47b7_utkast.json | RÄTTA | meta, html |

## 48901 Exercise Ball 65cm: UNDERKÄND

Produkten har samma EAN, 6430016901505, som den redan skrivna aktiva produkten 10411728240906 "Träningsboll Gymstick, 65 cm, Svart". Den produkten har SKU GYM62010, taggen texter-klara och lager 1. Enligt BESLUTSLOGG 2026-11-08 och R12a skrivs exakta dubbletter av andra aktiva annonser inte, eftersom lagret först måste flyttas. Källorna säger dessutom emot varandra om färgen: tillverkaren anger Graphite grey och den skrivna annonsen anger Svart.

I övrigt stämmer texten med https://www.gymstick.com/exercise-ball.html (SKU 620-X, EAN stämmer, PVC, 65 x 65 x 65 cm, 1,24 kg, handpump och träningsguide). Lastgränsen på 100 kg, "rehabilitering" och "anti-slip" är rätt utelämnade. Utkastet kan alltså användas om David väljer att behålla den här annonsen i stället.

## 48902 Barbell Pad: RÄTTA

Produkten har SKU 61003, EAN 6430062511635 och lager 923. Det finns ingen tillverkarsida. Bygghemma.se (Gy61003, samma EAN) anger gjutet skumgummi, svart, nackspår och att kudden kläms runt stången samt används vid squats, lunges och hip thrusts. Det täcker alla uppgifter i utkastet (v1.6/v1.7), och formuleringen "enligt återförsäljaren" är korrekt. Den är inte en dubblett: Barbell Pad Pro (61253) och Kraftmark Barbell Pad (KM10026) är andra artiklar. Skydds-, komfort- och tjockleksord är rätt utelämnade.

- **meta**
  - Före: "Barbell Pad från Gymstick är ett nackstöd av gjutet skumgummi med nackspår. Den används vid squats, lunges och hip thrusts. Artikelnummer 61003."
  - Efter: "Barbell Pad från Gymstick kläms runt skivstången och är gjord av gjutet skumgummi med nackspår. Den används vid squats, lunges och hip thrusts."
  - Skäl: "nackstöd" är ett subtilt stöd- och skyddslöfte som inte står i källan, och inledningen var cirkulär (skriptvarning).
- **html**
  - Före: `<li>Montering: Klämmas runt stången</li>`
  - Efter: `<li>Montering: Kläms runt stången</li>`
  - Skäl: grammatikfel.

## Avvisade (k_47b7_avvisade.json, 12 st)

Ingen avvisning är uppenbart fel, så ingen produkt lyfts ur. Skälen:

- **Utan entydig källa:** Armbågsstöd 1.0, Back Support 2.0, Barbell Pad Pro och Justerbart handtag saknar en entydig källa för exakt SKU/EAN. Den egna texten består bara av löften.
- **EAN stämmer inte:** för Horisontell stång stämmer EAN inte med tillverkarsidan, och sidan beskriver 4-station.
- **Bärande del, tunn källa:** Vevlager och Stödhjul har tunn eller trasig källa och saknar lastgräns.
- **Ingen träff på EAN:** Skridskoskidor Acadia SK 21.
- **Kemikalie med farovarning:** Grease remover. Märkningen kan inte kontrolleras.
- **Motsägande källor:** Korkstart och Cykelklocka (5 mm mot 35 mm).
- **För få fakta:** Dricksflaska Beany har färre än två fakta.

## Fråga till David

Exercise Ball 65 cm finns som två aktiva annonser med samma EAN: 10581106000138 (lager 408, utan text) och 10411728240906 (lager 1, skriven). Vilken annons ska behållas? Lagret behöver flyttas innan den andra arkiveras.
