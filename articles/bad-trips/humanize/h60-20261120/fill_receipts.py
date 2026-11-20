#!/usr/bin/env python3
"""fill_receipts.py - the making-sense receipts of turn 52's tries (tools/humanization/sense_receipt.py), built as h59's
(its R entries for the lineages are loaded from ../h59-20261120/fill_receipts.py), with the three fresh reads (reads/: each
read the draft kept as reads/read-text-KEY.txt, the try before the reads' fixes) and each marked line's fate.

  python3 fill_receipts.py [KEY...]      then sense_receipt.py check TEST-KEY.txt TEST-KEY.receipt.json
"""
import importlib.util, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
_spec = importlib.util.spec_from_file_location('fill59', HERE.parent / 'h59-20261120' / 'fill_receipts.py')
F59 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(F59)
import make_reads as M  # noqa: E402  (this folder's copy, so the reads are read from this folder's reads/)

NEED, HISF, FIT = F59.NEED, F59.HISF, F59.FIT
R59 = F59.R


def read_sents(key):
    return M.sentences((HERE / 'reads' / ('read-text-%s.txt' % key)).read_text(encoding='utf-8').strip())


def parse(key):
    import re
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

# Try 5 (h60e). e01 from d01, within 20% of c01 (166c0ee5, the lineage's best near miss): the AI High window over the
# two mistakes (37 words in b01, c01 and d01) had the arguing sentence changed twice; its other half, the panel's "hedged,
# tidy twist" ("they might hear it as permission", permission to do what?), was never changed, so this check changes it.
R['e01-harm-1'] = dict(R59['d01-harm-1'])
R['e01-harm-1']['pay'] = list(R59['d01-harm-1']['pay'])
R['e01-harm-1']['pay'][3] = (
    'they know not to nod along either, since the friend might think they\'re okay with them hurting someone',
    'the other mistake, the opposite of arguing', 'And if you nod along')
R['e01-harm-1']['keep_his'] = {2: (
    'kept for this check: "the lines below" are the script directly under this paragraph in the guide ("Non-combative '
    'philosophical grounding"), which the reader reads next, and "them" can only be the friend who would be led back; '
    'lesson 19b and the ledger allow one change a check from the near miss (c01, 166c0ee5; this try is at 19% of it), '
    'spent on the untested half of the AI High window; naming the belief and the script ("the script below", what "God is '
    'in everyone" leads to) is the next check\'s change if this one leaves S2 below High')}
R['e01-harm-1']['keep_fit'] = {2: (
    'kept for this check, as the read against his fixes\' mark: in the guide the lines are in front of the reader, '
    'directly under this paragraph, where the script turns "God is in everyone" into "every body sacred"; the read saw the '
    'paragraph alone; saying what the belief leads to is the next check\'s change')}
R['e01-harm-1']['questions'] = dict(R59['d01-harm-1']['questions'],
    Q3=('PASS: "they might think you\'re okay with them doing it" says what nodding along tells the friend (the panel on '
        'b01: "they might hear it as permission" a hedged, tidy twist; permission to do what?); "doing it" is the hurting '
        'just named'),
    Q9='PASS: the two mistakes in two sentences; one change this check, the last sentence\'s tail (lesson 19b)')

# e02 from c02 (0f63c962, AI Low over every window, no Human window): the five "if" sentences of c02 built differently
# (his way 2), then the reads' marks fixed: "In that state ... too much" named, "say it" said as "tell you to stop",
# "whatever they say" as "even if they ask you to".
R['e02-touch-1'] = dict(R59['c02-touch-1'])
R['e02-touch-1']['pay'] = [
    ('they ask before any touch, even their hand on the friend\'s heart, and have the words to ask with', 'the heading '
     'names touch and consent; the section before was a hand on your own heart', None),
    ('they know even a hug, the comfort they were about to give, can be too much for a friend already overwhelmed',
     'why the asking matters, after the asking', 'Even a hug'),
    ('they know holding the friend down can make them feel attacked and fight', 'the worse case, after the hug', 'And if'),
    ('if the friend wants space, they sit about six feet away and talk only if the friend wants to', 'the other answer to '
     'the question ("or would you rather have space?")', "If they'd rather have space"),
    ('they stop when the friend says stop', 'after asking, when to stop', 'none: a new step, after the asking and its '
     'answers'),
    ('they know pulling away or freezing means stop too, since the friend may be too overwhelmed to tell them to stop',
     'the stop without words, after the spoken one', 'means stop too'),
    ('they ask again whenever they can\'t tell what the friend wants', 'what to do between yes and stop', 'Ask again'),
    ('they look at their own reasons, and hold off when the touch is mostly to calm themselves', 'the last check, on the '
     'helper', 'none: the turn from the friend to the helper, said as an instruction to the helper'),
    ('they never touch the friend in a sexual way, even if the friend asks them to', 'the other thing the check can find, '
     'the one with no exception', 'even if they ask you to')]
R['e02-touch-1']['keep_need'] = {3: (
    'reworded, not cut: the reader\'s moment is wanting to comfort the friend "maybe with a hug", and asking (S1) covers '
    'touch in general; this line says the hug they were about to give can be too much for someone already overwhelmed, so '
    'they ask before that too; said now with the state named, as the read against his fixes asked ("Even a hug can be too '
    'much when they\'re already overwhelmed.")')}
R['e02-touch-1']['questions'] = dict(R59['c02-touch-1']['questions'],
    Q3=('PASS: "when they\'re already overwhelmed" names the state ("In that state" read vague); "to tell you to stop" '
        'names what they can\'t say ("say it" could be stop or the overwhelm); "even if they ask you to" names what they '
        'might say ("whatever they say")'),
    Q9=('PASS: the five "if" sentences of c02 built differently (his way 2): "means stop too", "Ask again whenever", '
        '"and hold off if"; the motive check and what it finds joined, one thought'))

# e03 from d03 (bcf53335; within 40% of it, with c03 and d03 two small tries checked from b03, the lineage's best near
# miss by likelihood): the third sentence's packed "with the lights turned down and a doctor if they need one" said as
# its own clauses, as both reads against his fixes asked (h59's of d03 and this one), the change h59 named as next.
R['e03-demons-4'] = dict(R59['d03-demons-4'])
R['e03-demons-4']['pay'] = [
    R59['d03-demons-4']['pay'][0], R59['d03-demons-4']['pay'][1],
    ('they know when to set the advice aside: someone too sick or too scared to think straight to send love gets steady '
     'first', 'the limit, after the advice it limits', "If someone's too overwhelmed"),
    ('they know what getting steady takes: the lights turned down, and a doctor if the friend needs one', 'what "get '
     'steady" means here, right after it', 'Turn the lights down'),
    ('they leave the talk about demons until the person can think straight again', 'what waits while they get steady, '
     'and until when ("think straight" again, as in the sentence before)', 'until they can think straight again')]
R['e03-demons-4']['keep_his'] = {1: R59['b03-demons-4']['keep_his'][1]}
R['e03-demons-4']['keep_fit'] = {2: (
    'kept: this sentence read Human High in c03 and d03 (54624d11, bcf53335), and the worry the read names ("I\'m afraid, '
    'so it has already hooked me") is answered where the reader meets it: the paragraph before says almost nobody can love '
    'what terrifies them while terrified, so train before you need it, and the next sentence says what to do when someone '
    'is too scared to send love')}
R['e03-demons-4']['questions'] = dict(R59['d03-demons-4']['questions'],
    Q9=('PASS: the third sentence\'s "with the lights turned down and a doctor if they need one" said as its own clauses '
        '("Turn the lights down, and get them a doctor if they need one."), as the reads against his fixes asked of d03 '
        'and of this draft (way 1); the draft the reads saw had a new last sentence too, which goes back to d03\'s so this '
        'check changes one thing (lesson 19b)'))
R['e03-demons-4']['checked'] = []


# Try 6 of harm and demons, try 5 of touch (h60f).
# f01: the last try of the harm lineage. c01's two small tries (d01, e01) left the AI High window over the two mistakes
# as it was (37 to 41 words), so this try fixes what the reads and the panel marked at once: S2's unnamed belief and lines
# (both reads of e01), the arguing sentence's parenthesis and pair build (the panel on b01), with the first sentence,
# Human Medium three times, as it is.
R['f01-harm-1'] = dict(R['e01-harm-1'])
R['f01-harm-1']['pay'] = [
    R59['d01-harm-1']['pay'][0],
    ('they know what to do with it: to lead the friend back to not hurting anyone, start from the friend\'s own belief, '
     'the way the script below does: God is in everyone, so every body is sacred', 'after what it means, what to do '
     'about it', 'To lead them back'),
    ('they know not to argue, since it can make the friend dig in to prove they\'re God, and which lines that means not '
     'saying', 'the first easy mistake, after the way to go', 'none: what not to do, which the reader expects after what '
     'to do'),
    ('they know what nodding along does: the friend might think they\'re okay with them hurting someone', 'the other '
     'mistake, the opposite of arguing', 'If you nod along')]
R['f01-harm-1']['keep_his'] = {}
R['f01-harm-1']['keep_fit'] = {}
R['f01-harm-1']['keep_need'] = {}
R['f01-harm-1']['questions'] = dict(R['e01-harm-1']['questions'],
    Q1=('PASS: the payoff first in each sentence: the sign; "To lead them back to not hurting anyone"; the arguing '
        'sentence leads with what arguing does, the lines not to say after it; what nodding along does'),
    Q3=('PASS: "the script below" for "the lines below", and what it says ("God is in everyone, so every body is '
        'sacred"), as both reads of e01 asked; "you\'re okay with them hurting someone" says what nodding along tells '
        'them; the read against his fixes on this draft marked "is no good either" (a contrast that only says what not '
        'to do): said as what nodding does'),
    Q9='PASS: the two mistakes in two sentences, each built its own way; the parenthesis of lines said in the sentence')

# f02 from e02 (043b2d5d, the lineage's first Human window; within 20% of it): the AI Medium window ("Ask again ... Be
# honest with yourself about why ..., and hold off if ...") said plainly: the motive check as a question the helper asks
# before touching, what it finds its own sentence; then the reads' mark on it fixed (name the two answers).
R['f02-touch-1'] = dict(R['e02-touch-1'])
R['f02-touch-1']['pay'] = list(R['e02-touch-1']['pay'][:7]) + [
    ('before touching, they ask themselves whether the touch is for the friend or for themselves', 'the last check, on '
     'the helper', 'none: the turn from the friend to the helper, said as an instruction to the helper'),
    ('they hold off when the touch is mostly to calm themselves', 'what the check can find, right after it',
     "If it's mostly"),
    R['e02-touch-1']['pay'][8]]
R['f02-touch-1']['keep_need'] = {}
R['f02-touch-1']['keep_his'] = {7: (
    'kept for this check: in place it follows "Stop as soon as they say stop", so the pulling away and freezing are the '
    'friend\'s; naming them ("If they pull away or freeze") brings back the "if" shape the check before took out (his '
    'way 2), and lesson 19b and the ledger allow one change a check from the near miss (e02, 043b2d5d), spent here on '
    'the AI Medium window')}
R['f02-touch-1']['keep_fit'] = {2: (
    'kept: the quote closes in the text ("... or would you rather have space?"); the read\'s copy, one sentence a line, '
    'dropped the closing mark (make_reads.py splits after the question mark), so the rest never sounded like words to '
    'say aloud in the text itself')}
R['f02-touch-1']['questions'] = dict(R['e02-touch-1']['questions'],
    Q3=('PASS: as e02, and the motive check names its two answers ("whether the touch is for them or for you"), as the '
        'read against his fixes on this draft asked of "who it\'s for"'),
    Q9=('PASS: e02\'s joined "Be honest with yourself about why you want to touch them, and hold off if it\'s mostly to '
        'calm yourself down" (AI Medium) said as the question the helper asks and what it can find, one step each'))

# f03 from e03 (d5484803, Human Written: Human High 70, Human Medium 10; the near miss, within 20% of it): only the last
# sentence, "Leave the demon talk until ...", where "the demon talk" could be any talk of demons or the advice to send
# the demon love: said as what waits, which the three reads of e03's draft read without a mark.
R['f03-demons-4'] = dict(R['e03-demons-4'])
R['f03-demons-4']['pay'] = list(R['e03-demons-4']['pay'][:4]) + [
    ('they know when to teach the friend to send the demon love: once the friend can think straight again',
     'what waits while they get steady, and until when ("think straight" again, as in the sentence before)',
     'Once they can think straight again')]
R['f03-demons-4']['keep_his'] = {
    1: R59['b03-demons-4']['keep_his'][1],
    3: ('kept for this check: it read Human High in e03 (d5484803), and "get steady" is spelled out by the next sentence '
        '(the lights turned down, a doctor); lesson 19b and the ledger allow one change a check from the near miss '
        '(e03), and this check is at 18% of it, spent on the last sentence, the one window below High'),
    4: ('kept for this check: it read Human High in e03 (d5484803); its reason is the sentence before (too sick or too '
        'scared to think straight), and when someone needs a doctor is the guide\'s Call medics list, its own section; '
        'one change a check from the near miss, spent on the last sentence')}
R['f03-demons-4']['keep_fit'] = {4: (
    'kept for this check: it read Human High in e03 (d5484803); when someone needs a doctor is the guide\'s Call medics '
    'list, its own section, which the medical part sends readers to; one change a check from the near miss, spent on '
    'the last sentence')}
R['f03-demons-4']['keep_need'] = {}
R['f03-demons-4']['questions'] = dict(R['e03-demons-4']['questions'],
    Q3=('PASS: "the demon talk" (any talk of demons, or the advice to send the demon love?) said as what waits: '
        '"teach them to send the demon love"'),
    Q9='PASS: one change this check, the last sentence (lesson 19b); the rest as e03, Human High')


# g02, touch's last try (6 of 6), from f02 (df0baed1, the lineage's best near miss by likelihood; within 20% of it): the
# mark the read against his fixes made on f02 and e02 both, "Pulling away or freezing" with nobody's name on it, named.
R['g02-touch-1'] = dict(R['f02-touch-1'])
R['g02-touch-1']['pay'] = list(R['f02-touch-1']['pay'])
R['g02-touch-1']['pay'][5] = (
    'they know that if the friend pulls away or freezes, that means stop too, since the friend may be too overwhelmed to '
    'tell them to stop', 'the stop without words, after the spoken one', 'that means stop too')
R['g02-touch-1']['keep_his'] = {5: (
    'kept for this check: lesson 19b and the ledger allow one change a check from the near miss (f02, df0baed1), and '
    'this one names who pulls away (marked by the reads of e02 and f02, a word a reader could take two ways); "sit about '
    'six feet away and only talk if they want to" is one picture of giving space, said the same since c02, and splitting '
    'it is a compression fix, not a two-ways word')}
R['g02-touch-1']['keep_fit'] = {}
R['g02-touch-1']['keep_need'] = {}
R['g02-touch-1']['questions'] = dict(R['f02-touch-1']['questions'],
    Q3=('PASS: as f02, and "If they pull away or freeze, that means stop too" names whose pulling away it is and says '
        'what it means (his tenth way: "it means"), as the reads against his fixes on e02 and f02 asked'),
    Q9='PASS: one change this check (lesson 19b)')


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
