"""Section 15, Emulate round c (2026-10-17, after batch 323g): the paradise subsection's heading with H2-P1 and H2-P2 from v3.
The subsection reads "Mostly Human" (323g, https://www.pangram.com/history/4b6fc9e9-c969-4691-9b11-224e675ce71b) with one
40-word AI window, low: the heading and H2-P1, whose second sentence is the published meaning put back after both round b
calls dropped it ("The warmth has hard limits, and for LGBTQ+ people who cross them, it can be brutal."). P1 with P2 reads
Human without the heading (0.19). u01 is the heading, P1 and P2; two calls, plain text (the law's link as its words). Run
from this folder: python3 make_inputs.py"""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402
bs = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 'v3.md').read_text(encoding='utf-8')) if b.strip()]
i = bs.index('## All is not well in paradise')
assert bs[i + 1].startswith('But does this mean') and bs[i + 2].startswith('Sénégal passed a law')
inputs = {'u01': 'All is not well in paradise\n\n' + plain(bs[i + 1]) + '\n\n' + plain(bs[i + 2])}
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'units.json').write_text(json.dumps({'u01': ['H2', 'H2-P1', 'H2-P2'], 'source': 'v3'}) + '\n', encoding='utf-8')
print({k: len(v.split()) for k, v in inputs.items()})
