#!/usr/bin/env python3
"""r09: r08 with Joel's batch-6 answers (2026-11-04 16:00 UTC, experiments/t09-answers/), then the standard swap.

F6-1 (the stacks opener), F6-4 (the cleanse stacks) and F6-6 (glutamine's caution) approved: already in r08. F6-2, my
suggestion for his three categories, rejected ("this isn't the problem"): his paragraph stays as it is. F6-3: his kits
paragraph word for word ("these kits", "gut lining", "Finally,"). F6-5: his two paragraphs word for word, start low and
when to see a doctor. Writes r09.html and r09.md. No API calls."""
import hashlib, html as H, json, pathlib, subprocess, sys

from bs4 import BeautifulSoup

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
from typography_swap import swap_html  # noqa: E402

ans = json.loads((HERE.parents[2] / 'experiments' / 't09-answers' / 'joel-20261104-1600-b6-answers.json').read_text(encoding='utf-8'))
his = {it['id']: it['your_version'] for it in ans['items']}
soup = BeautifulSoup((HERE.parent / 'r08' / 'r08.html').read_text(encoding='utf-8'), 'html.parser')


def one(start):
    hits = [x for x in soup.find_all('p') if x.get_text().strip().startswith(start)]
    assert len(hits) == 1, (start, len(hits))
    return hits[0]


def para(text):
    return BeautifulSoup('<p>%s</p>' % H.escape(text, quote=False), 'html.parser').p


one('Gemini suggested three kits').replace_with(para(his['F6-3'].strip()))
a, b = [x.strip() for x in his['F6-5'].split('\n\n')]
pa, pb = para(a), para(b)
one('Start any kit at a low dose').replace_with(pa)
one("But don't start a stack at all").replace_with(pb)
out, swapped = swap_html(str(soup))
(HERE / 'r09.html').write_text(out, encoding='utf-8')
subprocess.run([sys.executable, str(HERE.parent / 'r01' / 'html_to_md.py'), str(HERE / 'r09.html'), str(HERE / 'r09.md')], check=True)
print('r09.html', hashlib.sha256(out.encode('utf-8')).hexdigest(), '| swapped', swapped)
