#!/usr/bin/env python3
"""r33.html: r32.html (../../r32/live-update/) with AskRigor linked to https://askrigor.com, as r33.md has it: the name
in Pooyan's item and the domain written out in the plant foods item. Each link is made the way the post's other links
are (rel="noopener noreferrer nofollow", target="_blank"). The text doesn't change: every paragraph and list item must
still read exactly as EXPECTED-TEXT-r32.txt, copied here as EXPECTED-TEXT-r33.txt. Writes r33.html. No API calls."""
import hashlib
import pathlib
import re

from bs4 import BeautifulSoup, NavigableString

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parents[1]
URL = 'https://askrigor.com'
html = (FIX / 'r32' / 'live-update' / 'r32.html').read_text(encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
root = soup.find('div', class_='ProseMirror')


# Pooyan's item ("AskRigor, my research tool, is what told me ...") and the plant foods item ("... re-check it with askrigor.com")
for start, word in (('Update', 'AskRigor'), ('For the most research-backed recommendations', 'askrigor.com')):
    ps = [p for p in root.find_all('p') if p.get_text('').startswith(start)]
    assert len(ps) == 1, (start, len(ps))
    hits = [t for t in ps[0].find_all(string=True) if word in t and t.parent.name != 'a']
    assert len(hits) == 1 and str(hits[0]).count(word) == 1, (word, [str(h)[:40] for h in hits])
    t = hits[0]
    before, after = str(t).split(word)
    a = soup.new_tag('a', href=URL, rel='noopener noreferrer nofollow', target='_blank')
    a.string = word
    t.insert_before(NavigableString(before))
    t.insert_before(a)
    t.insert_before(NavigableString(after))
    t.extract()
out = str(soup)
expected = (FIX / 'r32' / 'live-update' / 'EXPECTED-TEXT-r32.txt').read_text(encoding='utf-8')
(HERE / 'EXPECTED-TEXT-r33.txt').write_text(expected, encoding='utf-8')
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
assert got == expected.split('\n'), 'the text changed'
links = [a for a in check.find_all('a') if a.get('href') == URL]
assert [a.get_text() for a in links] == ['askrigor.com', 'AskRigor'] or [a.get_text() for a in links] == ['AskRigor', 'askrigor.com'], [a.get_text() for a in links]
(HERE / 'r33.html').write_text(out, encoding='utf-8')
print('r33.html', hashlib.sha256(out.encode('utf-8')).hexdigest(), len(got), 'checked lines unchanged;',
      [str(a)[:110] for a in links])
