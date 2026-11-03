# Skrivrapport: korta metabeskrivningar (117 produkter, Best of Sports)

Datum: 2026-11-03. Butik: BEST OF SPORTS (bestofsports.se, verifierad med get-shop-info). Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/kort_meta_skriv.json`. Före-läge: `rapporter/shopify-original-2026-11-03/kort_meta_fore.json`.

## Status 2026-11-03 (uppdaterad efter koordinatorns besked): stoppad, 4 produkter felaktiga i Shopify

- Verifierat rätt (läst tillbaka och jämfört i python): 102 produkter (filindex 0–85 samt 16 av batchen 86–105). Av dessa rättades 8054, 3030 och 3039 med skriptets utskrift, och de är verifierade.
- Skrivet men felaktigt i Shopify (fel i mina handskrivna variabler, rättningen blev också fel): 10581109932298 (nr 3175, "balansuträning"), 10581112226058 (nr 3227, "draövningar"), 10581112422666 (nr 3232, "grepposition"), 10581119467786 (nr 3261, "stretchingsövningar"). Filens text är rätt i skrivfilen. Titlarna är oförändrade.
- Inte skrivna: 11 produkter (filindex 106–116).
- Orsak: mutationens text skrivs för hand i verktygsanropet. Skriptet skriver ut variablerna, men jag kan inte kopiera dem exakt. Under körningen gjorde jag 9 skrivfel i handskrivna variabler, i 7 produkter. Flera rättningsförsök införde nya fel. Jag ska inte göra fler skrivningar med den metoden.
- Ej rättat ännu: 10581109932298 har nu även "balansuträning" (enligt skrivsvaret). Ingen ny skrivning har gjorts efter det.
- Nästa steg (kräver ett beslut): antingen skrivs de 4 felaktiga och de 11 återstående av något annat slag (till exempel ett skript som kan skicka mutationen själv, om det finns ett sådant verktyg), eller så görs det av någon som kan kopiera utskriften.

## Tidigare status: avbruten efter 43 av 117 produkter

Avbrottet följde regeln "avbryt vid första avvikelse". Avvikelsen orsakades av mig.

## Vad som gjordes

1. **Före-läge (117 av 117 lästa live, före skrivning):** alla är ACTIVE. Alla `seo.description` är tomma, så ingen produkt hoppades över. `seo.title` är null på 20 produkter, vilket betyder att SEO-titeln är lika med produkttiteln.
2. **Kanarie (3 produkter):** skrevs, lästes tillbaka och jämfördes. Titel oförändrad, beskrivning exakt lika med filen.
3. **Batch 4–23 (20 produkter):** skrevs med skriptets utskrift, lästes tillbaka. Jämförelse i python mot skrivfil och före-läge: 23 kontrollerade (inklusive kanarie), 0 avvikelser.
4. **Batch 24–43 (20 produkter):** skrevs och lästes tillbaka. Jämförelse i python: 20 kontrollerade, **1 avvikelse** (se nedan). Avbrott.

## Avvikelsen

- Produkt: `gid://shopify/Product/10472486109450` (Skidskrapa Start, Metall), skrivfilens nr 8054, ej i kanarie.
- Fil (rätt): "…används för att rengöra skidornas **belag**."
- Shopify (fel, nu live): "…används för att rengöra skidornas **beläg**."
- Orsak: jag skrev mutationens variabler för hand i stället för att kopiera skriptets utskrift ordagrant. Det är precis det som lärdomen 2026-11-03 ("Haiku skrev om en metabeskrivning för hand") varnar för. Jag gjorde felet trots att skriptet fanns.
- Titel är oförändrad och övriga 19 produkter i batchen stämmer.
- Åtgärd: en produkt har en felstavning i metabeskrivningen. Den behöver rättas med en ny skrivning av exakt filens text, körd via skriptet.

## Vad som inte är gjort

- Produkterna 44–117 (74 stycken) är **inte skrivna**. Före-läget för dem finns i `kort_meta_fore.json`.
- Den felstavade produkten är inte rättad.

## Ändrat i Shopify

Ja: 43 produkter har fått `seo.title` och `seo.description` (productUpdate, endast seo). Inga andra fält har ändrats. Handle, status, taggar, titel och beskrivning är inte ändrade.

## Förslag till nästa steg (kräver ett ja)

1. Rätta produkten 10472486109450 med skriptet (en produkt, `seo` från filen).
2. Fortsätt med produkterna 44–117 i batcher om 20 med samma kontroll (återläsning och python-jämförelse). Starta med en ny kanarie.
