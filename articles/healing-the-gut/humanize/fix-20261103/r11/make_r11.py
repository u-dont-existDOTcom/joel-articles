#!/usr/bin/env python3
"""r11: r10 with the one slip of ours that the pre-publish reads found (2026-11-04, after Joel's "publish it" of 20:27 UTC).

Phase 3, step 5 said "And if the herbs failed", the Gem's logic ("If herbs failed"), but his H2O2 swap in steps 1 and 2
tells the reader to avoid most herbal antibiotics, so the herbs it points to were never taken. Three readers flagged it
(the sense read's block 55, clarity 3.2, compare F2.5). The fewest words: "And if all that failed" (steps 1 to 4).
Every other finding is in his published text or his own versions and goes to him (../r10/prepublish/FINDINGS.md).
Writes r11.html and r11.md. No API calls."""
import hashlib
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
R10 = HERE.parent / 'r10'
OLD = 'And if the herbs failed, the overgrowth is too severe'
NEW = 'And if all that failed, the overgrowth is too severe'

for ext in ('html', 'md'):
    t = (R10 / ('r10.' + ext)).read_text(encoding='utf-8')
    assert t.count(OLD) == 1, (ext, t.count(OLD))
    t = t.replace(OLD, NEW)
    out = HERE / ('r11.' + ext)
    out.write_text(t, encoding='utf-8')
    print(out.name, hashlib.sha256(t.encode('utf-8')).hexdigest())
