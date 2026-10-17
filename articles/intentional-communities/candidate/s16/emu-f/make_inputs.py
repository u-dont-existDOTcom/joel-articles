"""Section 16, Emulate round f (2026-10-17, after batch 345g): v11 (a, a) reads Human in every paragraph and pair but the whole
section reads AI over two windows that round e's rewrites did not move (345g, 0.45,
https://www.pangram.com/history/3f5d0143-1cd5-4bfb-b1a7-7b640db7b950), each sent whole as Pangram windowed it:
- f01: H2-P3 to H2-P5 (the inner pl/ork where you live, the group that may never own land, what remote readers can build):
  116 to 127 words AI in every shape (345g), three list-shaped paragraphs in a row.
- f02: H3-P5 to H3-P8 (the visit, what it teaches, the land, nothing to sell): 141 words AI in shape a, 218 inside H3.
Three calls each, plain text, on the laptop (emulate-runs/community-s16f). Run from this folder: python3 make_inputs.py"""
import json, pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402
subprocess.run([sys.executable, str(HERE.parent / 'make_v11.py'), 'a', 'a'], check=True, capture_output=True)
SKIP = re.compile(r'^(\[image \d+\]|\[caption\])')
bl = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 'v11.md').read_text(encoding='utf-8')) if b.strip()]
prose = [b for b in bl if not SKIP.match(b)]
IDS = (['H1'] + ['H1-P%d' % i for i in range(1, 4)] + ['H2'] + ['H2-P%d' % i for i in range(1, 7)] + ['H3'] +
       ['H3-P%d' % i for i in range(2, 12)])
assert len(prose) == len(IDS)
T = dict(zip(IDS, prose))
G = {'f01': ['H2-P3', 'H2-P4', 'H2-P5'], 'f02': ['H3-P5', 'H3-P6', 'H3-P7', 'H3-P8']}
CALLS = {'f01': 'ABC', 'f02': 'ABC'}
inputs = {k: '\n\n'.join(plain(T[p]) for p in v) for k, v in G.items()}
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=True, indent=1) + '\n', encoding='ascii')
(HERE / 'units.json').write_text(json.dumps(dict(G, calls=CALLS, source='v11 a a')) + '\n', encoding='utf-8')
print({k: len(v.split()) for k, v in inputs.items()})
