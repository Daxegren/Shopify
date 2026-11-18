# Tillägg 2026-11-18: inköpspriser, sitemap-gap, moms och marknader (Workout Brands)

Nytt avsnitt; befintlig text i `genomlysning.md` är oförändrad. Bara läsning (`graphql_query` med sidning, ShopifyQL). Inga mutationer, inga prisförslag, ingen ändring av spärrlistan, inga taggar rörda. Butiken kontrollerades med `get-shop-info` före läsningen: `workoutbrands.com`, SEK. Underlaget kom från koordinatorsessionen (hänvisning till Davids uppdrag "börja med Workout Brands") och motsvarar beslut 1, 6 och 9 med alternativ (a) i `rapporter/beslut-2026-11-18.md`; Davids eget ja på de nio besluten finns ännu inte.

## 1. Inköpspriser (beslut 1)

Underlag: samma 7 371 aktiva produkter och 33 007 varianter som i huvudrapporten (de första fem varianterna per produkt; 101 varianter saknar inköpspris). Marginal efter moms för Sverige: `(pris/1,25 − inköp)/(pris/1,25)`. Skriptet `shopify-sync/scripts/analysera_inkop_wb.py` ger siffrorna; filer i `data/inkop_*`.

### Fakta
- Tre grupper: 23 799 varianter har marginal 30–90 % ("rimliga"), 8 920 över 90 %, 141 under inköpspris (negativ marginal), 46 mellan 0 och 30 %, 101 saknar inköpspris.
- **De rimliga har inköpspris i hela kronor** (5 370 av 5 421 produkter, första varianten) och pris som slutar på 9 i 99 % av fallen; kvoten pris/inköp har median 3,18 (kvartiler 2,89 och 3,18). Det ser ut som prisformel från ett inköpspris i kronor.
- **De 8 920 över 90 % har kvot pris/inköp 27,05** (kvartiler 24,83 och 29,53), inköpspris-median 12,90 kr, och **88 % har decimaler** (1 667 av 1 893 produkter). Slutdecimalerna är .90 (4 622 varianter), .50 (1 407), .00 (1 103), .95 (826), .99 (250) och .45 (163): typiska listpriser i valuta, till exempel 2,45, 7,90, 12,90, 16,90.
- **Importväg:** 92,3 % av varianterna **utan** taggen `in sheet` har marginal över 90 %, mot 0,8 % av dem **med** taggen (23 447 varianter med taggen, 9 459 utan). Efter skapandeår: 2023 0 %, 2024 0 %, 2025 19,9 %, **2026 92,6 %** (3 335 varianter).
- **Märken:** Build your Brand 99,5 %, MJ Gonzales 100 %, Zoo York 99,6 %, Urban Classics 97,6 %, Lost Youth 95,9 %, Ecko Unltd. 75,8 %, Rocawear 61,6 %, Dangerous DNGRS 52,1 %; MT Men 22 %, UC Ladies 15 %, Brandit 15 % (`data/inkop_per_vendor.csv`). Per produkttyp: Sneakers 99,3 %, tom typ 71,6 %, Hoodie 35,9 %, T-shirt 28,4 % (`data/inkop_per_produkttyp.csv`).
- Inom en produkt är det i regel alla varianter eller inga: 1 880 produkter har alla varianter över 90 %, 36 är blandade, 5 433 har inga. Samma SKU-modell är blandad i bara 28 av 8 676 fall; för alla tio-i-topp-exempel per märke (`data/inkop_exempel_per_vendor.csv`, 353 rader) finns **inget** rimligt inköpspris på samma SKU-modell hos annan variant eller produkt (kolumnen "samma_skumodell_rimligt_inkop_finns" = nej för de tio tydligaste i varje märke).
- Pris- och lagerfaktorer: andelen över 90 % är 24,0 % på prisjobbsprodukter och 29,4 % utan prisjobb, 19,0 % på varianter utan lager och 37,8 % med lager. Prisjobbet verkar alltså inte vara orsaken.
- **Under inköpspris (141 varianter):** Relode 49, Gavelo 28, vendor "Out of stock" 26, CLN 14, Under Armour 9, outlet 8, UC Men 5, MT Men 1. Kvot pris/(inköp inkl. moms-justering) har median 0,46. Ingen ligger på prisjobbet. Ett tydligt enskilt fall: MT All Time Favorite Oversize Tee (SKU MT3590-10122-0051), pris 229 kr och inköp 798,50 kr (`data/inkop_under_inkop_141.csv`).
- **Saknar inköpspris (101 varianter, 22 produkter första variant):** 85 har vendor "workoutbrands.com" (troligen egna produkter eller presentkort), 7 UC Ladies, 4 "Out of stock" (`data/inkop_saknas_22.csv`).

### Hypotestest (fakta om testet, bedömning om slutsatsen)
Om inköpspriset i de 8 920 varianterna är i euro och räknas om till kronor med en växelkurs (testad 9,5–12), blir marginalen:

| Kurs (kr per euro) | Median marginal | Kvartiler | Andel varianter 30–70 % | Under 0 % |
|---|---|---|---|---|
| 9,5 | 56,1 % | 52,2 % och 59,8 % | 95,7 % | 0 % |
| 10,5 | 51,5 % | 47,1 % och 55,5 % | 96,7 % | 0 % |
| **11** | **49,2 %** | 44,6 % och 53,4 % | **97,1 %** | 0 % |
| 11,5 | 46,9 % | 42,1 % och 51,3 % | 96,3 % | 0,1 % |
| 12 | 44,6 % | 39,6 % och 49,2 % | 95,6 % | 0,1 % |

Testet "samma formelmarginal som de rimliga (60,6 %)" ger en implicit faktor på 55 (kvartiler 50 och 60), alltså ingen enskild valutakurs: 0 % av varianterna hamnar mellan 10 och 12. Bara 256 av 8 920 är paket eller set (titeln innehåller pack/set), så "per styck i ett paket" förklarar inte mönstret.

### Rangordnad hypotes (BEDÖMNING, ej bekräftad)
1. **Mest sannolik: inköpspriset är leverantörens listpris i euro, oomräknat, och skrivs av en annan importväg än kalkylbladet (taggen `in sheet`).** Stöd: decimaler som .90/.95/.45, nästan alla med taggen `in sheet` är i kronor och nästan alla utan är det inte, ett rimligt marginalintervall (44–53 % vid kurs 10,5–11,5) och nästan inga negativa värden efter omräkning. Svaghet: om priset sattes med 60,6 % marginal i euro-värdet vore kvoten 8,5 i stället för 11, så utgångspunkten för prissättningen är oklar.
2. **Annan valuta eller leverantörsenhet än euro** (till exempel enhetspris före frakt och tull, eller dansk/polsk valuta): går inte att utesluta, men .90-ändelserna och intervallet 44–53 % talar mer för euro.
3. **Inmatningsfel i enskilda poster** förklarar de 141 under inköpspris och de ensamma blandade produkterna, men inte 8 920 varianter. (Exempel: 798,50 kr för en T-shirt som säljs för 229 kr ser ut som ett sifferfel eller en annan produkts pris, samma slags fel som i BEST OF SPORTS.)

### Vad David eller leverantören behöver bekräfta (ingen skrivning görs)
- I vilken valuta anger leverantörsflödet inköpspriset för de varianter som saknar taggen `in sheet` (Build your Brand, MJ Gonzales, Zoo York, Urban Classics, Lost Youth, delar av Ecko, Rocawear, DNGRS)? Jämför mot en faktura eller prislista för tre exempel: Basic Tank BB011-00007-0058 (inköp 2,45, pris 129 kr), MT Flames Of Hope Tee MT3779-00007-0058 (7,90, 279 kr) och en sneaker.
- Vilket flöde eller vilken app skriver inköpspris i butiken i de två importvägarna, och används någon omräkning av valuta?
- Är de 141 under inköp avsiktliga (utförsäljning) eller fel (Relode, Gavelo, CLN, "Out of stock")?
- Inga nya inköpspriser föreslås här och inga skrivs.

## 2. Sitemap-gapet (beslut 6)

### Fakta
- Sitemapen (`/sitemap_products_1…7.xml`) har 6 921 produktadresser; butiken har 7 371 aktiva produkter. **450 saknas.** (En tidigare siffra, 466, innehöll 16 falska träffar eftersom produkternas handle med tecknet ® är URL-kodad i sitemapen; efter avkodning återstår 450.)
- **449 av de 450 är inte publicerade i försäljningskanalen Online Store** (`published_status:unpublished` ger 449 aktiva produkter; `productsCount` med `published_status:published` ger 6 922). Alla 449 har `publishedAt = null`. Av dem har 362 lager över 0 (summa 579 245 enheter), 87 har lager 0; 3 saknar bild.
- Orsaker (per kanal, `resourcePublications`): **405 är publicerade bara i kanalen "Meta AI and Muse"** (publikations-id slutar på …743496, publicerades 2026-10-15 och 2026-11-03/04), **43 är inte publicerade i någon kanal alls**, 1 produkt (Sorona Regular Tee 5-pack) är publicerad i fyra kanaler men inte i Online Store. Kontrollprodukt: 93969055958 är den kanal där publicerade produkter har publicerats (äldre Online Store-publikation).
- Ingen skillnad på status: alla 449 är `ACTIVE`. Inga är utkast i någon kanal.
- Skapad: i batchar. Flest dagar: 2026-08-27 (62), 2025-02-20 (54), 2026-02-21 (26), 2025-02-19 (19), 2026-09-19 (11). Efter månad: 2025-02 87, 2025-03 53, 2026-02 51, **2026-08 95**. 368 uppdaterades i november 2026 och 150 bär prisjobbstaggen `price-change-job-active` (prisjobbet skriver alltså även på produkter som inte är synliga i webbutiken).
- Märken (`data/sitemapgap_per_vendor.csv`): UC Men 89, UC Ladies 79, Urban Classics 42, MT Men 40, Urban Classics Accessoires 23, Flexfit 18, Ecko Unltd. 18, Brandit 13, Urban Classics Kids 13, Merchcode 9. Barnprodukter 24, outlet 4.
- Den sista produkten som saknas utan att vara opublicerad är 8351417237832 (`ua-vanish-woven-8in-shorts-academy`, vendor "Out of stock"). Den är publicerad i Online Store men saknas i sitemapen; orsak oklar (cache eller sitemapens bygge).
- Listor: `data/sitemapgap_ej_publicerade_online_store_449.csv` (id, handle, titel, vendor, typ, skapad, uppdaterad, lager, media, antal kanaler, orsak, prisjobb), `data/sitemapgap_per_vendor.csv`, `data/sitemapgap_17_ovriga_handles.json` (de 17 handles som först såg ut som gap, varav 16 var kodningsfel).

### Bedömning
Att 405 produkter är publicerade i Meta-kanalen men inte i webbutiken tyder på att en publiceringsåtgärd (troligen en app eller en kanalsynk) hoppade över Online Store, inte att produkterna är avsiktligt dolda. Det är inte bevisat; det kan vara avsiktlig avpublicering. 362 produkter med lager är alltså osynliga för webbköpare. Beslutet om publicering är Davids; inget ändras här.

## 3. Moms och marknader (beslut 9)

### Fakta
- Butiksnivå: `taxesIncluded = false`, `taxShipping = false`.
- **Marknad Sweden är den enda av 33 marknader med uttrycklig prisinställning:** `inclusiveTaxPricingStrategy = INCLUDES_TAXES_IN_PRICE`. Alla andra 32 marknader (Danmark, Finland, Norge, Tyskland m.fl.) har `priceInclusions = null`, det vill säga ingen egen inställning (de följer butiksnivån: moms läggs på). Tre marknader är utkast (Irland, Serbien, USA). Danmark, Norge, Finland m.fl. är egna marknader med egen valuta (DKK, NOK, EUR …).
- 100 senaste ordrarna (2026-10-10 till 2026-11-17, `data/moms_ordrar_antal_per_land.json`): 93 svenska (SEK, `taxesIncluded = true`, "SE Moms" 25 %). Exempel #3460: pris 199,00, varav moms 39,80. Övriga ett exempel per land: **Danmark** #3461: vara 449,0 DKK, delsumma 404,10, skatt 118,27 ("DK Moms" 25 %), totalt 591,37, `taxesIncluded = false` (moms läggs på). **Nederländerna** #3379: 58,95 EUR, moms 15,09 (21 %), totalt 86,94. **Belgien** #3386, **Italien** #3383 (22 %) och **Polen** #3375 (23 %) har skatt som läggs på och `taxesIncluded = false`. **Norge** #3404 (451 NOK) och **Brasilien** #3381 (124 BRL) har ingen skattrad och totalt = vara + frakt.
- Inget land utom Sverige har mer än ett exempel i de 100 ordrarna (urvalet är litet för de andra).

### Oklart (ej läsbart via läsfråga)
- Vad den publika butiken **visar** för konsumenter i Danmark och övriga marknader (pris med eller utan moms, och om texten "inkl. moms" visas). Prisinställningen är läst; visningen är inte kontrollerad på sidan (en kontroll kräver ytterligare publika anrop med landsval).
- Om `null` i `priceInclusions` verkligen innebär "exklusive moms i visningen" för varje marknad eller om temat visar något annat.
- Skatteinställningarna per land (Inställningar, Skatter och tullar) är inte läsbara via de läsfrågor som användes.
- Om danska och andra marknadspriser är omräknade från SEK eller har egna priser (vara 449,0 DKK i #3461 jämfört med 486,75 SEK för en annan vara; olika varor, ingen jämförelse görs här).

## Filer (nya)
`data/inkop_siffror.json`, `data/inkop_per_vendor.csv`, `data/inkop_per_produkttyp.csv`, `data/inkop_exempel_per_vendor.csv`, `data/inkop_under_inkop_141.csv`, `data/inkop_saknas_22.csv`, `data/sitemapgap_ej_publicerade_online_store_449.csv`, `data/sitemapgap_per_vendor.csv`, `data/sitemapgap_17_ovriga_handles.json`, `data/moms_ordrar_antal_per_land.json`; skript `shopify-sync/scripts/analysera_inkop_wb.py`.
