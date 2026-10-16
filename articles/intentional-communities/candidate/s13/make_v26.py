"""Section 13 draft v26 (2026-10-16): v25 with a break back in H2-P2. Its v21 version, which passed Pangram with H2-P1 (batch
299g), had one ("Where are you still unsure?", march S B S in round r10); v23 merged its last two sentences to fix the
subsection's landing rate (linter B7/B13), and both march readings of rounds r16 and r17 then found no break (S S). The gate
blocks a fix that takes a paragraph's break (E173), so the break goes back mid-paragraph, where it doesn't end the paragraph on a
short line: "Long list, huh?", a remark about the list itself (E176). Both march readings of review-r18 see it (S B S) in the
subsection around it; the subsection lints REVIEW (landing rate 0.4). Exact old -> new pairs on v25 and v25b; writes v26.md,
v26b.md and v26-fixes.json. Run from this folder: python3 make_v26.py"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
FIX = [("Mark the places on your list where you're still unsure, too.",
        "Long list, huh? Mark the places on it where you're still unsure, too.",
        'the break H2-P2 lost in v23 (E173), as a remark about the list (E176); review-r18/MARCH-labels-h2a-a.txt and -b.txt: '
        'S B S', 'H2-P2')]
log = []
for src, out in (('v25.md', 'v26.md'), ('v25b.md', 'v26b.md')):
    t = (HERE / src).read_text(encoding='utf-8')
    for old, new, why, pid in FIX:
        assert t.count(old) == 1, (src, old)
        t = t.replace(old, new)
        if src == 'v25.md':
            log.append({'id': pid, 'old': old, 'new': new, 'why': why, 'disposition': 'review-r18 (march), this file'})
    (HERE / out).write_text(t, encoding='utf-8')
(HERE / 'v26-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(log), 'change(s); wrote v26.md, v26b.md')
