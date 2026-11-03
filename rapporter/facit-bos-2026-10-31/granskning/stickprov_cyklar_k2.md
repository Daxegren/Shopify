# Stickprov cyklar och cykeldelar, skrivfil k_skriv_2.json (2026-11-03)

Kontrollant: Sonnet, endast läsning. Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info. Inget skrevs i Shopify.

Urval: 10 av 34 (6126, 6133, 6140, 6143, 6147, 6153, 6160, 6169, 6206, 6207), spridda över damcyklar, hybrid, gravel, hopfällbar, tillbehör och växelreglage. Inkluderar id 10472243265802 (6206) och 10472240972042 (6207) samt 6147.

Metod: live-läsning via graphql_query (title, handle, status, tags, seo, descriptionHtml) jämförd med skrivfilen (titel, seo_title, meta, html), standardblocket jämfört maskinellt (`html.endswith`), övrigt text mot text. Fakta kontrollerade mot `shopify-original-2026-11-03/vag2k_2_fore.json`.

## Resultat: 0 avvikelser av 10

| Nr | Id | Titel | SEO-titel (live) | Meta | HTML | Status/tagg |
|---|---|---|---|---|---|---|
| 6126 | 10472332951818 | lika | lika | lika | lika | ACTIVE, texter-klara |
| 6133 | 10462795366666 | lika | lika | lika | lika | ACTIVE, texter-klara |
| 6140 | 10462191780106 | lika | lika | lika | lika | ACTIVE, texter-klara |
| 6143 | 10472334065930 | lika | lika | lika | lika | ACTIVE, texter-klara |
| 6147 | 10572695503114 | lika | lika | lika | lika | ACTIVE, texter-klara |
| 6153 | 10472287928586 | lika | lika | lika | lika | ACTIVE, texter-klara |
| 6160 | 10475420975370 | lika | lika | lika | lika | ACTIVE, texter-klara |
| 6169 | 10475980849418 | lika | null (lika med titeln, avsett) | lika | lika | ACTIVE, texter-klara |
| 6206 | 10472243265802 | lika | lika | lika | lika | ACTIVE, texter-klara |
| 6207 | 10472240972042 | lika | null (lika med titeln, avsett) | lika | lika | ACTIVE, texter-klara |

Radbrytning mellan `<li>` i live är avsedd. Standardblocket (Leverans, retur, garanti, Säljare) är teckenlikt skrivfilen i alla 10 och saknar markörer.

## Standardkontroller
- Längder: titel 37 till 64 tecken (max 70), SEO-titel 28 till 42 (max 43), meta 136 till 153 (130 till 155). Inga versaler, högst 2 kommatecken, inga utropstecken.
- Stavning: "Växelreglage" korrekt i 6206 och 6207. Inga skrivfel funna.
- Formatregler: stor bokstav efter kolon och i titelns beskrivande ord ("Svart och Guld", "Brun och Svart", "Hopfällbar Cykel") följs.
- Faktaregeln: allt belagt i före-filen. "Enligt tillverkaren" används för tillverkarpåståenden (6153 tillbehör, 6169 användning, 6206 intern kabeldragning). Inga ursprungsuppgifter ("Tillverkad i EU/Polen"), märkesbakgrund (Giants "grundat 1972") eller superlativ har förts över. Vikt, mått och växlar stämmer mot källan.

## Anmärkningar (ingen avvikelse från skrivfilen)
- 6153: SEO-titeln börjar "Cykel Tabou Kinetic 2.0 Plus W, Svart/Guld" medan titeln börjar "Damcykel". Giltigt enligt standarden (42 tecken), men typordet skiljer sig. Skrivfilen och live är lika, så ingen rättning föreslås utan beslut.
- 6133 och 6140: ramstorlekar och vikt (6133: 18,2 kg) utelämnade pga. varianter, i linje med regeln om varianter.
