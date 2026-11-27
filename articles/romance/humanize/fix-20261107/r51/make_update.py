#!/usr/bin/env python3
"""make_update.py: UPDATE-PLAN.json, what the live post's editor must hold after the update of 2026-11-27 (r51).

Joel, 2026-11-27 20:11 UTC: "yes update the post", with his check of the r50 draft A (every window Human High; B's r49
check was all High too). Post 197034035, "Romance Advice I Wish My Parents Taught Me".

The update is one transaction in the post's editor (update.js), never a paste, and touches only what changes:
- every live paragraph in whole/REPLACEMENTS.json (the fixed version: the checks' replacements, his answers and my tested
  changes, through r50) takes its new paragraphs; an empty list removes it. Each new paragraph keeps the live paragraph's
  links whose words are still there once, plus the links his answers added (r30/HIS-T4.json, r40/HIS-T9.json), the way
  whole/fixed_md.py puts them in FIXED.md, and 366's link on "who writes" to Esther Perel's post (his version on the
  second page, review/teach-20261107/ANSWERS-T2.json). His *word* emphasis becomes italics.
- the reel he asked for goes after 149 (r30/HIS-T4.json, embeds), as the Instagram block Substack itself made from its
  address (pasted into the temporary draft B, 2026-11-27 20:3x UTC: its attributes below); his new opening's YouTube
  video goes after 252's new paragraphs (r40/HIS-T9.json, embeds).
- every text in the post gets the typography swap (tools/humanization/typography_swap.py: straight quote marks, "--" for
  dashes), the new paragraphs here and the rest in the editor (update.js ports swap_text);
- the title's "Updated Nov 23, 2026" becomes "Updated Nov 27, 2026" (his rule: the date changes with every update).

The plan holds the live paragraph list's fingerprints (whole/LIVE-INDEX.txt), which the editor is checked against before
anything changes, and the paragraph list it must hold after (texts with the swap, whitespace removed).

  python3 articles/romance/humanize/fix-20261107/r51/make_update.py
"""
import hashlib
import html
import importlib.util
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parent
REPO = HERE.parents[4]
spec = importlib.util.spec_from_file_location('typography_swap', REPO / 'tools' / 'humanization' / 'typography_swap.py')
ts = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ts)
swap = lambda s: ts.swap_text(s)[0]
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
strip = lambda s: re.sub(r'\s+', '', s)

recs = [json.loads(l) for l in (FIX / 'live-check' / 'LIVE-POST-BLOCKS-20261123.jsonl').read_text(encoding='utf-8').splitlines()]
byn = {r['n']: r for r in recs if r.get('n') is not None}
index = [l.split() for l in (FIX / 'whole' / 'LIVE-INDEX.txt').read_text(encoding='utf-8').splitlines()]
repl = {int(k): v for k, v in json.loads((FIX / 'whole' / 'REPLACEMENTS.json').read_text(encoding='utf-8')).items()}

LAYER = json.loads((FIX / 'r30' / 'HIS-T4.json').read_text(encoding='utf-8'))
T9 = json.loads((FIX / 'r40' / 'HIS-T9.json').read_text(encoding='utf-8'))
links_of_card, card_of = {}, {}
for L in (LAYER, T9):
    for l in L.get('links', []):
        links_of_card.setdefault(l['card'], []).append((l['words'], l['href']))
    for ch in L['changes']:
        for n in ([ch['live']] if ch['kind'] == 'para' else ch['live'][:1]):
            card_of[n] = ch['card']
PEREL = (366, 'who writes', 'https://estherperel.substack.com/p/en-plus-when-you-come-alive-outside')
EMBEDS = [
    {'after': 149, 'type': 'instagram', 'why': 'r30/HIS-T4.json M-149: "and right here you can put this url in"',
     'attrs': {'instagram_id': 'Dfd1gZGN3cZ', 'title': '✨ A soul named Victoria on Instagram',
               'author_name': '@light_of_my_soul_22',
               'thumbnail_url': 'https://substack-post-media.s3.amazonaws.com/public/images/__ss-rehost__IG-snapshot-Dfd1gZGN3cZ.jpg',
               'like_count': None, 'comment_count': None,
               'profile_pic_url': 'https://substack-post-media.s3.amazonaws.com/public/images/__ss-rehost__IG-profile-pic-Dfd1gZGN3cZ.png',
               'follower_count': None, 'timestamp': None, 'belowTheFold': False}},
    {'after': 252, 'type': 'youtube2', 'why': 'r40/HIS-T9.json PRIMAL-1: the video on its own line between his fourth and fifth paragraphs',
     'attrs': {'videoId': 'ZsFKlxVUYG8', 'startTime': None, 'endTime': None}},
]
ATTRS = 'target="_blank" rel="noopener noreferrer nofollow"'


def para_html(text, links):
    """The paragraph's inner HTML: the swapped text, escaped, with *emphasis* as <em> and each link's words, where they
    appear once (a "before |words" link marks only the words after the bar), as a link."""
    t = swap(text)
    ems, plain, k = [], '', 0
    for m in re.finditer(r'(?<![\w*])\*([^*\s][^*]*?)\*(?![\w*])', t):
        plain += t[k:m.start()]
        ems.append((len(plain), len(plain) + len(m.group(1))))
        plain += m.group(1)
        k = m.end()
    plain += t[k:]
    spans = []
    for words, href in links:
        before, _, w = swap(words).rpartition('|')
        find = before + w
        if not w or plain.count(find) != 1:
            continue
        s = plain.index(find) + len(before)
        if any(not (s + len(w) <= a or s >= b) for a, b, _ in spans):
            continue
        spans.append((s, s + len(w), href))
    marks = sorted([(a, b, 'a', h) for a, b, h in spans] + [(a, b, 'em', None) for a, b in ems])
    out, k = '', 0
    for a, b, kind, h in marks:
        if a < k:
            raise SystemExit('overlapping marks in: ' + plain[:80])
        out += html.escape(plain[k:a], quote=False)
        inner = html.escape(plain[a:b], quote=False)
        out += ('<a href="%s" %s>%s</a>' % (html.escape(h), ATTRS, inner)) if kind == 'a' else '<em>%s</em>' % inner
        k = b
    out += html.escape(plain[k:], quote=False)
    return out, plain


ops = []
for n in sorted(repl):
    r = byn[n]
    links = [tuple(l) for l in r.get('links', [])] + links_of_card.get(card_of.get(n, ''), [])
    if n == PEREL[0]:
        links.append(PEREL[1:])
    news = [para_html(p, links) for p in repl[n]]
    ops.append({'n': n, 'tag': index[n][1], 'fp': index[n][2], 'html': [h for h, _ in news], 'text': [p for _, p in news]})
assert any(PEREL[2] in h for o in ops if o['n'] == 366 for h in o['html']), "366's link did not go in"

# the paragraph list after: each index entry's text(s), with the swap; a list item's paragraph (the P after its LI, with
# the same text) follows its LI; a removed paragraph has none
expected, prev = [], None
opn = {o['n']: o for o in ops}
for n, tag, fp in index:
    n = int(n)
    r = byn[n]
    if tag == 'P' and prev is not None and prev[1] == 'LI' and byn[prev[0]]['text'] == r['text']:
        texts = expected[-1][2]
    elif n in opn:
        texts = opn[n]['text']
    else:
        texts = [swap(norm(r['text']))]
    expected.append([n, tag, texts])
    prev = (n, tag)
flat = [strip(t) for _, _, ts_ in expected for t in ts_]

plan = {
    'post': 197034035,
    'url': 'https://ibogaqueen.substack.com/p/romance-advice-i-wish-my-parents',
    'made_from': {'replacements': hashlib.sha256((FIX / 'whole' / 'REPLACEMENTS.json').read_bytes()).hexdigest(),
                  'live_index': hashlib.sha256((FIX / 'whole' / 'LIVE-INDEX.txt').read_bytes()).hexdigest()},
    'title': {'from': 'Romance Advice I Wish My Parents Taught Me 🫶🏿💁🏿‍♂️🤦🏿‍♂️🤫😍 Updated Nov 23, 2026',
              'to': 'Romance Advice I Wish My Parents Taught Me 🫶🏿💁🏿‍♂️🤦🏿‍♂️🤫😍 Updated Nov 27, 2026'},
    'index': index,
    'ops': [{k: v for k, v in o.items() if k != 'text'} for o in ops],
    'embeds': EMBEDS,
    'expected_after': flat,
    'natives_after': {'captionedImage': 18, 'youtube2': 12, 'instagram': 3, 'button': 2, 'horizontalRule': 12},
}
out = HERE / 'UPDATE-PLAN.json'
out.write_text(json.dumps(plan, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(out.name, hashlib.sha256(out.read_bytes()).hexdigest(), 'ops', len(ops), 'removed', sum(1 for o in ops if not o['html']),
      'paragraphs after', len(flat), 'links in new paragraphs', sum(h.count('<a ') for o in ops for h in o['html']),
      'em', sum(h.count('<em>') for o in ops for h in o['html']))
