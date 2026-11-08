#!/usr/bin/env python3
"""apply_r25.py - round 25's answer (Joel, exported 2026-11-08 16:55 UTC; ANSWERS-R25-20261108-1655.json) put into the
guide: WHY-LESSON-CUT ("Every hard experience can feel like a profound lesson. But sometimes the lesson is just to ...",
B361), approved with no comment. It holds warning W102, so its loss is an owner change in
../../humanize/h01/FIDELITY-KEYS-R25.json.

  python3 apply_r25.py      write the guide after round 25 and print what changed
"""
import hashlib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parent.parent
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
BLOCKS = json.loads(BJ.read_text(encoding='utf-8'))
REVIEW = json.loads((HERE / 'REVIEW-R25.json').read_text(encoding='utf-8'))
ANSWERS = json.loads((HERE / 'ANSWERS-R25-20261108-1655.json').read_text(encoding='utf-8'))

assert ANSWERS['review_id'] == REVIEW['review_id'] == 'bad-trips-r25'
assert hashlib.sha256((HERE / 'PAGE-R25.md').read_bytes()).hexdigest() == ANSWERS['article']['sha256']
ITEM = {x['id']: x for x in ANSWERS['items']}
assert set(ITEM) == {s['id'] for s in REVIEW['suggestions']} == {'WHY-LESSON-CUT'}
assert ITEM['WHY-LESSON-CUT']['status'] == 'approved' and not ITEM['WHY-LESSON-CUT']['your_version']
before_md = MD.read_text(encoding='utf-8')
assert '\n\n'.join(b['md'] for b in BLOCKS) + '\n' == before_md, 'the blocks and the guide disagree'
cut = [b for b in BLOCKS if b['id'] == 'B361']
assert len(cut) == 1 and cut[0]['md'] == ITEM['WHY-LESSON-CUT']['before'], cut
BLOCKS = [b for b in BLOCKS if b['id'] != 'B361']
text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(text, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before_md)), len(re.findall(r'\S+', text))
print('B361: round 25 in (WHY-LESSON-CUT approved)')
print('%d words -> %d (%+d); GUIDE-SO-FAR.md sha256 %s' % (w0, w1, w1 - w0, hashlib.sha256(text.encode()).hexdigest()))
