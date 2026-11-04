#!/usr/bin/env python3
"""r08: r07 with the stacks section redone for a newcomer before any article check (Joel, 2026-11-04 14:41 UTC: "no the whole
article doesn't decide, we need to first fix any windows we can see before we check the article"; gate E354). In its own
API check the section read AI (5% human, 12 of 13 windows AI). Its paragraphs of mine now state what a newcomer read found
missing, in the reader's order (stacks/links/, hidden_links.py check clean), with the tell panel's agreed tells fixed
(stacks/panel/); his three-category paragraph is unchanged (it goes to him on a card). The glutamine caution's last
sentence, a Low window alone, says why the portal vein matters. Writes r08.html and r08.md. No API calls."""
import hashlib, html as H, pathlib, re, subprocess, sys

from bs4 import BeautifulSoup

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
from typography_swap import swap_html  # noqa: E402

draft = (HERE / 'stacks' / 'DRAFT-SECTION.md').read_text(encoding='utf-8')
paras = [b.strip() for b in draft.split('\n\n') if b.strip() and not b.startswith('#') and not re.match(r'\d\. ', b)]
P1, HIS, KITS, P80, P81A, P81B = paras
soup = BeautifulSoup((HERE.parent / 'r07' / 'r07.html').read_text(encoding='utf-8'), 'html.parser')


def one(start, tag='p'):
    hits = [x for x in soup.find_all(tag) if x.get_text().strip().startswith(start)]
    assert len(hits) == 1, (start, len(hits))
    return hits[0]


def para(text):
    return BeautifulSoup('<p>%s</p>' % H.escape(text, quote=False), 'html.parser').p


assert one('That said, some people').get_text().strip() == HIS, 'his paragraph changed in the draft'
one("I don't think there").replace_with(para(P1))
one('Gemini suggested these kits').replace_with(para(KITS))
one("You'll also find").replace_with(para(P80))
old = one('Start with low doses, especially')
b = para(P81B)
old.replace_with(para(P81A))
one('Whichever kit you get').insert_after(b)
cau = (HERE / 'stacks' / 'CAUTION-DRAFT.txt').read_text(encoding='utf-8').strip()
c = one('CAUTION: cancer cells')
c.replace_with(para(cau))
out, swapped = swap_html(str(soup))
(HERE / 'r08.html').write_text(out, encoding='utf-8')
subprocess.run([sys.executable, str(HERE.parent / 'r01' / 'html_to_md.py'), str(HERE / 'r08.html'), str(HERE / 'r08.md')], check=True)
print('r08.html', hashlib.sha256(out.encode('utf-8')).hexdigest(), '| swapped', swapped)
