#!/usr/bin/env python3
"""apply_r27.py - round 27's answers (Joel, exported 2026-11-09 01:24 UTC; ANSWERS-R27-20261109-0124.json) put into the
guide.

- BACK-HIERARCHY-WHY and BACK-GROUNDING-LOVE, approved: in as their cards had them.
- TEACH-LOOP, revised with his comment: "why did you lose my fixes from before? i'm putting them back and adding the fear
  panic loop plus my experience", then his Psychological First Aid as one piece. His round-24 version had the helper's
  anchor line and don'ts right after the first five minutes, and apply_r24.py put them under For the Person Helping's
  Don't instead (lesson bad-trips-2026-11-09b). So his five new paragraphs go in after the first five minutes, as he wrote
  them, and the Don't heading and its two paragraphs (B283, B284a, B284b), which his version now says in its place, go.
  The practice paragraph (B244, round 12's approved card), which his piece doesn't touch, stays right after his reminder,
  since it is that reminder's practice case. The Fear/Panic Loop section stays for now: whether it goes, now that his
  first five minutes has the panic loop, is on the decision page.
- TEACH-AFTERMATH, revised with his version (checked High: 85f35730): in as he wrote it, its labels kept bold in the
  guide's list.

Obvious typos fixed, each listed in TYPOS below. His comment on the aftermath card asks for my best first, with options,
pros and cons, and the choices that matter most: the decision page (lesson bad-trips-2026-11-09a).

  python3 apply_r27.py      write the guide after round 27 and print what changed
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
REVIEW = json.loads((HERE / 'REVIEW-R27.json').read_text(encoding='utf-8'))
ANSWERS = json.loads((HERE / 'ANSWERS-R27-20261109-0124.json').read_text(encoding='utf-8'))
assert ANSWERS['review_id'] == REVIEW['review_id'] == 'bad-trips-r27'
assert hashlib.sha256((HERE / 'PAGE-R27.md').read_bytes()).hexdigest() == ANSWERS['article']['sha256']
ITEM = {x['id']: x for x in ANSWERS['items']}
assert set(ITEM) == {s['id'] for s in REVIEW['suggestions']}
assert ITEM['BACK-HIERARCHY-WHY']['status'] == ITEM['BACK-GROUNDING-LOVE']['status'] == 'approved'
assert ITEM['TEACH-LOOP']['status'] == ITEM['TEACH-AFTERMATH']['status'] == 'revise'
before_md = MD.read_text(encoding='utf-8')
assert '\n\n'.join(b['md'] for b in BLOCKS) + '\n' == before_md, 'the blocks and the guide disagree'
UNIT = {b['id']: b for b in BLOCKS}
TYPOS = [  # (his text, as fixed, where)
    ('prayer, chanting, on them', 'prayer, chanting on them', 'his first five minutes: the comma left after "a confession or an insight" went'),
    ('more clear aftewards', 'more clear afterwards', 'his first five minutes, the panic loop'),
    ('for benefit all involved', 'to benefit all involved', 'his first five minutes, his own story (a word missing)'),
    ('onr or two trusted people', 'one or two trusted people', 'his aftermath list, shame'),
    ('](shame.u-dont-exist.com)', '](http://shame.u-dont-exist.com/)', 'his aftermath list: the link needed its http:// to open, as his other site links have'),
]


def fix(t):
    for a, b, _ in TYPOS:
        t = t.replace(a, b)
    return t


def at(after_id, new):
    i = [k for k, b in enumerate(BLOCKS) if b['id'] == after_id][0]
    for k, (bid, kind, md) in enumerate(new):
        BLOCKS.insert(i + 1 + k, {'id': bid, 'kind': kind, 'md': md, 'text': None})


# 1. the approvals
at('B87', [('R27-HIER', 'p', ITEM['BACK-HIERARCHY-WHY']['my_version'])])
assert UNIT['B295']['md'] == ITEM['BACK-GROUNDING-LOVE']['before']
UNIT['B295']['md'] = ITEM['BACK-GROUNDING-LOVE']['my_version']
# 2. his first five minutes as one piece
paras = [p.strip() for p in ITEM['TEACH-LOOP']['comment'].split('\n\n') if p.strip()]
assert paras[1] == 'Psychological First Aid: The First Five Minutes'
assert [UNIT[k]['md'] for k in ('B236', 'B240', 'B242')] == paras[2:5]
new = [fix(p) for p in paras[5:]]
assert len(new) == 5 and new[0].startswith('As the person helping') and new[4].startswith('I actually get something like this')
at('B244', [('R27-PFA%d' % (k + 1), 'p', t) for k, t in enumerate(new)])
for bid in ('B283', 'B284a', 'B284b'):
    assert bid in UNIT
BLOCKS[:] = [b for b in BLOCKS if b['id'] not in ('B283', 'B284a', 'B284b')]
# 3. his aftermath list
his = [p.strip() for p in fix(ITEM['TEACH-AFTERMATH']['your_version']).split('\n\n') if p.strip()]
UNIT['B425']['md'] = his[0]
items = []
for p in his[1:]:
    label, rest = p.split(': ', 1)
    items.append('- **%s:** %s' % (label, rest))
assert len(items) == 8, len(items)
UNIT['B426']['md'] = '\n'.join(items)

text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(text, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before_md)), len(re.findall(r'\S+', text))
print('round 27 in: two approvals, his first five minutes (5 paragraphs; the helper\'s Don\'t, 3 blocks, out), his aftermath list')
for a, b, where in TYPOS:
    print('  typo: %r -> %r (%s)' % (a, b, where))
print('%d words -> %d (%+d); GUIDE-SO-FAR.md sha256 %s' % (w0, w1, w1 - w0, hashlib.sha256(text.encode()).hexdigest()))
