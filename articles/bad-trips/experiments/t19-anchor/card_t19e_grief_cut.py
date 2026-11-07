#!/usr/bin/env python3
"""card_t19e_grief_cut.py - NOT APPLIED: a card for round 15. Cutting For the Person Helping's "real grief" paragraph (B84)
as a repeat loses two warnings the fidelity keys hold (drag/grief, trap/grinding), so it is his call, not a gate-E378 cut.
What follows is the cut as it would be made, after his decision of
2026-11-06 19:43 UTC (../t16-answers/JOEL-MESSAGE-20261106-1943.md: "make the cuts regardless of pangram if it makes the
guide read better"; gate E378).

"Don't drag somebody out of real grief." says again the paragraph two above it, "Crying, grieving, remembering, or
touching a genuine wound calls for loving awareness."; "Don't trap them inside a loop that is grinding them down either."
is what The Fear/Panic Loop section is for (its loop breaker); "Love isn't stubbornness." is a closing quip, read as AI by
all three readers of the tell panel (../../humanize/h17-20261107/panel-HELPER/PANEL.md). No fidelity key is in it.

  python3 apply_t19e.py      write the guide (../../GUIDE-SO-FAR.md and its blocks) and print what changed
"""
import hashlib
import json
import pathlib
import re

ART = pathlib.Path(__file__).resolve().parent.parent.parent
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
BLOCKS = json.loads(BJ.read_text(encoding='utf-8'))
UNIT = {b['id']: b for b in BLOCKS}
before_md = MD.read_text(encoding='utf-8')
assert '\n\n'.join(b['md'] for b in BLOCKS) + '\n' == before_md, 'the blocks and the guide disagree'
B84 = ("Don't drag somebody out of real grief. Don't trap them inside a loop that is grinding them down either. Love isn't "
       "stubbornness.")
assert UNIT['B84']['md'] == B84, UNIT['B84']['md']
BLOCKS = [b for b in BLOCKS if b['id'] != 'B84']
text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(text, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before_md)), len(re.findall(r'\S+', text))
print('B84 (the real-grief paragraph) cut')
print('%d words -> %d (%+d); GUIDE-SO-FAR.md sha256 %s' % (w0, w1, w1 - w0, hashlib.sha256(text.encode()).hexdigest()))
