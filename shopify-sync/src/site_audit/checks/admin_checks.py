"""Kontroller mot Shopify Admin-data: kollektioner, produkter, sidor och omdirigeringar."""

from __future__ import annotations

import re
from collections import defaultdict
from datetime import datetime, timedelta, timezone

from ..config import SiteConfig
from ..findings import Finding
from ..html_parse import split_locale
from ..shopify_admin import AdminData
from ..textutil import find_misspellings, fingerprint, jaccard, normalize, words

F = Finding

FILENAME_HANDLE_RE = re.compile(
    r"(\.(jpe?g|png|gif|webp|pdf|tiff?)$)|(^(img|dsc|dscn|dscf|image|photo|foto|screenshot|scan)[-_]?\d+)|"
    r"(^[0-9a-f]{8}-[0-9a-f]{4}-)|(^\d{6,}$)|(_\d{3,}$)|(-copy(-\d+)?$)|(-kopia(-\d+)?$)",
    re.I,
)
DUP_SUFFIX_RE = re.compile(r"-\d{1,2}$")
TEST_RE = re.compile(r"\b(test|testing|draft|utkast|kopia|copy|dummy|lorem|temp)\b", re.I)
YEAR_RE = re.compile(r"\b(20[0-3]\d)\b")

# Synonymer för sidor som ofta finns i flera exemplar.
PAGE_ROLES = {
    "about": ["about", "about us", "om oss", "om", "über uns", "uber uns", "om os", "meistä", "who we are"],
    "contact": ["contact", "contact us", "kontakt", "kontakta oss", "kontakt os", "yhteystiedot", "kontaktieren"],
    "faq": ["faq", "vanliga frågor", "frequently asked questions", "ofte stillede spørgsmål"],
    "shipping": ["shipping", "frakt", "leverans", "delivery", "versand", "levering", "leveransinformation"],
    "returns": ["returns", "retur", "returer", "byten och returer", "refund", "returns policy"],
}


def _norm_title(t: str | None) -> str:
    return normalize(re.sub(r"[^\w\s]", " ", t or ""))


def _base_title(t: str | None) -> str:
    """'Fine art prints – 12 (copy)' -> 'fine art prints'"""
    t = _norm_title(t)
    t = re.sub(r"\b(copy|kopia|\d+)\b", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def check_collections(admin: AdminData, site: SiteConfig) -> list[Finding]:
    out = []
    by_products: dict[tuple, list[dict]] = defaultdict(list)
    by_desc: dict[str, list[dict]] = defaultdict(list)
    by_base_title: dict[str, list[dict]] = defaultdict(list)
    all_tags = {t.lower() for p in admin.products for t in (p.get("tags") or [])}
    all_vendors = {(p.get("vendor") or "").lower() for p in admin.products}
    all_types = {(p.get("productType") or "").lower() for p in admin.products}

    for c in admin.collections:
        url = f"{site.base_url}/collections/{c['handle']}"
        count = (c.get("productsCount") or {}).get("count", 0)
        product_ids = tuple(sorted(n["id"] for n in (c.get("products") or {}).get("nodes", [])))
        rules = (c.get("ruleSet") or {}).get("rules") or []
        if count == 0:
            out.append(F("empty_collection", "high", "catalog", "Tom kollektion som kan indexeras",
                         url=url, resource=c["id"], evidence={"title": c["title"], "smart": bool(rules)}))
        elif count < 3:
            out.append(F("tiny_collection", "low", "catalog", f"Kollektion med bara {count} produkt(er)",
                         url=url, resource=c["id"], evidence={"title": c["title"]}))
        if product_ids:
            by_products[product_ids].append(c)
        desc = (c.get("description") or "").strip()
        if len(words(desc)) >= 15:
            by_desc[fingerprint(desc)].append(c)
        bt = _base_title(c.get("title"))
        if bt:
            by_base_title[bt].append(c)
        if not desc:
            out.append(F("collection_no_description", "low", "catalog", "Kollektion utan beskrivning",
                         url=url, resource=c["id"], evidence={"title": c["title"]}))
        if not (c.get("seo") or {}).get("description") and not desc:
            out.append(F("collection_no_meta_description", "low", "onpage", "Kollektion utan metabeskrivning",
                         url=url, resource=c["id"]))
        # Regler som inte kan matcha något
        for r in rules:
            col, rel, cond = r.get("column"), r.get("relation"), (r.get("condition") or "").strip()
            bad = False
            if col == "TAG" and rel == "EQUALS" and cond.lower() not in all_tags:
                bad = True
            elif col == "VENDOR" and rel == "EQUALS" and cond.lower() not in all_vendors:
                bad = True
            elif col == "TYPE" and rel == "EQUALS" and cond.lower() not in all_types:
                bad = True
            elif col == "TITLE" and rel == "CONTAINS" and len(cond) <= 2:
                bad = True
            if bad and admin.products:
                out.append(F("collection_rule_suspect", "medium", "catalog",
                             f"Regel {col} {rel} '{cond}' matchar troligen fel eller inget",
                             url=url, resource=c["id"], evidence={"title": c["title"], "rule": r}))
        if rules and (c.get("ruleSet") or {}).get("appliedDisjunctively") and len(rules) >= 8:
            out.append(F("collection_rule_complex", "info", "catalog", f"{len(rules)} regler med ELLER-villkor",
                         url=url, resource=c["id"]))

    for ids, cols in by_products.items():
        if len(cols) > 1:
            out.append(F("duplicate_collection_products", "high", "content",
                         f"{len(cols)} kollektioner har exakt samma produkter (doorway/dubblett)",
                         url=f"{site.base_url}/collections/{cols[0]['handle']}",
                         evidence={"collections": [c["handle"] for c in cols][:30], "products": len(ids), "count": len(cols)}))
    for fp, cols in by_desc.items():
        if len(cols) > 1:
            out.append(F("duplicate_collection_description", "medium", "content",
                         f"{len(cols)} kollektioner har identisk beskrivning",
                         url=f"{site.base_url}/collections/{cols[0]['handle']}",
                         evidence={"collections": [c["handle"] for c in cols][:30], "count": len(cols)}))
    for bt, cols in by_base_title.items():
        if len(cols) >= 3:
            out.append(F("collection_clones", "medium", "catalog", f"{len(cols)} kollektioner med i stort sett samma namn: '{bt}'",
                         url=f"{site.base_url}/collections/{cols[0]['handle']}",
                         evidence={"collections": [c["handle"] for c in cols][:40], "count": len(cols)}))
    # Nästan-identiska produktuppsättningar (>= 90 % överlapp)
    sets = [(c, set(n["id"] for n in (c.get("products") or {}).get("nodes", []))) for c in admin.collections]
    sets = [(c, s) for c, s in sets if len(s) >= 5]
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            a, b = sets[i][1], sets[j][1]
            if a == b or abs(len(a) - len(b)) > 0.2 * max(len(a), len(b)):
                continue
            if jaccard(a, b) >= 0.9:
                out.append(F("near_duplicate_collection", "medium", "content",
                             "Två kollektioner med ≥90 % samma produkter",
                             url=f"{site.base_url}/collections/{sets[i][0]['handle']}",
                             evidence={"other": sets[j][0]["handle"], "jaccard": round(jaccard(a, b), 2)}))
    return out


def check_products(admin: AdminData, site: SiteConfig) -> list[Finding]:
    out = []
    by_seo_title: dict[str, list[dict]] = defaultdict(list)
    by_title: dict[str, list[dict]] = defaultdict(list)
    by_desc: dict[str, list[dict]] = defaultdict(list)
    recent_cutoff = datetime.now(timezone.utc) - timedelta(days=site.thresholds.recent_product_days)
    missing_alt_recent = 0
    missing_alt_products = 0
    for p in admin.products:
        if p.get("status") != "ACTIVE":
            continue
        url = f"{site.base_url}/products/{p['handle']}"
        seo_title = ((p.get("seo") or {}).get("title") or "").strip()
        if seo_title:
            by_seo_title[seo_title.lower()].append(p)
        by_title[_norm_title(p.get("title"))].append(p)
        desc = (p.get("description") or "").strip()
        if len(words(desc)) >= 20:
            by_desc[fingerprint(desc)].append(p)
        if FILENAME_HANDLE_RE.search(p["handle"]):
            out.append(F("filename_handle", "medium", "catalog", "Handle ser ut som ett filnamn eller en kopia",
                         url=url, resource=p["id"], evidence={"handle": p["handle"], "title": p.get("title")}))
        elif DUP_SUFFIX_RE.search(p["handle"]) and not re.search(r"\d", p.get("title") or ""):
            out.append(F("duplicate_suffix_handle", "low", "catalog", "Handle slutar på -1/-2 (trolig dubblett)",
                         url=url, resource=p["id"], evidence={"handle": p["handle"]}))
        if not desc:
            out.append(F("product_no_description", "medium", "catalog", "Aktiv produkt utan beskrivning", url=url, resource=p["id"]))
        elif len(words(desc)) < 30:
            out.append(F("product_thin_description", "low", "catalog", f"Kort produktbeskrivning ({len(words(desc))} ord)",
                         url=url, resource=p["id"]))
        images = [m for m in (p.get("media") or {}).get("nodes", []) if m]
        if not images:
            out.append(F("product_no_images", "high", "media", "Aktiv produkt utan bilder", url=url, resource=p["id"]))
        no_alt = [m for m in images if not (m.get("alt") or "").strip()]
        if no_alt:
            missing_alt_products += 1
            created = p.get("createdAt")
            is_recent = bool(created) and datetime.fromisoformat(created.replace("Z", "+00:00")) >= recent_cutoff
            missing_alt_recent += is_recent
            out.append(F("product_images_no_alt", "medium" if is_recent else "low", "media",
                         f"{len(no_alt)} av {len(images)} produktbilder saknar alt-text",
                         url=url, resource=p["id"], evidence={"recent": is_recent, "missing": len(no_alt)}))
        if site.brand_terms:
            hits = find_misspellings(f"{p.get('title') or ''} {desc} {seo_title}", site.brand_terms, site.known_misspellings)
            for w, n in hits.items():
                out.append(F("brand_misspelling", "medium", "content", f"Felstavat varumärke '{w}' i produkt",
                             url=url, resource=p["id"], evidence={"word": w, "occurrences": n}))
    for title, ps in by_seo_title.items():
        if len(ps) > 1:
            out.append(F("duplicate_seo_title", "high", "onpage", f"{len(ps)} produkter delar samma SEO-titel (ärvd vid duplicering?)",
                         url=f"{site.base_url}/products/{ps[0]['handle']}",
                         evidence={"seo_title": title, "handles": [p["handle"] for p in ps][:30], "count": len(ps)}))
    for title, ps in by_title.items():
        if len(ps) > 1 and title:
            out.append(F("duplicate_product_title", "medium", "catalog", f"{len(ps)} aktiva produkter med samma titel",
                         url=f"{site.base_url}/products/{ps[0]['handle']}",
                         evidence={"title": title, "handles": [p["handle"] for p in ps][:30]}))
    for fp, ps in by_desc.items():
        if len(ps) > 1:
            out.append(F("duplicate_product_description", "low", "content", f"{len(ps)} produkter har identisk beskrivning",
                         url=f"{site.base_url}/products/{ps[0]['handle']}",
                         evidence={"handles": [p["handle"] for p in ps][:30], "count": len(ps)}))
    if missing_alt_products:
        out.append(F("alt_text_summary", "info", "media",
                     f"{missing_alt_products} aktiva produkter har bilder utan alt-text ({missing_alt_recent} skapade senaste {site.thresholds.recent_product_days} dagarna)",
                     url=site.base_url, evidence={"products": missing_alt_products, "recent": missing_alt_recent}))
    return out


def _role(title: str) -> str | None:
    t = _norm_title(title)
    for role, names in PAGE_ROLES.items():
        if t in names:
            return role
    return None


def check_pages(admin: AdminData, site: SiteConfig) -> list[Finding]:
    out = []
    roles: dict[str, list[dict]] = defaultdict(list)
    current_year = datetime.now(timezone.utc).year
    for pg in admin.pages:
        url = f"{site.base_url}/pages/{pg['handle']}"
        if not pg.get("isPublished"):
            continue
        body_words = len(words(re.sub(r"<[^>]+>", " ", pg.get("body") or "")))
        role = _role(pg.get("title") or "")
        if role:
            roles[role].append(pg)
        hay = f"{pg.get('title')} {pg['handle']}"
        if TEST_RE.search(hay):
            out.append(F("test_page_published", "high", "content", "Publicerad test-/kopiesida", url=url, resource=pg["id"],
                         evidence={"title": pg.get("title")}))
        if body_words < site.thresholds.thin_words and not role:
            out.append(F("thin_page", "low", "content", f"Publicerad sida med {body_words} ord", url=url, resource=pg["id"],
                         evidence={"title": pg.get("title"), "template": pg.get("templateSuffix")}))
        years = [int(y) for y in YEAR_RE.findall(hay)]
        if years and max(years) < current_year - 1:
            out.append(F("outdated_page", "low", "content", f"Publicerad sida om {max(years)} (gammalt event?)",
                         url=url, resource=pg["id"], evidence={"title": pg.get("title")}))
        if "avada" in hay.lower() or "sitemap" in (pg.get("handle") or ""):
            out.append(F("app_generated_page", "medium", "content", "Sida skapad av app (t.ex. AVADA-sitemap) som kan indexeras",
                         url=url, resource=pg["id"], evidence={"title": pg.get("title")}))
    for role, pages in roles.items():
        if len(pages) > 1:
            out.append(F("duplicate_role_page", "medium", "content", f"{len(pages)} publicerade '{role}'-sidor",
                         url=f"{site.base_url}/pages/{pages[0]['handle']}",
                         evidence={"handles": [p["handle"] for p in pages], "titles": [p.get("title") for p in pages]}))
    for a in admin.articles:
        if not a.get("isPublished"):
            continue
        url = f"{site.base_url}/blogs/{(a.get('blog') or {}).get('handle', 'news')}/{a['handle']}"
        if TEST_RE.search(f"{a.get('title')} {a['handle']}"):
            out.append(F("test_page_published", "high", "content", "Publicerad testartikel", url=url, resource=a["id"]))
        if site.brand_terms:
            for w in find_misspellings(f"{a.get('title') or ''} {re.sub(r'<[^>]+>', ' ', a.get('body') or '')}", site.brand_terms, site.known_misspellings):
                out.append(F("brand_misspelling", "medium", "content", f"Felstavat varumärke '{w}' i artikel", url=url, resource=a["id"]))
    for pg in admin.pages:
        if site.brand_terms and pg.get("isPublished"):
            for w in find_misspellings(f"{pg.get('title') or ''} {re.sub(r'<[^>]+>', ' ', pg.get('body') or '')}", site.brand_terms, site.known_misspellings):
                out.append(F("brand_misspelling", "medium", "content", f"Felstavat varumärke '{w}' på sida",
                             url=f"{site.base_url}/pages/{pg['handle']}", resource=pg["id"]))
    return out


def check_redirect_table(admin: AdminData, site: SiteConfig) -> list[Finding]:
    """Granskar Shopifys URL-omdirigeringar utan att crawla: kedjor, loopar, språkbyten och mål som saknas."""
    out = []
    by_path = {r["path"].rstrip("/").lower() or "/": r for r in admin.redirects}
    handles = {
        "products": {p["handle"] for p in admin.products if p.get("status") == "ACTIVE"},
        "collections": {c["handle"] for c in admin.collections},
        "pages": {p["handle"] for p in admin.pages if p.get("isPublished")},
    }
    locale_hits = defaultdict(int)
    for r in admin.redirects:
        path = r["path"].rstrip("/").lower() or "/"
        target = r["target"]
        tpath = re.sub(r"^https?://[^/]+", "", target).split("?")[0].rstrip("/").lower() or "/"
        if tpath == path:
            out.append(F("redirect_self", "high", "redirects", "Omdirigering pekar på sig själv", url=site.base_url + r["path"], resource=r["id"]))
            continue
        if tpath in by_path:
            out.append(F("redirect_table_chain", "high", "redirects", "Omdirigeringens mål är självt omdirigerat",
                         url=site.base_url + r["path"], resource=r["id"],
                         evidence={"target": target, "next": by_path[tpath]["target"]}))
        src_loc, _ = split_locale(path)
        dst_loc, dst_rest = split_locale(tpath)
        if dst_loc and dst_loc != src_loc:
            locale_hits[dst_loc] += 1
            out.append(F("redirect_table_locale", "high", "international",
                         f"Omdirigering skickar till språk/marknad '{dst_loc}'",
                         url=site.base_url + r["path"], resource=r["id"], evidence={"target": target}))
        m = re.match(r"^/(products|collections|pages)/([^/]+)$", dst_rest)
        if m and admin.products and m.group(2) not in handles[m.group(1)]:
            out.append(F("redirect_target_missing", "critical", "redirects",
                         f"Omdirigeringens mål ({m.group(1)}/{m.group(2)}) finns inte eller är inte publicerat",
                         url=site.base_url + r["path"], resource=r["id"], evidence={"target": target}))
    if admin.redirects:
        out.append(F("redirect_inventory", "info", "redirects", f"{len(admin.redirects)} omdirigeringar i Shopify",
                     url=site.base_url, evidence={"to_locale": dict(locale_hits)}))
    return out


def check_locales(admin: AdminData, site: SiteConfig) -> list[Finding]:
    out = []
    published = [l for l in admin.locales if l.get("published")]
    primary = next((l["locale"] for l in admin.locales if l.get("primary")), None)
    if published:
        out.append(F("locale_summary", "info", "international",
                     f"{len(published)} publicerade språk, primärt '{primary}'",
                     url=site.base_url, evidence={"locales": [l["locale"] for l in published], "markets": [m.get("name") for m in admin.markets]}))
    if site.primary_locale and primary and primary.lower() != site.primary_locale.lower():
        out.append(F("primary_locale_unexpected", "high", "international",
                     f"Butikens primära språk är '{primary}', förväntat '{site.primary_locale}'", url=site.base_url))
    if site.expected_locales:
        extra = {l["locale"].lower() for l in published} - {x.lower() for x in site.expected_locales}
        if extra:
            out.append(F("unexpected_locales", "medium", "international",
                         f"{len(extra)} publicerade språk utanför plan: {', '.join(sorted(extra))}", url=site.base_url))
    for name, err in admin.errors.items():
        out.append(F("admin_fetch_error", "info", "indexing", f"Admin-data '{name}' kunde inte hämtas", url=site.base_url, evidence={"error": err}))
    return out


ALL_ADMIN_CHECKS = [check_collections, check_products, check_pages, check_redirect_table, check_locales]


def run_admin_checks(admin: AdminData, site: SiteConfig) -> list[Finding]:
    out: list[Finding] = []
    for check in ALL_ADMIN_CHECKS:
        out.extend(check(admin, site))
    return out
