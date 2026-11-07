#!/usr/bin/env python3
"""Making-sense receipts (gate E365) for r09's section check (texts.py). Every sentence has its row: the live post's
sentences as well as mine, since the article's published text is not only his own words (gate E373).
Writes CHECK-<name>.txt and RECEIPT-<name>.json and checks each; exits 1 if one fails."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[5] / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
from texts import TEXTS  # noqa: E402

U = 'none: the live post’s sentence, unchanged, in its place in his story'
Q_ = 'none: the next question in his run of questions'
R = {
    'r09-dam': ('Holding up a leaky dam', 'Someone a few weeks into a relationship, deciding whether their growing certainty '
                'about the person is earned.', 'It tells the reader attachment turns a chance into certainty, which they may be '
                'feeling now.', [
        ('once attached, a chance becomes "she’s the right person"', 'opens the section', None),
        ('he asks what that certainty rests on', 'the challenge to it', 'Based on what?'),
        ('sometimes he learned something, sometimes only got attached, which makes it hard to question', 'the two answers',
         'Sometimes I actually learned something'),
        ('quick sex is a reason not to move in quickly too', 'what follows for living together', 'move in quickly too'),
        ('moving in right away is a common-law marriage without discussing it', 'why moving in waits', 'Moving in together right away'),
        ('so keep friends, a community, and dates to check in, since being entangled can pass for going well', 'what to do '
         'instead', 'So I want us to'),
        ('wanting her comes much sooner than knowing about children, community or a life together', 'why it takes time',
         'I can know I want her'),
        ('one of you will ask why they are special', 'the question that comes', 'At some point one of you will ask'),
        ('why them and not somebody else', 'the same question pressed', 'none: the second half of the quoted question'),
        ('if the answer is only that you had sex and got hitched', 'the bad answer', 'If the answer is basically'),
        ('that is a shame', 'his verdict', 'that’s a damn shame'),
    ]),
}
Q = {
    'Q1': 'PASS: each changed sentence gives its point first, in plain words',
    'Q2': 'N/A: these sections tell and ask; the advice in them is unchanged',
    'Q3': 'PASS: the people, places, numbers and things are named as in the live post',
    'Q4': 'PASS: no new term',
    'Q5': 'PASS: each sentence’s tie is in its words (the links field), or the link says why it needs none',
    'Q6': 'PASS: the order is the live post’s, with the reorders r03 to r05 recorded for the changed paragraphs',
    'Q7': 'PASS: each change keeps what the section tells the reader about their own case',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence in the changed paragraphs',
}
CHECKED = {}
bad = 0
for name, text in TEXTS.items():
    section, reader, why, rows = R[name]
    r = S.make(text, section, reader)
    assert len(r['sentences']) == len(rows), (name, len(r['sentences']), len(rows))
    for s, (pay, fol, link) in zip(r['sentences'], rows):
        s['payoff'], s['follows'] = 'the reader learns ' + pay, fol
        if 'link' in s:
            s['link'] = link
    r['opens']['why_reading'] = why
    r['same_point'] = 'none: read the section from its heading to the next for these points; each is made once, here'
    r['questions'] = dict(Q)
    r['checked'] = CHECKED.get(name, [{'point': 'the AI window’s point', 'found': 'the live post (../../live-check/AI-WINDOWS.json)',
                                       'still_needed': 'yes: the section needs it', 'fate': 'changed'}])
    r['placement'] = 'The whole section in its place in the live post, from its heading to the next.'
    (HERE / ('CHECK-%s.txt' % name)).write_text(text, encoding='utf-8')
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
