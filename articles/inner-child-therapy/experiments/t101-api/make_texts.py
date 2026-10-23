#!/usr/bin/env python3
"""Turn 101: texts for the API checks of what Joel's 14:05 answers changed, as it now stands in the article (built like
experiments/t100-api/make_texts.py). Changed paragraphs of 50 words or more go alone first; then the two parts of Borrow One
Competency at a Time (its opening with the three borrowings, and the new h3), five blocks around the new heading in Love
Doesn't Have to Wait for Trust, and Your Loan is PRE-APPROVED! from the prosperity paragraph to the Of course paragraph.
Writes TEXTS.json and texts/<name>.txt."""
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


def line(kind, b):
    t = plain(re.sub(r'^#+\s*', '', b) if kind == 'h' else b)
    return smart(t).replace('‍', '').replace('️', '')


def find(start):
    hits = [i for i, (k, b) in enumerate(seq) if b.startswith(start)]
    assert len(hits) == 1, (start, hits)
    return hits[0]


b0 = find('## Borrow One Competency at a Time')
b3 = find("### If the Love Isn't Coming Yet")
assert b3 == b0 + 5 and seq[b3 + 6][1].startswith('## Borrow Hindsight')
p5 = find("If the love still isn't coming, you can at least stop judging")
lh = find('### Instead of Blame')
oc = find('Of course, that’s not to say you should not try to suffer less, or get away from abusers.')
pr = find('And I’m certainly not preaching “prosperity philosophy,”')
assert oc == pr + 4
TEXTS = {
    't101_borrow_p5': [seq[p5]],
    't101_askgod_ofcourse': [seq[oc]],
    't101_askgod_prosperity': [seq[pr]],
    # after the paragraphs read Human alone
    't101_borrow_main': seq[b0:b3],
    't101_borrow_h3': seq[b3:b3 + 6],
    't101_love_junction': seq[lh - 2:lh + 3],
    't101_askgod_stretch': seq[pr:oc + 1],
}
out = {n: '\n'.join(line(k, b) for k, b in blocks) for n, blocks in TEXTS.items()}
(HERE / 'TEXTS.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
(HERE / 'texts').mkdir(exist_ok=True)
for n, t in out.items():
    (HERE / 'texts' / (n + '.txt')).write_text(t, encoding='utf-8')
    print('%-24s %4d words | %s' % (n, len(t.split()), t[:70].replace('\n', ' / ')))
