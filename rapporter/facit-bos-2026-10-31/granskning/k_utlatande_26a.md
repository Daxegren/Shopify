# Granskningsutlåtande k_26a (dubbdäck), BEST OF SPORTS

Granskare: Opus, bara läsning. Datum 2026-11-05. Utkastfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_26a_utkast.json`. Butiken bekräftad som BEST OF SPORTS via Admin API (`shopify_api.py`). Källan lästes live på nytt för alla fyra produkter. Tillverkarens sidor (suomityres.fi) och ebikeparts.fi öppnades. Ingenting skrevs i Shopify.

Underlag: regelboken v1.4–v1.8, BESLUTSLOGG (2026-11-05), butiksprofilen och Davids beslut 2026-11-05 om dubbdäck: de får skrivas utan prestandapåståenden, bara med fakta (storlek/ETRTO, dubbantal, dubbtyp och avsedd användning när källan anger den).

## Domar

| Nr | Id | Produkt | Dom |
|---|---|---|---|
| 26001 | 10472189788426 | Schwalbe Winter 47-559 | GODKÄND |
| 26002 | 10472303919370 | Suomi Tyres Hile W240 40-622 | RÄTTA (språk, R11) |
| 26003 | 10472304017674 | Suomi Tyres Routa W126 50-622 | GODKÄND |
| 26004 | 10472304050442 | Suomi Tyres Porcupine W408 TT 65-622 | GODKÄND |

## Rättningar

**26002, html** (före förekommer en gång)
- Före: `<p>Vinterdäck från Suomi Tyres med 240 dubbar. Hile W240 har storleken 40-622 (28 tum).</p>`
- Efter: `<p>Suomi Tyres Hile W240 är ett vinterdäck med 240 dubbar. Däcket har storleken 40-622 (28 tum).</p>`

**26002, meta** (före förekommer en gång, efter 83 tecken)
- Före: `Vinterdäck från Suomi Tyres med 240 dubbar. Hile W240 har storleken 40-622 (28 tum).`
- Efter: `Suomi Tyres Hile W240 är ett vinterdäck med 240 dubbar i storleken 40-622 (28 tum).`

Skäl: den första meningen saknar verb (R11). Fakta ändras inte.

## Särskilt granskade punkter

1. **Grepp, säkerhet och halka:** inga sådana påståenden finns i någon titel, SEO-titel, meta eller beskrivning. Ordet "tillverkaren" förekommer bara i standardblocket ("Tillverkarens garanti"). Live-källornas "goda grepp", "säkerställer ett fast grepp", "punkteringsskydd", "slitstark" och "hållbarhet" är utelämnade.
2. **26003 "reflekterande sidor":** får stå. Det beskriver hur däcket är byggt och står både i live-källan ("Alla Routa-modeller har reflekterande randiga sidor") och hos tillverkaren ("Routa models are always with reflective side"). Utkastet påstår inget om synlighet eller säkerhet. Det blir ett säkerhetspåstående först om texten säger att man syns bättre eller kör säkrare. Det motsvarar "Färg: Svart-Reflex" på 26001.
3. **"240 lbs" och "408 lbs" som dubbantal:** båda är belagda i tillverkarens tabeller.
   - Hile W240: T601281 har 40-622, 28 tum och dubbantal 240 (https://suomityres.fi/products/winter/mtb/hile-w240).
   - Porcupine/Piikkisika: T501081 har 65-622, 29 tum och dubbantal 408 med dubbtypen Alum./Crown (https://suomityres.fi/products/winter/mtb/piikkisika/T500781).
   - Routa W126: T503181 har 50-622 och dubbantal 126 (https://suomityres.fi/products/winter/city/routa). Lbs-raderna tolkas inte i texten.
4. **26001, titel utan tum:** godtagbar. Live-titeln anger 1.85 tum och tabellen 1.75 tum (R2), medan ETRTO 47-559 är densamma i båda. "26 tum" i beskrivningen följer entydigt av 559. Titeln är unik mot syskonen (30-622, Marathon Winter 47-507).
5. **26004, SEO-titel utan "TT":** godtagbar. Med "TT" blir den 45 tecken, och gränsen är 43. Utan "TT" är den 42 tecken och ändå unik mot syskonet W408 TT 62-622 (T500101, utkast).
6. **TT eller TLR (26004):** "TT" i live-titeln är rätt. Tillverkaren listar T501081 under *Piikkisika Tube Type* ("TUBE TYPE"), och TLR-versionen i samma storlek har koden T300200 (https://suomityres.fi/products/winter/mtb/piikkisika-tlr/T300100). Det är ebikeparts.fi som har fel när sidan kallar T501081 "TLR". Därför var det rätt att utelämna vikten 1250 g därifrån. **Till koordinatorn:** byt webbkällan i `att_bekrafta` till tillverkarens sida.
7. **Leveranstidsmeningen:** 26003 och 26004 har taggen "På beställning" och meningen. 26001 och 26002 saknar både taggen och meningen. Alla fyra är rätt.
8. **Lastgränser:** inga. Schwalbes "Maximal belastning: 100 kg" är utelämnad.
9. **Dubbletter (R12a):** sökning på titel, SKU och EAN gav ingen annan aktiv produkt med samma SKU. Syskonen i andra storlekar är utkast eller arkiverade, och ETRTO i titeln skiljer dem åt.

## Valfritt (inget fel)
- 26003: användningsraden "Lämplig för pendlingscyklar, gruscyklar och lastcyklar" är en egen ren rad i live-källan och bekräftas av tillverkaren ("For commuting, gravel bikes and cargo bike"). Enligt beslutet får den läggas till, men det är inget fel att den saknas.
- 26002: dubbtypen finns hos tillverkaren ("full-steel studs") men inte i live-källan. Den får läggas till med källa, men det krävs inte.

## Till koordinatorn
Davids beslut 2026-11-05 om dubbdäck (fakta utan prestandapåståenden) har ingen rad i `shopify-sync/docs/BESLUTSLOGG.md` ännu. Lägg till raden innan skrivfilen byggs.
