// insert.js: run in a post's editor (/publish/post/<id>) in the desktop app's browser pane, with window.__plan set to the
// post's PLAN-*.json (make_plans.py). It builds one transaction that puts each new section in before its anchor heading
// (found once, by level and text) and checks it; nothing changes until dispatch: window.__ins.ed.view.dispatch(window.__ins.tr)
// (only while the document is still window.__ins.base). Then the editor saves the draft; the live post changes only
// with Update (tools/humanization/substack_update.js, no email).
await (async () => {
  const P = window.__plan;
  const ed = [...document.querySelectorAll('.ProseMirror')].map((e) => e.editor).find(Boolean);
  if (!P || !ed) return {ok: false, why: 'no plan or no editor'};
  if (!location.pathname.endsWith('/' + P.post)) return {ok: false, why: 'not post ' + P.post};
  const S = ed.schema, state = ed.state, doc = state.doc;
  const norm = (s) => s.replace(/[‘’]/g, "'").replace(/[“”]/g, '"').replace(/\s+/g, ' ').trim();
  const heads = [];
  doc.forEach((n, off) => { if (n.type.name === 'heading') heads.push([n.attrs.level, norm(n.textContent), off]); });
  for (const ins of P.inserts) {
    if (ins.heading && heads.some((h) => h[1] === norm(ins.heading))) return {ok: false, why: 'already has ' + ins.heading};
    if (!ins.heading && doc.textContent.includes(ins.texts[0].slice(0, 60))) return {ok: false, why: 'already has ' + ins.id};
  }
  let parser = S.cached && S.cached.domParser;
  if (!parser) { ed.can().setContent('<p>x</p>'); parser = S.cached.domParser; }
  if (!parser || ed.state.doc !== doc) return {ok: false, why: 'no parser, or the document changed'};
  const parse = (h) => parser.parse(new window.DOMParser().parseFromString('<!doctype html><body>' + h + '</body>', 'text/html').body).content;
  const jobs = [];
  for (const ins of P.inserts) {
    const at = heads.filter((h) => h[0] === ins.before[0] && h[1] === norm(ins.before[1]));
    if (at.length !== 1) return {ok: false, why: 'anchor "' + ins.before[1] + '" found ' + at.length + ' times'};
    if (ins.after_text) {
      const prev = doc.resolve(at[0][2]).nodeBefore;
      let k = 0, txt = '';
      doc.forEach((n, off) => { if (off < at[0][2] && n.textContent.trim()) txt = n.textContent; });
      if (!norm(txt).includes(norm(ins.after_text))) return {ok: false, why: 'the paragraph before "' + ins.before[1] + '" is not the one the plan follows: ' + txt.slice(0, 80)};
    }
    const frag = parse(ins.html);
    const got = [];
    frag.forEach((n) => got.push(norm(n.textContent)));
    if (got.length !== ins.texts.length || got.some((t, k) => t !== norm(ins.texts[k]))) return {ok: false, why: ins.id + ' parsed to other text', got, want: ins.texts};
    jobs.push({id: ins.id, pos: at[0][2], frag});
  }
  jobs.sort((a, b) => b.pos - a.pos);
  const tr = state.tr;
  for (const j of jobs) tr.insert(j.pos, j.frag);
  const links = [];
  for (const j of jobs) j.frag.descendants((n) => { if (n.isText) for (const m of n.marks) if (m.type.name === 'link') links.push([j.id, m.attrs.href, m.attrs.target, m.attrs.rel]); });
  const kinds = [];
  for (const j of jobs) j.frag.forEach((n) => kinds.push([j.id, n.type.name, n.attrs.level || null]));
  window.__ins = {ed, base: doc, tr};
  return {ok: true, before: doc.childCount, after: tr.doc.childCount, jobs: jobs.map((j) => [j.id, j.pos, j.frag.childCount]), kinds, links};
})()
