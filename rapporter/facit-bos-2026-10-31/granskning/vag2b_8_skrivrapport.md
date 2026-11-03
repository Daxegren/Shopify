# Skrivrapport Velomarket vinter, våg 2b, grupp 8 (26 produkter)

Status: **AVBRUTEN före skrivning.** Ingen produkt skrevs i Shopify. Inga taggar lades till.

## Kontroller
- Butik: BEST OF SPORTS (bestofsports.se), bekräftad via get-shop-info.
- Live-läsning: 26 av 26 produkter lästa. Alla ACTIVE. Ingen har taggen `texter-klara`. Ingen har redan skrivna titlar.
- Före-läge sparat: `rapporter/shopify-original-2026-11-03/vag2b_8_fore.json` (26 poster, innan något skrevs).
- Kontrollskript på kopia (`granskning/tmp_kopia_vag2b8/kontroll_b8.json`, html mappad till beskrivning, standardblock markerat, källtext = före-läget, `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70`): **26 produkter, 3 FEL, 28 VARNINGAR.**

## Fel som stoppade skrivningen
- **10494685380874 (Skidstav Rex Omega i Glasfiber), FEL tal_utan_kalla x3.** Beskrivningen anger "Varianter: 125, 135 och 160". Talen finns inte i produktens källtext (före-läget). Källtexten nämner inga varianter, bara handtaget Tour 11 mm och stavlängdsformlerna. Enligt standarden (avsnitt 2, punkt 2, "Tal") och LARDOMAR 2026-11-03 tas uppgiften bort, eller produkten lyfts till David. Jag rättade inte texten för hand.

Varningarna är godtagna enligt uppdraget: "Passar för" saknar "passar dig som" (avsiktligt), och 10462242570506 (tom beskrivning i källan) och 10472242839818 (kort text) fick ordvarning.

## Hoppade över
Inga. Alla 26 produkter var ACTIVE och oskrivna.

## Nästa steg (kräver beslut)
1. David (eller Opus-granskare) avgör Rex Omega: ta bort raden "Varianter: 125, 135 och 160" och kör om kontrollen, eller låt produkten utgå från gruppen.
2. Därefter byggs skrivfilen om med det beslutet. Mutation skrivs av skript och klistras in ordagrant. Kanarie om 3 produkter först.
3. Inget har skrivits i Shopify, så ingen återläsning eller tagg behövs för denna grupp.
