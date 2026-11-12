# Andra granskningen av pilottexterna, kategorisidor BOS (2026-11-12)

Oberoende granskare (Opus), endast läsning. Jämfört: `pilot_texter.py` mot `underlag/<handle>.json`; siffror och märken räknade i `alla_titlar`. Samma arbetssätt som `granskning-opus.md`. Rättelserna nedan är gjorda i `pilot_texter.py` (utkast), kontroll 0 fel; underlagsfelen är inte åtgärdade (se beslutsfilen).

**Gemensamt (alla tio):** `pilotutkast.md` och `pilot/*.json` stämmer med `pilot_texter.py`. Bara `<p>`, inget `&`. 61–84 ord, SEO-titel 27–43 tecken, meta 131–155 tecken, alla unika. Första meningen har verb och är inte cirkulär. Inga löften, hälsa, kvalitet, leveranstid, frakt eller ursprung. Velomarket och Gorilla Sports Norden nämns inte. Alla "minst N" rätt golvade, prisspann rätt avrundade, alla 30 exempelmodeller ordagrant ur `alla_titlar`.

Regeln från lärdomen 2026-11-05 ("bland annat" före varje ofullständig uppräkning) gav de flesta fynden.

## Resultat per kategori

| Kategori | Utfall | Fel som rättades (före → efter) | Kvarstår som kontrollpunkt (underlag) |
|---|---|---|---|
| motionscykel | godkänd | – | dubbletter i underlaget (texten säger "produkter", påverkas inte) |
| roddmaskin | godkänd | – | 61 ord, nära golvet 60 |
| crosstrainer | godkänd | – | "minst 20" = exakt 20 (ingen marginal); valfritt "nivåer" i st. f. "motståndsnivåer" (titeln säger "8 Nivåer") |
| kettlebell | godkänd | – | två riktiga kettlebells ligger bland övriga (påverkar inte texten) |
| lopband | godkänd | – | "GT1.0 Treadmill" och "Treadmill BH FITNESS Nydo" (engelska titlar) ligger bland övriga; kan ändra märken och lägsta pris |
| cykellas | rättad | Typlistan efter kolon såg fullständig ut (Ramlås AXA Defender saknades), M-Wave saknades. Brödtext: "…säljer cykellås: vajerlås, … från bland annat AXA, Squire och Giant" → "…säljer cykellås, bland annat vajerlås, … kabellås, från AXA, Squire, Giant och M-Wave". Meta → "Köp cykellås, bland annat …, från AXA, Squire, Giant och M-Wave. Minst 50 lås från cirka 90 kr." (145 tecken) | Hantellås räknas som cykellås (56 i st. f. 55; "minst 50" håller). Dyraste, "Vikbart Lås AXA Fold Lite 80" 5 339 kr (nästa 2 979 kr) kan vara ett prisfel i butiken: kontrollera före skrivning |
| elcyklar | rättad | "TENWAYS" → "Tenways" (4 ställen: brödtext, SEO-titel, meta; 21 av 22 titlar skriver Tenways, R8 förbjuder versaler). "Tenways och ADO har flest modeller" → "…flest produkter" (unika modeller: ADO 12, Tenways 8, Giant 8). Meta: "från Tenways, ADO, Giant, Fiido och Engwe" → "från bland annat …" (märkeslistan ofullständig) | "Electric bike VOGUE Avenger" och "Electric cargo bike CARGOBIKE Delight" ligger bland övriga; lägsta pris ("från cirka 13 900 kr") kan vara fel om Vogue Avenger är billigare. ADO/SOKE/AXA i versaler följer titlarna (fråga om R8) |
| sparkcykel | rättad (var underkänd) | Meta saknade "bland annat" (S'Cool saknas) → "…från bland annat SOKE, Union, Rideoo, Versatyl och Ethic. Minst 50 produkter från cirka 2 200 kr." (151 tecken). De tre tidigare felen (klistermärke, Rideoo, "modeller") är åtgärdade | Underlaget utesluter "barn"; barnsparkcyklar syns ändå på sidan och kan göra "prisklassen 2 200–5 000 kr" fel. Kontrollera de 43 övriga produkterna |
| hantlar | rättad (felen fanns redan förra gången) | "Vikterna … från 2 till 50 kg" → "från 1 till 50 kg" (brödtext och meta; "Hantelset Tunturi Platinum Hex Rubber, 1–10 kg" missades av kg-regexen). "från Tunturi, Gymstick, Hammer, Toorx och Christopeit" → "från bland annat …" (Zipro saknas). Meta → "Köp hantlar, hantelset och justerbara hantlar från bland annat Tunturi, Gymstick, Hammer och Toorx. Vikter från 1 till 50 kg. Priser från cirka 70 kr." (150 tecken) | Underlaget har fel: hantelställ och hantelstänger räknas som hantlar (cirka 44 i st. f. 48 produkter, "minst 40" håller); engelska titlar ("Pro Chrome Hantel 0,5kg", "60 kg vinyl skivstångs- och hantelset", "Quick-Lock Dumbbell 36kg") ligger bland övriga, så vikterna är troligen 0,5–60 kg och lägsta priset kan vara under 69 kr. Granskarens rekommendation: kör om underlaget med "dumbbell" som typord före låsning |
| tunturi | rättad | Meta räknade upp typerna som fullständig lista → "Köp Tunturi hos BEST OF SPORTS, bland annat motionscyklar, löpband, roddmaskiner, träningsbänkar och hantlar. Minst 300 produkter från cirka 40 kr." (147 tecken) | – |

## Slutsats från granskaren
Kontrollskriptet kan inte hitta de här felen. De kommer från underlaget: kg-regexen missar intervall ("1–10 kg"), engelska titlar hamnar bland övriga, och tillbehör räknas som huvudprodukter. Granskningen av underlaget bör vara ett fast steg före varje text, inte bara gälla sparkcykel.

## Efter rättelserna
`kategori_kontroll.py`: 0 fel. Tre texter (motionscykel, roddmaskin, kettlebell) och två till (crosstrainer, lopband) ändrades inte. De fem kvarvarande underlagsfrågorna (hantlar, lopband, elcyklar, sparkcykel, cykellas) kräver omkörning av underlaget mot butiken (läsning) och är inte gjorda. En tredje granskning behövs av de fem ändrade texterna efter eventuell omkörning. Inget ändrades i Shopify.
