"""My check of each repeat the readers found, and the two federation trims for Joel's W08 (2026-10-23).

Run after every `clarity_read.py collect` of this folder (collect rebuilds ITEMS.json from the READER files): it sets my
pick and the reason I checked against the whole article (WORKING.html's text, ARTICLE.txt), drops duplicates and cuts that
another question already asks about, narrows one cut, and adds the W08 trims, which no reader proposed.

  python3 articles/intentional-communities/candidate/joel-20261023/repeats/picks.py   (from the repo root)
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / 'tools' / 'humanization'))
import clarity_read as C  # noqa: E402

A, B, DROP = 'A', 'B', 'drop'
PICKS = {
    '1.1': (B, 'Your story\'s set-up for what "Why Communities Keep Dying" explains: the next paragraph\'s "Which meant weekly '
               'meetings ..." hangs on it.'),
    '1.2': (B, 'The essay\'s thesis up front, for readers who stop early (your 61 b); the section after it says it in full.'),
    '1.3': (A, 'The two Instagram stories just showed it; "chaotic, but sincere" is all it adds.'),
    '1.4': (DROP, 'the smaller cut of only its second sentence is offered instead, which keeps your "A week of feeling '
                  'transformed isn\'t what it\'s for."'),
    '1.5': (B, 'The manual\'s own definition, for readers who go straight to it (your 61 b).'),
    '1.6': (B, 'Here the model is laid out, with what the essay\'s line doesn\'t say: not a professional, a guru or the founder '
               'everyone depends on.'),
    '1.7': (A, 'The sentence before says it; "That answers the reasonable objection ..." still follows.'),
    '1.8': (A, 'Your two examples just made the point, and the essay\'s opening says it (that set-up stays).'),
    '5.1': (B, 'Part of the list of what makes them the closest whole example; teaching outsiders and working beyond one '
               'village are two of its reasons, told in full later.'),
    '5.2': (A, 'The essay\'s opening defines "escuelita".'),
    '5.3': (A, 'The clause before it, "how many daughter communities there are", gives the purpose, and the paragraph ends on '
               '"A week of feeling transformed isn\'t what it\'s for."'),
    '5.4': (B, 'Your 57 a, just put in: readers who go straight to the manual meet medicine here as one of four parts that '
               '"have to pl/ork together", before the essay\'s line.'),
    '5.5': (A, 'The essay credits the book with all three; the entry still says what the book is about.'),
    '6.1': (DROP, 'the pointer your 61 b asked for ("we should definitely include a pointer tho to the sections we are moving '
                  'down")'),
    '6.2': (A, 'The section\'s opening says the warmth has hard limits, and your next two sentences carry the lesson.'),
    '6.3': (DROP, 'the same cut as another reader\'s, listed once'),
    '6.4': (B, 'It\'s what the container part says about why the container gets skipped, with its four examples; the '
               'manual\'s opening line is about founders\' interests in general.'),
    '6.5': (DROP, 'your own sentence (your answer to 39, 2026-10-17)'),
    '6.6': (B, 'Your joke, told once; "experience collectors" earlier is the same idea, but here it\'s part of the case '
               'against psychedelics.'),
    '7.1': (B, 'It applies the point to communities built on peak experiences, which is this section\'s case.'),
    '7.2': (B, 'It adds that the cost grows the deeper someone goes.'),
    '7.3': (DROP, 'the same cut as another reader\'s, listed once'),
    '8.1': (A, 'It sums up the section\'s paragraphs; "Even so, there will still be disagreements about this." still follows '
               'the jealousy paragraph.'),
    '8.2': (DROP, 'question 64 asks about the same words (your reason the village isn\'t for everyone)'),
    '8.3': (B, 'It says what the kibbutz finding means (group care is fine, replacing the bond with parents isn\'t); your '
               '"bias" later is your own preference, a different point.'),
    '8.4': (A, 'The bullet says it in full ("Hear the child even when the accused is someone people love ..."); the closing '
               'line restates it.'),
    '8.5': (DROP, 'question 64 cuts its "grain of salt"; "Is it settled anthropology? No, it\'s provocative observation." '
                  'stays as the list\'s own caution, for readers who use the list without the essay'),
    '9.1': (B, 'The set-up the money section pays off; the payoff\'s summing-up line is the cut instead (listed below).'),
    '9.2': (B, 'The essay\'s membership steps end on what full membership gives, for readers who don\'t go on to the manual.'),
    '9.3': (B, 'It sets up your commune-name joke and the Trungpa line, and readers who stop at the essay never reach the '
               'founderism section.'),
    '9.4': (DROP, 'your 49 answer put "If it can\'t, it can still avoid punishing departure." back (2026-10-17)'),
    '9.5': (A, 'A one-line summing-up after the section has said it.'),
    '9.6': (A, 'Narrowed by me: "Who decides how these things are budgeted and distributed?" stays, since it leads into the '
               'founderism questions that come next.'),
    '10.1': (B, 'The essay\'s bottom line for readers who don\'t go on to the manual; the next paragraph\'s "kicking them out" '
                'leans on it.'),
    '10.2': (B, 'Its reason, that communities keep learning from one another, isn\'t in the assimilation paragraph.'),
    '10.3': (A, 'The paragraph\'s first sentence says it.'),
    '10.4': (A, 'The paragraph says it again two sentences on ("Otherwise their “right” to leave is only on paper"), right '
                'after the remedy.'),
    '10.5': (DROP, 'the same cut as another reader\'s, listed once'),
    '10.6': (DROP, 'the same cut as another reader\'s, listed once'),
}
NARROW = {'9.6': 'What do members owe one another? What happens when someone wants to leave?'}
W08 = [
    {'key': 'W08.1', 'section': 'From One Community to a Movement',
     'quote': 'If the legal or economic environment requires money, the federation also needs to have a cash budget for '
              'dealing with it.',
     'why': 'Your W08 ("i agree with condesning this but we should mention the FEC"): one detail of what running a federation '
            'takes, after the list of its jobs.',
     'loses': 'that a federation may need a cash budget where the law or the economy requires money',
     'note': 'One of two trims for your W08, which GPT\'s reply said I\'d wrongly kept; the FEC, its rebuilding and PEACH '
             'stay.'},
    {'key': 'W08.2', 'section': 'From One Community to a Movement',
     'quote': 'Two communities might want to be closely linked as friends, and that doesn’t stop both of them from also '
              'being part of a general federation.',
     'why': 'Your W08: one of two examples that federation work needn\'t be one body; the FEC\'s PEACH health pool stays as '
            'the example.',
     'loses': 'the example of two communities linked as friends inside a bigger federation',
     'note': 'The second W08 trim; "There can also be local clusters, or single-function institutions like the FEC’s PEACH '
             'health pool ..." follows.'},
]


def main():
    text = (HERE / 'ARTICLE.txt').read_text(encoding='utf-8')
    items = [x for x in json.loads((HERE / 'ITEMS.json').read_text(encoding='utf-8')) if not x['key'].startswith('W08')]
    unknown = [x['key'] for x in items if x['key'] not in PICKS]
    for x in items:
        if x['key'] in NARROW:
            q = NARROW[x['key']]
            assert q in x['quote'] or q in text
            x['quote'] = q
            where = C.locate(text, q)
            x['found'], x['line'], x['heading'] = where is not None, where[0] if where else None, where[1] if where else None
        x['heading'] = x.get('heading') or x.get('section')
        if x['key'] not in PICKS:
            continue
        pick, note = PICKS[x['key']]
        if pick == DROP:
            x['status'], x['note'] = 'drop', note
            x.pop('my_pick', None)
        else:
            x['status'], x['my_pick'], x['note'] = 'keep', pick, note
    for w in W08:
        where = C.locate(text, w['quote'])
        assert where is not None, w['quote']
        items.append(dict(w, part=0, kind='TRIM', said_already='', found=True, line=where[0], heading=where[1],
                          status='keep', my_pick='A', by='mine'))
    (HERE / 'ITEMS.json').write_text(json.dumps(items, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    live = [x for x in items if x.get('status', 'keep') == 'keep']
    print('%d items: %d offered (%d A, %d B), %d looked at and kept; not yet checked: %s' % (
        len(items), len(live), sum(x.get('my_pick') == 'A' for x in live), sum(x.get('my_pick') == 'B' for x in live),
        len(items) - len(live), ', '.join(unknown) or 'none'))


if __name__ == '__main__':
    main()
