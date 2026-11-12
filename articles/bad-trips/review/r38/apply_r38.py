#!/usr/bin/env python3
"""apply_r38.py - his round-38 answer (export of 2026-11-12 18:19:16 UTC, ANSWERS-R38-20261112-1819.json) into the guide.

- TEACH-BRAIN revised: his version of My Brain Feels Damaged's heading and checks, the text of his last check (4739068c,
  Human Written, Human High 174; ../../experiments/t38-answers/JOEL-TRIES-TEACH-BRAIN.md), in whole, with three obvious
  corrections ("no need to ask me for obvious corrections", round 37): one space in "Humic Acid  +", "are unconscious"
  made "are they unconscious", "-Wetting" made "- Wetting". The heading (B102), the lead-in (B104, its link to the stroke
  list kept on "stroke warning signs"), his nine lines as a list (R38-BRAIN-LIST) and his closing line (R38-BRAIN-2).
- His reason for the electrolytes, from his comment ("because magnesium (and then potassium) can be depleted by some drugs
  esp MDMA and iboga, altho i don't think just electrolytes would be sufficient"), goes at the end of the paragraph that
  says what comes first (B103), in his words, so the heading's new remedy is in the section.
- B106's first sentence ("For objective stroke-like signs, I would use DMSO immediately while someone calls medics.")
  goes: his lead-in says it (lesson bad-trips-2026-11-12b, once his version holds a point, every other place goes).

  python3 articles/bad-trips/review/r38/apply_r38.py      (from the repo root)
"""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
B = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
ids = [b['id'] for b in B]
STROKE = '[stroke warning signs](https://www.stroke.org/en/about-stroke/stroke-symptoms)'

i = ids.index('B102')
assert B[i]['md'] == '## If Someone Says "My Brain Feels Damaged": DMSO + Humic Acid First'
B[i]['md'] = '## If Someone Says "My Brain Feels Damaged": DMSO + Humic Acid + Electrolytes First'

i = ids.index('B103')
assert B[i]['md'].endswith("in my experience, but I'm still collecting data from others.")
ELEC = ("I add electrolytes too, because magnesium (and then potassium) can be depleted by some drugs, especially MDMA and "
        "iboga, although I don't think just electrolytes would be sufficient.")
B[i]['md'] += ' ' + ELEC

i = ids.index('B104')
assert B[i]['md'].startswith('While using DMSO, check wakefulness')
B[i]['md'] = 'While the DMSO is working, check for %s that would trigger a call to medics:' % STROKE
B[i + 1:i + 1] = [
    {'id': 'R38-BRAIN-LIST', 'kind': 'ul', 'text': None, 'md': '\n'.join([
        '- First, are they unconscious or breathing abnormally?',
        "- Feel whether they're very hot.",
        '- Have them talk and smile. Is their speech slurred, or does one side of their face droop?',
        '- Ask them to hold both arms out in front of them, and see if one drifts down.',
        '- If you can safely hold them as they try, have them stand and walk a few steps to see if they keep their balance.',
        '- Wetting or soiling themselves is another sign to watch for.',
        '- Watch for a seizure, and for vomiting that keeps coming back.',
        '- Ask about a really bad headache or chest pain.',
        '- Check if their vision has changed.'])},
    {'id': 'R38-BRAIN-2', 'kind': 'p', 'text': None,
     'md': ("When they're too out of it to help you do the checks, or if the brain-damage feeling stays despite sufficient "
            "treatment, then you've done what you can do, and it's time to call for help.")},
]
ids = [b['id'] for b in B]
j = ids.index('B106')
first = 'For objective stroke-like signs, I would use DMSO immediately **while someone calls medics**. '
assert B[j]['md'].startswith(first)
B[j]['md'] = B[j]['md'][len(first):]

MD.write_text('\n\n'.join(b['md'] for b in B) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

OE = ART / 'OWNER-EDITS.json'
oe = json.loads(OE.read_text(encoding='utf-8'))
have = {e.get('id') for e in oe['entries']}
new = [
    {'id': 'r38-teach-brain', 'status': 'applied',
     'what': ('My Brain Feels Damaged\'s heading and checks are his version, the text of his last check 4739068c: "+ '
              'Electrolytes" in the heading, the lead-in "check for stroke warning signs that would trigger a call to '
              'medics:", his nine lines and his closing line, with three obvious corrections; his reason for the '
              'electrolytes at the end of B103 in his words; B106\'s first sentence gone, since his lead-in says it '
              '(round 38, card TEACH-BRAIN; review/r38/apply_r38.py)'),
     'joel': ('2026-11-12 18:19:16 UTC: round 38\'s export, TEACH-BRAIN revised, with his six tries; "some really obvious '
              'problems again"'),
     'must_contain_exact': ['DMSO + Humic Acid + Electrolytes First', 'that would trigger a call to medics:',
                            '- First, are they unconscious or breathing abnormally?',
                            '- If you can safely hold them as they try, have them stand and walk a few steps',
                            "then you've done what you can do, and it's time to call for help.",
                            'because magnesium (and then potassium) can be depleted by some drugs'],
     'must_not_contain': ['While using DMSO, check wakefulness', 'For objective stroke-like signs, I would use DMSO immediately']},
]
oe['entries'] += [e for e in new if e['id'] not in have]
OE.write_text(json.dumps(oe, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('in:', len('\n\n'.join(b['md'] for b in B).split()), 'words')
