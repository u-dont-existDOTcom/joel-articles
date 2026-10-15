"""Section 13, Emulate round f (2026-10-15): H5-P2 and H5-P4 from draft v11 (the same in v10), after both read AI in batch
291g: H5-P2 over its first 71 words (the opening, Joel's line and the first three questions, which carry the published
list nearly item by item; https://www.pangram.com/history/6f743823-7d92-4bb4-b576-368896475b56) and H5-P4 over its whole
length (https://www.pangram.com/history/8592c980-ad7c-4480-8f65-c44a1a4cd78a). Two calls each, plain text (the research
link is not in these two). Run from this folder: python3 make_inputs.py"""
import json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
bs = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 'v11.md').read_text(encoding='utf-8')) if b.strip()]
i = bs.index('## When Somebody Has to Go')
p2, p4 = bs[i + 2], bs[i + 4]
assert p2.startswith('That said,') and p4.startswith('Also pick a mediator')
inputs = {'i01': p2, 'i02': p4}
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'units.json').write_text(json.dumps({'i01': [[4, 2], 'v11'], 'i02': [[4, 4], 'v11']}) + '\n', encoding='utf-8')
for k, v in inputs.items(): print(k, len(v.split()), v[:80])
