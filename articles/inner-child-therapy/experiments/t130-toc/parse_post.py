"""Split the live post into sections: one per heading (h1-h5), with own text and word counts.
Usage: python3 parse_post.py LIVE-POST-20261116-0212.json > sections.json"""
import json, re, sys
from bs4 import BeautifulSoup, NavigableString, Tag

d = json.load(open(sys.argv[1]))
soup = BeautifulSoup(d['body_html'], 'html.parser')
root = soup
blocks = [c for c in root.children if isinstance(c, Tag)]

def words(t):
    return len(re.findall(r"[\w’'\-]+", t))

def block_text(tag):
    # skip images/embeds captions? keep captions as text but mark kind
    return re.sub(r'\s+', ' ', tag.get_text(' ', strip=True)).strip()

sections = []
cur = {'idx': 0, 'level': 0, 'heading': '(before first heading)', 'blocks': []}
sections.append(cur)
for b in blocks:
    name = b.name
    if re.fullmatch(r'h[1-6]', name or ''):
        cur = {'idx': len(sections), 'level': int(name[1]), 'heading': block_text(b), 'heading_html': str(b)[:400], 'blocks': []}
        sections.append(cur)
        continue
    cls = ' '.join(b.get('class', []))
    kind = name
    if name == 'div':
        if 'captioned-image' in cls or b.find('img'): kind = 'image'
        elif 'youtube' in cls: kind = 'youtube'
        elif 'pullquote' in cls: kind = 'pullquote'
        elif 'embedded-post' in cls or 'post-card' in cls: kind = 'postcard'
        else: kind = 'div:' + cls[:40]
    t = block_text(b)
    cur['blocks'].append({'kind': kind, 'text': t, 'words': words(t) if kind in ('p','ul','ol','blockquote','pullquote') else 0})

for s in sections:
    s['own_words'] = sum(x['words'] for x in s['blocks'])
# subtree words: own + following deeper sections
for i, s in enumerate(sections):
    tot = s['own_words']
    for t in sections[i+1:]:
        if s['level'] and t['level'] <= s['level']: break
        if s['level'] == 0: break
        tot += t['own_words']
    s['tree_words'] = tot
json.dump(sections, sys.stdout, ensure_ascii=False, indent=1)
