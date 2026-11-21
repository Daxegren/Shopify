# Granskning k_53a (2 utkast, 0 avvisade), Opus, 2026-11-17

Källa: live-läsning 2026-11-17 (`rapporter/shopify-original-2026-11-17/k_53a_kalla_live_granskning.json`), butikens titlar (`rapporter/inventering-bos-2026-11-17/alla_produkter.json`) och Giants egna produktsidor. JSON-utlåtandet finns i `vag2_skriv/k_utlatande_53a.json`. Varje ändring (före → efter) är kontrollerad i python: texten som ändras finns exakt en gång i sitt fält. Ingenting har ändrats i Shopify.

**Resultat:** 0 GODKÄND, 2 RÄTTA, 0 UNDERKÄND. Avvisningsfilen är tom, vilket är rätt.

| nr | Produkt | Dom | Kort skäl |
|---|---|---|---|
| 53001 | Giant Stratus Comp 2.5, svart (190000255) | RÄTTA | Typordet "Styrtejp" byts till "Handtagstejp" i titel, SEO-titel, meta och text (sju ställen), så att produkten heter som de sex skrivna syskonen. Fakta stämmer med Giants sida. |
| 53002 | Giant Pinner Comp, lila (230000105) | RÄTTA | "Varje pedal har 9 formgjutna stift" blir "Varje sida har 9 formgjutna stift". Giant anger 9 stift per sida, och en pedal har två sidor. Övriga fakta gäller Pinner Comp, inte Elite. |

## 53001 Stratus Comp 2.5
- Giants sida (https://www.giant-bicycles.com/int/stratus-comp-2dot5-bar-tape-2024) gäller exakt modellen: 70 g för paret, 2,5 mm, EVA, självhäftande baksida, ändpluggar och PU-avslutningstejp ingår. Svart har artikelnummer 190000255 (bildfilen). EAN är variantens streckkod i butiken.
- Ett påstående har "enligt tillverkaren": vibrationsdämpning, som Giant skriver ordagrant. Grepp och komfort är rätt utelämnade.
- **Typordet.** Davids fråga (beslut-2026-11-17-6, punkt 1) löd "rätta titeln till handtagstejp", men rekommendationsraden under den skrev "Styrtejp". Hans ja binder därför inte entydigt ordet Styrtejp, och syftet var att rätta produkttypen. Butiken har sex skrivna handtagstejper som alla heter "Handtagstejp", bland dem samma familj (Stratus 2.0 och Stratus Pro 2.0). "Styrtejp" finns inte bland de godkända typorden. Enligt R7 ska produkten därför heta "Handtagstejp". Titel och SEO-titel blir 42 tecken, och metan 134 tecken. Handle ändras inte.

## 53002 Pinner Comp lila
- Butikens källtext (som beskriver Pinner Elite och anger 380 g) är rätt nog inte använd. Giants sida (https://www.giant-bicycles.com/int/pinner-comp-flat-pedals-2022?partnumber=230000105) anger kropp av nylonkomposit, axel av Cr-Mo-stål, förseglade lager, 9 stift per sida och konkav form. Mått 117 x 110 mm, stödyta 112 x 105 mm och vikt 350 g. Lila är artikelnummer 230000105 (bildfilen).
- Maxvikt saknas, därför "Ej känd" enligt v1.10. Texten har inga hållbarhetsord ("durable" och "strong" är utelämnade) och ingen "enligt tillverkaren".
- "Mountainbike" godtas: Giant vänder sig till trail- och enduroåkare, och det skrivna syskonet heter Pinner Comp MTB.
- Titel, SEO-titel och meta krockar inte med Pinner Comp Röd, Pinner Comp MTB eller Pinner Elite Lila.
- Avvikelsen att handle slutar på -230000107 medan SKU är 230000105 noteras bara. Handle ändras aldrig.

## Beslut för David
- **Typord för 53001.** Alternativ A (rekommenderas): "Handtagstejp", som de sex skrivna syskonen. Alternativ B: "Styrtejp", som det stod i rekommendationen. Då stryks rättningen, och de två typorden blandas i butiken. Om inget beslutas gäller A.
