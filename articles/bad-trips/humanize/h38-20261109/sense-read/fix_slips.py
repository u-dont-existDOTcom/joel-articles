#!/usr/bin/env python3
"""fix_slips.py - the word-for-sense read's three slips in the model's text, fixed with the fewest words.

The read (gate E331; SKILL.md, "Word-for-sense read before publication") found every planted error (9 of 9), so its
other findings and its silence can be trusted. Each finding was read in place and traced to its source
(RESULTS.md beside this script). These three are in text the model drafted for his post of 3 November (gate E373), so
they are fixed here without asking him (lesson bad-trips-2026-11-09a: "do your best first"):

- B93, the heading over the call-medics list, "Call medics while acting for:": "acting for" reads as acting on someone's
  behalf, and the line right under the list already says what "while acting" meant ("The remedies below can begin
  while help is being arranged."). Cut to "Call medics for:", the way the next heading reads ("Bring in mental-health
  support when:").
- B249, the first line under "Stillness or Movement?", "Test them rather than ...": "them" points only at the heading.
- B428, under "No "another ceremony will fix this" reflex.": the list after "Don't take more" turns from things you take
  into things you do ("intense breathwork, fast, push kundalini, ..."), so "take more" governs "intense breathwork" and
  "fast" reads as an adjective. "cannabis or ketamine, do intense breathwork" ends what is taken and starts what is done.

  python3 fix_slips.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[2]
BJ, MD = ART / 'GUIDE-SO-FAR-blocks.json', ART / 'GUIDE-SO-FAR.md'
FIXES = [
    ('B93', '## Call medics while acting for:', '## Call medics for:'),
    ('B249', 'Test them rather than turning them into rival religions.',
     'Test stillness and movement rather than turning them into rival religions.'),
    ('B428', "Don't take more psychedelics, cannabis, ketamine, intense breathwork, fast,",
     "Don't take more psychedelics, cannabis or ketamine, do intense breathwork, fast,"),
]

blocks = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in blocks) + '\n' == MD.read_text(encoding='utf-8')
for bid, old, new in FIXES:
    hits = [b for b in blocks if old in (b['md'] or '')]
    assert len(hits) == 1 and hits[0]['id'] == bid, (bid, [b['id'] for b in hits])
    assert hits[0]['md'].count(old) == 1
    hits[0]['md'] = hits[0]['md'].replace(old, new)
    print('%s: %s' % (bid, hits[0]['md'][:200]))
MD.write_text('\n\n'.join(b['md'] for b in blocks) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
