#!/usr/bin/env python3
"""apply_r04.py - round 4's answers (Joel, 2026-11-04 14:58 UTC; ANSWERS-R04-20261104-1458.json) put into the guide, and
the Quick Bad Trip Checklist taken out now that the triage app shows version 9 (his message of 11:35 UTC; the live
page's widget, saved from his laptop at 14:59 UTC, is byte for byte APP-V9-20261104.html: ../../experiments/t07-answers/).

Starts from the guide after round 3 (../r03/GUIDE-AFTER-R03-blocks.json, which round 4's page showed) and writes the guide
after round 4 (GUIDE-AFTER-R04.md beside this script, and GUIDE-AFTER-R04-blocks.json), which becomes
../../GUIDE-SO-FAR.md:

- W-CBD2 (approved, with his comment "now fix it so it passes pangram", which is the next step, not words to put in):
  the CBD sentences, with three links, as its card said: "approved" to the FDA's Epidiolex label, "12-week trial" to the
  trial the old sentence linked, "2025 study" to Patel et al. 2025 on PubMed;
- APP-1 to APP-4 (approved): the four lines that pointed to the checklist point to the triage app, "triage app" linking it;
- the checklist itself, B3 ("# Quick Bad Trip Checklist") to B64 (its closing divider), out (OWNER-EDITS
  checklist-to-app); B0, the app link at the top, and the post's picture stay. Three things only the checklist had (in
  neither the long part nor the app: each of its sentences was compared with both) move into the long part, his words
  as they were, the way round 2 moved what only the Longer Triage said (his structure answer A): step 1b's "These checks
  include several recognized stroke warning signs." (with its stroke.org link) after the long part's list of checks;
  step 3's "Soothing meditative music, like that of Chantress Seba and others on my music page, can be very helpful."
  (with his music page's link) into the Music list; and step 14's link to his love page, on "Sending Love" in the
  heading of Dealing With Sorrow (as CL-14 put it on "love" in step 14's heading).

Each change is made on the block's own Markdown and checked: the block turned back into page text the way PAGE-R04.md
was made must equal the card's "after" exactly, or the script stops.

  python3 apply_r04.py            write the guide after round 4 and print what changed
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

BLOCKS = json.loads((HERE.parent / 'r03' / 'GUIDE-AFTER-R03-blocks.json').read_text(encoding='utf-8'))
PMAP = json.loads((HERE / 'PAGE-R04-map.json').read_text(encoding='utf-8'))['map']
REVIEW = json.loads((HERE / 'REVIEW-R04.json').read_text(encoding='utf-8'))
ANSWERS = json.loads((HERE / 'ANSWERS-R04-20261104-1458.json').read_text(encoding='utf-8'))
OUT = HERE / 'GUIDE-AFTER-R04.md'
OUT_BLOCKS = HERE / 'GUIDE-AFTER-R04-blocks.json'

LIST_ITEM = re.compile(r'^(- |\d+\. )')
STATUS = {x['id']: x['status'] for x in ANSWERS['items']}
assert ANSWERS['review_id'] == REVIEW['review_id'], (ANSWERS['review_id'], REVIEW['review_id'])
assert set(STATUS) == {s['id'] for s in REVIEW['suggestions']}, 'answers and cards differ'
assert STATUS == {'W-CBD2': 'approved', 'APP-1': 'approved', 'APP-2': 'approved', 'APP-3': 'approved',
                  'APP-4': 'approved'}, STATUS
for x in ANSWERS['items']:
    assert x['your_version'] in ('', x['my_version']), ('his own words on %s' % x['id'])
    assert not x['comment'] or (x['id'] == 'W-CBD2' and x['comment'] == 'now fix it so it passes pangram'), x['id']
APPLY = [s for s in REVIEW['suggestions'] if STATUS[s['id']] == 'approved']
CARD = {s['id']: s for s in APPLY}
APP = 'https://ibogaqueen.com/1625-2/'
FDA = 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/210365s024s029s030lbl.pdf'
GEL = 'https://pubmed.ncbi.nlm.nih.gov/35802375/'
PATEL = 'https://pubmed.ncbi.nlm.nih.gov/40673944/'

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


# ---------------------------------------------------------------- the cards (each by hand: their words take links)


def by_hand(cid, bid, k, old_md, new_md):
    """Replace OLD_MD with NEW_MD in the block's Markdown; the page text of the result must be the card's after."""
    md = get_md(bid, k)
    assert md.count(old_md) == 1, (cid, bid, md)
    md = md.replace(old_md, new_md)
    want = CARD[cid]['edits'][0]['after']
    got = page_text(md, k is not None)
    if got != want:
        raise SystemExit('%s %s: the result is not the card\'s after\n  got:  %r\n  want: %r' % (cid, bid, got, want))
    set_md(bid, k, md)
    LOG.append('%s: %s' % (bid, cid))


by_hand('W-CBD2', 'B111', None,
        'CBD has established antiseizure activity in several epilepsy syndromes, and [transdermal CBD reaches systemic '
        'circulation](%s), although it has not been validated as rapid seizure rescue.' % GEL,
        'Purified oral CBD is [approved](%s) for the seizures of Lennox-Gastaut syndrome, Dravet syndrome and tuberous '
        'sclerosis complex. For focal seizures outside those syndromes, the evidence is mixed. In a [12-week trial](%s), '
        'a CBD skin gel reached the blood at levels like oral CBD\'s but did no better than placebo. In a '
        '[2025 study](%s) of high-dose oral CBD, around 23 mg/kg a day (about 1,400 mg for a 60 kg adult), focal '
        'seizures fell by about half to three quarters over nearly three years, but it had no placebo group to compare '
        'with. None of it tested CBD as rapid seizure rescue.' % (FDA, GEL, PATEL))
by_hand('APP-1', 'B234', None, 'The checklist above gives the order.', 'The [triage app](%s) gives the order.' % APP)
by_hand('APP-2', 'B272', None, 'The quick checklist above contains the stripped-down 3 a.m. plan.',
        'The [triage app](%s) has the stripped-down 3 a.m. plan.' % APP)
by_hand('APP-3', 'B370', None, 'return to the acute checklist instead', 'return to the [triage app](%s) instead' % APP)
by_hand('APP-4', 'B437', None, 'use the checklist first', 'use the [triage app](%s) first' % APP)

# the checklist: B3 to B64, out (OWNER-EDITS checklist-to-app; the triage app shows version 9)
ids = [u['bid'] for u in doc]
a, b = ids.index('B3'), ids.index('B64')
assert UNIT['B3']['md'] == '# Quick Bad Trip Checklist' and UNIT['B64']['kind'] == 'hr' and ids[b + 1] == 'B65', ids[b + 1]
for u in doc[a:b + 1]:
    u['gone'] = True
LOG.append('B3 to B64: the Quick Bad Trip Checklist, %d blocks, out (it is in the triage app, version 9)' % (b + 1 - a))

# what only the checklist had, into the long part (his words, with their links)
STROKE = 'https://www.stroke.org/en/about-stroke/stroke-symptoms'
MUSIC = 'http://music.u-dont-exist.com/'
LOVE = 'http://love.u-dont-exist.com/'
assert '[stroke warning signs](%s)' % STROKE in UNIT['B9']['md'] and '[music page](%s)' % MUSIC in UNIT['B16']['md']
assert '[love](%s)' % LOVE in UNIT['B58']['md']
md = UNIT['B104']['md']
first = 'While using DMSO, check wakefulness, breathing, temperature, speech, facial symmetry, both arms, balance, walking, bodily control, seizure activity, severe headache, repeated vomiting, chest pain, and vision.'
assert md.count(first) == 1, md
UNIT['B104']['md'] = md.replace(first, first + ' These checks include several recognized [stroke warning signs](%s).' % STROKE)
LOG.append('B104: step 1b\'s stroke warning signs line and link, after the list of checks')
u = UNIT['B304']
k = [n for n, it in enumerate(u['items']) if it.startswith('Try a steady drum rhythm')]
assert len(k) == 1, u['items']
u['items'].insert(k[0] + 1, 'Soothing meditative music, like that of Chantress Seba and others on my [music page](%s), can be very '
                  'helpful.' % MUSIC)
u['cut'].insert(k[0] + 1, False)
LOG.append('B304: step 3\'s Chantress Seba line and the music page link, into the Music list')
h = UNIT['B376']['md']
assert h == '## Dealing With Sorrow: Missing Versus Sending Love', h
UNIT['B376']['md'] = '## Dealing With Sorrow: Missing Versus [Sending Love](%s)' % LOVE
LOG.append('B376: step 14\'s love page link, on "Sending Love" in the heading')
moves = inserts = []

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
