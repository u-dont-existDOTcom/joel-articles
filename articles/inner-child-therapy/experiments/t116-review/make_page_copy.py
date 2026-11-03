#!/usr/bin/env python3
"""Turn 116: the copy of Joel's reorganized guide that the marking page shows (GUIDE-PAGE.md), from
experiments/t116-joel/JOEL-GUIDE-20261103.md. It differs from his file only where the page tool would show it wrong,
never in his words or characters:
  - bold marks (**) go, since the page has no bold and would show them as asterisks (his bold labels in Signs of
    Manipulation, the goodwill wish, and a bold "n" and a bold space in My Journey, leftovers in his file);
  - each list item, and the manipulation list's first item, starts its own block, since his list lines end in a line
    break the page would run together;
  - italics inside a link's text go, since the page shows a link's text with its asterisks.
The suggestions (REVIEW.json) are written against this copy; build_review.py applies them back to his text by words.

  python3 make_page_copy.py"""
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent / 't116-joel' / 'JOEL-GUIDE-20261103.md'
md = SRC.read_text(encoding='utf-8')
out = md.replace('**', '')
# a list item on its own line (numbered or "- ") after another line: a blank line before it
out = re.sub(r'[ \t]*\n(?=(?:\d+\.|-)\s)', '\n\n', out)
# the manipulation list: its intro line ends in a line break before the first bold label
out = out.replace('check for include :  \nGaslighting', 'check for include :\n\nGaslighting')
# italics inside a link's text ([*Unforgivable*](...)): the page shows a link's text as it is, asterisks and all
out = re.sub(r'\[\*([^\]*]+)\*\]\(', r'[\1](', out)
(HERE / 'GUIDE-PAGE.md').write_text(out, encoding='utf-8')
print('GUIDE-PAGE.md', len(out.split()), 'words')
