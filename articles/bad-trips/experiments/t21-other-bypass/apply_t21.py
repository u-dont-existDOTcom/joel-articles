#!/usr/bin/env python3
"""apply_t21.py - The Other Bypass's last paragraph (B346, "Skip this inner work, and the trauma doesn't vanish ...") cut,
by Joel's standing decision of 2026-11-06 19:43 UTC (../t16-answers/JOEL-MESSAGE-20261106-1943.md: "make the cuts
regardless of pangram if it makes the guide read better"; gate E378).

B346 says again the same section's B342: bypassed shadow work shows up in ordinary life, his first two marriages his own
case ("When shadow work is bypassed in meditation and therapy, it may appear in ordinary life without explaining itself.").
B346's "It leaks into marriages, friendships, sex, money ..." and "the curriculum arrives through heartbreak, divorce ..."
are that point's examples. The section now ends on where to begin (B345, his Inner Child Therapy and Self-Hypnosis guides).

No fidelity key is in the paragraph (it is in none of FIDELITY-KEYS-R11.json's units; the check must PASS).

  python3 apply_t21.py      write the guide (../../GUIDE-SO-FAR.md and its blocks) and print what changed
"""
import hashlib
import json
import pathlib
import re

ART = pathlib.Path(__file__).resolve().parent.parent.parent
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
BLOCKS = json.loads(BJ.read_text(encoding='utf-8'))
before_md = MD.read_text(encoding='utf-8')
assert '\n\n'.join(b['md'] for b in BLOCKS) + '\n' == before_md, 'the blocks and the guide disagree'
i = next(k for k, b in enumerate(BLOCKS) if b['id'] == 'B346')
assert BLOCKS[i]['md'].startswith("Skip this inner work, and the trauma doesn't vanish."), BLOCKS[i]['md']
assert BLOCKS[i - 1]['id'] == 'B345' and BLOCKS[i + 1]['id'] == 'B347'
del BLOCKS[i]
text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(text, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before_md)), len(re.findall(r'\S+', text))
print("B346: the second telling of bypassed shadow work showing up in ordinary life cut")
print('%d words -> %d (%+d); GUIDE-SO-FAR.md sha256 %s' % (w0, w1, w1 - w0, hashlib.sha256(text.encode()).hexdigest()))
