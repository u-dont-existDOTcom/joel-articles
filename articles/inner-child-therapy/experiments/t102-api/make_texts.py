#!/usr/bin/env python3
"""Turn 102, first round: the four paragraphs Joel's 94 and 95 answers changed (experiments/t102-installs/apply_t102.py),
each alone. Their stretches come after they pass (make_texts_2.py). Writes TEXTS.json and texts/."""
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


STARTS = {
    't102_borrow_p5': "If the love still isn't coming",
    't102_pain_p': 'And when the symptoms come and go randomly',
    't102_untangle_p': 'Differentiation is slow, and it goes on your whole life.',
    't102_sharing_p': 'So I’d ask them, before handing over any tricky specifics',
}
TEXTS = {n: [seq[find(s)]] for n, s in STARTS.items()}

if __name__ == '__main__':
    out = {n: '\n'.join(line(k, b) for k, b in blocks) for n, blocks in TEXTS.items()}
    (HERE / 'TEXTS.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for n, t in out.items():
        (HERE / 'texts' / (n + '.txt')).write_text(t, encoding='utf-8')
        print('%-18s %4d words | %s' % (n, len(t.split()), t[:90].replace('\n', ' / ')))
