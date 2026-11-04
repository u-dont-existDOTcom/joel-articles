#!/usr/bin/env python3
"""r04: r03 with Joel's batch-3 answers (2026-11-04 10:18 UTC, experiments/t06-answers/), then the standard swap.

- The glutamine item: his F3-1 word for word, with the Dr. Rhonda link put back on "watch Dr. Rhonda vid" (the marking
  page's text has no links).
- The butyrate item: his F3-2 word for word (his second web-app try, Possibly human 100%).
- The TCA intermediates: mine, written for a reader who doesn't know the links (gate E343): the newcomer read's gaps
  (tca/links/LINKS.json), each stated or left as a question for him, `hidden_links.py check` clean, the blind meaning check
  (tca/MEANING-VERDICTS.json).
- The dose and the cancer caution as in r03 (Human through the API).
- tools/humanization/typography_swap.py --html on the result.

Writes r04.html and r04.md. No API calls.
"""
import hashlib, html as H, json, pathlib, re, subprocess, sys

from bs4 import BeautifulSoup

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
from typography_swap import swap_html  # noqa: E402

A = 'rel="noopener noreferrer nofollow" target="_blank"'
soup = BeautifulSoup((HERE.parent / 'r03' / 'r03.html').read_text(encoding='utf-8'), 'html.parser')
F = json.loads((HERE / 'FUELS-r04.json').read_text(encoding='utf-8'))
assert F.get('tca'), 'the TCA item is not in FUELS-r04.json yet'


def inline(t):
    t = H.escape(t, quote=False)
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: '<a href="%s" %s>%s</a>' % (m.group(2), A, m.group(1)), t)


li = [x for x in soup.find_all('li') if x.find('p') and x.find('p').get_text().startswith('Mitochondrial and cellular energy starvation')]
assert len(li) == 1, len(li)
new = ('<li><p>%s</p><ul><li><p>%s</p><ul><li><p>%s</p></li><li><p>%s</p></li></ul></li><li><p>%s</p></li>'
       '<li><p>%s</p></li></ul></li>') % tuple(inline(F[k]) for k in ('top', 'glutamine', 'dosing', 'caution', 'butyrate', 'tca'))
li[0].replace_with(BeautifulSoup(new, 'html.parser'))

out, swapped = swap_html(str(soup))
(HERE / 'r04.html').write_text(out, encoding='utf-8')
subprocess.run([sys.executable, str(HERE.parent / 'r01' / 'html_to_md.py'), str(HERE / 'r04.html'), str(HERE / 'r04.md')], check=True)
print('r04.html', hashlib.sha256(out.encode('utf-8')).hexdigest(), '| swapped', swapped)
