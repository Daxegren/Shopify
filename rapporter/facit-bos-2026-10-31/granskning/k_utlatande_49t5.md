# Granskningsutlåtande k_49t5 (2026-11-08)

Oberoende granskning enligt regelbok v1.12. Granskaren har bara läst i Shopify och har inte ändrat något där. Produkterna lästes live via Admin API (ShopifyKlient, BEST OF SPORTS).

| nr | id | dom |
|---|---|---|
| 49401 | 10612578976010 | RÄTTA |
| 49402 | 10636716376330 | GODKÄND |

## 49401 Cykelhandskar Disney Mickey: RÄTTA

Fält html. Före:
`<p>Cykelhandskarna Disney Mickey har Mickey-motiv och säljs under artikelnummer 59090. Enligt leverantören har handskarna damasker.</p>`

Efter:
`<p>De här cykelhandskarna har motiv med Disneyfiguren Mickey och säljs under artikelnummer 59090.</p>`

Skäl: Live ACTIVE, 59090, EAN 5902308590908, lager 1, ej spärrad. Typordet Cykelhandskar stöds av källtexten. Meningen om damasker stryks: ordet passar inte på handskar, ser maskinöversatt ut och är oklart (R2), och 'Enligt leverantören' är en arbetsterm (R11). Inledningen 'Disney Mickey har Mickey-motiv' är nästan cirkulär och skrivs om. Galaxus (återförsäljare, art.nr 59090) bekräftar Disney Mickey-cykelhandskar men anger grå/gul och vuxen målgrupp, medan andra källor anger barn. Färg, storlek och målgrupp är därför rätt utelämnade. Ingen tillverkarsida för EAN hittades, men v1.12 tillåter titelns uppgifter. Inga löften, ingen dubblett ('Mickey fuses' är en annan artikel och DRAFT). Formatet och standardblocket stämmer.

## 49402 Adduktortränare: GODKÄND

Live ACTIVE, 100936-00019-0001, EAN 4260438736360, lager 1001, vendor Gorilla Sports Norden, ej spärrad. Leverantörens egen sida https://www.gorillasports.se/products/adduktor-tranare (artikelnumret finns i bildfilnamnen) beskriver två klädda byglar med en fjäder i mitten som kläms ihop. Produkttypen är alltså entydig. Utkastet säger bara att produkten tränar adduktorerna på lårens insida. Det stämmer och är inget effektlöfte. Skaderisk, starkare muskler och symmetri är rätt utelämnade. Produkten bär ingen last, så v1.10 gäller inte. Typordet Adduktortränare är titelns ord sammanskrivet. Ingen dubblett eller SEO-krock i butiken. Formatet stämmer (titel och SEO 15 tecken, meta 116 tecken med verb), och standardblocket är exakt. Valfritt: utkastaren kan lägga till 'två klädda byglar som hålls ihop av en fjäder' ur leverantörssidan.

## Avvisade (k_49t5_avvisade.json): alla nio står fast

- Åtta avvisningar gäller exakta dubbletter med lager, där SKU eller EAN är desamma som i en annan aktiv annons (R12a): 49403, 49405, 49406, 49407, 49408, 49409, 49410 och 49411. För 49403 finns dessutom ett skyddslöfte i källan.
- 49404 (Toorx WBX-70): produkttypen är oklar, eftersom titeln anger både boxningssäck och fastball. Enligt v1.12 punkt 5 ska produkten avvisas.

Ingen avvisning är uppenbart fel.

## Kontrollerade tillverkar- och leverantörskällor

- 49401: https://www.galaxus.at/en/s3/product/disney-bike-gloves-mickey-59090-one-size-cycling-gloves-33036369. Det är en återförsäljare. Art.nr 59090 stämmer, men färg och målgrupp avviker.
- 49402: https://www.gorillasports.se/products/adduktor-tranare. Det är leverantörens egen sida. Artikelnumret och priset (159 kr) stämmer.
