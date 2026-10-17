"""Section 15 draft v12 (2026-10-17): v9 with H1-P4 as round d's shape c, the only one of eleven that reads Human alone
(327g: 0.54 alone, 0.30 in H1). Ten shapes that keep the published "often pass through" read AI alone (326g, 327g, 330g,
332g, 335g). Trace r7 T1 called c's "so much is taken care of by" a SHIFT (a large share handled, for "often pass
through"); Emulate wrote the same reading from the published sentence in rounds a, d and e. The choice is Joel's (questions
page, question 40); c is in until he answers. Writes v12.md. Run from this folder: python3 make_v12.py"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
subprocess.run([sys.executable, str(HERE / 'make_v9.py'), 'g'], check=True, capture_output=True)
t = (HERE / 'v9.md').read_text(encoding='utf-8')
G = json.loads((HERE / 'v8-variants.json').read_text(encoding='utf-8'))['H1-P4']['g']
C = json.loads((HERE / 'v6-variants.json').read_text(encoding='utf-8'))['H1-P4']['c']
assert t.count(G) == 1
(HERE / 'v12.md').write_text(t.replace(G, C), encoding='utf-8')
print('wrote v12.md with H1-P4 c')
