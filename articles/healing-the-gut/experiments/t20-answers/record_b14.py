#!/usr/bin/env python3
"""Batch 14's answers (Joel, 2026-11-07 01:11 UTC: all five approved, four with "didn't need to ask") checked and
recorded. Each card's version must be r30's paragraph word for word and its "before" r22's: F14-1's version is Phase 4's
first paragraph with the step joined (r30's block 58) and its "before" the step (r22's block 59, which the card cuts); F14-2
to F14-5 are r22's blocks 62 to 65, r30's 61 to 64. r30 is then r22 with every card in, so r30 is the article with every
answer in. His comments go into FATES-b14.json word for word; the oxytocin one is acted on in r31 (lesson gut-2026-11-07c).
Exits 1 if a card isn't as approved."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parents[1] / 'humanize' / 'fix-20261103'
REPO = HERE.parents[3]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

answers = json.loads((HERE / 'REVIEW-ANSWERS-b14.json').read_text(encoding='utf-8'))
review = json.loads((FIX / 'r30' / 'b14' / 'REVIEW.json').read_text(encoding='utf-8'))
assert answers['review_id'] == review['review_id'] == 'healing-the-gut-b14-r30-20261107'
b22 = [b['text'] for b in sr.blocks((FIX / 'r22' / 'r22.md').read_text(encoding='utf-8'))]
b30 = [b['text'] for b in sr.blocks((FIX / 'r30' / 'r30.md').read_text(encoding='utf-8'))]
WANT = {'F14-1': (58, [59]), 'F14-2': (61, [62]), 'F14-3': (62, [63]), 'F14-4': (63, [64]), 'F14-5': (64, [65])}
cards = {c['id']: c for c in review['suggestions']}
fates, bad = [], []
for item in answers['items']:
    new, old = WANT[item['id']]
    ok = (item['status'] == 'approved' and not item['your_version'].strip() and item['my_version'] == b30[new]
          and item['before'].split('\n\n') == [b22[i] for i in old]
          and [e['block'] for e in cards[item['id']]['edits']] in ([58, 59], old))
    bad += [] if ok else [item['id']]
    fates.append({'id': item['id'], 'title': item['title'], 'status': item['status'], 'at': item['updated'],
                  'comment': item['comment'], 'in_r30': ok,
                  'fate': ('in r30 as approved, word for word' if ok else 'NOT as approved: check')
                  + ('; the oxytocin gloss corrected in r31 after his comment' if item['id'] == 'F14-3' else '')})
# r30 is r22 with the five cards in and nothing else: every other block the same, in order
rest22 = [t for i, t in enumerate(b22) if i not in (59, 62, 63, 64, 65) and i != 58]
rest30 = [t for i, t in enumerate(b30) if i not in (58, 61, 62, 63, 64)]
assert rest22 == rest30 and len(b22) == len(b30) + 1
(HERE / 'FATES-b14.json').write_text(json.dumps({'review_id': answers['review_id'], 'counts': answers['counts'],
                                                 'fates': fates}, ensure_ascii=False, indent=1) + '\n',
                                     encoding='utf-8')
for f in fates:
    print(f['id'], f['status'], f['fate'], '|', f['comment'])
sys.exit(1 if bad else 0)
