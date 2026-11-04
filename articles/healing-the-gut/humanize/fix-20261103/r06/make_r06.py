#!/usr/bin/env python3
"""r06: r05 with Joel's batch-5 answers (2026-11-04 12:35 UTC, experiments/t08-answers/), then the standard swap.

F5-1, F5-2 and F5-4 approved (already in r05). F5-3: his acids paragraph word for word, with "ctiric" (a non-word) read
as "citric" and the Gillooly link on his "(Gillooly et al., 1983)". Writes r06.html and r06.md. No API calls.
"""
import hashlib, html as H, json, pathlib, re, subprocess, sys

from bs4 import BeautifulSoup

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
from typography_swap import swap_html  # noqa: E402

A = 'rel="noopener noreferrer nofollow" target="_blank"'
soup = BeautifulSoup((HERE.parent / 'r05' / 'r05.html').read_text(encoding='utf-8'), 'html.parser')
F = json.loads((HERE / 'FUELS-r06.json').read_text(encoding='utf-8'))


def inline(t):
    t = H.escape(t, quote=False)
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: '<a href="%s" %s>%s</a>' % (m.group(2), A, m.group(1)), t)


p = [x for x in soup.find_all('p') if x.get_text().startswith('Malic and citric acid (which make green apples')]
assert len(p) == 1, len(p)
p[0].replace_with(BeautifulSoup('<p>%s</p>' % inline(F['acids']), 'html.parser'))
out, swapped = swap_html(str(soup))
(HERE / 'r06.html').write_text(out, encoding='utf-8')
subprocess.run([sys.executable, str(HERE.parent / 'r01' / 'html_to_md.py'), str(HERE / 'r06.html'), str(HERE / 'r06.md')], check=True)
print('r06.html', hashlib.sha256(out.encode('utf-8')).hexdigest(), '| swapped', swapped)
