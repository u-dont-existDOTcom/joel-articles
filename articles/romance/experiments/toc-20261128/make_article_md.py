#!/usr/bin/env python3
"""The live post as Markdown for section_refs.py: ARTICLE-NOW.md. Each top-level heading as #..., each other top-level
block with words as a paragraph, its links written [words](href); a list's items each on a "- " line.

  python3 make_article_md.py LIVE-BODY-20261128.html
"""
import os, re, sys
from bs4 import BeautifulSoup, NavigableString, Tag

HERE = os.path.dirname(os.path.abspath(__file__))


def inline(node):
    out = []
    for c in node.children:
        if isinstance(c, NavigableString):
            out.append(str(c))
        elif isinstance(c, Tag):
            if c.name == 'a' and c.get('href'):
                out.append('[%s](%s)' % (inline(c).strip(), c['href']))
            elif c.name in ('script', 'style', 'template'):
                continue
            else:
                out.append(inline(c))
    return ''.join(out)


def main(path):
    soup = BeautifulSoup(open(path, encoding='utf-8').read(), 'html.parser')
    lines = []
    for b in soup.children:
        if not isinstance(b, Tag):
            continue
        if re.fullmatch(r'h[1-6]', b.name or ''):
            lines.append('#' * int(b.name[1]) + ' ' + re.sub(r'\s+', ' ', b.get_text('')).strip())
        elif b.name in ('ul', 'ol'):
            for li in b.find_all('li', recursive=False):
                t = re.sub(r'\s+', ' ', inline(li)).strip()
                if t:
                    lines.append('- ' + t)
        else:
            t = re.sub(r'\s+', ' ', inline(b)).strip()
            if t:
                lines.append(t)
    open(os.path.join(HERE, 'ARTICLE-NOW.md'), 'w', encoding='utf-8').write('\n\n'.join(lines) + '\n')
    print(len(lines), 'blocks')


if __name__ == '__main__':
    main(sys.argv[1])
