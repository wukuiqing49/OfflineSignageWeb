#!/usr/bin/env python3
"""Submit all sitemap URLs to IndexNow API (Bing, Yandex, Seznam, Naver)."""

import argparse
import json
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SITEMAP_PATH = ROOT / "sitemap.xml"
KEY = "dfa8d8fe4060466682a78c762a3f6075"

def get_urls(host: str):
    if not SITEMAP_PATH.exists():
        return [f"https://{host}/"]
    content = SITEMAP_PATH.read_text(encoding="utf-8")
    urls = []
    for line in content.splitlines():
        if "<loc>" in line:
            loc = line.strip().replace("<loc>", "").replace("</loc>", "").replace("<url>", "").replace("</url>", "")
            if loc.startswith("http"):
                urls.append(loc)
            elif loc.startswith("/"):
                urls.append(f"https://{host}{loc}")
    return sorted(set(urls))

def submit(host: str):
    url_list = get_urls(host)
    payload = {
        "host": host,
        "key": KEY,
        "keyLocation": f"https://{host}/{KEY}.txt",
        "urlList": url_list
    }
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    
    endpoints = [
        "https://api.indexnow.org/indexnow",
        "https://www.bing.com/indexnow"
    ]
    
    print(f"Submitting {len(url_list)} URLs for host {host} to IndexNow endpoints...")
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="localhost", help="Domain host name to submit")
    args = parser.parse_args()
    submit(args.host)
