#!/usr/bin/env python3
"""The checked text and the reading of each of Joel's shared Pangram pages (history links with their ucc share code):
a headless browser loads each page, which needs no sign-in, and reads the text between "Highlight" and "Overview".
Run on his laptop with the GUI runner's Playwright and his Brave (2026-11-04: his card for the fuels gave only links).

  python3 read_share.py OUT.json URL [URL ...]
"""
import json, re, sys
from playwright.sync_api import sync_playwright

out = {}
with sync_playwright() as p:
    b = p.chromium.launch(headless=True, executable_path='/usr/bin/brave-browser')
    pg = b.new_page()
    for u in sys.argv[2:]:
        pg.goto(u, wait_until='networkidle', timeout=60000)
        pg.wait_for_timeout(3500)
        t = pg.evaluate('document.body.innerText')
        m = re.search(r'Highlight\n(.*?)\nOverview', t, re.S)
        out[u.split('/history/')[1].split('?')[0]] = {'text': m.group(1) if m else None,
                                                      'verdict_block': t[t.find('Overview'):t.find('Similarity')][:600]}
    b.close()
json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
