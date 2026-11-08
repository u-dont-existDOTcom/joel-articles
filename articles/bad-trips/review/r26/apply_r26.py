#!/usr/bin/env python3
"""apply_r26.py - round 26's answers (Joel, exported 2026-11-08 16:48 UTC; ANSWERS-R26-20261108-1648.json) put into the
guide: HELPER-OPEN-CUT (For the Person Helping's first sentence) and AFT-TRAUMA-ONCE (the aftermath list's trauma line),
both approved with no comment, on the page's third version.

  python3 apply_r26.py      write the guide after round 26 and print what changed
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
REVIEW = json.loads((HERE / 'REVIEW-R26.json').read_text(encoding='utf-8'))
ANSWERS = json.loads((HERE / 'ANSWERS-R26-20261108-1648.json').read_text(encoding='utf-8'))

assert ANSWERS['review_id'] == REVIEW['review_id'] == 'bad-trips-r26'
assert hashlib.sha256((HERE / 'PAGE-R26.md').read_bytes()).hexdigest() == ANSWERS['article']['sha256']
ITEM = {x['id']: x for x in ANSWERS['items']}
assert set(ITEM) == {s['id'] for s in REVIEW['suggestions']} == {'HELPER-OPEN-CUT', 'AFT-TRAUMA-ONCE'}
for k in ITEM:
    assert ITEM[k]['status'] == 'approved' and not ITEM[k]['your_version'] and not ITEM[k]['comment'], k
before_md = MD.read_text(encoding='utf-8')
assert '\n\n'.join(b['md'] for b in BLOCKS) + '\n' == before_md, 'the blocks and the guide disagree'
UNIT = {b['id']: b for b in BLOCKS}

FIRST = ('A good sitter is not there to win a philosophy debate, perform a rescue fantasy, impose an interpretation, or '
         'demonstrate spiritual advancement. ')
assert UNIT['B280']['md'].startswith(FIRST), UNIT['B280']['md']
UNIT['B280']['md'] = UNIT['B280']['md'][len(FIRST):]
assert UNIT['B280']['md'] == ITEM['HELPER-OPEN-CUT']['my_version'], UNIT['B280']['md']

TRAUMA = ('- **Trauma material:** trauma-informed therapy or integration support, without immediate confrontation while '
          'destabilized.\n')
assert UNIT['B426']['md'].count(TRAUMA) == 1, UNIT['B426']['md']
UNIT['B426']['md'] = UNIT['B426']['md'].replace(TRAUMA, '')

text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(text, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before_md)), len(re.findall(r'\S+', text))
print('B280, B426: round 26 in (HELPER-OPEN-CUT and AFT-TRAUMA-ONCE approved)')
print('%d words -> %d (%+d); GUIDE-SO-FAR.md sha256 %s' % (w0, w1, w1 - w0, hashlib.sha256(text.encode()).hexdigest()))
