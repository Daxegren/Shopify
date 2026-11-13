# Beslut 3: brödsmula till specifik kollektion. Testplan och kodförslag

David godkände beslut 3 den 2026-11-12 med villkoret att tester görs först och att inget får gå sönder. Inget är ändrat i butiken. Kodförslaget bygger på temafilen som sparades 2026-10-26 (`rapporter/shopify-original-2026-10-26/bos-tema/sections__main-product.liquid`). **Temat kan ha ändrats sedan dess: läs den levande filen innan något görs och jämför.**

## Hur brödsmulan fungerar idag (läst ur koden, bekräftat i renderad HTML)
Blocket `type` i `sections/main-product.liquid` väljer den **första toppnivålänken i huvudmenyn** (`main-menu`) som produkten tillhör, med några undantag på titel. Därför blir det bara sex breda sidor. Därefter kommer en länk till en sökning på produkttypen (`/search?q=product_type:...`, finns på 47 av 48 testade sidor) och produktnamnet. Strukturerad data (JSON-LD) byggs separat högst upp i filen och använder samma toppnivålogik.

## Förslag (minsta möjliga ändring, bara tillägg)
Lägg in följande **före** raden `{%- if type_label != blank -%}` i blocket `type`. Ingenting befintligt tas bort eller ändras. Om produkten inte tillhör någon undermeny-kollektion visas brödsmulan exakt som idag.

```liquid
{%- liquid
  assign sub_category = blank
  if main_category != blank
    for child in main_category.links
      if child.type == 'collection_link' and prod_col_handles contains child.object.handle
        assign sub_category = child
        for grandchild in child.links
          if grandchild.type == 'collection_link' and prod_col_handles contains grandchild.object.handle
            assign sub_category = grandchild
            break
          endif
        endfor
        break
      endif
    endfor
  endif
-%}
{%- if sub_category != blank -%}
  <a href="{{ sub_category.url }}" class="breadcrumb-link" style="text-decoration: underline; text-transform: none !important;">{{ sub_category.title }}</a>
  <span aria-hidden="true" class="breadcrumb-separator" style="margin: 0 4px; color: #888;">›</span>
{%- endif -%}
```
Resultat: `Hem › Kondition › Kettlebell › [produkttyp] › Produktnamn`. Strukturerad data ändras **inte** i första steget (mindre risk). Den kan utökas i ett andra steg om första steget är grönt.

### Begränsning (bedömning, inte mätt)
Förslaget når bara kollektioner som finns i huvudmenyn (165 av 344). Av de nio svagt länkade synliga kollektionerna gäller det sex (kona-1, cykelsolglasogon, skivstangsset, tranings-t-shirt-dam, romet, skyddsutrustning-cykel). traningsutrustning-for-hemmagym, pre-workout-pwo och benmaskiner är inte i menyn och påverkas inte; de behöver länkar i kategoritexter (beslut 2). Hur många produkter som tillhör varje menykollektion har inte mätts.

## Testordning (inget publiceras före steg 5)
1. **Kopia.** Duplicera det publicerade temat (Teman → Åtgärder → Duplicera). Ändra bara kopian. Originalet ligger kvar som reservkopia.
2. **Ändra kopian** enligt förslaget ovan (efter att ha jämfört med levande fil).
3. **Förhandsgranska** kopian och spara 48 produktsidor som HTML (Spara sida som), filnamn = produktens handle + `.html`. Handles står i `brodsmula-fore.json`. (Förhandsgranskningen kräver inloggning och är spärrad i robots.txt, därför hämtar skriptet den inte.)
4. **Automatisk jämförelse:** `python3 -I shopify-sync/scripts/brodsmula_kontroll.py fran-filer --katalog <mappen> --ut efter.json` och sedan `jamfor rapporter/intern-lankning-bos-2026-11-12/brodsmula-fore.json efter.json`. Godkänt kräver för varje sida: ingen länk borttagen, högst en tillagd länk och den pekar på en kollektion, ordningen oförändrad, produktnamnet kvar, en canonical, giltig JSON-LD, samma övriga länkar och samma antal h1. Skriptet har 14 tester utan nätverk. Före-bilden visade 0 slumpskillnader mellan två hämtningar (6 sidor), så avvikelser är riktiga.
5. **Manuell kontroll** i förhandsvisningen: minst en produkt per huvudkategori, en produkt som ligger i flera menykollektioner, en utan undermeny-kollektion, en med tom produkttyp, ett presentkort, och mobil bredd (brödsmulan får inte brytas konstigt). Klicka på den nya länken.
6. **Publicera** kopian först när steg 4 och 5 är gröna. Om något går fel: publicera den ursprungliga temakopian igen (en minut).
7. **Efter publicering:** `snapshot` igen mot den publika sidan och `jamfor` mot före-bilden, samt kör länkmätningen om (`intern_lankning_mat.py`) för att se innehållslänkarna per kollektion. Kontrollera dagen efter i Search Console att antalet indexerade sidor inte sjunker.

## Vad som kan gå fel
- Menyn ändras av någon: brödsmulan ändras med den (gäller redan idag).
- Produkter i många menykollektioner får den första i menyordning, inte nödvändigtvis den mest passande.
- Sidans laddtid: en extra loop över menyn per produktsida; menyn har några hundra poster, så effekten är sannolikt liten men bör kännas i förhandsvisningen.

## Uppdatering 2026-11-13: steg 1 gjort i Shopify
- Butiken var BEST OF SPORTS (kontrollerat med `get-shop-info`; kopplingen byttes från Gorilla Sports med `switch-shop`).
- Den levande `sections/main-product.liquid` lästes: skiljer sig från 2026-10-26-originalet bara på de tre godkända `shop.url`→`request.origin`-raderna. Ankarraden `{%- if type_label != blank -%}` finns en gång (rad 727).
- **Opublicerad temakopia skapad:** "Brödsmula test 2026-11-13" (`gid://shopify/OnlineStoreTheme/196608491786`), duplicerad från det publicerade temat. Filen i kopian har samma kontrollsumma som den levande (md5 683650d83661ad3ee65038488e138c25).
- **Kodtillägget är inte inlagt.** Att skriva filen via verktyget kräver att hela filen (112 kB) skickas i ett anrop, vilket inte ryms. Tillägget (22 rader, bara tillägg) ligger i `brodsmula-andring.diff`. Det läggs in manuellt i kopian i temaredigeraren (steg 2 i mejlet). Efteråt läser jag tillbaka filen ur kopian och jämför mot förväntad kontrollsumma 0f376f73be0ef5bcaa820bb4f5923adb (kan skilja på blanksteg om det klistrats in annorlunda; då jämför jag raderna).
- Det publicerade temat är orört.

## Uppdatering 2026-11-13 (senare): tillägget inlagt i testkopian av Claude
- Lösning på storleksproblemet: den färdiga filen laddades upp via `stagedUploadsCreate` (ett tillfälligt uppladdningsmål, ingen fil skapades i butikens filbibliotek) och skrevs till kopian med `themeFilesUpsert` (body-typ URL). Skrivningen riktades bara mot den opublicerade kopian (`196608491786`).
- **Verifierat genom återläsning:** `sections/main-product.liquid` i kopian är 112 078 byte, md5 `0f376f73be0ef5bcaa820bb4f5923adb`, exakt den förväntade filen (levande fil + de 22 raderna i `brodsmula-andring.diff`).
- **Det publicerade temat är orört:** huvudtemat `195516039434` har fortfarande md5 `683650d8…` på filen och oförändrad tidsstämpel (2026-11-12 14:02).
- Kvar: förhandsgranska kopian, spara de 48 sidorna (`brodsmula-testsidor.csv`), kör `brodsmula_kontroll.py` och gör de manuella kontrollerna (steg 3–5). Publicering görs av David.

## Testresultat 2026-11-13 (testkopian "Brödsmula test 2026-11-13")
Hämtat med Davids delningslänk och hans uttryckliga ok (trots robots.txt, bara kopian och de 48 sidorna, högst 1 anrop/s). Varje hämtad sida bekräftades komma från kopian (`Shopify.theme.id` = 196608491786, `role: unpublished`).
- **Automatisk jämförelse mot före-bilden (`brodsmula_kontroll.py jamfor`): GODKÄND, 0 fel på 48 sidor.** Ingen länk borttagen, ordningen oförändrad, produktnamnet kvar, en canonical, giltig JSON-LD, samma övriga länkar och samma antal h1 på alla sidor.
- **31 av 48 sidor fick den nya länken** (ovrig-utrustning 8 av 8, gymutrustning 7 av 8, kosttillskott 7 av 8, varumarke 5 av 8, cyklar 4 av 8). 17 sidor fick ingen, vilket är väntat: produkten ligger inte i någon undermeny-kollektion.
- **Länkmål:** 20 unika nya länkmål, alla svarar 200.
- **Mobil (390 px) och dator (1 280 px):** skärmbilder i `skarmbilder/`. Brödsmulan bryts till två rader på mobil när produktnamnet är långt, men är läsbar. Sidan utan ny länk ser ut som förut.
- **Observationer (bedömning):** (1) För produkter under Varumärken blir den nya länken en varumärkessida (Tunturi, Giant) och inte en ämneskategori. (2) Tre skid-/skridskoprodukter fick länk till `/collections/skidor` eller `/collections/pjaxor`; brödsmulan följer produktens kollektionstillhörighet, så om en skridsko ligger i "skidor" är det ett datafel i katalogen, inte i koden. (3) Strukturerad data (JSON-LD) ändras inte i den här versionen.
- **Inte testat:** presentkort, produkt med tom produkttyp, och Google-sidan efter publicering. Presentkort och tom produkttyp bör kontrolleras manuellt i förhandsgranskningen innan publicering.
- Resultatfil: `brodsmula-efter-kopia.json`. Publicering görs av David; efter publicering körs `snapshot` + `jamfor` mot den publika sidan samt länkmätningen om.

## Version 2 (2026-11-13): förbättrad regel, mätt och testad före publicering
**Bakgrund.** Efter publiceringen av version 1 visade analysen av de 17 sidorna utan ny länk (`brodsmula-17-utan-ny-lank.md`) att koden bara letar under produktens första huvudgren. Version 2 letar i hela menyträdet när version 1 inte ger någon ämneslänk.

**Regel v2 (konservativ).** Behåll v1 när den redan ger en ämneslänk. Annars: sök ämneskollektioner i hela menyn (inte Varumärken, inte menyposter som pekar på en huvudgren, och inte den generiska `tillbehor`), djupast först, därefter menyordning; huvudlänken i brödsmulan blir valets egen huvudgren. Ingen varumärkeslänk läggs till på produkter som hör till en ämneshubb. Strukturerad data (JSON-LD) ändras inte. Filen: `brodsmula-v2-andring.diff` (89 rader; ersätter v1-blocket, 22 rader).

**Mätning över hela katalogen (3 860 produkter, simulerat, `brodsmula-sim/`).** Simuleringen validerades först mot verkligheten: v1 stämmer med de verkliga brödsmulorna på 48 av 48 testsidor och 60 av 60 sidor i v2-urvalet, och temans verkliga Liquid-kod (v1) körd i en Liquid-motor stämmer med simuleringen på 3 860 av 3 860 produkter.
- Med Hybridcykel i menyn får **1 962 produkter (51 %)** en underkollektion i brödsmulan med v1.
- Med v2 får **2 515 produkter (65 %)** en ämneslänk. 847 produkter får en länk där det inte fanns någon, och 628 produkter byter varumärkeslänk (Varumärken › Tunturi) mot ämneslänk (till exempel Konditionsutrustning › Motionscykel); befintliga ämneslänkar rörs inte.
- **1 345 produkter (35 %) saknar fortfarande ämneslänk**: 857 under Varumärken, 297 under Konditionsutrustning, 181 under Cyklar, 10 övriga. De ligger bara i breda kollektioner eller i kollektioner som inte finns i menyn. För 357 av dem finns ett förslag på saknad kollektion (ordstamsmatchning, grov heuristik): `brodsmula-sim/produkter-utan-specifik-kollektion.csv` (alla 3 860 i `produkter.csv`).
- Liquid-koden för v2 (körd i motorn) stämmer med simuleringen på 3 860 av 3 860 produkter. Motorn är inte Shopifys egen, så den verkliga förhandsgranskningen är fortfarande testet som räknas.

**Test i Shopify (före publicering).** Ny opublicerad temakopia "Brödsmula v2 test 2026-11-13" (`gid://shopify/OnlineStoreTheme/196613013770`), duplicerad från det publicerade temat. `sections/main-product.liquid` i kopian återläst: md5 `1fbbb1c3c0d501db49c0e2a4628313ee`, 113 914 byte, exakt den förväntade filen. Publicerat tema oförändrat (md5 `0f376f73…`). Före-bild från publika sidan för 60 produkter: `brodsmula-v2-fore.json` (urval i `brodsmula-v2-testsidor.csv`: 20 får ny länk, 20 byter huvudlänk, 10 oförändrade, 10 utan länk). Kvar: hämta samma 60 sidor ur kopian, `brodsmula_kontroll.py jamfor ... --tillat-hubbbyte`, skärmbilder, samt de manuella kontrollerna. Kräver Davids ok att hämta från förhandsgranskningen av den nya kopian.

### Testresultat v2 2026-11-13 (kopian "Brödsmula v2 test 2026-11-13")
Hämtat med Davids uttryckliga ok (bara v2-kopian, 60 sidor, högst ungefär 1 anrop/s, trots robots.txt). Varje sida bekräftades komma från v2-kopian (`Shopify.theme.id` 196613013770, `role: unpublished`).
- **Jämförelse mot före-bilden (`jamfor --tillat-hubbbyte`): GODKÄND, 0 fel på 60 sidor.** Ingen sida har fått en länk som inte är en kollektion, produktnamnen är kvar, varje sida har en canonical och giltig strukturerad data, antalet h1 och övriga länkar är oförändrade.
- **Verkligt resultat = simulerat resultat på 60 av 60 sidor.** 40 sidor fick ny eller utbytt kollektionslänk (20 + 20 enligt urvalet), 20 sidor oförändrade (10 med och 10 utan ämneslänk).
- **Länkmål:** 30 unika nya länkmål, alla svarar 200.
- **Skärmbilder** (mobil 390 px, dator 1 280 px): `skarmbilder/mobil-v2-*.png`, `dator-v2-*.png`. Brödsmulan bryts till två rader på mobil vid långa produktnamn, men är läsbar.
- **Observation (bedömning):** Brödsmulan följer produktens kollektionstillhörighet. En hjälm "för elcyklar" ligger i Elcykel men inte i Cykelhjälmar, och får därför länken Elcykel; det visar att de saknade medlemskapen (se `produkter-utan-specifik-kollektion.csv`) påverkar hur träffsäker brödsmulan blir.
- **Verktygsrättning under testet:** testverktyget underkände först byte från varumärkeslänk till ämneslänk (förväntat mönster var fel: både huvudlänk och underlänk byts). Regeln rättades och testades (19 tester), och körningen om gav 0 fel.
- **Kvar:** manuella kontroller (presentkort, produkt med tom produkttyp), och att Davids anställde säger att hans kopia är klar innan v2 läggs in där (se nedan).

### Införande i den kopia som ska publiceras (Kopia av Brödsmula test 2026-11-13, `196612718858`)
Den kopian ägs av Davids anställde och redigeras av honom: den rörs inte medan han arbetar (en fil skrivs över i sin helhet). När han meddelar att den är färdig: (1) läs filens kontrollsumma, förväntat `0f376f73be0ef5bcaa820bb4f5923adb` om ingen annan ändrat `main-product.liquid`; (2) är den lika, skriv v2-filen (md5 `1fbbb1c3c0d501db49c0e2a4628313ee`) och återläs; (3) är den ändrad, läs hans fil, lägg in bara v2-blocket ovanpå och verifiera att skillnaden mot hans fil bara är v2-blocket; (4) han publicerar.
