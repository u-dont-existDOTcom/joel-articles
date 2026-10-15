"""Section 13, Emulate round e (2026-10-15): H1-P1 and H1-P2 as one unit, from draft v9. v9's H1-P2 (round b's e01-emuB
with the published meaning put back) read AI-Generated over its whole length in batch 289g
(https://www.pangram.com/history/4326944e-db0c-4ea5-a531-cef3d978ef00): its three middle sentences had become nearly
the published ones. A fresh round from the meaning-faithful v9 needs fewer words put back. Two calls, plain text.
Run from this folder: python3 make_inputs.py"""
import json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
bs = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 'v9.md').read_text(encoding='utf-8')) if b.strip()]
assert bs[0].startswith('# Your Little') and bs[1].startswith("Don't worry") and bs[2].startswith("Don't combine")
inputs = {'h01': bs[1] + '\n\n' + bs[2]}
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'units.json').write_text(json.dumps({'h01': [[0, 1], [0, 2], 'v9']}) + '\n', encoding='utf-8')
print(inputs['h01'])
