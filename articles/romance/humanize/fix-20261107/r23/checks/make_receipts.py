#!/usr/bin/env python3
"""Making-sense receipts (gate E365) for r23's checks (texts.py). Every sentence has its row: a sentence an earlier
receipt in this article already has a row for keeps it (r21's and r22's included); the rest are written here. Writes
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
    if '/r23/' in f:
        continue
    for s in json.load(open(f, encoding='utf-8')).get('sentences', []):
        if s.get('s') and s.get('payoff'):
            OLD[s['s'].strip()] = (s['payoff'], s['follows'], s.get('link'))
NEW = {
    'I’d rather be able to say “she’s cute” about a woman at the next table, and have my girlfriend say the same about some guy, without it turning into a fight, because':
        ('he’d rather both can mention a small attraction without a fight, since otherwise every mention is a confession '
         'and people hide them', 'his own preference, with its reason', None),
    'Lots of couples promise forever and nobody else':
        ('many couples promise lifelong exclusivity', 'opens the paragraph', None),
    'Look around at how many actually live that way':
        ('far fewer live it', 'the reader can see the gap', 'that way'),
    'In a polyamorous relationship the boundaries might be more negotiable, but then somebody':
        ('polyamory’s boundaries can be negotiated, so someone has to negotiate them', 'the other kind of relationship',
         'In a polyamorous relationship'),
    'Polyamory can be dishonest too, like when':
        ('polyamory can be dishonest too, as when someone who can’t get close to one person dates several and calls it '
         'polyamory', 'opens the paragraph: the other side', None),
    'Or when someone keeps cheating':
        ('or when a cheater announces he’s poly without the work that would make it ethical', 'a second example',
         'Or when'),
    'If you can’t do monogamy, say so':
        ('if you can’t do monogamy, say so, since pretending can hurt more than an affair', 'what to do instead',
         'monogamy'),
}
META = {
    'r23-jeal367': ('Jealousy (367)', 'Someone in, or weighing, a monogamous relationship.',
                    'It tells the reader why small attractions should be mentionable.'),
    'r23-jeal368': ('Jealousy (368 and 369)', 'Someone weighing a monogamous or polyamorous relationship.',
                    'It tells the reader where each kind of relationship can turn dishonest.'),
    'r23-jeal369': ('Jealousy (369)', 'Someone weighing a polyamorous relationship.',
                    'It tells the reader how polyamory can be dishonest too.'),
    'r23-ideal': ('Beware idealization (143 to 151)', 'Someone being idealized by a new partner.',
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
    'r23-jeal367': [{'point': 'the Low window on 367’s second sentence', 'found': 'r22 (#124)', 'still_needed': 'yes',
                     'fate': 'changed'}],
    'r23-jeal368': [{'point': 'the AI windows on 368 and 369', 'found': 'r22 (#125)', 'still_needed': 'yes', 'fate': 'changed'}],
    'r23-jeal369': [{'point': 'the AI window on 369', 'found': 'r22 (#126)', 'still_needed': 'yes', 'fate': 'changed'}],
    'r23-ideal': [{'point': 'the AI and Low windows on 147 and 148', 'found': 'the section check #92, then the pair #123 '
                   '(High and Medium)', 'still_needed': 'yes', 'fate': 'changed'}],
}
PLACE = {
    'r23-jeal367': '367 by itself (E343).',
    'r23-jeal368': '368 with 369 after it (E343, E349).',
    'r23-jeal369': '369 by itself (E343).',
    'r23-ideal': 'The section, 143 to 151, as #92 had it, with r22’s 147 and 148.',
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
