#!/usr/bin/env python3
"""typography_swap.py - the standard typographic swap (gate E337): curly quote marks become straight ones, and each em
dash becomes the spaced en dash Joel types (" – "). Nothing else changes.

Joel, 2026-11-03 22:02 UTC: "yes make that swapping standard". The evidence: pangram-humanization-lab PR #195
(state/experiments/quote-style-41-20261103/) and PR #196 (state/experiments/dash-style-41-20261103/). Straightening
improved 40 of 113 borderline paragraphs of his articles on Pangram 4.1 and hurt 4. The dash swap improved 9 of 47 AI or
borderline ones and hurt none. Paragraphs already at 100% Human, High barely moved either way. His own straight marks
stay as he typed them (curling them only hurt).

  python3 tools/humanization/typography_swap.py FILE [--html] [--write]   # prints what changes; --write saves it
  python3 tools/humanization/typography_swap.py --check FILE [--html]     # exit 1 if anything would change

With --html, only the text between tags changes (attributes, URLs and scripts are left alone). No third-party packages,
so CI's bare Python can run it.
"""
import argparse
import pathlib
import re
import sys

QUOTES = str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"'})
EM = '—'
EN = '–'


def swap_text(text):
    """The swapped text and the number of characters changed. An em dash between two digits (a range) becomes an
    unspaced en dash; any other em dash, with or without spaces around it, becomes " – "."""
    out = text.translate(QUOTES)
    out = re.sub(r'(?<=\d)' + EM + r'(?=\d)', EN, out)
    out = re.sub(r'[  ]?' + EM + r'[  ]?', ' ' + EN + ' ', out)
    # a dash that ended a line or opened one gets no space on that side
    out = re.sub(r' ' + EN + r' (?=\n|$)', ' ' + EN, out)
    out = re.sub(r'(?:(?<=\n)|^) ' + EN + ' ', EN + ' ', out)
    changed = sum(1 for c in text if c in '‘’“”' + EM)
    return out, changed


TAG = re.compile(r'(<script\b.*?</script>|<style\b.*?</style>|<[^>]*>)', re.S | re.I)


def swap_html(html):
    """The same swap on the text between tags only."""
    parts, n = [], 0
    for i, piece in enumerate(TAG.split(html)):
        if i % 2:          # a tag, a script or a style block: untouched
            parts.append(piece)
        else:
            t, c = swap_text(piece)
            parts.append(t)
            n += c
    return ''.join(parts), n


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('file')
    ap.add_argument('--html', action='store_true')
    ap.add_argument('--write', action='store_true')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args(argv)
    p = pathlib.Path(a.file)
    src = p.read_text(encoding='utf-8')
    new, n = (swap_html if a.html else swap_text)(src)
    if a.check:
        print('%s: %d character(s) to swap' % (p, n))
        return 1 if new != src else 0
    if a.write and new != src:
        p.write_text(new, encoding='utf-8')
    print('%s: %d character(s) %s' % (p, n, 'swapped' if a.write else 'would be swapped'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
