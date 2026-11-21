# Beslutsunderlag 2026-11-04 (sjunde passet: onboarding WORKOUT BRANDS, fas 1)

## 1. Sammanfattning
Jag påbörjade fas 1 för WORKOUT BRANDS, men Shopify-verktyget krävde ny inloggning, så butiken är inte verifierad och inventeringen bygger på butikens offentliga produktdata. Butiken visade sig vara streetwear och mode (Urban Classics, Mister Tee, Brandit), inte träningsutrustning som utkastet antog. Jag skapade en butiksprofil och en spärrlista som utkast samt en genomlysningsrapport med 13 rangordnade fynd. Search Console, GA4 och Google Ads är inte anslutna i Windsor, och Ahrefs gick inte att läsa. Inget ändrades i Shopify.

## 2. Resultat
- **Före:** ingen profil, ingen inventering. **Efter:** 6 920 publicerade produkter inventerade, 104 356 varianter, alla 66 514 bilder saknar alt-text, 145 titlar är dubbletter (311 produkter), 127 titlar slutar på en enskild storlek.
- **Kontroll:** produktantalet kommer från publika sidor (`products.json`, 28 sidor). Siffrorna är inte jämförda med Shopify-admin och omfattar inte utkast eller arkiverade produkter. Bara fyra sidor genomlystes.

## 3. Beslut som behövs
- **Inloggning Shopify-verktyget:** logga in igen och bekräfta att butiken är workoutbrands.com. Rekommendation: ja. Risk: ingen. Utan: ingen verifierad inventering, inga marknader/valutor/kollektioner/SEO-täckning.
- **Butikens inriktning:** bekräfta streetwear/mode (profil och regler anpassas). Rekommendation: ja. Utan: profilen förblir utkast.
- **Dataåtkomst:** koppla Search Console, GA4 och Google Ads (Windsor eller BigQuery enligt ny-sajt.md) och bekräfta Ahrefs-plan. Rekommendation: ja. Utan: ingen analys av sökluckor eller GEO med data.
- **`utanfor_tills_vidare`:** godkänn förslagen i profilen (Out of stock, outlet, barn, titlar med enskild variant, dubbletter, solglasögon, mobilskal). Rekommendation: ja. Utan: fas 2 startar inte.
- **Märkesmodell:** hur vendor ska användas (märkeslinjer som UC Men/UC Ladies samma märke Urban Classics?). Rekommendation: ett märke per vendor. Utan: R8 går inte att tillämpa.
- **Åtgärdsförslag:** godkänn eller avstå från fynd 1–13 i `rapporter/workoutbrands-2026-11-04/genomlysning.md`. Rekommendation: börja med alt-texter (1) och variantrensade titlar (2).

## 4. Ändrat
- **Shopify: nej.** Ingenting ändrades i Shopify, tema, Search Console, Analytics eller Google Ads.
- **Filer (nya):** `shopify-sync/config/butiksprofil-workoutbrands.json`, `shopify-sync/config/sparrlista-workoutbrands.json` (utkast, aktiv=false), `shopify-sync/scripts/offentlig_inventering.py`, `rapporter/workoutbrands-2026-11-04/` (genomlysning, sammanställning, sitemap-index), denna fil, rader i ändringsloggen och beslutsloggen. Rådatan (124 MB) committades inte.

## 5. Nästa steg
Om du säger ja till inloggning och dataåtkomst: jag verifierar butiken, inventerar via Shopify (status, marknader, kollektioner, SEO-täckning), kompletterar genomlysningen med Search Console, GA4 och Ads, och uppdaterar profil och rapport. Fas 2 startar när du godkänt profil, spärrar och åtgärder.
