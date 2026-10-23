#!/usr/bin/env python3
"""Turn 100, second part: Joel's message of 2026-10-23 13:10 UTC (experiments/t100-answers/JOEL-20261023-1310.md), his two
updated paragraphs of Your Loan is PRE-APPROVED! (under Ask God for a Loan), word for word with his link.

- His first paragraph starts where the old paragraph's second half started ("And even (or especially) when I am
  suffering"), so the old first half ("That may sound like a silly, quirky waste of time to some folks. ... something pure
  and sacred.") stays as its own paragraph before it, unchanged (question 93.3 asks whether he meant to cut it). His changes:
  "this tribulation" for "it", and his link on "wellspring of compassion in my heart for all of us".
- His second paragraph replaces the "Of course, that's not to say you should not try to suffer less" paragraph. It leaves
  out "nor does gratitude for difficulties justify staying with an abuser" (PGQ-031's point that no one is required to
  thank an abuser) and the two sentences on the endless loop and less being more (PGQ-033's point that the list never
  ends), and ends on his new meditate-or-pray sentence: questions 93.1 and 93.2.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
D = HERE.parent / 't100-tries' / 'drafts'
SRC = 'experiments/t100-answers/JOEL-20261023-1310.md'
read = lambda n: (D / n).read_text(encoding='utf-8').strip()
SPLIT = ' And even (or especially) when I am suffering'


def note(what):
    return '<!-- Turn 100 (his message of 2026-10-23 13:10 UTC, ' + SRC + '): ' + what + ' -->'


def main():
    lines = ART.read_text(encoding='utf-8').split('\n')

    def one(start):
        hits = [i for i, l in enumerate(lines) if l.startswith(start)]
        assert len(hits) == 1, (start, hits)
        return hits[0]

    a, b = read('his-askgod-a.txt'), read('his-askgod-b.txt')
    i = one('That may sound like a silly, quirky waste of time to some folks.')
    old = lines[i]
    assert old.count(SPLIT) == 1
    first = old[:old.index(SPLIT)]
    j = one('Of course, that’s not to say you should not try to suffer less, nor does gratitude')
    assert j > i
    lines[j:j + 1] = [note("his updated paragraph, word for word (\"i also updated 2 paragraphs in ask god for a loan you're pre-approved\"). "
                           "It leaves out \"nor does gratitude for difficulties justify staying with an abuser\" and the two sentences "
                           "after \"That’s something to be grateful for.\" (the endless loop, less is more): questions 93.1 and 93.2."), '', b]
    lines[i:i + 1] = [first, '', note("his updated paragraph, word for word, with his link; it starts where the paragraph above used to "
                                      "go on, so the paragraph above is the old one's first half, unchanged (question 93.3)."), '', a]
    ART.write_text('\n'.join(lines), encoding='utf-8')
    print('installed his two paragraphs; the old first half kept as its own paragraph')


if __name__ == '__main__':
    main()
