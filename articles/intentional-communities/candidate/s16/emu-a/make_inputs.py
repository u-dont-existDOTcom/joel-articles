"""Section 16, Emulate round a (2026-10-17): the published section whole, "Practice Comes Before Property", its heading, two
subheadings and nineteen paragraphs as plain text (links as their words, no emphasis), without the two images and the caption
(which stays as published). Two calls, A and B, on the laptop (emulate-runs/community-s16a). The headings stay Joel's whatever
Emulate does with them; his meaning goes back in afterwards, inside Emulate's sentences, and the repeats check's dedup
(../review-r1/) decides which repeated points stay. Run from this folder: python3 make_inputs.py"""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402
SKIP = re.compile(r'^(\[image \d+\]|\[caption\])')
bl = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 'v0.md').read_text(encoding='utf-8')) if b.strip()]
keep = [b for b in bl if not SKIP.match(b)]
inputs = {'s01': '\n\n'.join(plain(b.lstrip('#').strip()) for b in keep)}
units = {'s01': ['H1'] + ['H1-P%d' % i for i in range(1, 4)] + ['H2'] + ['H2-P%d' % i for i in range(1, 7)] + ['H3'] +
                ['H3-P%d' % i for i in range(1, 12)]}
assert len(keep) == len(units['s01']), (len(keep), len(units['s01']))
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'units.json').write_text(json.dumps(units) + '\n', encoding='utf-8')
for k, v in inputs.items():
    print(k, len(v.split()), 'words')
