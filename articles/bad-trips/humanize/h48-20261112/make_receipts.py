#!/usr/bin/env python3
"""make_receipts.py - the making-sense receipts for this folder's carries (gate E365), as in ../h46-20261112/make_receipts.py,
with the read against his fixes (gate bad-trips-2026-11-12g, HIS-FIXES.json) and the needed read (NEEDED.json).

  python3 make_receipts.py KEY...
"""
import copy, json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
SR = REPO / 'tools/humanization/sense_receipt.py'
NEEDED = json.loads((HERE / 'NEEDED.json').read_text(encoding='utf-8'))
HISFIX = json.loads((HERE / 'HIS-FIXES.json').read_text(encoding='utf-8'))
sys.path.insert(0, str(HERE.parent / 'h46-20261112'))
from make_receipts import R as R46  # noqa: E402
CHECK = 'none: a list line, the next check the reader expects after the one before'
b3 = R46['brain-c3']
R = {'brain-p1': copy.deepcopy(b3)}
R['brain-p1']['mine'] = (
    b3['mine'][:3] +
    [("they keep the DMSO going while someone calls medics when any check turns up a problem, or when the person is too "
      "out of it to answer", 'what to do with the checks, said before them', 'If any check')] +
    b3['mine'][3:13] + [b3['mine'][15]])
R['brain-p1']['same_point'] = ('merged here: B106\'s first sentence ("For objective stroke-like signs, I would use DMSO '
                               'immediately while someone calls medics.") said here as what to do with the checks, now before '
                               'them ("If any check turns up a problem ..., keep the DMSO going while someone calls medics:"); '
                               'B106 keeps the rest')
R['brain-p1']['questions']['Q1'] = ('PASS: the action ("keep the DMSO going while someone calls medics") is said before the '
                                    'checks it serves, as in his Chest Pain fix; each line is one check and what it shows')
R['brain-p1']['questions']['Q5'] = ('PASS: "If any check turns up a problem", "Is their speech slurred", "another sign to watch '
                                    'for", "If everything checks out" say each relation')
R['brain-p1']['questions']['Q6'] = ('PASS: why the checks, what to do when one shows a sign or can\'t be done, the checks, the '
                                    'case they all pass')
R['acute-c1'] = {
 'section': 'Acute Medical and Neurological Rescue',
 'reader': ('someone with a friend in a severe trip, deciding whether to handle it themselves or get them to an emergency '
            'room'),
 'mine': [
  ('they know this part is about medical and neurological rescue', 'the heading',
   'none: the section heading itself, typed with the test'),
  ('they calm and stabilize the trip where the person is, unless a sign on the Call medics list shows up or they can\'t '
   'keep the person from getting hurt', 'it opens the section under its heading', 'none: the first sentence under its heading'),
  ('they know staying can bring the person down faster than an ambulance ride and hours in an emergency room, even from '
   'a severe trip', 'why stay, after what to do', 'that way'),
 ],
 'placement': ('Acute Medical and Neurological Rescue, its opening paragraph (B100 and B76 as one), after the contacts that '
               'close When to Bring In Outside Help, before the emergency room paragraph (B77)'),
 'why_reading': 'it tells someone with a friend in a severe trip whether to handle it where they are, before any remedy',
 'same_point': ('merged here: B76\'s six conditions are the Call medics list\'s own lines (trouble breathing, dangerous '
                'overheating, seizures, the brain checks, collapse or not waking), so this paragraph points to the list '
                '(his BODY-ONCE answer of round 35: "my paragraph should not say anything that should be going in that above '
                'list"); the one condition the list lacks, keeping them from getting hurt, stays here; B77 keeps the emergency '
                'room\'s drugs'),
 'questions': {
  'Q1': 'PASS: the paragraph opens on what to do ("I\'d calm and stabilize the trip right where they are"), its conditions after',
  'Q2': 'PASS: "calm and stabilize the trip", "keep them from getting hurt": the helper\'s acts',
  'Q3': 'PASS: "the signs on the Call medics list above" says which signs',
  'Q4': 'PASS: no term; "field rescue" said as "right where they are"',
  'Q5': 'PASS: "as long as" and "that way" say each relation',
  'Q6': 'PASS: what to do, when not, then why',
  'Q7': 'PASS: both sentences bear on whether to stay or go',
  'Q8': 'PASS: one paragraph on where to handle a severe trip',
  'Q9': 'PASS: one step a sentence; the six conditions are the list\'s, not packed here',
 }}


def fill(key):
    text = HERE / ('TEST-%s.txt' % key)
    out = HERE / ('TEST-%s.receipt.json' % key)
    d = R[key]
    r = subprocess.run([sys.executable, str(SR), 'make', str(text), '--section', d['section'], '--reader', d['reader'], '--out',
                        str(out)], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); return
    rc = json.loads(out.read_text(encoding='utf-8'))
    if len(rc['sentences']) != len(d['mine']):
        print(key, 'has', len(rc['sentences']), 'sentences and', len(d['mine']), 'entries:')
        for x in rc['sentences']:
            print('  ', x['s'])
        return
    mine = iter(d['mine'])
    for i, s in enumerate(rc['sentences']):
        payoff, follows, link = next(mine)
        s['payoff'], s['follows'] = payoff, follows
        if i:
            s['link'] = link
    rc['placement'], rc['same_point'], rc['questions'] = d['placement'], d['same_point'], d['questions']
    rc['opens']['why_reading'] = d['why_reading']
    rc['needed'] = NEEDED[key]
    rc['his_fixes'] = HISFIX[key]
    out.write_text(json.dumps(rc, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    o = (c.stdout + c.stderr).strip()
    print(key, o.splitlines()[-1] if o else c.returncode)
    if c.returncode:
        print(o)


if __name__ == '__main__':
    for k in sys.argv[1:] or list(R):
        fill(k)
