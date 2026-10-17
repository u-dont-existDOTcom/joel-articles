"""Section 16, Emulate round g (2026-10-17, while batch 346g runs): the two subsections sent whole, the way round d's call on the
whole opening made it read Human (344g, 0.00 to 0.16) where calls on parts of a subsection (rounds e and f) did not move the
whole section's windows (345g):
- g01: H2 whole (H2-P1 to H2-P6) in v12's meaning;
- g02: H3-P2 to H3-P8 (the first month's work to the nothing-to-sell paragraph; the father paragraph and the close read Human
  in every screen and stay).
Three calls each, plain text, on the laptop (emulate-runs/community-s16g). Run from this folder: python3 make_inputs.py"""
import json, pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402
subprocess.run([sys.executable, str(HERE.parent / 'make_v12.py')], check=True, capture_output=True)
SKIP = re.compile(r'^(\[image \d+\]|\[caption\])')
bl = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 'v12.md').read_text(encoding='utf-8')) if b.strip()]
prose = [b for b in bl if not SKIP.match(b)]
IDS = (['H1'] + ['H1-P%d' % i for i in range(1, 4)] + ['H2'] + ['H2-P%d' % i for i in range(1, 7)] + ['H3'] +
       ['H3-P%d' % i for i in range(2, 12)])
assert len(prose) == len(IDS)
T = dict(zip(IDS, prose))
G = {'g01': ['H2-P%d' % i for i in range(1, 7)], 'g02': ['H3-P%d' % i for i in range(2, 9)]}
CALLS = {'g01': 'ABC', 'g02': 'ABC'}
inputs = {k: '\n\n'.join(plain(T[p]) for p in v) for k, v in G.items()}
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=True, indent=1) + '\n', encoding='ascii')
(HERE / 'units.json').write_text(json.dumps(dict(G, calls=CALLS, source='v12')) + '\n', encoding='utf-8')
print({k: len(v.split()) for k, v in inputs.items()})
