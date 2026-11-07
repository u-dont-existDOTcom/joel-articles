#!/usr/bin/env python3
"""Making-sense receipts (gate E365) for r18's checks (texts.py). Every sentence has its row: the live post's sentences
as well as mine (gate E373). A sentence an earlier receipt in this article already has a row for keeps that row; the
rest are written here by their place in the text. Writes CHECK-<name>.txt and RECEIPT-<name>.json and checks each;
exits 1 if one fails."""
import glob
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
from texts import TEXTS  # noqa: E402

OLD = {}
for f in sorted(glob.glob(str(ROOT / 'articles' / 'romance' / 'humanize' / '**' / 'RECEIPT-*.json'), recursive=True)):
    if '/r18/' in f:
        continue
    for s in json.load(open(f, encoding='utf-8')).get('sentences', []):
        if s.get('s') and s.get('payoff'):
            OLD[s['s'].strip()] = (s['payoff'], s['follows'], s.get('link'))

NEXT_Q = 'none: the next question in his list, after the one before'
NEW = {
    'r18-choosing': {
        13: ('with humility the questions change, starting with what remains if the romance changes', 'what changes then',
             'Then the questions change for me'),
        14: ('are they promising actions, or pretending to promise feelings', 'the next question', NEXT_Q),
        18: ('can they rethink the deal if life changes, and what do they owe each other if they split', 'the last questions',
             'If our lives change'),
    },
    'r18-convo': {
        0: ('he wouldn’t ask about past mistakes out of the blue', 'opens the section', None),
        1: ('that would make a weird date', 'why he wouldn’t', 'That would be a pretty weird date'),
        2: ('at the right time he would ask about their recent relationships', 'when he would ask', 'At the right time, though'),
        3: ('if every story blames the other person, he asks what they learned', 'what he listens for', 'If every story ends'),
        4: ('"I have baggage" says almost nothing', 'a vague answer he hears', 'tells me almost nothing'),
        5: ('he asks what they struggle with now', 'what he asks instead', 'What are you having trouble with now'),
        6: ('he asks what makes relationships hard for them', 'his next question', NEXT_Q),
        7: ('both should be honest about how well they handle their issues', 'what he wants of both',
            'I’d want both of us to be honest'),
        8: ('which addictions or impulses they can’t control', 'a question for both',
            'none: the first question of what both should be honest about'),
        9: ('how dependable they are', 'another question for both', NEXT_Q),
        10: ('what they will need forgiving for more than once', 'another question for both', NEXT_Q),
        11: ('that says more than claiming to be healed', 'why he asks it', 'That tells me more'),
        19: ('if someone says they shut down, he asks what that meant in practice', 'a vague answer he would probe',
             'And if you tell me you shut down'),
    },
    'r18-nitty': {
        3: ('a badly made bed can seem to mean he doesn’t care, which is a lot for a bed to carry', 'what it turns into',
            'If I don’t do it well'),
        4: ('another person’s insecurities can be exhausting', 'another cost of a partner', 'can also be exhausting'),
        5: ('alone he feels free, being introverted and a bit autistic', 'why living alone suits him', 'It’s easy to feel free'),
        6: ('in a relationship he is suddenly expected to read every mood', 'what changes in a relationship',
            'All that works wonderfully until'),
    },
    'r18-vows': {
        7: ('Matthew and James make the vow look more suspicious still, since a yes should be enough', 'the next verses',
            'even more suspicious'),
    },
    'r18-loss': dict(enumerate([
        ('he is better off for what happened with Bee, Key and H., without calling all of it good', 'opens the section',
         None),
        ('loss taught him what love alone never would, as Rumi says', 'why he is better off', 'Loss taught me things'),
        ('Rumi’s real words are about a reed torn and hollowed into a flute', 'the source of the paraphrase', 'The real quote'),
        ('Bee taught him what being in love means for him', 'what each woman taught', 'From Bee'),
        ('he learned the kind of woman he wants', 'what else Bee taught', 'I learned the kind of woman'),
        ('Key had much of the same, which is why he fell for her', 'what Key taught', 'Key repeated a lot of that'),
        ('both taught him openness and curiosity aren’t wholly good', 'a harder lesson', 'from both of them'),
        ('openness can mean an undeveloped self or inner adult', 'why they aren’t wholly good', 'They can also indicate'),
        ('H. taught him closeness without falling in love', 'what H. taught', 'From H.'),
        ('he still treasures their support', 'how he feels about it', 'I still treasure'),
        ('judge a relationship by what you learned, not only its result', 'the lesson for the reader',
         'start measuring what you actually learned'),
        ('relationships are growth in many ways', 'why to measure that', 'Relationships are a process'),
        ('staying together isn’t the only result', 'what a result is', 'The result is not only'),
        ('what makes love work isn’t easy or marketable', 'a turn to how hard it is', 'Romantic love is not easy'),
        ('he can’t sell a quick fix', 'his joke about it', 'I can’t sell you the fix'),
        ('he jokes about a link to a love class', 'the joke’s punchline', 'Just kidding'),
        ('such relationships are rare, so romance has long been seen as destabilizing', 'a wider view',
         'A relationship like this is rare'),
        ('Somé’s The Spirit of Intimacy makes that point', 'a book on it', 'makes that point'),
        ('Somé was Dagara, from Burkina Faso', 'who Somé was', 'Somé came from'),
        ('for the Dagara, marriage is arranged, spiritual and communal', 'what her people believe', 'To her people'),
        ('they distrust romance', 'their view of romance', 'They’re suspicious of romance'),
        ('her idea that the relationship is bigger than the egos fits his point', 'what he takes from her',
         'But one of her ideas fits'),
        ('she calls that the spirit of the relationship', 'her name for it', 'She calls it'),
        ('that spirit is the universe knowing itself through us', 'what the spirit is to him', 'That spirit is like'),
        ('nobody can make the spirit stay', 'its limit', 'command the spirit to remain'),
        ('at best we serve it and listen for what it wants to change', 'what we can do', 'At our best, we serve it'),
        ('thinking we own it pushes it away', 'what drives it off', 'When we start thinking we own it'),
        ('his parents shared Somé’s view of community and Spirit', 'his parents’ view', 'My parents agreed with Somé'),
        ('they were loving and poly but not romantic', 'what they were like', 'They were also not romantic'),
        ('he wished they were in love, without the words for it then', 'how he felt as a child',
         'I actually wished they were in love'),
        ('they taught him everyone was basically good', 'what else they taught', 'Also reminiscent of Somé'),
        ('he learned love and community, not how hard romance is alone or how good people do damage',
         'what he did and didn’t learn', 'So I learned something about love'),
        ('it took him decades to see that real pathology exists', 'what he learned late', 'It took me many decades'),
        ('pathology festers in the right environment', 'what feeds it', 'But pathology festers'),
        ('our culture seals couples off and calls it privacy', 'the environment that feeds it',
         'The dominant culture hermetically seals'),
        ('it expects the couple to give each other everything', 'what it expects', 'that sealed room'),
        ('then it blames the couple for the predictable failure', 'what happens after', 'Then it treats the predictable failure'),
        ('romance myths become real because we act them out', 'why the myths persist', 'The myths around romantic love'),
        ('we act as if jealousy proves love and an ending means failure', 'the myths named', 'We act as though'),
        ('we suffer inside those ideas and keep remarrying', 'what it costs', 'Then we suffer inside ideas'),
        ('he may have written this for his son Bear, last seen at five', 'who the article is for',
         'I wrote this whole article for my son'),
        ('he tells Bear sex comes with a special love and wanting children', 'his talk to Bear', 'Bear, sex can be'),
        ('wanting each other isn’t love', 'his first advice to Bear', 'Don’t imagine you love each other'),
        ('don’t promise future feelings', 'his next advice', 'promise what your heart will feel'),
        ('let love grow honestly', 'what to do instead', 'Let the love and bond'),
        ('learn each other slowly and keep friends and community around', 'his last advice', 'Learn about each other'),
        ('a sacred relationship opens the heart even if it ends', 'his closing, back to Rumi', 'I believe Rumi was right'),
    ])),
}
# Sentences whose old rows opened a check and so had no link, now inside the section: the link alone.
OVERRIDE = {'The most recent conflicts are the best place to look.': 'The most recent conflicts',
            'We also find something like my warning': 'We also find something like my warning'}
META = {
    'r18-choosing': ('What are you actually choosing together?',
                     'A couple about to commit or move in, who haven’t said what each of them means by it.',
                     'It tells the reader to say what "together" means before committing.'),
    'r18-convo': ('The conversation about flaws',
                  'Someone dating, wondering how to ask a new partner about their past relationships and flaws.',
                  'It tells the reader what to ask about past relationships, and when.'),
    'r18-nitty': ('From flow to nitty gritty', 'Someone used to living alone, about to share daily life with a partner.',
                  'It tells the reader how small daily things start to carry weight in a relationship.'),
    'r18-vows': ('Which marriage vows are honest?',
                 'A couple about to write or say wedding vows, wondering what they can honestly promise.',
                 'It tells the reader which vows are honest: actions, not feelings.'),
    'r18-loss': ('What I gained from loss', 'Someone after a breakup, wondering what the relationship was worth.',
                 'It tells the reader to measure a relationship by what they learned.'),
}
Q = {
    'Q1': 'PASS: each changed sentence gives its point first, in plain words',
    'Q2': 'N/A: these sections tell and ask; the advice in them is unchanged',
    'Q3': 'PASS: the people, places, numbers and things are named as in the live post',
    'Q4': 'PASS: no new term; "inner adult" and "the spirit of the relationship" are used as the live post uses them',
    'Q5': 'PASS: each sentence’s tie is in its words (the links field), or the link says why it needs none',
    'Q6': 'PASS: the order is the live post’s; the joins named in texts.py keep it',
    'Q7': 'PASS: each change keeps what the section tells the reader about their own case',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence in the changed paragraphs',
}
LOW = [{'point': 'the Low windows’ points', 'found': 'the live post (../../live-check/LOW-WINDOWS.json), the last part’s '
        'check (#47, ../../r07/checks/RESULTS-r07.json) and the spots’ checks (S7 #34, S9 #10, S21 #46, S20 in #103)',
        'still_needed': 'yes: the section needs them', 'fate': 'changed'}]
bad = 0
for name, text in TEXTS.items():
    section, reader, why = META[name]
    r = S.make(text, section, reader)
    new = NEW.get(name, {})
    assert all(0 <= i < len(r['sentences']) for i in new), name
    for i, s in enumerate(r['sentences']):
        row = new.get(i)
        if row is None:
            row = OLD[s['s'].strip()]
            ov = next((v for k, v in OVERRIDE.items() if s['s'].startswith(k)), None)
            if ov:
                row = (row[0], row[1], ov)
        pay, fol, link = row
        s['payoff'] = pay if pay.startswith('the reader learns ') else 'the reader learns ' + pay
        s['follows'] = fol
        if 'link' in s:
            s['link'] = link
    r['opens']['why_reading'] = why
    r['same_point'] = 'none: read the section from its heading to the next for these points; each is made once, here'
    r['questions'] = dict(Q)
    r['checked'] = LOW
    r['placement'] = 'The whole section, in its place in the live post, its heading left out.'
    if name == 'r18-loss':
        r['late_ok'] = {'Relationships': 'an everyday word, not a term: his sentence says what a relationship is for, it '
                                          'does not define the word, and the sentence is his, unchanged'}
    (HERE / ('CHECK-%s.txt' % name)).write_text(text, encoding='utf-8')
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
