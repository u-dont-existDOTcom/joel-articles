#!/usr/bin/env python3
"""r02: r01 with Joel's batch-1 answers (2026-11-03 22:02 UTC, experiments/t04-answers/) applied to the protocol section,
then the standard typographic swap (gate E337) on the whole post.

- PI, P2, P3, P4, P6: the versions he approved on the batch-1 page; P1 and P5: his own versions (APPROVED-b1.json says
  what, if anything, differs from his words).
- The phase nicknames are gone (his Q-NICK answer: "drop them but make sure if you're dropping them that nothing is
  referring to them"): nothing else in the post refers to them ("Gut Health Architect" is the Gem's name). His P5 keeps
  "(Let's Play Gardener!)", which is his.
- tools/humanization/typography_swap.py --html on the result: curly marks straight, each em dash his spaced en dash.

Writes r02.html and r02.md (via ../r01/html_to_md.py). No API calls.
"""
import hashlib, json, pathlib, re, subprocess, sys

from bs4 import BeautifulSoup

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
from typography_swap import swap_html  # noqa: E402

SRC = HERE.parent / 'r01' / 'r01.html'
APP = json.loads((HERE / 'APPROVED-b1.json').read_text(encoding='utf-8'))
soup = BeautifulSoup(SRC.read_text(encoding='utf-8'), 'html.parser')
A = 'rel="noopener noreferrer nofollow" target="_blank"'


def inline(t):
    t = t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: '<a href="%s" %s>%s</a>' % (m.group(2), A, m.group(1)), t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', t)
    return t


def md_to_html(md):
    """The writers' Markdown (a "####" heading, paragraphs, "- " bullets, "  1. " numbered steps, which nest in the
    bullet before them when there is one) as the editor's HTML: <h4><strong>, <p>, <ul><li><p>, <ol><li><p>."""
    out, ul, ol, ol_in_li = [], None, None, False
    def close_ol():
        nonlocal ol, ol_in_li
        if ol is not None:
            html = '<ol>%s</ol>' % ''.join(ol)
            if ol_in_li and ul:
                ul[-1] = ul[-1][:-len('</li>')] + html + '</li>'
            else:
                out.append(html)
        ol, ol_in_li = None, False
    def close_ul():
        nonlocal ul
        close_ol()
        if ul is not None:
            out.append('<ul>%s</ul>' % ''.join(ul))
        ul = None
    for block in md.split('\n\n'):
        line = block.rstrip()
        if not line.strip():
            continue
        m_num = re.match(r'^\s+\d+\.\s+(.*)$', line, re.S)
        if line.startswith('#### '):
            close_ul()
            out.append('<h4><strong>%s</strong></h4>' % inline(line[5:].strip()))
        elif line.startswith('- '):
            close_ol()
            if ul is None:
                ul = []
            ul.append('<li><p>%s</p></li>' % inline(line[2:].strip()))
        elif m_num:
            if ol is None:
                ol, ol_in_li = [], ul is not None
            ol.append('<li><p>%s</p></li>' % inline(m_num.group(1).strip()))
        else:
            close_ul()
            out.append('<p>%s</p>' % inline(line.strip()))
    close_ul()
    return ''.join(out)


def phase_nodes(n):
    h = [x for x in soup.find_all('h4') if x.get_text().startswith('Phase %d:' % n)]
    assert len(h) == 1, (n, len(h))
    h = h[0]
    nodes = [h]
    sib = h.find_next_sibling()
    while sib is not None and sib.name != 'h4' and not (sib.name in ('h2', 'h3')):
        nodes.append(sib)
        sib = sib.find_next_sibling()
    return nodes


for n in range(1, 7):
    nodes = phase_nodes(n)
    new = BeautifulSoup(md_to_html(APP['P%d' % n]['text']), 'html.parser')
    first = nodes[0]
    for child in list(new.contents):
        first.insert_before(child)
    for x in nodes:
        x.decompose()

pi = [p for p in soup.find_all('p') if p.get_text().startswith('This protocol is designed to be executed in phases')]
assert len(pi) == 1
pi[0].clear()
pi[0].append(BeautifulSoup(inline(APP['PI']['text'].strip()), 'html.parser'))

html, swapped = swap_html(str(soup))
(HERE / 'r02.html').write_text(html, encoding='utf-8')
subprocess.run([sys.executable, str(HERE.parent / 'r01' / 'html_to_md.py'), str(HERE / 'r02.html'), str(HERE / 'r02.md')], check=True)
print('r02.html', hashlib.sha256(html.encode('utf-8')).hexdigest(), '| swapped', swapped, 'characters')
