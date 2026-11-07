#!/usr/bin/env python3
"""apply_r14.py - round 14's answer (Joel, exported 2026-11-07 00:28 UTC; ANSWERS-R14-20261107-0028.json) put into the
guide: CONTACT-PLAIN (Who to Contact, and When's opening, its second sentence said plainly), approved with no comment.

The card worked on the page's plain text; the guide keeps its Markdown (the first sentence's italic *before*). Only the
second sentence changes.

  python3 apply_r14.py      write the guide after round 14 and print what changed
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
REVIEW = json.loads((HERE / 'REVIEW-R14.json').read_text(encoding='utf-8'))
ANSWERS = json.loads((HERE / 'ANSWERS-R14-20261107-0028.json').read_text(encoding='utf-8'))

assert ANSWERS['review_id'] == REVIEW['review_id'] == 'bad-trips-r14'
assert hashlib.sha256((HERE / 'PAGE-R14.md').read_bytes()).hexdigest() == ANSWERS['article']['sha256']
ITEM = {x['id']: x for x in ANSWERS['items']}
assert set(ITEM) == {s['id'] for s in REVIEW['suggestions']} == {'CONTACT-PLAIN'}
assert ITEM['CONTACT-PLAIN']['status'] == 'approved' and not ITEM['CONTACT-PLAIN']['your_version']
before_md = MD.read_text(encoding='utf-8')
assert '\n\n'.join(b['md'] for b in BLOCKS) + '\n' == before_md, 'the blocks and the guide disagree'
UNIT = {b['id']: b for b in BLOCKS}
OLD = 'Hours and services change, and not every option works in every country.'
NEW = 'Their hours and services change, and some only work in one country.'
assert UNIT['B262']['md'].count(OLD) == 1, UNIT['B262']['md']
UNIT['B262']['md'] = UNIT['B262']['md'].replace(OLD, NEW)
assert re.sub(r'\*(.+?)\*', r'\1', UNIT['B262']['md']) == ITEM['CONTACT-PLAIN']['my_version'], UNIT['B262']['md']
text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(text, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before_md)), len(re.findall(r'\S+', text))
print('B262: round 14 in (CONTACT-PLAIN approved)')
print('%d words -> %d (%+d); GUIDE-SO-FAR.md sha256 %s' % (w0, w1, w1 - w0, hashlib.sha256(text.encode()).hexdigest()))
