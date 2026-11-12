#!/usr/bin/env python3
"""apply_r38b.py - his two fixes of 2026-11-12 19:44 UTC (../../experiments/t38-answers/JOEL-VERSIONS-20261112-1944.md) into
the guide, whole, each from his Pangram check (Human Written, Human High: Active Seizure 5e41c575, My Brain Feels Damaged
a0b8ac56), with obvious corrections only (trailing spaces; a period at the end of his last call line).

- Active Seizure's two lists (H49-SEIZE-LIST, H49-SEIZE-CALL) are his.
- My Brain Feels Damaged: his electrolytes sentence in B103; "- Check if their vision has changed." gone from his list.
- The Call medics list's seizure line said what his call list now says ("A convulsive seizure lasting over 5 minutes"): it
  also told the reader to call for "repeated seizures without normal recovery, or a first or substantially different
  seizure", the two he cut from Active Seizure as wrong advice for an overdose and something nobody can tell (lesson
  bad-trips-2026-11-12b: once his version holds a point, the other places that say it follow it). Shown to him.

  python3 articles/bad-trips/review/r38/apply_r38b.py      (from the repo root)
"""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
B = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
ids = [b['id'] for b in B]

i = ids.index('H49-SEIZE-LIST')
B[i]['md'] = '\n'.join([
    '- Move any dangerous objects away from them, especially anything hard or sharp.',
    "- Don't restrain them, since that can cause injuries, but do put pillows where appropriate, especially under the head.",
    '- Loosen any tight clothing.',
    '- Turn them gently onto their side, which helps them breathe.',
    "- Keep everything out of their mouth while they're convulsing or not fully conscious."])
i = ids.index('H49-SEIZE-CALL')
B[i]['md'] = '\n'.join([
    '- A convulsive seizure goes on for over 5 minutes.',
    '- Their breathing gets slow and shallow.',
    '- Their lips turn blue or gray.',
    '- They get dangerously hot (not just regular sweating).',
    "- They injure their head, break a bone, or bleeding won't stop."])

i = ids.index('B103')
old = ("I add electrolytes too, because magnesium (and then potassium) can be depleted by some drugs, especially MDMA and "
       "iboga, although I don't think just electrolytes would be sufficient.")
assert B[i]['md'].endswith(old)
B[i]['md'] = B[i]['md'][:-len(old)] + ("I give electrolytes to drink also, because magnesium (and then potassium) can be depleted "
                                       "by some drugs, especially MDMA and iboga, although I don't think just electrolytes would "
                                       "be sufficient to reverse damage already underway.")
i = ids.index('R38-BRAIN-LIST')
assert B[i]['md'].endswith('\n- Check if their vision has changed.')
B[i]['md'] = B[i]['md'][:-len('\n- Check if their vision has changed.')]

i = ids.index('B94')
old94 = ('- A convulsive seizure lasting about five minutes, repeated seizures without normal recovery, or a first or '
         'substantially different seizure')
assert B[i]['md'].count(old94) == 1
B[i]['md'] = B[i]['md'].replace(old94, '- A convulsive seizure lasting over 5 minutes')

MD.write_text('\n\n'.join(b['md'] for b in B) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

OE = ART / 'OWNER-EDITS.json'
oe = json.loads(OE.read_text(encoding='utf-8'))
have = {e.get('id') for e in oe['entries']}
new = [
    {'id': 'r38b-seize', 'status': 'applied',
     'what': ('Active Seizure\'s first aid and call list are his version, the text of his check 5e41c575 (pillows under the '
              'head; over 5 minutes; no "another seizure before they\'ve recovered" and no "first seizure"; injuries said as '
              'what happens) (review/r38/apply_r38b.py)'),
     'joel': ('2026-11-12 19:44 UTC: "i fixed active seizure section, it was giving some wrong advice (if it\'s their first '
              'seizure? ... that\'s what we are expecting if the overdose causes a seizure... and how would someone know if '
              'they have another seizure before the first is over?)"'),
     'must_contain_exact': ['but do put pillows where appropriate, especially under the head.',
                            '- A convulsive seizure goes on for over 5 minutes.',
                            "- They injure their head, break a bone, or bleeding won't stop."],
     'must_not_contain': ["It's their first seizure", "Another seizure starts before they've recovered"]},
    {'id': 'r38b-brain', 'status': 'applied',
     'what': ('My Brain Feels Damaged: his electrolytes sentence ("I give electrolytes to drink also ... to reverse damage '
              'already underway") and no vision check, the text of his check a0b8ac56 (review/r38/apply_r38b.py)'),
     'joel': ('2026-11-12 19:44 UTC: "the changed vision thing made no sense (they are tripping, their vision should '
              'change...) and i clarified my electrolytes part"'),
     'must_contain_exact': ['I give electrolytes to drink also', 'sufficient to reverse damage already underway.'],
     'must_not_contain': ['Check if their vision has changed']},
    {'id': 'r38b-call-seizure', 'status': 'applied',
     'what': ('The Call medics list\'s seizure line says what his Active Seizure call list says, "A convulsive seizure lasting '
              'over 5 minutes", without the first seizure and the repeated seizures he cut there (review/r38/apply_r38b.py; '
              'shown to him in the turn\'s report)'),
     'joel': '2026-11-12 19:44 UTC, the same message ("it was giving some wrong advice")',
     'must_contain_exact': ['- A convulsive seizure lasting over 5 minutes'],
     'must_not_contain': ['or a first or substantially different seizure']},
]
oe['entries'] += [e for e in new if e['id'] not in have]
OE.write_text(json.dumps(oe, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('in:', len('\n\n'.join(b['md'] for b in B).split()), 'words')
