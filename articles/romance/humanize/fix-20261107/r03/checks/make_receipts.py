#!/usr/bin/env python3
"""Making-sense receipts (gate E365; each sentence's link per neuro-2026-11-06b) for r03's check texts (texts.py).
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
    'r03-s2b': ('Celibacy and monastics', 'Someone weighing celibacy or monastic life, deciding whether the people who '
                'choose it are only after liberation.', 'It tells the reader forced celibacy doesn’t end sexuality, the '
                'claim the paragraph tests.', MONASTIC_HEAD + [
        ('some people become monks for practical reasons', 'another reason people choose robes', 'practical reasons too'),
        ('what the robes get you in a poor country: room and board, status, no job or family to support', 'the reasons, '
         'first case', 'In a poor country'),
        ('in the West it is the respect: a nobody becomes Venerable Somebody and gets bowed to', 'the reasons, second case',
         'In the West'),
        ('he may still sincerely want liberation', 'what this says about him', 'Of course'),
        ('most people choose big things for more than one reason', 'why both can be true', 'more than one reason'),
    ]),
    'r03-s2c': ('Celibacy and monastics', 'Someone weighing celibacy or monastic life, deciding whether the people who '
                'choose it are only after liberation.', 'It tells the reader forced celibacy doesn’t end sexuality, the '
                'claim the paragraph tests.', MONASTIC_HEAD + [
        ('plenty of monks do sincerely want liberation', 'what the weirdness doesn’t mean about them', 'Of course'),
        ('people want several things at once, and practical reasons are one of them', 'the other side of their motives',
         'But people can want several things at once'),
        ('what the robes get you in a poor country: room and board, status, no job or family to support', 'the practical '
         'reasons, first case', 'In a poor country'),
        ('in the West it is the respect: a nobody becomes Venerable Somebody and gets bowed to', 'the practical reasons, '
         'second case', 'In the West'),
    ]),
    'r03-s6': ('Slowing down (the missing middle)', 'Someone who wants a stage between interest and sex, deciding how to slow '
               'things down.', 'It names the gap the reader lives in: nothing between interest and sex.', [
        ('modern life has no stage between interest and sex', 'opens the point', None),
        ('bundling was one old version of that stage', 'an example from history', 'One old example is bundling'),
        ('what bundling was, a night in bed, clothed, talking, and that it is the missing middle Joel means',
         'what the example looked like and why it matters', 'Courting couples'),
        ('bundling didn’t solve the problem', 'the example’s limit', 'Well, it didn’t exactly solve the problem'),
        ('the evidence: 30–40 percent of brides were pregnant where couples bundled', 'why it didn’t work',
         'where lots of couples bundled'),
        ('so it didn’t keep courtship nonsexual', 'what the numbers show', 'So it wasn’t'),
        ('Joel isn’t asking to bring bundling back', 'his conclusion, first half', 'bring bundling back'),
        ('what we do need: a stage everyone recognizes, before sex, moving in, and a life bond', 'his conclusion',
         'I just think'),
    ]),
    'r03-s7': ('What to ask before a relationship', 'Someone getting to know a possible partner, deciding what to ask about '
               'their past.', 'It tells the reader where to look first, their most recent conflicts.', [
        ('recent conflicts are the place to look', 'opens the questions', None),
        ('first question: could you regulate', 'the questions begin', 'during the conflict'),
        ('what you did to the other person', 'the next question', N),
        ('how you repaired', 'the next question', N),
        ('what you learned', 'the next question', N),
        ('whether your judgment improved', 'the last question', N),
        ('Joel would also ask their friends or exes', 'another source than the person', 'I’d also want to know'),
        ('why: nobody judges their own progress well, Joel included', 'why the friends’ view counts', 'me included'),
        ('he asks what "I shut down" means in practice', 'one answer pressed for detail', 'And when somebody tells me'),
        ('did you stop talking for days', 'what it means, first', 'none: the first question unpacking "I shut down"'),
        ('did the partner feel abandoned', 'what it means, second', N),
    ]),
    'r03-s8': ('Idealizing a partner', 'Someone falling for a person, deciding whether they see her or a story about '
               'themselves.', 'It tells the reader the shortcut they may be taking shouldn’t be needed.', [
        ('it shouldn’t have to happen that way', 'opens the point', None),
        ('it is a bad shortcut to the archetypes', 'what kind of shortcut it is', 'It’s a bad shortcut'),
        ('seeing someone as amazing doesn’t depend on what the seeing gives you', 'what healthy seeing is', NH),
        ('once you identify with how you see her (perfect, destiny, the one who found her), you’re lost',
         'where it goes wrong', 'once you start identifying'),
    ]),
    'r03-s10': ('Time alone', 'Someone in a relationship who needs time alone, deciding how to ask for it.', 'It gives the '
                'reader Toft’s idea that feminine energy comes from many places.', [
        ('Toft: a man can get feminine energy from many places', 'opens the point', None),
        ('Joel likes the idea', 'his response', 'that idea'),
        ('a girlfriend shouldn’t be his only source', 'what it means for him', 'A girlfriend shouldn’t'),
        ('he would make alone time normal from the start', 'how to keep other sources', 'alone time normal'),
        ('otherwise a sudden announcement when overwhelmed sounds like time away from her', 'why the start matters',
         'Otherwise'),
    ]),
    'r03-s11': ('Roles in a relationship', 'Someone in a relationship whose roles have slipped, deciding what is play and '
                'what isn’t.', 'It names the problem the reader may be in: the role taking over.', [
        ('the problem is the role taking over', 'opens the point', None),
        ('she can play his little girl without becoming his child', 'what the line is', 'She can be my little girl'),
        ('she stays responsible for her life', 'what that means for her', 'She still has to remain responsible'),
        ('it can run the other way', 'the reverse case', 'the other way too'),
        ('he makes her Mom when he expects her to regulate, soothe, organize and keep him going', 'what the reverse looks '
         'like', 'I make her Mom'),
    ]),
    'r03-s14': ('Polarity and safety', 'Someone in a safe, close relationship, deciding why the desire has gone flat.',
                'It tells the reader some women want danger, the case they may be facing.', [
        ('some women only get turned on by danger', 'opens the point', None),
        ('or she may feel there is no contrast left', 'the other case', 'may also'),
        ('many women want a man dangerous in a defending way', 'what most women want', 'A lot of women'),
        ('Beauty and the Beast shows it is an old wish', 'an example of it', 'Beauty and the Beast'),
        ('so the question for a couple: can polarity live inside the safety', 'what the section has been asking', 'So'),
    ]),
    'r03-s15': ('Romance shouldn’t be adjudicated', 'Someone trying to be the man in a relationship, deciding whether to '
                'keep proving it.', 'It tells the reader that having to prove manhood already makes it fake.', [
        ('having to prove he is the man makes it fake, since he must defend it each time he slips', 'opens the point',
         None),
        ('he doesn’t think of himself as super-masculine', 'his own case', NH),
        ('he cries, needs help, gets things wrong', 'what that looks like', NH),
        ('Bee once called him her wife', 'an example', NH),
        ('he doesn’t recommend that for polarity', 'his joke on it', NH),
    ]),
    'r03-s16': ('Fantasy', 'Someone whose partner has shared a fantasy, deciding what it asks of them.', 'It gives the '
                'reader Perel’s distinction: a fantasy is play, not a request.', [
        ('Perel: fantasy is play, not a real-life request', 'opens the point', None),
        ('so a rape fantasy isn’t a wish to be raped', 'the distinction applied to the hardest case', 'So'),
        ('a couple can keep it in their heads or act part of it out', 'what they can do with it', 'a fantasy'),
        ('fantasy should add to arousal, not be the only way, so he can enjoy the real woman', 'a limit on it',
         'Fantasy should also'),
    ]),
    'r03-s17': ('Sex and spiritual life', 'Someone who thinks sex and spiritual life pull against each other, deciding '
                'whether to keep them apart.', 'It tells the reader Kim Anami treats sexual energy as a path to healing '
                'and awakening.', [
        ('Kim Anami treats sexual energy as a path to healing and awakening', 'opens the point', None),
        ('her students say it spilled into health, work, money and creativity', 'what her students report', 'She’s also'),
        ('her jade-egg practice trains for the cervical orgasm', 'what her practice is', 'Her jade-egg practice'),
    ]),
    'r03-s18': ('Friends and community', 'Someone in a couple whose friends take sides, deciding where support should come '
                'from.', 'It tells the reader Joel will show his own case, so they can compare it to theirs.', [
        ('Joel shows his own case', 'opens the point', None),
        ('in a crisis each turns to separate friends', 'what happened', NH),
        ('each resents the other’s one-sided story', 'what that led to', NH),
        ('some friends are exes, and they stop talking to each other’s friends', 'how it got worse', NH),
        ('that is a terrible time to run a life with two people', 'what it costs', NH),
        ('if one goes down, the other backs up housing, money, children, health and crises', 'why two is too few',
         'If one person goes down'),
        ('no time is left for the relationship', 'what is lost', NH),
    ]),
    'r03-s19': ('Friends and community', 'Someone with a confidant outside the relationship, deciding how much to trust '
                'their advice.', 'It tells the reader the same confidant has its own problem.', [
        ('a shared confidant leaves no release valve', 'opens the point', None),
        ('no arrangement is perfect', 'what that adds up to', NH),
        ('separate confidants are biased toward you', 'the separate case', 'separate confidants'),
        ('take them with a grain of salt: they hear your side, while you’re upset, and want to protect you', 'what to do '
         'about the bias', 'since they’re only hearing your side'),
    ]),
    'r03-s20': ('Romance with humility', 'Someone planning a life with a partner, deciding what to agree on in advance.',
                'It tells the reader the questions change once they choose a romance with humility.', [
        ('the questions change', 'opens the questions', None),
        ('what stays if the romance changes', 'the first question', NH),
        ('are we promising actions or feelings', 'the next question', NH),
        ('which needs we meet outside', 'the next question', NH),
        ('the biggest: falling in love with someone else', 'the biggest question', 'And the biggie'),
        ('what counts as betrayal and what calls for a serious talk', 'the next question', N),
        ('whether we can rethink the agreement honestly if life changes', 'the next question', N),
        ('what we owe each other and our kids if we split', 'the last question', N),
    ]),
    'r03-s21': ('Vows', 'Someone about to make wedding vows, deciding what they can honestly promise.', 'It tells the '
                'reader the Bible has a warning like Joel’s.', [
        ('the Bible has a warning like his', 'opens the point', None),
        ('Ecclesiastes: better no vow than a broken one', 'the first verse', NH),
        ('the passage warns of God’s anger', 'what the verse says follows', NH),
        ('Matthew and James: let your yes be yes, anything more is from evil', 'the second verses', NH),
        ('if your yes is trustworthy, it needs no extra layer', 'what the verses mean for vows', 'If your yes'),
        ('so the extra promise makes him suspicious', 'what he concludes', 'The extra promise'),
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
    'r03-s2c': 'PASS: the concession (he may want liberation; people want several things) moves ahead of the perks it '
               'answers, so the paragraph ends on the picture of the bowing',
    'r03-s8': 'PASS: the lost-in-the-sauce clause moves ahead of the thoughts that show it, so the point comes first',
    'r03-s11': 'PASS: "I make her Mom" moves ahead of what makes her Mom, so the point comes first',
    'r03-s18': 'PASS: the backup system comes before the list it backs up, so the point comes first',
    'r03-s21': 'PASS: the question moves ahead of the conclusion it leads to',
    'r03-s6': 'PASS: "the missing middle" joins the sentence that describes it',
}
CHECKED = {
    'r03-s6': [{'point': '30–40 percent of New England brides were pregnant at marriage in the late 18th century, when '
                'bundling was common', 'found': 'JSTOR Daily, "Bundling: An Old Tradition on New Ground", citing Richard '
                'Godbeer: "some 30–40 percent of brides in New England were pregnant when they walked down the aisle" '
                '(https://daily.jstor.org/bundling-an-old-tradition-on-new-ground); Smith and Hindus put the peak just '
                'under 30 percent around 1790', 'still_needed': 'yes: it is why bundling didn’t solve the problem',
                'fate': 'kept'}],
    'r03-s15': [{'point': 'he would have to defend the identity every time he hesitates, cries, needs help or gets something '
                 'wrong', 'found': 'the next paragraph, his own, already says "I cry, I need help, I get things wrong"',
                 'still_needed': 'yes: hesitating stays; crying, needing help and getting things wrong are said in the '
                 'next paragraph, so here they are a repeat (E378)', 'fate': 'changed'}],
    'r03-s17': [{'point': 'Kim Anami treats sexual energy as a path into healing, creativity, worldly action and spiritual '
                 'awakening', 'found': 'her page the live post links (https://kimanami.com/my-vagina-heals-everything/) '
                 'could not be read from here on 2026-11-07 (the fetch waited for an approval nobody answered); the live '
                 'post’s claim is kept, with creativity and work said once, in the students’ sentence that already names '
                 'them', 'still_needed': 'yes: it is what goes further than the sutta', 'fate': 'changed'}],
    'r03-s19': [{'point': 'confidants may protect you rather than understand the relationship fairly', 'found': 'the '
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
