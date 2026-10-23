-- 9. Alla problem i Merchant Center räknade per typ (inte bara det första per produkt), med exempel.
--    Svarar på: vilka problem är vanligast, och vilka produkter ska rättas först?
WITH latest AS (
  SELECT offer_id, title, issues_json FROM `PROJ.site_audit.merchant_products_bestofsports`
  WHERE d = (SELECT MAX(d) FROM `PROJ.site_audit.merchant_products_bestofsports`)
), i AS (
  SELECT offer_id, title, JSON_VALUE(x, '$.description') AS problem, JSON_VALUE(x, '$.severity') AS allvar,
         JSON_VALUE(x, '$.attribute') AS falt
  FROM latest, UNNEST(IFNULL(JSON_EXTRACT_ARRAY(issues_json), [])) AS x
)
SELECT problem, ANY_VALUE(allvar) AS allvar, ANY_VALUE(falt) AS falt, COUNT(DISTINCT offer_id) AS produkter,
       ARRAY_TO_STRING(ARRAY_AGG(DISTINCT title LIMIT 5), ' | ') AS exempel
FROM i GROUP BY 1 ORDER BY produkter DESC LIMIT 30;
