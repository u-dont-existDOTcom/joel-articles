#!/usr/bin/env python3
"""apply_t19.py - Get One Human Anchor's "committee" line (end of B255) cut, by Joel's decision of 2026-11-06 19:43 UTC
(../t16-answers/JOEL-MESSAGE-20261106-1943.md: "make the cuts regardless of pangram if it makes the guide read better";
gate E378).

"A committee of frantic people rarely improves anyone's nervous system." says again the section's first paragraph,
"Others get worse because too many people crowd in and start advising, arguing, spiritualizing, or panicking." The
paragraph now ends on "That is backup.", which is what it adds: the second adult backs up the one lead.

No fidelity key is in the line (it is in none of FIDELITY-KEYS-R11.json's units; W079, the warning before it, is kept
whole).

  python3 apply_t19.py      write the guide (../../GUIDE-SO-FAR.md and its blocks) and print what changed
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
CUT = " A committee of frantic people rarely improves anyone's nervous system."
assert UNIT['B255']['md'].endswith('That is backup.' + CUT), UNIT['B255']['md']
UNIT['B255']['md'] = UNIT['B255']['md'][:-len(CUT)]
text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(text, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before_md)), len(re.findall(r'\S+', text))
print('B255: the committee line cut')
print('%d words -> %d (%+d); GUIDE-SO-FAR.md sha256 %s' % (w0, w1, w1 - w0, hashlib.sha256(text.encode()).hexdigest()))
