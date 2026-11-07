#!/usr/bin/env python3
"""r31.html: the editor HTML his post gets in its next update, from r12.html, the HTML the second update put in (so the
post's editor holds it now, E332; the third update, r17, was never put in: Joel, 2026-11-06 21:26 UTC, "i will tell you if
i want an incremental publish, otherwise keep working on the fixes"), with r31's words in every paragraph that changed
since r12.

r31 is r30, the whole article his extension read Human Written with no window below Medium (draft E, #208), with
oxytocin's gloss corrected after his comment on F14-3 (Phase 5 checked again, Human Written, #209). As for r17.html:
each changed paragraph gets r31's words through html_text_edit.set_text (links, italics and bold kept on the same words),
the post's own native blocks stay (its pictures, videos and paywall), and every quote mark is curled the way the checks
read it (curl_nodes, E362 (gut)). One thing r17.html didn't need: Phase 4's one numbered step, an ordered list of one item
nested in the bullet that holds Phase 4's first paragraph, is joined to that paragraph in r30, so the paragraph takes the
joined words and the one-item list goes (as in draft E's payload, ../../r30/substack/make_payload_e.py).

Checks that every paragraph and list item of the result reads exactly as the lines the checks read, in order:
EXPECTED-TEXT-r31.txt, draft E's checked text (../../r30/substack/EXPECTED-TEXT-E.txt) with the one gloss changed.
Writes r31.html and EXPECTED-TEXT-r31.txt. No API calls."""
import difflib
import hashlib
import pathlib
import re
import sys

from bs4 import BeautifulSoup

HERE = pathlib.Path(__file__).resolve().parent
R31 = HERE.parent
FIX = R31.parent
REPO = HERE.parents[5]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
sys.path.insert(0, str(FIX / 'r12' / 'substack'))
import html_text_edit as E  # noqa: E402
import suggestion_review as sr  # noqa: E402

squash = lambda s: re.sub(r'\s+', ' ', s).strip()
straight = lambda s: s.translate(str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"'}))
b12 = sr.blocks((FIX / 'r12' / 'r12.md').read_text(encoding='utf-8'))
b31 = sr.blocks((R31 / 'r31.md').read_text(encoding='utf-8'))
P4, STEP = 58, 59
assert len(b12) == len(b31) + 1
assert b12[STEP]['text'].startswith('So check your organs (Brown).') and 'Or is it your bile?' in b31[P4]['text']
TARGET = {i: (b31[i]['text'] if i < STEP else None if i == STEP else b31[i - 1]['text']) for i in range(len(b12))}

src = (FIX / 'r30' / 'substack' / 'make_payload_e.py').read_text(encoding='utf-8')
ns = {}
exec(src[src.index('def split_new'):src.index("doc = (FIX / 'r12' / 'r12.html')")], {'difflib': difflib}, ns)
split_new = ns['split_new']

doc = (FIX / 'r12' / 'r12.html').read_text(encoding='utf-8')
paras = E.paragraphs(doc)
edits = []
for i, x in enumerate(b12):
    y = TARGET[i]
    if y is None or x['text'] == y:
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
    for p, part in zip(run, split_new([squash(p[4]) for p in run], squash(y))):
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
step_text = squash(straight(b12[STEP]['text']))
hits = [li for li in root.find_all('li') if li.find('p') and squash(straight(li.find('p').get_text(''))) == step_text]
assert len(hits) == 1, len(hits)
ol = hits[0].find_parent('ol')
assert ol is not None and len(ol.find_all('li', recursive=False)) == 1
assert squash(straight(ol.find_previous_sibling('p').get_text(''))) == squash(straight(b31[P4]['text']))
ol.decompose()
curl_nodes(root)
out = str(soup)

# every paragraph and list item now reads as the checks read them, in order, and nothing else does
expected = (FIX / 'r30' / 'substack' / 'EXPECTED-TEXT-E.txt').read_text(encoding='utf-8')
old_gloss, new_gloss = 'boosts oxytocin (the “love hormone”)', 'boosts oxytocin (a bonding hormone)'
assert expected.count(old_gloss) == 1
expected = expected.replace(old_gloss, new_gloss)
(HERE / 'EXPECTED-TEXT-r31.txt').write_text(expected, encoding='utf-8')
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
want = expected.split('\n')
got = [l for l in lines if squash(l) not in ('', 'Double click to interact with video')]
assert got == want, [(i, a[:60], b[:60]) for i, (a, b) in enumerate(zip(got, want)) if a != b][:5] or (len(got), len(want))
(HERE / 'r31.html').write_text(out, encoding='utf-8')
print('r31.html', hashlib.sha256(out.encode('utf-8')).hexdigest(), len(edits), 'editor paragraphs changed, one list removed;',
      len(want), 'checked lines, exactly and in order')
