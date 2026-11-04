# Granskningsutlåtande k_11e, k_11f, k_11g (Opus, endast läsning)

Datum 2026-11-04. Källan hämtades live via Admin API (bara läsning, 64 produkter: 17 utkast och 47 avvisade, med varianter). Regler: regler-v1.md v1.6, BESLUTSLOGG, butiksprofilen, standard §12, §14, §16, LARDOMAR. Domar per produkt finns i `vag2_skriv/k_utlatande_11efg.json` (fält `nr`, `id`, `fil`, `dom`, `rattningar`, `skal`, och för RÄTTA även `regel` och `allvarlighet`). Varje före-text förekommer exakt en gång i sitt fält (kontrollerat i python).

## Resultat

| Batch | Utkast | GODKÄND | RÄTTA | UNDERKÄND |
|---|---|---|---|---|
| k_11e | 9 | 4 (9915, 9917, 9918, 9920) | 0 | 5 (9907–9911) |
| k_11f | 5 | 2 (9946, 9948) | 3 (9943, 9947, 9949) | 0 |
| k_11g | 3 | 2 (9952, 9964) | 1 (9953) | 0 |
| Summa | 17 | 8 | 4 | 5 |

## Huvudfynd

1. **Go Walker 9907–9911 underkänns som grupp.** Enligt webbkontrollen (v1.6) är Go Walker stavgångsstavar i fasta längder 105–125 cm. Gigantti anger tillverkarnummer Gy231105, som är samma som vår SKU 231105, och Kaufland kallar dem "Stöcke" (par). Utkasten har tre fel. (a) "Go Walker" står först i titeln, men det är ett modellnamn och inget typord (R7). Fem längder av samma produkt får dessutom tre olika typord: träningsstav, vandringsstav och promenadstavar. Singular och plural blandas också, så kunden får motstridiga besked om antalet stavar. (b) Utkasten säger "justerbar längd" (9907, 9911), men det motsägs av att varje längd säljs som en egen artikel (R2). (c) 9910 säger att staven används för styrketräning på gym. Det är fel och skulle ha nått kund. **Gör om:** använd typordet "Promenadstavar" i alla fem, som källan i 9909/9911 och webbkällan, och skriv titeln som "Promenadstavar Gymstick Go Walker, NNN cm, Svart och Vit". Skriv bara längd, färg och användning för promenad/stavgång, och lägg webbkällan i att_bekrafta.
2. **9949 Peltonen:** varianterna "195 och 202" stod utan enhet. Peltonens katalog 2021–22 anger längderna i cm, så raden rättas till "Längd: 195 och 202 cm". Webbkällan ska läggas i att_bekrafta. Första meningen har också fel numerus ("skidorna … är en lätt träningsskida"). Jag rättade inte den, eftersom ett fält bara kan ha en rättning. Byggaren kan ändra den för hand eller lämna den.
3. **9943 Limar Argo:** vikten 26 g är bekräftad av Bike24, där tillverkaren anges som källa, och av Limars egen sida. Påståendet "näskudde med högt grepp" är ett greppåstående, så det ska stå med "enligt tillverkaren" (R5).
4. **9947:** i metan står "bröstrem för upp till 165 cm", men källan säger att måttet gäller bröstomfånget. "tablets" ändras till "surfplattor". **9953:** "blåsvartrutigt konstläder", eftersom konstläder är neutrum.
5. **Granskade punkter som godkändes:**
   - 9964: typordet Stuntsparkcykel följer den redan skrivna systern (b_skriv_23) och källans "sparkcykel" (R7). Lastgränsen 100 kg står på en svensk rad med etikett (R4).
   - 9948: längdskidbindningen är inte säkerhetskritisk i R6-mening och står inte i profilens lista.
   - 9946 och 9947: inga hälsoord. "Mäter hjärtfrekvensen" anger en funktion.
   - 9920: "Latsdragstång" behålls enligt R7. Stavningen "Latsdragsstång" vore normal svenska och är ett möjligt stavningsbeslut för David.
   - 9915 och 9917: tunna källor med kort meta enligt §14.

## Avvisningar (47)

Alla avvisningar är motiverade utifrån egen källa och nuvarande regler, och ingen behöver ändras till godkänd i den här granskningen. Fem grupper:

- **Varianter som titeln inte förklarar (R3), avvisning kvarstår:** 9904, 9906, 9913, 9914, 9922, 9925, 9927, 9940.
- **Hälso-, stöd- eller skyddsprodukter (R5/R6), kvarstår:** 9913, 9930, 9931, 9937, 9941, 9942. Avvisningarna gäller kategorin, inte bara tunn källa.
- **Barn, kemikalie, trasig källa eller säkerhetsdel, kvarstår:**
  - barnprodukter: 9951, 9954, 9955–9957, 9960–9962
  - kemikalie: 9958
  - trasig källa: 9959, 9945, 9963
  - spegel som är synlighets- och säkerhetsnära: 9944. Den kan webbkontrolleras senare, men det är låg prioritet.
- **Bärande delar utan lastgräns:** 9903, 9905, 9912, 9926, 9929. Jag sökte efter 9926 Premium Chin Up Bar (61006) och hittade ingen entydig webbkälla, bara andra Gymstick-stänger. Avvisningen kvarstår.
- **Strikt avvisade för tunn källa eller oklar typ, där v1.6 kan rädda produkten (Gymstick):**
  - **9928 Pro Pump Set 20 kg (61057PU):** webbkällor stämmer överens. Setet innehåller en vadderad stång på 140 cm, skivorna 2 × 5, 2 × 2,5 och 2 × 1,25 kg, 30 mm hål och snabblås. Källor: [Elgiganten](https://www.elgiganten.se/product/sport-fritid/sport-fitness/traningsutrustning-tillbehor/gymstick-pro-pump-set-20-kg-skivstangset/259157), [Decathlon](https://www.decathlon.ch/en/p/mp/gymstick-pro-pump-dumbbell-set-20-kg-with-140-cm-padded-bar/4f4c6004-dad3-4b47-b81d-2527ef680b9a/c1). Skälet "okänt innehåll" gäller alltså inte längre. **Rekommendation:** gör ett nytt utkast med webbkälla.
  - **Sannolikt samma läge, inte kontrollerat en och en:** 9936 och 9938 (pump-set), 9932, 9933, 9934, 9935 och 9939 (avvisade för "oklar produkttyp"), samt 9901, 9902, 9916, 9919, 9921 och 9924 i k_11e. För många av dem saknas notering om att webben har sökts. Ingen av avvisningarna är fel enligt reglerna före v1.6, men de bör gå en runda till med webbsökning, främst på återförsäljarsidor eftersom gymstick.com svarade 403 på direkt hämtning.
  - 9916 kallas "nära dubblett av 9917", men produkterna har olika SKU och pris (61156, 499 kr, mot 61246, 399 kr). Avvisningen bör motiveras med tunn källa, inte med dubblett.

## Webbkällor
- Go Walker: https://www.gigantti.fi/product/urheilu-ja-vapaa-aika/telttailu-ja-retkeily/gymstick-kavelysauva-go-walker-kavelysauvat-105-cm/258498, https://www.kaufland.de/m/~1391589/
- Limar Argo: https://www.bike24.com/p2671692.html, https://us.limar.com/products/argo
- Peltonen Acadia: https://cdn.shopify.com/s/files/1/2247/3993/files/Peltonen_collection_2021-22.pdf
- Gymstick Pro Pump Set: se ovan

Ingenting ändrades i Shopify.
