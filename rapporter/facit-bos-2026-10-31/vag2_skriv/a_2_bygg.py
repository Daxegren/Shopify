import sys, json, subprocess, importlib.util, os
base="/home/user/Shopify/rapporter/facit-bos-2026-10-31"
sys.path.insert(0, base)
import bygg_skriv
from format_regler import tillamp
bygg_skriv.BEST |= {"10472277639434","10472277737738","10472259813642","10471310262538"}
spec=importlib.util.spec_from_file_location("m",base+"/vag2_skriv/a_2_modul.py"); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
inn={x["id"]:x for x in json.load(open(base+"/vag2_skriv/a_2_in.json"))}
out=[]; chk=[]
for p in m.D:
    if p.get("html_skip"):
        out.append({"id":p["id"],"nr":p["nr"],"titel":None,"seo_title":None,"meta":None,"html":None,"handhavd":True,"fakta":p["fakta"],"att_bekrafta":p["att_bekrafta"]}); continue
    q=tillamp(p); h=bygg_skriv.html(q)
    out.append({"id":q["id"],"nr":q["nr"],"titel":q["titel"],"seo_title":q["seo_title"],"meta":q["meta"],"html":h,"fakta":q["fakta"],"att_bekrafta":q["att_bekrafta"]})
    bh=h.replace("<h2>Leverans, retur och garanti</h2>","[[STANDARDBLOCK]]<h2>Leverans, retur och garanti</h2>",1)
    i=bh.find("<p><strong>Säljare:</strong>"); j=bh.find("</p>",i)+4
    bh=bh[:j]+"[[/STANDARDBLOCK]]"+bh[j:]
    chk.append({"id":q["id"],"titel":q["titel"],"seo_title":q["seo_title"],**({"meta":q["meta"]} if q["meta"] else {}),"beskrivning":bh,"fakta":q["fakta"]})
json.dump(out,open(base+"/vag2_skriv/a_2_utkast.json","w"),ensure_ascii=False,indent=1)
json.dump(chk,open("/tmp/claude-0/-home-user/fbbd95a3-8b18-5096-a6b5-20df3e4eb235/scratchpad/a_2_chk.json","w"),ensure_ascii=False,indent=1)
for x in out:
    if x["titel"]: print(x["nr"],len(x["titel"]),len(x["seo_title"]),len(x["meta"] or ""),x["titel"],"|",x["seo_title"])
r=subprocess.run([sys.executable,"/home/user/Shopify/shopify-sync/scripts/kontrollera_produkttext.py","/tmp/claude-0/-home-user/fbbd95a3-8b18-5096-a6b5-20df3e4eb235/scratchpad/a_2_chk.json","--seo-title-max","43"],capture_output=True,text=True); print(r.stdout[-5000:],r.stderr[-800:])
