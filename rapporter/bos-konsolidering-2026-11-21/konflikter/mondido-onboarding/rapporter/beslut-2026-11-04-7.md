# Beslutsunderlag 2026-11-04 (7): Mondido – vad finns?

## 1. Sammanfattning
Uppdraget var att ta reda på vad Mondido är i det här sammanhanget innan något arbete påbörjas. Repot innehåller inga uppgifter om Mondido, och de tre externa källorna som skulle visa en butik eller domän gick inte att använda i den här sessionen (se Resultat). Det är därför inte bekräftat om Mondido är en Shopify-butik, en betaltjänst eller ett eget bolag. Ingen inventering, butiksprofil eller genomlysning har gjorts, eftersom de bara ska göras för en bekräftad Shopify-butik. Sessionen stannar här och frågar David.

## 2. Resultat
Före och efter: ingen förändring, ingen data ändrad.

| Källa | Utfall |
|---|---|
| Repot (sökning på "Mondido", alla filer utom git-historiken) | 0 träffar. Mondido nämns varken i dokumentationen, i `sites.portfolio.draft.toml` eller i tidigare rapporter |
| Shopify-konto (kontroll av butik) | Kunde inte kontrolleras. Shopify-kopplingen krävde ny inloggning, så ingen butik kunde listas eller verifieras |
| Windsor.ai (anslutna källor) | Bara en Facebook-sida är ansluten ("Gorilla Sports Nordics"). Ingen Search Console, GA4, Google Ads eller Shopify. Ingen Mondido-koppling finns alltså |
| Ahrefs (domänen mondido.com och mondido.se) | Avslogs av tjänsten ("Insufficient plan"). Abonnemanget ger inte tillgång till domändata, så ingen domän kunde bekräftas eller avfärdas |

Kontroll: varje källa anropades en gång; svaren ovan är tjänsternas egna. Slutsatsen är därför "obekräftat", inte "finns inte".

## 3. Beslut som behövs
1. **Vad är Mondido?**
   - Alternativ A: en Shopify-butik. Då behövs att Shopify-kopplingen loggas in på nytt och att butiken väljs; därefter görs fas 1 (inventering, butiksprofil, spärrlista, genomlysning), bara läsning.
   - Alternativ B: betalleverantören eller ett eget bolag/projekt, inte en butik. Då görs ingen fas 1. Jag skriver i stället en kort förteckning över vilka delar av systemet (regelbok, genomlysning av SEO/GEO, textkvalitet) som kan användas för en sådan sajt och vad som skulle behövas (domän, Search Console- och GA4-åtkomst).
   - Rekommendation: svara på frågan först. Jag har inget underlag för att välja åt dig.
   - Risk: om jag gissar fel läggs tid på en butiksprofil för något som inte är en butik.
   - Om inget beslutas: inget mer görs för Mondido.
2. **Om Mondido är en sajt som ska granskas:** vill du att Ahrefs-abonnemanget uppgraderas, eller räcker Search Console och GA4 via Windsor.ai (kräver att de kopplas in)? Rekommendation: Search Console och GA4, eftersom de ger egna data utan extra kostnad. Om inget beslutas används inga externa SEO-data.

## 4. Ändrat
- Nya/ändrade filer: denna rapport, en rad i `shopify-sync/docs/ANDRINGSLOGG.md`, en rad i `shopify-sync/docs/BESLUTSLOGG.md`. Ingen befintlig text ändrades.
- Ändrat i Shopify: **nej**. Inget ändrades heller i teman, Search Console, Analytics eller Google Ads.
- Ingen annan butiks filer eller status rördes.

## 5. Nästa steg
Om David säger A: logga in Shopify igen, verifiera butiken med get-shop-info, kör fas 1 enligt `butiksprofil-bestofsports.json` som mall. Om David säger B: skriv förteckningen över vad som kan återanvändas och stanna igen.

## Tillägg (senare samma dag): publik kontroll av mondido.com
Efter att en annan session bett mig att inte använda Shopify-verktygets butiksbyte (kopplingen delas mellan sessioner) kontrollerades bara publika sidor. Sammanfattningen av sidan är gjord av ett litet automatiskt verktyg och är inte egenkontrollerad.

- **Mondido är en betaltjänst**, "Mondido Payments", en svensk betalpartner som erbjuder lokala betalmetoder (Swish, Klarna, Vipps, Trustly, Apple Pay). Det stämmer med att betalning i GS Coach ska ske via Mondido.
- **Sajten verkar själv ligga på Shopify** (adresser som `/cart`, `/collections`, `/products`, `/blogs` och bildadresser under `/cdn/shop/`) och marknadsför en Shopify-app för betalmetoder.
- Webbsökning på "Mondido" gav inga användbara träffar. Det är inte ett belägg för något.
- Ej kontrollerat: om sajten finns i Davids Shopify-konto (kräver butiksbyte, som inte får göras nu), samt Search Console, GA4 och Ads (inte anslutna i Windsor.ai).

**Slutsats:** Mondido är med stor sannolikhet inte en butik med produkter att skriva texter för, utan en betaltjänst med en marknadsföringssajt. Fas 1 för butiker (inventering, spärrlista, produkttexter) är därför inte aktuell. Beslut 1 i rapporten kvarstår: David anger om Mondido ska granskas som sajt (SEO/GEO), och i så fall hur data kopplas in.
