#!/usr/bin/env python3
"""r07: r06 with the stacks section's last two paragraphs redone for a newcomer (p80/, p81/): the two that read AI in the
whole-article check of r06 (r06/substack/RESULT-A.json). Each states the links a newcomer read found missing, in the
reader's order (gates E345, E347, E351; hidden_links.py check clean) and passed the blind meaning check
(MEANING-VERDICTS*.json). Writes r07.html and r07.md. No API calls."""
import hashlib, html as H, pathlib, subprocess, sys

from bs4 import BeautifulSoup

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
from typography_swap import swap_html  # noqa: E402

soup = BeautifulSoup((HERE.parent / 'r06' / 'r06.html').read_text(encoding='utf-8'), 'html.parser')
for start, f in (('I wouldn', 'p80/DRAFT.txt'), ('Start with low doses, especially', 'p81/DRAFT.txt')):
    p = [x for x in soup.find_all('p') if x.get_text().startswith(start)]
    assert len(p) == 1, (start, len(p))
    p[0].replace_with(BeautifulSoup('<p>%s</p>' % H.escape((HERE / f).read_text(encoding='utf-8').strip(), quote=False), 'html.parser'))
out, swapped = swap_html(str(soup))
(HERE / 'r07.html').write_text(out, encoding='utf-8')
subprocess.run([sys.executable, str(HERE.parent / 'r01' / 'html_to_md.py'), str(HERE / 'r07.html'), str(HERE / 'r07.md')], check=True)
print('r07.html', hashlib.sha256(out.encode('utf-8')).hexdigest(), '| swapped', swapped)
