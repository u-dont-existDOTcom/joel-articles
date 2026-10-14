"""Section 11 v13 (2026-10-12): v12 with P5c, from the sweep for the kind of break Joel found in section 12 at 05:33
(sweep-20261012/sweep-G7.md): P5's "If it needs the founder's “blessing”" had lost the published "every" and "still"
("If every adaptation still needs the founder's approval"), with an "it" that had no clear target. Run from candidate/."""
import json, pathlib
C = pathlib.Path(__file__).resolve().parents[2]
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
old = json.loads((C / 's11/fix-v3-parts.json').read_text(encoding='utf-8'))['P5e']
new = json.loads((C / 's11/fix-v26-parts.json').read_text(encoding='utf-8'))['P5c']
assert art.count(old) == 1, 'section 11 P5 is not as v12 has it; stop'
art = art.replace(old, new)
mark = '<!-- CANDIDATE: section 11 v12 (2026-10-12)'
assert art.count(mark) == 1
art = art.replace(mark, '<!-- 2026-10-12: section 11 v13 = v12 with P5c ("If every change they make still needs the founder\'s “blessing”"; the '
                  'published "every" and "still" back, found by the sweep in sweep-20261012/). The section 100% Human (1,686 words, '
                  '07:46:55 UTC, batch 267g), P5c with P4 100% Human (268g); s11/PREDICTIONS-s11.md. -->\n' + mark)
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
print('installed section 11 v13')
