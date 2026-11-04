# Klassificering av butikssessionernas lärdomar (2026-11-04)

Skapad av samordnaren. Filen fylls bara på. Varje fynd är antingen butiksoberoende (regelbok eller test) eller butiksspecifikt (profil eller regelförslag). Källa: `LARDOMAR.md`, profiler och rapporter på respektive gren.

| Fynd | Butik | Typ | Var det hör hemma | Status |
|---|---|---|---|---|
| `switch-shop` på den delade Shopify-kopplingen bryter andra sessioner | Alpha Zoo, B You (2 sessioner), Gorilla, Workout Brands, Happy Parent, HYPR | Oberoende | R24 i regelboken; kan inte testas av skript. Förslag S12: en rad i CLAUDE.md så att alla sessioner läser den vid start | Regel inlagd; S12 väntar |
| Åtkomst får inte antas; publik katalog saknar status, SEO-fält och översättningar | Alpha Zoo, HYPR, Mondido | Oberoende | R24 | Inlagd |
| Språk: danska/finska/norska/tyska kräver modersmålstalare | Alpha Zoo | Oberoende | R20 (Alpha Zoo-grenens formulering) | Inlagd, S10 väntar på David |
| Märke med egen versalstavning (BYOU) | B You | Oberoende mekanism, butiksspecifikt värde | R21 + test i `skrivfil_kontroll.py`; värdet i B Yous profil | Inlagd och testad |
| Påståendeord i säljande texter (437 av 869) | Gorilla | Oberoende | R22 + varningstest; butiksspecifika ord i `paastaendeord_extra` | Inlagd och testad |
| Barn, tillskott, foder: särskilda regler och granskare | Happy Parent, HYPR, Alpha Zoo | Oberoende princip, butiksspecifika regler | R23; reglerna B1–B12 och tillskottsreglerna stannar som utkast på sina grenar | Inlagd; utkasten väntar på David |
| Inriktningen antogs fel (streetwear, inte träning) | Workout Brands | Oberoende | R25 och fältet `inriktning_bekraftad` i mallprofilen | Inlagd |
| Hårda mellanslag i butikens editor (690 fel) | Gorilla | Butiksspecifikt värde, oberoende test finns | Testet ger redan FEL; om de ska tillåtas beslutar David (S8). Fältet `hardt_mellanslag_i_befintlig_text` i mallen | Väntar på S8 |
| Dubbla produktposter i strukturerad data, saknade alt-texter, H1 | Gorilla, Alpha Zoo, B You, Happy Parent, Workout Brands | Tema/teknik, inte textregel | Hör till genomlysningarnas åtgärdsförslag, inte regelboken | Ingen regel |
| Fel bolags köpvillkor, saknad leverans/retur | HYPR | Butiksspecifikt | HYPR:s genomlysning och S5a | Ingen regel |
| Märkesmodell per vendor (UC Men/Ladies) | Workout Brands | Butiksspecifikt | Workout Brands profil (S9) | Ingen regel |
| Dubbelarbete: två sessioner gjorde B You | Alpha Zoo, B You | Process | Starta en session per butik och kontrollera `oversikt.md` först | Notering |
| Tre sessioner numrerade regelboken v1.5 oberoende | BOS, Alpha Zoo, samordnare | Process | Samordnaren äger versionsnummer; v1.7 ovan | Se LARDOMAR |

## Mallprofilen: vad som saknades
Fältet för bolag, inriktning och `inriktning_bekraftad`, `regelverkskansligt`, åtkomstblock (app, miljövariabler, Allowed domains), dataåtkomst (Search Console, GA4, Ads, Ahrefs), `marken_versaler`, `paastaendeord_extra`, `meta_utfyllnad` (var hårdkodad till BEST OF SPORTS i skriptet), språkfälten, valuta och hårda mellanslag. Mallen: `shopify-sync/config/butiksprofil-MALL.json`.
