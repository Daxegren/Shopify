# Stickprov tillbehör, skrivfil b_skriv_5 (kontroll 2026-11-03)

Butik: BEST OF SPORTS (bestofsports.se) bekräftad. Endast läsning. Urval 10 av 28: 8049, 8050, 8054 (rättade i b_utlatande_22_23), 8063 (meta null), 8064, 8096 (först oskrivna), 8067, 8075, 8088, 8091.
Jämfört tecken för tecken (python): titel, seo.title (null när lika med titeln), metabeskrivning, descriptionHtml. Standardblocket jämfördes mot en transkriberad kopia av live-texten (inte mekaniskt för varje produkt, men texten var identisk vid genomläsning). Taggen texter-klara och status ACTIVE kontrollerades för alla 10.

## Resultat
- Titel, SEO-titel, HTML (inkl. rättade formuleringar), tagg texter-klara, status ACTIVE: 10 av 10 stämmer exakt.
- Fakta mot före-filen (vag2b_5_fore.json): inga påhittade uppgifter funna. Utelämnat enligt regeln: leverantörens "grundat 1972", "perfekta valet", "antibakteriell plast", "extremt hållbara", "stötdämpning". Stavning och formatregler (stor bokstav efter kolon, beskrivande ord) utan anmärkning.
- 8063 meta null: live null, stämmer.

## AVVIKELSE (allvarlig men begränsad): metabeskrivning saknas live
Gäller alla produkter där skrivfilen har meta och seo_title är lika med titeln. Skrivagenten utelämnade då hela seo-objektet (prompten säger "utelämna seo om SEO-titeln är lika med titeln") och tappade därmed metan. Live seo.description = null, filen har text. Kontrollerat live: 11 av 11 i hela filen drabbade (3 i stickprovet, 8 kontrollerade separat).

| nr | id | Före (live) | Efter (ska vara, ur skrivfilen) |
|---|---|---|---|
| 8064 | 10494696587530 | null | Ass Savers Fendor Bendor Regular är en vikbar bakskärm i polypropen som väger 50 g. Enligt tillverkaren passar den däckbredder på 23–35 mm. |
| 8096 | 10548232618250 | null | Giant Cleanspring är en genomskinlig, blå dricksflaska på 600 ml. Flaskan är gjord av plast som är 100 % BPA-fri, enligt tillverkaren. |
| 8088 | 10541328367882 | null | Liv Supreme SF är cykelhandskar för damer med ergonomisk, förformad tumdesign. Den förlängda manschetten ersätter kardborrefästet. |

Övriga drabbade (meta ur b_skriv_5.json): 8055 (10475355570442), 8057 (10475361894666), 8058 (10475385356554), 8061 (10475981930762), 8074 (10523464368394), 8080 (10525550510346), 8089 (10541366640906), 8095 (10541370016010). Live seo = {null, null} för alla.
Produkterna med seo_title skilt från titeln (8065, 8069, 8073, 8075, 8086, 8091) har sannolikt meta; 8075 och 8091 verifierade, övriga ej kontrollerade.

Åtgärd (kräver ditt ja, ingen skrivning gjord): skriv seo.description för de 11, med seo.title utelämnat/null. Samma fel kan gälla andra skrivfiler (b_skriv_2 till 6, c, k) som skrevs med samma prompt: kör motsvarande kontroll (meta i fil, null live).
