"""Parts 2 to 4 of the repeats read, each split in two (parts 5 to 10), after their readers looped (2026-10-23).

The first readers of parts 2, 3 and 4 spent their whole output thinking, three times in a row each (about 20 minutes),
and wrote nothing; part 1's reader finished (READER-1.md). They were stopped. Each of those parts is split here at the
heading nearest its middle, and the halves get the current brief (tools/humanization/clarity_read.py, whose "Work
quickly" line was made stronger after this), so each reader owns half as many points. PART-2 to PART-4 and their briefs
stay as the record of the first try; collect reads only READER-*.md.

  python3 articles/intentional-communities/candidate/joel-20261023/repeats/resplit.py   (from the repo root)
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / 'tools' / 'humanization'))
import clarity_read as C  # noqa: E402

ABOUT = ("Joel's long article on intentional communities (an essay, then a How-To Manual, then an appendix of films and "
         "books), for a general Substack audience")
MAX_ITEMS = 6


def halves(text):
    lines = text.split('\n')
    heads = [i for i, l in enumerate(lines) if l.startswith('## ') and i > 0]
    mid = len(text) / 2
    pos = lambda i: len('\n'.join(lines[:i]))
    cut = min(heads, key=lambda i: abs(pos(i) - mid))
    return '\n'.join(lines[:cut]), '\n'.join(lines[cut:])


def main():
    brief1 = (HERE / 'BRIEF-1.txt').read_text(encoding='utf-8')
    assert ABOUT in brief1, 'the first briefs named the article this way'
    k = 5
    for old in (2, 3, 4):
        for half in halves((HERE / ('PART-%d.txt' % old)).read_text(encoding='utf-8')):
            (HERE / ('PART-%d.txt' % k)).write_text(half, encoding='utf-8')
            brief = C.REPEAT_BRIEF.format(
                article=(HERE / 'ARTICLE.txt'), k=k, n=10, about=ABOUT, question='', examples='', books='', kept='',
                part=(HERE / ('PART-%d.txt' % k)), report=(HERE / ('READER-%d.md' % k)), max_items=MAX_ITEMS)
            (HERE / ('BRIEF-%d.txt' % k)).write_text(brief, encoding='utf-8')
            print('PART-%d.txt (from part %d): %d characters, starts "%s"' % (k, old, len(half), half.split('\n')[0][:60]))
            k += 1


if __name__ == '__main__':
    main()
