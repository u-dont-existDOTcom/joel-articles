#!/usr/bin/env python3
"""apply_h51.py - his message of 2026-11-12 22:34 UTC into Active Seizure and the Call medics list, through the gate
(tools/humanization/apply_gate.py, gate bad-trips-2026-11-12l): nothing of mine goes in unless a check of it by itself read
Human High in every window, or, for a list whose lines are about the person its section is about, the section did.

- Active Seizure's call list (H49-SEIZE-CALL): an overdose seizure its own line ("They have a seizure after taking too much,
  or you don't know how much they took."), the 5 minutes for a seizure on a normal dose ("you're right about over 5 minutes
  that's an epilepsy rule"), and the heat line with how to tell ("you can tell by touching someone's forehead"): callp-c3.
  By itself it read Human with a Medium window over its last four lines, three of them his, whatever my heat line said, and
  his own heat line read AI there (RESULTS.md); in its section it read Human High in one window (c00d2cae). So it goes in on
  his exception: its lines are about the friend the section is about ("they", "their"), which they can't say by themselves.
- After it, a paragraph of mine from his words (H51-SEIZE-WAIT): which seizure the 5 minutes is for, his reason ("they can
  lower seizure threshold even with a normal dose") and his comparison ("most likely less dangerous than an actual drug
  overdose seizure"): explone-c5, Human High 56 by itself (fa2258eb).
- The Call medics list at the top (B94) says the same seizure line the same way (lesson bad-trips-2026-11-12b); B94 as a
  whole read AI before this (h42-02) and is still on the list to humanize.

  python3 apply_h51.py [--dry]
"""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
REPO = HERE.parents[3]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
KEYS = ART / 'humanize/h01/FIDELITY-KEYS-R40.json'
LEDGER = ART / 'humanize/pangram-ledger.jsonl'
SP = pathlib.Path('/tmp/claude-0/-home-claude/7a3d2b92-4547-585d-83c0-bf816aa7e013/scratchpad')
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(REPO / 'tools/humanization'))
from build_tests import CALL3, EXPL5  # noqa: E402
import apply_gate  # noqa: E402

SECTION_OK = ("the call list's lines are about the friend the Active Seizure section is about ('they', 'their'): by itself it "
              "read Human with a Medium window over its last four lines, three of them his, whatever my heat line said (and "
              "his own heat line read AI there), and in its section Human High in one window (c00d2cae)")
LINES = CALL3.split('\n')[1:]
MINE = [LINES[0], LINES[1], LINES[4]]
apply_gate.require(str(LEDGER), [EXPL5])
apply_gate.require(str(LEDGER), MINE, section_ok=SECTION_OK)

dry = '--dry' in sys.argv
B = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
ids = [b['id'] for b in B]
i = ids.index('B112')
assert B[i]['md'] == CALL3.split('\n')[0]
i = ids.index('H49-SEIZE-CALL')
assert B[i]['md'].startswith('- A convulsive seizure goes on for over 5 minutes.')
B[i]['md'] = '\n'.join(LINES)
if 'H51-SEIZE-WAIT' not in ids:
    B.insert(i + 1, dict(B[i], id='H51-SEIZE-WAIT', kind='p', md=EXPL5))
i = [b['id'] for b in B].index('B94')
old94 = '- A convulsive seizure lasting over 5 minutes'
assert B[i]['md'].count(old94) == 1
B[i]['md'] = B[i]['md'].replace(old94, '- A seizure after taking too much (or an unknown amount), or one on a normal dose lasting over 5 minutes')

text = '\n\n'.join(b['md'] for b in B) + '\n'
out = SP / 'guide-h51-dry.md' if dry else MD
out.write_text(text, encoding='utf-8')
if not dry:
    BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    OE = ART / 'OWNER-EDITS.json'
    oe = json.loads(OE.read_text(encoding='utf-8'))
    for e in oe['entries']:
        if e.get('id') == 'r38b-seize':
            e['must_contain_exact'] = [x if x != '- A convulsive seizure goes on for over 5 minutes.' else
                                       '- A seizure on a normal dose goes on for over 5 minutes.' for x in e['must_contain_exact']]
            e['what'] += ('; 2026-11-12 22:34 UTC, his message: an overdose seizure its own call line and the 5 minutes for a '
                          'seizure on a normal dose, the heat line with the forehead (humanize/h51-20261112/apply_h51.py)')
        if e.get('id') == 'r38b-call-seizure':
            e['must_contain_exact'] = ['- A seizure after taking too much (or an unknown amount), or one on a normal dose lasting over 5 minutes']
            e['what'] += ('; 2026-11-12 22:34 UTC: the same line as his Active Seizure call list now says it, an overdose seizure '
                          'and the 5 minutes for a seizure on a normal dose (humanize/h51-20261112/apply_h51.py)')
    have = {e['id'] for e in oe['entries']}
    if 'h51-seize-wait' not in have:
        oe['entries'].append({
            'id': 'h51-seize-wait', 'status': 'applied',
            'what': ("Active Seizure: the paragraph after the call list says which seizure the 5 minutes is for, why a seizure can "
                     "come on a normal dose, and that it is most likely less dangerous than an overdose seizure "
                     "(humanize/h51-20261112/apply_h51.py)"),
            'joel': ('2026-11-12 22:34 UTC: "you\'re right about over 5 minutes that\'s an epilepsy rule. altho we should also keep '
                     'in mind that if someone does have epilepsy, they are more likely to have seizures on psychedelics so explain '
                     'that they can lower seizure threshold even with a normal dose and people with already low seizure thresholds '
                     'might have seizures which are most likely less dangerous than an actual drug overdose seizure"'),
            'must_contain': ['Psychedelics can lower the seizure threshold even at a normal dose',
                             'most likely less dangerous than an actual drug overdose seizure']})
    OE.write_text(json.dumps(oe, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    KA = ART / 'KEEP-AS-IS.json'
    ka = json.loads(KA.read_text(encoding='utf-8'))
    for e in ka['keep']:
        if e.get('id') == 'K8' and e['quote'] != '- A seizure on a normal dose goes on for over 5 minutes.':
            e['quote'] = '- A seizure on a normal dose goes on for over 5 minutes.'
            e['reworded'] += ('; 2026-11-12 22:34 UTC, his message ("you\'re right about over 5 minutes that\'s an epilepsy rule"): '
                              'the 5 minutes for a seizure on a normal dose, an overdose seizure its own line, in both places')
    KA.write_text(json.dumps(ka, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/fidelity_keys.py'), 'check', str(KEYS), str(out)],
                   capture_output=True, text=True)
print(('dry' if dry else 'applied') + ': the call list, the 5-minutes paragraph, the Call medics line |', len(text.split()), 'words')
print((r.stdout + r.stderr).strip()[-1200:])
