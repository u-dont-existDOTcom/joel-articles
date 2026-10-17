"""Put section 15 draft v12 in HUMANIZED-SO-FAR.md in place of the published section (2026-10-17), after every paragraph read
Human alone (tools/humanization/paragraphs_alone.py must pass over batches 322g to 335g) and the whole section read Human
(338g: s15/b338/b338-results.json, key S15v12, 100% Human). Joel, 2026-10-17 02:07 UTC: "continue, and don't stop because
this is overnight run". H1-P4 is round d's shape c until Joel answers question 40. Run from candidate/:
python3 s15/install/install_s15_v12.py"""
import json, pathlib, subprocess, sys
C = pathlib.Path(__file__).resolve().parents[2]
REPO = C.parents[2]
S15 = C / 's15'
BATCHES = sorted(str(p) for p in S15.glob('b3*') if (p / 'drafts.json').exists())
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'paragraphs_alone.py'), str(S15 / 'v12.md')] + BATCHES,
                   capture_output=True, text=True)
assert r.returncode == 0, 'every paragraph has to read Human alone first:\n' + r.stdout
res = json.loads((S15 / 'b338' / 'b338-results.json').read_text(encoding='utf-8'))['S15v12']
assert res[0].startswith('Human') and all(w.startswith('Human') for w in res[3].split('; ')), ('the whole section', res)
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'preservation_keys.py'), str(S15 / 'preservation-keys.json'),
                    str(S15 / 'v12.md')], capture_output=True, text=True)
assert 'verdict: PASS' in r.stdout, r.stdout
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
H, NEXT = '# What This Looks Like From Sénégal', '# Practice Comes Before Property'
a = art.index(H); b = art.index(NEXT, a)
v0 = (S15 / 'v0.md').read_text(encoding='utf-8').strip()
assert art[a:b].strip() == v0, 'the article does not hold the published section 15; stop'
v12 = (S15 / 'v12.md').read_text(encoding='utf-8').strip()
note = ('<!-- CANDIDATE: section 15 v12 (2026-10-17, the overnight run): Emulate rounds a to e (s15/emu-a to emu-e) with the '
        'published meaning put back (s15/make_v1.py to make_v12.py), meaning rounds r1 to r8 with their DISPOSITIONS files, '
        'key-word check PASS, lint REVIEW. Pangram web app: every paragraph Human alone (322g to 335g; '
        'tools/humanization/paragraphs_alone.py PASS) and the whole section 100% Human (338g). H1-P4 is round d\'s shape c '
        '("so much is taken care of by"), the only one of eleven that reads Human alone; trace r7 called it a shift from the '
        'published "often pass through", so it is question 40 for Joel. Not accepted until Joel says so. -->\n')
art = art[:a] + note + v12 + '\n\n' + art[b:]
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
print('installed section 15 v12')
