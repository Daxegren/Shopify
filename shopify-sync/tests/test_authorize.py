import hashlib
import hmac
import threading
import urllib.error
import urllib.parse
import urllib.request

import pytest

from shopify_sync.authorize import OAuthFlow, serve, verify_hmac

SECRET = "hush"
SHOP = "gorilla-test.myshopify.com"


def sign(params):
    msg = "&".join(f"{k}={v}" for k, v in sorted(params.items()))
    return {**params, "hmac": hmac.new(SECRET.encode(), msg.encode(), hashlib.sha256).hexdigest()}


def make_flow(stored, exchange=None):
    return OAuthFlow(
        SHOP, "cid", SECRET, "https://preview.example/", "read_orders,read_products",
        store=stored.append,
        exchange=exchange or (lambda shop, cid, secret, code: {"access_token": f"tok-{code}", "scope": "read_orders,read_products"}),
    )


def test_verify_hmac():
    params = sign({"shop": SHOP, "timestamp": "1"})
    assert verify_hmac(params, SECRET)
    assert not verify_hmac({**params, "shop": "evil.myshopify.com"}, SECRET)


def test_rejects_bad_shop():
    with pytest.raises(ValueError):
        OAuthFlow("evil.com", "cid", SECRET, "https://x", "read_orders", store=print)


def test_entry_redirects_to_authorize():
    flow = make_flow([])
    status, headers, _ = flow.handle("/", sign({"shop": SHOP, "timestamp": "1"}))
    assert status == 302
    loc = urllib.parse.urlsplit(headers["Location"])
    q = dict(urllib.parse.parse_qsl(loc.query))
    assert loc.netloc == SHOP and loc.path == "/admin/oauth/authorize"
    assert q["redirect_uri"] == "https://preview.example/callback"
    assert q["state"] == flow.state and q["scope"] == "read_orders,read_products"


def test_callback_stores_token_once_verified():
    stored = []
    flow = make_flow(stored)
    bad_state = sign({"shop": SHOP, "code": "c1", "state": "wrong"})
    assert flow.handle("/callback", bad_state)[0] == 400
    unsigned = {"shop": SHOP, "code": "c1", "state": flow.state, "hmac": "00"}
    assert flow.handle("/callback", unsigned)[0] == 400
    assert stored == [] and not flow.done

    status, _, body = flow.handle("/callback", sign({"shop": SHOP, "code": "c1", "state": flow.state}))
    assert status == 200 and "tok-c1" not in body
    assert stored == ["tok-c1"] and flow.done


def test_reports_missing_scopes():
    flow = make_flow([], exchange=lambda *a: {"access_token": "t", "scope": "read_orders"})
    _, _, body = flow.handle("/callback", sign({"shop": SHOP, "code": "c", "state": flow.state}))
    assert "read_products" in body


def test_http_server_end_to_end():
    stored = []
    flow = make_flow(stored)
    port = 18765
    t = threading.Thread(target=serve, args=(flow, port), daemon=True)
    t.start()
    query = urllib.parse.urlencode(sign({"shop": SHOP, "code": "xyz", "state": flow.state}))
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    for _ in range(50):
        try:
            with opener.open(f"http://127.0.0.1:{port}/callback?{query}", timeout=2) as resp:
                assert resp.status == 200
            break
        except urllib.error.URLError:
            threading.Event().wait(0.05)
    t.join(timeout=5)
    assert stored == ["tok-xyz"] and not t.is_alive()
