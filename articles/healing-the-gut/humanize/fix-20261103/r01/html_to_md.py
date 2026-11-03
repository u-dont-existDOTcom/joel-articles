#!/usr/bin/env python3
"""The article's reader-visible blocks as Markdown, one block per paragraph or list item, links kept as [text](url).

Usage: python3 html_to_md.py IN.html OUT.md
Headings become #..####, top-level list items "- ", list items inside a list item "  1. " or "  - " (each its own
block, so the marking page can point at one item), paragraphs as they are. Bold and italic marks are dropped (the
review reads words, not styling); the editor's video placeholders and empty paragraphs are left out. Exact characters
(curly or straight quotes, dashes) are kept. No API calls.
"""
import pathlib
import re
import sys

from bs4 import BeautifulSoup, NavigableString, Tag

SKIP_CLASSES = {'captioned-image-container', 'paywall-editor', 'youtube-wrap', 'subscription-widget-wrap-editor'}


def inline(el):
    out = []
    for c in el.children:
        if isinstance(c, NavigableString):
            out.append(str(c))
        elif isinstance(c, Tag):
            if c.name == 'a' and c.get('href'):
                txt = inline(c)
                out.append('[%s](%s)' % (txt, c['href']) if txt.strip() else '')
            elif c.name in ('ul', 'ol'):
                continue
            elif c.name == 'br':
                out.append(' ')
            elif c.name == 'div' or (c.get('class') and SKIP_CLASSES & set(c.get('class'))):
                continue
            else:
                out.append(inline(c))
    return ''.join(out)


def walk(el, blocks, depth=0):
    for c in el.children:
        if not isinstance(c, Tag):
            continue
        cls = set(c.get('class') or [])
        if cls & SKIP_CLASSES or (c.name == 'div' and c.get('data-component-name')):
            continue
        if c.name in ('h1', 'h2', 'h3', 'h4'):
            t = re.sub(r'\s+', ' ', inline(c)).strip()
            if t:
                blocks.append('#' * int(c.name[1]) + ' ' + t)
        elif c.name == 'p':
            t = re.sub(r'[ \t]+', ' ', inline(c)).strip()
            if t:
                blocks.append(t)
        elif c.name in ('ul', 'ol'):
            for n, li in enumerate(c.find_all('li', recursive=False), 1):
                paras = [re.sub(r'[ \t]+', ' ', inline(p)).strip() for p in li.find_all('p', recursive=False)]
                t = ' '.join(x for x in paras if x)
                marker = ('  ' * depth) + ('%d. ' % n if c.name == 'ol' else '- ')
                if t:
                    blocks.append(marker + t)
                for sub in li.find_all(['ul', 'ol'], recursive=False):
                    wrapper = BeautifulSoup('', 'html.parser').new_tag('div')
                    walk_list(sub, blocks, depth + 1)
        elif c.name == 'blockquote':
            t = re.sub(r'\s+', ' ', inline(c)).strip()
            if t:
                blocks.append('> ' + t)
        elif c.name == 'div':
            walk(c, blocks, depth)


def walk_list(lst, blocks, depth):
    for n, li in enumerate(lst.find_all('li', recursive=False), 1):
        paras = [re.sub(r'[ \t]+', ' ', inline(p)).strip() for p in li.find_all('p', recursive=False)]
        t = ' '.join(x for x in paras if x)
        marker = ('  ' * depth) + ('%d. ' % n if lst.name == 'ol' else '- ')
        if t:
            blocks.append(marker + t)
        for sub in li.find_all(['ul', 'ol'], recursive=False):
            walk_list(sub, blocks, depth + 1)


def convert(html):
    soup = BeautifulSoup(html, 'html.parser')
    root = soup.find(attrs={'data-testid': 'editor'}) or soup
    blocks = []
    walk(root, blocks)
    return '\n\n'.join(blocks) + '\n'


if __name__ == '__main__':
    md = convert(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'))
    pathlib.Path(sys.argv[2]).write_text(md, encoding='utf-8')
    print(len(md.split('\n\n')), 'blocks')
