"""Bundles all pages into one self-contained preview file (double-click to open)."""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import build  # writes the normal site too
ROOT = build.ROOT
css = (ROOT/"assets/style.css").read_text()
js = (ROOT/"assets/site.js").read_text()
keys = {"index.html":"home","nft-admin/index.html":"nft-admin","money-transfer-platform/index.html":"money-transfer-platform","medical-students-app/index.html":"medical-students-app"}
pages = {}
titles = {}
for path,key in keys.items():
    html = (ROOT/path).read_text()
    body = re.search(r"<body>(.*)<script", html, re.S).group(1)
    body = body.replace('"../assets/','"assets/')
    body = body.replace('href="../"','href="#home"').replace('href="./"','href="#home"')
    body = re.sub(r'href="(?:\.\./)*#work"','href="#work"',body)
    body = re.sub(r'href="(?:\.\./)*(nft-admin|money-transfer-platform|medical-students-app)/"',r'href="#\1"',body)
    body = body.replace('class="brand" href=""','class="brand" href="#home"')
    pages[key]=body
    titles[key]=re.search(r"<title>(.*?)</title>",html).group(1)
head = re.search(r"<head>(.*)</head>",(ROOT/"index.html").read_text(),re.S).group(1)
head = re.sub(r'<link rel="stylesheet"[^>]*>', "<style>"+css+"</style>", head)
out = f"""<!DOCTYPE html><html lang="en"><head>{head}</head><body><div id="app"></div>
<script id="pages" type="application/json">{json.dumps(pages).replace('</','<\\/')}</script>
<script>
var P=JSON.parse(document.getElementById('pages').textContent),T={json.dumps(titles)};
function reveal(){{{js}}}
function show(){{var h=location.hash.slice(1),k=P[h]?h:'home';document.getElementById('app').innerHTML=P[k];document.title=T[k];
 if(h==='work'){{setTimeout(function(){{var w=document.getElementById('work');w&&w.scrollIntoView();}},50)}}else window.scrollTo(0,0);reveal();}}
addEventListener('hashchange',show);show();
</script></body></html>"""
(ROOT.parent/"adi-portfolio-preview.html").write_text(out)
print("preview bytes", len(out))
