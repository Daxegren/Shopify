# Skrivrapport f_skriv_9 (2026-11-04)

Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info. Skrivfil: vag2_skriv/f_skriv_9.json (23 produkter; 10222 och 10223 avvisade och saknas).

## Före
Alla 23 hade status ACTIVE, ingen hade taggen texter-klara, och ingen titel eller beskrivning var lika skrivfilens. seo.title och seo.description var null på alla. Före-läget finns i rapporter/shopify-original-2026-11-04/f_9_fore.json.
Begränsning: före-filen skrevs av hand från läsningen och inte maskinellt. descriptionHtml för 10211 (10461966860554) saknar Trix-bildblocket mitt i texten (ca 6 000 tecken), vilket står i fältet "not" i filen. Övriga fält och övriga 22 produkter är fullständiga enligt läsningen.

## Kontroll före skrivning
kontrollera_produkttext.py på kopia (html mappad till beskrivning, standardblock markerat, --seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70, källtext = före-läget): 23 produkter, 0 FEL, 23 VARNINGAR (alla varningen om rubriken "Passar för", känd och godtagen).
På beställning-taggen: 11 produkter har den (10201–10203, 10205–10212 utom 10204; dvs 10201, 10202, 10203, 10205, 10206, 10207, 10208, 10209, 10210, 10211, 10212) och alla 11 har leveranstidsmeningen i standardblocket. De 12 utan taggen (10204, 10213–10221, 10224, 10225) har inte meningen. Inga osynliga tecken i skrivfilen.

## Skrivning
productUpdate med title, seo{title, description} och descriptionHtml. Mutationen skrevs ut av skript (json.dumps, ensure_ascii=True) och klistrades in ordagrant. Kanarie: 3 produkter, därefter batcher om 5 (3+5+5+5+5). Inga userErrors. Handle, status och pris rördes inte.

## Återläsning
Alla 23 återlästa (högst 4 åt gången) och jämförda i python mot skrivfilen: status ACTIVE, titel, seo.title (null godtas när den är lika med titeln), seo.description och descriptionHtml tecken för tecken. Resultat: 23 av 23 lika, 0 avvikelser, ingen omskrivning behövdes. Det jämförda svaret klistrades in i python-filer; handles och taggar jämfördes för hand.

## Taggar
tagsAdd "texter-klara" på alla 23, inga fel. Efteråt bekräftat att alla tidigare taggar finns kvar (inklusive Velomarket, Hammer, Toorx, Tunturi, På beställning, Fell) och att handle och status är oförändrade (kontroll för hand mot före-läget).

## Hoppade över
Inga.

## Notering
Texten för 10212 (Platinum Latsdrag/Rodd) bygger på att källan anger två vikter (120 kg viktmagasin och 230 kg); texten anger bara viktmagasinet. Ej en avvikelse mot skrivfilen.
