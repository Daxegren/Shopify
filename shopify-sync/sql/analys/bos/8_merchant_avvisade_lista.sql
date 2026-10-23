-- 8. Avvisade produkter i Merchant Center, en rad per produkt, med alla problem. Senaste ögonblicksbilden.
--    Svarar på: vilka produkter är det, och varför (till exempel "Guns and Parts" eller "Promotional overlay on image")?
SELECT offer_id, title, disapproved_countries AS avvisad_i, top_issue, issue_count, issues_json
FROM `PROJ.site_audit.merchant_products_bestofsports`
WHERE d = (SELECT MAX(d) FROM `PROJ.site_audit.merchant_products_bestofsports`)
  AND (is_disapproved OR IFNULL(disapproved_countries, '') != '')
ORDER BY top_issue, title;
