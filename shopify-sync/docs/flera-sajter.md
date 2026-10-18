# Flera butiker: separat arbete och gemensam analys

Det här dokumentet beskriver hur tillväxtdatan hanteras för alla butiker och sajter, och vilka synergier en gemensam analys kan ge. Det kompletterar `docs/ny-sajt.md` (steg för att lägga till en sajt) och `docs/tillvaxtdata.md` (datakällor och tabeller).

## Principer

| Enhet | Vad den styr | Varför |
|---|---|---|
| **Butik** (en Shopify-butik) | Shopify-data, GA4, Google Ads, Meta, vyerna `growth_daily_<butik>` | Ordrar, besök och annonser hör till butiken, inte till domänen. Gorilla Sports .se och .dk är en butik med två marknader |
| **Domän** (en sajt i `sites.toml`) | Genomlysning (crawl) och Search Console | Varje domän har egen sökbarhet och egna sidor |
| **Bolag** | Gräns för kunddata och för Google Cloud-projekt | Varje bolag är personuppgiftsansvarigt för sina kunder. Se ny-sajt.md om projektval |

**Hur det blir separat:** varje butik har egna tabeller (`…_<butik>`), eget kommando (`site-audit refresh --site <sajt>`), egna vyer och egen rapport. Allt som görs för Gorilla Sports går att göra för en enskild butik utan att de andra berörs.

**Hur det blir gemensamt:** `site-audit growth-sql` genererar vyerna `portfolio_daily` och `portfolio_weekly`, som lägger butikernas dagssummor under varandra: butik, bolag, bransch, dag, marknad, ordrar, omsättning, besök, annonskostnad och nyckeltal. Frågan `sql/analys/portfolio_30d.sql` jämför sedan alla butiker och marknader med varandra.

**Portföljen innehåller bara dagssummor per butik och marknad.** Inga kunduppgifter, ordrar på radnivå eller e-postadresser hamnar där.

## Butikerna

Det här är vad som är känt. Allt markerat "behövs" måste fyllas i innan butiken kan läggas till. Utkast till konfiguration finns i `sites.portfolio.draft.toml`.

| Butik | Domäner | Bransch (gissning, bekräfta) | Finns i `sites.toml` | Behövs |
|---|---|---|---|---|
| Gorilla Sports | gorillasports.se, .dk | träning | ja | Meta- och Google Ads-åtkomst, se `tillvaxtdata.md` |
| Best of Sports | bestofsports.se, .dk, .fi | sport/träning | nej | Shopify-domän, bolag, GA4, annonskonton |
| Workout Brands | workoutbrands.com | träning/varumärken | nej | samma, plus vilka valutor butiken säljer i |
| Mankovsky Gallery | mankovskygallery.com | konst | nej | samma, och eget projekt om bolaget är ett annat |
| Alpha Zoo | alphazoo.se, .dk, .fi | husdjur | nej | samma |
| Happy Parent | happyparent.store | förälder/barn | nej | samma |
| HYPR Nutrition | hyprnutrition.se | kosttillskott | nej | samma. HYPR Sthlm AB är ett annat bolag än Gorilla Sports |
| B You Underwear | byouunderwear.se | underkläder | nej | samma |

**Tre nivåer per butik**, så att varje butik ger värde direkt och byggs ut stegvis:

| Nivå | Innehåll | Vad du behöver göra |
|---|---|---|
| A | Shopify-ordrar | En installationslänk per butik i Shopify Partners och godkänn i butiken (cirka 10 minuter) |
| B | + GA4 och Search Console | Tjänstkontot som läsare i GA4 och som användare i varje Search Console-egendom (cirka 10 minuter per butik) |
| C | + Google Ads och Meta | Åtkomst enligt `tillvaxtdata.md` (30 minuter per butik, mer om en utvecklartoken saknas) |

Redan nivå A och B räcker för en portföljjämförelse av ordrar, besök och andel som köper. Annonserna kan läggas till efteråt.

## Synergier, i den ordning jag bedömer att de är värda att ta

1. **Kontrollgrupp för orsaksanalys.** Gorillas tapp i september har två möjliga förklaringar: något som är butikens eget (annonser, lager, konvertering), eller något som drabbar alla (säsong, Google, konsumentklimat). Vi saknar fjolårsdata för att skilja dem åt. Med fler butiker blir de andra butikerna kontrollgrupp: om träningsbutikerna föll lika mycket är det marknaden, och om de inte föll är det Gorilla. Det är det som `oms_relativt_median` i portföljfrågan mäter. Det här är den enskilt största vinsten och den går att få redan med nivå A och B.
2. **Jämförelse av nyckeltal.** Andel besök som köper, intäkt per annonskrona (MER), snittorder och annonskostnad av omsättning, per butik och marknad. Jämförelser görs främst inom samma bransch. Det pekar ut den butik och det steg som släpar efter, och sätter en rimlig målnivå.
3. **Delade tester.** Mankovsky, Happy Parent och B You har sannolikt för lite trafik för att testa något med säkra resultat på egen hand. Ett annonsbudskap, en erbjudandeform eller en produktsidelayout som visar sig fungera i en större butik kan införas i de små, med en gemensam testlogg i samma format. Det kräver ett gemensamt sätt att logga tester (`site-audit log-change` finns och kan utökas).
4. **Marknadsexpansion.** Best of Sports och Alpha Zoo säljer redan i Sverige, Danmark och Finland. Deras finska siffror (konvertering, snittorder, annonskostnad) är bästa underlaget för om och hur Gorilla Sports ska gå in i Finland.
5. **Samma tekniska fel i flera butiker.** Genomlysningen hittade hos Gorilla en trust badge-app som lägger 284 KB skript på varje sida, ett temasuffix i alla titlar och bristfälligt schema. Butiker som delar tema eller apparna har sannolikt samma fel. En rättning tas fram en gång och används i alla.
6. **Annonsbudgivning mot varandra.** Om flera butiker kan nås av samma sökningar (till exempel Gorilla och Best of Sports på träningsutrustning) kan de bjuda mot varandra i Google och driva upp klickpriset. Det kan kontrolleras när sökordsdata från Google Ads finns för flera butiker. Det är ett av få fall där en gemensam vy direkt sänker kostnad.
7. **Gemensam administration.** En Meta Business Manager och ett Google Ads-hanterarkonto (MCC) per bolag ger färre inloggningar och en enda plats för behörigheter. Det är praktiskt, och det minskar risken att åtkomst glöms bort när någon slutar.
8. **Gemensam kampanjkalender.** Black Friday är 27 november 2026. En kalender över vad varje butik kör, och en jämförelse mot förra året, gör att planeringen kan göras för alla på en gång. Det är det mest tidskritiska skälet att få igång datan snart.
9. **Produkter och leverantörer.** Om butikerna delar leverantörer eller varumärken går det att se vilka produkter som säljer var, jämföra priser och lager, och förhandla gemensamma volymer. Kräver produktnivådata från varje butik.
10. **Kunder över butiker** (korsförsäljning, till exempel från träningsutrustning till kosttillskott). Potentiellt störst, men juridiskt känsligast: butiker som tillhör olika bolag får inte dela kunduppgifter utan rättslig grund och information till kunderna. Jag rekommenderar att vänta och börja med den aggregerade analysen ovan. Frågan ska ses av jurist innan någon kundlista flyttas.

## Gränser för jämförelserna

- **Branscherna skiljer sig.** Konst och underkläder har helt olika konvertering och snittorder. Jämför förändring över tid och kvoter inom bransch, inte råa nivåer mellan branscher.
- **Små butiker ger brus.** Använd fyraveckorsperioder och titta på flera mått. En ensam vecka säger lite.
- **Valutor summeras inte.** SEK, DKK och EUR jämförs med kvoter och förändringar i procent.
- **GA4-historiken skiljer.** Vissa butiker har längre historik än Gorilla (som har data först från mars 2026), vilket kan ge det fjolårsunderlag som saknas.
- **Annonsernas konverteringsvärde är plattformens egen tillskrivning** och överlappar mellan Google och Meta. Shopify-omsättningen är facit.

## Så läggs en butik till

1. Fyll i ett block i `sites.portfolio.draft.toml` (nivå A, B och C efter hand) och flytta det till `sites.toml`.
2. Följ stegen i `ny-sajt.md`. Använd en egen hemlighet för butikens Shopify-token (till exempel `bestofsports-shopify-token`).
3. Lägg butikens domäner som egna sajter med samma `data_key`. Sajten som har `ga4_property_id`, annonskonton och `shopify_dataset` får `growth_views = true`.
4. Hämta historik (`site-audit backfill …`), generera och kör vyerna (`site-audit growth-sql`) och kontrollera siffrorna mot Shopify och annonsplattformarna.
5. Kör portföljfrågan och lägg till butiken i den löpande rapporten.

Först när alla butikens källor hämtas kan vyerna skapas, eftersom BigQuery kräver att tabellerna finns.
