"""Section 16, Emulate round b (2026-10-17, after batch 328g): the paragraphs of v4 that read AI, each sent with its fixed
meaning (review round r4) so Emulate's sentences carry it and less goes back by hand.
- b01: H1-P1 alone and b02: H1-P1 with H1-P2. H1-P1 and H1-P2 together read AI (0.98,
  https://www.pangram.com/history/e76fc7b9-d9c3-443f-ae36-b97d5b91e528); H1-P2 with H1-P3 read Human (0.34), so H1-P1 is the
  one ("Most people building community do the steps in the wrong order.", round r4's fix, is the published claim).
- b03: H2-P2 with H2-P3. H2-P3 is the AI window of H2-P2 with H2-P3 (47 words,
  https://www.pangram.com/history/32c0bd47-eec5-4f81-b958-5115491b445b) and read AI with H2-P4 (0.55).
- b04: H2-P5 with H2-P6. H2-P6 can only be read with H2-P5, and their pair read Mixed: H2-P5's first four sentences AI
  (https://www.pangram.com/history/22374e6f-c4cc-447d-9eb5-1d24f37b4a5f), though H2-P5 alone read Human (0.09).
- b05: H3-P4, H3-P5 and H3-P6, the AI window of H3 (110 words, https://www.pangram.com/history/cf73ff95-0341-4230-8dd3-694e494cc3e6);
  each pair among H3-P3 to H3-P7 read AI (0.62 to 0.94).
Two calls each, plain text, on the laptop (emulate-runs/community-s16b). Run from this folder: python3 make_inputs.py"""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402
SKIP = re.compile(r'^(\[image \d+\]|\[caption\])')
bl = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 'v4.md').read_text(encoding='utf-8')) if b.strip()]
prose = [b for b in bl if not SKIP.match(b)]
IDS = (['H1'] + ['H1-P%d' % i for i in range(1, 4)] + ['H2'] + ['H2-P%d' % i for i in range(1, 7)] + ['H3'] +
       ['H3-P%d' % i for i in range(2, 12)])
assert len(prose) == len(IDS)
T = dict(zip(IDS, prose))
G = {'b01': ['H1-P1'], 'b02': ['H1-P1', 'H1-P2'], 'b03': ['H2-P2', 'H2-P3'], 'b04': ['H2-P5', 'H2-P6'],
     'b05': ['H3-P4', 'H3-P5', 'H3-P6']}
inputs = {k: '\n\n'.join(plain(T[p]) for p in v) for k, v in G.items()}
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'units.json').write_text(json.dumps(dict(G, source='v4')) + '\n', encoding='utf-8')
print({k: len(v.split()) for k, v in inputs.items()})
