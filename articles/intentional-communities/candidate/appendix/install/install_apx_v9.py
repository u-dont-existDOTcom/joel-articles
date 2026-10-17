"""Put the appendix draft v9 in HUMANIZED-SO-FAR.md in place of the published appendix (2026-10-17), after every entry read
Human alone, with its neighbor under its heading, or in the shortest run Pangram can read (tools/humanization/paragraphs_alone.py
must pass over the appendix batches 329g to 343g) and the whole appendix read 100% Human (343g:
appendix/b343/b343-results.json, key APXv9). Joel, 2026-10-17 02:07 UTC: "continue, and don't stop because this is overnight
run". The appendix runs to the end of the article. Run from candidate/: python3 appendix/install/install_apx_v9.py"""
import json, pathlib, subprocess, sys
C = pathlib.Path(__file__).resolve().parents[2]
REPO = C.parents[2]
APX = C / 'appendix'
BATCHES = sorted(str(p) for p in APX.glob('b3*') if (p / 'drafts.json').exists())
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'paragraphs_alone.py'), str(APX / 'v9.md')] + BATCHES,
                   capture_output=True, text=True)
assert r.returncode == 0, 'every entry has to read Human in its run first:\n' + r.stdout
res = json.loads((APX / 'b343' / 'b343-results.json').read_text(encoding='utf-8'))['APXv9']
assert res[0].startswith('Human') and all(w.startswith('Human') for w in res[3].split('; ')), ('the whole appendix', res)
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
H = '# Appendix: Watch These, Then Read These'
a = art.index(H)
v0 = (APX / 'v0.md').read_text(encoding='utf-8').strip()
assert art[a:].strip() == v0, 'the article does not hold the published appendix; stop'
v9 = (APX / 'v9.md').read_text(encoding='utf-8').strip()
note = ('<!-- CANDIDATE: the appendix v9 (2026-10-17, the overnight run): Emulate round a (appendix/emu-a) for the entries, the '
        'published meaning put back (appendix/make_v1.py to make_v9.py), meaning rounds r7, r12, r12x, r14 and r16 (traces of '
        'every entry, a cold read, the stance check) with their DISPOSITIONS files. Pangram web app: every entry Human in its '
        'run (329g to 343g; tools/humanization/paragraphs_alone.py PASS, list entries in the shortest run Pangram can read) and '
        'the whole appendix 100% Human (343g). The breaks in the list are question 41 for Joel. Not accepted until Joel says '
        'so. -->\n')
art = art[:a] + note + v9 + '\n'
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
print('installed the appendix v9')
