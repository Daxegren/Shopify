-- 6. Produkter som kostar annonspengar men inte säljer (senaste 28 dagarna), med lagerstatus.
--    Svarar på: hur mycket går till produkter utan köp, och är de slut i lager?
WITH a AS (
  SELECT LOWER(item_id) AS item_id, ANY_VALUE(title) AS title, ANY_VALUE(currency) AS currency, SUM(cost) AS kostnad,
         SUM(clicks) AS klick, SUM(conversions) AS konv, SUM(conversions_value) AS varde
  FROM `PROJ.site_audit.google_ads_products_daily_bestofsports`
  WHERE d >= DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 28 DAY)
  GROUP BY 1
), tot AS (SELECT SUM(kostnad) AS k FROM a)
SELECT item_id, title, currency, ROUND(kostnad) AS kostnad, klick, ROUND(konv, 1) AS konv, ROUND(varde) AS varde,
       ROUND(kostnad / (SELECT k FROM tot) * 100, 1) AS andel_av_kostnad_pct
FROM a WHERE konv = 0 AND klick >= 5 ORDER BY kostnad DESC LIMIT 30;
