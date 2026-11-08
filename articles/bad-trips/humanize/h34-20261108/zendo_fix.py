#!/usr/bin/env python3
"""zendo_fix.py - "Zendo-style" explained where the guide first uses it (For the Person Helping, B280).

SKILL.md, Writing for Pangram, fix 2: a term is explained once, where it is first used, inside the sentence that names
it, without asking him. The needed read on B280 (`../h32-20261108/NEEDED-READ.md`) found "Zendo-style" and "harm
reduction" may be unfamiliar, and a second needed read on the explained sentence (NEEDED-READ.md beside this script)
found two of the principles unclear to such a reader: "sitting rather than guiding" read literally, and "talking through
rather than down" taken for talking down to someone, so each is said with who it's done to; and the last principle is
said in the project's own words ("Difficult is not necessarily bad"), since "X does not Y" reads as AI to him (round 1,
RP-13: "humans don't use that so much"). The facts are from the
project's own pages, read 2026-11-08: "Zendo Project provides peer
support services at events" and offers harm reduction training (https://zendoproject.org/about); its four principles
are a safe space, sitting not guiding, through not down, and difficult is not necessarily bad
(https://zendoproject.org/4-principles-of-psychedelic-care). The line read AI before (2026-11-07, h16), so the fix goes
in without a check. The opening line's cut is round 26's card: "perform a rescue fantasy" is said nowhere else.

  python3 zendo_fix.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ, MD = ART / 'GUIDE-SO-FAR-blocks.json', ART / 'GUIDE-SO-FAR.md'
OLD = ('Zendo-style harm reduction can be summarized as creating a safe space, sitting rather than guiding, talking through '
       'rather than down, and remembering that difficult does not automatically mean bad.')
NEW = ('The Zendo Project, a harm-reduction group that offers peer support at festivals and other events to people having a '
       'hard time in an altered state, sums up its approach in four principles: creating a safe space, sitting with the '
       'person rather than guiding them, talking them through it rather than down from it, and remembering that difficult '
       'isn\'t necessarily bad.')
blocks = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in blocks) + '\n' == MD.read_text(encoding='utf-8')
hits = [b for b in blocks if OLD in b['md']]
assert len(hits) == 1 and hits[0]['id'] == 'B280', [b['id'] for b in hits]
hits[0]['md'] = hits[0]['md'].replace(OLD, NEW)
print(hits[0]['md'])
MD.write_text('\n\n'.join(b['md'] for b in blocks) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
