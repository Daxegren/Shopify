# Översikt Shopify/Ecomduct – läge 2026-11-04 kväll

Skriven av samordnaren (grenen `claude/oversikt-samordnare`). Öppna frågor i prioritetsordning ligger i `oppna_fragor.json` (S1–S11 nya, F1–F12 från BEST OF SPORTS). Alla sessioner har bara läst; inget har ändrats i någon butik utom BEST OF SPORTS.

| Butik | Gren | Fas | Klart | Blockerar | Beslut som väntar på David |
|---|---|---|---|---|---|
| BEST OF SPORTS | `claude/zealous-johnson-0ywddr` | Skrivfas | 540 fitnessprodukter skrivna och verifierade; API-väg byggd; elcyklar k_01d klara, k_02b under granskning | Gränsen för användning delas av nio sessioner | F1–F12 (pilot 20, lastgräns, typord, dubbletter, FLUID m.fl.) |
| Alpha Zoo | `claude/alphazoo-byou-onboarding` | Fas 1 klar (publik data) | Profil, tom spärrlista, genomlysning (24 produkter, 62 kategorier), site-audit | Admin, Search Console, GA4, Ads, Ahrefs ej nåbara | S1, S3, S4, S5c, S7, S10 |
| B You Underwear | `claude/byou-onboarding` (+ filer från Alpha Zoo-grenen) | Fas 1 klar (publik data) | 13 produkter, 16 kollektioner; två profiler och två genomlysningar finns | Samma som Alpha Zoo; dubbelarbete | S1, S3, S4, S6 |
| Gorilla Sports | `claude/gorillasports-onboarding` | Fas 1 klar (publik data) | 869 produkter inventerade; profil och spärrlista (inaktiv); dubbla produktposter i strukturerad data | Åtkomst; ton ej beslutad | S1, S3, S4, S8 |
| Workout Brands | `claude/workoutbrands-onboarding` | Fas 1 klar (publik data) | 6 920 produkter, 104 356 varianter; är streetwear, inte träning | Åtkomst; inriktning obekräftad | S1, S3, S4, S9 |
| Happy Parent | `claude/happyparent-onboarding` | Fas 1 klar (publik data) | 581 produkter; B1–B12 föreslagna; bred spärrlista (ca 360 poster) | Åtkomst; CE-dokumentation | S1, S3, S4, S5b |
| HYPR Nutrition | `claude/hyprnutrition-onboarding` | Fas 1 klar (publik data) | 9 produkter, 86 artiklar; regler för tillskott (utkast); alla produkter spärrade | Åtkomst; regulatorisk granskare; fel bolags villkor | S1, S3, S4, S5a |
| Mondido | `claude/mondido-onboarding` | Stoppad | Publik kontroll: betaltjänst, inte butik | Davids besked | S2 |
| To The Moon | `claude/tothemoon-onboarding` | Stoppad | Ingen träff i repot; inget gissat | Davids besked | S2 |

## Observationer
- Alla sex fas 1-sessioner bröt samma gång mot samma fälla: `switch-shop` på den delade Shopify-kopplingen (se `LARDOMAR.md`). Regeln finns nu hos alla.
- Filnamnskrockar mellan grenarna: `beslut-2026-11-04-7.md` finns på fem grenar och på huvudgrenen, `-5` på Alpha Zoo och huvudgrenen (S11).
- Alpha Zoo-grenen ändrade `regler-v1.md` (rubrik till v1.5 och R20/R21) medan BOS-grenen redan har ett eget v1.5-avsnitt. Måste sammanföras i regelboken (uppgift 2).
- Dubbelarbete: B You gjordes av två sessioner; Alpha Zoo-sessionens filer är huvudspår.

## Sammanslagning (2026-11-04 kväll, Davids ja på S11)
Alla åtta butiksgrenar är sammanslagna in i `claude/oversikt-samordnare` med `shopify-sync/scripts/samordna_sammanslagning.sh`; grenarna själva är oförändrade. Ingen pull request, main orörd. Loggfilerna i `docs/` har båda sidors rader. Filer med samma namn: `rapporter/beslut-2026-11-04-7-<butik>.md` (byou, gorillasports, hyprnutrition, mondido, tothemoon, workoutbrands), `beslut-2026-11-04-5-alphazoo.md` och `shopify-sync/scripts/offentlig_inventering-<butik>.py` (gorillasports, workoutbrands; Alpha Zoos version behåller namnet). Kvarstår: två B You-profiler (S6) och att kontrollskriptet stoppar på profiler med TODO i standardblocket (B You, HYPR).

## Mondido och To The Moon (2026-11-04, Davids besked)
Mondido erbjuder betaltjänster till Shopify-butiker; To The Moon är hemsidan för investmentbolaget (veckovisa förfrågningar från entreprenörer som söker investeringar). Ingen av dem är en butik, så fas 1 för butiker är inte aktuell. Raderna Mondido och To The Moon i tabellen ovan ersätts av detta (tabellen skrevs före beskedet). Sessionerna får vila; ingen ny uppgift skickad. Frågan S2 är avklarad.
