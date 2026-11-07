#!/usr/bin/env python3
"""apply_t22.py - Give the Session a Beginning and an End: B366's second sentence ("A lot of prevention is boring: being
rested, starting before everyone is exhausted, leaving time afterward, having food ready, and knowing how the session
ends.") cut, by Joel's standing decision of 2026-11-06 19:43 UTC (../t16-answers/JOEL-MESSAGE-20261106-1943.md: "make the
cuts regardless of pangram if it makes the guide read better"; gate E378).

The sentence lists ahead of time what the section's list (B368) then says item by item: rested (Rest and timing: don't
begin already depleted), starting before everyone is exhausted (begin earlier in the day), leaving time afterward
(Integration time), food ready (food and eating, in Rest and timing, Closure and Integration time) and knowing how the
session ends (Closure). B366 now says only to think through the beginning, middle and end, and the list follows.

No fidelity key is in the sentence (it is in none of FIDELITY-KEYS-R11.json's units; the check must PASS).

  python3 apply_t22.py      write the guide (../../GUIDE-SO-FAR.md and its blocks) and print what changed
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
CUT = (" A lot of prevention is boring: being rested, starting before everyone is exhausted, leaving time afterward, having "
       "food ready, and knowing how the session ends.")
assert UNIT['B366']['md'].endswith(CUT), UNIT['B366']['md']
UNIT['B366']['md'] = UNIT['B366']['md'][:-len(CUT)]
text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(text, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before_md)), len(re.findall(r'\S+', text))
print("B366: the list's preview (\"A lot of prevention is boring: ...\") cut")
print('%d words -> %d (%+d); GUIDE-SO-FAR.md sha256 %s' % (w0, w1, w1 - w0, hashlib.sha256(text.encode()).hexdigest()))
