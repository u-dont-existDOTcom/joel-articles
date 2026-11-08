#!/usr/bin/env python3
"""dedup_cut.py - the one repeat the third repeats read found that loses nothing (For the Person Helping's Do list).

A fresh reader read the first five minutes, Stillness or Movement? and the helper's opening and Do list against the whole
guide (REPEATS-FIRST-FIVE.md beside this script; what each finding came to is in RESULTS.md). The Do list's "Offer
choices instead of commands." says only what the list's own first line does with its questions ("Would less light
help?" "Music or quiet?" "Closer or farther away?"), his don'ts below it ("Don't force eye contact, touch, music, ...
on them") and his Give the Session ("offers you choices if relevant"); its cut loses no fidelity key, no keep-as-is line
and no owner edit, so it goes in (turn 16, his message of 2026-11-06 19:43 UTC: "make the cuts regardless of pangram if
it makes the guide read better").

  python3 dedup_cut.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ, MD = ART / 'GUIDE-SO-FAR-blocks.json', ART / 'GUIDE-SO-FAR.md'
OLD = '- Offer choices instead of commands.\n'
blocks = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in blocks) + '\n' == MD.read_text(encoding='utf-8')
hits = [b for b in blocks if OLD in b['md']]
assert len(hits) == 1 and hits[0]['kind'] == 'ul', [(b['id'], b['kind']) for b in hits]
hits[0]['md'] = hits[0]['md'].replace(OLD, '')
print(hits[0]['id'], hits[0]['md'])
MD.write_text('\n\n'.join(b['md'] for b in blocks) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
