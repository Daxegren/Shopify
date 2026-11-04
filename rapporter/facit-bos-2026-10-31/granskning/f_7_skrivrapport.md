# Skrivrapport f_skriv_7 (Velomarket fitness, 2026-11-04)

Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info före skrivning.

- Produkter i filen: 23 (10158 och 10165 saknas, avvisade). Skrivna: 23. Hoppade över: 0 (alla ACTIVE, ingen hade texter-klara, ingen hade hela posten lika med filen).
- Före-läge sparat i `rapporter/shopify-original-2026-11-04/f_7_fore.json` före första skrivningen. Före: seo.title och seo.description var null på alla 23.
- Kontrollskriptet (`--seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70`, på kopia med standardblock markerat): 0 FEL, 29 VARNINGAR (kända: saknar avsnittet "passar dig som" eftersom rubriken är "Passar för", och långt första stycke på 5 produkter).
- Skrivning: 5 batcher (3 kanarie, därefter 5, 5, 5, 5), högst 5 produkter per anrop, mutationerna utskrivna av `f7work/gen.py` (json.dumps ensure_ascii=True, vägrar osynliga tecken) och inklistrade ordagrant. Inga userErrors. seo skickades alltid med både title och description.
- Återläsning: efter varje batch, högst 4 produkter per fråga, jämförd i python (`f7work/ver.py`) tecken för tecken: titel, seo.title (null = titeln), seo.description, descriptionHtml (inkl. radbrytningar), handle, status och taggar mot före-läget, samt sökning efter osynliga tecken (U+00AD, nollbredd, NBSP). Resultat: 22 av 23 exakt lika. Inget gjordes för hand.
- Enda avvikelsen: 10665231515914 (Crosstrainer Hammer Crossfly BT). Texten "push & turn-kontrollknapp" lagras av Shopify som "push &amp; turn-kontrollknapp" (HTML-normalisering av &). I övrigt identisk; efter ersättning &amp; -> & är texten lika med filen. Omskrivning ger samma resultat, så den gjordes inte. Rekommendation: godta, eller ändra "&" till "och" i skrivfilen om David vill.
- Taggen "På beställning": finns exakt på 13 produkter och just dessa har meningen "Beställningsvaror kan ta upp till en vecka längre"; de 10 övriga saknar både tagg och mening. Kontrollerat maskinellt.
- Taggar: tagsAdd "texter-klara" på alla 23, inga userErrors; återläst, alla har taggen och samtliga tidigare taggar (Velomarket, Gymstick, På beställning m.fl.) finns kvar. Handle och status oförändrade. Pris rördes inte.
- Anmärkning: före-läget hämtades via en fråga vars svar sparades till fil av verktyget, så ingen text skrevs av för hand.
