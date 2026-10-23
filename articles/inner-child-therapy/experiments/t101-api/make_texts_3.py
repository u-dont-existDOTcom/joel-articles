#!/usr/bin/env python3
"""Turn 101, third round: Borrow Hindsight P1 with the Higher Self line back (draft h02). His 49.5 (2026-10-18 19:06 UTC,
experiments/t72-answers/JOEL-20261018-1906.md: "it's normal that we'd say one thing in the guide and then explain it more in the
section that differentiates the guide from IFS"; recorded as "49, 5: both stay") kept it, and turn 93's cut of AI tells took it
out (the coverage check, experiments/t101-coverage/COVERAGE-B.md item 5). Alone, then the h2 with it. Writes TEXTS-3.json."""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from paragraphs_alone import reader_blocks  # noqa: E402
from ptext import plain  # noqa: E402
from substack_check_text import smart  # noqa: E402

md = re.sub(r'<!--.*?-->', '', (ROOT / 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8'), flags=re.S)
seq = reader_blocks(md)
D = HERE.parent / 't101-tries' / 'drafts'


def line(kind, b):
    t = plain(re.sub(r'^#+\s*', '', b) if kind == 'h' else b)
    return smart(t).replace('‍', '').replace('️', '')


h = [i for i, (k, b) in enumerate(seq) if b.startswith('## Borrow Hindsight')][0]
assert seq[h + 1][1].startswith('I sometimes ask: "How would I respond') and seq[h + 4][1].startswith('## Remember When')
p1 = ('p', (D / 'h02-hindsight-P1.txt').read_text(encoding='utf-8').strip())
TEXTS = {'t101c_hindsight_p1': [p1], 't101c_hindsight_h2': [seq[h], p1, seq[h + 2], seq[h + 3]]}
out = {n: '\n'.join(line(k, b) for k, b in blocks) for n, blocks in TEXTS.items()}
(HERE / 'TEXTS-3.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
for n, t in out.items():
    (HERE / 'texts' / (n + '.txt')).write_text(t, encoding='utf-8')
    print('%-22s %4d words | %s' % (n, len(t.split()), t[:80].replace('\n', ' / ')))
