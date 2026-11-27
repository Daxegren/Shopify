# Förslag: ta bort barnjackor och tröjor ur två vinterjackskollektioner (Workout Brands), 2026-11-27

Ej genomfört. Väntar på Davids ja.

## Problem
Kollektionerna styrs av taggar: `vinterjacka-kvinna` = taggarna `vinterjacka` OCH `Women` (46 produkter); `vinterjacka-man-och-kvinna` = taggen `vinterjacka` (124). Sex produkter bär taggen `vinterjacka` men är inte vuxenjackor:

| Produkt | Typ | Status | Lager | I kollektion |
|---|---|---|---|---|
| UC Sweat Parka | tröja (Hoodie) | aktiv | 17 773 | kvinna + herr&dam |
| Ladies Sweat Parka | tröja (Hoodie) | aktiv | 3 874 | kvinna + herr&dam |
| UC Girls Sweat Parka | barntröja | aktiv | 61 | herr&dam |
| UC Boys Basic Bubble Jacket | barnjacka | aktiv | 325 | herr&dam |
| B Kids BW Parka | barnjacka | aktiv | 425 | herr&dam |
| UC Boys Shiny Puffer Jacket With Hood | barnjacka | utkast | 1 274 | herr&dam (syns inte) |

Kontroll: sökningen "taggen vinterjacka och (kids, Hoodie, BARN, sweatshirt)" ger exakt dessa sex, inga fler.

## Alternativ
**A. Utesluta på kollektionsnivå (rekommenderas).** Lägg till uteslutningsvillkor på de två kollektionerna: ta bort produkter med taggen `kids` eller `Hoodie`. Produkterna, deras taggar och priser rörs inte. Följd: dam 46 → 44, herr&dam 124 → 118 (varav barnjackorna och tröjorna försvinner därifrån); nya produkter med dessa taggar hålls också utanför. Ångra: ta bort uteslutningsvillkoren.
**B. Ta bort taggen `vinterjacka` från de sex produkterna.** Rör produkterna, och fyra av dem bär prisjobbstaggen `price-change-job-active` (Black Friday). Kan också påverka andra kollektioner som använder taggen. Rekommenderas inte nu.
**C. Låta det vara och flytta barnjackorna till egna kollektioner senare.** Ingen risk, men kunderna ser fortfarande tröjor och barnjackor under "Vinterjacka".

## Genomförande för A (efter ja)
1. Före-fil: nuvarande regler och produktantal (finns i denna fil: dam 46, herr&dam 124; reglerna ovan).
2. Kanarie: `vinterjacka-kvinna` (källa 13766295880): uteslutning matchning ANY, taggvillkor `kids` och `Hoodie`. Återläs: 44 produkter, ingen av de två tröjorna kvar.
3. Därefter `vinterjacka-man-och-kvinna` (källa 13766328648): samma uteslutning. Återläs: 118 produkter, inga av de sex kvar.
4. Beskrivningstexterna ändras inte; texten för herr&dam stämmer bättre efteråt.

## Risk
- Alla produkter med taggen `Hoodie` eller `kids` försvinner ur dessa två kollektioner, även framtida. Det är avsikten, men om en vuxenjacka någon gång får taggen `Hoodie` försvinner den också.
- Barnjackor blir inte kvar i någon vinterjackskollektion. Det finns `jacka-pojke` och `jacka-flicka` för barn.
