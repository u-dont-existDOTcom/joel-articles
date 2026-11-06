#!/usr/bin/env python3
"""The paste payloads for two whole-article checks through temporary Substack drafts (the free route; Joel, 2026-11-03
22:02 UTC: "we don't do whole article checks with pangram GUI ... i have a free route for those"):
  draft C: r20, the clarity fixes and Phase 5's second try at its first two steps (../../r20/);
  draft D: r21, the clarity fixes and the third try (../r21.md).
Draft B (r17, #183) read those two steps Low, and a cut of Phases 3 to 6 reads them AI even unchanged (#187), so only the
whole article can say which try, if either, reads them High; everything else in C and D is r17 word for word except the
two clarity fixes, which read Human, High in their own stretch (#185).

Each payload is built as draft B's was (../../r17/substack/make_payload.py): r12.html, the live post's editor HTML block
for block, with every paragraph whose words changed since r12 given the new words through html_text_edit.set_text (links,
italics and bold kept on the same words); no pictures, video embeds or paywall marker; every quote mark curled the way the
post shows it (E362 (gut)). Writes PAYLOAD-<X>.html, EXPECTED-TEXT-<X>.txt (the text his extension reads,
substack_check_text.checked_text) and PAYLOADS.json. No API calls."""
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
DRAFTS = {'C': ('r20', FIX / 'r20' / 'r20.md'), 'D': ('r21', FIX / 'r21' / 'r21.md')}
b12 = sr.blocks((FIX / 'r12' / 'r12.md').read_text(encoding='utf-8'))


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


def build(letter, name, path):
    bn = sr.blocks(path.read_text(encoding='utf-8'))
    assert len(b12) == len(bn)
    doc = (FIX / 'r12' / 'r12.html').read_text(encoding='utf-8')
    paras = E.paragraphs(doc)
    edits, report = [], []
    for i, (x, y) in enumerate(zip(b12, bn)):
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
        parts = split_new([squash(p[4]) for p in run], squash(y['text']))
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
    assert not missing, (letter, 'blocks not in the payload', missing[:10])
    checked = SCT.checked_text(body)
    (HERE / ('PAYLOAD-%s.html' % letter)).write_text(body, encoding='utf-8')
    (HERE / ('EXPECTED-TEXT-%s.txt' % letter)).write_text(checked, encoding='utf-8')
    words = ' '.join(straight(' '.join(blocks)).split())
    return {'draft': letter, 'source': 'r12.html with %s\'s words' % name,
            'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'title': 'Healing the Gut, draft %s (temp, delete after)' % letter,
            'words': len(words.split()), 'payload_sha256': hashlib.sha256(body.encode('utf-8')).hexdigest(),
            'words_sha256': hashlib.sha256(words.encode('utf-8')).hexdigest(),
            'checked_chars': len(checked), 'checked_sha256': hashlib.sha256(checked.encode('utf-8')).hexdigest(),
            'straight_marks_left': sum(body.count(c) for c in '"\'') - body.count('href="') * 2,
            'paragraphs_changed': len(edits), 'tags_dropped_or_moved': [r for r in report if r['dropped'] or r['moved']]}


out = {k: build(k, *v) for k, v in DRAFTS.items()}
# the drafts differ from draft B only where their sources differ from r17
b_text = (FIX / 'r17' / 'substack' / 'EXPECTED-TEXT-B.txt').read_text(encoding='utf-8').split('\n')
for k in out:
    lines = (HERE / ('EXPECTED-TEXT-%s.txt' % k)).read_text(encoding='utf-8').split('\n')
    out[k]['lines_changed_from_B'] = [i for i, (a, b) in enumerate(zip(b_text, lines)) if a != b]
    assert len(lines) == len(b_text), (k, len(lines), len(b_text))
(HERE / 'PAYLOADS.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
for k, m in out.items():
    print(k, {x: m[x] for x in ('words', 'checked_chars', 'checked_sha256', 'straight_marks_left', 'paragraphs_changed',
                                'lines_changed_from_B')}, 'tags:', m['tags_dropped_or_moved'][:3])
