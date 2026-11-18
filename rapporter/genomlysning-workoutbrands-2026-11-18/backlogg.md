# Prioriterad backlog, Workout Brands (högst 15 punkter, effekt mot insats)

Allt nedan är förslag. Inget är utfört. Punkter som skriver i butiken kräver Davids ja (se `rapporter/beslut-2026-11-18.md`).

| # | Åtgärd | Effekt | Insats | Risk | Kräver |
|---|---|---|---|---|---|
| 1 | Kontrollera inköpspriser: 1 927 produkter har marginal över 90 % eller pris under inköp (`data/sparr_inkopspris_misstankt.csv`); fastställ enhet/valuta med leverantören | Hög (prisbeslut hänger på detta) | Låg | Låg (läsning) | David/leverantör |
| 2 | Identifiera appen bakom `price-change-job-active`/`BF26` (2 897 aktiva produkter, 10 % rabatt via jämförpris) och dess återställningsinställning före Black Friday | Hög | Låg | Hög om taggar rensas fel | David |
| 3 | Aktivera spärrlista (barn, outlet, Out of stock, prisjobb, dubbletter, titel med storlek) | Hög (skyddar mot fel textskrivning) | Låg | Låg | David |
| 4 | Avgränsa bottrafik (251 563 sessioner/90 d, 88 % desktop direkt, USA/Brasilien 0 % konvertering) så att mätningen går att lita på | Hög (all mätning) | Medel | Låg | David (Cloudflare/analys) |
| 5 | Hämta Search Console-export (`gsc_export.py sc-domain:workoutbrands.com`) | Hög (visar vad som drar trafik) | Låg | Låg | David (Cloud Shell) |
| 6 | Undersök 466 aktiva produkter som saknas i sitemapen (373 med lager): är de ej publicerade i Online Store? | Hög om försäljningskanal saknas | Låg | Låg | David |
| 7 | Fyll SEO-titel för 6 988 produkter (nu temats reservtitel) och SEO-meta för 3 059; en kategori i taget | Medel–hög | Medel | Medel | David (ton, standard) |
| 8 | Rensa produkttext: ta bort upprepat produktnamn först i texten (81 %), rätta ordföljd/grammatik, 61 engelska och 39 blandade texter | Medel | Hög | Medel | David (textregler) |
| 9 | Städa kollektioner: 42 tomma, 4 "test", 4 "radera", 15 dubblettitlar, 39 handles med suffix; gör efter Black Week | Medel | Låg | Medel (avpublicering kräver omdirigering) | David, tidigast 2026-12-01 |
| 10 | Länka de 350 kollektioner (≥10 produkter) som saknar länk på genomsökta sidor; mät med brödsmula först | Medel | Medel | Låg | David |
| 11 | Märkesmodell: normalisera `vendor` (UC Men/UC Ladies/MT Men = linje, "Out of stock"/"outlet" = status); 80 produkter saknar typ; 17 skiftlägesdubbletter i taggar | Medel | Hög | Medel | David |
| 12 | Meddela meta för 11 sidor, rätta dubbla H1 på 10 sidor, saknad H1 på `/pages/contact` | Låg–medel | Låg | Låg | David (tema) |
| 13 | Ta bort eller dölj oanvända menyer ("Startsida 2.0 (nelly.com)", "GYMSHARK") | Låg | Låg | Låg | David |
| 14 | Rätta 97 titlar som slutar på enskild storlek och 171 dubbletitlar (366 produkter); sammanslagning efter beslut | Låg–medel | Hög | Medel | David |
| 15 | Kontrollera momsvisning per marknad (Sverige inkl. moms, Danmark exkl. i nuvarande ordrar) och jämförpris mot lägsta pris 30 dagar | Medel | Låg | Medel | David |
