#!/usr/bin/env python3
"""His answers on the eighth page (2026-11-24 12:34 UTC, review/teach-20261124b/ANSWERS-T8.json) as a layer over the
fixed version, after r38's junk layer: HIS-T8.json, which whole/build.py applies.

- The two cards he approved (J-B217, J-B255) go in as the cards had them (r38/junk/CARDS-T8.json), each with the check
  that read its section Human High.
- J-B54 he left undecided: it stays as the article has it.
- Q-B476 and Q-B478: his answers say what the passages meant; my fixes of them from his answers are r39/MINE-R39.json.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
ANS = json.loads((ROOT / 'articles/romance/review/teach-20261124b/ANSWERS-T8.json').read_text(encoding='utf-8'))
CARDS = json.loads((HERE.parent / 'r38' / 'junk' / 'CARDS-T8.json').read_text(encoding='utf-8'))
items = {i['id']: i for i in ANS['items']}
assert items['J-B54']['status'] == 'pending'
out = []
for cid in ('J-B217', 'J-B255'):
    it, changes = items[cid], CARDS[cid]
    assert it['status'] == 'approved', cid
    assert it['my_version'] == '\n\n'.join(c['after'][0] for c in changes), cid
    for c in changes:
        out.append({'card': cid, 'kind': 'para', 'live': c['live'], 'before': c['before'], 'after': list(c['after']),
                    'comment': 'approved', 'his_checks': list(c['his_checks']), 'section_key': c['section_key']})
(HERE / 'HIS-T8.json').write_text(json.dumps({
    'about': 'His answers on the eighth marking page (review/teach-20261124b/ANSWERS-T8.json, exported 2026-11-24 12:34 '
             'UTC): the two approved cards. J-B54 he left undecided.', 'whose': 'his', 'changes': out},
    ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('HIS-T8:', len(out), 'changes')
