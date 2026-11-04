#!/usr/bin/env python3
"""apply_r01.py - round 1's answers (Joel, 2026-11-03 18:59 UTC; ANSWERS-R01-20261103-1859.json) put into the guide.

Starts from his post as published (../../original-blocks.json, the blocks of master.md) and writes the guide after round
1 (GUIDE-AFTER-R01.md, beside this script; it was ../../GUIDE-SO-FAR.md until round 2 went in, which now starts from it):

- every card he approved, as REVIEW-R01.json shows it (its edits, moves and inserts), with RP-4 his way: the paragraph
  goes but his line stays, in his words, as the last sentence of the paragraph before it;
- RP-13, where he overruled my "leave" ("remove it");
- the answers that change words: Q-1 (smell humic acid first), Q-4 (the 3 a.m. section's quote of the note matches it),
  Q-5 (room first in all four places), Q-7 (step 12's charcoal sentence goes).
SF-2 (left, as advised), Q-2 and Q-8 (a: nothing moves) change nothing here; Q-3 and Q-6 become lines drafted from his
words on round 2's page, and ST-1 (A) is round 2 itself.

The cards' edits are written against the review page's text (../../original-page.md: no bold marks, one list item a
block). Here each is applied to the article's own Markdown: a cut block or list item goes; a change of words is the page
text's changed middle, found once in the block's Markdown (bold marks allowed inside it) and replaced. Every edit has to
apply exactly once, or the script stops.

  python3 apply_r01.py            write GUIDE-AFTER-R01.md (and its blocks, GUIDE-AFTER-R01-blocks.json, with the
                                  round-1 block ids kept) and print what changed
"""
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parent.parent
BLOCKS = json.loads((ART / 'original-blocks.json').read_text(encoding='utf-8'))
PMAP = json.loads((ART / 'original-page-map.json').read_text(encoding='utf-8'))['map']
REVIEW = json.loads((HERE / 'REVIEW-R01.json').read_text(encoding='utf-8'))
ANSWERS = json.loads((HERE / 'ANSWERS-R01-20261103-1859.json').read_text(encoding='utf-8'))
OUT = HERE / 'GUIDE-AFTER-R01.md'

LIST_ITEM = re.compile(r'^(- |\d+\. )')
STATUS = {x['id']: x['status'] for x in ANSWERS['items']}
APPLY = [s for s in REVIEW['suggestions']
         if s['type'] != 'question' and (STATUS[s['id']] in ('approved', 'revise') and s['advice'] == 'approve'
                                         or s['id'] == 'RP-13')]

# ---------------------------------------------------------------- the document as units

doc = []          # [{'bid', 'md'} or {'bid', 'items': [md...], 'ordered': bool}]
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
        doc.append({'bid': b['id'], 'kind': b['kind'], 'items': items, 'ordered': b['kind'] == 'ol', 'cut': [False] * len(items)})
    else:
        doc.append({'bid': b['id'], 'kind': b['kind'], 'md': md})
UNIT = {u['bid']: u for u in doc}

PAGE = {}         # page index -> (bid, item index or None)
for bid, idxs in PMAP.items():
    u = UNIT[bid]
    if 'items' in u:
        assert len(idxs) == len(u['items']), (bid, len(idxs), len(u['items']))
        for k, i in enumerate(idxs):
            PAGE[i] = (bid, k)
    else:
        for i in idxs:
            PAGE[i] = (bid, None)


def strip_marks(md):
    """The Markdown without bold marks, and for each character of the result its place in the Markdown."""
    out, pos, i = [], [], 0
    while i < len(md):
        if md.startswith('**', i):
            i += 2
            continue
        out.append(md[i])
        pos.append(i)
        i += 1
    return ''.join(out), pos


def middle(before, after):
    """The changed middle of a page-text edit: (removed, inserted)."""
    a = 0
    while a < min(len(before), len(after)) and before[a] == after[a]:
        a += 1
    z = 0
    while z < min(len(before), len(after)) - a and before[-1 - z] == after[-1 - z]:
        z += 1
    return before[a:len(before) - z], after[a:len(after) - z], before[max(0, a - 30):a], before[len(before) - z:][:30]


def get_md(bid, k):
    u = UNIT[bid]
    return u['items'][k] if k is not None else u['md']


def set_md(bid, k, md):
    u = UNIT[bid]
    if k is not None:
        u['items'][k] = md
    else:
        u['md'] = md


LOG = []


def replace_once(bid, k, old, new, why):
    md = get_md(bid, k)
    if md.count(old) == 1:
        set_md(bid, k, md.replace(old, new))
        LOG.append('%s%s: %s' % (bid, '' if k is None else ' item %d' % (k + 1), why))
        return
    plain, pos = strip_marks(md)
    if plain.count(old) != 1:
        raise SystemExit('%s %s: %r found %d times in %r' % (why, bid, old, plain.count(old), md))
    s = plain.index(old)
    e = s + len(old)
    ms, me = pos[s], (pos[e - 1] + 1)
    seg = md[ms:me]
    # keep bold marks that open or close inside the replaced stretch balanced: only plain replacements are allowed here
    if '**' in seg:
        raise SystemExit('%s %s: the words cross a bold mark in %r' % (why, bid, md))
    set_md(bid, k, md[:ms] + new + md[me:])
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


def page_text_edit(card, e):
    bid, k = PAGE[e['block']]
    if not e['after']:
        cut(bid, k, card['id'])
        return
    rem, ins, left, right = middle(e['before'], e['after'])
    if not rem and not ins:
        raise SystemExit('%s: an edit that changes nothing' % card['id'])
    if not rem:
        # an insertion: anchor it on the words before it
        replace_once(bid, k, left, left + ins, card['id'])
    else:
        replace_once(bid, k, rem, ins, card['id'])


# ---------------------------------------------------------------- round 1's cards

moves, inserts = [], []
for card in APPLY:
    if card['id'] == 'RP-4':
        continue                                # his way, below
    for e in card.get('edits', []):
        page_text_edit(card, e)
    for m in card.get('moves', []):
        moves.append((card['id'], m))
    for ins in card.get('inserts', []):
        inserts.append((card['id'], ins))

# RP-4, his way: B142 goes; his line stays, in his words, at the end of the paragraph before it
cut('B142', None, 'RP-4')
UNIT['B141']['md'] = UNIT['B141']['md'] + ' A gut-driven mental hell is often mistaken as shadow work.'
LOG.append('B141: RP-4, his line ("A gut-driven mental hell is often mistaken as shadow work") added as its last sentence')

# ---------------------------------------------------------------- the answers that change words

replace_once('B144', 0, 'Smell humic acid, take a 5mg lick of it.',
             'Smell humic acid first; if that doesn’t help, take a 5mg lick of it.', 'Q-1 (a): smell it first')
replace_once('B272', None, '“No actions until morning”', '“No big actions until morning”', 'Q-4 (a): the quote matches the note')
replace_once('B252', None, 'body → room → human → time → meaning', 'room → body → human → time → meaning', 'Q-5 (a)')
replace_once('B375', 2, 'body → room → human → time', 'room → body → human → time', 'Q-5 (a)')
replace_once('B415', None, 'Then return to body, room, human, time, and love.', 'Then return to room, body, human, time, and love.',
             'Q-5 (a)')
replace_once('B54', None, ' Charcoal belongs only in the separate recent-oral-ingestion branch.', '', 'Q-7 (b)')

# ---------------------------------------------------------------- moves and inserts, in each card's order


def unit_of(page_i):
    bid, k = PAGE[page_i]
    return bid, k


def take(bids_items):
    """Remove these blocks (or all items of a list block) from the document and return them."""
    taken = []
    for bid, k in bids_items:
        u = UNIT[bid]
        if k is not None and len(u['items']) > 1:
            # moving a list item alone is not needed in round 1; a whole list moves as one block
            raise SystemExit('moving one item of %s is not supported' % bid)
        if u in taken:
            continue
        doc.remove(u)
        taken.append(u)
    return taken


def put_before(units, page_i):
    bid, k = unit_of(page_i)
    if k not in (None, 0):
        raise SystemExit('a move or insert before item %d of %s' % (k + 1, bid))
    at = doc.index(UNIT[bid])
    for n, u in enumerate(units):
        doc.insert(at + n, u)


for cid, ins in sorted(inserts, key=lambda x: x[1].get('seq', 0)):
    hashes = '#' * int(ins['kind'][1])
    u = {'bid': 'N-%s' % cid, 'kind': ins['kind'], 'md': '%s %s' % (hashes, ins['text'])}
    UNIT[u['bid']] = u
    put_before([u], ins['before'])
    LOG.append('%s: new heading "%s" before %s' % (cid, u['md'], PAGE[ins['before']][0]))

for cid, m in sorted(moves, key=lambda x: (x[0], x[1].get('seq', 0))):
    pairs, seen = [], set()
    for i in m['blocks']:
        bid, k = unit_of(i)
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


parts = [x for x in (unit_md(u) for u in doc) if x is not None]
# the guide's blocks after round 1, with their round-1 ids kept (new ones start with N-), for round 2's page
OUT_BLOCKS = HERE / 'GUIDE-AFTER-R01-blocks.json'
OUT_BLOCKS.write_text(json.dumps([{'id': u['bid'], 'kind': u['kind'], 'md': unit_md(u), 'text': None}
                                  for u in doc if unit_md(u) is not None], ensure_ascii=False, indent=1) + '\n',
                      encoding='utf-8')
# a divider left directly under another divider, or right before a heading that already follows one, would be a stray
text = '\n\n'.join(parts) + '\n'
OUT.write_text(text, encoding='utf-8')

orig = '\n\n'.join(b['md'] for b in BLOCKS)
w0, w1 = len(re.findall(r'\S+', orig)), len(re.findall(r'\S+', text))
print('\n'.join(LOG))
print('%d cards applied (%s); %d words -> %d (%+d); %s sha256 %s' % (
    len(APPLY), ', '.join(s['id'] for s in APPLY), w0, w1, w1 - w0, OUT.name, hashlib.sha256(text.encode()).hexdigest()))
