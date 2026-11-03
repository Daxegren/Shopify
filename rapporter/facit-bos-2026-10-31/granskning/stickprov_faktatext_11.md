# Stickprov faktatext grupp 11 (b_skriv_11.json), 2026-11-03

Kontrollant: läsläge, inget skrivet i Shopify. Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info.
Urval: 10 av 14 (index 0-9): Peltonen Acadia SK 25 Med, Supra C 21 Medium, Acadia SK 25 Stiff, Acadia SK 21 Medium; Limar Horus Matt Black Titanium, Kosmos Jungle Matt Black Amaranth, Kosmos PH Matt Black, Kosmos Space Blue Orange, Caos Matt Black Blue, Kosmos Matt Gray. Ej kontrollerade: Kosmos Space Titanium Amaran, Horus Matt Gray, Horus Transp Light Gray, F90.

## Teckenjämförelse live mot skrivfil (python)
Alla 10: titel, SEO-titel, metabeskrivning och descriptionHtml är identiska tecken för tecken (inklusive radbrytning mellan li, som lagras av Shopify). Peltonen: seo.title lagras null (lika med titeln), avsett. seo.description live = filens meta. Inga avvikelser.

## Status, tagg, titel
- Status ACTIVE och taggen texter-klara finns på alla 10.
- Peltonen-titlarna börjar "Längdskidor Peltonen" (4 av 4).
- SEO-titlar högst 43 tecken (längsta 39).

## Fakta mot före-filen (vag2b_11_fore.json)
Inga påhittade uppgifter hittades. Tal (25, 21, 44/44/44 mm, PRG-4000/4100/3600, 100 %, UV400, Cat. 3, 400 nm) finns i källan eller titeln. Skate/klassisk och längd nämns inte i någon text. Funktionspåståenden (lätta träningsskidor, toppskidornas konstruktion, ramen lätt och ultratålig, ventilation som förhindrar imma, Caos UV-skydd upp till 400 nm) står med "enligt tillverkaren". Inga omdömen, priser eller hälsoord.

## Varianter
- Acadia SK 21 Medium: butiken har 2 varianter (181, 188). Meta "två varianter" stämmer.
- Acadia SK 25 Stiff: 3 varianter (174, 181, 188). Meta "tre varianter" stämmer.
- Acadia SK 25 Med: 1 variant (174), metan nämner inga varianter. OK.

## Anmärkningar (inga fel, för beslut)
1. Kosmos PH, spec/passar för: "Fotokromatiskt system", "antidimma-system" och "luftcirkulationssystem" står utan "enligt tillverkaren" (som produktnamn på system i källan, ingen effekt påstås). Linsraden har "(enligt tillverkaren)" för UV400/Cat.3, men källa anges inte uttryckligen. Bedömning: godtagbart; stramast vore att lägga "enligt tillverkaren" på hela systemraden.
2. Caos-ingressen: "kitet innehåller en lins med 100 % UV-skydd upp till 400 nm" står i samma mening som "Enligt tillverkaren", men raden "Linser i kitet" i specifikationen nämner Cat. 3 utan förbehåll. Bedömning: OK, ej UV-påstående i den raden.
3. Korta metabeskrivningar under 130 tecken (avsnitt 14, tunn källa, tillåtet): Horus 123, Space Blue Orange 102, Matt Gray 94; "Finns hos BEST OF SPORTS." är inte tillagd (krävs bara under 70).
4. Peltonen: handtag/slug är kvar som "skridskor-..." och taggen "Skridskor" finns kvar (ingen textfråga, ändras inte i faktatextläget).
5. Källans "universal" (Stiff) skrivs "Universell" och "SK 25 Med" kommer ur titeln "MED". Båda rimliga.

Slutsats: 10 av 10 utan avvikelse mot skrivfilen och utan faktafel. Full kontroll av de 4 återstående ej nödvändig.
