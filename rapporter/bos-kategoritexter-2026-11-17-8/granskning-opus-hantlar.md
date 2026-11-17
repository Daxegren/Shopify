# Granskning av kategoritext: hantlar (2026-11-17)

Oberoende granskning, bara läsning. Inga Shopify-anrop och inga nätverksanrop. Kontrollerna kördes med `python3 -I` mot absoluta sökvägar.

Granskat: `T['hantlar']` i `pilot_texter_v2.py` (brödtext, SEO-titel, meta).
Underlag: `underlag/hantlar.json` (53 köpbara huvudprodukter i `alla_titlar`, 11 köpbara övriga i `ovriga_titlar`) och `hantlar_paket_live.json` (22 köpbara produkter med "set"/"paket" i titeln, med största kg och lager).
Regler: `shopify-sync/docs/kategoritexter-standard.md`, avsnitt 2, 3, 4 och 8.

## Kontroll av Davids krav (meta och vikter)

**(1) Största paketvikt.**
- I liveläsningen har *Skivstångs- och Hantelset Gymstick, Vinyl, 60 kg* störst vikt i titeln: 60 kg, lager 224, alltså köpbar. Näst störst är *Hantel- och Skivstångsset Tunturi Vinyl 50 kg* (lager 3).
- Produkten finns bland `ovriga_titlar`, inte bland huvudprodukterna. Förklaringen är att titeln börjar med "Skivstångs-". Därför står `kg_i_titlar_max` som 50,0 i underlaget och inte 60.
- Jag gick igenom alla 64 titlar i `alla_titlar` och `ovriga_titlar` och letade efter titlar med större vikt utan ordet set eller paket. Ingen titel anger mer än 60 kg. De största är *Skivstång Tunturi MX100 12,7–45,3 kg* (45,3 kg), *Justerbar Hantel Tunturi MX Select MX85 5,6–38,6 kg Räfflad* (38,6 kg) och *Hantel … Platinum Hex …, 37,5 kg*.
- Alla titlar med "set" eller "paket" i underlaget finns också i liveläsningen, och liveläsningen innehåller inga titlar som saknas i underlaget.
- Brödtexten och metan anger båda 60 kg. **Det stämmer.**

**(2) Lägsta vikt.** Den lägsta vikten i någon titel är 0,5 kg (*Pro Chrome Hantel 0,5kg - enkel*, en huvudprodukt). Texten och metan anger 0,5 kg. **Det stämmer.**

## Kontroll av varje påstående i brödtexten (3)

| Påstående | Underlag | Resultat |
|---|---|---|
| "säljer hantlar, hantelset och justerbara hantlar" | Titlar som börjar med Hantel, Hantelset och Justerbar Hantel finns | OK |
| Märkena Tunturi, Gymstick, Toorx, Hammer och Christopeit, med "bland annat" | `marken`: Tunturi 26, Gymstick 10, Toorx 7, Hammer 5, Christopeit 2. Inget leverantörsnamn nämns (Gorilla Sports Norden) | OK |
| "minst 50 produkter" | 53 köpbara huvudprodukter, golvat till tiotal: 50 | OK |
| "Vikterna i produktnamnen går från 0,5 kg upp till 60 kg" | Lägsta 0,5 kg, högsta 60 kg (övrig produkt, köpbar) | OK |
| "där den tyngsta produkten är Skivstångs- och Hantelset Gymstick, Vinyl, 60 kg" | Underlaget har bara vikter ur titlarna, inte produkternas totalvikt | **FEL, se F1** |
| Hantelset på bland annat 15, 20 och 28 kg | Hantelset Gymstick Vinyl, 15 kg; Hantelset Tunturi, 20 kg; Hantelset Tunturi Vinyl, 28 kg | OK |
| Kombinerade hantel- och skivstångsset på bland annat 20, 50 och 60 kg | Christopeit 4-i-1, 20 kg; Tunturi Vinyl 50 kg; Gymstick Vinyl 60 kg | OK |
| Material i titlarna: bland annat gjutjärn, vinyl, neopren och gummi | Gjutjärn (Toorx, E Series), Vinyl (flera), Neopren (Toorx, Tunturi Centuri), Gummibelagd, gummerad och Gummiöverdrag (Tunturi, Zipro) | OK |
| "Tunturi har flest produkter" | 26 enligt `marken` (26 titlar), näst flest Gymstick med 10 | OK |
| Exempel: Hantelset Tunturi Vinyl, 28 kg | Ordagrant i `alla_titlar` | OK |
| Exempel: Justerbar Hantel Hammer SmartLock med Vrid-och-lås-mekanism | Ordagrant i `alla_titlar` | OK |
| Exempel: Hantel Zipro HEX gummerad 2,5 kg, svart | Ordagrant i `alla_titlar` | OK |

## Form och regler (4)

- Brödtexten har 117 ord, inom 60–200. **OK.**
- SEO-titeln "Hantlar – Hantelset och justerbara hantlar" har 42 tecken (högst 43). Typordet står först, följt av en avgränsare. Ingen annan kollektion i `alla_kollektioner_seo_live.json` har samma titel. **OK.**
- Metan har 145 tecken, inom 70–155 och även inom standardens 120–155. Den inleds med verbet "Köp". **OK.**
- Den första meningen i brödtexten har ett verb ("säljer"). **OK.**
- Texten innehåller inga prisuppgifter. Ordet "pris" förekommer bara i standardmeningen "Öppna en produkt för att se pris …", som inte anger något belopp. **OK.**
- Texten innehåller inga löften och inga förbjudna superlativ som "bäst", "perfekt" eller "ledande". **OK.** Superlativet "tyngsta" behandlas under F1.
- Texten skriver "produkter", inte "modeller". **OK.**
- Uppräkningarna av märken, vikter och material har "bland annat". **OK.** Om typuppräkningen, se A2.

---

## FAKTAFEL

### F1. "den tyngsta produkten" saknar stöd och är sannolikt fel

Underlaget innehåller bara de vikter som står i titlarna. Det säger ingenting om hur mycket en produkt väger totalt. Flera hantelset anger bara ett viktintervall per hantel och väger troligen mer än 60 kg sammanlagt:

- *Hantelset Tunturi PU Pro, 10 Par, 2–12 kg*: tio par mellan 2 och 12 kg väger normalt långt över 60 kg.
- *Hantelset Tunturi Platinum Hex Rubber, 1–10 kg*.

Påståendet att 60 kg-setet är "den tyngsta produkten" kan därför inte beläggas med underlaget och är troligen fel. Davids krav gäller den största vikten bland paketen *enligt titlarna*, och det ska formuleras så.

- **Före:** "Vikterna i produktnamnen går från 0,5 kg upp till 60 kg, där den tyngsta produkten är Skivstångs- och Hantelset Gymstick, Vinyl, 60 kg."
- **Efter:** "Vikterna i produktnamnen går från 0,5 kg upp till 60 kg, som är den största vikt som anges för ett paket: Skivstångs- och Hantelset Gymstick, Vinyl, 60 kg."

---

## ANMÄRKNINGAR (inte faktafel)

**A1. Metan nämner inte antal.** Standarden (avsnitt 4) säger att metan ska nämna "typ, märken och lägsta pris eller antal". Priser får inte skrivas medan prisjobbet pågår, men metan anger inte heller något antal. Davids viktkrav har tagit platsen. Om David vill följa standarden fullt ut går det inte att lägga till "Minst 50 produkter." utan att korta något annat, eftersom metan då blir längre än 155 tecken. David behöver avgöra om viktkravet ersätter antalskravet för den här kollektionen.

**A2. Typuppräkningen saknar "bland annat".** "säljer hantlar, hantelset och justerbara hantlar" är en uppräkning som inte är bevisat fullständig. Kollektionen innehåller också kombinerade hantel- och skivstångsset, och sådana nämns senare i texten. Avsnitt 8.4 kräver "bland annat" före uppräkningar som inte är fullständiga. Mönstret är detsamma som i första meningen för de andra kategorierna, och "hantlar" kan läsas som ett samlingsord, så jag räknar det inte som faktafel. Möjlig rättelse: "säljer bland annat hantlar, hantelset och justerbara hantlar".

**A3. Metan kan läsas som att även det minsta paketet väger 0,5 kg.**
- **Före:** "Från 0,5 kg upp till 60 kg i största paketet."

Lägsta vikten 0,5 kg gäller en enskild hantel, inte ett paket. Davids formulering är "vikterna går från 0,5 kg …".
- **Förslag:** "Vikter från 0,5 kg upp till 60 kg i största paketet." Metan får då 152 tecken.

Samma sak gäller "största paketet": med 60 kg avses den största vikten som *anges i en titel* (se F1). Formuleringen godtas här eftersom den följer Davids beställning ordagrant.

**A4. 60 kg kommer från en "övrig" produkt.** `kg_i_titlar_max` i underlaget är 50,0, eftersom 60 kg-setet inte räknas som huvudprodukt. Om `kategori_kontroll.py` jämför talen i texten med `kg_i_titlar_max` kommer kontrollen att flagga 60 kg felaktigt. Ange `hantlar_paket_live.json` som källa för 60 kg i kontrollen. Om 60 kg-setet blir slutsålt eller tas bort före skrivningen blir 50 kg rätt värde. Enligt avsnitt 8.1 ska därför liveläsningen köras om direkt före skrivningen. Setets pris i underlaget, 1 844,10 kr, har ören, vilket tyder på att prisjobbet påverkar produkten. Det påverkar inte texten, som saknar priser.

**A5. Märkesantal i titlar och i vendor-fältet skiljer sig åt.** Gymstick står i 6 titlar men har 10 produkter enligt `marken`, som bygger på vendor-fältet (det fält i Shopify som anger produktens märke eller leverantör). Texten påstår ingen ordning mellan Gymstick och Toorx, så det har ingen betydelse för texten. Om en senare version skriver "Gymstick har näst flest" behöver det kontrolleras.

**A6. Exemplet med Zipro.** Zipro finns bara i ett exempel. Märket är köpbart, med 1 produkt, så det är tillåtet.

## Kan texten vilseleda? (5)

Ja, på en punkt: "den tyngsta produkten" (F1). En kund kan tro att inget paket i kollektionen väger mer än 60 kg, fast hantelset med tio par troligen väger mer. Rättelsen i F1 tar bort den risken. Metan (A3) kan vilseleda något om vad 0,5 kg avser. I övrigt stämmer alla tal, märken, exempeltitlar och vikter med underlaget och liveläsningen.

Antal faktafel: 1
