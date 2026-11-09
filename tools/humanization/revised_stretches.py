#!/usr/bin/env python3
"""revised_stretches.py - after a round's answers go in, list each card he revised with his own version whose stretch is
still in the article.

Gate bad-trips-2026-11-09d. Joel, 2026-11-09 17:22 UTC, on a card that asked whether to cut the section his round-27
version had replaced: "i thought i already merged it and cut that section in the last turn." When he revises a card with
his version, the card's stretch is what his version replaces, wherever his version goes in. A sentence of the stretch
that is still in the article, and isn't in his version, means the stretch was kept by mistake (or kept on purpose, which
--kept records).

  python3 tools/humanization/revised_stretches.py --answers ANSWERS.json --review REVIEW.json --page PAGE.md \
      --article ARTICLE.md [--kept CARD "why it stays"] ...

PAGE.md is the page text the review was built on (its spans index its blocks); ARTICLE.md is the article after the
round went in. Exit 0 when nothing of a revised card's stretch is left (or each card left is --kept), 1 otherwise.
"""
import argparse
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import suggestion_review as sr  # noqa: E402

SENT = re.compile(r'(?<=[.!?])["”’)\]]*\s+')
MIN_CHARS = 25   # shorter pieces ("Do", "Repeat:") turn up anywhere


def norm(t):
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t or '')
    t = t.replace('’', "'").replace('“', '"').replace('”', '"')
    t = re.sub(r'[*_`>#]', '', t)
    return ' '.join(t.lower().split())


def stale(answers, review, page_md, article_md):
    """[(card id, sentence)] for each sentence of a revised card's stretch that the article still has and his version
    doesn't."""
    bl = sr.blocks(page_md)
    art = norm(' '.join(b['text'] for b in sr.blocks(article_md)))
    items = {x['id']: x for x in answers.get('items', [])}
    out = []
    for s in review.get('suggestions', []):
        it = items.get(s.get('id'))
        if not it or it.get('status') != 'revise':
            continue
        # his version can come in "your version" or in the comment; the page fills "your version" with the stretch
        # itself, so one he left unchanged is no version (round 27's fear-loop card: his whole first five minutes came
        # in the comment)
        yours = it.get('your_version') or ''
        if norm(yours) == norm(it.get('before') or ''):
            yours = ''
        his = norm(yours + ' ' + (it.get('comment') or ''))
        if len(his) < 40:
            continue
        for sp in s.get('spans', []):
            text = bl[sp['block']]['text'][sp['start']:sp['end']]
            for piece in SENT.split(text):
                n = norm(piece)
                if len(n) >= MIN_CHARS and n in art and n not in his:
                    out.append((s['id'], piece.strip()))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--answers', required=True)
    ap.add_argument('--review', required=True)
    ap.add_argument('--page', required=True)
    ap.add_argument('--article', required=True)
    ap.add_argument('--kept', nargs=2, action='append', default=[], metavar=('CARD', 'WHY'))
    a = ap.parse_args(argv)
    left = stale(json.loads(pathlib.Path(a.answers).read_text(encoding='utf-8')),
                 json.loads(pathlib.Path(a.review).read_text(encoding='utf-8')),
                 pathlib.Path(a.page).read_text(encoding='utf-8'),
                 pathlib.Path(a.article).read_text(encoding='utf-8'))
    kept = {c: w for c, w in a.kept}
    bad = [(c, t) for c, t in left if c not in kept]
    for c, t in left:
        print('%s %s: "%s"' % ('kept' if c in kept else 'STILL IN', c, t[:110]) + (' (%s)' % kept[c] if c in kept else ''))
    if bad:
        print('%d sentence(s) of revised stretches are still in the article: his version replaces the stretch, so cut '
              'them, or say why one stays with --kept (gate bad-trips-2026-11-09d)' % len(bad))
        return 1
    print('PASS: no revised card\'s stretch is left in the article')
    return 0


if __name__ == '__main__':
    sys.exit(main())
