# Skrivrapport vag2k_1 (Velomarket, Best of Sports)

Status: **avbruten 2026-11-03** efter första avvikelse (produkt nr 6032, se nedan). Inga taggar är satta (steg 5 har inte nåtts).

## Underlag
- Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_skriv_1.json` (90 produkter).
- Före-läge (sparat före första skrivning): `rapporter/shopify-original-2026-11-03/vag2k_1_fore.json` (90 poster: id, title, handle, status, tags, seo, descriptionHtml).
- Butik: BEST OF SPORTS (bestofsports.se), verifierad med get-shop-info.

## Före-läge och urval
- Live-läsning av alla 90 produkter: alla 90 har status ACTIVE.
- Ingen produkt har taggen "texter-klara" före skrivning.
- Ingen produkt hade titeln lika med skrivfilens titel.
- Hoppade över: 0.
- Live-id-mängden är identisk med skrivfilens (90 unika id).

## Kontroll på kopia (kontrollera_produkttext.py)
- Kopian är byggd av skrivfilen med html som beskrivning, standardblocket inlagt mellan [[STANDARDBLOCK]] och [[/STANDARDBLOCK]] (alla 90 hade rubriken "Leverans, retur och garanti"), fakta = före-läget (titel, SEO och beskrivning som ren text), `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS"`.
- Första körningen: 2 FEL, båda på nr 6075 (`tal_utan_kalla`, 2.4). Orsak: källan skriver "29x2 .4"" med mellanslag, så talet fanns i källan men kontrollen hittade det inte. Rättad i kontrollkopian (inte i skrivfilen).
- Efter rättningen: **0 FEL**, 103 VARNINGAR:
  - 90 `struktur` (avsnittet "Passar dig som" saknas; skrivfilen använder "Passar för", vilket är känt och godtaget).
  - 12 `engelska_ord` (färgnamnen Tiger Red 6056, Gunmetal Black 6071, Abyss Black 6054; 4 fält vardera). Är namn från tillverkaren, lämnas kvar. Granskarna avgör.
  - 1 `titel_kommatecken` (nr 6071 med 3 kommatecken, decimalkomma i mått; godtaget enligt instruktionen).

## Skrivning
- Skrivet med `productUpdate(product: ...)`, max 6 produkter per mutation, fält title, seo{title, description} och descriptionHtml. Handle och status ändrades inte.
- Skrivna produkter (21 st): nr 6006, 6009, 6010 (kanarie), 6013–6018, 6023–6034 (inklusive 6032, se avvikelse nedan).
  - Kanarie 6006, 6009, 6010: läst tillbaka för hand, sedan maskinellt i nästa kontroll.
  - 6013–6018: maskinell återläsning, alla fält OK.
  - 6023–6028: maskinell återläsning, alla fält OK.
  - 6029, 6030, 6031, 6033, 6034: maskinell återläsning, alla fält OK.
  - **6032 (id 10530156347658): AVVIKELSE, stoppat.** Live `seo.description` är "Giant Talon 3 XS är en mountainbike med 27,5-tums hjul, aluminiumram, 16 växlar och hydrauliska skivbromsar. Framgaffeln har 80 mm slaglängd." Skrivfilen säger "Giant Talon 3 i ramstorlek XS är en mountainbike med 27,5-tumshjul, aluminiumram, 16 växlar och hydrauliska skivbromsar i färgen Panther." Felet är mitt: meta-texten skrevs in från eget minne i stället för från skrivfilen. Titel, handle, status och descriptionHtml för 6032 är korrekta.
- Ingen produkt har skrivits efter 6032. De 69 återstående är inte skrivna.

## Återläsning
- Metod: läsning av live via Shopify-API, sparad som fil, jämförelse i Python mot skrivfilen och före-läget. Fält: title, handle, status, seo.title, seo.description, descriptionHtml (exakt strängjämförelse, inga normaliseringar behövdes), tags (före-taggar kvar).
- Shopify lagrade radbrytningar mellan `<li>` exakt som skrivet.
- För de 3 kanarieprodukterna gjordes den första läsningen för hand och den andra maskinellt.

## Beslut och nästa steg
1. Rätta 6032:s seo.description till skrivfilens text, läs tillbaka och kontrollera maskinellt. Först därefter fortsätter skrivningen med resten (69 produkter, batcher om högst 6).
2. Sätt taggen "texter-klara" på alla skrivna produkter när skrivningen är klar, med bekräftelse att befintliga taggar finns kvar.
