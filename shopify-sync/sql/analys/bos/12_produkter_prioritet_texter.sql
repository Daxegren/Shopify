-- 12. Vilka produkter ska få bättre titel och beskrivning först? Rangordnar på vad som redan ger trafik eller kostar annonspengar.
--     Underlag: Search Console (produktsidor, 90 dagar, SE), Google Ads per produkt (28 dagar) och Shopify-produkter (aktiva, lager).
--     Koppling: sökvägen /products/<handle> mot products.handle, och produkt-id i annonsernas item_id (shopify_SE_<produkt-id>_<variant-id>).
--     Svarar på: var ger textarbetet mest? Hög visning med låg klickfrekvens = titel och metabeskrivning. Annonskostnad utan köp = beskrivning, pris, förtroende.
--     Kör som: bq query --use_legacy_sql=false --max_rows=60 "$(sed 's/PROJ/gorilla-sports-data/g' sql/analys/bos/12_produkter_prioritet_texter.sql)"
WITH gsc AS (
  SELECT REGEXP_EXTRACT(url, r'/products/([^/?#]+)') AS handle, SUM(clicks) AS klick, SUM(impressions) AS visningar,
         SAFE_DIVIDE(SUM(sum_position), SUM(impressions)) + 1 AS position
  FROM `PROJ.site_audit.gsc_api_url_bestofsports_se`
  WHERE data_date >= DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 90 DAY) AND REGEXP_CONTAINS(url, r'/products/')
  GROUP BY 1
), ads AS (
  SELECT REGEXP_EXTRACT(item_id, r'(?i)shopify_[a-z]{2}_(\d+)_') AS produkt_id, SUM(cost) AS kostnad, SUM(clicks) AS annonsklick,
         SUM(conversions) AS konv
  FROM `PROJ.site_audit.google_ads_products_daily_bestofsports`
  WHERE d >= DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 28 DAY)
  GROUP BY 1
), p AS (
  SELECT handle, title, vendor, total_inventory, REGEXP_EXTRACT(id, r'(\d+)$') AS produkt_id
  FROM `PROJ.shopify_bestofsports.products` WHERE status = 'ACTIVE'
)
SELECT p.title, p.vendor, p.total_inventory AS lager, g.klick, g.visningar, ROUND(g.position, 1) AS position,
       ROUND(SAFE_DIVIDE(g.klick, g.visningar) * 100, 2) AS ctr_pct, ROUND(a.kostnad) AS annonskostnad, a.annonsklick, ROUND(a.konv, 1) AS annonskonv,
       -- poäng: visningar (synlighet vi kan få klick av) + annonskostnad utan köp (pengar som redan går åt)
       ROUND(IFNULL(g.visningar, 0) * 0.02 + IF(IFNULL(a.konv, 0) = 0, IFNULL(a.kostnad, 0), 0), 1) AS prioritet
FROM p
LEFT JOIN gsc g USING (handle)
LEFT JOIN ads a USING (produkt_id)
WHERE g.visningar > 0 OR a.kostnad > 0
ORDER BY prioritet DESC LIMIT 60;
