"""Section 16 draft v4 (2026-10-17): v3 with the fixes of trace T9 of review round r4 (review-r4/trace-T9.md) for H3-P10:
- "help build" made readers helpers, not builders (published: "Maybe somebody will build"): "will build";
- "something good" lost the published "useful": "something useful";
- "Maybe you'll teach someone else" lost "that community" (published: "Maybe that community will teach somebody who builds
  another"), so the readers became the teachers and what gets built stopped being a community: "Maybe that community will
  teach someone else".
Writes v4.md and v4-fixes.json. Run from this folder: python3 make_v4.py"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
t = (HERE / 'v3.md').read_text(encoding='utf-8')
FIX = [
 ('H3-P10', "Maybe some of you will help build something good from this. Maybe you'll teach someone else, who'll build another.",
  "Maybe some of you will build something useful from this. Maybe that community will teach someone else, who'll build "
  "another.",
  'trace T9: the published "will build" and "something useful"; "that community" back as the one that teaches'),
]
log = []
for pid, old, new, why in FIX:
    assert t.count(old) == 1, (pid, old[:50])
    t = t.replace(old, new)
    log.append({'id': pid, 'old': old, 'new': new, 'why': why})
(HERE / 'v4.md').write_text(t, encoding='utf-8')
(HERE / 'v4-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v4.md', len(log), 'fixes')
