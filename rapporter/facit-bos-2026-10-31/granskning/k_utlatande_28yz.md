# Granskning k_28z (utkast) och k_28y (avvisade), 2026-11-05

Oberoende granskare, endast läsning. Källan hämtad live via Admin API (`shopify_api.py`, ShopifyKlient). Butik bekräftad: BEST OF SPORTS, 6f2e53-67.myshopify.com (bestofsports.se). Inget ändrat i Shopify, inget committat.

| nr | id | fil | dom | skäl |
|---|---|---|---|---|
| 28101 | 10472295989514 | k_28z_utkast.json | GODKÄND | Se nedan. |
| 28289 | 10676715323658 | k_28y_avvisade.json | UNDERKÄND (avvisning bekräftad) | Sittdynor till barnlåda på lastcykel = barntransport/säte för barn, fortfarande utanför enligt profilen; tunn källa (R3). |

## 28101 Barncykel Romet Jolene 24, Vit-Rosa

- Live: ACTIVE, "Barncykel ROMET Jolene 24, vit-rosa", productType Cyklar, taggar Cyklar, Romet, Velomarket (inte "På beställning"), en variant Default Title / 24130733-A / 6739 kr. Färgen i titeln låser ingen variant (R3).
- Fakta mot källan: aluminiumram, S (13 tum), 135–155 cm (en gång "enligt tillverkaren"), Shimano, 21 växlar, V-bromsar, fästpunkter för stänkskärmar och andra tillbehör: alla står entydigt i källan.
- Trasiga rader rätt utelämnade (R2): "135 cm - 135 cm - 135 cm - 135 cm" och "Shimano Tourney: 21 bromsok" (Tourney nämns inte).
- "Hjulvikt: 13,4 kg" rätt utelämnad: oklart om det är cykelns eller hjulens vikt. Syskonet 28202 anger "Cykelvikt", men syskonets källa får inte användas (R1). Öppen fråga till David enligt utkastarens `att_bekrafta`.
- Barnlinjen: inga säkerhets-, skydds-, komfort- eller utvecklingspåståenden ("säkerhet i åtanke", "bekväm", "säkerställer att ditt barn lär sig" m.fl. borta).
- Format: titel 35 tecken / 1 komma, SEO-titel 35 (≤43), meta 144 (70–155) med verb, inte cirkulär. `format_regler.py` och `skrivfil_kontroll.py`: 0 fel. "Passar för" finns. Standardblocket exakt som `b_skriv_24.json`. Ingen leveranstidsmening (rätt, taggen saknas).
- Unikhet: titel, SEO-titel och meta krockar inte med något annat utkast eller någon k_skriv_*-fil. 28202 (Jolene 24 Turkos, annat id och SKU) är ingen dubblett. Passar för-punkterna är identiska med 28202, vilket är tillåtet (R12 gäller titel, SEO och meta).

## 28289 Sittdynor Cargobike of Sweden (avvisad)

Live: ACTIVE, productType Cargobike-tillbehör, taggar Barncykel, Lastcykel, På beställning m.fl., variant 1521-22 / 2209 kr. Källan är en mening ("Setet innehåller två sittdynor med ryggstöd"). Produkten är säte/sittdyna för barntransport, som `frislappta_2026_11_05.barn` uttryckligen håller utanför. Avvisningen står; kan inte släppas.

## Resultat
1 godkänd, 0 rättas, 1 avvisning bekräftad. Öppen fråga till David: är "Hjulvikt 13,4 kg" cykelns vikt (då kan den läggas till i en senare omgång)?
