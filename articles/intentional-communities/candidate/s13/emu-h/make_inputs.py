"""Section 13, Emulate round h (2026-10-15): H3-P1, the land-title paragraph, from draft v16. It reads Human alone
(https://www.pangram.com/history/8c9e35a5-e5ca-4d73-a590-2d9bdd4c47d3) and AI under its heading "Resources, Land, and Exit
Terms", twice with the same text and the same reading (292g https://www.pangram.com/history/9ac75023-1174-491a-a638-722dcbada762,
293g https://www.pangram.com/history/ef3cdc0c-fd0a-455e-8e68-1c0e7a9c147a). k01 is the heading with the paragraph, k02 the
paragraph alone. Two calls each, plain text; the heading stays Joel's whatever Emulate does with it.
Run from this folder: python3 make_inputs.py"""
import json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
bs = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 'v16.md').read_text(encoding='utf-8')) if b.strip()]
i = bs.index('## Resources, Land, and Exit Terms')
assert bs[i + 1].startswith('Who has the title to the land?')
inputs = {'k01': 'Resources, Land, and Exit Terms\n\n' + bs[i + 1], 'k02': bs[i + 1]}
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'units.json').write_text(json.dumps({'k01': ['heading', [2, 1], 'v16'], 'k02': [[2, 1], 'v16']}) + '\n', encoding='utf-8')
print(open(HERE / 'inputs.json', encoding='utf-8').read())
