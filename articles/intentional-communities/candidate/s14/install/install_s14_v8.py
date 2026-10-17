"""Replace section 14 v5 in HUMANIZED-SO-FAR.md with draft v8 (2026-10-17), after every paragraph read Human alone (batches
315g, 313g, 306g, 305g; tools/humanization/paragraphs_alone.py must pass) and the whole section read Human (316g, 0.17: s13/b316/b316-results.json, key S14v8). Joel,
2026-10-16 23:38 UTC: "let's merge/dedup section 14 without losing important things pls". Run from candidate/:
python3 s14/install/install_s14_v8.py"""
import pathlib, subprocess, sys
C = pathlib.Path(__file__).resolve().parents[2]
REPO = C.parents[2]
S14 = C / 's14'
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'paragraphs_alone.py'), str(S14 / 'v8.md')] +
                   [str(S14 / d) for d in ('b315', 'b313', 'b306', 'b305')], capture_output=True, text=True)
assert r.returncode == 0, 'every paragraph has to read Human alone first:\n' + r.stdout
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
H, NEXT = '# Dissolution and Exit', '# What This Looks Like From Sénégal'
note_a = art.index('<!-- CANDIDATE: section 14 v5')
a = art.index(H, note_a); b = art.index(NEXT, a)
v5 = (S14 / 'v5.md').read_text(encoding='utf-8').strip()
assert art[a:b].strip() == v5, 'the article does not hold section 14 v5; stop'
v8 = (S14 / 'v8.md').read_text(encoding='utf-8').strip()
note = ('<!-- CANDIDATE: section 14 v8 (2026-10-17): v5 deduplicated at Joel\'s word (2026-10-16 23:38 UTC): the last paragraph\'s point in P5, P2 kept as in v5 after two '
        'shorter versions read AI alone (313g, 315g), and "The Farm\'s communal economy" (a repeated pause) '
        '(s14/make_v6.py to make_v8.py). Records: s14/review-r1 to '
        'review-r6 with their DISPOSITIONS files; key-word check PASS; lint REVIEW. Pangram web app: every paragraph Human alone '
        '(305g-x, 315g; tools/humanization/paragraphs_alone.py PASS) and the whole section Human (316g). Not accepted '
        'until Joel says so. -->\n')
art = art[:note_a] + note + v8 + '\n\n' + art[b:]
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
print('installed section 14 v8')
