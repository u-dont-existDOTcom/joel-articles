#!/usr/bin/env python3
"""Turn 105: for each collected item, the note just before its paragraph in the article, which says whose words it is
(a quick aid for my check; the decision is mine, item by item)."""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
SRC = (HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8')


def note_before(quote):
    for v in (quote, quote.replace("'", '’'), quote.replace('’', "'")):
        i = SRC.find(v)
        if i >= 0:
            break
    else:
        return '(quote not found in the source)'
    j = SRC.rfind('<!--', 0, i)
    k = SRC.find('-->', j)
    gap = SRC[k + 3:i]
    n = re.sub(r'\s+', ' ', SRC[j + 4:k]).strip()
    return ('' if gap.count('\n\n') < 2 else '[note is %d paragraphs up] ' % gap.count('\n\n')) + n[:260]


if __name__ == '__main__':
    kind = sys.argv[1]
    for x in json.loads((HERE / kind / 'ITEMS.json').read_text(encoding='utf-8')):
        print('%s %s | %s\n    %s\n' % (x['key'], x.get('kind') or x.get('move'), x['quote'][:150], note_before(x['quote'])))
