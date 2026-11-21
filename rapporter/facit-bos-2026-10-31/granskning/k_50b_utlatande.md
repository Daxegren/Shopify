# Granskning k_50b (13 utkast), Opus, 2026-11-17

Källa: live-läsning 2026-11-17 (`rapporter/shopify-original-2026-11-17/k_50b_kalla_live_granskning.json`), samt webbkoll mot tillverkare och återförsäljare. Utlåtande i JSON: `vag2_skriv/k_utlatande_50b.json`. Alla före-strängar finns exakt en gång i sina fält (kontrollerat i python). Ingenting har ändrats i Shopify.

**Resultat:** 3 GODKÄND, 9 RÄTTA, 1 UNDERKÄND. Inga avvisade utkast fanns i batchen. Ingen produkt har taggen "På beställning".

| nr | Produkt | Dom | Kort skäl |
|---|---|---|---|
| 50101 | Ramväska Basil Navigator Storm M | RÄTTA | Tillverkaren (basil.com) visar att väskan sitter på ramen, inte på sadel eller styre (felöversättning). Tillverkarens två måttuppgifter går isär, så måtten utelämnas. |
| 50102 | Handskar Spiderman (barn) | RÄTTA | Texten är sanningsenlig och utan skyddslöfte. Metan saknade verb. Risk till David nedan. |
| 50103 | Pakväska Basil City grå | GODKÄND | Webbkollen hos basil.com bekräftar art.nr, EAN, 28 l som kan utökas till 32 l, vattenavvisande och Universal Bridge. |
| 50104 | Styrväska Pro Gravel Discover | RÄTTA | "Styckväska" är en felstavning av styrväska. Butikens skrivna syskon heter "Styrväska". |
| 50105 | Sparkcykelhjul Panda Spoked V2 | RÄTTA | Typordet ändras till "Sparkcykelhjul" (26 skrivna syskon). Metan saknade verb. |
| 50106 | Handskar Giant Chill X LF | RÄTTA | Det engelska "Glove" stryks. Flagga: en annan aktiv produkt har samma titel (se nedan). |
| 50107 | Cykelklocka Brave Classics Mini | RÄTTA | "(Tyskland)" är en obekräftad ursprungsuppgift och tas bort ur meta, beskrivning och specifikation. |
| 50108 | Cykelhållare Choetech H067 | GODKÄND | Modellen H067 bekräftas av Galaxus och Mwave. Den trasiga skoterraden är rätt utelämnad. |
| 50109 | Dricksflaska Giant Doublespring 750 ml blå/grå | RÄTTA | "Antibakteriell" stryks (praxis). SEO-titeln var nästan identisk med 600 ml-flaskan. |
| 50110 | Dricksflaska Giant Doublespring 750 ml blå/svart | RÄTTA | SEO-titeln krockade exakt med redan skriven 600 ml (10468718641418). "Antibakteriell" stryks. |
| 50111 | Dricksflaska Giant Doublespring 750 ml transparent/svart | RÄTTA | "Antibakteriell" stryks. |
| 50112 | Vattenflaska Nils NCD04 | GODKÄND | Alla uppgifter står i källan. Kvalitetsorden är rätt utelämnade. |
| 50113 | Cykelskydd Oxford Aquatex (03-CC100) | UNDERKÄND | Trolig exakt dubblett av skriven 10635765743882 (handle "oxfcc100", samma Oxford CC100). Källans mått 192 x 72 cm motsäger tillverkarens 200 x 80 cm. |

## Viktigaste fynden
1. **Dubblettrisk 50113.** Oxford CC100 finns redan skriven och aktiv. Koordinatorn bör läsa streckkoden på 10635765743882. Är den 5030009319648 gäller dubblettbeslutet. Annars skrivs produkten med tillverkarens mått 200 x 80 x 110 cm.
2. **SEO-krock 50110** mot en redan skriven fil, som byggskriptets unikhetskontroll också ska fånga.
3. **"Antibakteriell"** var med i alla tre Giant-flaskor trots tidigare praxis att stryka det. Det är ett förslag till nytt skripttest (hälso- och biocidord).
4. **Typord.** "Hjul till sparkcykel" ska vara "Sparkcykelhjul" och bör läggas i `godkanda_typord`. "Cykelskydd" är rätt ord, "Cykelöverdrag" används inte i butiken. "Styckväska" ska vara "Styrväska".
5. **50106 Giant Chill X LF.** 10554367475978 (art.nr 830001141) har identisk live-titel. Återförsäljarlistor kopplar 830001091 till storlek XL, men det gick inte att bekräfta entydigt, så storleken anges inte. Nästa text för syskonet måste få en titel som skiljer sig.

## Beslut för David
- **50102 Spiderman-handskar.** Barnprodukten marknadsförs av leverantören som skydd mot stötar. Utkastet tar inte med något skyddspåstående och följer beslutet 2026-11-08 om aktiva barnprodukter. Rekommendation: skriv. Alternativet är att hålla barnprodukter med skyddsmarknadsföring utanför helt (då underkänns 50102).
- **50104 Styrväska.** Rekommendation: rätta felstavningen. Alternativet är att behålla live-ordet "Styckväska" ordagrant enligt R7.

## Webbkällor
- https://www.basil.com/en/p/8715019182761/basil-navigator-storm-m-frame-bag-2-2-liters-black/
- https://www.basil.com/en/city-double-bicycle-bag-grey-melee.html
- https://picar.hu/en/Panda-Spoked-V2-100mm-Wheel-Chrome
- https://www.alfjonescycles.co.uk/product/4765/giant-chill-x-glove/
- https://meinhartje.com/en/brave-classic-bell-copenhagen/03203338
- https://www.galaxus.de/en/s1/product/choetech-h067-adjustable-bicycle-holder-black-smartphone-holder-43245929
- https://www.oxfordproducts.com/oxford-aquatex-single-bicycle-cover-cc100.html
