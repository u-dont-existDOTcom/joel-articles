#!/usr/bin/env python3
"""apply_t19b.py - the violence part's "recruit one additional calm adult" sentence (start of B292) cut, by Joel's
decision of 2026-11-06 19:43 UTC (../t16-answers/JOEL-MESSAGE-20261106-1943.md: "make the cuts regardless of pangram if it
makes the guide read better"; gate E378).

"When you are the only helper and safety is slipping, recruit one additional calm adult or crisis professional." says
again Get One Human Anchor's "When safety, fatigue, logistics, violence, or self-harm risk exceeds what one person can
hold, bring in one additional calm adult or crisis professional.", which names violence among its cases. The paragraph
now opens on what is said only here: when to call crisis or emergency services.

No fidelity key is in the sentence (it is in none of FIDELITY-KEYS-R11.json's units; W079 is Get One Human Anchor's copy,
kept whole).

  python3 apply_t19b.py      write the guide (../../GUIDE-SO-FAR.md and its blocks) and print what changed
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
CUT = "When you are the only helper and safety is slipping, recruit one additional calm adult or crisis professional. "
assert UNIT['B292']['md'].startswith(CUT + 'Call crisis or emergency services'), UNIT['B292']['md']
UNIT['B292']['md'] = UNIT['B292']['md'][len(CUT):]
text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(text, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before_md)), len(re.findall(r'\S+', text))
print("B292: the second copy of \"recruit one additional calm adult\" cut")
print('%d words -> %d (%+d); GUIDE-SO-FAR.md sha256 %s' % (w0, w1, w1 - w0, hashlib.sha256(text.encode()).hexdigest()))
