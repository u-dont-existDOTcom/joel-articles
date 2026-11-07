#!/usr/bin/env python3
"""Making-sense receipts (gate E365; each sentence's link per neuro-2026-11-06b) for r02's check texts (texts.py).
Writes CHECK-<name>.txt and RECEIPT-<name>.json and checks each; exits 1 if one fails."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[5] / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
from texts import TEXTS  # noqa: E402

N = 'none: the next question of the same list, in the same form'
R = {
    'r02-s2': ('Celibacy and monastics', 'Someone weighing celibacy or monastic life, deciding whether it would really free '
               'them.', 'It tells the reader forced celibacy doesn’t end sexuality, the claim the paragraph tests.', [
        ('forced celibacy doesn’t end sexuality', 'opens the point', None),
        ('where it usually goes: somewhere weird', 'what happens to it', 'it eventually sends it'),
        ('the point pressed as a question', 'the point pressed', 'Why wouldn’t it?'),
        ('the robes also bring perks', 'another reason people choose robes', 'The robes come with perks too'),
        ('what a monk gets in a poor country', 'the perks, first case', 'A monk in a poor country gets'),
        ('in the West the perk is status', 'the perks, second case', 'In the West'),
        ('what that status looks like: people bowing to a nobody', 'the status made concrete', 'Venerable Somebody'),
        ('he may still want liberation', 'what this says about him', 'He can still'),
        ('and enjoy the bowing at the same time', 'the other half of him', 'He can also enjoy the bowing'),
    ]),
    'r02-s6': ('Slowing down (the missing middle)', 'Someone who wants a stage between interest and sex, deciding how to slow '
               'things down.', 'It names the gap the reader lives in: nothing between interest and sex.', [
        ('modern life has no stage between interest and sex', 'opens the point', None),
        ('bundling was one old version of that stage', 'an example from history', 'One old example is bundling'),
        ('what bundling was: a night in bed, clothed, talking', 'what the example looked like', 'Courting couples'),
        ('that is the missing middle Joel means', 'why the example matters', 'the missing middle I mean'),
        ('bundling didn’t solve the problem', 'the example’s limit', 'It didn’t exactly solve the problem, though'),
        ('the evidence: 30–40 percent of brides were pregnant when bundling was common', 'why it didn’t work',
         'bundling was common then'),
        ('so it didn’t keep courtship nonsexual', 'what the numbers show', 'So much for'),
        ('Joel isn’t asking to bring bundling back', 'his conclusion, first half', 'bring bundling back'),
        ('what we do need: a recognized way to go slow before sex, moving in, and a life bond', 'his conclusion',
         'But we need'),
    ]),
    'r02-s7': ('What to ask before a relationship', 'Someone getting to know a possible partner, deciding what to ask about '
               'their past.', 'It tells the reader where to look first, their most recent conflicts.', [
        ('recent conflicts are the place to look', 'opens the questions', None),
        ('first question: could you regulate', 'the questions begin', 'during the conflict'),
        ('what you did to the other person', 'the next question', N),
        ('how you repaired', 'the next question', N),
        ('what you learned', 'the next question', N),
        ('whether your judgment improved', 'the last question', N),
        ('Joel would also ask their friends or exes, since people misjudge their own progress', 'another source than the '
         'person', 'I’d also want to know'),
        ('what "I shut down" looks like in practice', 'one answer pressed for detail', 'And if somebody tells me'),
        ('did you go silent for days', 'what it looks like, first', 'none: the first question unpacking "I shut down"'),
        ('did the partner feel abandoned', 'what it looks like, second', N),
    ]),
    'r02-s8': ('Idealizing a partner', 'Someone falling for a person, deciding whether they see her or a story about '
               'themselves.', 'It tells the reader the shortcut they may be taking shouldn’t be needed.', [
        ('it shouldn’t have to happen that way', 'opens the point', None),
        ('it is a bad shortcut to the archetypes', 'what kind of shortcut it is', 'It’s a bad shortcut'),
        ('seeing someone as amazing is fine if it isn’t about what it does for him', 'what healthy seeing is',
         'Seeing someone as amazing is fine'),
        ('once it becomes a story about him, he’s lost', 'where it goes wrong', 'The minute it turns into a story about me'),
    ]),
    'r02-s9': ('Living alone and living together', 'Someone used to living alone, deciding what a relationship will ask of '
               'them.', 'It tells the reader living alone is easy, which they likely know.', [
        ('living alone is easy', 'opens the point', None),
        ('he can make his bed whenever he wants', 'an example of the ease', 'I can make my bed'),
        ('with a girlfriend, making the bed becomes a sign of love', 'the same example in a relationship',
         'making the bed in the morning'),
        ('doing it badly can look like not caring', 'what that costs', 'If I don’t do it well'),
        ('so a bed carries too much weight', 'what the example shows', 'So a bed'),
    ]),
    'r02-s10': ('Time alone', 'Someone in a relationship who needs time alone, deciding how to ask for it.', 'It gives the '
                'reader Toft’s idea that feminine energy comes from many places.', [
        ('Toft: a man can get feminine energy from many places', 'opens the point', None),
        ('Joel likes the idea', 'his response', 'that idea'),
        ('a girlfriend shouldn’t be his only source', 'what it means for him', 'A girlfriend shouldn’t'),
        ('he wants alone time to be normal from the start, not a sudden announcement', 'how to keep other sources',
         'I want alone time to be normal between us'),
        ('a late announcement sounds like he needs time away from her', 'why a sudden announcement goes wrong', 'By then'),
    ]),
    'r02-s11': ('Roles in a relationship', 'Someone in a relationship whose roles have slipped, deciding what is play and '
                'what isn’t.', 'It names the problem the reader may be in: the role taking over.', [
        ('the problem is the role taking over', 'opens the point', None),
        ('she can play his little girl without becoming his child', 'what the line is', 'She can be my little girl'),
        ('she stays responsible for her life', 'what that means for her', 'She still has to remain responsible'),
        ('it can run the other way', 'the reverse case', 'the other way too'),
        ('if she calms, patches and runs his life, she has become his mom', 'what the reverse looks like',
         'I’ve turned her into my mom'),
    ]),
    'r02-s12': ('Roles in a relationship', 'Someone in a relationship who keeps fixing their partner, deciding whose '
                'responsibility is whose.', 'It admits Joel’s own failing, which the reader may share.', [
        ('Joel can become condescending', 'opens the point', None),
        ('he finds it intolerable', 'how he feels about it', 'I find that intolerable'),
        ('"I feel like your patient" means both should look at what they’re doing', 'what to do when it happens',
         'If someone tells me'),
        ('he knows his side', 'his part in it', 'on my side'),
        ('helping and being needed feel good', 'what his side is', 'Helping feels good'),
        ('he often had the answer, so they kept asking', 'why it kept happening', 'so of course they kept asking me'),
        ('he had to check whether they were caring for themselves', 'what he had to look at', 'without me'),
    ]),
    'r02-s13': ('Roles in a relationship', 'Someone in a relationship of teacher and student, deciding whether it is still '
                'healthy.', 'It tells the reader what Joel could teach, the side they may recognize.', [
        ('what Joel could teach these women', 'opens the point', None),
        ('what they could teach him', 'the other side', 'They could pull me into life more'),
        ('taking turns is healthy', 'what that adds up to', 'we take turns'),
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
    'Q9': 'PASS: one step per sentence; the small words carry the relations (but, so, since, though, as long as)',
}
CHECKED = {'r02-s6': [{'point': '30–40 percent of New England brides were pregnant at marriage in the late 18th century, when '
                       'bundling was common', 'found': 'JSTOR Daily, "Bundling: An Old Tradition on New Ground", citing '
                       'Richard Godbeer: "some 30–40 percent of brides in New England were pregnant when they walked down the '
                       'aisle" (https://daily.jstor.org/bundling-an-old-tradition-on-new-ground); Smith and Hindus put the '
                       'peak just under 30 percent around 1790', 'still_needed': 'yes: it is why bundling didn’t solve the '
                       'problem', 'fate': 'kept'}]}
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
    r['checked'] = CHECKED.get(name, [{'point': 'the AI window’s point', 'found': 'the live post (../../live-check/AI-WINDOWS.json)',
                                       'still_needed': 'yes: the paragraph needs it', 'fate': 'changed'}])
    r['placement'] = 'The paragraph in its place in the live post, with the paragraph before it.'
    (HERE / ('CHECK-%s.txt' % name)).write_text(text, encoding='utf-8')
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
