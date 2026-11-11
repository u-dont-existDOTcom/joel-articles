#!/usr/bin/env python3
"""ITEMS.py - print the h42a batch as the page helpers take it ([[key, text, sha256], ...]), for window.__run and
window.__readC in Pangram's dashboard tab (tools/humanization/pangram_page_helpers.js)."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
U = json.loads((HERE / 'UNITS.json').read_text(encoding='utf-8'))
print(json.dumps([[u['key'], (HERE / 'units' / (u['key'] + '.txt')).read_text(encoding='utf-8').rstrip('\n'), u['sha256']]
                  for u in U], ensure_ascii=False))
