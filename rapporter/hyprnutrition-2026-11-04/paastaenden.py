import json,re,sys
P=json.load(open("offentlig_products.json"))
KAT={
"hälsopåstående (funktion/effekt)":r"immunförsvar|leder\b|ledern|hud\b|spänstig|kollagensyntes|muskel|återhämtning|energi\w*|trötthet|koncentration|kognitiv|hjärn|benhälsa|stärker|stödjer|stöd åt|stödja|hälsa|välmående|inflammation|stelhet|smärt|upptag|biotillgäng|prestation|uppiggande|balanserad|fokus",
"näringspåstående (hög/källa/fri)":r"sockerfri|sugar-free|koffeinfri|proteinrik|källa till|hög halt|rent |100 ?%|utan tillsats|vegan",
"sjukdom/medicinskt":r"sjukdom|behandl\w+|bota|förebygg\w*|lindra\w*|artros|reumat|diabetes|depression|ångest|cancer|hjärt|blodtryck|kolesterol|virus|infektion|förkylning",
"dosrekommendation/bruksanvisning":r"\b\d+\s?(g|mg|kapslar|tabletter|sticks|servings|burk\w*)\b.{0,40}(per dag|dagligen|dos|portion)|rekommenderad|dagl\w+ dos|ta \d|1–2|\bdagligen\b",
"jämförelse/superlativ":r"ultimat\w*|bäst\w*|premium\w*|potent\w*|kliniskt|välstuderad\w*|maximal\w*|absolut",
"viktminskning/kroppsförändring":r"viktminsk\w*|fettförbränn\w*|gå ner i vikt|bygga muskler|muskelmassa|muskeltillväxt",
}
rows=[]
for p in P:
    t=re.sub(r"<[^>]+>"," ",p["body_html"] or "");t=re.sub(r"\s+"," ",t)
    for k,rx in KAT.items():
        hits=sorted({m.group(0).lower() for m in re.finditer(rx,t,re.I)})
        if hits: rows.append((p["id"],p["title"][:45],k,", ".join(hits)[:140]))
json.dump(rows,open("paastaenden_produkter.json","w"),ensure_ascii=False,indent=1)
for r in rows: print(*r,sep=" | ")
