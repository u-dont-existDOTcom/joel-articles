#!/usr/bin/env python3
"""apply_r39c.py - his call list version f6b4e35a in, whole, and the first of the two DMSO points he said yes to.

- His message of 2026-11-13 14:15 UTC: "but i want this version which explains better:
  https://www.pangram.com/history/f6b4e35a-6b04-43f2-b06a-d2fa1034f16e". Its text, read from his Pangram history in the
  desktop app's browser pane on 2026-11-13 (turn 43; the link to his computer was back): Human Written, 0% AI, one window
  Human High 102. His list replaces Active Seizure's call list whole (H49-SEIZE-CALL); its second item now says which
  seizure the 5 minutes is for and why, so the paragraph after the list that said the same (H51-SEIZE-WAIT, mine, from his
  points of 2026-11-12 22:34 UTC) goes: his item says it, in his words ("which doesn't indicate brain damage" where my
  paragraph had "most likely less dangerous than an actual drug overdose seizure"). The paragraph, kept here so the cut can
  be undone:
    "Waiting the 5 minutes is only for a seizure on a normal dose. Psychedelics can lower the seizure threshold even at a
    normal dose, so someone with epilepsy or who's otherwise prone to seizures can have a seizure without taking too much.
    Their seizure is most likely less dangerous than an actual drug overdose seizure."
- His message of 2026-11-13 14:56 UTC, "and yes i want the dmso fixes you mentioned": "organ or stem cell transplants" made
  "stem cell transplants" (DMSO is the standard preservative for frozen stem cells; donor organs are kept cold without it).
  The other point (Hanslick et al. 2009 said as what it found) goes in with the Lu & Mattson merge he asked for at 14:59 UTC,
  once checked (../../humanize/h53-20261113/).

  python3 articles/bad-trips/review/r39/apply_r39c.py      (from the repo root)
"""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
B = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
ids = [b['id'] for b in B]

HIS_LIST = ("- They have a seizure after taking too much, or you don't know how much they took\n"
            "- Note that psychedelics do reduce the seizure threshold, so if someone is prone to seizures, a normal dose could "
            "produce a seizure for them which doesn't indicate brain damage, but if it goes on over 5 minutes, that's too much\n"
            "- Their breathing gets slow and shallow\n"
            "- Their lips turn blue or gray\n"
            "- When you touch their forehead, it's very hot (not just sweaty)\n"
            "- They injure their head, break a bone, or bleeding won't stop")
WAIT = ("Waiting the 5 minutes is only for a seizure on a normal dose. Psychedelics can lower the seizure threshold even at a "
        "normal dose, so someone with epilepsy or who's otherwise prone to seizures can have a seizure without taking too much. "
        "Their seizure is most likely less dangerous than an actual drug overdose seizure.")

i = ids.index('H49-SEIZE-CALL')
assert B[i - 1]['md'] == 'Call medics if any of these happen:'
B[i]['md'] = HIS_LIST
if 'H51-SEIZE-WAIT' in ids:
    j = ids.index('H51-SEIZE-WAIT')
    assert B[j]['md'] == WAIT, B[j]['md']
    del B[j]

ORGAN_OLD = "It's routinely used in humans who receive organ or stem cell transplants,"
ORGAN_NEW = "It's routinely used in humans who receive stem cell transplants,"
k = [n for n, b in enumerate(B) if b['id'] == 'R39B-DMSO-2'][0]
if ORGAN_OLD in B[k]['md']:
    B[k]['md'] = B[k]['md'].replace(ORGAN_OLD, ORGAN_NEW)
assert ORGAN_NEW in B[k]['md']

MD.write_text('\n\n'.join(b['md'] for b in B) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

# The records: r38b-seize's exact line is now his new item (the threshold still in both places: KEEP-AS-IS K8).
OE = ART / 'OWNER-EDITS.json'
oe = json.loads(OE.read_text(encoding='utf-8'))
NEW_LINE = ("- Note that psychedelics do reduce the seizure threshold, so if someone is prone to seizures, a normal dose could "
            "produce a seizure for them which doesn't indicate brain damage, but if it goes on over 5 minutes, that's too much")
for e in oe['entries']:
    if e['id'] == 'r38b-seize':
        e['must_contain_exact'] = [NEW_LINE if x == '- A seizure on a normal dose goes on for over 5 minutes' else x
                                   for x in e['must_contain_exact']]
        if 'f6b4e35a' not in e['what']:
            e['what'] += ('; 2026-11-13, his version f6b4e35a ("but i want this version which explains better"): the list '
                          'whole, the 5-minute line with his explanation in it (review/r39/apply_r39c.py)')
    if e['id'] == 'h51-seize-wait' and e['status'] != 'superseded':
        e['status'] = 'superseded'
        e['superseded_by'] = ('r39c-call-list-his: his version f6b4e35a of 2026-11-13 says this paragraph\'s points in the '
                              'list\'s second item, in his words ("which doesn\'t indicate brain damage" for "most likely '
                              'less dangerous than an actual drug overdose seizure"), so the paragraph is cut as said twice')
have = {e['id'] for e in oe['entries']}
new = [
    {'id': 'r39c-call-list-his', 'status': 'applied',
     'what': ("Active Seizure's call list is his version f6b4e35a, whole; the paragraph after it that said the same (mine) cut "
              "(review/r39/apply_r39c.py)"),
     'joel': '2026-11-13 14:15 UTC: "but i want this version which explains better" (f6b4e35a)',
     'must_contain_exact': [NEW_LINE + '\n', "- When you touch their forehead, it's very hot (not just sweaty)\n"],
     'must_not_contain': ['Waiting the 5 minutes is only for a seizure on a normal dose.',
                          '- Their forehead feels very hot (not just sweaty)']},
    {'id': 'r39c-stem-cell', 'status': 'applied',
     'what': 'The DMSO section: "organ or stem cell transplants" made "stem cell transplants" (review/r39/apply_r39c.py)',
     'joel': '2026-11-13 14:56 UTC: "and yes i want the dmso fixes you mentioned"',
     'must_contain': ["It's routinely used in humans who receive stem cell transplants,"],
     'must_not_contain': ['organ or stem cell transplants']},
]
oe['entries'] += [e for e in new if e['id'] not in have]
OE.write_text(json.dumps(oe, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

# KEEP-AS-IS K8: the threshold line he agreed stays in both places is now his new item.
KP = ART / 'KEEP-AS-IS.json'
kp = json.loads(KP.read_text(encoding='utf-8'))
for it in kp['keep']:
    if it.get('id') == 'K8' and it['quote'] != NEW_LINE:
        it['quote'] = NEW_LINE
        it['reworded'] += ('; 2026-11-13, his version f6b4e35a ("but i want this version which explains better"): the line '
                           'with his explanation of the seizure threshold in it, still in both places')
KP.write_text(json.dumps(kp, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('applied: his call list f6b4e35a, the 5-minute paragraph out, stem cell transplants |',
      len(MD.read_text(encoding='utf-8').split()), 'words')
