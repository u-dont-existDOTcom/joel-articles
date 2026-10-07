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
Rows taken from ARTICLE must sit under the heading they have in ARTICLE, in ARTICLE's order: a block's last heading
is the one its rows are shown under, and the page isn't written when a row would show elsewhere (2026-10-07: the page
showed section 8's P7 a section early, and Joel asked why it had been moved). --no-heading-check turns this off.
"source" lists starts of source paragraphs, or {"quote": ..., "from": ...} for part of one;
[] for none. The lane's older key "guide" is read the same way. "note" is one line; "notes"
is a list shown as bullets.
"""
import argparse, difflib, html, json, pathlib, re, subprocess, sys

QUOTES = str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"'})
LINK = re.compile(r'\[([^\]]*)\]\(([^)]*)\)')
LIST_LINE = re.compile(r'^(\d+\.|[-*+]) ', re.M)
BR = '\u00b6'  # a line break inside a paragraph with a list; a word of its own, so diffs keep it

CSS = """
:root{--bg:#fbfaf7;--fg:#1f1d1a;--mute:#6b665e;--line:#e3ded4;--card:#fff;--mark:rgba(240,190,60,.35);--flag:rgba(255,86,48,.16);--link:#2f5fa7}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#171614;--fg:#ece8e1;--mute:#a39d93;--line:#34312c;--card:#201e1b;--mark:rgba(240,190,60,.28);--flag:rgba(255,86,48,.25);--link:#8fb4ee}}
:root[data-theme=dark]{--bg:#171614;--fg:#ece8e1;--mute:#a39d93;--line:#34312c;--card:#201e1b;--mark:rgba(240,190,60,.28);--flag:rgba(255,86,48,.25);--link:#8fb4ee}
body{background:var(--bg);color:var(--fg);font:17px/1.6 Georgia,serif;margin:0;padding:24px 16px}
main{max-width:1100px;margin:0 auto} h1,h2,h3{font-family:system-ui,sans-serif;line-height:1.25}
a{color:var(--link)}
.meta{font:14px/1.5 system-ui,sans-serif;color:var(--mute)}
.intro{font:15px/1.55 system-ui,sans-serif;max-width:760px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:14px 0} @media(max-width:760px){.grid{grid-template-columns:1fr}}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 18px;overflow-wrap:anywhere}
.lbl{font:600 13px/1.3 system-ui,sans-serif;text-transform:uppercase;letter-spacing:.04em;color:var(--mute)}
.mark{background:var(--mark);border-radius:3px;padding:0 2px} .flag{background:var(--flag);border-radius:3px;padding:0 2px}
del{color:var(--mute);text-decoration-thickness:1px}
.notes{font:15px/1.5 system-ui,sans-serif;margin:8px 0 0;padding-left:20px} .notes li{margin:4px 0}
.block{margin-top:28px}
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


def norm_heading(h):
    return re.sub(r'\s+', ' ', h.lstrip('#').strip()).translate(QUOTES).lower()


def heading_check(m, cur):
    """Rows that show an ARTICLE paragraph under a heading other than its own, or out of the article's order.

    Joel, 2026-10-07 15:05, on community section 8: "P7 is in the wrong section. You moved it from "the mother is
    primary" to the prior section? why?" The article had P7 under its heading; the page map had put P2 to P7 in one
    block and P8 to P11 in the next, so the page showed P7 a section early. The page is how he reviews the article, so
    it must group rows the way the article does."""
    heads, h = [], None
    for p in cur:
        if p.startswith('#'):
            h = norm_heading(p)
        heads.append(h)
    page_h, last, wrong = None, -1, []
    for blk in m['blocks']:
        if blk.get('headings'):
            page_h = norm_heading(blk['headings'][-1])
        for r in blk['rows']:
            if 'article' not in r:
                continue
            i = cur.index(find(cur, r['article'], r.get('label', 'row')))
            if heads[i] != page_h:
                wrong.append('%s is under "%s" in the article but under "%s" on the page'
                             % (r.get('label', 'row'), heads[i], page_h))
            if i < last:
                wrong.append('%s comes before the row above it in the article' % r.get('label', 'row'))
            last = max(last, i)
    return wrong


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


def source_cell(items, sparas, label):
    if not items:
        return '<p class="lbl">No %s</p>' % html.escape(label.lower())
    out, prev = [], None
    for g in items:
        if isinstance(g, dict):
            src = ' · ' + html.escape(g['from']) if g.get('from') else ''
            out.append('<p class="lbl">%s%s</p><p>%s</p>' % (html.escape(label), src, html.escape(g['quote'])))
        else:
            # Whole source paragraphs in a row (a lead-in and its list items) share one label.
            lbl = '' if isinstance(prev, str) else '<p class="lbl">%s</p>' % html.escape(label)
            out.append('%s<p>%s</p>' % (lbl, html.escape(plain(find(sparas, g, 'source'))[0])))
        prev = g
    return ''.join(out)


def git(cwd, *args):
    return subprocess.run(['git', '-C', str(cwd)] + list(args), capture_output=True, text=True, check=True).stdout


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('map'); ap.add_argument('out')
    ap.add_argument('--article', required=True); ap.add_argument('--source', required=True)
    ap.add_argument('--since', default='HEAD')
    ap.add_argument('--against-source', action='store_true')
    ap.add_argument('--source-label', default='Original')
    ap.add_argument('--no-heading-check', action='store_true',
                    help="don't stop when a row sits under another heading than the article's (an old map that groups on purpose)")
    a = ap.parse_args()
    m = json.loads(pathlib.Path(a.map).read_text(encoding='utf-8'))
    art = pathlib.Path(a.article).resolve()
    cur = paragraphs(art.read_text(encoding='utf-8'))
    wrong = [] if a.no_heading_check else heading_check(m, cur)
    if wrong:
        sys.exit('the page would group rows differently from the article:\n  ' + '\n  '.join(wrong))
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
    body = ['<p class="meta">%s</p>' % html.escape(m.get('meta', '')), '<p class="meta">%s</p>' % legend]
    body += ['<p class="intro">%s</p>' % html.escape(t) for t in m.get('intro', [])]
    for blk in m['blocks']:
        body.append('<div class="block">')
        for h in blk.get('headings', []):
            n = min(len(h) - len(h.lstrip('#')), 3) or 2
            body.append('<h%d>%s</h%d>' % (n, html.escape(h.lstrip('#').strip()), n))
        for r in blk['rows']:
            items = r.get('source', r.get('guide', []))
            if 'text' in r:
                text, links, state = re.sub(r'\s+', ' ', keep_lines(r['text'])), [], 'not in the article'
                base = None
                if r.get('proposal_of'):
                    base = plain(find(cur, r['proposal_of'], r.get('label', 'row')))[0]
                elif r.get('proposal_of_text'):
                    base = re.sub(r'\s+', ' ', keep_lines(r['proposal_of_text']))
                elif 'PROPOSAL' in r.get('label', '').upper():
                    base = best_match(text, cur)
                if r.get('flag'):
                    shown = flag_html(text, r['flag'])
                elif base and base.translate(QUOTES) != text.translate(QUOTES):
                    shown = diff_html(base, text)
                    state = 'proposal, not in the article: highlighted words are what it adds to the paragraph that is'
                else:
                    shown = html.escape(text)
            else:
                text, links = plain(find(cur, r['article'], r.get('label', 'row')))
                if a.against_source:
                    starts = [g for g in items if isinstance(g, str)]
                    prev = plain(find(sparas, starts[0], 'source'))[0] if starts else None
                    word = 'the original'
                else:
                    prev, word = best_match(text, old), 'then'
                if r.get('flag'):
                    shown, state = flag_html(text, r['flag']), 'in the article'
                elif prev is None:
                    shown, state = html.escape(text), 'new since %s' % word
                elif prev.translate(QUOTES) == text.translate(QUOTES):
                    shown, state = html.escape(text), 'unchanged'
                else:
                    shown, state = diff_html(prev, text), 'changed from %s' % word
            shown = shown.replace(BR, '<br>')
            if text.startswith('https://') and ' ' not in text:
                shown = '<a href="%s">%s</a>' % (html.escape(text), html.escape(text))
            notes = ['<p class="meta">%s%s</p>' % (html.escape(state), (' · ' + html.escape(r['note'])) if r.get('note') else '')]
            if r.get('notes'):
                notes.append('<ul class="notes">%s</ul>' % ''.join('<li>%s</li>' % html.escape(n) for n in r['notes']))
            if links:
                notes.append('<p class="meta">Links: %s</p>' % ', '.join(
                    '%s → <a href="%s">%s</a>' % (html.escape(t.replace('*', '')), html.escape(u), html.escape(u)) for t, u in links))
            body.append('<div class="grid"><div class="card">%s</div><div class="card"><p class="lbl">%s</p><p>%s</p>%s</div></div>'
                        % (source_cell(items, sparas, a.source_label), html.escape(r.get('label', '')), shown, ''.join(notes)))
        body.append('</div>')
    page = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>%s</title><style>%s</style></head><body><main><h1>%s</h1>%s</main></body></html>'
            % (html.escape(m['title']), CSS, html.escape(m['title']), '\n'.join(body)))
    pathlib.Path(a.out).write_text(page, encoding='utf-8')
    print('%s: %d rows -> %s' % (m['title'], sum(len(b['rows']) for b in m['blocks']), a.out))


if __name__ == '__main__':
    main()
