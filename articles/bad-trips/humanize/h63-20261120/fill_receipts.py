#!/usr/bin/env python3
"""fill_receipts.py - the making-sense receipts of turn 55's tries (tools/humanization/sense_receipt.py), built on
turn 54's (../h62-20261120/fill_receipts.py, whose R entries are loaded here), with the three fresh reads of each draft
(reads/: each read the draft kept as reads/read-text-KEY.txt) and each marked line's fate.

  python3 fill_receipts.py [KEY...]      then sense_receipt.py check TEST-KEY.txt TEST-KEY.receipt.json
"""
import importlib.util, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
_spec = importlib.util.spec_from_file_location('fill62', HERE.parent / 'h62-20261120' / 'fill_receipts.py')
F62 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(F62)
import make_reads as M  # noqa: E402  (this folder's copy, so the reads are read from this folder's reads/)

NEED, HISF, FIT, ANSWER = F62.NEED, F62.HISF, F62.FIT, F62.ANSWER
R62 = F62.R


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

# d3, the ozone story's second try (B197), from the near miss c3-ozone-1 (4cf06939: Human Medium 17, Human Low 21,
# Human Low 6, AI Low 15 over the last line). One change a check (lesson 19b): the last line, which all three reads of c3
# marked as a summing-up the reader can do nothing with, now ends on what to do, joined with "so"; "address" said as
# "work on". 17% of the near miss's words.
ONE = ('kept for this check: lesson 19b and the ledger allow one change a check from the near miss (c3-ozone-1, '
       '4cf06939), spent on the last line, the one AI window; ')
R['d3-ozone-2'] = dict(R62['c3-ozone-1'])
R['d3-ozone-2']['pay'] = list(R62['c3-ozone-1']['pay'])
R['d3-ozone-2']['pay'][4] = (
    'they know DMSO and the water work on different kinds of overload, so when one doesn\'t help they try the other',
    'what the one case suggests beyond itself, and what to do with it, after the advice', 'The mistake')
R['d3-ozone-2']['keep_need'] = {}
R['d3-ozone-2']['keep_his'] = {
    2: ONE + '"It" is the smelling just named and "the experience" the trip, the same either way; naming the ozone ("The '
             'ozone made the trip stronger") is the change for a Low window still below High after this check',
    3: ONE + 'the water is the section\'s subject, explained under its heading; "that situation" is the alarm just '
             'described; what each did, said separately, is a later check\'s change',
    4: ONE + 'the advice the story leads to; tying it to the line before ("So after that ...") is a later check\'s '
             'change if its Low window stays',
    5: ('the line this check changes: it now ends on what to do ("so if one doesn\'t help, try the other"); which kind of '
        'overload each fits isn\'t known yet (his DMSO lines: "I don\'t yet know why"), and "The mistake" says it comes '
        'from his one case; putting the advice first is the next check\'s change if the line stays below High')}
R['d3-ozone-2']['keep_fit'] = {
    5: ('how long to give one before trying the other isn\'t said, and he hasn\'t said; S3 says the water helped fast, '
        'which is what the reader has; kept for this check, one change from the near miss')}
R['d3-ozone-2']['questions'] = dict(R62['c3-ozone-1']['questions'],
    Q2=('PASS: the instructions ("I don\'t recommend inhaling ozone", "if one doesn\'t help, try the other") say what to '
        'do, in the reader\'s terms'),
    Q9=('PASS: one change this check, the last line (lesson 19b): its use joined to it with "so", "address" said as '
        '"work on"'))


# e3, the ozone story's third try, from d3 (7794e2d9: Human Written, Human High 44 over the story, Human Medium 25 over the
# last line). One change: in the last line, "aged ozonated-charcoal water" said as "the water", since the line before has
# just named it (the long name twice in a row reads like a model's); 3% of d3's words.
ONE3 = ('kept for this check: lesson 19b and the ledger allow one change a check from the near miss (d3-ozone-2, '
        '7794e2d9, Human High 44 over the first four sentences), spent on the last line, the one window below High; ')
R['e3-ozone-3'] = dict(R['d3-ozone-2'])
R['e3-ozone-3']['keep_his'] = {
    2: ONE3 + '"It" is the smelling just named and "the experience" the trip; what the alarm felt like is his to say, and '
             'the sentence read Human High in d3',
    3: ONE3 + '"that situation" is the alarm just described; the water is the section\'s subject, explained under its heading',
    4: ONE3 + 'the advice the story leads to, right after the story',
    5: ('the line this check changes ("the water" for the long name the line before has just used); it ends on what to do; '
        'which kind of overload each fits isn\'t known yet (his DMSO lines: "I don\'t yet know why"), and "The mistake" '
        'says it comes from his one case')}
R['e3-ozone-3']['keep_fit'] = {
    5: ('the line before says which helped after ozone (the water, fast, where DMSO didn\'t), so a reader in that case '
        'has the answer before this line; "if one doesn\'t help, try the other" is for the cases beyond this one; how long '
        'to give one first isn\'t said, and he hasn\'t said; kept for this check, one change from the near miss')}
R['e3-ozone-3']['keep_need'] = {}
R['e3-ozone-3']['questions'] = dict(R['d3-ozone-2']['questions'],
    Q3='PASS: "the water" is the aged ozonated-charcoal water the line before names; "that situation" is the alarm',
    Q9='PASS: one change this check, "the water" for the long name in the last line (lesson 19b)')


# f3, the ozone story's fourth try, from d3 again (7794e2d9, the lineage's best: Human High 44, Human Medium 25 over the
# last line); e3's "the water" for the long name read worse (71fcaf75: the last line Human Low 23), so the long name stays.
# One change: the last line's "if one doesn't help, try the other" said with the remedies named, "if DMSO doesn't help,
# try the water, and the other way around", as the read against his fixes asked (which one, and the payoff concrete) and
# the fit read of e3 asked (a reader could start with DMSO); 10% of d3's words.
ONE4 = ('kept for this check: lesson 19b and the ledger allow one change a check from the near miss (d3-ozone-2, '
        '7794e2d9, Human High 44 over the first four sentences), spent on the last line, the one window below High; ')
R['f3-ozone-4'] = dict(R['d3-ozone-2'])
R['f3-ozone-4']['pay'] = list(R['d3-ozone-2']['pay'])
R['f3-ozone-4']['pay'][4] = (
    'they know that if DMSO doesn\'t help they try the water, and if the water doesn\'t, DMSO, since the two work on '
    'different kinds of overload', 'what the one case suggests beyond itself, and what to do with it, after the advice',
    'The mistake')
R['f3-ozone-4']['keep_his'] = {
    2: ONE4 + '"It" is the smelling just named and "the experience" the trip; what the alarm felt like is his to say',
    3: ONE4 + '"that situation" is the alarm just described; the water is the section\'s subject, explained under its heading',
    4: ONE4 + 'the advice the story leads to, right after the story',
    5: ('the line this check changes: it names which to try ("if DMSO doesn\'t help, try the water, and the other way '
        'around"); which kind of overload each fits isn\'t known yet (his DMSO lines: "I don\'t yet know why"), and "The '
        'mistake" says it comes from his one case')}
R['f3-ozone-4']['keep_fit'] = {
    5: ('the line before says which helped after ozone (the water, fast, where DMSO didn\'t), and this line now names '
        'both ways round; how long to give one first isn\'t said, and he hasn\'t said; kept for this check, one change '
        'from the near miss')}
R['f3-ozone-4']['keep_need'] = {}
R['f3-ozone-4']['questions'] = dict(R['d3-ozone-2']['questions'],
    Q3='PASS: the remedies named in the advice ("if DMSO doesn\'t help, try the water"); "that situation" is the alarm',
    Q9='PASS: one change this check, the advice with the remedies named (lesson 19b)')


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
