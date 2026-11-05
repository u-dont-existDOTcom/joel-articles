#!/usr/bin/env python3
"""The paste payload for the whole-article check of r06 through a temporary Substack draft (the free route; Joel,
2026-11-03 22:02 UTC: "we don't do whole article checks with pangram GUI ... i have a free route for those").

From r10.html, Substack's own editor HTML: the body without the editor wrapper, the two pictures, the video embeds and
the paywall marker (the check reads text, and the paid view shows the whole post). Every quote mark is curled the way
the post shows it (curl(), the Inner Child lane's, gate in pull request 285): Substack's editor curls straight marks on
paste and curls a double one after an opening bracket the wrong way. 20,523 characters, so one draft (the check reads up
to 99,999). Writes PAYLOAD-A.html, TEXT-A.txt and PAYLOAD.json (the payload's SHA-256 and the words' SHA-256 the paste
helper checks). No API calls."""
import hashlib, json, pathlib, sys

from bs4 import BeautifulSoup, NavigableString

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT / 'articles' / 'inner-child-therapy' / 'experiments' / 't119-substack'))
OPENERS = set('([{—–-/')


def curl_nodes(root):
    """curl() across the text nodes in order, each knowing the character before it."""
    prev = ' '
    for node in [n for n in root.descendants if isinstance(n, NavigableString)]:
        s, out = str(node), []
        for i, c in enumerate(s):
            p = s[i - 1] if i else prev
            nxt = s[i + 1] if i + 1 < len(s) else ' '
            if c == '"':
                out.append('“' if p.isspace() or p in OPENERS else '”')
            elif c == "'":
                out.append('‘' if (p.isspace() or p in OPENERS or p in '"“') and nxt.isalnum() else '’')
            else:
                out.append(c)
        new = ''.join(out)
        if new != s:
            node.replace_with(new)
        if s:
            prev = s[-1]
    return root


soup = BeautifulSoup((HERE.parent / 'r10.html').read_text(encoding='utf-8'), 'html.parser')
root = soup.find('div', class_='ProseMirror')
for el in root.find_all(['figure', 'iframe', 'svg']):
    el.decompose()
# the editor's own placeholder on a video embed ("Double click to interact with video") came with the editor HTML; pasted,
# it became three paragraphs of text in the first draft (2026-11-04), so the embeds go whole
for el in root.find_all(string=lambda s: s and s.strip() == 'Double click to interact with video'):
    box = el.find_parent('div', class_=lambda c: c and any('youtube' in x or 'embed' in x for x in c)) or el.parent
    box.decompose()
for d in root.find_all('div'):
    if not d.get_text(strip=True) or 'paywall-editor' in (d.get('class') or []):
        d.decompose()
for d in root.find_all('div'):
    d.unwrap()
for a in root.find_all(True):
    for k in [k for k in a.attrs if k not in ('href',)]:
        del a[k]
curl_nodes(root)
body = ''.join(str(c) for c in root.contents)
text = root.get_text('\n')
# the words the paste helper compares, counted as the editor shows them: one block's text with no break at a link's edge
# (text above splits "strategy</a>." into "strategy" and ".", 3,425 words where the editor has 3,387; 2026-11-04)
blocks = [el.get_text('') for el in root.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li'])
          if not (el.name == 'li' and el.find(['p', 'ul', 'ol']))]
words = ' '.join(' '.join(blocks).translate(str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"'})).split())
(HERE / 'PAYLOAD-A.html').write_text(body, encoding='utf-8')
(HERE / 'TEXT-A.txt').write_text(text, encoding='utf-8')
meta = {'source': 'r10.html', 'source_sha256': hashlib.sha256((HERE.parent / 'r10.html').read_bytes()).hexdigest(),
        'title': 'Healing the Gut, draft A (temp, delete after)', 'chars': len(text), 'words': len(words.split()),
        'payload_sha256': hashlib.sha256(body.encode('utf-8')).hexdigest(),
        'words_sha256': hashlib.sha256(words.encode('utf-8')).hexdigest(),
        'straight_marks_left': sum(body.count(c) for c in '"\'') - body.count('href="') * 2}
(HERE / 'PAYLOAD.json').write_text(json.dumps(meta, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps(meta, ensure_ascii=False))
