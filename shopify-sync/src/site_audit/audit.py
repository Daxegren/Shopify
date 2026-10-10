"""Kör en hel genomlysning för en sajt: admin-data, crawl, kontroller, rapport och lagring."""

from __future__ import annotations

import json
import logging
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .checks import run_admin_checks, run_crawl_checks, run_cross_checks
from .config import SiteConfig
from .crawler import Crawler, CrawlResult
from .findings import Finding, sort_findings, summarize
from .shopify_admin import AdminData, fetch_admin_data

log = logging.getLogger(__name__)


@dataclass
class AuditRun:
    run_id: str
    site: SiteConfig
    started_at: str
    finished_at: str | None = None
    crawl: CrawlResult | None = None
    admin: AdminData | None = None
    findings: list[Finding] = field(default_factory=list)
    search: Any = None  # SearchData när --search-data används

    def summary(self) -> dict[str, Any]:
        s = summarize(self.findings)
        s["run_id"] = self.run_id
        s["site"] = self.site.name
        s["started_at"] = self.started_at
        s["finished_at"] = self.finished_at
        if self.crawl:
            urls = self.crawl.urls.values()
            s["crawl"] = {
                "urls": len(self.crawl.urls),
                "sitemap_urls": len(self.crawl.sitemap.entries),
                "sitemaps": len(self.crawl.sitemap.sitemaps),
                "status_200": sum(1 for u in urls if u.status == 200 and not u.redirect_count),
                "redirected": sum(1 for u in urls if u.redirect_count),
                "errors_4xx": sum(1 for u in urls if 400 <= u.status < 500),
                "errors_5xx": sum(1 for u in urls if u.status >= 500),
            }
        if self.admin:
            s["admin"] = self.admin.counts()
        return s


def _shopify_client(site: SiteConfig):
    token = site.shopify_token()
    if not site.shop_domain or not token:
        return None
    from shopify_sync.config import ShopifyConfig
    from shopify_sync.shopify_client import ShopifyClient

    return ShopifyClient(ShopifyConfig(site.shop_domain, site.api_version, token, None, None))


def reconcile_redirect_targets(findings: list[Finding], crawl: CrawlResult) -> list[Finding]:
    """Admin-kontrollen ser bara primära handles. Ett mål kan ändå fungera (översatt handle,
    Shopifys automatiska omdirigering), så crawlens utfall avgör: 200 = inget fel, fel = kvar,
    ej hämtad = sänkt till 'kunde inte verifieras'."""
    from .crawler import normalize_url

    out = []
    for f in findings:
        if f.check != "redirect_target_missing" or not f.url:
            out.append(f)
            continue
        cu = crawl.urls.get(normalize_url(f.url))
        if cu is None:
            out.append(f)
        elif cu.status == 200:
            continue
        elif cu.status == 0:
            f.severity, f.check = "low", "redirect_target_unverified"
            f.message = "Omdirigeringens mål saknas i admin och kunde inte verifieras i crawlen"
            out.append(f)
        else:
            f.evidence["crawl_status"] = cu.status
            out.append(f)
    return out


def run_audit(site: SiteConfig, crawl: bool = True, admin: bool = True, admin_client=None, crawler: Crawler | None = None,
              search_store=None, search_days: int = 90, psi_per_type: int = 0) -> AuditRun:
    run = AuditRun(run_id=f"{site.name}-{datetime.now(timezone.utc):%Y%m%dT%H%M%S}-{uuid.uuid4().hex[:6]}",
                   site=site, started_at=datetime.now(timezone.utc).isoformat())
    if admin:
        client = admin_client or _shopify_client(site)
        if client is None:
            log.warning("%s: ingen Shopify-token (%s) – hoppar över admin-delen", site.name, site.shopify_token_env)
        else:
            run.admin = fetch_admin_data(client)
            run.findings += run_admin_checks(run.admin, site)
    if crawl:
        extra = [(site.base_url + r["path"], "admin_redirect") for r in (run.admin.redirects if run.admin else [])]
        run.crawl = (crawler or Crawler(site)).crawl(extra)
        run.findings += run_crawl_checks(run.crawl, site)
        if run.admin:
            run.findings += run_cross_checks(run.crawl, run.admin, site)
            run.findings = reconcile_redirect_targets(run.findings, run.crawl)
        if psi_per_type:
            from .psi import psi_findings

            run.findings += psi_findings(run.crawl, psi_per_type)
        if search_store is not None and site.gsc_table:
            from .checks.data_checks import fetch_search_data, run_data_checks

            try:
                sd = fetch_search_data(search_store, site, search_days)
                run.search = sd
                run.findings += run_data_checks(run.crawl, sd, site)
            except Exception:  # noqa: BLE001 - sökdata är ett tillägg, inte ett krav
                log.exception("%s: Search Console-data kunde inte hämtas", site.name)
    run.findings = sort_findings(run.findings)
    run.finished_at = datetime.now(timezone.utc).isoformat()
    return run


def save_local(run: AuditRun, out_dir: str | Path) -> Path:
    """Sparar råa resultat som JSON/JSONL så att körningen kan analyseras eller laddas upp senare."""
    d = Path(out_dir) / run.run_id
    d.mkdir(parents=True, exist_ok=True)
    (d / "summary.json").write_text(json.dumps(run.summary(), ensure_ascii=False, indent=2))
    with open(d / "findings.jsonl", "w") as fh:
        for f in run.findings:
            fh.write(json.dumps(f.to_dict(), ensure_ascii=False) + "\n")
    if run.crawl:
        with open(d / "pages.jsonl", "w") as fh:
            for cu in run.crawl.urls.values():
                fh.write(json.dumps(cu.to_row(), ensure_ascii=False, default=str) + "\n")
        (d / "geo.json").write_text(json.dumps([g.__dict__ for g in run.crawl.geo], ensure_ascii=False, indent=2))
    if run.admin:
        (d / "admin_counts.json").write_text(json.dumps({"counts": run.admin.counts(), "errors": run.admin.errors}, indent=2))
    return d
