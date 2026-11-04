# Genomlysning GORILLA SPORTS (gorillasports.se/.dk), onboarding fas 1

Datum 2026-11-04. Bara läsning av offentliga sidor, publika flöden och repots filer. Inget ändrat i Shopify, tema, Search Console, Analytics eller Google Ads.

## 1. Vad som är anslutet (och inte)
| Källa | Läge | Följd |
|---|---|---|
| Shopify-verktyget | Kräver ny inloggning ("sign in again"). Butiken kunde inte verifieras med get-shop-info, så ingen läsning gjordes där | Inventeringen bygger på publika flödet. Status, SEO-fält, marknader, lager saknas |
| Windsor.ai | Endast `facebook_organic` (Gorilla Sports Nordics) är ansluten. **Search Console, GA4, Google Ads saknas** | Ingen sökefterfrågan-/trafikanalys kunde göras i den här sessionen |
| Ahrefs | Alla anrop avvisas med "Insufficient plan" (samma som 2026-10-09). Brand Radar ingår därmed inte | Ingen sökordsvolym, backlinks eller AI-synlighet |
| Repots site-audit (sites.toml) | Gorilla är konfigurerad (SE/DK, GSC `sc-domain`, GA4 320165929, Ads SE+DK, BigQuery `gorilla-sports-data`) men körs mot BigQuery/Secret Manager som inte nås härifrån | Nattliga fynd och GSC/GA4-tabeller kan läsas av David eller en session med Google Cloud-åtkomst |
| Miljön | Innehåller bara BEST OF SPORTS-appens nycklar. De används inte här (annan butik) | Gorilla behöver egen app/nyckel för skrivning i fas 2 |

## 2. Fynd, rangordnade efter effekt och risk
Urval: 120 slumpade produktsidor (seed 20261104), 25 .dk-produktsidor, startsidor, 40 kollektioner, 6 informationssidor.

| # | Fynd | Belägg | Effekt | Risk att åtgärda | Förslag (utförs ej) |
|---|---|---|---|---|---|
| 1 | **Dubbel Product-schema på varje produktsida** (två `Product`-block: ett från temat/app med betyg och ett med gtin13 och returpolicy) | 120 av 120 | Hög (rich results, AI-sökmotorer får två motsägande poster) | Medel (tema/app) | Slå ihop till ett block; behåll gtin, returpolicy, betyg. Kontrollera med Rich Results Test. Kräver tema-åtkomst |
| 2 | **Inga alt-texter på produktbilder** | 8 140 av 8 140 bilder; 6 914 av 10 478 `img` på sidorna | Hög (bildsök, tillgänglighet) | Låg | Generera alt ur titel + variant via API (reversibelt). David beslutar mönster |
| 3 | **Titeltaggen får suffix och radbrytning**: `Titel\n – Gorilla Sports Nordics` på alla sidor, startsidan `Gorilla Sports - … – Gorilla Sports Nordics` (märket två gånger) | 120/120 produkter; start .se/.dk | Medel (trunkerade titlar, 38 av 120 produkttitlar >60 tecken, 30 av 40 kollektioner >60) | Låg–medel (tema) | Ta bort suffixet eller kort märkesnamn; rensa radbrytning. Tema-ändring av David |
| 4 | **Metabeskrivning verkar saknas som eget värde**: 80 av 120 börjar med produkttiteln, 22 av 120 är >155 tecken. Typiskt Shopifys automatik av brödtexten | 120 | Medel (CTR) | Låg | Bekräfta med Admin API vilka som är tomma; skriv kort sann meta enligt standard §14 |
| 5 | **Beskrivningen börjar med titeln som h2** | 815/869 | Medel (dubbel rubrik, svag första mening) | Låg | Tas bort vid textrullning; kräver regel i profilen |
| 6 | **Säljande/oanvänd påståendeton**: R5-ord (stabil, robust, skyddar, slitstark, säker, premium, bästa, professionell) i 437 av 869 beskrivningar; lastgräns-liknande uttryck i 489; "enligt tillverkaren" i 0 | Hela katalogen | Medel (regelrisk, tillit) | Medel (kräver omskrivning) | Fas 2 efter Davids val av ton |
| 7 | **Betyg i strukturerad data från liten bas**: `aggregateRating` 4,9 med 3 omdömen på en produkt; ingen på de andra | 1 av 3 granskade | Låg–medel (påstående mot kund) | Låg | Bekräfta att omdömena är riktiga (jfr lärdom 2026-10-26: kontrollera varifrån betyg kommer) |
| 8 | **Varumärkesfältet i schema = "Gorilla Sports Norden"** (leverantörsvärde) i stället för "Gorilla Sports" | 777 produkter | Medel (GEO: samma märke under 4 namn) | Låg | Samla leverantörsfältet till ett värde (beslut) |
| 9 | **Hreflang bara sv och da-DK** + x-default mot .se; 2 av 120 produktsidor saknar hreflang | 118/120 | Låg | Låg | Åtgärda de som saknas; överväg om DK-sidor ska ha egen x-default |
| 10 | **H1 saknas/fel antal**: 3 av 40 kollektioner (parallettes, hantelset, foam-roller-massageboll) och 2 informationssidor (`gorilla-sports`, `kontakta-oss`) | 5 sidor | Låg–medel | Låg | Tema/innehåll |
| 11 | **Emoji i kollektionstitlar** ("Parallettes … 💪", "Helkroppsträning 🏋️‍♀️") | exempel i 40 | Låg | Låg | Ta bort ur title-taggen |
| 12 | **Kollektioner med tunt innehåll**: inte bedömt; 208 kollektioner varav många smalt överlappande (viktskivor 26/30/50 mm m.fl.) | sitemap | Medel | Medel | Kräver GSC-data (saknas) för att välja vilka som ska slås ihop |
| 13 | **Titeldubbletter**: 12 titlar förekommer två–tre gånger (Löpband MAXXUS M8 ×3 m.fl.) | 13 produkter | Medel (kannibalisering) | Medel | Granska varianter; spärrlistad i utkast |
| 14 | **Startsidan saknar WebSite/SearchAction**; Organization finns (adress, kontakt, sameAs) | start | Låg | Låg | Lägg till |
| 15 | **Sidvikt**: HTML ca 430 kB per produkt-/startsida (median 434 kB) | 120 | Låg–medel | Medel | Mät med `psi_snapshot.py` före åtgärd (lärdom 2026-10-20) |

**Det som fungerar:** canonical självpekande på alla 120 + 25 sidor, en canonical per sida, `lang` rätt per domän, .dk helt översatt (25/25 danska), Product + BreadcrumbList + Organization finns, sitemap med produkter, kollektioner, sidor, bloggar och artiklar, robots.txt tillåter alla crawlers (inga AI-bottar blockerade).

## 3. GEO (hur tydligt för en AI-sökmotor)
- **Märke:** schema säger "Gorilla Sports Nordics" (Organization) men brand "Gorilla Sports Norden" eller "Gorilla Sports" (fynd 1, 8). Tre namn för samma sak försvagar entiteten.
- **Produkter:** pris, valuta, lager, gtin finns i schema; tillverkarpåståenden saknar "enligt tillverkaren" (fynd 6); duplicerade Product-block (fynd 1).
- **Leveransvillkor:** sidorna `/pages/delivery`, `/returning`, `/payments` finns och har h1 och meta; returpolicy finns i Product-schema (hasMerchantReturnPolicy) men inte frakt (`shippingDetails` saknas i det vi såg). Tidigare genomlysning (2026-10-09, skrivbord) pekade på att leveranstid anges olika på olika sidor; det är inte omkontrollerat här.
- **Agentläsbarhet:** butiken exponerar `agents.md`, `/.well-known/ucp` och robots.txt-instruktioner (Shopifys standard). `llms.txt` returnerar en Cloudflare-utmaning till automatiska klienter (inte bedömt om det är avsiktligt).
- **Ej mätt:** faktisk synlighet i AI-svar (Ahrefs Brand Radar kräver plan).

## 4. Luckor mellan efterfrågan och sidor
Kunde **inte** göras: kräver Search Console, GA4, Google Ads eller Ahrefs. Verktyg och SQL finns i repot (`sql/analys/sokfragor_luckor.sql`, `kategori_sokord.sql`, `doda_sidor_med_trafik.sql`) men körs mot BigQuery. Nästa steg är att David (eller en session med Google Cloud-åtkomst) kör dem, eller att Windsor kopplas till Search Console/GA4/Google Ads.

## 5. Textkontroll mot regelboken (R1–R19)
Skript: `skrivfil_kontroll.py` med `butiksprofil-gorillasports.json` och `sparrlista-gorillasports.json`. Urval 120 (med verklig SEO-titel/meta) och alla 869 (titel + beskrivning). Underlag: `rapporter/gorillasports-2026-11-04/kontroll_*.txt`.

| Kontroll | Urval 120 | Alla 869 |
|---|---|---|
| Fel totalt (skript) | 137 | 736 |
| Osynligt tecken | 96 (varav nästan alla hårda mellanslag U+00A0 från editorn) | 690 (686 bara NBSP, 4 nollbreddstecken U+200B) |
| Meta utanför 70–155 | 22 (alla >155) | n/a |
| SEO-titel >43 | 13 | n/a |
| Liten bokstav efter kolon | 6 | 21 |
| Titeldubblett | 0 | 25 poster (12 titlar) |
| Standardblock | n/a (inget Gorilla-block definierat) | n/a |
| Cirkulär inledning, förbjudna uttryck, "N tum skärm" | 0 | 0 |
| Märke i versaler (R8, profilens märken) | 0 | 0 (men MAXXUS/EXCALIBUR/TRIGRIP är versaler i 210 titlar, ej testade, kräver beslut) |
| R5-ord (utanför skriptet, egen sökning) | | 437 av 869 |
| `&` i texten | | 31 |

**Läsning:** Tolka inte 736 som "736 dåliga texter". Nästan allt är NBSP, som BOS-regeln flaggar men som i Gorillas editor är normalt (David bör besluta om regeln ska gälla Gorilla; annars rensas NBSP vid skrivning). De verkliga innehållsfynden är: säljande/oanvända påståenden (437), titeln upprepad som h2 (815), meta >155 (18 %), titeldubbletter (13), versaler i titlar (210). R1–R4 och R11–R12a kan inte avgöras utan leverantörsunderlag och är därför G-regler för granskare i fas 2. **Gränser:** skriptet mäter format, inte sanning; metafälten kommer från den renderade sidan och kan vara automatik.

## 6. Frågor till David
1. Ska Gorillas **ton** förbli säljande, eller följa BOS faktatextläge? (Avgör fynd 5–6.)
2. Vilka **märken** ska skyddas (GS, MAXXUS, EXCALIBUR, TRIGRIP)? Är versalerna avsiktliga?
3. Är **hårda mellanslag** (NBSP) tillåtna i Gorilla-texter?
4. **Utanför tills vidare:** godkänner du förslaget (vibrationsplattor, massagestolar, pulsmätare, barnhandskar; massagebollar/foam rollers valfritt)?
5. Finns ett **standardblock** (leverans/retur/garanti) och en **klartagg**? Vilka taggar får aldrig ändras?
6. **Åtkomst:** vill du ansluta Search Console, GA4 och Google Ads i Windsor (eller köra BigQuery-frågorna), logga in Shopify-verktyget på Gorilla, och skapa en egen Admin API-app för Gorilla? Ahrefs-planen räcker inte; ska den uppgraderas eller hoppar vi över den?
7. Ska Gorillas texter vara **utgångspunkt för BEST OF SPORTS** enligt tidigare beslut även om fas 1 visar att de är säljande?
