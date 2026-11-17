# Granskning 2 av kategoritext: hantlar (2026-11-17)

Oberoende granskning, bara läsning. Inga Shopify-anrop och inga nätverksanrop. Kontrollerna kördes med `python3 -I` mot absoluta sökvägar.

Granskat: `T['hantlar']` i `pilot_texter_v2.py` (brödtext, SEO-titel, meta). Övriga kategorier i filen är inte granskade.
Underlag: `underlag/hantlar.json` (`alla_titlar` 53 rader, `ovriga_titlar` 11, `marken`) och `hantlar_paket_live.json` (22 köpbara paket med största kg och lager).
Regler: `shopify-sync/docs/kategoritexter-standard.md`, avsnitt 2, 3, 4 och 8.
Jämförelse: `granskning-opus-hantlar.md` (granskning 1) och `pilot_texter_v2_efter_granskning1.py`.

## Vad som ändrats sedan granskning 1

- Brödtext, stycke 2: "där den tyngsta produkten är …" är ersatt med "som är den största vikten som anges för ett paket: Skivstångs- och Hantelset Gymstick, Vinyl, 60 kg". 60 kg har lagts till bland de kombinerade seten.
- Meta: nu "… Vikter från 0,5 kg upp till 60 kg i största paketet." (förslaget i A3 från granskning 1). Meningen "Minst 50 produkter." finns inte längre i metan.

## Davids krav: vikter i metan

**Största paketvikt, kontrollerad självständigt.** Jag läste alla 64 köpbara titlar (`alla_titlar` och `ovriga_titlar`) och tog fram alla kg-tal, även övre gränser i intervall som "2–12 kg" och "12,7–45,3 kg".
- Titlar med "set" eller "paket" (även engelska "Dumbbell Set"): 23 st. Den största vikten är 60 kg i *Skivstångs- och Hantelset Gymstick, Vinyl, 60 kg* (bland `ovriga_titlar`, lager 224 i liveläsningen). Näst störst är *Hantel- och Skivstångsset Tunturi Vinyl 50 kg*. Ett paket saknar kg i titeln (*Hantelset Tunturi Centuri Neopren med Ställ, 3 Par*).
- Ingen titel alls, paket eller inte, anger mer än 60 kg. Störst utanför paketen: *Skivstång Tunturi MX100 12,7–45,3 kg* och *Justerbar Hantel Tunturi MX Select MX85 5,6–38,6 kg Räfflad*.
- Paket-titlarna i underlaget och i `hantlar_paket_live.json` är exakt samma mängd (inga saknas åt något håll). Livefilens största värde är också 60 kg.

**Lägsta vikt.** 0,5 kg (*Pro Chrome Hantel 0,5kg - enkel*, huvudprodukt). Ingen titel anger lägre.

**Meta:** "Vikter från 0,5 kg upp till 60 kg i största paketet." uppfyller Davids krav. **OK.**

## Kontroll av varje påstående

| Påstående | Underlag | Resultat |
|---|---|---|
| "säljer hantlar, hantelset och justerbara hantlar" | Titlar som börjar med Hantel, Hantelset, Justerbar Hantel finns | OK (se A2) |
| Märken Tunturi, Gymstick, Toorx, Hammer, Christopeit med "bland annat" | `marken`: 26, 10, 7, 5, 2. Leverantören Gorilla Sports Norden nämns inte | OK |
| "minst 50 produkter" | 53 rader i `alla_titlar` (52 unika titlar, en titel står två gånger), golvat till 50 | OK |
| "går från 0,5 kg upp till 60 kg" | Lägst 0,5, högst 60 i alla titlar | OK |
| "60 kg, som är den största vikten som anges för ett paket: Skivstångs- och Hantelset Gymstick, Vinyl, 60 kg" | Största paketvikt i titlarna är 60 kg; titeln står ordagrant i `ovriga_titlar` och i livefilen | OK, faktafel F1 från granskning 1 är rättat |
| Hantelset på bland annat 15, 20 och 28 kg | Hantelset Gymstick Vinyl, 15 kg; Hantelset Tunturi, 20 kg; Hantelset Tunturi Vinyl, 28 kg | OK |
| Kombinerade hantel- och skivstångsset på bland annat 20, 50 och 60 kg | Christopeit 4-i-1, 20 kg; Tunturi Vinyl 50 kg; Gymstick Vinyl 60 kg | OK |
| Material bland annat gjutjärn, vinyl, neopren och gummi | Gjutjärn (Toorx, E Series), Vinyl (flera), Neopren (Toorx, Tunturi Centuri), Gummibelagd/gummerad/Gummiöverdrag | OK |
| "Tunturi har flest produkter" | 26 enligt `marken`, näst flest Gymstick 10 | OK |
| Exempel: Hantelset Tunturi Vinyl, 28 kg | Ordagrant i `alla_titlar` | OK |
| Exempel: Justerbar Hantel Hammer SmartLock med Vrid-och-lås-mekanism | Ordagrant i `alla_titlar` | OK |
| Exempel: Hantel Zipro HEX gummerad 2,5 kg, svart | Ordagrant i `alla_titlar` | OK |
| Meta: märken Tunturi, Gymstick, Toorx och Hammer med "bland annat" | `marken` | OK |

## Form och regler

- Brödtext 122 ord (60–200). **OK.**
- SEO-titel "Hantlar – Hantelset och justerbara hantlar": 42 tecken (högst 43), typordet först, unik i `alla_kollektioner_seo_live.json`. **OK.**
- Meta 152 tecken (inom 70–155 och standardens 120–155), inleds med verbet "Köp". **OK.**
- Första meningen har verb ("säljer"). **OK.**
- Inga priser eller belopp. "pris" finns bara i standardmeningen "Öppna en produkt för att se pris …"; SEO-titel och meta saknar pris. **OK.**
- Inga löften eller förbjudna superlativ (bäst, perfekt, ledande, garanti, gratis, leverans). "tyngsta" är borta. "största" avser en uppgift i titeln och är belagd. **OK.**
- "produkter", inte "modeller". **OK.**
- Uppräkningar av märken, vikter och material har "bland annat". **OK** (typuppräkningen, se A2).
- Inga tillbehör räknas bland huvudprodukterna (hantelställ, stänger m.m. ligger i `ovriga_titlar`). **OK** (8.2).

---

## FAKTAFEL

Inga. Faktafelet F1 från granskning 1 ("den tyngsta produkten") är rättat och inget nytt faktafel har tillkommit.

---

## ANMÄRKNINGAR (inte faktafel)

**A1. Metan anger inte antal (kvarstår, nu tydligare).** Avsnitt 4 kräver att metan nämner "typ, märken och lägsta pris eller antal". Pris får inte skrivas medan prisjobbet pågår, och "Minst 50 produkter." har tagits bort för att ge plats åt viktkravet. Metan uppfyller därmed inte standarden på den punkten. Att lägga tillbaka antalet ger mer än 155 tecken om inget annat kortas (till exempel "från bland annat Tunturi, Gymstick och Toorx"). David behöver avgöra om viktkravet ersätter antalskravet för hantlar.

**A2. Typuppräkningen saknar "bland annat" (kvarstår).** "hantlar, hantelset och justerbara hantlar" i första meningen och i metan är inte en bevisat fullständig uppräkning; kollektionen har också kombinerade hantel- och skivstångsset. Avsnitt 8.4. Samma mönster som övriga kategorier, och "hantlar" kan läsas som samlingsord. Möjlig rättelse: "säljer bland annat hantlar, hantelset och justerbara hantlar".

**A3. "i största paketet" i metan.** Formuleringen betyder i praktiken "den största vikten som anges i ett paketnamn" (se F1 i granskning 1). Brödtexten säger detta exakt, metan kortare. Godtas, eftersom den följer Davids beställning.

**A4. 60 kg vilar på en "övrig" produkt och på aktuellt lager (kvarstår).** `kg_i_titlar_max` i underlaget är 50,0. En automatisk kontroll mot det fältet flaggar 60 kg felaktigt; ange `hantlar_paket_live.json` som källa. Om 60 kg-setet säljs slut eller tas bort före skrivningen blir 50 kg rätt värde i både brödtext och meta. Kör om liveläsningen direkt före skrivning (8.1).

**A5. Dubblett i `alla_titlar`.** "Hantel TUNTURI Platinum Hex Gummibelagd Hantel, 37,5 kg" står två gånger (två produkter med samma titel). 52 unika titlar; "minst 50" håller ändå.

## Kan texten vilseleda?

Nej på någon faktapunkt. Vikterna, paketets namn, märken, exempeltitlar och material stämmer med underlaget och liveläsningen. Det som återstår är formfrågor (A1, A2) och färskheten i 60 kg-uppgiften (A4).

Antal faktafel: 0
