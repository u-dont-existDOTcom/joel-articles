#!/usr/bin/env python3
"""Making-sense receipts (gate E365) for r08's section check (texts.py). Every sentence has its row: the live post's
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
    'r08-s22': ('After leaving', 'Someone just out of a relationship, deciding what to tell people and how to see their ex.',
                'It tells the reader the aftermath is worse than the breakup, the stretch they may be in.', [
        ('the breakup is hard, the aftermath worse', 'opens the section', None),
        ('avoid public demonization, but don’t hide the truth to save face', 'the first advice', 'Public demonization'),
        ('sometimes the truth is abuse, coercion or serious deception', 'what the truth can be', 'Sometimes the truth'),
        ('how much you say, who you tell and how publicly depend on what happened and why you tell', 'how to tell it',
         'How much you say'),
        ('once out, you can see what you couldn’t while bonded', 'the turn to seeing the past', 'Once you’re out'),
        ('look at your part, and at what was true on your ex’s side, so you don’t flatten them', 'what to look at',
         'Look at what you contributed'),
        ('it can feel like they were fake all along, since that explains everything', 'the easy story about them',
         'It might feel like'),
        ('check whether that is really the simplest explanation before settling on it', 'what to do about it', 'But check'),
        ('ask people not invested in your innocence: a therapist, pastor or stranger may see more clearly', 'who can '
         'help check it', 'It helps to ask'),
        ('the curiosity itself can heal', 'what the checking gives you', 'Even the curiosity'),
        ('spiritual practice matters at an ending, but not to skip the feelings', 'the next help', 'Spiritual practice'),
        ('pray for your ex', 'the first practice', 'Pray for'),
        ('remember the good, and don’t let pain license hate', 'the next practice', 'Remember what was real'),
        ('avoid the New Age idea that everyone mirrors you', 'a belief to drop', 'Avoid the New Age belief'),
        ('it isn’t true', 'his verdict on it', 'No, that isn’t true'),
        ('we partly mirror each other, but each was formed by much else', 'what is true instead', 'We partly mirror'),
        ('Devadatta kept trying to kill the Buddha', 'an example', 'the Buddha'),
        ('your part doesn’t erase theirs', 'what the example shows', 'your part'),
        ('ask what Mr. Rogers would do', 'a way to practice it', 'Sometimes it helps to ask'),
        ('public demonization needn’t be the last chapter', 'his own lesson', 'I also learned'),
        ('cutting contact forever may block an apology', 'why it needn’t be', 'If you avoid contact forever'),
        ('distance for a while can help', 'the middle way', 'But it can help'),
        ('after an apology, remember you deserve stable love', 'a caution', 'It can be tempting'),
        ('you’re not a yo-yo', 'his punch line', 'You’re not a yo-yo'),
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
CHECKED = {
    'r08-s22': [{'point': 'the most parsimonious explanation', 'found': '"parsimonious" means the simplest explanation that '
                 'fits the evidence (the plain word a high-school graduate knows, gate E369)', 'still_needed': 'yes: it is '
                 'the test he gives for accepting the easy story', 'fate': 'changed'}],
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
