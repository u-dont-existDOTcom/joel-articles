#!/usr/bin/env python3
"""fill_receipts.py - the making-sense receipts of turn 54's C2 and C3 tries (tools/humanization/sense_receipt.py): his
answers to the contradictions check's questions C2 and C3 (chat, 2026-11-20 22:40 UTC: "C1 a C2a C3 a C4 a"), with the
three fresh reads (reads/: each read the draft kept as reads/read-text-KEY.txt) and each marked line's fate. C1 and C4 take
words out and add none, so they are checked as they will stand (--unchanged), with no receipt.

  python3 fill_receipts.py [KEY...]      then sense_receipt.py check TEST-KEY.txt TEST-KEY.receipt.json
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_reads as M  # noqa: E402

NEED = ('a fresh agent (Sonnet) given tools/humanization/needed_read_brief.md with only the text, its heading and what it is '
        'for (reads/need-%s.txt; the draft it read: reads/read-text-%s.txt)')
HISF = ('a fresh agent (Sonnet) given tools/humanization/his_fixes_brief.md, the twelve ways, with the text one sentence a '
        'line (reads/his-%s.txt; the draft it read: reads/read-text-%s.txt)')
FIT = ('a fresh agent (Sonnet) given tools/humanization/fit_read_brief.md, the universal version (reads/fit-%s.txt; the '
       'draft it read: reads/read-text-%s.txt)')
ANSWER = 'his answer in chat, 2026-11-20 22:40 UTC ("C1 a C2a C3 a C4 a")'


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
            if found:
                fit.append({'s': S(int(m.group(1))), 'found': ', '.join(found), 'n': int(m.group(1))})
    need = []
    t = (HERE / 'reads' / ('need-%s.txt' % key)).read_text(encoding='utf-8')
    for line in t.split('UNNEEDED:', 1)[-1].splitlines():
        m = re.match(r'\s*-\s*S(\d+):', line)
        if m:
            need.append((int(m.group(1)), S(int(m.group(1)))))
    return his, fit, need


R = {}

# C2 (his answer a): No Rash Actions' lock line, as the pair the apply gate checks (the line, under 50 words, with its
# neighbour, his list of don'ts). The reads read the stretch with his answer's words, "Put yourself on an action lock:
# nothing big until you've slept and eaten, and nothing life-changing for 24-72 hours." (S3 of the stretch); the read
# against his fixes marked it as two limits packed in one sentence (way 1) and his list after it as restating its
# "until you've slept and eaten" as if new (way 12). His list already holds the sleep-and-eat clock, so the line keeps
# only the longer one: both clocks stay in the passage, each said once (what his answer a was for).
OWN_B318 = ('his own words (his round-23 version of the list of don\'ts, card TEACH-DONTS, Pangram e1537940, Human High '
            'alone, as he sent it; OWNER-EDITS r23-teach-donts), not part of this change')
R['c2-lock-1'] = {
    'section': 'No Rash Actions: Visions Are Not Commands',
    'reader': ('someone on a trip, or the friend with them, who is sure something has to be done tonight (quit a job, tell '
               'the family everything, send the message) and is reading whether to'),
    'pay': [('they hold off on anything life-changing (quitting, breaking up, confessing everything) for one to three days, '
             'however sure they feel tonight', 'the paragraph before says the urgency is part of the state and acting on it '
                                                'isn\'t safe; this is what to do instead, the rule and how long it lasts',
             None)],
    'placement': ('in place of "Put yourself on a 24-72 hour action lock." (B317), right after No Rash Actions\' opening '
                  'paragraph (B316: the urgency is part of the state, and acting on it isn\'t safe) and before his list of '
                  'what waits until they\'ve slept and eaten (B318); the line says the longer clock, his list the shorter '
                  '(his C2 answer a: two clocks, each where it belongs)'),
    'why_reading': ('it tells someone sure they must act tonight the rule for their case: nothing life-changing, and for how '
                    'long'),
    'same_point': ('none: read the section from its heading to the next for the points (the urgency is the state; the lock; '
                   'his list of what waits until they\'ve slept and eaten; writing it down and going over it with one '
                   'grounded person); the sleep-and-eat clock is his list\'s, so the line says only the 24-72 hours, and '
                   'the night\'s lines elsewhere (tomorrow\'s notebook, the anchor script, the triage app) keep tomorrow or '
                   'morning'),
    'keep_need': {},
    'keep_his': {
        4: OWN_B318 + '; its other mark, restating the lock line\'s "until you\'ve slept and eaten" as if new, is answered '
                      'in the lock line, which no longer says it',
        5: OWN_B318 + '; his examples of what to think twice about, in his voice',
        6: OWN_B318 + '; "change your mind" is about the conclusions it names (enlightened, damaged, the universe '
                      'explained), and the acts are held by the lock line'},
    'keep_fit': {
        4: OWN_B318 + '; the lock line before it is the firm rule, and his "maybe" is his voice on the examples',
        5: OWN_B318 + '; quitting and confessing are life-changing, which the lock line now holds for 24-72 hours, so '
                      'they aren\'t exempt',
        6: OWN_B318 + '; it is about the conclusions (permanently enlightened or damaged), not the acts, which the lock '
                      'line holds'},
    'questions': {
        'Q1': ('PASS: the rule first ("Put yourself on an action lock"), then what it holds and for how long; his list '
               'after it says what waits until they\'ve slept and eaten'),
        'Q2': ('PASS: something the reader does ("Put yourself on"), for what the paragraph before says: acting on the '
               'state\'s urgency isn\'t safe'),
        'Q3': ('PASS: "nothing life-changing", with his list after it naming the things (quit your job, break up, confess '
               'everything); "24-72 hours" says how long'),
        'Q4': 'PASS: "action lock" said by what it holds ("nothing life-changing for 24-72 hours")',
        'Q5': ('PASS: the lock follows the paragraph before (acting on the urgency isn\'t safe), and his list follows the '
               'lock with the shorter clock ("Until you have slept and eaten")'),
        'Q6': 'PASS: the rule, then the examples; the longer clock in the rule, the shorter in his list',
        'Q7': 'PASS: for someone sure they must act tonight, how long to wait is their case',
        'Q8': 'N/A: no group of mine in the text; the list is his',
        'Q9': ('PASS: one clock in the line; his answer\'s "nothing big until you\'ve slept and eaten" is left to his list, '
               'which already says it (the read against his fixes marked the two limits packed in one line, and his list '
               'restating the first)')},
}

# C3 (his answer a): the ozone story with "suggested" for "showed me", so one case suggests what his DMSO lines leave
# open ("I don't yet know why"). One word changed; the paragraph's other lines are as the guide has had them since the
# published original.
ONE_WORD = ('not part of this change: ' + ANSWER + ' changes one word of the last sentence; the paragraph\'s own '
            'humanizing is a later lineage of its own')
R['c3-ozone-1'] = {
    'section': 'Shungite, Aged Ozonated-Charcoal Water, or Boiled Charcoal Water',
    'reader': ('the friend of someone whose trip turned more intense near ozone, with DMSO and the aged ozonated-charcoal '
               'water at hand, reading which to use and what not to do'),
    'pay': [
        ('they learn the mistake to avoid from the writer\'s own experience: smelling ozone gas directly on a trip',
         'the paragraph before says no ozone gas was present when the water calmed a crying baby; this is what the gas '
         'itself did, on a trip', None),
        ('they know what it costs: the ozone made the trip stronger and frightening', 'what the mistake did, right after it',
         'It intensified'),
        ('they know that after ozone made a trip alarming, the aged ozonated-charcoal water helped fast where DMSO didn\'t, '
         'so they reach for the water', 'after what the mistake did, what was tried for it and what helped',
         'that situation'),
        ('they don\'t inhale ozone, or let their friend', 'the advice the story leads to, after it',
         'none: the advice the story leads to, said plainly right after it'),
        ('they know DMSO and the water aren\'t interchangeable, so when one doesn\'t help they try the other',
         'what the one case suggests beyond itself, after the advice', 'The mistake')],
    'placement': ('B197, in Shungite, Aged Ozonated-Charcoal Water, or Boiled Charcoal Water, after the paragraph saying no '
                  'ozone gas was present when the water calmed a crying baby (B196) and before what to do without an '
                  'ozone-water purifier (B198); one word changed (his C3 answer a)'),
    'why_reading': ('it tells a friend whose trip turned alarming near ozone that the writer made the same mistake, so what '
                    'follows is what helped and what to avoid'),
    'same_point': ('none: read the section from its heading to the next for the points (what the water feels like, the '
                   'crying baby, the ozone mistake, boiled charcoal water without a purifier); the DMSO lines ("Sometimes '
                   'DMSO works better, and sometimes the water wins. I don\'t yet know why") are in another section, and '
                   '"suggested" makes this line agree with them (C3)'),
    'keep_need': {5: ('they know DMSO and the water aren\'t interchangeable, so when one doesn\'t help they try the other (his '
                      'DMSO lines say the same: sometimes DMSO works better, sometimes the water wins); kept as ' + ANSWER +
                      ', the line with "suggested" for "showed me"; the reads\' point that it gives no kinds goes to him')},
    'keep_his': {
        2: ONE_WORD + '; "It" is the smelling just named and "the experience" the psychedelic state, the same either way',
        3: ONE_WORD + '; "that situation" ties it to the alarm before it',
        5: ('kept as ' + ANSWER + ': the line with "suggested" for "showed me"; whether it goes, since the reads found no '
            'use for it beyond what his DMSO lines say, is his call, asked in this turn\'s reply')},
    'keep_fit': {5: ('kept as ' + ANSWER + ': it can\'t say which kinds, because he doesn\'t know yet (his DMSO lines: "I don\'t '
                     'yet know why"), which is why "suggested" replaces "showed me"; whether it goes is his call, asked in '
                     'this turn\'s reply')},
    'questions': {
        'Q1': 'PASS: the mistake first, then what it did, what helped, the advice, what it suggests',
        'Q2': 'PASS: the one instruction ("I don\'t recommend inhaling ozone") says what not to do, in the reader\'s terms',
        'Q3': ('PASS: "ozone gas", "DMSO", "aged ozonated-charcoal water" named; "that situation" is the alarm just '
               'described'),
        'Q4': ('PASS: DMSO and the water are the guide\'s remedies, each explained in its own section; no new term here'),
        'Q5': 'PASS: the mistake, what it did, what helped it, the advice, what it suggests: each from the one before',
        'Q6': 'PASS: the story in the order it happened, then the advice, then what it suggests',
        'Q7': 'PASS: for a friend whose trip got worse near ozone, which remedy helped is their case',
        'Q8': 'N/A: no groups or lists in the paragraph',
        'Q9': 'PASS: one step a sentence; one word changed this check (his C3 answer a)'},
}


def fill(key):
    r = R[key]
    p = HERE / ('TEST-%s.receipt.json' % key)
    d = json.loads(p.read_text(encoding='utf-8'))
    d['section'], d['reader'] = r['section'], r['reader']
    mine = [s for s in d['sentences'] if not s.get('his')]
    assert len(mine) == len(r['pay']), (key, len(mine), len(r['pay']))
    for s, (pay, fol, link) in zip(mine, r['pay']):
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
