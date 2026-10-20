# Underlag: kategorisidor för crosstrainer, motionscykel och ställbara hantlar (gorillasports.se)

Förslag, inte beslut. Inget är ändrat i Shopify. Allt nedan ska godkännas av David innan någon sida ändras. Datan är Search Console-sökfrågor 2026-07-01 – 2026-10-17 (tabellen `site_audit.gsc_api_url_query_gorillasports_se`), utan anonymiserade sökfrågor.

## Fakta
| Sökord | Sida som rankar | Visningar | Klick | Position |
|---|---|---|---|---|
| crosstrainer (huvudord) | `/collections/crosstrainer-kondition` | 1 791 på sidan; 943 på själva ordet | 0 | 22,5 (ordet: 26,1) |
| crosstrainers, crosstrainer hemma, crosstrainer för hemmet/hemmabruk | samma sida | 272 / 252 / 76 / 74 | 0 | 6,3 / 24,4 / 22,2 / 21,7 |
| motionscykel (huvudord) | `/collections/motionscykel-kondition` | 254 på sidan; 385 på ordet | 0 | 35,0 (ordet: 37,3) |
| motionscykel mot spinningcykel (jämförelser) | blogg `motionscyklar-eller-spinningcyklar-vi-forklarar-skillnaden` | 228 | 12 | 5,8 (jämförelseorden 3–4) |
| spinningcykel (kategori) | `/collections/spinningcykel` | 192 | 0 | 42,4 |
| ställbara hantlar | `/collections/stallbara-hantlar` (även `?page=2`) | 168 på ordet | 0 | 19,9 |

- Sidan Etals föreslog som ny (`/crosstrainer/`) behövs inte: kategorisidan finns och rankar på plats 22. En ny sida skulle konkurrera med den.
- Bloggen om motionscykel mot spinningcykel är den enda sidan i gruppen som får klick (12). Den är den billigaste vägen in till kategorierna.
- Ställbara hantlar har små volymer i verklig data (168 visningar på 90 dagar), mycket mindre än rapportens uppskattning.

## Förslag per sida
**Crosstrainer (`crosstrainer-kondition`)**
1. Titel och H1 med de varianter besökarna skriver: "Crosstrainer för hemmet och gymmet" (ordningen och formuleringen avgörs av sortimentet).
2. Kort intro ovanför produktrutnätet (2–3 meningar som direkt svarar vem en crosstrainer passar). Ca 300–500 ord köpguide under rutnätet: val efter motstånd och svänghjul, stegläng, högsta användarvikt, ljudnivå och utrymme, samt jämförelse med löpband och motionscykel. Fakta om produkterna hämtas ur sortimentet (inga påståenden som inte kan styrkas).
3. Fyra till fem riktiga frågor med korta svar (till exempel hemma eller på gym). Räkna inte med utdrag i sökresultatet; syftet är besökaren.
4. Interna länkar med ankartexten "crosstrainer" från de bloggar som redan nämner den: `hur-du-bor-trana-for-att-branna-fett`, `skillnaden-mellan-olika-lopband`, `trana-kondition-hemifran`.
5. Kontrollera varför "crosstrainers" ligger på plats 6,3 utan klick (vilken sida och vilket resultat).

**Motionscykel (`motionscykel-kondition` och `spinningcykel`)**
1. Lägg tydliga länkar från bloggen som redan rankar (`motionscyklar-eller-spinningcyklar-vi-forklarar-skillnaden`) till båda kategorierna, högt upp och sist i texten. Kontrollera först om länkar redan finns.
2. Ge de två kategorierna olika roller i texten (motionscykel för hemmaträning och lätt kondition, spinningcykel för intensiv träning) och länka dem till varandra, så att de inte konkurrerar om samma sökord.
3. Realistisk förväntan: huvudordet "motionscykel" ligger på plats 35 mot stora återförsäljare. Textändringar räcker troligen inte för topp 10 på det ordet; jämförelseorden där ni redan står på 3–4 är det som går att utnyttja.

**Ställbara hantlar (`stallbara-hantlar`)**
1. Kort intro och en köpguide (viktintervall, låsmekanism, fäste för skivstångsplattor om det finns). Gör ändringen först om crosstrainer och motionscykel gett effekt, eftersom volymen är liten.
2. Kontrollera att `?page=2` inte indexeras som egen sida (visas i Search Console på plats 16,8).

## Mätning
Logga varje ändring i testloggen (`site-audit test add`) med startdatum, sida och hypotes. Måttet klick och visningar per sida i Search Console utvärderas efter 28 dagar mot övriga kategorisidor. Måttet per sida (`gsc_clicks`) är inte byggt än.

## Fråga till David
Vilka av förslagen får jag förbereda som färdig text (titlar, introtext, köpguide) att läsa igenom innan något läggs i Shopify? Rekommendation: crosstrainer först och bloggens länkar till motionscykelkategorierna, eftersom de ger mest per insats.
