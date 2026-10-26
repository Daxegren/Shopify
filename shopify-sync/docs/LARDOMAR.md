# Lärdomar från arbetet

Syftet är att samma fel inte upprepas i nya arbetspass. Filen fylls bara på: nya poster läggs överst, gamla ändras inte. Läs den innan du rekommenderar en ändring i en butik, ett tema eller en datamodell.

## Hur en post skrivs
Datum, vad som gick fel eller upptäcktes, och regeln som följer av det.

---

### 2026-10-26: Föreslå inget utan en genomgång av det som redan finns
- **Vad hände:** jag föreslog "fem nya kontroller" i genomlysningen, varav en (brödsmulor på kategorisidor) redan fanns som `breadcrumb_schema_missing`. Jag hade inte gått igenom genomlysningens ca 150 kontroller eller läst de senaste fynden per sajt innan jag föreslog. Flera av dagens förslag byggde dessutom på ett urval på 60 sidor och på några temafiler, inte på hela temat eller en genomlysning av hela sajten.
- **Regel:** före varje förslag på en ändring, en ny kontroll eller en åtgärd: (1) lista vad som redan finns (`scripts/audit_tackning.py`, `git grep` i kontrollerna, `standardtester.md`), (2) läs de senaste fynden per sajt för ämnet, (3) läs de berörda filerna i sin helhet (hela temafiler, inte bara de rader som verkar relevanta), (4) skriv i förslaget vad som är genomgånget och vad som inte är det, och rekommendera inte en åtgärd som "ja" innan helheten är känd. David vill inte ha förslag utan att helheten är känd.


### 2026-10-26: Rekommendera inte en ändring i kod någon annan skrivit utan att veta avsikten och dagens effekt
- **Vad hände:** jag föreslog att ta bort canonical-blocket i BOS `theme.liquid` och byta `shop.url` mot `request.origin` i breadcrumbs och Organization, innan jag hade kontrollerat varför blocket fanns, vad Google gör i dag och om `shop.url` i Organization var ett fel. Organization-URL på varumärkets huvuddomän är normalt och korrekt, och adress och språk i Organization kan vara företagets, inte marknadens.
- **Regel:** innan en ändring föreslås: (1) ta reda på avsikten (fråga David, läs loggen), (2) mät dagens effekt (till exempel vilken canonical Google valt), (3) skilj det som är bevisat från det som är en hypotes och säg det, (4) testa på en kopia av temat före publicering.

### 2026-10-26: Kontrollera att ett mått mäter det det påstås mäta, innan det presenteras som fynd
- **Vad hände:** i onsite-kontrollen gav FAQ-måttet 100 % (räknade alla `<details>`), alt-textmåttet 67,8–88,9 % (räknade dekorativa SVG-ikoner), sidnumrering flaggades som felaktig canonical, och två canonical-taggar upptäcktes inte alls eftersom skriptet bara läste den sista.
- **Regel:** testa nya mått mot ett känt fall och granska exempel innan siffran används. Läs exempelsidor, inte bara andelar.

### 2026-10-26: Skriv inte "tyder på" om orsaken inte är uppdelad
- **Vad hände:** jag skrev att hoppet vid fraktgränsen 800 kr "tyder på att kunder fyller på". Uppdelningen visade att 108 av 165 ordrar var enkelradsordrar där produktens eget pris låg där. Påfyllning var en mindre del.
- **Regel:** dela upp materialet innan en orsak antyds, och rätta öppet när uppdelningen visar något annat.

### 2026-10-25: Kontrollera aggregeringar mot totalsumman
- **Vad hände:** ett SQL-resultat för Gravity Pro 2 byggde på `GROUP BY` med NULL-nyckel och `ANY_VALUE(title)`, vilket gav ett felaktigt belopp som David vidarebefordrade till en extern part.
- **Regel:** summera varje uppdelning och jämför mot totalen, kontrollera NULL-grupper och namnge antaganden innan en siffra lämnas ut.

### Fakta om uppsättningen (David har bekräftat)
- **Best of Sports:** tre separata domäner med eget språk: bestofsports.se (svenska), bestofsports.dk (danska), bestofsports.fi (finska, med svenska under /sv/). **.fi och .dk ska ranka självständigt på finska och danska.** Bekräftat av David 2026-10-26.
- **`shop.url` är alltid butikens primärdomän,** även på de andra domänerna. För marknadsspecifika adresser (canonical, brödsmulor, produktens `url`) används `request.origin`. Organization-schemat får peka på varumärkets huvuddomän.
- **Redirecttabellen är gemensam** för alla domäner i butiken; handtag är översatta per språk.
- **Köp av hälsopåståenden:** EU-reglerna (1924/2006, 432/2012) gäller även försiktiga formuleringar. Se tidigare BOS-arbete.
