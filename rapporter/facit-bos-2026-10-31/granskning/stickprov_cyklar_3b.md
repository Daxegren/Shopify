# Stickprov cyklar 3b (k_skriv_3b.json), 2026-11-03

Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info. Endast läsning.

## Metod
- 10 av 27 produkter lästes live via graphql_query (title, handle, status, tags, seo, descriptionHtml) och jämfördes maskinellt i python (strängjämförelse, tecken för tecken) mot titel, seo_title, meta och html i `vag2_skriv/k_skriv_3b.json`.
- Begränsning: live-svaret fördes över till python-filen för hand (inklistrat, ingen automatisk export finns från verktyget). Den gemensamma svansen (Leverans, retur, garanti, Säljare) klistrades in en gång och lades på alla tio; att svansen är identisk i alla tio live-svar är kontrollerat visuellt, inte maskinellt.
- Urval (index i filen): 7091, 7101, 7114*, 7117*, 7126, 7130*, 7144*, 7145*, 7154*, 7162* (* = rättat utlåtande i k_utlatande_13_15 / 16_17: sju produkter).
- Rättningarnas "efter"-text finns i skrivfilen och "före"-texten är borta för alla rättade fält (kontrollerat maskinellt för alla 13 rättningar på de sju).

## Resultat
| Kontroll | Utfall |
|---|---|
| title, seo_title, meta, html live = skrivfil | Identiska för alla 10 (0 teckenavvikelser) |
| Radbrytning mellan li | Finns både i live och i skrivfil (avsett) |
| seo.title | Satt och olik titeln i alla 10 (ingen null) |
| Status ACTIVE | 10 av 10 |
| Tagg texter-klara | 10 av 10 |
| Längder | Titel 33-64 (max 70), SEO 23-41 (max 43), meta 132-151 (130-155) |
| Kommatecken i titel | Max 2 utöver decimalkomma (7117, 7162 visar 3 tecken pga 27,5) |
| Förbjudna ord, utropstecken, pris, hälsoord | Inga träffar |
| Versal efter kolon | Alla, utom varumärkesnamnet microSHIFT (7144, 7145), avsett varumärkesstavning |
| Stavning | Inga fel funna. "Niagra" (7114) är källans stavning |
| Påhittade fakta mot före-filen | Inga hittade. Alla tal, komponenter och mått går att spåra till vag2k_3b_fore.json |

## Avvikelser mot skrivfilen
Inga (0).

## Observationer (inga avvikelser, för beslut)
1. **7091 Giant Propel Advanced 2 och 7126 Liv EnviLiv Advanced 2:** källan säger bara "Shimano 105" och 24 växlar. 24 växlar (2x12) med Shimano 105 är i praktiken Di2 (elektronisk, batteri); mekanisk 105 är 11-växlad. Texten säger varken mekanisk eller elektronisk och nämner inget batteri, så inget antyds, men utlåtandena (GODKÄND) resonerade inte om det, till skillnad från 7080 som underkändes av samma skäl. Rekommendation: David avgör om de två ska stå kvar eller bekräftas hos leverantören (regeln om elektronik i avsnitt 10).
2. **7162 Liv Tempt 3 XS:** punkten "Dig som söker en cykel som tillverkaren beskriver som designad för kvinnor" bygger på källans mening om hela Liv-sortimentet ("Liv-sortimentet är designat för kvinnor"), inte om just denna modell. Mindre överdrift, ej faktafel.
3. 7117 Kona Coco: punkteringsskydd är borträttat (säkerhetsegenskap), korrekt. 7126 och 7101 har aldrig lagts om i titeln (Racercykel/Mountainbike följer taggar), godtagbart.
