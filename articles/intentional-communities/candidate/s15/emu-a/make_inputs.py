"""Section 15, Emulate round a (2026-10-17): the published section whole, "What This Looks Like From Sénégal", its heading,
two subheadings and twenty paragraphs as plain text (links as their words, no emphasis), without the images, the two captions
(which stay as published) and the page's embed lines ("[image 21]", the Professor Baby Sheep link card, "Double click to
interact with video"). Two calls, A and B, on the laptop (emulate-runs/community-s15a). The headings stay Joel's whatever
Emulate does with them; his meaning goes back in afterwards, inside Emulate's sentences.
Run from this folder: python3 make_inputs.py"""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402
SKIP = re.compile(r'^(\[image \d+\]|\[caption\]|\[Professor Baby Sheep|Double click to interact with video)')
bl = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 'v0.md').read_text(encoding='utf-8')) if b.strip()]
keep = [b for b in bl if not SKIP.match(b)]
inputs = {'s01': '\n\n'.join(plain(b) for b in keep)}
units = {'s01': ['H1'] + ['H1-P%d' % i for i in range(1, 6)] + ['H2'] + ['H2-P%d' % i for i in range(1, 8)] + ['H3'] +
                ['H3-P%d' % i for i in range(1, 9)]}
assert len(keep) == len(units['s01']), (len(keep), len(units['s01']))
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'units.json').write_text(json.dumps(units) + '\n', encoding='utf-8')
for k, v in inputs.items():
    print(k, len(v.split()), 'words')
