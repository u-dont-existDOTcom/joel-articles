#!/usr/bin/env python3
"""apply_r36.py - his round-36 answers (export of 2026-11-12 14:45:53 UTC, ANSWERS-R36-20261112-1445.json) into the guide.

- MEDICAL-HOW: "a" (one teaching card a round, as now), with "you shouldn't need my opinions on stuff in order to pass.
  my opinions are extra. have you systematically looked at all of the fixes i've shown you and what are the idfferences
  in how you write vs how i fix?": no change to the guide; the systematic read is ../../humanize/h46-20261112/his-fixes/.
- TEACH-SS revised: his version, the text of his last check (9e32c090, Human, High 121), in whole, with one change: "the
  these" made "these". Checked as it goes in (../../humanize/h46-20261112/RESULTS.md): with only that fixed it reads
  Human Written, the heading and first sentence Medium and the rest High (0dfe5d10); with his period and lowercase
  "hypertonia" fixed too it read Medium in three windows (9cb1844e), so those stay as he typed them. His lines go in as the
  list B133 was, one pattern a line; his "So if you see any of these patterns, call medics." replaces B134's two
  sentences, W037's warning words with them (his change, recorded in FIDELITY-KEYS-R36.json).

  python3 articles/bad-trips/review/r36/apply_r36.py      (from the repo root)
"""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
B = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
ids = [b['id'] for b in B]


def unit(bid):
    return B[ids.index(bid)]


assert unit('B131')['md'] == '### Recognizing serotonin toxicity'
assert unit('B132')['md'].startswith('Clinicians often use the Hunter criteria.')
assert unit('B134')['md'].startswith('This is a recognition aid rather than a command')
unit('B132')['md'] = ('We can use the same Hunter criteria that clinicians use to diagnose serotonin syndrome. One or more of these '
                      'patterns makes the diagnosis more likely:')
unit('B133')['md'] = '\n'.join([
    '- Spontaneous clonus: involuntary rhythmic muscle spasms, with no stimulation needed to set it off, would be one full '
    'pattern',
    '- Inducible clonus, spasms set off by stretching/flexing a muscle, plus agitation or sweating would be counted as one '
    'pattern altogether.',
    '- Ocular clonus (rapid involuntary eye movements) plus agitation or sweating, another pattern together.',
    '- Another is tremor (shaking) along with hyperreflexia (abnormally brisk reflexes).',
    '- Lastly, Hypertonia (muscular rigidity) with fever above 38°C (100.4°F), as well as ocular or inducible clonus.'])
unit('B134')['md'] = 'So if you see any of these patterns, call medics.'
MD.write_text('\n\n'.join(b['md'] for b in B) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

# fidelity: R34's keys with his round-36 change
K34 = ART / 'humanize/h01/FIDELITY-KEYS-R34.json'
K36 = ART / 'humanize/h01/FIDELITY-KEYS-R36.json'
k = json.loads(K34.read_text(encoding='utf-8'))
k['about'] += (' | R36 (2026-11-12 14:45 UTC): R34 with the owner_changes of rounds 35 and 36 (his TEACH-SS version, '
               'export of 14:45:53 UTC).')
k['owner_changes'].append({
    'by': ('articles/bad-trips/review/r36/ANSWERS-R36-20261112-1445.json, card TEACH-SS (revised): his version of '
           'Suspected Serotonin Syndrome\'s recognition part, in his check 9e32c090 ("now it\'s all high conf human"), '
           'says the lead-in his way ("One or more of the these patterns makes the diagnosis more likely:", "the '
           'diagnosis" for "serotonin toxicity") and ends on '
           '"So if you see any of these patterns, call medics." in place of the recognition-aid line and "Dangerous heat, '
           'rigidity, clonus, confusion, or rapid worsening deserves medical help."'),
    'keys_lost': {'W036': [['following'], ['toxicity']], 'W037': [['dangerous'], ['deserves'], ['rigidity']]}})
K36.write_text(json.dumps(k, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

# his edits, recorded so a later pass can't undo them
OE = ART / 'OWNER-EDITS.json'
oe = json.loads(OE.read_text(encoding='utf-8'))
have = {e.get('id') for e in oe['entries']}
new = [
    {'id': 'r36-teach-ss', 'status': 'applied',
     'what': ('Suspected Serotonin Syndrome\'s recognition part is his version, the text of his last check 9e32c090, with '
              '"the these" made "these" (round 36, card TEACH-SS; review/r36/apply_r36.py)'),
     'joel': ('2026-11-12 14:45:53 UTC: round 36\'s export, TEACH-SS revised, with his three tries and "now it\'s all high '
              'conf human"'),
     'must_contain_exact': ['We can use the same Hunter criteria that clinicians use to diagnose serotonin syndrome.',
                            'would be counted as one pattern altogether.',
                            'So if you see any of these patterns, call medics.'],
     'must_not_contain': ['This is a recognition aid rather than a command to wait for every criterion before acting.',
                          'Clinicians often use the Hunter criteria. One or more of the following patterns']},
]
oe['entries'] += [e for e in new if e['id'] not in have]
OE.write_text(json.dumps(oe, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('in:', unit('B132')['md'][:70], '|', len('\n\n'.join(b['md'] for b in B).split()), 'words')
