# Våg 2, utkast 2026-11-17 (prisfria). handle -> (stycken, seo_titel, meta). Länkmeningar (herrcyklar, traningsmaskin) läggs till efter stycken via vag2_tillagg.json.
PRIS = "Öppna en produkt för att se pris, lagerstatus och produktuppgifter."
T = {
'traningsmaskin': (
 ["BEST OF SPORTS säljer träningsmaskiner och hemmagym från bland annat Tunturi, Hammer och Finnlo by Hammer. Här finns minst 5 produkter.",
  "Kategorin omfattar bland annat träningsmaskiner, hemmagym, en latsdragsstation, en träningsstation och sissy squat-bänkar. " + PRIS,
  "Exempel på produkter: Träningsmaskin Tunturi WT85 Leverage Pulley Gym; Latsdragsstation Hammer Multi-Lat Tower; Träningsstation Hammer Bio Force Extreme Sixpack Plus."],
 "Träningsmaskin – Tunturi, Hammer",
 "Köp till exempel träningsmaskin, hemmagym eller latsdragsstation från bland annat Tunturi, Hammer och Finnlo by Hammer. Minst 5 produkter."),
'herrcyklar': (
 ["BEST OF SPORTS säljer herrcyklar och stadscyklar från bland annat Romet, Giant och Tabou. Här finns minst 10 produkter.",
  "Romet har flest produkter. Några produkter anger 27 växlar eller 28 tum i produktnamnet.",
  PRIS,
  "Exempel på produkter: Herrcykel Romet Wagant 7; Herrcykel Tabou Kinetic 1.0, 28 tum; Stadscykel Giant Attend RS 2 GTS, Svart."],
 "Herrcykel – Romet, Giant, Tabou",
 "Köp herrcykel eller stadscykel från bland annat Romet, Giant och Tabou. Här finns minst 10 produkter hos BEST OF SPORTS."),
'hybridcykel': (
 ["BEST OF SPORTS säljer hybridcyklar från Romet och Giant. Här finns minst 25 produkter.",
  "Romet har flest produkter. Flera hybridcyklar anger antal växlar i produktnamnet, till exempel 11, 18 eller 21 växlar. I kategorin finns även andra produkter, bland annat barnstolar, cykelväskor och sparkcyklar.",
  PRIS,
  "Exempel på produkter: Hybridcykel Giant Escape 3 Disc, 700x38c, Metallic Blue; Hybridcykel Romet Wagant 3, 21 Växlar, Blå; Hybridcykel Giant Roam 2, 700c, Svart."],
 "Hybridcykel – Giant och Romet",
 "Köp hybridcykel från Giant och Romet. Här finns minst 25 produkter, bland annat med 11, 18 eller 21 växlar, hos BEST OF SPORTS."),
'traningsbank': (
 ["BEST OF SPORTS säljer träningsbänkar från bland annat Tunturi, Hammer, BH Fitness, Finnlo by Hammer och Christopeit. Här finns minst 30 produkter.",
  "Tunturi har flest produkter. Flera träningsbänkar är hopfällbara eller justerbara enligt produktnamnet, och det finns bland annat en magbänk.",
  PRIS,
  "Exempel på produkter: Träningsbänk Tunturi Centuri UB100 Utility Bench; Träningsbänk Christopeit AB 1000; Träningsbänk Tunturi WB20 Basic Weight Bench."],
 "Träningsbänk – Tunturi, Hammer, BH Fitness",
 "Köp träningsbänk från bland annat Tunturi, Hammer, BH Fitness och Christopeit, till exempel hopfällbar eller justerbar. Minst 30 produkter."),
'grepptraning': (
 ["BEST OF SPORTS säljer redskap för greppträning från bland annat Gymstick, till exempel fingerexpandrar, handtränare, greppstärkare och greppringar. Här finns minst 10 produkter.",
  "Några produkter anger justerbart motstånd eller är justerbara enligt produktnamnet, och kategorin omfattar även ett viktset och ett justerbart handtag. " + PRIS,
  "Exempel på produkter: Fingerexpander Gymstick Active, Set med 2 st; Handtränare Gymstick, Justerbar, med Räknare; Greppstärkare Gymstick Active Power."],
 "Greppträning – Handtränare, fingerexpander",
 "Köp redskap för greppträning från bland annat Gymstick, till exempel handtränare, fingerexpandrar och greppstärkare. Minst 10 produkter."),
'boxning': (
 ["BEST OF SPORTS säljer boxningsutrustning, bland annat boxningshandskar, boxningssäckar och boxningsdockor, från bland annat Tunturi, Toorx, Hammer och Gymstick. Här finns minst 30 produkter.",
  "Tunturi har flest produkter. Boxningshandskar finns i bland annat 10, 12, 14 och 16 oz.",
  PRIS,
  "Exempel på produkter: Boxningshandskar Toorx Leopard, 12 oz, Polyuretan; Boxningssäck Tunturi Classic Boxing Bag 80 cm, inkl. kedja; Boxningsdocka Tunturi Slam Man."],
 "Boxning – Handskar, säckar och dockor",
 "Köp boxningsutrustning, till exempel handskar, säckar och dockor, från bland annat Tunturi, Toorx, Hammer och Gymstick. Minst 30 produkter."),
'racercykel': (
 ["BEST OF SPORTS säljer landsvägscyklar och racercyklar från Giant. Här finns minst 20 produkter.",
  "Flera produkter anger kolfiber eller carbon i produktnamnet, och serier som TCR, Defy, Contend och Propel finns. Kategorin innehåller även andra produkter, bland annat tillbehör som pedaler och pedalblock samt motionscyklar och sparkcyklar.",
  PRIS,
  "Exempel på produkter: Landsvägscykel Giant Contend 1, 700x28c, Rosewood; Landsvägscykel Giant Defy Advanced 2, 700x32c, Abyss Black; Landsvägscykel Giant Propel Advanced 2, 700c, Carbon."],
 "Racercykel – Landsvägscyklar från Giant",
 "Köp racercykel och landsvägscykel från Giant, bland annat serierna TCR, Defy, Contend och Propel. Här finns minst 20 produkter."),
'stankskarmar-cykel': (
 ["BEST OF SPORTS säljer cykelstänkskärmar, bland annat stänkskärmset, framskärmar och bakskärmar, från bland annat Hebie, SKS, Giant och Ass Savers. Här finns minst 40 produkter.",
  "Hebie och SKS har flest produkter. Flera produkter anger hjulstorlek i produktnamnet, till exempel 28 tum eller 26–29 tum.",
  PRIS,
  "Exempel på produkter: Stänkskärmset Hebie Taipan Trekking, 28 tum, Svart; Framskärm SKS Shockblade för 28–29 tum; Bakskärm Giant Speedshield Clip-On."],
 "Stänkskärm cykel – Hebie, SKS, Giant",
 "Köp cykelstänkskärmar, till exempel stänkskärmset, framskärmar och bakskärmar, från bland annat Hebie, SKS, Giant och Ass Savers. Minst 40 produkter."),
'traningsutrustning-for-hemmagym': (
 ["BEST OF SPORTS säljer träningsutrustning för hemmagym från bland annat Tunturi, Toorx, Hammer, BH Fitness och Christopeit. Här finns minst 700 produkter.",
  "Sortimentet omfattar bland annat motionscyklar, löpband, roddmaskiner, träningsbänkar, kettlebells och viktskivor. " + PRIS,
  "Exempel på produkter: Motionscykel Tunturi Signature E60; Träningsbänk Tunturi WB20 Basic Weight Bench; Kettlebell Tunturi Competition, 8 kg."],
 "Träningsutrustning för hemmagym",
 "Köp träningsutrustning för hemmagym, bland annat motionscyklar, löpband, roddmaskiner, träningsbänkar och kettlebells. Minst 700 produkter."),
}
