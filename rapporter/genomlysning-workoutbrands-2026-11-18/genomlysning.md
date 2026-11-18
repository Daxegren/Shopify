# Genomlysning av Workout Brands (workoutbrands.com), 2026-11-18

Läsande genomlysning enligt `shopify-sync/docs/genomlysning-ny-butik.md`, steg 0–7. Körd natten 2026-11-17 till 2026-11-18. Inget skrevs i Shopify eller i något annat konto. Siffror i `data/`. **Fakta** = läst direkt ur Shopify, ShopifyQL eller publik sida. **Bedömning** = min tolkning, som David kan ändra.

## Steg 0. Butiken bekräftad
**Fakta.** `get-shop-info` (före varje större läsning): namn och domän `workoutbrands.com`, valuta SEK, plan Shopify (Grow enligt `shop.plan`), myshopify-adress `doyou-se.myshopify.com`. Inte BEST OF SPORTS. `switch-shop` användes aldrig.
- Skatt: butiksinställningen `taxesIncluded = false`, men de fem senaste svenska ordrarna har `taxesIncluded = true` med "SE Moms" 25 % (order #3460: pris 199,00 kr, varav moms 39,80 kr). Danska order #3461 har `taxesIncluded = false`: momsen läggs på priset (667,17 kr + 150,08 kr). Storefrontens pris (`/products/<handle>.js`) är lika med adminpriset (M65 Giant Jacket 799,00 kr).
- Marknader: 33 (30 aktiva, tre utkast: Irland, Serbien, USA). 24 presentationsvalutor aktiverade. 20 publicerade språk, svenska primärt. Fraktländer: 29.
- **Bedömning.** Svenska priser är konsumentpriser inklusive 25 % moms. Marginal efter moms för Sverige beräknas därför som `(pris/1,25 − inköp)/(pris/1,25)`. För marknader där moms läggs på (till exempel Danmark) ser marginalen annorlunda ut; det är inte räknat här.

## Steg 1. Aktivitet
**Fakta (ShopifyQL, SEK).** Butiken har omsättning, till skillnad från BEST OF SPORTS.
- 12 månader (2025-11 till 2026-11-17): 1 244 ordrar, brutto 428 206 kr. Månader: toppar december 2025 (202 ordrar, 77 913 kr) och januari 2026 (171, 72 881); lägst april 2026 (46, 15 772); augusti 2026 153 ordrar. Oktober 2026: 100 ordrar, 38 736 kr. November hittills: 29 ordrar, 12 996 kr. (`data/forsaljning_manad.csv`)
- Fakturaland (12 mån): Sverige 907 ordrar och 293 057 kr, Danmark 284 och 105 226 kr; övriga länder under 15 ordrar var.
- Märken (brutto 12 mån): Brandit 160 330 kr (628 ordrar), UC Men 106 136 kr, UC Ladies 67 850 kr. Tillsammans cirka 82 % av märkesraderna. Under Armour 6 784 kr brutto men 890 kr netto.
- Toppprodukt 90 dagar: B Jerseyshirt Stripe Longsleeve, 108 ordrar och 18 671 kr brutto (av 61 353 kr för topp 20).
- Sessioner 90 dagar: 251 563. USA 120 967 (konvertering 0 %), Brasilien 17 955 (0 %), Sverige 17 316 (1,32 %). Desktop 225 448 sessioner, konvertering 0,009 % och 92 % avvisning; mobil 24 731, konvertering 0,85 %. Källa "direct" 220 533 sessioner med konvertering 0,035 %; sökning 22 274 (0,54 %); betald 4.
- **Bedömning.** Större delen av trafiken är sannolikt inte mänsklig (bottrafik, direkt, desktop, USA, Brasilien, Kina). Besöksstatistik och konverteringsgrad i Shopify är därför missvisande tills det är avgränsat. Verklig kundtrafik är i huvudsak Sverige på mobil. Prioritering bör ske efter omsättning per märke och efter Search Console när den finns.

## Steg 2. Katalog och kollektioner
**Fakta.**
- Produkter totalt 15 648: aktiva 7 371, utkast 8 149, arkiverade 125. Av de aktiva skapades 74 före 2025, 6 578 under 2025 och 719 under 2026. Hela de aktiva 7 371 lästes (74 + 7 297, exakt som `productsCount`). Utkasten lästes inte rad för rad.
- Leverantörsfältet (`vendor`): 54 värden. Största: UC Ladies 1 207, MT Men 931, UC Men 905, Urban Classics Accessoires 485, Brandit 385, MT Upscale 366, Flexfit 286, Miss Tee 275, Merchcode 231. Fältet blandar märkeslinje och status: "Out of stock", "outlet", "workoutbrands.com". Produkttyp: 101 värden, 80 aktiva saknar typ. Största: T-shirt 2 223, Hoodie 917, Jacka 497, Keps 413.
- Taggar: 447 olika bland aktiva. Importmarkör "in sheet" 5 315, "urban classics" 6 965, kampanj/prisjobb `BF26` 2 897 och `price-change-job-active` 2 897 (samma produkter; butiken totalt 3 925 inklusive utkast), "outlet" 89, "Sale" 29. 17 taggar finns i flera skiftlägen.
- SEO: SEO-titel saknas på 6 988 av 7 371 aktiva (temat faller tillbaka på produkttiteln; 338 har suffixet " | Workout Brands"). SEO-metabeskrivning saknas på 3 059; 352 är över 155 tecken, 28 under 70; median 125 tecken.
- Dubbletitlar bland aktiva: 171 grupper (366 produkter). 97 titlar slutar på en storlek (86 enligt striktare test).
- Lager: 2 081 aktiva produkter (28 %) har noll i lager. 3 saknar bild.
- Kollektioner: 673 (492 smarta, 181 manuella). 42 tomma, 54 med 1–4 produkter, median 38. 3 opublicerade, 4 publicerade i en enda kanal. SEO-titel saknas på 550, SEO-meta på 341, beskrivning på 83. 39 handles med -N-suffix (till exempel `klanning-dam-2`, `urban-classics-1`). 15 dubblettitlar. Fyra kollektioner heter "test" och fyra "radera" (en med 3 produkter, `gymvaska`); "Tröjor: Dam & Herr (kopia)" har 402 produkter. Flera kollektioner innehåller i praktiken hela katalogen (till exempel `workout-brands-black-friday-2025`, `plus-size-klader-herr-dam` med 14 950 produkter inklusive utkast). (`data/kollektioner_problem.csv`, 146 rader)
- Omdirigeringar: 6 630 (`urlRedirectsCount` var läsbart, till skillnad från vad som gällde för BEST OF SPORTS).
- Sitemap (svenska): 6 921 produkter, 670 kollektioner. **466 aktiva produkter finns inte i sitemapen** (373 av dem har lager). Alla 42 tomma kollektioner finns i sitemapen.
- **Bedömning.** Katalogen är en importerad leverantörskatalog (Urban Classics-gruppen, Brandit m.fl.) med tydliga import-spår. De 466 saknade i sitemapen tyder på att produkterna inte är publicerade i försäljningskanalen Online Store; det är inte verifierat. De tomma, "test"- och "radera"-kollektionerna är städning, men inga strukturella liveändringar bör göras före 2026-12-01 om Black Week-stoppet som gäller BEST OF SPORTS också ska gälla här (David avgör).

## Steg 3. Priser och marginal
Urval: alla 7 371 aktiva produkter, de första fem varianterna per produkt (33 008 varianter; median 9 varianter per produkt, så lägre eller högre storlekar kan saknas). Inköpspris (`unitCost`) saknas på 101 varianter (22 produkter).
**Fakta.**
- Marginal efter moms, alla 32 906 varianter med inköpspris: median 60,7 %, kvartiler 56,9 % och 94,6 %.
- **27 % av varianterna (cirka 8 900) har marginal över 90 %.** Bland dem hela märken: Build your Brand 100 %, MJ Gonzales 100 %. Exempel: Camo Jacquard Backpack, pris 463 kr, inköpspris 16,90 kr; UC Sorona Regular Tee, pris 199 kr, inköpspris 6,50 kr. 1 927 produkter (första varianten) har antingen marginal över 90 % eller pris under inköpspris. Övriga 73 % ligger tätt kring 60,6 % (kvartiler 56,7 % och 60,7 %), vilket ser ut som en prisformel.
- Under inköpspris efter moms: 141 varianter (`data/under_inkop.csv`). Under 20 % marginal: 159. Mellan 30 och 50 %: 417.
- Jämförpris: 14 619 varianter har jämförpris över priset (rabatt, median 9,9 %). 14 108 av dem hör till de 2 897 produkter som har taggen `price-change-job-active`; alla varianter på dessa produkter har jämförpris över pris (rabatt 9,3–10,5 %). 13 008 varianter utan prisjobb har jämförpris exakt lika med priset (meningslöst jämförpris). 5 varianter har jämförpris under priset.
- Prisjobbet: ingen av butikens produktmetafält anger prisjobb eller prisapp (metafält: Shopify-standard, `mm-google-shopping.custom_product`, `custom.fit3` på 2 846). Taggen `price-change-job-active` finns på 2 897 aktiva produkter och är tillsammans med `BF26` ett tecken på ett kampanjjobb inför Black Friday 2026 (10 % rabatt via jämförpris). Vilken app som styr jobbet går inte att se utan åtkomst till apparna.
- **Bedömning.** Den höga marginalen på 27 % av varianterna är sannolikt fel enhet eller fel valuta i inköpspriset (till exempel inköpspris i euro per styck på produkter vars priser tydligt följer en annan formel), inte verklig vinst. Marginalsiffran 60,7 % gäller bara de 73 % som verkar ha inköpspris i kronor. Inga prisförslag bör tas fram för butiken innan inköpspriserna är kontrollerade. Detta är samma sorts fel som i BEST OF SPORTS-lärdomen om fel produkts inköpspris. `pris_forslag.py` användes inte: skriptet utgår från BEST OF SPORTS (40 % marginal, 25 % moms på alla priser, hållen vid ±25 %) och skulle här ge 1 927 felaktiga förslag.
- Jämförpris ska vara det lägsta priset de senaste 30 dagarna (EU:s prisinformationsregler; allmän kunskap, inte juridisk rådgivning). Att alla 14 108 varianter har exakt 10 % rabatt tyder på att jämförpriset är det gamla priset. Om priset sänktes nyligen och jämförpriset inte var det lägsta de senaste 30 dagarna är det ett risk. Kontrollera innan Black Friday.

## Steg 4. Textkvalitet
Täckning: alla 7 371 aktiva produkter har körts genom automatiska kontroller (heuristiker, inte läsning av varje text). Dessutom ett slumpurval om 300 produkter (`data/textprov_300.csv`) där jag läst 12 exempel manuellt. Alla produkter har någon text.
**Fakta (automatiskt).**
- Tomma beskrivningar 16, under 30 ord 8. Median 91 ord (kvartiler 75 och 111).
- 5 952 av 7 371 (81 %) inleds med produktnamnet i klartext (det engelska namnet läggs rakt framför första meningen, utan skiljetecken: "Coloured Buckle Canvas Belt En stilren och funktionell canvasbälte …").
- Språkblandning: 61 mestadels engelska, 39 blandade svenska/engelska. "Vanliga frågor" finns inte i någon (0). "Om märket"-text 2. Ampersand i HTML 22; obalanserad HTML 2.
- 322 inledningar ser cirkulära ut ("X är en X", heuristik, ej verifierat). 56 grupper (128 produkter) har identisk inledning. 623 texter nämner leverantörens eller märkets namn.
- Urvalet: SEO-titel saknas på 284 av 300, SEO-meta på 126 av 300.
**Bedömning.** Texterna ser maskinskrivna ut från leverantörsmall, med grammatikfel som kan följa av översättning ("en canvasbälte"). Mönstret med produktnamn före första meningen och bristen på SEO-titel är de största, enhetliga luckorna. Att texterna går att skriva om kräver beslut om ton, märkesmodell och standardblock (TODO i profilen). Inget är skrivet.

## Steg 5. Struktur och SEO
**Fakta.** Publik genomsökning av `workoutbrands.com`, högst cirka 1,4 anrop per sekund, `robots.txt` följd (200, 2 603 byte; `Disallow` för bland annat `/cart`, `/checkout`, sortering och filter), neutral användaragent `SiteReviewBot/1.0`. Resultat: startsidan, 101 kollektioner och 17 sidor lästes (125 sidor). **Cloudflare svarade HTTP 429 på produktsidor vid sex försök** (efter cirka 120 stora sidor), även efter väntan på 60 respektive 30 sekunder; ingen kringgång försöktes. Produktsidor och blogg saknas därför i genomsökningen. En enskild produktsida gick att hämta separat efter en paus (HTTP 200).
- Startsidan: titel "Workout Brands – Streetwear, Träningskläder & Skor", metabeskrivning finns, en H1. Alla 119 sidor har titel, canonical (pekar på sig själva) och 21 hreflang-länkar; 11 saknar metabeskrivning (bland annat `/collections/outlet`, `/pages/varumarken`, `/blogs/news`). Tio sidor har två H1, en saknar H1 (`/pages/contact`).
- Strukturerad data på alla sidor: BreadcrumbList, Organization (med kontaktuppgifter); ItemList på kollektioner; Article på bloggsidor. Bilder saknar sällan alt-text på dessa sidor (median 0 per sida, 76 bilder per sida).
- Sidstorlek: median 571 kB HTML, störst 1,3 MB; 76 bilder per sida (kollektioner 49 produktkort, sidbrytning med `rel="next"`).
- Länkning: startsidans huvudmeny länkar sitewide till 101 kollektioner (klickdjup 1) och 13 sidor. I de 119 genomsökta sidorna hittades länkar till 229 av de 673 kollektionerna; **444 kollektioner (varav 350 med minst 10 produkter) har ingen länk på något genomsökt ställe**. Det är en nedre gräns för "föräldralösa": produktsidor, där brödsmulor länkar till kollektioner, ingick inte. Kollektionssidor länkar vidare till i median 51 andra kollektioner.
- Menyer: `main-menu` (Kvinna/Man till `/pages/...`), `main-menu-2` (Startsida), samt två menyer som ser ut som kopior av andra butikers startsidor: "Startsida 2.0 (nelly.com)" och "Startsida 2.0 GYMSHARK".
- Språk: 20 publicerade språk i Shopify; sitemap och hreflang ger 21 språkversioner. Språkversionerna har egna sitemaps.
**Behövs från David för Search Console** (kör `shopify-sync/scripts/gsc_export.py sc-domain:workoutbrands.com` i Cloud Shell med din egen inloggning; läsning): rapporterna sida (page), sökfråga (query), sida × sökfråga (page_query), land (country), enhet (device) och dagsvis historik (month) för 16 månader. Dessutom i Search Console direkt: Sidindexering ("Sidor") med orsaker till att sidor inte indexeras, Sitemaps (inskickade kontra indexerade, särskilt 466 saknade produkter), och Kärnvärden (Core Web Vitals). Ingen nyckel skickas i chatten och Windsor.ai används inte.

## Steg 6. Leverantörsflöden och automation
**Fakta.** Det går inte att läsa appar eller schemalagda jobb i butiken (åtkomsten saknar `scriptTags` och appar). Indirekta spår:
- `price-change-job-active` på 2 897 aktiva produkter (3 925 totalt) och `BF26`: samma produkter, och på samtliga är jämförpriset 9,3–10,5 % över priset.
- Importmarkören "in sheet" på 5 315 aktiva produkter och "urban classics" på 6 965: produkterna kommer ur ett kalkylblad eller en leverantörsimport, med inköpspris från leverantör.
- Inköpspris på 27 % av varianterna ser inte rimligt ut (steg 3).
- Fältet `vendor` används som status ("Out of stock", "outlet").
**Risker (enligt BEST OF SPORTS-lärdomarna) — bedömning.** (1) Id mot artikelnummer: ett jobb som slår upp inköpspris på fel nyckel ger fel inköpspris; de 1 927 misstänkta kan vara ett sådant fall. (2) En regel "sänk aldrig priset" eller en prisapp med återställning kan låsa kvar höga priser eller ta tillbaka gamla priser när kampanjtaggen tas bort; rensa inte `price-change-job-active` eller `BF26` innan appen är identifierad. (3) Skrivning av pris bör kräva en huvudbrytare, AV som standard.

## Steg 7. Leverans
Filer: `genomlysning.md` (den här), `backlogg.md` (15 punkter), `data/` (siffror, spärrkandidater per grupp, kollektionsproblem, genomsökning), `data/sparrkandidater_antal.json`. Butiksprofilen är uppdaterad i `shopify-sync/config/butiksprofil-workoutbrands.json`. Beslutsfil: `rapporter/beslut-2026-11-18.md` (med listan "Behöver Davids ja").

### Spärrlistekandidater (förslag, aktiv=false tills David beslutar; idfiler i `data/sparr_*.csv`, antal bland aktiva)
barn (MT Kids, Urban Classics Kids) 311 plus 71 med barntagg; "Out of stock" som vendor eller typ 37; outlet 92; prisjobb/BF26 2 897; titel med enskild storlek 86; dubbletitlar 366; solglasögon 111; mobilskal 28; vendor som inte är märke 138; misstänkt inköpspris 1 927; saknar inköpspris 22; presentkort 1.

### Begränsningar
Utkast (8 149 produkter) lästes inte. Bara de första fem varianterna per produkt lästes. Genomsökningen stoppades av Cloudflare efter 125 sidor. Ingen Search Console, ingen annonsdata, ingen läsning av appar. Textkontrollen är automatisk (heuristik), inte full manuell granskning.
