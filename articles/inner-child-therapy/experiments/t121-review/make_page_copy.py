#!/usr/bin/env python3
"""Turn 121: the copy of the guide that the marking page shows (GUIDE-PAGE.md), from HUMANIZED-ARTICLE-SO-FAR.md as it is
now (his aside back). It differs from the article only where the page tool would show it wrong, never in his words or
characters, as turn 116's copy did (experiments/t116-review/make_page_copy.py):
  - bold marks (**) go, since the page has no bold and would show them as asterisks;
  - each list item starts its own block, since list lines ending in a line break would run together;
  - italics inside a link's text go, since the page shows a link's text with its asterisks.
  python3 make_page_copy.py"""
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
md = SRC.read_text(encoding='utf-8')
out = md.replace('**', '')
out = re.sub(r'[ \t]*\n(?=(?:\d+\.|-)\s)', '\n\n', out)
out = re.sub(r'\[\*([^\]*]+)\*\]\(', r'[\1](', out)
(HERE / 'GUIDE-PAGE.md').write_text(out, encoding='utf-8')
print('GUIDE-PAGE.md', len(out.split()), 'words')
