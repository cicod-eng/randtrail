#!/usr/bin/env python3
"""Submit URLs to IndexNow (Bing/Yandex/Seznam/Naver).

Usage:
    python3 indexnow_submit.py                  # submit every URL in sitemap.xml
    python3 indexnow_submit.py https://randtrail.com/new-page/  # submit specific URLs
"""
import json
import re
import sys
import urllib.request

KEY = "c94d118a4ac660ccae74351ac54c8f10"
HOST = "randtrail.com"
API = "https://api.indexnow.org/indexnow"


def sitemap_urls():
    with open("sitemap.xml", encoding="utf-8") as f:
        s = f.read()
    return re.findall(r"<loc>([^<]+)</loc>", s)


def submit(urls):
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": f"https://{HOST}/{KEY}.txt",
        "urlList": urls,
    }
    req = urllib.request.Request(
        API,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        print(f"HTTP {r.status}: {r.read().decode()}")
    print(f"Submitted {len(urls)} URLs")


if __name__ == "__main__":
    urls = sys.argv[1:] if len(sys.argv) > 1 else sitemap_urls()
    submit(urls)
