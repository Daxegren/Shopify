# Beslutsunderlag 2026-11-04 (7): "To The Moon", första kartläggning

## 1. Sammanfattning
Uppdraget var att ta reda på vad "To The Moon" är och, om det är en Shopify-butik, göra en första genomlysning. Det går inte att fastställa än. Repot innehåller ingen träff på namnet (varken som butik, domän eller projekt), och i `sites.toml` och portföljutkastet finns ingen sådan sajt. Kopplingen till Shopify var bruten i den här sessionen (inloggningen hade gått ut), så butikskontot kunde inte kontrolleras. Windsor.ai visar bara ett Facebook-organiskt konto (Gorilla Sports Nordics), alltså ingen Search Console, GA4 eller Ads för namnet, och Ahrefs svarade "Insufficient plan" på projektlistan. Därför har ingen inventering, butiksprofil eller spärrlista skapats. Jag har inte gissat.

## 2. Resultat
- Sökning i repot efter "to the moon", "to-the-moon" och "tothemoon" (alla skiftlägen): 0 träffar. En bredare sökning på "moon" gav bara träffar i produktdatafiler för Best of Sports (produktnamn), inget som rör en butik eller domän.
- `shopify-sync/sites.toml`, `sites.portfolio.draft.toml` och `docs/flera-sajter.md`: ingen sajt med det namnet. Kända kommande sajter enligt BESLUTSLOGG: Alpha Zoo och B You Underwear.
- Shopify (`get-shop-info`): kunde inte köras, inloggning krävs (se Beslut 1). Ingen butik verifierad.
- Windsor.ai `get_connectors`: ett anslutet konto (Facebook Organic, "Gorilla Sports Nordics"). Ingen koppling för Search Console, GA4, Google Ads eller Merchant.
- Ahrefs: projektlistan nekades (plan saknar behörighet). Ingen domän slogs upp, eftersom en domän inte ska gissas.
- Kontroll: sökningarna kördes mot grenens hela arbetskopia; svaren ovan är direkta verktygssvar.

## 3. Beslut som behövs
1. **Vad är "To The Moon"?**
   - Alternativ: (a) Shopify-butik, (b) varumärke eller domän utan egen butik, (c) projekt eller annat.
   - Rekommendation: David anger typ och, om det finns, domän och butikens `.myshopify.com`-adress.
   - Risk: om jag gissar kan fel butik eller domän läsas.
   - Om inget beslutas: ingenting vidare görs.
2. **Om det är en Shopify-butik: ordna åtkomst.**
   - Alternativ: (a) David loggar in på Shopify-kopplingen i claude.ai och väljer butiken, (b) API-vägen enligt `textutrullning-rutin.md` med token som hemlig variabel i miljön (aldrig i chatten) och butikens adress under Tillåtna domäner.
   - Rekommendation: (a) för en första läsning, (b) vid större körningar.
   - Risk: låg, bara läsning. Om inget beslutas: ingen inventering kan göras.
3. **Källor för genomlysning (Search Console, GA4, Ads).** Behörighet för tjänstkontot enligt `docs/ny-sajt.md` steg 2–3 samt val av Google Cloud-projekt (samma bolag som Gorilla Sports = samma projekt, annars eget). Utan detta blir genomlysningen begränsad till vad som syns publikt.

## 4. Ändrat
- Nya filer: `rapporter/beslut-2026-11-04-7.md` (denna).
- Nya rader: `shopify-sync/docs/ANDRINGSLOGG.md` och `shopify-sync/docs/BESLUTSLOGG.md` (bara tillägg).
- Inget ändrades i Shopify, Search Console, Analytics, Google Ads eller i någon annan butiks filer eller status.

## 5. Nästa steg
Om David anger vad "To The Moon" är och att det är en Shopify-butik: verifiera butiken (`switch-shop` + `get-shop-info`), inventera produkter (bara läsning), skapa `shopify-sync/config/butiksprofil-tothemoon.json` efter mallen för Best of Sports och en tom spärrlista, genomlys SEO, metadata, struktur och GEO med tillgängliga källor och redovisa åtgärdsförslag. Annars: berätta vad som skulle kunna återanvändas och vad som behövs, efter Davids besked.

Delar av systemet som kan återanvändas oavsett typ: butiksprofil och regelbok (`regler-v1.md`), kontroll av skrivfiler (`skrivfil_kontroll.py`), statusfiler, och sajtkonfigurationen i `sites.toml` (en butik = en datanyckel).
