"""Crawlar en sajt: sitemaps först, sedan interna länkar till begränsat djup.
Varje URL sparas med statuskod, omdirigeringskedja och sidfakta."""

from __future__ import annotations

import logging
import re
import time
from collections.abc import Iterable
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from urllib.parse import urlsplit, urlunsplit

from .config import SiteConfig
from .fetch import INVALID_TARGET, FetchResult, Fetcher, RateLimiter
from .html_parse import PageFacts, parse_page
from .sitemap import SitemapResult, read_sitemaps

log = logging.getLogger(__name__)


@dataclass
class CrawledUrl:
    url: str
    source: str              # "sitemap", "link", "seed", "redirect_target", "admin_redirect"
    depth: int
    status: int
    final_url: str
    hops: list[dict[str, Any]]
    error: str | None
    loop: bool
    elapsed_ms: int
    content_type: str
    x_robots_tag: str | None
    in_sitemap: bool = False
    sitemap: str | None = None
    facts: PageFacts | None = None
    linked_from: list[str] = field(default_factory=list)

    @property
    def redirect_count(self) -> int:
        return max(0, len(self.hops) - 1)

    def to_row(self) -> dict[str, Any]:
        row = {
            "url": self.url, "source": self.source, "depth": self.depth, "status": self.status,
            "final_url": self.final_url, "redirect_count": self.redirect_count, "hops": self.hops,
            "error": self.error, "loop": self.loop, "elapsed_ms": self.elapsed_ms,
            "content_type": self.content_type, "x_robots_tag": self.x_robots_tag,
            "in_sitemap": self.in_sitemap, "sitemap": self.sitemap,
            "linked_from_count": len(self.linked_from), "linked_from_sample": self.linked_from[:5],
        }
        if self.facts:
            row.update(self.facts.to_dict())
        return row


@dataclass
class GeoProbe:
    profile: str
    path: str
    status: int
    final_url: str
    hops: list[dict[str, Any]]


@dataclass
class CrawlResult:
    site: str
    started_at: str
    finished_at: str | None
    sitemap: SitemapResult
    urls: dict[str, CrawledUrl]
    geo: list[GeoProbe]
    robots_txt: str | None = None


# Kundkonto, kassa och varukorg: privata sidor som alltid omdirigerar och inte ska granskas.
PRIVATE_PATHS = re.compile(r"^(/[a-z]{2}(-[a-z]{2})?)?/(customer_authentication|account|cart|checkouts?)(/|$)", re.I)
RETRY_MAX = 500

TRACKING_PARAMS = re.compile(r"^(pr_[a-z_]+|shpxid|_pos|_sid|_psid|_ss|_psq|_v|_fid|srsltid|gclid|fbclid|utm_[a-z]+|variant)$", re.I)
# I omdirigeringsmål kan variant= vara avsiktligt (en viss storlek eller färg) och behålls.
REDIRECT_TRACKING_PARAMS = re.compile(r"^(pr_[a-z_]+|shpxid|_pos|_sid|_psid|_ss|_psq|_v|_fid|srsltid|gclid|fbclid|utm_[a-z]+)$", re.I)


def normalize_url(url: str) -> str:
    """Normaliserar och tar bort Shopifys rekommendations- och spårningsparametrar."""
    from urllib.parse import parse_qsl, urlencode

    p = urlsplit(url)
    path = p.path or "/"
    if path != "/" and path.endswith("/"):
        path = path.rstrip("/")
    query = urlencode([(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True) if not TRACKING_PARAMS.match(k)])
    return urlunsplit((p.scheme.lower(), p.netloc.lower(), path, query, ""))


def strip_tracking(url: str, pattern: re.Pattern = REDIRECT_TRACKING_PARAMS) -> str:
    """Tar bort spårningsparametrar men behåller resten av adressen som den är."""
    from urllib.parse import parse_qsl, urlencode

    p = urlsplit(url)
    query = urlencode([(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True) if not pattern.match(k)])
    return urlunsplit((p.scheme, p.netloc, p.path, query, p.fragment))


def interleave_by_sitemap(sm: SitemapResult) -> list[str]:
    """Varvar URL:er från varje sitemap (produkter, kollektioner, sidor, språk), så att en
    begränsad crawl ändå täcker alla sidtyper och språk."""
    buckets: dict[str, list[str]] = {}
    for e in sm.entries:
        buckets.setdefault(e.sitemap, []).append(normalize_url(e.url))
    out, seen = [], set()
    lists = list(buckets.values())
    i = 0
    while any(i < len(l) for l in lists):
        for l in lists:
            if i < len(l) and l[i] not in seen:
                seen.add(l[i])
                out.append(l[i])
        i += 1
    return out


def _hops(res: FetchResult) -> list[dict[str, Any]]:
    return [{"url": h.url, "status": h.status, "location": h.location} for h in res.hops]


class Crawler:
    def __init__(self, site: SiteConfig, fetcher: Fetcher | None = None):
        self.site = site
        s = site.crawl
        self.fetcher = fetcher or Fetcher(s.user_agent, s.requests_per_second, s.timeout_s)
        self.include = [re.compile(p) for p in s.include_patterns]
        self.exclude = [re.compile(p) for p in s.exclude_patterns]
        self.retry_cooldown_s = 30.0
        self.retry_rps = 1.0

    def allowed(self, url: str) -> bool:
        p = urlsplit(url)
        if p.netloc.lower() != self.site.host:
            return False
        if PRIVATE_PATHS.match(p.path):
            return False
        target = p.path + ("?" + p.query if p.query else "")
        if any(rx.search(target) for rx in self.exclude):
            return False
        if self.include and not any(rx.search(target) for rx in self.include):
            return False
        return True

    def _crawl_one(self, url: str, source: str, depth: int) -> CrawledUrl:
        res = self.fetcher.fetch(url)
        cu = CrawledUrl(
            url=url, source=source, depth=depth, status=res.status, final_url=normalize_url(res.final_url),
            hops=_hops(res), error=res.error, loop=res.loop, elapsed_ms=res.elapsed_ms,
            content_type=res.content_type, x_robots_tag=res.headers.get("x-robots-tag"),
        )
        # Omdirigerade URL:er analyseras inte; målet crawlas separat och räknas en gång.
        if res.status == 200 and res.is_html and res.body and not res.redirect_count:
            try:
                cu.facts = parse_page(res.final_url, res.body, self.site.host)
            except Exception:  # en trasig sida ska inte stoppa hela crawlen
                log.exception("Kunde inte tolka %s", url)
        return cu

    def crawl(self, extra_urls: Iterable[tuple[str, str]] = ()) -> CrawlResult:
        started = datetime.now(timezone.utc).isoformat()
        base = self.site.base_url
        robots = self.fetcher.fetch(base + "/robots.txt")
        sm = read_sitemaps(self.fetcher, base + "/sitemap.xml")
        log.info("%s: %d URL:er i %d sitemaps", self.site.name, len(sm.entries), len(sm.sitemaps))

        results: dict[str, CrawledUrl] = {}
        sitemap_map = {normalize_url(e.url): e for e in sm.entries}
        frontier: list[tuple[str, str, int]] = [(normalize_url(base + "/"), "seed", 0)]
        frontier += [(u, "sitemap", 0) for u in interleave_by_sitemap(sm)]
        frontier += [(normalize_url(u), src, 0) for u, src in extra_urls]
        queued: set[str] = set()
        links_from: dict[str, set[str]] = {}
        max_pages = self.site.crawl.max_pages

        with ThreadPoolExecutor(max_workers=self.site.crawl.concurrency) as pool:
            while frontier and len(results) < max_pages:
                batch = []
                for url, src, depth in frontier:
                    if url in queued or url in results:
                        continue
                    if src in ("link", "redirect_target") and not self.allowed(url):
                        continue
                    queued.add(url)
                    batch.append((url, src, depth))
                    if len(results) + len(batch) >= max_pages:
                        break
                frontier = []
                futures = {pool.submit(self._crawl_one, u, s, d): (u, s, d) for u, s, d in batch}
                for fut in as_completed(futures):
                    u, s, d = futures[fut]
                    cu = fut.result()
                    entry = sitemap_map.get(u)
                    if entry:
                        cu.in_sitemap, cu.sitemap = True, entry.sitemap
                    results[u] = cu
                    # Följ slutmålet för omdirigeringar så att målsidan också granskas.
                    if cu.redirect_count and cu.final_url not in results:
                        frontier.append((cu.final_url, "redirect_target", d))
                    if cu.facts and self.site.crawl.follow_internal_links and d < self.site.crawl.max_link_depth:
                        for link in cu.facts.internal_links:
                            nl = normalize_url(link)
                            links_from.setdefault(nl, set()).add(u)
                            if nl not in results:
                                frontier.append((nl, "link", d + 1))
                    elif cu.facts:
                        for link in cu.facts.internal_links:
                            links_from.setdefault(normalize_url(link), set()).add(u)
        self._retry_failed(results)
        for url, sources in links_from.items():
            if url in results:
                results[url].linked_from = sorted(sources)

        geo = self.geo_probe()
        return CrawlResult(self.site.name, started, datetime.now(timezone.utc).isoformat(), sm, results, geo,
                           robots.body.decode(errors="replace") if robots.status == 200 else None)

    def _retry_failed(self, results: dict[str, CrawledUrl]) -> None:
        """Hämtar om URL:er som föll på 429 eller nätverksfel, efter en paus och i lägre takt."""
        failed = [cu for cu in results.values()
                  if cu.status == 0 and not cu.loop and not (cu.error or "").startswith(INVALID_TARGET)][:RETRY_MAX]
        if not failed:
            return
        log.info("%s: hämtar om %d URL:er som misslyckades", self.site.name, len(failed))
        time.sleep(self.retry_cooldown_s)
        old = self.fetcher.limiter
        self.fetcher.limiter = RateLimiter(self.retry_rps)
        try:
            for cu in failed:
                new = self._crawl_one(cu.url, cu.source, cu.depth)
                if new.status == 0:
                    continue
                new.in_sitemap, new.sitemap = cu.in_sitemap, cu.sitemap
                results[cu.url] = new
        finally:
            self.fetcher.limiter = old

    def geo_probe(self) -> list[GeoProbe]:
        probes = []
        for profile in self.site.geo_profiles:
            headers = {"Accept-Language": profile.accept_language}
            cookies = {"localization": profile.country_cookie} if profile.country_cookie else None
            for path in self.site.crawl.geo_probe_paths:
                res = self.fetcher.fetch(self.site.base_url + path, headers=headers, cookies=cookies, read_body=False)
                probes.append(GeoProbe(profile.name, path, res.status, res.final_url, _hops(res)))
        return probes
