# Oberoende granskning av kategoritexter, våg 2 (2026-11-17)

Granskare: Opus (oberoende, endast läsning). Inga Shopify-anrop och inga nätverksanrop har gjorts.

**Underlag:** `vag2_texter.py` (texterna), `vag2dir/underlag/<handle>.json` (faktaunderlag), `vag2/rå_<handle>.json` (rådata), `shopify-sync/docs/kategoritexter-standard.md` (avsnitt 2, 3, 4 och 8) och de sista posterna i `LARDOMAR.md`.

**Metod:** Varje påstående har kontrollerats mot `alla_titlar` (huvudprodukter), `ovriga_titlar` och `marken`. Antal, märken, typer, egenskaper och exempeltitlar har räknats med `python3 -I` direkt i JSON-filerna, inte med kontrollskriptet. Ordantal räknas på styckena utan den separata "Se även"-meningen.

**Skillnad mellan felklasserna:**
- **FAKTAFEL** = ett påstående som inte stämmer med underlaget, eller en uppräkning som framställs som fullständig fast den inte är det (standarden 8.4 och lärdomen från 2026-11-12). Ska rättas före skrivning.
- **ANMÄRKNING** = stil, numerus, risk eller vilseledande sammanhang där påståendet ändå är sant. Valfritt att åtgärda.

## Översikt

| Kategori | Huvudprodukter (underlag) | "minst N" | Golv enligt standard | Marginal | Ord | SEO-titel (tecken) | Meta (tecken) | Utfall |
|---|---|---|---|---|---|---|---|---|
| traningsmaskin | 8 | 5 | 5 | 3 | 62 | 32 | 144 | Godkänd (anmärkningar) |
| herrcyklar | 11 (10 unika titlar) | 10 | 10 | 1 (0 på unika titlar) | 63 | 31 | 120 | Godkänd (anmärkningar) |
| hybridcykel | 27 | 25 | 25 | 2 | 78 | 29 | 127 | Godkänd (anmärkningar) |
| traningsbank | 19 | 15 | 15 | 4 | 69 | 43 | 133 | **Fel** (1 faktafel) |
| grepptraning | 11 | 10 | 10 | 1 | 68 | 42 | 134 | **Fel** (2 faktafel) |
| boxning | 30 | 30 | 30 | **0** | 71 | 37 | 150 | **Fel** (1 faktafel) |
| racercykel | 24 | 20 | 20 | 4 | 73 | 39 | 127 | Godkänd (anmärkningar) |
| stankskarmar-cykel | 47 | 40 | 40 | 7 | 74 | 36 | 142 | **Fel** (1 faktafel) |
| traningsutrustning-for-hemmagym | 714 (709 unika titlar) | 700 | 700 | 14 (9 på unika titlar) | 61 | 31 | 139 | Godkänd (anmärkningar) |

Allmänt för alla nio texter: varje första mening har verb ("säljer"), alla metabeskrivningar börjar med "Köp", ingen text innehåller prisuppgifter (meningen "Öppna en produkt för att se pris …" anger inget pris), och ingen innehåller "modeller", superlativ, kvalitets-, säkerhets-, hälso- eller effektlöften, leveranstid, frakt eller ursprung. Alla texter håller 60–200 ord, alla SEO-titlar högst 43 tecken och alla metabeskrivningar 120–155 tecken. Alla 27 exempeltitlar finns ordagrant i `alla_titlar`. Leverantörerna "Gorilla Sports Norden" och "Velomarket" nämns inte som märken.

---

## 1. traningsmaskin: godkänd

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 5 produkter" | 8 huvudprodukter (huvud_regex tomt, alla köpbara räknas); femtalsgolv ger 5 | Godkänd |
| "från bland annat Tunturi, Hammer och Finnlo by Hammer" | marken: Tunturi 3, Hammer 2, Finnlo by Hammer 1 (plus leverantören Gorilla Sports Norden 2) | Godkänd |
| "träningsmaskiner och hemmagym" | Träningsmaskin 2 titlar, Hemmagym 2 titlar | Godkänd |
| "latsdragsstationer, träningsstationer och sissy squat-bänkar" | Latsdragsstation 1, Träningsstation 1, Sissy Squat 2 | Godkänd (se anmärkning) |
| Exempel: 3 titlar | Alla 3 finns ordagrant | Godkänd |
| SEO "Träningsmaskin – Tunturi, Hammer" (32) | Typord först, två vanligaste märkena | Godkänd |
| Meta (144) | Märken med "bland annat", antal 5 | Godkänd |

**Anmärkningar**
- A1. "latsdragsstationer" och "träningsstationer" står i plural men varje typ har bara 1 produkt. Det går att läsa som typnamn och är inte fel, men ett förslag: "… hemmagym, en latsdragsstation, en träningsstation och sissy squat-bänkar".
- A2. I metan räknas "träningsmaskin, hemmagym eller latsdragsstation" upp utan sissy squat och träningsstation. Formen "Köp X, Y eller Z" är en uppmaning och inte en innehållsförteckning, så det räknas inte som fel.

## 2. herrcyklar: godkänd

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 10 produkter" | 11 huvudprodukter, femtalsgolv ger 10. Titeln "Herrcykel ROMET Orkan M, grå-röd" förekommer två gånger, så det finns 10 unika titlar | Godkänd, marginal 1 (0 räknat på unika titlar) |
| "herrcyklar och stadscyklar" | herrcykel 8, stadscykel 3 | Godkänd |
| "från bland annat Romet, Giant och Tabou" | Romet 7, Giant 3, Tabou 1 | Godkänd |
| "Romet har flest produkter" | 7 mot 3 och 1 | Godkänd |
| "Några produkter anger 27 växlar eller 28 tum" | "27 Växlar": 1 (Wagant 8). "28 tum": 2 (Romet Orkan M, Tabou Kinetic 1.0) | Godkänd |
| Exempel: 3 titlar | Alla 3 finns ordagrant | Godkänd |
| SEO (31), meta (120) | Meta har "bland annat" före märkena | Godkänd |

**Anmärkningar**
- A3. Marginalen är 0 räknat på unika titlar. Om en Romet- eller Giant-produkt säljs slut före skrivning blir "minst 10" fel. Kör om underlaget direkt före skrivning (standarden 8.1).
- A4. Den taggstyrda kollektionen innehåller också 3 köpbara produkter som inte är cyklar: "Boxningsdocka Tunturi Slam Man", "Multivitamin för Män Trec, 90 kapslar" och "Kosttillskott Trec Essensey Multivit For Him + Maca Root, 90 kapslar". Texten påstår inget om dem, men sidan visar dem under en text om herrcyklar. Detta är en fråga om kollektionens taggar, inte om texten. Kosttillskott ligger dessutom under `utanfor_tills_vidare`.

## 3. hybridcykel: godkänd

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 25 produkter" | 27, femtalsgolv ger 25 | Godkänd, marginal 2 |
| "från Romet och Giant" | Romet 16, Giant 11. Inga andra märken bland huvudprodukterna | Godkänd (fullständig lista) |
| "Romet har flest produkter" | 16 mot 11 | Godkänd |
| "till exempel 11, 18 eller 21 växlar" | 11 Växlar: 2, 18 Växlar: 3, 21 Växlar: 7 (24 Växlar: 3 finns också, men "till exempel" täcker det) | Godkänd |
| "även andra produkter, bland annat barnstolar, cykelväskor och sparkcyklar" | ovriga_titlar: barnstolar (9 titlar som börjar med Barnstol/Barnsits), cykelväskor (3 "Cykelväska Basil" och 1 Pakväska), sparkcyklar (11 "Sparkcykel") | Godkänd |
| Exempel: 3 titlar | Alla 3 finns ordagrant | Godkänd |
| SEO (29), meta (127) | | Godkänd |

**Anmärkningar**
- A5. Bland övriga produkter finns andra cyklar som en kund kan uppfatta som hybrid- eller stadscyklar: "Damcykel Liv Flourish 3, 700x38c …", "LIV Flourish 3 Disc Women's Bike, Muscat Blanc", "Cykel EXCELSIOR Swan Urban, Aubergine" och elcyklar från Giant, Tenways och Victoria. "från Romet och Giant" stämmer enligt underlagets definition, men "från bland annat Romet och Giant" vore säkrare.
- A6. Meta: "Här finns minst 25 produkter, bland annat med 11, 18 eller 21 växlar" läses lite tungt. Förslag: "Köp hybridcykel från Giant och Romet, till exempel med 11, 18 eller 21 växlar. Här finns minst 25 produkter hos BEST OF SPORTS." (127 tecken)

## 4. traningsbank: FEL (1 faktafel)

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 15 produkter" | 19, femtalsgolv ger 15 | Godkänd, marginal 4 |
| "från bland annat Tunturi, Christopeit, Finnlo by Hammer, BH Fitness och Hammer" | Tunturi 12, Christopeit 2, Finnlo by Hammer 2, BH Fitness 1, Hammer 1 (Tunturi räknat i titlarna: 12) | Godkänd |
| "Tunturi har flest produkter" | 12 mot högst 2 | Godkänd |
| "hopfällbara eller justerbara enligt produktnamnet" | Hopfällbar: 2 (CT40, UB20). Justerbar: 3 (AB20, MX Select, UB80). Totalt 5 | Godkänd |
| "det finns bland annat magbänkar" | 1 titel: "Träningsbänk Tunturi AB20 Magbänk, Justerbar" | Godkänd (se anmärkning) |
| Exempel: 3 titlar | Alla 3 finns ordagrant | Godkänd |
| SEO "Träningsbänk – Tunturi, Christopeit, Hammer" | 43 tecken, exakt på gränsen | Godkänd (se anmärkning) |
| **Meta: "från Tunturi, Christopeit, Finnlo by Hammer och Hammer"** | marken innehåller också **BH Fitness (1)**: "Träningsbänk BH Fitness Optima". Märkeslistan saknar "bland annat" ("bland annat" i metan gäller "hopfällbar eller justerbar") och framställs därför som fullständig | **FAKTAFEL** |

**FAKTAFEL F1 (meta)**
- Före: `Köp träningsbänk, bland annat hopfällbar eller justerbar, från Tunturi, Christopeit, Finnlo by Hammer och Hammer. Minst 15 produkter.`
- Efter: `Köp träningsbänk från bland annat Tunturi, Christopeit, Finnlo by Hammer och Hammer, till exempel hopfällbar eller justerbar. Minst 15 produkter.` (145 tecken)
- Belägg: `traningsbank.json` → `marken` innehåller `["BH Fitness", 1]`, och `alla_titlar` innehåller "Träningsbänk BH Fitness Optima".

**Anmärkningar**
- A7. "magbänkar" står i plural men bara 1 titel innehåller "Magbänk". Förslag: "… och det finns bland annat en magbänk."
- A8. SEO-titeln har 43 tecken (0 i marginal). "Hammer" har 1 produkt, medan Finnlo by Hammer har 2. Standarden säger "de tre vanligaste märkena". Christopeit och Finnlo by Hammer har 2 vardera, så "Hammer" som tredje märke är inte det vanligaste. Det är inte fel eftersom titeln inte påstår någon rangordning.
- A9. Exempeltiteln "Träningsbänk Tunturi Centuri UB100 Utility Bench" används också i traningsutrustning-for-hemmagym. Byt i någon av texterna för att undvika dubblerat innehåll.

## 5. grepptraning: FEL (2 faktafel)

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 10 produkter" | 11, femtalsgolv ger 10 | Godkänd, marginal 1 |
| "från bland annat Gymstick" | Gymstick 9 (plus leverantören Gorilla Sports Norden 2) | Godkänd |
| **Text, mening 1: "greppträning från bland annat Gymstick: fingerexpandrar, handtränare, greppstärkare och greppringar"** | Typerna finns (Fingerexpander 2, Handtränare 2, Greppstärkare 2, Greppringar 1). Listan efter kolonet saknar "bland annat". Mening 2 lägger till viktset och justerbart handtag, men **"Extra Grepp Barbell Grips, Svarta"** nämns inte, så hela uppräkningen framställs som fullständig fast den inte är det | **FAKTAFEL** |
| "justerbart motstånd eller justerbar inställning i produktnamnet" | "Justerbart Motstånd": 1. "Justerbar": 1 (Handtränare). "Justerbart handtag": 1. Ingen titel innehåller ordet "inställning" | Godkänd i sak (se anmärkning) |
| "även ett viktset och ett justerbart handtag" | "Viktset Gymstick Vinyl Grip Pump Set, 20 kg" 1, "Justerbart handtag, lätt" 1 | Godkänd |
| Exempel: 3 titlar | Alla 3 finns ordagrant | Godkänd |
| SEO "Greppträning – Handtränare, fingerexpander" (42) | | Godkänd (se anmärkning) |
| **Meta: "från bland annat Gymstick: handtränare, fingerexpandrar, greppstärkare och greppringar"** | Typlistan saknar "bland annat" och framställs som fullständig. Viktset, justerbart handtag och Extra Grepp Barbell Grips saknas | **FAKTAFEL** |

**FAKTAFEL F2 (text, mening 1)**
- Före: `BEST OF SPORTS säljer greppträning från bland annat Gymstick: fingerexpandrar, handtränare, greppstärkare och greppringar.`
- Efter: `BEST OF SPORTS säljer greppträning från bland annat Gymstick, till exempel fingerexpandrar, handtränare, greppstärkare och greppringar.` (texten får då 70 ord)
- Belägg: `grepptraning.json` → `alla_titlar` innehåller "Extra Grepp Barbell Grips, Svarta", "Viktset Gymstick Vinyl Grip Pump Set, 20 kg" och "Justerbart handtag, lätt". Ingen av dem finns i listan efter kolonet.

**FAKTAFEL F3 (meta)**
- Före: `Köp greppträning från bland annat Gymstick: handtränare, fingerexpandrar, greppstärkare och greppringar. Här finns minst 10 produkter.`
- Efter: `Köp greppträning från bland annat Gymstick, till exempel handtränare, fingerexpandrar, greppstärkare och greppringar. Här finns minst 10 produkter.` (147 tecken)
- Belägg: samma som F2. Metan saknar dessutom "även"-meningen som i brödtexten visar att det finns fler typer.

**Anmärkningar**
- A10. "justerbar inställning i produktnamnet": inget produktnamn innehåller "inställning". Förslag: "Några produkter anger i produktnamnet att de är justerbara, till exempel justerbart motstånd, …"
- A11. SEO-titeln har inkonsekvent versalisering ("Handtränare" med stor bokstav, "fingerexpander" med liten). Förslag: "Greppträning – handtränare, fingerexpander".
- A12. Ett viktset på 20 kg i greppträning är en fråga om kollektionens taggar. Texten redovisar det öppet.

## 6. boxning: FEL (1 faktafel)

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 30 produkter" | 30 (huvud_regex tomt), tiotalsgolv ger 30 | Godkänd, **marginal 0** |
| "bland annat boxningshandskar, boxningssäckar och boxningsdockor" | Boxningshandskar 11 (plus 2 "Boxing gloves HAMMER"), Boxningssäck 5, Boxningsdocka 2 | Godkänd |
| "från bland annat Tunturi, Toorx, Hammer och Gymstick" | Tunturi 14, Toorx 7, Hammer 3, MAXXUS 2, Gymstick 2, Zipro 1 | Godkänd |
| "Tunturi har flest produkter" | 14 mot 7 | Godkänd |
| "10, 12, 14 och 16 oz" | 10 oz: 3, 12 oz: 4, 14 oz: 2, 16 oz: 1 | Godkänd |
| Exempel: 3 titlar | Alla 3 finns ordagrant | Godkänd |
| SEO (37) | | Godkänd |
| **Meta: "från Tunturi, Toorx, Hammer och Gymstick"** | Märkeslistan saknar "bland annat" ("bland annat" gäller typerna). marken innehåller också **MAXXUS (2)** och **Zipro (1)** | **FAKTAFEL** |

**FAKTAFEL F4 (meta)**
- Före: `Köp boxningsutrustning, bland annat boxningshandskar, boxningssäckar och boxningsdockor, från Tunturi, Toorx, Hammer och Gymstick. Minst 30 produkter.`
- Efter: `Köp boxningsutrustning, till exempel handskar, säckar och dockor, från bland annat Tunturi, Toorx, Hammer och Gymstick. Minst 30 produkter.` (139 tecken; om man bara lägger till "bland annat" blir metan 163 tecken, över gränsen)
- Belägg: `boxning.json` → `marken` innehåller `["MAXXUS", 2]` och `["Zipro", 1]`. I `alla_titlar` finns "Boxningssäck MAXXUS Vatten & Luft 100cm/26kg", "Boxningssäck Maxxus, Vatten och Luft, 150 cm" och "Gymnastikgummiband/boxningssäcksfäste ZIPRO Hållare".

**Anmärkningar**
- A13. Marginalen är 0. Om en enda produkt säljs slut eller avpubliceras före skrivning blir "minst 30" fel, och golvet blir då 25. Kör om underlaget direkt före skrivning.

## 7. racercykel: godkänd

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 20 produkter" | 24, femtalsgolv ger 20 | Godkänd, marginal 4 |
| "landsvägscyklar och racercyklar från Giant" | Landsvägscykel 23, Racercykel 1, Giant 24 | Godkänd |
| "kolfiber eller carbon i produktnamnet" | kolfiber: 1, Carbon: 5, totalt 6 | Godkänd (se anmärkning) |
| "serier som TCR, Defy, Contend och Propel" | TCR 10, Defy 5, Contend 5, Propel 4 | Godkänd |
| "även tillbehör som pedaler och pedalblock" | ovriga_titlar: Pedaler 3 (Giant), Pedalblock 2 och Pedalplattor 1 (Look) | Godkänd |
| Exempel: 3 titlar | Alla 3 finns ordagrant | Godkänd |
| SEO (39), meta (127) | | Godkänd |

**Anmärkningar**
- A14. Kan vilseleda: kategorin innehåller också produkter som inte är tillbehör till racercyklar, till exempel motions- och spinningcyklar (Hammer Speed Race, 4 titlar), trick- och stuntsparkcyklar (Union Aero, 6 titlar), pjäxor (Alpina), en stepbräda (Tunturi Aero Step) och en hjälm för barn. Texten nämner bara "tillbehör som pedaler och pedalblock". Förslag: "Kategorin innehåller även andra produkter, bland annat pedaler, pedalblock och spinningcyklar." Rensa helst taggarna (beslut om struktur).
- A15. "Carbon" står i fyra av fem titlar på färgens plats ("700c, Carbon") och kan vara ett färgnamn. Texten säger bara att produktnamnet anger det, vilket stämmer.
- A16. Underlaget: "Cykel Giant TCR Advanced 2 Disc-PC Hematite" ligger bland övriga, trots att huvud_regex innehåller `^cykel giant tcr`. Om den räknas blir antalet 25 och golvet 25. "minst 20" är fortfarande sant. Kontrollera regeln i `kategorier_underlag.py`. Bland övriga finns också "Damcykel Liv Avail AR 2, 700x32c" (en landsvägscykel för damer från Liv).

## 8. stankskarmar-cykel: FEL (1 faktafel)

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 40 produkter" | 47, tiotalsgolv ger 40 | Godkänd, marginal 7 |
| "bland annat stänkskärmset, framskärmar och bakskärmar" | Stänkskärmset 14, Framskärm 12, Bakskärm 10 | Godkänd |
| "från bland annat Hebie, SKS, Giant och Ass Savers" | Hebie 17, SKS 14, Giant 8, Ass Savers 3, Academy 1, XLC 1 (Velomarket 3 är leverantör) | Godkänd |
| "Hebie och SKS har flest produkter" | Vendor: Hebie 17, SKS 14. Räknat i titlarna: Hebie 17, SKS 17 (3 SKS-produkter har leverantören Velomarket) | Godkänd |
| "28 tum eller 26–29 tum" | 28 tum: 2, 26–29 tum: 6 | Godkänd |
| Exempel: 3 titlar | Alla 3 finns ordagrant | Godkänd |
| SEO (36) | | Godkänd |
| **Meta: "från Hebie, SKS, Giant och Ass Savers"** | Märkeslistan saknar "bland annat". marken innehåller också **Academy (1)** och **XLC (1)** | **FAKTAFEL** |

**FAKTAFEL F5 (meta)**
- Före: `Köp stänkskärmar till cykel, bland annat stänkskärmset, framskärmar och bakskärmar, från Hebie, SKS, Giant och Ass Savers. Minst 40 produkter.`
- Efter: `Köp cykelstänkskärmar, till exempel stänkskärmset, framskärmar och bakskärmar, från bland annat Hebie, SKS, Giant och Ass Savers. Minst 40 produkter.` (149 tecken)
- Belägg: `stankskarmar-cykel.json` → `marken` innehåller `["Academy", 1]` och `["XLC", 1]`. I `alla_titlar` finns "Framskärm XLC MG-C05 för Hjul 26–29 tum" och "Stänkskärmsset för ACADEMY 24" hjul".

**Anmärkningar**
- A17. Om "flest" räknas på vendor har Hebie ensamt flest (17 mot 14). Om det räknas på titlarna delar Hebie och SKS förstaplatsen (17 vardera). Formuleringen stämmer med båda räknesätten.

## 9. traningsutrustning-for-hemmagym: godkänd

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 700 produkter" | 714, hundratalsgolv ger 700. 709 unika titlar (4 titlar förekommer dubbelt) | Godkänd, marginal 14 (9 på unika titlar) |
| "från bland annat Tunturi, Toorx, Hammer, BH Fitness och Christopeit" | De fem största i marken: 295, 141, 80, 55, 54 | Godkänd |
| "motionscyklar, löpband, roddmaskiner, träningsbänkar, kettlebells och viktskivor" | Titlar som börjar med typordet: motionscykel 58, löpband 42, roddmaskin 21, träningsbänk 30, kettlebell 27, viktskivor 44 | Godkänd |
| Exempel: 3 titlar | Alla 3 finns ordagrant | Godkänd |
| SEO (31), meta (139) | Typerna står efter "bland annat" | Godkänd |

**Anmärkningar**
- A18. Texten har 61 ord, nära den nedre gränsen på 60. Om någon mening tas bort hamnar texten under gränsen.
- A19. Exempeltiteln "Träningsbänk Tunturi Centuri UB100 Utility Bench" är densamma som i traningsbank (se A9).
- A20. Vendor Trec (14) är här träningshandskar, flaskor och krita, inte kosttillskott. Det är inget problem.

---

## Sammanställning av faktafel

| Nr | Kategori | Fält | Fel | Belägg i underlaget |
|---|---|---|---|---|
| F1 | traningsbank | meta | Märkeslistan framställs som fullständig men saknar BH Fitness | marken: BH Fitness 1; "Träningsbänk BH Fitness Optima" |
| F2 | grepptraning | text, mening 1 | Typlistan framställs som fullständig; Extra Grepp Barbell Grips (samt viktset och handtag i mening 1) saknas | alla_titlar |
| F3 | grepptraning | meta | Typlistan framställs som fullständig; viktset, handtag och barbell grips saknas | alla_titlar |
| F4 | boxning | meta | Märkeslistan framställs som fullständig men saknar MAXXUS och Zipro | marken: MAXXUS 2, Zipro 1 |
| F5 | stankskarmar-cykel | meta | Märkeslistan framställs som fullständig men saknar Academy och XLC | marken: Academy 1, XLC 1 |

Felen F1, F3, F4 och F5 är samma typ som i lärdomen 2026-11-12 ("metatexter räknade upp märken eller typer som om listan var fullständig"). Kontrollskriptet fångar inte denna typ av fel. Föreslå att `kategori_kontroll.py` kräver "bland annat" eller "till exempel" före varje märkeslista i metan som inte innehåller alla märken i `marken` utom leverantörerna.

Inga antal är fel, alla märkesuppgifter om flest produkter stämmer, alla nämnda typer och egenskaper finns i titlarna, och alla exempeltitlar finns ordagrant. Risker inför skrivning: boxning har marginal 0, och herrcyklar har marginal 0 räknat på unika titlar. Underlaget ska köras om direkt före skrivning.

Antal faktafel: 5
