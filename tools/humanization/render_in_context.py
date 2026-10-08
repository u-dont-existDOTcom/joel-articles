#!/usr/bin/env python3
"""render_in_context.py - an article's paragraphs beside their source, with the changes marked.

Shared version (2026-09-30) of the inner child lane's page tool, for any article and any
source. Joel, 2026-09-30 03:29 UTC: "I like how you are doing this original vs new diff,
that's good make that durable"; and 17:09 UTC, on a list of changes he couldn't follow:
"you should have used the side by side comparison script". It carries his standing rule to
show humanization work in context, with the source next to each paragraph.

Usage:
  python3 render_in_context.py MAP.json OUT.html --article ARTICLE.md --source SOURCE
          [--since REV | --against-source] [--source-label TEXT]

ARTICLE.md is the humanized text (Markdown). SOURCE is what it was made from: Markdown or
plain text, or HTML (tags are stripped). Only the labels and notes in the map are typed by
hand; paragraph text comes from ARTICLE and SOURCE, so the page can't show a version that
isn't the one in the files.

Two ways to mark changes:
  --since REV        against the version of ARTICLE at git revision REV (default HEAD): the
                     version Joel last saw. Run it before committing the turn.
  --against-source   against the row's source paragraph (the first "source" start in the
                     row): what the rewrite changed from the original.
Either way, highlighted words are new and struck words are cut.

MAP.json:
{
 "title": "The New Age May Dawn Suddenly",
 "meta": "Community article · section 1 · 2026-09-30",
 "intro": ["one paragraph of explanation", "..."],
 "blocks": [
  {"headings": ["## The New Age May Dawn Suddenly"],
   "rows": [
    {"label": "P2", "article": "I just put a movie",
     "source": ["I recently put my father"], "notes": ["What I'd do: ...", "..."]},
    {"label": "P5 · candidate", "text": "...", "flag": "a span Pangram flagged",
     "source": [{"quote": "part of a paragraph", "from": "source paragraph 4"}], "note": "..."}
   ]}
 ]
}
"article" is the start of a paragraph in ARTICLE; "text" is a candidate that isn't in it.
A "text" row that proposes a change to a paragraph in ARTICLE (its label says PROPOSAL, or it
has "proposal_of": the start of that paragraph) is diffed against it, so the proposed words are
highlighted and any cut ones struck (Joel, 2026-10-01 15:59: "on the proposals please highlight
the new part that's proposed so it's easier to read"). A proposal on a candidate that isn't in
ARTICLE gives that candidate's whole text as "proposal_of_text" (2026-10-03).
A lead-in that ends with a colon and the list right after it count as one paragraph, and the
list keeps its lines on the page (2026-10-01: Love Doesn't Wait P12, whose row showed only its
lead-in, and whose proposal highlighted the whole list as new).
"source" lists starts of source paragraphs, or {"quote": ..., "from": ...} for part of one;
[] for none. The lane's older key "guide" is read the same way. "note" is one line; "notes"
is a list shown as bullets.

Context (Joel, 2026-10-07 15:44: "whenever you give me the in-context side by side, you need
to actually give me the context in that page so i can understand what's coming from what").
Every row has a place in ARTICLE, and the page shows it: the section path above the first row
of each block, the article paragraph right before a row (or run of rows next to each other),
and the paragraph or heading right after it. A row in ARTICLE ("article") or a proposal
("proposal_of") has its place already. A candidate ("text") says where it would go:
  "after": "start of the ARTICLE paragraph (or heading line) it would follow", or
  "after_row": "label of an earlier row in this map that it would follow" (B2 after B1).
A candidate without a place stops the page, so it can't go out without its context; a row
that isn't article text at all (a link, a note) can say "place": "none". --context N shows N
paragraphs on each side (default 1).

Repeats (2026-10-08; Joel, 2026-10-07 23:18: "some of that looked like it was duplicating other
stuff from before ... did you make the dedup pass before trying to humanize?"). A row can list
what in it the article, or another row, already says:
  "repeats": [{"span": "words in this row", "in": "start of the ARTICLE paragraph that says it",
               "says": "the words there", "how": "optional: same point, same words"}]
Use "in_row": "label of another row" instead of "in" for a repeat between two drafts. The span is
marked blue, and a note gives the section and the words that already say it. Every span and every
"says" has to be in its text, or the page stops: a dedup note can't quote something that isn't
there. (On a row that shows a diff, the spans aren't marked, and the notes still list them.)
A block can have "intro": ["a paragraph shown under its headings", ...].

What a draft carries (2026-10-08; Joel, 02:23: "i also don't understand how you got depth draft 1 from the r4
guide? doesn't look like a good rewrite of that one sentence. i'm so confused. same for draft 2 it seems like
way more than the one sentence it's coming from?"). The turn-35 page gave each draft the first sentence of its
guide paragraph as its source, so drafts that carry the whole paragraph looked like inflated rewrites. Now:
  - a {"quote": ...} that's part of a paragraph in SOURCE is shown inside that whole paragraph, with the quoted
    part marked, so a fragment can't stand in for the passage;
  - a row can list "carries": [{"draft": "a sentence of the draft", "guide": "the guide words it carries"
    (or null: added by the writer), "note": "optional"}], shown as a two-column table. Every quote is
    checked against the row and the source.
"""
import argparse, difflib, html, json, math, pathlib, re, subprocess, sys

QUOTES = str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"'})
LINK = re.compile(r'\[([^\]]*)\]\(([^)]*)\)')
LIST_LINE = re.compile(r'^(\d+\.|[-*+]) ', re.M)
BR = '\u00b6'  # a line break inside a paragraph with a list; a word of its own, so diffs keep it

CSS = """
:root{--bg:#fbfaf7;--fg:#1f1d1a;--mute:#6b665e;--line:#e3ded4;--card:#fff;--mark:rgba(240,190,60,.35);--flag:rgba(255,86,48,.16);--dup:rgba(60,130,230,.14);--dupline:#3c82e6;--link:#2f5fa7}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#171614;--fg:#ece8e1;--mute:#a39d93;--line:#34312c;--card:#201e1b;--mark:rgba(240,190,60,.28);--flag:rgba(255,86,48,.25);--dup:rgba(90,150,240,.22);--dupline:#7fb0f5;--link:#8fb4ee}}
:root[data-theme=dark]{--bg:#171614;--fg:#ece8e1;--mute:#a39d93;--line:#34312c;--card:#201e1b;--mark:rgba(240,190,60,.28);--flag:rgba(255,86,48,.25);--dup:rgba(90,150,240,.22);--dupline:#7fb0f5;--link:#8fb4ee}
body{background:var(--bg);color:var(--fg);font:17px/1.6 Georgia,serif;margin:0;padding:24px 16px}
main{max-width:1100px;margin:0 auto} h1,h2,h3{font-family:system-ui,sans-serif;line-height:1.25}
a{color:var(--link)}
.meta{font:14px/1.5 system-ui,sans-serif;color:var(--mute)}
.intro{font:15px/1.55 system-ui,sans-serif;max-width:760px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:14px 0} @media(max-width:760px){.grid{grid-template-columns:1fr}}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 18px;overflow-wrap:anywhere}
.lbl{font:600 13px/1.3 system-ui,sans-serif;text-transform:uppercase;letter-spacing:.04em;color:var(--mute)}
.mark{background:var(--mark);border-radius:3px;padding:0 2px} .flag{background:var(--flag);border-radius:3px;padding:0 2px}
.dup{background:var(--dup);border-bottom:2px dotted var(--dupline);border-radius:3px;padding:0 2px}
.carries{width:100%;border-collapse:collapse;font:14px/1.45 system-ui,sans-serif;margin-top:4px}
.carries th,.carries td{border-top:1px solid var(--line);padding:6px 8px 6px 0;vertical-align:top;text-align:left}
.carries th{font-weight:600;color:var(--mute)} .add{color:var(--mute);font-style:italic}
del{color:var(--mute);text-decoration-thickness:1px}
.notes{font:15px/1.5 system-ui,sans-serif;margin:8px 0 0;padding-left:20px} .notes li{margin:4px 0}
.block{margin-top:28px}
.ctx{background:transparent;border:1px dashed var(--line);border-radius:10px;padding:10px 16px;margin:10px 0;color:var(--mute);font-size:15px;overflow-wrap:anywhere}
.ctx p{margin:.35em 0} .ctx .h{font:600 15px/1.3 system-ui,sans-serif;color:var(--fg)}
.where{font:13px/1.4 system-ui,sans-serif;color:var(--mute);margin:4px 0 0}
"""


def paragraphs(md):
    md = re.sub(r'<!--.*?-->', '', md, flags=re.S)
    out = []
    for p in (p.strip() for p in re.split(r'\n\s*\n', md) if p.strip()):
        if out and LIST_LINE.match(p) and out[-1].endswith(':'):
            out[-1] += '\n' + p  # a lead-in and its list
        else:
            out.append(p)
    return out


def keep_lines(t):
    """Mark the line breaks of a paragraph that has a list, so they survive the whitespace collapse."""
    t = t.strip()
    return re.sub(r'\s*\n\s*', ' %s ' % BR, t) if LIST_LINE.search(t) else t


def html_text(s):
    s = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', s, flags=re.S)
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'</(p|h[1-6]|li|blockquote|div)>', '\n\n', s)
    s = html.unescape(re.sub(r'<[^>]+>', '', s))
    return re.sub(r'\n\s*\n+', '\n\n', s).strip()


def plain(p):
    """A paragraph's visible text (no link targets or emphasis marks) and its links."""
    links = LINK.findall(p)
    t = keep_lines(LINK.sub(r'\1', p).replace('*', ''))
    return re.sub(r'\s+', ' ', t).strip(), links


def find(paras, start, what):
    key = start.translate(QUOTES)
    hits = [p for p in paras if plain(p)[0].translate(QUOTES).startswith(key)]
    if len(hits) != 1:
        sys.exit('%s: %d paragraphs start with %r' % (what, len(hits), start))
    return hits[0]


def best_match(text, old_paras):
    tw, best, score = text.split(), None, 0.0
    for p in old_paras:
        pt = plain(p)[0]
        r = difflib.SequenceMatcher(None, pt.split(), tw, autojunk=False).ratio()
        if r > score:
            best, score = pt, r
    return best if score >= 0.4 else None


def diff_html(old, new):
    a, b = old.split(), new.split()
    segs = [[op == 'equal', a[i1:i2], b[j1:j2]]
            for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes()]
    # A word or two left "equal" between two changes ("like", "a") chops a rewritten sentence
    # into pieces; fold them into one change so the cut and the new words each read whole.
    merged = True
    while merged:
        merged = False
        for k in range(1, len(segs) - 1):
            if segs[k][0] and len(segs[k][2]) <= 2 and not segs[k - 1][0] and not segs[k + 1][0]:
                p, e, n = segs[k - 1], segs[k], segs[k + 1]
                segs[k - 1:k + 2] = [[False, p[1] + e[1] + n[1], p[2] + e[2] + n[2]]]
                merged = True
                break
    out = []
    for same, old_w, new_w in segs:
        if same:
            out.append(html.escape(' '.join(new_w)))
            continue
        if old_w:
            out.append('<del>%s</del>' % html.escape(' '.join(old_w)))
        if new_w:
            out.append('<span class="mark">%s</span>' % html.escape(' '.join(new_w)))
    return ' '.join(out)


def flag_html(text, span):
    i = text.find(span)
    if i < 0:
        sys.exit('flag span not in its text: %r' % span[:60])
    return (html.escape(text[:i]) + '<span class="flag">%s</span>' % html.escape(span)
            + html.escape(text[i + len(span):]))


def spans_html(text, spans):
    """text with each (span, css class) wrapped. Every span has to be in the text (curly and straight
    quotes count as the same), and no two may overlap."""
    key, found = text.translate(QUOTES), []
    for span, cls in spans:
        i = key.find(span.translate(QUOTES))
        if i < 0:
            sys.exit('%s span not in the row\'s text: %r' % ('repeat' if cls == 'dup' else cls, span[:60]))
        found.append((i, i + len(span), cls))
    found.sort()
    for (_, end, _), (start, _, _) in zip(found, found[1:]):
        if start < end:
            sys.exit('two marked spans overlap at %r' % text[start:end][:60])
    out, k = [], 0
    for i, j, cls in found:
        out += [html.escape(text[k:i]), '<span class="%s">%s</span>' % (cls, html.escape(text[i:j]))]
        k = j
    out.append(html.escape(text[k:]))
    return ''.join(out)


def row_text(r, cur):
    """What a row shows: its candidate text, or its article paragraph."""
    if 'text' in r:
        return re.sub(r'\s+', ' ', keep_lines(r['text']))
    return plain(find(cur, r['article'], r.get('label', 'row')))[0]


def repeat_notes(r, cur, rows):
    """The dedup notes for a row: where the article (or another row) already says what its spans say.
    Each span and each quote is checked against the text it names."""
    lab, text, out = r.get('label', 'row'), None, []
    for rp in r.get('repeats', []):
        text = text if text is not None else row_text(r, cur)
        if rp['span'].translate(QUOTES) not in text.translate(QUOTES):
            sys.exit('%s: repeat span not in the row: %r' % (lab, rp['span'][:60]))
        if rp.get('in'):
            i = find_index(cur, rp['in'], lab + ' (repeat "in")')
            there, where = plain(cur[i])[0], 'Already in the article, in %s' % ' › '.join(section_path(cur, i))
        elif rp.get('in_row'):
            if rp['in_row'] not in rows:
                sys.exit('%s: repeat in_row %r is not a row label' % (lab, rp['in_row']))
            there, where = row_text(rows[rp['in_row']], cur), 'Also in %s, on this page' % rp['in_row']
        else:
            sys.exit('%s: a repeat needs "in" (an article paragraph) or "in_row" (a row label)' % lab)
        if rp['says'].translate(QUOTES) not in there.translate(QUOTES):
            sys.exit('%s: the repeat quote is not in that paragraph: %r' % (lab, rp['says'][:60]))
        out.append('%s: “%s”%s' % (where, rp['says'], (' (%s)' % rp['how']) if rp.get('how') else ''))
    return out


def whole_paragraph(quote, sparas):
    """The source paragraph a quote comes from, when it's in the source file (else None)."""
    key = re.sub(r'\s+', ' ', quote).translate(QUOTES).strip()
    for p in sparas:
        t = plain(p)[0]
        if key and key in t.translate(QUOTES):
            return t
    return None


def carries_html(r, items, sparas, text):
    """The row's "carries" list as a table: each draft sentence beside the guide words it carries, or "added by
    the writer" (Joel, 2026-10-08 02:23: "i also don't understand how you got depth draft 1 from the r4 guide? doesn't
    look like a good rewrite of that one sentence"). Every quote is checked: the draft words against the row, the
    guide words against the row's source cell or the source file."""
    if not r.get('carries'):
        return ''
    lab = r.get('label', 'row')
    cell = ' '.join(plain(find(sparas, g, 'source'))[0] if isinstance(g, str) else (whole_paragraph(g['quote'], sparas) or g['quote'])
                    for g in items).translate(QUOTES)
    whole = ' '.join(plain(p)[0] for p in sparas).translate(QUOTES)
    rows = []
    for c in r['carries']:
        d = c['draft']
        if re.sub(r'\s+', ' ', d).translate(QUOTES) not in text.translate(QUOTES):
            sys.exit('%s: a "carries" draft quote is not in the row: %r' % (lab, d[:60]))
        g = c.get('guide')
        if g and g.translate(QUOTES) not in cell and g.translate(QUOTES) not in whole:
            sys.exit('%s: a "carries" guide quote is not in the source: %r' % (lab, g[:60]))
        gcell = html.escape(g) if g else '<span class="add">added by the writer</span>'
        if c.get('note'):
            gcell += ' <span class="add">(%s)</span>' % html.escape(c['note'])
        rows.append('<tr><td>%s</td><td>%s</td></tr>' % (html.escape(d), gcell))
    return ('<p class="meta">What each sentence carries:</p><table class="carries"><tr><th>The draft</th><th>The guide</th></tr>%s</table>'
            % ''.join(rows))


def source_cell(items, sparas, label):
    if not items:
        return '<p class="lbl">No %s</p>' % html.escape(label.lower())
    out, prev = [], None
    for g in items:
        if isinstance(g, dict):
            src = ' · ' + html.escape(g['from']) if g.get('from') else ''
            whole = whole_paragraph(g['quote'], sparas)
            q = re.sub(r'\s+', ' ', g['quote']).strip()
            if whole and whole.translate(QUOTES) != q.translate(QUOTES):
                # A quote is never shown alone when its paragraph is in the source: the page shows the whole
                # paragraph, with the quoted part marked (2026-10-08: the turn-35 page showed one sentence of each
                # guide paragraph, and the drafts that carry the whole paragraph looked like inflated rewrites).
                i = whole.translate(QUOTES).find(q.translate(QUOTES))
                body = (html.escape(whole[:i]) + '<span class="mark">%s</span>' % html.escape(whole[i:i + len(q)])
                        + html.escape(whole[i + len(q):]))
                out.append('<p class="lbl">%s%s · the marked part, in its paragraph</p><p>%s</p>' % (html.escape(label), src, body))
            else:
                out.append('<p class="lbl">%s%s</p><p>%s</p>' % (html.escape(label), src, html.escape(g['quote'])))
        else:
            # Whole source paragraphs in a row (a lead-in and its list items) share one label.
            lbl = '' if isinstance(prev, str) else '<p class="lbl">%s</p>' % html.escape(label)
            out.append('%s<p>%s</p>' % (lbl, html.escape(plain(find(sparas, g, 'source'))[0])))
        prev = g
    return ''.join(out)


HEAD = re.compile(r'^(#{1,6})\s+(.*)$')


def find_index(paras, start, what):
    key = start.translate(QUOTES)
    hits = [i for i, p in enumerate(paras) if plain(p)[0].translate(QUOTES).startswith(key)]
    if len(hits) != 1:
        sys.exit('%s: %d paragraphs start with %r' % (what, len(hits), start))
    return hits[0]


def place_rows(m, cur):
    """Each row's position in the article: a paragraph's own index for a row in the article or a
    proposal, and a fraction after the paragraph (or row) it follows for a candidate."""
    pos, by_label, used = {}, {}, {}
    for bi, blk in enumerate(m['blocks']):
        for ri, r in enumerate(blk['rows']):
            key, lab = (bi, ri), r.get('label', 'row')
            if 'article' in r:
                pos[key] = float(find_index(cur, r['article'], lab))
            elif r.get('proposal_of'):
                pos[key] = float(find_index(cur, r['proposal_of'], lab))
            elif r.get('after'):
                i = find_index(cur, r['after'], lab + ' (after)')
                n = used.get(i, 0); used[i] = n + 1
                pos[key] = i + 0.5 + n * 0.01
            elif r.get('after_row'):
                if r['after_row'] not in by_label:
                    sys.exit('%s: after_row %r is not an earlier row label' % (lab, r['after_row']))
                pos[key] = pos[by_label[r['after_row']]] + 0.001
            elif r.get('place') == 'none' or (r.get('text', '').startswith('https://') and ' ' not in r.get('text', '')):
                pos[key] = None
            else:
                sys.exit('%s: a candidate needs a place in the article ("after", "after_row" or "proposal_of"), so '
                         'the page can show what comes before and after it (Joel, 2026-10-07)' % lab)
            by_label[lab] = key
    return pos


def section_path(cur, i):
    """The headings above paragraph i, outermost first."""
    path, level = [], 7
    for j in range(min(int(i), len(cur) - 1), -1, -1):
        m = HEAD.match(cur[j].strip())
        if m and len(m.group(1)) < level:
            level = len(m.group(1))
            path.insert(0, m.group(2).strip())
            if level == 1:
                break
    return path


def ctx_html(cur, idxs, label):
    out = ['<div class="ctx"><p class="lbl">%s</p>' % html.escape(label)]
    for i in idxs:
        m = HEAD.match(cur[i].strip())
        if m:
            out.append('<p class="h">%s %s</p>' % ('#' * len(m.group(1)), html.escape(LINK.sub(r'\1', m.group(2)).replace('*', ''))))
        else:
            out.append('<p>%s</p>' % html.escape(plain(cur[i])[0]).replace(BR, '<br>'))
    out.append('</div>')
    return ''.join(out)


def before_idxs(cur, p, n):
    """Up to n article paragraphs right before position p (a heading counts, and doesn't use up n)."""
    i = int(p) - 1 if p == int(p) else int(p)
    out, k = [], 0
    while i >= 0 and k < n:
        out.insert(0, i)
        if not HEAD.match(cur[i].strip()):
            k += 1
        i -= 1
    return out


def after_idxs(cur, p, n):
    """Up to n article paragraphs right after position p. A heading doesn't use up n, so when a section
    starts next, its heading and its first paragraph both show (2026-10-07: Also Look Outward opens with
    "Once you're in that happy place", which points back past the heading)."""
    i = int(p) + 1
    out, k = [], 0
    while i < len(cur) and k < n:
        out.append(i)
        if not HEAD.match(cur[i].strip()):
            k += 1
        i += 1
    return out


def between(p, q):
    """The article paragraphs strictly between positions p < q (a row at an integer is that paragraph)."""
    return list(range(math.floor(p) + 1, math.ceil(q)))


def adjacent(p, q):
    """True when no article paragraph sits between positions p < q."""
    return p is not None and q is not None and q > p and not between(p, q)


def git(cwd, *args):
    return subprocess.run(['git', '-C', str(cwd)] + list(args), capture_output=True, text=True, check=True).stdout


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('map'); ap.add_argument('out')
    ap.add_argument('--article', required=True); ap.add_argument('--source', required=True)
    ap.add_argument('--since', default='HEAD')
    ap.add_argument('--against-source', action='store_true')
    ap.add_argument('--source-label', default='Original')
    ap.add_argument('--context', type=int, default=1, help='article paragraphs to show before and after each run of rows')
    a = ap.parse_args()
    m = json.loads(pathlib.Path(a.map).read_text(encoding='utf-8'))
    art = pathlib.Path(a.article).resolve()
    cur = paragraphs(art.read_text(encoding='utf-8'))
    src = pathlib.Path(a.source)
    raw = src.read_text(encoding='utf-8')
    sparas = paragraphs(html_text(raw) if src.suffix.lower() in ('.html', '.htm') else raw)
    if a.against_source:
        old, legend = None, ('Against the %s on the left: <span class="mark">highlighted</span> words are new, '
                             '<del>struck</del> words are the original\'s that were cut, and <span class="flag">red</span> '
                             'is a span Pangram flagged.' % html.escape(a.source_label.lower()))
    else:
        old = paragraphs(git(art.parent, 'show', '%s:./%s' % (a.since, art.name)))
        rev = git(art.parent, 'log', '-1', '--format=%h, %cd', '--date=format:%Y-%m-%d %H:%M UTC', a.since).strip()
        legend = ('Against the version you last saw (%s): <span class="mark">highlighted</span> words are new, '
                  '<del>struck</del> words are cut, and <span class="flag">red</span> is a span Pangram flagged.' % html.escape(rev))
    rows = {r.get('label', 'row'): r for blk in m['blocks'] for r in blk['rows']}
    if any(r.get('repeats') for r in rows.values()):
        legend += (' <span class="dup">Blue</span> is something the article, or another draft on this page, '
                   'already says; the note under it says where.')
    body = ['<p class="meta">%s</p>' % html.escape(m.get('meta', '')), '<p class="meta">%s</p>' % legend]
    body += ['<p class="intro">%s</p>' % html.escape(t) for t in m.get('intro', [])]
    pos = place_rows(m, cur)
    for bi, blk in enumerate(m['blocks']):
        body.append('<div class="block">')
        for h in blk.get('headings', []):
            n = min(len(h) - len(h.lstrip('#')), 3) or 2
            body.append('<h%d>%s</h%d>' % (n, html.escape(h.lstrip('#').strip()), n))
        body += ['<p class="intro">%s</p>' % html.escape(t) for t in blk.get('intro', [])]
        placed = [pos[(bi, ri)] for ri in range(len(blk['rows']))]
        first = next((q for q in placed if q is not None), None)
        if first is not None:
            path = section_path(cur, first)
            if path:
                body.append('<p class="where">Where it goes: %s</p>' % ' › '.join(html.escape(x) for x in path))
        seen_idx = {int(q) for q in placed if q is not None and q == int(q)}   # rows that are article paragraphs
        for ri, r in enumerate(blk['rows']):
            p = placed[ri]
            prev_p = placed[ri - 1] if ri > 0 else None
            if p is not None and not adjacent(prev_p, p):
                bi_ = [i for i in before_idxs(cur, p, a.context) if i not in seen_idx and (prev_p is None or i > prev_p)]
                if bi_:
                    seen_idx.update(bi_)
                    body.append(ctx_html(cur, bi_, 'Right before it in the article'))
            items = r.get('source', r.get('guide', []))
            dups = [(rp['span'], 'dup') for rp in r.get('repeats', [])]
            marks = list(dict.fromkeys(([(r['flag'], 'flag')] if r.get('flag') else []) + dups))  # a span listed twice is marked once
            if 'text' in r:
                text, links, state = re.sub(r'\s+', ' ', keep_lines(r['text'])), [], 'not in the article'
                base = None
                if r.get('proposal_of'):
                    base = plain(find(cur, r['proposal_of'], r.get('label', 'row')))[0]
                elif r.get('proposal_of_text'):
                    base = re.sub(r'\s+', ' ', keep_lines(r['proposal_of_text']))
                elif 'PROPOSAL' in r.get('label', '').upper():
                    base = best_match(text, cur)
                if r.get('flag') and not dups:
                    shown = flag_html(text, r['flag'])
                elif not r.get('flag') and base and base.translate(QUOTES) != text.translate(QUOTES):
                    shown = diff_html(base, text)
                    state = 'proposal, not in the article: highlighted words are what it adds to the paragraph that is'
                else:
                    shown = spans_html(text, marks)
            else:
                text, links = plain(find(cur, r['article'], r.get('label', 'row')))
                if a.against_source:
                    starts = [g for g in items if isinstance(g, str)]
                    prev = plain(find(sparas, starts[0], 'source'))[0] if starts else None
                    word = 'the original'
                else:
                    prev, word = best_match(text, old), 'then'
                if r.get('flag'):
                    shown, state = spans_html(text, marks), 'in the article'
                elif prev is None:
                    shown, state = spans_html(text, marks), 'new since %s' % word
                elif prev.translate(QUOTES) == text.translate(QUOTES):
                    shown, state = spans_html(text, marks), 'unchanged'
                else:
                    shown, state = diff_html(prev, text), 'changed from %s' % word
            shown = shown.replace(BR, '<br>')
            if text.startswith('https://') and ' ' not in text:
                shown = '<a href="%s">%s</a>' % (html.escape(text), html.escape(text))
            notes = ['<p class="meta">%s%s</p>' % (html.escape(state), (' · ' + html.escape(r['note'])) if r.get('note') else '')]
            if r.get('notes'):
                notes.append('<ul class="notes">%s</ul>' % ''.join('<li>%s</li>' % html.escape(n) for n in r['notes']))
            rep = repeat_notes(r, cur, rows)
            if rep:
                notes.append('<p class="meta">What already says it:</p><ul class="notes">%s</ul>'
                             % ''.join('<li>%s</li>' % html.escape(n) for n in rep))
            notes.append(carries_html(r, items, sparas, text))
            if links:
                notes.append('<p class="meta">Links: %s</p>' % ', '.join(
                    '%s → <a href="%s">%s</a>' % (html.escape(t.replace('*', '')), html.escape(u), html.escape(u)) for t, u in links))
            body.append('<div class="grid"><div class="card">%s</div><div class="card"><p class="lbl">%s</p><p>%s</p>%s</div></div>'
                        % (source_cell(items, sparas, a.source_label), html.escape(r.get('label', '')), shown, ''.join(notes)))
            next_p = placed[ri + 1] if ri + 1 < len(placed) else None
            if p is not None and not adjacent(p, next_p):
                ai_ = [i for i in after_idxs(cur, p, a.context) if i not in seen_idx and (next_p is None or next_p <= p or i < next_p)]
                if ai_:
                    seen_idx.update(ai_)
                    body.append(ctx_html(cur, ai_, 'Right after it in the article'))
        body.append('</div>')
    page = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>%s</title><style>%s</style></head><body><main><h1>%s</h1>%s</main></body></html>'
            % (html.escape(m['title']), CSS, html.escape(m['title']), '\n'.join(body)))
    pathlib.Path(a.out).write_text(page, encoding='utf-8')
    print('%s: %d rows -> %s' % (m['title'], sum(len(b['rows']) for b in m['blocks']), a.out))
    # E152 (Joel, 2026-10-07 23:18: "starting with C1, PGQ-002 (in) i was confused about what the context was for that"):
    # a row in the article shows its source too. Not an error, since some older rows have none; a reminder to look.
    bare = [r.get('label', 'row') for r in rows.values() if 'article' in r and not r.get('source', r.get('guide'))]
    if bare:
        print('note: %d article rows show no source: %s' % (len(bare), '; '.join(bare)), file=sys.stderr)


if __name__ == '__main__':
    main()
