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
