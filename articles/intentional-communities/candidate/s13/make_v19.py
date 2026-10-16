"""Section 13 draft v19 (2026-10-15): v18 with H3-P1 in way B (v17b.md: Emulate round h's sentences with the meaning put
back), the one way that read Human under "Resources, Land, and Exit Terms" in batch 294g. Writes v19.md and v19-fixes.json.
Run from this folder: python3 make_v19.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


v18, v17b = blocks((HERE / 'v18.md').read_text(encoding='utf-8')), blocks((HERE / 'v17b.md').read_text(encoding='utf-8'))
i = v18.index('## Resources, Land, and Exit Terms') + 1
assert v17b.index('## Resources, Land, and Exit Terms') + 1 == i
old, new = v18[i], v17b[i]
out = list(v18)
out[i] = new
(HERE / 'v19.md').write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v19-fixes.json').write_text(json.dumps([{'id': 'H3-P1', 'old': old, 'new': new,
    'why': 'batch 294g: way B reads Human alone (https://www.pangram.com/history/844e3252-d579-40cb-a74b-450334a0e899) and '
           'under its heading (https://www.pangram.com/history/71bcef45-586a-4fec-bc6c-f6c84786ca8f); ways A and C read AI '
           'under the heading'}], ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(new)
