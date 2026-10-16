"""Section 13, Emulate round j (2026-10-16, Joel's 34 a at 21:05 UTC: "34a and learn from how emulate fixes it"): the two
stretches that read AI inside the whole of v26 (batch 304g stage 2, https://www.pangram.com/history/9a7c5448-ae59-47ba-9133-72b1a8c76673),
each sent whole, as round i sent the land subsection, which then read Human.
- j01: H1-P3 and H1-P4 with the values subsection (its heading and H2-P1 to H2-P4), from v26. The section's first AI window
  (505 words) runs from H1-P3 ("Until that's happened, the group is still a circle of promising strangers") through it.
- j02: the last subsection (its heading and H5-P1 to H5-P4), from v26 (way A). The section's last AI window (323 words) runs
  from H5-P1's last sentence to the end, and the subsection reads AI as a whole both ways (304g).
Two calls each, plain text (links and italics come back afterwards); the headings and Joel's own sentences stay his whatever
Emulate does with them, and his meaning goes back in afterwards. Run from this folder: python3 make_inputs.py"""
import json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
bs = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 'v26.md').read_text(encoding='utf-8')) if b.strip()]
link = re.compile(r'\[([^\]]+)\]\([^)]+\)')
def plain(b):
    b = link.sub(r'\1', b)
    b = b.replace('*', '')
    return b[3:] if b.startswith('## ') else b
h2 = bs.index('## Please Choose the Values Before Falling in Love With the View')
h3 = bs.index('## Resources, Land, and Exit Terms')
h5 = bs.index('## When Somebody Has to Go')
assert bs[h2 - 2].startswith('Until that') and bs[h2 - 1].startswith('Along with that')
inputs = {'j01': '\n\n'.join(plain(b) for b in bs[h2 - 2:h3]),
          'j02': '\n\n'.join(plain(b) for b in bs[h5:])}
units = {'j01': ['H1-P3', 'H1-P4', 'heading', 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', 'v26'],
         'j02': ['heading', 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4', 'v26']}
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'units.json').write_text(json.dumps(units) + '\n', encoding='utf-8')
for k, v in inputs.items():
    print(k, len(v.split()), 'words', len(v.split('\n\n')), 'blocks')
