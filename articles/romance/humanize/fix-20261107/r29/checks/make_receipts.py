#!/usr/bin/env python3
"""Making-sense receipt (gate E365) for r29-jeal: r27-jeal-b's receipt rows, with the one changed sentence's row."""
import glob
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import sense_receipt as S  # noqa: E402
from texts import TEXTS  # noqa: E402

OLD = {}
for f in sorted(glob.glob(str(ROOT / 'articles' / 'romance' / 'humanize' / '**' / 'RECEIPT-*.json'), recursive=True)):
    if '/r29/' in f:
        continue
    for s in json.load(open(f, encoding='utf-8')).get('sentences', []):
        if s.get('s') and s.get('payoff'):
            OLD[s['s'].strip()] = (s['payoff'], s['follows'], s.get('link'))
NEW = {'Polyamory can also be a way of escaping deeper intimacy, like the college friend': (
    'polyamory can be a way to escape deeper intimacy, like the college friend with four girlfriends from Labels',
    'the drama of negotiating', 'can also be')}
prev = json.load(open(HERE.parents[1] / 'r27' / 'checks' / 'RECEIPT-r27-jeal-b.json', encoding='utf-8'))
text = TEXTS['r29-jeal']
r = S.make(text, prev['section'], prev['reader'])
for s in r['sentences']:
    row = next((v for k, v in NEW.items() if s['s'].startswith(k)), None) or OLD.get(s['s'].strip())
    assert row, s['s'][:60]
    pay, fol, link = row
    s['payoff'] = pay if pay.startswith('the reader learns ') else 'the reader learns ' + pay
    s['follows'] = fol
    if 'link' in s:
        s['link'] = link or 'none: it opens its paragraph, and the paragraph before it ends its own point'
for k in ('opens', 'same_point', 'questions', 'placement', 'needed'):
    r[k] = prev[k]
r['opens']['first_sentence'] = S.sentences(text)[0]
r['checked'] = [{'point': 'the college friend told twice (his answer to ASK-FRIEND-TWICE: "agree with your plan")',
                 'found': 'Labels 40 and his 369', 'still_needed': 'yes: they meet the friend once and are pointed back',
                 'fate': 'changed'}]
(HERE / 'RECEIPT-r29-jeal.json').write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
p = S.check(text, r)
print('r29-jeal', 'PASS' if not p else p)
sys.exit(1 if p else 0)
