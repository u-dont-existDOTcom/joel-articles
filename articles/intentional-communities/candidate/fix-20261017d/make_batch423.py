"""Batch 423g (2026-10-17 night): the six cuts make_tighten.py held because the march found each took out its paragraph's only
break (E173), now that a cut goes to Pangram whatever the march says (pangram_gate.py, "cut_of"; Joel, 21:37 UTC, on the two cuts
held before: "it made no difference taking those exclamation phrases out for pangram"). The three held rewordings stay held.
- section 13 v37: v36 (installed, 422g) with its five cuts; v37a with the opening's two only, v37b with the other three, so a
  whole that reads AI can be traced (the gate's lesson of 2026-10-17 19:14: add changes one at a time);
- section 15 v17: v16 (installed, 422g) with its one cut.
Each changed paragraph alone (50 words or more) and with each neighbor under its heading when one of the two is under 50, and
each section whole, in the format its last check used (section 13: ptext's section(); 15: its own batches' format). March labels:
the march rounds that read these exact texts (march-r1, and r2 and r3 for the conflict paragraph); cold reads: cold.json (the
first build of v36 and v16 had these cuts); the tone check read each (TONE-tighten.md: FINE).
Run from candidate/: python3 fix-20261017d/make_batch423.py"""
import hashlib, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
sys.path.insert(0, str(HERE))
from ptext import plain, section  # noqa: E402
from make_tighten import HELD  # noqa: E402

JOEL = 'Joel, 2026-10-17 21:37 UTC (joel-20261017/joel-20261017-2137-message.txt): '
SKIP = re.compile(r'^(\[image \d+\]|\[Professor Baby Sheep|Double click to interact with video|<!--)')
H13, H15 = '# Your Little Forming Group Already Is the Community', '# What This Looks Like From Sénégal'
CUTS = [h for h in HELD if h[2] == 'cut']
assert len(CUTS) == 6 and all(not new or old.endswith(new) for _, _, _, old, new, _ in CUTS), CUTS


def own_whole(md):
    out = []
    for blk in [x.strip() for x in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)) if x.strip()]:
        if SKIP.match(blk):
            continue
        if blk.startswith('[caption]'):
            blk = re.sub(r'^\[caption\]\s*', '', blk)
        out.append(plain(blk.lstrip('#').strip()))
    return '\n\n'.join(out)


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)) if b.strip()]


def paras(md):
    out, h = [], 0
    for b in blocks(md):
        if b.startswith('#'):
            h += 1
        elif not SKIP.match(b) and not b.startswith('[caption]'):
            out.append((h, plain(b)))
    return out


def apply(md, cuts):
    for sec, where, kind, old, new, why in cuts:
        assert md.count(old) == 1, (where, old[:60], md.count(old))
        md = md.replace(old, new)
    return md


# every march reading by its exact text
READ = {}
for rnd in ('march-r1', 'march-r2', 'march-r3'):
    f = HERE / rnd
    ids = json.loads((f / 'march-ids.json').read_text())
    texts = [t.strip() for t in re.split(r'\n\s*\n', (f / 'march-in.md').read_text(encoding='utf-8')) if t.strip()]
    L = [dict(re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', (f / ('MARCH-labels-%s.txt' % x)).read_text(), re.M)) for x in 'ab']
    for i, k in enumerate(ids):
        READ.setdefault(texts[i], ([m[str(i + 1)] for m in L], '%s (%s)' % (rnd, k)))

COLD = json.loads((HERE / 'cold.json').read_text())
v36 = (C / 's13' / 'v36.md').read_text(encoding='utf-8')
v16 = (C / 's15' / 'v16.md').read_text(encoding='utf-8')
art = (HERE / 'article-with-tighten.md').read_text(encoding='utf-8')
assert section(v36, H13) == section(art, H13)   # the same text 422g read as S13v36
s13cuts = [c for c in CUTS if c[0] == 's13']
VERS = {
    'S13v37': ('s13', v36, apply(v36, s13cuts), C / 's13' / 'v37.md', 'batch 422g: section 13 v36 100% Human'),
    'S13v37a': ('s13', v36, apply(v36, [c for c in s13cuts if c[1].startswith('Opening')]), C / 's13' / 'v37a.md',
                'batch 422g: section 13 v36 100% Human'),
    'S13v37b': ('s13', v36, apply(v36, [c for c in s13cuts if not c[1].startswith('Opening')]), C / 's13' / 'v37b.md',
                'batch 422g: section 13 v36 100% Human'),
    'S15v17': ('s15', v16, apply(v16, [c for c in CUTS if c[0] == 's15']), C / 's15' / 'v17.md', 'batch 422g: section 15 v16 100% Human'),
}
drafts, gate = {}, {}
for key, (s, src, dst, path, was) in VERS.items():
    path.write_text(dst, encoding='utf-8')
    a, b = paras(src), paras(dst)
    assert len(a) == len(b)
    pa, pb = [p for _, p in a], [p for _, p in b]
    parts = ['installed']
    for i, (x, y) in enumerate(zip(pa, pb)):
        if x == y:
            continue
        why = [w for sec, where, kind, old, new, w in CUTS if sec == s and plain(old.strip()) in x and (not new or True)]
        rec = {'kind': 'edit', 'was': was, 'grounding': 'OK', 'grounding_note': 'no claim of mine: a cut (make_tighten.py, HELD)',
               'stance': 0, 'stance_note': 'a cut of a line the whole-article reader called padding, or a stock question; no position '
               'added or taken away', 'missing': [], 'cold': COLD[s][0], 'cold_note': COLD[s][1],
               'joel_note': JOEL + '48 a (the tightening pass) and 51 a ("make sure it reads well")'}
        mw, mn = READ.get(x), READ.get(y)
        assert mw and mn, (key, i, y[:60])
        rec.update(march_was=mw[0], march=mn[0], march_note='fix-20261017d/%s and %s' % (mw[1], mn[1]))
        k0 = '%s-p%d' % (key, i + 1)
        if len(y.split()) >= 50:
            drafts[k0] = y; gate[k0] = dict(rec, cut_of=x); parts.append(k0)
        for j in (i - 1, i + 1):
            if 0 <= j < len(pb) and b[j][0] == b[i][0] and min(len(pb[i].split()), len(pb[j].split())) < 50:
                lo, hi = sorted((i, j))
                k = '%s+%s' % (k0, 'prev' if j < i else 'next')
                drafts[k] = pb[lo] + '\n\n' + pb[hi]; gate[k] = dict(rec, cut_of=pa[lo] + '\n\n' + pa[hi]); parts.append(k)
    drafts[key] = section(dst, H13) if s == 's13' else own_whole(dst)
    gate[key] = {'kind': 'section', 'parts': parts, 'repeats': 0, 'repeats_note': 'nothing added: cuts only (make_tighten.py, HELD)'}
for k in drafts:
    gate[k]['words'] = len(drafts[k].split())
seen, aliases = {}, {}
for k in list(drafts):
    if drafts[k] in seen:
        aliases[k] = seen[drafts[k]]; del drafts[k]
    else:
        seen[drafts[k]] = k
for k in gate:   # a section's part that is the same text as an earlier item is that item (the gate checks the item it runs)
    if gate[k]['kind'] == 'section':
        gate[k]['parts'] = list(dict.fromkeys(aliases.get(p, p) for p in gate[k]['parts']))
for k in aliases:
    del gate[k]
for k in drafts:
    print(k, gate[k]['words'], gate[k]['kind'], gate[k].get('march_was'), gate[k].get('march'), '|', drafts[k][:60].replace('\n', ' / '))
print('aliases:', aliases)
print(len(drafts), 'items,', sum(gate[k]['words'] for k in drafts), 'words')
out = HERE / 'b423'
out.mkdir(exist_ok=True)
(out / 'aliases.json').write_text(json.dumps(aliases, indent=1) + '\n', encoding='utf-8')
(out / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(out / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(out / 'drafts.json'),
                    str(out / 'GATE.json'), str(out / 'b423.js'), '--name', 'B423', '--lint-article',
                    str(C / 'HUMANIZED-SO-FAR.md')] + list(drafts), capture_output=True, text=True)
print(r.stdout[-2500:], r.stderr[-2500:])
if r.returncode == 0:
    items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
    (out / 'b423-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
