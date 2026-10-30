-- 13. Ligger de skrivna produkttitlarna kvar efter nattens synk? Pilotens 20 produkter i Best of Sports, skrivna 2026-10-30.
--     Bakgrund: 12 titlar hade gått tillbaka till leverantörens original efter skrivning 2026-10-25 (orsak ej fastställd; Velomarket3 ändrar status och kanaler, inte titlar enligt produkthändelserna).
--     Kör efter varje nattlig synk (Shopify-synken i BigQuery körs på natten, kolla _synced_at):
--       bq query --use_legacy_sql=false --max_rows=40 "$(sed -e 's/PROJ/gorilla-sports-data/g' -e 's/SHOPDS/shopify_bestofsports/g' sql/analys/bos/13_kontroll_skrivna_titlar.sql)"
--     Läs så här: rad med titel_ok = false har fått en annan titel än den vi skrev. Status ARCHIVED betyder att leverantörssynken har arkiverat produkten (AL 1 var arkiverad 2026-10-28).
WITH forvantat AS (
  SELECT * FROM UNNEST(ARRAY<STRUCT<id STRING, titel STRING>>[
  ('10462768038154', 'Motionscykel Christopeit AL 1, magnetbroms med 8 nivåer, svart'),
  ('10541370114314', 'Motionscykel Toorx BRX 65 Comfort med ryggstöd'),
  ('10411848532234', 'Spinningcykel Hammer Speed Race SR med 10,1-tums pekskärm'),
  ('10472280850698', 'Löpband Christopeit TM 750S, hopfällbart, 1,75 hk'),
  ('10472307982602', 'Gåband Hammer Walk 2.0 Norsk, ekfinish, 1–6 km/h'),
  ('10472295596298', 'Löpband Tunturi Cardio Fit T5 med Bluetooth, hopfällbart'),
  ('10541268795658', 'Träningsbänk Tunturi UB70 Utility Bench, justerbar'),
  ('10507302764810', 'Träningsbänk Finnlo by Hammer Tricon Flex, hopfällbar'),
  ('10488326193418', 'Elcykel Giant Talon E+ 29", mountainbike, Asphalt Green'),
  ('10656694239498', 'Hopfällbar elcykel ADO Air 20 Ultra (2026), grå'),
  ('10471131250954', 'Barncykel Liv Tempt 20" mountainbike, AI Blue'),
  ('10588451635466', 'Kettlebell Tunturi Platinum Competition, tävlingsstandard'),
  ('10475621089546', 'Vikbart cykellås AXA Fold 85, 85 cm, Sold Secure Bronze'),
  ('10636604932362', 'Träningsbänk Gorilla Sports, rak, svart, 250 kg maxbelastning'),
  ('10636617875722', 'Viktskivor Movit gjutjärn med gummibeläggning, 30/31 mm, set 2–40 kg'),
  ('10472323186954', 'Pre-workout Trec Boogieman, Candy, 20 g per portion'),
  ('10475978981642', 'Cykelhjälm Nutcase Darth Lightnin\' Reflective MIPS, 56–60 cm'),
  ('10472233566474', 'Handpump Giant Control Mini Road+, svart, 160 psi'),
  ('10411495555338', 'Solglasögon Limar F30, vit, rökfärgad lins'),
  ('10588446589194', 'Kettlebell Tunturi PE 16 kg, PVC fylld med sand')
  ])
)
SELECT f.id, f.titel = p.title AS titel_ok, p.status, p.title AS titel_nu, p.updated_at, p._synced_at
FROM forvantat f LEFT JOIN `PROJ.SHOPDS.products` p ON REGEXP_EXTRACT(p.id, r'(\d+)$') = f.id
ORDER BY titel_ok, f.id;
