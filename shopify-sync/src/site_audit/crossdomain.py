"""Jämför flera domäner som delar butik (till exempel bestofsports.se, .dk och .fi) sida för sida (T18).

Genomlysningen granskar varje domän för sig. Det som bara syns när domänerna ställs mot varandra är: sidor som är
oöversatta kopior, canonical som pekar på en systerdomän, hreflang som inte är ömsesidig och produktpriser i fel valuta.
Jämförelsen hämtar ett urval av samma adresser från varje domän (startsida, kategorier och produkter som finns i alla)."""

from __future__ import annotations

import logging
from collections import defaultdict
from itertools import combinations
from urllib.parse import urlsplit

from .config import SiteConfig
from .findings import Finding
from .html_parse import PageFacts, page_type, parse_page
from .sitemap import read_sitemaps

log = logging.getLogger(__name__)
F = Finding
SAMPLE_TYPES = ("collection", "product")


def host_of(url: str) -> str:
    return urlsplit(url).netloc.lower()


def evenly(items: list[str], n: int) -> list[str]:
    """n jämnt fördelade element ur en sorterad lista (samma urval varje gång)."""
    items = sorted(items)
    if len(items) <= n:
        return items
    step = len(items) / n
    return [items[int(i * step)] for i in range(n)]


def common_paths(sitemap_paths: dict[str, dict[str, list[str]]], per_type: int) -> list[str]:
    """Adresser av varje sidtyp som finns på alla domäner. sitemap_paths[sajt][typ] = lista med sökvägar."""
    sites = list(sitemap_paths)
    out: list[str] = []
    for ptype in SAMPLE_TYPES:
        sets = [set(sitemap_paths[s].get(ptype, [])) for s in sites]
        shared = set.intersection(*sets) if sets else set()
        out.extend(evenly(sorted(shared), per_type))
    return out


def collect_pages(sites: dict[str, SiteConfig], fetcher, per_type: int = 12) -> tuple[dict[str, dict[str, PageFacts]], list[str]]:
    """Hämtar urvalet från varje domän. Returnerar (sidfakta per sajt och sökväg, anteckningar)."""
    notes: list[str] = []
    sitemap_paths: dict[str, dict[str, list[str]]] = {}
    for name, site in sites.items():
        sm = read_sitemaps(fetcher, site.base_url.rstrip("/") + "/sitemap.xml")
        by_type: dict[str, list[str]] = defaultdict(list)
        for e in sm.entries:
            path = urlsplit(e.url).path
            by_type[page_type(path)].append(path)
        sitemap_paths[name] = by_type
        if not sm.entries:
            notes.append(f"{name}: sitemapen gav inga adresser ({sm.errors[:1]})")
    paths = ["/"] + common_paths(sitemap_paths, per_type)
    if len(paths) == 1:
        notes.append("Domänerna har inga gemensamma kategori- eller produktadresser (översatta handles?). Jämförelsen gäller bara startsidorna.")
    pages: dict[str, dict[str, PageFacts]] = {name: {} for name in sites}
    for name, site in sites.items():
        base = site.base_url.rstrip("/")
        for path in paths:
            res = fetcher.fetch(base + path)
            if res.status == 200 and res.is_html:
                pages[name][path] = parse_page(res.final_url, res.body, host_of(base))
            else:
                notes.append(f"{name}{path}: HTTP {res.status or res.error}")
    return pages, notes


def _fingerprint_or_title(f: PageFacts) -> tuple[str | None, str | None]:
    return f.text_fingerprint, (f.title or "").strip().lower() or None


def compare_domains(pages: dict[str, dict[str, PageFacts]], sites: dict[str, SiteConfig]) -> list[Finding]:
    """Rena jämförelser av insamlade sidfakta. Inga nätverksanrop."""
    out: list[Finding] = []
    hosts = {name: host_of(s.base_url) for name, s in sites.items()}
    all_hosts = set(hosts.values())

    # 1. Oöversatta kopior: samma text eller samma titel på två domäner i olika länder
    for a, b in combinations(pages, 2):
        shared = sorted(set(pages[a]) & set(pages[b]))
        if not shared or sites[a].primary_locale == sites[b].primary_locale:
            continue
        same = []
        for p in shared:
            fa, ta = _fingerprint_or_title(pages[a][p])
            fb, tb = _fingerprint_or_title(pages[b][p])
            if (fa and fa == fb) or (ta and ta == tb):
                same.append(p)
        if same:
            share = len(same) / len(shared)
            out.append(F("cross_domain_untranslated", "high" if share >= 0.3 else "medium", "international",
                         f"{a} och {b}: {len(same)} av {len(shared)} jämförda sidor har samma text eller titel trots olika språk",
                         url=pages[a][same[0]].url,
                         evidence={"sites": [a, b], "same": len(same), "compared": len(shared), "sample": same[:10]}))

    for name, site in sites.items():
        own = hosts[name]
        siblings = all_hosts - {own}
        fp = pages.get(name, {})
        # 2. Canonical till en annan domän i butiken
        to_sibling = [f for f in fp.values() if f.canonical and host_of(f.canonical) in siblings]
        if to_sibling:
            out.append(F("canonical_to_sibling_domain", "high", "international",
                         f"{name}: {len(to_sibling)} sidor har canonical till en systerdomän och faller ur Googles index",
                         url=to_sibling[0].url, evidence={"count": len(to_sibling), "sample": [f.url for f in to_sibling[:10]]}))
        # 3. hreflang mot systerdomäner
        if fp:
            linked = [p for p, f in fp.items() if any(host_of(u) in siblings for u in f.hreflang.values())]
            if len(linked) < len(fp) / 2:
                out.append(F("hreflang_missing_between_domains", "medium", "international",
                             f"{name}: bara {len(linked)} av {len(fp)} sidor pekar med hreflang på systerdomänerna",
                             url=site.base_url, evidence={"with_sibling_hreflang": len(linked), "pages": len(fp)}))
            # 4. Ömsesidighet: A pekar på B men B pekar inte tillbaka på A
            for p, f in fp.items():
                for lang, target in f.hreflang.items():
                    th = host_of(target)
                    other = next((n for n, h in hosts.items() if h == th and n != name), None)
                    if not other:
                        continue
                    back = pages.get(other, {}).get(urlsplit(target).path or "/")
                    if back is not None and not any(host_of(u) == own for u in back.hreflang.values()):
                        out.append(F("hreflang_not_reciprocal", "medium", "international",
                                     f"{name}{p} pekar på {other} med hreflang men {other} pekar inte tillbaka",
                                     url=f.url, evidence={"from": name, "to": other, "hreflang": lang}))
                        break
        # 5. Valuta i produktschemat
        expected = (site.shopify_currency or "").upper()
        if expected:
            wrong = [f for f in fp.values() for ps in f.product_schema
                     if ps.get("currencies") and set(ps["currencies"]) - {expected}]
            if wrong:
                out.append(F("schema_currency_mismatch", "high", "schema",
                             f"{name}: {len(wrong)} produktsidor visar pris i annan valuta än {expected} i produktschemat",
                             url=wrong[0].url, evidence={"expected": expected, "count": len(wrong), "sample": [f.url for f in wrong[:10]]}))
    return out
