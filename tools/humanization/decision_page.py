#!/usr/bin/env python3
"""decision_page.py - an interactive review page for Joel: many independently actionable proposals, each with Approve,
Revise, Reject and Pending and a note, built from one items file (2026-10-25).

UDA's patterns/owner-questions-page.md ("Minimum review-page behavior"): a list of many independently actionable
proposals goes to the owner as an interactive page in the same turn, never a static page answered by numbers, with
Approve / Revise / Reject / Pending and an editable note per item (nothing is approved by silence; notes on Pending items
are kept), search, filters, progress, JSON export with the review's identity and import of a compatible export, and
explicit text colors in every field in light and dark. The project's review interface
(project-sources/review_interface_template.html.txt) is a diff view with Keep / Remove / Brainstorm per passage; this page
is for proposals (a cut, a point of view the author has to supply, a reshaped section), and it embeds the same tested
field colors, project-sources/review-form-controls.css, word for word.

  python3 tools/humanization/decision_page.py SPEC.json OUT.html [--artifact]

SPEC.json:
  {"review_id": "...", "title": "...", "source_sha256": "<the article's SHA-256>", "source_name": "...",
   "repo_file": "<a link to this page's file in Git>", "intro": ["paragraph", ...],
   "groups": [{"id": "pov", "title": "...", "intro": "...", "approve": "what Approve does here",
               "reject": "what Reject does here"}, ...],
   "items": [{"id": "P1", "group": "pov", "title": "...", "section": "...", "whose": "...",
              "blocks": [{"label": "Before", "paras": [[["text", ""], ["marked", "mark"], ["struck", "del"]], ...]},
                         {"label": "Now", "paras": [...]}],
              "fields": [{"label": "...", "text": "..."} or {"label": "...", "list": ["...", ...]}],
              "links": [{"text": "...", "url": "https://..."}], "approve": "...", "reject": "..."}]}
A passage is a list of [text, mark] pieces, mark "" (plain), "mark" (the span in question), "del" (cut) or "ins" (added).
Two blocks are shown side by side on a wide screen and one above the other on a phone. An item's own "approve" and
"reject" override its group's.

The page is one self-contained HTML file: no network, decisions kept in the browser (localStorage, wrapped in try/catch)
and in the JSON the owner copies or downloads. Downloads work when the file is opened from disk; inside a hosted viewer
that blocks them, Copy JSON and the JSON box still work. An import is refused unless its review_id and source_sha256 are
this page's, and ids it doesn't know are reported, never guessed.
"""
import argparse
import html
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]
CONTROLS = REPO / 'project-sources' / 'review-form-controls.css'
FORMAT = 'joel-review-decisions-v1'
MARKS = {'', 'mark', 'del', 'ins'}

CSS = r'''
/* An editor's review sheet: article passages set like page proofs (a book face), controls in a plain sans, one blue
   accent for actions, and the four decisions in their own colors. */
:root {
  --bg: #f4f6f9; --surface: #ffffff; --ink: #1d2430; --muted: #566072; --line: #d8dee7; --soft: #eef2f7;
  --accent: #2b4c9b; --accent-ink: #ffffff; --mark: #fff0b8; --mark-ink: #1d2430; --del: #fde4e4; --del-ink: #8a2c2c;
  --ins: #dff3e6; --ins-ink: #1f5b38; --ok: #1f7a4d; --rev: #8a5d00; --no: #a33a3a; --wait: #5d6675;
  --ok-bg: #e3f4ea; --rev-bg: #fbf0d9; --no-bg: #fbe5e5; --wait-bg: #eceff4;
  --serif: "Source Serif 4", "Source Serif Pro", Georgia, "Times New Roman", serif;
  --sans: "IBM Plex Sans", "Segoe UI", system-ui, -apple-system, Arial, sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #12161d; --surface: #1a2029; --ink: #e6eaf1; --muted: #a3adbd; --line: #2e3744; --soft: #222a35;
  --accent: #8fb0ff; --accent-ink: #0f1420; --mark: #5a4b12; --mark-ink: #fff6d6; --del: #4d2222; --del-ink: #ffd2d2;
  --ins: #1d3d2a; --ins-ink: #c9f2d8; --ok: #6fd39d; --rev: #f0c35c; --no: #ff9a9a; --wait: #b2bccb;
  --ok-bg: #173826; --rev-bg: #3d3112; --no-bg: #3f1d1d; --wait-bg: #262e3a; color-scheme: dark } }
:root[data-theme="dark"] {
  --bg: #12161d; --surface: #1a2029; --ink: #e6eaf1; --muted: #a3adbd; --line: #2e3744; --soft: #222a35;
  --accent: #8fb0ff; --accent-ink: #0f1420; --mark: #5a4b12; --mark-ink: #fff6d6; --del: #4d2222; --del-ink: #ffd2d2;
  --ins: #1d3d2a; --ins-ink: #c9f2d8; --ok: #6fd39d; --rev: #f0c35c; --no: #ff9a9a; --wait: #b2bccb;
  --ok-bg: #173826; --rev-bg: #3d3112; --no-bg: #3f1d1d; --wait-bg: #262e3a; color-scheme: dark }
* { box-sizing: border-box }
body { margin: 0; background: var(--bg); color: var(--ink); font: 15px/1.55 var(--sans) }
.wrap { max-width: 1120px; margin: 0 auto; padding-block: 20px 72px;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)) }
h1 { font: 600 clamp(1.5rem, 3.2vw, 2.1rem)/1.2 var(--sans); margin: 4px 0 10px; text-wrap: balance }
h2 { font: 600 1.15rem/1.3 var(--sans); margin: 34px 0 6px; text-wrap: balance }
h3 { font: 600 1.02rem/1.35 var(--sans); margin: 0; text-wrap: balance }
.eyebrow { font: 600 12px/1.4 var(--sans); letter-spacing: .08em; text-transform: uppercase; color: var(--accent) }
.intro p, .group-intro { max-width: 72ch; color: var(--ink) }
.group-intro { color: var(--muted); margin: 0 0 12px }
a { color: var(--accent) }
.bar { position: sticky; top: env(safe-area-inset-top, 0px); z-index: 5; background: var(--bg); border-bottom: 1px solid var(--line);
  padding-block: 10px; display: flex; flex-wrap: wrap; gap: 8px; align-items: center }
body::before { content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 10; background: var(--bg) }
.bar input[type=search] { flex: 1 1 220px; min-width: 0; border: 1px solid var(--line); border-radius: 6px; padding: 8px 10px }
.bar select { border: 1px solid var(--line); border-radius: 6px; padding: 7px 8px; max-width: 100% }
button { font: inherit; cursor: pointer; border-radius: 6px; border: 1px solid var(--line); background: var(--surface); color: var(--ink); padding: 7px 12px }
button:focus-visible, a:focus-visible { outline: 3px solid var(--accent); outline-offset: 2px }
button.primary { background: var(--accent); color: var(--accent-ink); border-color: var(--accent) }
.progress { display: flex; flex-wrap: wrap; gap: 6px 14px; align-items: center; margin: 14px 0 4px; font-variant-numeric: tabular-nums; color: var(--muted) }
.meter { flex: 1 1 200px; height: 8px; background: var(--soft); border-radius: 6px; overflow: hidden; min-width: 120px }
.meter span { display: block; height: 100%; width: 0; background: var(--accent) }
#counts { display: flex; flex-wrap: wrap; gap: 4px 12px }
.count b { color: var(--ink) }
.card { background: var(--surface); border: 1px solid var(--line); border-radius: 8px; margin: 12px 0; padding: 14px 16px; display: grid; gap: 10px }
.card[data-status=approved] { border-left: 5px solid var(--ok) }
.card[data-status=needs_revision] { border-left: 5px solid var(--rev) }
.card[data-status=rejected] { border-left: 5px solid var(--no) }
.card-top { display: flex; flex-wrap: wrap; gap: 6px 10px; align-items: baseline }
.cid { font: 600 12px/1 var(--mono); color: var(--muted) }
.sec { color: var(--muted); font-size: 13px }
.whose { font-size: 13px; color: var(--muted) }
.pill { font: 600 12px/1 var(--sans); padding: 4px 8px; border-radius: 999px; background: var(--wait-bg); color: var(--wait) }
.pill.approved { background: var(--ok-bg); color: var(--ok) } .pill.needs_revision { background: var(--rev-bg); color: var(--rev) }
.pill.rejected { background: var(--no-bg); color: var(--no) }
.blocks { display: grid; gap: 12px; grid-template-columns: repeat(auto-fit, minmax(min(100%, 420px), 1fr)) }
.block { min-width: 0; border: 1px solid var(--line); border-radius: 6px; padding: 10px 12px; background: var(--soft) }
.block-label { font: 600 12px/1.3 var(--sans); letter-spacing: .06em; text-transform: uppercase; color: var(--muted); margin-bottom: 4px }
.passage { font: 16px/1.6 var(--serif); margin: 6px 0; overflow-wrap: anywhere }
.passage mark { background: var(--mark); color: var(--mark-ink); padding: 0 2px; border-radius: 2px }
.passage del { background: var(--del); color: var(--del-ink) }
.passage ins { background: var(--ins); color: var(--ins-ink); text-decoration: none }
.field { margin: 0 }
.field dt { font: 600 13px/1.4 var(--sans); color: var(--muted) }
.field dd { margin: 2px 0 0 0; max-width: 80ch; overflow-wrap: anywhere }
.field ul { margin: 2px 0 0; padding-left: 20px } .field li { margin: 3px 0 }
.label-chip { font: 600 11px/1 var(--mono); padding: 3px 5px; border-radius: 4px; background: var(--soft); color: var(--accent); margin-right: 4px; white-space: nowrap }
.decide { display: grid; gap: 8px; border-top: 1px solid var(--line); padding-top: 10px }
.means { font-size: 13px; color: var(--muted); max-width: 90ch }
.choices { display: flex; flex-wrap: wrap; gap: 6px }
.choices button[aria-pressed=true][data-d=approved] { background: var(--ok); color: var(--surface); border-color: var(--ok) }
.choices button[aria-pressed=true][data-d=needs_revision] { background: var(--rev); color: var(--surface); border-color: var(--rev) }
.choices button[aria-pressed=true][data-d=rejected] { background: var(--no); color: var(--surface); border-color: var(--no) }
.choices button[aria-pressed=true][data-d=pending] { background: var(--wait); color: var(--surface); border-color: var(--wait) }
textarea { width: 100%; min-height: 64px; resize: vertical; border: 1px solid var(--line); border-radius: 6px; padding: 8px 10px; font: 15px/1.5 var(--sans) }
.links { font-size: 13px; display: flex; flex-wrap: wrap; gap: 4px 14px }
.panel { background: var(--surface); border: 1px solid var(--line); border-radius: 8px; padding: 14px 16px; margin: 26px 0 0; display: grid; gap: 10px }
.panel .row { display: flex; flex-wrap: wrap; gap: 8px; align-items: center }
.status-line { font-size: 14px; color: var(--muted); min-height: 1.4em }
.status-line.bad { color: var(--no) } .status-line.good { color: var(--ok) }
.empty { color: var(--muted); font-style: italic }
.foot { color: var(--muted); font-size: 13px; margin-top: 28px; overflow-wrap: anywhere }
@media (prefers-reduced-motion: no-preference) { .meter span { transition: width .2s } }
'''

JS = r'''
'use strict';
const src = JSON.parse(document.getElementById('review-data').textContent);
const KEY = 'review-' + src.review_id + '-' + src.source_sha256.slice(0, 12);
const LABEL = {pending: 'Pending', approved: 'Approved', needs_revision: 'Revise', rejected: 'Rejected'};
const BUTTON = {approved: 'Approve', needs_revision: 'Revise', rejected: 'Reject', pending: 'Pending'};
const groups = new Map(src.groups.map(g => [g.id, g]));
const ids = new Set(src.items.map(x => x.id));
let state = {decisions: {}};
try { const old = JSON.parse(localStorage.getItem(KEY) || 'null'); if (old && old.source_sha256 === src.source_sha256 && old.decisions) state.decisions = old.decisions; } catch (e) {}
const $ = s => document.querySelector(s);
function el(tag, cls, text) { const n = document.createElement(tag); if (cls) n.className = cls; if (text !== undefined) n.textContent = text; return n; }
function rec(id) { return state.decisions[id] || {status: 'pending', note: ''}; }
function save() { try { localStorage.setItem(KEY, JSON.stringify({source_sha256: src.source_sha256, decisions: state.decisions})); } catch (e) {} refresh(); }
function setDecision(id, status) { const r = rec(id); state.decisions[id] = {status: status, note: r.note || '', updated: new Date().toISOString()}; save(); }
function setNote(id, note) { const r = rec(id); state.decisions[id] = {status: r.status || 'pending', note: note, updated: new Date().toISOString()}; save(); }
function passage(pieces) {
  const p = el('p', 'passage');
  for (const [text, mark] of pieces) { if (!mark) p.append(document.createTextNode(text)); else p.append(el(mark, '', text)); }
  return p;
}
function card(item) {
  const g = groups.get(item.group) || {};
  const c = el('article', 'card'); c.id = 'item-' + item.id; c.dataset.id = item.id; c.dataset.group = item.group;
  const top = el('div', 'card-top');
  top.append(el('span', 'cid', item.id), el('h3', '', item.title), el('span', 'pill', 'Pending'));
  c.append(top);
  if (item.section) c.append(el('div', 'sec', item.section));
  if (item.whose) c.append(el('div', 'whose', 'Whose words: ' + item.whose));
  if (item.blocks && item.blocks.length) {
    const bs = el('div', 'blocks');
    for (const b of item.blocks) { const d = el('div', 'block'); d.append(el('div', 'block-label', b.label)); for (const p of b.paras) d.append(passage(p)); bs.append(d); }
    c.append(bs);
  }
  if (item.fields && item.fields.length) {
    const dl = el('dl', 'field');
    for (const f of item.fields) {
      dl.append(el('dt', '', f.label));
      const dd = el('dd');
      if (f.list) { const ul = el('ul'); for (const x of f.list) { const li = el('li'); const m = x.match(/^(SOURCE-SUPPORTED|ARTICLE-HINTED|NEW OWNER CHOICE)\s*:?\s*/); if (m) { li.append(el('span', 'label-chip', m[1]), document.createTextNode(x.slice(m[0].length))); } else li.textContent = x; ul.append(li); } dd.append(ul); }
      else dd.textContent = f.text;
      dl.append(dd);
    }
    c.append(dl);
  }
  if (item.links && item.links.length) { const l = el('div', 'links'); for (const k of item.links) { const a = el('a', '', k.text); a.href = k.url; a.target = '_blank'; a.rel = 'noopener'; l.append(a); } c.append(l); }
  const dec = el('div', 'decide');
  dec.append(el('div', 'means', 'Approve: ' + (item.approve || g.approve || 'do what is proposed.') + ' Reject: ' + (item.reject || g.reject || 'leave it as it is.') + ' Revise: change it the way your note says.'));
  const ch = el('div', 'choices'); ch.setAttribute('role', 'group'); ch.setAttribute('aria-label', 'Decision for ' + item.id);
  for (const d of ['approved', 'needs_revision', 'rejected', 'pending']) {
    const b = el('button', '', BUTTON[d]); b.type = 'button'; b.dataset.d = d; b.id = 'd-' + item.id + '-' + d;
    b.addEventListener('click', () => { setDecision(item.id, d); if (d === 'needs_revision') ta.focus(); });
    ch.append(b);
  }
  const ta = el('textarea'); ta.id = 'note-' + item.id; ta.setAttribute('aria-label', 'Your note on ' + item.id);
  ta.placeholder = 'Your note (kept with any decision, Pending included)';
  ta.value = rec(item.id).note || '';
  ta.addEventListener('input', () => setNote(item.id, ta.value));
  dec.append(ch, ta); c.append(dec);
  return c;
}
function render() {
  const main = $('#items'); main.textContent = '';
  for (const g of src.groups) {
    const items = src.items.filter(x => x.group === g.id);
    if (!items.length) continue;
    const sec = el('section', 'group'); sec.dataset.group = g.id;
    sec.append(el('h2', '', g.title + ' (' + items.length + ')'));
    if (g.intro) sec.append(el('p', 'group-intro', g.intro));
    for (const it of items) sec.append(card(it));
    main.append(sec);
  }
  const gs = $('#fgroup'); for (const g of src.groups) { const o = el('option', '', g.title); o.value = g.id; gs.append(o); }
}
function matches(item, q) {
  if (!q) return true;
  const hay = [item.id, item.title, item.section, item.whose, rec(item.id).note].concat((item.fields || []).map(f => f.text || (f.list || []).join(' ')))
    .concat((item.blocks || []).flatMap(b => b.paras.map(p => p.map(x => x[0]).join('')))).join(' ').toLowerCase();
  return q.toLowerCase().split(/\s+/).every(w => hay.includes(w));
}
function refresh() {
  const q = $('#search').value.trim(), fg = $('#fgroup').value, fs = $('#fstatus').value, fn = $('#fnote').checked;
  const counts = {pending: 0, approved: 0, needs_revision: 0, rejected: 0};
  let shown = 0;
  for (const item of src.items) {
    const r = rec(item.id), c = document.getElementById('item-' + item.id);
    counts[r.status] = (counts[r.status] || 0) + 1;
    c.dataset.status = r.status;
    const pill = c.querySelector('.pill'); pill.textContent = LABEL[r.status]; pill.className = 'pill ' + r.status;
    for (const b of c.querySelectorAll('.choices button')) b.setAttribute('aria-pressed', String(b.dataset.d === r.status));
    const ok = matches(item, q) && (!fg || item.group === fg) && (!fs || r.status === fs) && (!fn || (r.note || '').trim());
    c.hidden = !ok; if (ok) shown++;
  }
  for (const s of document.querySelectorAll('section.group')) s.hidden = ![...s.querySelectorAll('.card')].some(c => !c.hidden);
  const total = src.items.length, done = total - counts.pending;
  $('#meter').style.width = (100 * done / total).toFixed(1) + '%';
  $('#counts').innerHTML = '';
  for (const [k, v] of [['approved', counts.approved], ['needs_revision', counts.needs_revision], ['rejected', counts.rejected], ['pending', counts.pending]]) {
    const s = el('span', 'count'); const b = el('b', '', String(v)); s.append(b, document.createTextNode(' ' + LABEL[k])); $('#counts').append(s);
  }
  $('#shown').textContent = shown === total ? 'Showing all ' + total : 'Showing ' + shown + ' of ' + total;
  $('#none').hidden = shown !== 0;
}
function exportData() {
  const items = src.items.map(x => { const r = rec(x.id); return {id: x.id, group: x.group, title: x.title, status: r.status, note: r.note || '', updated: r.updated || null}; });
  const counts = {}; for (const i of items) counts[i.status] = (counts[i.status] || 0) + 1;
  return {format: src.format, review_id: src.review_id, title: src.title, source_name: src.source_name, source_sha256: src.source_sha256,
          exported_utc: new Date().toISOString(), counts: counts, items: items};
}
function say(msg, kind) { const s = $('#statusLine'); s.textContent = msg; s.className = 'status-line' + (kind ? ' ' + kind : ''); }
async function copyJson() {
  const text = JSON.stringify(exportData(), null, 1); $('#jsonBox').value = text; $('#jsonBox').hidden = false;
  try { await navigator.clipboard.writeText(text); say('Copied. Paste it into the chat.', 'good'); }
  catch (e) { $('#jsonBox').focus(); $('#jsonBox').select(); say('Copying was refused here, so the JSON is selected in the box below: copy it from there.', 'bad'); }
}
function showJson() { const b = $('#jsonBox'); b.value = JSON.stringify(exportData(), null, 1); b.hidden = false; b.focus(); b.select(); say('The JSON is in the box below, selected.'); }
function downloadJson() {
  const text = JSON.stringify(exportData(), null, 1);
  try { const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([text], {type: 'application/json'}));
        a.download = src.review_id + '-decisions.json'; document.body.append(a); a.click(); a.remove();
        say('If no file appeared (some viewers block downloads), use Copy JSON instead.'); }
  catch (e) { say('Downloading isn\'t allowed here: use Copy JSON instead.', 'bad'); }
}
function importText(text) {
  let d; try { d = JSON.parse(text); } catch (e) { say('That isn\'t JSON this page can read: ' + e.message, 'bad'); return; }
  if (!d || d.review_id !== src.review_id || d.source_sha256 !== src.source_sha256) { say('Not imported: that export is for another review or another version of the article (its review_id or source_sha256 differs).', 'bad'); return; }
  const unknown = [], next = {};
  for (const it of d.items || []) {
    if (!ids.has(it.id)) { unknown.push(it.id); continue; }
    const st = ['pending', 'approved', 'needs_revision', 'rejected'].includes(it.status) ? it.status : 'pending';
    next[it.id] = {status: st, note: it.note || '', updated: it.updated || null};
  }
  state.decisions = Object.assign({}, state.decisions, next);
  for (const item of src.items) { const t = document.getElementById('note-' + item.id); if (t) t.value = rec(item.id).note || ''; }
  save(); say('Imported ' + Object.keys(next).length + ' decisions' + (unknown.length ? '; not on this page, so left out: ' + unknown.join(', ') : '') + '.', unknown.length ? 'bad' : 'good');
}
let clearArmed = false;
function clearAll() {
  if (!clearArmed) { clearArmed = true; $('#clearAll').textContent = 'Click again to clear every decision and note'; setTimeout(() => { clearArmed = false; $('#clearAll').textContent = 'Clear all'; }, 5000); return; }
  clearArmed = false; $('#clearAll').textContent = 'Clear all'; state.decisions = {};
  for (const t of document.querySelectorAll('.decide textarea')) t.value = '';
  save(); say('Cleared.');
}
function nextUndecided() {
  const n = src.items.find(x => rec(x.id).status === 'pending' && !document.getElementById('item-' + x.id).hidden) || src.items.find(x => rec(x.id).status === 'pending');
  if (!n) { say('Nothing is pending.', 'good'); return; }
  const c = document.getElementById('item-' + n.id); c.hidden = false; c.scrollIntoView({block: 'start'}); c.querySelector('button').focus({preventScroll: true});
}
render();
for (const id of ['#search', '#fgroup', '#fstatus', '#fnote']) $(id).addEventListener('input', refresh);
$('#copyJson').addEventListener('click', copyJson); $('#copyJson2').addEventListener('click', copyJson);
$('#showJson').addEventListener('click', showJson); if ($('#downloadJson')) $('#downloadJson').addEventListener('click', downloadJson);
$('#clearAll').addEventListener('click', clearAll); $('#next').addEventListener('click', nextUndecided);
$('#importText').addEventListener('click', () => importText($('#importBox').value));
$('#importFile').addEventListener('change', e => { const f = e.target.files && e.target.files[0]; if (!f) return; const r = new FileReader(); r.onload = () => importText(String(r.result)); r.readAsText(f); });
refresh();
'''


def check_spec(spec):
    for k in ('review_id', 'title', 'source_sha256', 'groups', 'items'):
        if k not in spec:
            raise SystemExit('the spec has no %r' % k)
    if not re.fullmatch(r'[0-9a-f]{64}', spec['source_sha256']):
        raise SystemExit('source_sha256 is not a SHA-256')
    gids = [g['id'] for g in spec['groups']]
    if len(set(gids)) != len(gids):
        raise SystemExit('two groups share an id')
    seen = set()
    for it in spec['items']:
        if not it.get('id') or it['id'] in seen:
            raise SystemExit('an item has no id, or a repeated one: %r' % it.get('id'))
        seen.add(it['id'])
        if it.get('group') not in gids:
            raise SystemExit('%s: its group %r is not one of the groups' % (it['id'], it.get('group')))
        if not it.get('title'):
            raise SystemExit('%s has no title' % it['id'])
        for b in it.get('blocks', []):
            for p in b['paras']:
                for piece in p:
                    if len(piece) != 2 or piece[1] not in MARKS:
                        raise SystemExit('%s: a passage piece must be [text, mark] with mark one of %s' % (it['id'], sorted(MARKS)))
        for k in it.get('links', []):
            if not k['url'].startswith('https://'):
                raise SystemExit('%s: links must be https: %s' % (it['id'], k['url']))


def build(spec, full=True):
    """The page's HTML for SPEC (a dict, as in the docstring): a whole document for a file (FULL), or, for a Claude
    artifact, the page's content alone, since the artifact viewer wraps it in its own document."""
    page = _content(spec)
    if not full:
        # a Claude artifact's viewer blocks any download the page starts, so that version offers Copy JSON and the box only
        btn = '<button id="downloadJson" type="button">Download JSON</button>'
        assert page.count(btn) == 1
        page = page.replace(btn, '').replace(', or download it when you have this page open as a file.', '.')
        # and no script-driven save either: the download function goes, and its listener is guarded
        i = page.index('function downloadJson() {')
        j = page.index('function importText(text) {', i)
        page = page[:i] + page[j:]
        assert 'createObjectURL' not in page and '.download =' not in page
        return page
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n</head>\n<body>\n'
            + page + '</body>\n</html>\n')


def _content(spec):
    check_spec(spec)
    data = dict(spec, format=FORMAT)
    blob = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
    controls = CONTROLS.read_text(encoding='utf-8')
    intro = ''.join('<p>%s</p>' % linkify(p) for p in spec.get('intro', []))
    t = html.escape(spec['title'])
    return ('<title>%s</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;600&family=IBM+Plex+Sans:wght@400;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap">\n'
            '<style>%s\n%s</style>\n'
            '<div class="wrap">\n<header><div class="eyebrow">%s</div><h1>%s</h1><div class="intro">%s</div></header>\n'
            '<div class="progress"><div class="meter" aria-hidden="true"><span id="meter"></span></div><div id="counts" class="count"></div>'
            '<span id="shown"></span></div>\n'
            '<div class="bar" role="search"><input id="search" type="search" placeholder="Search the items and your notes" aria-label="Search">'
            '<select id="fgroup" aria-label="Show a group"><option value="">All groups</option></select>'
            '<select id="fstatus" aria-label="Show a status"><option value="">Any status</option><option value="pending">Pending</option>'
            '<option value="approved">Approved</option><option value="needs_revision">Revise</option><option value="rejected">Rejected</option></select>'
            '<label><input id="fnote" type="checkbox"> With a note</label>'
            '<button id="next" type="button">Next pending</button><button id="copyJson" class="primary" type="button">Copy JSON</button></div>\n'
            '<main id="items"></main><p id="none" class="empty" hidden>Nothing matches. Clear the search or the filters.</p>\n'
            '<section class="panel" aria-labelledby="send"><h2 id="send">Send your decisions back</h2>'
            '<p>Copy the JSON and paste it into the chat (from either account), or download it when you have this page open as a file. '
            'Your decisions also stay in this browser, so you can stop and come back.</p>'
            '<div class="row"><button id="copyJson2" class="primary" type="button">Copy JSON</button><button id="showJson" type="button">Show JSON</button>'
            '<button id="downloadJson" type="button">Download JSON</button><button id="clearAll" type="button">Clear all</button></div>'
            '<textarea id="jsonBox" rows="8" readonly hidden aria-label="Your decisions as JSON"></textarea>'
            '<h3>Load decisions you exported before</h3><div class="row"><input id="importFile" type="file" accept="application/json,.json" aria-label="A JSON file"></div>'
            '<textarea id="importBox" rows="4" placeholder="Or paste an export here" aria-label="Paste an export"></textarea>'
            '<div class="row"><button id="importText" type="button">Load the pasted JSON</button></div>'
            '<div id="statusLine" class="status-line" role="status"></div></section>\n'
            '<p class="foot">%s</p>\n</div>\n'
            '<script type="application/json" id="review-data">%s</script>\n<script>%s</script>\n') % (
        t, CSS, controls, html.escape(spec.get('eyebrow', 'Review')), t, intro, foot(spec), blob, JS)


def linkify(text):
    """TEXT escaped, with its [words](https://...) links made links."""
    out, pos = [], 0
    for m in re.finditer(r'\[([^\]]+)\]\((https://[^)\s]+)\)', text):
        out.append(html.escape(text[pos:m.start()]))
        out.append('<a href="%s" target="_blank" rel="noopener">%s</a>' % (html.escape(m.group(2), quote=True), html.escape(m.group(1))))
        pos = m.end()
    out.append(html.escape(text[pos:]))
    return ''.join(out)


def foot(spec):
    bits = ['Review %s' % html.escape(spec['review_id']), 'article SHA-256 %s' % spec['source_sha256'][:16] + '…']
    if spec.get('source_name'):
        bits.append('the article: ' + html.escape(spec['source_name']))
    if spec.get('repo_file'):
        bits.append('<a href="%s" target="_blank" rel="noopener">this page\'s file in Git</a>' % html.escape(spec['repo_file'], quote=True))
    return ' · '.join(bits)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('spec')
    ap.add_argument('out')
    ap.add_argument('--artifact', action='store_true', help='write the content alone, for a Claude artifact')
    a = ap.parse_args(argv)
    spec = json.loads(pathlib.Path(a.spec).read_text(encoding='utf-8'))
    page = build(spec, full=not a.artifact)
    pathlib.Path(a.out).write_text(page, encoding='utf-8')
    print('%s: %d items in %d groups, %d bytes' % (a.out, len(spec['items']), len(spec['groups']), len(page.encode('utf-8'))))
    return 0


if __name__ == '__main__':
    sys.exit(main())
