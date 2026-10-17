"""Section 15, Emulate round d (2026-10-17, after batch 326g): the two paragraphs of v5 that read AI alone after round r4's
meaning fixes, each sent with its fixed meaning so Emulate's sentences carry it and less goes back by hand.
- d01: H1-P4 alone (0.63, https://www.pangram.com/history/450bed2b-5f14-4d43-95da-0c3d3ec84536); its variant s read 0.56.
- d02: H1-P3 and H1-P4 together (H1-P3 read Human; the pair gives Emulate the run-up).
- d03: H3-P2 alone (0.49, https://www.pangram.com/history/0a8b17d6-927f-4f87-832c-53bcdea2f18c); its second sentence is the
  51-word AI window inside H3 (https://www.pangram.com/history/b23ced61-c7ba-4362-b5a6-3557cbd66d9a).
Two calls each, plain text, on the laptop (emulate-runs/community-s15d). Run from this folder: python3 make_inputs.py"""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402
bs = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 'v5.md').read_text(encoding='utf-8')) if b.strip()]
p3 = [b for b in bs if b.startswith('And the humor!')][0]
p4 = [b for b in bs if b.startswith('In the villages and families')][0]
h3p2 = [b for b in bs if b.startswith('The problem is that it can be soul destroying')][0]
inputs = {'d01': plain(p4), 'd02': plain(p3) + '\n\n' + plain(p4), 'd03': plain(h3p2)}
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'units.json').write_text(json.dumps({'d01': ['H1-P4'], 'd02': ['H1-P3', 'H1-P4'], 'd03': ['H3-P2'], 'source': 'v5'}) + '\n',
                                 encoding='utf-8')
print({k: len(v.split()) for k, v in inputs.items()})
