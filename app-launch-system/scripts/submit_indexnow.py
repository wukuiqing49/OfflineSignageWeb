#!/usr/bin/env python3
"""Submit all sitemap URLs to IndexNow API (Bing, Yandex, Seznam, Naver)."""

import json
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SITEMAP_PATH = ROOT / "sitemap.xml"
HOST = "heyehoi.cn"
KEY = "d8f4c2e61a7b40989f3a5e1289bc704a"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

def get_urls():
    if not SITEMAP_PATH.exists():
        return [f"https://{HOST}/"]
    content = SITEMAP_PATH.read_text(encoding="utf-8")
    urls = []
    for line in content.splitlines():
        if "<loc>" in line:
            loc = line.strip().replace("<loc>", "").replace("</loc>", "").replace("<url>", "").replace("</url>", "")
            if loc.startswith("http"):
                urls.append(loc)
    return sorted(set(urls))

def submit():
    url_list = get_urls()
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": url_list
    }
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    
    endpoints = [
        "https://api.indexnow.org/indexnow",
        "https://www.bing.com/indexnow"
    ]
    
    print(f"Submitting {len(url_list)} URLs to IndexNow endpoints...")
    for endpoint in endpoints:
        req = urllib.request.Request(
            endpoint,
            data=data,
            headers={
                "Content-Type": "application/json; charset=utf-8",
                "User-Agent": "OfflineSignage-IndexNow/1.0"
            },
            method="POST"
        )
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                print(f"[{resp.status}] {endpoint}: OK")
        except urllib.error.HTTPError as e:
            print(f"[{e.code}] {endpoint}: {e.reason} ({e.read().decode('utf-8', errors='ignore')})")
        except Exception as e:
            print(f"[ERROR] {endpoint}: {e}")

if __name__ == "__main__":
    submit()
