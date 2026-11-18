# Prisförslagstest Workout Brands, kurs 11 kr/EUR (endast läsning)

Butiken bekräftad som workoutbrands.com (get-shop-info). Inga mutationer, inga skrivningar, inga taggar, spärrlistor eller priser rörda. Inga prisändringar föreslås för skrivning; allt nedan är ett test.

## Underlag
- Alla 109 781 varianter på alla 7 371 aktiva produkter lästes (sidindelade läsfrågor). Antalet stämmer med butikens variantantal per produkt för samtliga produkter (kontrollerat).
- Fält: pris, jämförpris, SKU, unitCost (inköp), lager, produkttaggar, vendor.
- Indelning: 108 530 varianter ingår i testet, 1 236 saknar inköpspris och 15 ligger under inköpspris (negativ marginal) och redovisas separat i `prisforslag_test_wb_utanfor_test.csv`.
- Eurogrupp (arbetsdefinition): marginal över 90 % med unitCost som den står, formel (pris/1,25 − inköp)/(pris/1,25), ordinarie pris = jämförpris om det är högre än priset, annars priset. Inköp i kronor = unitCost × 11. Övriga varianter räknas med unitCost som den står.
- Förslagslogik: `bedom()` i `shopify-sync/scripts/pris_forslag.py` med målmarginal 0,60, golv 0,55, tak 0,65, tolerans ±0,03; formelpris = inköp/(1−0,60)×1,25 avrundat uppåt till närmaste …9; ändringar över ±25 % hålls kvar.
- Skript: `shopify-sync/scripts/prisforslag_test_wb.py`. Resultatfil: `prisforslag_test_wb_11kr.csv` (en rad per testad variant, kolumnen godkand är tom).

## 1. Eurogruppen mot övriga, kurs 11

| Mått | Eurogrupp | Övriga |
|---|---|---|
| Varianter | 30 184 | 78 346 |
| Produkter | 2 021 | 5 486 |
| Marginal nu (efter korrigering): under 50 % | 11 704 | 1 495 |
| 50–57 % | 13 042 | 319 |
| 57–63 % | 3 408 | 75 735 |
| 63–70 % | 1 243 | 780 |
| 70–80 % | 738 | 4 |
| över 80 % | 49 | 13 |
| Inom 57–63 % och ingen rea: rörs inte av skriptet | 2 471 | 36 816 |
| Skulle få höjt pris | 25 435 | 1 853 |
| Skulle få sänkt pris | 2 120 | 35 332 |
| Oförändrat pris (lika) | 158 | 4 345 |
| Hålls kvar av ±25 %-regeln (av höjda/sänkta) | 14 721 (14 199 upp, 522 ner) | 1 691 (1 674 upp, 17 ner) |
| Median prisändring | +25,1 % | −1,5 % |
| Medelvärde prisändring | +22,6 % | +0,3 % |
| Median / medel utan de hållna | +17,9 % / +13,8 % | −1,5 % / −1,5 % |
| Med prisjobbstaggen price-change-job-active | 10 545 | 39 253 |
| Pågående rea (jämförpris över pris) | 11 183 | 40 532 |

Så läses tabellen:
- "Inom 57–63 %" i marginalfördelningen mäts på ordinarie pris och inkluderar varianter med pågående rea. Raden "rörs inte" räknar bara varianter utan rea, eftersom skriptet räknar om varianter med pågående rea mot ordinarie pris även om marginalen redan ligger i intervallet. Därför skiljer sig 75 735 från 36 816 i gruppen övriga.
- Höjt/sänkt avser skriptets förslag före ±25 %-regeln; "hålls kvar" är den delmängd som överstiger ±25 %.
- Prisjobbstaggen betyder att skrivning ska utebli (flaggan PRISJOBBSTAGG_SKRIVS_EJ i filen). Varianter med rea får flaggan REA_PAGAR_RAKNA_OM_EFTER_ATERSTALLNING.

## 2. Per vendor (topp 15 efter antal varianter)

| Vendor | Varianter | Varav euro | Inom 57–63 (rörs ej) | Höjs | Sänks | Hålls | Median % | Prisjobb | Rea |
|---|---|---|---|---|---|---|---|---|---|
| UC Ladies | 23 832 | 2 872 | 8 955 | 2 744 | 11 136 | 1 909 | −1,5 | 12 627 | 12 879 |
| UC Men | 18 458 | 2 442 | 4 798 | 2 574 | 9 779 | 1 871 | −1,3 | 11 931 | 12 413 |
| MT Men | 10 446 | 2 099 | 6 622 | 2 020 | 1 591 | 1 343 | 13,0 | 2 233 | 2 260 |
| Build your Brand | 8 714 | 8 672 | 1 334 | 5 789 | 1 433 | 2 384 | 18,3 | 1 678 | 1 798 |
| Brandit | 8 097 | 709 | 1 156 | 980 | 5 250 | 837 | −1,0 | 5 971 | 6 609 |
| MT Upscale | 5 924 | 456 | 4 027 | 470 | 1 162 | 295 | −1,3 | 1 559 | 1 559 |
| Miss Tee | 4 865 | 462 | 2 858 | 449 | 1 549 | 322 | −1,5 | 1 656 | 1 665 |
| Merchcode | 2 764 | 836 | 1 377 | 816 | 551 | 693 | 24,2 | 684 | 699 |
| MJ GONZALES | 2 365 | 2 365 | 0 | 2 330 | 35 | 1 254 | 25,1 | 1 298 | 1 301 |
| DEF | 2 222 | 865 | 555 | 835 | 604 | 455 | 4,6 | 1 238 | 1 278 |
| Urban Classics Kids | 1 926 | 299 | 1 073 | 287 | 524 | 167 | −1,3 | 624 | 629 |
| New Morning Studios | 1 743 | 1 689 | 246 | 1 354 | 143 | 578 | 23,0 | 580 | 580 |
| Ecko Unltd. | 1 421 | 1 013 | 57 | 970 | 351 | 758 | 26,5 | 879 | 909 |
| Lost Youth | 1 386 | 1 349 | 0 | 1 353 | 3 | 482 | 19,6 | 1 095 | 1 095 |
| Starter Black Label | 1 251 | 51 | 395 | 57 | 658 | 26 | −1,2 | 814 | 814 |

Marginalfördelningen per vendor finns i `prisforslag_test_wb_sammanfattning.json`. Build your Brand (99,5 % euro), MJ GONZALES (100 %), Lost Youth (97 %) och New Morning Studios (97 %) är nästan helt eurogrupp.

## 3. Känslighet för kursen (bara eurogruppen påverkas)

| Kurs | Inom 57–63 (rörs ej) | Höjs | Sänks | Hålls kvar av ±25 % |
|---|---|---|---|---|
| 10 | 6 460 | 19 249 | 4 301 | 3 817 |
| 11 | 2 471 | 25 435 | 2 120 | 14 721 |
| 12 | 1 465 | 27 305 | 1 112 | 22 477 |

Övriga gruppen är oberoende av kursen (36 816 / 1 853 / 35 332 / 1 691). Eurogruppens utfall är mycket känsligt: kring 10 kr per euro hamnar fler inom intervallet, vid 12 kr hålls drygt 22 000 varianter kvar av ±25 %-regeln.

## 4. Observationer om data (fakta)
- 6 varianter har pris över 5 000 kr, bland dem BY004-04568 (125 229 kr, jämförpris 139 139 kr, inköp 3,45) på produkt 10289919230280. Det är sannolikt inmatningsfel och ger felaktiga marginaler i testet. 109 varianter har pris under 20 kr (till exempel 8,01 kr på samma produkt).
- Eurogruppsdefinitionen fångar varje variant med marginal över 90 %. Den skiljer inte ut dem som har hög marginal av andra skäl (till exempel felaktigt högt pris) från dem med euro-inköp. Davids bekräftelse gäller varianter utan taggen `in sheet`; testet använder marginalkriteriet som arbetsdefinition.

## 5. Inte räknat
Frakt, tull och andra inköpsomkostnader (inköpspriset antas vara leverantörens listpris exklusive dessa); faktisk kurs per leverans (11 kr per euro är antagen, känslighet i avsnitt 3); moms på andra marknader än Sverige (priser antas ha 25 % svensk moms inräknad; andra marknader lägger moms ovanpå); om jämförpriset ska användas som ordinarie pris (testet gör det när det är högre än priset); varianter utan inköpspris (1 236) och under inköpspris (15); valutakonvertering av priser för andra marknader; lagerkostnad och efterfrågan.
