import json,re,html,urllib.request
from concurrent.futures import ThreadPoolExecutor
R=json.load(open("sidgranskning.json"))
U=[r["url"] for r in R if "/blogs/" in r["url"] and r["url"].count("/")>=5]
def get(u):
    try: t=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0 (onboarding-lasning)"}),timeout=40).read().decode("utf-8","replace")
    except Exception as e: return u,""
    m=re.search(r"<article.*?</article>",t,re.S) or re.search(r"<main.*?</main>",t,re.S)
    b=re.sub(r"<(script|style)[^>]*>.*?</\1>"," ",m.group(0) if m else t,flags=re.S)
    return u,re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>"," ",b)))
with ThreadPoolExecutor(5) as ex: res=dict(ex.map(get,U))
json.dump(res,open("artiklar_text.json","w"),ensure_ascii=False)
print(len(res),sum(1 for v in res.values() if v))
