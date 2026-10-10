"""Textverktyg: normalisering, fingeravtryck, stavfelsavstånd och enkel språkgissning."""

from __future__ import annotations

import hashlib
import re
import unicodedata
from collections import Counter

WORD_RE = re.compile(r"[^\W\d_]+(?:['’-][^\W\d_]+)*", re.UNICODE)


def words(text: str) -> list[str]:
    return WORD_RE.findall(text.lower())


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text or "").lower()
    return re.sub(r"\s+", " ", text).strip()


def fingerprint(text: str) -> str:
    return hashlib.sha1(normalize(text).encode()).hexdigest()


def shingles(text: str, k: int = 5) -> set[int]:
    w = words(text)
    if len(w) < k:
        return {hash(" ".join(w))} if w else set()
    return {hash(" ".join(w[i:i + k])) for i in range(len(w) - k + 1)}


def jaccard(a: set, b: set) -> float:
    if not a and not b:
        return 1.0
    return len(a & b) / len(a | b)


def osa_distance(a: str, b: str) -> int:
    """Damerau-Levenshtein (optimal string alignment): byte av två bokstäver räknas som 1."""
    la, lb = len(a), len(b)
    d = [[0] * (lb + 1) for _ in range(la + 1)]
    for i in range(la + 1):
        d[i][0] = i
    for j in range(lb + 1):
        d[0][j] = j
    for i in range(1, la + 1):
        for j in range(1, lb + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + cost)
            if i > 1 and j > 1 and a[i - 1] == b[j - 2] and a[i - 2] == b[j - 1]:
                d[i][j] = min(d[i][j], d[i - 2][j - 2] + 1)
    return d[la][lb]


def find_misspellings(text: str, brand_terms: list[str], known: list[str] | None = None, max_distance: int = 2) -> Counter:
    """Hittar ord som ligger nära ett varumärke men inte är exakt det, t.ex. 'Mankosvky'."""
    hits: Counter = Counter()
    brands = [b.lower() for b in brand_terms if len(b) >= 5]
    known_l = {k.lower() for k in (known or [])}
    for w in set(words(text)):
        if w in known_l:
            hits[w] += text.lower().count(w)
            continue
        for b in brands:
            if w == b or abs(len(w) - len(b)) > max_distance:
                continue
            if w[0] != b[0]:
                continue
            if osa_distance(w, b) <= max_distance:
                hits[w] += text.lower().count(w)
    return hits


# Små stoppordslistor räcker för att skilja språken åt på sidnivå.
STOPWORDS = {
    "sv": "och att det som en på är för med har inte till av den om de var vi ett så kan eller vår våra här alla",
    "en": "the and to of a in is for that you with on it are this be your as at our we or by from all",
    "de": "und der die das zu nicht ist ein eine mit für auf den dem sie wir es sich auch bei aus oder",
    "da": "og at det en til er på som med af for ikke de den har vi kan eller et vores alle",
    "no": "og at det en til er på som med av for ikke de den har vi kan eller et våre alle",
    "fi": "ja on että ei se hän ovat kanssa tai mutta kun myös joka mikä sekä ole olla meidän",
    "fr": "le la les et de des un une du est pour pas que qui dans en sur avec nous vous ou",
    "es": "el la los las y de del que en un una es por para con no se su al lo como nuestro",
    "it": "il la le e di che un una per non con sono del della nel al da ci come nostro",
    "nl": "de het een en van ik te dat die in is niet op met voor zijn er ons of uw",
    "pl": "i w na nie się z do to że jest jak po co ale lub dla od przez nasz",
}
_STOP = {lang: set(s.split()) for lang, s in STOPWORDS.items()}


def guess_language(text: str, min_hits: int = 8) -> tuple[str | None, float]:
    """Returnerar (språk, andel) där andel är hur stor del av stoppordsträffarna språket står för."""
    counts: Counter = Counter()
    for w in words(text):
        for lang, stop in _STOP.items():
            if w in stop:
                counts[lang] += 1
    total = sum(counts.values())
    if total < min_hits:
        return None, 0.0
    lang, n = counts.most_common(1)[0]
    return lang, n / total


def locale_language(locale: str | None) -> str | None:
    if not locale:
        return None
    lang = locale.split("-")[0].lower()
    return {"nb": "no", "nn": "no"}.get(lang, lang)
