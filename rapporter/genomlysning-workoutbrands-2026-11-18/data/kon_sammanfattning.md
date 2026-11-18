# Könsklassning av aktiva produkter och kollektioner, Workout Brands (endast läsning)

Butiken bekräftad som workoutbrands.com (get-shop-info). Inget skrevs i Shopify; inga taggar, metafält eller priser rörda.

## Regel (fast)
- **dam:** tagg Dam, Women, woman eller Kvinna (hela taggen, skiftlägesokänsligt), eller titel som börjar med Ladies eller Women, eller vendor UC Ladies.
- **herr:** tagg Herr, Man eller Men (hela taggen, skiftlägesokänsligt).
- **unisex:** tagg Unisex.
- **Klass, i denna prioritetsordning:** båda (både dam- och herrsignal) > unisex (taggen Unisex, utan konflikt) > bara dam > bara herr > ingen.
- En produkt med både Unisex och bara en könstagg räknas som unisex. En produkt på vendor UC Ladies med en herrtagg räknas som båda.
- Skript: `shopify-sync/scripts/kon_klassning_wb.py`.

## 1. Totalt (7 371 aktiva produkter, katalogläsning natten 2026-11-17)
| Klass | Antal | Andel |
|---|---|---|
| bara herr | 3 483 | 47,3 % |
| bara dam | 2 109 | 28,6 % |
| båda (konflikt) | 921 | 12,5 % |
| ingen könstagg/signal | 819 | 11,1 % |
| unisex | 39 | 0,5 % |

Taggantal bland de aktiva (hela taggar, skiftlägesokänsligt): men 4 285, man 3 554, herr 2 992, women 2 921, woman 2 287, dam 2 248, kvinna 561, unisex 60. Taggen woman (småbokstav) förekommer på 2 287 produkter. Siffrorna avviker något från koordinatorns (7 380 aktiva) eftersom min läsning är från natten.

## 2a. Per vendor (topp 25)
| Vendor | Produkter | bara dam | bara herr | unisex | båda | ingen |
|---|---|---|---|---|---|---|
| UC Ladies | 1 207 | 1 195 | 0 | 0 | 12 | 0 |
| MT Men | 931 | 9 | 848 | 0 | 45 | 29 |
| UC Men | 905 | 7 | 839 | 0 | 10 | 49 |
| Urban Classics Accessoires | 485 | 105 | 31 | 4 | 296 | 49 |
| Brandit | 385 | 26 | 186 | 11 | 73 | 89 |
| MT Upscale | 366 | 5 | 352 | 0 | 4 | 5 |
| Flexfit | 286 | 1 | 3 | 9 | 241 | 32 |
| Miss Tee | 275 | 248 | 5 | 0 | 11 | 11 |
| Merchcode | 231 | 3 | 214 | 4 | 8 | 2 |
| Build your Brand | 208 | 80 | 62 | 0 | 5 | 61 |
| DEF | 191 | 42 | 127 | 6 | 2 | 14 |
| Urban Classics Kids | 157 | 2 | 0 | 1 | 0 | 154 |
| MT Kids | 154 | 3 | 3 | 0 | 0 | 148 |
| MT Accessoires | 129 | 12 | 12 | 0 | 77 | 28 |
| MJ GONZALES | 128 | 9 | 113 | 1 | 3 | 2 |
| Starter Black Label | 121 | 16 | 97 | 0 | 6 | 2 |
| Dangerous DNGRS | 104 | 40 | 55 | 0 | 2 | 7 |
| Ecko Unltd. | 101 | 1 | 88 | 0 | 2 | 10 |
| Rocawear | 87 | 16 | 62 | 0 | 4 | 5 |
| Just Rhyse | 83 | 27 | 53 | 0 | 0 | 3 |
| Lost Youth | 74 | 2 | 67 | 1 | 0 | 4 |
| MT Ladies | 73 | 65 | 2 | 0 | 1 | 5 |
| Merchcode Ladies | 69 | 64 | 5 | 0 | 0 | 0 |
| CS | 66 | 1 | 9 | 0 | 51 | 5 |
| MT X Artist | 56 | 4 | 50 | 0 | 0 | 2 |

Observation: UC Men och UC Ladies räknas här som aktiva produkter men antalet (905 och 1 207) är bara de märkesnamn som butiken använder; produkter av Urban Classics-linjen finns också under vendors "Urban Classics", "Urban Classics Accessoires" och "Urban Classics Kids".

## 2b. Per produkttyp (topp 15)
| Typ | Produkter | bara dam | bara herr | unisex | båda | ingen |
|---|---|---|---|---|---|---|
| T-shirt | 2 223 | 446 | 1 549 | 4 | 15 | 209 |
| Hoodie | 917 | 226 | 573 | 5 | 13 | 100 |
| Jacka | 497 | 180 | 269 | 1 | 3 | 44 |
| Keps | 413 | 14 | 20 | 10 | 323 | 46 |
| Långärmad tröja | 324 | 99 | 184 | 0 | 4 | 37 |
| Byxor | 249 | 95 | 120 | 0 | 2 | 32 |
| Shorts | 245 | 83 | 138 | 1 | 2 | 21 |
| Mjukisbyxor | 178 | 42 | 117 | 1 | 1 | 17 |
| Skjorta | 148 | 36 | 97 | 0 | 2 | 13 |
| Topp | 137 | 135 | 0 | 0 | 1 | 1 |
| Linne | 134 | 65 | 61 | 1 | 0 | 7 |
| Jeans | 120 | 38 | 64 | 0 | 1 | 17 |
| Tights | 117 | 110 | 2 | 0 | 0 | 5 |
| Solglasögon | 111 | 13 | 2 | 0 | 92 | 4 |
| Klänning | 110 | 103 | 0 | 0 | 0 | 7 |

Mönster: konflikterna ("båda") finns främst på produkter som verkligen är för alla (kepsar 323, solglasögon 92, Flexfit 241, tillbehör), där taggarna Dam, Herr, Kvinna, Man, men, woman och Women ligger på samma produkt; de är därför inte fel utan ett sätt att tagga unisex. Det är en bedömning.

## 3. Kollektioner (674 stycken, alla lästa; `kon_kollektioner.csv`)
- Medlemskap lästes för alla 674 kollektioner (hela kollektionen om högst 300 produkter, annars de första 300 i butikens standardordning). Andelar räknas på de aktiva produkter som finns bland dessa (draft/arkiverade ingår inte). 53 kollektioner har inga aktiva produkter bland de lästa.
- Kandidater för könsfilter (bara dam minst 20 % och bara herr minst 20 %, minst 10 aktiva produkter): **62 kollektioner**, alla manuella. Hela listan finns i `kon_kollektioner.csv` (kolumn `kandidat_konsfilter` = ja, sorterad efter antal analyserade produkter).
- De största kandidaterna: varjacka-dam-herr, hoodie-herr-dam (2 257 produkter; bara dam 20,7 %, bara herr 63,1 %), streetwear-man-och-kvinna (6 413), trojor-dam-herr, vardagsklader-man-och-kvinna (2 811), plus-size-klader-herr-dam (14 964), urban-classics (480), urban-classics-1 (14 772), vinterklader-herr-dam, hatt, smycken-1, t-shirt-herr-dam (5 897), byxor-herr-dam, jackor-herr-dam, jeans-herr-dam, sportklader-herr-dam, cargobyxor-herr-dam, def-herr-och-dam, dangerous-dngrs-herr-och-dam, just-rhyse-herr-och-dam, starter-black-label-herr-och-dam, forvert-herr-och-dam, thug-life-herr-och-dam.
- Nära tröskeln (inte kandidater): hoodie-herr-dam-1 (dam 19,7 %, herr 68,7 %), brandit-herr-och-dam (6 813 produkter: dam 6,8 %, herr 49,1 %, båda 23,3 %, ingen 16,8 %), mister-tee-herr-och-dam (8 226: dam 76,7 %, herr 16,3 %), rocawear-herr-och-dam (228: dam 18,4 %, herr 71,3 %).
- Varumärkessidor och blandkollektioner med tydligt sned fördelning visar att könstaggarna saknas på många produkter (Brandit 89 av 385 utan könssignal), så ett filter byggt på taggar skulle tappa produkter.
- **Redan separata versioner** (handle utan suffix + -herr/-dam/-man/-kvinna/-herr-och-dam): 155 grundnamn har minst två varianter. Exempel: thug-life (-herr, -dam, -herr-och-dam), urban-classics (-man, -kvinna, grund), just-rhyse, def, forvert, dangerous-dngrs, starter-black-label (-man och -herr-och-dam), shorts (-kvinna, -man, -herr, -dam, grund), fleecejackor, klader-till-kontoret, essentials, underklader, populara-produkter, jultroja. Fullständig grupplista: `kon_syskon.json`.
- Obs: flera "separata" versioner är inte separerade. jultroja-herr och jultroja-dam har båda 63,6 % herr och 36,4 % dam (samma 11 produkter som jultrojor-herr-dam). biker-shorts-dam har 50 % herr (identisk med traningsshorts-herr-dam). fleecejackor-herr har 26,8 % dam. brandit-dam och brandit-damjackor är identiska.
- Fler kollektioner finns som urval av hela butiken: produkter-over-500, wob-alla-produkter och workout-brands-black-friday-2025 (14 964 produkter) visar samma blandade profil.

## 4. Konflikt och ingen könstagg
- 20 tydligaste konfliktprodukterna (alla sju könstaggar: Dam, Herr, Kvinna, Man, men, woman, Women): 19 Flexfit-produkter (kepsar, mössor) och Brandit B Classic T-Shirt (9340098871624, även unisex). Lista: `kon_konflikt_och_ingen.csv` (grupp konflikt).
- 20 utan könstagg med störst lager: i huvudsak Build your Brand (Basic Oversize Hoody, Kids Basic Tee m.fl.), Flexfit Wooly Combed china Youth (lager 150 219), UC Cotton Loose Tee (UC Men, 126 344), New Morning Studios Sleeveless Tee. Lista i samma fil (grupp ingen_konstagg).

## 5. Prisjobbstaggade (price-change-job-active, 2 897 st)
| Klass | Antal |
|---|---|
| bara herr | 1 655 |
| bara dam | 875 |
| ingen | 255 |
| båda | 102 |
| unisex | 10 |

Ett könsfilter bygger på klassen och rör alla 2 897 (de får ett kön eller ingen). Skulle man bara tillföra eller rätta könsdata där den saknas eller krockar (klasserna ingen och båda) gäller det 357 av dem; övriga 2 540 har redan ett tydligt kön. Ingenting skrivs.

## Inte kontrollerat
Om butikens tema redan har filter för metafältet `shopify.target-gender` (definitionen finns men värdena är tomma enligt koordinatorn), vilka kollektioner som visas i menyer, och hur många produkter som saknas i kollektionsurvalet (första 300).
