#!/usr/bin/env python3
"""Turn 101, second round: If the Love Isn't Coming Yet (the new h3) again, with my P9 changed (draft h01) so it no longer
opens on the thank-you right after old P5's thank-you line (the move put them next to each other; check t101_borrow_h3).
Built like make_texts.py. Writes TEXTS-2.json and texts/<name>.txt."""
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


b3 = [i for i, (k, b) in enumerate(seq) if b.startswith("### If the Love Isn't Coming Yet")][0]
blocks = seq[b3:b3 + 6]
assert blocks[5][1].startswith("The thank-you you weren't waiting for")
blocks[5] = ('p', (D / 'h01-borrow-P9.txt').read_text(encoding='utf-8').strip())
out = {'t101b_borrow_h3': '\n'.join(line(k, b) for k, b in blocks)}
(HERE / 'TEXTS-2.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
for n, t in out.items():
    (HERE / 'texts' / (n + '.txt')).write_text(t, encoding='utf-8')
    print('%-24s %4d words | %s' % (n, len(t.split()), t[-160:].replace('\n', ' / ')))
