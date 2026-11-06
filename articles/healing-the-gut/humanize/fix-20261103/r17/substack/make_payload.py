#!/usr/bin/env python3
"""The paste payload for the whole-article check of r17 through a temporary Substack draft (the free route; Joel,
2026-11-03 22:02 UTC: "we don't do whole article checks with pangram GUI ... i have a free route for those").

r17 is the article with every answer of batches 9 to 11 in and batch 12's window fixes (on his page, not yet approved).
The payload starts from r12.html, the live post's editor HTML block for block, and each paragraph whose words changed
since r12 gets r17's words through html_text_edit.set_text, which keeps its links, italics and bold on the same words.
Then as r12's payload: no pictures, video embeds or paywall marker (the check reads text), and every quote mark curled
the way the post shows it, so the draft carries the characters the update will carry (E362 (gut)). Writes PAYLOAD-B.html,
TEXT-B.txt and PAYLOAD.json. No API calls."""
import hashlib
import json
import pathlib
import re
import sys

from bs4 import BeautifulSoup, NavigableString

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parents[1]
REPO = HERE.parents[5]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
sys.path.insert(0, str(FIX / 'r12' / 'substack'))
import html_text_edit as E  # noqa: E402
import suggestion_review as sr  # noqa: E402

squash = lambda s: re.sub(r'\s+', ' ', s).strip()
straight = lambda s: s.translate(str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"'}))
b12 = sr.blocks((FIX / 'r12' / 'r12.md').read_text(encoding='utf-8'))
b17 = sr.blocks((FIX / 'r17' / 'r17.md').read_text(encoding='utf-8'))
assert len(b12) == len(b17)
def split_new(old_parts, new_text):
    """The new block's text cut where the old block's paragraphs met: each boundary is mapped from the old words to the
    new by their longest matching runs."""
    import difflib
    if len(old_parts) == 1:
        return [new_text]
    old_words = ' '.join(old_parts).split(' ')
    new_words = new_text.split(' ')
    bounds, n = [], 0
    for part in old_parts[:-1]:
        n += len(part.split(' '))
        bounds.append(n)
    sm = difflib.SequenceMatcher(None, old_words, new_words, autojunk=False)
    cuts = []
    for b in bounds:
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if i1 <= b <= i2:
                cuts.append(j1 + (b - i1) if tag == 'equal' else (j2 if b == i2 else j1))
                break
    out, last = [], 0
    for c in cuts:
        out.append(' '.join(new_words[last:c]))
        last = c
    out.append(' '.join(new_words[last:]))
    return out


doc = (FIX / 'r12' / 'r12.html').read_text(encoding='utf-8')
paras = E.paragraphs(doc)
edits, report = [], []
for i, (x, y) in enumerate(zip(b12, b17)):
    if x['text'] == y['text']:
        continue
    want = squash(straight(x['text']))
    run = None
    for n in (1, 2, 3):   # a Markdown block can be one to three of the editor's paragraphs (a list item's second <p>)
        for k in range(len(paras) - n + 1):
            if squash(straight(' '.join(p[4] for p in paras[k:k + n]))) == want:
                assert run is None, (i, 'found twice')
                run = paras[k:k + n]
        if run:
            break
    assert run, (i, x['text'][:70])
    parts = split_new([squash(p[4]) for p in run], squash(y['text']))
    for p, part in zip(run, parts):
        if squash(straight(p[4])) == squash(straight(part)):
            continue
        new_inner, dropped, moved = E.set_text(doc[p[2]:p[3]], part)
        edits.append((p[2], p[3], new_inner))
        report.append({'block': i, 'dropped': [str(d) for d in dropped], 'moved': [str(m) for m in moved]})
for si, ei, new_inner in sorted(edits, reverse=True):
    doc = doc[:si] + new_inner + doc[ei:]

# r12's payload builder, as it cleaned the live post's editor HTML (r12/substack/make_payload.py)
from make_payload import curl_nodes  # noqa: E402  (importing it builds draft A's files again, unchanged)

soup = BeautifulSoup(doc, 'html.parser')
root = soup.find('div', class_='ProseMirror')
for el in root.find_all(['figure', 'iframe', 'svg']):
    el.decompose()
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
blocks = [el.get_text('') for el in root.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li'])
          if not (el.name == 'li' and el.find(['p', 'ul', 'ol']))]
words = ' '.join(straight(' '.join(blocks)).split())
# every block of r17 is in the payload, word for word (marks straightened)
pay = squash(straight(' '.join(blocks)))
missing = [y['i'] for y in b17 if squash(straight(y['text'])) not in pay]
assert not missing, ('blocks of r17 not in the payload', missing[:10])
(HERE / 'PAYLOAD-B.html').write_text(body, encoding='utf-8')
(HERE / 'TEXT-B.txt').write_text(text, encoding='utf-8')
meta = {'source': 'r12.html with r17\'s words', 'r17_sha256': hashlib.sha256((FIX / 'r17' / 'r17.md').read_bytes()).hexdigest(),
        'title': 'Healing the Gut, draft B (temp, delete after)', 'chars': len(text), 'words': len(words.split()),
        'payload_sha256': hashlib.sha256(body.encode('utf-8')).hexdigest(),
        'words_sha256': hashlib.sha256(words.encode('utf-8')).hexdigest(),
        'straight_marks_left': sum(body.count(c) for c in '"\'') - body.count('href="') * 2,
        'paragraphs_changed': len(edits), 'tags_dropped_or_moved': [r for r in report if r['dropped'] or r['moved']]}
(HERE / 'PAYLOAD.json').write_text(json.dumps(meta, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({k: v for k, v in meta.items() if k != 'tags_dropped_or_moved'}, ensure_ascii=False))
print('tags dropped or moved:', json.dumps(meta['tags_dropped_or_moved'], ensure_ascii=False)[:1500])
