#!/usr/bin/env python3
"""apply_r03.py - round 3's answers (Joel, 2026-11-04 14:25 UTC; ANSWERS-R03-20261104-1425.json) put into the guide.

Round 3 is the warnings check (gate E344; ../../experiments/t05-warnings/WARNINGS-CHECK.md). Starts from the guide as
it stood after round 2 (../../GUIDE-SO-FAR-blocks.json, which round 3's page showed) and writes the guide after round 3
(GUIDE-AFTER-R03.md beside this script, and its blocks, GUIDE-AFTER-R03-blocks.json, with the block ids kept), which
becomes ../../GUIDE-SO-FAR.md:

- the 7 cards he approved, as REVIEW-R03.json has them (W-SS, W-ITCH, W-SLEEP, W-TAR, W-NSAID, W-CHOLINE, W-CHEST; W-SS
  came back with his version equal to mine);
- W-SLEEP's link: "proven in rats" was the link to the rat study; the new sentence, "In rats, higher doses made sleep
  lighter.", carries the same link (its card said so; the page shows link words only);
- not applied: W-GLORY (rejected: "not sure why mice with no immune system says about an herb humans use traditionally
  already") and W-CBD (to revise, with his comment: the paragraph goes back to him redone, on round 4's page).

The cards' edits are written against the review page's text (PAGE-R03.md: no bold, links shown as their words, one list
item a block). Each change of words is applied to the block's own Markdown one changed stretch at a time (a word-level
diff of the page's before and after), so the links, bold and italics in the words around it stay as they were; a stretch
that covers a whole link or bold span takes its markup with it. After every edit, the block's Markdown is turned back into
page text the way PAGE-R03.md was made and must equal the card's "after" exactly, or the script stops.

  python3 apply_r03.py            write the guide after round 3 and print what changed
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

BLOCKS = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
PMAP = json.loads((HERE / 'PAGE-R03-map.json').read_text(encoding='utf-8'))['map']
REVIEW = json.loads((HERE / 'REVIEW-R03.json').read_text(encoding='utf-8'))
ANSWERS = json.loads((HERE / 'ANSWERS-R03-20261104-1425.json').read_text(encoding='utf-8'))
OUT = HERE / 'GUIDE-AFTER-R03.md'
OUT_BLOCKS = HERE / 'GUIDE-AFTER-R03-blocks.json'

LIST_ITEM = re.compile(r'^(- |\d+\. )')
STATUS = {x['id']: x['status'] for x in ANSWERS['items']}
assert ANSWERS['review_id'] == REVIEW['review_id'], (ANSWERS['review_id'], REVIEW['review_id'])
assert set(STATUS) == {s['id'] for s in REVIEW['suggestions']}, 'answers and cards differ'
for x in ANSWERS['items']:
    if x['status'] == 'approved':   # an approved card with his own words would need them put in by hand
        assert not x['comment'] and x['your_version'] in ('', x['my_version']), ('his own words on %s' % x['id'])
assert STATUS == {'W-CBD': 'revise', 'W-SS': 'approved', 'W-ITCH': 'approved', 'W-SLEEP': 'approved',
                  'W-TAR': 'approved', 'W-NSAID': 'approved', 'W-CHOLINE': 'approved', 'W-GLORY': 'rejected',
                  'W-CHEST': 'approved'}, STATUS
APPLY = [s for s in REVIEW['suggestions'] if STATUS[s['id']] == 'approved']
RATS = 'https://www.sciencedirect.com/science/article/abs/pii/S0378427405000810'

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
    if card['id'] == 'W-SLEEP':
        continue          # done by hand below, with its link
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

# W-SLEEP: the rat study's link moves from "proven in rats" to the new sentence (its card: "the same link")
k = 2
md = UNIT['B203']['items'][k]
old = 'This is [proven in rats](%s).' % RATS
assert md.count(old) == 1, md
UNIT['B203']['items'][k] = md.replace(old, '[In rats, higher doses made sleep lighter](%s).' % RATS)
want = [s for s in APPLY if s['id'] == 'W-SLEEP'][0]['edits'][0]['after']
assert page_text(UNIT['B203']['items'][k], True) == want, (page_text(UNIT['B203']['items'][k], True), want)
LOG.append('B203 item 3: W-SLEEP, the link moves with the words (same address)')

assert not moves and not inserts, (moves, inserts)

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
