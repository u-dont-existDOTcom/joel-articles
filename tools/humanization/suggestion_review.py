#!/usr/bin/env python3
"""suggestion_review.py - the whole article with every suggestion marked where it applies, for Joel to decide.

Joel, 2026-10-25 14:40 UTC, after four lists of suggestions with my picks for the hypnosis guide: "i'm sorry this
current approach is way too dificult, you're giving me half suggestion that are out of context. why don't you give me
the full HTML guide with highlighting where you notice x,y,z type of problems (color-coded) and your suggestion for that
and then my comment box on your suggestion with approve reject reivse buttons etc i'm sure ytou can amek this
muchbetter". UDA's patterns/owner-questions-page.md (multi-item decision pages) had already asked for an interactive
page in the same turn as the suggestions; the four lists broke it (lesson E265).

The page is the article from its Markdown, every block in order with its P-number (para_numbers.py, the numbers on
every page he reads). Each suggestion is highlighted on the exact words it changes, in its type's colour, and its card
sits right under that paragraph: what changes (the paragraph as it would read, cut words struck through and new words
marked), why, what stays, my advice, and his buttons, Approve / Reject / Revise / Not approved yet, with a comment box.
Revise opens his own version of the paragraph, starting from mine. Nothing counts as approved until he clicks Approve
(REVIEW-INTERFACE-DIRECT-DECISION-ADDENDUM.md). A suggestion a reader made that I'd leave as it is shows as a quiet
grey line he can open and overrule. Answers save as he clicks (the artifact's store when the page is published with
the db capability, and this browser's storage) and export as JSON, which the page can import again. The form controls
are project-sources/review-form-controls.css, inlined (the 2026-10-23 white-on-white comment boxes).

  python3 tools/humanization/suggestion_review.py check REVIEW.json      # every span and before-text is in the article
  python3 tools/humanization/suggestion_review.py page REVIEW.json OUT.html

REVIEW.json (the lane's build script writes it; see find_quote, block_text and cut_text for its helpers):
  {"format": "joel-suggestion-review-v1", "review_id", "title", "intro": [paragraphs], "git_file": the page's file,
   "article": {"file": repo-relative Markdown, "sha256"}, "built", "links": {"guide", "review"} (GitHub pages to name),
   "types": {key: {"label", "about"}},
   "suggestions": [{
      "id": "CV-2.4" (stable; letters, digits, - . only), "type": a key of types, "title": a few words,
      "advice": "approve" (I suggest it) or "leave" (a reader suggested it, I'd leave the text as it is),
      "spans": [{"block": i, "start", "end"}]   the words to highlight (offsets in block_text(i)),
      "edits": [{"block": i, "before": block_text(i), "after": the block as it would read ("" = the block goes)}],
      "inserts": [{"before": i, "kind": "h1".."h4" (Markdown "#".."####") or "p", "text", "seq"}]   new blocks before block i,
      "moves": [{"blocks": [i, ...], "before": j, "seq"}]   blocks that move to just before block j (at one place,
                 inserts and moves go in "seq" order),
      "what", "why", "stays", "deciding", "advice_note", "found_by", "warning" (optional), "overlaps" (other ids on
      the same paragraphs, optional),
      "approve_label" (optional: "cut it", "use this wording", ...),
      "decided" (optional): {"status": "approved"|"rejected"|"revise", "text", "comment", "by", "at"}}]}
"""
import argparse
import datetime
import difflib
import hashlib
import html
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import para_numbers  # noqa: E402
from html_links import join_split_links  # noqa: E402  (a pasted post card's link, split across its heading)

TEMPLATE = HERE / 'suggestion_review_template.html'
FORM_CSS = ROOT / 'project-sources' / 'review-form-controls.css'
FORMAT = 'joel-suggestion-review-v1'
GENERATOR = 'suggestion_review.py 1.0 (2026-10-25)'
ID_OK = re.compile(r'^[A-Za-z0-9][A-Za-z0-9.\-]{0,80}$')
LINK = re.compile(r'\[([^\]]+)\]\(([^)\s]+)\)')
EMPH = re.compile(r'(?<![\w*])\*([^*\s][^*]*?)\*(?!\*)')
HEAD = re.compile(r'^(#{1,6})\s+(.*)$')
BULLET = re.compile(r'^([-*+])\s+(.*)$')
NUMBERED = re.compile(r'^(\d+)\.\s+(.*)$')
QUOTE_LINE = re.compile(r'^>\s?(.*)$')
NATIVE = {'%%checkout_url%%': 'subscribe button', '%%share_url%%': 'share button'}
STRAIGHT = str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"', '–': '-', '—': '-', ' ': ' '})


# ---------------------------------------------------------------- the article as blocks

def segments(s):
    """The inline pieces of one Markdown line: [{"t": text, "href": url or None, "em": bool}]."""
    out, pos = [], 0
    while pos < len(s):
        m1, m2 = LINK.search(s, pos), EMPH.search(s, pos)
        m = min((x for x in (m1, m2) if x), key=lambda x: x.start(), default=None)
        if not m:
            out.append({'t': s[pos:], 'href': None, 'em': False})
            break
        if m.start() > pos:
            out.append({'t': s[pos:m.start()], 'href': None, 'em': False})
        if m.re is LINK:
            out.append({'t': m.group(1), 'href': m.group(2), 'em': False})
        else:
            out.append({'t': m.group(1), 'href': None, 'em': True})
        pos = m.end()
    return [x for x in out if x['t']]


def native_of(kind, segs, text):
    """What a block is when it isn't prose: an image, a video, a post card, a button (REVIEW-INTERFACE-SPEC.md's native
    objects, so editor text such as "Double click to interact with video" never shows as the article's words)."""
    t = text.strip()
    if t == 'Double click to interact with video':
        return 'video'
    if re.fullmatch(r'\[?image \d+\]?', t):
        return t.strip('[]')
    if len(segs) == 1 and segs[0]['href'] in NATIVE:
        return NATIVE[segs[0]['href']]
    if len(segs) == 1 and segs[0]['href'] and kind.startswith('h'):
        return 'post card: ' + t
    if t.endswith('Copy link') and any(x['href'] for x in segs):
        return 'post card: ' + t[:-len('Copy link')].strip()
    if segs and segs[-1]['href'] and re.fullmatch(r'image \d+', segs[-1]['t'].strip()) and len(segs) > 1:
        return 'post card details'
    if t == 'Read full story' and segs and segs[0]['href']:
        return 'post card link'
    return None


def blocks(md):
    """The article's visible blocks in order: dicts with kind, level, marker, segs, text (plain, as a reader reads it),
    pn (its P-number, or None for a heading), section (the nearest heading above), path (the headings above it).
    The Markdown is read the way render_article_so_far.py reads it (a split post card joined first), so the P-numbers
    are the ones on his other pages."""
    raw = re.split(r'\n\s*\n', join_split_links(md))
    out, heads = [], []
    for b, pn in para_numbers.number_blocks(raw):
        v = para_numbers.visible(b)
        if not v:
            continue
        v = re.sub(r'\s*\n\s*', ' ', v)
        kind, level, marker, body = 'p', 0, '', v
        m = HEAD.match(v)
        if m:
            level = len(m.group(1))
            kind, body = 'h%d' % level, m.group(2).strip()
        elif BULLET.match(v):
            kind, marker, body = 'li', '•', BULLET.match(v).group(2)
        elif NUMBERED.match(v):
            kind, marker, body = 'oli', NUMBERED.match(v).group(1) + '.', NUMBERED.match(v).group(2)
        elif QUOTE_LINE.match(v):
            kind, body = 'quote', QUOTE_LINE.match(v).group(1)
        segs = segments(body)
        native = native_of(kind, segs, ''.join(x['t'] for x in segs))
        if level:
            heads = [h for h in heads if h[0] < level] + [(level, ''.join(x['t'] for x in segs))]
        out.append({'i': len(out), 'kind': kind, 'level': level, 'marker': marker, 'segs': segs, 'native': native,
                    'text': ''.join(x['t'] for x in segs), 'pn': pn,
                    'section': heads[-1][1] if heads else '', 'path': [h[1] for h in heads]})
    return out


def block_text(bl, i):
    return bl[i]['text']


def where(bl, i):
    """"Section, P3" for block i, the way the records name paragraphs; a heading is named by itself."""
    b = bl[i]
    if b['level']:
        return 'the heading "%s"' % b['text']
    return '%s, %s' % (b['section'] or 'the opening', b['pn'] or 'list item')


def norm_map(s):
    """(s with quotes, dashes and spaces made plain, a list giving each of its characters' index in s)."""
    out, idx = [], []
    for k, ch in enumerate(s):
        ch = ch.translate(STRAIGHT)
        if ch == '…':
            out += ['.', '.', '.']
            idx += [k, k, k]
            continue
        if ch.isspace():
            if out and out[-1] == ' ':
                continue
            ch = ' '
        out.append(ch)
        idx.append(k)
    return ''.join(out), idx


def find_quote(bl, quote, near=None):
    """(block index, start, end) of QUOTE: the one block whose text holds it, exactly or with only quote marks, dashes and
    spacing differing. NEAR (a block index) picks the nearest of several. Raises ValueError when it isn't there."""
    q = quote.strip()
    q = re.sub(r'^[-*•]\s+', '', q)
    hits = []
    for b in bl:
        t = b['text']
        for m in re.finditer(re.escape(q), t):
            hits.append((b['i'], m.start(), m.end()))
    if not hits:
        nq = norm_map(q)[0].strip()
        for b in bl:
            nt, idx = norm_map(b['text'])
            for m in re.finditer(re.escape(nq), nt):
                s, e = idx[m.start()], idx[m.end() - 1] + 1
                hits.append((b['i'], s, e))
    if not hits:
        raise ValueError('not in the article: %r' % quote[:120])
    if len(hits) > 1:
        if near is None:
            raise ValueError('in the article %d times: %r' % (len(hits), quote[:120]))
        hits.sort(key=lambda h: abs(h[0] - near))
    return hits[0]


HANGING = re.compile(r'\s*(?:[–—]|--|,|;|:)\s*$')
SENTENCE_END = re.compile(r'[.!?…][”"’\')\]]*$')


def cut_text(line, start, end):
    """LINE with line[start:end] cut, as it will read, tidied only where the cut joins (clarity_read.cut_text's rules:
    a dash, comma or colon left hanging goes, a comma left at a sentence's start goes, the next word gets its capital
    when the cut took a sentence's start, an emptied bracket goes). The rest of the paragraph stays byte for byte, so a
    cut never quietly fixes, or breaks, anything else in it."""
    b, r = line[:start].rstrip(), line[end:].lstrip()
    gone = line[start:end].rstrip()
    if gone[-1:] in '.!?' and b and not SENTENCE_END.search(b) and (not r or r[:1].isupper() or r[:1] in '“"‘\'('):
        b += gone[-1]   # the cut took the sentence's full stop with it
    if b.endswith('(') and r.startswith(')'):
        b, r = b[:-1].rstrip(), r[1:].lstrip()
    if (not r or r[0] in '.,;:!?)]') and HANGING.search(b):
        b = HANGING.sub('', b)
    starts = not b or SENTENCE_END.search(b)
    if starts and r[:1] in (',', ';', ':'):
        r = r[1:].lstrip()
    if starts:
        m = re.match(r'([“"‘\'(\[]*)([^\W\d_])', r)
        if m and m.group(2).islower():
            r = r[:m.start(2)] + m.group(2).upper() + r[m.end(2):]
    if not b or not r:
        return (b or r).strip()
    if r[0] in '.,;:!?)]”’':
        return b + r
    return b + ' ' + r


def links_in(bl, i, start, end):
    """The link texts of block i that the span start..end touches."""
    out, pos = [], 0
    for s in bl[i]['segs']:
        a, z = pos, pos + len(s['t'])
        if s['href'] and a < end and z > start:
            out.append(s['t'])
        pos = z
    return out


# ---------------------------------------------------------------- checks

def check(review, bl):
    """Problems with REVIEW against the article's blocks: [message]."""
    probs, ids = [], set()
    n = len(bl)
    for s in review['suggestions']:
        sid = s.get('id', '?')
        if not ID_OK.match(sid):
            probs.append('%s: id must be letters, digits, "-" and "." only' % sid)
        if sid in ids:
            probs.append('%s: id used twice' % sid)
        ids.add(sid)
        if s.get('type') not in review['types']:
            probs.append('%s: unknown type %r' % (sid, s.get('type')))
        if s.get('advice') not in ('approve', 'leave'):
            probs.append('%s: advice must be "approve" or "leave"' % sid)
        for k in ('title', 'what', 'why', 'stays', 'deciding'):
            if not (s.get(k) or '').strip():
                probs.append('%s: no %s' % (sid, k))
        if not (s.get('spans') or s.get('inserts') or s.get('moves')):
            probs.append('%s: nothing to show in the article (no spans, inserts or moves)' % sid)
        if not (s.get('edits') or s.get('inserts') or s.get('moves')):
            probs.append('%s: no change (edits, inserts or moves)' % sid)
        for sp in s.get('spans', []):
            i = sp.get('block')
            if not isinstance(i, int) or not 0 <= i < n:
                probs.append('%s: span block %r is not in the article' % (sid, i))
                continue
            if not 0 <= sp['start'] < sp['end'] <= len(bl[i]['text']):
                probs.append('%s: span %d-%d is outside block %d' % (sid, sp['start'], sp['end'], i))
        for e in s.get('edits', []):
            i = e.get('block')
            if not isinstance(i, int) or not 0 <= i < n:
                probs.append('%s: edit block %r is not in the article' % (sid, i))
                continue
            if e.get('before') != bl[i]['text']:
                probs.append('%s: the before-text of block %d is not the article\'s' % (sid, i))
            if e.get('after') == e.get('before'):
                probs.append('%s: block %d\'s after-text is the same as before' % (sid, i))
        for ins in s.get('inserts', []):
            if not 0 <= ins.get('before', -1) <= n or ins.get('kind') not in ('h1', 'h2', 'h3', 'h4', 'p') or not ins.get('text'):
                probs.append('%s: a bad insert %r' % (sid, ins))
        for mv in s.get('moves', []):
            bs, to = mv.get('blocks') or [], mv.get('before', -1)
            if not bs or any(not 0 <= i < n for i in bs) or not 0 <= to <= n or to in bs:
                probs.append('%s: a bad move %r' % (sid, mv))
        d = s.get('decided')
        if d and d.get('status') not in ('approved', 'rejected', 'revise'):
            probs.append('%s: decided status must be approved, rejected or revise' % sid)
    return probs


# ---------------------------------------------------------------- the page

def esc(s):
    return html.escape(s or '', quote=True)


def tokens(s):
    return re.findall(r'\w+|\s+|[^\w\s]', s)


def diff_html(before, after):
    """AFTER with the words cut from BEFORE struck through (del) and the new words marked (ins)."""
    a, b = tokens(before), tokens(after)
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == 'equal':
            out.append(esc(''.join(a[i1:i2])))
            continue
        if i2 > i1:
            out.append('<del>%s</del>' % esc(''.join(a[i1:i2])))
        if j2 > j1:
            added = ''.join(b[j1:j2])
            if '\n\n' in added:   # a new paragraph break: show it, since whitespace alone is invisible
                out.append('<ins class="br">¶ new paragraph</ins>' + esc(added).replace('\n\n', '\n'))
            else:
                out.append('<ins>%s</ins>' % esc(added))
    return ''.join(out)


def first_words(s, n=14):
    w = s.split()
    return ' '.join(w[:n]) + (' …' if len(w) > n else '')


def block_inner(b, marks):
    """Block b's inline HTML, with MARKS ([(start, end, suggestion id, type, advice)]) highlighted."""
    cuts = {0, len(b['text'])}
    for s, e, *_ in marks:
        cuts.update((s, e))
    pos, out = 0, []
    for seg in b['segs']:
        a, z = pos, pos + len(seg['t'])
        pts = sorted(c for c in cuts if a < c < z)
        for x, y in zip([a] + pts, pts + [z]):
            piece = esc(seg['t'][x - a:y - a])
            if seg['em']:
                piece = '<em>%s</em>' % piece
            if seg['href']:
                piece = '<a href="%s" target="_blank" rel="noopener noreferrer">%s</a>' % (esc(seg['href']), piece)
            cover = [m for m in marks if m[0] <= x and y <= m[1]]
            if cover:
                ids = ' '.join(m[2] for m in cover)
                cls = ' '.join(['hl', 't-' + cover[0][3]] + (['leave'] if all(m[4] == 'leave' for m in cover) else [])
                               + (['multi'] if len(cover) > 1 else []))
                piece = '<mark class="%s" data-s="%s">%s</mark>' % (cls, esc(ids), piece)
            out.append(piece)
        pos = z
    return ''.join(out)


def block_html(b, marks):
    loc = esc(b['pn'] or '')
    if b['native']:
        body = '<span class="native">[%s]</span>' % esc(b['native'])
        href = next((x['href'] for x in b['segs'] if x['href'] and x['href'].startswith('http')), None)
        if href:
            body += ' <a href="%s" target="_blank" rel="noopener noreferrer">open</a>' % esc(href)
        return '<div class="blk native-blk" id="b%d" data-b="%d">%s</div>' % (b['i'], b['i'], body)
    inner = block_inner(b, marks)
    if b['level']:
        lv = min(b['level'] + 1, 6)
        return '<h%d class="blk" id="b%d" data-b="%d">%s</h%d>' % (lv, b['i'], b['i'], inner, lv)
    pn = '<span class="pn">%s</span>' % loc if loc else ''
    if b['kind'] in ('li', 'oli'):
        return ('<div class="blk li" id="b%d" data-b="%d">%s<span class="mk">%s</span><span class="lt">%s</span></div>'
                % (b['i'], b['i'], pn, esc(b['marker']), inner))
    if b['kind'] == 'quote':
        return '<blockquote class="blk" id="b%d" data-b="%d">%s%s</blockquote>' % (b['i'], b['i'], pn, inner)
    return '<p class="blk" id="b%d" data-b="%d">%s%s</p>' % (b['i'], b['i'], pn, inner)


APPROVE = {'reread': 'use this wording', 'structure': 'make this change', 'innerchild': 'use this wording', 'typo': 'fix it',
           'caveat': 'cut it', 'repeat': 'cut it'}
APPROVE_LEAVE = {'reread': 'use the reader\'s version', 'structure': 'make this change anyway', 'innerchild': 'add it anyway',
                 'typo': 'fix it', 'caveat': 'cut it anyway', 'repeat': 'cut it anyway'}
KIND_NAMES = {'h1': 'heading', 'h2': 'heading', 'h3': 'subheading', 'h4': 'subheading', 'p': 'line'}


def change_html(s, bl):
    """The card's view of the change: each edited block as it would read, each new heading, each move."""
    out = []
    for ins in s.get('inserts', []):
        nxt = bl[ins['before']]['text'] if ins['before'] < len(bl) else ''
        tag = 'div' if ins['kind'] == 'p' else 'h5'
        out.append('<div class="chg"><div class="chg-k">New %s, above %s</div><%s class="ins-h"><ins>%s</ins></%s>'
                   '<div class="ctx">%s</div></div>' % (KIND_NAMES[ins['kind']], esc(where(bl, ins['before']) if ins['before'] < len(bl) else 'the end'),
                                                       tag, esc(ins['text']), tag, esc(first_words(nxt))))
    for mv in s.get('moves', []):
        moved = ' / '.join(first_words(bl[i]['text'], 12) for i in mv['blocks'])
        to = mv['before']
        prev = bl[to - 1]['text'] if to > 0 else ''
        nxt = bl[to]['text'] if to < len(bl) else ''
        out.append('<div class="chg"><div class="chg-k">Moves %s</div><div class="mv-src">%s</div>'
                   '<div class="chg-k">to sit between</div><div class="ctx">%s</div><div class="mv-arrow">↳ here</div>'
                   '<div class="ctx">%s</div><button type="button" class="link-btn go" data-go="b%d">Show where it goes</button></div>'
                   % ('from ' + esc(where(bl, mv['blocks'][0])), esc(moved), esc(first_words(prev, 16) if prev else '(the start)'),
                      esc(first_words(nxt, 16) if nxt else '(the end)'), to if to < len(bl) else to - 1))
    for e in s.get('edits', []):
        b = bl[e['block']]
        head = 'How %s would read' % esc(where(bl, e['block']))
        if not e['after']:
            out.append('<div class="chg"><div class="chg-k">%s is cut</div><div class="dif"><del>%s</del></div></div>'
                       % (esc(where(bl, e['block'])).capitalize(), esc(b['text'])))
        else:
            out.append('<div class="chg"><div class="chg-k">%s</div><div class="dif">%s</div></div>'
                       % (head, diff_html(b['text'], e['after'])))
    return ''.join(out)


def card_html(s, bl, types):
    t = types[s['type']]
    sid = s['id']
    leave = s['advice'] == 'leave'
    approve = s.get('approve_label') or (APPROVE_LEAVE if leave else APPROVE).get(s['type'], 'make this change')
    if leave and s.get('approve_label'):
        approve += ' anyway'
    rows = [('What changes', s['what']), ('Why', s['why']), ('What stays', s['stays']),
            ('You\'re deciding', s['deciding'])]
    info = ''.join('<div class="row"><span class="lab">%s</span> <span>%s</span></div>' % (esc(k), esc(v)) for k, v in rows)
    if s.get('warning'):
        info += '<div class="row warn"><span class="lab">Note</span> <span>%s</span></div>' % esc(s['warning'])
    if s.get('overlaps'):
        info += ('<div class="row also"><span class="lab">Also on this paragraph</span> %s</div>'
                 % ' '.join('<button type="button" class="link-btn go" data-go="c-%s">%s</button>' % (esc(o), esc(o))
                            for o in s['overlaps']))
    advice = ('<b>Leave it as it is.</b> ' if leave else '<b>Approve.</b> ') + esc(s.get('advice_note') or '')
    found = esc(s.get('found_by') or '')
    return f'''<section class="card t-{esc(s['type'])}{' leave' if leave else ''}" id="c-{esc(sid)}" data-id="{esc(sid)}" data-type="{esc(s['type'])}" data-advice="{esc(s['advice'])}" data-block="{(s.get('spans') or [{}])[0].get('block', '')}">
<div class="card-top"><button type="button" class="chip t-{esc(s['type'])}" data-filter-type="{esc(s['type'])}" title="{esc(t['about'])}">{esc(t['label'])}</button><span class="cid">{esc(sid)}</span><span class="ctitle">{esc(s['title'])}</span><span class="pill" aria-live="polite">Not approved yet</span><button type="button" class="link-btn fold" aria-expanded="{'false' if leave else 'true'}">{'Open' if leave else 'Fold'}</button></div>
<div class="card-body"{' hidden' if leave else ''}>
<div class="changes">{change_html(s, bl)}</div>
<div class="info">{info}<div class="row advice"><span class="lab">My advice</span> <span>{advice}</span></div>{f'<div class="row src"><span class="lab">Found by</span> <span>{found}</span></div>' if found else ''}</div>
<div class="decide" role="group" aria-label="Decision on {esc(sid)}"><button type="button" class="dec approve" data-dec="approved">Approve: {esc(approve)}</button><button type="button" class="dec reject" data-dec="rejected">Reject: keep it as it is</button><button type="button" class="dec revise" data-dec="revise">Revise</button><button type="button" class="dec undo" data-dec="pending">Not approved yet</button></div>
<label class="yours-wrap" hidden><span class="lab">Your version</span><textarea class="yours" rows="4" placeholder="Your wording, or what to change"></textarea></label>
<label class="note-wrap"><span class="lab">Your comment</span><textarea class="note" rows="2" placeholder="A note on this suggestion (optional)"></textarea></label>
<div class="saved-line"></div>
</div></section>'''


def page(review, md, bl):
    types = review['types']
    marks = {}
    cards_after = {}
    for s in review['suggestions']:
        for sp in s.get('spans', []):
            marks.setdefault(sp['block'], []).append((sp['start'], sp['end'], s['id'], s['type'], s['advice']))
        if s.get('spans'):
            at = max(sp['block'] for sp in s['spans'][:1])
        elif s.get('moves'):
            at = s['moves'][0]['blocks'][-1]
        else:
            at = s['inserts'][0]['before']
        cards_after.setdefault(at, []).append(s)
    pre_ins = {}
    for s in review['suggestions']:
        for ins in s.get('inserts', []):
            pre_ins.setdefault(ins['before'], []).append((s, ins))
        for mv in s.get('moves', []):
            pre_ins.setdefault(mv['before'], []).append((s, {'kind': 'move', 'text': first_words(bl[mv['blocks'][0]]['text'], 12),
                                                            'from': mv['blocks'][0], 'seq': mv.get('seq', 0)}))
            for i in mv['blocks']:
                marks.setdefault(i, [])
    moving = {i: s for s in review['suggestions'] for mv in s.get('moves', []) for i in mv['blocks']}
    parts, sections = [], []
    for b in bl:
        for s, ins in sorted(pre_ins.get(b['i'], []), key=lambda x: x[1].get('seq', 0)):
            parts.append(marker_html(s, ins, bl, types))
        h = block_html(b, sorted(marks.get(b['i'], [])))
        if b['i'] in moving:
            s = moving[b['i']]
            h = '<div class="moving t-%s%s" data-s="%s"><div class="moving-k">Moves (%s)</div>%s</div>' % (
                esc(s['type']), ' leave' if s['advice'] == 'leave' else '', esc(s['id']), esc(s['id']), h)
        parts.append(h)
        if b['level'] and b['level'] <= 3:
            sections.append((b['i'], b['level'], b['text']))
        for s in sorted(cards_after.get(b['i'], []), key=lambda s: ((s.get('spans') or [{'start': 0}])[0]['start'], s['id'])):
            parts.append(card_html(s, bl, types))
    for s, ins in pre_ins.get(len(bl), []):
        parts.append(marker_html(s, ins, bl, types))
    data = {
        'format': FORMAT, 'review_id': review['review_id'], 'title': review['title'], 'git_file': review.get('git_file', ''),
        'article': review['article'], 'built': review.get('built', ''), 'generator': GENERATOR,
        'types': types,
        'suggestions': [{k: s.get(k) for k in ('id', 'type', 'title', 'advice', 'what', 'deciding', 'decided')}
                        | {'where': where(bl, (s.get('spans') or [{'block': None}])[0]['block']) if s.get('spans') else
                           where(bl, s['moves'][0]['blocks'][0]) if s.get('moves') else
                           'above ' + where(bl, s['inserts'][0]['before']) if s['inserts'][0]['before'] < len(bl) else 'the end',
                           'proposed': proposed_text(s, bl), 'before': before_text(s, bl)}
                        for s in review['suggestions']],
        'sections': [{'b': i, 'level': lv, 'text': t} for i, lv, t in sections],
    }
    form_css = FORM_CSS.read_text(encoding='utf-8')
    tpl = TEMPLATE.read_text(encoding='utf-8')
    legend = ''.join('<button type="button" class="chip t-%s" data-filter-type="%s" aria-pressed="true" title="%s">%s <span class="n" data-count-type="%s"></span></button>'
                     % (esc(k), esc(k), esc(v['about']), esc(v['label']), esc(k)) for k, v in types.items())
    intro = ''.join('<p>%s</p>' % x for x in review.get('intro', []))
    out = (tpl.replace('__TITLE__', esc(review['title']))
              .replace('__INTRO__', intro)
              .replace('__LEGEND__', legend)
              .replace('__SRC__', source_line(review))
              .replace('/*__FORM_CSS__*/', form_css)
              .replace('__MAIN__', '\n'.join(parts))
              .replace('__DATA__', json.dumps(data, ensure_ascii=False).replace('</', '<\\/')))
    return out


def source_line(review):
    """Where the page comes from, as links he can open (repo_links.py: never a repository path)."""
    links = review.get('links') or {}
    guide = links.get('guide')
    data = links.get('review')
    g = '<a href="%s" target="_blank" rel="noopener noreferrer">the guide so far</a>' % esc(guide) if guide else 'the guide so far'
    d = '<a href="%s" target="_blank" rel="noopener noreferrer">the list of suggestions</a>' % esc(data) if data else 'the list of suggestions'
    return ('This page is a view of what\'s in Git: %s (version %s) and %s, built %s. Your answers go into Git as well, once '
            'you tell me you\'re done.' % (g, esc(review['article']['sha256'][:8]), d, esc(review.get('built', ''))))


def marker_html(s, ins, bl, types):
    leave = ' leave' if s['advice'] == 'leave' else ''
    if ins['kind'] == 'move':
        return ('<div class="marker t-%s%s" data-s="%s"><span class="mk-k">%s moves here:</span> %s '
                '<button type="button" class="link-btn go" data-go="c-%s">See the card</button></div>'
                % (esc(s['type']), leave, esc(s['id']), esc(s['id']), esc(ins['text']), esc(s['id'])))
    return ('<div class="marker t-%s%s" data-s="%s"><span class="mk-k">%s, new %s:</span> <span class="mk-h">%s</span></div>'
            % (esc(s['type']), leave, esc(s['id']), esc(s['id']), KIND_NAMES[ins['kind']], esc(ins['text'])))


def proposed_text(s, bl):
    """The text his Revise box starts from: my version of every block the suggestion changes."""
    parts = []
    for ins in s.get('inserts', []):
        parts.append(('#' * int(ins['kind'][1]) + ' ' if ins['kind'] != 'p' else '') + ins['text'])
    for e in s.get('edits', []):
        parts.append(e['after'] if e['after'] else '(cut: %s)' % first_words(bl[e['block']]['text'], 10))
    for mv in s.get('moves', []):
        parts.append('(move "%s" to just before "%s")' % (first_words(bl[mv['blocks'][0]]['text'], 8),
                                                         first_words(bl[mv['before']]['text'], 8) if mv['before'] < len(bl) else 'the end'))
    return '\n\n'.join(parts)


def before_text(s, bl):
    return '\n\n'.join(bl[e['block']]['text'] for e in s.get('edits', []))


def load(review_path):
    review = json.loads(pathlib.Path(review_path).read_text(encoding='utf-8'))
    if review.get('format') != FORMAT:
        raise SystemExit('not a %s file: %s' % (FORMAT, review_path))
    art = ROOT / review['article']['file']
    md = art.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    if sha != review['article']['sha256']:
        raise SystemExit('the article changed since REVIEW.json was built (%s, not %s): build it again'
                         % (sha[:12], review['article']['sha256'][:12]))
    return review, md, blocks(md)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    c = sub.add_parser('check')
    c.add_argument('review')
    p = sub.add_parser('page')
    p.add_argument('review')
    p.add_argument('out')
    a = ap.parse_args(argv)
    review, md, bl = load(a.review)
    probs = check(review, bl)
    for x in probs:
        print('PROBLEM', x)
    if a.cmd == 'check':
        print('%d suggestions, %d problems' % (len(review['suggestions']), len(probs)))
        return 1 if probs else 0
    if probs:
        print('not writing the page: fix the problems first')
        return 1
    out = page(review, md, bl)
    pathlib.Path(a.out).write_text(out, encoding='utf-8')
    print(a.out, len(out), 'bytes,', len(review['suggestions']), 'suggestions')
    return 0


if __name__ == '__main__':
    sys.exit(main())
