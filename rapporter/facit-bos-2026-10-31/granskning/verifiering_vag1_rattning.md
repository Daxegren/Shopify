# Verifiering våg 1, rättning – BEST OF SPORTS (2026-11-01)

Oberoende kontroll. Bara läsning i Shopify, ingenting skrevs. Butiken kontrollerades först med get-shop-info: BEST OF SPORTS (bestofsports.se).

**Underlag:** `facit-bos-2026-10-31/vag1_skriv/rattade.json` (26 produkter), `shopify-original-2026-11-01/vag1_rattning_fore.json` (status före), `shopify-original-2026-11-01/pilot20-efter.json` (pilot).
**Metod:** title, status, seo{title description} och descriptionHtml hämtades via graphql_query (`nodes`) i fyra batchar om högst 8. Jämförelsen gjordes tecken för tecken med ett skript. Två avvikelser godtogs: radbrytningen som Shopify lägger mellan `<li>`, och SEO-titel null när seo_title i filen är samma som titeln.

## Resultat

- **26 av 26 identiska** med facit i titel, SEO-titel, meta och html.
- **Status:** samma som före för alla 26 (21 ACTIVE, 5 DRAFT: nr 202, 303, 402, 502 och 815). Ingen status har ändrats.
- **Regelkontroll:**
  - Enheter: ml, oz, cm, mm och kg skrivs med gemener överallt. "Ml", "Oz", "Cm", "Mm" och "Kg" förekommer inte.
  - "Vrid-och-lås" finns i titeln på nr 704 (i brödtexten med gemen i "vrid-och-lås-mekanism").
  - "Hammer-löpband" finns på nr 115 och "Gummibelagd" i titeln på nr 815.
  - Titlar: alla har högst 70 tecken. Ingen titel har kolon.
  - SEO-titlar: alla har högst 43 tecken, även där Shopify har null och titeln används.
  - Meta: alla som finns har 130–155 tecken.

## Avvikelser mot facit
Inga.

## Regelbrott som finns i både facit och live
1. **Nr 303 (10472303689994), html, avsnittet Vanliga frågor:** bindestreck i stället för tankstreck i två intervall: "166-178 cm" och "179-190 cm". Bör vara "166–178 cm" och "179–190 cm". "155–165 cm" i samma mening är rätt.
2. **Meta saknas (null) på 7 produkter:** nr 113, 114, 115, 903, 402, 408 och 601. Det stämmer med facit (meta null), men produkterna ligger utanför kravet på 130–155 tecken. Nr 113, 114, 115, 402 och 408 har dessutom bara en mening i brödtexten och inga avsnitt.

## Språkgranskning (26 produkter)
- **Nr 106:** meta "Hjulet väger 1 kg, är i svart och grönt syntetmaterial." Ett "och" saknas: "väger 1 kg och är i …".
- **Nr 107:** meta "Justerbara med kardborrefäste, i grått och svart." är en mening utan verb. Specifikationen "Set: 2 per set" upprepar sig själv.
- **Nr 909:** både meta och första meningen i html lyder "Tunturi massagerulle i kork som väger 680 g." Meningen saknar huvudverb (bara en bisats), till exempel "… är en massagerulle i kork som väger 680 g."
- **Nr 115:** "Silikonspray för Hammer-löpband, 400 ml." och **nr 408:** "Toorx träningsmatta på 180 x 90 x 0,6 cm." Båda är meningar utan verb.
- **Nr 302:** "Hjulet tränar överkropp och bål" säger att hjulet tränar. Bättre: "Med hjulet tränar du överkropp och bål."
- **Nr 315:** "Dig som vill kunna välja en annan vikt, eftersom modellen finns i andra vikter" är cirkulärt och klumpigt. "Finns även i andra vikter" och "Set om 2" upprepar annan text.
- **Nr 414:** två rader heter "Storlek" ("L 30,5 x B 16 x H 12,5 cm" och "14 oz"). Den första bör heta "Mått". "Dig som söker 14 oz" låter konstigt.
- **Nr 502:** i meta står "Tunturi Gymnastikboll" med versal G mitt i meningen. Bör vara "Tunturi gymnastikboll".
- **Nr 601:** ordföljden i "Mobilhållare för Arm Toorx" (titel och SEO-titel) är konstig. "Mobilhållare Toorx för arm" vore naturligare.
- **Nr 702 och 812:** samma text, men 702 skriver "poser" och 812 "positioner". "Poser" är en anglicism, och texterna bör vara enhetliga. "yin yoga" skrivs normalt "yinyoga" på svenska.
- **Nr 704:** titeln "… med Vrid-och-lås" saknar ett substantiv (jämför "vrid-och-lås-mekanism" i texten). Det följer regeln men läses ofullständigt. Specifikationen saknar viktintervall.
- **Nr 307:** meta slutar med "Storlek: En storlek.", vilket säger lite.
- **Nr 810:** "squats" är engelska (alternativet är "knäböj"). Det är godtagbart som träningsjargong.

## Pilotprodukter
**10475621089546 – Vikbart Cykellås AXA Fold 85, 85 cm, Sold Secure Bronze (ACTIVE)**
- Live jämfört med pilot20-efter.json: titel och SEO-titel är lika. Html skiljer sig på en punkt: stavfelet "ställänkar" i filen är rättat till "stållänkar" live.
- Längder: titel 55, meta 137, SEO-titel 65 tecken ("… | Best of Sports"). SEO-titeln är över gränsen 43, om den gäller piloten.
- Språk:
  - "parkerar cykeln en kortare till medellång tid": "under" saknas ("under en kortare till medellång tid").
  - "Hållare med fäste för flaskhållarfästen": "fäste" står två gånger och meningen är klumpig.
  - Fraktraden har "(inom Sverige 179 kr)", vilket våg 1-produkterna saknar. Texterna är alltså inte enhetliga.

**10588446589194 – Kettlebell Tunturi PE 16 kg, PVC Fylld med Sand (ACTIVE)**
- Live jämfört med pilot20-efter.json: titel och SEO-titel är lika. Html skiljer sig på en punkt: "en enkel redskap" i filen är rättat till "ett enkelt redskap" live.
- Längder: titel 47, meta 133, SEO-titel 58 tecken ("… | Best of Sports"). Även den är över 43.
- Språk:
  - FAQ-svaret "Du kan göra samma övningar, den är gjord av PVC med sandfyllning." har ett kommatecken mellan två huvudsatser, och den andra delen svarar inte på frågan.
  - Specifikationsrader blandar fält: "Vikt: 16 kg, färg: Svart" och "Finns i olika vikter, produktkod 14TUSCL183".
  - Meta nämner "styrka, kondition och rörlighet" men FAQ "styrka, koordination, flexibilitet och bålstabilitet". Lite spretigt.
  - Fraktraden har "(inom Sverige 179 kr)", som i AXA-piloten.

## Slutsats
Live stämmer exakt med facit för alla 26 produkter, och ingen status har ändrats. Det som återstår finns redan i facit: bindestrecken i nr 303, sju produkter utan meta och de språkpunkter som listas ovan. Båda pilotprodukterna har fått sina stavfel rättade jämfört med pilot20-efter.json, men deras SEO-titlar är längre än 43 tecken.
