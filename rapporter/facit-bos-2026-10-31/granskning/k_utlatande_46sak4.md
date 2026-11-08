# Granskningsutlåtande k_46sak4: aktiva produkter i tidigare utanför-kategorier (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan texter-klara får faktatext även i säkerhets-, barn- och övriga tidigare utanför-kategorier), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och formatet i `k_utlatande_43.json`.

Alla 14 utkast är ACTIVE. Standardblocket är exakt rätt på alla; leveranstidsmeningen finns på exakt de tre som har taggen På beställning (46303, 46312, 46314). Titel ≤70 tecken och ≤2 kommatecken, SEO ≤43, meta 117–148 tecken, "Passar för" finns på alla. Titlar, SEO-titlar och metatexter krockar inte med andra utkast-/skrivfiler i `rapporter/`. Butiken söktes på modellnamnen (AXA Compact/Compactline, Melon, Little Nutty, Bookman, Absolute, Axact, StrongLock, Signature C65, WP 5000, Xcalibur, Alpina T 8) för R12a. `skrivfil_kontroll.py` på de rättade texterna ger bara 2 FEL: 46307 och 46308 står i spärren `utanfor-tills-vidare-2026-11-04` (barn). Beslutet 2026-11-08 frisläpper aktiva barn- och hjälmprodukter, men spärrlistan behöver ett undantag innan de kan skrivas. Varje rättning är ETT sammanhängande före/efter-par per fält, och varje före-text förekommer exakt en gång i utkastet (kontrollerat i python).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_46sak4.json`.

## Resultat: 8 GODKÄND, 5 RÄTTA, 1 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 46301 | 10472303198474 | k_46sak4_utkast.json | RÄTTA | seo_title, meta |
| 46302 | 10472306606346 | k_46sak4_utkast.json | GODKÄND | – |
| 46303 | 10472325415178 | k_46sak4_utkast.json | RÄTTA | html, meta |
| 46304 | 10472330756362 | k_46sak4_utkast.json | GODKÄND | – |
| 46305 | 10472330789130 | k_46sak4_utkast.json | GODKÄND | – |
| 46306 | 10488282317066 | k_46sak4_utkast.json | GODKÄND | – |
| 46307 | 10472346124554 | k_46sak4_utkast.json | GODKÄND | – |
| 46308 | 10475979702538 | k_46sak4_utkast.json | GODKÄND | – |
| 46309 | 10475367956746 | k_46sak4_utkast.json | RÄTTA | html |
| 46310 | 10475432476938 | k_46sak4_utkast.json | UNDERKÄND | – |
| 46311 | 10475619942666 | k_46sak4_utkast.json | GODKÄND | – |
| 46312 | 10494693507338 | k_46sak4_utkast.json | RÄTTA | titel |
| 46313 | 10494697341194 | k_46sak4_utkast.json | RÄTTA | html |
| 46314 | 10494777229578 | k_46sak4_utkast.json | GODKÄND | – |

## Rättningar (före → efter)

- **46301 seo_title:** "Reflexklistermärken Bookman Adventure" → "Reflexklistermärken Bookman Adventure, Gul"
- **46301 meta:** "Reflexklistermärken från Bookman som kan monteras på cykelramar, styren och hjälmar. Klistermärkena går att kombinera i olika färger och designer." → "De gula reflexklistermärkena Bookman Reflective Adventure Stickers kan sättas på cykelramar, styren och hjälmar och kombineras med andra färger."
- **46303 html:** "Enligt tillverkaren tar du hantlarna från ställets höjd vid höften." → "Hantlarna tas från stället i höfthöjd enligt tillverkaren."
- **46303 meta:** "Hantlarna lyfts från ställets höjd vid höften." → "Hantlarna tas från stället i höfthöjd."
- **46309 html:** "<li>Bindning: Touring Auto eller Touring Basic</li>" → "<li>Passande bindning: Touring Auto eller Touring Basic</li>"
- **46312 titel:** "Roddmaskin Christopeit WP 5000, ek" → "Roddmaskin Christopeit WP 5000, Ek"
- **46313 html:** "Den har sex funktioner: aktuell hastighet" → "Den visar aktuell hastighet"

## Löften (hälsa, säkerhet, skydd, utveckling, prestanda, kvalitet)

Alla texter genomsöktes efter både tydliga och subtila löften. Inget finns kvar: säkerhet, synlighet, skydd, stötdämpning (MIPS beskrivs bara som friktionslager), komfort, kylning, stöldskydd/säkerhetsnivå, ljusräckvidd, robust/stabil/slitstark, ledvänlig, muskel- och uthållighetseffekt och ergonomi är utelämnade. Det som står kvar är ordagranna källuppgifter: standarder CE/CPSC/AS (en gång enligt tillverkaren på barnhjälmarna), vattentätt yttre (en gång enligt tillverkaren), varmt foder, härdade stållänkar och max användarvikt (svensk rad med etikett, en gång enligt tillverkaren). Lastgräns för hantelstället: "Ej känd" (v1.10).

## Domar och skäl

- **46301 (RÄTTA):** Live ACTIVE, en variant 489, EAN 7350051864896, lager 4. Uppgifterna (montering på ram/styre/hjälm, lätta att ta bort, kombinera färger och designer) finns i egen källa; säkerhet, synlighet och väderbeständighet rätt utelämnade (v1.9). RÄTTA: SEO-titel och meta saknade färgen och skulle krocka med de aktiva syskonen Adventure Stickers Green (10471175520522) och Vit (10548248215818); metans första mening saknade huvudverb.
- **46302 (GODKÄND):** Live ACTIVE, H9340S, EAN 8445960018290, lager 1. Alla uppgifter står ordagrant i egen källa (24 nivåer, PMS servomotor, 15 kg svänghjul, Q-factor 190, 800 W, FTMS, mått, 62 kg). Max användarvikt 130 kg som svensk rad med etikett, en gång enligt tillverkaren (R4). Inga löften. Ingen dubblett (Xcalibur Multimedia H9340TFT är annan artikel).
- **46303 (RÄTTA):** Live ACTIVE, 17373, lager 0, tagg På beställning, leveranstidsmeningen finns. Stället till StrongLock 8.0 (skrivna hanteln 10507432722698 är annan artikel). Lastgräns saknas i egen källa och hittades inte på nätet för artikelnummer 17373 (sökning gav bara 17374/17376 och StrongLock 4.0-stället); 'Maximal lastgräns: Ej känd' enligt v1.10. Ergonomi, rygg, stabilitet och halkfria fötter rätt utelämnade. RÄTTA: meningen om höfthöjd var otydlig svenska i både html och meta.
- **46304 (GODKÄND):** Live ACTIVE, MUA.P001M.XL, EAN 4260182014554, lager 7. Alla uppgifter ur egen svensk källa; säkerhetsstandarder, komfort och kylning utelämnade. Storlek utelämnad eftersom källan anger två storlekar (skrivna syskon anger 'Storlekar i serien', frivilligt). Ingen annan Closed Eyes-produkt i butiken.
- **46305 (GODKÄND):** Live ACTIVE, MUA.G087M.XL, EAN 4260243726167, lager 4. Uppgifterna stämmer med egen källa; inga löften. OBS: syskonet 10471081541898 (MUA.G087M.ML, samma live-titel) är DRAFT; om det aktiveras och skrivs måste titlarna skiljas åt (storlek).
- **46306 (GODKÄND):** Live ACTIVE, MUA.P112M.ML, EAN 4260243722558, lager 4. Användning (cykling, skateboard, elcykel), Fidlock, 12 luftventiler, Spin Dial, vikt och material ur egen källa. 'Huvudskydd', 'säkerhet', 'svalt' utelämnade. Färg brun ur live-titeln, enda varianten.
- **46307 (GODKÄND):** Live ACTIVE, 10002420, EAN 194521042806, lager 7. Storlek XS 48–52 cm, MIPS beskrivet bara som friktionslager (ingen stötdämpande effekt), polykarbonat, Fidlock, 11 ventilationsöppningar, GROW Flex Fit; standarder CE/CPSC/AS en gång 'enligt tillverkaren' ur egen källa (fakta, inget löfte). Skydds-, komfort- och ventilationslöften utelämnade. Obs: skrivfil_kontroll ger FEL eftersom id finns i spärren utanfor-tills-vidare-2026-11-04 (barn); beslutet 2026-11-08 frisläpper aktiva barn-/hjälmprodukter, men spärrlistan behöver ett undantag innan skrivning.
- **46308 (GODKÄND):** Live ACTIVE, 10001790, EAN 194521007850, lager 3. Samma bedömning som 46307: bara fakta, standarder en gång enligt tillverkaren, inga skyddslöften. Samma spärrlisteanmärkning (undantag krävs före skrivning).
- **46309 (RÄTTA):** Live ACTIVE, fem storleksvarianter 28–32 i svart, 29 billigare, lager 44: samma artikel i olika storlek, v1.9 uppfylld (titel/SEO låser varken storlek eller pris; storlekarna i meta är just de som säljs). Vattentätt yttre en gång enligt tillverkaren; snölås, mjuk sula och varmt foder står ordagrant i källan. RÄTTA: 'Bindning:' kunde läsas som att bindning ingår; källan anger bara lämplig bindning.
- **46310 (UNDERKÄND):** UNDERKÄND (R12a, dubblett): samma modell som redan skrivna aktiva 10472255455498 'Framlampa AXA Compact Line Battery 20, USB' (texter-klara, lager 16): Compactline Front 20 lux, 12 h, USB. Bara förpackningskoden skiljer (93932095CB/EAN 8713249290065 mot 93932095BX/EAN 8713249267197); samma modell, färg och storlek (beslut 2026-11-05). Titeln kan inte skiljas ut utan en påhittad skillnad. Avvisades av samma skäl i k_04a. Kräver Davids beslut (arkivera den ena efter att lagret flyttats, eller skriv med förpackningen som skillnad om han godkänner).
- **46311 (GODKÄND):** Live ACTIVE, 59051195KS, EAN 8713249346830, lager 22. Längd 110 cm, härdade stållänkar 5 mm, polyesterhölje, klick-in, 2 nycklar och nyckelbeställning ur egen källa. Säkerhetsnivå 7/15, 'starkt', 'skyddar' och stöldrisk utelämnade. Inte dubblett av Absolute 5-150, 7-150, 8-110 eller 9-110 (andra längder och tjocklekar).
- **46312 (RÄTTA):** Live ACTIVE, 30-2265, EAN 4044163022659, lager 3, tagg På beställning, leveranstidsmeningen finns. Alla specifikationer ur egen svensk källa; max användarvikt 150 kg en gång enligt tillverkaren; robust, stabil, slitstark, ledvänlig, muskel- och uthållighetslöften utelämnade. RÄTTA: beskrivande ord i titeln ska ha stor bokstav (R9).
- **46313 (RÄTTA):** Live ACTIVE, 410000003, EAN 4718905972532, lager 24. Källan säger '6 funktioner' men listar fem; den skrivna Axact 9W räknar automatisk på/av som funktion. RÄTTA: texten sa 'sex funktioner:' följt av fem, vilket inte är entydigt; nu 'visar' och listan. Spec 'Antal funktioner: 6' och titeln följer källan och den skrivna 9W.
- **46314 (GODKÄND):** Live ACTIVE, 23TCF65000, EAN 8717842036570, lager 1, tagg På beställning, leveranstidsmeningen finns. Typordet Crosstrainer står i egen källa och i taggarna (R7). Motsägelsen 32/26 belastningsnivåer och oklara 'Belastning: 35 kg' rätt utelämnade. 7-tums skärm, 26 program, Bluetooth, PMS, 50 cm steglängd, mått, vikt och 150 kg enligt tillverkaren stämmer.

## Avvisade (k_46sak4_avvisade.json)

Alla 10 avvisningar kontrollerades live och är riktiga: trampolin med bara löftestext (v1.10 undantar trampoliner), Fila-skridskor där källan anger 35–43 men varianterna är 30/31, Tunturi-skivor med olika pris och motsägande håldiameter, Liv Tempt med motsägande målgrupp och lager 0, Union Lite S redan skriven, fälgskydd för 6 779 kr med bara titel, viktlås och pedalklossar med tom källa, och Romet Finale där titeln säger röd men källan grön. Ingen lyfts ur.

## Frågor till David

1. 46310 AXA Compactline 20 lux (93932095CB) är samma lampa som den skrivna 10472255455498 (93932095BX), bara annan förpackningskod. Ska den ena arkiveras efter att lagret flyttats, eller ska båda ligga kvar?
2. 46307 och 46308 (barnhjälmar) står på spärrlistan; ett undantag med hänvisning till beslutet 2026-11-08 behövs innan skrivning.
3. Melon Camouflage Black finns också i M/L (10471081541898, DRAFT). Om den aktiveras behöver titlarna skiljas åt med storlek.
