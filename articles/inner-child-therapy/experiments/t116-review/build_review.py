#!/usr/bin/env python3
"""Turn 116: the marking page for Joel's reorganized guide (his ODT of 2026-11-03 21:00 UTC; his message: "i think it's
basically ready to publish unless you have suggestions... prob still some redundancy that could be cut out but i didn't
see how... maybe double check to make sure it all flows since lots of reorg, possibly some terms get defined too late
now"), built with tools/humanization/suggestion_review.py on GUIDE-PAGE.md (make_page_copy.py): REVIEW.json,
REVIEW.html, REVIEW-artifact.html.

Where the suggestions come from: my own whole read of his file (in order, for flow, terms used before they're explained,
pointers his moves broke, repeats, and sense), an independent reader's read (experiments/t116-joel/INDEPENDENT-READ.md,
a fresh agent that saw only his file; what I took from it is marked "found_by"), the link and picture comparison with
the guide I last gave him (experiments/t116-joel/LINKS.md, relink.py), and the sentence comparison (EDITS.md). The six
suggestions that put words of mine into his sentences are the exact words the owner-delivery gate admitted
(experiments/t116-gate/G1..G6/FOR-JOEL.txt); the build stops if one isn't. Everything else is a cut, a move, his own
words put back, a typo or a question.

  python3 articles/inner-child-therapy/experiments/t116-review/build_review.py"""
import datetime
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

ARTICLE = 'articles/inner-child-therapy/experiments/t116-review/GUIDE-PAGE.md'
BRANCH = 'handoff/claude-dangerous-adult-20260924-1631'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/%s/articles/inner-child-therapy/experiments/' % BRANCH
MD = (ROOT / ARTICLE).read_text(encoding='utf-8')
BL = sr.blocks(MD)
GATE = HERE.parent / 't116-gate'
RELINK = json.loads((HERE / 'RELINK.json').read_text(encoding='utf-8'))
OWNER_SOURCE_FOUR_PAIRS = ('It’s four pairs, starting with pleasure and pain, and gain and loss. The other two are about what '
                           'people think of you: praise and blame, and good reputation and disgrace.')
DOG = ('Sometimes it’s not that you can’t love in general. Your dog can chew up your good shoes and be forgiven before '
       'you’ve found the other one. But maybe you direct that love to your little one and the attempt goes flat, or starts '
       'to feel weirdly unsafe. Just feel that love you can feel for others for a minute, in your body, before you try to '
       'redirect anything. Then as you relax into that and enjoy it more, imagine it flowing downhill, like an overflowing '
       'river of delicious chocolate. Now imagine how happy your inner child is at the bottom of the hill to play in that '
       'chocolate love that rolled down!')
CRISIS = 'Do the same if you can’t stop yourself, or you’re badly disoriented or intoxicated.'

TYPES = {
    'links': {'label': 'Links and pictures', 'about': 'What the file you edited lost: links, pictures and videos. My fault: the Word file I sent you last time had none of them.'},
    'pointer': {'label': 'Pointers your moves broke', 'about': 'A "that X", "as described in", or a term used before it is explained, because its setup moved or went.'},
    'repeat': {'label': 'Repeats', 'about': 'The same thing said twice, with a cut that loses nothing.'},
    'check': {'label': 'Worth a second look', 'about': 'A label or a line I would weigh again before publishing.'},
    'format': {'label': 'Formatting leftovers', 'about': 'Headings, stray lines and numbers left from the reorganizing.'},
    'typo': {'label': 'Typos', 'about': 'Obvious typos only, a chapter per card; your spelling and style otherwise stay.'},
    'ask': {'label': 'Questions', 'about': 'Your call: a question, with my recommendation.'},
}
S = []


def q(text, near=None):
    return sr.find_quote(BL, text, near)


def span(text, near=None):
    i, s, e = q(text, near)
    return {'block': i, 'start': s, 'end': e}


def gated(gid):
    p = GATE / gid / 'FOR-JOEL.txt'
    assert p.exists(), 'not admitted by the gate: ' + gid
    words = p.read_text(encoding='utf-8')
    proof = json.loads((GATE / gid / 'FOR-JOEL.proof.json').read_text(encoding='utf-8'))
    assert proof['candidate_sha256'] == hashlib.sha256(words.encode('utf-8')).hexdigest(), gid
    return words


def replace_in(i, pairs):
    """Block i's text with each (old, new) applied once; each old must occur exactly once."""
    t = BL[i]['text']
    for old, new in pairs:
        assert t.count(old) == 1, (i, old, t.count(old))
        t = t.replace(old, new)
    return t


def add(**k):
    S.append(k)


# ---------------------------------------------------------------- links and pictures

HEAD_OF = {b['text']: b['i'] for b in BL if b['level']}


def links_cards():
    rows = RELINK['base_links']
    spans, seen = [], set()
    for r in rows:
        if r['action'] == 'restore':
            spans.append({'block': r['block'], 'start': r['start'], 'end': r['end']})
            seen.add(r['block'])
    for t in RELINK['his_typed_links']:
        spans.append({'block': t['block'], 'start': t['start'], 'end': t['end']})
    for o in RELINK['odd_typed_links']:
        spans.append(span(sr.LINK.sub(r'\1', o).replace('\xa0', ' ')))
    spans.sort(key=lambda s: (s['block'], s['start']))
    n_restore = sum(r['action'] == 'restore' for r in rows)
    add(id='L1', type='links', advice='ask', title='Put the links back',
        question=('Shall I put back the %d links the guide had where your words still are, and make your own %d typed links '
                  '(the ones written as [words](address), which your file and Substack show as typed) real links? I recommend yes. '
                  'Every highlighted word on this page is one of them.' % (n_restore, len(RELINK['his_typed_links']) + len(RELINK['odd_typed_links']))),
        why=('The Word file I sent you last time had no links at all (I built it from plain text), so the file you edited kept only '
             'six, the ones you put in yourself. On this page your typed links look like links, because the page reads that '
             'typing; in your file they are text. The details, link by link, are in RELINK.md (%s). The fixes in it: the shame '
             'guide goes to the address you gave me tonight; Key goes to her Substack (%s, where the guide\'s old link for her '
             'lands too); the Wiley and PMC links lose the "utm_source=chatgpt.com" on the end, and the song link its playlist '
             'part; "spiritual bypassing" gets your bypassing link at its first use in My Journey, as the last guide had it, '
             'and at the Appendix; the four typed in a form even this page can\'t read become plain links (the love-language '
             'song, building community, spiritual bypassing, and the doubled Lucia institute link). I opened all 93 '
             'addresses from your laptop today: all open but Wiley, which refuses scripts (it\'s your link, so it stays), and '
             'shame.innerself.love, which doesn\'t resolve.') % (BLOB + 't116-review/RELINK.md', 'substack.com/@keygoddess11'),
        stays=('Six of the last guide\'s links stay out: five went with words you cut (tonglen, the small pilot study, and three in '
               'the My Journey lines you rewrote), and "Another" now starts a different sentence. Three more stay out because you '
               'put your own link on the same words (the Serenity Prayer, female iboga) or the words are a heading now.'),
        advice_note='Yes. I\'d also make a habit of it: I check every file I send you for its links and pictures now.',
        spans=spans, found_by='the link comparison (links.py, relink.py)')
    natives = [
        ('Welcome, lovey bunnies!', 'the top chart, "Inner Child Reparenting: Connect Today, Nurture Today, Heal Tomorrow", above the first line'),
        ('Céline’s right up there', 'the Céline Dion video you subtitled, which "Céline’s right up there" and the next section\'s "Céline’s song" lean on'),
        ('Rosey Grier’s It’s All Right to Cry is a little further down', 'the Rosey Grier video, after the first Chicken-and-Egg paragraph, which "a little further down" points at'),
        ('The image below maps out the details as best as I can fit:', 'the study chart, where your file has a lone "."'),
        ('Here’s a map of what to try when:', 'the Somatic Therapy Modalities Map post embed'),
        ('Your Loan is PRE-APPROVED!', 'the EndSickness.org short on gratitude, under this heading'),
        ('Yep. Exactly like that.', 'the sleep-paralysis drawing ("Jinn Al Kaboos"), which "Yep. Exactly like that." answers'),
    ]
    add(id='L2', type='links', advice='ask', title='Seven pictures and videos from the live post',
        question=('Keep these seven from the post when you update it? I recommend yes, and I\'ll put them in the Substack draft '
                  'in the same places: ' + '; '.join(x[1] for x in natives) + '.'),
        why=('Your file has your six new pictures, but none of the post\'s own (the file I sent had none). Five of your lines still '
             'point at one, so without them those lines point at nothing.'),
        stays='Your six new pictures stay where you put them.',
        advice_note='Yes.', spans=[span(x[0], HEAD_OF.get(x[0])) for x in natives], found_by='the comparison with the live post (master.html) and the last guide')
    add(id='L3', type='links', advice='ask', title='The studies screenshot is cut off',
        question=('The screenshot under "some studies" (Listen To Your Body, Or Else!) is cropped on the right ("certai", "bodily" '
                  'run off the edge), and it shows a chat answer\'s styling. Re-take it uncropped, or replace it with one line '
                  'and the link? I\'d re-take it uncropped.'),
        why='A cut-off screenshot reads as unfinished, and it is the evidence for the paragraph above it.',
        advice_note='Re-take it uncropped; the paragraph and its link stay as they are.',
        spans=[span('image 2'), span('some studies')], found_by='me, looking at the picture')


# ---------------------------------------------------------------- formatting leftovers

def format_cards():
    dot = next(b['i'] for b in BL if b['text'].strip() == '.')
    add(id='F1', type='format', advice='approve', title='The lone "." where the study chart goes',
        spans=[{'block': dot, 'start': 0, 'end': 1}], edits=[{'block': dot, 'before': BL[dot]['text'], 'after': ''}],
        what='The "." line under "The image below maps out the details as best as I can fit:" goes; the study chart goes there (L2).',
        why='It is a placeholder, and on the page it reads as a stray full stop.', stays='The line before it.',
        deciding='If you keep the "." on purpose as your marker, reject this and I\'ll swap it for the chart when I make the draft.',
        found_by='me')
    h = q('https://www.youtube.com/watch?v=JQs2watlFws')[0]
    nxt = q('What to Make of a Passing Feeling')[0]
    add(id='F2', type='format', advice='approve', title='The mantra video link is a heading, above its paragraph',
        spans=[{'block': h, 'start': 0, 'end': len(BL[h]['text'])}],
        edits=[{'block': h, 'before': BL[h]['text'], 'after': ''}],
        inserts=[{'before': nxt, 'kind': 'p', 'text': 'https://www.youtube.com/watch?v=JQs2watlFws', 'seq': 0}],
        what=('The YouTube link stops being a heading and moves under the paragraph that ends "...For the Benefit of All Beings:", '
              'on its own line, so Substack shows the video there. (The empty heading at the end of Close the Session goes too.)'),
        why='As a heading it would show in the table of contents as a web address, and the colon at the end of the paragraph points at a video that comes before it.',
        stays='The link itself, and the paragraph.', deciding='Reject if you put it above the paragraph on purpose.', found_by='me')
    add(id='F3', type='format', advice='approve', title='What to Make of a Passing Feeling, one level up',
        spans=[span('What to Make of a Passing Feeling')],
        edits=[{'block': nxt, 'before': BL[nxt]['text'], 'after': '## What to Make of a Passing Feeling'}],
        what='The heading goes from a subsection of Gentle Meditation and Mantra to a section beside it.',
        why='It is about not over-reading a feeling, not about meditation; it came from Catch the Hook, and under the mantra heading the table of contents files it there.',
        stays='Its words and its place.', deciding='Reject if you want it under the mantra section.', found_by='me, and the independent reader')
    rumi = q('Jelaluddin Rumi wrote')[0]
    rumi_p = ('Jelaluddin Rumi wrote: “The most secure place to hide a treasure of gold is some desolate, unnoticed place. Why '
              'would anyone hide treasure in plain sight? And so it is said: ‘Joy is hidden in sorrow.’”')
    add(id='F4', type='format', advice='approve', title='The Rumi quote is a heading',
        spans=[{'block': rumi, 'start': 0, 'end': len(BL[rumi]['text'])}],
        edits=[{'block': rumi, 'before': BL[rumi]['text'], 'after': ''}],
        inserts=[{'before': rumi + 1, 'kind': 'p', 'text': rumi_p, 'seq': 0}],
        what='The quote becomes the first paragraph under The Joy In Sorrow, with its quote marks closed (it opened two and closed one).',
        why='As a heading it is a whole sentence in large type in the table of contents, and The Joy In Sorrow above it has nothing under it.',
        stays='His words, every one.', deciding='Reject if you want it as a heading.', found_by='me')
    nums = [q('3. Finding People and Building Trust')[0], q('5. When One Life Has Ended')[0], q('6. The Love Has to Move')[0]]
    add(id='F5', type='format', advice='approve', title='Numbers left on three headings',
        spans=[{'block': i, 'start': 0, 'end': 2} for i in nums],
        edits=[{'block': i, 'before': BL[i]['text'], 'after': BL[i]['text'][3:]} for i in nums],
        what='"3.", "5." and "6." come off; you already took 1, 2 and 4 off.',
        why='They are left from the chat\'s six-section plan for Bringing Reparenting Into Real Life.', stays='The headings\' words.',
        deciding='Reject if you want all six numbered (then 1, 2 and 4 need theirs back).', found_by='me')
    add(id='F6', type='format', advice='ask', title='"Mo’ Money, Mo’ Problems" on its own line',
        question=('"Mo’ Money, Mo’ Problems" stands alone between two paragraphs of Your Loan is PRE-APPROVED! Did you mean it as a '
                  'small heading for the prosperity part? I\'d make it one (a level below Your Loan is PRE-APPROVED!).'),
        why='On its own as a paragraph it reads like a stray line; as a heading it sets up the Biggie Smalls line two paragraphs down.',
        advice_note='A small heading.', spans=[span('Mo’ Money, Mo’ Problems')], found_by='me')


# ---------------------------------------------------------------- typos, a chapter per card

TYPOS = [
    ('shying way from the silly', 'shying way', 'shying away'),
    ('heal  itself', 'heal\xa0 itself', 'heal\xa0itself'),
    ('So left it out of the first version', 'So left it', 'So I left it'),
    ('crucial.Without', 'crucial.Without', 'crucial. Without'),
    ('continue with reparenting:', 'reparenting:', 'reparenting.'),
    ('start beliving in you', 'beliving', 'believing'),
    ('But it even though my depression', 'But it even though', 'But even though'),
    ('identifying as the frightened kid still', 'frightened kid still', 'frightened kid'),
    ('manages to be get a perfect', 'to be get', 'to get'),
    ('their children bring home . 😛', 'bring home . ', 'bring home. '),
    ('relationship orquitting a job', 'orquitting', 'or quitting'),
    ('anyone abou tthis', 'abou tthis', 'about this'),
    ('borrowed adulthood trick', '».,\xa0 The new', '». The new'),
    ('Pema Chödrön(who inspired', 'Chödrön(who', 'Chödrön (who'),
    ('follows him as an idiot', 'follows him as an idiot', 'follows him is an idiot'),
    ('(along with spirituality) , but', ') , but', '), but'),
    ('feel loved (Nurterer)', 'Nurterer', 'Nurturer'),
    ('In the movie A Beautiful Day in the Neighborhood. Lloyd', 'Neighborhood. Lloyd', 'Neighborhood, Lloyd'),
    ('“I don’t trust you.” you can answer', 'you.” you can', 'you,” you can'),
    ('You’re little one will be watching', 'You’re little one', 'Your little one'),
    ('once you’re ears guards are off', 'you’re ears guards', 'your ear guards'),
    ('calledscaffolding', 'calledscaffolding', 'called scaffolding'),
    ('heard and addressed .', 'addressed .', 'addressed.'),
    ('every time while we don’t', 'while we don’t', 'while you don’t'),
    ('remember fondlly', 'fondlly', 'fondly'),
    ('Borrrow Your Love For Someone Else', 'Borrrow', 'Borrow'),
    ('for example). hope you are able', '). hope', '). I hope'),
    ('to listen to their rejection be patient', 'rejection be patient', 'rejection, be patient'),
    ('Inayat Khan, wrote,“God', 'wrote,“God', 'wrote, “God'),
    ('(”You hated that coat”)', '(”You', '(“You'),
    ('“Who abused me & how? »', 'how?\xa0»', 'how?”'),
    ('might want to be written.Then', 'written.Then', 'written. Then'),
    ('you might be surprised sometimes the myriad', 'surprised sometimes the myriad', 'surprised sometimes by the myriad'),
    ('sometime’s it’s not', 'sometime’s', 'sometimes'),
    ('Pharao Tutankhamun', 'Pharao', 'Pharaoh'),
    ('(”Once upon a time', '(”Once', '(“Once'),
    ('schedule.If someone', 'schedule.If', 'schedule. If'),
    ('too much to hold, You may have heard', 'hold, You', 'hold. You'),
    ('lucky ,» it’s not', 'lucky\xa0,»', 'lucky\xa0»,'),
    ('Even, going on a date', 'Even, going', 'Even going'),
    ('remember that In John 14:12', 'that In John', 'that in John'),
    ('suppressed as you grew up..', 'grew up..', 'grew up.'),
    ('playing the « chamelion »', 'chamelion', 'chameleon'),
    ('That chamelion’s fake', 'That chamelion’s', 'That chameleon’s'),
    ('the chamelion was a skillset', 'the chamelion was', 'the chameleon was'),
    ('(”I hate cooking', '(”I hate', '(“I hate'),
    ('my post Treasuring the Inner Child’s Gift', 'Child’s Gift', 'Child’s Gift.'),
    ('kind of test--”First', '--”First', '--“First'),
    ('here you, let’s pl/ork', 'here you, let’s', 'here you go, let’s'),
    ('“May you loving, peaceful', 'May you loving', 'May you be loving'),
    ('in the appendix,.', 'appendix,.', 'appendix.'),
    ('want to think with you Actually', 'with you Actually', 'with you. Actually'),
    ('your subconsciosu', 'subconsciosu', 'subconscious'),
    ('inidivdual therapist', 'inidivdual', 'individual'),
    ('developed in 1980s-1990s', 'developed in 1980s', 'developed in the 1980s'),
    ('set limits..', 'limits..', 'limits.'),
    ('committed to. all that sounds', 'to. all that', 'to. All that'),
    ('(It’s normally described as', '(It’s normally', 'It’s normally'),
    ('maps the your difficulties', 'maps the your', 'maps your'),
    ('Internal Family Systems (FS)', '(FS)', '(IFS)'),
    ('powerful meditations.For example', 'meditations.For', 'meditations. For'),
    ('excluded condition.And the parts', 'condition.And', 'condition. And'),
]
NOTES = {
    'while you don’t': 'you changed "Most of us feel better and call them" to "You call them", and the end still said "we"',
    'or quitting': 'with "Quitting a job?" folded into the sentence, the space after "or" went',
    'reparenting.': 'stage 1 ended on a colon with nothing after it',
    'It’s normally': 'the bracket opened before "It’s" never closed',
    'lucky\xa0»,': 'the comma sat inside the closing quote mark',
}


def typo_cards():
    by_ch = {}
    for find, old, new in TYPOS:
        i = q(find)[0]
        ch = BL[i]['path'][0] if BL[i]['path'] else BL[i]['text']
        by_ch.setdefault(ch, []).append((i, old, new))
    order = [b['text'] for b in BL if b['level'] == 1]
    for n, ch in enumerate(sorted(by_ch, key=order.index), 1):
        items = by_ch[ch]
        blocks = {}
        spans = []
        for i, old, new in items:
            blocks.setdefault(i, []).append((old, new))
            t = BL[i]['text']
            k = t.find(old)
            spans.append({'block': i, 'start': k, 'end': k + len(old)})
        edits = [{'block': i, 'before': BL[i]['text'], 'after': replace_in(i, pairs)} for i, pairs in sorted(blocks.items())]
        notes = ['%s (%s)' % (new.strip(), NOTES[new]) for _, _, new in items if new in NOTES]
        extra = (' In My Journey your file also has a bold "n" ("A**n** old childhood wound") and a bold space before "And a lot of '
                 'the childhood stuff"; they go too.') if ch == 'Understanding Reparenting' else ''
        add(id='T%d' % n, type='typo', advice='approve', title='Typos in %s (%d)' % (ch, len(items)), spans=spans, edits=edits,
            what='%d obvious typos: a missing space or word, a doubled letter, a quote mark the wrong way round.%s' % (len(items), extra),
            why='Typos only.' + (' Two need a word of explanation: ' + '; '.join(notes) + '.' if notes else ''),
            stays='Everything else, your spelling choices included ("wizdumb", "sMothered", "tho", "youngin’", "goin").',
            deciding='Reject any one by saying which in the comment box.', found_by='me')


def quotes_card():
    spans = []
    for b in BL:
        for m in re.finditer(r'«\xa0|\xa0»|\xa0[!?:]| :', b['text']):
            spans.append({'block': b['i'], 'start': m.start(), 'end': m.end()})
    n_q = sum(b['text'].count('«') for b in BL)
    n_s = sum(len(re.findall(r'\xa0[!?:]| :', b['text'])) for b in BL)
    add(id='Q1', type='ask', advice='ask', title='French quote marks and spaces',
        question=('Your file has %d pairs of « » and %d spaces before ! ? or : (LibreOffice\'s French autocorrect puts them in, '
                  'with a no-break space). Change them all to English “ ” and no space, the way the rest of the guide has it? '
                  'I recommend yes. Each one is highlighted.' % (n_q, n_s)),
        why='In an English post they read as typos; the quotes in the same paragraphs are “ ”.',
        advice_note='Yes, all of them; your quotes of Malia, your mom and the CIA examples keep their words.',
        spans=spans, found_by='me')


# ---------------------------------------------------------------- pointers his moves broke

def pointer_cards():
    g = {k: gated(k) for k in ('G1', 'G2', 'G3', 'G4', 'G5', 'G6')}
    i = q('as described in Noticing Counts')[0]
    add(id='P1', type='pointer', advice='approve', title='"As described in Noticing Counts" points forward now',
        spans=[span('as described in Noticing Counts')],
        edits=[{'block': i, 'before': BL[i]['text'], 'after': replace_in(i, [('as described in Noticing Counts', g['G1'])])}],
        what='"(as described in Noticing Counts)" becomes "(%s)".' % g['G1'],
        why='Noticing Counts is in Building Your Inner Adult now, after this section. "Further on" is how you point ahead yourself ("in « Untangling the Belonging Bargains » further on").',
        stays='The instruction and the borrowed adult.', deciding='Reject to keep the pointer as it was, or cut it in the comment box.',
        found_by='me, and the independent reader')
    i = q('avoidance of differentiation')[0]
    add(id='P2', type='pointer', advice='approve', title='"Differentiation" comes up before its section',
        spans=[span('avoidance of differentiation')],
        edits=[{'block': i, 'before': BL[i]['text'], 'after': replace_in(i, [('avoidance of differentiation.', 'avoidance of differentiation ' + g['G2'] + '.')])}],
        what='After your "avoidance of differentiation": "%s".' % g['G2'],
        why='You brought the word in here (it said "the pattern"), and Differentiation: Keeping Your Own Ground is far ahead, in Bringing Reparenting Into Real Life. The words are yours, from "We get deeper into finding and building that self ... further on".',
        stays='Your sentence.', deciding='Reject if the word is clear enough here on its own.', found_by='me')
    i = q('earns that guard’s trust')[0]
    add(id='P3', type='pointer', advice='approve', title='"That guard’s trust": no guard yet',
        spans=[span('that guard’s trust')],
        edits=[{'block': i, 'before': BL[i]['text'], 'after': replace_in(i, [('that guard’s', g['G3'])])}],
        what='"Your Protector earns that guard’s trust" becomes "Your Protector earns %s trust".' % g['G3'],
        why='This paragraph sat under Hear the Guard First, where "that guard" was the protective part. You moved it to the end of Protecting and Building Trust and called it "Earning their trust"; the guard image only comes later, in If the Love Isn\'t Coming Yet.',
        stays='The roommate, the rent and your two examples.', deciding='Reject if you meant a guard here and want it set up instead.',
        found_by='me, and the independent reader')
    i = q('That future you probably also knows')[0]
    add(id='P4', type='pointer', advice='approve', title='"That future you": its setup is cut',
        spans=[span('That future you')],
        edits=[{'block': i, 'before': BL[i]['text'], 'after': replace_in(i, [('That future you', g['G4'])])}],
        what='"That future you probably also knows..." becomes "%s probably also knows...".' % g['G4'],
        why='You cut the sentence it pointed back to ("It’s a question borrowed from your future self"). "Your future self" is your phrase from The Chicken-and-Egg Problem.',
        stays='Your new lines about your mom and "One man’s humor is another’s wisdom".', deciding='Reject to put the cut sentence back instead.',
        found_by='me')
    i = q('this cast of perfected future characters')[0]
    add(id='P5', type='pointer', advice='approve', title='"This cast of perfected future characters" was built 190 lines back',
        spans=[span('this cast of perfected future characters')],
        edits=[{'block': i, 'before': BL[i]['text'], 'after': replace_in(i, [('future characters in your mind', 'future characters ' + g['G5'] + ' in your mind')])}],
        what='"%s" after "this cast of perfected future characters".' % g['G5'],
        why='The cast is the wiser future versions of you and the others in Borrow Hindsight (The Inner Guide); this section comes after Forgiving Yourself, so "this cast" reads as if it had just been built.',
        stays='Your sentence.', deciding='Reject if you\'d rather move this section next to Borrow Hindsight.', found_by='me, and the independent reader')
    i = q('stay curious about its motivations')[0]
    add(id='P6', type='pointer', advice='approve', title='"Its motivations": the critical voice is two paragraphs up',
        spans=[span('stay curious about its motivations')],
        edits=[{'block': i, 'before': BL[i]['text'], 'after': replace_in(i, [('about its motivations', 'about ' + g['G6'] + ' motivations')])}],
        what='"stay curious about its motivations" becomes "stay curious about %s motivations".' % g['G6'],
        why='Between "a critical voice" and this "its" comes the Mr. Rogers story about Lloyd, so the first "its" has nothing near it; your later "its" and "that voice" follow from it.',
        stays='The trick, the kernels of truth, sending it on its way.', deciding='Reject if it reads clearly to you.', found_by='me, and the independent reader')
    a, b = q('Re-evaluation counseling always ends')[0], q('Re-evaluation Counseling , a global movement')[0]
    add(id='P7', type='pointer', advice='approve', title='Re-evaluation Counseling is explained at its second mention',
        spans=[span('Re-evaluation counseling always ends'), span('Re-evaluation Counseling , a global movement of peer counseling,')],
        edits=[{'block': a, 'before': BL[a]['text'], 'after': replace_in(a, [('Re-evaluation counseling always ends', 'Re-evaluation Counseling, a global movement of peer counseling, always ends')])},
               {'block': b, 'before': BL[b]['text'], 'after': replace_in(b, [('Re-evaluation Counseling , a global movement of peer counseling, counts', 'Re-evaluation Counseling counts')])}],
        what='Your ", a global movement of peer counseling," and its link move from When the Urge to Escape Arrives to its first mention, in Use Childhood Photographs Gently.',
        why='Practicing comes before When the Practice Gets Difficult now, so the photos section names it first, with no explanation.',
        stays='Your words, all of them, in a different spot.', deciding='Reject to keep it as is.', found_by='me, and the independent reader')
    a, b = q('I call it pl/ork')[0], q('call the deeper therapy pl/ork, play + work')[0]
    add(id='P8', type='pointer', advice='approve', title='"Pl/ork" is spelled out 790 lines after you coin it',
        spans=[span('I call it pl/ork'), span('pl/ork, play + work')],
        edits=[{'block': a, 'before': BL[a]['text'], 'after': replace_in(a, [('I call it pl/ork\xa0!', 'I call it pl/ork (play + work)\xa0!')])},
               {'block': b, 'before': BL[b]['text'], 'after': replace_in(b, [('pl/ork, play + work.', 'pl/ork.')])}],
        what='Your "play + work" moves from Play Is Part of the Work to the first "I call it pl/ork", in the nutshell.',
        why='The reader meets pl/ork in the nutshell and uses it three times (let\'s pl/ork, pl/orkfully) before it is spelled out near the end.',
        stays='Both sentences, and your second "I call the deeper therapy pl/ork".', deciding='Reject if you like the reveal late.', found_by='me, and the independent reader')
    i = q('the Adult Protector to start paying attention')[0]
    add(id='P9', type='pointer', advice='approve', title='"The Adult Protector" after "hereafter just the Protector"',
        spans=[span('the Adult Protector')],
        edits=[{'block': i, 'before': BL[i]['text'], 'after': replace_in(i, [('the Adult Protector', 'the Protector')])}],
        what='"Adult" comes out of "ask the Adult Protector to start paying attention".',
        why='The nutshell says "a safe Adult Protector (hereafter just the Protector)", and this is the only place after it that says Adult Protector.',
        stays='The sentence.', deciding='Reject if you want the full name here.', found_by='me')
    solomon = q('Or put somebody you care about into your exact life')[0]
    add(id='P10', type='pointer', advice='approve', title='"The dog kind of love": the dog paragraph went missing',
        spans=[span('The dog kind of love is real love.'), span('Borrow Your Love For Someone Else'.replace('Borrow', 'Borrrow'))],
        inserts=[{'before': solomon, 'kind': 'p', 'text': DOG, 'seq': 0}],
        what=('Your dog-and-chocolate paragraph from the last guide goes back as the first paragraph under Borrow Your Love For Someone '
              'Else, in your characters.'),
        why=('Ask God for a Loan still starts "The dog kind of love is real love" and "I don’t want to lump that in with the dog", and '
             'nothing before it has a dog now. Your new heading, Borrow Your Love For Someone Else, is what that paragraph does (feel '
             'the love you have for others, then let it flow down to your little one), so I think it slipped out in the move.'),
        stays='The Solomon\'s paradox paragraph after it, which then starts "Or put somebody you care about..." the way it did.',
        deciding='Reject if you cut it on purpose; then "The dog kind of love is real love" and "with the dog" need to go (I\'d cut the first sentence and the clause).',
        found_by='me, and the independent reader')
    i = q('quick map for finding the bargain')[0]
    add(id='P11', type='pointer', advice='approve', title='"Four Pairs That Commonly Hook the Child" never names the pairs',
        spans=[span('Four Pairs That Commonly Hook the Child'), span('Pema Chödrön has a quick map for finding the bargain.')],
        edits=[{'block': i, 'before': BL[i]['text'], 'after': replace_in(i, [('quick map for finding the bargain. ', 'quick map for finding the bargain. ' + OWNER_SOURCE_FOUR_PAIRS + ' ')])}],
        what='Your two sentences naming the pairs go back after "Pema Chödrön has a quick map for finding the bargain."',
        why='They were in the chapter you sent the other chat today and in the file it gave you back; in this file the heading and "a quick map" promise them and nothing names them. Looks like they slipped out.',
        stays='Everything else in the paragraph.', deciding='Reject if you cut them on purpose; then the heading needs a new name.',
        found_by='me, and the independent reader')
    add(id='P12', type='ask', advice='ask', title='Hear the Guard First is gone: on purpose?',
        question=('The section that taught hearing the protective part out before your little one (Hear the Guard First, with If it '
                  'won\'t step back and If it\'s been calling all this stupid), and the skeptic guard before it, aren\'t in this '
                  'version. You moved its other two subsections out (to Shame and to Earning their trust) and took out "the way you did in '
                  'Hear the Guard First", so it looks deliberate. But the IFS appendix still says "my section, “meet the protector '
                  'first,”", and two of your appendix pictures still say "hear the protector first" (Schema) and "the guard at the '
                  'door" (Lucia). Was the cut meant? If yes, I\'d cut "my section," so the line reads as it did before ("so “meet '
                  'the protector first” would fit right in over there").'),
        why='Readers will look for the section the appendix points to. The pictures also use "protector" for the guard, which you keep apart from the Protector.',
        advice_note='If the cut was meant: cut "my section," and leave the pictures (their words are small). If not: I put the section back after When the Urge to Escape Arrives.',
        spans=[span('my section, “meet the protector first,”'), span('image 4'), span('image 5')], found_by='me, and the independent reader')
    add(id='P13', type='ask', advice='ask', title='The re-do itself is missing',
        question=('Using hindsight to « re-do » memories sets up reliving a memory "in a better way" and says "we will contrast it with the '
                  'corrected version", but then goes to what good discipline would have been, and ends there: no step where the '
                  'reader replays the memory with the corrected version. Did a paragraph get lost, or do you want one? I\'d add two or '
                  'three sentences of the re-do (in your words; I can draft it from what you tell me).'),
        why='The heading promises the re-do; the reader who tries it has the setup and the discussion but not the move.',
        advice_note='Add the step. Tell me how you do it and I\'ll write it up for you to mark.',
        spans=[span('Whatever the situation was, we will contrast it with the corrected version.')], found_by='me, and the independent reader')


# ---------------------------------------------------------------- repeats

def repeat_cards():
    k, l = q('helped me think through some of these ideas')[0], q('Key developed the Guide’s sense of direction')[0]
    nairobi = 'She led a guided inner-child meditation in Nairobi in January 2026 for twenty people, and it’s up on YouTube.'
    add(id='R1', type='repeat', advice='approve', title='Key\'s credit, three times, one inside Lisa Romano\'s paragraph',
        spans=[span('Key developed the Guide’s sense of direction, and the identity and differentiation work from Bowen I mentioned earlier.'),
               span(nairobi)],
        edits=[{'block': k, 'before': BL[k]['text'], 'after': BL[k]['text'] + ' ' + nairobi},
               {'block': l, 'before': BL[l]['text'], 'after': replace_in(l, [(' Key developed the Guide’s sense of direction, and the identity and differentiation work from Bowen I mentioned earlier. ' + nairobi, '')])}],
        what='"Key developed the Guide’s sense of direction, and the identity and differentiation work from Bowen I mentioned earlier." goes, and her Nairobi meditation sentence moves up to your new Key paragraph.',
        why='Your new Key paragraph says she added the Guide, and Practicing Differentiation credits her with differentiation from Bowen; in Lisa Romano\'s paragraph, "She led a guided inner-child meditation" reads as Lisa.',
        stays='Lisa Romano\'s two sentences, Key\'s paragraph, and the Nairobi meditation with its link.', deciding='Reject to keep the three credits.',
        found_by='me, and the independent reader')
    i = q('So warmth and safety come first for a while')[0]
    add(id='R2', type='repeat', advice='approve', title='Timing Is Individual says its first sentence again at the end',
        spans=[span('So warmth and safety come first for a while, and the direction can grow once there’s a clear little one in there to guide.')],
        edits=[{'block': i, 'before': BL[i]['text'], 'after': replace_in(i, [(' So warmth and safety come first for a while, and the direction can grow once there’s a clear little one in there to guide.', '')])}],
        what='The last sentence goes: "So warmth and safety come first for a while, and the direction can grow once there’s a clear little one in there to guide."',
        why='It is a "So..." summary of the paragraph\'s first sentence ("Most of us need enough Nurturer and Protector first"), and your new order line in Borrow One Competency at a Time already says safety, then love, then guidance. You cut summary lines like it all through your edit.',
        stays='The shepherd beating sheep, and the paragraph after.', deciding='Reject if you want "once there’s a clear little one in there to guide", the one thing it adds.',
        found_by='the independent reader')
    i = q('never problems at all from up there')[0]
    add(id='R3', type='repeat', advice='approve', title='"From that higher vantage point ... from up there"',
        spans=[span('from up there, and that can')],
        edits=[{'block': i, 'before': BL[i]['text'], 'after': replace_in(i, [('never problems at all from up there, and', 'never problems at all, and')])}],
        what='"from up there" goes from the end of the clause.', why='Your new start, "From that higher vantage point,", says where; the old end says it again.',
        stays='The sentence.', deciding='Reject to keep both.', found_by='me')
    a, b = q('Re-evaluation counseling always ends')[0], q('what century Pharao Tutankhamun')[0]
    rc = 'Re-evaluation counseling always ends on this “Present Time” reminder. Can be as simple and silly as “Oh, Today is Monday, my favorite day of the week!”'
    add(id='R4', type='repeat', advice='leave', title='Two silly present-time endings, photos and Close the Session',
        spans=[span(rc), span('remind yourself about something silly and obvious')],
        edits=[{'block': a, 'before': BL[a]['text'], 'after': replace_in(a, [(' ' + rc, '')])},
               {'block': b, 'before': BL[b]['text'], 'after': BL[b]['text'] + ' ' + rc}],
        what='The independent reader\'s idea: the Re-evaluation Counseling line and the Monday joke move from the photos section to Close the Session.',
        why='Both sections end on the same move, a silly obvious fact about the present.',
        stays='Every word.', deciding='Approve if you want the trim; I\'d leave both, since the photos one is about putting a photo away and you took out my line tying them together.',
        found_by='the independent reader')


# ---------------------------------------------------------------- worth a second look, and questions

def check_and_ask_cards():
    i = q('punishment hug. »')[0]
    t = BL[i]['text']
    old = '«\xa0punishment hug.\xa0» (which is called «\xa0therapeutic holding\xa0» in the literature) and I feel'
    add(id='C1', type='check', advice='approve', title='"Therapeutic holding" is a name for something contested',
        spans=[span('(which is called « therapeutic holding » in the literature)')],
        edits=[{'block': i, 'before': t, 'after': replace_in(i, [(old, '«\xa0punishment hug\xa0», and I feel')])}],
        what='"(which is called « therapeutic holding » in the literature)" comes out; your "punishment hug" and "time-in" stay.',
        why=('In the literature, therapeutic holding is mostly attachment therapy\'s practice of holding a child, sometimes until '
             'the child submits, and it is written about critically: the American Academy of Child and Adolescent Psychiatry piece "Is '
             'Therapeutic Holding Dead" (https://www.aacap.org/aacap/Member_Resources/Practice_Information/SR_Articles/Is_Therapeutic_Holding_Dead.aspx) '
             'opposes it on medical-risk grounds, and US accredited hospitals have restricted it to crisis control since 1999. A reader who '
             'looks it up finds that, not your loving time-in.'),
        stays='Your whole account of your dad, Bear and your sister.',
        deciding='Reject if you want the term in; then I\'d at least fix the punctuation ("« punishment hug » (which ... literature), and").',
        found_by='me, checked on the web')
    i = q('A crisis line counts, and the person on the other end can be a total stranger.')[0]
    add(id='C2', type='check', advice='approve', title='The crisis section lost when "the same" applies',
        spans=[span('A crisis line counts, and the person on the other end can be a total stranger.')],
        edits=[{'block': i, 'before': BL[i]['text'], 'after': replace_in(i, [('can be a total stranger.', 'can be a total stranger. ' + CRISIS)])}],
        what='One sentence from the last guide goes back: "%s"' % CRISIS,
        why=('You cut the paragraph\'s reassurance and caveats, which is right. This one is when the first instruction applies: someone '
             'who can\'t stop themselves, or is drunk or high, isn\'t always "about to act" by their own reading.'),
        stays='Your cuts of the rest ("Can’t tell if that’s you?", "None of that is me answering...", the closing lines).',
        deciding='Reject if you\'d rather keep the section as short as you made it.', found_by='me')
    add(id='A1', type='ask', advice='ask', title='"Another ex of mine (X)"',
        question=('The intro now says "another ex of mine (X)". Is the X a placeholder, her initial, or meant to stay? And is she '
                  'Xandria, who comes up in the shame section? I\'d take "(X)" out: she had panic attacks, and the last guide left her '
                  'unnamed on purpose so it wouldn\'t read as Key.'),
        why='"(X)" reads as a note to yourself.', advice_note='Take "(X)" out.', spans=[span('another ex of mine (X)')], found_by='me, and the independent reader')
    add(id='A2', type='ask', advice='ask', title='Lao Tsu and The Art of War',
        question=('"As Lao Tsu might have said (if I could ever have read that whole boring Art of War book)": The Art of War is Sun '
                  'Tzu\'s. Is the mix-up the joke? If not, I\'d say Sun Tzu.'),
        why='A reader who knows will take it as a slip, unless the joke makes it clear.', advice_note='Sun Tzu, unless it\'s the joke.',
        spans=[span('As Lao Tsu might have said')], found_by='me')
    add(id='A3', type='ask', advice='ask', title='"“What’s a ‘boundary’?”, I might be asking."',
        question='Did you mean "you might be asking" (the reader), the way "“What’s an ‘internal attack’?”" works two sections down? I\'d say "you".',
        why='As "I", it reads as if you didn\'t know what a boundary is.', advice_note='"you".',
        spans=[span('I might be asking')], found_by='me')
    add(id='A4', type='ask', advice='ask', title='"...so that you :" and then a heading',
        question=('Borrow the Adult To Become the Adult ends "Try to see the end goal as attainable right at the start here so that you :" '
                  'and the heading after it finishes the sentence ("Don’t Sell Your Inner Adult To Buy An Outer Adult"). I read it as '
                  'meant, and it works; the independent reader read it as a sentence cut off. Keep it? I\'d keep it.'),
        why='On Substack the heading is in big type, so some readers will take the colon as a broken sentence.', advice_note='Keep it.',
        spans=[span('so that you :')], found_by='the independent reader')
    add(id='A5', type='ask', advice='ask', title='"What century ... (1332 BCE)"',
        question='"what century Pharao Tutankhamun was crowned (1332 BCE in case you forgot!)": 1332 BCE is a year. "What year"? I\'d say year.',
        why='The joke lands better when the answer matches the question.', advice_note='"what year".',
        spans=[span('what century Pharao Tutankhamun was crowned')], found_by='me')
    add(id='A6', type='ask', advice='ask', title='The larger cuts: all meant?',
        question=('Besides the ones with their own cards (the dog paragraph, the four pairs, Hear the Guard First), these went whole: '
                  'Instead of Blame with its six questions (it was in Love Can Start Before It’s Trusted); Just Like Me, with tonglen; '
                  'the Ideal Parent Figure pilot study; "If a part hesitates about being touched or about sex"; When your kind words '
                  'sound empty and If the relief doesn\'t last (When to Change the Strategy); the opener of When the Urge to Escape '
                  'Arrives (the drink, the ex, the new business); the fever-and-kitchen and "hello??" examples in Between Spoiling and '
                  'Clamping Down; the "no self" and "resistance" paragraph and the love-bombing lines in Don\'t Sell Your Inner Adult; '
                  'and in the IFS appendix "Can\'t find a calm, compassionate Self in there? Then borrow." and "The inner Guide is the '
                  'closest thing here to a Higher Self". Were they all meant? I\'d assume so (nothing points at them), unless one '
                  'slipped out in the moving.'),
        why='Nothing in the guide points at these, so they read fine without them; this is only to catch one that slipped out, the way the dog paragraph and the four pairs did.',
        advice_note='If all were meant, just say so. Each one\'s words are in EDITS.md, at the end.',
        spans=[span('Between Spoiling and Clamping Down'), span('When to Change the Strategy'), span('Love Can Start Before It’s Trusted')],
        found_by='the sentence comparison (EDITS.md)')


def main():
    links_cards()
    pointer_cards()
    repeat_cards()
    check_and_ask_cards()
    format_cards()
    typo_cards()
    quotes_card()
    # the page template colours eight type keys (suggestion_review_template.html, .t-reread to .t-ask): mine take theirs
    keymap = {'links': 'caveat', 'pointer': 'structure', 'repeat': 'repeat', 'check': 'innerchild', 'format': 'cut',
              'typo': 'typo', 'ask': 'ask'}
    types = {keymap[k]: v for k, v in TYPES.items()}
    for x in S:
        x['type'] = keymap[x['type']]
    review = {
        'format': sr.FORMAT, 'review_id': 'inner-child-t116-joel-guide', 'title': 'Your reorganized guide, marked',
        'intro': [
            ('This is your reorganized guide (the file you sent tonight), with everything I\'d change before you publish marked in place. '
             'The biggest thing is the links and pictures: the Word file I sent you last time had none, so yours lost them. '
             'The rest is small: pointers your moves left pointing the wrong way, a few repeats, typos, and questions.'),
            ('Approve, Reject or Revise each card; questions have an answer box. Your answers save as you click. When you\'re done, tell '
             'me in the chat. I put the approved ones into your text and make the Substack draft with the links and pictures in.'),
            ('Six cards put a few words of mine into your sentences (the two pointers and the four "that X" fixes); each passed the '
             'owner-delivery gate with three independent readers. Everything else is a cut, a move, your own words put back, a typo '
             'or a question. What I learned from your edits is in LESSONS.md (%s).' % (BLOB + 't116-joel/LESSONS.md')),
        ],
        'git_file': 'articles/inner-child-therapy/experiments/t116-review/REVIEW.html',
        'article': {'file': ARTICLE, 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'links': {'guide': BLOB + 't116-review/GUIDE-PAGE.md', 'review': BLOB + 't116-review/REVIEW.json'},
        'types': types, 'suggestions': S,
    }
    probs = sr.check(review, BL)
    if probs:
        sys.exit('\n'.join(probs))
    (HERE / 'REVIEW.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    counts = {}
    for s in S:
        counts[s['type']] = counts.get(s['type'], 0) + 1
    print('REVIEW.json', len(S), 'cards', counts, 'typos', len(TYPOS))


if __name__ == '__main__':
    main()
