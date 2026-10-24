#!/usr/bin/env python3
"""The questions page as a page Joel can open on any device (turn 94, 2026-10-22).

Joel, 2026-10-22 19:50 UTC: "you didn't give me an answers page. isn't that a standing rule to always give answers page ..?"
The rule (UDA patterns/owner-questions-page.md, rule 2): OWNER-QUESTIONS.md is the master copy, and where the surface can
publish a page, the file is also published as one: on Claude, an artifact. The page is a view, so update the file first,
then rebuild and republish:
  python3 articles/inner-child-therapy/tools/questions_page.py OUT.html
and publish OUT.html to the same artifact (its link is at the top of OWNER-QUESTIONS.md). Open questions and the to-do list
are shown in full; each Decided entry is folded under its heading.
"""
import html
import pathlib
import re
import sys


HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent / 'OWNER-QUESTIONS.md'

STYLE = """
<title>Inner Child Owner Questions</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Newsreader:opsz,wght@6..72,500;6..72,600&family=JetBrains+Mono:wght@400&display=swap">
<style>
/* Layout: one reading column; open questions first, then the to-do list, then the folded record of decisions. */
:root {
  --bg: #f4f6f5; --surface: #ffffff; --ink: #1d2629; --muted: #56656a; --rule: #d9e0de;
  --ask: #6a4c9c; --todo: #a8601a; --next: #2c6a9e; --done: #2f7a52; --code-bg: #e9eeec;
  --display: "Newsreader", Georgia, "Times New Roman", serif;
  --body: "Atkinson Hyperlegible", "Segoe UI", system-ui, sans-serif;
  --mono: "JetBrains Mono", ui-monospace, Menlo, Consolas, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #121618; --surface: #1a2023; --ink: #e4e9e7; --muted: #9aa8ac; --rule: #2c3538;
  --ask: #b39ae0; --todo: #e2a35f; --next: #7fb3e0; --done: #7ccaa0; --code-bg: #232b2e; color-scheme: dark } }
:root[data-theme="dark"] {
  --bg: #121618; --surface: #1a2023; --ink: #e4e9e7; --muted: #9aa8ac; --rule: #2c3538;
  --ask: #b39ae0; --todo: #e2a35f; --next: #7fb3e0; --done: #7ccaa0; --code-bg: #232b2e; color-scheme: dark }
body { background: var(--bg); color: var(--ink); font-family: var(--body); font-size: 17px; line-height: 1.6; }
.wrap { max-width: 46rem; margin: 0 auto; padding-block: 2rem 4rem;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
h1, h2, h3 { font-family: var(--display); line-height: 1.25; text-wrap: balance; }
h1 { font-size: 2.1rem; margin: 0 0 .4rem; font-weight: 600; }
h2 { font-size: 1.45rem; margin: 2.6rem 0 .8rem; padding-top: 1rem; border-top: 1px solid var(--rule); font-weight: 600; }
h3 { font-size: 1.15rem; margin: 1.8rem 0 .5rem; font-weight: 600; }
p, li { max-width: 65ch; }
a { color: var(--next); text-underline-offset: 2px; }
a:focus-visible, summary:focus-visible { outline: 2px solid var(--next); outline-offset: 2px; border-radius: 3px; }
code { font-family: var(--mono); font-size: .82em; background: var(--code-bg); padding: .08em .35em; border-radius: 4px;
  overflow-wrap: anywhere; }
ul { padding-left: 1.3rem; } li { margin: .25rem 0; } li > ul { margin: .2rem 0 .4rem; }
.lead { color: var(--muted); margin: 0 0 1rem; }
.links { display: flex; flex-wrap: wrap; gap: .4rem 1.2rem; margin: .6rem 0 0; font-size: .95rem; }
.q { background: var(--surface); border: 1px solid var(--rule); border-left: 4px solid var(--ask); border-radius: 6px;
  padding: .2rem 1.1rem .8rem; margin: 1.1rem 0; }
.q.todo { border-left-color: var(--todo); } .q.next { border-left-color: var(--next); }
.q h3 { margin-top: .9rem; }
blockquote { margin: .8rem 0; padding: .5rem 1rem; border-left: 3px solid var(--rule); color: var(--muted); }
blockquote.callout-important { border-left-color: var(--ask); } blockquote.callout-warning { border-left-color: var(--todo); }
blockquote.callout-tip { border-left-color: var(--done); } blockquote.callout-note { border-left-color: var(--next); }
blockquote p { margin: .3rem 0; }
.kind { font-family: var(--body); font-size: .72rem; letter-spacing: .08em; text-transform: uppercase; color: var(--muted);
  margin-left: .4rem; font-weight: 700; }
details { border-bottom: 1px solid var(--rule); padding: .35rem 0; }
details > summary { cursor: pointer; font-family: var(--display); font-size: 1.05rem; font-weight: 600; padding: .3rem 0;
  list-style-position: outside; margin-left: 1.1rem; }
details[open] > summary { margin-bottom: .4rem; }
details > div { padding: 0 0 .6rem 1.1rem; }
.foot { margin-top: 3rem; color: var(--muted); font-size: .9rem; }
@media (prefers-reduced-motion: no-preference) { details > div { animation: none; } }
</style>
"""


# E214 (Joel, 2026-10-22 23:54 UTC: "can you please always give me the links to the checks you want me to copy and fix? i
# thought that was a rule already."): an open question that says a stretch reads AI links the check that shows it, a
# pangram.com result page (feed or history) or, for an API check, its results or checks page on GitHub.
AI_READING = re.compile(r'\b(?:still|reads?) AI\b|\bread (?:as )?AI\b|\bread (?:High|Medium|Low)\b|\bAI windows?\b', re.I)
CHECK_LINK = re.compile(r'pangram\.com/(?:feed|history)/|github\.com/\S*(?:results|RESULTS|checks|CHECKS)\S*')


def unlinked_ai_asks(md):
    """The headings of open questions that say a stretch reads AI but link no check (E214)."""
    md = re.sub(r'<!--.*?-->', '', md, flags=re.S)
    m = re.search(r'^## Open questions\n(.*?)(?=^## |\Z)', md, flags=re.S | re.M)
    if not m:
        return []
    return [b.split('\n', 1)[0] for b in re.split(r'(?=^### )', m.group(1), flags=re.M)
            if b.startswith('### ') and AI_READING.search(b) and not CHECK_LINK.search(b)]


def unpaneled_help_asks(md):
    """The open questions' items that ask Joel's help with tells but link no tell panel record (E253 (Inner Child))."""
    sys.path.insert(0, str(HERE.parents[2] / 'tools' / 'humanization'))
    from pangram_links_check import unpaneled_help
    md = re.sub(r'<!--.*?-->', '', md, flags=re.S)
    m = re.search(r'^## Open questions\n(.*?)(?=^## |\Z)', md, flags=re.S | re.M)
    return [u[:120] for u in unpaneled_help(m.group(1))] if m else []


# E257 (Inner Child; Joel, 2026-10-24 22:55 UTC: "can you durably fix the owner questions page so that you don't say things
# like "your 100.6, still open" bc i hope you know i have no idea at this point what my 100.6 was."): an open question or a
# to-do item says what an earlier question was, never just its number. A decided question's number is any number at the
# start of a question heading on the page ("### 🟢 96 to 99, ...", "### 🟢 78.2, 84 and 85, ...", "#### 101. ..."); the
# open ones ("### 🟣 102. ...") may name their own items. Quotes, link addresses and code are left out of the search.
HEAD_NUMS = re.compile(r'^#{3,4}\s+(?:\S+\s+)?(?:Questions?\s+)?(\d{1,3}(?:\.\d+)?(?:(?:,\s*|\s+and\s+|\s+to\s+)\d{1,3}(?:\.\d+)?)*)(?=[.,\s])', re.M)
DOTTED_REF = re.compile(r'(?<![\w.#/-])(\d{2,3})\.\d{1,2}(?![\d.%\w])')
WORD_REF = re.compile(r'\b(?:questions?|your|my|item)\s+(\d{2,3})(?:\.\d{1,2})?\b(?![%\d])', re.I)


def question_numbers(md):
    """(every question number a heading on the page starts with, the open questions' numbers)."""
    seen, opened = set(), set()
    for m in HEAD_NUMS.finditer(md):
        nums = [int(float(x.split('.')[0])) for x in re.findall(r'\d{1,3}(?:\.\d+)?', m.group(1))]
        if ' to ' in m.group(1) and len(nums) >= 2:
            nums += list(range(nums[0], nums[-1] + 1))
        seen.update(nums)
        if '🟣' in m.group(0):
            opened.update(nums)
    return seen, opened


def old_number_refs(md):
    """Places in the open questions and the to-do list that point to a decided question by its number alone (E257)."""
    md = re.sub(r'<!--.*?-->', '', md, flags=re.S)
    seen, opened = question_numbers(md)
    # every number from the page's first question to the newest open one, other than the open ones (a gap, like an item
    # that was answered inside a combined heading, is old too)
    old = set(range(min(seen), max(opened | seen) + 1)) - opened if seen else set()
    bad = []
    for name in ('Open questions', 'For you to do'):
        m = re.search(r'^## %s[^\n]*\n(.*?)(?=^## |\Z)' % re.escape(name), md, flags=re.S | re.M)
        if not m:
            continue
        body = re.sub(r'<details>.*?</details>', ' ', m.group(1), flags=re.S)
        body = re.sub(r'\]\([^)\s]*(?:\([^)\s]*\)[^)\s]*)*\)', ']', body)              # link addresses
        body = re.sub(r'`[^`]*`', ' ', body)                                            # code
        body = re.sub(r'"[^"\n]*"|“[^”\n]*”', ' ', body)                              # quotes
        for line in body.split('\n'):
            if re.match(r'^#{3,4}\s', line):
                line = re.sub(r'^#{3,4}\s+\S+\s+\d{1,3}\.', '', line)                 # a heading's own number
            for rx in (DOTTED_REF, WORD_REF):
                for r in rx.finditer(line):
                    if int(r.group(1)) in old:
                        bad.append(line.strip()[:140])
                        break
    return sorted(set(bad), key=bad.index)


def render(md):
    import mistune  # only the page needs it; the E214 check runs without it
    md = re.sub(r'<!--.*?-->', '', md, flags=re.S)
    lines = md.split('\n')
    title = lines[0].lstrip('# ').strip()
    body = '\n'.join(lines[1:])
    out = mistune.create_markdown(plugins=['table', 'strikethrough'], escape=True)(body)
    out = re.sub(r'<blockquote>\s*<p>\[!(\w+)\]\s*', lambda m: '<blockquote class="callout callout-%s"><p>' % m.group(1).lower(), out)
    # cut into h2 sections
    parts = re.split(r'(?=<h2>)', out)
    head, sections = parts[0], parts[1:]
    html_out = ['<div class="wrap">', '<h1>%s</h1>' % html.escape(title)]
    html_out.append(head.replace('<p>', '<p class="lead">', 2))
    html_out.append(LINKS)
    for sec in sections:
        name = re.match(r'<h2>(.*?)</h2>', sec).group(1)
        rest = sec[len(re.match(r'<h2>.*?</h2>', sec).group(0)):]
        blocks = re.split(r'(?=<h3>)', rest)
        html_out.append('<h2>%s</h2>' % name)
        html_out.append(blocks[0])
        for b in blocks[1:]:
            h = re.match(r'<h3>(.*?)</h3>', b, flags=re.S).group(1)
            inner = b[len(re.match(r'<h3>.*?</h3>', b, flags=re.S).group(0)):]
            if name.startswith('Decided'):
                html_out.append('<details><summary>%s</summary><div>%s</div></details>' % (h, inner))
            else:
                kind = 'todo' if '🟠' in h else ('next' if '🔵' in h else '')
                html_out.append('<section class="q %s"><h3>%s</h3>%s</section>' % (kind, h, inner))
    html_out.append('<p class="foot">This page is a view of <code>articles/inner-child-therapy/OWNER-QUESTIONS.md</code>, '
                    'rebuilt from it after every change. Answer in chat, like <code>85: A</code>.</p></div>')
    return STYLE + '\n'.join(html_out)


LINKS = ''


def main(argv):
    global LINKS
    out = pathlib.Path(argv[1]) if len(argv) > 1 else HERE / 'QUESTIONS-PAGE.html'
    links = [('The file on GitHub', 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/OWNER-QUESTIONS.md'),
             ('The article so far', 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md')]
    LINKS = '<p class="links">' + ''.join('<a href="%s">%s</a>' % (u, t) for t, u in links) + '</p>'
    md = SRC.read_text(encoding='utf-8')
    bad = unlinked_ai_asks(md)
    if bad:
        print('refused (E214): these open questions say a stretch reads AI but link no check:\n  ' + '\n  '.join(bad),
              file=sys.stderr)
        return 1
    bad = unpaneled_help_asks(md)
    if bad:
        print('refused (E253): these open questions ask your help with tells but link no tell panel record '
              '(tools/humanization/tell_panel.py):\n  ' + '\n  '.join(bad), file=sys.stderr)
        return 1
    bad = old_number_refs(md)
    if bad:
        print('refused (E257): these lines point to a decided question by its number alone; say what it was:\n  '
              + '\n  '.join(bad), file=sys.stderr)
        return 1
    out.write_text(render(md), encoding='utf-8')
    print('wrote', out)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
