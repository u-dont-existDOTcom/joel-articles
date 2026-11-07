#!/usr/bin/env python3
"""Batch 13's answer (Joel, 2026-11-06 23:59 UTC: F13-1 approved) checked and recorded, and r22 built: r17 with the
approved card, the article with every answer in. The card's version must be r21's block 28 word for word and its
"before" r17's. Writes FATES-b13.json and ../../humanize/fix-20261103/r22/r22.md; exits 1 if the card isn't as approved."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parents[1] / 'humanize' / 'fix-20261103'
REPO = HERE.parents[3]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

answers = json.loads((HERE / 'REVIEW-ANSWERS-b13.json').read_text(encoding='utf-8'))
review = json.loads((FIX / 'r21' / 'b13' / 'REVIEW.json').read_text(encoding='utf-8'))
assert answers['review_id'] == review['review_id'] == 'healing-the-gut-b13-r21-20261106'
md17 = (FIX / 'r17' / 'r17.md').read_text(encoding='utf-8')
b17 = [b['text'] for b in sr.blocks(md17)]
b21 = [b['text'] for b in sr.blocks((FIX / 'r21' / 'r21.md').read_text(encoding='utf-8'))]
cards = {c['id']: c for c in review['suggestions']}
fates, bad, md22 = [], [], md17
for item in answers['items']:
    card = cards[item['id']]
    blocks = [e['block'] for e in card['edits']]
    ok = (item['status'] == 'approved' and not item['your_version'].strip()
          and item['my_version'].split('\n\n') == [b21[i] for i in blocks]
          and item['before'].split('\n\n') == [b17[i] for i in blocks])
    if ok:
        for i in blocks:
            assert md22.count(b17[i]) == 1
            md22 = md22.replace(b17[i], b21[i])
    else:
        bad.append(item['id'])
    fates.append({'id': item['id'], 'title': item['title'], 'status': item['status'], 'at': item['updated'],
                  'blocks': blocks, 'in_r22': ok,
                  'fate': 'in r22 as approved, word for word' if ok else 'NOT as approved: check'})
(FIX / 'r22').mkdir(exist_ok=True)
(FIX / 'r22' / 'r22.md').write_text(md22, encoding='utf-8')
(HERE / 'FATES-b13.json').write_text(json.dumps({'review_id': answers['review_id'], 'counts': answers['counts'],
                                                 'fates': fates}, ensure_ascii=False, indent=1) + '\n',
                                     encoding='utf-8')
for f in fates:
    print(f['id'], f['status'], f['fate'])
sys.exit(1 if bad else 0)
