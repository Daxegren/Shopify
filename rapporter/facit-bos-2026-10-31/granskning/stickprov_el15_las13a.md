# Stickprov elcyklar (b_skriv_15) och lås (b_skriv_13a), 2026-11-03

Kontrollant: Claude (endast läsning, inget skrivet i Shopify). Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info.
Metod: live-läsning via graphql_query (högst 4 produkter åt gången: title, status, tags, seo{title description}, descriptionHtml), teckenvis jämförelse i python mot skrivfilen (titel, seo_title, meta, html; null i seo.title tolkas som lika med titeln; radbrytning mellan li är avsedd), plus kontroll mot före-filerna vag2b_15_fore.json och vag2b_13a_fore.json (tal, påståenden).
Eftersom live-texten måste föras över till python för hand uppstod tre inklistringsfel hos kontrollanten (8785, 8780: "när" blev "when"; 8651: extra li). Alla tre försvann vid omläsning och ny jämförelse (ingen verklig avvikelse).

## Uppgift A: 12 av 25 (b_skriv_15)
Kontrollerade: 8777, 8778, 8785, 8791, 8792, 8794, 8798, 8799, 8800, 8801 (nio granskarrättade: 8777, 8798, 8778, 8791, 8792, 8794, 8799, 8800, 8801, alltså alla nio, samt 8785) och spridda 8780 (fixie), 8783 (Giant Fathom).
Resultat: titel, seo.title, meta och html identiska med skrivfilen för alla 12. Status ACTIVE och taggen texter-klara finns på alla. Inga osynliga tecken (U+00AD, U+200B/C/D, U+2060, U+FEFF, U+00A0). Meningen om längre leveranstid står på alla med taggen "På beställning" (8777, 8778, 8780, 8783, 8791, 8794, 8798, 8799, 8800) och på ingen utan (8785, 8792, 8801). Titel högst 70, SEO-titel högst 43, meta 133-150 tecken. Alla tal i texterna finns i före-källan (8791/8792: "1 150" mm = "1150" i källan). Räckvidd, laddtid och topphastighet står bara som "enligt tillverkaren". Motor, batteri, display, växlar och bromsar återger källan. Inga omdömen eller lagkrav.
Anmärkningar (ingen avvikelse mot skrivfilen, men för beslut):
1. 8778 Tenways CGO009 innehåller en appfunktion: intro "kan kopplas till TENWAYS-appen" och punkten "Dig som vill kunna koppla cykeln till TENWAYS-appen". Källan säger "Via TENWAYS-appen kan du dessutom koppla upp cykeln för extra kontroll och översikt", så det är inte påhittat, men uppgiften sade att appfunktioner inte ska förekomma. Förslag: ta bort de två ställena.
2. 8799 Giant Explore: "MIK HD-pakethållare" under Ingår. Källans engelska maskinöversättning lyder "MIK HD rear frame" (beskrivningen nämner "luggage rack"). Tolkningen är rimlig men inte ordagrann. Låg risk.
3. 8791 och 8792 skiljer sig åt avsiktligt (8791 "Fjädring fram", 8792 "Fjädring") i enlighet med respektive källa.

## Uppgift B: 6 av 29 (b_skriv_13a)
Kontrollerade: 8647, 8648, 8651, 8655, 8660, 8664. Status ACTIVE och texter-klara finns på alla sex. Ingen "På beställning" och ingen leveranstidsmening (korrekt). Titel, seo.title och meta identiska för alla sex. Alla tal finns i källan. Säkerhetsnivå återges som "enligt tillverkaren" (8647: 7 av 15, 8655: 14 av 15, 8660: 9 av 15, 8664: 3). Inga säkerhetslöften, stöldskydd eller omdömen.
Metalängder: 8647 133, 8648 149, 8651 122, 8655 105, 8660 136, 8664 122 (alla minst 70 enligt avsnitt 17).

### AVVIKELSE 8647 Vikbart Lås AXA Fold Lite 80: osynligt tecken
Live-texten (läst två gånger) innehåller mjukt bindestreck U+00AD i ordet "remmar", som "rem­mar", på två ställen. Skrivfilen har inget U+00AD (kontrollerat i kod: '­' in html är False för alla fält).
Före (live, html): `...eller med medföljande rem­mar</li>` och `<li>Hållare: För cykelramen, medföljande rem­mar ingår</li>`
Efter (ska vara, skrivfilen): `...eller med medföljande remmar</li>` och `<li>Hållare: För cykelramen, medföljande remmar ingår</li>`
Obs: avvikelsen är konstaterad genom att texten kopierades ur live-svaret och kontrollerades i python (ord 0xad, två gånger). Kontrollantens egen första inklistring tappade tecknet, så en fullständig automatisk teckenjämförelse av detta fält gjordes inte; förslag: rättningen sker via update av descriptionHtml med texten från skrivfilen och ny omläsning. Övriga fält på 8647 är identiska.

## Sammanfattning
18 produkter kontrollerade (12 + 6). 17 av 18 identiska med skrivfilen utan anmärkning mot skrivfilen; 1 verklig avvikelse (8647, U+00AD x2). 2 innehållsanmärkningar (8778 appfunktion, 8799 "MIK HD-pakethållare"). Inget skrevs i Shopify.
