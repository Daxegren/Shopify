"""Formatregler beslutade av David 2026-11-01: (1) stor bokstav efter kolon, (2) stor bokstav på beskrivande ord i titel och SEO-titel."""
import re
SMA = {"och", "med", "för", "i", "på", "av", "till", "om", "utan", "samt", "eller", "en", "ett", "som", "att", "vid", "från", "x", "of", "by"}
ENHETER = {"cm", "mm", "kg", "g", "tum", "hk", "khz", "lux", "w", "wh", "psi", "bar", "m", "l", "st", "nm", "km/h", "kw", "gr", "mah", "v"}
def _ord(w, forst):
    k = re.match(r"^([\(\"'\[]*)(.*?)([\)\"'\],.;:!?]*)$", w)
    pre, kärna, suf = k.group(1), k.group(2), k.group(3)
    if not kärna: return w
    l = kärna.lower()
    if re.search(r"\d", kärna): return w
    if any(c.isupper() for c in kärna[1:]): return w  # MG, LED, USB, iPhone
    if not forst and (l in SMA or l in ENHETER): return pre + kärna + suf
    if "-" in kärna:
        kärna = "-".join(p[:1].upper() + p[1:] for p in kärna.split("-"))
    else:
        kärna = kärna[:1].upper() + kärna[1:]
    return pre + kärna + suf
def titel_versaler(t):
    ws = t.split(" ")
    return " ".join(_ord(w, i == 0) for i, w in enumerate(ws))
def kolon_versal(s):
    return re.sub(r":(\s+)([a-zåäö])", lambda m: ":" + m.group(1) + m.group(2).upper(), s)
def tillamp(p):
    """Returnerar en kopia av utkastet med reglerna tillämpade på alla textfält."""
    q = dict(p)
    q["titel"] = titel_versaler(kolon_versal(p["titel"]))
    q["seo_title"] = titel_versaler(kolon_versal(p["seo_title"]))
    for f in ("meta", "intro", "marke"):
        if q.get(f): q[f] = kolon_versal(q[f])
    for f in ("passar", "spec"):
        q[f] = [kolon_versal(x) for x in p[f]]
    q["faq"] = [(kolon_versal(a), kolon_versal(b)) for a, b in p["faq"]]
    return q
