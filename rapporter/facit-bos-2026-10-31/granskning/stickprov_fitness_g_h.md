# Stickprov fitness g_1–g_4 och h_1–h_3, h_7 (BEST OF SPORTS, endast läsning)

Datum 2026-11-04. Butik bekräftad med get-shop-info: BEST OF SPORTS, bestofsports.se. Inget skrevs till Shopify.

## Resultat
42 produkter kontrollerade, **0 avvikelser**. Alla 8 skrivfiler är täckta. Urvalet är 5 till 6 per fil och alla 5 i h_7: 42 av 135 produkter (31 procent). Kravet "minst 5 per fil" är uppfyllt. Per grupp: g 21 av 57 (37 procent), h 21 av 78 (27 procent), alltså över 10 produkter och 20 procent i båda.

Kontroller per produkt:
- `jamfor_live.py <skrivfil> <livefil>` (titel, seo.title, seo.description, descriptionHtml tecken för tecken, osynliga tecken): 0 avvikelser i alla 8 filer.
- Taggen texter-klara finns, status ACTIVE.
- Beställningsmeningen finns exakt på de 11 produkter som har taggen "På beställning" och på inga andra.
- Standardblocket i skrivfilen är identiskt med det kanoniska (b_skriv_24.json) på alla 42.
- Inga förbjudna uttryck ("Vanliga frågor", "Om märket", "Om Tunturi/Hammer/Toorx", "driftsvikt"), inget märke i versaler, inga img, figure, iframe eller video i beskrivningarna.
- Lastgränser: alla förekomster har etiketten "enligt tillverkaren".
- Läst "med blotta ögat": inga påhittade säkerhets- eller hälsopåståenden utöver sådana som står med "enligt tillverkaren" (t.ex. halkfri, halkskydd, skyddar ansiktet).

## Urval
| Fil | Produkt-id (nr) | Skäl |
|---|---|---|
| g_1 | 10376, 10381, 10386, 10412, 10397 | lastgräns "enligt tillverkaren"; 10386, 10412, 10397 På beställning |
| g_2 | 10417, 10430, 10444, 10487, 10488, 10471 | På beställning (10417, 10430, 10444, 10488), ersatt äldre text (10471, 10487), ersatt FAQ och Om märket (10488) |
| g_3 | 10493, 10526, 10511, 10543, 10549 | lastgräns (10493), brutna rader i originalet (10526, 10549) |
| g_4 | 10599, 10612, 10595, 10613, 10615 | 10612 hade trasig live-titel, 10599 och 10595 omskrivna, 10595 och andra hade "Om Tunturi"-block |
| h_1 | 10377, 10382, 10387, 10421, 10432, 10429 | lastgräns; 10432 flaggat av skrivaren (tal i bokstäver), 10429 ersatte 6073 tecken marknadstext, På beställning |
| h_2 | 10437, 10459, 10452, 10463, 10433 | På beställning (10437, 10459), lastgräns |
| h_3 | 10481, 10472, 10489, 10499, 10502 | lastgräns (10481), halk-/effektformuleringar att kontrollera |
| h_7 | 10608, 10610, 10611, 10614, 10616 | alla 5; 10616 På beställning |

(Id i tabellen är nr i skrivfilen, de fullständiga produkt-id:na finns i filerna.)

## Begränsningar (öppet redovisade)
1. **Inklistring:** MCP-svaren går inte att spara till fil från bash. Live-läsningen (graphql nodes, 4 åt gången, 11 anrop) skrevs av mig in i `live_alla.json` med ett python-skript. Ett skrivfel hos mig ger falsk avvikelse, inte falsk överensstämmelse, men jag har inte kunnat bevisa att inklistringen är felfri.
2. **Standardblocket** (avsnittet Leverans, retur och garanti) skrevs in en gång som gemensam konstant i live-filen, med eller utan beställningsmeningen enligt vad live-svaret visade. Jämförelsen mot skrivfilen är därför för blocket inte oberoende för 41 av 42 produkter. Blocket jämfördes tecken för tecken mot det kanoniska blocket i skrivfilerna, och jag läste igenom alla 42 live-block med ögat. Det är inte en maskinell jämförelse av live mot kanoniskt block.
3. Live-filen är sparad i scratchpad (`/tmp/claude-0/-home-user/fbbd95a3-8b18-5096-a6b5-20df3e4eb235/scratchpad/sp/live_alla.json`), inte i repot.
4. **Bildblock och pilotprodukter:** kontrollerat bara att inga img, figure, iframe eller video finns i live-beskrivningarna. Jag kontrollerade inte pilotprodukternas lista eller bildmedia (inga media lästes), och handle/status jämfördes inte mot före-filer (`--fore` användes inte). Handle och status ser oförändrade ut enligt skrivrapporterna, men detta stickprov bevisar det inte.
5. R7, R11 och R12 (typord, första mening, längdgränser, unikhet mot övriga butiken) kontrollerades inte här. Det är bygg- och granskarsteg.
