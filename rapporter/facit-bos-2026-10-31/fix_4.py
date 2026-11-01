# Stickprov 2026-11-01: David ville ha mer information på Toorx träningsmatta 200x100x0,9 (nr 1).
# Tillägg: material PVC och halkfri yta (återförsäljarsidor Galaxus och Mediaworld; ej tillverkarens egen sida).
import copy, importlib
D = []
for _p in importlib.import_module("vag1_06").D:
    if _p["id"] == "10472299102474":
        q = copy.deepcopy(_p)
        q["fakta"] += " Tillägg från återförsäljarsidor 2026-11-01 (Galaxus, Mediaworld): PVC, halkfri yta, stötdämpande struktur."
        q["intro"] = "Träningsmatta från Toorx i PVC med halkfri yta, 200 x 100 x 0,9 cm."
        q["passar"] = ["Dig som vill ha en stor träningsmatta (200 x 100 cm)"]
        q["spec"] = ["Material: PVC", "Yta: halkfri", "Mått: 200 x 100 x 0,9 cm"]
        q["meta"] = "Toorx träningsmatta i PVC med halkfri yta, 200 x 100 x 0,9 cm. Modell MAT-200 från Toorx, en stor och halkfri träningsmatta på 200 x 100 cm."
        q["motivering"] = "Källan i butiken är bara titeln. Material och halkfri yta kommer från två återförsäljarsidor och är markerade för bekräftelse."
        q["att_bekrafta"] = ["Material (PVC) och halkfri yta kommer från återförsäljarsidor, inte från Toorx datablad. Bekräfta mot Toorx.", "Vikt och användningsområden saknas. Källan anger inte vilket mått som är tjocklek (0,9 cm läses ur titelns tredje mått).", "En återförsäljare anger 0,6 cm för en 200 x 100-matta. Bekräfta tjockleken."]
        D.append(q)
