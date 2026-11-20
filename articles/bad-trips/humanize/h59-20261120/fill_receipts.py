#!/usr/bin/env python3
"""fill_receipts.py - (built as h58's) the making-sense receipts of turn 51's tries (tools/humanization/sense_receipt.py),
with the three fresh reads (reads/: each read the draft kept as reads/read-text-KEY.txt, the try before the reads' fixes)
and each marked line's fate.

  python3 fill_receipts.py [KEY...]      then sense_receipt.py check TEST-KEY.txt TEST-KEY.receipt.json
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_reads as M  # noqa: E402

NEED = ('a fresh agent (Sonnet) given tools/humanization/needed_read_brief.md with only the text, its heading and what it is '
        'for (reads/need-%s.txt; the draft it read: reads/read-text-%s.txt)')
HISF = ('a fresh agent (Sonnet) given tools/humanization/his_fixes_brief.md, the eleven ways, with the text one sentence a '
        'line (reads/his-%s.txt; the draft it read: reads/read-text-%s.txt)')
FIT = ('a fresh agent (Sonnet) given tools/humanization/fit_read_brief.md, the universal version (reads/fit-%s.txt; the '
       'draft it read: reads/read-text-%s.txt)')


def read_sents(key):
    return M.sentences((HERE / 'reads' / ('read-text-%s.txt' % key)).read_text(encoding='utf-8').strip())


def parse(key):
    rs = read_sents(key)
    S = lambda n: rs[n - 1]
    his = []
    for line in (HERE / 'reads' / ('his-%s.txt' % key)).read_text(encoding='utf-8').splitlines():
        m = re.match(r'\s*-\s*S(\d+):\s*([\d, ]+)\s*[—-]', line)
        if m:
            his.append({'s': S(int(m.group(1))), 'difference': m.group(2).strip(), 'n': int(m.group(1))})
    fit = []
    for line in (HERE / 'reads' / ('fit-%s.txt' % key)).read_text(encoding='utf-8').splitlines():
        m = re.match(r'\s*-\s*S(\d+):\s*(.*)$', line)
        if m:
            found = [q for q in ('ANYWAY', "CAN'T TELL", 'FROM', 'MISREAD') if re.search(re.escape(q) + r' yes', m.group(2))]
            fit.append({'s': S(int(m.group(1))), 'found': ', '.join(found), 'n': int(m.group(1))})
    need = []
    t = (HERE / 'reads' / ('need-%s.txt' % key)).read_text(encoding='utf-8')
    for line in t.split('UNNEEDED:', 1)[-1].splitlines():
        m = re.match(r'\s*-\s*S(\d+):', line)
        if m:
            need.append((int(m.group(1)), S(int(m.group(1)))))
    return his, fit, need


R = {}
R['b01-harm-1'] = dict(
    section='For the Person Helping: When What They Say Turns Toward Harm',
    reader=('someone sitting with a tripping friend who has just said something like "I am God, so I can kill", reading what '
            'to do right now, before the script that follows'),
    pay=[('they take the words as a sign someone could get hurt, not as talk to wave off', 'the heading names the case; '
          'this says what it means the moment they hear it', None),
         ('they know what to do with it: start from the friend\'s own belief and lead back to not hurting anyone, the way '
          'the script below does with "God is in everyone"', 'after what it means, what to do about it',
          'none: the next step, said as an instruction after the sign it answers'),
         ('they know not to argue ("No you\'re not") or nod along, and why: a fight over who\'s right, or what sounds like '
          'permission', 'the two easy mistakes, after the way to go', 'none: what not to do, which the reader expects after what to do; each mistake says what it can lead to')],
    placement=('first paragraph under "When What They Say Turns Toward Harm", before the script ("Non-combative '
               'philosophical grounding") and the lines after it, which "the lines below" points to'),
    why_reading='it names the moment they are in (a friend saying "I am God, so I can kill") and says what it means',
    same_point=('none: read the section from its heading to the next for how to take the statement and what not to '
                'do: the script after it gives the words to say, and "When talk of harm continues" says what to do when '
                'the script doesn\'t work; only this paragraph says how to take it and the two mistakes'),
    keep_need={}, keep_his={},
    keep_fit={},
    questions={'Q1': 'PASS: the sign it is first, then what to do, then the two mistakes with their reason',
               'Q2': 'PASS: take it as a sign, start from what they believe, lead them back; arguing and nodding along '
                     'each with what it can do',
               'Q3': 'PASS: "someone could get hurt", "God is in everyone", "a fight over who\'s right"',
               'Q4': 'PASS: no term a high-school graduate wouldn\'t know; "status fight" said as "a fight over who\'s right"',
               'Q5': 'PASS: the second sentence says what to do with the sign; the third turns to what not to do',
               'Q6': 'PASS: what it means, what to do, what not to do: the order a helper needs it in',
               'Q7': 'PASS: each sentence is about this friend saying this now',
               'Q8': 'PASS: one paragraph, one statement and how to answer it',
               'Q9': 'PASS: the old first sentence split in two, one step each (the read against his fixes, way 1)'})

R['b02-touch-1'] = dict(
    section='Touch, Consent, and Compassion',
    reader=('someone helping a friend through a hard trip who wants to comfort them, maybe with a hug or a hand on them, '
            'right after the guide suggested putting a hand on your own heart'),
    pay=[('they ask before any touch, even a hand on the heart the section before suggested, and have the words to ask '
          'with', 'the heading names touch and consent; the section before was a hand on your own heart', None),
         ('they know why to ask: a hug can be too much in that state, and holding someone down can feel like an attack',
          'why the asking matters, after the asking', 'none: the reason for the sentence before, said as what can happen'),
         ('they know they can help without touching at all: six feet away, silent', 'the other answer to the question '
          '("or would you rather have space?")', 'none: what to do if they choose space'),
         ('they stop at "stop", and also when the friend pulls away, freezes, or they can\'t tell', 'after asking, '
          'when to stop', 'none: a new step, after the ones before it'),
         ('they check their own reasons and hold off when the touch is mostly to calm themselves, or has anything sexual '
          'in it', 'the last check, on the helper', 'too')],
    placement=('the section after "Hand on Heart and Gratitude", which ends on putting a hand on your own heart; this '
               'paragraph turns to touching someone else, and the pair is the whole section'),
    why_reading='it tells someone about to touch a tripping friend to ask first, and gives them the question',
    same_point=('none: read the section from its heading to the next for asking before touch, when to stop and the '
                'helper\'s own reasons: the section is these two paragraphs, and the "Do" list of For the Person Helping '
                'asks "Closer or farther away?", not about touch'),
    keep_need={}, keep_his={},
    keep_fit={},
    questions={'Q1': 'PASS: each sentence opens on what to do or what can happen; the question to ask comes in the first',
               'Q2': 'PASS: ask, sit six feet away, stop, check your own reasons: all the helper\'s acts',
               'Q3': 'PASS: "a hand on their heart", "a hug", "holding them down", "six feet away"',
               'Q4': 'PASS: no term to explain',
               'Q5': 'PASS: the reason follows the asking; "If they say stop" follows the asking; "too" marks the last check',
               'Q6': 'PASS: ask, why, the no-touch answer, when to stop, the helper\'s own reasons',
               'Q7': 'PASS: each line is about touching this friend now',
               'Q8': 'PASS: all about touch and consent',
               'Q9': ('PASS: "nonsexual, consensual, and unrelated to the helper\'s needs" said as the helper checking their '
                      'own reasons; the list of five kinds of touch cut to the two that say why')})

R['b03-demons-4'] = dict(
    section='Demons, Jinn, Entities, and Shadow Forces',
    reader=('someone on a trip, or sitting with someone who is, facing what feels like a demon, who has just read that love '
            'is a better move than fighting it and to train sending love before they need it'),
    pay=[('they don\'t take sending love as giving up: it makes them unhookable', 'the paragraph before ends on practicing '
          'being the space rather than the storm; this answers "isn\'t that passive?"', None),
         ('they know why love works: what feels like a demon has nothing to hook into, since its hooks catch only on '
          'things like hatred and fear', 'it says what "unhookable" means', 'since'),
         ('they know when to set it aside: someone sick or too scared to think gets steady first, lights down and a '
          'doctor if needed, and the demon talk waits', 'the limit, after the advice it limits', 'If someone\'s too '
          'overwhelmed')],
    placement=('the end of "Demons, Jinn, Entities, and Shadow Forces", after the paragraph on training to send love '
               '(B400), before "Abuse Memories"; "It" continues that paragraph\'s "Practice being the space rather than '
               'the storm"'),
    why_reading='it answers the worry the paragraph before raises: that meeting a demon with love is passive',
    same_point=('none: read the section from its heading to the next for why love works and when to set it aside: '
                'B399 and B400 say fighting feeds it and love is the better move, and only this paragraph says why love '
                'leaves it nothing to hook and when to stabilize first'),
    keep_need={}, keep_fit={},
    keep_his={1: ('kept as it is: his round-22 move, carried in these words by h28 and pinned as his (OWNER-EDITS '
                  'h28-unhookable); in the guide "It" follows B400\'s "Practice being the space rather than the storm", '
                  'so it is the sending of love, and the next sentence says what "unhookable" means')},
    questions={'Q1': 'PASS: unhookable first, then why, then when not to',
               'Q2': 'PASS: help them get steady first, lights down, a doctor if they need one, the philosophy later',
               'Q3': 'PASS: "the demon" named where "it" could have been the love (the read against his fixes, way 10)',
               'Q4': 'PASS: "unhookable" explained in the sentence after it ("nothing to hook into"), the pinned sentence '
                     'can\'t take it; "nondual demonology" said as "the demon philosophy"',
               'Q5': 'PASS: "since" says why love leaves nothing to hook; "If someone\'s too overwhelmed" is the limit',
               'Q6': 'PASS: the worry, the reason, the limit',
               'Q7': 'PASS: each sentence bears on meeting what feels like a demon now',
               'Q8': 'PASS: one picture (hooks), two of the original four examples, as the needed read asked',
               'Q9': 'PASS: "medically, physically, or psychologically" said as "sick or too scared to think straight"'})

R['b04-spirit-2'] = dict(
    section='Spiritual ≠ "Getting Your Ass Kicked"',
    reader=('someone who takes trips for spiritual growth, telling a spiritual answer that helps someone suffering from one '
            'that ignores them, right after the guide names spiritual bypassing and spiritual practice'),
    pay=[('they can recognise bypassing: a big spiritual line ("this is all karma", "everything is Love") said while the '
          'person shaking in the corner is ignored', 'the line before names the two, bypassing first', None),
         ('they know practice also says love is here, and acts on it by taking care of that person', 'the other of the '
          'two, set against the first by what it does', 'too'),
         ('they know what taking care means: dim the lights, clear away what they could get hurt on, call for help if '
          'it\'s more than they can handle', 'what "take care of that person" means, in steps', 'none: the steps of the '
          'care the sentence before names'),
         ('they stop pretending nothing\'s wrong, and remind the person that the feeling is allowed to move through',
          'the last part of practice, the one bypassing does the opposite of', 'also')],
    placement=('under "Spiritual ≠ "Getting Your Ass Kicked"", after "This is one side of the difference between spiritual '
               'bypassing and spiritual practice:", which these two paragraphs complete; "That is tripsitting, shadow '
               'work, and the path becoming practical." (B337) goes: a summing-up line the read against his fixes marks '
               '(way 6), whose point the steps now show'),
    why_reading='it gives the reader the first of the two the line before named, in a form they can recognise',
    same_point=('none: read the section from its heading to the next for what bypassing and practice each do: B333 '
                'says suffering alone fixes nobody and B334 names the two; only this pair says what each does when someone '
                'suffers ("The Other Bypass", the next section, is the opposite bypass)'),
    keep_need={}, keep_his={}, keep_fit={},
    questions={'Q1': 'PASS: each sentence opens on what bypassing or practice is or does',
               'Q2': 'PASS: dim the lights, clear away what they could get hurt on, call for help, stop pretending, '
                     'remind them: what the sitter does',
               'Q3': 'PASS: "that person" is the person shaking in the corner; "what they\'re feeling" names whose feeling',
               'Q4': 'PASS: "bypassing" defined in the sentence that uses it; "hold the experience" said as letting the '
                     'feeling move through',
               'Q5': 'PASS: "too" sets practice against bypassing; "We also" adds the last part',
               'Q6': 'PASS: bypassing, then practice, then its steps',
               'Q7': 'PASS: each step is something a sitter does for this person now',
               'Q8': 'PASS: the karma and Love lines are bypassing; the steps are practice',
               'Q9': 'PASS: the packed list split: the care in one sentence, the honesty in another'})


# Turn 51's second tries (h59c), after the tell panels (panel-b0N-*/PANEL.md): c01 and c03 from their near misses, a word
# or two a reader could take two ways; c02 a new wording (b02 read AI twice, no Human window).
R['c01-harm-1'] = dict(R['b01-harm-1'])
R['c01-harm-1']['pay'] = [
    ('they take the words as a sign their friend could really hurt someone', 'the heading names the case; this says what '
     'it means the moment they hear it', None),
    R['b01-harm-1']['pay'][1],
    ('they know not to argue ("No you\'re not"), since it can make the friend dig in to prove they\'re God, or nod along, '
     'since the friend might take it as their blessing', 'the two easy mistakes, after the way to go',
     'none: what not to do, which the reader expects after what to do; each mistake says what it can lead to')]
R['c01-harm-1']['questions'] = dict(R['b01-harm-1']['questions'], Q3='PASS: "they could really hurt someone" (the panel: '
    '"someone could get hurt" was vague about who), "God is in everyone", "dig in to prove they\'re God"')
R['c02-touch-1'] = dict(R['b02-touch-1'])
R['c02-touch-1']['pay'] = [
    R['b02-touch-1']['pay'][0],
    ('they know why to ask: a hug can be too much in that state, and holding them down can make them feel attacked and '
     'fight', 'why the asking matters, after the asking', 'In that state'),
    ('if the friend wants space, they sit about six feet away and talk only if the friend wants to', 'the other answer to '
     'the question ("or would you rather have space?")', "If they'd rather have space"),
    ('they stop at "stop", and also when the friend pulls away or freezes, since someone that overwhelmed may not manage '
     'to say it', 'after asking, when to stop', 'none: a new step, after the asking and its answers'),
    ('when they can\'t tell what the friend wants, they ask again', 'what to do between yes and stop', 'unclear'),
    ('they look at their own reasons before touching', 'the last check, on the helper', 'none: the turn from the friend '
     'to the helper, said as an instruction to the helper'),
    ('they hold off when the touch is mostly to calm themselves, and never touch with anything sexual in it', 'what to do '
     'with what the check finds', "If it's mostly")]
R['c02-touch-1']['questions'] = dict(R['b02-touch-1']['questions'],
    Q9='PASS: "nonsexual, consensual, and unrelated to the helper\'s needs" said as the helper\'s own reasons, one each; '
       '"seems unsure" said as asking again')
R['c03-demons-4'] = dict(R['b03-demons-4'])
R['c03-demons-4']['pay'] = [
    R['b03-demons-4']['pay'][0],
    ('they know why love works: what feels like a demon has nothing to hook into, since its hooks catch only on hatred '
     'and fear', 'it says what "unhookable" means', 'since'),
    ('they know when to set it aside: someone too sick or scared to send love gets steady first, lights down and a doctor '
     'if needed, and the demon talk waits until they can think again', 'the limit, after the advice it limits',
     "If someone's too overwhelmed")]
R['c03-demons-4']['questions'] = dict(R['b03-demons-4']['questions'],
    Q4='PASS: "unhookable" explained in the sentence after it; "reach love" said as "send love", the section\'s own words '
       '(B400: "sending love to a frightening image"); "nondual demonology" said as "the demon talk"')


# After the reads of the second tries: what each marked and what was done (reads/*-c0N-*.txt).
R['c01-harm-1']['pay'][2] = (
    'they know not to argue ("No you\'re not"), since it can make the friend dig in to prove they\'re God, or nod along, '
    'since the friend might hear it as permission', 'the two easy mistakes, after the way to go',
    'none: what not to do, which the reader expects after what to do; each mistake says what it can lead to')
R['c01-harm-1']['questions'] = dict(R['c01-harm-1']['questions'],
    Q3='PASS: "they could really hurt someone" (the panel: "someone could get hurt" was vague about who); "the lines below '
       'do by saying God is in everyone" (the read against his fixes: "when they say" could be the friend)',
    Q9=('PASS: one step a sentence in the first two; the read against his fixes marked the last as two ideas in one '
        'sentence (way 1): lesson 19b allows a word or two per check from a near miss (b01, 5daecc97), so its split is the '
        'next check\'s change if this one doesn\'t lift it'))
R['c02-touch-1']['pay'] = [
    ('they ask before any touch, even their hand on the friend\'s heart, and have the words to ask with', 'the heading '
     'names touch and consent; the section before was a hand on your own heart', None),
    ('they know a hug can be too much in that state', 'why the asking matters, after the asking', 'In that state'),
    ('they know holding the friend down can make them feel attacked and fight', 'the worse case, after the hug', 'And if'),
    ('if the friend wants space, they sit about six feet away and talk only if the friend wants to', 'the other answer to '
     'the question ("or would you rather have space?")', "If they'd rather have space"),
    ('they stop when the friend says stop', 'after asking, when to stop', 'none: a new step, after the asking and its '
     'answers'),
    ('they stop when the friend pulls away or freezes too, since the friend may be too overwhelmed to say stop',
     'the stop without words, after the spoken one', 'too'),
    ('when they can\'t tell what the friend wants, they ask again', 'what to do between yes and stop', 'unclear'),
    ('they look at their own reasons before touching', 'the last check, on the helper', 'none: the turn from the friend '
     'to the helper, said as an instruction to the helper'),
    ('they hold off when the touch is mostly to calm themselves', 'the first thing the check can find', "If it's mostly"),
    ('they never touch the friend in a sexual way, even if the friend seems to ask for it', 'the other thing the check '
     'can find, the one with no exception', 'whatever they say')]
R['c03-demons-4']['pay'] = [
    R['b03-demons-4']['pay'][0],
    ('they know why love works: what feels like a demon has nothing to hook into, since its hooks catch only on hatred '
     'and fear', 'it says what "unhookable" means', 'since'),
    ('they know when to set the advice aside: someone too sick or scared to send love gets steady first, lights down and a '
     'doctor if needed', 'the limit, after the advice it limits', "If someone's too overwhelmed"),
    ('they leave the talk about demons until the person can think again', 'what waits while they get steady, and until '
     'when', 'until they can think again')]
R['c03-demons-4']['keep_need'] = {1: (
    'they don\'t take sending love as giving up, which the paragraph before (train sending love, be the space rather than '
    'the storm) can sound like; and it is his move, pinned as his (OWNER-EDITS h28-unhookable), which a card would have '
    'to ask him to cut')}


# The third small tries (h59d), each from its best near miss: d01 from c01 (166c0ee5), d03 within 20% of b03 (84881428).
R['d01-harm-1'] = dict(R['c01-harm-1'])
R['d01-harm-1']['pay'] = [
    R['c01-harm-1']['pay'][0],
    ('they know what to do with it: to lead the friend back to not hurting anyone, start from the friend\'s own belief, the '
     'way the script below does with "God is in everyone"', 'after what it means, what to do about it', 'To lead them '
     'back'),
    ('they know not to argue ("No you\'re not"), since it can make the friend dig in to prove they\'re God',
     'the first easy mistake, after the way to go', 'none: what not to do, which the reader expects after what to do'),
    ('they know not to nod along either, since the friend might hear it as permission', 'the other mistake, the '
     'opposite of arguing', 'And if you nod along')]
R['d01-harm-1']['questions'] = dict(R['c01-harm-1']['questions'],
    Q1='PASS: the payoff first in the second sentence too ("To lead them back to not hurting anyone, start from what they '
       'believe", his Hunter fix, lesson 20c); the sign, what to do, the two mistakes',
    Q9='PASS: the two mistakes in two sentences, as the read against his fixes asked of c01')
R['d03-demons-4'] = dict(R['c03-demons-4'])
R['d03-demons-4']['pay'] = [
    R['c03-demons-4']['pay'][0], R['c03-demons-4']['pay'][1],
    ('they know when to set the advice aside: someone too sick or too scared to think straight gets steady first, with '
     'the lights turned down and a doctor if needed', 'the limit, after the advice it limits', "If someone's too "
     'overwhelmed'),
    ('they leave the talk about demons until the person can think straight again', 'what waits while they get steady, '
     'and until when ("think straight" again, as in the sentence before)', 'until they can think straight again')]
R['d03-demons-4']['keep_his'] = dict(R['b03-demons-4']['keep_his'])
R['d03-demons-4']['keep_his'][3] = (
    'kept for this check: lesson 19b allows a word or two per check from the near miss (b03, 84881428, within 20% of it '
    'by the ledger), and this check spends them on the hedge ("maybe" out), one word uncompressed ("the lights turned '
    'down") and the matching "think straight again"; the split into its own clauses is the next check\'s change')
R['d03-demons-4']['questions'] = dict(R['c03-demons-4']['questions'],
    Q9='PASS: "with the lights down" uncompressed to "with the lights turned down" (his "came along with it", lesson 20d); '
       'the split of the third sentence waits a check (lesson 19b)')


def fill(key):
    r = R[key]
    p = HERE / ('TEST-%s.receipt.json' % key)
    d = json.loads(p.read_text(encoding='utf-8'))
    d['section'], d['reader'] = r['section'], r['reader']
    assert len(d['sentences']) == len(r['pay']), (key, len(d['sentences']), len(r['pay']))
    for s, (pay, fol, link) in zip(d['sentences'], r['pay']):
        s['payoff'], s['follows'] = pay, fol
        if 'link' in s:
            s['link'] = link or 'none: a new step, which the reader expects after the one before'
    d['checked'] = r.get('checked', [])
    d['placement'] = r['placement']
    d['opens']['why_reading'] = r['why_reading']
    d['same_point'] = r['same_point']
    his, fit, need = parse(key)
    d['needed'] = {'reader': NEED % (key, key), 'unneeded': [s for n, s in need],
                   'kept': {s: r['keep_need'][n] for n, s in need if n in r['keep_need']}}
    d['his_fixes'] = {'reader': HISF % (key, key), 'marked': [{'s': m['s'], 'difference': m['difference']} for m in his],
                      'kept': {m['s']: r['keep_his'][m['n']] for m in his if m['n'] in r['keep_his']}}
    d['fit'] = {'reader': FIT % (key, key), 'marked': [{'s': m['s'], 'found': m['found']} for m in fit],
                'kept': {m['s']: r['keep_fit'][m['n']] for m in fit if m['n'] in r['keep_fit']}}
    d['questions'] = r['questions']
    p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    for k in sys.argv[1:] or list(R):
        fill(k)
        print('filled', k)
