"""Batch 451g (2026-10-18): the triaged sections with a resampled stretch, screened whole (HG35: its triaged fixes with
B17 from emu-w; HG06: P3 and P4 from emu-u, P6 from emu-w, P5 the quotation as published), with the paragraph checks of
their new stretches, and every refix section that is ready (make_b446.collect()). Predictions: a triaged section with one
new short stretch 0.75; a paragraph check by its length. Run from humanize/: python3 fix-20261018/make_b451.py [--batch N] [--write]"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
sys.path.insert(0, str(HERE))
import refix_runs as R  # noqa: E402
import faithful as F  # noqa: E402
import install_fixed as I  # noqa: E402
import paragraphs_alone as PA  # noqa: E402
import make_b446 as B  # noqa: E402
from mkbatch import write_batch  # noqa: E402

rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
num = int(sys.argv[sys.argv.index('--batch') + 1]) if '--batch' in sys.argv else 451
g434 = json.loads((HERE / 'b434' / 'GATE.json').read_text(encoding='utf-8'))
RF = HERE / 'rf-f'
RF.mkdir(exist_ok=True)
dirs = [d for d in sorted(HERE.glob('b4*')) if list(d.glob('*-results.json'))]
seen = set(PA.results(dirs))
drafts, gate, preds = {}, {}, {}
# HG35: the refix (emu-r) with B17 resampled (emu-w), and the triage's fixes of the other stretches (rf-a/HG35.review.json)
for key, folders, review, name in (('HG35', ['emu-r', 'emu-w'], HERE / 'rf-a' / 'HG35.review.json', 'HG35-refix3'),
                                   ('HG06', ['emu-s', 'emu-u', 'emu-w'], None, 'HG06-refix3')):
    rec = g434[key + '-fix']
    fixed = HERE / rec['reviews']
    u = R.units_fixed(fixed, [HERE / d for d in folders])
    uf = RF / ('%s.units.json' % key)
    uf.write_text(json.dumps(u, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    src = uf
    if review:
        F.apply(str(uf), str(review), str(RF / ('%s.fixed.json' % key)))
        src = RF / ('%s.fixed.json' % key)
    d = json.loads(src.read_text(encoding='utf-8'))
    text = '\n\n'.join(p for x in d['units'] for p in x['paras'])
    files = sorted({x['file'] for x in d['units'] if x.get('refix')})
    drafts[name] = text
    base = {'kind': 'emulate', 'emulate': (rec.get('emulate') or []) + [rel(f) for f in files], 'published': rec.get('published'),
            'fixed': [rel(fixed)] + ([rel(HERE / 'rf-a' / 'HG35.fixed.json')] if review else []), 'lint': 'REVIEW',
            'runs': sorted(pathlib.Path(f).parent.name + '/' + pathlib.Path(f).name for f in files)}
    gate[name] = dict(base)
    preds[name] = ('Human', 0.75, 'a section that read Human with one short stretch from a new Emulate sample')
    for i, t, x in I.para_texts(I.section_md(src), seen):
        kind = 'alone' if x == t else ('next' if x.startswith(t) else ('prev' if x.endswith(t) else 'run'))
        pn = '%s-w-p%d%s' % (key, i + 1, '' if kind == 'alone' else '+' + kind)
        drafts[pn] = x
        gate[pn] = dict(base, paragraph=i + 1, check=kind, section='%s (this batch)' % name)
        w = len(x.split())
        preds[pn] = ('Human', 0.70 if w < 80 else (0.77 if w < 120 else 0.79), 'paragraph %d of %s (%s), %d words' % (i + 1, key, kind, w))
d2, g2, p2, held = B.collect()
drafts.update(d2); gate.update(g2); preds.update(p2)
print(len(drafts), 'texts:', ' '.join(drafts))
print('held:', ' '.join('%s (%s)' % x for x in held) or '-')
if '--write' in sys.argv:
    intro = ('Pangram\'s web app. Triaged sections with a resampled stretch (HG35, HG06) and their new paragraphs, and the refix '
             'sections that are ready (edit checks of triaged fixes, paragraph checks). Predictions written before the run.')
    write_batch(HERE, num, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
