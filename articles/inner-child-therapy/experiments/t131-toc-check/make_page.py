#!/usr/bin/env python3
"""Build the contents options page (turn 131's version of ../t130-toc/make_page.py): each option as Substack's sidebar
shows it, the readers' scores, and a pick per heading that saves as Joel clicks (the artifact's db, else this browser)
and copies out as JSON. New here: Fable's pick as the starting choice, one heading it would add, a switch that shows
only the headings where Fable and Opus differ, and the level of a pick taken from the option picked.
  python3 make_page.py OUT.html"""
import json, os, sys, html
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'tools', 'humanization'))
import toc_sidebar as ts

def load(f):
    return [e for e in json.load(open(os.path.join(HERE, f))) if not e.get('drop')]

T130 = os.path.join(HERE, '..', 't130-toc')
NOW = load(os.path.join(T130, 'LIVE-TOC.json'))
OPTS = json.load(open(os.path.join(HERE, 'PAGE-OPTIONS.json')))   # written by the turn's script: options, scores, picks, notes
words = {e['id']: e['words'] for e in NOW}
data = {'now': NOW, 'options': {}, 'scores': OPTS['scores'], 'pick': OPTS['pick'], 'notes': OPTS.get('notes', {}),
        'pointers': OPTS.get('pointers', []), 'room': ts.ROOM, 'added': [], 'kinds': {}, 'hide': OPTS.get('hide_columns', [])}
for key, meta in OPTS['options'].items():
    E = load(os.path.join(HERE, meta['file']))
    keep = []
    for e in E:
        if e.get('part_of'):            # a heading the option would add to the post
            data['added'].append({'id': e['id'], 'after': e['part_of'], 'level': e['level'], 'heading': e['heading'], 'option': key, 'why': e.get('why', '')})
            continue
        e['words'] = words[e['id']]
        if key == 'fable' and e.get('kind'):
            data['kinds'][e['id']] = e['kind']
        keep.append({'id': e['id'], 'level': e['level'], 'heading': e['heading'], 'words': e['words']})
    data['options'][key] = {'label': meta['label'], 'entries': keep}

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
.q b{font-family:Inter,system-ui,sans-serif}
table.sc{border-collapse:collapse;font:14px/1.4 Inter,system-ui,sans-serif;margin:8px 0}table.sc th,table.sc td{border-bottom:1px solid var(--line);padding:6px 10px;text-align:left}
table.sc td.n{text-align:right;font-variant-numeric:tabular-nums}
.bars{display:flex;gap:18px;overflow-x:auto;padding-bottom:8px}
.col{flex:0 0 auto}.col h3{font:600 13px/1.3 Inter,system-ui,sans-serif;margin:0 0 6px;color:var(--soft);text-transform:uppercase;letter-spacing:.05em}
.menu{width:max-content;max-height:620px;overflow-y:auto;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:8px;box-shadow:0 2px 10px rgba(0,0,0,.06)}
.menu .ct{font:500 11px/20px Inter,system-ui,sans-serif;text-transform:uppercase;padding:4px;color:var(--ink)}
.row{padding:4px}.lab{display:block;box-sizing:border-box;width:217px;font:400 15px/20px Inter,system-ui,sans-serif;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:var(--soft)}
.l1 .lab{color:var(--ink)}.l2 .lab{padding-left:12px}.l3 .lab{padding-left:24px}.l4 .lab{padding-left:36px}
.row.changed .lab{color:var(--accent)}.row.hl{background:rgba(154,74,31,.12);border-radius:4px}
.legend{font:13px/1.4 Inter,system-ui,sans-serif;color:var(--soft);margin:6px 0 0}
.tools{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
button{font:500 14px/1 Inter,system-ui,sans-serif;padding:9px 12px;border-radius:7px;border:1px solid var(--line);background:var(--card);color:var(--ink);cursor:pointer}
button.pri{background:var(--accent);border-color:var(--accent);color:#fff}button:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.part{margin:22px 0 6px;font:600 15px/1.3 Inter,system-ui,sans-serif}
.item{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 12px;margin:6px 0}
.item .top{display:flex;gap:10px;align-items:baseline;font:13px/1.4 Inter,system-ui,sans-serif;color:var(--faint)}
.item .why{font:13px/1.45 Inter,system-ui,sans-serif;color:var(--soft);margin:4px 0 6px}
.ch{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:6px}
.ch label{display:flex;gap:8px;align-items:flex-start;border:1px solid var(--line);border-radius:6px;padding:7px 8px;cursor:pointer;font:15px/1.35 Inter,system-ui,sans-serif}
.ch label.sel{border-color:var(--accent);box-shadow:inset 0 0 0 1px var(--accent)}
.ch small{display:block;font-size:12px;color:var(--faint)}
.st{font:600 11px/1 Inter,system-ui,sans-serif;padding:2px 6px;border-radius:9px;border:1px solid currentColor;white-space:nowrap}
.st.fits{color:var(--ok)}.st.tight{color:var(--warn)}.st.cut{color:var(--bad)}
input[type=text],textarea{width:100%;font:15px/1.4 Inter,system-ui,sans-serif;padding:7px 8px;border:1px solid var(--line);border-radius:6px;background:var(--paper);color:var(--ink)}
textarea{min-height:70px}.saved{font:13px/1.4 Inter,system-ui,sans-serif;color:var(--faint)}
ul.pt{font:14px/1.5 Inter,system-ui,sans-serif;color:var(--soft)}
.flt{font:14px/1.3 Inter,system-ui,sans-serif;color:var(--soft);display:flex;gap:6px;align-items:center;padding:6px 4px}
.kind{font:600 11px/1 Inter,system-ui,sans-serif;padding:2px 6px;border-radius:9px;background:rgba(154,74,31,.12);color:var(--accent);white-space:nowrap}
.sticky{position:sticky;top:0;background:var(--paper);padding:8px 0;z-index:2;border-bottom:1px solid var(--line)}
</style></head><body><main>
<h1>__TITLE__</h1>
<p class="sub">Inner Child Self-Love Reparenting Guide · the contents as Substack's narrow sidebar shows it · __DATE__</p>
<div class="q" id="question"></div>
<h2>What fresh readers found</h2><div id="scores"></div>
<h2>The options, as the sidebar shows them</h2>
<p class="legend">Each list is drawn at the sidebar's width with the font it used on your laptop (Inter, 15px), so the "…" falls where it falls for you. Headings that differ from yours are in colour. The last list follows your picks below as you make them. On a phone, swipe sideways to see the other lists.</p>
<div class="bars" id="bars"></div>
<h2>Your pick, heading by heading</h2>
<div class="sticky"><div class="tools">
<button type="button" class="pri" data-all="fable">Take all of Fable's</button>
<button type="button" data-all="pick">Take all of Opus's</button>
<button type="button" data-all="C">Take all of GPT's</button>
<button type="button" data-all="now">Keep all as they are</button>
<button type="button" id="copy">Copy my answers</button>
<label class="flt"><input type="checkbox" id="onlydiff"> Only where Fable and Opus differ</label>
<span class="saved" id="saved" aria-live="polite"></span></div></div>
<div id="items"></div>
<h2>Anything else</h2><textarea id="comment" placeholder="Your comment for the next turn"></textarea>
<h2>Words in the text that name a heading</h2><ul class="pt" id="pointers"></ul>
<p class="legend" id="gitnote"></p>
</main>
<script>
const D = __DATA__;
const KEYS = Object.keys(D.options);
const byId = {}; D.now.forEach(e => byId[e.id] = {now: e});
KEYS.forEach(k => D.options[k].entries.forEach(e => (byId[e.id] = byId[e.id] || {})[k] = e));
const STORE_KEY = 'inner-child-toc-t130';
let ans = {picks: {}, own: {}, comment: ''};
try { const s = localStorage.getItem(STORE_KEY); if (s) ans = Object.assign(ans, JSON.parse(s)); } catch (e) {}
let db = null, doc = null;
const cv = document.createElement('canvas').getContext('2d');
function measure(t){ cv.font = '400 15px Inter'; return cv.measureText(t).width; }
function status(t, lvl){ const room = D.room[lvl], w = measure(t); return w > room + .01 ? 'cut' : (room - w < 12 ? 'tight' : 'fits'); }
function esc(s){ return String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }
function pickOf(id){ return ans.picks[id] || D.pick[id] || 'now'; }
function choice(id){ const p = pickOf(id); if (p === 'own') return (ans.own[id] || byId[id].now.heading); return (byId[id][p] || byId[id].now).heading; }
function levelOf(id){ const p = pickOf(id); return ((p !== 'own' && byId[id][p]) || byId[id].now).level; }
function addedOn(a){ return (ans.picks[a.id] || 'add') === 'add'; }
function differs(id){ const f = byId[id].fable, o = byId[id].pick; return !!(f && o && (f.heading !== o.heading || f.level !== o.level)); }
const KIND = {'yours-short': 'your words, shortened', 'kept-whole': 'left whole on purpose', 'new-words': 'not your words', 'added-heading': 'a heading to add'};
function menu(title, entries, changedFrom){
  const rows = entries.map(e => `<div class="row l${e.level}${changedFrom && changedFrom[e.id] !== e.heading ? ' changed' : ''}" data-id="${e.id}"><div class="lab">${esc(e.heading)}</div></div>`).join('');
  return `<div class="col"><h3>${esc(title)}</h3><div class="menu"><div class="ct">Contents</div>${rows}</div></div>`;
}
function drawBars(){
  const nowMap = {}; D.now.forEach(e => nowMap[e.id] = e.heading);
  let h = menu('Yours, as it is', D.now, null);
  const withAdded = (entries, key, on) => { const out = []; entries.forEach(e => { out.push(e); D.added.forEach(a => { if (a.after === e.id && (key ? a.option === key : on(a))) out.push({id: a.id, level: a.level, heading: a.heading}); }); }); return out; };
  KEYS.filter(k => !D.hide.includes(k)).forEach(k => h += menu(D.options[k].label, withAdded(D.options[k].entries, k), nowMap));
  const mine = withAdded(D.now.map(e => ({id: e.id, level: levelOf(e.id), heading: choice(e.id)})), null, addedOn);
  h += menu('Your picks', mine, nowMap);
  document.getElementById('bars').innerHTML = h;
  document.querySelectorAll('.menu').forEach(m => m.addEventListener('scroll', () => { const t = m.scrollTop; document.querySelectorAll('.menu').forEach(o => { if (o !== m && Math.abs(o.scrollTop - t) > 2) o.scrollTop = t; }); }));
}
let onlyDiff = false;
function addedItems(list){
  return list.map(a => { const on = addedOn(a);
    return `<div class="item" id="i-${a.id}"><div class="top"><span>${a.id}</span><span>${'#'.repeat(a.level)}</span><span class="kind">Fable: ${KIND['added-heading']}</span></div><div class="why">${a.why}</div><div class="ch">` +
      `<label class="${on ? 'sel' : ''}"><input type="radio" name="p-${a.id}" value="add" ${on ? 'checked' : ''}><span>${esc(a.heading)}<small>Add this heading · <span class="st ${status(a.heading, a.level)}">${status(a.heading, a.level)}</span></small></span></label>` +
      `<label class="${on ? '' : 'sel'}"><input type="radio" name="p-${a.id}" value="no" ${on ? '' : 'checked'}><span>Don’t add it<small>The post keeps the headings it has</small></span></label></div></div>`; }).join('');
}
function drawItems(){
  let h = '', part = '';
  D.now.forEach(e => {
    const opts = [['now', 'As it is']].concat(KEYS.map(k => [k, D.options[k].label]));
    const texts = opts.map(([k]) => (byId[e.id][k] || e).heading);
    if (e.level === 1) h += `<div class="part">${esc(e.heading)}</div>`;
    const levels = opts.map(([k]) => (byId[e.id][k] || e).level);
    const addedHere = D.added.filter(a => a.after === e.id);
    if (onlyDiff && !differs(e.id) && !addedHere.length) return;
    if (texts.every(t => t === texts[0]) && levels.every(l => l === levels[0])) { h += addedItems(addedHere); return; }
    const cur = ans.picks[e.id] || D.pick[e.id] || 'now';
    const groups = [];
    opts.forEach(([k, lab]) => {
      const t = (byId[e.id][k] || e).heading, lvl = (byId[e.id][k] || e).level;
      const g = groups.find(x => x.t === t && x.lvl === lvl);
      if (g) { g.keys.push(k); g.labs.push(lab); } else groups.push({t, lvl, keys: [k], labs: [lab]});
    });
    let labels = '';
    groups.forEach(g => {
      const k = g.keys.includes(cur) ? cur : g.keys[0];
      const on = g.keys.includes(cur);
      const lv = g.lvl !== e.level ? ' · as ' + '#'.repeat(g.lvl) : '';
      labels += `<label class="${on ? 'sel' : ''}"><input type="radio" name="p-${e.id}" value="${k}" ${on ? 'checked' : ''}><span>${esc(g.t)}<small>${esc(g.labs.join(' · '))}${lv} · <span class="st ${status(g.t, g.lvl)}">${status(g.t, g.lvl)}</span></small></span></label>`;
    });
    // mark labels shared by several options
    labels += `<label class="${cur === 'own' ? 'sel' : ''}"><input type="radio" name="p-${e.id}" value="own" ${cur === 'own' ? 'checked' : ''}><span style="flex:1">Your own words<input type="text" data-own="${e.id}" value="${esc(ans.own[e.id] || '')}" placeholder="${esc(e.heading)}"></span></label>`;
    const note = D.notes[e.id] ? `<div class="why">${D.notes[e.id]}</div>` : '';
    const kind = D.kinds[e.id] ? `<span class="kind">Fable: ${KIND[D.kinds[e.id]] || D.kinds[e.id]}</span>` : '';
    h += `<div class="item" id="i-${e.id}"><div class="top"><span>${e.id}</span><span>${'#'.repeat(e.level)}</span><span>${e.words} words</span>${kind}</div>${note}<div class="ch">${labels}</div></div>`;
    h += addedItems(addedHere);
  });
  document.getElementById('items').innerHTML = h;
}
function save(){
  try { localStorage.setItem(STORE_KEY, JSON.stringify(ans)); } catch (e) {}
  const s = document.getElementById('saved');
  if (doc) { doc.set(Object.assign({updated: new Date().toISOString()}, ans)).then(() => s.textContent = 'Saved').catch(() => s.textContent = 'Saved in this browser only'); }
  else s.textContent = 'Saved in this browser';
}
document.addEventListener('change', ev => {
  const t = ev.target;
  if (t.type === 'radio' && t.name.startsWith('p-')) { ans.picks[t.name.slice(2)] = t.value; save(); drawItemsKeepScroll(); drawBars(); }
});
document.addEventListener('input', ev => {
  const t = ev.target;
  if (t.dataset && t.dataset.own) { ans.own[t.dataset.own] = t.value; ans.picks[t.dataset.own] = 'own'; save(); drawBars(); }
  if (t.id === 'comment') { ans.comment = t.value; save(); }
});
function drawItemsKeepScroll(){ const y = window.scrollY; drawItems(); window.scrollTo(0, y); }
document.querySelectorAll('[data-all]').forEach(b => b.addEventListener('click', () => {
  const k = b.dataset.all; D.now.forEach(e => { ans.picks[e.id] = k; }); D.added.forEach(a => { ans.picks[a.id] = (k === a.option) ? 'add' : 'no'; }); save(); drawItemsKeepScroll(); drawBars();
}));
document.getElementById('copy').addEventListener('click', async () => {
  const out = JSON.stringify({page: STORE_KEY, saved: new Date().toISOString(), headings: Object.fromEntries(D.now.map(e => [e.id, choice(e.id)])), levels: Object.fromEntries(D.now.filter(e => levelOf(e.id) !== e.level).map(e => [e.id, levelOf(e.id)])), added: D.added.filter(addedOn).map(a => ({id: a.id, after: a.after, level: a.level, heading: a.heading})), picks: ans.picks, own: ans.own, comment: ans.comment}, null, 1);
  try { await navigator.clipboard.writeText(out); document.getElementById('saved').textContent = 'Copied: paste it into the chat'; }
  catch (e) { const ta = document.getElementById('comment'); ta.value = out; ta.select(); document.getElementById('saved').textContent = 'Copy the text in the box below'; }
});
document.getElementById('onlydiff').addEventListener('change', ev => { onlyDiff = ev.target.checked; drawItemsKeepScroll(); });
document.getElementById('question').innerHTML = D.scores.question;
document.getElementById('scores').innerHTML = D.scores.table;
document.getElementById('pointers').innerHTML = D.pointers.map(p => `<li>${p}</li>`).join('');
document.getElementById('gitnote').innerHTML = D.scores.git;
document.getElementById('comment').value = ans.comment || '';
function draw(){ drawBars(); drawItems(); }
draw();
if (document.fonts && document.fonts.ready) document.fonts.ready.then(draw);
(async () => {
  try {
    if (!window.claude || !window.claude.use) return;
    db = await window.claude.use('db'); if (!db) return;
    doc = db.doc('answers/joel');
    const timer = setTimeout(() => {}, 10000);
    const snap = await doc.get(); clearTimeout(timer);
    const v = snap && (snap.data ? snap.data() : snap);
    if (v && v.picks) { ans = Object.assign(ans, {picks: v.picks, own: v.own || {}, comment: v.comment || ''}); document.getElementById('comment').value = ans.comment; draw(); document.getElementById('saved').textContent = 'Your answers are back'; }
  } catch (e) { doc = null; }
})();
</script></body></html>"""
title = OPTS['title']
out = T.replace('__TITLE__', html.escape(title)).replace('__DATE__', html.escape(OPTS['date'])).replace('__DATA__', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))
open(sys.argv[1], 'w').write(out)
print('page', len(out))
