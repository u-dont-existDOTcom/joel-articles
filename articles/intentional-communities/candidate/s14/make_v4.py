"""Section 14 draft v4 (2026-10-16): v3 with ending W2 (batch 303g: P6 with P7, P5 to P7 and the whole section all read Human)
and round r5's dispositions (two P2 fixes from its trace, one P3 fix from its cold reads) (review-r5/DISPOSITIONS-r5.md). Exact old -> new pairs on v3-W2.md; writes v4.md and
v4-fixes.json. Run from this folder: python3 make_v4.py"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
R5 = 'review-r5/DISPOSITIONS-r5.md'
FIX = [
 ("Who keeps childcare going and makes sure the kids continue to go to school?",
  "Who keeps childcare and schooling going?",
  'trace r5 T1: SHIFT, "makes sure the kids continue to go to school" narrowed schooling in any form (in the community, at '
  'home) to attending a school; the published "keeps childcare and schooling going"'),
 ("Who takes responsibility for tiding people over until they’re housed and settled again, including with outside cash or "
  "benefits, if relevant?",
  "Who takes responsibility for bridging people’s food, housing and care, and any outside cash or benefits, if relevant?",
  'trace r5 T1: LOST, v3\'s "tiding people over until they\'re housed and settled again" no longer named food, housing and '
  'care as what gets bridged, added an end point, and dropped "bridges", which P3\'s "bridge/successor" leans on. The '
  'published words back, as the trace\'s fix has them, with "people\'s" and "any" so that the paragraph doesn\'t carry two '
  'lists of three (linter E125)'),
 ("assign a bridge/successor for each critical function", "assign a bridge or successor for each critical function",
  'a repeated pause (both cold reads of round r5: "bridge/successor"): the published "Preassign a bridge or successor for each '
  'critical function", without the slash'),
]
t = (HERE / 'v3-W2.md').read_text(encoding='utf-8')
log = []
for old, new, why in FIX:
    assert t.count(old) == 1, old
    t = t.replace(old, new)
    log.append({'id': 'P3' if 'bridge/successor' in old else 'P2', 'old': old, 'new': new, 'why': why, 'disposition': R5})
(HERE / 'v4.md').write_text(t, encoding='utf-8')
(HERE / 'v4-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(log), 'changes; wrote v4.md')
