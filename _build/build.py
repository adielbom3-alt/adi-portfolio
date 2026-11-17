"""Builds the static site from the page sources in this folder.
Run:  python3 _build/build.py      (from the site root)
IMG is where images live. While images are still on the old WordPress site
it points there; after they are copied into assets/img it becomes the local path.
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOCAL_IMG = (ROOT / "assets" / "img").exists() and any((ROOT / "assets" / "img").iterdir())
REMOTE = "https://adidamari.co.il/wp-content/uploads/"

RESUME = "https://drive.google.com/file/d/1dUDBJgoNw1x8Hw4QgFYmObVrlOSRtjmj/view"
LINKEDIN = "https://www.linkedin.com/in/adi-elbom-dam-ari/"
WHATSAPP = "https://api.whatsapp.com/send?phone=972507307688"
EMAIL = "adi.elbom3@gmail.com"

ICON_MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>'
ICON_WA = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 11.5a8.5 8.5 0 0 1-12.6 7.4L3 20l1.2-4.2A8.5 8.5 0 1 1 20 11.5Z"/></svg>'
ICON_IN = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9.75h4V21H3V9.75Zm6.5 0h3.8v1.6h.06c.53-1 1.84-2.05 3.79-2.05 4.05 0 4.8 2.6 4.8 6V21h-4v-5.1c0-1.22-.02-2.8-1.7-2.8-1.71 0-1.97 1.33-1.97 2.7V21h-4V9.75Z"/></svg>'
ICON_CV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/></svg>'
ARROW = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'


def page(title, desc, body, depth, current=""):
    up = "../" * depth
    img = (up + "assets/img/") if LOCAL_IMG else REMOTE
    body = body.replace("{IMG}", img).replace("{UP}", up).replace("{ARROW}", ARROW)
    work_cls = ' class="current"' if current == "work" else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Ccircle cx='32' cy='32' r='32' fill='%231F1F1F'/%3E%3Ctext x='32' y='43' font-family='Georgia,serif' font-size='34' font-weight='700' text-anchor='middle' fill='%23fff'%3EA%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Red+Hat+Display:wght@300;400;500;600;700&family=Song+Myung&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
<div class="navholder">
  <nav class="site" aria-label="Main">
    <a class="brand" href="{up}">Adi Elbom.</a>
    <div class="navlinks">
      <a href="{up}#work"{work_cls}>Work</a>
      <a href="{RESUME}" target="_blank" rel="noopener">Resume</a>
      <a class="hide-sm" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>
      <a class="cta" href="{WHATSAPP}" target="_blank" rel="noopener">Let’s chat</a>
    </div>
  </nav>
</div>
{body}
<footer class="site-foot" id="contact">
  <div class="foot-inner">
    <div class="foot-main">
      <h2 class="foot-title reveal"><span class="hl">Let’s Connect.</span></h2>
      <div class="foot-links">
        <a href="{WHATSAPP}" target="_blank" rel="noopener">WhatsApp <span class="ext" aria-hidden="true">↗</span></a>
        <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn <span class="ext" aria-hidden="true">↗</span></a>
        <a href="mailto:{EMAIL}">Email <span class="ext" aria-hidden="true">↗</span></a>
      </div>
    </div>
    <div class="clock" id="clock" aria-live="off">
        <span class="clock-icons" aria-hidden="true">
          <svg class="ci ci-sunrise" viewBox="0 0 32 32"><path d="M4 23h24M9 23a7 7 0 0 1 14 0"/><path d="M16 9v3M7.5 13.5l2 2M24.5 13.5l-2 2M3.5 19h2.5M26 19h2.5"/><path d="M13 6l3-3 3 3"/></svg>
          <svg class="ci ci-sun" viewBox="0 0 32 32"><circle cx="16" cy="16" r="5.5"/><path d="M16 3v3.5M16 25.5V29M3 16h3.5M25.5 16H29M6.8 6.8l2.5 2.5M22.7 22.7l2.5 2.5M6.8 25.2l2.5-2.5M22.7 9.3l2.5-2.5"/></svg>
          <svg class="ci ci-sunset" viewBox="0 0 32 32"><path d="M4 23h24M9 23a7 7 0 0 1 14 0"/><path d="M16 9v3M7.5 13.5l2 2M24.5 13.5l-2 2M3.5 19h2.5M26 19h2.5"/><path d="M13 27l3 3 3-3"/></svg>
          <svg class="ci ci-moon" viewBox="0 0 32 32"><path d="M21.5 20.5A9.5 9.5 0 0 1 11.5 6a10 10 0 1 0 14 13.5 9.4 9.4 0 0 1-4 1Z"/><path d="M23 5.5v3M21.5 7h3M26.5 11v2M25.5 12h2"/></svg>
        </span>
        <span class="clock-label">Local time · Tel Aviv</span>
        <span class="clock-time"><span class="hh">--</span><span class="colon">:</span><span class="mm">--</span></span>
    </div>
  </div>
  <div class="foot-bottom">
    <span>© 2026 Adi Elbom Dam Ari · Product Designer</span>
    <a href="#top" onclick="window.scrollTo({{top:0,behavior:'smooth'}});return false;">Back to top ↑</a>
  </div>
</footer>
<script src="{up}assets/site.js"></script>
</body>
</html>
"""


sys.path.insert(0, str(pathlib.Path(__file__).parent))
from pages import PAGES  # noqa: E402

for path, (title, desc, depth, current, body) in PAGES.items():
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(title, desc, body, depth, current), encoding="utf-8")
    print("wrote", out.relative_to(ROOT))
print("images:", "local assets/img" if LOCAL_IMG else "linked from adidamari.co.il")
