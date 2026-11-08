#!/usr/bin/env python3
"""dedup_cut.py - the one repeat the two repeats reads found that loses nothing (run after zendo_fix.py).

His first round-24 complaint: "there's still way too much duplication here". Two fresh readers read the stretches round
24 named against the whole guide (REPEATS-AFTERMATH.md, REPEATS-NAMED.md beside this script; what each finding came to
is in RESULTS.md). One sentence repeats only what the guide says elsewhere, and its cut loses no fidelity key, no
keep-as-is line and no owner edit: What Kind of Aftermath Is This?'s "Stabilize through sleep, food, routine, sober
support, ordinary body, and ordinary world." His After the Storm paragraph above it already says it ("Give me sleep,
natural food, pure water, a nice nature walk", "talking with someone grounded"), the list's first line has "routine",
and the Grounding Menu has the body and the ordinary world. A repeat cut that loses nothing goes in (turn 16, his
message of 2026-11-06 19:43 UTC: "make the cuts regardless of pangram if it makes the guide read better").

  python3 dedup_cut.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ, MD = ART / 'GUIDE-SO-FAR-blocks.json', ART / 'GUIDE-SO-FAR.md'
OLD = ' Stabilize through sleep, food, routine, sober support, ordinary body, and ordinary world.'
blocks = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in blocks) + '\n' == MD.read_text(encoding='utf-8')
hits = [b for b in blocks if OLD in b['md']]
assert len(hits) == 1 and hits[0]['id'] == 'B428', [b['id'] for b in hits]
hits[0]['md'] = hits[0]['md'].replace(OLD, '')
print(hits[0]['md'])
MD.write_text('\n\n'.join(b['md'] for b in blocks) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
