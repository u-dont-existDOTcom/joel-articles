// Behaviour test for the contents picks page's saving (lesson toc-2026-11-24c), run by tests/test_contents_picks_page.py
// when node and jsdom are there:  NODE_PATH=<dir with jsdom> node contents_picks_page_merge.cjs PAGE.html
// The page (built by the test) has S011, S015, S040, S050, S060 and S122, each starting on the proposal.
const { JSDOM, VirtualConsole } = require('jsdom');
const fs = require('fs');
(async () => {
const html = fs.readFileSync(process.argv[2], 'utf8');
const delay = ms => new Promise(r => setTimeout(r, ms));
const clone = o => JSON.parse(JSON.stringify(o));
const HIS = { picks: { S011: 'own', S015: 'own' }, own: { S011: 'Undo Accidental Affirmations', S015: "You're Better Than The Pros" }, answers: {}, comment: '' };
let fails = 0;
const ok = (name, cond, extra = '') => { if (!cond) fails++; console.log((cond ? 'ok   ' : 'FAIL ') + name + (extra ? '  ' + extra : '')); };
function open({ storeDoc, claudeAfter = 0, noDb = false }) {
  const errs = []; const vc = new VirtualConsole(); vc.on('jsdomError', e => errs.push(String(e.message || e)));
  const store = { doc: storeDoc ? clone(storeDoc) : null, sets: 0, gets: 0 };
  const api = { use: async () => noDb ? null : ({ doc: () => ({
    get: async () => { store.gets++; await delay(15); return store.doc ? clone(store.doc) : null; },
    set: async v => { await delay(15); store.sets++; store.doc = clone(v); } }) }) };
  const dom = new JSDOM(html, { runScripts: 'dangerously', pretendToBeVisual: true, virtualConsole: vc, url: 'https://example.test/',
    beforeParse(w) { w.HTMLCanvasElement.prototype.getContext = () => ({ font: '', measureText: t => ({ width: String(t).length * 8 }) }); w.scrollTo = () => {};
      if (!claudeAfter) w.claude = api; else setTimeout(() => { w.claude = api; }, claudeAfter); } });
  const w = dom.window, d = w.document;
  const radio = (id, v) => [...d.querySelectorAll(`input[name="p-${id}"]`)].find(x => x.value === v);
  const checked = id => { const r = [...d.querySelectorAll(`input[name="p-${id}"]`)].find(x => x.checked); return r && r.value; };
  const type = (id, text) => { const inp = d.querySelector(`input[data-own="${id}"]`); inp.focus(); inp.value = text; inp.dispatchEvent(new w.Event('input', { bubbles: true })); return inp; };
  return { w, d, store, errs, radio, checked, type, status: () => d.getElementById('saved').textContent, close: () => w.close() };
}
// A. the ordinary visit: his saved answers come back, nothing is written until he changes something
{ const p = open({ storeDoc: HIS }); await delay(400);
  ok('A his answers are back', p.status() === 'Your answers are back', p.status());
  ok('A S011 shows his own words', p.checked('S011') === 'own' && p.d.querySelector('input[data-own="S011"]').value === 'Undo Accidental Affirmations');
  ok('A nothing written on opening', p.store.sets === 0, 'sets ' + p.store.sets);
  ok('A S122 starts on the proposal', p.checked('S122') === 'pick', String(p.checked('S122')));
  p.radio('S040', 'now').click(); await delay(900);
  ok('A a pick is saved with his earlier answers', p.store.doc.picks.S040 === 'now' && p.store.doc.own.S011 === 'Undo Accidental Affirmations' && p.store.doc.picks.S015 === 'own', JSON.stringify(p.store.doc.picks));
  ok('A the record carries the heading text', p.store.doc.headings.S015 === "You're Better Than The Pros" && p.store.doc.headings.S122 === 'Breathe Less (Buteyko)', p.store.doc.headings.S122);
  ok('A saved', p.status() === 'Saved', p.status()); ok('A no script errors', p.errs.length === 0, p.errs.join(' | ')); p.close(); }
// B. he types before the saved answers connect: nothing of his is lost, nothing saved is lost
{ const p = open({ storeDoc: HIS, claudeAfter: 1200 }); await delay(300);
  const inp = p.type('S122', 'Buteyko and Systema'); p.radio('S040', 'now').click();
  ok('B says where it is saved meanwhile', /in this browser/.test(p.status()), p.status());
  await delay(2200);
  ok('B his early title reached the saved answers', p.store.doc.own.S122 === 'Buteyko and Systema' && p.store.doc.picks.S122 === 'own' && p.store.doc.picks.S040 === 'now', JSON.stringify(p.store.doc.picks));
  ok('B the saved answers are still there', p.store.doc.own.S011 === 'Undo Accidental Affirmations' && p.store.doc.picks.S015 === 'own');
  ok('B the page shows both', p.checked('S122') === 'own' && p.checked('S011') === 'own' && inp.value === 'Buteyko and Systema');
  ok('B the box kept its focus', p.d.activeElement === inp); ok('B no script errors', p.errs.length === 0, p.errs.join(' | ')); p.close(); }
// C. another tab or device saved meanwhile: this one keeps those answers when it saves
{ const p = open({ storeDoc: HIS }); await delay(400);
  const t = Date.now() + 1000;
  p.store.doc.picks.S050 = 'now'; p.store.doc.own.S011 = 'Undo It'; p.store.doc.at = { 'p:S050': t, 'o:S011': t };
  p.radio('S060', 'now').click(); await delay(900);
  ok('C the other tab\'s answers survive this save', p.store.doc.picks.S050 === 'now' && p.store.doc.own.S011 === 'Undo It' && p.store.doc.picks.S060 === 'now', JSON.stringify(p.store.doc.picks));
  ok('C and show on this page', p.checked('S050') === 'now' && p.d.querySelector('input[data-own="S011"]').value === 'Undo It');
  p.close(); }
// D. an older change here never overwrites a newer one made elsewhere
{ const p = open({ storeDoc: HIS }); await delay(400);
  p.type('S122', 'Old Title'); await delay(900);
  p.store.doc.own.S122 = 'Newer Title'; p.store.doc.at['o:S122'] = Date.now() + 5000; p.store.doc.at['p:S122'] = Date.now() + 5000;
  p.d.querySelector('input[data-own="S122"]').blur(); p.radio('S060', 'now').click(); await delay(900);
  ok('D the newer title stands', p.store.doc.own.S122 === 'Newer Title', p.store.doc.own.S122);
  ok('D and shows here', p.d.querySelector('input[data-own="S122"]').value === 'Newer Title'); p.close(); }
// E. no saved answers reachable: the page says so
{ const p = open({ storeDoc: HIS, noDb: true }); await delay(400);
  ok('E says it is not connected', /Not connected/.test(p.status()), p.status());
  p.radio('S040', 'now').click(); await delay(100);
  ok('E and that the pick is in this browser only', /this browser only/.test(p.status()), p.status()); p.close(); }
// F. a first visit with an empty store and nothing local writes nothing
{ const p = open({ storeDoc: null }); await delay(400); ok('F nothing written', p.store.sets === 0); p.radio('S040', 'now').click(); await delay(900);
  ok('F first pick creates the record', p.store.doc && p.store.doc.picks.S040 === 'now'); p.close(); }
console.log(fails ? fails + ' FAILED' : 'all passed'); process.exit(fails ? 1 : 0);
})();
