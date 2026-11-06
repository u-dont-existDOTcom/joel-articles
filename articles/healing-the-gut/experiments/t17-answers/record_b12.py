#!/usr/bin/env python3
"""Batch 12's answers (Joel, 2026-11-06 21:06 UTC: all three cards approved) checked against r17 and recorded.

Each approved card's version must be r17's text word for word, block by block, and its "before" r12's (the text on his
page), so r17 is the article with every answer in and draft B (r17's payload, 3,992 words) carries exactly what he
approved. Writes FATES-b12.json; exits 1 if a card's text isn't where it should be."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parents[1] / 'humanize' / 'fix-20261103'
REPO = HERE.parents[3]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

answers = json.loads((HERE / 'REVIEW-ANSWERS-b12.json').read_text(encoding='utf-8'))
review = json.loads((FIX / 'r17' / 'b12' / 'REVIEW.json').read_text(encoding='utf-8'))
assert answers['review_id'] == review['review_id'] == 'healing-the-gut-b12-r17-20261106'
b12 = [b['text'] for b in sr.blocks((FIX / 'r12' / 'r12.md').read_text(encoding='utf-8'))]
b17 = [b['text'] for b in sr.blocks((FIX / 'r17' / 'r17.md').read_text(encoding='utf-8'))]
cards = {c['id']: c for c in review['suggestions']}
fates, bad = [], []
for item in answers['items']:
    card = cards[item['id']]
    blocks = [e['block'] for e in card['edits']]
    mine = item['my_version'].split('\n\n')
    before = item['before'].split('\n\n')
    ok = (item['status'] == 'approved' and not item['your_version'].strip()
          and mine == [b17[i] for i in blocks] and before == [b12[i] for i in blocks])
    if not ok:
        bad.append(item['id'])
    fates.append({'id': item['id'], 'title': item['title'], 'status': item['status'], 'at': item['updated'],
                  'blocks': blocks, 'in_r17': ok,
                  'fate': 'in r17 as approved, word for word; in draft B' if ok else 'NOT as approved: check'})
(HERE / 'FATES-b12.json').write_text(json.dumps({'review_id': answers['review_id'], 'counts': answers['counts'],
                                                 'fates': fates}, ensure_ascii=False, indent=1) + '\n',
                                     encoding='utf-8')
for f in fates:
    print(f['id'], f['status'], f['fate'])
sys.exit(1 if bad else 0)
