-- 10. Produkttitlar i Merchant Center som slutar på "Default Title" eller har andra tydliga rester från leverantörsdata.
--     Svarar på: hur många titlar behöver rättas, och vilka är mest synliga (annonsklick)?
WITH latest AS (
  SELECT offer_id, title FROM `PROJ.site_audit.merchant_products_bestofsports`
  WHERE d = (SELECT MAX(d) FROM `PROJ.site_audit.merchant_products_bestofsports`)
), ads AS (
  SELECT LOWER(item_id) AS item_id, SUM(clicks) AS klick, ROUND(SUM(cost)) AS kostnad
  FROM `PROJ.site_audit.google_ads_products_daily_bestofsports`
  WHERE d >= DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 28 DAY) GROUP BY 1
)
SELECT l.offer_id, l.title, IFNULL(a.klick, 0) AS klick_28d, IFNULL(a.kostnad, 0) AS kostnad_28d
FROM latest l LEFT JOIN ads a ON LOWER(l.offer_id) = a.item_id
WHERE REGEXP_CONTAINS(l.title, r'(?i)default title|\bdefault\b$') ORDER BY klick_28d DESC, l.title LIMIT 40;
