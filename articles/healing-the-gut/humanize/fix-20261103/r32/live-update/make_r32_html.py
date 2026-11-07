#!/usr/bin/env python3
"""r32.html: the editor HTML his post gets in its next update: r31.html (../../r31/live-update/, r12.html with r31's
words, Phase 4's one-item list removed, every quote mark curled) with Joel's news about Pooyan as one more sub-item of
"Years of accumulated shit in your guts", after the A1-dairy item and before the CAUTION, as r32.md has it. Its label is
bold, as the CAUTION after it is: "<strong>Update</strong>: ...". The new item's quote marks are curled the same way
(curl_nodes), and every paragraph and list item of the result must read exactly as EXPECTED-TEXT-r32.txt, which is r31's
checked lines with the new one after the A1-dairy line. The new item read Human Written, High, in its place (#210).
Writes r32.html and EXPECTED-TEXT-r32.txt. No API calls."""
import hashlib
import pathlib
import re
import sys

from bs4 import BeautifulSoup

HERE = pathlib.Path(__file__).resolve().parent
R32 = HERE.parent
FIX = R32.parent
REPO = HERE.parents[5]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
sys.path.insert(0, str(FIX / 'r12' / 'substack'))
import suggestion_review as sr  # noqa: E402
from make_payload import curl_nodes  # noqa: E402  (r12's; importing it rebuilds draft A's files, unchanged)

b32 = sr.blocks((R32 / 'r32.md').read_text(encoding='utf-8'))
NEW = b32[12]['text']
assert NEW.startswith('Update: Pooyan') and b32[11]['text'].startswith('However, while we don')
html = (FIX / 'r31' / 'live-update' / 'r31.html').read_text(encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
root = soup.find('div', class_='ProseMirror')
hits = [li for li in root.find_all('li') if li.find('p') and li.find('p').get_text('').startswith('However, while we don')]
assert len(hits) == 1
li = soup.new_tag('li')
p = soup.new_tag('p')
strong = soup.new_tag('strong')
strong.string = 'Update'
p.append(strong)
assert NEW.startswith('Update: ')
p.append(NEW[len('Update'):])
li.append(p)
hits[0].insert_after(li)
curl_nodes(li)
out = str(soup)
new_line = li.get_text('')
assert "'" not in new_line and '"' not in new_line

expected = (FIX / 'r31' / 'live-update' / 'EXPECTED-TEXT-r31.txt').read_text(encoding='utf-8').split('\n')
k = [i for i, l in enumerate(expected) if l.startswith('However, while we don’t know if Pooyan')]
assert len(k) == 1
expected = expected[:k[0] + 1] + [new_line] + expected[k[0] + 1:]
(HERE / 'EXPECTED-TEXT-r32.txt').write_text('\n'.join(expected), encoding='utf-8')
check = BeautifulSoup(out, 'html.parser').find('div', class_='ProseMirror')
lines = []
for el in check.find_all(['p', 'li']):
    if el.name == 'li' and el.find(['p', 'ul', 'ol']):
        continue
    if el.find_parent(['figure']) or el.find_parent(class_=lambda c: c and ('youtube' in c or 'embed' in c)):
        continue
    t = el.get_text('').replace(' ', ' ')
    if t.strip() and not re.match(r'^https?://\S+$', t.strip()):
        lines.append(t.rstrip())
got = [l for l in lines if re.sub(r'\s+', ' ', l).strip() not in ('', 'Double click to interact with video')]
assert got == expected, [(i, a[:60], b[:60]) for i, (a, b) in enumerate(zip(got, expected)) if a != b][:5] or (len(got), len(expected))
(HERE / 'r32.html').write_text(out, encoding='utf-8')
print('r32.html', hashlib.sha256(out.encode('utf-8')).hexdigest(), len(expected), 'checked lines, exactly and in order;',
      'new line:', new_line[:90])
