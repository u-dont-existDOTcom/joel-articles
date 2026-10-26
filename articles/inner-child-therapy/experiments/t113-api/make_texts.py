#!/usr/bin/env python3
"""Turn 113's API texts (copied from turn 111's, from turn 110's and experiments/t109-api/make_texts.py): the same reader text as Substack shows it
(comments removed, smart quotes), from the installed article or from a candidate one.

  T = Texts(md)          md: the article's Markdown (installed, or with candidate sections in it)
  T.para(START)          one paragraph alone, by its first words
  T.h2(HEADING)          a heading with its paragraphs up to the next heading, heading line first

candidate_md() is the guide with every turn-113 proposal in, so a check reads exactly what the review sheet offers."""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ART = ROOT / 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from paragraphs_alone import reader_blocks  # noqa: E402
from ptext import plain  # noqa: E402
from substack_check_text import smart  # noqa: E402


def candidate_md():
    """The guide with every turn-113 proposal in (experiments/t113-shape/PROPOSAL-ARTICLE.md, made by proposals.py)."""
    return (HERE.parent / 't113-shape' / 'PROPOSAL-ARTICLE.md').read_text(encoding='utf-8')


class Texts:
    def __init__(self, md):
        self.seq = reader_blocks(re.sub(r'<!--.*?-->', '', md, flags=re.S))

    @staticmethod
    def line(kind, b):
        t = plain(re.sub(r'^#+\s*', '', b) if kind == 'h' else b)
        return smart(t).replace('‍', '').replace('️', '')

    def para(self, start):
        hits = [i for i, (k, b) in enumerate(self.seq) if k == 'p' and b.startswith(start)]
        assert len(hits) == 1, (start, hits)
        return self.line(*self.seq[hits[0]])

    def h2(self, heading):
        hits = [i for i, (k, b) in enumerate(self.seq) if k == 'h' and re.sub(r'^#+\s*', '', b) == heading]
        assert len(hits) == 1, (heading, hits)
        i = hits[0]
        out = [self.line(*self.seq[i])]
        for k, b in self.seq[i + 1:]:
            if k == 'h':
                break
            if k == 'p':
                out.append(self.line(k, b))
        return '\n'.join(out)
