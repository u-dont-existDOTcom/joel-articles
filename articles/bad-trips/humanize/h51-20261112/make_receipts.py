#!/usr/bin/env python3
"""make_receipts.py - the making-sense receipts for this folder's tests (gate E365), with the needed read (NEEDED.json),
the read against his fixes (HIS-FIXES.json, gate bad-trips-2026-11-12g) and the universal fit read (FIT.json, gates
bad-trips-2026-11-12j and k).

  python3 make_receipts.py KEY...
"""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
SR = REPO / 'tools/humanization/sense_receipt.py'
NEEDED = json.loads((HERE / 'NEEDED.json').read_text(encoding='utf-8'))
HISFIX = json.loads((HERE / 'HIS-FIXES.json').read_text(encoding='utf-8'))
FIT = json.loads((HERE / 'FIT.json').read_text(encoding='utf-8'))
HIS = 'none: his line (5e41c575, 19:44 UTC), the next one in his list'
HISR = 'none: his rescue paragraph (9320d4ec, 22:34 UTC), its next sentence'
READER = ('someone whose friend is having a seizure right now, deciding what to do while it lasts, when to call medics, and '
          'whether to give a rescue medicine they have')
HEADING = [('they know this part is for a seizure happening now', 'the heading', 'none: the section heading itself')]
FIRST = [
    ('they time the seizure and do the steps below while it lasts', 'his lead-in', 'none: the first sentence under its heading'),
    ('they move dangerous objects away, especially hard or sharp ones', 'his first step', HIS),
    ('they don\'t restrain the person, and put pillows under their head', 'his next step', HIS),
    ('they loosen tight clothing', 'his next step', HIS),
    ('they turn the person gently onto their side to help them breathe', 'his next step', HIS),
    ('they keep everything out of the person\'s mouth', 'his last step', HIS)]
CALL = [
    ('they know the lines below are when to call medics', 'his lead-in', 'Call medics if'),
    ('they call medics at once for a seizure after taking too much, or when they don\'t know how much was taken',
     'the overdose seizure, his point of 22:34 UTC', 'none: his list, its first line'),
    ('they call medics when a seizure on a normal dose goes past 5 minutes', 'the epilepsy rule, for the other seizures', HIS),
    ('they call medics when breathing gets slow and shallow', 'his next sign', HIS),
    ('they call medics when the lips turn blue or gray', 'his next sign', HIS),
    ('they call medics when the forehead feels very hot, not just sweaty', 'his heat sign, said with how to tell (22:34 UTC)', HIS),
    ('they call medics for a head injury, a broken bone or bleeding that won\'t stop', 'his last sign', HIS)]
EXPL = [
    ('they wait the 5 minutes only for a seizure on a normal dose', 'which seizure the 5 minutes is for',
     'none: the paragraph after the call list, on its second line'),
    ('they know someone prone to seizures can have one on a normal dose, since psychedelics lower the threshold',
     'why a seizure on a normal dose happens', 'Psychedelics can lower'),
    ('they know that seizure is most likely less dangerous than an overdose seizure', 'his comparison, why it gets the 5 minutes',
     'Their seizure')]
RESCUE = [
    ('they give an epilepsy rescue medicine, if the person has one, as its label instructs', 'his rescue paragraph',
     'If they have a rescue medicine'),
    ('they know these are benzodiazepines, as a spray, a gel or a shot, since pills can\'t be swallowed', 'his forms', HISR),
    ('they keep a close eye on breathing after giving it, more so after opioids or alcohol', 'his last sentence', HISR)]
QUESTIONS = {
    'Q1': 'PASS: the call list says its action first; the paragraph after it opens on which seizure the 5 minutes is for',
    'Q2': 'PASS: "Call medics if", "Waiting the 5 minutes is only for": the helper\'s acts',
    'Q3': 'PASS: "after taking too much", "on a normal dose", "Their forehead feels very hot (not just sweaty)"',
    'Q4': 'PASS: "the seizure threshold" said with who it matters for ("someone with epilepsy or who\'s otherwise prone to seizures")',
    'Q5': 'PASS: "so", "only for", "Their seizure" say each relation and whose seizure',
    'Q6': 'PASS: when to call, which seizure gets the 5 minutes, why, and how it compares',
    'Q7': 'PASS: each line bears on calling medics during a seizure',
    'Q8': 'PASS: the call list, then one paragraph on the 5 minutes',
    'Q9': 'PASS: one point a line or sentence'}
R = {
 'seize-c10': dict(mine=HEADING + FIRST + CALL + EXPL + RESCUE,
                   placement='Active Seizure, as a whole: his first aid, his call list with the two changes of 22:34 UTC, the paragraph on the 5 minutes, his rescue paragraph',
                   same_point=('none: read the section from its heading to What Else May Help for the call to medics; the Call medics '
                               'list at the top says the same seizure line, and now says it the same way')),
 'callp-c3': dict(mine=[(a, b, c if i else 'none: the list checked by itself') for i, (a, b, c) in enumerate(CALL)],
                  placement='Active Seizure, its call list (H49-SEIZE-CALL with B112), checked by itself for the gate',
                  same_point='none: read the section from its heading to What Else May Help for the call to medics'),
 'explone-c5': dict(mine=[(a, b, c if i else 'none: the paragraph checked by itself') for i, (a, b, c) in enumerate(EXPL)],
                    placement='Active Seizure, the paragraph on the 5 minutes, after the call list, checked by itself for the gate',
                    same_point='none: read the section from its heading to What Else May Help for the 5 minutes'),
}

CALL4 = list(CALL)
CALL4[5] = ('they call medics when they get dangerously hot, felt on the forehead, not just sweating',
            'his heat line, with how to tell (22:34 UTC)', HIS)
R['callp-c4'] = dict(R['callp-c3'], mine=[(a, b, c if i else 'none: the list checked by itself') for i, (a, b, c) in enumerate(CALL4)])
R['seize-c11'] = dict(R['seize-c10'], mine=HEADING + FIRST + CALL4 + EXPL + RESCUE)

CALL5 = list(CALL)
CALL5[5] = ('they call medics when the forehead, touched, is very hot, not just sweaty', 'his heat sign, with how to tell (22:34 UTC)', HIS)
R['callp-c5'] = dict(R['callp-c3'], mine=[(a, b, c if i else 'none: the list checked by itself') for i, (a, b, c) in enumerate(CALL5)])
R['seize-c12'] = dict(R['seize-c10'], mine=HEADING + FIRST + CALL5 + EXPL + RESCUE)

CALL6 = list(CALL)
CALL6[5] = ('they call medics when the person gets dangerously hot, not just sweating', 'his heat sign, as he wrote it', HIS)
R['callp-c6'] = dict(R['callp-c3'], mine=[(a, b, c if i else 'none: the list checked by itself') for i, (a, b, c) in enumerate(CALL6)])
R['seize-c13'] = dict(R['seize-c10'], mine=HEADING + FIRST + CALL6 + EXPL + RESCUE)


def fill(key):
    text = HERE / ('TEST-%s.txt' % key)
    out = HERE / ('TEST-%s.receipt.json' % key)
    d = R[key]
    r = subprocess.run([sys.executable, str(SR), 'make', str(text), '--section', 'Active Seizure', '--reader', READER, '--out',
                        str(out)], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); return
    rc = json.loads(out.read_text(encoding='utf-8'))
    if len(rc['sentences']) != len(d['mine']):
        print(key, 'has', len(rc['sentences']), 'sentences and', len(d['mine']), 'entries')
        for x in rc['sentences']:
            print('  ', x['s'][:80])
        return
    for i, (s, (payoff, follows, link)) in enumerate(zip(rc['sentences'], d['mine'])):
        s['payoff'], s['follows'] = payoff, follows
        if i:
            s['link'] = link
    rc['placement'], rc['same_point'], rc['questions'] = d['placement'], d['same_point'], QUESTIONS
    rc['opens']['why_reading'] = 'it tells someone whose friend is seizing when to call medics, and which seizure gets the 5 minutes'
    rc['needed'], rc['his_fixes'], rc['fit'] = NEEDED[key], HISFIX[key], FIT[key]
    out.write_text(json.dumps(rc, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    o = (c.stdout + c.stderr).strip()
    print(key, o.splitlines()[-1] if o else c.returncode)
    if c.returncode:
        print(o)


if __name__ == '__main__':
    for k in sys.argv[1:] or list(R):
        fill(k)
