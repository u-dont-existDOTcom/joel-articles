"""Section 16, Emulate round c (2026-10-17, after batch 337g): the three stretches that read AI inside the whole section (337g,
https://www.pangram.com/history/f59dcec4-f2b8-4a60-9d02-a160433641d0, 0.54), each sent whole with its fixed meaning (v6, with
H1-P2 as in v5) so Emulate rewrites the stretch as one piece; section 13's lesson (2026-10-16): a stretch that passes only
paragraph by paragraph has to pass as a stretch.
- c01: the heading and H1 whole (H1-P1 to H1-P3): its opening read AI in every shape (328g, 333g, 337g).
- c02: H2-P2 to H2-P5 (the forty acres to the remote reader's list): 165 words AI inside the whole, though each pair read Human.
- c03: H3-P3 to H3-P6 (the practice group to the visit): 114 words AI inside the whole and in H3, and H3-P4 AI with each neighbor.
Two calls each, plain text, on the laptop (emulate-runs/community-s16c). Run from this folder: python3 make_inputs.py"""
import json, pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402
subprocess.run([sys.executable, str(HERE.parent / 'make_v6.py')], check=True, capture_output=True)
SKIP = re.compile(r'^(\[image \d+\]|\[caption\])')
bl = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 'v6.md').read_text(encoding='utf-8')) if b.strip()]
prose = [b for b in bl if not SKIP.match(b)]
IDS = (['H1'] + ['H1-P%d' % i for i in range(1, 4)] + ['H2'] + ['H2-P%d' % i for i in range(1, 7)] + ['H3'] +
       ['H3-P%d' % i for i in range(2, 12)])
assert len(prose) == len(IDS)
T = dict(zip(IDS, prose))
V5P2 = json.loads((HERE.parent / 'v6-fixes.json').read_text(encoding='utf-8'))[0]['old']
T['H1-P2'] = T['H1-P2'].replace(json.loads((HERE.parent / 'v6-fixes.json').read_text(encoding='utf-8'))[0]['new'], V5P2)
G = {'c01': ['H1', 'H1-P1', 'H1-P2', 'H1-P3'], 'c02': ['H2-P2', 'H2-P3', 'H2-P4', 'H2-P5'],
     'c03': ['H3-P3', 'H3-P4', 'H3-P5', 'H3-P6']}
inputs = {k: '\n\n'.join(plain(T[p].lstrip('#').strip()) for p in v) for k, v in G.items()}
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'units.json').write_text(json.dumps(dict(G, source='v6, H1-P2 as in v5')) + '\n', encoding='utf-8')
print({k: len(v.split()) for k, v in inputs.items()})
