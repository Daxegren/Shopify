# Granskningsutlåtande k_12a och k_12b (Opus, endast läsning)

Datum 2026-11-04. Källan hämtades live via Admin API, bara läsning: 19 produkter med varianter, streckkoder och taggar. Regler: regler-v1.md v1.6, BESLUTSLOGG, butiksprofilen och LARDOMAR. Granskaren läste själv webbsidorna. En sökträff utan läsbar sida räknades inte. Domar per produkt finns i `vag2_skriv/k_utlatande_12.json` (fälten `nr`, `id`, `fil`, `dom`, `rattningar`, `skal`; RÄTTA-poster har också `regel` och `allvarlighet`). Varje före-text förekommer exakt en gång i sitt fält (kontrollerat i python).

## Resultat

| Batch | Utkast | GODKÄND | RÄTTA | UNDERKÄND |
|---|---|---|---|---|
| k_12a | 10 | 10 (10001–10008, 10010, 10012) | 0 | 0 |
| k_12b | 9 | 7 (10020–10023, 10025–10027) | 2 (10015, 10024) | 0 |
| Summa | 19 | 17 | 2 | 0 |

## Huvudfynd

1. **Webbkällorna stämmer med exakt modell.** Granskaren läste sju sidor och jämförde EAN (streckkoden) eller tillverkarnummer med vår variant. Alla stämde:
   - Gigantti Go Walker: Gy231105 och 6430016905817
   - Kärkkäinen Pro Pump: 6430016909013
   - Kärkkäinen Vivid: 6430062515398
   - Kärkkäinen Vinyl Grip: 6430016904339
   - Bygghemma: Gy61158 och 6430062510263
   - Elgiganten Universal Spike: 6430016905152
   - Kärkkäinen Court Mini Hoop: 6430016902137
   - Gigantti Air Track: GY61200-BL och 6430062514315

   Hos Kärkkäinen står numret bara i bildadressen, men det stämmer med vår streckkod.
2. **10007 Vinyl Grip godkänns, inte underkänns.** Utkastet byggde på en sökträff. Granskaren kunde läsa sidan (https://karkkainen.com/en-en/gymstick-20kg-vinyl-grip-pump---setti-1) och den bekräftar allt som står i texten: tredelad stång på 140 cm, vinylskivor 2 × 1,25, 2 × 2,5 och 2 × 5 kg samt fjäderlås. Byggaren ska ändra `att_bekrafta` till "sidan läst av granskaren 2026-11-04".
3. **Go Walker 10001–10005** följer utlåtande 11efg. Alla fem har typordet Promenadstavar och fast längd ur titeln. Ingen text säger "justerbar", nämner styrketräning eller gör hälsopåståenden.
4. **Typorden** Viktset, Stavspetsar, Promenadstavar och Tricepsstång har stöd:
   - Viktset finns som butikstagg på alla tre seten.
   - Stavspetsar och Tricepsstång står i svenska webbkällor.
   - Promenadstavar har stöd i livekällan och i Gigantti.

   Förslag: lägg till "viktset" och "promenadstavar" i profilens `godkanda_typord`.
5. **10026 Air Track:** texten innehåller inga påståenden om skydd, stötdämpning eller leder. Adressen i att_bekrafta (/yrityksille/) ger 404, men konsumentsidan hos Gigantti har samma innehåll. Varuste-adressen i att_bekrafta är bara domänen; den fullständiga adressen är https://varuste.net/da/p111085/uutiset.php. Själva kategorin behöver ett beslut, se nedan.
6. **10027 Kona:** taggen "På beställning" finns live, så meningen om längre leveranstid är rätt. Eagle 90 Transmission är mekanisk, och texten påstår inget om typen av växling.
7. **Viktskivor 10020–10025:** varje text räknar upp alla varianter och nämner inga priser. Håldiametrarna stämmer per produkt:
   - 10020: 31 mm hål för 30 mm stång
   - 10021: 51 mm hål
   - 10022: 51 mm hål för 50 mm stång
   - 10023: passar 50 mm-stänger; "51 mm" togs bort ur titeln, vilket är försiktigt
   - 10024: innercirkel 50,4 mm

   Lastgränsen 200 kg för 10025 står på en svensk rad med etikett (R4).
8. **Rättningar:**
   - **10015:** en enda återförsäljarsida räcker, eftersom EAN-numret entydigt binder sidan till vår produkt. Utkastet säger att svenskt typord saknas, men sidans svenska text använder "basketkorg". Titel och SEO-titel blir därför "Basketkorg Gymstick Court Mini Hoop" (R7).
   - **10024:** "Material: Gummi" ändras till "Ytskikt: Gummi". Källan anger bara ett lager gummi och säger inget om kärnan (R1).

## Avvisningar (9)
Alla nio avvisningar är motiverade:
- 10009, 10011, 10013, 10014, 10016–10018: ingen läsbar sida som gäller exakt modellen, eller produkttypen är oklar.
- 10019: balansbräda med lastgräns bara på engelska.
- 10028: elektronisk växling (AXS) och färg som titeln låser. Den väntar på Davids beslut.

## Beslut för David
- 10026 Air Track (uppblåsbar gymnastikmatta) underkändes tidigare (c_4 nr 3052) som landningsunderlag som ofta används av barn. Den nya texten gör inga skyddspåståenden, och kategorin står inte i profilens lista över sådant som hålls utanför. Granskaren godkänner texten. Om David vill att landningsmattor ska hållas utanför stryks produkten ur skrivfilen.

Ingenting ändrades i Shopify.
