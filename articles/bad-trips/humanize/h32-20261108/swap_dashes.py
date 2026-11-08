#!/usr/bin/env python3
"""swap_dashes.py - the standard swap's dash rule, applied to the whole guide (gate E353 (Inner Child),
tools/humanization/typography_swap.py): each spaced en dash this guide still had from the swap's first form (" – ", the
rule until 2026-11-04) becomes his two hyphens, "--", with no spaces. Joel, 2026-11-04 16:30 UTC, asked whether that meant
every article: "yes to both ... it won't matter anyway in high conf human sections. it could flip low conf ones ai".
Each block's Markdown goes through the shared swap, so the blocks and GUIDE-SO-FAR.md stay one text.

  python3 swap_dashes.py
"""
import importlib.util
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
REPO = ART.parents[1]
spec = importlib.util.spec_from_file_location('ts', REPO / 'tools/humanization/typography_swap.py')
TS = importlib.util.module_from_spec(spec)
spec.loader.exec_module(TS)
BJ, MD = ART / 'GUIDE-SO-FAR-blocks.json', ART / 'GUIDE-SO-FAR.md'
blocks = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in blocks) + '\n' == MD.read_text(encoding='utf-8')
n = 0
for b in blocks:
    s = TS.swap_text(b['md'])[0]
    if s != b['md']:
        n += 1
        b['md'] = s
MD.write_text('\n\n'.join(b['md'] for b in blocks) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('%d blocks changed' % n)
