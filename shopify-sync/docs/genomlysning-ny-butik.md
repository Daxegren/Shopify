# Genomlysning av en ny butik (läsande): körbar metod med lärdomar från BEST OF SPORTS

Skapad 2026-11-17 av koordinatorn på Davids uppdrag (kör över natten på en annan butik). Filen fylls bara på. Allt här är LÄSNING. Inga skrivningar i någon butik, inga nycklar i chatt eller repo, aldrig `switch-shop` (David byter koppling själv). Gorilla Sports: bara läsning, analys och utkast tills David säger annat. Läs först: `CLAUDE.md`, `shopify-sync/docs/BESLUTSLOGG.md`, `LARDOMAR.md`, `seo-geo-genomlysning-metod.md`, `ny-butik-checklista.md`.

## Steg 0. Vilken butik, och är kopplingen rätt?
`get-shop-info` (namn, domän, valuta, plan). Är det BEST OF SPORTS (`6f2e53-67.myshopify.com`): stoppa, den är redan genomlyst. Notera `taxesIncluded` och marknader/språk i butiken; de styr hur marginal och priser läses.

## Steg 1. Är butiken aktiv? (ShopifyQL, `run-analytics-query`)
- `FROM sales SHOW orders, gross_sales, net_sales TIMESERIES month SINCE -12m UNTIL today`
- `FROM sales SHOW gross_sales, net_sales, orders GROUP BY product_title ORDER BY gross_sales DESC LIMIT 20 SINCE -90d UNTIL today`
- `FROM sessions SHOW sessions, conversion_rate GROUP BY session_country SINCE -90d UNTIL today` (och per enhet, referrer).
Lärdom BOS: 34 ordrar och cirka 52 000 kr brutto på 12 månader (november 2026: 0 ordrar). Prioritering efter omsättning går bara om butiken har omsättning; annars prioriteras efter synlighet (Search Console) och risk.

## Steg 2. Katalog och kollektioner (`graphql_query`, högst 100 per sida)
Antal produkter per status, produkter utan SEO-titel/meta/beskrivning, dubbletter (samma titel), taggar (särskilt jobbtaggar som `price-change-job-active`), leverantörer och produkttyper. Kollektioner: antal, smarta mot manuella, regler, tomma, avpublicerade, överlappande namn och handles med suffix (`-se`, `-1`, `-kopia`). Antal omdirigeringar (`urlRedirects`). Lärdomar BOS: 112 av 349 kollektioner tomma, 15 par med `-se` som gav 404 men hade visningar, felaktiga kollektionsregler (märke "Christopeit Sport Germany" gav 0 medlemmar; cyklar innehöll kosttillskott).

## Steg 3. Priser och marginal
`inventoryItem.unitCost` mot variantens `price` och `compareAtPrice`. Marginal efter moms = `(pris/1,25 − inköp)/(pris/1,25)` (justera om priser inte inkluderar moms). Redovisa median, kvartiler, varianter under inköpspris, över 60 %, och jämförpris som är högre än priset. Lärdomar BOS: median 40 % på 4 510 varianter; 10 varianter under inköpspris; ett fel inköpspris (en annan produkts pris via id-uppslag) och regeln "sänk aldrig priset" låste kvar 92 för höga priser (AXA 5 339 kr mot 679 kr). Kontrollera om en prisapp (Bulk Price Editor eller liknande) har återställningsinställning innan kampanjtaggar tas bort. Jämförpris ska vara det lägsta priset de senaste 30 dagarna (EU:s prisinformationsregler; allmän kunskap, inte juridisk rådgivning).

## Steg 4. Textkvalitet (urval, 150–300 produkter, olika kategorier)
Mät: saknad meta, längd (titel högst 70, SEO-titel högst 43 + suffix, meta 70–155), cirkulär inledning ("X är en X"), "Vanliga frågor" och "Om märket" kopierade från leverantör, språkblandning, tal som inte stämmer, `&`, tomma beskrivningar, HTML-fel. Lärdomar BOS: 45 % av utkasten godkändes direkt, 43 % rättades, 11 % underkändes; 87 % av rättningarna var innehåll; automatiska kontroller fångar cirka 9–22 %.

## Steg 5. Struktur och SEO
Search Console behöver Davids egen Cloud Shell-inloggning (`shopify-sync/scripts/gsc_export.py`); ingen nyckel i chatt, aldrig Windsor.ai. Utan den: bara strukturfynd. Publik genomsökning (högst 3 anrop per sekund, följ robots.txt, Cloudflare kan stoppa): föräldralösa sidor, klickdjup, inlänkar per kollektion, ankartexter, trasiga länkar. Lärdomar BOS: kategorisidor på position 26–77, märkessidor bäst (position 10–16), brödsmulan länkade 6 av 349 kategorier tills den byggdes om, en omdirigering gäller först när källsidan avpublicerats.

## Steg 6. Leverantörsflöden och automation
Finns en synk mot leverantör: hur matchas produkter (id eller artikelnummer), vilka jobb skriver pris, finns "sänk aldrig priset"-regler, jobbtaggar och schemalagda återställningar? Lärdom BOS: ett jobb slog upp på id medan leverantörens adress tolkade numret som artikelnummer och skrev fel produkts inköpspris; en huvudbrytare för prisskrivning, AV som standard, är rätt skydd.

## Steg 7. Leverans
1. Rapport i `rapporter/genomlysning-<butik>-<datum>/` med siffror, och vad som är fakta respektive bedömning.
2. Utkast till butiksprofil (`butiksprofil-<butik>.json`, platshållare för allt som kräver Davids svar) och spärrlistekandidater (barn, kosttillskott, skydd, hälso- och kroppspåståenden, läkemedel).
3. Prioriterad backlog (högst 15 punkter, effekt mot insats) och en lista "Behöver Davids ja".
4. Beslutsfil `rapporter/beslut-<datum>-<n>.md` med exakt de fem rubrikerna, överst "Behöver Davids ja: N punkter". Nya lärdomar sist i `LARDOMAR.md`, rad i `ANDRINGSLOGG.md`.
