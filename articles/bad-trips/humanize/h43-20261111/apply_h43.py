#!/usr/bin/env python3
"""apply_h43.py - this folder's fixes that read better in Pangram, put into the guide (GUIDE-SO-FAR-blocks.json and
GUIDE-SO-FAR.md). Each is applied only where its old words are in the guide exactly once; a fix whose check read worse
than the words it replaced stays out (RESULTS.md says which).

  python3 apply_h43.py      apply and print each block changed
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
sys.path.insert(0, str(HERE))
import build_tests as T  # noqa: E402

BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
BLOCKS = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in BLOCKS) + '\n' == MD.read_text(encoding='utf-8'), 'the blocks and the guide disagree'

APPLY = [
    # (why, [(old, new), ...]); the checks are in RESULTS.md
    # h42-08-fix2 (Human Low to Medium, 83f4caef) went in with these and came out again the same turn: it dropped
    # "adjunct remedy", his choice kept as K12 in KEEP-AS-IS.json ("the one thing that flipped it was adding 'remedy'
    # to 'adjunct'"); keep_as_is.py check caught it. fix3 keeps the words (apply_h43b.py)
    ('h42-17-fix1: Nausea Smoothers, Human Low to High (d00c127c)', T.FIXES['h42-17']),
    ('h42-30-fix1: Grounding Menu 2, Human Low to Medium (7fd43eaf)', T.FIXES['h42-30']),
    ('h42-20-fix1: Mental Stabilizers 3, AI to Human High throughout (f0dd7b3f)', T.FIXES['h42-20']),
    ('h42-22-fix1: Mental Stabilizers 5, AI to Human High throughout (913f21aa)', T.FIXES['h42-22']),
    ('anchor-a1: Get One Human Anchor, its first two paragraphs, AI to Human (3a3fd073)', [
        ("Many bad trips get worse because somebody is alone with a frightened or over-certain mind. Other times it's the "
         "opposite: too many people crowd in and start advising, arguing, spiritualizing, or panicking.",
         "Being alone with a frightened or over-certain mind can make a bad trip worse. So can a crowd of people telling "
         "them what it all means, or panicking right along with them."),
        ("So **one calm person should be the anchor** and take the lead. One person can only handle so much, though. When "
         "fatigue or logistics get to be too much, or keeping them safe does, or there's a risk of violence or self-harm, "
         "bring in **one more calm adult or a crisis professional** to back them up.",
         "So have **one calm person be the anchor** and take the lead. One person can only handle so much, though. If "
         "fatigue or logistics start getting to be too much for them, or keeping everyone safe does, bring in **one more "
         "calm adult or a crisis professional** to back them up, and do it right away if there's any risk of violence or "
         "self-harm."),
    ]),
]

for why, pairs in APPLY:
    for old, new in pairs:
        hits = [b for b in BLOCKS if old in b['md']]
        assert len(hits) == 1 and hits[0]['md'].count(old) == 1, (why, old[:60], len(hits))
        hits[0]['md'] = hits[0]['md'].replace(old, new)
        print('%s: %s' % (hits[0]['id'], why))
MD.write_text('\n\n'.join(b['md'] for b in BLOCKS) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
