# Åtgärdslista: var pengarna försvinner på Gorilla Sports (förslag, ström 3, 2026-10-27)

**Status:** förslag (nivå A, bara analys). Ingenting är ändrat i butik, annonskonto, tema eller Google Cloud. Inget av nedanstående utförs utan Davids ja; **annonsändringar är nivå C och kräver även Rudes ja.** Jag har inte kunnat köra något mot BigQuery, Google Ads eller Shopify. Alla siffror kommer ur tidigare resultatfiler (fil, datum, avsnitt anges). Skattningar anger antaganden och osäkerhet; ingen rad påstår att en åtgärd *ger* en viss intäktsökning.

**Så läser du listan.** *Bevisat* = en siffra ur en körd fråga eller en uppgift som lästs ur kod eller konfiguration. *Hypotes* = min tolkning, inte avgjord. **Nivå** enligt `standardtester.md`: A = rapport/analys utan ändring, B = David godkänner en grupp, C = David godkänner varje ändring (pris, annonser, och allt i tema/spårning som David gör själv i temaredigeraren). **99,9 %** = riktlinjen i `arbetsstrommar.md` (tillägget 2026-10-27): Gorilla får bara förändringar som är exakt reversibla, bygger på entydigt bevis ur hela genomsökningen, **inte rör rankingkänsligt innehåll, pris, annonser, spårning eller mallar**, kan kontrolleras mot ett mått som kan misslyckas, och där skadan är liten och synlig. Eftersom pengaåtgärder i praktiken rör annonser, pris, spårning eller mallar uppfyller **ingen åtgärd som ändrar något** riktlinjen; de är förslag på nivå B/C med David som beslutar. Läsning och analys ändrar inget och är därför utanför riktlinjen.

## Tre mönster i pengarna (bevisat, med period och urval)
1. **Tappet sitter i Google-märkta ordrar.** Mellan P0 (2026-08-13–09-11) och P1 (2026-09-12–10-11) minskade ordrarna med −407 808 SEK (SE −187 453, DK −220 355; urval: 1 537 ordrar i de två perioderna, SE 840 och DK 697). Ordrar märkta Google (senaste besöket, kolumnerna "Google" och "google") står för −230 412 SEK, 56 % av nettotappet (`trafik-konvertering-resultat-2026-10-13.txt`, avsnitt 2 och 4). Märkningen "Google" innehåller både betald och organisk trafik.
2. **Annonsklick följer försäljningen per produkt.** 87 av 390 produkter där Googles produktklick minskade står för −317 335 SEK av −391 087 (81 %); slutsålt (dagens lager 0) förklarar minst −41 477 (ca 11 %; undre gräns) (`beslut-2026-10-26.md` §9, 30 dagar mot 30 före). Sambandet visar inte orsak.
3. **Konverteringen har sjunkit samtidigt som trafiken.** GA4-sessioner SE 35 686 → 29 505 (−17 %), DK 34 855 → 26 630 (−24 %); GA4-konvertering SE 1,11 → 0,99 % och DK 1,08 → 0,97 % (≈ −10 %); Shopify-ordrar SE −23,5 %, DK −30,8 % (`trafik-konvertering-resultat-2026-10-13.txt`). GA4-köp motsvarar 80–83 % (SE) och 90–91 % (DK) av Shopify-ordrarna i båda perioderna, så GA4-mätningen verkar inte ha försämrats mellan perioderna (egen uträkning; GA4 är ändå inte facit).

Storleksordning på konverteringsfallet (aritmetik, inte prognos): om andelen som köper hade legat kvar på P0:s nivå med P1:s trafik hade GA4-köpen varit ca 11 % fler (SE ≈ 328 mot 291, DK ≈ 288 mot 257), i omsättning ca 115 000 SEK per 30 dagar med periodens snittorder (SE 1 827 SEK, DK 1 053 DKK omräknat med P1:s kvot 1,51). Det visar vad fallet kostar, inte vad en åtgärd skulle ge.

## Prioriterad lista

| Prio | Åtgärd | Vem | Nivå | Uppfyller 99,9 % |
|---|---|---|---|---|
| 1 | Storsäljare som tappat: kontrollera tillgänglighet, börja med chinsstången | David (inköp), Claude (analys) | A (analys); beslut om inköp utanför butiken | Gäller inte (ingen ändring i butik) |
| 2 | Search Brand - Mixed SE (ROAS 0,88): granska söktermer och konvertering | Rude | C | Nej (annonser) |
| 3 | Mät GTM-dubbelladdning och spårningsintegritet innan något ändras | David kör, Claude läser | A (mätning); åtgärd C | Nej (spårning, mall) |
| 4 | Läs köpflödets resultat (långköraren) | David kör, Claude läser | A | Gäller inte |
| 5 | Performance Max DK: steg 0, därefter begränsat test av ROAS-mål | Rude, David | A (steg 0), C (test) | Nej (annonser) |
| 6 | Produkter med annonskostnad men inget värde (Hemmagympaketet Budget m.fl.) | David (kontroll), Rude (annonser) | A (kontroll), C | Nej (annonser) |
| 7 | Annonser på produkter som inte går att köpa | Claude (körning), Rude | A, C | Nej (annonser) |
| 8 | Meta DK Adv+ Sales (ROAS 2,59) | Annonsansvarig för Meta (oklart vem), David | C | Nej (annonser) |
| 9 | Rabattnivån i SE | Claude (körning), David | A, C | Nej (pris/rabatt) |
| 10 | Merchant Center för Gorilla: data saknas | David | A/B | Gäller inte |
| 11 | E-post: data saknas | David | A | Gäller inte |
| 12 | Priser strax under fraktgränsen | Claude (körning), David | A, C | Nej (pris) |

Prioritetsordningen väger (a) belopp som är bevisat, (b) hur säker orsaken är, (c) hur billig och reversibel åtgärden är. Rad 1–4 är billiga och lättförstådda. Rad 5 har störst *möjlig* effekt men också störst osäkerhet (se `roas-golv-och-dk-pmax.md`).

---

## 1. Storsäljare som tappat: kontrollera tillgänglighet (chinsstången först)
- **Vad:** ta reda på vilka av de 30 mest sålda produkterna för 28–90 dagar sedan som i dag sålt nästan ingenting och är slut, inaktiva eller borttagna, och avgör per produkt om den ska fyllas på, ersättas eller avvecklas. Första kandidat är *Kombinerad Chinsstång och Dipsställning Vägg*.
- **Bevis (bevisat):** DK 26 → 1 sålda, −48 035 SEK; SE 6 → 0, −12 054 SEK (`trafik-konvertering-resultat-2026-10-13.txt` avsnitt 5, P0 → P1); tillsammans ca 60 000 SEK, 15 % av tappet (`beslut-2026-10-12-2.md`). Annonsklick DK 445 → 27, värde 13 953 → 732 (`annonser-resultat-2026-10-14.txt` avsnitt 3). Andra stora tapp i samma tabell: Rygglyftsbänk Hyperextension Hopfällbar SE 26 → 11 (−27 935), Kettlebell GS Svart 2–20 kg DK 29 → 2 (−13 846), Kettlebell Fitness 2–20 kg SE 35 → 7 (−13 042), Hexagonhantlar PREMIUM DK 24 → 6 (−12 232). Dagens lager för chinsstången är 0 (`beslut-2026-10-12-2.md`).
- **Hypotes:** att slutsåld var det som *startade* tappet. Lagret är en ögonblicksbild utan historik, så när varan tog slut vet vi inte. Skillnaden mellan "slutsåld" och "avvecklad av leverantören" syns inte i datan; det kräver en kontroll i Shopify och mot leverantören (lagret styrs av leverantören, `omsattning_tapp_per_produkt.sql`).
- **Skattning:** om försäljningen av chinsstången skulle återkomma i samma takt som före (60 089 SEK per 30 dagar) och bidragsmarginalen är 34–37 % av omsättningen inklusive moms (`roas-golv-och-dk-pmax.md`, antagande) rör det sig om ca 20 000–22 000 SEK i bidrag per 30 dagar. Osäkert: en vara kan ha sålt i en kampanjperiod och återkommer kanske inte.
- **Osäkerhet:** hög för orsak, låg för belopp (försäljningstappet är uppmätt).
- **Vem:** David och inköp beslutar om påfyllning. Claude kör `storsaljare_tapp.sql` för att hitta resten av listan (30 produkter, per marknad, med status, lager, veckoförsäljning, annonsklick).
- **Nivå:** A för analysen. Inköp är ett affärsbeslut utanför butiken; en eventuell statusändring i Shopify är nivå C.
- **99,9 %:** gäller inte (ingen ändring i butik, annons, tema eller spårning).

## 2. Search Brand - Mixed SE: ROAS 0,88
- **Vad:** be Rude granska söktermer, matchningstyper och konverteringsåtgärd för kampanjen, och avgöra om den ska begränsas eller pausas.
- **Bevis (bevisat):** 30 dagar: kostnad 7 261, värde 6 394, ROAS 0,88, 338 klick (`beslut-2026-10-26.md` §13). Månadsjämförelse P0 → P1: kostnad 8 302 → 7 852, klick 372 → 369, värde 28 657 → 8 267, alltså ROAS 3,45 → 1,05 (egen uträkning) med *oförändrat antal klick* (`annonser-resultat-2026-10-14.txt` avsnitt 2). Systerkampanjen Search Brand Exact är stabil: värde 48 497 → 50 335, ROAS 11,07 (§13).
- **Hypotes:** att något ändrats i vilka söktermer kampanjen träffar eller i hur konverteringarna tillskrivs. Det är det värde per klick som rasat, inte volymen. Orsaken är okänd (söktermsrapport saknas).
- **Skattning:** på Net Profit version 1 (SE bidragsmarginal ca 37 %, antagande) är bidraget efter annonskostnad ca −4 900 SEK per 30 dagar (`roas-golv-och-dk-pmax.md` avsnitt 1). Om kampanjens värde mest är köp som skulle skett ändå (varumärkessök) är förlusten ännu närmare hela kostnaden. Beloppet är litet; värdet ligger i att signalen kan avslöja ett mätproblem.
- **Osäkerhet:** medel. Siffran är uppmätt; orsaken inte.
- **Vem:** Rude. **Nivå:** C. **99,9 %:** nej (annonser).

## 3. Spårningsintegritet: mät först, ändra sedan
- **Vad:** mät om containern GTM-M2JNXNW faktiskt körs två gånger och om GA4-händelser och Meta-pixel skickas dubbelt, före och efter samtycke, med `scripts/gtm_natverkstest.py` (nytt). Först därefter beslut om att ta bort en laddning.
- **Bevis (bevisat):** onsite-kontrollen fann containern laddad två gånger på Gorilla, dels i `theme.liquid`, dels via snippeten `google-tag-manager` (`beslut-2026-10-26.md` §22). Samma sak flaggas av den nya kontrollen `gtm_container_loaded_twice` i nästa genomlysning (§24, §28). Påverkan på mätningen är **inte verifierad** (§22).
- **Bevis för att mätproblem finns i annonsplattformarna (hypotes):** plattformarnas konverteringsvärde har sjunkit mer (Google SE −76 %, DK −83 %) än butikens ordrar (SE −16 %, DK −29 %) mellan första och sista veckan i `beslut-2026-10-26.md` §10. Det kan bero på färre visningar, inte på spårning; delar kan vara försämrad spårning (samtycke, taggar).
- **Bevis mot att GA4 skulle ha tappat:** förhållandet GA4-köp / Shopify-ordrar är stabilt (SE 83 → 80 %, DK 91 → 90 %, egen uträkning ur `trafik-konvertering-resultat-2026-10-13.txt`). GA4 visar alltså inte att något gått sönder mellan P0 och P1. Det säger inget om Google Ads- eller Meta-taggar.
- **Observation om mätmetoden (bevisat i självtest):** en webbläsare slår ihop två skripttaggar med *exakt samma adress* till ett nätverksanrop, men skriptet körs ändå två gånger. Det betyder att ett test som bara räknar anrop kan missa en dubbelladdad container. `gtm_natverkstest.py` läser därför även DOM (antal skriptelement och inbyggda laddningsskript) och antal `gtm.js`-händelser i dataLayer.
- **Kanalen "web":** ordrar utan registrerad källa (kolumnen `source_name` = "web") minskade SE 64 → 48 och DK 59 → 31 mellan P0 och P1 (−35 191 respektive −47 103 SEK), näst störst efter Google (`trafik-konvertering-resultat-2026-10-13.txt` avsnitt 4). **Hypotes:** en del av dem är annonsrelaterade köp där källan tappats (t.ex. samtycke eller UTM); inte undersökt.
- **Osäkerhet:** hög för effekt på siffrorna, låg för att dubbelladdningen finns.
- **Vem:** David kör testet i Cloud Shell; Claude läser resultatet. Själva ändringen i `theme.liquid` görs av David i temaredigeraren.
- **Nivå:** A för mätning. Temaändringen är C (spårning, mall).
- **99,9 %:** nej (spårning och mall ingår i undantagen).

## 4. Köpflödets resultat (ännu inte lästa)
- **Vad:** läs resultaten från långköraren `scripts/langkorare_gorilla.sh` (läge, indexering, renderande kategorikontroll, samtycke och spårning, köpflöde mobil och desktop, tillgänglighet). Skriptet skrevs 2026-10-26 (`ANDRINGSLOGG.md`), men resultaten har inte lästs (`beslut-2026-10-26.md` avsnitt 5: "läs resten av långköraren"). `kopflode_test.py` har dessutom bara testats mot en låtsasbutik (`beslut-2026-10-23.md`).
- **Bevis för att frågan är värd att ställa (bevisat från Shopifys rapport, relaterad av David, ej kontrollerad av oss):** konvertering 1,38 → 0,98 % mot fjolåret; andel som når kassan 3,41 → 2,17 %; andel som lägger i varukorgen 4,44 → 3,36 %; andel som slutför i kassan 40,33 → 45,24 % (alltså inte kassan); mobil 71 % av besöken med 0,90 % konvertering mot 1,38 % i fjol (`beslut-2026-10-14.md`). Min egen kontroll av samma analys: konverteringen mot föregående period *minskade* (GA4 −10 till −11 %), inte förbättrades.
- **Hypotes:** försämringen sitter före kassan (produktsida, pris, leveransbesked, tillgänglighet, mobilupplevelse). Orsaken är inte undersökt.
- **Osäkerhet:** hög.
- **Vem:** David kör skriptet (kräver Playwright); Claude läser. **Nivå:** A. **99,9 %:** gäller inte (läsning).

## 5. Performance Max DK
- **Vad:** steg 0 (kontrollera ändringshistorik, tillgänglighet, andel förlorade visningar och moms i konverteringsvärdet), därefter ev. test av lägre ROAS-mål med budgettak och stoppregler. Fullständigt förslag i `roas-golv-och-dk-pmax.md`.
- **Bevis (bevisat):** ROAS 2,94 mot mål 5, kostnad 16 743, värde 49 289 (30 dagar, `beslut-2026-10-26.md` §13); Google DK visningar −80 %, kostnad −76 % första till sista veckan (§10); dagsbudgeten används till ca 22 %. **Hypotes:** att målet är den begränsande faktorn. Mot den talar att värdet per klick halverades (35,0 → 18,4 DKK) och att Meta DK tappat lika mycket (−62 %).
- **Break-even:** ROAS 2,94 ligger vid uppskattad rörlig break-evenpunkt (2,9–3,0) för DK. Mer volym i samma kampanj betalar sig inte om den ger samma ROAS.
- **Osäkerhet:** hög. Marginalen är oklar, moms oklart, inkrementalitet okänd.
- **Vem:** Rude och David. **Nivå:** A för steg 0, **C för testet (kräver Davids och Rudes ja)**. **99,9 %:** nej.

## 6. Produkter med annonskostnad men inget värde
- **Vad:** kontrollera pris, lager och produktsida för de produkter som fortfarande får klick men ingen försäljning, och därefter låta Rude utesluta eller byta ut dem.
- **Bevis (bevisat):** Hemmagympaketet – Budget (SE) 497 → 345 klick, kostnad 6 575 → 4 604, värde 31 636 → 534; Kettlebellpaket GS Svart 17–30 kg 90 → 19 klick, värde 23 276 → 0; Styrketräningspaket – 60 kg 108 → 29 klick, värde 10 462 → 0; Fot och handledsvikt Paket 10 kg 258 → 107 klick, värde 15 342 → 1 796 (`annonser-resultat-2026-10-14.txt` avsnitt 3). Per produkt (30 dagar, §12 i `beslut-2026-10-26.md`): 399 av 477 SE-produkter har ROAS under 1 och står för 53 % av produktkostnaden men 1,5 % av värdet (DK 301 av 336: 66 % och 0,9 %). Täckningen är bara 76 % (SE) och 56 % (DK) av Googles kostnad, så siffran ska inte läsas som en prognos.
- **Hypotes:** produkterna har en lokal orsak (pris, lager, flöde, produktsida). Beslut O i `beslut-2026-10-14.md` (kontrollera produkterna) ligger kvar obesvarat i filerna.
- **Osäkerhet:** medel för orsak. Per produkt är 30 dagar kort och brusigt.
- **Vem:** David kontrollerar i Shopify (Claude når inte Gorillas butik), Rude utesluter. **Nivå:** A för kontrollen, C för annonserna. **99,9 %:** nej.

## 7. Annonser på produkter som inte går att köpa
- **Vad:** kör den rättade frågan `annonser_pa_slutsalda.sql` (Gorilla) för att räkna annonskostnad på produkter som är slut, inaktiva eller borttagna, och låt Rude utesluta dem om beloppet är väsentligt.
- **Bevis:** den första versionen var felaktig (alla annonsrader hamnade i en grupp; `ANDRINGSLOGG.md` 2026-10-26) och enligt ändringsloggen 2026-10-26 var den rättade versionen syntaxkontrollerad men inte körd (om den körts sedan finns inget resultat i filerna). **Det finns alltså inget bevisat belopp för annonskostnad på produkter som inte går att köpa.** Det som är bevisat: slutsålt förklarar minst −41 477 SEK av omsättningstappet (§9), och Google slutade själv visa chinsstången DK när den tog slut (445 → 27 klick), vilket tyder på att kostnaden där blev låg.
- **Hypotes:** att kostnaden på otillgängliga produkter är väsentlig. Kan vara liten.
- **Osäkerhet:** hög (inget belopp). **Vem:** Claude (körning, David kör i Cloud Shell), Rude (åtgärd). **Nivå:** A, sedan C. **99,9 %:** nej.

## 8. Meta DK Adv+ Sales
- **Vad:** granska kampanjen: ROAS 2,59, kostnad 25 281, värde 65 585 (30 dagar, `beslut-2026-10-26.md` §13). På Net Profit version 1 (DK bidragsmarginal 33–35 %) är bidraget efter annons ca −2 600 till −3 700 DKK per 30 dagar (`roas-golv-och-dk-pmax.md`, antagande).
- **Bevis (bevisat):** Meta DK per vecka: ROAS 7,37 → 2,37 (lägst 1,76), konverteringsvärde per klick 16,6 → 6,3 DKK (−62 %), kostnad och klick i stort sett stabila (§10).
- **Hypotes:** försämringen sitter i DK:s konvertering (sajt eller sortiment), eftersom Googles PMax visar samma mönster. Meta-värdet är Metas egen tillskrivning och kan vara överskattat.
- **Osäkerhet:** hög. **Vem:** den som sköter Meta (ej angivet i filerna), David. **Nivå:** C. **99,9 %:** nej.

## 9. Rabattnivån i SE
- **Vad:** ta reda på vilka rabattkoder och automatiska rabatter som bär rabatten, med `rabatter_koder.sql` (nytt), och därefter besluta om regler.
- **Bevis (bevisat):** rabatt i procent av ordervärdet SE 10,1 % → 11,7 %, DK 3,3 % → 3,2 % (P0 → P1, `trafik-konvertering-resultat-2026-10-13.txt` avsnitt 1). Shopifys egen analys: rabatter 30 335 → 102 753 kr mot fjolåret, ca 10,5 % av bruttoförsäljningen mot 3,2 % (`beslut-2026-10-14.md`; ej kontrollerad av oss).
- **Hypotes:** att rabatterna sänker nettoförsäljningen utan att ge motsvarande merförsäljning. Datan visar vad som getts, inte om den gav merförsäljning; det kräver en jämförelse som inte går att göra ur tabellerna. Beslut Q i `beslut-2026-10-14.md` är obesvarat.
- **Osäkerhet:** hög för effekt. **Vem:** Claude (körning), David (beslut). **Nivå:** A för analys, C för ändrade regler. **99,9 %:** nej.

## 10. Merchant Center för Gorilla: data saknas
- **Vad:** avgör om avvisade produkter får klick eller har lager. `merchant_avvisade.sql` kräver tabellen `merchant_products_gorillasports_se`.
- **Bevis (bevisat):** `sites.toml` har `merchant_account_id` bara för Best of Sports (rad 113), inte för Gorilla. Det finns alltså sannolikt ingen Merchant-data för Gorilla. (Tabellen är inte kontrollerad i BigQuery; `KEY=gorillasports bash scripts/kontrollera_datakallor.sh` visar det.) Merchant-fynden som finns (7 avvisade, 73 utan enhetspris, 69 små bilder) gäller Best of Sports, inte Gorilla (`beslut-2026-10-23.md`).
- **Hypotes:** att avvisade produkter kostar pengar. Ingen uppgift för Gorilla.
- **Vem:** David (Merchant-id och läsrätt för tjänstkontot, konfiguration). **Nivå:** A (läsning) men kräver en ändring av behörighet/konfiguration som David beslutar. **99,9 %:** gäller inte.

## 11. E-post: data saknas
- **Vad:** ta reda på hur stor del av ordrarna e-post och SMS står för, och om flödena (välkomst, övergiven varukorg, uppföljning) finns och fungerar.
- **Bevis:** `klaviyo_enabled` finns inte i `sites.toml` för Gorilla (standard är `false`, `config.py`), så `epost_andel.sql` kan inte köras. Inga e-postvärden syntes heller i kanalfördelningen (`source_name`/utm-källor i `trafik-konvertering-resultat-2026-10-13.txt` avsnitt 4); e-post är sannolikt osynlig där.
- **Observation (probabelt fel):** `epost_andel.sql` läser vyn `growth_daily_KEY` ur datasetet `shopify`, men vyerna skapas i datasetet `site_audit` (`src/site_audit/growth_sql.py` rad 134 och `config.py` rad 84). Filen ägs inte av mig och är oförändrad; samordnaren bör rätta den innan den används.
- **Okänt:** om Gorilla använder Klaviyo eller något annat e-postverktyg, och vilka flöden som finns. **Vem:** David. **Nivå:** A. **99,9 %:** gäller inte.

## 12. Priser strax under fraktgränsen
- **Vad:** kör `priser_strax_under_gransen.sql` (inte körd) för en lista över produkter som ligger strax under 800 kr (SE) och 700 DKK (DK), och bedöm därefter enskilda priser.
- **Bevis (bevisat men litet):** Pull Up Bar Chinsstång Multi Dörr kostar i snitt 799 kr i ordrar som betalar frakt; åtta ordrar saknade i snitt 6 kr till fri frakt och betalade 179 kr (`beslut-2026-10-26.md` §20, 90 dagar). Det är åtta ordrar, ca 1 400 kr i frakt på 90 dagar, och priset är inte kontrollerat mot listpris och rabatt (§20: "ska kontrolleras ... innan något ändras"). Andel som betalar frakt: SE 22 %, DK 45 % (§19).
- **Hypotes:** att korgar tippas över gränsen av priset. Påfyllning förklarar bara en mindre del av ökningen vid 800 kr (108 av 165 ordrar mellan 800 och 1 000 kr är enkelradsordrar, §20). Effekten på konvertering är inte mätbar utan varukorgsvärden ur GA4.
- **Osäkerhet:** hög. **Vem:** Claude (körning), David (prisbeslut). **Nivå:** A, sedan **C för varje prisändring**. **99,9 %:** nej (pris).

---

## Vad som saknas för att avgöra
1. **Verklig marginal** (vad Shopifys `unit_cost` är; Net Profit version 2 med vikter; DK-bidragets 43,3 mot 41,2 %) och vilka kostnader som är fasta. Utan den går inget ROAS-golv att fastställa. Se `roas-golv-och-dk-pmax.md`.
2. **Moms i plattformens konverteringsvärde.** En känd order kan avgöra.
3. **Ändringshistorik och andel förlorade visningar** i Google Ads (finns inte i BigQuery) och Rudes svar på frågan om mål-ROAS ändrats sedan augusti (beslut N, `beslut-2026-10-14.md`).
4. **Lagerhistorik.** När storsäljarna tog slut.
5. **Fjolårsdata för ordrar och trafik.** Shopify-ordrar finns 60 dagar bakåt (`read_all_orders` saknas) och GA4 från mars 2026. `pengalage_veckovis.sql` visar fjolår som NULL om det saknas.
6. **Varukorgsvärde mot konvertering** (för fraktgränsen): kräver GA4-händelser i BigQuery. `ga4_dataset = "gorilla-sports-data.analytics_320165929"` är konfigurerat i `sites.toml`, men om exporten finns och är färsk är inte kontrollerat.
7. **Merchant-data och e-postdata för Gorilla** (rad 10–11).
8. **Köpflödets resultat och samtyckes-/spårningstesten** (rad 3–4).
9. **Inkrementalitet.** Hur mycket av Googles och Metas värde som är verklig merförsäljning. Ingen holdout finns.
10. **Vad som ändrades i slutet av augusti och början av september** i tema, pris, frakt, appar, kassa, kampanjer eller produktflöde (`beslut-2026-10-26.md` §10, fråga 1). Inte besvarad.

## Körningar David behöver göra (i ordning)
Alla är läsning. Kör i Cloud Shell i mappen `~/Shopify/shopify-sync` efter att filerna hämtats med `git pull` (jag har inte committat; det gör samordnaren). Klistra in resultatet så läser jag det.

```bash
# 1. Datakontroll: finns tabellerna och är de färska? (A)
KEY=gorillasports bash scripts/kontrollera_datakallor.sh

# 2. Pengaläget vecka för vecka, två marknader, 12 veckor (A). Läs datakontrollen först.
sed 's/PROJ/gorilla-sports-data/g' sql/analys/pengalage_veckovis.sql | bq query --use_legacy_sql=false --max_rows=100 | tee pengalage.txt

# 3. Storsäljare som tappat (A)
sed 's/PROJ/gorilla-sports-data/g' sql/analys/storsaljare_tapp.sql | bq query --use_legacy_sql=false --max_rows=100 | tee storsaljare.txt

# 4. Annonser på produkter som inte går att köpa, rättad version (A)
sed -e 's/PROJ/gorilla-sports-data/g' -e 's/KEY/gorillasports_se/g' -e 's/SHOPDS/shopify/g' sql/analys/annonser_pa_slutsalda.sql | bq query --use_legacy_sql=false --max_rows=60 | tee slutsalda.txt

# 5. Rabattkoder (A)
sed 's/PROJ/gorilla-sports-data/g' sql/analys/rabatter_koder.sql | bq query --use_legacy_sql=false --max_rows=100 | tee rabatter.txt

# 6. Priser strax under fraktgränsen (A, inte körd tidigare)
sed 's/PROJ/gorilla-sports-data/g' sql/analys/priser_strax_under_gransen.sql | bq query --use_legacy_sql=false --max_rows=60 | tee prisgrans.txt

# 7. GTM-nätverkstest (A; kräver Playwright: pip install playwright && playwright install chromium)
python3 scripts/gtm_natverkstest.py --url https://www.gorillasports.se/ --out gtm-gorilla-se
python3 scripts/gtm_natverkstest.py --url https://www.gorillasports.dk/ --out gtm-gorilla-dk
python3 scripts/gtm_natverkstest.py --url https://www.gorillasports.se/products/<en-produkt> --out gtm-gorilla-se-produkt

# 8. Köpflöde, samtycke och tillgänglighet (A), den befintliga långköraren (egen flik, 45–90 minuter enligt skriptet)
nohup bash scripts/langkorare_gorilla.sh > ~/langkorare-gorilla.log 2>&1 &
```

Två frågor till David som inte är körningar: (1) hur Rude svarat på frågan om mål-ROAS och ändringshistorik, (2) om konverteringsvärdet i Google Ads är inklusive eller exklusive moms (en känd order).

## Täckning
**Genomläst i sin helhet:** `CLAUDE.md`, `LARDOMAR.md`, `arbetsstrommar.md` (inklusive riskprofilen 2026-10-27), `trafik-konvertering-resultat-2026-10-13.txt`, `omsattning-30d-resultat-2026-10-12.txt`, `annonser-resultat-2026-10-14.txt`, `tackningskarta-2026-10-26.md`, `tillvaxtdata.md`, `beslut-2026-10-26.md` avsnitt 7–20 (övriga avsnitt översiktligt), SQL-filerna `omsattning_*.sql`, `annonser_*.sql`, `cos_30d.sql`, `marginal_*.sql`, `net_profit_ordrar.sql`, `frakt_*.sql` (kommentarer och struktur), `merchant_avvisade.sql`, `epost_andel.sql`. **Delvis läst för att verifiera enskilda uppgifter:** `beslut-2026-10-14.md`, `beslut-2026-10-12-2.md`, `beslut-2026-10-18-7.md`, `beslut-2026-10-23.md`, `standardtester.md` (T23–T26, T30–T40), `ANDRINGSLOGG.md` (utvalda rader), `sites.toml`, `growth_sql.py`, `sql/growth/views.sql`.
**Inte läst:** `beslut-2026-10-18-7.md` avsnitt 6 (produkttapp per produkt, SE/DK), BOS-underlagen (utanför uppdraget), Google Ads-gränssnittet, Shopify admin, arket "SWE - Net Profit". `frakt_*.sql`-resultaten är lästa via `beslut-2026-10-26.md` §19–20, inte som rådata (ingen separat resultatfil fanns).
**Fynd som inte finns i filerna och därför inte påstås:** annonskostnad på otillgängliga produkter, Merchant-läget för Gorilla, e-postens andel, fjolårets ordrar, orsaken till konverteringsfallet.
