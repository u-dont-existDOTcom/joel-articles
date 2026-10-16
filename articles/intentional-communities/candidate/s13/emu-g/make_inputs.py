"""Section 13, Emulate round g (2026-10-15): H1-P2, the conflict paragraph, from draft v14. Round e's version (v12, with
the published meaning put back) reads Human beside H1-P1 (https://www.pangram.com/history/c54b25d8-1c62-479d-bdbd-d775a1de6dbb)
and AI alone (https://www.pangram.com/history/200f9c1d-79c6-4f49-8223-503258cec054), so a fresh round from it: j01 is the
paragraph alone, j02 is it after H1-P1, as round e had it. Two calls each, plain text. Run from this folder:
python3 make_inputs.py"""
import json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
bs = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 'v14.md').read_text(encoding='utf-8')) if b.strip()]
assert bs[0].startswith('# Your Little') and bs[1].startswith("Don't worry") and bs[2].startswith("Don't even think")
inputs = {'j01': bs[2], 'j02': bs[1] + '\n\n' + bs[2]}
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'units.json').write_text(json.dumps({'j01': [[0, 2], 'v14'], 'j02': [[0, 1], [0, 2], 'v14']}) + '\n', encoding='utf-8')
print(inputs['j02'])
