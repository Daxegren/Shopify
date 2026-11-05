# Granskningsutlåtande k_33b (kosttillskott, BEST OF SPORTS)

Granskare: Opus, oberoende. Datum: 2026-11-05. Bara läsning: källan lästes live via Admin API (shopify_api.py, butiken bekräftad som BEST OF SPORTS/bestofsports.se). Inget ändrades i Shopify och inget committades.

Underlag: regelbok v1.4–v1.10, BESLUTSLOGG (Davids beslut 2026-11-05: endast produktfakta och dos enligt tillverkaren, inga effektpåståenden), butiksprofil, LARDOMAR, kosttillskott-exempel-2026-11-05.md och tidigare utlåtanden (k_utlatande_28jk30e, k_32cde).

## Resultat

- GODKÄND: 1 (33020)
- RÄTTA: 6 (33012, 33014, 33018, 33019, 33021, 33022). Alla gäller typordet i titel och SEO-titel. Meta och html är rena.
- UNDERKÄND: 2 (33013, 33015). Båda innehåller glukosamin, som Läkemedelsverket har klassat som läkemedel.
- Avvisade (33016 Collagen Anti-Age, 33017 Berberine+Turmeric): avvisningen står sig. 33016 har en motsägelse mellan källtext och ingredienslista, och namnet "Anti-Age" är ett påstående. 33017 har en trasig ingredienslista ("lakritsrotsextrakt (Berberis aristata)"), och typordet "Antioxidant" är ett effektord. Ingen av dem lyfts.

## Kontroller som gjorts på alla

- Varje mängd (procent, mg, dos, ml, g, temperatur) jämfördes mot live-texten. Inga avvikelser hittades.
- Effektord söktes i titel, SEO, meta, "Passar för" och specifikation (energi, minne, sömn, stress, led, hud, stöd, bidrar, hjälper, vitalitet, adaptogen m.fl.). De enda träffarna med påståendeinnehåll var typordet "Adaptogen", som rättas. Övriga träffar är ingredienser eller förvaring (rödbetsjuicekoncentrat, antioxidant tokoferoler, "skyddad mot ljus") eller tillverkarens säkerhetsvarningar ("sömntabletter" i 33021, "före sänggåendet").
- Kontrollscriptets "halsa" på koffein, vitamin och Energi är kända falsklarm. De bedömdes manuellt som OK.
- Källornas generella allergenrader ("kan innehålla mjölk, soja, vete ...") har utelämnats i alla utkast, vilket är rätt. Ingen allergenrad i utkasten säger emot ingredienslistan, och fisk och gelatin står i 33015:s ingredienslista.
- Standardblocket är exakt likt b_skriv_24. Ingen har taggen "På beställning". Alla är ACTIVE med en variant och har lager.
- Titlarna har ≤70 tecken och ≤2 kommatecken, SEO-titlarna ≤43 tecken (även efter rättning) och metan 133–147 tecken med verb, utom 33015 (se nedan). Alla är unika mot alla *_utkast.json och *skriv*.json och mot butikens titlar (sökning på Ashwagandha, Caffeine, Bacopa och Hyaluronic).

## Typorden

- **Adaptogen** (33018, 33019, 33021, 33022) är ett effektord. Det betyder att produkten hjälper kroppen att anpassa sig till stress, alltså ett underförstått hälsopåstående (förordning 1924/2006 art. 2.2.5). Källtexterna själva använder ordet som påstående ("har adaptogena egenskaper och hjälper till att bibehålla vitalitet"). Det byts mot **Kosttillskott**. Ordet står i källtexten för 33018 och 33022 och är productType för alla fyra, med prejudikat i 30007 "Kosttillskott Trec Coenzyme Q10". Avsteget från live-ordet (R7) motiveras av påståendereglerna och redovisas för David.
- **Mineral kapslar** (33014) är fel i sak, eftersom produkten inte innehåller något mineral. Ordet byts mot Kosttillskott (källan: "är ett kosttillskott"). **Mineral** (33013) och **Mineralpulver** (33015) gäller underkända produkter. Det första är fel i sak, det andra delvis riktigt (kalcium, magnesium).
- **Koffeintabletter** (33012) är inget effektord, men det säger emot "120 kapslar" i samma titel. Ordet byts mot "Koffein", som står i källtexten.
- **Energigel** (33020) är en vedertagen produktbenämning som används i den skrivna 30018. Ingen rättning.

## Laglighet i Sverige

- **Ashwagandha (33019, 33021, 33022):** produkten är inte olaglig i Sverige. Livsmedelsverket (sidan "Växtbaserade kosttillskott", granskad 2026-09-16, och nyheten 2025-05-02) skriver att verket "inväntar EUs granskning och har inte gjort någon egen riskvärdering av växten". Ashwagandha är ett av tolv ämnen under EU-granskning, och företagen ska kunna visa att produkten är säker. Det finns inget svenskt förbud och ingen läkemedelsklassning. Tyska BfR avråder. Enligt sekundärkällor är ashwagandha förbjudet i kosttillskott i Danmark och Frankrike, och Nederländerna avser att förbjuda det. 33019 innehåller extrakt av hela växten, även bladen. Därför GODKÄND efter rättning, men med en risk som David behöver känna till.
- **Bacopa (33018):** lagligt. Växten räknas inte som nytt livsmedel i EU-katalogen (använd före 1997), och ingen svensk läkemedelsklassning hittades. Källans minnespåståenden finns inte i utkastet.
- **Koffein (33012, 33020):** lagligt. Varningstexterna för barn och gravida finns med.
- **Glukosamin (33013, 33015):** Läkemedelsverket beslutade 2001 att "produkter som innehåller glukosamin ska klassificeras som läkemedel" (riksdagens skriftliga fråga 2000/01:1500, svar 2001-07-24). År 2003 kallade verket fortsatt försäljning i hälsokostbutik för "en överträdelse av läkemedelslagen" (Läkemedelsvärlden 2003-08-07). Godkända glukosaminläkemedel finns (Glucomed, Glucosamine Navamedic). Ingen senare ändring av klassningen hittades, men källorna är gamla, och nyare praxis har inte kunnat bekräftas. Därför UNDERKÄND tills David beslutat.
- **Hyaluron och kondroitin (33014):** ingen svensk läkemedelsklassning hittades. Lagligt enligt det som har kunnat kontrolleras.

## Domar

| nr | id | produkt | dom | rättning eller skäl |
|---|---|---|---|---|
| 33012 | 10472270004490 | Koffein Essensey Caffeine | RÄTTA | titel: "Koffeintabletter Trec Essensey Caffeine, 120 kapslar" → "Koffein Trec Essensey Caffeine, 120 kapslar"; seo_title: "Koffeintabletter Trec Essensey Caffeine" → "Koffein Trec Essensey Caffeine" |
| 33013 | 10472277180682 | Glucosamine+Chondroitin+MSM | UNDERKÄND | Kan vara otillåtet i Sverige: glukosamin är klassat som läkemedel av Läkemedelsverket. Riksdagen skriftlig fråga 2000/01:1500 med svar 2001-07-24 (https://www.riksdagen.se/sv/dokument-och-lagar/dokument/skriftlig-fraga/glukosamin_go111500/): "Läkemedelsverket har beslutat att produkter som innehålle… |
| 33014 | 10472277213450 | Hyaluronic Acid | RÄTTA | titel: "Mineral kapslar Trec Essensey Hyaluronic Acid, 90 kapslar" → "Kosttillskott Trec Essensey Hyaluronic Acid, 90 kapslar"; seo_title: "Mineral kapslar Trec Hyaluronic Acid" → "Kosttillskott Trec Hyaluronic Acid" |
| 33015 | 10472277311754 | TBL Flexi Move | UNDERKÄND | Innehåller glukosaminsulfat 2KCl (ingredienslistan), och samma läkemedelsklassning som för 33013 gäller: Riksdagen skriftlig fråga 2000/01:1500 med svar 2001-07-24 (https://www.riksdagen.se/sv/dokument-och-lagar/dokument/skriftlig-fraga/glukosamin_go111500/): "Läkemedelsverket har beslutat att produ… |
| 33018 | 10472280719626 | Bacopa Monnieri | RÄTTA | titel: "Adaptogen Trec Essensey Bacopa Monnieri, 90 kapslar" → "Kosttillskott Trec Essensey Bacopa Monnieri, 90 kapslar"; seo_title: "Adaptogen Trec Essensey Bacopa Monnieri" → "Kosttillskott Trec Essensey Bacopa Monnieri" |
| 33019 | 10472280785162 | Ashwagandha Max | RÄTTA | titel: "Adaptogen Trec Ashwagandha Max, 60 kapslar" → "Kosttillskott Trec Ashwagandha Max, 60 kapslar"; seo_title: "Adaptogen Trec Ashwagandha Max" → "Kosttillskott Trec Ashwagandha Max" |
| 33020 | 10472297693450 | Hydro Caffeine Energy Gel | GODKÄND | Live: ACTIVE, EAN-SKU 5902114048365, 39 kr, lager 12. Ingredienserna, 60 ml per portion, upp till 3 per dag (180 ml), skaka före, varningarna (under 18 år, hjärt-kärlsjukdom, koffeinintolerans, inte före sänggåendet, inga andra koffeinkällor) och förvaringen vid 5–25 °C stämmer. Energiboost-, result… |
| 33021 | 10472297824522 | Ashwagandha | RÄTTA | titel: "Adaptogen Trec Ashwagandha, 60 kapslar" → "Kosttillskott Trec Ashwagandha, 60 kapslar"; seo_title: "Adaptogen Trec Ashwagandha" → "Kosttillskott Trec Ashwagandha" |
| 33022 | 10472302018826 | Ashwagandha KSM-66 | RÄTTA | titel: "Adaptogen Trec Ashwagandha KSM-66, 60 kapslar" → "Kosttillskott Trec Ashwagandha KSM-66, 60 kapslar"; seo_title: "Adaptogen Trec Ashwagandha KSM-66" → "Kosttillskott Trec Ashwagandha KSM-66" |

Fullständiga skäl per produkt finns i `vag2_skriv/k_utlatande_33b.json`. Varje rättning är ett enda sammanhängande före/efter-par per fält, och alla fore-strängar träffar exakt en gång i utkastet (kontrollerat).

## Frågor till David

1. **Glukosamin (33013, 33015):** ska produkterna skrivas trots Läkemedelsverkets klassning från 2001, eller ska klassningen först kontrolleras med Läkemedelsverket? Rekommendation: skriv dem inte, och fråga Läkemedelsverket om produkterna ens får säljas. Risk om de skrivs: vi marknadsför det som kan vara ett oregistrerat läkemedel. Om inget beslutas ligger de kvar med de gamla texterna, som innehåller ledpåståenden.
2. **Ashwagandha (33019, 33021, 33022) och Danmark:** produkterna är lagliga i Sverige. Säljer butiken till Danmark eller Frankrike, där ashwagandha enligt sekundärkällor är förbjudet? Rekommendation: skriv texterna, men spärra leverans dit eller kontrollera saken.
3. **Typordet Kosttillskott i stället för Adaptogen och Mineral kapslar:** bekräftelse behövs, eftersom det avviker från live-ordet (R7).

Källor: [Livsmedelsverket, Växtbaserade kosttillskott](https://www.livsmedelsverket.se/livsmedel-och-innehall/kosttillskott/vaxtbaserade-kosttillskott/), [Livsmedelsverket omarbetar informationen om ashwagandha](https://www.livsmedelsverket.se/foretagande-regler-kontroll/nyheter-for-livsmedelsforetag/nyheter-for-foretag/livsmedelsverket-omarbetar-informationen-om-ashwagandha/), [BfR om ashwagandha](https://mobil.bfr.bund.de/cm/349/ashwagandha-food-supplements-with-potential-health-risks.pdf), [Riksdagen fråga 2000/01:1500 glukosamin](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/skriftlig-fraga/glukosamin_go111500/), [Läkemedelsvärlden 2003](https://www.lakemedelsvarlden.se/halsokostaffarer-saljer-ater-glukosamin/), [MDPI Foods 14(18):3275 (Bacopa, novel food)](https://www.mdpi.com/2304-8158/14/18/3275), [nutritioninsight.com om ashwagandha i Europa](https://nutritioninsight.com/news/regulatory-update-spotlight-on-international-authorities-response-to-ashwagandha-safety-concerns.html), [food-safety.com, Nederländerna](https://www.food-safety.com/articles/11333-netherlands-set-to-ban-ashwagandha).
