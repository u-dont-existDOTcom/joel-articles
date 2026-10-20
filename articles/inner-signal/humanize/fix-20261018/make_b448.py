"""Batch 448g (2026-10-18): the emu-u refix screens (HG18's third sample, HG24's second, HG06's third paragraph again,
with the new paragraphs' checks), and every refix section that is ready (make_b446.collect()). Predictions: a later refix
sample of a window that read AI 0.6 (3 of 4 in 445g and 447g read Human... HG18's second didn't); a paragraph check by
its length. Run from humanize/: python3 fix-20261018/make_b448.py [--batch N] [--write]"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
sys.path.insert(0, str(HERE))
import refix_runs as R  # noqa: E402
import install_fixed as I  # noqa: E402
import paragraphs_alone as PA  # noqa: E402
import make_b446 as B  # noqa: E402
from mkbatch import write_batch  # noqa: E402

rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
num = int(sys.argv[sys.argv.index('--batch') + 1]) if '--batch' in sys.argv else 448
g434 = json.loads((HERE / 'b434' / 'GATE.json').read_text(encoding='utf-8'))
g441 = json.loads((HERE / 'b441' / 'GATE.json').read_text(encoding='utf-8'))
ER, ES, EU = HERE / 'emu-r', HERE / 'emu-s', HERE / 'emu-u'
PLAN = [('HG18', g434, [ER, ES, EU], 'HG18-refix3', 0.6, 'a third refix sample of its two AI windows (445g: 47 and 114 words)'),
        ('HG24', g441, [ES, EU], 'HG24-refix2', 0.6, 'a second refix sample of its two AI windows (445g: 87 and 54 words)'),
        ('HG06', g434, [ES, EU], 'HG06-refix2', 0.7, 'Human whole in 434g and 445g; its third paragraph, AI with its neighbour in 445g, from a third sample')]
dirs = [d for d in sorted(HERE.glob('b4*')) if list(d.glob('*-results.json'))]
seen = set(PA.results(dirs))
drafts, gate, preds = {}, {}, {}
for key, g, folders, name, c, why in PLAN:
    rec = g[key + '-fix']
    fixed = HERE / rec['reviews']
    text, files = R.assembled_fixed(fixed, folders)
    drafts[name] = text
    base = {'kind': 'emulate', 'emulate': (rec.get('emulate') or []) + [rel(f) for f in files], 'published': rec.get('published'),
            'fixed': [rel(fixed)], 'lint': 'REVIEW', 'runs': sorted(pathlib.Path(f).parent.name + '/' + pathlib.Path(f).name for f in files)}
    gate[name] = dict(base)
    preds[name] = ('Human', c, why)
    if key == 'HG06':
        u = R.units_fixed(fixed, folders)
        uf = HERE / 'rf-c' / ('%s.units.json' % key)
        uf.write_text(json.dumps(u, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        for i, t, x in I.para_texts(I.section_md(uf), seen):
            kind = 'alone' if x == t else ('next' if x.startswith(t) else ('prev' if x.endswith(t) else 'run'))
            pn = '%s-u-p%d%s' % (key, i + 1, '' if kind == 'alone' else '+' + kind)
            drafts[pn] = x
            gate[pn] = dict(base, paragraph=i + 1, check=kind, section='%s (this batch)' % name)
            w = len(x.split())
            preds[pn] = ('Human', 0.70 if w < 80 else 0.77, 'paragraph %d of %s with the emu-u stretch (%s), %d words' % (i + 1, key, kind, w))
d2, g2, p2, held = B.collect()
drafts.update(d2); gate.update(g2); preds.update(p2)
print(len(drafts), 'texts:', ' '.join(drafts))
print('held:', ' '.join('%s (%s)' % x for x in held) or '-')
if '--write' in sys.argv:
    intro = ('Pangram\'s web app. The emu-u refix screens (HG18, HG24, HG06), and the refix sections that are ready (edit checks '
             'of their triaged fixes, paragraph checks). Never installed from here. Predictions written before the run.')
    write_batch(HERE, num, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
