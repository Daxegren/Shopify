# Skrivrapport f_1fix (2026-11-04)

Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info.
Beslut: Davids alt A 2026-11-04. Maxvikt/användarvikt utelämnas när källan är engelsk "Maximum operating weight".

- Produkter: 10021 (10472323776778), 10024 (10468770087178), 10025 (10471307411722). Alla hade redan taggen texter-klara och skrevs om.
- Före-läge: rapporter/shopify-original-2026-11-04/f_1fix_fore.json
- Skrivning: ett productUpdate-anrop med tre produkter (title, seo{title, description}, descriptionHtml), mutationen utskriven av python med json.dumps(ensure_ascii=True) och inklistrad ordagrant. Skriptet kontrollerade osynliga tecken (inga) och att "användarvikt" saknas. userErrors: inga.
- Orörda: taggar, handle, status, pris.

## Återläsning (maskinell jämförelse, tecken för tecken mot f_skriv_1fix.json)
| Nr | Titel | SEO-titel | Meta | descriptionHtml |
|---|---|---|---|---|
| 10021 | lika | lika | lika | lika |
| 10024 | lika | lika | lika | lika |
| 10025 | lika | lika | lika | lika |

- Ordet "användarvikt" finns inte i någon text (titel, seo, meta, html) hos de tre.
- Leveranstidsmeningen ("Beställningsvaror kan ta upp till en vecka längre") finns i alla tre, och alla har taggen "På beställning". Regeln uppfylld.
- Taggar kvar (inkl. texter-klara), status ACTIVE, handle oförändrat.
- Obs: återläsningen jämfördes mot ett inklistrat svar i python; inga avvikelser, så ingen handskriven rättning behövdes.
