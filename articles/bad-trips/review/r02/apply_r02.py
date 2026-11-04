#!/usr/bin/env python3
"""apply_r02.py - round 2's answers (Joel, 2026-11-04 10:26 UTC; ANSWERS-R02-20261104-1026.json) put into the guide.

Starts from the guide after round 1 (../r01/GUIDE-AFTER-R01-blocks.json, made by ../r01/apply_r01.py) and writes the
guide after round 2 (GUIDE-AFTER-R02.md beside this script, and its blocks, GUIDE-AFTER-R02-blocks.json, with the block
ids kept; new blocks are N-<card>). The humanize pass starts from it (../../humanize/h01/swap.py makes
../../GUIDE-SO-FAR.md, the guide as it stands):

- every card he approved (all 26, none with a comment or his own version), as REVIEW-R02.json has it: its edits, moves
  and inserts;
- the "More:" line at the end of each checklist step, as "More: [the section's title](its link on Substack)" (the page
  shows the words, the card's insert carries the link);
- CL-14's link: "love" in step 14's heading links to his love page, as the Longer Triage's "Can love be reached yet?"
  did before LT-1 cut it (the card said so; the page couldn't show a link in a heading).

The cards' edits are written against the review page's text (PAGE-R02.md: no bold, links shown as their words, one list
item a block). Each change of words is applied to the block's own Markdown one changed stretch at a time (a word-level
diff of the page's before and after), so the links, bold and italics in the words around it stay as they were; a stretch
that covers a whole link or bold span takes its markup with it. After every edit, the block's Markdown is turned back into
page text the way PAGE-R02.md was made and must equal the card's "after" exactly, or the script stops.

  python3 apply_r02.py            write the guide after round 2 and print what changed
"""
import difflib
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parent.parent
sys.path.insert(0, str(ART.parents[1] / 'tools' / 'humanization'))
import suggestion_review as SR  # noqa: E402

BLOCKS = json.loads((HERE.parent / 'r01' / 'GUIDE-AFTER-R01-blocks.json').read_text(encoding='utf-8'))
PMAP = json.loads((HERE / 'PAGE-R02-map.json').read_text(encoding='utf-8'))['map']
REVIEW = json.loads((HERE / 'REVIEW-R02.json').read_text(encoding='utf-8'))
ANSWERS = json.loads((HERE / 'ANSWERS-R02-20261104-1026.json').read_text(encoding='utf-8'))
OUT = HERE / 'GUIDE-AFTER-R02.md'
OUT_BLOCKS = HERE / 'GUIDE-AFTER-R02-blocks.json'

LIST_ITEM = re.compile(r'^(- |\d+\. )')
STATUS = {x['id']: x['status'] for x in ANSWERS['items']}
assert ANSWERS['review_id'] == REVIEW['review_id'], (ANSWERS['review_id'], REVIEW['review_id'])
assert set(STATUS) == {s['id'] for s in REVIEW['suggestions']}, 'answers and cards differ'
for x in ANSWERS['items']:
    assert not x['your_version'] and not x['comment'], ('his own words on %s: put them in by hand' % x['id'])
APPLY = [s for s in REVIEW['suggestions'] if STATUS[s['id']] == 'approved']
LOVE = 'http://love.u-dont-exist.com/'

# ---------------------------------------------------------------- the document as units (as round 1's script)

doc = []
for b in BLOCKS:
    md = b['md']
    lines = md.split('\n')
    if b['kind'] in ('ul', 'ol') and lines and LIST_ITEM.match(lines[0]):
        items = []
        for ln in lines:
            if LIST_ITEM.match(ln):
                items.append(LIST_ITEM.sub('', ln, count=1))
            else:
                items[-1] += '\n' + ln
        doc.append({'bid': b['id'], 'kind': b['kind'], 'items': items, 'ordered': b['kind'] == 'ol',
                    'cut': [False] * len(items)})
    else:
        doc.append({'bid': b['id'], 'kind': b['kind'], 'md': md})
UNIT = {u['bid']: u for u in doc}

PAGE = {}
for bid, idxs in PMAP.items():
    u = UNIT[bid]
    if 'items' in u:
        assert len(idxs) == len(u['items']), (bid, len(idxs), len(u['items']))
        for k, i in enumerate(idxs):
            PAGE[i] = (bid, k)
    else:
        assert len(idxs) == 1 or u['kind'] == 'blockquote', (bid, idxs)
        for i in idxs:
            PAGE[i] = (bid, None)


def get_md(bid, k):
    u = UNIT[bid]
    return u['items'][k] if k is not None else u['md']


def set_md(bid, k, md):
    u = UNIT[bid]
    if k is not None:
        u['items'][k] = md
    else:
        u['md'] = md


def page_text(md, item):
    """The text the review page shows for this Markdown (as tools/page_md.py and suggestion_review.blocks make it)."""
    if item:
        md = '- ' + ' '.join(x.strip() for x in md.split('\n'))
    else:
        md = md.replace('  \n', ' ')
    md = md.replace('**', '')
    if re.search(r'\*\[|\]\([^)]*\)\*|\[\*', md):
        md = md.replace('*', '')
    return SR.blocks(md + '\n')[0]['text']


LINK = re.compile(r'\[([^\]]*)\]\(([^)\s]*(?:\([^)\s]*\)[^)\s]*)*)\)')


def plain_map(md):
    """md as plain text, with each plain character's place in md, and the markup spans (link or bold or italic) as
    (md start, md end, text start, text end) in md."""
    out, pos, spans = [], [], []
    i = 0
    while i < len(md):
        if md.startswith('**', i):
            j = md.find('**', i + 2)
            if j > 0:
                spans.append((i, j + 2, i + 2, j))
            i += 2
            continue
        if md[i] == '*':
            j = md.find('*', i + 1)
            if j > 0 and not md.startswith('**', j):
                spans.append((i, j + 1, i + 1, j))
            i += 1
            continue
        m = LINK.match(md, i)
        if m:
            spans.append((m.start(), m.end(), m.start(1), m.end(1)))
            for t in range(m.start(1), m.end(1)):
                if md.startswith('**', t) or (md[t] == '*'):
                    continue
                out.append(md[t])
                pos.append(t)
            i = m.end()
            continue
        if md.startswith('  \n', i):
            out.append(' ')
            pos.append(i)
            i += 3
            continue
        if md[i] == '\n':
            j = i + 1
            while j < len(md) and md[j] == ' ':
                j += 1
            out.append(' ')
            pos.append(i)
            i = j
            continue
        out.append(md[i])
        pos.append(i)
        i += 1
    return ''.join(out), pos, spans


TOKEN = re.compile(r'\s+|\w+|[^\w\s]')


def tokens(t):
    return TOKEN.findall(t)


LOG = []


def change_words(bid, k, before, after, why):
    md = get_md(bid, k)
    item = k is not None
    if page_text(md, item) != before:
        raise SystemExit('%s %s: the block is not what the card saw\n  md:   %r\n  card: %r' % (why, bid, md, before))
    plain, pos, spans = plain_map(md)
    if plain != before:
        raise SystemExit('%s %s: my plain text differs from the page\'s\n  mine: %r\n  page: %r' % (why, bid, plain, before))
    ta, tb = tokens(before), tokens(after)
    ca = [0]
    for t in ta:
        ca.append(ca[-1] + len(t))
    ops = [o for o in difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes() if o[0] != 'equal']
    for tag, i1, i2, j1, j2 in reversed(ops):
        ps, pe, new = ca[i1], ca[i2], ''.join(tb[j1:j2])
        if ps < pe:
            ms, me = pos[ps], pos[pe - 1] + 1
            for s0, s1, t0, t1 in sorted(spans, key=lambda s: s[1] - s[0]):
                if ms <= t0 and me >= t1:          # the stretch covers this span's text: its markup goes with it
                    ms, me = min(ms, s0), max(me, s1)
            for s0, s1, t0, t1 in spans:           # a stretch that cuts across a span's edge: not done blind
                inside = t0 <= ms and me <= t1
                outside = me <= s0 or ms >= s1
                covers = ms <= s0 and me >= s1
                if not (inside or outside or covers):
                    raise SystemExit('%s %s: %r cuts across markup in %r' % (why, bid, md[ms:me], md))
        else:
            ms = me = pos[ps] if ps < len(pos) else len(md)
        md = md[:ms] + new + md[me:]
    if page_text(md, item) != after:
        raise SystemExit('%s %s: the result is not the card\'s after\n  got:  %r\n  want: %r' % (
            why, bid, page_text(md, item), after))
    set_md(bid, k, md)
    LOG.append('%s%s: %s' % (bid, '' if k is None else ' item %d' % (k + 1), why))


def cut(bid, k, why):
    u = UNIT[bid]
    if k is None:
        assert not u.get('gone'), bid
        u['gone'] = True
    else:
        assert not u['cut'][k], (bid, k)
        u['cut'][k] = True
    LOG.append('%s%s: %s (cut)' % (bid, '' if k is None else ' item %d' % (k + 1), why))


def take(pairs):
    taken = []
    for bid, k in pairs:
        u = UNIT[bid]
        if k is not None and len(u['items']) > 1:
            raise SystemExit('moving one item of %s is not supported' % bid)
        if u in taken:
            continue
        doc.remove(u)
        taken.append(u)
    return taken


def put_before(units, page_i):
    bid, k = PAGE[page_i]
    if k not in (None, 0):
        raise SystemExit('a move or insert before item %d of %s' % (k + 1, bid))
    at = doc.index(UNIT[bid])
    for n, u in enumerate(units):
        doc.insert(at + n, u)


# ---------------------------------------------------------------- the cards

moves, inserts = [], []
for card in APPLY:
    for e in card.get('edits', []):
        bid, k = PAGE[e['block']]
        if not e['after']:
            cut(bid, k, card['id'])
        else:
            change_words(bid, k, e['before'], e['after'], card['id'])
    for m in card.get('moves', []):
        moves.append((card['id'], m))
    for ins in card.get('inserts', []):
        inserts.append((card['id'], ins))

# CL-14: "love" in step 14's heading takes the link the Longer Triage's fifth question had
assert 'CL-14' in STATUS and STATUS['CL-14'] == 'approved'
h = UNIT['B58']['md']
assert h == '## 14. Can I send love to the one suffering?', h
assert LOVE in UNIT['B88']['md'] and UNIT['B88'].get('gone'), 'the Longer Triage\'s love link should be the one cut'
UNIT['B58']['md'] = '## 14. Can I send [love](%s) to the one suffering?' % LOVE
LOG.append('B58: CL-14, "love" in the heading links to %s' % LOVE)

for cid, ins in sorted(inserts, key=lambda x: x[1].get('seq', 0)):
    if ins['kind'] == 'p':
        md = ins['text']
        if ins.get('href'):
            assert ins['text'].startswith('More: '), ins
            md = 'More: [%s](%s)' % (ins['text'][len('More: '):], ins['href'])
    else:
        md = '%s %s' % ('#' * int(ins['kind'][1]), ins['text'])
    u = {'bid': 'N-%s' % cid, 'kind': ins['kind'], 'md': md}
    assert u['bid'] not in UNIT, u['bid']
    UNIT[u['bid']] = u
    put_before([u], ins['before'])
    LOG.append('%s: new %s "%s" before %s' % (cid, ins['kind'], md, PAGE[ins['before']][0]))

for cid, m in sorted(moves, key=lambda x: (x[0], x[1].get('seq', 0))):
    pairs, seen = [], set()
    for i in m['blocks']:
        bid, k = PAGE[i]
        if bid not in seen:
            seen.add(bid)
            pairs.append((bid, None))
    put_before(take(pairs), m['before'])
    LOG.append('%s: %s moved before %s' % (cid, ', '.join(b for b, _ in pairs), PAGE[m['before']][0]))

# ---------------------------------------------------------------- write


def unit_md(u):
    if u.get('gone'):
        return None
    if 'items' in u:
        keep = [it for it, c in zip(u['items'], u['cut']) if not c]
        if not keep:
            return None
        if u['ordered']:
            return '\n'.join('%d. %s' % (n + 1, it) for n, it in enumerate(keep))
        return '\n'.join('- ' + it for it in keep)
    return u['md']


kept = [u for u in doc if unit_md(u) is not None]
# no divider left directly after another divider or at a heading that follows one
for a, b in zip(kept, kept[1:]):
    assert not (a['kind'] == 'hr' and b['kind'] == 'hr'), ('two dividers in a row', a['bid'], b['bid'])
text = '\n\n'.join(unit_md(u) for u in kept) + '\n'
OUT.write_text(text, encoding='utf-8')
OUT_BLOCKS.write_text(json.dumps([{'id': u['bid'], 'kind': u['kind'], 'md': unit_md(u), 'text': None} for u in kept],
                                 ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
w0 = len(re.findall(r'\S+', '\n\n'.join(b['md'] for b in BLOCKS)))
w1 = len(re.findall(r'\S+', text))
print('\n'.join(LOG))
print('%d cards applied; %d words -> %d (%+d); %s sha256 %s' % (len(APPLY), w0, w1, w1 - w0, OUT.name,
                                                               hashlib.sha256(text.encode()).hexdigest()))
