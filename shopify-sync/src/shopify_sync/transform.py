"""Omvandlar JSONL-rader från Shopify Bulk Operations till tabellrader."""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Any

# Shopify-id:n har formen gid://shopify/<Typ>/<nummer>.


def gid_type(gid: str | None) -> str | None:
    if not gid or not gid.startswith("gid://shopify/"):
        return None
    return gid.split("/")[3]


def _get(obj: Any, *path: str) -> Any:
    for key in path:
        if not isinstance(obj, dict):
            return None
        obj = obj.get(key)
    return obj


def _money(obj: Any, *path: str) -> str | None:
    return _get(obj, *path, "shopMoney", "amount")


def _int(value: Any) -> int | None:
    if value is None or value == "":
        return None
    return int(value)


def _join(values: Any) -> str | None:
    if not values:
        return None
    return ",".join(str(v) for v in values)


def _strip_internal(obj: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in obj.items() if k != "__parentId"}


def order_row(o: dict[str, Any], synced_at: str) -> dict[str, Any]:
    first = _get(o, "customerJourneySummary", "firstVisit") or {}
    last = _get(o, "customerJourneySummary", "lastVisit") or {}
    return {
        "id": o["id"],
        "name": o.get("name"),
        "created_at": o.get("createdAt"),
        "updated_at": o.get("updatedAt"),
        "processed_at": o.get("processedAt"),
        "cancelled_at": o.get("cancelledAt"),
        "closed_at": o.get("closedAt"),
        "financial_status": o.get("displayFinancialStatus"),
        "fulfillment_status": o.get("displayFulfillmentStatus"),
        "currency_code": o.get("currencyCode"),
        "total_price": _money(o, "totalPriceSet"),
        "current_total_price": _money(o, "currentTotalPriceSet"),
        "subtotal_price": _money(o, "subtotalPriceSet"),
        "total_discounts": _money(o, "totalDiscountsSet"),
        "total_shipping": _money(o, "totalShippingPriceSet"),
        "total_tax": _money(o, "totalTaxSet"),
        "total_refunded": _money(o, "totalRefundedSet"),
        "discount_codes": _join(o.get("discountCodes")),
        "source_name": o.get("sourceName"),
        "customer_id": _get(o, "customer", "id"),
        "shipping_country": _get(o, "shippingAddress", "countryCodeV2"),
        "first_visit_source": first.get("source"),
        "first_visit_utm_source": _get(first, "utmParameters", "source"),
        "first_visit_utm_medium": _get(first, "utmParameters", "medium"),
        "first_visit_utm_campaign": _get(first, "utmParameters", "campaign"),
        "first_visit_landing_page": first.get("landingPage"),
        "last_visit_source": last.get("source"),
        "last_visit_utm_source": _get(last, "utmParameters", "source"),
        "last_visit_utm_medium": _get(last, "utmParameters", "medium"),
        "last_visit_utm_campaign": _get(last, "utmParameters", "campaign"),
        "refund_count": len(o.get("refunds") or []),
        "raw": _strip_internal(o),
        "_synced_at": synced_at,
    }


def line_item_row(li: dict[str, Any], synced_at: str) -> dict[str, Any]:
    quantity = _int(li.get("quantity"))
    current = _int(li.get("currentQuantity"))
    removed = quantity - current if quantity is not None and current is not None else None
    return {
        "id": li["id"],
        "order_id": li["__parentId"],
        "product_id": _get(li, "product", "id"),
        "variant_id": _get(li, "variant", "id"),
        "sku": li.get("sku"),
        "title": li.get("title"),
        "variant_title": li.get("variantTitle"),
        "vendor": li.get("vendor"),
        "quantity": quantity,
        "current_quantity": current,
        "removed_quantity": removed,
        "original_unit_price": _money(li, "originalUnitPriceSet"),
        "discounted_total": _money(li, "discountedTotalSet"),
        "raw": _strip_internal(li),
        "_synced_at": synced_at,
    }


def product_row(p: dict[str, Any], synced_at: str) -> dict[str, Any]:
    return {
        "id": p["id"],
        "handle": p.get("handle"),
        "title": p.get("title"),
        "status": p.get("status"),
        "vendor": p.get("vendor"),
        "product_type": p.get("productType"),
        "tags": _join(p.get("tags")),
        "created_at": p.get("createdAt"),
        "updated_at": p.get("updatedAt"),
        "published_at": p.get("publishedAt"),
        "total_inventory": _int(p.get("totalInventory")),
        "online_store_url": p.get("onlineStoreUrl"),
        "seo_title": _get(p, "seo", "title"),
        "seo_description": _get(p, "seo", "description"),
        "raw": _strip_internal(p),
        "_synced_at": synced_at,
    }


def variant_row(v: dict[str, Any], synced_at: str) -> dict[str, Any]:
    return {
        "id": v["id"],
        "product_id": v["__parentId"],
        "sku": v.get("sku"),
        "title": v.get("title"),
        "barcode": v.get("barcode"),
        "price": v.get("price"),
        "compare_at_price": v.get("compareAtPrice"),
        "unit_cost": _get(v, "inventoryItem", "unitCost", "amount"),
        "inventory_quantity": _int(v.get("inventoryQuantity")),
        "created_at": v.get("createdAt"),
        "updated_at": v.get("updatedAt"),
        "raw": _strip_internal(v),
        "_synced_at": synced_at,
    }


def customer_row(c: dict[str, Any], synced_at: str) -> dict[str, Any]:
    return {
        "id": c["id"],
        "created_at": c.get("createdAt"),
        "updated_at": c.get("updatedAt"),
        "number_of_orders": _int(c.get("numberOfOrders")),
        "amount_spent": _get(c, "amountSpent", "amount"),
        "currency_code": _get(c, "amountSpent", "currencyCode"),
        "country": _get(c, "defaultAddress", "countryCodeV2"),
        "tags": _join(c.get("tags")),
        "raw": _strip_internal(c),
        "_synced_at": synced_at,
    }


# gid-typ -> (tabell, radfunktion)
ROUTES = {
    "Order": ("orders", order_row),
    "LineItem": ("order_line_items", line_item_row),
    "Product": ("products", product_row),
    "ProductVariant": ("product_variants", variant_row),
    "Customer": ("customers", customer_row),
}


def route(objects: Iterable[dict[str, Any]], synced_at: str) -> Iterator[tuple[str, dict[str, Any]]]:
    """Ger (tabellnamn, rad) för varje JSONL-objekt. Okända typer hoppas över."""
    for obj in objects:
        target = ROUTES.get(gid_type(obj.get("id")))
        if target is None:
            continue
        table, fn = target
        yield table, fn(obj, synced_at)
