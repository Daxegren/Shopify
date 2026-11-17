# Granskning av batch k_50a (BEST OF SPORTS), 2026-11-17

Granskare: Opus. Granskaren har bara läst och har inte ändrat något i Shopify. Utkasten finns i `vag2_skriv/k_50a_utkast.json` (22 st), och de avvisade i `k_50a_avvisade.json` (2 st). Som källa användes en live-läsning från i dag, `rapporter/shopify-original-2026-11-17/k_50a_kalla_live_granskning.json`. Utlåtandet i JSON-form finns i `vag2_skriv/k_utlatande_50a.json`. Varje ändring där (före → efter) har kontrollerats med skript: texten som ändras finns exakt en gång i sitt fält, och längderna håller sig inom gränserna även efter ändringen.

## Resultat
- **GODKÄND (13):** 50001, 50003, 50004, 50005, 50006, 50024, 50010, 50013, 50014, 50015, 50016, 50018, 50019
- **RÄTTA (9):** 50002, 50021, 50007, 50009, 50012, 50017, 50020, 50022, 50023
- **UNDERKÄND (0)**

## Viktigaste fynden
1. **50002 Tunturi Pro Gel:** Live-texten och live-titeln är vår egen facit-text från 2026-10-31. Leverantörens originaltitel saknade ordet "Läder". Leverantörens originaltext finns sparad i `utkast_kontroll.json` (fältet fakta) och anger läder, gel i handflatorna, öppna fingrar, handledsstöd med kardborreband, innerhandske och att handskarna säljs parvis. De uppgifterna läggs tillbaka. Påståendena om halkfrihet, skydd och hygien följer inte med, och inte heller färgerna grå/svart, eftersom produkten inte har färgvarianter. Om koordinatorn bara vill använda live-källan blir domen GODKÄND utan ändring. Då är ordet "läder" bara belagt i den sparade originaltexten. Produkten får skrivas trots att S kostar mer än övriga storlekar (v1.9: lager 11, samma artikel i olika storlekar).
2. **"Anti-Burst" struket ur gymbollarnas titlar:** Det är rätt. Säkerhetslöften som anti-burst tas bort enligt standarden §10 och R5. Ett sådant ord måste stå med "enligt tillverkaren", och det går inte i en titel. De skrivna systerprodukterna har inte heller ordet. R7 handlar om typordet och hindrar inte att uppgifter stryks. **50021:** färgen ändras från "Rose Gold" till "Roséguld", som är butikens ord.
3. **50019, lyftstång:** "Maximal lastgräns: Ej känd" och meningen "Maximal lastgräns är inte känd." är rätt formulerade enligt v1.10 och tidigare beslut. Webbens uppgifter kommer bara från återförsäljare och går isär (100 kg och 200 kg). Enligt beslutet 2026-11-05 ska lastgränsen då anges som Ej känd.
4. **50012:** Typordet Viktplatta byts till Viktskiva. Det har stöd i källtexten och i butiksprofilen. SEO-titeln (titeln som visas i sökmotorer) får vikten 5 kg, annars skulle den krocka med den osålda 15 kg-skivan.
5. **50007:** "Yoga set" blir "Yogaset", som är butikens ord och svensk sammanskrivning. Innehållet stämmer med en webbkoll (Sportano och mediamarkt.pl). **50017:** SEO-titeln får tillbaka märket Tunturi, och ordet "Dumbbell" stryks ur titeln, som för de skrivna syskonen.
6. **50009, pulsbälte:** Uppgiften "vattentät upp till 20 m" står ordagrant i källan, återges med "enligt tillverkaren" och bekräftas av Tunturis egen produktsida. "Elliptiska tränare" byts till "crosstrainers".
7. **50020:** Metabeskrivningen (texten under länken i sökresultaten) saknade verb och har fått ett. **50022 och 50023:** "med Ryggstöd" ska ha stor bokstav enligt formatregeln, som i den skrivna BRX R3000. "PMS, servomotor" återges ordagrant och förklaras inte. Det är rätt.
8. **50016, hula hoop:** Produkten har taggen "På beställning" och meningen om längre leveranstid finns i standardblocket. Laddnings- och driftstid står en gång med "enligt tillverkaren". 50004: det är rätt att 110 cm är struket (v1.8: två varianter med samma pris).
9. **Formatskriptet:** `titel_versaler` skulle göra om typorden "Telefon- och surfplattahållare" (50018) och "Hantel- och skivstångsset" (50020) till "…och Surfplattahållare" och "…och Skivstångsset". Det bör kontrolleras vid bygget att typordet behåller liten bokstav.

## Avvisade
- **50901 Tunturi Wrist Wraps, red:** Avvisningen är **rätt**. Titeln anger röd, men specifikationen anger svart, och då ska produkten avvisas enligt R3. Det andra skälet håller däremot inte ensamt: handlindor får skrivas utan skyddspåståenden enligt besluten 2026-11-05 och 2026-11-08.
- **50902 Spokey Lava XL:** Avvisningen är **inte förenlig med v1.12**. Typ, märke, modell, färg och storlek står entydigt i titeln, och artikelnumret är 928977. Enligt v1.12 får en text byggas av titelns uppgifter (som Mickey-handskarna i k_49t5). Den motsägande meningen "passar nästan alla händer" ska utelämnas. Rekommendation: nytt kort utkast med bara titelfakta och artikelnummer, utan EAN.

## Webbkällor
- https://sportano.com/p/35987/spokey-mantra-yoga-set-928924 (50007)
- https://velomarket.ee/en/products/yoga-set-spokey-mantra-set-black/ (50007)
- https://www.tunturi.com/en/chest-belt-53khz.html (50009, enligt sökresultat)
- https://outlet-pc.com/SE/products/bh-0190906-soporte-para-smartphone-y-tablet-fitness-regulable-4-7-13-negro (50018)
- https://www.galaxus.de/en/s3/product/tunturi-langhantelstange-mit-30-mm-schraubverschluessen-180-cm-dumbbell-bars-6065376 (50019, 100 kg)
- https://www.decathlon.co.uk/p/mp/barbell-bar-180cm-screw/391e0051-5a57-49ae-9c26-9051c620dbf3/c249 (50019, 200 kg)
