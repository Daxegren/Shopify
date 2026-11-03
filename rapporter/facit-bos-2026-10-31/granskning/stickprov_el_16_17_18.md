# Stickprov elcyklar/cyklar, skrivfil 16, 17, 18 (2026-11-03)

Kontrollant: Sonnet, endast läsning. Butik bekräftad: BEST OF SPORTS (bestofsports.se).

## Urval (21 av 66)
- b_skriv_16 (7): 8747, 8749, 8752, 8763 (eltrehjuling), 8768, 8769, 8773 (Liv Lurra).
- b_skriv_17 (7): 8803, 8805, 8814 (10472298053898), 8815 (10472298414346), 8817 (10472303493386), 8823, 8829.
- b_skriv_18 (7): 8831, 8838, 8842, 8848, 8852, 8854, 8858.

## Metod
Live läst via graphql_query (4 produkter åt gången): title, status, tags, seo, descriptionHtml. Jämfört tecken för tecken i python mot skrivfilen: titel, seo_title (null när lika med titeln), meta, html (hela innehållet före "Leverans, retur och garanti" jämfört direkt; standardblocket byggt från live-texten och jämfört, med meningen om längre leveranstid endast när taggen "På beställning" finns). Standardblockets text i live-svaret granskades med ögat mot mallen, inte med kod.

## Resultat
- Tecken för tecken mot skrivfilen: 21 av 21 identiska (titel, SEO-titel, meta, html). Inga extra mellanslag, inga ändrade ord, inga osynliga tecken (soft hyphen, nollbreddsmellanslag, nbsp).
- Status ACTIVE och taggen texter-klara: 21 av 21.
- Meningen om längre leveranstid: finns på alla produkter med taggen "På beställning" och på ingen utan (8747, 8805, 8815, 8817, 8823, 8831 saknar tagg och mening).
- Längder: SEO-titel 24-43 tecken, meta 131-154 tecken.
- Tal: alla tal i titel, meta och beskrivning finns i före-filerna (vag2b_16/17/18_fore.json).
- Räckvidd, laddtid (8817) och motor/batteri/display återges som källan anger; alla räckvidder står "enligt tillverkaren". Inga omdömen (säker, tålig, lätt att använda), lagkrav, spårning/GPS/app/lås, inga felkopierade vanliga-frågor-avsnitt.
- Motsägande källuppgifter är utelämnade: Lurra (batteri 750 Wh/5,5 kW), Kona El Kahuna (däck 2,25 mot 2,5 tum), Fiido X (app, lås), ADO Air 30 Pro (växlande navmotor, GPS, app), CGO800S (motormärke Mivice).
- Stavning: inga fel funna. Synonymer mot källan (mellanmotor/mittmotor, mid-engine/mittmotor) bedömda som oskadliga.

## Avvikelser
Inga. Inget att rätta i dessa 21.
