#!/usr/bin/env python3
"""Turn 122: the three earlier OWNER-EDITS.json entries his marking-page answers overtook (check_owner_edits.py failed them
right after apply_t122.py). Each change keeps the entry's record and says what replaced which part:
  - joel-121-aside: his aside's paragraph went with the whole Hearthwork section he rewrote (HW-1, HW-3 "delete"), so the
    entry is superseded by joel-122-hw-1;
  - emoji-pass-20261001: "Try again. 😅" went with his version of If You Really Did Hurt Them's P2 (M-B36: "i couldn't honestly
    understand this lol, glad i changed it"), so that one string leaves must_contain; the rest of the entry holds;
  - joel-92-20261022: "I'd still try a small good thing" was P5 of When Being Happy Feels Like Abandoning Someone, which he
    asked me to delete (M-B13), so it leaves the entry's order; his 14 years paragraph and its place hold.
  python3 articles/inner-child-therapy/experiments/t122-apply/supersede_t122.py"""
import json
import pathlib

LEDGER = pathlib.Path(__file__).resolve().parents[2] / 'OWNER-EDITS.json'
WHEN = '2026-11-04 13:44 UTC (experiments/t122-answers/ANSWERS-20261104-1344.json)'
d = json.loads(LEDGER.read_text(encoding='utf-8'))
E = {e['id']: e for e in d['entries']}
a = E['joel-121-aside']
assert a['status'] == 'applied'
a['status'] = 'superseded'
a['superseded_by'] = 'joel-122-hw-1'
a['superseded'] = 'Joel rewrote the whole Hearthwork section on the round-9 marking page and deleted this paragraph with it (HW-3: "delete"), %s.' % WHEN
m = E['emoji-pass-20261001']
assert 'Try again. 😅' in m['must_contain']
m['must_contain'] = [s for s in m['must_contain'] if s != 'Try again. 😅']
m.setdefault('changes', []).append({'at': WHEN, 'removed': {'must_contain': 'Try again. 😅'},
                                    'why': 'his version of If You Really Did Hurt Them, P2 (M-B36), has no "Try again." (joel-122-m-b36)'})
o = E['joel-92-20261022']
assert o['order'][-1] == "I'd still try a small good thing"
o['order'] = o['order'][:-1]
o.setdefault('changes', []).append({'at': WHEN, 'removed': {'order': "I'd still try a small good thing"},
                                    'why': 'he asked me to delete that paragraph, P5 of When Being Happy Feels Like Abandoning Someone (M-B13: "i want you to delete P5"; joel-122-m-b13)'})
LEDGER.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('superseded joel-121-aside; emoji-pass-20261001 and joel-92-20261022 updated')
