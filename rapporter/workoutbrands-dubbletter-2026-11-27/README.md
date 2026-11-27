# Dubbletter bland jackkollektioner, Workout Brands, 2026-11-27 (genomfört efter Davids ja: "kör A, byt namn på höstjackorna, länka vinterjackorna")

## Gjort i Shopify (återläst)
- **A, herr:** `jacka-herr`: taggvillkoret `Jacket`+`men` ersatt av `jacka`+`Herr`; lagervillkoret (> 1) kvar. 134 → 161 produkter. Cirka 20 av dem är inte typen Jacka (västar, collegejackor, kappor, några hoodies och långärmade tröjor).
- **A, dam:** `jacka-dam`: `Jacket`+`Women` ersatt av `jacka`+`Dam`; lagervillkoret kvar. 100 → 164 produkter. Cirka 27 av dem är inte typen Jacka.
- **Omdirigeringar skapade:** `/collections/jackor-herr` → `/collections/jacka-herr`, `/collections/jackor-dam` → `/collections/jacka-dam`. De börjar gälla först när de två gamla kollektionerna är avpublicerade (verktygsspärr; se nedan).
- **Höstjackorna:** `jackor-herr-dam` har fått titeln "Höstjackor - Herr & Dam" och SEO-titeln "Höstjackor herr och dam" (handle oförändrad, 208 produkter). Ingen metabeskrivning ännu.
- Före-läge: `fore_regler.json`. Ångra regeln: ta bort villkoret `jacka`+`Herr`/`Dam` och lägg tillbaka `Jacket`+`men`/`Women`.

## Kvar (David kör i Cloud Shell)
- Avpublicera `jackor-herr` och `jackor-dam` från Webbshop: `wb_avpublicera.py --lista avpublicera_lista.csv`.
- Länka vinterjackorna i menyn `startsida-2-0-gymshark` (den som det publicerade temat använder för DAM/HERR): `wb_meny.py --meny startsida-2-0-gymshark --plan meny_plan.json`. Lägger "Vinterjacka" efter "Jacka" under DAM > KLÄDER och HERR > KLÄDER.
