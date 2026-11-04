#!/usr/bin/env python3
"""Turn 128: SKETCHES.html, the marking page of sketch ideas for GPT (ideas.py), each with where it goes in his live post
(SPOTS.json, from the spots found so that no stretch of text runs past about 300 words, a desktop screen or two phone
screens, before a picture, video, card or pull quote). He marks each Make it / Skip / Change (a note), kept in the page's
own store (the db capability, collection "marks", one document per sketch, S01 to S85), which I read back."""
import html
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from ideas import CAST, IDEAS, STYLE  # noqa: E402

spots = json.loads((HERE / 'SPOTS.json').read_text(encoding='utf-8'))
assert len(spots) == len(IDEAS) == 85, (len(spots), len(IDEAS))


def first_words(t, n=14):
    w = re.sub(r'\s+', ' ', t).strip().split(' ')
    return ' '.join(w[:n]) + ('…' if len(w) > n else '')


cards = []
for s in spots:
    title, point, prompt = IDEAS[s['n']]
    sec = s['section'].split(' > ')
    cards.append({'id': 'S%02d' % s['n'], 'title': title, 'point': point, 'prompt': prompt,
                  'gentle': prompt.startswith('Gentle'), 'section': ' › '.join(sec[-2:]) if len(sec) > 1 else sec[0],
                  'after': first_words(s['before']), 'next': first_words(s['next'], 10) if s['next'] else ''})
DATA = {'style': STYLE, 'cast': CAST, 'cards': cards}
(HERE / 'SKETCHES.json').write_text(json.dumps(DATA, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

PAGE = r'''<title>Inner Child Guide Sketches</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&display=swap">
<style>
/* Layout: one column of sketchbook cards under a sticky filter bar; the hand-lettered face only for numbers and titles. */
:root {
  --paper: #fbfaf6; --card: #ffffff; --ink: #23252a; --muted: #62666f; --line: #dcdcd5;
  --orange: #d9772b; --orange-soft: #fbeadb; --teal: #2b8a8a; --teal-soft: #dcefee; --gray-soft: #eeeeea;
  --hand: "Kalam", "Comic Neue", "Segoe Print", cursive; --body: "Source Sans 3", "Segoe UI", system-ui, sans-serif;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --paper: #1c1d20; --card: #25272b; --ink: #ecebe6; --muted: #a7aab1; --line: #3a3c42;
  --orange: #f0954d; --orange-soft: #4a3222; --teal: #5cc0bf; --teal-soft: #1f3b3b; --gray-soft: #303237; color-scheme: dark } }
:root[data-theme="dark"] {
  --paper: #1c1d20; --card: #25272b; --ink: #ecebe6; --muted: #a7aab1; --line: #3a3c42;
  --orange: #f0954d; --orange-soft: #4a3222; --teal: #5cc0bf; --teal-soft: #1f3b3b; --gray-soft: #303237; color-scheme: dark }
* { box-sizing: border-box; }
body { background: var(--paper); color: var(--ink); font: 400 1.0625rem/1.55 var(--body); margin: 0; }
.wrap { max-width: 48rem; margin: 0 auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 1.5rem 4rem; }
h1 { font: 700 2.1rem/1.15 var(--hand); margin: 0 0 .4rem; text-wrap: balance; }
.lede { color: var(--muted); margin: 0 0 1.25rem; max-width: 40rem; }
.how { background: var(--card); border: 1px solid var(--line); border-radius: 10px; padding: 1rem 1.1rem; display: grid; gap: .75rem; }
.how h2 { font: 700 1.25rem/1.2 var(--hand); margin: 0; }
.how ol { margin: 0; padding-left: 1.25rem; display: grid; gap: .35rem; }
.how code { font-size: .9em; background: var(--gray-soft); padding: .05em .35em; border-radius: 4px; overflow-wrap: anywhere; }
.setup { white-space: pre-wrap; background: var(--gray-soft); border-radius: 8px; padding: .75rem .85rem; font-size: .95rem; margin: 0; }
.row { display: flex; flex-wrap: wrap; gap: .5rem; align-items: center; }
button { font: 600 .95rem/1 var(--body); border-radius: 999px; border: 1px solid var(--line); background: var(--card); color: var(--ink); padding: .55rem .9rem; cursor: pointer; }
button:hover { border-color: var(--ink); }
button:focus-visible, textarea:focus-visible { outline: 3px solid var(--teal); outline-offset: 2px; }
button.primary { background: var(--ink); color: var(--paper); border-color: var(--ink); }
.bar { position: sticky; top: env(safe-area-inset-top, 0px); z-index: 5; background: var(--paper); padding-block: .75rem; margin-top: 1.25rem; border-bottom: 1px solid var(--line); }
body::before { content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 10; background: var(--paper); }
.filters button[aria-pressed="true"] { background: var(--teal-soft); border-color: var(--teal); }
.count { font-variant-numeric: tabular-nums; color: var(--muted); font-weight: 400; }
.status { font-size: .9rem; color: var(--muted); min-height: 1.3em; }
.cards { display: grid; gap: 1rem; margin-top: 1rem; }
.card { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 1rem 1.1rem; display: grid; grid-template-columns: 4.2rem minmax(0, 1fr); gap: .25rem 1rem; }
.num { font: 700 1.7rem/1 var(--hand); color: var(--orange); padding-top: .15rem; }
.card[data-choice="make"] { border-color: var(--teal); box-shadow: inset 4px 0 0 var(--teal); }
.card[data-choice="skip"] { opacity: .6; }
.card[data-choice="change"] { border-color: var(--orange); box-shadow: inset 4px 0 0 var(--orange); }
.body { min-width: 0; display: grid; gap: .5rem; }
.title { font: 700 1.3rem/1.2 var(--hand); margin: 0; }
.tag { display: inline-block; font: 600 .75rem/1 var(--body); letter-spacing: .04em; text-transform: uppercase; color: var(--teal); background: var(--teal-soft); border-radius: 999px; padding: .3rem .55rem; vertical-align: .2em; margin-left: .4rem; }
.where { font-size: .95rem; color: var(--muted); }
.where b { color: var(--ink); font-weight: 600; }
.point { margin: 0; }
.prompt { margin: 0; background: var(--orange-soft); border-radius: 8px; padding: .7rem .85rem; }
.marks button[aria-pressed="true"][data-c="make"] { background: var(--teal); color: var(--paper); border-color: var(--teal); }
.marks button[aria-pressed="true"][data-c="skip"] { background: var(--gray-soft); border-color: var(--muted); }
.marks button[aria-pressed="true"][data-c="change"] { background: var(--orange); color: var(--paper); border-color: var(--orange); }
textarea { width: 100%; min-height: 4.2rem; font: 400 1rem/1.4 var(--body); color: var(--ink); background: var(--paper); border: 1px solid var(--line); border-radius: 8px; padding: .5rem .6rem; resize: vertical; }
.saved { font-size: .85rem; color: var(--muted); }
@media (max-width: 30rem) { .card { grid-template-columns: minmax(0, 1fr); } .num { font-size: 1.4rem; } }
@media (prefers-reduced-motion: reduce) { * { scroll-behavior: auto !important; } }
</style>

<div class="wrap">
  <h1>Sketches for the Inner Child guide</h1>
  <p class="lede">85 spots in your live post where the text runs longer than about one computer screen, or two phone screens, without a picture, a video, a card or a pull quote. Each card has a funny sketch idea for GPT (a few in the hard sections are gentle instead), drawn from the paragraph just before it, and says exactly where it goes.</p>

  <section class="how" aria-labelledby="how-h">
    <h2 id="how-h">How to use these with GPT</h2>
    <ol>
      <li>Start one ChatGPT chat and paste the setup below. Ask it for a character sheet of the two characters first, so every sketch looks like the same pair.</li>
      <li>Then copy each card's prompt into that chat, one at a time.</li>
      <li>Save each picture with its number as the name (<code>S01.png</code>, <code>S02.png</code>…) in <code>~/ai-work/claude-dangerous-lane/inbox/t113/sketches/</code> on your laptop, and tell me. I'll put each one in the post where its card says.</li>
      <li>Mark a card <b>Skip</b> if you don't want it, or <b>Change</b> with a note if you want it different. I read your marks.</li>
    </ol>
    <pre class="setup" id="setup"></pre>
    <div class="row"><button class="primary" id="copy-setup" type="button">Copy the setup</button><button id="copy-all" type="button">Copy all 85 prompts</button><span class="status" id="copy-status" role="status"></span></div>
  </section>

  <div class="bar">
    <div class="row filters" role="group" aria-label="Show">
      <button type="button" data-f="all" aria-pressed="true">All <span class="count" id="n-all"></span></button>
      <button type="button" data-f="open" aria-pressed="false">Not marked <span class="count" id="n-open"></span></button>
      <button type="button" data-f="make" aria-pressed="false">Make it <span class="count" id="n-make"></span></button>
      <button type="button" data-f="change" aria-pressed="false">Change <span class="count" id="n-change"></span></button>
      <button type="button" data-f="skip" aria-pressed="false">Skip <span class="count" id="n-skip"></span></button>
    </div>
    <div class="status" id="db-status" role="status">Loading your marks…</div>
  </div>

  <div class="cards" id="cards"></div>
</div>

<script>
const DATA = __DATA__;
const $ = (s, r = document) => r.querySelector(s);
const marks = {};
let db = null;
let filter = 'all';
const setupText = DATA.style + '\n\n' + DATA.cast + '\n\nFirst, draw a character sheet of the grown-up and the little one in this style. Then I will send the sketches one by one, numbered.';
$('#setup').textContent = setupText;
const promptText = (c) => c.id + ': ' + c.prompt + ' (Same sketch style and the same two characters as the setup.)';
const allText = () => setupText + '\n\n' + DATA.cards.map((c) => promptText(c) + '\nGoes after the paragraph that starts "' + c.after + '" (' + c.section + ').').join('\n\n');

async function copy(text, btn) {
  const st = $('#copy-status');
  try { await navigator.clipboard.writeText(text); flash(btn, 'Copied'); st.textContent = ''; }
  catch (e) {
    const ta = document.createElement('textarea'); ta.value = text; ta.setAttribute('readonly', ''); ta.style.position = 'fixed'; ta.style.top = '-1000px';
    document.body.appendChild(ta); ta.select();
    let ok = false; try { ok = document.execCommand('copy'); } catch (e2) {}
    ta.remove();
    if (ok) flash(btn, 'Copied'); else st.textContent = 'Copying is blocked here: select the text and copy it yourself.';
  }
}
function flash(btn, t) { const old = btn.dataset.label || btn.textContent; btn.dataset.label = old; btn.textContent = t; setTimeout(() => { btn.textContent = old; }, 1400); }
$('#copy-setup').addEventListener('click', (e) => copy(setupText, e.currentTarget));
$('#copy-all').addEventListener('click', (e) => copy(allText(), e.currentTarget));

function render() {
  const root = $('#cards');
  root.textContent = '';
  for (const c of DATA.cards) {
    const m = marks[c.id] || {};
    const choice = m.choice || '';
    if (filter === 'open' && choice) continue;
    if (['make', 'skip', 'change'].includes(filter) && choice !== filter) continue;
    const el = document.createElement('article');
    el.className = 'card'; el.id = c.id; el.dataset.choice = choice;
    el.innerHTML = '<div class="num"></div><div class="body"><h3 class="title"></h3><div class="where">Goes after the paragraph that starts <b class="after"></b> <span class="sec"></span></div><p class="point"></p><p class="prompt"></p><div class="row"><button type="button" class="copy">Copy prompt</button></div><div class="row marks" role="group" aria-label="Your mark"><button type="button" data-c="make">Make it</button><button type="button" data-c="change">Change</button><button type="button" data-c="skip">Skip</button></div><textarea aria-label="What to change" placeholder="What to change (optional)"></textarea><div class="saved"></div></div>';
    $('.num', el).textContent = c.id;
    const t = $('.title', el); t.textContent = c.title;
    if (c.gentle) { const g = document.createElement('span'); g.className = 'tag'; g.textContent = 'gentle'; t.appendChild(g); }
    $('.after', el).textContent = '“' + c.after + '”';
    $('.sec', el).textContent = '(' + c.section + (c.next ? '; the next one starts “' + c.next + '”' : '') + ')';
    $('.point', el).textContent = 'Shows: ' + c.point;
    $('.prompt', el).textContent = c.prompt;
    $('.copy', el).addEventListener('click', (e) => copy(promptText(c), e.currentTarget));
    const ta = $('textarea', el); ta.id = 'note-' + c.id; ta.value = m.note || '';
    ta.hidden = !(choice === 'change' || (m.note || '').trim());
    for (const b of el.querySelectorAll('.marks button')) {
      b.setAttribute('aria-pressed', String(b.dataset.c === choice));
      b.addEventListener('click', () => {
        const next = b.dataset.c === choice ? '' : b.dataset.c;
        save(c.id, {choice: next, note: ta.value}, true).then(() => { if (next === 'change') { const t2 = document.getElementById('note-' + c.id); if (t2) t2.focus(); } });
      });
    }
    let timer = null;
    ta.addEventListener('input', () => { clearTimeout(timer); timer = setTimeout(() => save(c.id, {choice: (marks[c.id] || {}).choice || (ta.value.trim() ? 'change' : ''), note: ta.value}, false), 900); });
    ta.addEventListener('blur', () => { if (pending) { pending = false; render(); } });
    $('.saved', el).textContent = m.at ? 'Saved ' + new Date(m.at).toLocaleString() : '';
    root.appendChild(el);
  }
  counts();
}

let pending = false;
const typing = () => { const a = document.activeElement; return !!(a && a.tagName === 'TEXTAREA' && a.closest('#cards')); };
function counts() {
  const n = (f) => DATA.cards.filter((c) => (marks[c.id] || {}).choice === f).length;
  $('#n-all').textContent = DATA.cards.length;
  $('#n-open').textContent = DATA.cards.filter((c) => !(marks[c.id] || {}).choice).length;
  $('#n-make').textContent = n('make'); $('#n-change').textContent = n('change'); $('#n-skip').textContent = n('skip');
}
async function save(id, m, rerender) {
  const doc = {choice: m.choice, note: (m.note || '').slice(0, 2000), at: new Date().toISOString()};
  marks[id] = doc;
  if (rerender) render(); else { const card = document.getElementById(id); if (card) card.dataset.choice = doc.choice; counts(); pending = true; }
  const st = $('#db-status');
  if (!db) { st.textContent = 'Your marks can’t be saved in this view, so tell me in chat instead.'; return; }
  try { await db.doc('marks/' + id).set(doc); st.textContent = 'Saved. I read your marks from here.'; }
  catch (e) { st.textContent = 'That mark didn’t save (' + (e && e.code || 'error') + '). Try again in a moment, or tell me in chat.'; }
}

for (const b of document.querySelectorAll('.filters button')) {
  b.addEventListener('click', () => {
    filter = b.dataset.f;
    for (const x of document.querySelectorAll('.filters button')) x.setAttribute('aria-pressed', String(x === b));
    render();
  });
}
render();

(async () => {
  const st = $('#db-status');
  try { db = window.claude && window.claude.use ? await window.claude.use('db') : null; } catch (e) { db = null; }
  if (!db) { st.textContent = 'Your marks can’t be saved in this view, so tell me in chat instead.'; return; }
  const timer = setTimeout(() => { st.textContent = 'Your saved marks can’t be reached yet; they will show when they load.'; }, 10000);
  db.collection('marks').onSnapshot((snap) => {
    if (!snap.metadata.fromCache) clearTimeout(timer);
    for (const d of snap.docs) marks[d.id] = Object.assign({}, d.data());
    st.textContent = snap.size ? 'Your marks are saved here, and I read them.' : 'No marks yet. Mark any card and it is saved for me to read.';
    if (typing()) { pending = true; counts(); } else render();
  }, (e) => { clearTimeout(timer); st.textContent = 'Your marks stopped syncing (' + (e && e.code || 'error') + '). Reload the page to try again.'; });
})();
</script>
'''
page = PAGE.replace('__DATA__', json.dumps(DATA, ensure_ascii=False).replace('</', '<\\/'))
(HERE / 'SKETCHES.html').write_text(page, encoding='utf-8')
print('SKETCHES.html', len(page), 'bytes;', len(cards), 'cards;', sum(c['gentle'] for c in cards), 'gentle')
