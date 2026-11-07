# Granskningsutlåtande k_38a (2026-11-07)

Granskaren har bara läst i Shopify och inte ändrat något där. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient) mot BEST OF SPORTS på bestofsports.se. Underlaget är CLAUDE.md, `regler-v1.md` (R1, R3, R7, R12, R12a, R13, v1.6–v1.10), BESLUTSLOGG (Davids beslut 2026-11-07 om storlek ur artikelnummer), LARDOMAR, butiksprofilen och formatet i `k_utlatande_36ab`. `skrivfil_kontroll.py` gav 0 fel.

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_38a.json`.

## Resultat

| nr | id | produkt | dom |
|---|---|---|---|
| 38001 | 10565633638666 | Kona Rove AL/DL, Gloss Aragorn, 52 cm | GODKÄND |
| 38002 | 10682105987338 | Kona Dew (2027), Gloss Metallic Peridot, XL (57 cm) | RÄTTA (SEO-titel) |
| 38003 | 10682106052874 | Kona Dew (2027), Gloss Fancy Karman, XL (57 cm) | RÄTTA (SEO-titel) |

## Storleken är verifierad för exakt artikelnummer

Utkastaren härledde storleken ur artikelnumrets slutsiffror. Granskaren hittade Konas egna produktdata, där exakt artikelnummer står med storlek. Härledningen behövs alltså inte, och uppgiften i `att_bekrafta` bör ändras från "härledd" till "verifierad hos Kona".

| artikel | Konas variant | källa |
|---|---|---|
| B37RVADRDSHIN52 | 52 (av 48/50/52/54/56/58) | [en-eu.konaworld.com/products/rove-al-dl-37](https://en-eu.konaworld.com/products/rove-al-dl-37) |
| B37DWGNSHIN06 | XL (SM 01, MD 03, LG 05, XL 06) | [en-eu.konaworld.com/products/dew-b37-gn](https://en-eu.konaworld.com/products/dew-b37-gn) |
| B37DWBL1SHIN06 | XL (SM 01, MD 03, LG 05, XL 06) | [en-eu.konaworld.com/products/dew-b37-bl1](https://en-eu.konaworld.com/products/dew-b37-bl1) |

Egen live-källa anger M = 52 cm (Rove) och XL = 57 cm (Dew), så "M (52 cm)" och "XL (57 cm)" stämmer.

## 38001 Rove AL/DL 52 cm: GODKÄND

Live: ACTIVE, en variant, 18 399 kr, lager 0, med taggen På beställning. Varje uppgift står i egen källa: ram och gaffel i Kona 6061-aluminium (gaffeln "Disc"), Shimano Cues, 9 växlar, Shimano Sora mekaniska, Maxxis Rambler 700x40mm, 700c slanglösa fälgar, skärmar ingår och fästpunkter för flaskhållare. Inga prestanda- eller kvalitetsord. Leveranstidsmeningen finns, och standardblocket är exakt. Titeln har 49 tecken och 2 kommatecken, SEO-titeln 43 tecken och metan 133 tecken med verb. Produkten skiljer sig från syskonet 10530213429514 (…54, M/L) genom "52 cm".

## 38002 och 38003 Dew XL: RÄTTA

Fakta står i egen (engelsk) källa. "Skivbromsar" står inte där (bara "Tektro HD-M280 hydraulic"), men [Konas sida för Dew 2027](https://en-eu.konaworld.com/products/dew-37) anger Tektro M280-ok och 160 mm-skivor. Uppgiften får därför stå enligt R1 v1.6. Leveranstidsmeningen och standardblocket är exakta. Titlarna har 57 och 53 tecken och 2 kommatecken, metan 137 och 133 tecken. De två utkasten skiljer sig från varandra genom färgen och från syskonen (S/M/L) genom XL.

| nr | fält | före | efter |
|---|---|---|---|
| 38002 | seo_title | Kona Dew (2027), Peridot, XL (57 cm) | Cykel Kona Dew (2027), Peridot, XL (57 cm) |
| 38003 | seo_title | Kona Dew (2027), Fancy Karman, XL | Cykel Kona Dew (2027), Fancy Karman, XL |

Skäl: R7 kräver att typordet står först även i SEO-titeln. Syskonet Fancy Karman (10682105561354) har "Cykel Kona Dew (2027), …". Efter rättningen har SEO-titlarna 42 och 39 tecken. Båda är unika mot alla utkast, alla skrivfiler och live. "(57 cm)" ryms inte i 38003 inom 43 tecken.

## Iakttagelse (ingen åtgärd i den här batchen)

Det skrivna syskonet Kona Dew Peridot (10682105626890) har SEO-titeln "Kona Dew (2027), Gloss Metallic Peridot" utan typord. Om den ska rättas krävs en egen korrigeringsfil.
