#!/usr/bin/env python3
"""render_questions.py - turn OWNER-QUESTIONS.md into the published "Community Article Questions" page.

The Markdown file in Git is the master (UDA patterns/owner-questions-page.md, rule 2); this writes the view. Republish the
output to the same artifact every time the file changes (its URL is in STATUS.md and the handoff).

Usage: python3 tools/render_questions.py OWNER-QUESTIONS.md community-questions.html
"""
import html
import re
import sys

import markdown

sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parents[4] / 'tools' / 'humanization'))
from html_links import autolink_markdown  # noqa: E402  Joel, 2026-10-16: "your links are not clickable"

KINDS = {'🟣': ('q', 'Question for you'), '🟠': ('todo', 'For you to do'), '🔵': ('next', 'Next or in progress'),
         '🟢': ('done', 'Done or decided')}
CALLOUTS = {'IMPORTANT': 'q', 'WARNING': 'todo', 'TIP': 'done', 'NOTE': 'next'}

STYLE = '''<title>Community Article Questions</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:opsz,wght@7..72,500;7..72,650&family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Layout: one reading column; four status colours carry the meaning, everything else stays quiet. */
:root {
  --bg: #f5f7fa; --surface: #ffffff; --fg: #1b2130; --muted: #586174; --rule: #dbe0e8; --link: #2a5db0;
  --q: #6d43c9; --q-soft: #f1ebff; --todo: #b65a06; --todo-soft: #fff1e3; --next: #23649e; --next-soft: #e7f1fb;
  --done: #2b7a52; --done-soft: #e6f5ec;
  --display: "Literata", Georgia, "Times New Roman", serif;
  --body: "Atkinson Hyperlegible", "Segoe UI", system-ui, sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #12151b; --surface: #191d25; --fg: #e5e8ee; --muted: #9ba4b4; --rule: #2b313c; --link: #8db7f5;
  --q: #b8a1ff; --q-soft: #251d3d; --todo: #f3a95e; --todo-soft: #33230f; --next: #85b9ef; --next-soft: #15263a;
  --done: #79d3a0; --done-soft: #142b20; color-scheme: dark } }
:root[data-theme="dark"] {
  --bg: #12151b; --surface: #191d25; --fg: #e5e8ee; --muted: #9ba4b4; --rule: #2b313c; --link: #8db7f5;
  --q: #b8a1ff; --q-soft: #251d3d; --todo: #f3a95e; --todo-soft: #33230f; --next: #85b9ef; --next-soft: #15263a;
  --done: #79d3a0; --done-soft: #142b20; color-scheme: dark }
body { background: var(--bg); color: var(--fg); font-family: var(--body); font-size: 1rem; line-height: 1.6;
  padding-inline: 16px; padding-block: 28px 56px; }
main { max-width: 46rem; margin-inline: auto; display: grid; gap: 1.75rem; min-width: 0; }
h1 { font-family: var(--display); font-weight: 650; font-size: clamp(1.6rem, 4vw, 2.1rem); line-height: 1.2;
  margin: 0; text-wrap: balance; }
h2 { font-family: var(--display); font-weight: 500; font-size: 1.3rem; margin: 0 0 .5rem; text-wrap: balance;
  display: flex; align-items: center; gap: .6rem; }
section { display: grid; gap: .75rem; min-width: 0; }
.head { display: grid; gap: .6rem; }
.head p { margin: 0; }
.meta { color: var(--muted); }
.legend { display: flex; flex-wrap: wrap; gap: .5rem; margin: 0; padding: 0; list-style: none; }
.chip { display: inline-flex; align-items: center; gap: .4rem; font-size: .85rem; padding: .15rem .6rem;
  border-radius: 999px; border: 1px solid var(--rule); background: var(--surface); }
.dot { inline-size: .7rem; block-size: .7rem; border-radius: 50%; flex: none; display: inline-block;
  vertical-align: baseline; }
.dot.q { background: var(--q); } .dot.todo { background: var(--todo); } .dot.next { background: var(--next); }
.dot.done { background: var(--done); }
.callout { margin: 0; padding: .55rem .8rem; border-radius: 6px; font-weight: 700; font-size: .95rem; }
.callout.q { background: var(--q-soft); color: var(--q); } .callout.todo { background: var(--todo-soft); color: var(--todo); }
.callout.next { background: var(--next-soft); color: var(--next); } .callout.done { background: var(--done-soft); color: var(--done); }
section.open > p { margin: 0; }
section.open > p > strong:first-child { font-family: var(--display); font-weight: 650; font-size: 1.1rem; }
section.open ul { margin: 0; padding-inline-start: 1.3rem; }
section.open .q-block { background: var(--surface); border: 1px solid var(--rule); border-radius: 8px;
  padding: .9rem 1rem; display: grid; gap: .55rem; }
section.open .q-block p { margin: 0; }
ul.items { list-style: none; margin: 0; padding: 0; display: grid; gap: .55rem; }
ul.items > li { display: grid; grid-template-columns: .7rem 1fr; gap: .65rem; align-items: start; min-width: 0; }
ul.items > li > .dot { margin-top: .45rem; }
ul.items > li > div { min-width: 0; overflow-wrap: anywhere; }
.gap { block-size: .4rem; }
a { color: var(--link); text-underline-offset: 2px; }
a:focus-visible { outline: 2px solid var(--link); outline-offset: 2px; border-radius: 2px; }
code { font-family: var(--mono); font-size: .86em; background: var(--surface); border: 1px solid var(--rule);
  border-radius: 4px; padding: .05rem .3rem; overflow-wrap: anywhere; user-select: all; }
.small { font-size: .85rem; color: var(--muted); }
.q-block strong .dot { margin-right: .45rem; }
</style>
'''


def marker(m):
    kind, label = KINDS[m]
    return '<span class="dot %s" role="img" aria-label="%s"></span>' % (kind, label)


def render(md_text):
    lines = md_text.split('\n')
    title = lines[0].lstrip('# ').strip()
    body = '\n'.join(lines[1:])
    # callouts: "> [!KIND]\n> text" -> a coloured line
    def callout(m):
        return '\n<p class="callout %s">%s</p>\n' % (CALLOUTS[m.group(1)], html.escape(m.group(2).strip()))
    body = re.sub(r'(?m)^> \[!(IMPORTANT|WARNING|TIP|NOTE)\]\n> (.+)$', callout, body)
    # GitHub starts a list right after a paragraph line; python-markdown needs a blank line first
    body = re.sub(r'(?m)^((?!- )[^\n]+)\n(?=- )', r'\1\n\n', body)
    # a blank line between two bullets separates groups (days); keep it as a gap, not a loose list
    body = re.sub(r'(?m)^(- [^\n]*)\n\n(?=- )', r'\1\n- @@GAP@@\n', body)
    out = markdown.markdown(autolink_markdown(body), extensions=['sane_lists'])
    out = out.replace('<li>@@GAP@@</li>', '<li class="gap" aria-hidden="true"></li>')
    # legend paragraph
    def legend(m):
        chips = []
        for emoji, (kind, label) in KINDS.items():
            chips.append('<li class="chip"><span class="dot %s"></span>%s</li>' % (kind, label))
        return '<ul class="legend" aria-label="Colours">%s</ul>' % ''.join(chips)
    out = re.sub(r'<p>Colours:[^<]*</p>', legend, out)
    # sections
    parts = re.split(r'(<h2>.*?</h2>)', out)
    html_out = ['<header class="head"><h1>%s</h1>%s</header>' % (html.escape(title), parts[0])]
    for i in range(1, len(parts), 2):
        h, content = parts[i], parts[i + 1]
        name = re.sub('<.*?>', '', h)
        cls = 'open' if name.startswith('Open') else 'todo' if name.startswith('For you') else \
            'done' if name.startswith('Decided') else 'next'
        kind = {'open': 'q'}.get(cls, cls)
        h = h.replace('<h2>', '<h2><span class="dot %s"></span>' % kind, 1)
        if cls == 'open':
            # each question: its bold title paragraph plus the list and paragraphs up to the next question
            blocks = re.split(r'(?=<p><strong>🟣)', content)
            content = blocks[0] + ''.join('<div class="q-block">%s</div>' % b for b in blocks[1:])
        else:
            content = content.replace('<ul>', '<ul class="items">')
            content = re.sub(r'<li>([🟣🟠🔵🟢]) (.*?)</li>', lambda m: '<li>%s<div>%s</div></li>' % (marker(m.group(1)), m.group(2)),
                             content, flags=re.S)
        content = re.sub('[🟣🟠🔵🟢] ?', lambda m: marker(m.group(0).strip()), content)
        html_out.append('<section class="%s">%s%s</section>' % (cls, h, content))
    page = '\n'.join(html_out)
    page = page.replace('<p>The master copy of this page', '<p class="small">The master copy of this page')
    return STYLE + '<main>\n' + page + '\n</main>\n'


def main():
    src, dst = sys.argv[1], sys.argv[2]
    text = open(src, encoding='utf-8').read()
    open(dst, 'w', encoding='utf-8').write(render(text))
    print('%s: %d bytes' % (dst, len(open(dst, encoding='utf-8').read())))


if __name__ == '__main__':
    main()
