# BOS: variantnamn (läsande kartläggning 2026-11-23)

Utlöst av en kundrapport (via David): på `styrketraningsset-tunturi-hantel-skivstangsset-20-kg-14tuscl454` heter varianterna "14TUSCL454" och "14TUSCL455", alltså SKU, utan att säga vad de är (priset är 639 respektive 799 kr och den andra är slutsåld). Toorx Olympic EVO Kettlebell har varianten "blue" på engelska. Davids önskan: se över variantnamn på alla produkter. **Inget är ändrat i butiken.**

## Resultat (4 003 aktiva produkter skannade)

| Typ | Antal varianter | Berörda produkter |
|---|---|---|
| SKU som variantnamn (flera varianter, titel = SKU) | 101 | se filen |
| Engelskt ord som variantnamn (blue, black, red, default title m.fl.) | 196 | se filen |
| Kodliknande namn | 6 | se filen |
| **Totalt** | 303 varianter | **209 produkter** |

Flest per märke: Tunturi 64, Giant 52, Hammer 19, Romet 18, Toorx 17. 189 av 303 varianter ligger på produkter med `price-change-job-active`. Alternativnamnet är generiskt ("Title" på 3 343 produkter utan riktiga varianter; "Variant" på 655 produkter) och bör inte alla bytas: många "Variant"-värden kan vara korrekta. Fil: `rapporter/bos-variantnamn-2026-11-23.csv` (typ, handle, titel, märke, variantnamn, SKU, prisjobbstagg).

## Varför det inte går att göra automatiskt på alla

Ett variantnamn som "14TUSCL454" kan bara ersättas med det som faktiskt skiljer varianterna åt (till exempel "Skruvlås" mot "Skruvfäste", eller en vikt). Den uppgiften finns inte i butiken; den finns hos leverantören (Velomarket-flödet) eller i produktbeskrivningen. En gissning skulle skapa felaktiga namn på något kunden köper. Engelska färgord (blue, black) kan däremot översättas säkert.

## Förslag i tre steg (alla kräver eget ja)

1. **Engelska färgord till svenska** (blue → Blå osv.): 196 varianter, mekaniskt och lågrisk. Före-fil och återläsning.
2. **SKU som variantnamn:** ta fram vad varianterna skiljer sig på (leverantörsdata, titel, beskrivning) per produkt, 101 varianter på cirka 40 produkter, och föreslå namn som David godkänner. Där skillnaden inte går att fastställa: namnge efter något verifierbart (till exempel "Variant 1"/"Variant 2" med SKU i beskrivningen) eller låt bli.
3. **Orsaken:** kontrollera om prissynken (Velomarket-flödet) skapar variantnamnen från SKU vid import. Annars återkommer felen på nya produkter.

Prisjobbstaggen: samma fråga som för taggförslagen (att byta variantnamn ändrar inte pris, men prisjobbet kan skriva varianter). Kräver beslut.

## Kundrapporten från 18 november (Armin Nasri, via David)

Länkarna: Tunturi-setet ovan (SKU som variantnamn) och Toorx Olympic EVO Kettlebell (variant "blue"). Rapporten säger att han "hittat två produkter med konstiga titlar"; jag ser bara en titelrelaterad sak i de två länkarna. Be David vidarebefordra den andra produkten, eller Armins ursprungliga mejl.
