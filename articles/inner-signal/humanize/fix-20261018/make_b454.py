"""Batch 454g (2026-10-18): new samples of the small AI windows of HG14 and HG33 (emu-ab, over their triaged text split by
paragraph), screened whole, and every refix section that is ready (make_b446.collect(): the edits of HG37 and HG02+03).

New in this batch, to save a round per section:
  - an edit's paragraph checks go in the same batch as the edit (they used to wait for the edit's result): 20 of 24
    triaged edits read Human whole, and a paragraph that doesn't change keeps its check whatever the edit does;
  - a screened window sample's paragraph checks go with its screen, for the same reason;
  - a paragraph check's chance is tools/para_chance.py's (by how much of it isn't Emulate's), not its length;
  - a refix sample's chance is 0.72 (first samples 22 of 30 Human, later samples 10 of 14).
Run from humanize/: python3 fix-20261018/make_b454.py [--batch N] [--write]"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
sys.path.insert(0, str(HERE))
import refix_runs as R  # noqa: E402
import install_fixed as I  # noqa: E402,F401  (puts tools/humanization on the path)
import paragraphs_alone as PA  # noqa: E402
import para_chance as PC  # noqa: E402
import make_b446 as B  # noqa: E402
from mkbatch import write_batch  # noqa: E402

B.PC = PC
rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
num = int(sys.argv[sys.argv.index('--batch') + 1]) if '--batch' in sys.argv else 454
dirs = [d for d in sorted(HERE.glob('b4*')) if list(d.glob('*-results.json'))]
seen = set(PA.results(dirs))
drafts, gate, preds, held = B.collect()
# the edits' paragraph checks in the same batch
for nm in [k for k in list(drafts) if k.endswith('-rfix')]:
    key = nm[:-5]
    fx = REPO / gate[nm]['reviews']
    base = {'kind': 'emulate', 'emulate': gate[nm].get('emulate'), 'published': gate[nm].get('published'), 'fixed': [gate[nm]['reviews']], 'lint': 'REVIEW'}
    B.para_items(key, fx, dict(base, section='%dg %s (this batch)' % (num, nm)), 'checked with its edit (%s, this batch)' % nm, seen, drafts, gate, preds, 'e')
# HG02+03: its refix (443g) read Human but for Joel's table-of-contents note (AI, low: question 3, default "keep it and count
# the section as done"), so collect() skips it; its edit goes in by hand, with the march read of its one fixed stretch
import march_pairs as M  # noqa: E402
import triage_apply as T  # noqa: E402
r443 = json.loads((HERE / 'b443' / 'b443-results.json').read_text(encoding='utf-8'))
g443 = json.loads((HERE / 'b443' / 'GATE.json').read_text(encoding='utf-8'))
uf, fx = HERE / 'rf-i' / 'HG02+03.units.json', HERE / 'rf-i' / 'HG02+03.fixed.json'
old = '\n\n'.join(p for u in json.loads(uf.read_text(encoding='utf-8'))['units'] for p in u['paras'])
assert old == json.loads((HERE / 'b443' / 'drafts.json').read_text(encoding='utf-8'))['HG02+03-refix']
fd = json.loads(fx.read_text(encoding='utf-8'))
new = '\n\n'.join(p for u in fd['units'] for p in u['paras'])
src = {u['blocks'][0]: u for u in json.loads(uf.read_text(encoding='utf-8'))['units']}
mw, mn, reads = [], [], {}
for u in fd['units']:
    if u['kind'] == 'emulate' and u.get('fixes'):
        r = M.lookup(str(HERE), 'HG02+03-B%d' % u['blocks'][0], src[u['blocks'][0]]['paras'], u['paras'])
        if r:
            mw += r[1]; mn += r[2]; reads['HG02+03-B%d' % u['blocks'][0]] = r[0]
if reads:
    g = g443['HG02+03-refix']
    nm = 'HG02+03-rfix'
    drafts[nm] = new
    gate[nm] = {'kind': 'edit', 'was': '443g HG02+03-refix, Human but for Joel\'s table-of-contents note (AI, low; question 3): '
                'https://www.pangram.com/history%s' % r443['HG02+03-refix'][5], 'was_kind': 'emulate', 'lint_was': g.get('lint'),
                'march_was': mw, 'march': mn, 'march_reads': reads, 'cold': 'OK', 'grounding': 'OK', 'stance': 0, 'missing': [], 'repeats': 0,
                'lint': 'REVIEW', 'reviews': rel(fx), 'verify': [rel(HERE / 'rf-i' / 'HG02+03.verify.part1.out.txt')],
                'adjudication': rel(HERE / 'rf-i' / 'HG02+03.triage.json'), 'emulate': g.get('emulate'), 'published': g.get('published'),
                'fixes': sum(len(u.get('fixes') or []) for u in fd['units'])}
    preds[nm] = ('AI', 0.15, 'its 443g refix read Human except Joel\'s table-of-contents note (AI, low), which stays as he wrote it; 5 triaged '
                 'fixes, %d%% of the words changed. A 100%% Human headline needs that note to read Human this time' % round(100 * T.changed(old, new)))
    base = {'kind': 'emulate', 'emulate': g.get('emulate'), 'published': g.get('published'), 'fixed': [rel(fx)], 'lint': 'REVIEW'}
    B.para_items('HG02+03', fx, dict(base, section='%dg %s (this batch)' % (num, nm)), 'checked with its edit (%s, this batch)' % nm,
                 seen, drafts, gate, preds, 'e')
else:
    held.append(('HG02+03', 'march needed for its fixed stretch'))
# HG14 and HG33: emu-ab's samples of their 451g AI windows, over the triaged text split by paragraph (rf-h/KEY.split.json)
g451 = json.loads((HERE / 'b451' / 'GATE.json').read_text(encoding='utf-8'))
for key in ('HG14', 'HG33'):
    sp = HERE / 'rf-h' / ('%s.split.json' % key)
    text, files = R.assembled_fixed(sp, [HERE / 'emu-ab'])
    uf = HERE / 'rf-k' / ('%s.units.json' % key)
    assert text == '\n\n'.join(p for u in json.loads(uf.read_text(encoding='utf-8'))['units'] for p in u['paras']), key
    name = key + '-refix2'
    rec = g451[key + '-rfix']
    drafts[name] = text
    base = {'kind': 'emulate', 'emulate': (rec.get('emulate') or []) + [rel(f) for f in files], 'published': rec.get('published'),
            'fixed': [rel(sp)], 'lint': 'REVIEW', 'runs': sorted(pathlib.Path(f).parent.name + '/' + pathlib.Path(f).name for f in files)}
    gate[name] = dict(base)
    preds[name] = ('Human', 0.72, 'its triaged text (Human but for small windows in 451g) with new samples of those windows; refix samples so far: '
                   'first 22 of 30 Human, later 10 of 14')
    B.para_items(key, uf, dict(base, section='%dg %s (this batch)' % (num, name)), 'checked with its screen (%s, this batch)' % name,
                 seen, drafts, gate, preds, 'n')
print(len(drafts), 'texts:', ' '.join(drafts))
print('held:', ' '.join('%s (%s)' % x for x in held) or '-')
if '--write' in sys.argv:
    intro = ('Pangram\'s web app. New samples of HG14\'s and HG33\'s small AI windows, the edits of the refix sections that are '
             'ready, and every paragraph check of those texts in the same batch. Predictions written before the run.')
    write_batch(HERE, num, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
