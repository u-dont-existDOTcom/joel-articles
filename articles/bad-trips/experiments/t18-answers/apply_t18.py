#!/usr/bin/env python3
"""apply_t18.py - the first five minutes' reminder (B243) and the sitter's script in Get One Human Anchor (B260) said the
same two things; they are said once, by Joel's decision of 2026-11-06 19:43 UTC (../t16-answers/JOEL-MESSAGE-20261106-1943.md:
"make the cuts regardless of pangram if it makes the guide read better"; gate E378) and gate bad-trips-2026-11-06a.

B243 ended "It's intense right now, and it'll pass. We can sort out the rest of your life tomorrow." B260 says "This is a
wave. We don't have to solve your whole life right now." The two sentences go from B243, which keeps what only it says
(where they are, the time, what they took, that its effects will peak and then change); B260 keeps them in the post's own
words, which the fidelity keys hold as a warning ("We don't have to solve your whole life right now."). The order Joel
chose, room -> body -> human -> time -> meaning (KEEP-AS-IS K7), is unchanged.

  python3 apply_t18.py      write the guide (../../GUIDE-SO-FAR.md and its blocks) and print what changed
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
B243 = ("> You're in *[place]*. It's *[date/time]*. You took *[substance, if known]*, and its effects will peak and then "
        "change. It's intense right now, and it'll pass. We can sort out the rest of your life tomorrow.")
assert UNIT['B243']['md'] == B243, UNIT['B243']['md']
assert "This is a wave. We don't have to solve your whole life right now." in UNIT['B260']['md']
UNIT['B243']['md'] = ("> You're in *[place]*. It's *[date/time]*. You took *[substance, if known]*, and its effects will peak "
                      "and then change.")
text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(text, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before_md)), len(re.findall(r'\S+', text))
print('B243: "It\'s intense right now, and it\'ll pass. We can sort out the rest of your life tomorrow." cut (said in B260)')
print('%d words -> %d (%+d); GUIDE-SO-FAR.md sha256 %s' % (w0, w1, w1 - w0, hashlib.sha256(text.encode()).hexdigest()))
