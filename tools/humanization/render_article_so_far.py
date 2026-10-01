#!/usr/bin/env python3
"""render_article_so_far.py - render an article's humanized Markdown as one HTML file for Joel.

Usage (from the repo root):
  python3 tools/humanization/render_article_so_far.py [OUT.html] --article ARTICLE.md
          [--ledger OWNER-EDITS.json] [--title TEXT]

  --article  the humanized article so far (Markdown)
  --ledger   that article's OWNER-EDITS.json; without it, no owner-edits check and no box
  --title    the page title; default: the article's folder name, title-cased, plus
             ", humanized so far" ("inner-child-therapy" -> "Inner Child Therapy, humanized so far")
  OUT.html   default: /mnt/user-data/outputs/<the article's folder>-humanized-so-far.html
For example, Inner Child:
  python3 tools/humanization/render_article_so_far.py OUT.html \\
      --article articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md \\
      --ledger articles/inner-child-therapy/OWNER-EDITS.json

OWNER-FACING-TURN-CONTRACT.md (active since 2026-09-17): every owner-facing turn ends
with the full humanized article so far. Run this at the end of every turn and send the
file. A comment that starts with "<!-- CANDIDATE:" becomes a visible note, so a candidate
section is never shown as accepted prose. All other comments stay invisible.

With --ledger it also runs check_owner_edits.py against that ledger (Joel, 2026-09-27 21:18:
"so how can we prevent that kind of error in future where you say you will write something
and don't write it?"). An edit or claim a record says is in the article but isn't goes in a
red box at the top, and the script exits 1. Owner edits still waiting are listed in a short
box under it, so nothing he asked for sits unseen in a draft file.
"""
import argparse, html, json, pathlib, re, sys
import markdown
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import check_owner_edits

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('out', nargs='?', help='the HTML file to write')
ap.add_argument('--article', required=True, help='the humanized article so far (Markdown)')
ap.add_argument('--ledger', help="the article's OWNER-EDITS.json (no ledger: no owner-edits check)")
ap.add_argument('--title', help='the page title')
a = ap.parse_args()
SRC = pathlib.Path(a.article)
FOLDER = SRC.resolve().parent.name
OUT = pathlib.Path(a.out or '/mnt/user-data/outputs/%s-humanized-so-far.html' % FOLDER)
TITLE = a.title or '%s, humanized so far' % FOLDER.replace('-', ' ').title()

md = SRC.read_text(encoding='utf-8')
md = re.sub(r'<!--\s*CANDIDATE:(.*?)-->',
            lambda m: '\n\n<div class="candidate">' + html.escape(m.group(1).strip()) + '</div>\n\n',
            md, flags=re.S)
body = markdown.markdown(md)
chk = check_owner_edits.run(SRC, a.ledger) if a.ledger else None
top = ''
if chk and chk['failed']:
    items = ''.join('<li><b>%s</b>: %s<ul>%s</ul></li>' % (html.escape(f['id']), html.escape(f['what']),
                    ''.join('<li>%s</li>' % html.escape(x) for x in f['fails'])) for f in chk['failed'])
    top += '<div class="notin"><b>A record says this is in the article, and it isn\'t:</b><ul>%s</ul></div>' % items
ledger = {e['id']: e for e in json.loads(pathlib.Path(a.ledger).read_text(encoding='utf-8'))['entries']} if chk else {}
waiting = [w for w in chk['waiting'] if ledger.get(w['id'], {}).get('joel')] if chk else []
if waiting:
    items = ''.join('<li>%s <i>(waits for %s)</i></li>' % (html.escape(w['what']), html.escape(w['waits_for'])) for w in waiting)
    top += '<div class="waiting"><b>Your edits not in the article yet:</b><ul>%s</ul></div>' % items
body = top + body
page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>
body {{ max-width: 42rem; margin: 2rem auto; padding: 0 1rem; font: 17px/1.6 Georgia, serif; color: #222; background: #fff; }}
h1, h2, h3 {{ font-family: system-ui, sans-serif; line-height: 1.25; }}
blockquote {{ color: #555; border-left: 3px solid #ccc; margin-left: 0; padding-left: 1rem; font-size: 0.9em; }}
.candidate {{ font-family: system-ui, sans-serif; font-size: 0.85em; background: #fff6e0; border: 1px solid #e0b84c; border-radius: 6px; padding: 0.6rem 0.8rem; margin: 2rem 0 0.5rem; }}
a {{ color: #0b5cad; }}
.notin {{ font-family: system-ui, sans-serif; font-size: 0.85em; background: #fde8e8; border: 2px solid #c0392b; border-radius: 6px; padding: 0.6rem 0.8rem; margin: 1rem 0; }}
.waiting {{ font-family: system-ui, sans-serif; font-size: 0.85em; background: #f3f6fa; border: 1px solid #9fb3c8; border-radius: 6px; padding: 0.6rem 0.8rem; margin: 1rem 0; }}
</style></head><body>
{body}
</body></html>
"""
OUT.write_text(page, encoding='utf-8')
print(OUT, len(page), 'bytes')
if chk is None:
    print('owner edits: not checked (no --ledger)')
    sys.exit(0)
print('owner edits: %d pass, %d failed, %d waiting' % (chk['passed'], len(chk['failed']), len(chk['waiting'])))
for f in chk['failed']:
    print('NOT IN THE ARTICLE: %s: %s' % (f['id'], '; '.join(f['fails'])))
sys.exit(1 if chk['failed'] else 0)
