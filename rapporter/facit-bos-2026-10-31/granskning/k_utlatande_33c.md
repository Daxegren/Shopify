# Granskningsutlåtande k_33c (BEST OF SPORTS), 2026-11-05

Granskaren är Opus och har bara läst. Underlaget är `vag2_skriv/k_33c_utkast.json`, nio kosttillskott och energiprodukter (33023–33031). Källtext, status, varianter (SKU, EAN, pris), lager och taggar lästes live via Admin API (`shopify_api.py`, ShopifyKlient) 2026-11-05. Butiken bekräftades som BEST OF SPORTS (bestofsports.se). Ingenting skrevs i Shopify. Regler: regler-v1.md (v1.4–v1.10), BESLUTSLOGG 2026-11-05 (rad 'Kvarvarande kosttillskott ... skrivs utan att först fråga Livsmedelsverket eller jurist'), profilen, LARDOMAR och praxis i k_33b och k_32i33a (Boogieman- och Ashwagandha-syskonen).

**Resultat:** 0 GODKÄND, 8 RÄTTA, 1 UNDERKÄND (33030). På en rättad kopia utan 33030 ger `skrivfil_kontroll.py` 0 fel och 0 varningar. Utkastet gav 6 varningar om cirkulär inledning. `kontrollera_produkttext.py` ger 6 'halsa'. Fem av dem gäller ingrediensen koffein i meta, och det är ett känt falsklarm. En gäller 'Energi' i 33023, alltså typordet Energidryck, som jag har bedömt manuellt (se nedan). Titlarna har 39–70 tecken och högst 2 kommatecken, SEO-titlarna 31–42 tecken och metatexterna 133–150 tecken, alla med verb. Titel, SEO-titel och meta är unika inom batchen och mot alla andra utkast och `k_skriv_*.json` i `vag2_skriv/`. Varje 'före' förekommer exakt en gång i sitt fält, och varje fält har ETT sammanhängande före/efter-par. Standardblocket är identiskt med det kanoniska (`b_skriv_24.json`). Ingen produkt har taggen 'På beställning', och ingen text har leveranstidsmeningen. Alla har status ACTIVE och lager större än 0.

## Genomgående

- **Mängder mot live:** alla procentsatser, doser, ingredienslistor, förvaringsrader och varningsrader stämmer med live. Undantaget är de koffeinhaltiga shottarna (33027–33030). Live anger 15 ml per portion och 750 mg beta-alanin och 300 mg citrullinmalat, men utan att säga vad mängden gäller. Tillverkaren (trecnutrition.com/brands/trec/trec-core/boogieman-shot/) anger 50 ml (en halv flaska) med 2500 mg beta-alanin, 1000 mg citrullinmalat och 200 mg koffein för samma receptur. En äldre version (EAN 5902114017675) anges av leki.pl med 15 ml och 60 mg koffein. Det går inte att avgöra, så dos och mg-värden stryks (R2), som i den skrivna 33010.
- **Effektord:** jag sökte i titel, SEO-titel, meta, Passar för och specifikation efter energi, stöd, bidra, hjälp, förbättr, öka, minsk, trött, fokus, koncentr, uthåll, prestation, återhämt, immun, led, hud, sömn, minne, stress, vitalitet, potens, libido, viktminsk, anti-age, hälsa, naturlig, adaptogen, skärpa, kick, boost, muskel, blodflöde, optimal, ideal och premium. Efter rättning finns bara 'energidryck' (33023) och ingrediensord (citronjuicekoncentrat) kvar. Inga 'kan hjälpa', 'stödjer' eller 'bidrar till'.
- **Typord (R7, praxis k_33b och k_32i33a):** de skrivna syskonen (Boogieman Shot 33002, 33003 och 33010, Ashwagandha 33019, 33021 och 33022, Korean Ginseng 33005) har typordet Kosttillskott, efter att live-orden Adaptogen, Energishot och Koffeindrink byttes ut. Samma typord används här för 33024–33029 och 33031. Energidryck (33023) behålls, eftersom det är en vedertagen produktbenämning, som Energigel i 33020. 'Energikapslar' (33024) och 'Energishot' (shottarna) är våra egna eller leverantörens effektnära ord och byts.
- **Produktnamn:** 'Boogieman', 'Boogieman Shot' och 'Zero' är rena namn. 'Zero' stämmer med en ingredienslista utan socker, och texten påstår inget om socker. 'Herbal Energy' betyder ordagrant växtbaserad energi och är ett fantasinamn som kan uppfattas som ett hälsopåstående (1924/2006 art. 1.3). Det tas bort, som 'Tribido' i k_32i33a (se beslut 1).
- **33023 Zero:** källans 'inga sötningsmedel' säger emot ingredienslistan (sukralos, acesulfam K). Utkastaren har rätt utelämnat påståendet och den kopierade dosraden '50 ml'.
- **33029/33030 typord:** live-ordet 'Koffeinsot' är en felstavning av 'Koffeinshot' (Velomarkets engelska titel är 'Caffeine shot'). Utkastets 'Energishot' saknar stöd i produktens egen titel och ersätts med familjens Kosttillskott.
- **33031 'Koffeinfritt':** ingredienslistan saknar koffein och koffeinkällor. Butikens äldre utkastannons heter 'Boogieman Shot Caffeine Free', och återförsäljare (store.mygp.com, muscleshop.lt) säljer den som Caffeine Free. Titeln får tillverkarens variantnamn 'Caffeine Free' efter typordet. Texten innehåller inget eget påstående om koffeinfrihet.
- **Förpackning:** tillverkaren anger en flaska på 100 ml för shottarna. Källans 'Förvara burken' rättas därför till 'Flaskan', så att texten inte säger emot sig själv.

## Juridisk kontroll (webbsök 2026-11-05)

- **Ashwagandha (33025):** enligt Livsmedelsverkets sida 'Växtbaserade kosttillskott' (https://www.livsmedelsverket.se/livsmedel-och-innehall/kosttillskott/vaxtbaserade-kosttillskott/, senast granskad 2026-09-16) är ashwagandha 'ett av de 12 vanligt förekommande ämnen eller växter i kosttillskott som just nu granskas av EU'. Där står också: 'Livsmedelsverket inväntar EUs granskning och har inte gjort någon egen riskvärdering av växten' och 'Alla företag som tillverkar eller säljer kosttillskott ska kunna visa att deras produkter är säkra för konsumenterna.' Nyheten 'Livsmedelsverket omarbetar informationen om ashwagandha' (2025-05-02) innehåller varken förbud eller avrådan. **Slutsats:** ashwagandha är inte förbjudet i kosttillskott i Sverige, så produkten godkänns med bara fakta (dom RÄTTA för typordet). Danmark har förbjudit ashwagandha (2023), och tyska BfR avråder. Se beslut 2.
- **Guarana och ginseng (33024) och Boswellia (33026):** Livsmedelsverket har inga förbud eller avrådanden om dem. Sidan nämner bara ashwagandha bland EU:s granskade ämnen. Alla tre säljs som kosttillskott i Sverige, och Korean Ginseng (33005) är redan skriven. Godkänns med bara fakta. Rosenrot och ginseng i 33031 står bara som ingredienser.

## Beslut för David

1. **Namnet 'Herbal Energy' (33024).** Alternativ: (a) ta bort namnet ur titel och text, som granskat (rekommendation, samma linje som Tribido), eller (b) behåll tillverkarens namn, men då ska produkten underkännas. Risk med (a): kunder som söker på 'Herbal Energy' hittar sämre, men handle och EAN är oförändrade. Om inget beslutas skrivs (a).
2. **Ashwagandha på bestofsports.dk.** Ashwagandha är förbjudet i kosttillskott i Danmark sedan 2023. Butiken har samma produkter på .dk, och här finns 33025 och de skrivna 33019, 33021 och 33022. Rekommendation: ta bort dessa från den danska marknaden (Markets). Det är en butiksändring och kräver ditt ja. Texten för Sverige påverkas inte. Om inget beslutas fortsätter produkterna att visas för danska kunder.
3. **Boogieman-dubbletter.** 33030 Bubble Gum är samma produkt och smak som den skrivna 33010 och underkänns (R12a). 33027 Skogsbär och 33028 Grapefrukt-Lime motsvarar 33002 Forest Fruit och 33003 Grapefruit-Lime (olika EAN, alla aktiva med lager). Rekommendation: ta med alla tre paren i planen för dubbletter. Tills dess skrivs 33027 och 33028 (deras live-texter har energi- och trötthetspåståenden, som bör bort), och 33030 behåller sin live-text med påståenden. Alternativ: skriv även 33030 med ett avvikande typord. Det rekommenderas inte.
4. **Profilen:** `frislappta_2026_11_05.kosttillskott` i butiksprofilen säger fortfarande att 'växtextrakt, koffein/energishots' är utanför, trots BESLUTSLOGG 2026-11-05. Profilen behöver uppdateras med ditt ja, så att framtida granskare inte underkänner enligt R6.
5. **Märkning vid distansförsäljning:** källorna saknar näringsvärden och koffeinhalt per portion. Det är ett allmänt hål för alla kosttillskott, inte bara den här batchen.

## Per produkt

| nr | id | dom | fält som rättas |
|---|---|---|---|
| 33023 | 10472323088650 | RÄTTA | meta, html |
| 33024 | 10472323219722 | RÄTTA | titel, seo_title, meta, html |
| 33025 | 10472351203594 | RÄTTA | titel, seo_title, meta, html |
| 33026 | 10635764334858 | RÄTTA | titel, seo_title, meta, html |
| 33027 | 10656694042890 | RÄTTA | titel, seo_title, meta, html |
| 33028 | 10656694075658 | RÄTTA | titel, seo_title, meta, html |
| 33029 | 10656694141194 | RÄTTA | titel, seo_title, meta, html |
| 33030 | 10656694173962 | UNDERKÄND | - |
| 33031 | 10656694206730 | RÄTTA | titel, seo_title, meta, html |

### 33023 (10472323088650, k_33c_utkast.json): RÄTTA

Live: ACTIVE, 'Energidryck TREC Boogieman Zero 500ml', EAN 5902114042912, 19 kr, lager 14, en variant. Ingredienslistan, användningen 30 minuter före träning, förvaringen och varningsraden (gravida, ammande, under 18 år, cirkulation, koffeinkänslighet, alkohol, annat koffein, före sänggåendet) stämmer ord för ord. Källans 'inga sötningsmedel' säger emot ingredienslistan (sukralos, acesulfam K) och är rätt utelämnat (R2). Sötningsmedlen står bara i listan. Dosraden '50 ml eller följ tillverkarens anvisningar' och 'skaka' för en kolsyrad dryck på 500 ml är rätt utelämnade (troligen kopierade från shot-texterna). 'Läcker', 'uppfriskande' och 'ökad fysisk och mental stress' är borta. Typordet Energidryck är live-ordet och en vedertagen produktbenämning (som Energigel i 33020, k_33b), inget effektlöfte. 'Zero' är tillverkarens produktnamn och stämmer med en ingredienslista utan socker. Det står inget om socker eller kalorier i texten. Rättning: cirkulär inledning i meta och första meningen (skriptvarning). Två 'enligt tillverkaren' (R5).

- `meta` före: `Trec Boogieman Zero är en kolsyrad energidryck med tropisk fruktsmak, taurin, koffein samt vitamin B6 och B12. Flaskan innehåller 500 ml.`
  efter: `Trec Boogieman Zero är kolsyrad, har tropisk fruktsmak och innehåller taurin, koffein samt vitamin B6 och B12. Flaskan rymmer 500 ml.`

- `html` före: `Trec Boogieman Zero är en kolsyrad energidryck med`
  efter: `Den kolsyrade drycken Trec Boogieman Zero har`

### 33024 (10472323219722, k_33c_utkast.json): RÄTTA

Live: ACTIVE, 'Naturliga energikapslar TREC Herbal Energy, 60 kapslar', EAN 5902114017798, 119 kr, lager 7. Procentsatserna (63 % guarana med 22 % koffein, 8 % och 8 % ginseng med 10 % och 5 % ginsenosider), dosen 2 kapslar med 300 ml vatten en gång dagligen, 'inte mer än 3 på varandra följande månader', förvaringen och varningarna stämmer. Den motsägande tidsraden ('helst efter frukost' och 'ta inte ... efter frukost') är rätt utelämnad (R2), och 'Naturliga' är borta. Juridik: Livsmedelsverket har ingen förbudsuppgift om guarana eller ginseng, och båda säljs allmänt som kosttillskott i Sverige. Korean Ginseng (33005) är redan skriven. Rättning 1, typordet: 'Energikapslar' är vårt eget typord och beskriver en effekt (kapslar som ger energi). Det byts mot Kosttillskott (productType, och samma typord som för 33005 och 33b). Rättning 2, namnet: 'Herbal Energy' betyder ordagrant växtbaserad energi. Ett fantasinamn som kan uppfattas som ett hälsopåstående får enligt förordning 1924/2006 art. 1.3 bara användas tillsammans med ett godkänt påstående, och det finns inget godkänt påstående för koffein eller guarana. Samma bedömning som för 'Tribido' i k_32i33a: namnet tas bort ur titel, SEO-titel, meta och första meningen. Produkten identifieras genom Trec, guarana, ginseng, 60 kapslar och EAN, och handle ändras inte (R12a). Vill David behålla tillverkarens namn ska produkten i stället underkännas. Meta och första mening skrivs samtidigt om utan cirkulär inledning.

- `titel` före: `Energikapslar Trec Herbal Energy, 60 kapslar`
  efter: `Kosttillskott Trec Guarana och Ginseng, 60 kapslar`

- `seo_title` före: `Energikapslar Trec Herbal Energy`
  efter: `Kosttillskott Trec Guarana och Ginseng`

- `meta` före: `Trec Herbal Energy är ett komplex med guaranaextrakt och ginsengextrakt i 60 kapslar. Dosen är 2 kapslar med 300 ml vatten en gång dagligen.`
  efter: `Trecs kapslar innehåller guaranaextrakt samt koreanskt och amerikanskt ginsengextrakt. Burken har 60 kapslar, dosen är 2 kapslar en gång dagligen.`

- `html` före: `Trec Herbal Energy är ett komplex av guaranaextrakt samt koreanskt och amerikanskt ginsengextrakt i kapselform`
  efter: `Kapslarna från Trec innehåller ett komplex av guaranaextrakt samt koreanskt och amerikanskt ginsengextrakt`

### 33025 (10472351203594, k_33c_utkast.json): RÄTTA

Live: ACTIVE, 'Adaptogen TREC ESSENSEY ASHWAGANDHA EXCLUSIVE KSM-66 90 kapslar', SKU 21724/EAN 5902114047412, 199 kr, lager 8. 40 % KSM-66-extrakt (5 % withanolider), maltodextrin, HPMC-kapsel, dosen 1 kapsel med måltid, förvaringen och varningen stämmer. 'Vegetarianer ... enligt tillverkaren' följer källan ('idealiskt för vegetarianer tack vare sin cellulosakapsel'). Alla stress-, uthållighets-, energi- och vitalitetspåståenden är borta. Juridik: Livsmedelsverkets sida om växtbaserade kosttillskott (https://www.livsmedelsverket.se/livsmedel-och-innehall/kosttillskott/vaxtbaserade-kosttillskott/, granskad 2026-09-16) säger att ashwagandha är ett av tolv ämnen som granskas av EU, att verket 'inväntar EUs granskning och har inte gjort någon egen riskvärdering av växten', och att företagen ska kunna visa att produkterna är säkra. Nyheten 2025-05-02 ('Livsmedelsverket omarbetar informationen om ashwagandha') innehåller varken förbud eller avrådan. Ashwagandha är alltså inte förbjudet i kosttillskott i Sverige. Därför godkänns innehållet med bara fakta. Danmark har däremot förbjudit det (2023), och BfR avråder (se beslut om .dk). Rättning: typordet Kosttillskott i stället för källordet Ashwagandha, enhetligt med de skrivna 33019, 33021 och 33022 ('Kosttillskott Trec Ashwagandha ...', k_33b). SEO-titeln får 'Exclusive', eftersom 'Kosttillskott Trec Ashwagandha KSM-66' redan finns på 33022. Cirkulär meta och första mening rättas.

- `titel` före: `Ashwagandha Trec Essensey Exclusive KSM-66, 90 kapslar`
  efter: `Kosttillskott Trec Essensey Ashwagandha Exclusive KSM-66, 90 kapslar`

- `seo_title` före: `Ashwagandha Trec Essensey KSM-66`
  efter: `Kosttillskott Trec Ashwagandha Exclusive`

- `meta` före: `Trec Essensey Ashwagandha Exclusive KSM-66 är ett kosttillskott med ashwagandha-rotextrakt i 90 kapslar. Dosen är 1 kapsel dagligen.`
  efter: `Trec Essensey Ashwagandha Exclusive KSM-66 innehåller ashwagandha-rotextrakt i cellulosakapslar. Burken har 90 kapslar, dosen är 1 kapsel dagligen.`

- `html` före: `är ett kosttillskott som innehåller`
  efter: `innehåller`

### 33026 (10635764334858, k_33c_utkast.json): RÄTTA

Live: ACTIVE, 'Adaptogen TREC ESSENSEY BOSWELLIA SERRATA 90 kapslar', SKU 21728/EAN 5902114047436, 129 kr, lager 11. 77 % extrakt av indisk rökelse med 60 % boswellinsyra, HPMC-kapsel, 2 kapslar dagligen med vatten och mat, förvaringen och varningen stämmer. '1000 mg' (anger inte per vad) och 'indiskt fikonträd' (fel) är rätt utelämnade (R2), och ben- och ledpåståendena är borta. Juridik: Boswellia nämns inte på Livsmedelsverkets sida och omfattas inte av något svenskt förbud som jag har hittat. Livsmedelsverket nämner bara ashwagandha bland EU:s tolv granskade ämnen. Boswellia säljs som kosttillskott hos svenska återförsäljare. Rättning: typordet Kosttillskott (live 'Adaptogen' är ett effektord, praxis k_33b), cirkulär meta och första mening. 'Boswellia Serrata' är kvar som namn. En 'enligt tillverkaren'.

- `titel` före: `Boswellia Serrata Trec Essensey, 90 kapslar`
  efter: `Kosttillskott Trec Essensey Boswellia Serrata, 90 kapslar`

- `seo_title` före: `Boswellia Serrata Trec Essensey`
  efter: `Kosttillskott Trec Boswellia Serrata`

- `meta` före: `Trec Essensey Boswellia Serrata är ett kosttillskott med extrakt av indisk rökelse i 90 kapslar. Dosen är 2 kapslar dagligen med vatten och mat.`
  efter: `Trec Essensey Boswellia Serrata innehåller extrakt av indisk rökelse med 60 % boswellinsyra. Burken har 90 kapslar, dosen är 2 kapslar dagligen.`

- `html` före: `är ett kosttillskott som innehåller`
  efter: `innehåller`

### 33027 (10656694042890, k_33c_utkast.json): RÄTTA

Live: ACTIVE, 'Energishot TREC Boogieman Shot 100ml, Skogsbär', EAN 5902114081416, 29 kr, lager 4. Typordet: live 'Energishot' ersätts med Kosttillskott, som för de skrivna Boogieman-syskonen 33002, 33003 och 33010 (k_skriv_32i33a, där Energishot och Koffeindrink byttes av samma skäl: 'energi' ligger nära ett energilöfte, och källan säger 'flytande kosttillskott', R7). Dos och mängder: live anger 15 ml per portion och beta-alanin 750 mg och citrullinmalat 300 mg utan att säga vad mängden gäller. Tillverkarens sida (https://trecnutrition.com/brands/trec/trec-core/boogieman-shot/) anger för samma receptur (inosin, AAKG, taurin, citrullinmalat, koffein) en portion på 50 ml (en halv flaska) med 2500 mg beta-alanin, 1000 mg citrullinmalat och 200 mg koffein. En äldre version med eget EAN (leki.pl, EAN 5902114017675) anger 15 ml, 750 mg och 60 mg koffein. Vilken som gäller just detta EAN går inte att avgöra, och en för låg dos med koffein får inte stå (R2). Därför stryks 15 ml och mg-värdena, som i 33010. Användningen '30 minuter före träning', 'skakas väl' och alla varningar står kvar. Förpackning: tillverkaren anger en flaska på 100 ml, så 'flaska' står kvar (R1 v1.6), men raden 'Förvaring: Burken stängd' (källans ord) rättas till 'Flaskan stängd', så att texten inte säger emot sig själv. Cirkulär inledning i meta och första meningen ('X är ett ... kosttillskott') rättas (skriptvarning, praxis k_30ab och k_32i33a). Taurin och koffein står i meta som ingredienser, utan effekt (skriptets 'halsa' på 'koffein' är ett känt falsklarm). Alla energi-, fokus-, uthållighets- och blodflödesfraser ur källan är borta, och L-tyrosin, som saknas i ingredienslistan, är rätt utelämnat. Möjlig dubblett: 33002 (10462770135306, 'Forest Fruit' = skogsbär, EAN 5902114047320, ACTIVE, lager 10) är redan skriven. Olika EAN, och en svensk respektive en engelsk smakbenämning, ger unika titlar. Bör tas med i planen för dubbletter.

- `titel` före: `Energishot Trec Boogieman Shot, Skogsbär, 100 ml`
  efter: `Kosttillskott Trec Boogieman Shot Skogsbär, 100 ml`

- `seo_title` före: `Energishot Trec Boogieman Skogsbär`
  efter: `Kosttillskott Trec Boogieman Skogsbär`

- `meta` före: `Trec Boogieman Shot Skogsbär är ett flytande kosttillskott i flaska på 100 ml med beta-alanin och citrullinmalat. Portionen är 15 ml.`
  efter: `Trec Boogieman Shot Skogsbär innehåller beta-alanin, citrullinmalat, taurin och koffein. Det flytande kosttillskottet säljs i flaska på 100 ml.`

- `html` före: `är ett färdigt att dricka flytande kosttillskott i flaska på 100 ml. Huvudingredienserna är beta-alanin (750 mg) och citrullinmalat (300 mg). Portionen är 15 ml.</p><h2>Passar för</h2><ul>
<li>Dig som vill ha ett flytande kosttillskott i färdig shot</li>
<li>Dig som vill ha en portion om 15 ml att dricka 30 minuter före träning</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Flytande kosttillskott (shot)</li>
<li>Smak: Skogsbär</li>
<li>Förpackning: Flaska, 100 ml</li>
<li>Innehåll: Beta-alanin (750 mg), citrullinmalat (300 mg), L-arginin, taurin och koffein</li>
<li>Ingredienser: Vatten, äppeljuicekoncentrat 17 %, beta-alanin, citronjuicekoncentrat 3 %, L-arginin-alfa-ketoglutarat (AAKG), taurin, L-citrullinmalat, vattenfritt koffein, inosin, smakämnen, sötningsmedel (acesulfam K, sukralos, neotam), maltodextrin, konserveringsmedel (kaliumsorbat, natriumbensoat)</li>
<li>Rekommenderad daglig dos: 15 ml</li>
<li>Användning: 15 ml (1 portion) 30 minuter före träning, skakas väl före användning</li>
<li>Förvaring: Burken`
  efter: `levereras färdig att dricka i en flaska på 100 ml. Det flytande kosttillskottet har beta-alanin och citrullinmalat som huvudingredienser.</p><h2>Passar för</h2><ul>
<li>Dig som vill ha ett flytande kosttillskott i färdig shot</li>
<li>Dig som vill ha en färdig shot att dricka 30 minuter före träning</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Flytande kosttillskott (shot)</li>
<li>Smak: Skogsbär</li>
<li>Förpackning: Flaska, 100 ml</li>
<li>Innehåll: Beta-alanin, citrullinmalat, L-arginin, taurin och koffein</li>
<li>Ingredienser: Vatten, äppeljuicekoncentrat 17 %, beta-alanin, citronjuicekoncentrat 3 %, L-arginin-alfa-ketoglutarat (AAKG), taurin, L-citrullinmalat, vattenfritt koffein, inosin, smakämnen, sötningsmedel (acesulfam K, sukralos, neotam), maltodextrin, konserveringsmedel (kaliumsorbat, natriumbensoat)</li>
<li>Användning: 30 minuter före träning, skakas väl före användning</li>
<li>Förvaring: Flaskan`

### 33028 (10656694075658, k_33c_utkast.json): RÄTTA

Live: ACTIVE, 'Energishot TREC Boogieman Shot 100ml, Grapefrukt-Lime', EAN 5902114081423, 29 kr, lager 5. Typordet: live 'Energishot' ersätts med Kosttillskott, som för de skrivna Boogieman-syskonen 33002, 33003 och 33010 (k_skriv_32i33a, där Energishot och Koffeindrink byttes av samma skäl: 'energi' ligger nära ett energilöfte, och källan säger 'flytande kosttillskott', R7). Dos och mängder: live anger 15 ml per portion och beta-alanin 750 mg och citrullinmalat 300 mg utan att säga vad mängden gäller. Tillverkarens sida (https://trecnutrition.com/brands/trec/trec-core/boogieman-shot/) anger för samma receptur (inosin, AAKG, taurin, citrullinmalat, koffein) en portion på 50 ml (en halv flaska) med 2500 mg beta-alanin, 1000 mg citrullinmalat och 200 mg koffein. En äldre version med eget EAN (leki.pl, EAN 5902114017675) anger 15 ml, 750 mg och 60 mg koffein. Vilken som gäller just detta EAN går inte att avgöra, och en för låg dos med koffein får inte stå (R2). Därför stryks 15 ml och mg-värdena, som i 33010. Användningen '30 minuter före träning', 'skakas väl' och alla varningar står kvar. Förpackning: tillverkaren anger en flaska på 100 ml, så 'flaska' står kvar (R1 v1.6), men raden 'Förvaring: Burken stängd' (källans ord) rättas till 'Flaskan stängd', så att texten inte säger emot sig själv. Cirkulär inledning i meta och första meningen ('X är ett ... kosttillskott') rättas (skriptvarning, praxis k_30ab och k_32i33a). Taurin och koffein står i meta som ingredienser, utan effekt (skriptets 'halsa' på 'koffein' är ett känt falsklarm). Alla energi-, fokus-, uthållighets- och blodflödesfraser ur källan är borta, och L-tyrosin, som saknas i ingredienslistan, är rätt utelämnat. SEO-titeln blir 'Kosttillskott Trec Boogieman Grapefrukt' (hela smaknamnet ger 44 tecken). Den skiljer sig från 33003 ('Grapefruit', 10462770299146, EAN 5902114017675, ACTIVE, lager 9, redan skriven) bara i en bokstav. Det är samma smak, så det är en möjlig dubblett som bör tas med i planen för dubbletter.

- `titel` före: `Energishot Trec Boogieman Shot, Grapefrukt-Lime, 100 ml`
  efter: `Kosttillskott Trec Boogieman Shot Grapefrukt-Lime, 100 ml`

- `seo_title` före: `Energishot Trec Boogieman Grapefrukt-Lime`
  efter: `Kosttillskott Trec Boogieman Grapefrukt`

- `meta` före: `Trec Boogieman Shot Grapefrukt-Lime är ett flytande kosttillskott i flaska på 100 ml med beta-alanin och citrullinmalat. Portionen är 15 ml.`
  efter: `Trec Boogieman Shot Grapefrukt-Lime innehåller beta-alanin, citrullinmalat, taurin och koffein. Det flytande kosttillskottet säljs i flaska på 100 ml.`

- `html` före: `är ett färdigt att dricka flytande kosttillskott i flaska på 100 ml. Huvudingredienserna är beta-alanin (750 mg) och citrullinmalat (300 mg). Portionen är 15 ml.</p><h2>Passar för</h2><ul>
<li>Dig som vill ha ett flytande kosttillskott i färdig shot</li>
<li>Dig som vill ha en portion om 15 ml att dricka 30 minuter före träning</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Flytande kosttillskott (shot)</li>
<li>Smak: Grapefrukt-Lime</li>
<li>Förpackning: Flaska, 100 ml</li>
<li>Innehåll: Beta-alanin (750 mg), citrullinmalat (300 mg), L-arginin, taurin och koffein</li>
<li>Ingredienser: Vatten, äppeljuicekoncentrat 17 %, beta-alanin, citronjuicekoncentrat 3 %, L-arginin-alfa-ketoglutarat (AAKG), taurin, L-citrullinmalat, vattenfritt koffein, inosin, smakämnen, sötningsmedel (acesulfam K, sukralos, neotam), maltodextrin, konserveringsmedel (kaliumsorbat, natriumbensoat)</li>
<li>Rekommenderad daglig dos: 15 ml</li>
<li>Användning: 15 ml (1 portion) 30 minuter före träning, skakas väl före användning</li>
<li>Förvaring: Burken`
  efter: `levereras färdig att dricka i en flaska på 100 ml. Det flytande kosttillskottet har beta-alanin och citrullinmalat som huvudingredienser.</p><h2>Passar för</h2><ul>
<li>Dig som vill ha ett flytande kosttillskott i färdig shot</li>
<li>Dig som vill ha en färdig shot att dricka 30 minuter före träning</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Flytande kosttillskott (shot)</li>
<li>Smak: Grapefrukt-Lime</li>
<li>Förpackning: Flaska, 100 ml</li>
<li>Innehåll: Beta-alanin, citrullinmalat, L-arginin, taurin och koffein</li>
<li>Ingredienser: Vatten, äppeljuicekoncentrat 17 %, beta-alanin, citronjuicekoncentrat 3 %, L-arginin-alfa-ketoglutarat (AAKG), taurin, L-citrullinmalat, vattenfritt koffein, inosin, smakämnen, sötningsmedel (acesulfam K, sukralos, neotam), maltodextrin, konserveringsmedel (kaliumsorbat, natriumbensoat)</li>
<li>Användning: 30 minuter före träning, skakas väl före användning</li>
<li>Förvaring: Flaskan`

### 33029 (10656694141194, k_33c_utkast.json): RÄTTA

Live: ACTIVE, 'Koffeinsot TREC Boogieman Shot 100ml, Tropical', EAN 5902114081430, 29 kr, lager 3. 'Koffeinsot' är en felstavning av 'Koffeinshot' (Velomarkets engelska titel: 'Caffeine shot TREC Boogieman Shot'). Utkastets 'Energishot' saknar stöd i produktens egen titel (R7) och för in ordet energi. Familjens typord Kosttillskott används i stället. Den äldre Tropical-annonsen 10472267940106 är ARCHIVED, så detta är ingen dubblett (v1.5). Typordet: live 'Energishot' ersätts med Kosttillskott, som för de skrivna Boogieman-syskonen 33002, 33003 och 33010 (k_skriv_32i33a, där Energishot och Koffeindrink byttes av samma skäl: 'energi' ligger nära ett energilöfte, och källan säger 'flytande kosttillskott', R7). Dos och mängder: live anger 15 ml per portion och beta-alanin 750 mg och citrullinmalat 300 mg utan att säga vad mängden gäller. Tillverkarens sida (https://trecnutrition.com/brands/trec/trec-core/boogieman-shot/) anger för samma receptur (inosin, AAKG, taurin, citrullinmalat, koffein) en portion på 50 ml (en halv flaska) med 2500 mg beta-alanin, 1000 mg citrullinmalat och 200 mg koffein. En äldre version med eget EAN (leki.pl, EAN 5902114017675) anger 15 ml, 750 mg och 60 mg koffein. Vilken som gäller just detta EAN går inte att avgöra, och en för låg dos med koffein får inte stå (R2). Därför stryks 15 ml och mg-värdena, som i 33010. Användningen '30 minuter före träning', 'skakas väl' och alla varningar står kvar. Förpackning: tillverkaren anger en flaska på 100 ml, så 'flaska' står kvar (R1 v1.6), men raden 'Förvaring: Burken stängd' (källans ord) rättas till 'Flaskan stängd', så att texten inte säger emot sig själv. Cirkulär inledning i meta och första meningen ('X är ett ... kosttillskott') rättas (skriptvarning, praxis k_30ab och k_32i33a). Taurin och koffein står i meta som ingredienser, utan effekt (skriptets 'halsa' på 'koffein' är ett känt falsklarm). Alla energi-, fokus-, uthållighets- och blodflödesfraser ur källan är borta, och L-tyrosin, som saknas i ingredienslistan, är rätt utelämnat.

- `titel` före: `Energishot Trec Boogieman Shot, Tropical, 100 ml`
  efter: `Kosttillskott Trec Boogieman Shot Tropical, 100 ml`

- `seo_title` före: `Energishot Trec Boogieman Tropical`
  efter: `Kosttillskott Trec Boogieman Tropical`

- `meta` före: `Trec Boogieman Shot Tropical är ett flytande kosttillskott med tropisk fruktsmak i flaska på 100 ml med beta-alanin och citrullinmalat. Portionen är 15 ml.`
  efter: `Trec Boogieman Shot Tropical har tropisk fruktsmak och innehåller beta-alanin, citrullinmalat, taurin och koffein. Flaskan rymmer 100 ml.`

- `html` före: `är ett färdigt att dricka flytande kosttillskott med tropisk fruktsmak i flaska på 100 ml. Huvudingredienserna är beta-alanin (750 mg) och citrullinmalat (300 mg). Portionen är 15 ml.</p><h2>Passar för</h2><ul>
<li>Dig som vill ha ett flytande kosttillskott i färdig shot</li>
<li>Dig som vill ha en portion om 15 ml att dricka 30 minuter före träning</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Flytande kosttillskott (shot)</li>
<li>Smak: Tropisk frukt (Tropical)</li>
<li>Förpackning: Flaska, 100 ml</li>
<li>Innehåll: Beta-alanin (750 mg), citrullinmalat (300 mg), L-arginin, taurin och koffein</li>
<li>Ingredienser: Vatten, äppeljuicekoncentrat 17 %, beta-alanin, citronjuicekoncentrat 3 %, L-arginin-alfa-ketoglutarat (AAKG), taurin, L-citrullinmalat, vattenfritt koffein, inosin, aromer, sötningsmedel (acesulfam K, sukralos, neotam), maltodextrin, konserveringsmedel (kaliumsorbat, natriumbensoat)</li>
<li>Rekommenderad daglig dos: 15 ml</li>
<li>Användning: 15 ml (1 portion) 30 minuter före träning, skakas väl före användning</li>
<li>Förvaring: Burken`
  efter: `har tropisk fruktsmak och levereras färdig att dricka i en flaska på 100 ml. Det flytande kosttillskottet har beta-alanin och citrullinmalat som huvudingredienser.</p><h2>Passar för</h2><ul>
<li>Dig som vill ha ett flytande kosttillskott i färdig shot</li>
<li>Dig som vill ha en färdig shot att dricka 30 minuter före träning</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Flytande kosttillskott (shot)</li>
<li>Smak: Tropisk frukt (Tropical)</li>
<li>Förpackning: Flaska, 100 ml</li>
<li>Innehåll: Beta-alanin, citrullinmalat, L-arginin, taurin och koffein</li>
<li>Ingredienser: Vatten, äppeljuicekoncentrat 17 %, beta-alanin, citronjuicekoncentrat 3 %, L-arginin-alfa-ketoglutarat (AAKG), taurin, L-citrullinmalat, vattenfritt koffein, inosin, aromer, sötningsmedel (acesulfam K, sukralos, neotam), maltodextrin, konserveringsmedel (kaliumsorbat, natriumbensoat)</li>
<li>Användning: 30 minuter före träning, skakas väl före användning</li>
<li>Förvaring: Flaskan`

### 33030 (10656694173962, k_33c_utkast.json): UNDERKÄND

Live: ACTIVE, 'Koffeinsot TREC Boogieman Shot 100ml, Bubble Gum', EAN 5902114081409, 29 kr, lager 4. UNDERKÄND som dubblett (R12a): samma modell och smak som den redan skrivna 33010 (10471287783690, 'Kosttillskott Trec Boogieman Shot Bubble Gum, 100 ml', EAN 5902114046781, ACTIVE, lager 18), med samma ingredienslista. Med familjens typord blir titeln och SEO-titeln identiska med 33010 (R12 kräver unikhet). Med utkastets 'Energishot' blir den bara unik genom ett effektnära typord, som inte står i produktens egen titel. I övrigt gäller samma fel som för 33027–33029 (15 ml och mg-värden som säger emot tillverkaren, 'Burken' mot 'flaska', cirkulär inledning). Observera att live-texten med energi-, trötthets- och blodflödespåståenden ligger kvar tills dubbletten hanteras. Rekommendation: ta med paret 33010/33030 i planen för dubbletter (Davids beslut 2026-11-05 'slå ihop').

### 33031 (10656694206730, k_33c_utkast.json): RÄTTA

Live: ACTIVE, 'Koffeinfritt energishot TREC Boogieman Shot Ice Tea Peach 100ml', EAN 5902114081393, 29 kr, lager 12. Procentsatserna (beta-alanin 5 %, AAKG 2 %, citrullinmalat 2 %, glukuronolakton 0,7 %, rosenrot 0,7 %, ginseng 0,1 %, B6 0,01 %), 15 ml per portion, 3 portioner och 45 ml per dag, 'före, under eller efter träning', förvaringen och varningen stämmer. Källan har inga koffeinvarningar, och de är rätt utelämnade. Koffein: ingredienslistan har varken koffein eller någon koffeinkälla. Butikens äldre utkastannons (10472297562378, DRAFT) heter 'Boogieman Shot Caffeine Free', och återförsäljare (store.mygp.com 'Caffeine Free BoogieMan Shot Trec Nutrition Peach Ice Tea 100ml', muscleshop.lt) säljer den som Caffeine Free. Utkastet är inte aktivt och räknas inte som dubblett. Rättning 1, titeln: 'Koffeinfritt Energishot' blir familjens typord Kosttillskott med tillverkarens variantnamn 'Caffeine Free' (70 tecken). Det ger ingen energi-antydan, och koffeinfriheten står som produktnamn i stället för som eget påstående. Rättning 2: 'Burken' blir 'Flaskan' (tillverkaren: flaska på 100 ml). Rättning 3: cirkulär meta och första mening. Rosenrot och ginseng står bara som ingredienser. Mygp anger 800 mg beta-alanin per 15 ml, medan källans 5 % ger 750 mg. Texten anger inga mg, så avvikelsen påverkar inte texten. Lägg till mygp-adressen i att_bekrafta.

- `titel` före: `Koffeinfritt Energishot Trec Boogieman Shot, Ice Tea Peach, 100 ml`
  efter: `Kosttillskott Trec Boogieman Shot Caffeine Free, Ice Tea Peach, 100 ml`

- `seo_title` före: `Energishot Trec Boogieman Ice Tea Peach`
  efter: `Kosttillskott Trec Boogieman Ice Tea Peach`

- `meta` före: `Trec Boogieman Shot Ice Tea Peach är ett flytande kosttillskott på 100 ml med beta-alanin, citrullinmalat och rosenrotsextrakt. Portionen är 15 ml.`
  efter: `Trec Boogieman Shot Ice Tea Peach innehåller beta-alanin, citrullinmalat och rosenrotsextrakt. Flaskan rymmer 100 ml, portionen är 15 ml.`

- `html` före: `är ett färdigt att dricka flytande kosttillskott i flaska på 100 ml. Ingredienslistan innehåller beta-alanin 5 %, L-citrullinmalat 2 % och rosenrotsextrakt 0,7 %. Portionen är 15 ml.</p><h2>Passar för</h2><ul>
<li>Dig som vill ha ett flytande kosttillskott i färdig shot</li>
<li>Dig som vill ha en portion om 15 ml att dricka före, under eller efter träning</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Flytande kosttillskott (shot)</li>
<li>Smak: Ice Tea Peach</li>
<li>Förpackning: Flaska, 100 ml</li>
<li>Innehåll: Beta-alanin, citrullinmalat, L-arginin, glukuronolakton, rosenrotsextrakt, kolin, koreanskt ginsengextrakt och vitamin B6</li>
<li>Ingredienser: Vatten, äppeljuicekoncentrat 17 %, beta-alanin 5 %, citronjuicekoncentrat 3 %, L-arginin-alfa-ketoglutarat (AAKG) 2 %, L-citrullinmalat 2 %, glukuronolakton 0,7 %, rosenrotsextrakt 0,7 % (1 % salidrosider, 1 % rosaviner), syra (citronsyra), kolinbitartrat, koreanskt ginsengextrakt (Panax ginseng) 0,1 % (1 % ginsenosider), aromer, färgämnen (ammoniumsulfitkaramell), sötningsmedel (acesulfam K, sukralos, neotam), konserveringsmedel (kaliumsorbat, natriumbensoat), vitamin B6 (pyridoxinhydroklorid) 0,01 %</li>
<li>Rekommenderad daglig dos: 45 ml</li>
<li>Användning: 15 ml (1 portion) 30 minuter före, under eller efter träning, 3 portioner per dag, skakas väl före användning</li>
<li>Förvaring: Burken`
  efter: `levereras färdig att dricka i en flaska på 100 ml. Ingredienslistan innehåller beta-alanin 5 %, L-citrullinmalat 2 % och rosenrotsextrakt 0,7 %. Portionen är 15 ml.</p><h2>Passar för</h2><ul>
<li>Dig som vill ha ett flytande kosttillskott i färdig shot</li>
<li>Dig som vill ha en portion om 15 ml att dricka före, under eller efter träning</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Flytande kosttillskott (shot)</li>
<li>Smak: Ice Tea Peach</li>
<li>Förpackning: Flaska, 100 ml</li>
<li>Innehåll: Beta-alanin, citrullinmalat, L-arginin, glukuronolakton, rosenrotsextrakt, kolin, koreanskt ginsengextrakt och vitamin B6</li>
<li>Ingredienser: Vatten, äppeljuicekoncentrat 17 %, beta-alanin 5 %, citronjuicekoncentrat 3 %, L-arginin-alfa-ketoglutarat (AAKG) 2 %, L-citrullinmalat 2 %, glukuronolakton 0,7 %, rosenrotsextrakt 0,7 % (1 % salidrosider, 1 % rosaviner), syra (citronsyra), kolinbitartrat, koreanskt ginsengextrakt (Panax ginseng) 0,1 % (1 % ginsenosider), aromer, färgämnen (ammoniumsulfitkaramell), sötningsmedel (acesulfam K, sukralos, neotam), konserveringsmedel (kaliumsorbat, natriumbensoat), vitamin B6 (pyridoxinhydroklorid) 0,01 %</li>
<li>Rekommenderad daglig dos: 45 ml</li>
<li>Användning: 15 ml (1 portion) 30 minuter före, under eller efter träning, 3 portioner per dag, skakas väl före användning</li>
<li>Förvaring: Flaskan`
