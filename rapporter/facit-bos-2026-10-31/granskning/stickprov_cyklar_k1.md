# Stickprov cyklar, skrivfil k_skriv_1 (2026-11-03)

Kontrollagent, endast läsning. Inget skrevs i Shopify. Butik bekräftad med get-shop-info: BEST OF SPORTS, bestofsports.se.

## Urval
18 av 90 produkter (20 procent), spridda över hela filen (index i filen, 0 till 89):
6006, 6015, 6024, 6029, 6032, 6036, 6042, 6048, 6054, 6062, 6066, 6071, 6075, 6078, 6088, 6093, 6119, 6125.
Med: 6032, 6075 och 6119 (titeln med 3 kommatecken).

## Metod
- Live-läsning via graphql_query (title, handle, status, tags, seo{title description}, descriptionHtml) för alla 18.
- Teckenvis jämförelse (Python, sträng mot sträng) mot `vag2_skriv/k_skriv_1.json`: titel, SEO-titel (lagrad som null när den är lika med titeln), metabeskrivning, html. Beställningsmeningen i standardblocket kontrollerades mot taggen `På beställning`.
- Fakta jämförda mot källan `shopify-original-2026-11-03/vag2k_1_fore.json`: alla tal i titel, SEO, meta och beskrivning (komma och punkt lika), samt manuell läsning av källtexten för varje påstående som kan vara påhittat (märkeszoner, "enligt tillverkaren", ingår-listor, mått).
- Formatregler: titel högst 70 tecken och högst 2 kommatecken, SEO-titel högst 43, meta 130 till 155, unikhet mot hela filen, stor bokstav efter kolon.

## Resultat
| Kontroll | Resultat |
|---|---|
| Titel, SEO-titel, meta, html teckenvis lika med skrivfilen | 18 av 18 lika, 0 avvikelser |
| SEO-titel null i Shopify när lika med titeln | 6088, 6093, 6125: ja (avsett) |
| Radbrytning mellan `<li>` | Finns live, avsett |
| Standardblocket (leverans, retur, reklamation, säljare) | Identiskt; beställningsmeningen finns exakt på de med taggen `På beställning` (6015, 6024, 6029, 6042, 6048, 6054, 6075, 6078) |
| Taggen `texter-klara` | 18 av 18 |
| Status ACTIVE | 18 av 18 |
| Handle | Oförändrad mot källan |
| Tal som saknas i källan | 0 |
| Påhittade fakta | Inga funna (se anmärkningar) |
| Titel högst 70 tecken | Alla (längsta 61) |
| SEO-titel högst 43 | Alla (längsta 42, 6125) |
| Meta 130 till 155 | Alla (132 till 151) |
| Dubbletter av titel, SEO eller meta i filen | Inga |
| Stor bokstav efter kolon | OK. Enda gemena efter kolon är "microSHIFT Advent" (6015, 6029), ett märkesnamn |
| Stavning | Inga fel |

Slutsats: 0 avvikelser mellan skrivfil och live, 0 faktafel, 0 formatfel.

## Titeln med 3 kommatecken: 6119
Titel live och i skrivfilen: `Cykel Romet Rambler R7.0, 27,5 tum, Grå och Röd` (47 tecken).
Kommatecknen är: (1) separator efter "R7.0", (2) decimalkomma i "27,5", (3) separator efter "tum". Alltså 2 riktiga avgränsare och 1 decimalkomma i ett mått. Ingen överträdelse av regeln om högst 2 kommatecken; det är den kända falska positiven. Källtiteln skriver också måttet som 27,5. Ingen åtgärd.
Jämför 6032 ("Talon 3 XS 27,5 tum, Panther"), som har decimalkomma men bara 2 kommatecken totalt.

## Anmärkningar (inga avvikelser, inget att rätta)
1. 6036: titeln och metan säger "700c". Källan anger däcket som 700x25c; "700c" är hjulstorleken som följer av det. Rimlig härledning, ingen avvikelse.
2. 6125: titeln säger Damcykel. Källtiteln har bara "Cykel ... 2.0 D", men produkten har taggen Damcyklar och "D" är damsuffixet. Källtexten säger dessutom "Vintage Classic 1.0 D" medan titeln är 2.0; skrivfilen följer titeln (rätt). Kan läggas under "att bekräfta" om David vill.
3. 6075 och 6078 (Liv Tempt): typen "Mountainbike" i stället för källans "Damcykel", och "Livs damsortiment/sortiment för kvinnor" finns i källan ("Liv-sortimentet för kvinnor"). OK.
4. Små stilskillnader mellan produkter: "29-tums hjul" (6015 meta) mot "29-tumshjul" (6029). Båda är godtagbar svenska.
5. Utelämnat ur texterna men inte fel: bland annat hjulvikt 10,9 kg (6006) och ramstorlekslistor. Hellre för lite än för mycket.

## Avvikelser, före och efter
Inga.
