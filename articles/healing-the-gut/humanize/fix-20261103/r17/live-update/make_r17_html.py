#!/usr/bin/env python3
"""r17.html: the editor HTML his post gets in its third update (2026-11-06), from r12.html, the HTML the second update
put in (so the post's editor holds it now, E332), with r17's words in every paragraph that changed since r12.

Draft B (../substack/) read Human Written in his extension, no AI windows, on the same words (prediction #183,
../draft-b-check/). As there: each changed paragraph gets r17's words through html_text_edit.set_text, which keeps its
links, italics and bold on the same words, and a Markdown block that spans several editor paragraphs is cut where they
met (split_new). Unlike the payload, the post's own native blocks stay (its pictures, videos and paywall), and every
quote mark is curled the way the check read it (curl_nodes, E362 (gut): what goes into the live post is the text that was
checked, every character of it). Checks that every paragraph and list item of the result reads exactly as the line the
extension read (../substack/EXPECTED-TEXT-B.txt), in order. Writes r17.html. No API calls."""
import hashlib
import pathlib
import re
import sys

from bs4 import BeautifulSoup

HERE = pathlib.Path(__file__).resolve().parent
R17 = HERE.parent
FIX = R17.parent
REPO = HERE.parents[5]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
sys.path.insert(0, str(FIX / 'r12' / 'substack'))
import html_text_edit as E  # noqa: E402
import suggestion_review as sr  # noqa: E402

squash = lambda s: re.sub(r'\s+', ' ', s).strip()
straight = lambda s: s.translate(str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"'}))
b12 = sr.blocks((FIX / 'r12' / 'r12.md').read_text(encoding='utf-8'))
b17 = sr.blocks((R17 / 'r17.md').read_text(encoding='utf-8'))
assert len(b12) == len(b17)
src = (R17 / 'substack' / 'make_payload.py').read_text(encoding='utf-8')
ns = {}
exec(src[src.index('def split_new'):src.index("doc = (FIX / 'r12' / 'r12.html')")], {'difflib': None}, ns)
split_new = ns['split_new']

doc = (FIX / 'r12' / 'r12.html').read_text(encoding='utf-8')
paras = E.paragraphs(doc)
edits = []
for i, (x, y) in enumerate(zip(b12, b17)):
    if x['text'] == y['text']:
        continue
    want = squash(straight(x['text']))
    run = None
    for n in (1, 2, 3):
        for k in range(len(paras) - n + 1):
            if squash(straight(' '.join(p[4] for p in paras[k:k + n]))) == want:
                assert run is None, (i, 'found twice')
                run = paras[k:k + n]
        if run:
            break
    assert run, (i, x['text'][:70])
    for p, part in zip(run, split_new([squash(p[4]) for p in run], squash(y['text']))):
        if squash(straight(p[4])) == squash(straight(part)):
            continue
        new_inner, dropped, moved = E.set_text(doc[p[2]:p[3]], part)
        assert not dropped and not moved, (i, dropped, moved)
        edits.append((p[2], p[3], new_inner))
for si, ei, new_inner in sorted(edits, reverse=True):
    doc = doc[:si] + new_inner + doc[ei:]

from make_payload import curl_nodes  # noqa: E402  (r12's; importing it rebuilds draft A's files, unchanged)

soup = BeautifulSoup(doc, 'html.parser')
root = soup.find('div', class_='ProseMirror')
curl_nodes(root)
out = str(soup)

# every paragraph and list item now reads as the extension read draft B's, in order
check = BeautifulSoup(out, 'html.parser').find('div', class_='ProseMirror')
lines = []
for el in check.find_all(['p', 'li']):
    if el.name == 'li' and el.find(['p', 'ul', 'ol']):
        continue
    if el.find_parent(['figure']) or el.find_parent(class_=lambda c: c and ('youtube' in c or 'embed' in c)):
        continue
    t = el.get_text('').replace(' ', ' ')
    if t.strip() and not re.match(r'^https?://\S+$', t.strip()):
        lines.append(t.rstrip())
want = (R17 / 'substack' / 'EXPECTED-TEXT-B.txt').read_text(encoding='utf-8').split('\n')
got = [l for l in lines if squash(l) not in ('', 'Double click to interact with video')]
missing = [w for w in want if w not in got]
assert not missing, ('lines the check read that r17.html lacks', [m[:80] for m in missing[:5]])
(HERE / 'r17.html').write_text(out, encoding='utf-8')
print('r17.html', hashlib.sha256(out.encode('utf-8')).hexdigest(), len(edits), 'editor paragraphs changed;',
      len(want), 'checked lines all present')
