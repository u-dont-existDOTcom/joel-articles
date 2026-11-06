#!/usr/bin/env python3
"""apply_r09.py - round 9's answer (Joel, exported 2026-11-06 16:38 UTC; ANSWERS-R09-20261106-1638.json) put into the
guide: card ROOM-FIRST approved, his exercise. The room's questions (B238) become my fix of the first part, which read
Human, 0% alone (https://www.pangram.com/history/07e19481-bb99-4b40-932f-ab16315f4502), and his annoying-room paragraph
(B239), said plainly in its first sentence, goes.

Starts from the guide after round 8 (../../GUIDE-SO-FAR-blocks.json as main has it after pull request 310, whose page
form is PAGE-R09.md, the SHA-256 his export names) and writes the guide after round 9 (GUIDE-AFTER-R09.md and
GUIDE-AFTER-R09-blocks.json beside this script), which becomes ../../GUIDE-SO-FAR.md.

  python3 apply_r09.py            write the guide after round 9 and print what changed
"""
import hashlib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parent.parent
BLOCKS = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
REVIEW = json.loads((HERE / 'REVIEW-R09.json').read_text(encoding='utf-8'))
ANSWERS = json.loads((HERE / 'ANSWERS-R09-20261106-1638.json').read_text(encoding='utf-8'))
FIX = (ART / 'humanize' / 'h08-20261106' / 'FIX-P5P6.txt').read_text(encoding='utf-8').strip()
OUT = HERE / 'GUIDE-AFTER-R09.md'
OUT_BLOCKS = HERE / 'GUIDE-AFTER-R09-blocks.json'

assert ANSWERS['review_id'] == REVIEW['review_id'] == 'bad-trips-r09', (ANSWERS['review_id'], REVIEW['review_id'])
assert hashlib.sha256((HERE / 'PAGE-R09.md').read_bytes()).hexdigest() == ANSWERS['article']['sha256']
ITEM = {x['id']: x for x in ANSWERS['items']}
assert set(ITEM) == {s['id'] for s in REVIEW['suggestions']} == {'ROOM-FIRST'}
card = ITEM['ROOM-FIRST']
assert card['status'] == 'approved', card['status']
assert hashlib.sha256(FIX.encode()).hexdigest() == 'a700044065ec140c6ddf5cdc768f319e8c2e8608b9cf8d91af0eddfbe424d9e1'
assert card['my_version'].split('\n\n')[0] == FIX

UNIT = {b['id']: b for b in BLOCKS}


def plain(md):
    return re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'\1', md).strip()


assert plain(UNIT['B238']['md']) + '\n\n' + plain(UNIT['B239']['md']) == card['before'].strip()
assert all('](' not in UNIT[i]['md'] for i in ('B238', 'B239')), 'a link in a paragraph the card changes'
UNIT['B238']['md'] = FIX
BLOCKS = [b for b in BLOCKS if b['id'] != 'B239']

text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
OUT.write_text(text, encoding='utf-8')
OUT_BLOCKS.write_text(json.dumps([{'id': b['id'], 'kind': b['kind'], 'md': b['md'], 'text': None} for b in BLOCKS],
                                 ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
before = (ART / 'GUIDE-SO-FAR.md').read_text(encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before)), len(re.findall(r'\S+', text))
print('B238: ROOM-FIRST, my fix of the first part (07e19481, Human); B239 out')
print('1 card applied; %d words -> %d (%+d); %s sha256 %s' % (w0, w1, w1 - w0, OUT.name,
                                                              hashlib.sha256(text.encode()).hexdigest()))
