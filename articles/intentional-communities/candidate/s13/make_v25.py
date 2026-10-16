"""Section 13 draft v25 (2026-10-16): v24 with the fixes round r17 called for (review-r17/DISPOSITIONS-r17.md). Under the
convergent-review rule a new finding on unchanged words is fixed only when the fix puts back the published words or makes the
sentence plain and loses nothing; these do. Exact old -> new pairs on v24 and v24b (way B of H5-P2). Writes v25.md,
v25b.md and v25-fixes.json. Run from this folder: python3 make_v25.py"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
R17 = 'review-r17/DISPOSITIONS-r17.md'
FIX = [
 ("Even giving it six months will give you more data, but there’s still no “good person” detector.",
  "Six months will give you more data, but there’s still no “good person” detector.",
  'trace r17 T4: "it" in "giving it six months" had no noun in reach (vibes? a stage? the person?), so a reader could take '
  'six months for something other than watching people. The published "Six months gives you a larger sample; it does not '
  'validate a "good person" detector." has no "it"; its subject back, and the rest of the sentence unchanged', 'H4-P6'),
 ("Along with that, you'll also need to budget for what the group can provide on the practical side.",
  "Along with that, you'll also need a budget of what the group can provide on the practical side.",
  'a repeated pause (cold reads r16 a and r17 b: "budget for what the group can provide"): "budget for" reads as setting '
  'money aside for something, where the published "Do the boring capacity budget too" is a tally of what the group has. '
  'The published noun back, nothing else', 'H1-P4'),
 ("They should have clear terms, and the chance to be heard",
  "All of them should have clear terms, and the chance to be heard",
  'a repeated pause (validation read V1 and cold read r17 b: "They should have clear terms"): after "(yes, even interns!)" '
  'and "Why wouldn\'t they be?", "They" could be the interns alone; the published "they need clear terms" is about all '
  'five groups, which "All of them" says', 'H4-P9'),
]
log = []
for src, out in (('v24.md', 'v25.md'), ('v24b.md', 'v25b.md')):
    t = (HERE / src).read_text(encoding='utf-8')
    for old, new, why, pid in FIX:
        assert t.count(old) == 1, (src, old)
        t = t.replace(old, new)
        if src == 'v24.md':
            log.append({'id': pid, 'old': old, 'new': new, 'why': why, 'disposition': R17})
    (HERE / out).write_text(t, encoding='utf-8')
(HERE / 'v25-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(log), 'change(s); wrote v25.md, v25b.md')
