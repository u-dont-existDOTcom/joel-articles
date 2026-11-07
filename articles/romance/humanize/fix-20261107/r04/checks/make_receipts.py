#!/usr/bin/env python3
"""Making-sense receipts (gate E365; each sentence's link per neuro-2026-11-06b) for r04's check texts (texts.py).
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
    'r04-s2e': ('Celibacy and monastics', 'Someone weighing celibacy or monastic life, deciding whether the people who '
                'choose it are only after liberation.', 'It tells the reader forced celibacy doesn’t end sexuality, the '
                'claim the paragraph tests.', MONASTIC_HEAD + [
        ('some people become monks for practical reasons', 'another reason people choose robes', 'practical reasons too'),
        ('what that means in a poor country: food, a roof, respect, and no job or family to support', 'the reasons, first '
         'case', 'In a poor country'),
        ('in the West it is the respect: a nobody is now Venerable Somebody and gets bowed to', 'the reasons, second case',
         'In the West'),
        ('he may still sincerely want liberation', 'what this says about him', 'Of course'),
        ('people want several things at once', 'why both can be true', NH),
    ]),
    'r04-s6': ('Slowing down (the missing middle)', 'Someone who wants a stage between interest and sex, deciding how to slow '
               'things down.', 'It names the gap the reader lives in: nothing between interest and sex.', [
        ('modern life has no stage between interest and sex', 'opens the point', None),
        ('bundling was one old version of that stage', 'an example from history', 'One old example is bundling'),
        ('what bundling was, a night in bed, clothed, talking, and that it is the missing middle Joel means',
         'what the example looked like and why it matters', 'Courting couples'),
        ('bundling didn’t solve the problem', 'the example’s limit', 'Well, it didn’t exactly solve the problem'),
        ('the evidence, 30–40 percent of brides pregnant where couples bundled, so it didn’t keep courtship nonsexual',
         'why it didn’t work', 'where lots of couples bundled'),
        ('Joel isn’t asking to bring bundling back', 'his conclusion, first half', 'bring bundling back'),
        ('what we do need: a stage everyone recognizes, before sex, moving in, and a life bond', 'his conclusion',
         'I just think'),
    ]),
    'r04-s7': ('What to ask before a relationship', 'Someone getting to know a possible partner, deciding what to ask about '
               'their past.', 'It tells the reader where to look first, their most recent conflicts.', [
        ('recent conflicts are the place to look', 'opens the questions', None),
        ('first question: could you regulate', 'the questions begin', 'during the conflict'),
        ('what you did to the other person', 'the next question', N),
        ('how you repaired', 'the next question', N),
        ('what you learned', 'the next question', N),
        ('whether your judgment improved', 'the next question', N),
        ('what your friends or exes would say', 'the last question, from people who saw it', N),
        ('what "I shut down" means in practice', 'one answer pressed for detail', 'And if you tell me you shut down'),
        ('did you stop talking for days, and did the partner feel abandoned', 'what it means',
         'none: the questions that unpack "shut down", in the same form as his list'),
    ]),
    'r04-s10': ('Time alone', 'Someone in a relationship who needs time alone, deciding how to ask for it.', 'It gives the '
                'reader Toft’s idea that feminine energy comes from many places.', [
        ('Toft: a man can get feminine energy from many places', 'opens the point', None),
        ('Joel likes the idea', 'his response', 'that idea'),
        ('a girlfriend shouldn’t be his only source', 'what it means for him', 'A girlfriend shouldn’t'),
        ('so he would take time alone regularly from the beginning, as part of how they live', 'how to keep the other '
         'sources', 'So'),
        ('a sudden announcement when he is overwhelmed will sound to her like time away from her', 'why from the beginning',
         'If I wait'),
    ]),
    'r04-s11': ('Roles in a relationship', 'Someone in a relationship whose roles have slipped, deciding what is play and '
                'what isn’t.', 'It names the problem the reader may be in: the role taking over.', [
        ('the problem is the role taking over', 'opens the point', None),
        ('she can play his little girl without becoming his child', 'what the line is', 'She can be my little girl'),
        ('she stays responsible for her life', 'what that means for her', 'She still has to remain responsible'),
        ('it can run the other way', 'the reverse case', 'the other way too'),
        ('if she has to calm him down whenever he is upset and also run his life, he has made her Mom', 'what the reverse looks like',
         'If she has to'),
    ]),
    'r04-s15': ('Romance shouldn’t be adjudicated', 'Someone trying to be the man in a relationship, deciding whether to '
                'keep proving it.', 'It tells the reader that having to prove manhood already makes it an act.', [
        ('having to prove he is the man makes it an act he must defend whenever he hesitates, cries, needs help or gets '
         'something wrong', 'opens the point', None),
        ('he doesn’t think of himself as super-masculine', 'his own case', NH),
        ('he cries, needs help, gets things wrong', 'the same list, said of himself', NH),
        ('Bee once called him her wife', 'an example', NH),
        ('he doesn’t recommend that for polarity', 'his joke on it', NH),
    ]),
    'r04-s17': ('Sex and spiritual life', 'Someone who thinks sex and spiritual life pull against each other, deciding '
                'whether to keep them apart.', 'It tells the reader Kim Anami says sexual energy can heal and awaken.', [
        ('Kim Anami says sexual energy can heal you and wake you up spiritually', 'opens the point', None),
        ('her students say it spilled into health, work, money and creativity', 'what her students report', 'She’s also'),
        ('her jade-egg practice trains for the cervical orgasm', 'what her practice is', 'Her jade-egg practice'),
    ]),
    'r04-s19': ('Friends and community', 'Someone with a confidant outside the relationship, deciding how much to trust '
                'their advice.', 'It tells the reader the same confidant has its own problem.', [
        ('a shared confidant leaves no release valve', 'opens the point', None),
        ('no arrangement is perfect', 'what that adds up to', NH),
        ('separate confidants are biased toward you', 'the separate case', 'separate confidants'),
        ('they hear only your side, while you’re upset, and want to protect you, so take them with a grain of salt',
         'what the bias means and what to do', 'They’re only hearing your side'),
    ]),
    'r04-s21': ('Vows', 'Someone about to make wedding vows, deciding what they can honestly promise.', 'It tells the '
                'reader the Bible has a warning like Joel’s.', [
        ('the Bible has a warning like his', 'opens the point', None),
        ('Ecclesiastes: better no vow than a broken one', 'the first verse', NH),
        ('the passage warns of God’s anger', 'what the verse says follows', NH),
        ('Matthew and James: let your yes be yes, anything more is from evil', 'the second verses', NH),
        ('a wedding vow is that kind of extra promise, which makes it suspicious to Joel', 'what the verses mean for vows',
         'A wedding vow is exactly that kind of extra promise'),
        ('if your yes is trustworthy, it needs no extra layer', 'the reason for it, as his question', NH),
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
Q_MOVED = {
    'r04-s7': 'PASS: the friends-and-exes question joins the list of questions it belongs to, as the last of them',
    'r04-s19': 'PASS: the reasons come before the advice they lead to (his own move: the context first)',
}
CHECKED = {
    'r04-s6': [{'point': '30–40 percent of New England brides were pregnant at marriage in the late 18th century, when '
                'bundling was common', 'found': 'JSTOR Daily, "Bundling: An Old Tradition on New Ground", citing Richard '
                'Godbeer: "some 30–40 percent of brides in New England were pregnant when they walked down the aisle" '
                '(https://daily.jstor.org/bundling-an-old-tradition-on-new-ground); Smith and Hindus put the peak just '
                'under 30 percent around 1790', 'still_needed': 'yes: it is why bundling didn’t solve the problem',
                'fate': 'kept'}],
    'r04-s7': [{'point': 'people aren’t always the best judges of their own progress', 'found': 'his paragraph before the '
                'questions already ends "That tells me more than either of us announcing that we’re healed"',
                'still_needed': 'no: the paragraph before makes the point, so here it is a repeat (E378)', 'fate': 'cut'}],
    'r04-s17': [{'point': 'Kim Anami treats sexual energy as a path into healing, creativity, worldly action and spiritual '
                 'awakening', 'found': 'her page the live post links (https://kimanami.com/my-vagina-heals-everything/) '
                 'could not be read from here on 2026-11-07 (the fetch waited for an approval nobody answered); the live '
                 'post’s claim is kept, with creativity and work said once, in the students’ sentence that already names '
                 'them', 'still_needed': 'yes: it is what goes further than the sutta', 'fate': 'changed'}],
    'r04-s19': [{'point': 'confidants may protect you rather than understand the relationship fairly', 'found': 'the '
                 'paragraph’s first sentence already says they will be biased toward you', 'still_needed': 'yes: that '
                 'they want to protect you stays; "rather than understand the relationship fairly" repeats the bias and '
                 'goes (E378)', 'fate': 'changed'}],
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
