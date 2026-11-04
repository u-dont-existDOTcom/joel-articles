#!/usr/bin/env python3
"""r10: r09 with Joel's batch-7 answers (2026-11-04 16:41 UTC, experiments/t10-answers/), then the standard swap.

F7-1: his whole stacks section as he checked it (Human Written, 100%, 600 words): his minimal edits to the start-low and
doctor paragraphs, word for word. F7-2: his three-category lead-in becomes "A good stack should cover these 3 categories:".
Writes r10.html and r10.md. No API calls."""
import hashlib, html as H, json, pathlib, subprocess, sys

from bs4 import BeautifulSoup

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
from typography_swap import swap_html  # noqa: E402

tries = json.loads((HERE.parents[2] / 'experiments' / 't10-answers' / 'his-web-app-tries.json').read_text(encoding='utf-8'))
his = tries['50328626-56f3-45be-8e79-f65e9394e44c']['text'].split('\n')
SL = [l for l in his if l.startswith('Start any of these supplements')][0]
DOC = [l for l in his if l.startswith('Some severe symptoms warrant')][0]
P2 = 'A good stack should cover these 3 categories:'
soup = BeautifulSoup((HERE.parent / 'r09' / 'r09.html').read_text(encoding='utf-8'), 'html.parser')


def one(start):
    hits = [x for x in soup.find_all('p') if x.get_text().strip().startswith(start)]
    assert len(hits) == 1, (start, len(hits))
    return hits[0]


def para(text):
    return BeautifulSoup('<p>%s</p>' % H.escape(text, quote=False), 'html.parser').p


one('Start any kit at a low dose').replace_with(para(SL))
one('Some severe symptoms warrant').replace_with(para(DOC))
one('That said, some people want').replace_with(para(P2))
# every other line of his checked section is already r09's, word for word
md = BeautifulSoup(str(soup), 'html.parser').get_text('\n')
for line in his[1:]:
    if line.startswith('That said'):
        continue
    assert ' '.join(line.split()) in ' '.join(md.split()), line[:60]
out, swapped = swap_html(str(soup))
(HERE / 'r10.html').write_text(out, encoding='utf-8')
subprocess.run([sys.executable, str(HERE.parent / 'r01' / 'html_to_md.py'), str(HERE / 'r10.html'), str(HERE / 'r10.md')], check=True)
print('r10.html', hashlib.sha256(out.encode('utf-8')).hexdigest(), '| swapped', swapped)
