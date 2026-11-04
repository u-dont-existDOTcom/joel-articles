#!/usr/bin/env python3
"""swap.py - the humanize pass, step 1: the standard typographic swap (gate E337 (gut); tools/humanization/typography_swap.py)
on the guide after round 2, before any rewording and before any check.

Curly quote marks become straight ones and each em dash becomes his spaced en dash (" – "; between two digits, an
unspaced en dash). Nothing else changes. Reads ../../review/r02/GUIDE-AFTER-R02-blocks.json and writes the guide as it
stands, ../../GUIDE-SO-FAR.md, with its blocks (../../GUIDE-SO-FAR-blocks.json, the block ids kept).

  python3 swap.py
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
sys.path.insert(0, str(ART.parents[1] / 'tools' / 'humanization'))
import typography_swap as TS  # noqa: E402

blocks = json.loads((ART / 'review' / 'r02' / 'GUIDE-AFTER-R02-blocks.json').read_text(encoding='utf-8'))
n = 0
for b in blocks:
    b['md'], c = TS.swap_text(b['md'])
    n += c
text = '\n\n'.join(b['md'] for b in blocks) + '\n'
(ART / 'GUIDE-SO-FAR.md').write_text(text, encoding='utf-8')
(ART / 'GUIDE-SO-FAR-blocks.json').write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('%d characters swapped; GUIDE-SO-FAR.md sha256 %s' % (n, hashlib.sha256(text.encode()).hexdigest()))
