#!/usr/bin/env python3
"""apply_t19c.py - Alone at 3 a.m.'s movement paragraph (B274) keeps only what Stillness or Movement? doesn't say, by
Joel's decision of 2026-11-06 19:43 UTC (../t16-answers/JOEL-MESSAGE-20261106-1943.md: "make the cuts regardless of
pangram if it makes the guide read better"; gate E378).

Cut, as said already two sections up:
- "pace the same hallway": Stillness or Movement?'s "pace slowly in a contained space";
- "fold towels, wash a cup": its parallel processing's "fold five towels, or wash one cup";
- "When movement makes you more frantic, sit with both feet against the floor or lie under a blanket.": its "When pacing
  begins to resemble escape, sit against a wall or lie under a blanket." (and its two-minute test's "more activated and
  impulsive").
Kept, said only here: the other ways to move (teeth, stretching, a calm shower, wall push-ups) and "Then protect sleep."
Stillness or Movement?, with the fidelity keys' W077 ("The goal is to let the nervous system discharge without creating a
new danger."), is unchanged; no fidelity key is in what is cut.

  python3 apply_t19c.py      write the guide (../../GUIDE-SO-FAR.md and its blocks) and print what changed
"""
import hashlib
import json
import pathlib
import re

ART = pathlib.Path(__file__).resolve().parent.parent.parent
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
BLOCKS = json.loads(BJ.read_text(encoding='utf-8'))
UNIT = {b['id']: b for b in BLOCKS}
before_md = MD.read_text(encoding='utf-8')
assert '\n\n'.join(b['md'] for b in BLOCKS) + '\n' == before_md, 'the blocks and the guide disagree'
OLD = ("When the body still needs movement, keep it contained and boring: pace the same hallway, fold towels, wash a cup, "
       "brush your teeth, stretch gently, take a calm shower, or do a few slow wall push-ups. When movement makes you more "
       "frantic, sit with both feet against the floor or lie under a blanket. Then protect sleep.")
NEW = ("When the body still needs movement, keep it contained and boring: brush your teeth, stretch gently, take a calm "
       "shower, or do a few slow wall push-ups. Then protect sleep.")
assert UNIT['B274']['md'] == OLD, UNIT['B274']['md']
UNIT['B274']['md'] = NEW
text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(text, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before_md)), len(re.findall(r'\S+', text))
print("B274: Alone at 3 a.m.'s movement paragraph keeps only what is said only there")
print('%d words -> %d (%+d); GUIDE-SO-FAR.md sha256 %s' % (w0, w1, w1 - w0, hashlib.sha256(text.encode()).hexdigest()))
