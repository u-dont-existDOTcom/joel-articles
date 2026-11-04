#!/usr/bin/env python3
"""r03: r02 with Joel's batch-2 answers (2026-11-04 00:37 UTC, experiments/t05-answers/), then the standard swap.

- The stacks section: S2-1, S2-3, S2-4 and S2-5 as he approved them; S2-2 his own version (a paragraph and his three
  categories as the list), its double space and missing full stop fixed.
- The mitochondrial fuels under Leaky gut: his first paragraph word for word (read from his last shared Pangram page;
  one double space fixed), and the rest (glutamine, its dose and its caution, butyrate, the TCA intermediates) written
  the way his is built (FUELS-r03.json; gate E342), each part checked before it goes to him.
- tools/humanization/typography_swap.py --html on the result (his S2-2 had curly quotes).

Writes r03.html and r03.md. No API calls.
"""
import hashlib, html as H, json, pathlib, re, subprocess, sys

from bs4 import BeautifulSoup

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
from typography_swap import swap_html  # noqa: E402

A = 'rel="noopener noreferrer nofollow" target="_blank"'
soup = BeautifulSoup((HERE.parent / 'r02' / 'r02.html').read_text(encoding='utf-8'), 'html.parser')
F = json.loads((HERE / 'FUELS-r03.json').read_text(encoding='utf-8'))
S = json.loads((HERE / 'STACKS-r03.json').read_text(encoding='utf-8'))


def inline(t):
    t = H.escape(t, quote=False)
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: '<a href="%s" %s>%s</a>' % (m.group(2), A, m.group(1)), t)


def frag(s):
    return BeautifulSoup(s, 'html.parser')


def one(found, what):
    assert len(found) == 1, (what, len(found))
    return found[0]


# the fuels: the whole list item, its nested lists included
li = one([x for x in soup.find_all('li') if x.find('p') and x.find('p').get_text().startswith('Mitochondrial & Cellular Energy Starvation')], 'fuels')
new = ('<li><p>%s</p><ul><li><p>%s</p><ul><li><p>%s</p></li><li><p>%s</p></li></ul></li><li><p>%s</p></li>'
       '<li><p>%s</p></li></ul></li>') % tuple(inline(F[k]) for k in ('top', 'glutamine', 'dosing', 'caution', 'butyrate', 'tca'))
li.replace_with(frag(new))

# the stacks section
def para(start):
    return one([p for p in soup.find_all('p') if p.get_text().startswith(start)], start)

para('I do not think there is a universal supplement stack').replace_with(frag('<p>%s</p>' % inline(S['S2-1'])))
p75 = para('That said, some people want a ready-made starting point')
ol = p75.find_next_sibling()
assert ol.name == 'ol' and ol.get_text().startswith('Microbiome support'), ol.name
his = S['S2-2']
ol.replace_with(frag('<ol>%s</ol>' % ''.join('<li><p>%s</p></li>' % inline(x) for x in his[1:])))
p75.replace_with(frag('<p>%s</p>' % inline(his[0])))
para('The best general commercial stack').replace_with(frag('<p>%s</p>' % inline(S['S2-3'])))
para('I would not recommend general').replace_with(frag('<p>%s</p>' % inline(S['S2-4'])))
para('Start low, especially with prebiotics').replace_with(frag('<p>%s</p>' % inline(S['S2-5'])))

out, swapped = swap_html(str(soup))
(HERE / 'r03.html').write_text(out, encoding='utf-8')
subprocess.run([sys.executable, str(HERE.parent / 'r01' / 'html_to_md.py'), str(HERE / 'r03.html'), str(HERE / 'r03.md')], check=True)
print('r03.html', hashlib.sha256(out.encode('utf-8')).hexdigest(), '| swapped', swapped)
