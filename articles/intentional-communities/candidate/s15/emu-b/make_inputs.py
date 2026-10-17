"""Section 15, Emulate round b (2026-10-17, after batch 322g): the stretches of draft v2 that read AI, each sent whole, as
section 13's rounds i and j sent theirs (the stretch then read Human). Plain text (links as their words, no emphasis), without
the images, captions and the page's embed lines; the headings stay Joel's whatever Emulate does with them, and his meaning
goes back in afterwards, inside Emulate's sentences.
- t01: H1-P4 (the villages, the workshop and the aunt). AI alone (0.99, https://www.pangram.com/history/15d5e4a5-3566-4637-bb21-83c126acae96),
  and its second half is the 33-word AI window inside H1 (https://www.pangram.com/history/7d9018c6-0801-42bb-b0ba-ecf1536eef00).
- t02: the subsection "All is not well in paradise", its heading and H2-P1 to H2-P7. Two AI windows inside it (190 words from
  the heading through P3, 75 from P6's second sentence through P7; https://www.pangram.com/history/bb201de7-6ea6-478a-8789-0f55b30489cb);
  P1 with P2 has a 38-word AI window (https://www.pangram.com/history/3e196978-04b5-4d9f-9210-81ffa3e8f059), P3 with P4 reads AI (0.99).
- t03: the subsection "Lessons from the Black Tax", its heading and H3-P1 to H3-P8. A 646-word AI window from the heading
  through P7 (https://www.pangram.com/history/2363a5c6-0532-44e4-9c82-099d022ab2c6); P1 to P5 and P7 read AI alone.
Two calls each, A and B, on the laptop (emulate-runs/community-s15b). Run from this folder: python3 make_inputs.py"""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402
SKIP = re.compile(r'^(\[image \d+\]|\[caption\]|\[Professor Baby Sheep|Double click to interact with video)')
bl = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 'v2.md').read_text(encoding='utf-8')) if b.strip()]
keep = [b for b in bl if not SKIP.match(b)]
names = ['H1'] + ['H1-P%d' % i for i in range(1, 6)] + ['H2'] + ['H2-P%d' % i for i in range(1, 8)] + ['H3'] + \
        ['H3-P%d' % i for i in range(1, 9)]
assert len(keep) == len(names), (len(keep), len(names))
B = dict(zip(names, keep))
assert B['H2'] == '## All is not well in paradise' and B['H3'] == '## Lessons from the Black Tax'
assert B['H1-P4'].startswith('In the villages') and B['H2-P7'].startswith('But the old') and B['H3-P8'].startswith('Oh, and')
units = {'t01': ['H1-P4'], 't02': ['H2'] + ['H2-P%d' % i for i in range(1, 8)], 't03': ['H3'] + ['H3-P%d' % i for i in range(1, 9)]}
inputs = {k: '\n\n'.join(plain(B[n].lstrip('#').strip()) for n in v) for k, v in units.items()}
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'units.json').write_text(json.dumps(dict(units, source='v2')) + '\n', encoding='utf-8')
for k, v in inputs.items():
    print(k, len(v.split()), 'words')
