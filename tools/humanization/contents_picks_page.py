#!/usr/bin/env python3
"""contents_picks_page.py - Joel's contents picks page: his headings as Substack's narrow contents sidebar shows them,
beside each proposal, then every heading in order with the first words of its section, the options as radio choices with
fits / only just fits / cut off, a "Your own words" box, the run's questions, and his answers saved as he goes.

What it does and why:
- Every option is shown as the sidebar shows it, cut-offs included (gates bad-trips-2026-11-09f, inner-child-2026-11-16a),
  with the first words of its section as context (Joel, 2026-11-22: "show me all the context so the part i am looking at
  makes sense").
- The "Your own words" box marks where the sidebar cuts a heading at that level: a dashed line at the cut-off, drawn in
  the sidebar's font (Inter 15px; 217, 205, 193 and 181px for h1 to h4, tools/humanization/toc_sidebar.py), and under the
  box, as he types, whether it fits, only just fits or is cut off, and what the sidebar would show (lesson
  toc-2026-11-23a; Joel, 2026-11-23 17:24 UTC: "I told you before but i'd still like to have some visible maker for
  "your own words" where it would show me how long it can be").
- It declares the artifact's database, saves every change there, one write at a time, with the heading text of every
  pick and not only which column was clicked; answers saved only in this browser go up to the database when it opens; and
  "Copy my answers" gives the same record as JSON for the chat (lesson bad-trips-2026-11-21c). Declare it after the first
  publish: capabilities {"db": {"rules": [{"path": "", "read": "view", "write": "admin"}]}}.
- Options with the same text merge into one choice, so a pick is never split between two identical buttons.

  python3 tools/humanization/contents_picks_page.py RUN_DIR PAGE-OPTIONS.json OUT.html

RUN_DIR holds CONTENTS-NOW.json ([{id, level, heading, words}] in the post's order), SECTIONS.json ([{id, text}]) and
each option's file ([{id, level, heading, kind}]). PAGE-OPTIONS.json: {title, sub, store, primary (the option key the
"Take all of the proposal" button picks), options: {key: {label, file}}, pick: {id: key}, notes: {id: html},
kinds: {kind: plain label}, questions: [{id, text}], scores: {question, table, git}}. The first run is
articles/nibbana/experiments/toc-20261123/ (make_results.py writes its PAGE-OPTIONS.json).
"""
import html, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import toc_sidebar as ts


def first_words(text, n=34):
    w = text.split()
    return ' '.join(w[:n]) + (' …' if len(w) > n else '')


def main(run_dir, opts_path, out_path):
    O = json.load(open(opts_path, encoding='utf-8'))
    now = json.load(open(os.path.join(run_dir, 'CONTENTS-NOW.json'), encoding='utf-8'))
    S = {s['id']: s for s in json.load(open(os.path.join(run_dir, 'SECTIONS.json'), encoding='utf-8'))}
    for e in now:
        e['first'] = first_words(S[e['id']]['text'])
    opts = {}
    for key, meta in O['options'].items():
        E = {e['id']: e for e in json.load(open(os.path.join(run_dir, meta['file']), encoding='utf-8'))}
        opts[key] = {'label': meta['label'], 'entries': [{'id': i, 'level': E[i]['level'], 'heading': E[i]['heading'],
                                                           'kind': E[i].get('kind', '')} for i in (e['id'] for e in now)]}
    data = {'now': now, 'options': opts, 'pick': O.get('pick', {}), 'notes': O.get('notes', {}), 'room': ts.ROOM,
            'scores': O['scores'], 'questions': O.get('questions', []), 'store': O['store'], 'kinds': O.get('kinds', {})}
    page = T.replace('__TITLE__', html.escape(O['title'])).replace('__SUB__', html.escape(O['sub'])).replace('__PRIMARY__', O.get('primary', 'pick'))
    page = page.replace('__DATA__', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))
    open(out_path, 'w', encoding='utf-8').write(page)
    print('page', out_path, len(page))


T = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{--ink:#1d1b18;--soft:#5b554d;--faint:#8d867c;--line:#e6e0d6;--paper:#fbf8f3;--card:#fff;--accent:#9a4a1f;--ok:#2f6b3a;--warn:#9a6a00;--bad:#a3322a}
@media (prefers-color-scheme: dark){:root{--ink:#ece6dc;--soft:#c2b9ab;--faint:#958c80;--line:#3a352f;--paper:#1c1a17;--card:#24211d;--accent:#e08a57;--ok:#7cc48a;--warn:#e0b24f;--bad:#ef7d72}}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.5 Georgia,"Iowan Old Style",serif}
main{max-width:1180px;margin:0 auto;padding:28px 20px 80px}
h1{font:600 26px/1.25 Inter,system-ui,sans-serif;margin:0 0 6px}h2{font:600 19px/1.3 Inter,system-ui,sans-serif;margin:34px 0 10px}
.sub{color:var(--soft);margin:0 0 18px}.q{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px 18px;margin:16px 0}
table.sc{border-collapse:collapse;font:14px/1.4 Inter,system-ui,sans-serif;margin:8px 0}table.sc th,table.sc td{border-bottom:1px solid var(--line);padding:6px 10px;text-align:left}
table.sc td.n{text-align:right;font-variant-numeric:tabular-nums}
.bars{display:flex;gap:18px;overflow-x:auto;padding-bottom:8px}
.col{flex:0 0 auto}.col h3{font:600 13px/1.3 Inter,system-ui,sans-serif;margin:0 0 6px;color:var(--soft);text-transform:uppercase;letter-spacing:.05em}
.menu{width:max-content;max-height:620px;overflow-y:auto;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:8px;box-shadow:0 2px 10px rgba(0,0,0,.06)}
.menu .ct{font:500 11px/20px Inter,system-ui,sans-serif;text-transform:uppercase;padding:4px;color:var(--ink)}
.row{padding:4px}.lab{display:block;width:217px;font:400 15px/20px Inter,system-ui,sans-serif;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:var(--soft)}
.l1 .lab{color:var(--ink)}.l2 .lab{padding-left:12px}.l3 .lab{padding-left:24px}.l4 .lab{padding-left:36px}
.row.changed .lab{color:var(--accent)}
.legend{font:13px/1.4 Inter,system-ui,sans-serif;color:var(--soft);margin:6px 0 0}
.tools{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
button{font:500 14px/1 Inter,system-ui,sans-serif;padding:9px 12px;border-radius:7px;border:1px solid var(--line);background:var(--card);color:var(--ink);cursor:pointer}
button.pri{background:var(--accent);border-color:var(--accent);color:#fff}button:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.part{margin:26px 0 6px;font:600 15px/1.3 Inter,system-ui,sans-serif}
.item{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 12px;margin:6px 0}
.item.same{opacity:.9}
.item .top{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;font:13px/1.4 Inter,system-ui,sans-serif;color:var(--faint)}
.ctx{font:italic 14px/1.45 Georgia,serif;color:var(--soft);margin:4px 0 8px}
.why{font:13px/1.45 Inter,system-ui,sans-serif;color:var(--soft);margin:2px 0 6px}
.ch{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:6px}
.ch label{display:flex;gap:8px;align-items:flex-start;border:1px solid var(--line);border-radius:6px;padding:7px 8px;cursor:pointer;font:15px/1.35 Inter,system-ui,sans-serif}
.ch label.sel{border-color:var(--accent);box-shadow:inset 0 0 0 1px var(--accent)}
.ch small{display:block;font-size:12px;color:var(--faint)}
.st{font:600 11px/1 Inter,system-ui,sans-serif;padding:2px 6px;border-radius:9px;border:1px solid currentColor;white-space:nowrap}
.st.fits{color:var(--ok)}.st.tight{color:var(--warn)}.st.cut{color:var(--bad)}
.kind{font:600 11px/1 Inter,system-ui,sans-serif;padding:2px 6px;border-radius:9px;background:rgba(154,74,31,.12);color:var(--accent);white-space:nowrap}
input[type=text],textarea{width:100%;font:15px/1.4 Inter,system-ui,sans-serif;padding:7px 8px;border:1px solid var(--line);border-radius:6px;background:var(--paper);color:var(--ink)}
textarea{min-height:70px}.saved{font:13px/1.4 Inter,system-ui,sans-serif;color:var(--faint)}
.sticky{position:sticky;top:0;background:var(--paper);padding:8px 0;z-index:2;border-bottom:1px solid var(--line)}
.flt{font:14px/1.3 Inter,system-ui,sans-serif;color:var(--soft);display:flex;gap:6px;align-items:center;padding:6px 4px}
.scroll{overflow-x:auto;max-width:100%}ul.legend{padding-left:20px}
.ownbox{position:relative;display:block;margin-top:5px;max-width:100%}
.ch label[data-ownlab]{grid-column:1/-1}
.ownbox input[type=text]{font:400 15px/20px Inter,system-ui,sans-serif;padding:7px 8px;border:1px solid var(--line);width:calc(var(--room) + 300px);max-width:100%}
.cutline{position:absolute;top:-3px;bottom:-3px;left:calc(9px + var(--room));border-left:2px dashed var(--warn);pointer-events:none}
.ownbox.cut .cutline{border-left-color:var(--bad)}
.ownst{display:block;margin-top:4px;font:12px/1.35 Inter,system-ui,sans-serif;color:var(--faint)}.ownst b{font-weight:600}
.ownst.fits b{color:var(--ok)}.ownst.tight b{color:var(--warn)}.ownst.cut b{color:var(--bad)}
</style></head><body><main>
<h1>__TITLE__</h1>
<p class="sub">__SUB__</p>
<div class="q" id="question"></div>
<h2>What fresh readers found</h2><div id="scores"></div>
<h2>The contents, as the sidebar shows it</h2>
<p class="legend">Each list is drawn at the sidebar's width in the font it uses (Inter, 15px), so the "…" falls where it falls on your post. Headings that differ from yours are in colour. The last list follows your picks.</p>
<div class="bars" id="bars"></div>
<h2>Your pick, heading by heading</h2>
<p class="legend">Every heading is here, in order, with the first words of its section. The proposal is picked to start with; click another, or write your own. Your picks save as you go.</p>
<div class="sticky"><div class="tools">
<button type="button" class="pri" data-all="__PRIMARY__">Take all of the proposal</button>
<button type="button" data-all="now">Keep all as they are</button>
<button type="button" id="copy">Copy my answers</button>
<label class="flt"><input type="checkbox" id="onlydiff"> Only the headings that would change</label>
<span class="saved" id="saved" aria-live="polite"></span></div></div>
<div id="items"></div>
<div id="qs"></div>
<h2>Anything else</h2><textarea id="comment" placeholder="Your comment for the next turn"></textarea>
<p class="legend" id="gitnote"></p>
</main>
<script>
const D = __DATA__;
const KEYS = Object.keys(D.options);
const byId = {}; D.now.forEach(e => byId[e.id] = {now: e});
KEYS.forEach(k => D.options[k].entries.forEach(e => byId[e.id][k] = e));
const STORE_KEY = D.store;
let ans = {picks: {}, own: {}, answers: {}, comment: ''};
let local = null;
try { const s = localStorage.getItem(STORE_KEY); if (s) { local = JSON.parse(s); ans = Object.assign(ans, local); } } catch (e) {}
let doc = null;
const cv = document.createElement('canvas').getContext('2d');
function measure(t){ cv.font = '400 15px Inter'; return cv.measureText(t).width; }
function status(t, lvl){ const room = D.room[lvl], w = measure(t); return w > room + .01 ? 'cut' : (room - w < 12 ? 'tight' : 'fits'); }
const SAY = {fits: 'fits', tight: 'only just fits', cut: 'cut off'};
function shownText(t, lvl){ const room = D.room[lvl]; if (measure(t) <= room + .01) return t; let a = Array.from(t);
  while (a.length && measure(a.join('').trimEnd() + '…') > room) a.pop(); return a.join('').trimEnd() + '…'; }
function ownStatus(t, lvl){
  const room = D.room[lvl], h = '#'.repeat(lvl);
  if (!t) return {cls: '', html: `The dashed line is where the sidebar cuts a ${h} heading (${room}px at 15px).`};
  const st = status(t, lvl), left = Math.round(room - measure(t));
  if (st === 'cut') return {cls: 'cut', html: `<b>cut off</b>: the sidebar shows “${esc(shownText(t, lvl))}”`};
  if (st === 'tight') return {cls: 'tight', html: `<b>only just fits</b>: ${left}px to spare, so some browsers may cut a letter`};
  return {cls: 'fits', html: `<b>fits</b>: ${left}px to spare`};
}
function placeLine(ob){
  const inp = ob.querySelector('input'), line = ob.querySelector('.cutline'); if (!inp || !line) return;
  const x = 9 + D.room[+inp.dataset.level] - inp.scrollLeft;
  line.style.left = x + 'px'; line.style.display = (x < 4 || x > inp.offsetWidth - 2) ? 'none' : '';
}
document.addEventListener('scroll', ev => { const t = ev.target; if (t && t.dataset && t.dataset.own) placeLine(t.parentNode); }, true);
['keyup', 'click', 'focusin', 'select'].forEach(n => document.addEventListener(n, ev => { const t = ev.target; if (t && t.dataset && t.dataset.own) placeLine(t.parentNode); }));
function showOwn(id, lvl, t){
  const s = ownStatus(t, lvl), el = document.getElementById('st-' + id), ob = document.getElementById('ob-' + id);
  if (el) { el.className = 'ownst ' + s.cls; el.innerHTML = s.html; }
  if (ob) { ob.classList.toggle('cut', s.cls === 'cut'); placeLine(ob); }
  const r = document.querySelector(`input[name="p-${id}"][value="own"]`); if (r) r.checked = true;
  const it = document.getElementById('i-' + id); if (it) it.querySelectorAll('.ch label').forEach(l => l.classList.toggle('sel', l.dataset.ownlab === id));
}
function esc(s){ return String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }
function pickOf(id){ return ans.picks[id] || D.pick[id] || 'now'; }
function choice(id){ const p = pickOf(id); if (p === 'own') return (ans.own[id] || byId[id].now.heading); return (byId[id][p] || byId[id].now).heading; }
function differs(id){ return KEYS.some(k => byId[id][k] && byId[id][k].heading !== byId[id].now.heading); }
function record(){ return {page: STORE_KEY, saved: new Date().toISOString(), picks: ans.picks, own: ans.own, answers: ans.answers, comment: ans.comment,
  headings: Object.fromEntries(D.now.map(e => [e.id, choice(e.id)])), changed: D.now.filter(e => choice(e.id) !== e.heading).map(e => ({id: e.id, was: e.heading, now: choice(e.id)}))}; }
function menu(title, entries, from){
  const rows = entries.map(e => `<div class="row l${e.level}${from && from[e.id] !== e.heading ? ' changed' : ''}"><div class="lab">${esc(e.heading)}</div></div>`).join('');
  return `<div class="col"><h3>${esc(title)}</h3><div class="menu"><div class="ct">Contents</div>${rows}</div></div>`;
}
function drawBars(){
  const nowMap = {}; D.now.forEach(e => nowMap[e.id] = e.heading);
  let h = menu('Yours, as it is', D.now, null);
  KEYS.forEach(k => h += menu(D.options[k].label, D.options[k].entries, nowMap));
  h += menu('Your picks', D.now.map(e => ({id: e.id, level: e.level, heading: choice(e.id)})), nowMap);
  document.getElementById('bars').innerHTML = h;
  document.querySelectorAll('.menu').forEach(m => m.addEventListener('scroll', () => { const t = m.scrollTop; document.querySelectorAll('.menu').forEach(o => { if (o !== m && Math.abs(o.scrollTop - t) > 2) o.scrollTop = t; }); }));
}
let onlyDiff = false;
function drawItems(){
  let h = '';
  D.now.forEach(e => {
    const changes = differs(e.id);
    if (e.level === 1) h += `<div class="part">${esc(e.heading)}</div>`;
    if (onlyDiff && !changes) return;
    const cur = pickOf(e.id);
    const opts = [], seen = {};
    [['now', 'As it is']].concat(KEYS.filter(k => byId[e.id][k] && byId[e.id][k].heading !== e.heading).map(k => [k, D.options[k].label])).forEach(([k, lab]) => {
      const t = (byId[e.id][k] || e).heading;
      if (seen[t] !== undefined) { opts[seen[t]][1] += ' · ' + lab; return; }
      seen[t] = opts.length; opts.push([k, lab]); });
    const curText = cur === 'own' ? null : (byId[e.id][cur] || e).heading;
    let labels = '';
    opts.forEach(([k, lab]) => {
      const t = (byId[e.id][k] || e).heading, st = status(t, e.level), on = curText === t;
      labels += `<label class="${on ? 'sel' : ''}"><input type="radio" name="p-${e.id}" value="${k}" ${on ? 'checked' : ''}><span>${esc(t)}<small>${esc(lab)} · <span class="st ${st}">${SAY[st]}</span></small></span></label>`;
    });
    const ow = ans.own[e.id] || '', os = ownStatus(ow, e.level);
    labels += `<label class="${cur === 'own' ? 'sel' : ''}" data-ownlab="${e.id}"><input type="radio" name="p-${e.id}" value="own" ${cur === 'own' ? 'checked' : ''}><span style="flex:1;min-width:0">Your own words<span class="ownbox${os.cls === 'cut' ? ' cut' : ''}" id="ob-${e.id}" style="--room:${D.room[e.level]}px"><input type="text" data-own="${e.id}" data-level="${e.level}" value="${esc(ow)}" placeholder="Type a heading" aria-describedby="st-${e.id}"><i class="cutline" aria-hidden="true"></i></span><small class="ownst ${os.cls}" id="st-${e.id}" aria-live="polite">${os.html}</small></span></label>`;
    const k0 = KEYS.find(k => byId[e.id][k] && byId[e.id][k].heading !== e.heading);
    const kd = k0 ? byId[e.id][k0].kind || '' : '', kl = (D.kinds && kd in D.kinds) ? D.kinds[kd] : kd;
    const kind = kl ? `<span class="kind">${esc(kl)}</span>` : (changes ? '' : '<span>kept as it is</span>');
    const note = D.notes[e.id] ? `<div class="why">${D.notes[e.id]}</div>` : '';
    h += `<div class="item${changes ? '' : ' same'}" id="i-${e.id}"><div class="top"><span>${e.id}</span><span>${'#'.repeat(e.level)}</span><span>${e.words} words</span>${kind}</div><div class="ctx">${esc(e.first)}</div>${note}<div class="ch">${labels}</div></div>`;
  });
  document.getElementById('items').innerHTML = h;
}
function drawQs(){
  if (!D.questions.length) return;
  let h = '<h2>Questions</h2>';
  D.questions.forEach(q => { h += `<div class="item"><div class="top"><span>${esc(q.id)}</span></div><div class="why" style="font-size:15px;color:var(--ink)">${q.text}</div><textarea data-q="${esc(q.id)}" placeholder="Your answer">${esc(ans.answers[q.id] || '')}</textarea></div>`; });
  document.getElementById('qs').innerHTML = h;
}
let writing = false, dirty = false, timer = null;
function flush(){
  if (!doc) return;
  if (writing) { dirty = true; return; }
  writing = true; dirty = false;
  const s = document.getElementById('saved');
  doc.set(record()).then(() => { s.textContent = 'Saved'; }).catch(() => { s.textContent = 'Saved in this browser only'; })
    .finally(() => { writing = false; if (dirty) flush(); });
}
function save(){
  try { localStorage.setItem(STORE_KEY, JSON.stringify(ans)); } catch (e) {}
  const s = document.getElementById('saved');
  if (doc) { s.textContent = 'Saving…'; clearTimeout(timer); timer = setTimeout(flush, 500); }
  else s.textContent = 'Saved in this browser';
}
document.addEventListener('change', ev => { const t = ev.target;
  if (t.type === 'radio' && t.name.startsWith('p-')) { ans.picks[t.name.slice(2)] = t.value; save(); redraw(); } });
document.addEventListener('input', ev => { const t = ev.target;
  if (t.dataset && t.dataset.own) { ans.own[t.dataset.own] = t.value; ans.picks[t.dataset.own] = 'own'; showOwn(t.dataset.own, +t.dataset.level, t.value); save(); drawBars(); }
  if (t.dataset && t.dataset.q) { ans.answers[t.dataset.q] = t.value; save(); }
  if (t.id === 'comment') { ans.comment = t.value; save(); } });
function redraw(){ const y = window.scrollY; drawItems(); drawBars(); window.scrollTo(0, y); }
document.querySelectorAll('[data-all]').forEach(b => b.addEventListener('click', () => { const k = b.dataset.all; D.now.forEach(e => { ans.picks[e.id] = (k === 'now' || byId[e.id][k]) ? k : 'now'; }); save(); redraw(); }));
document.getElementById('copy').addEventListener('click', async () => {
  const out = JSON.stringify(record());
  try { await navigator.clipboard.writeText(out); document.getElementById('saved').textContent = 'Copied: paste it into the chat'; }
  catch (e) { const ta = document.getElementById('comment'); ta.value = out; ta.select(); document.getElementById('saved').textContent = 'Copy the text in the box below'; } });
document.getElementById('onlydiff').addEventListener('change', ev => { onlyDiff = ev.target.checked; redraw(); });
document.getElementById('question').innerHTML = D.scores.question;
document.getElementById('scores').innerHTML = D.scores.table;
document.getElementById('gitnote').innerHTML = D.scores.git;
document.getElementById('comment').value = ans.comment || '';
function draw(){ drawBars(); drawItems(); drawQs(); }
draw();
if (document.fonts && document.fonts.ready) document.fonts.ready.then(draw);
(async () => {
  try {
    for (let i = 0; i < 30 && !(window.claude && window.claude.use); i++) await new Promise(r => setTimeout(r, 100));
    if (!window.claude || !window.claude.use) return;
    const db = await window.claude.use('db'); if (!db) return;
    doc = db.doc('answers/joel');
    const snap = await doc.get();
    const v = snap && (snap.data ? snap.data() : snap);
    if (v && v.picks) { ans = Object.assign(ans, {picks: v.picks, own: v.own || {}, answers: v.answers || {}, comment: v.comment || ''}); document.getElementById('comment').value = ans.comment; draw(); document.getElementById('saved').textContent = 'Your answers are back'; }
    else if (local && Object.keys(local.picks || {}).length) { await doc.set(record()); document.getElementById('saved').textContent = 'Saved what this browser had'; }
  } catch (e) { doc = null; }
})();
</script></body></html>"""

if __name__ == '__main__':
    main(*sys.argv[1:])
