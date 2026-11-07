#!/usr/bin/env python3
"""Making-sense receipt (gate E365) for r19's check (texts.py): 201 by itself. Its first two sentences keep their rows
from r18's receipt; its closing sentence's row is written here. Writes CHECK-<name>.txt and RECEIPT-<name>.json and
checks it; exits 1 if it fails."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
from texts import TEXTS  # noqa: E402

OLD = {s['s'].strip(): (s['payoff'], s['follows'], s.get('link'))
       for s in json.load(open(HERE.parents[1] / 'r18' / 'checks' / 'RECEIPT-r18-nitty.json', encoding='utf-8'))['sentences']}
ROWS = {
    'r19-nitty201': [
        None,
        None,
        ('in a relationship he is suddenly expected to read every mood, and never to use that skill to manipulate',
         'what changes in a relationship', 'All that works wonderfully until'),
    ],
    'r19-nitty201b': [
        None,
        None,
        ('in a relationship he is suddenly expected to read minds and silences and check in, without manipulating',
         'what changes in a relationship', 'All that works wonderfully until'),
    ],
}
SEC = json.load(open(HERE.parents[1] / 'r18' / 'checks' / 'RECEIPT-r18-nitty.json', encoding='utf-8'))['sentences']
ROWS['r19-nitty'] = [(x['payoff'], x['follows'], x.get('link')) for x in SEC[:6]] + [ROWS['r19-nitty201b'][2]]
ROWS['r19-nitty2'] = list(ROWS['r19-nitty'])
FIRST = {'r19-nitty201': ('another person’s insecurities can be exhausting', 'opens the paragraph', None),
         'r19-nitty201b': ('another person’s insecurities can be exhausting', 'opens the paragraph', None)}
Q = {
    'Q1': 'PASS: the changed sentence gives its point first, in plain words',
    'Q2': 'N/A: this paragraph tells; it gives no advice',
    'Q3': 'PASS: the things are named as in the live post',
    'Q4': 'PASS: no new term',
    'Q5': 'PASS: each sentence’s tie is in its words (the links field)',
    'Q6': 'PASS: the order is the live post’s',
    'Q7': 'PASS: the change keeps what the paragraph tells the reader',
    'Q8': 'PASS: no item moved between groups; in the second try the shift goes in with the mind-reading it '
          'repeats',
    'Q9': 'PASS: one step per sentence',
}
LOW = [{'point': 'the AI window’s point', 'found': 'r18’s check of the section (#108, ../../r18/checks/RESULTS-r18.json)',
        'still_needed': 'yes: the paragraph needs it', 'fate': 'changed'}]
bad = 0
for name, text in TEXTS.items():
    r = S.make(text, 'From flow to nitty gritty', 'Someone used to living alone, about to share daily life with a partner.')
    rows = ROWS[name]
    assert len(rows) == len(r['sentences']), (name, len(rows), len(r['sentences']))
    for i, (s, row) in enumerate(zip(r['sentences'], rows)):
        if row is None:
            row = FIRST[name] if i == 0 else OLD[s['s'].strip()]
        pay, fol, link = row
        s['payoff'] = pay if pay.startswith('the reader learns ') else 'the reader learns ' + pay
        s['follows'] = fol
        if 'link' in s:
            s['link'] = link
    r['opens']['why_reading'] = 'It tells the reader what a partner’s moods start to ask of him.'
    r['same_point'] = 'none: read the section from its heading to the next for these points; each is made once, here'
    r['questions'] = dict(Q)
    r['checked'] = LOW
    r['placement'] = ('The whole section, in its place in the live post, its heading left out.' if name in ('r19-nitty', 'r19-nitty2') else
                      'The paragraph by itself, for the section gate (E343), after the section read AI on its last sentence.')
    if name in ('r19-nitty', 'r19-nitty2'):
        r['opens']['why_reading'] = 'It tells the reader how small daily things start to carry weight in a relationship.'
    (HERE / ('CHECK-%s.txt' % name)).write_text(text, encoding='utf-8')
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
