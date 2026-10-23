-- 7. Hur många produkter har problem i Merchant Center, och vilka problem är vanligast? Senaste ögonblicksbilden.
--    Svarar på: tappar produkterna synlighet i Shopping och gratis listningar på grund av fel i flödet?
WITH latest AS (
  SELECT * FROM `PROJ.site_audit.merchant_products_bestofsports`
  WHERE d = (SELECT MAX(d) FROM `PROJ.site_audit.merchant_products_bestofsports`)
)
SELECT IF(is_disapproved, 'avvisad', IF(issue_count > 0, 'godkänd med problem', 'utan problem')) AS status,
       IFNULL(NULLIF(top_issue, ''), '(inget)') AS vanligaste_problem, COUNT(*) AS produkter
FROM latest GROUP BY 1, 2 ORDER BY produkter DESC LIMIT 25;
