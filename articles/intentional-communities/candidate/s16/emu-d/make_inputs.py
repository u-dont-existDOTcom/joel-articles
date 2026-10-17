"""Section 16, Emulate round d (2026-10-17, after batch 340g): the two stretches still reading AI, each sent whole in v8's
meaning so Emulate rewrites the stretch as one piece.
- d01: the heading and H1 whole, in shape e and y (v8 e y): H1-P1 with H1-P2 read Human (340g, 0.46), but H1 read AI in every
  shape (0.88 to 0.95), and H1-P2 with H1-P3 too (0.63 to 0.86; v4's H1-P3 had read Human with H1-P2, 328g, 0.34). Four calls.
- d02: H3-P5 to H3-P7 (the visit, what it teaches, the land): H3 read AI over the end of H3-P5 and H3-P6 (340g, 73 words), and
  H3-P6 with H3-P7 read AI (0.34) once trace r13 T3's fix took out its "Or". Three calls.
Plain text, on the laptop (emulate-runs/community-s16d). Run from this folder: python3 make_inputs.py"""
import json, pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402
subprocess.run([sys.executable, str(HERE.parent / 'make_v8.py'), 'e', 'y'], check=True, capture_output=True)
SKIP = re.compile(r'^(\[image \d+\]|\[caption\])')
bl = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 'v8.md').read_text(encoding='utf-8')) if b.strip()]
prose = [b for b in bl if not SKIP.match(b)]
IDS = (['H1'] + ['H1-P%d' % i for i in range(1, 4)] + ['H2'] + ['H2-P%d' % i for i in range(1, 7)] + ['H3'] +
       ['H3-P%d' % i for i in range(2, 12)])
assert len(prose) == len(IDS)
T = dict(zip(IDS, prose))
G = {'d01': ['H1', 'H1-P1', 'H1-P2', 'H1-P3'], 'd02': ['H3-P5', 'H3-P6', 'H3-P7']}
CALLS = {'d01': 'ABCD', 'd02': 'ABC'}
inputs = {k: '\n\n'.join(plain(T[p].lstrip('#').strip()) for p in v) for k, v in G.items()}
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=True, indent=1) + '\n', encoding='ascii')
(HERE / 'units.json').write_text(json.dumps(dict(G, calls=CALLS, source='v8 e y')) + '\n', encoding='utf-8')
print({k: len(v.split()) for k, v in inputs.items()})
