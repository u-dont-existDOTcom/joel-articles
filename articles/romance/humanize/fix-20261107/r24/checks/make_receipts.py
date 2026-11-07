#!/usr/bin/env python3
"""Making-sense receipts (gate E365) for r24's checks (texts.py). Every sentence has its row: a sentence an earlier
receipt in this article already has a row for keeps it (r21's to r23's included); the rest are written here. Writes
CHECK-<name>.txt and RECEIPT-<name>.json and checks each; exits 1 if one fails."""
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
    if '/r24/' in f:
        continue
    for s in json.load(open(f, encoding='utf-8')).get('sentences', []):
        if s.get('s') and s.get('payoff'):
            OLD[s['s'].strip()] = (s['payoff'], s['follows'], s.get('link'))
NEW = {
    'Maybe I do talk about them too much sometimes, but they still matter':
        ('maybe he talks about exes too much, but they still matter to him', 'his answer to her request', 'Maybe'),
    'If I’m supposed to listen to everything on her mind, I don’t want to have to pretend they':
        ('if he listens to all on her mind, he won’t pretend his exes aren’t on his', 'why they stay in his talk',
         'If I’m supposed to listen'),
}
META = {
    'r24-jeal366': ('Jealousy (366 to 370)', 'Someone in, or weighing, a monogamous or polyamorous relationship.',
                    'It tells the reader which kind of honesty each kind of relationship needs.'),
    'r24-ideal': ('Beware idealization (143 to 151)', 'Someone being idealized by a new partner.',
                  'It tells the reader why too much idealization is a warning sign.'),
}
Q = {
    'Q1': 'PASS: each changed sentence gives its point first, in plain words',
    'Q2': 'N/A: these paragraphs tell; they give no advice beyond what the live post gives',
    'Q3': 'PASS: the people are named as in the live post',
    'Q4': 'PASS: no new term; BPD is used earlier in the article',
    'Q5': 'PASS: each sentence’s tie is in its words (the links field), or it opens its paragraph',
    'Q6': 'PASS: the order is the live post’s',
    'Q7': 'PASS: each change keeps what the paragraph tells the reader',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence',
}
LOW = {
    'r24-jeal366': [{'point': 'the AI windows on 366 to 370', 'found': 'r21’s stretch (#119), then its paragraphs (#124, '
                     '#127, #128)', 'still_needed': 'yes', 'fate': 'changed'}],
    'r24-ideal': [{'point': 'the AI windows on 151’s end', 'found': 'r23’s section check (#130)', 'still_needed': 'yes',
                   'fate': 'changed'}],
}
PLACE = {
    'r24-jeal366': '366 to 370: r22’s 367 and r23’s 368 and 369 with the paragraph before and after (E349).',
    'r24-ideal': 'The section, 143 to 151, with r22’s 147 and 148 and 151’s short sentences joined.',
}
bad = 0
for name in META:
    text = TEXTS[name]
    section, reader, why = META[name]
    r = S.make(text, section, reader)
    for s in r['sentences']:
        row = next((v for k, v in NEW.items() if s['s'].startswith(k)), None) or OLD.get(s['s'].strip())
        assert row, ('no row', name, s['s'][:60])
        pay, fol, link = row
        s['payoff'] = pay if pay.startswith('the reader learns ') else 'the reader learns ' + pay
        s['follows'] = fol
        if 'link' in s:
            s['link'] = link or 'none: it opens its paragraph, and the paragraph before it ends its own point'
    r['opens']['why_reading'] = why
    r['same_point'] = 'none: read the section from its heading to the next for these points; each is made once, here'
    r['questions'] = dict(Q)
    r['checked'] = LOW[name]
    r['placement'] = PLACE[name]
    (HERE / ('CHECK-%s.txt' % name)).write_text(text, encoding='utf-8')
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
