# Skrivrapport: språkrättning Gymstick del 3 och 4 (2026-11-03)

Butik: BEST OF SPORTS (bestofsports.se), verifierat med get-shop-info. Inget committat.

## Återupptagen körning
Live lästes för alla 24 berörda produkter före skrivning och jämfördes med skrivfilen (nu), skrivfilen i git HEAD~1 (före rättning) och `vag2c_ratt_34_fore.json`.
- Redan rättade live (lika med nya skrivfilen, skrevs inte om): 3165, 3178, 3179, 3180, 3183, 3185, 3188, 3189, 3193, 3194, 3205, 3207, 3212, 3215, 3219 (15 st).
- Identiska med versionen före rättning och därför rättade nu: 3221, 3224, 3233, 3249, 3285, 3290, 3291, 3292, 3294 (9 st). Kanarie 3221, 3224, 3233 först, återläst, därefter 6 st.
- Produkter som skilde sig från båda: inga.
- Före-filen fanns redan och innehåller pre-rättningsläget, så den skrevs inte över. Läget vid start av denna körning ligger i `rapporter/shopify-original-2026-11-02/vag2c_ratt_34_fore_2.json`.

## Före och efter per produkt
Del 3
- 3165 html: "Bollen är 20 cm." -> "Bollen är 20 cm stor."
- 3178 meta och html: "är en svart träningsmatta på 140 x 60 x 1,0 cm" -> "är svart och mäter 140 x 60 x 1,0 cm"
- 3179 meta och html: "är en grå träningsmatta i NBR som mäter 170 x 60 cm och är 1,5 cm tjock" -> "är grå, mäter 170 x 60 cm och är 1,5 cm tjock"; meta "Mattan passar för" -> "Enligt tillverkaren passar mattan för"
- 3180 html: "är ett träningsband för styrka" -> "används för styrka, flexibilitet och dynamisk uppvärmning"
- 3183 meta och html: "är en hantel med sexkantig form" -> "har sexkantig form"; meta "Finns i" -> "Den finns i"
- 3185 html: "är en kettlebell för styrke- och konditionsträning" -> "används för styrke- och konditionsträning"
- 3188 html: "är ett gummigolv på 100 x 100 cm" -> "mäter 100 x 100 cm"
- 3189 meta och html: "är ett svartgrått gummigolv på 100 x 100 cm med tjockleken 0,8 cm" -> "är svartgrått, mäter 100 x 100 cm och är 0,8 cm tjockt"
- 3193 meta och html: "är en hantel med vinylbeläggning" -> "har vinylbeläggning"; "Nybörjare och erfarna" -> "Nybörjare och erfarna utövare"
- 3194 meta och html: "är en hantel med TPU-beläggning" -> "har TPU-beläggning"
- 3205 meta: "är tillverkad av slitstarkt material" -> "är gjord av slitstarkt material"
- 3207 html: "komplettera sin befintliga" -> "komplettera din befintliga"
- 3212 meta: "nybörjare och erfarna." -> "nybörjare och erfarna utövare."
- 3215 meta: "är en träningsyta" -> "är en balanskudde"
- 3219 meta och html: "är en matta på 105 x 105 x 2 cm" -> "mäter 105 x 105 x 2 cm"
- 3221 meta och html: "Träningshandskar från Gymstick i svart-grå färg, i storlekarna" -> "Gymstick träningshandskar finns i svart-grå färg och i storlekarna"; html "träningshandskar i svart-grå färg." -> "träningshandskar finns i svart-grå färg."
- 3224 meta och html: motsvarande ("finns i rosa-svart färg i storlekarna S, M och L"; html "finns i rosa-svart färg.")
Del 4
- 3233 html: "golv och vikterna" -> "golvet och vikterna"
- 3249 html: "yoga och stretching, för alla nivåer" -> "yoga och stretching på alla nivåer"; "Storlekar: Två storlekar" -> "Storlekar: Två"
- 3285 html: "är träningskoner för träning av snabbhet" -> "är koner för träning av snabbhet"
- 3290 meta: "är tillverkad av slitstarkt material" -> "är gjord av slitstarkt material"
- 3291 SEO-titel: "Träningsband Gymstick Vivid, Set med 3" -> "Träningsband Gymstick Vivid, 3 Band"
- 3292 html: "övningar för hela kroppen" -> "övningar över hela kroppen"
- 3294 meta: "är den slagtålig och skyddar väggen mot missade pilar runt standarddarttavlor" -> "är den slagtålig, passar runt standarddarttavlor och skyddar väggen mot missade pilar"

## Lämnat orört
- Stil och noteringar utan fel: 3248 ("set ... Set" i modellnamnet), 3252 ("Motstånd: Olika motståndsnivåer"), 3272 (nästan cirkulär "Fot- och handmassagerulle är en rulle"), 3179 ton, 3224 "crossfit" (källan).
- 3249: "Storlekar: Två" är den kortare varianten. Varianterna heter "65" och "75" utan enhet, så "65 och 75 cm" skrevs inte (enheten är inte bekräftad). Fråga till David om cm ska stå.
- Typord (Krita/Gymtalk, Fitnessboll/Träningsboll) och produktnamn: inget ändrat. 3215 balanskudde är en tolkning som redan var flaggad i utkastet.

## Kontroller
Maskinellt: titel högst 70 tecken och högst 2 kommatecken, SEO-titel högst 43, meta 130-155 eller null, inga dubbletter av titel, SEO-titel eller meta över alla c_skriv_*.json och a_skriv.json (alla 84 poster i del 3 och 4 kontrollerade): inga avvikelser. kontrollera_produkttext.py på kopia (html -> beskrivning, standardblock markerat, --seo-title-max 43 --seo-suffix " – BEST OF SPORTS", källtext = före-filen): 24 produkter, 0 FEL, 26 varningar (24 x avsnittet heter "Passar för", 2 x kort text för 3290 och 3291).
För hand: live läst före skrivning (jämfört med fore-filen och skrivfilen på de ändrade textställena, resten genomläst), och efter skrivning lästes title, handle, status, tags, seo.title, seo.description och descriptionHtml tillbaka för de 9 skrivna och jämfördes tecken för tecken mot skrivfilen: alla lika. De 15 tidigare rättade lästes samma sak före skrivning (live = skrivfilen). Status ACTIVE, handle och taggar (inkl. texter-klara) oförändrade. Jämförelsen av MCP-svar är gjord för hand, inte diffad i bash.
Skrivfilerna c_skriv_resten_3.json och c_skriv_resten_4.json stämmer med live utan ytterligare ändring.
