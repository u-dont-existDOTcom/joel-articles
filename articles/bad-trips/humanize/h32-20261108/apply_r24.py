#!/usr/bin/env python3
"""apply_r24.py - his round-24 answers of 2026-11-08 15:01 UTC put into the guide
(../../review/r24/ANSWERS-R24-20261108-1501.json; his message, ../../experiments/t26-answers/).

Both cards came back revised, with his own versions, each checked by him in Pangram:
- TEACH-FIRM. He tested his don'ts after the first five minutes, as the card's tests had been, and fixed what read
  Medium in his first try (6f85cc29: the reminder and its script, and the last sentence) until the whole text read Human
  at High as one window (82851dc3). So three of its parts change the guide:
  - B242 and B243, the reminder and its script, become his one sentence (the practice case, B244, stays after it: his test
    stopped at the reminder, as the card's base did);
  - B283 and B284, the Don't heading and its three bullets, become his anchor sentence and his don'ts paragraph under the
    same heading (in his test the anchor sentence stood where the section's heading was, and "So don't" follows it).
- His (Re)defining "Bad Trip" (in TEACH-FIRM's comment: "this looks like it's also duplicating stuff in redefining bad
  trip section... so let's change that to this which is a little bit less redundant"): B330 and B331 become his three
  paragraphs. Not yet checked in Pangram.
- TEACH-LABELS: his Give the Session a Beginning and an End (Human, High as one 429-word window, 0469ebb9): B366 to B368
  (the opening, "When you have a choice:" and the six labelled bullets, the card's scope) become his seven paragraphs. The
  section's picture (B365) and its triage-app line (B370) stay, as they were outside the card.

His typos, fixed and checked (bad-trips-2026-11-07e): "people ... purify themself" -> "themselves"; trailing spaces.

  python3 apply_r24.py      write the guide (GUIDE-SO-FAR.md and its blocks) and print what changed
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
ANS = json.loads((ART / 'review/r24/ANSWERS-R24-20261108-1501.json').read_text(encoding='utf-8'))
ITEMS = {x['id']: x for x in ANS['items']}

BLOCKS = json.loads((HERE / 'GUIDE-BEFORE-R24-blocks.json').read_text(encoding='utf-8'))   # the guide after round 23, frozen
before = (HERE / 'GUIDE-BEFORE-R24.md').read_text(encoding='utf-8')
assert '\n\n'.join(b['md'] for b in BLOCKS) + '\n' == before, 'the blocks and the guide disagree'
UNIT = {b['id']: b for b in BLOCKS}


def paras(text):
    return [p.strip() for p in text.replace('\r', '').split('\n\n') if p.strip()]


# TEACH-FIRM: his test text, the first five minutes through his don'ts
firm = paras(ITEMS['TEACH-FIRM']['your_version'])
assert firm[0] == 'Psychological First Aid: The First Five Minutes', firm[0]
assert firm[1] == UNIT['B236']['md'] and firm[2] == UNIT['B240']['md'], 'his base differs from the guide'
assert UNIT['B242']['md'].startswith('Then remind them where they are') and UNIT['B243']['kind'] == 'blockquote'
HIS_REMIND, HIS_ANCHOR, HIS_DONTS = firm[3], firm[4], firm[5]
assert HIS_REMIND.startswith('Sometimes it can be helpful to remind them') and HIS_ANCHOR.startswith('As the person helping')
assert HIS_DONTS.startswith("So don't try to win an argument") and len(firm) == 6

# his (Re)defining "Bad Trip", in the same card's comment
c = ITEMS['TEACH-FIRM']['comment']
redef = paras(c[c.index('(Re)defining "Bad Trip"'):])
assert redef[0] == '(Re)defining "Bad Trip"' and len(redef) == 4, len(redef)
HIS_REDEF = redef[1:]

# TEACH-LABELS: his Give the Session, heading first
labels = ITEMS['TEACH-LABELS']['your_version'].replace('\r', '')
head, rest = labels.split('\n', 1)
assert head.strip() == 'Give the Session a Beginning and an End'
HIS_SESSION = [' '.join(l.strip() for l in p.split('\n')) for p in paras(rest)]
assert len(HIS_SESSION) == 7, len(HIS_SESSION)
TYPOS = [('purify themself', 'purify themselves')]
for a, b in TYPOS:
    assert sum(p.count(a) for p in HIS_SESSION) == 1, a
    HIS_SESSION = [p.replace(a, b) for p in HIS_SESSION]

new, n = [], 0


def block(bid, kind, md):
    return {'id': bid, 'kind': kind, 'md': md, 'text': None}


for b in BLOCKS:
    i = b['id']
    if i == 'B242':
        new.append(dict(b, md=HIS_REMIND)); n += 1
    elif i == 'B243':
        continue
    elif i == 'B284':
        new.append(block('B284a', 'p', HIS_ANCHOR)); new.append(block('B284b', 'p', HIS_DONTS)); n += 1
    elif i == 'B330':
        for k, p in enumerate(HIS_REDEF):
            new.append(block('B330%s' % 'abc'[k], 'p', p))
        n += 1
    elif i == 'B331':
        continue
    elif i == 'B366':
        for k, p in enumerate(HIS_SESSION):
            new.append(block('B366%s' % 'abcdefg'[k], 'p', p))
        n += 1
    elif i in ('B367', 'B368'):
        continue
    else:
        new.append(b)
assert n == 4
after = '\n\n'.join(b['md'] for b in new) + '\n'
MD.write_text(after, encoding='utf-8')
BJ.write_text(json.dumps(new, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('%d words -> %d (%+d): B242-B243 his reminder; B284 his anchor and don\'ts; B330-B331 his (Re)defining; '
      'B366-B368 his Give the Session' % (len(before.split()), len(after.split()), len(after.split()) - len(before.split())))
