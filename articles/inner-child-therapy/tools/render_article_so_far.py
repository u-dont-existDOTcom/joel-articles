#!/usr/bin/env python3
"""render_article_so_far.py - render HUMANIZED-ARTICLE-SO-FAR.md as one HTML file for Joel.

Usage:
  python3 render_article_so_far.py [OUT.html]

OWNER-FACING-TURN-CONTRACT.md (active since 2026-09-17): every owner-facing turn ends
with the full humanized article so far. Run this at the end of every turn and send the
file. A comment that starts with "<!-- CANDIDATE:" becomes a visible note, so a candidate
section is never shown as accepted prose. All other comments stay invisible.
"""
import html, pathlib, re, sys
import markdown

SRC = pathlib.Path(__file__).resolve().parent.parent / 'HUMANIZED-ARTICLE-SO-FAR.md'
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else
                   '/mnt/user-data/outputs/inner-child-therapy-humanized-so-far.html')

md = SRC.read_text(encoding='utf-8')
md = re.sub(r'<!--\s*CANDIDATE:(.*?)-->',
            lambda m: '\n\n<div class="candidate">' + html.escape(m.group(1).strip()) + '</div>\n\n',
            md, flags=re.S)
body = markdown.markdown(md)
page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Inner Child Therapy, humanized so far</title>
<style>
body {{ max-width: 42rem; margin: 2rem auto; padding: 0 1rem; font: 17px/1.6 Georgia, serif; color: #222; background: #fff; }}
h1, h2, h3 {{ font-family: system-ui, sans-serif; line-height: 1.25; }}
blockquote {{ color: #555; border-left: 3px solid #ccc; margin-left: 0; padding-left: 1rem; font-size: 0.9em; }}
.candidate {{ font-family: system-ui, sans-serif; font-size: 0.85em; background: #fff6e0; border: 1px solid #e0b84c; border-radius: 6px; padding: 0.6rem 0.8rem; margin: 2rem 0 0.5rem; }}
a {{ color: #0b5cad; }}
</style></head><body>
{body}
</body></html>
"""
OUT.write_text(page, encoding='utf-8')
print(OUT, len(page), 'bytes')
