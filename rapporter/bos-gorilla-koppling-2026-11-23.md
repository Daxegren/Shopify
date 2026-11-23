# BOS och Gorilla Sports: kopplingen (läsande kartläggning 2026-11-23)

Utlöst av David: "Det borde vara fler produkter från Gorilla Sports, vi måste se över kopplingen mellan Gorilla Sports och Best Of Sports och potentiellt bygga en egen sync." **Inget är ändrat.**

## Läge i BOS i dag (läst live)

| Märke i BOS | Aktiva | Utkast | Arkiverade | Totalt |
|---|---|---|---|---|
| Gorilla Sports Norden | 282 | 337 | 35 | 654 |
| Gorilla Sports | 8 | 18 | 1 | 27 |
| **Summa** | **290** | **355** | **36** | **681** |

232 av de aktiva har lager över 0. 279 av de 681 har `price-change-job-active`. Mer än hälften av Gorilla Sports-produkterna i BOS är alltså **utkast**. Det är den främsta förklaringen till att kategorierna (power rack, bänkpress, viktställ) saknar Gorilla-produkter: de finns, men ligger som utkast med lager 0.

## Vad som är känt om hur de kommer in

Det finns ingen dokumenterad Gorilla Sports-sync i det som finns i repot eller i Velomarket-synken (Lovable-projektet "BOS - Velomarket", som bara hämtar från Velomarket). Gorilla-produkterna i BOS kommer alltså från något annat flöde (manuell import, CSV eller ett tidigare verktyg). Det är **inte fastställt** hur, och inte varför så många är utkast. Det är det första som behöver utredas.

## Vad som saknas för att avgöra om en egen sync behövs

1. Hur många produkter Gorillas egen butik har och hur många av dem som finns i BOS (kräver läsning av Gorillas butik; BOS-sessionen har bara BOS-uppgifter, så David eller Cloud Shell behöver ge en läsning).
2. Varför 337 produkter är utkast (leverantörens lager 0, manuell avpublicering eller en tidigare synk som sätter utkast vid slutsålt?).
3. Vilken källa som ska gälla: Gorillas butik, deras leverantörsflöde eller HQ:s produktregister. Gorillas butik ägs av huvudkontoret (David äger den inte), så en egen sync mot den kräver HQ:s medgivande och en egen app (vi använde en BigQuery Sync-token som nödlösning tidigare; det ska inte bli permanent).

## Förslag

Steg 1 (läsande, inget byggs): jämför Gorillas butik och BOS per SKU: vilka finns i båda, vilka saknas i BOS, och vilka av BOS-utkasten som har lager i Gorilla. Steg 2: beslut om egen sync, med den befintliga Velomarket-synken som förebild (marginalregler, pris- och lagerlogik, `price-guard`), men en egen källa och egna regler.
