#!/usr/bin/env python3
"""Draft C's whole-article check (his extension, 2026-11-06 23:53 UTC; the link he sent at 23:59 UTC as both C and D,
whose text is draft C's), from RESULT.json (substack_check_text.py result, which matched the page's SHA-256): writes
LEDGER-RESULTS.json for pangram_ledger.py results, key gut-r20-article (prediction #189), every window with its text so
gate E354 can see what it read (gut-2026-11-06c)."""
import json, pathlib
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
r = json.loads((HERE / 'RESULT.json').read_text(encoding='utf-8'))
text = r['text']
lw = [{'label': w['label'], 'confidence': w['confidence'], 'words': w['word_count'],
       'calibrated': round(w['calibrated_confidence'], 4), 'text': text[w['start_index']:w['end_index']].strip()}
      for w in r['windows']]
ledger = {'gut-r20-article': {'headline': r['headline'], 'fraction_ai': r['fraction_ai'], 'words': r['word_count'],
                              'windows': lw, 'utc': '2026-11-06T23:53:48Z', 'link': r['link']}}
(HERE / 'LEDGER-RESULTS.json').write_text(json.dumps(ledger, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(Counter((w['label'], w['confidence']) for w in r['windows']))
