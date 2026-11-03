# Stickprov tillbehör, skrivfil b_skriv_7 (43 produkter), 2026-11-03

Kontrollagent, endast läsning. Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info.
Live-läsning på nytt via graphql_query (title, handle, status, tags, seo, descriptionHtml), jämförd i python mot b_skriv_7.json.

## Urval (10 av 43)
8213 Wisp SF handskar (rättad), 8216 Pace Gel SF handskar (meta null, rättad), 8229 Liv-flaska 600 ml (rättad), 8227 Sadelväska Shadow DX, 8238 / 8246 / 8249 innerslangar, 8222 Framkorg Green Life L (rättad), 8255 Stänkskärmar Velo 55 (meta null, rättad), 8253 Handtag Ethic Slim (rättad).
Krav uppfyllda: 3 innerslangar, 3 handskar/flaskor, 2 med meta null, 6 med rättat utlåtande i b_utlatande_27_28.json.

## Resultat: inga avvikelser
- Titel, SEO-titel, metabeskrivning och html-huvud (allt före rubriken "Leverans, retur och garanti") är tecken för tecken lika filen i alla 10. Shopifys lagring av seo.title som null när den är lika med titeln (8213, 8216, 8227) och radbrytning mellan <li> är avsett.
- seo.description live = filens meta; null endast för 8216 och 8255 (filens meta null).
- Längder: titel 32-60, SEO-titel 30-41 (högst 43), meta 132-149 (130-155). Inga kommatecken- eller versalbrott sågs.
- Taggen texter-klara finns på alla 10, status ACTIVE på alla 10. Övriga taggar oförändrade mot före-filen (8222 har kvar Cykelbelysning från före-läget, ej en avvikelse).
- Innerslangar: 8238 = 24 tum, Schrader (autoventil), ETRTO 50/60-507. 8246 = 28 tum (700C), Presta, 32/47-622/635, däckbredd 32-47 mm. 8249 = 27,5 tum, Presta, 57/70-584. Dimension och ventil stämmer med titel och före-fil och är konsekventa i titel, SEO, meta, brödtext och specifikation (24/507, 622/635, 27,5/584 hänger ihop).
- Fakta mot rapporter/shopify-original-2026-11-03/vag2b_7_fore.json: inga påhittade uppgifter. Bekräftade bland annat BPA-fri och lätt att rengöra (8229), minst 30 l, rotting, handgjord, MIK-kit/lådfästkit säljs separat (8222), 117 g gummi (8253), 0,7 l och 160 x 80 x 80 mm (8227). Utelämnat avsiktligt: UPF-solskydd (8213), märkeshistorik (Giant, Basil). Stavning och formatregler (stor bokstav efter kolon, versaler i titel) utan anmärkning.
- Notering (ingen åtgärd): 8216 och 8255 har tunn källa (tom före-text) och texterna är korta med "enligt tillverkaren" respektive färg/modell enligt titeln, i linje med standarden.

## Begränsning
Standardblocket (Leverans, retur och garanti) jämfördes inte tecken för tecken i python mot live. I filen är blocket identiskt i alla 43 (en enda variant, 659 tecken, kontrollerat i de 10), och i live lästes det visuellt som identiskt i alla 12 hämtade produkter.

## Produkterna 10462782554378 och 10462856806666 (inte i b_skriv_7)
- 10462782554378 Justerbar Hantel Toorx 1,5-18 kg, 12 Steg: status DRAFT, taggar Hantlar, Konditionsträning & Fitness, texter-klara, Toorx, Velomarket.
- 10462856806666 Gymnastikboll Tunturi Gymball 90 cm, Blå: status DRAFT, taggar Fell, Konditionsträning & Fitness, texter-klara, Tunturi, Velomarket.
- Båda var DRAFT redan i shopify-original-2026-11-02/tag_texter_klara_fore.json (före taggningen) och fick texter-klara i en tidigare våg. Statusen är alltså inte ändrad av vågen, men texter-klara på DRAFT-produkter är värt ett beslut av David (publicering ingår inte i uppdraget).
