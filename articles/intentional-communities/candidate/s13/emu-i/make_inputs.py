"""Section 13, Emulate round i (2026-10-15, after batch 299g): the two stretches that read AI in every context they were checked in,
each sent whole so Emulate rewrites the run, not one paragraph at a time.
- l01: the land subsection, heading and H3-P1 to H3-P5 from v21. It reads 100% AI as a whole (299g,
  https://www.pangram.com/history/0b7c2345-0629-47ef-b66a-75f5f9be2e22) and inside the section's first AI window (298g,
  https://www.pangram.com/history/5e450ea7-ed52-402b-bae4-de06d266aec7), though each paragraph reads Human alone.
- l02: H4-P9, the heading "When Somebody Has to Go", H5-P1 and H5-P2 from v21. 100% AI as a stretch (299g,
  https://www.pangram.com/history/edf0cb54-e5f7-428f-8e37-253d2954eea1) and the section's second AI window.
Two calls each, plain text; the headings stay Joel's whatever Emulate does with them, and his meaning goes back in afterwards.
Run from this folder: python3 make_inputs.py"""
import json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
bs = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 'v21.md').read_text(encoding='utf-8')) if b.strip()]
link = re.compile(r'\[([^\]]+)\]\([^)]+\)')
def plain(b):
    b = link.sub(r'\1', b)
    b = b.replace('*', '')
    return b[3:] if b.startswith('## ') else b
h3 = bs.index('## Resources, Land, and Exit Terms')
h4 = bs.index('## From Visitor to Member—Slowly')
h5 = bs.index('## When Somebody Has to Go')
assert bs[h3 + 1].startswith('Who has the title to the land?') and bs[h4 - 1].startswith('For the full sequence')
assert bs[h5 - 1].startswith('Do visitors, volunteers') and bs[h5 + 2].startswith('On the other hand')
inputs = {'l01': '\n\n'.join(plain(b) for b in bs[h3:h4]),
          'l02': '\n\n'.join(plain(b) for b in bs[h5 - 1:h5 + 3])}
units = {'l01': ['heading', 'H3-P1', 'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', 'v21'],
         'l02': ['H4-P9', 'heading', 'H5-P1', 'H5-P2', 'v21']}
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'units.json').write_text(json.dumps(units) + '\n', encoding='utf-8')
for k, v in inputs.items():
    print(k, len(v.split()), 'words')
    print(v)
    print()
