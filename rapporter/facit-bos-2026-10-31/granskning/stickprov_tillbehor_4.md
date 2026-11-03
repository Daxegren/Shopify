# Stickprov tillbehör grupp 4 (b_skriv_4.json), 2026-11-03

Skrivskyddad kontroll. Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info. Inget skrevs.

## Urval (10 av 34)
- 8042, 8044: rättade efter att metan tappats; seo_title lika med titel, fil har meta.
- 8015, 8035, 8038, 8041: seo_title lika med titel, ingen meta i filen.
- 8005, 8019, 8029, 8047: rättade utlåtanden i b_utlatande_20_21.json (RÄTTA), har meta.
- Avvikelse mot uppdraget: filen har bara två produkter (8042, 8044) där seo_title är lika med titeln och meta finns. Fyra sådana finns inte. Fyra med seo_title lika med titeln utan meta ingår därför.

## Resultat: 0 avvikelser
Jämförelse i python, tecken för tecken, live mot skrivfilen:
- Titel: lika i alla 10.
- SEO-titel: live null där filen har seo_title lika med titeln (8042, 8044, 8015, 8035, 8038, 8041). Övriga fyra lika med filen.
- seo.description: lika med filens meta i de sex med meta (8042 146 tecken, 8044 148, 8005 154, 8019 141, 8029 137, 8047 149). Null live där filens meta är null (8015, 8035, 8038, 8041).
- descriptionHtml: identisk med filens html, inklusive radbrytning mellan li. Standardblocket är lika i alla. 8044 har meningen om längre leveranstid för beställningsvaror (tagg "På beställning").
- Status ACTIVE och taggen texter-klara finns på alla 10.

## Fakta mot före-filen (vag2b_4_fore_skriv34.json)
Inga påhittade uppgifter. Alla tal och egenskaper finns i källan: 6 mm och styv mejsel (8005), 26–27,5 tum och plast (8019), 28/37-609/642 och Schrader (8029), 5 m, 2–3 par, 250 km "enligt tillverkaren" och +5 till −20 °C (8042), 10 bar, 144 psi, 900 mm, 650 mm och stålrör (8044), T-format handtag och monteringsram (8047).
Rättningarna är på plats live: "ta bort" i stället för "rengöra" i 8005, "Mått: 6 mm", och "Rengör först skidans sidor" utan "styrzonen".
Medvetet utelämnat och ok: leverantörens varumärkestext ("Grundat 1972", "världens ledande") i 8047, maxtryck 5 bar i 8047 (källan är oklar), "borrdäck 355 mm" i 8038, "För 28 mm breda däck" i 8029.

## Formatregler
- Titel högst 70 tecken och högst 2 kommatecken: ok.
- SEO-titel högst 43 tecken (längst 38): ok.
- Meta 130–155 tecken (137–154): ok.
- Stor bokstav efter kolon, stor bokstav på beskrivande ord i titlarna, enheter med liten bokstav: ok.
- Stavning: inga fel funna. Inga utropstecken, superlativ, priser eller hälsopåståenden.

## Begränsning
Standardblocket (Leverans, retur och garanti) jämfördes mot en konstant som jag skrev in från live-svaret. Att blocket är lika i alla 10 live-svar är kontrollerat med ögat. Resten är maskinjämfört.
