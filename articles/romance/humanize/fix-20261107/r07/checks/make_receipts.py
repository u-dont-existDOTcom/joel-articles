#!/usr/bin/env python3
"""Making-sense receipts (gate E365; each sentence's link per neuro-2026-11-06b) for r07's check texts (texts.py).
Writes CHECK-<name>.txt and RECEIPT-<name>.json and checks each; exits 1 if one fails."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[5] / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
from texts import TEXTS  # noqa: E402

N = 'none: the next question of the same list, in the same form'
NH = 'none: his sentence, unchanged, in the order the live post has it'
MONASTIC_HEAD = [
    ('forced celibacy doesn’t end sexuality', 'opens the point', None),
    ('where it usually goes: somewhere weird', 'what happens to it', 'it eventually sends it'),
    ('the point pressed as a question', 'the point pressed', 'Why wouldn’t it?'),
]
R = {
    'r07-s21': ('Vows', 'Someone about to make wedding vows, deciding what they can honestly promise.', 'It tells the '
                'reader the Bible has a warning like Joel’s.', [
        ('the Bible has a warning like his', 'opens the point', None),
        ('Ecclesiastes: better no vow than a broken one', 'the first verse', NH),
        ('the passage warns of God’s anger', 'what the verse says follows', NH),
        ('Matthew and James: let your yes be yes, anything more is from evil, which makes the extra promise suspicious',
         'the second verses and what they mean for vows', 'which makes the extra promise'),
    ]),
}
Q = {
    'Q1': 'PASS: each changed sentence gives its point first, in plain words',
    'Q2': 'N/A: these paragraphs tell and ask; the advice in them is unchanged',
    'Q3': 'PASS: the people, places, numbers and things are named as in the live post',
    'Q4': 'PASS: no new term',
    'Q5': 'PASS: each sentence’s tie is in its words (the links field), or the link says why it needs none',
    'Q6': 'PASS: nothing moved',
    'Q7': 'PASS: each change keeps what the paragraph tells the reader about their own case',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence; the small words carry the relations (but, so, since, because, otherwise)',
}
Q_MOVED = {}
CHECKED = {
    'r07-s21': [{'point': 'if your yes is trustworthy, why does it need another layer?', 'found': 'the verse in the same '
                 'sentence already says it: let your yes be yes, and anything beyond comes from evil', 'still_needed': 'no: '
                 'it says the verse again as a question, so it is a repeat (E378)', 'fate': 'cut'}],
}
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
    r['same_point'] = 'none: read the section from its heading to the next for this paragraph’s point; it is made once, here'
    r['questions'] = dict(Q)
    if name in Q_MOVED:
        r['questions']['Q6'] = Q_MOVED[name]
    r['checked'] = CHECKED.get(name, [{'point': 'the AI window’s point', 'found': 'the live post (../../live-check/AI-WINDOWS.json)',
                                       'still_needed': 'yes: the paragraph needs it', 'fate': 'changed'}])
    r['placement'] = 'The paragraph in its place in the live post, with the paragraph or paragraphs before it.'
    (HERE / ('CHECK-%s.txt' % name)).write_text(text, encoding='utf-8')
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
