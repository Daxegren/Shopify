# Våg 2k-2 (cyklar och cykeldelar): skrivrapport

Datum: 2026-11-03. Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_skriv_2.json` (34 produkter). Före-läge: `rapporter/shopify-original-2026-11-03/vag2k_2_fore.json` (34 poster, sparat före skrivning).

## Status: KLAR (34 av 34)

## Butik
BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info.

## Kontroll
Kopia: `rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2k2b/kopia.json`. Efter koordinatorns rättning av 6147 (24-tumshjul borttaget): 34 produkter, 0 FEL, 37 VARNINGAR (rubriken "Passar för" och tunn källa på tre produkter, godtagna).

## Skrivning
- Kanarie (3) och fem batcher om 6 produkter, sammanlagt 33 produkter, via productUpdate. Varje variabel togs fram av `vars_vag2k2.py` ur skrivfilen.
- Avvikelse: produkt 10472243265802 (SL-M2010-9R) skrevs först med fel stavning i tre fält ("växlereglage"/"växlindikator"). Rättad med ny productUpdate från skriptutskriften och läst tillbaka.
- Sista produkten 10472240972042 (SL-A050) skriven och läst tillbaka.
- Seo-titel lagrad som null där den är lika med titeln (avsett, Shopify).
- Handle och status oförändrade på alla 34.

## Återläsning
Alla 34: title, handle, status, seo.title, seo.description, descriptionHtml och tags lästes tillbaka med query. Titel, handle, status, seo och taggar jämförda mot skrivfilen (för hand). descriptionHtml jämförd för hand. Den maskinella jämförelsen är inte gjord eftersom svaren från Shopify inte kan matas in i skriptet.

## Taggen "texter-klara"
Lagd på alla 34 med tagsAdd, inga userErrors. Befintliga taggar finns kvar (verifierat i svaren, t.ex. "cykel", "Vikbar cykel", "växel", "Damcykel", "Tabou").

## Ändrat i Shopify
Ja: 34 produkters title, seo och descriptionHtml samt taggen "texter-klara". Inga handle eller status ändrade. Inga andra produkter berörda.

## Öppet
- Stickprov (20 procent, minst 10 av Sonnet-kontrollant) enligt processen är ej gjort.
- Nattkontroll av titlar för denna våg: ej gjord.
