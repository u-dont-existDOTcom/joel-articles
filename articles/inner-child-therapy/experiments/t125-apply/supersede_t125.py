#!/usr/bin/env python3
"""Turn 125: the one earlier OWNER-EDITS.json entry his marking-page answers overtook (check_owner_edits.py failed it right
after apply_t125.py): joel-116-117-guide, his reorganized guide, held "so “meet the protector first” would fit right in over
there", which he approved changing to "meet the guard first" (card SR-514; joel-125-sr-514). That one string leaves its
must_contain, with a record of why; the rest of the entry holds.
  python3 articles/inner-child-therapy/experiments/t125-apply/supersede_t125.py"""
import json
import pathlib

LEDGER = pathlib.Path(__file__).resolve().parents[2] / 'OWNER-EDITS.json'
WHEN = '2026-11-04 16:11 UTC (experiments/t125-answers/ANSWERS-20261104-1611.json)'
OLD = 'so “meet the protector first” would fit right in over there'
d = json.loads(LEDGER.read_text(encoding='utf-8'))
e = {x['id']: x for x in d['entries']}['joel-116-117-guide']
assert OLD in e['must_contain']
e['must_contain'] = [s for s in e['must_contain'] if s != OLD]
e.setdefault('changes', []).append({'at': WHEN, 'removed': {'must_contain': OLD},
                                    'why': 'he approved card SR-514 of the sense-read marking page: "meet the guard first" (joel-125-sr-514)'})
LEDGER.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('joel-116-117-guide updated')
