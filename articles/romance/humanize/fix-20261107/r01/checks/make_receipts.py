#!/usr/bin/env python3
"""Making-sense receipts (gate E365; each sentence's link per neuro-2026-11-06b) for r01's five check texts (texts.py).
Writes CHECK-<name>.txt and RECEIPT-<name>.json and checks each; exits 1 if one fails."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[5] / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
from texts import TEXTS  # noqa: E402

# per text: (section, reader, why the first sentence is worth reading, [(payoff, follows, link)] per sentence)
R = {
    'r01-s1': ('Casual sex (Sex is never just sex)', 'Someone thinking about casual sex, deciding what they owe if it goes further than '
               'they planned.', 'It is the line people actually say before casual sex, so the reader recognizes it as theirs.', [
        ('the reader hears the honest casual-sex line', 'opens the example', None),
        ('the speaker admits they are not pretending', 'the line goes on', 'I’m not pretending'),
        ('the speaker says what they still want', 'the line ends', 'still'),
        ('the reader learns the line is honest about tonight', 'what the line covers', 'That’s honest'),
        ('the reader learns what the line leaves out: tonight can make a baby', 'what the line doesn’t cover', 'But tonight'),
        ('the reader sees the phone call that comes with a pregnancy', 'the baby made concrete', 'If this girl gets pregnant'),
        ('the reader is asked what they would do', 'after the call', 'Then what?'),
        ('the first option: blocking her', 'one answer to "then what"', 'none: an option answering the question before'),
        ('the second option: child support', 'the next answer', 'none: the next option, in the same form'),
        ('the third option: pushing an abortion she sees as killing her child', 'the next answer', 'none: the next option, in the same form'),
        ('the same choices can fall on the man', 'the options turned around', 'vice versa'),
        ('the reader hears Joel’s own case: an abortion he learned of a year later', 'a real case of the options',
         'My first girlfriend'),
        ('the reader is told this is what sex can do', 'what the case shows', 'This is what'),
        ('the reader knows no contraception removes the risk', 'why it applies to everyone', 'No contraception'),
    ]),
    'r01-s2': ('Celibacy and monastics', 'Someone weighing celibacy or monastic life, deciding whether it would really free them.',
               'It tells the reader forced celibacy doesn’t end sexuality, the claim the paragraph tests.', [
        ('the reader learns forced celibacy doesn’t end sexuality', 'opens the point', None),
        ('the reader learns where it usually goes: somewhere weird', 'what happens to it', 'it eventually sends it'),
        ('the reader is asked why it wouldn’t', 'the point pressed', 'Why wouldn’t it?'),
        ('the reader learns people also become monks for practical reasons', 'another reason people choose robes',
         'for practical reasons too'),
        ('the reader learns what the robes bring in a poor country', 'the practical reasons, first case', 'the robes come with'),
        ('the reader learns what they bring in the West: respect and people bowing', 'the practical reasons, second case',
         'Even in the West'),
        ('the reader learns the practical and the sincere can go together', 'what this says about the monk',
         'Of course, he can sincerely want liberation and still enjoy the bowing'),
    ]),
    'r01-s3': ('Being wanted for what you provide', 'Someone wondering whether they are loved for themselves or for what they '
               'bring.', 'It grants the reader that wanting support is reasonable, then says it muddies the waters, the tension '
               'they would recognize.', [
        ('the reader learns wanting support is reasonable and still muddies things for Joel', 'opens the point', None),
        ('the reader learns love and practical wants can come together, and that men are no different',
         'what muddies the waters', 'I understand that she might really love me while still wanting'),
        ('the reader sees the same mix from the man’s side', 'the man’s version of it',
         'A man can really love a woman for who she is while also'),
    ]),
    'r01-s4': ('Being wanted for what you provide', 'Someone wondering whether they are loved for themselves or for what they '
               'bring.', 'It tells the reader the question goes deeper than the practical one they just read about.', [
        ('the reader learns the question is more than practical', 'opens the point', None),
        ('the reader learns it is philosophical', 'what kind of question', 'It’s philosophical'),
        ('the reader hears the provider’s insecurity in his own words', 'what the question is',
         'insecurity inside the provider role'),
        ('the reader learns Joel doesn’t need provision to be irrelevant', 'his answer to the question', 'the answer'),
        ('the reader learns what she may like about him', 'what provision adds to attraction', 'Maybe she likes'),
        ('the reader learns what he likes about her', 'the same from his side', 'I definitely like'),
        ('the reader learns what he wants: the bond to outgrow the first attraction', 'what matters beyond it',
         'I just want what we have to grow bigger'),
        ('the reader hears Bee’s line on why: going up or down', 'why it has to grow', 'Because'),
    ]),
    'r01-s5': ('Loved when you stop being useful', 'Someone wondering whether a partner would stay when they stop being useful.',
               'It promises a smaller test of the same question, which is the reader’s question too.', [
        ('the reader learns a smaller test came later', 'opens the story', None),
        ('the reader learns what happened: shoes that didn’t fit', 'the test begins', 'Bee gave me some shoes'),
        ('the reader learns the result: a month with a bad knee', 'what the shoes did', 'I wore them'),
        ('the reader learns how Bee cared for him: reluctantly', 'her response', 'She did nurse me'),
        ('the reader learns she kept doubting the injury', 'more of her response', 'She also kept suggesting'),
        ('the reader learns Joel understood the doubt', 'his reading of it', 'I get why'),
        ('the reader learns how it still felt, and what she may have wished', 'what the test showed him',
         'It still felt dismissive, though'),
    ]),
}
Q = {
    'Q1': 'PASS: each changed sentence gives its point first, in plain words',
    'Q2': 'N/A: these paragraphs tell and ask; the only advice is in the unchanged words',
    'Q3': 'PASS: the people, places and things are named as in the live post',
    'Q4': 'PASS: no new term; Venerable Somebody is his phrase, explained by the bowing',
    'Q5': 'PASS: each sentence’s tie is in its words (the links field), or the link says why it needs none',
    'Q6': 'PASS: nothing moved',
    'Q7': 'PASS: each change keeps what the paragraph tells the reader about their own case',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence; the small words carry the relations (but, even, of course, since, though)',
}
CHECKED = {
    'r01-s1': [{'point': 'the line is honest about tonight but tonight can make a baby', 'found': 'the live post: "That may be '
                'candid about what you expect now. It doesn’t settle what either of you will owe ... Sex can make a child." '
                '(AI High on the middle sentence)', 'still_needed': 'yes: it is the turn to the pregnancy questions',
                'fate': 'changed'}],
    'r01-s2': [{'point': 'practical reasons to become a monastic', 'found': 'the live post, the same facts (AI High and Low)',
                'still_needed': 'yes: it is the second reason after sexuality', 'fate': 'changed'}],
    'r01-s3': [{'point': '"Affection and practical motives often coexist, even if it isn’t the romantic ideal."',
                'found': 'the paragraph says it twice already, for her and for him (AI High on the summary)',
                'still_needed': 'no: a repeat of the paragraph’s own point', 'fate': 'cut'}],
    'r01-s4': [{'point': 'provision may be part of attraction; he wants the bond to outgrow it', 'found': 'the live post (AI Low '
                'on both sentences)', 'still_needed': 'yes: it answers the provider question', 'fate': 'changed'}],
    'r01-s5': [{'point': 'he understood her doubt, and it still felt dismissive', 'found': 'the live post (AI Medium)',
                'still_needed': 'yes: it is how the test ended for him', 'fate': 'changed'}],
}
bad = 0
for name, text in TEXTS.items():
    section, reader, why, rows = R[name]
    r = S.make(text, section, reader)
    sents = r['sentences']
    assert len(sents) == len(rows), (name, len(sents), len(rows))
    for s, (pay, fol, link) in zip(sents, rows):
        s['payoff'], s['follows'] = pay, fol
        if 'link' in s:
            assert link, (name, s['s'][:60])
            s['link'] = link
    r['opens']['why_reading'] = why
    r['same_point'] = ('none: read the section from its heading to the next for this paragraph’s point; it is made once, '
                       'here')
    r['questions'] = dict(Q)
    r['checked'] = CHECKED[name]
    r['placement'] = 'The paragraph in its place in the live post, with the line or paragraph before it.'
    (HERE / ('CHECK-%s.txt' % name)).write_text(text, encoding='utf-8')
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, len(text.split()), 'words', 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
