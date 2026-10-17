"""Replace section 13 v31 in HUMANIZED-SO-FAR.md with draft v33 (2026-10-17), after every paragraph read Human alone (batches
312g, 314g and 316g; tools/humanization/paragraphs_alone.py must pass), the whole section read Human (316g), and the review rounds
r21 to r23 converged (their DISPOSITIONS files). Joel, 2026-10-16 23:38 UTC: his "if the community uses them" back, the
book not leaning on Christian's order, the dedup. Run from candidate/: python3 s13/install/install_s13_v33.py"""
import pathlib, subprocess, sys
C = pathlib.Path(__file__).resolve().parents[2]
REPO = C.parents[2]
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'paragraphs_alone.py'), str(C / 's13' / 'v33.md'),
                    str(C / 's13' / 'b316'), str(C / 's13' / 'b314'), str(C / 's13' / 'b312')], capture_output=True, text=True)
assert r.returncode == 0, 'every paragraph has to read Human alone first:\n' + r.stdout
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
H = '# Your Little Forming Group Already Is the Community'
note_a = art.index('<!-- CANDIDATE: section 13 v31')
a = art.index(H, note_a)
b = art.index('<!-- CANDIDATE: section 14', a)
v31 = (C / 's13' / 'v31.md').read_text(encoding='utf-8').strip()
assert art[a:b].strip() == v31, 'the article does not hold section 13 v31; stop'
v33 = (C / 's13' / 'v33.md').read_text(encoding='utf-8').strip()
note = ('<!-- CANDIDATE: section 13 v33 (2026-10-17): v31 with Joel\'s "if the community uses them" back (his 23:38 answer), '
        'the short visit\'s punchline replaced (the one paragraph that read AI alone, 312g), the book line pointing to the book '
        'for its nuts and bolts instead of its order (his 23:38 answer), the dedup he asked for, round r21\'s trace fixes and '
        'seven plainer phrases from the pause tally (s13/make_v32.py), then H2-P4 rewritten (the whole section\'s one AI window in '
        '314g) and the two repeats a reader would most notice cut (s13/make_v33.py). Records: s13/review-r1 to review-r23b '
        'with their DISPOSITIONS files; key-word check PASS (s13/preservation-keys.json); lint REVIEW. Pangram web app: every '
        'paragraph Human alone (312g, 314g, 316g; tools/humanization/paragraphs_alone.py PASS) and the whole section Human (316g). '
        'Not accepted until Joel says so. -->\n')
art = art[:note_a] + note + v33 + '\n\n' + art[b:]
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
print('installed section 13 v33')
