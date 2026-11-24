#!/usr/bin/env python3
"""His answers on the seventh page (2026-11-24 02:06 UTC, review/teach-20261124/ANSWERS-T7.json) as a layer over the
fixed version, after r37's: HIS-T7.json, which whole/build.py applies.

- The nine cards he approved (M-07, M-16, M-26, M-28, M-31, M-35, M-54, M-68, M-82) go in as the cards had them
  (r37/CARDS-T7.json), each with the check that read its section Human High.
- Q-67 "damn this was an absolute disaster. i fixed it": his own version of "Two Pillars Don't Hold The Roof Up", part 1,
  from his check (his-67.txt, the text Pangram holds for it, SHA-256 d5cab2e8...; Human, High, one window), replaces the
  section's six live paragraphs (330 to 335) with his five.
- Q-42: his answer says what the last clause meant; my fix of that sentence is r38/MINE-R38.json, after this layer.
"""
import hashlib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
ANS = json.loads((ROOT / 'articles/romance/review/teach-20261124/ANSWERS-T7.json').read_text(encoding='utf-8'))
CARDS = json.loads((HERE.parent / 'r37' / 'CARDS-T7.json').read_text(encoding='utf-8'))
items = {i['id']: i for i in ANS['items']}
HIS67 = 'https://www.pangram.com/history/1deb924a-6175-4847-95eb-38e1871287c3'

out = []
for cid, changes in CARDS.items():
    it = items[cid]
    assert it['status'] == 'approved', cid
    # the page showed the card's paragraphs as they would read; his answer carries them back
    assert it['my_version'] == '\n\n'.join(c['after'][0] for c in changes), cid
    for c in changes:
        out.append({'card': cid, 'kind': 'para', 'live': c['live'], 'before': c['before'], 'after': list(c['after']),
                    'comment': 'approved', 'his_checks': list(c['his_checks']), 'section_key': c['section_key']})
q67 = items['Q-67']
assert q67['status'] == 'answered' and HIS67.rsplit('/', 1)[1] in q67['comment'], q67['comment']
his = (HERE / 'his-67.txt').read_bytes()
assert hashlib.sha256(his).hexdigest() == 'd5cab2e8b2c52b33713f4aeb00b45f9c19715f0aa57c157be8e2bcc7e00deff6'
paras = [p.strip() for p in his.decode('utf-8').split('\n\n')]
assert len(paras) == 5
out.append({'card': 'Q-67', 'kind': 'run', 'live': [330, 331, 332, 333, 334, 335], 'after': paras,
            'comment': q67['comment'].split(' https://')[0].strip(), 'his_checks': [HIS67],
            'title': 'Two Pillars Don’t Hold The Roof Up, part 1: his own fix'})
(HERE / 'HIS-T7.json').write_text(json.dumps({
    'about': 'His answers on the seventh marking page (review/teach-20261124/ANSWERS-T7.json, exported 2026-11-24 02:06 '
             'UTC): the nine approved cards, and his own fix of Two Pillars, part 1, from his check.',
    'whose': 'his', 'changes': out}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('HIS-T7: %d changes (%s)' % (len(out), ', '.join(sorted({c['card'] for c in out}))))
