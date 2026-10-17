"""Section 16, Emulate round e (2026-10-17, after batch 344g): v10 db reads Human in every paragraph (paragraphs_alone PASS) and
in H1 as a whole (344g, 0.00), but the whole section reads AI over two stretches (344g, 0.44,
https://www.pangram.com/history/59fd7a4b-3f6f-4dda-85c0-4ef6207a2a0c), each sent whole in v10's meaning:
- e01: H2-P2 to H2-P4 (the forty acres, the inner pl/ork where you live, the group that practices for two years): 160 words AI
  inside the whole (with the caption before them), 120 in shapes dd and ed, though H2 read Human alone (340g, 0.32).
- e02: H3-P4 to H3-P6 (where to find them, the visit, what it teaches): 123 to 189 words AI inside the whole, and the end of
  H3-P5 with H3-P6 inside H3 (342g, 74 words).
Three calls each, plain text, on the laptop (emulate-runs/community-s16e). Run from this folder: python3 make_inputs.py"""
import json, pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402
subprocess.run([sys.executable, str(HERE.parent / 'make_v10.py'), 'db'], check=True, capture_output=True)
SKIP = re.compile(r'^(\[image \d+\]|\[caption\])')
bl = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 'v10.md').read_text(encoding='utf-8')) if b.strip()]
prose = [b for b in bl if not SKIP.match(b)]
IDS = (['H1'] + ['H1-P%d' % i for i in range(1, 4)] + ['H2'] + ['H2-P%d' % i for i in range(1, 7)] + ['H3'] +
       ['H3-P%d' % i for i in range(2, 12)])
assert len(prose) == len(IDS)
T = dict(zip(IDS, prose))
G = {'e01': ['H2-P2', 'H2-P3', 'H2-P4'], 'e02': ['H3-P4', 'H3-P5', 'H3-P6']}
CALLS = {'e01': 'ABC', 'e02': 'ABC'}
inputs = {k: '\n\n'.join(plain(T[p]) for p in v) for k, v in G.items()}
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=True, indent=1) + '\n', encoding='ascii')
(HERE / 'units.json').write_text(json.dumps(dict(G, calls=CALLS, source='v10 db')) + '\n', encoding='utf-8')
print({k: len(v.split()) for k, v in inputs.items()})
