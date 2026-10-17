"""Section 15, Emulate round e (2026-10-17, after batch 330g): H1-P4 read AI alone in both of v8's shapes with the published
"often go through" back (g 0.94, https://www.pangram.com/history/450082a7-13ba-4d19-8e9b-e00aedad18a2; m 0.91,
https://www.pangram.com/history/1d5121dc-9bfc-4470-909e-f09e8ef02046), and inside H1 too. Round d's shape c read Human (0.54)
but said the family takes care of "so much" (trace r7 T1). So the fixed meaning goes back to Emulate (the gate's lesson of
2026-10-17: "if the fix reads AI the fixed meaning goes back to Emulate").
- e01: H1-P4 (v8 g) alone.
- e02: H1-P3 and H1-P4 together (H1-P3 read Human; the pair gives Emulate the run-up).
Two calls each, plain text, on the laptop (emulate-runs/community-s15e). Run from this folder: python3 make_inputs.py"""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402
bs = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 'v9.md').read_text(encoding='utf-8')) if b.strip()]
p3 = [b for b in bs if b.startswith('And the humor!')][0]
p4 = [b for b in bs if b.startswith('In the villages and families')][0]
inputs = {'e01': plain(p4), 'e02': plain(p3) + '\n\n' + plain(p4)}
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'units.json').write_text(json.dumps({'e01': ['H1-P4'], 'e02': ['H1-P3', 'H1-P4'], 'source': 'v9'}) + '\n', encoding='utf-8')
print({k: len(v.split()) for k, v in inputs.items()})
