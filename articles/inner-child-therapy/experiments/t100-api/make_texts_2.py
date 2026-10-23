#!/usr/bin/env python3
"""Turn 100, second part: texts for the API checks of Joel's two updated paragraphs (his message of 13:10 UTC), as they
now stand in the article: each alone, then five paragraphs of Your Loan is PRE-APPROVED! around them (his TB and roselle
paragraph, the old paragraph's first half, his two, and "Notice how"). Built like make_texts.py. Writes TEXTS-2.json and
texts/<name>.txt."""
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


i_a = find('And even (or especially) when I am suffering')
i_b = find('Of course, that’s not to say you should not try to suffer less.')
assert i_b == i_a + 1 and seq[i_a - 1][1].startswith('That may sound like a silly') and seq[i_a - 2][1].startswith('If you have a moment right now')
assert seq[i_b + 1][1].startswith('Notice how, when you offer thanks')
TEXTS = {
    't100_askgod_a': [seq[i_a]],
    't100_askgod_b': [seq[i_b]],
    't100_askgod_stretch': [seq[i_a - 2], seq[i_a - 1], seq[i_a], seq[i_b], seq[i_b + 1]],
}
out = {n: '\n'.join(line(k, b) for k, b in blocks) for n, blocks in TEXTS.items()}
(HERE / 'TEXTS-2.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
(HERE / 'texts').mkdir(exist_ok=True)
for n, t in out.items():
    (HERE / 'texts' / (n + '.txt')).write_text(t, encoding='utf-8')
    print('%-20s %4d words | %s' % (n, len(t.split()), t[:70].replace('\n', ' / ')))
