#!/usr/bin/env python3
"""The Pangram check texts for his picks, as readers see the post: inline markup joins with no space ("<em>right
now</em>." reads "right now."), paragraphs, list items and captions are lines of their own, and what isn't his text is
left out (Substack's Share and Subscribe buttons, and the cards of embedded posts and videos, which show other people's
words). make_files.py's SECTIONS.json joined every tag with a space (fine for word counts), which put 134 spaces before
punctuation into the first whole-article check text (voided in the ledger, NB-toc-whole#31).

  python3 check_texts.py      # writes pangram/WHOLE-AFTER.txt and pangram/S015-AFTER.txt from LIVE-BODY-20261123.html
"""
import hashlib, json, os, re
from bs4 import BeautifulSoup, NavigableString, Tag

HERE = os.path.dirname(os.path.abspath(__file__))
BLOCK = {'p', 'li', 'figcaption', 'blockquote', 'div', 'ul', 'ol', 'pre', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table', 'tr'}
SKIP_COMPONENTS = re.compile(r'(?i)button|subscri|share|embeddedpost|youtube|instagram|twitter|tweet|spotify|vimeo|poll|footnote-anchor|digest|latex')


def skip(tag):
    attrs = ' '.join([tag.get('data-component-name') or ''] + (tag.get('class') or []))
    return bool(SKIP_COMPONENTS.search(attrs)) or tag.name in ('button', 'script', 'style', 'svg', 'iframe', 'img', 'picture', 'source')


def lines_of(node):
    """The node's text as lines: block boundaries break lines, inline markup joins with nothing between."""
    out, cur = [], []

    def flush():
        t = re.sub(r'\s+', ' ', ''.join(cur)).strip()
        if t:
            out.append(t)
        cur.clear()

    def walk(n):
        if isinstance(n, NavigableString):
            cur.append(str(n))
            return
        if not isinstance(n, Tag) or skip(n):
            return
        if n.name == 'br':
            flush()
            return
        block = n.name in BLOCK
        if block:
            flush()
        for c in n.children:
            walk(c)
        if block:
            flush()
    walk(node)
    flush()
    return out


def sections(html):
    soup = BeautifulSoup(html, 'html.parser')
    cur = {'idx': 0, 'lines': []}
    out = [cur]
    for b in soup.children:
        if not isinstance(b, Tag):
            continue
        if re.fullmatch(r'h[1-6]', b.name or ''):
            cur = {'idx': len(out), 'heading': re.sub(r'\s+', ' ', b.get_text('')).strip(), 'lines': []}
            out.append(cur)
            continue
        if skip(b):
            continue
        cur['lines'] += lines_of(b)
    return {'S%03d' % s['idx']: s for s in out}


def main():
    R = sections(open(os.path.join(HERE, 'LIVE-BODY-20261123.html'), encoding='utf-8').read())
    plan = json.load(open(os.path.join(HERE, 'PLAN.json'), encoding='utf-8'))['sections']
    old = {s['id']: s for s in json.load(open(os.path.join(HERE, 'SECTIONS.json'), encoding='utf-8'))}
    for i, s in R.items():  # the same sections as SECTIONS.json, by heading
        if i != 'S000':
            assert s['heading'] == old[i]['heading'], (i, s['heading'])

    def body(e, fix):
        ls = list(R[e['id']]['lines'])
        if fix and 'text_edit' in e:
            hits = [k for k, l in enumerate(ls) if e['text_edit']['from'] in l]
            assert len(hits) == 1, e['id']
            ls[hits[0]] = ls[hits[0]].replace(e['text_edit']['from'], e['text_edit']['to'])
        if 'open_line' in e:
            ls = [e['open_line']] + ls
        return ls

    def text(entries, fix, first_lines=None):
        out = []
        for e in entries:
            if e['heading']:
                out.append(e['heading'])
            b = body(e, fix)
            out += b[:first_lines] if first_lines else b
        return '\n\n'.join(out)
    whole = text(plan, fix=False)                     # S015's first line as he has it: its fix is checked by itself
    before = '\n\n'.join(sum(([R[i]['heading']] + R[i]['lines'] for i in sorted(R) if i != 'S000'), []))  # the live text
    s015 = text([e for e in plan if e['id'] == 'S015'], fix=True, first_lines=2)
    os.makedirs(os.path.join(HERE, 'pangram'), exist_ok=True)
    live = text(plan, fix=True)                       # the post as published at 18:01:47 UTC (the two held headings as they were)
    for name, t in [('WHOLE-AFTER.txt', whole), ('S015-AFTER.txt', s015), ('WHOLE-BEFORE.txt', before), ('WHOLE-LIVE-1801.txt', live)]:
        path = os.path.join(HERE, 'pangram', name)
        if os.path.exists(path) and open(path, encoding='utf-8').read() != t:
            print(name, 'kept as checked (a Pangram check was run on it; PLAN.json has changed since)')
            continue
        open(path, 'w', encoding='utf-8').write(t)
        print(name, len(t.split()), 'words', hashlib.sha256(t.encode()).hexdigest(),
              'spaces before punctuation:', len(re.findall(r' [.,;:!?](?=\s|$)', t)))


if __name__ == '__main__':
    main()
