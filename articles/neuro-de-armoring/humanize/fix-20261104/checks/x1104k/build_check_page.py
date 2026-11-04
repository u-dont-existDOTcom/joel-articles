"""Neuro De-Armoring Checks: the batch's paragraphs for Joel to check in Pangram's web app, one at a time (his message of
2026-11-04 14:59 UTC: "i'm not topping up the api unless you think it's really important because we have tons of gui
credits still"). Each copy button copies the paragraph's text exactly as TEXTS.json has it, and nothing else: no label,
number or mark of this page (E326; his history of 2 November, where my cards pages' labels came along with the text).

  python3 articles/neuro-de-armoring/humanize/fix-20261104/checks/x1104k/build_check_page.py
Writes CHECK-PAGE.html here.
"""
import datetime
import html
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
TEXTS = json.loads((HERE / 'TEXTS.json').read_text(encoding='utf-8'))
PRED = {r['key']: r for r in json.loads((HERE / 'PREDICTIONS.json').read_text(encoding='utf-8'))}
WHAT = {
    'b085': 'The stop instruction now comes first, the way your agmatine warning starts, and the list has uneven shapes.',
    'b086': '"Take that as a safety signal" is said as what it means: your sensitivity is coming back.',
    'b088': 'Your own "Who this is for" build from the uridine section, with "though".',
    'b089': 'The uses in brackets after "what it\'s been used for", and the evidence caveat moved to the end.',
    'b090': 'First try, never checked: the API ran out before it.',
    'b091': 'First try, never checked: the API ran out before it.',
}


def card(n, key):
    t = TEXTS[key]
    p = PRED[key]
    return ('<section class="card" aria-labelledby="h-%(k)s">\n'
            '<div class="head"><h2 id="h-%(k)s"><span class="n">%(n)d</span>%(name)s</h2>'
            '<span class="meta">%(w)d words · my chance of Human: %(c)d%%</span></div>\n'
            '<p class="what">%(what)s</p>\n'
            '<div class="text" id="t-%(k)s">%(t)s</div>\n'
            '<div class="row"><button type="button" class="copy" id="c-%(k)s" data-for="t-%(k)s">Copy paragraph %(n)d</button>'
            '<span class="done" id="d-%(k)s" aria-live="polite"></span></div>\n'
            '</section>') % {'k': key, 'n': n, 'name': html.escape(p['name'][0].upper() + p['name'][1:]), 'w': len(t.split()),
                             'c': round(p['chance'] * 100), 'what': html.escape(WHAT[key]), 't': html.escape(t)}


def main():
    built = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    cards = '\n'.join(card(i + 1, k) for i, k in enumerate(TEXTS))
    page = '''<title>Neuro De-Armoring Checks</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* one column of check slips: a label, the paragraph as it will be pasted, one copy button */
:root {
  --bg: #f3f6f5; --paper: #ffffff; --ink: #17201e; --muted: #56635f; --line: #d3dcd9; --accent: #1f6f62; --accent-ink: #ffffff;
  --body: "Atkinson Hyperlegible", "Segoe UI", system-ui, sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #121816; --paper: #1a2220; --ink: #e4ece9; --muted: #9aa8a3; --line: #2e3a37; --accent: #5cc0ad; --accent-ink: #0d1412; color-scheme: dark } }
:root[data-theme="dark"] {
  --bg: #121816; --paper: #1a2220; --ink: #e4ece9; --muted: #9aa8a3; --line: #2e3a37; --accent: #5cc0ad; --accent-ink: #0d1412; color-scheme: dark }
body { background: var(--bg); color: var(--ink); font-family: var(--body); font-size: 16px; line-height: 1.55;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 28px 48px; }
main { max-width: 46rem; margin: 0 auto; display: flex; flex-direction: column; gap: 18px; }
h1 { font-size: 1.6rem; line-height: 1.2; margin: 0; text-wrap: balance; }
.intro { display: flex; flex-direction: column; gap: 8px; color: var(--ink); }
.intro p { margin: 0; max-width: 65ch; }
.small { color: var(--muted); font-size: 0.9rem; }
.card { background: var(--paper); border: 1px solid var(--line); border-radius: 6px; padding: 16px; display: flex; flex-direction: column; gap: 10px; min-width: 0; }
.head { display: flex; flex-wrap: wrap; align-items: baseline; justify-content: space-between; gap: 4px 12px; }
h2 { font-size: 1.05rem; margin: 0; display: flex; gap: 10px; align-items: baseline; text-wrap: balance; }
.n { font-family: var(--mono); font-weight: 500; color: var(--accent); }
.meta { font-family: var(--mono); font-size: 0.78rem; letter-spacing: 0.02em; color: var(--muted); font-variant-numeric: tabular-nums; }
.what { margin: 0; color: var(--muted); font-size: 0.92rem; }
.text { border-left: 3px solid var(--line); padding: 4px 0 4px 12px; white-space: pre-wrap; overflow-wrap: anywhere; user-select: all; -webkit-user-select: all; }
.row { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
button.copy { font: inherit; font-weight: 700; font-size: 0.95rem; background: var(--accent); color: var(--accent-ink); border: 0; border-radius: 4px; padding: 8px 14px; cursor: pointer; }
button.copy:focus-visible { outline: 3px solid var(--ink); outline-offset: 2px; }
.done { font-size: 0.9rem; color: var(--muted); }
@media (prefers-reduced-motion: no-preference) { button.copy { transition: filter 0.15s; } button.copy:hover { filter: brightness(1.08); } }
</style>
<main>
<div class="intro">
<h1>Neuro De-Armoring Checks</h1>
<p>Six paragraphs for Pangram's web checker, each checked by itself. Copy one, paste it in by itself, check it, and send me the link. The button copies the paragraph only, without this page's numbers or labels.</p>
<p>I wrote my predictions down before you check: I expect all six to read AI. My chances of a Human result are 25%% to 35%%. Paragraphs 1 to 4 are second tries, after the three readers' notes on the first tries.</p>
<p class="small">Batch x1104k, built %(built)s.</p>
</div>
%(cards)s
</main>
<script>
document.querySelectorAll('button.copy').forEach(function (b) {
  b.addEventListener('click', function () {
    var el = document.getElementById(b.dataset.for);
    var done = document.getElementById('d-' + b.dataset.for.slice(2));
    var text = el.textContent;
    function selectIt() {
      var r = document.createRange(); r.selectNodeContents(el);
      var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
      done.textContent = 'Selected: press Ctrl+C or Cmd+C to copy.';
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () { done.textContent = 'Copied.'; }, selectIt);
    } else { selectIt(); }
  });
});
</script>
''' % {'built': built, 'cards': cards}
    (HERE / 'CHECK-PAGE.html').write_text(page, encoding='utf-8')
    print('ok', len(page), list(TEXTS))


if __name__ == '__main__':
    main()
