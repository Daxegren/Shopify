# Plan: kvarvarande produkter i BEST OF SPORTS (inventering 2026-11-04)

Underlag: `rapporter/inventering-bos-2026-11-04/` (`alla_produkter.json` = läsning via API av alla 5 315 produkter, `plan_batcher.csv` = produkt per batch, `sparr_*.csv` = spärrade). Spärrarna är inlagda i `shopify-sync/config/sparrlista.json` och stoppar skrivfiler i `skrivfil_kontroll.py`.

| Läge | Antal |
|---|---|
| Aktiva produkter utan taggen texter-klara | 1 721 |
| Pilotens 20 (14 av dem är aktiva och otaggade) | 14 |
| Utanför tills vidare (barn 211, kosttillskott 86, massage 19, rullskridskor 15, vibrationsplattor 2) | 333 |
| Tidigare avvisade | 567 |
| Titeldubbletter (äldsta skrivs, övriga spärras) | 26 |
| **Att skriva** | **781** i 37 batcher om högst 25 |

Batchprefix `k_<grupp><bokstav>` (t.ex. `k_01a`). Ordning (störst och redan godkända faktatextgrupper först; försäljning/visningar går inte att läsa med appens behörighet, bara `read_products`):

| Grupp | Antal | Batcher |
|---|---|---|
| 01 elcyklar | 61 | 3 |
| 02 cyklar | 134 | 6 |
| 03 cykelhjälmar | 8 | 1 |
| 04 cykelbelysning | 15 | 1 |
| 05 sparkcyklar | 13 | 1 |
| 06 cykellås | 24 | 1 |
| 07 cykeldelar och tillbehör | 89 | 4 |
| 08 vikter, stänger, kabelhandtag | 126 | 6 |
| 09 fitnessmaskiner och stationer | 56 | 3 |
| 10 yoga, mattor, band, småutrustning | 91 | 4 |
| 11 övrigt (heterogen, granskas för hand först) | 164 | 7 |

Gruppindelningen är nyckelordsbaserad och ungefärlig; produkter flyttas vid utkast om källan säger annat. Faktatextläge och regelbok v1.4 gäller för allt. Grupp 03, 05 och 06 (hjälmar, sparkcyklar, lås) och 01 (elcyklar) är redan godkända faktatextgrupper.
