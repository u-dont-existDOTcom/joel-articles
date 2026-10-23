#!/usr/bin/env python3
"""Turn 102: the check texts for The Inner Guide with question 98 A's three headings (THE-INNER-GUIDE.md, question 99), built from the
article as it is, for when Joel picks. Not sent: headings are never picked by a Pangram result (docs/HUMANIZATION-GATE.md),
so the checks wait for his answer. Writes INNER-GUIDE-TEXTS.json: the h1 opening (heading and P1), then each new h2
with its paragraphs."""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from paragraphs_alone import reader_blocks  # noqa: E402
from ptext import plain  # noqa: E402
from substack_check_text import smart  # noqa: E402

md = re.sub(r'<!--.*?-->', '', (ROOT / 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8'), flags=re.S)
seq = reader_blocks(md)
i = [k for k, (t, b) in enumerate(seq) if b == '# The Inner Guide'][0]
j = [k for k, (t, b) in enumerate(seq) if b == '## Timing Is Individual'][0]
P = {n: seq[k] for n, k in enumerate(range(i + 1, j), 1)}
assert len(P) == 10


def line(kind, b):
    t = plain(re.sub(r'^#+\s*', '', b) if kind == 'h' else b)
    return smart(t).replace('‍', '').replace('️', '')


H = lambda t: ('h', t)  # noqa: E731
TEXTS = {
    't99_ig_opening': [seq[i], P[1]],
    't99_ig_spoiling': [H('## Between Spoiling and Clamping Down'), P[2], P[3], P[4], P[5]],
    't99_ig_perfect': [H('## A Healthy Mind Is Not a Perfect Mind'), P[6], P[7], P[8]],
    't99_ig_belonging': [H('## A Belonging Deeper Than Any Group'), P[9], P[10]],
}
out = {n: '\n'.join(line(k, b) for k, b in blocks) for n, blocks in TEXTS.items()}
(HERE / 'INNER-GUIDE-TEXTS.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
for n, t in out.items():
    print('%-18s %4d words | %s' % (n, len(t.split()), t[:80].replace('\n', ' / ')))
