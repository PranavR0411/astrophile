#!/usr/bin/env python3
"""
Copy every image the site loads from Wix (static.wixstatic.com) into assets/img/
and rewrite the HTML to use the local copies. Run once from the repo root:

    python3 tools/localize_images.py

Afterwards the site no longer depends on your Wix account. Uses only the
Python standard library.
"""
import hashlib
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "assets" / "img"
IMG.mkdir(parents=True, exist_ok=True)
PATTERN = re.compile(r'https://static\.wixstatic\.com/media/[^"\'\s)]+')

pages = [ROOT / "index.html", ROOT / "projects.html", *sorted((ROOT / "projects").glob("*.html"))]
urls = sorted({u for p in pages for u in PATTERN.findall(p.read_text(encoding="utf-8"))})
local = {}

for url in urls:
    base = url.split("/media/")[1].split("/")[0]
    ext = base.rsplit(".", 1)[-1].lower()
    if "/v1/" in url:  # resized thumbnail
        name = base.rsplit(".", 1)[0][:40] + "-" + hashlib.md5(url.encode()).hexdigest()[:6] + "." + ext
    else:
        name = base.replace("~", "-")
    dest = IMG / name
    if not dest.exists():
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            dest.write_bytes(r.read())
        print("saved", name)
    local[url] = name

for p in pages:
    text = p.read_text(encoding="utf-8")
    prefix = "../" if p.parent.name == "projects" else ""
    for url, name in local.items():
        text = text.replace(url, f"{prefix}assets/img/{name}")
    p.write_text(text, encoding="utf-8")

print(f"Done: {len(local)} images in assets/img, {len(pages)} pages updated.")
