# Best of Sports: första analysen (2026-10-23)

Underlag: Search Console (API, bestofsports.se, nov 2025 till 19 okt 2026), GA4 (bestofsports.se, 23 sep till 22 okt), Google Ads (28 dagar), Merchant Center (ögonblicksbild 23 okt) och Shopify-ordrar (60 dagar, 17 sep till 19 okt). Danmark och Finland har ännu ingen historik (Search Console och GA4 sattes upp 22 okt). Inget i Shopify har ändrats.

## 1. Det viktigaste
1. **Butiken har få ordrar eftersom trafiken är liten och inget av den köper.** På .se kom 834 besök på 30 dagar och 0 köp i GA4. Shopify bekräftar: en enda SEK-order (17 sep) och inga därefter. Med 1 % konvertering hade 834 besök gett ungefär 8 ordrar.
2. **Hälften av trafiken är betald** (441 av 834 besök) och den betalda trafiken har gett 0 försäljning. Shopping-kampanjen "Rude: Shopping >1000kr" kostade 2 588 SEK på 28 dagar för 424 klick (6,1 kr per klick), 0 konverteringar. 54 % av kostnaden går till två barncyklar (LIV Tempt 24: 974 kr, ROMET Rambler 20: 414 kr), också utan försäljning.
3. **Synligheten i Google är låg men förbättras.** Snittposition 54 (dec 2025) till 31 (okt 2026), klick från 44 till ca 170 per månad. Visningarna ligger stilla på 18–22 tusen per månad.
4. **Kategorisidorna är största outnyttjade ytan.** De har 35 347 visningar på 90 dagar (62 % av alla) men bara 99 klick (0,28 % klickfrekvens) och snittposition 24. Produktsidor: 2,68 % klickfrekvens på position 11.
5. **Merchant Center är i huvudsak friskt** (735 av 894 produkter utan problem), men 73 saknar enhetspris, 69 har för små bilder och 7 är avvisade, varav en markerad som "Guns and Parts".

## 2. Siffror
| Mått | Värde |
|---|---|
| Klick i Google per månad (SE) | 44 (dec 2025) till ca 170 (aug–sep 2026) |
| Visningar per månad | 18–22 tusen |
| Snittposition | 54 till 31 |
| Besök (GA4, 30 dagar) | Betald sök 441, organisk sök 203, direkt 159, organisk shopping 18, övrigt 13 |
| Köp (GA4, 30 dagar) | 0 |
| Shopify-ordrar (17 sep–19 okt) | 6 (SEK 1, DKK 1, EUR 4), totalt ca 9 200 kr i butiksvalutan |
| Google Ads (28 dagar) | 2 588 kr, 83 769 visningar, 424 klick, 0 konverteringar |
| Merchant | 735 utan problem, 73 saknar enhetspris, 69 små bilder, 7 avvisade |

Sidtyper i Google (90 dagar, SE): produkt 2 206 sidor, 290 klick; kategori 531 sidor, 99 klick; blogg 208 sidor, 92 klick; startsida 23 klick.

## 3. Vad datan inte kan svara på
- **Varför köper ingen?** Kan bero på pris, frakt, förtroende, betalning eller att trafiken har låg köpavsikt. Det syns inte i datan utan i själva köpflödet.
- **Om annonsernas konverteringsmätning fungerar.** GA4 och Shopify visar båda 0 försäljning på .se, så det är troligen inte ett mätfel, men det är bara fem veckor och 424 klick. Vid 0,5 % konvertering är 0 köp på 424 klick inte ovanligt (cirka 12 % chans). Stickprovet är för litet för att döma enskilda produkter.
- **De fem ordrarna i EUR, DKK och SEK.** Ordrarna i EUR och DKK finns inte i GA4, som saknar trafik för .dk och .fi före 22 okt.
- **Danmark och Finland.** Ingen historik. Mätning startar från 22 okt.
- **Direkttrafiken (159 besök)** kan innehålla egna besök och tester.

## 4. Förslag, i prioritetsordning
Inget genomförs utan ditt ja, och det som rör Shopify, Google Ads eller Merchant Center beslutar du om.

1. **Gå igenom köpflödet på .se som kund** (mobil): pris, frakt, betalning, förtroendesignaler. Lägg en testorder om det går. Ingen kod behövs. Skälet är att 0 av 834 besök köper och att inget i datan förklarar varför.
2. **Prata med Rude om Shopping-kampanjen:** hur konverteringar mäts, varför barncyklarna får 54 % av kostnaden, och om priströskeln ">1000kr" är rätt. Kampanjen är inte vår; vi ändrar den inte.
3. **Merchant Center:** rätta de 7 avvisade (kontrollera särskilt "Guns and Parts"), de 73 utan enhetspris och de 69 små bilderna. Produkttitlar som slutar på "Default Title" (till exempel "Cykel GIANT Talon 3 (2022) 27.5" Amber Glow Default Title") bör rättas i flödet eller i Shopify.
4. **Kategorisidorna:** arbeta med de som har flest visningar och sämst position (pre-workout, motionscykel, träningsbänk, cyklar, rodd). Samma metod som för Gorilla: tydligare text, interna länkar, rätt rubriker. Mät med `gsc_clicks` mot övriga kategorisidor.
5. **Danmark och Finland:** verifiera GA4-taggen per domän i realtidsvyn, och se till att Search Console-exporten fyller på.

## 5. Nästa mätning
Om en vecka: samma sju frågor (`sql/analys/bos/`) körs igen, då med GA4 för alla tre domäner och mer underlag. Effekten av ändringar mäts med klick och visningar per sida, eftersom ordrarna är för få för att mäta på.
