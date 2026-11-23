#!/usr/bin/env python3
"""His answers on the fifth page (2026-11-22 23:43 UTC, review/teach-20261122/ANSWERS-T5.json) as a layer over the
fixed version, after r30's: HIS-T5.json, which whole/build.py applies.

- Q-409 "change diagnosed to defined then": his M-409 sentence says "literally defined as".
- Q-314 "2nd wife": the live paragraph's "my first wife, Bee" says "my second wife, Bee".
- Q-392: "i had changed her to H.D. because i had put H. for my other friend in therapycircle, heidi. but i guess then
  maybe i removed heidi so if that's the case then we can put HD back to H": no other "H." is left in the article (every
  one is her), so "H.D." is "H." again.
- Q-14 "no i meant and pressuring men into making it look like men know what they want, how can i say that lol": his
  sentence in the words of his answer, "like men know what they want", so the second "they" can only be the men (a
  "themselves" at its end would have doubled the next sentence's "for themselves").
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
T4 = json.loads((HERE.parent / 'r30' / 'HIS-T4.json').read_text(encoding='utf-8'))
LIVE = {}
for line in (HERE.parent / 'live-check' / 'LIVE-POST-BLOCKS-20261122.jsonl').read_text(encoding='utf-8').splitlines():
    r = json.loads(line)
    if r.get('n') is not None:
        LIVE[r['n']] = r['text']
his = {c['card']: c for c in T4['changes']}

EDITS = [  # (live paragraph, card or None for the live words, wrong, right, his words)
    (409, 'M-409', 'literally diagnosed as', 'literally defined as', 'change diagnosed to defined then'),
    (314, None, 'especially my first wife, Bee', 'especially my second wife, Bee', '2nd wife'),
    (392, None, 'like I had with H.D., where', 'like I had with H., where',
     'if that\'s the case then we can put HD back to H'),
    (14, 'M-14', 'pressuring men into making it look like they know what they want.',
     'pressuring men into making it look like men know what they want.',
     'no i meant and pressuring men into making it look like men know what they want, how can i say that lol'),
]
out = []
for n, card, wrong, right, said in EDITS:
    before = his[card]['after'][0] if card else LIVE[n]
    assert before.count(wrong) == 1, (n, wrong)
    out.append({'card': card or 'live %d' % n, 'kind': 'para', 'live': n, 'before': before,
                'after': [before.replace(wrong, right)], 'comment': said, 'his_checks': [], 'was': wrong, 'now': right})
data = {'about': __doc__.strip().split('\n\n')[0], 'answers': 'review/teach-20261122/ANSWERS-T5.json',
        'links': [], 'embeds': [], 'changes': out}
(HERE / 'HIS-T5.json').write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('changes', len(out))
