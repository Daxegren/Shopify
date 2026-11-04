# Stickprov fitness h_skriv_4, h_skriv_5, h_skriv_6 (BEST OF SPORTS)

Datum 2026-11-04. Kontrollant: Sonnet, ENDAST LÄSNING (inget skrevs till Shopify). Butik bekräftad med get-shop-info: BEST OF SPORTS, bestofsports.se.

## Resultat
30 av 65 produkter kontrollerade (10 per fil, 46 procent, över kravet 8 per fil). **0 avvikelser.**

| Kontroll | h_4 (10 av 23) | h_5 (10 av 21) | h_6 (10 av 21) |
|---|---|---|---|
| jamfor_live.py: titel, seo.title, seo.description, descriptionHtml tecken för tecken, handle och status mot före | 0 avvikelser | 0 | 0 |
| Taggen texter-klara finns | 10/10 | 10/10 | 10/10 |
| Beställningsmeningen exakt en gång på "På beställning" och aldrig utan taggen | 3 PB-produkter OK | 2 OK | 5 OK |
| Hela standardblocket maskinellt mot b_skriv_24.json (alla 26 block där är identiska; PB-variant = samma block plus meningen) | 10/10 | 10/10 | 10/10 |
| Förbjudna uttryck, "&", bildblock (img/figure/picture), märket i versaler, "enligt källan" | 0 | 0 | 0 |
| Pilotprodukter (pilot-20-csv) | 0 | 0 | 0 |
| "Anti-Burst" i text (bara kvar i handles, som inte ändras) | 0 | 0 | 0 |
| skrivfil_kontroll.py på hela filerna (23/21/21 produkter) | 0 FEL, 0 varningar | 0 / 0 | 0 / 0 |

## Urval (nr, produkt-id, skäl)
- h_4: 10506 (10472300216586, rättad), 10509 (10472249884938, rättad), **10510** (10472260862218, hade skrivfilens titel men gammal SEO/beskrivning: nu live-lika), **10512** (10430372151562, rättad, lastgräns "enligt tillverkaren"), 10521 (10475386503434, PB, rättad), 10523 (10470943424778, rättad), **10527** (10430370775306, rättad, lastgräns), **10528** (10472265023754, rättad, Anti-Burst struket), 10529 (10472208236810, PB), 10530 (10472261320970, PB).
- h_5: 10531 (10472261288202, PB), 10532 (10480045424906, PB), 10537 (10475983175946, lastgräns), 10540 (10475371233546, rättad), 10568 (10472311128330, rättad), 10569 (10624084115722, rättad), 10572 (10515743441162, rättad), 10533 (10475369791754), 10534 (10472277442826, engelskt typord Balance Trainer), 10536 (10461958144266).
- h_6: 10587 (10471350534410, PB, rättad), **10590** (10472289108234, PB, lastgräns), **10592** (10468731683082, PB, lastgräns), **10597** (10472308539658, PB, rättad), **10598** (10472310931722, PB, gammal SEO ersatt: live-SEO är skrivfilens), 10586 (10472213315850, rättad), 10593 (10471026819338, rättad), 10601 (10411853512970, rättad), 10602 (10472289698058, rättad), 10583 (10472263221514).
Fetstil = produkter som uppdraget pekade ut. Alla "På beställning"-produkter i h_5 (2 av 2) ingår; i h_4 ingår 3 av 3; i h_6 ingår 5 av 5 som finns i filen (10587, 10590, 10592, 10597, 10598).

## Noteringar (inga avvikelser)
- 10587: specraden "Halkfri sida: Trä, PVC och kakel" saknar eget "enligt tillverkaren", medan inledningen och meta har det. Identisk med skrivfilen och högst två förekomster; bedöms inte som avvikelse men kan granskas av Gransk om R5 ska gälla även specrader.
- 10593: ordet "säkerhetsrem" är delnamn på produkten, inte ett säkerhetspåstående.
- 10512 och 10527 har "enligt tillverkaren" två gånger (löptext och lastgräns), vilket är inom gränsen R5.

## Begränsningar (öppet redovisade)
1. Live-svaren hämtades med graphql_query nodes(ids), 2–4 produkter per fråga, och **klistrades in för hand** i JSON-filer (scratchpad: /tmp/claude-0/-home-user/fbbd95a3-8b18-5096-a6b5-20df3e4eb235/scratchpad/live/h{4,5,6}_{a,b,c}.json, sammanslagna till live_h4.json, live_h5.json, live_h6.json). En felöverföring vid inklistringen kan i teorin dölja eller skapa en avvikelse. Det som talar mot det: 30 av 30 matchar skrivfilen tecken för tecken, vilket inte är sannolikt vid slumpmässiga inklistringsfel. Filerna ligger i scratchpad, inte i repot (kontrollantuppdraget tillät bara rapportfilen).
2. Stickprov: 35 av 65 produkter lästes inte. Slutsatsen gäller de 30, inte hela filerna (skrivfil_kontroll.py täckte dock alla 65).
3. Taggarna kontrollerades bara för texter-klara och På beställning; att Velomarket/Gymstick är orörda jämfördes inte mot före-filerna.
4. Skripten kontrollerar inte sakinnehåll mot leverantörens källtext (R1/R3/R5 är G-regler); R5-orden söktes maskinellt men källstödet bedömdes inte.
