#!/usr/bin/env python3
"""apply_r13.py - round 13's answer (Joel, exported 2026-11-07 00:01 UTC; ANSWERS-R13-20261107-0001.json) put into the
guide: ANCHOR-OPPOSITE (Get One Human Anchor's first paragraph, its second sentence said as talk) and ANCHOR-BACKUP (its
second paragraph, with its limit said as an aside), both approved with no comment.

The cards worked on the page's plain text; the guide keeps its Markdown: the second paragraph keeps its bold on the two
people it names, as the card said ("The bold stays on the two people it names."). The page his export names (PAGE-R13.md)
was made before Who to Contact's and Alone at 3 a.m.'s repeats were cut (../../experiments/t19-anchor/apply_t19d.py),
which touch neither paragraph; each paragraph is checked against the card's "before".

  python3 apply_r13.py      write the guide after round 13 and print what changed
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
REVIEW = json.loads((HERE / 'REVIEW-R13.json').read_text(encoding='utf-8'))
ANSWERS = json.loads((HERE / 'ANSWERS-R13-20261107-0001.json').read_text(encoding='utf-8'))

assert ANSWERS['review_id'] == REVIEW['review_id'] == 'bad-trips-r13'
assert hashlib.sha256((HERE / 'PAGE-R13.md').read_bytes()).hexdigest() == ANSWERS['article']['sha256']
ITEM = {x['id']: x for x in ANSWERS['items']}
assert set(ITEM) == {s['id'] for s in REVIEW['suggestions']} == {'ANCHOR-OPPOSITE', 'ANCHOR-BACKUP'}
assert all(ITEM[k]['status'] == 'approved' and not ITEM[k]['your_version'] for k in ITEM), 'not both approved as they were'
before_md = MD.read_text(encoding='utf-8')
assert '\n\n'.join(b['md'] for b in BLOCKS) + '\n' == before_md, 'the blocks and the guide disagree'
UNIT = {b['id']: b for b in BLOCKS}


def plain(s):
    return re.sub(r'\*\*(.+?)\*\*', r'\1', s)


assert plain(UNIT['B254']['md']) == ITEM['ANCHOR-OPPOSITE']['before'], UNIT['B254']['md']
assert plain(UNIT['B255']['md']) == ITEM['ANCHOR-BACKUP']['before'], UNIT['B255']['md']
NEW = {
    'B254': ITEM['ANCHOR-OPPOSITE']['my_version'],
    'B255': ("So **one calm person should be the anchor** and take the lead. One person can only handle so much, though. "
             "When fatigue or logistics get to be too much, or keeping them safe does, or there's a risk of violence or "
             "self-harm, bring in **one more calm adult or a crisis professional** to back them up."),
}
assert plain(NEW['B255']) == ITEM['ANCHOR-BACKUP']['my_version']
for bid, md in NEW.items():
    UNIT[bid]['md'] = md
text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(text, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before_md)), len(re.findall(r'\S+', text))
print('B254, B255: round 13 in (both cards approved)')
print('%d words -> %d (%+d); GUIDE-SO-FAR.md sha256 %s' % (w0, w1, w1 - w0, hashlib.sha256(text.encode()).hexdigest()))
