#!/usr/bin/env python3
"""Mäter intern länkning på en Shopify-butik (publika sidor, ingen inloggning, bara läsning).

Fristående: kräver varken BigQuery, Google Cloud eller hemligheter. Återanvänder fetch.py, sitemap.py,
html_parse.py och crawler.py i src/site_audit för hämtning, sitemap, sidtyper och spårningsparametrar.

Två steg (resultatet av steg 1 sparas i en katalog och kan återupptas):
  python3 -I shopify-sync/scripts/intern_lankning_mat.py crawl --bas https://bestofsports.se --ut <katalog>
  python3 -I shopify-sync/scripts/intern_lankning_mat.py analysera --bas https://bestofsports.se --ut <katalog> \
        --rapport rapporter/intern-lankning-bos-2026-11-12 [--gsc <csv med handle,visningar,position>]

Regler för hämtningen: robots.txt följs (Google-tolkning med * och $), neutral User-Agent utan e-post, högst 3 anrop per
sekund (förvalt 2,5), vid upprepade 429/5xx pausar skriptet och avbryter efter tre pauser. Tester: scripts/test_intern_lankning_mat.py.
"""
from __future__ import annotations

import argparse
import collections
import csv
import functools
import hashlib
import heapq
import json
import os
import random
import re
import statistics
import sys
import threading
import time
from urllib.parse import parse_qsl, urlencode, urljoin, urlsplit

SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from bs4 import BeautifulSoup  # noqa: E402
from site_audit.crawler import REDIRECT_TRACKING_PARAMS  # noqa: E402
from site_audit.fetch import Fetcher  # noqa: E402
from site_audit.html_parse import is_malformed_href, page_type  # noqa: E402
from site_audit.sitemap import read_sitemaps  # noqa: E402

try:
    import lxml  # noqa: F401
    PARSER = "lxml"
except ImportError:  # pragma: no cover
    PARSER = "html.parser"

USER_AGENT = "LinkStructureMeasure/1.0 (read-only internal link measurement; no login)"
MAX_RPS = 3.0
TEMPLATE_REGIONS = ("meny", "sidfot", "overlay", "sidomeny")   # block som upprepas på många sidor
FETCH_FAMILIES = ("home", "collection", "product", "page", "blog", "article")
EXCLUDED_PREFIXES = ("/cart", "/checkout", "/account", "/customer_authentication", "/search", "/cdn", "/apps",
                     "/services", "/recommendations", "/orders", "/admin", "/policies", "/.well-known")
GENERIC_ANCHORS = {
    "klicka här", "klick här", "här", "läs mer", "läs mer här", "läs mer »", "läs mera", "se mer", "visa mer", "mer",
    "mer info", "mer information", "visa alla", "se alla", "se alla produkter", "visa alla produkter", "shoppa",
    "shoppa nu", "köp nu", "gå till", "upptäck", "upptäck mer", "utforska", "klicka", "link", "länk", "read more",
    "click here", "»", "→", "›", ">", "...", "…",
}


# --------------------------------------------------------------------------------------------- robots.txt
class Robots:
    """Google-tolkning: längsta matchande mönster vinner, Allow vinner vid lika längd. Stöd för * och $."""

    def __init__(self, text: str, agent: str = "linkstructuremeasure"):
        groups: list[tuple[list[str], list[tuple[str, str]]]] = []
        agents: list[str] = []
        rules: list[tuple[str, str]] = []
        last_was_agent = False
        for raw in text.splitlines():
            line = raw.split("#", 1)[0].strip()
            if ":" not in line:
                continue
            key, _, val = line.partition(":")
            key, val = key.strip().lower(), val.strip()
            if key == "user-agent":
                if not last_was_agent and agents:
                    groups.append((agents, rules))
                    agents, rules = [], []
                agents.append(val.lower())
                last_was_agent = True
                continue
            last_was_agent = False
            if key in ("allow", "disallow"):
                rules.append((key, val))
        if agents:
            groups.append((agents, rules))
        chosen = None
        for ags, rls in groups:
            if any(a != "*" and a in agent for a in ags):
                chosen = rls
        if chosen is None:
            for ags, rls in groups:
                if "*" in ags:
                    chosen = rls
        self.rules = [(kind, self._compile(pat), len(pat)) for kind, pat in (chosen or []) if pat]

    @staticmethod
    def _compile(pattern: str):
        anchored = pattern.endswith("$")
        core = pattern[:-1] if anchored else pattern
        rx = "".join(".*" if ch == "*" else re.escape(ch) for ch in core)
        return re.compile("^" + rx + ("$" if anchored else ""))

    def allowed(self, path_and_query: str) -> bool:
        best_len, verdict = -1, True
        for kind, rx, plen in self.rules:
            if rx.match(path_and_query):
                if plen > best_len or (plen == best_len and kind == "allow"):
                    best_len, verdict = plen, kind == "allow"
        return verdict


# ------------------------------------------------------------------------------------- länkar och adresser
def norm_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def is_generic_anchor(text: str) -> bool:
    t = norm_ws(text).lower().strip(" .:!")
    return t in GENERIC_ANCHORS


def strip_fragment_and_tracking(url: str) -> tuple[str, list[str]]:
    """Tar bort #fragment och spårningsparametrar. Ger (adress, lista med borttagna parameternamn)."""
    p = urlsplit(url)
    kept, removed = [], []
    for k, v in parse_qsl(p.query, keep_blank_values=True):
        if REDIRECT_TRACKING_PARAMS.match(k):
            removed.append(k)
        else:
            kept.append((k, v))
    query = urlencode(kept)
    path = p.path or "/"
    if path != "/" and path.endswith("/"):
        path = path.rstrip("/")
    return path + ("?" + query if query else ""), removed


@functools.lru_cache(maxsize=200000)
def classify_target(path_query: str) -> tuple[str, str]:
    """Ger (familj, nyckel). Nyckeln är den adress som räknas som målsidan:
    produkter och kollektioner utan frågedel (utom ?page=N), /collections/x/products/y blir /products/y.
    Familjer: home, collection, product, page, blog, article, filter (kollektion med filterparametrar), other."""
    p = urlsplit(path_query)
    path = p.path or "/"
    q = parse_qsl(p.query, keep_blank_values=True)
    fam = page_type(path)
    m = re.match(r"^/collections/[^/]+/products/([^/]+)$", path)
    if m:
        return "product", "/products/" + m.group(1)
    if fam in ("collection", "blog") and q:
        if len(q) == 1 and q[0][0] == "page" and q[0][1].isdigit():
            return fam, path + ("?page=" + q[0][1] if q[0][1] != "1" else "")
        return "filter", path
    if fam in ("product", "page", "article", "home", "collection", "blog"):
        return fam, path
    return "other", path_query


def extract_links(html: bytes | str, page_url: str, host: str) -> dict:
    """Plockar länkar ur en sida. Varje länk får region (meny, sidfot, overlay, sidomeny, brodsmula, paginering,
    innehall, ovrigt) och temasektion. Ger {'links': [...], 'ext': antal externa, 'meta': {...}}."""
    soup = BeautifulSoup(html, PARSER)
    assigned: dict[int, tuple[str, str | None]] = {}

    def mark(container, region, section=None):
        for a in container.find_all("a", href=True):
            assigned.setdefault(id(a), (region, section))

    for el in soup.select(".shopify-section-group-header-group"):
        mark(el, "meny")
    for el in soup.select(".shopify-section-group-footer-group"):
        mark(el, "sidfot")
    for el in soup.select(".shopify-section-group-overlay-group"):
        mark(el, "overlay")
    main = soup.find("main")
    if main is not None:
        for el in main.select('[class*="custom-sidebar"]'):
            mark(el, "sidomeny")
        for el in main.find_all(True):
            classes = [c.lower() for c in (el.get("class") or [])]
            label = (el.get("aria-label") or "").lower()
            if "breadcrumb" in label or "brödsmula" in label or any("breadcrumb" in c for c in classes):
                mark(el, "brodsmula")
            elif "pagination" in label or "paginering" in label or any(c == "pagination" or c.startswith("pagination__") for c in classes):
                mark(el, "paginering")
        for s in main.find_all(True, id=re.compile(r"^shopify-section")):
            sid = s.get("id", "").split("__", 1)[-1]
            mark(s, "innehall", sid)
        mark(main, "innehall", None)

    links: dict[tuple, tuple] = {}
    ext = 0
    n_malformed = 0
    for a in soup.find_all("a", href=True):
        raw = a["href"].strip()
        if not raw or raw.startswith(("#", "mailto:", "tel:", "javascript:", "sms:", "whatsapp:")):
            continue
        malformed = is_malformed_href(raw)
        if malformed:
            n_malformed += 1
            links[("MALFORMED", raw[:120], "ovrigt")] = ("MALFORMED:" + raw[:120], "", assigned.get(id(a), ("ovrigt", None))[0], None, "", True)
            continue
        absolute = urljoin(page_url, raw)
        sp = urlsplit(absolute)
        if sp.scheme not in ("http", "https"):
            continue
        h = (sp.hostname or "").lower()
        if h != host and h != "www." + host:
            ext += 1
            continue
        pq = (sp.path or "/") + ("?" + sp.query if sp.query else "")
        target, removed = strip_fragment_and_tracking(pq)
        text = norm_ws(a.get_text(" ", strip=True))
        if not text:
            img = a.find("img")
            if img is not None and norm_ws(img.get("alt", "")):
                text = "[bild] " + norm_ws(img.get("alt", ""))
            elif norm_ws(a.get("aria-label", "")):
                text = "[aria] " + norm_ws(a.get("aria-label", ""))
            elif norm_ws(a.get("title", "")):
                text = "[title] " + norm_ws(a.get("title", ""))
            else:
                text = "(tom)"
        region, section = assigned.get(id(a), ("ovrigt", None))
        key = (target, text, region)
        track = ",".join(sorted(set(removed)))
        if key not in links:
            links[key] = (target, text, region, section, track, False)
        elif track and not links[key][4]:
            links[key] = (target, text, region, section, track, False)
    title = soup.title.get_text(strip=True) if soup.title else None
    h1 = soup.find("h1")
    canon = None
    for l in soup.find_all("link", rel=True):
        if "canonical" in [r.lower() for r in (l.get("rel") or [])] and l.get("href"):
            canon = l["href"].strip()
    rb = soup.find("meta", attrs={"name": re.compile(r"^robots$", re.I)})
    return {"links": list(links.values()), "ext": ext, "malformed": n_malformed,
            "meta": {"title": title, "h1": norm_ws(h1.get_text(" ", strip=True)) if h1 else None, "canonical": canon,
                     "robots_meta": rb.get("content") if rb else None}}


def canonical_path(url: str | None, host: str) -> str | None:
    if not url:
        return None
    sp = urlsplit(url)
    if sp.hostname and sp.hostname.lower() not in (host, "www." + host):
        return "EXTERN:" + url
    path = sp.path or "/"
    return path.rstrip("/") or "/"


# ------------------------------------------------------------------------------------------------ hämtning
class Abort(Exception):
    pass


class PoliteFetcher:
    """Lindar Fetcher: vid upprepade 429/5xx/nätverksfel pausar den och avbryter efter tre pauser."""

    def __init__(self, fetcher, max_consecutive=5, pause_s=120.0, max_pauses=3, sleep=time.sleep):
        self.fetcher, self.max_consecutive, self.pause_s, self.max_pauses, self.sleep = fetcher, max_consecutive, pause_s, max_pauses, sleep
        self.consecutive, self.pauses = 0, 0
        self.lock = threading.Lock()
        self.errors = collections.Counter()

    def fetch(self, url):
        res = self.fetcher.fetch(url)
        bad = res.status == 429 or res.status >= 500 or (res.status == 0 and not res.hops) or \
            (res.status == 0 and (res.error or "").startswith(("429", "ConnectionError", "ReadTimeout", "ConnectTimeout")))
        with self.lock:
            if bad:
                self.errors[res.status or (res.error or "fel")[:40]] += 1
                self.consecutive += 1
                if self.consecutive >= self.max_consecutive:
                    self.pauses += 1
                    if self.pauses > self.max_pauses:
                        raise Abort(f"Avbryter efter {self.max_pauses} pauser: upprepade 429/5xx/nätverksfel (senast {res.status} {res.error})")
                    self.consecutive = 0
                    limiter = getattr(self.fetcher, "limiter", None)
                    if limiter is not None and getattr(limiter, "interval", 0):
                        limiter.interval *= 1.5      # efter varje paus sänks takten med en tredjedel
                    pause = self.pause_s * self.pauses
                    print(f"[paus] upprepade fel, väntar {pause:.0f}s (paus {self.pauses}/{self.max_pauses})", flush=True)
                    self.sleep(pause)
            else:
                self.consecutive = 0
        return res


def make_record(url: str, res, in_sitemap: bool, kind: str, host: str, blocks: dict) -> dict:
    hops = [{"url": h.url, "status": h.status} for h in res.hops]
    final_path = urlsplit(res.final_url).path or "/"
    rec = {"url": url, "kind": kind, "in_sitemap": in_sitemap, "status": res.status, "final": res.final_url,
           "hops": hops, "redirected": res.redirect_count > 0, "error": res.error,
           "xrobots": res.headers.get("x-robots-tag") if res.headers else None, "type": page_type(urlsplit(url).path or "/"),
           "final_type": page_type(final_path), "links": [], "blocks": {}}
    if res.status == 200 and res.is_html and res.body:
        ex = extract_links(res.body, res.final_url, host)
        rec.update(ex["meta"])
        rec["ext"] = ex["ext"]
        rec["malformed"] = ex["malformed"]
        by_region = collections.defaultdict(list)
        own = []
        for l in ex["links"]:
            if l[2] in TEMPLATE_REGIONS:
                by_region[l[2]].append(list(l))
            else:
                own.append(list(l))
        rec["links"] = own
        for region, lst in by_region.items():
            lst.sort()
            sig = hashlib.sha1(json.dumps(lst, ensure_ascii=False).encode()).hexdigest()[:12]
            blocks.setdefault(sig, lst)
            rec["blocks"][region] = sig
    return rec


def disallowed_by_family(path_q: str) -> bool:
    return path_q.startswith(EXCLUDED_PREFIXES)


def crawl(base: str, out_dir: str, fetcher, rps: float = 2.5, products="all", seed: int = 1, deadline_min: float | None = None,
          threads: int = 3, extra_seeds: list[str] | None = None, progress_every: int = 100, skip_types: tuple = ()) -> dict:
    """Hämtar sitemap, startsida och länkade sidor. Skriver sidor.jsonl och block.jsonl i out_dir."""
    import queue

    os.makedirs(out_dir, exist_ok=True)
    host = urlsplit(base).hostname.lower()
    t0 = time.time()
    robots_res = fetcher.fetch(base + "/robots.txt")
    robots = Robots(robots_res.body.decode("utf-8", "replace") if robots_res.status == 200 else "")
    sm = read_sitemaps(fetcher.fetcher if hasattr(fetcher, "fetcher") else fetcher, base + "/sitemap.xml")
    sm_urls: dict[str, str] = {}
    for e in sm.entries:
        pq, _ = strip_fragment_and_tracking(urlsplit(e.url).path + ("?" + urlsplit(e.url).query if urlsplit(e.url).query else ""))
        sm_urls[pq] = e.sitemap
    prods = sorted(u for u in sm_urls if page_type(u) == "product")
    if products != "all" and int(products) < len(prods):
        prods = sorted(random.Random(seed).sample(prods, int(products)))
    prod_set = set(prods)
    seeds = [("/", 0)]
    for u in sorted(sm_urls):
        if u == "/" or page_type(u) in skip_types:
            continue
        if page_type(u) == "product":
            if u in prod_set:
                seeds.append((u, 3))
        else:
            seeds.append((u, 0))
    for u in extra_seeds or []:
        seeds.append((u, 0))
    rec_path, blk_path = os.path.join(out_dir, "sidor.jsonl"), os.path.join(out_dir, "block.jsonl")
    done: dict[str, dict] = {}
    blocks: dict[str, list] = {}
    if os.path.exists(rec_path):
        with open(rec_path, encoding="utf-8") as f:
            for line in f:
                r = json.loads(line)
                done[r["url"]] = r
    if os.path.exists(blk_path):
        with open(blk_path, encoding="utf-8") as f:
            for line in f:
                b = json.loads(line)
                blocks[b["sig"]] = b["links"]
    written_blocks = set(blocks)
    q: "queue.PriorityQueue" = queue.PriorityQueue()
    queued: set[str] = set()
    seq = [0]
    lock = threading.Lock()
    stats = {"discovered_queued": 0, "robots_skipped": [], "stopped": None}
    discover_products = products == "all"

    def enqueue(url, prio, kind):
        with lock:
            if url in queued:
                return
            queued.add(url)
            seq[0] += 1
            q.put((prio, seq[0], url, kind))

    def discover(rec):
        for (target, _a, region, _s, _t, mal) in rec["links"] + [l for sig in rec["blocks"].values() for l in blocks.get(sig, [])]:
            if mal:
                continue
            fam, key = classify_target(target)
            if fam not in FETCH_FAMILIES or key in queued or key in done:
                continue
            if fam == "product" and not discover_products:
                continue
            if fam in skip_types:
                continue
            if disallowed_by_family(key) or not robots.allowed(key):
                continue
            is_page = "?page=" in key
            enqueue(key, 1 if is_page else 2, "paginering" if is_page else "lankad")
            stats["discovered_queued"] += 1

    for u, prio in seeds:
        if u in done:
            continue
        if not robots.allowed(u):
            stats["robots_skipped"].append(u)
            continue
        enqueue(u, prio, "sitemap")
    queued.update(done)
    for r in list(done.values()):
        discover(r)
    out = open(rec_path, "a", encoding="utf-8")
    outb = open(blk_path, "a", encoding="utf-8")
    inflight = [0]
    counter = [len(done)]
    abort = []

    def worker():
        while True:
            if abort:
                return
            try:
                prio, _s, url, kind = q.get(timeout=1.0)
            except queue.Empty:
                with lock:
                    if inflight[0] == 0 and q.empty():
                        return
                continue
            with lock:
                inflight[0] += 1
            try:
                if deadline_min and time.time() - t0 > deadline_min * 60:
                    stats["stopped"] = "tidsgräns"
                    abort.append("tid")
                    return
                res = fetcher.fetch(base + url)
                with lock:
                    rec = make_record(url, res, url in sm_urls or url == "/", kind, host, blocks)
                    out.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    out.flush()
                    for sig in rec["blocks"].values():
                        if sig not in written_blocks:
                            written_blocks.add(sig)
                            outb.write(json.dumps({"sig": sig, "links": blocks[sig]}, ensure_ascii=False) + "\n")
                            outb.flush()
                    done[url] = rec
                    counter[0] += 1
                    n = counter[0]
                discover(rec)
                if n % progress_every == 0:
                    print(f"[{time.strftime('%H:%M:%S')}] {n} sidor hämtade, {q.qsize()} i kö", flush=True)
            except Abort as e:
                stats["stopped"] = str(e)
                abort.append(str(e))
                return
            finally:
                with lock:
                    inflight[0] -= 1

    ths = [threading.Thread(target=worker, daemon=True) for _ in range(threads)]
    for t in ths:
        t.start()
    for t in ths:
        t.join()
    out.close()
    outb.close()
    meta = {"bas": base, "start": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t0)), "slut": time.strftime("%Y-%m-%d %H:%M:%S"),
            "sekunder": int(time.time() - t0), "sitemap_adresser": len(sm_urls), "sitemap_fel": sm.errors,
            "sitemap_per_typ": dict(collections.Counter(page_type(u) for u in sm_urls)),
            "produkter_i_sitemap": len([u for u in sm_urls if page_type(u) == "product"]),
            "produkter_hamtade_urval": len(prods), "produkturval": "alla" if products == "all" else f"slumpmässigt urval, seed {seed}",
            "hamtade_sidor": len(done), "hastighet_anrop_per_sekund_max": rps, "user_agent": USER_AGENT,
            "robots_blockerade_sitemapadresser": stats["robots_skipped"], "stopp": stats["stopped"], "hoppade_over_sidtyper": list(skip_types),
            "fel_serier": dict(getattr(fetcher, "errors", {})), "pauser": getattr(fetcher, "pauses", 0), "sitemap_urls": sorted(sm_urls)}
    with open(os.path.join(out_dir, "meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
    return meta


# ------------------------------------------------------------------------------------------------ analys
def _open_text(path: str):
    """Öppnar path, eller path + '.gz' om bara den komprimerade filen finns."""
    if not os.path.exists(path) and os.path.exists(path + ".gz"):
        import gzip
        return gzip.open(path + ".gz", "rt", encoding="utf-8")
    return open(path, encoding="utf-8")


def load_run(out_dir: str) -> tuple[dict, dict, dict]:
    recs, blocks = {}, {}
    with _open_text(os.path.join(out_dir, "sidor.jsonl")) as f:
        for line in f:
            r = json.loads(line)
            recs[r["url"]] = r
    with _open_text(os.path.join(out_dir, "block.jsonl")) as f:
        for line in f:
            b = json.loads(line)
            blocks[b["sig"]] = b["links"]
    meta = {}
    mp = os.path.join(out_dir, "meta.json")
    if os.path.exists(mp):
        with open(mp, encoding="utf-8") as f:
            meta = json.load(f)
    return recs, blocks, meta


def page_links(rec: dict, blocks: dict):
    """Alla länkar på en sida: egna plus mallblock."""
    for l in rec["links"]:
        yield l
    for sig in rec["blocks"].values():
        for l in blocks.get(sig, []):
            yield l


def source_key(url: str) -> str:
    """Sidor med ?page=N räknas som samma källa som första sidan."""
    return url.split("?", 1)[0] if "?page=" in url else url


def is_live(rec: dict | None) -> bool:
    return bool(rec) and rec["status"] == 200 and not rec["redirected"]


def is_noindex(rec: dict, host: str = "") -> bool:
    return "noindex" in ((rec.get("robots_meta") or "") + " " + (rec.get("xrobots") or "")).lower()


def canonical_elsewhere(rec: dict, host: str) -> bool:
    c = canonical_path(rec.get("canonical"), host)
    if not c:
        return False
    own = urlsplit(rec["final"]).path.rstrip("/") or "/"
    return c != own


def resolve(recs: dict, key: str, max_hops: int = 3) -> str:
    """Följer omdirigering till slutadress (om den finns bland de hämtade sidorna)."""
    cur = key
    for _ in range(max_hops):
        r = recs.get(cur)
        if not r or not r["redirected"]:
            return cur
        fp = urlsplit(r["final"])
        nxt = (fp.path.rstrip("/") or "/") + ("?" + fp.query if fp.query else "")
        if nxt == cur:
            return cur
        cur = nxt
    return cur


def analyze(recs: dict, blocks: dict, sitemap_urls: set[str], host: str, gsc: list[dict] | None = None, twin_pairs: list[tuple] | None = None) -> dict:
    # 1. kantlista: källa -> mål (region, anchor)
    page_keys = {k: r for k, r in recs.items()}
    pages_by_block = collections.defaultdict(lambda: collections.Counter())   # region -> sig -> antal sidor
    seen_block_pages = set()
    for k, r in recs.items():
        if r["status"] == 200 and not r["redirected"]:
            for region, sig in r["blocks"].items():
                if (region, sig, source_key(k)) not in seen_block_pages:     # ?page=N räknas som samma sida
                    seen_block_pages.add((region, sig, source_key(k)))
                    pages_by_block[region][sig] += 1
    inl_src: dict[str, dict[str, set]] = collections.defaultdict(lambda: collections.defaultdict(set))
    tmpl_cnt: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)    # target -> region -> sidor
    anchors: dict[str, dict[str, collections.Counter]] = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
    anchor_srcs: dict[tuple, set] = collections.defaultdict(set)    # (mål, grupp, text) -> unika källsidor (pagineringssidor räknas som sin kollektion)
    track_rows, malformed_rows = [], []
    bad_family_counts = collections.Counter()
    adj_all: dict[str, set] = collections.defaultdict(set)
    adj_content: dict[str, set] = collections.defaultdict(set)
    target_sources: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)  # mål -> region -> antal sidor
    sample_src: dict[str, list] = collections.defaultdict(list)
    scoped_links = 0
    breadcrumb_targets: dict[tuple, set] = collections.defaultdict(set)   # (källtyp, mål) -> källsidor
    for k, r in recs.items():
        if r["status"] != 200 or r["redirected"]:   # en omdirigerad adress är ingen egen sida; målsidan räknas som källa
            continue
        sk = source_key(k)
        own_final = resolve(recs, k)
        for (target, text, region, section, track, mal) in r["links"]:
            if mal:
                malformed_rows.append((sk, target[10:], region))
                continue
            fam, key = classify_target(target)
            if "/collections/" in target and "/products/" in target:
                scoped_links += 1
            if fam == "other" or fam == "filter":
                bad_family_counts[fam] += 1
                continue
            if key == sk or key == own_final:
                continue
            adj_all[k].add(key)       # djup: en pagineringssida (?page=N) är ett eget steg
            if region not in TEMPLATE_REGIONS:
                adj_content[k].add(key)
            if track:
                track_rows.append((sk, key, region, track))
            if region not in TEMPLATE_REGIONS:
                src_type = page_type(sk)
                cls = region if region in ("brodsmula", "paginering") else "innehall:" + src_type
                inl_src[key][cls].add(sk)
                if region != "paginering":
                    anchor_srcs[(key, "innehall" if region == "brodsmula" else region, text.lower())].add(sk)
                if region == "brodsmula" and fam == "collection":
                    breadcrumb_targets[(src_type, key)].add(sk)
                if len(sample_src[key]) < 3 and sk not in sample_src[key]:
                    sample_src[key].append(sk)
                target_sources[key][region] += 1
    for (key, grp, text), srcs_ in anchor_srcs.items():
        anchors[key][grp][text] += len(srcs_)
    # mallblock: räkna sidor per mål, utan självlänk
    for region, sigs in pages_by_block.items():
        for sig, npages in sigs.items():
            seen_targets = set()
            for (target, text, rg, section, track, mal) in blocks.get(sig, []):
                if mal:
                    malformed_rows.append((f"(mallblock {region}, {npages} sidor)", target[10:], region))
                    continue
                fam, key = classify_target(target)
                if fam in ("other", "filter"):
                    continue
                anchors[key][region][text.lower()] += npages
                if track:
                    track_rows.append(("(mallblock " + region + ", " + str(npages) + " sidor)", key, region, track))
                if key not in seen_targets:
                    seen_targets.add(key)
                    tmpl_cnt[key][region] += npages
    # en sida som själv ligger i sitt mallblock (t.ex. aktuell kollektion i menyn) räknas inte som inlänk till sig själv
    sig_keys = {sig: {classify_target(l[0])[1] for l in lst if not l[5]} for sig, lst in blocks.items()}
    for (region, sig, sk) in seen_block_pages:
        if sk in sig_keys.get(sig, ()) and tmpl_cnt[sk][region] > 0:
            tmpl_cnt[sk][region] -= 1
            anchors_self = [l[1].lower() for l in blocks[sig] if not l[5] and classify_target(l[0])[1] == sk]
            for at in anchors_self:
                if anchors[sk][region][at] > 0:
                    anchors[sk][region][at] -= 1
    # BFS-adjacens: lägg in mallblock per sida
    for k, r in recs.items():
        if r["status"] != 200 or r["redirected"]:
            continue
        for sig in r["blocks"].values():
            for (target, text, rg, section, track, mal) in blocks.get(sig, []):
                if mal:
                    continue
                fam, key = classify_target(target)
                if fam in ("other", "filter") or key == k:
                    continue
                adj_all[k].add(key)

    def bfs(adj):
        depth = {"/": 0}
        frontier = ["/"]
        while frontier:
            nxt = []
            for u in frontier:
                uf = resolve(recs, u)
                nbrs = set(adj.get(u, ()))
                if uf != u:
                    nbrs |= adj.get(uf, set())
                for v in nbrs:
                    for w in {v, resolve(recs, v)}:
                        if w not in depth:
                            depth[w] = depth[u] + 1
                            nxt.append(w)
            frontier = nxt
        return depth

    depth_all = bfs(adj_all)
    depth_content = bfs(adj_content)

    # 2. sidtabell (sitemap-sidor)
    rows = []
    for u in sorted(sitemap_urls | {"/"}):
        r = recs.get(u)
        typ = page_type(u)
        row = {"sida": u, "typ": typ, "status": r["status"] if r else "ej hämtad",
               "omdirigerad": bool(r and r["redirected"]), "i_sitemap": u in sitemap_urls or u == "/"}
        tm = tmpl_cnt.get(u, collections.Counter())
        srcs = inl_src.get(u, {})
        content_cnt = {c: len(s) for c, s in srcs.items()}
        n_content = sum(v for c, v in content_cnt.items() if c.startswith("innehall:") or c == "brodsmula")
        n_pag = content_cnt.get("paginering", 0)
        row.update({"djup_alla_lankar": depth_all.get(u), "djup_utan_meny_sidfot_sidomeny": depth_content.get(u),
                    "inlankar_meny_sidor": tm.get("meny", 0), "inlankar_sidfot_sidor": tm.get("sidfot", 0),
                    "inlankar_overlay_sidor": tm.get("overlay", 0), "inlankar_sidomeny_sidor": tm.get("sidomeny", 0),
                    "inlankar_innehall_sidor": n_content, "inlankar_paginering_sidor": n_pag})
        total_nontemplate = n_content + n_pag
        total_template = sum(tm.values())
        row["inlankar_totalt_unika_sidor"] = total_nontemplate + total_template
        kinds = []
        for rg in ("meny", "sidfot", "overlay", "sidomeny"):
            if tm.get(rg):
                kinds.append(rg)
        for c, v in sorted(content_cnt.items()):
            kinds.append(f"{c}={v}")
        row["orsak_typ_av_lank"] = "; ".join(kinds) if kinds else "ingen inlänk"
        row["foraldralos"] = bool(is_live(r) and typ in ("product", "collection", "page", "article", "blog") and (total_nontemplate + total_template) == 0)
        row["bara_navigation"] = bool(is_live(r) and typ in ("product", "collection", "page", "article", "blog") and total_nontemplate == 0 and total_template > 0
                                      and n_content == 0)
        rows.append(row)

    # 3. djup per sidtyp
    def depth_table(depth):
        tab = {}
        for typ in ("home", "collection", "product", "article", "blog", "page"):
            members = [u for u in sitemap_urls | {"/"} if page_type(u) == typ and is_live(recs.get(u))]
            ds = [depth[u] for u in members if u in depth]
            unreachable = len(members) - len(ds)
            dist = collections.Counter(min(d, 5) for d in ds)
            tab[typ] = {"sidor": len(members), "nadda": len(ds), "onaadda": unreachable,
                        "median": statistics.median(ds) if ds else None, "medel": round(statistics.mean(ds), 2) if ds else None,
                        "max": max(ds) if ds else None, "fordelning": {("5+" if k == 5 else str(k)): dist[k] for k in sorted(dist)}}
        return tab

    # 4. problemlänkar (e)
    problems = []
    all_targets = set(inl_src) | set(tmpl_cnt)
    unchecked = 0
    for t in sorted(all_targets):
        fam, _ = classify_target(t)
        if fam not in FETCH_FAMILIES:
            continue
        r = recs.get(t)
        if r is None or (r["status"] == 0 and "429" in (r.get("error") or "")):   # ej hämtad, eller stoppad av bot-kontrollen
            unchecked += 1
            continue
        why = None
        detail = ""
        if r["redirected"]:
            why = "omdirigerad"
            fin = r["final"]
            detail = f"{r['hops'][0]['status']} -> {urlsplit(fin).path or '/'} (slutstatus {r['status']})"
            if r["status"] != 200:
                why = "omdirigerad till fel"
        elif r["status"] in (404, 410):
            why = f"{r['status']} (finns inte)"
        elif r["status"] >= 400 or r["status"] == 0:
            why = f"fel {r['status'] or r.get('error')}"
        elif is_noindex(r):
            why = "noindex"
        elif canonical_elsewhere(r, host):
            why = "canonical pekar på annan adress"
            detail = r.get("canonical") or ""
        if why:
            reg = collections.Counter()
            for c, s in inl_src.get(t, {}).items():
                reg[c] += len(s)
            for rg, n in tmpl_cnt.get(t, {}).items():
                reg[rg] += n
            problems.append({"mal": t, "problem": why, "detalj": detail, "typ": page_type(t), "i_sitemap": t in sitemap_urls,
                             "antal_kallsidor": sum(reg.values()), "fran": "; ".join(f"{k}={v}" for k, v in sorted(reg.items())),
                             "exempelkallor": " | ".join(sample_src.get(t, []))})
    problems.sort(key=lambda x: -x["antal_kallsidor"])

    # 5. spårningsparametrar (f)
    tr_by_param = collections.Counter()
    tr_by_region = collections.Counter()
    tr_sources = set()
    tr_by_srctype = collections.defaultdict(set)
    for (src, key, region, param) in track_rows:
        tr_by_srctype[page_type(src) if src.startswith("/") else "mallblock"].add(src)
        for p in param.split(","):
            tr_by_param[p] += 1
        tr_by_region[region] += 1
        tr_sources.add(src)

    # 6. kollektionstabell
    colls = sorted(u for u in (sitemap_urls | set(all_targets)) if "?" not in u and page_type(u) == "collection")
    ctab = []
    for u in colls:
        tm = tmpl_cnt.get(u, collections.Counter())
        srcs = inl_src.get(u, {})
        cnt = {c: len(s) for c, s in srcs.items()}
        r = recs.get(u)

        def top(group, n=4):
            c = anchors.get(u, {}).get(group, collections.Counter())
            return " | ".join(f"{a} ({v})" for a, v in c.most_common(n))

        generic = sum(v for g in anchors.get(u, {}).values() for a, v in g.items() if is_generic_anchor(a))
        non_tmpl_anchor_total = sum(sum(c.values()) for g, c in anchors.get(u, {}).items() if g not in TEMPLATE_REGIONS)
        generic_content = sum(v for g, c in anchors.get(u, {}).items() if g not in TEMPLATE_REGIONS for a, v in c.items() if is_generic_anchor(a))
        ctab.append({
            "kollektion": u, "status": r["status"] if r else "ej hämtad", "i_sitemap": u in sitemap_urls,
            "i_meny": tm.get("meny", 0) > 0, "meny_sidor": tm.get("meny", 0), "i_sidfot": tm.get("sidfot", 0) > 0,
            "sidomeny_kallsidor": tm.get("sidomeny", 0),
            "innehall_fran_kollektion": cnt.get("innehall:collection", 0), "innehall_fran_produkt": cnt.get("innehall:product", 0),
            "innehall_fran_artikel": cnt.get("innehall:article", 0) + cnt.get("innehall:blog", 0), "innehall_fran_startsida": cnt.get("innehall:home", 0),
            "innehall_fran_ovrig_sida": cnt.get("innehall:page", 0) + cnt.get("innehall:other", 0),
            "brodsmula_kallsidor": cnt.get("brodsmula", 0), "paginering_kallsidor": cnt.get("paginering", 0),
            "innehall_totalt": sum(v for c, v in cnt.items() if c.startswith("innehall:") or c == "brodsmula"),
            "ankare_meny": top("meny"), "ankare_sidfot": top("sidfot"), "ankare_sidomeny": top("sidomeny"),
            "ankare_innehall": top("innehall"), "generiska_ankare_innehall": generic_content, "ankare_innehall_totalt": non_tmpl_anchor_total,
            "djup": depth_all.get(u), "djup_utan_navigation": depth_content.get(u),
        })
    # 7. tvillingar (g)
    twins = []
    for base_h, se_h in (twin_pairs or []):
        for h in (base_h, se_h):
            if h is None:
                continue
            u = "/collections/" + h
            r = recs.get(u)
            tm = tmpl_cnt.get(u, collections.Counter())
            cnt = {c: len(s) for c, s in inl_src.get(u, {}).items()}
            twins.append({"par": (base_h or "") + " / " + (se_h or ""), "handle": h, "roll": "-se" if h.endswith("-se") else "bas",
                          "status": r["status"] if r else "ej hämtad", "omdirigerad_till": (urlsplit(r["final"]).path if r and r["redirected"] else ""),
                          "i_sitemap": u in sitemap_urls, "canonical": canonical_path(r.get("canonical"), host) if r else None,
                          "noindex": is_noindex(r) if r else None, "titel": (r or {}).get("title"), "h1": (r or {}).get("h1"),
                          "i_meny": tm.get("meny", 0) > 0, "i_sidfot": tm.get("sidfot", 0) > 0, "sidomeny_kallsidor": tm.get("sidomeny", 0),
                          "innehall_kallsidor": sum(v for c, v in cnt.items() if c.startswith("innehall:") or c == "brodsmula"),
                          "ankare_meny": " | ".join(f"{a} ({v})" for a, v in anchors.get(u, {}).get("meny", collections.Counter()).most_common(3))})
    generic_anchor_counts = collections.Counter()
    for t, gs in anchors.items():
        if page_type(t.split("?")[0]) != "collection":
            continue
        for g, c in gs.items():
            if g in TEMPLATE_REGIONS:
                continue
            for a, v in c.items():
                if is_generic_anchor(a):
                    generic_anchor_counts[a] += v
    return {"breadcrumb_targets": sorted(((st, t, len(v)) for (st, t), v in breadcrumb_targets.items()), key=lambda x: -x[2]),
            "generic_anchors": generic_anchor_counts.most_common(), "rows": rows, "depth_all": depth_table(depth_all), "depth_content": depth_table(depth_content), "problems": problems,
            "unchecked_targets": unchecked, "tracking": {"lankar": len(track_rows), "per_parameter": dict(tr_by_param), "per_region": dict(tr_by_region),
                                                          "kallsidor": len(tr_sources), "kallsidor_per_typ": {k: len(v) for k, v in tr_by_srctype.items()}, "exempel": [list(x) for x in track_rows[:15]]},
            "malformed": malformed_rows, "collections": ctab, "twins": twins, "scoped_product_links": scoped_links,
            "ignored_link_families": dict(bad_family_counts),
            "anchors_long": [(t, g, a, v) for t, gs in anchors.items() if page_type(t.split("?")[0]) == "collection" for g, c in gs.items() for a, v in c.items()]}


# -------------------------------------------------------------------------------------------- utskrifter
def write_csv(path: str, rows: list[dict], fields: list[str] | None = None):
    fields = fields or (list(rows[0].keys()) if rows else [])
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: ("ja" if v is True else "nej" if v is False else ("" if v is None else v)) for k, v in r.items()})


def load_gsc(path: str) -> list[dict]:
    out = []
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            out.append({"handle": r["handle"].strip(), "visningar": int(r["visningar"]), "position": float(str(r["position"]).replace(",", "."))})
    return out


def weakest_visible(ctab: list[dict], gsc: list[dict]) -> list[dict]:
    by = {c["kollektion"].replace("/collections/", ""): c for c in ctab}
    out = []
    for g in gsc:
        c = by.get(g["handle"])
        if not c:
            out.append({**g, "status": "finns ej bland mätta kollektioner"})
            continue
        out.append({**g, "status": c["status"], "i_meny": c["i_meny"], "sidomeny_kallsidor": c["sidomeny_kallsidor"],
                    "innehall_totalt": c["innehall_totalt"], "innehall_fran_kollektion": c["innehall_fran_kollektion"],
                    "innehall_fran_produkt": c["innehall_fran_produkt"], "innehall_fran_artikel": c["innehall_fran_artikel"],
                    "djup_utan_navigation": c["djup_utan_navigation"], "ankare_innehall": c["ankare_innehall"]})
    out.sort(key=lambda x: (x.get("innehall_totalt", -1) if isinstance(x.get("innehall_totalt"), int) else -1, -x["visningar"]))
    return out


def md_table(header: list[str], rows: list[list]) -> str:
    out = ["| " + " | ".join(header) + " |", "|" + "|".join("---" for _ in header) + "|"]
    for r in rows:
        out.append("| " + " | ".join("" if v is None else str(v) for v in r) + " |")
    return "\n".join(out)


def matvarden_md(res: dict, recs: dict, meta: dict, gsc_rows: list[dict] | None) -> str:
    """Alla siffror i rapporten, genererade ur körningen (ingen handskriven siffra)."""
    L = []
    rows, ctab = res["rows"], res["collections"]
    sm_types = meta.get("sitemap_per_typ", {})
    L.append("# Mätvärden (genererade av `intern_lankning_mat.py`)\n")
    L.append(f"Körning: {meta.get('start')} till {meta.get('slut')} ({meta.get('sekunder')} s), högst {meta.get('hastighet_anrop_per_sekund_max')} anrop/s i den fullbordade omgången. "
             f"Sitemap: {meta.get('sitemap_adresser')} adresser ({', '.join(f'{k} {v}' for k, v in sorted(sm_types.items()))}). "
             f"Hämtade sidor totalt: {meta.get('hamtade_sidor')} (inklusive pagineringssidor). Produkturval: {meta.get('produkturval')}. "
             f"Hoppade över sidtyper: {', '.join(meta.get('hoppade_over_sidtyper') or []) or 'inga'}.\n")
    st = collections.Counter(r["status"] for r in recs.values())
    L.append("Statuskoder bland hämtade sidor: " + ", ".join(f"{k}: {v}" for k, v in sorted(st.items(), key=lambda x: str(x[0]))) + ".\n")
    L.append(f"Länkmål inom hämtade familjer som inte hämtades (bloggartiklar och blogtaggar): {res['unchecked_targets']}.\n")
    # (a)
    L.append("\n## (a) Föräldralösa sidor (i sitemap, svarar 200, ingen inlänk från någon hämtad sida, inte ens meny)\n")
    t = collections.defaultdict(lambda: [0, 0, 0])
    for r in rows:
        t[r["typ"]][0] += 1
        t[r["typ"]][1] += 1 if r["foraldralos"] else 0
        t[r["typ"]][2] += 1 if r["bara_navigation"] else 0
    L.append(md_table(["Sidtyp", "Sidor i sitemap", "Föräldralösa", "Bara meny/sidfot/sidomeny (ingen innehållslänk)"],
                      [[k, v[0], v[1], v[2]] for k, v in sorted(t.items())]))
    orph = [r["sida"] for r in rows if r["foraldralos"] and r["typ"] != "collection"]
    L.append("\n\nFöräldralösa sidor som inte är kollektioner: " + (", ".join(orph) if orph else "inga") + ".")
    # (b)
    for key, title in (("depth_all", "alla länkar (inklusive meny, sidfot och sidomeny)"),
                       ("depth_content", "utan meny, sidfot, varukorgsruta och sidomeny (bara länkar i sidans innehåll)")):
        L.append(f"\n\n## (b) Klickdjup från startsidan, {title}\n")
        L.append(md_table(["Sidtyp", "Sidor", "Nåbara", "Onåbara", "Median", "Medel", "Max", "Fördelning (djup: antal)"],
                          [[k, v["sidor"], v["nadda"], v["onaadda"], v["median"], v["medel"], v["max"],
                            ", ".join(f"{d}: {n}" for d, n in v["fordelning"].items())] for k, v in res[key].items()]))
    # (c)
    live = [c for c in ctab if c["status"] == 200]
    in_nav = [c for c in live if c["i_meny"] or c["sidomeny_kallsidor"] > 0]
    L.append("\n\n## (c) Inlänkar till kollektioner\n")
    L.append(f"Kollektioner som svarar 200: {len(live)} (sitemap: {sum(1 for c in live if c['i_sitemap'])}). Länkade från huvudmenyn: {sum(1 for c in live if c['i_meny'])}. "
             f"Länkade från sidomenyn på kollektionssidor: {sum(1 for c in live if c['sidomeny_kallsidor'] > 0)}. Länkade från sidfoten: {sum(1 for c in live if c['i_sidfot'])}. "
             f"Länkade från meny eller sidomeny: {len(in_nav)}; inte i någon meny: {len(live) - len(in_nav)}.\n")
    def bucket(n):
        return "0" if n == 0 else "1" if n == 1 else "2-4" if n <= 4 else "5-9" if n <= 9 else "10+"
    dist = collections.Counter((("i meny/sidomeny" if (c["i_meny"] or c["sidomeny_kallsidor"] > 0) else "inte i meny"), bucket(c["innehall_totalt"])) for c in live)
    L.append("Antal unika innehållskällor per kollektion (kollektionssidor, produkt-brödsmula, artiklar, startsida, övriga sidor; utan meny, sidfot, sidomeny och paginering):\n")
    L.append(md_table(["", "0", "1", "2-4", "5-9", "10+"], [[g] + [dist.get((g, b), 0) for b in ("0", "1", "2-4", "5-9", "10+")] for g in ("i meny/sidomeny", "inte i meny")]))
    L.append(f"\n\nKollektioner som får minst en innehållslänk från: kollektionssida {sum(1 for c in live if c['innehall_fran_kollektion'])}, produktsida (brödsmula) {sum(1 for c in live if c['brodsmula_kallsidor'])}, "
             f"produktsida (annan länk) {sum(1 for c in live if c['innehall_fran_produkt'])}, bloggartikel {sum(1 for c in live if c['innehall_fran_artikel'])}, startsida {sum(1 for c in live if c['innehall_fran_startsida'])}, "
             f"övrig sida {sum(1 for c in live if c['innehall_fran_ovrig_sida'])}.\n")
    L.append("\nProduktsidornas brödsmula (produkt till kollektion) pekar på dessa kollektioner:\n")
    bc = [b for b in res["breadcrumb_targets"] if b[0] == "product"]
    L.append(md_table(["Kollektion", "Antal produktsidor"], [[b[1], b[2]] for b in bc[:12]]) if bc else "Inga.")
    top = sorted(live, key=lambda c: -c["innehall_totalt"])[:10]
    L.append("\n\nTio kollektioner med flest innehållskällor:\n")
    L.append(md_table(["Kollektion", "Innehållskällor", "Varav kollektion", "Varav bloggartikel", "I meny"], [[c["kollektion"], c["innehall_totalt"], c["innehall_fran_kollektion"], c["innehall_fran_artikel"], "ja" if c["i_meny"] else "nej"] for c in top]))
    # (d)
    L.append("\n\n## (d) Ankartexter till kollektioner\n")
    gen = res["generic_anchors"]
    L.append(f"Generiska ankartexter i innehållslänkar till kollektioner (summerat över källsidor): {sum(v for _, v in gen)}; "
             f"kollektioner med minst en: {sum(1 for c in live if c['generiska_ankare_innehall'] > 0)}. Texter: " + (", ".join(f"'{a}' ({v})" for a, v in gen[:10]) or "inga") + ".")
    kinds = collections.Counter()
    for t, g, a, v in res["anchors_long"]:
        if g in TEMPLATE_REGIONS:
            continue
        kinds["tom" if a == "(tom)" else "bild (alt-text)" if a.startswith("[bild]") else "aria/title" if a.startswith(("[aria]", "[title]")) else "text"] += v
    L.append("\nInnehållslänkar till kollektioner efter ankartextens källa (summerat över källsidor): " + ", ".join(f"{k} {v}" for k, v in sorted(kinds.items())) + ".")
    all_generic = [c["kollektion"] for c in live if c["ankare_innehall_totalt"] > 0 and c["generiska_ankare_innehall"] == c["ankare_innehall_totalt"]]
    L.append(f"\nKollektioner där alla innehållslänkar har generisk ankartext: {len(all_generic)}" + (" (" + ", ".join(all_generic[:15]) + ")" if all_generic else "") + ".")
    # (e)
    L.append("\n\n## (e) Länkar till omdirigerade, saknade eller icke-indexerbara sidor\n")
    if res["problems"]:
        L.append(md_table(["Mål", "Problem", "Detalj", "Källsidor", "Från", "Exempelkällor"], [[p["mal"], p["problem"], p["detalj"], p["antal_kallsidor"], p["fran"], p["exempelkallor"]] for p in res["problems"][:30]]))
    else:
        L.append("Inga.")
    nred = sum(1 for r in recs.values() if r["redirected"])
    L.append(f"\n\nAntal hämtade adresser som omdirigerar: {nred}. Felformade länkadresser (mallkod i href): {len(res['malformed'])}. Länkar till /collections/x/products/y: {res['scoped_product_links']}.")
    # (f)
    tr = res["tracking"]
    L.append("\n\n## (f) Interna länkar med spårningsparametrar\n")
    L.append(f"Länkar: {tr['lankar']} från {tr['kallsidor']} källsidor. Per parameter: " + ", ".join(f"{k} {v}" for k, v in sorted(tr["per_parameter"].items())) +
             ". Per region: " + ", ".join(f"{k} {v}" for k, v in tr["per_region"].items()) +
             ". Källsidor per sidtyp: " + ", ".join(f"{k} {v}" for k, v in sorted(tr["kallsidor_per_typ"].items())) + ".\n\nExempel (källa, mål, region, parametrar):\n")
    L.append(md_table(["Källa", "Mål", "Region", "Parametrar"], tr["exempel"][:8]))
    # (g)
    L.append("\n\n## (g) Tvillingkollektioner med ändelsen -se\n")
    L.append(md_table(["Par", "Handle", "Roll", "Status", "I sitemap", "Canonical", "I meny", "Innehållskällor"],
                      [[t["par"], t["handle"], t["roll"], t["status"], "ja" if t["i_sitemap"] else "nej", t["canonical"] or "", "ja" if t["i_meny"] else "nej", t["innehall_kallsidor"]] for t in res["twins"]]))
    se_in_sm = [u for u in meta.get("sitemap_urls", []) if u.split("?")[0].endswith("-se")]
    L.append(f"\n\nAdresser i sitemapen som slutar på -se: {len(se_in_sm)}" + (" (" + ", ".join(se_in_sm[:10]) + ")" if se_in_sm else "") + ".")
    # (h)
    if gsc_rows:
        L.append("\n\n## (h) Search Console-mest synliga kollektioner, sorterade efter svagast länkning\n")
        L.append(md_table(["Handle", "Visningar", "Position", "Status", "I meny", "Innehållskällor", "Varav kollektion", "Varav övriga (start, produkt, sida)", "Varav artikel", "Djup utan navigation", "Vanligaste ankartexter i innehållet (antal källor)"],
                          [[g["handle"], g["visningar"], g["position"], g.get("status"), "ja" if g.get("i_meny") else "nej", g.get("innehall_totalt"), g.get("innehall_fran_kollektion"),
                            (g.get("innehall_totalt", 0) or 0) - (g.get("innehall_fran_kollektion", 0) or 0) - (g.get("innehall_fran_artikel", 0) or 0), g.get("innehall_fran_artikel"), g.get("djup_utan_navigation"), (g.get("ankare_innehall") or "").replace(" | ", " / ")] for g in gsc_rows]))
    return "\n".join(L) + "\n"


KOSTTILLSKOTT_ORD = ("protein", "pre-workout", "gainer", "kosttillskott", "aminosyr", "kreatin", "creatin", "bcaa", "vitamin")
BARN_ORD = ("barn", "junior")


def urval_gruppsidor(ctab: list[dict]) -> list[dict]:
    """Kollektioner vars handle innehåller något av orden ovan (grov heuristik på namnet, inte på sortimentet)."""
    out = []
    for c in ctab:
        h = c["kollektion"].replace("/collections/", "")
        grupp = "kosttillskott" if any(w in h for w in KOSTTILLSKOTT_ORD) else "barn/junior" if any(w in h for w in BARN_ORD) else None
        if grupp:
            out.append({"grupp": grupp, "kollektion": c["kollektion"], "status": c["status"], "i_meny": c["i_meny"], "innehall_totalt": c["innehall_totalt"],
                        "innehall_fran_kollektion": c["innehall_fran_kollektion"], "innehall_fran_artikel": c["innehall_fran_artikel"]})
    return sorted(out, key=lambda x: (x["grupp"], x["innehall_totalt"]))


TWIN_DEFAULT = [("pre-workout-pwo", "pre-workout-pwo-se"), ("elcyklar", "elcyklar-se"), ("kettlebell", "kettlebell-se"),
                ("hybridcykel", "hybridcykel-se"), ("racercykel", "racercykel-se"), ("ladcyklar", "ladcyklar-se"),
                ("skyddsutrustning-cykel", "skyddsutrustning-cykel-se"), ("pedaler-cykel", "pedaler-cykel-se"),
                ("cykeltillbehor", "cykeltillbehor-se"), ("barncyklar", "barncyklar-se"), ("gainers", "gainers-se"),
                ("proteinpulver", "proteinpulver-se"), ("parallettes", "parallettes-se"), (None, "skivstanger-se"), (None, "cykelglasogon-se")]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("crawl")
    c.add_argument("--bas", required=True)
    c.add_argument("--ut", required=True)
    c.add_argument("--hastighet", type=float, default=2.5, help=f"anrop per sekund (högst {MAX_RPS})")
    c.add_argument("--producter", default="all", help="'all' eller antal i slumpmässigt urval")
    c.add_argument("--seed", type=int, default=1)
    c.add_argument("--tid-min", type=float, default=None)
    c.add_argument("--hoppa-over", default="", help="kommaseparerade sidtyper som inte hämtas (t.ex. article)")
    a = sub.add_parser("analysera")
    a.add_argument("--bas", required=True)
    a.add_argument("--ut", required=True)
    a.add_argument("--rapport", required=True)
    a.add_argument("--gsc", default=None)
    args = ap.parse_args(argv)
    host = urlsplit(args.bas).hostname.lower()
    if args.cmd == "crawl":
        rps = min(args.hastighet, MAX_RPS)
        pf = PoliteFetcher(Fetcher(USER_AGENT, rps))
        twin_urls = ["/collections/" + h for pair in TWIN_DEFAULT for h in pair if h]
        meta = crawl(args.bas, args.ut, pf, rps=rps, products=args.producter, seed=args.seed, deadline_min=args.tid_min, extra_seeds=twin_urls,
                     skip_types=tuple(x for x in args.hoppa_over.split(",") if x))
        print(json.dumps({k: v for k, v in meta.items() if k != "sitemap_urls"}, ensure_ascii=False, indent=1))
        return 0 if not meta["stopp"] else 2
    recs, blocks, meta = load_run(args.ut)
    sm = set(meta.get("sitemap_urls", []))
    gsc = load_gsc(args.gsc) if args.gsc else None
    res = analyze(recs, blocks, sm, host, gsc, TWIN_DEFAULT)
    os.makedirs(args.rapport, exist_ok=True)
    fields = ["sida", "typ", "status", "omdirigerad", "i_sitemap", "djup_alla_lankar", "djup_utan_meny_sidfot_sidomeny", "inlankar_totalt_unika_sidor",
              "inlankar_meny_sidor", "inlankar_sidfot_sidor", "inlankar_overlay_sidor", "inlankar_sidomeny_sidor", "inlankar_innehall_sidor",
              "inlankar_paginering_sidor", "foraldralos", "bara_navigation", "orsak_typ_av_lank"]
    write_csv(os.path.join(args.rapport, "sidor.csv"), res["rows"], fields)
    write_csv(os.path.join(args.rapport, "kollektioner.csv"), res["collections"])
    write_csv(os.path.join(args.rapport, "lankproblem.csv"), res["problems"])
    write_csv(os.path.join(args.rapport, "tvillingar.csv"), res["twins"])
    al = [{"kollektion": t, "ursprung": g, "ankartext": a, "antal_kallsidor": v, "generisk": is_generic_anchor(a)} for t, g, a, v in res["anchors_long"]]
    al.sort(key=lambda x: (x["kollektion"], x["ursprung"], -x["antal_kallsidor"]))
    write_csv(os.path.join(args.rapport, "ankartexter.csv"), al, ["kollektion", "ursprung", "ankartext", "antal_kallsidor", "generisk"])
    write_csv(os.path.join(args.rapport, "kosttillskott-barn-junior.csv"), urval_gruppsidor(res["collections"]))
    gsc_rows = weakest_visible(res["collections"], gsc) if gsc else None
    if gsc_rows:
        write_csv(os.path.join(args.rapport, "gsc-svagast-lankade.csv"), gsc_rows)
    with open(os.path.join(args.rapport, "matvarden.md"), "w", encoding="utf-8") as f:
        f.write(matvarden_md(res, recs, meta, gsc_rows))
    summary = {k: v for k, v in res.items() if k not in ("rows", "collections", "problems", "anchors_long", "twins", "malformed", "breadcrumb_targets", "generic_anchors")}
    summary["antal_problem"] = len(res["problems"])
    summary["antal_felformade_lankar"] = len(res["malformed"])
    summary["meta"] = {k: v for k, v in meta.items() if k != "sitemap_urls"}
    with open(os.path.join(args.rapport, "matvarden.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=1)
    print(json.dumps({k: summary[k] for k in ("depth_all", "depth_content", "tracking", "antal_problem", "unchecked_targets")}, ensure_ascii=False)[:3000])
    return 0


if __name__ == "__main__":
    sys.exit(main())
