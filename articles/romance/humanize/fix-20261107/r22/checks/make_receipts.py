#!/usr/bin/env python3
"""Making-sense receipts (gate E365) for r22's checks (texts.py). Every sentence has its row: a sentence an earlier
receipt in this article already has a row for keeps it (r21's included); the rest are written here. Writes
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
    if '/r22/' in f:
        continue
    for s in json.load(open(f, encoding='utf-8')).get('sentences', []):
        if s.get('s') and s.get('payoff'):
            OLD[s['s'].strip()] = (s['payoff'], s['follows'], s.get('link'))
NEW = {
    'I’d rather be able to say “she’s cute”':
        ('he’d rather both partners can mention a small attraction without a fight', 'his own preference', None),
    'If only the serious crushes get mentioned':
        ('if only serious crushes get mentioned, each is a confession and people hide them all',
         'why he’d rather have it so: what happens otherwise', 'the serious crushes'),
    'Plenty of couples vow to be together forever':
        ('far more couples promise lifelong exclusivity than live it', 'opens the paragraph', None),
    'In a polyamorous relationship the boundaries might be more negotiable, but then somebody':
        ('polyamory’s boundaries can be negotiated, so someone has to negotiate them', 'the other kind of relationship',
         'In a polyamorous relationship'),
    'Polyamory can be dishonest too:':
        ('polyamory can be dishonest too: a way to cope with not connecting deeply, or to admit no self-control '
         'without the work that would make it ethical', 'opens the paragraph: the other side', None),
    'If you can’t do monogamy, it’s more honest to say so':
        ('admitting you can’t do monogamy is more honest, since pretending can hurt more than an affair',
         'what is still true', 'monogamy'),
    'If she says, “You’re perfect, I can’t find any flaw,”':
        ('if she says I’m perfect and flawless, he runs', 'the unhealthy case after the healthy one', 'If she says'),
    'I don’t mean it as a clinical diagnosis':
        ('he uses it almost like a diagnosis, though it isn’t a clinical one', 'a caveat on that claim', 'it'),
    'When the BPD splitting happens, she can go from worshipping me':
        ('with BPD splitting, she can go from worshipping him to hating him, privately and then publicly',
         'what the extreme leads to', 'worshipping me'),
    'Suddenly she can find plenty of flaws':
        ('then she finds plenty of flaws and reads them all as signs he was faking', 'more of what follows, against '
         'her "I can’t find any flaw"', 'Suddenly she can find plenty of flaws'),
    'Sometimes she ends up accusing me of thinking I’m perfect':
        ('sometimes she accuses him of thinking he’s perfect, though she was the one who said he was',
         'the irony it ends on', 'she'),
}
META = {
    'r22-jeal366': ('Jealousy (366 to 370)', 'Someone in, or weighing, a monogamous or polyamorous relationship.',
                    'It tells the reader which kind of honesty each kind of relationship needs.'),
    'r22-ideal147': ('Beware idealization (147 and 148)', 'Someone being idealized by a new partner.',
                     'It tells the reader why too much idealization is a warning sign.'),
    'r22-jeal367': ('Jealousy (367)', 'Someone in, or weighing, a monogamous relationship.',
                    'It tells the reader why small attractions should be mentionable.'),
    'r22-jeal368': ('Jealousy (368 and 369)', 'Someone weighing a monogamous or polyamorous relationship.',
                    'It tells the reader where each kind of relationship can turn dishonest.'),
    'r22-jeal369': ('Jealousy (369)', 'Someone weighing a polyamorous relationship.',
                    'It tells the reader how polyamory can be dishonest too.'),
    'r22-romance': ('Romance (282 to 290)', 'A woman or man wondering how strength and surrender fit together.',
                    'It tells the reader that letting a partner lead or care for you is a choice, not weakness.'),
}
Q = {
    'Q1': 'PASS: each changed sentence gives its point first, in plain words',
    'Q2': 'N/A: these paragraphs tell; they give no advice beyond what the live post gives',
    'Q3': 'PASS: the people and practices are named as in the live post',
    'Q4': 'PASS: no new term; BPD is used earlier in the article',
    'Q5': 'PASS: each sentence’s tie is in its words (the links field), or it opens its paragraph',
    'Q6': 'PASS: the order is the live post’s',
    'Q7': 'PASS: each change keeps what the paragraph tells the reader',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence',
}
LOW = {
    'r22-jeal366': [{'point': 'the AI windows on 366 to 370', 'found': 'r21’s stretch check (#119)', 'still_needed': 'yes',
                     'fate': 'changed'}],
    'r22-ideal147': [{'point': 'the AI window on 148 and the Low ones on 147’s quote and the punchline',
                      'found': 'r21’s pair check (#121)', 'still_needed': 'yes', 'fate': 'changed'}],
    'r22-jeal367': [{'point': 'the AI windows on 367', 'found': 'r21’s stretch check (#119)', 'still_needed': 'yes',
                     'fate': 'changed'}],
    'r22-jeal368': [{'point': 'the AI windows on 368 and 369', 'found': 'r21’s stretch check (#119)', 'still_needed': 'yes',
                     'fate': 'changed'}],
    'r22-jeal369': [{'point': 'the AI windows on 369', 'found': 'r21’s stretch check (#119)', 'still_needed': 'yes',
                     'fate': 'changed'}],
    'r22-romance': [{'point': 'the AI and Low windows on 285 to 287', 'found': 'the section check #98, then r21’s stretch '
                     '(#120, all High or Medium)', 'still_needed': 'yes', 'fate': 'changed'}],
}
PLACE = {
    'r22-jeal366': '366 to 370: the new 367 to 369 with the paragraph before and after it (E349).',
    'r22-ideal147': '147 (its disclaimer reworded, its quote joined) with the new 148, after the tell panel (../panel-ideal147/PANEL.md).',
    'r22-jeal367': '367 by itself, narrowing the stretch (E343).',
    'r22-jeal368': '368 with 369 after it (368 alone is under 50 words), narrowing the stretch (E343, E349).',
    'r22-jeal369': '369 by itself, narrowing the stretch (E343).',
    'r22-romance': 'The section, 282 to 290, as #98 had it, with r21’s 285 to 287.',
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
