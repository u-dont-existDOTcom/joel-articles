#!/usr/bin/env python3
"""r05: r04 with Joel's batch-4 answers (2026-11-04 11:32 UTC, experiments/t07-answers/), then the standard swap.

- The TCA item becomes the acids paragraph (card F4-3: "if you agree you can re-do the para so it focuses on glutamine for
  energy and breiefly explains the use of those acids"). Checked first (research/ACIDS-CHECK.md, gate E348): no study
  found showing dietary malic or citric acid fuels the gut lining; their better use is iron absorption (Gillooly et al.
  1983); nothing found for "boost stomach acid", so it stays out. Written in the order a newcomer asks (gate E347), its
  own newcomer read answered (acids/draft-read/LINKS.json).
- Glutamine keeps the energy point, with his two points from his TCA rewrite moved into it: "by pulling the tight
  junctions together" and "Glutamine also provides nitrogen to help build new cells".
- "TCA intermediates" leaves the fuels list in his opening paragraph and in Phase 5's step 4.
- tools/humanization/typography_swap.py --html on the result.

Writes r05.html and r05.md. No API calls.
"""
import hashlib, html as H, json, pathlib, re, subprocess, sys

from bs4 import BeautifulSoup

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
from typography_swap import swap_html  # noqa: E402

A = 'rel="noopener noreferrer nofollow" target="_blank"'
soup = BeautifulSoup((HERE.parent / 'r04' / 'r04.html').read_text(encoding='utf-8'), 'html.parser')
F = json.loads((HERE / 'FUELS-r05.json').read_text(encoding='utf-8'))


def inline(t):
    t = H.escape(t, quote=False)
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: '<a href="%s" %s>%s</a>' % (m.group(2), A, m.group(1)), t)


li = [x for x in soup.find_all('li') if x.find('p') and x.find('p').get_text().startswith('Mitochondrial and cellular energy starvation')]
assert len(li) == 1, len(li)
new = ('<li><p>%s</p><ul><li><p>%s</p><ul><li><p>%s</p></li><li><p>%s</p></li></ul></li><li><p>%s</p></li>'
       '<li><p>%s</p></li></ul></li>') % tuple(inline(F[k]) for k in ('top', 'glutamine', 'dosing', 'caution', 'butyrate', 'acids'))
li[0].replace_with(BeautifulSoup(new, 'html.parser'))

step = [x for x in soup.find_all(string=re.compile(r'\(glutamine, butyrate and TCA intermediates\)'))]
assert len(step) == 1, len(step)
step[0].replace_with(step[0].replace('(glutamine, butyrate and TCA intermediates)', '(glutamine and butyrate)'))

out, swapped = swap_html(str(soup))
assert 'TCA intermediates' not in BeautifulSoup(out, 'html.parser').get_text()
(HERE / 'r05.html').write_text(out, encoding='utf-8')
subprocess.run([sys.executable, str(HERE.parent / 'r01' / 'html_to_md.py'), str(HERE / 'r05.html'), str(HERE / 'r05.md')], check=True)
print('r05.html', hashlib.sha256(out.encode('utf-8')).hexdigest(), '| swapped', swapped)
