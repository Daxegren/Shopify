# Granskningsutlåtande k_49t2, tom eller tunn källa enligt v1.12 (2026-11-08)

Granskaren har bara läst i Shopify och har inte ändrat något där eller committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.12), BESLUTSLOGG till och med 2026-11-08 (faktatext även i tidigare utanför-kategorier; svensk text för tom eller tunn källa), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och formatet i `k_utlatande_43.json`.

Alla 10 utkast och de 3 avvisade produkterna är ACTIVE. Standardblocket är exakt rätt på alla. Leveranstidsmeningen finns bara på 49102 och 49106, som är de enda med taggen På beställning. Titeln är högst 54 tecken med högst 2 kommatecken, SEO-titeln högst 37 tecken och metatexten 93–143 tecken. Titlar, SEO-titlar och metatexter är unika mot alla andra filer i `vag2_skriv` och mot butikens titlar. Det kontrollerades med sökning på Stödhjul, Hunddörr, Professional Gloves, Pillerdosa, Grip Ball, Trampolin, ADO Air, Fiido Titan, Sadelöverdrag och Azimut. Varje rättning är ETT sammanhängande före/efter-par per fält, och varje före-text förekommer exakt en gång i utkastet (kontrollerat i python). `skrivfil_kontroll.py` på de rättade texterna gav 0 formatfel men 1 spärrfel (49103, se nedan).

Tillverkarkällor: För alla 10 sökte granskaren efter en tillverkarsida. Två finns och stämmer: uk.fiido.com (Extender Battery Combo for Titan: hållare, 2 batterier, 2 påsar) och adoebike.com (ADO Air Carbon Stand). Toorx (toorx.it, accessori.toorx.it), Selle Monte Grappa, Azimut, M-Wave, Trec och Amladcykler har ingen sida för exakt artikel. Där bygger texterna bara på egen källa och titel, vilket är tillåtet enligt v1.12.

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_49t2.json`.

## Resultat: 5 GODKÄND, 4 RÄTTA, 1 UNDERKÄND

| nr | id | dom | rättade fält / skäl |
|---|---|---|---|
| 49101 | 10472252932362 | RÄTTA | meta (saknade verb; "hjul i svart" tvetydigt) |
| 49102 | 10472262959370 | GODKÄND | – |
| 49103 | 10472279900426 | RÄTTA | html ("liten" obelagt). **Spärrad**: står på `tidigare-avvisade-2026-11-04` utan undantag |
| 49104 | 10472285569290 | RÄTTA | html ("Material: Gel" påstod material; titeln säger bara "med gel") |
| 49105 | 10472293499146 | UNDERKÄND | Oklar produkttyp: källan anger 24–29 tums hjul, vilket passar ett cykelstöd, inte ett vevlager |
| 49106 | 10472294842634 | GODKÄND | – |
| 49107 | 10472300085514 | RÄTTA | html (cirkulär inledning trampolin/studsmatta), meta (typord Studsmattan → Trampolinen) |
| 49108 | 10472302444810 | GODKÄND | – |
| 49109 | 10472305557770 | GODKÄND | – |
| 49110 | 10472323023114 | GODKÄND | – |

### Rättningar (före → efter)

- **49101 meta:** "Stödhjul från Selle Monte Grappa för barn som lär sig cykla, till cyklar med 12–16 tums hjul i svart. Artikelnummer 82." → "Stödhjulen från Selle Monte Grappa är avsedda för barn som lär sig cykla och för cyklar med 12–16 tums hjul. Färgen är svart. Artikelnummer 82."
- **49103 html:** `<li>Dig som vill ha en liten träningsboll från Toorx</li>` → `<li>Dig som vill ha en träningsboll från Toorx</li>`
- **49104 html:** `<li>Material: Gel</li>` → `<li>Utförande: Med gel</li>`
- **49107 html:** `<p>Trampolinen Toorx Trampoline på 97 cm används som studsmatta för träning hemma.</p>` → `<p>Trampolinen Toorx Trampoline på 97 cm är avsedd för träning hemma.</p>`
- **49107 meta:** "Studsmattan Toorx Trampoline på 97 cm är avsedd …" → "Trampolinen Toorx Trampoline på 97 cm är avsedd för träning hemma och har artikelnummer TF-01 hos BEST OF SPORTS."

## Löften och påståenden

Alla texter genomsöktes efter hälso-, säkerhets-, skydds-, utvecklings-, prestanda- och kvalitetsord. Följande ord från källorna är rätt utelämnade: högkvalitativa, bekväma, nödvändiga (stödhjul), blodcirkulation, stresslindring, rehabilitering (greppboll), kompakt, hållbar, perfekt, uthållighet, koordination, balans, robust, stabil, säker, alla åldrar (trampolin), halkfri, maximal komfort och säkerhet, Italien (handskar). Inget av detta finns kvar i titel, SEO, meta eller beskrivning. Avsedd användning står som "avsedd för" utan resultatlöfte. Barnprodukten (stödhjul) har inga säkerhets- eller utvecklingspåståenden. Batteripaketet har ingen kapacitet, spänning eller räckvidd.

## Lastgräns (v1.10)

På 49101 (stödhjul) och 49106 (stativ) står "Maximal lastgräns: Ej känd" och en mening om att lastgränsen inte är känd, eftersom ingen tillverkaruppgift finns. Det är rätt. Trampolinen (49107) har ingen lastrad, vilket också är rätt eftersom trampoliner är undantagna i v1.10.

## Varianter och dubbletter

Alla tio har en enda variant. På 49109 är färgen utelämnad eftersom uppgifterna motsäger varandra: titeln säger svart-röd, varianten black och MediaMarkt röd. Ingen produkt är dubblett av en skriven eller aktiv produkt. Närliggande artiklar har andra SKU:er: stödhjul 12–20 tum SKU 85 (DRAFT), handskar AHF-033/034, Trampoline Pro TF-03, Sadelunderlag SADL217 och batteri FX-145.

## Avvisade (k_49t2_avvisade.json): alla tre avvisningar står fast

- 49151 Gymstick Workout gloves S/M: samma EAN (6430062511888) som varianten S/M på den skrivna aktiva 10581112783114. Det är en exakt dubblett.
- 49152 Kindad Frozen 2: källan är tom och EAN ger ingen träff. "Kindad" är estniska för handskar eller vantar, men det framgår inte vilket av dem, och avvisningen är inte uppenbart fel.
- 49153 Toorx Safe Lock: titeln säger hantelvikter men taggarna säger cykellås och viktlås, och källan är tom. Det är en motsägelse.

## Frågor till David

1. 49103 (Toorx Power Grip Ball) står på spärrlistan `tidigare-avvisade-2026-11-04`. Ska de produkter som släpps av v1.12 få ett undantag (som `undantag-2026-11-05`)? Om inte stoppar `skrivfil_kontroll.py` produkten. Granskaren har inte ändrat spärrlistan.
2. 49105 (M-Wave Strong F, SKU 430706): live-titeln "Vevlager" är troligen fel. Källan tyder på ett cykelstöd för 24–29 tums hjul. Ska titeln och typen utredas före en ny omgång?
3. 49106: ska typordet vara Cykelstöd (godkänt i profilen och butikens tagg stödben) i stället för källans Stativ?
