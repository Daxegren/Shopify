# Granskningsutlåtande k_23d och k_23e (BEST OF SPORTS)

Granskare: Opus, endast läsning. Datum: 2026-11-05. Butiken är bekräftad via API (BEST OF SPORTS, 6f2e53-67.myshopify.com). Alla 12 produkter är hämtade live på nytt med `shopify_api.py`: alla är ACTIVE, ingen har texter-klara och ingen står på spärrlistan. Ingenting är skrivet i Shopify. Underlag: regler-v1.md (v1.5–v1.8), BESLUTSLOGG.md (raderna 2026-11-05), butiksprofil-bestofsports.json och agentprompter.md. Prejudikat: k_utlatande_09b (Hammer Core 2.0), f_utlatande_10 (skivstänger utan maxvikt), f_utlatande_5 (10122 träningscykel/Motionscykel), k_utlatande_05_06 (9359 typord från tillverkarsida) och k_utlatande_19de (20047).

**Utfall:** GODKÄND 10, RÄTTA 2 (23046, 23051), UNDERKÄND 0 (av 12).

Rättningarna är provkörda på kopior. Varje "före" förekommer exakt en gång i sitt fält. `skrivfil_kontroll.py` gav 0 fel och 0 varningar på båda filerna.

## Tabell

| nr | id | fil | dom | rättning och skäl |
|---|---|---|---|---|
| 23037 | 10475384930570 | k_23d | GODKÄND | Typordsbytet glidmedel → Klister godtas (se nedan). Bruksanvisningen stämmer med varuste.net. Basgreppssteget är rätt utelämnat. |
| 23039 | 10515737706762 | k_23d | GODKÄND | Giants sida har produktkod 400000166, samma som SKU. Den bekräftar 200 lm, IPX7, 1000 mAh Li-Ion-polymer, USB-kabel, 46 g och 53 x 28 x 28 mm. De trasiga raderna är utelämnade. |
| 23042 | 10548235403530 | k_23d | GODKÄND | Allt står i live. PE/PVC är rätt utelämnat (titel och källtext går isär), och måttet likaså. Leveranstidsmeningen är med. |
| 23043 | 10548235862282 | k_23d | GODKÄND | 25 x 20 x 28 cm står i live och bekräftas av Galaxus och Velomarket. PE/PVC är rätt utelämnat. Leveranstidsmeningen är med. |
| 23046 | 10581101674762 | k_23d | RÄTTA | **html:** "Ett par fjäderlås ingår men viktskivor ingår inte. Enligt tillverkaren är maxbelastningen 150 kg.</p>" → "Ett par fjäderlås ingår men viktskivor ingår inte.</p>"<br>**html:** "&lt;li&gt;Maxbelastning: 150 kg&lt;/li&gt;\n" → "" (raden tas bort)<br>Lastgränsen finns bara hos återförsäljare (se nedan). Övriga fakta stämmer med Elgiganten och Bygghemma. |
| 23051 | 10581105705226 | k_23e | RÄTTA | **html:** "&lt;li&gt;Max användarvikt: 110 kg (enligt tillverkaren)&lt;/li&gt;\n" → "" (raden tas bort)<br>Användarvikten finns bara hos återförsäljare (se nedan). Övrigt stämmer med Bygghemma och Prisma. Typordet Motionscykel godtas. |
| 23054 | 10581111013642 | k_23e | GODKÄND | Prisma (EAN-träff) anger 2–36 kg i steg om 2 kg, viktskivor av stål, stålhandtag med gummigrepp och styckförsäljning. Översättningarna är entydiga. |
| 23055 | 10581111046410 | k_23e | GODKÄND | Gigantti (EAN och GY61032) anger viktlägen, mekanismen högst upp och 30 x 18,3 x 22,4 cm. |
| 23058 | 10650167771402 | k_23e | GODKÄND | Två fakta ur live (aluminiumlegering, silver). Ursprunget är struket. Inget pris nämns i något fält. |
| 23060 | 10676607189258 | k_23e | GODKÄND | Samma produkt (se nedan). Fakta från Rideside med EAN-träff. |
| 20023 | 10581119336714 | k_23e | GODKÄND | Ingen lastgräns, enligt Davids beslut. Elgiganten (EAN och GY61336) anger två höjder, 68 x 28 cm och 3 kg. |
| 20047 | 10636687606026 | k_23e | GODKÄND | Inget "10kg" och ingen bärförmåga. Upphängningen beskrivs bara med mått och fästets material, ordagrant ur live. |

## Särskilt granskat

- **23046, maxbelastning 150 kg: räcker inte.** Uppgiften står ordagrant på svenska med etikett och enhet hos Elgiganten ("Maximal kapacitet (kg): 150") och Bygghemma ("Max Belastning 150 Kg", "Maxlast 150 kg"). Båda har EAN 6430062510546, och båda sidorna öppnade granskaren. Ingen sida från Gymstick finns, och min egen sökning gav ingen heller. Skälen till att den ändå stryks:
  1. "Enligt tillverkaren" påstår att tillverkaren har sagt det. En återförsäljares tabell är inte tillverkaren, och vi kan inte belägga det påståendet.
  2. Alt A (2026-11-04) godtar svensk lastgräns "i produktens egen källa". Beslut 3 (v1.7) säger att R4 gäller oförändrad för bärande delar. Webbfaktakollen i v1.6/v1.7 gäller fakta i allmänhet och lättar inte den särskilda lastgränsregeln.
  3. Prejudikat 09b: Hammer Core 2.0, där lastgränsen bara fanns hos återförsäljare, skrevs inte med lastgräns.
  
  **Beslut 3 tvingar ändå ingen avvisning.** En lyftstång bär viktskivor, inte kroppen, och är ingen bärande eller hängande del i beslutets mening (plyobox, stepbräda, upphängning, chinsstång). Skivstänger har skrivits utan maxvikt (f_10: 10235, 10238). Produkten skrivs alltså utan lastgräns.
- **23051, max användarvikt 110 kg: räcker inte, av samma skäl.** Uppgiften står på svenska bara hos Bygghemma. Prisma har den på finska, och det finns ingen sida från Gymstick. Motionscyklar skrivs utan användarvikt när den saknas (alt A), och cykeln omfattas inte av beslut 3:s avvisning. Typordet Motionscykel godtas: live säger "träningscykel", och ordet är synonymt. Bygghemma använder Motionscykel för exakt modellen, och 10122 är prejudikat.
- **23037, glidmedel → Klister.** Live-titelns "glidmedel" är sakligt fel: källtexten beskriver en fästvalla i tub för fästzonen. "Greppsmörjning", "klämmor", "klinker" och "lim" är maskinöversättningar av klister. Att behålla det fel ordet strider mot R2. varuste.net/sv/p68113 säljer exakt "Start Universal Wide Klister +10°...-5°C 55g" under Fästvallor > Klistervallor. EAN saknas på sidan, men namn, temperatur och vikt är identiska och det finns bara en sådan produkt. Bytet godtas därför enligt v1.6/v1.7, med prejudikat 9359. Förslag: lägg in "klister" i profilens `godkanda_typord`.
- **23060, "Stand Pad" mot "Scooter Stand 12 Standard": samma produkt.** SkatePro kallar exakt 12 Std-versionen "12 Std Scooter Standpad (works with 30mm wide wheels)". Rideside och Picar anger EAN 3760004842576 för 12 Standard, och samma EAN finns i variantens SKU, streckkod och handle. Classic- och Basic-versionerna för 24 mm har andra EAN (Basic: 3760004842569). **Prisavvikelse:** butiken tar 1 409 kr, medan återförsäljarna tar 2,95–9,95 €. Textutrullningen rör inte priset, men det bör läggas på Davids prislista.
- **23058, 9 kr:** inget fält nämner pris. Den enda träffen på " kr" i hela batchen är ordet "kromyta" i 23046. Priset finns redan på listan över prisavvikelser.
- **23042/23043, PE/PVC:** live-titeln säger PE, och källtexten säger PVC fyra gånger. Galaxus säger PE, och Velomarket och Decathlon säger PVC. Utelämnandet är riktigt (R2), och "PE" är struket ur titeln.
- **20047:** "10kg" eller "10 kg" förekommer inte i något fält, och inget sägs om upphängningens bärförmåga eller säkerhet.

## Beslut för David (förslag)

1. Får en ordagrann svensk lastgräns hos minst en svensk återförsäljare med EAN-träff skrivas när tillverkarsida saknas, till exempel utan "enligt tillverkaren"? Gäller 23046 (150 kg) och 23051 (110 kg). Rekommendation: nej, samma linje som 09b. Om inget beslutas skrivs produkterna utan lastgräns.
2. Lägg till typordet "klister" i profilen (23037).
3. Lägg till 23060 (1 409 kr) på listan över prisavvikelser.

## Webbkällor öppnade av granskaren (2026-11-05)

- varuste.net/sv/p68113/start-universal-wide-klister-10-5c-55g
- giant-bicycles.com/cz/recon-tl-200-2020
- elgiganten.se/…/gymstick-10kg-lifting-bar-skivstang/285255; bygghemma.se/…/skivstang-gymstick-lifting-bar-10-kg/p-928802
- bygghemma.se/…/motionscykel-gymstick-crank-bike-x4/p-928984; prisma.fi/tuotteet/100521066
- prisma.fi/tuotteet/111418215 (Quick-Lock hantel); gigantti.fi/…/gymstick-quick-lock-kettlebell-135-kg/542816
- rideside.at/en/equipment-voucher/ethic-scooter-stand-12.html; picar.hu/en/spd/3760004842576; skatepro.ca/en/298-31241.htm; skatepro.com/en-us/298-31240.htm
- elgiganten.se/…/vivid-step-board-stepbrada/446947
- Sökning: Galaxus, Velomarket och Decathlon (Tunturi 10 kg, 14TUSCL106). proshop.se och velomarket.ee gav 403.
