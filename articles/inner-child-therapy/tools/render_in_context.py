#!/usr/bin/env python3
"""render_in_context.py - a section's paragraphs next to the guide's originals, with changes marked.

Usage:
  python3 render_in_context.py MAP.json OUT.html [--since REV]

Joel, 2026-09-30 03:29 UTC, on the page Claude had been making by hand each turn: "I like how
you are doing this original vs new diff, that's good make that durable". It carries his standing
rule from 2026-09-28: show humanization work in context, where the section sits in the article,
with the guide's original next to each draft. Run it at the end of every turn, next to
render_article_so_far.py, and send both pages.

The page is built from the article (HUMANIZED-ARTICLE-SO-FAR.md), the guide (master.html) and a
small map for the turn in tools/in-context/. Only the labels and notes in the map are typed by
hand. Paragraph text comes from the article and the guide, so the page can't show a version that
isn't the one installed.

--since REV is the git revision Joel last saw (default HEAD, so run it before committing the
turn). Against it, words added are highlighted and words cut are struck through, and a paragraph
with no match there is marked new.

MAP.json:
{
 "title": "Not Every Hero Wears A Cape",
 "meta": "Inner Child Therapy · 2026-09-30, turn 5",
 "blocks": [
  {"headings": ["# Building Trust With Your Little One", "## Not Every Hero Wears A Cape"],
   "rows": [
    {"label": "P1 · Joel's", "article": "Set one boundary.",
     "guide": ["Set one boundary. Say no"], "note": "..."},
    {"label": "P5 · candidate", "text": "...", "flag": "the span Pangram flagged",
     "guide": [{"quote": "Afterward, review...", "from": "guide paragraph 4, second half"}], "note": "..."}
   ]}
 ]
}
"article" is the start of a paragraph in the article; "text" is a candidate that isn't installed.
"guide" lists starts of guide paragraphs, or {"quote": ..., "from": ...} for part of one; [] for none.
"""
import argparse, difflib, html, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
ARTICLE = HERE.parent / 'HUMANIZED-ARTICLE-SO-FAR.md'
sys.path.insert(0, str(HERE / 'reviewer'))
import reviewer  # noqa: E402  (guide_text reads master.html)

QUOTES = str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"'})
LINK = re.compile(r'\[([^\]]*)\]\(([^)]*)\)')

CSS = """
:root{--bg:#fbfaf7;--fg:#1f1d1a;--mute:#6b665e;--line:#e3ded4;--card:#fff;--mark:rgba(240,190,60,.35);--flag:rgba(255,86,48,.16);--link:#2f5fa7}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#171614;--fg:#ece8e1;--mute:#a39d93;--line:#34312c;--card:#201e1b;--mark:rgba(240,190,60,.28);--flag:rgba(255,86,48,.25);--link:#8fb4ee}}
:root[data-theme=dark]{--bg:#171614;--fg:#ece8e1;--mute:#a39d93;--line:#34312c;--card:#201e1b;--mark:rgba(240,190,60,.28);--flag:rgba(255,86,48,.25);--link:#8fb4ee}
body{background:var(--bg);color:var(--fg);font:17px/1.6 Georgia,serif;margin:0;padding:24px 16px}
main{max-width:1100px;margin:0 auto} h1,h2,h3{font-family:system-ui,sans-serif;line-height:1.25}
a{color:var(--link)}
.meta{font:14px/1.5 system-ui,sans-serif;color:var(--mute)}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:14px 0} @media(max-width:760px){.grid{grid-template-columns:1fr}}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 18px;overflow-wrap:anywhere}
.lbl{font:600 13px/1.3 system-ui,sans-serif;text-transform:uppercase;letter-spacing:.04em;color:var(--mute)}
.mark{background:var(--mark);border-radius:3px;padding:0 2px} .flag{background:var(--flag);border-radius:3px;padding:0 2px}
del{color:var(--mute);text-decoration-thickness:1px}
.block{margin-top:28px}
"""


def paragraphs(md):
    md = re.sub(r'<!--.*?-->', '', md, flags=re.S)
    return [p.strip() for p in re.split(r'\n\s*\n', md) if p.strip()]


def plain(p):
    """A paragraph's visible text (no link targets or emphasis marks) and its links."""
    links = LINK.findall(p)
    t = LINK.sub(r'\1', p).replace('*', '')
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


def guide_cell(items, gparas):
    if not items:
        return '<p class="lbl">No guide original</p>'
    out = []
    for g in items:
        if isinstance(g, dict):
            src = ' · ' + html.escape(g['from']) if g.get('from') else ''
            out.append('<p class="lbl">Guide original%s</p><p>%s</p>' % (src, html.escape(g['quote'])))
        else:
            out.append('<p class="lbl">Guide original</p><p>%s</p>' % html.escape(plain(find(gparas, g, 'guide'))[0]))
    return ''.join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('map'); ap.add_argument('out'); ap.add_argument('--since', default='HEAD')
    a = ap.parse_args()
    m = json.loads(pathlib.Path(a.map).read_text(encoding='utf-8'))
    cur = paragraphs(ARTICLE.read_text(encoding='utf-8'))
    old_md = subprocess.run(['git', '-C', str(ARTICLE.parent), 'show', '%s:./%s' % (a.since, ARTICLE.name)],
                            capture_output=True, text=True, check=True).stdout
    old = paragraphs(old_md)
    rev = subprocess.run(['git', '-C', str(ARTICLE.parent), 'log', '-1', '--format=%h, %cd', '--date=format:%Y-%m-%d %H:%M UTC', a.since],
                         capture_output=True, text=True, check=True).stdout.strip()
    gparas = paragraphs(reviewer.guide_text())
    body = ['<p class="meta">%s</p>' % html.escape(m.get('meta', '')),
            '<p class="meta">Against the version you last saw (%s): <span class="mark">highlighted</span> words are new, '
            '<del>struck</del> words are cut, and <span class="flag">red</span> is a span Pangram flagged.</p>' % html.escape(rev)]
    for blk in m['blocks']:
        body.append('<div class="block">')
        for h in blk.get('headings', []):
            n = min(len(h) - len(h.lstrip('#')), 3) or 2
            body.append('<h%d>%s</h%d>' % (n, html.escape(h.lstrip('#').strip()), n))
        for r in blk['rows']:
            if 'text' in r:
                text, links, state = r['text'], [], 'not in the article'
                shown = flag_html(text, r['flag']) if r.get('flag') else html.escape(text)
            else:
                text, links = plain(find(cur, r['article'], r.get('label', 'row')))
                prev = best_match(text, old)
                if r.get('flag'):
                    shown, state = flag_html(text, r['flag']), 'in the article'
                elif prev is None:
                    shown, state = html.escape(text), 'new since then'
                elif prev == text:
                    shown, state = html.escape(text), 'unchanged'
                else:
                    shown, state = diff_html(prev, text), 'changed'
            if text.startswith('https://') and ' ' not in text:
                shown = '<a href="%s">%s</a>' % (html.escape(text), html.escape(text))
            notes = ['<p class="meta">%s%s</p>' % (html.escape(state), (' · ' + html.escape(r['note'])) if r.get('note') else '')]
            if links:
                notes.append('<p class="meta">Links: %s</p>' % ', '.join(
                    '%s → <a href="%s">%s</a>' % (html.escape(t), html.escape(u), html.escape(u)) for t, u in links))
            body.append('<div class="grid"><div class="card">%s</div><div class="card"><p class="lbl">%s</p><p>%s</p>%s</div></div>'
                        % (guide_cell(r.get('guide', []), gparas), html.escape(r.get('label', '')), shown, ''.join(notes)))
        body.append('</div>')
    page = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>%s</title><style>%s</style></head><body><main><h1>%s</h1>%s</main></body></html>'
            % (html.escape(m['title']), CSS, html.escape(m['title']), '\n'.join(body)))
    pathlib.Path(a.out).write_text(page, encoding='utf-8')
    print('%s: %d rows -> %s' % (m['title'], sum(len(b['rows']) for b in m['blocks']), a.out))


if __name__ == '__main__':
    main()
