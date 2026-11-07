#!/usr/bin/env python3
"""Making-sense receipts (gate E365; each sentence's link per neuro-2026-11-06b) for r05's check texts (texts.py).
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
    'r05-s2f': ('Celibacy and monastics', 'Someone weighing celibacy or monastic life, deciding whether the people who '
                'choose it are only after liberation.', 'It tells the reader forced celibacy doesn’t end sexuality, the '
                'claim the paragraph tests.', MONASTIC_HEAD + [
        ('some people become monks for practical reasons', 'another reason people choose robes', 'practical reasons too'),
        ('what that means in a poor country: food, a roof, respect, and no job or family to support', 'the reasons, first '
         'case', 'In a poor country'),
        ('even where food doesn’t matter, as in the West, a nobody gets to be Venerable Somebody and is bowed to',
         'the reasons where the first one falls away', 'And even where the food doesn’t matter'),
        ('he may still sincerely want liberation', 'what this says about him', 'Of course'),
        ('people want several things at once', 'why both can be true', NH),
    ]),
    'r05-s7': ('What to ask before a relationship', 'Someone getting to know a possible partner, deciding what to ask about '
               'their past.', 'It tells the reader where to look first, their most recent conflicts.', [
        ('recent conflicts are the place to look', 'opens the questions', None),
        ('first question: could you regulate', 'the questions begin', 'during the conflict'),
        ('what you did to the other person', 'the next question', N),
        ('how you repaired', 'the next question', N),
        ('what you learned', 'the next question', N),
        ('whether your judgment improved', 'the next question', N),
        ('what your friends or exes would say', 'the last question, from people who saw it', N),
        ('what "I shut down" means in practice', 'one answer pressed for detail', 'And if you tell me you shut down'),
        ('whether it was days of silence or one quiet evening', 'what it means, first',
         'none: the first question unpacking "shut down", in the same form as his list'),
        ('whether the partner felt abandoned', 'what it means, second', N),
    ]),
    'r05-s9': ('Living alone and living together', 'Someone used to living alone, deciding what a relationship will ask of '
               'them.', 'It tells the reader living alone is easy, which they likely know.', [
        ('living alone is easy', 'opens the point', None),
        ('he can make his bed whenever he wants', 'an example of the ease', 'I can make my bed'),
        ('with a girlfriend, making the bed becomes a sign of love', 'the same example in a relationship',
         'making the bed in the morning'),
        ('doing it badly can look like not caring', 'what that costs', 'If I don’t do it well'),
        ('so a bed, of all things, carries too much weight', 'what the example shows', 'So a bed, of all things'),
    ]),
    'r05-s10': ('Time alone', 'Someone in a relationship who needs time alone, deciding how to ask for it.', 'It gives the '
                'reader Toft’s idea that feminine energy comes from many places.', [
        ('Toft: a man can get feminine energy from many places', 'opens the point', None),
        ('Joel likes the idea', 'his response', 'that idea'),
        ('a girlfriend shouldn’t be his only source', 'what it means for him', 'A girlfriend shouldn’t'),
        ('announcing "I need time for myself!" when already overwhelmed sounds like time away from her', 'the problem '
         'first, the context for his answer', 'When I’m already overwhelmed'),
        ('so he would make alone time normal from early on', 'his answer to it', 'So'),
    ]),
    'r05-s17': ('Sex and spiritual life', 'Someone who thinks sex and spiritual life pull against each other, deciding '
                'whether to keep them apart.', 'It tells the reader Kim Anami goes further than the suttas, that sexual '
                'energy can heal and awaken.', [
        ('Kim Anami goes further than the suttas: sexual energy can heal you and wake you up', 'opens the point', None),
        ('her students say it changed their health, work, creativity, even money', 'what her students report', 'She’s also'),
        ('her jade-egg practice trains for the cervical orgasm', 'what her practice is', 'Her jade-egg practice'),
    ]),
    'r05-s21': ('Vows', 'Someone about to make wedding vows, deciding what they can honestly promise.', 'It tells the '
                'reader the Bible has a warning like Joel’s.', [
        ('the Bible has a warning like his', 'opens the point', None),
        ('Ecclesiastes: better no vow than a broken one', 'the first verse', NH),
        ('the passage warns of God’s anger', 'what the verse says follows', NH),
        ('Matthew and James: let your yes be yes, anything more is from evil', 'the second verses', NH),
        ('taken seriously, that makes the wedding vow itself the suspicious part', 'what the verses mean for vows',
         'Taken seriously, that'),
        ('if your yes is trustworthy, why swear on top of it', 'the reason for it, as his question', 'why swear on top of it'),
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
    'r05-s10': 'PASS: the problem comes before his answer to it (his own move: the context first)',
}
CHECKED = {
    'r05-s17': [{'point': 'Kim Anami treats sexual energy as a path into healing, creativity, worldly action and spiritual '
                 'awakening', 'found': 'her page the live post links (https://kimanami.com/my-vagina-heals-everything/) '
                 'could not be read from here on 2026-11-07 (the fetch waited for an approval nobody answered); the live '
                 'post’s claim is kept, with creativity and work said once, in the students’ sentence that already names '
                 'them', 'still_needed': 'yes: it is what goes further than the sutta', 'fate': 'changed'}],
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
