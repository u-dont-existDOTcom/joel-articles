#!/usr/bin/env python3
"""merge_why.py - Why Bad Trips Tend to Happen said once, after his new (Re)defining "Bad Trip" (run after apply_r24.py).

Joel, 2026-11-08, on round 24's TEACH-LABELS: "there's still way too much duplication here. why bad trips tend to happen
the section above this, is duplicating a few other sections, including redefining a bad trip and first 5 minutes". His
new (Re)defining (B330a to B330c) already gives the main causes (too much at once, the dose and the body, old painful
memories, a fearful mindset, the setting or the people) and says some bad trips aren't shadow work. So:
- B356, the heading, goes; what only the section said moves under his (Re)defining, after his three paragraphs;
- B357 and B358 (the "blockage visible" line and its picture, Universe Sends What You Need) move there as they are;
- B359 ("That frame can be useful. It cannot be the only frame.") goes: his "Other bad trips seem unrelated to shadow
  work" says it;
- B360, the causes, keeps the ones said nowhere else and drops the ones his paragraph or another section says: dose,
  an unsafe setting, unresolved trauma, too much too fast (his (Re)defining) and panic loops (The Fear/Panic Loop);
- B361 ("sometimes the lesson is just to lower the dose or stop the practice, get some sleep ...") moves too, after the
  causes: its points are said elsewhere (stopping the practice and the room in the first five minutes, food and sleep in
  his Give the Session, the people in his (Re)defining), but it holds a fidelity key's warning, so its cut is his call
  on round 25's card WHY-LESSON-CUT;
- B362 and B363, the thinking traps from CBT, move there as they are (said nowhere else).
The originals are in GUIDE-BEFORE-R24.md beside this script, so every cut can be put back.

  python3 merge_why.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ, MD = ART / 'GUIDE-SO-FAR-blocks.json', ART / 'GUIDE-SO-FAR.md'
blocks = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in blocks) + '\n' == MD.read_text(encoding='utf-8')
U = {b['id']: b for b in blocks}
OLD360 = ('A bad trip or destabilizing state may also come from dose, drug interactions, sleep deprivation, cannabis, '
          'hunger, dehydration, an unsafe setting, sexual or social pressure, **unresolved trauma**, panic loops, medical '
          'symptoms, psychosis-like symptoms, fasting, intense breathwork, meditation overload, retreat pressure, or simply '
          'too much too fast.')
NEW360 = ('A bad trip or destabilizing state may also come from drug interactions, sleep deprivation, cannabis, hunger, '
          'dehydration, sexual or social pressure, medical symptoms, psychosis-like symptoms, fasting, intense breathwork, '
          'meditation overload, or retreat pressure.')
assert U['B356']['md'] == '## Why Bad Trips Tend to Happen'
assert U['B359']['md'] == 'That frame can be useful. It cannot be the only frame.'
assert U['B360']['md'] == OLD360, U['B360']['md']
assert U['B361']['md'].startswith('Every hard experience can feel like a profound lesson.')
assert U['B362']['md'].startswith('Cognitive distortions') and U['B363']['kind'] == 'ul'
U['B360']['md'] = NEW360
MOVED = ['B357', 'B358', 'B360', 'B361', 'B362', 'B363']
GONE = {'B356', 'B359'}
out = []
for b in blocks:
    if b['id'] in GONE or b['id'] in MOVED:
        continue
    out.append(b)
    if b['id'] == 'B330c':
        out.extend(U[i] for i in MOVED)
assert len(out) == len(blocks) - len(GONE)
MD.write_text('\n\n'.join(b['md'] for b in out) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('Why Bad Trips Tend to Happen under (Re)defining: B356, B359 cut; B360 trimmed; B357, B358, B360, B361, B362, B363 moved')
