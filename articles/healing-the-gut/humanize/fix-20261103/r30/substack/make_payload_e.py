#!/usr/bin/env python3
"""The paste payload for draft E, the whole-article check of r30 through a temporary Substack draft (the free route;
Joel, 2026-11-03 22:02 UTC: "we don't do whole article checks with pangram GUI ... i have a free route for those").
r30 is r22 (r17 with batch 13's F13-1) with batch 14's fixes: Phase 4's one numbered step joined to the paragraph above
it, with the bile case asked first, and Phase 5's opener and three steps. Every paragraph or section that tested AI by
itself now tests Human (gate gut-2026-11-07a: #206, #207; the ledger names no open window in r30).

Built as drafts C and D were (../../r21/substack/make_payloads.py): r12.html, the live post's editor HTML, with every
paragraph whose words changed since r12 given the new words through html_text_edit.set_text (links, italics and bold kept
on the same words); no pictures, video embeds or paywall marker; every quote mark curled as the post shows it (E362
(gut)). One thing those drafts didn't need: r12's Phase 4 step is an ordered list of one item nested in the bullet that
holds Phase 4's first paragraph, and r30 joins the two, so that paragraph takes the joined words and the one-item list
goes. Writes PAYLOAD-E.html, EXPECTED-TEXT-E.txt (the text his extension reads, substack_check_text.checked_text) and
PAYLOADS.json. No API calls."""
import difflib
import hashlib
import json
import pathlib
import re
import sys

from bs4 import BeautifulSoup

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parents[1]
REPO = HERE.parents[5]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
sys.path.insert(0, str(FIX / 'r12' / 'substack'))
import html_text_edit as E  # noqa: E402
import substack_check_text as SCT  # noqa: E402
import suggestion_review as sr  # noqa: E402
from make_payload import curl_nodes  # noqa: E402  (r12's builder; importing it rebuilds draft A's files, unchanged)

squash = lambda s: re.sub(r'\s+', ' ', s).strip()
straight = lambda s: s.translate(str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"'}))
SRC = FIX / 'r30' / 'r30.md'
b12 = sr.blocks((FIX / 'r12' / 'r12.md').read_text(encoding='utf-8'))
bn = sr.blocks(SRC.read_text(encoding='utf-8'))
P4, STEP = 58, 59
assert len(b12) == len(bn) + 1
assert b12[P4]['text'].startswith('Benjamin Brown') and b12[STEP]['text'].startswith('So check your organs (Brown).')
assert bn[P4]['text'].startswith('Benjamin Brown') and 'Or is it your bile?' in bn[P4]['text']
TARGET = {i: (bn[i]['text'] if i < STEP else None if i == STEP else bn[i - 1]['text']) for i in range(len(b12))}


def split_new(old_parts, new_text):
    """The new block's text cut where the old block's paragraphs met (draft B's rule)."""
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
    parts = split_new([squash(p[4]) for p in run], squash(y))
    for p, part in zip(run, parts):
        if squash(straight(p[4])) == squash(straight(part)):
            continue
        new_inner, dropped, moved = E.set_text(doc[p[2]:p[3]], part)
        edits.append((p[2], p[3], new_inner))
        report.append({'block': i, 'dropped': [str(d) for d in dropped], 'moved': [str(m) for m in moved]})
for si, ei, new_inner in sorted(edits, reverse=True):
    doc = doc[:si] + new_inner + doc[ei:]
soup = BeautifulSoup(doc, 'html.parser')
root = soup.find('div', class_='ProseMirror')
# the join: r12's one-item ordered list under Phase 4's first paragraph goes; its words are in that paragraph now
step_text = squash(straight(b12[STEP]['text']))
hits = [li for li in root.find_all('li') if li.find('p') and squash(straight(li.find('p').get_text(''))) == step_text]
assert len(hits) == 1, len(hits)
ol = hits[0].find_parent('ol')
assert ol is not None and len(ol.find_all('li', recursive=False)) == 1
assert squash(straight(ol.find_previous_sibling('p').get_text(''))) == squash(straight(bn[P4]['text']))
ol.decompose()
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
blocks = [el.get_text('') for el in root.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li'])
          if not (el.name == 'li' and el.find(['p', 'ul', 'ol']))]
pay = squash(straight(' '.join(blocks)))
missing = [y['i'] for y in bn if squash(straight(y['text'])) not in pay]
assert not missing, ('blocks not in the payload', missing[:10])
assert step_text not in pay
checked = SCT.checked_text(body)
(HERE / 'PAYLOAD-E.html').write_text(body, encoding='utf-8')
(HERE / 'EXPECTED-TEXT-E.txt').write_text(checked, encoding='utf-8')
words = ' '.join(straight(' '.join(blocks)).split())
b_lines = (FIX / 'r17' / 'substack' / 'EXPECTED-TEXT-B.txt').read_text(encoding='utf-8').split('\n')
e_lines = checked.split('\n')
changed = []
for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, b_lines, e_lines, autojunk=False).get_opcodes():
    if tag != 'equal':
        changed.append({'B': [i1, i2], 'E': [j1, j2], 'kind': tag})
out = {'E': {'draft': 'E', 'source': 'r12.html with r30\'s words, Phase 4\'s one-item step list joined to its paragraph',
             'source_sha256': hashlib.sha256(SRC.read_bytes()).hexdigest(),
             'title': 'Healing the Gut, draft E (temp, delete after)',
             'words': len(words.split()), 'payload_sha256': hashlib.sha256(body.encode('utf-8')).hexdigest(),
             'words_sha256': hashlib.sha256(words.encode('utf-8')).hexdigest(),
             'checked_chars': len(checked), 'checked_lines': len(e_lines),
             'checked_sha256': hashlib.sha256(checked.encode('utf-8')).hexdigest(),
             'straight_marks_left': sum(body.count(c) for c in '"\'') - body.count('href="') * 2,
             'paragraphs_changed': len(edits), 'lists_removed': 1,
             'tags_dropped_or_moved': [r for r in report if r['dropped'] or r['moved']],
             'lines_changed_from_B': changed}}
(HERE / 'PAYLOADS.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
m = out['E']
print({x: m[x] for x in ('words', 'checked_chars', 'checked_lines', 'checked_sha256', 'straight_marks_left',
                         'paragraphs_changed', 'lines_changed_from_B')}, 'tags:', m['tags_dropped_or_moved'][:3])
