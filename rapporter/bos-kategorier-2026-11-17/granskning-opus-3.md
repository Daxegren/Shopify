# Tredje granskningen av pilottexterna (2026-11-17): hantlar, cykellås, elcyklar, sparkcykel, tunturi

Oberoende granskare (Opus), endast läsning. Texterna (`pilot_texter.py`, oförändrade sedan 2026-11-12) jämförda med det nya underlaget i `rapporter/bos-kategorier-2026-11-17/underlag/`. Inga rättelser är gjorda än: texterna skrivs om i ett pass när prisjobbet är avslutat (standarden avsnitt 8). Priser ändras inte till rabattpriser.

**Gemensamt:** längder inom gränserna (72–87 ord, SEO 36–42 tecken, meta 145–152). Bara `<p>`, första meningen har verb, inga löften, leveranstid, frakt eller hälsa, leverantörsnamn nämns inte. "Minst N" är för lågt i fyra texter (antalen har ökat) men inte osant. Kontrollskriptet missar att "minst N" ligger under golvvärdet och godkänner "minst 60" i elcyklar bara för att 60 finns i "CGO600". Öppen fråga till David (R8): AXA (38 titlar), ADO och SOKE skrivs med versaler i titlarna.

## Rättelser per text (före → efter)
| Kategori | Fel | Före → efter |
|---|---|---|
| hantlar | Exempelmodell bytt namn | "Hantel ZIPRO HEX 2.5kg, svart" → "Hantel Zipro HEX gummerad 2,5 kg, svart" |
| | Vikter (belägg: "Pro Chrome Hantel 0,5kg", set på 60 kg ligger bland övriga eftersom regeln stoppar "skiv") | "från 1 till 50 kg" → "från 0,5 till 60 kg" (eller 0,5–50 kg om 60 kg-settet inte ska räknas) |
| | Antal (53 produkter, 52 unika) | "minst 40" → "minst 50" |
| cykellås | Antal (63) | "minst/Minst 50" → "60". Märkeslistan utan "bland annat" är nu fullständig (AXA 41, Squire 16, Giant 5, M-Wave 1). Valfritt: byt exemplet Fold Lite 80 |
| elcyklar | Exempelmodell bytt namn | "El-lastcykel AMLADCYKLER Deluxe" → "El-lastcykel Amladcykler Deluxe" |
| | Antal (78) | "minst/Minst 60" → "70". Valfritt: "Ett tiotal" → "Minst tio produkter" (13) |
| sparkcykel | Exempelmodell bytt namn | "Stuntscooter Union Lite S Scooter Svart" → "Stuntscooter Union Lite S, Svart" |
| | Antal (87) | "minst/Minst 50" → "80" |
| tunturi | – | Godkänd i sak (381 produkter, alla typord belagda); bara prisfrågor nedan |

## Beror på prisjobbet (avgörs när rabatten slutar)
| Kategori | Text nu | Nytt underlag | Kommentar |
|---|---|---|---|
| hantlar | cirka 70–14 500 kr | 59–14 489 kr | 71,10 kr = 79 kr minus 10 %; lägsta blir troligen cirka 60–70 |
| cykellås | cirka 90–5 300 kr | 89–4 805,10 kr | Taket = 5 339 kr minus 10 %. 5 339 kr är troligen ett prisfel: samma lås finns som "Köp AXA Fold Lite 80" för 679 kr, nästa dyraste lås 2 969 kr |
| elcyklar | cirka 13 900–104 000 kr | 13 829–103 769 kr | Avrundat 13 800 och 103 800; skillnaden ser inte ut som rabatt, kontrollera igen |
| sparkcykel | cirka 2 200–5 000 kr | 1 412,10–5 049 kr | Golvet 1 412,10 kr = 1 569 kr minus 10 %; barnsparkcyklar från 656 kr ligger på sidan |
| tunturi | cirka 40–50 800 kr | 39–50 679 kr | Taket blir 50 700 |

## Fynd i underlaget och butiken (ingen textfråga)
- Sparkcykel: "Stuntsparkcykel Razor Beast V6 för barn" räknas som huvudprodukt (barnregeln läser bara två första ord); fem barnsparkcyklar (656–2 209 kr) ligger på sidan; titlar på estniska, engelska och med felstavning ("Trikitõukeratas Ethic", "Trikssparkcykel Ethic", "Trick scooter SOKE PRO", "Ethic Pandora Complete Pro Scooter M Blue"); misstänkta tillbehörspriser (griptape 1 419–1 489 kr, klistermärke 1 459 kr, ställ 1 409–1 459 kr).
- Cykellås: "Köp AXA Fold Lite 80" (679 kr) är ett lås men räknas som övrigt; möjliga dubbletter (Resolute C10-150, Resolute 6-60); kollektionen innehåller även handtag, grips, bromsskiva, hantelvikter och fjäderklämmor.
- Hantlar: dubbletttitel "Hantel TUNTURI Platinum Hex Gummibelagd Hantel, 37,5 kg"; 60 kg-settet räknas som övrigt men 50 kg-settet som huvudprodukt.
- Tunturi: kollektionen innehåller akupressurprodukter (utanför utrullningen; texten nämner dem inte).

## Förbättringar av skripten (inte gjorda)
1. Sparkcykelns barnregel ska läsa hela titeln.
2. Hantlarnas regel för "skiv" ska undanta kombinerade set.
3. `kategori_kontroll.py` ska varna när "minst N" ligger under golvvärdet.

**Rekommendation från granskaren:** gör alla rättelser i ett pass när prisjobbet är slut: kör om underlaget, sedan kontrollen, sedan en ny granskning.
