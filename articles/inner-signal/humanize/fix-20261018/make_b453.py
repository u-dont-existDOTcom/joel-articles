"""Batch 453g (2026-10-18): three edits of sections whose newest text read Human in 451g, each with the triaged fixes of
its newest stretch's second reading (rf-j) and the paragraph checks of every paragraph not yet checked in that text:
HG35 (B17 from emu-w: the four things that can all be true put back), HG06 (P4's attribution, P6's nine forces),
HG26 (B8 from emu-y: "the main" guidelines, "depending on the person", the limit of self-hypnosis). With every refix
section that is ready (make_b446.collect(): HG16 and HG38+39 paragraph checks).
Run from humanize/: python3 fix-20261018/make_b453.py [--batch N] [--write]"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
sys.path.insert(0, str(HERE))
import install_fixed as I  # noqa: E402
import paragraphs_alone as PA  # noqa: E402
import triage_apply as T  # noqa: E402
import make_b446 as B  # noqa: E402
from mkbatch import write_batch  # noqa: E402

rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
num = int(sys.argv[sys.argv.index('--batch') + 1]) if '--batch' in sys.argv else 453
drafts, gate, preds, held = B.collect()
g451 = json.loads((HERE / 'b451' / 'GATE.json').read_text(encoding='utf-8'))
r451 = json.loads((HERE / 'b451' / 'b451-results.json').read_text(encoding='utf-8'))
mq = json.loads((HERE / 'march-q' / 'march.json').read_text(encoding='utf-8'))
dirs = [d for d in sorted(HERE.glob('b4*')) if list(d.glob('*-results.json'))]
seen = set(PA.results(dirs))
PLAN = [('HG35', 'HG35-refix3', HERE / 'rf-f' / 'HG35.fixed.json', HERE / 'rf-f' / 'HG35.fixed2.json', HERE / 'rf-f' / 'HG35.review2.json', ['HG35-B17']),
        ('HG06', 'HG06-refix3', HERE / 'rf-f' / 'HG06.units.json', HERE / 'rf-f' / 'HG06.fixed.json', HERE / 'rf-f' / 'HG06.review.json', ['HG06-B3', 'HG06-B6']),
        ('HG26', 'HG26-refix2', HERE / 'rf-h' / 'HG26.units.json', HERE / 'rf-h' / 'HG26.fixed.json', HERE / 'rf-h' / 'HG26.review.json', ['HG26-B8'])]
for key, was_name, was_path, fx, review, marches in PLAN:
    g = g451[was_name]
    old = '\n\n'.join(p for u in json.loads(was_path.read_text(encoding='utf-8'))['units'] for p in u['paras'])
    assert old == json.loads((HERE / 'b451' / 'drafts.json').read_text(encoding='utf-8'))[was_name], key
    new = '\n\n'.join(p for u in json.loads(fx.read_text(encoding='utf-8'))['units'] for p in u['paras'])
    nm = key + '-rfix'
    drafts[nm] = new
    gate[nm] = {'kind': 'edit', 'was': '451g %s, 100%% Human: https://www.pangram.com/history%s' % (was_name, r451[was_name][5]), 'was_kind': 'emulate',
                'lint_was': g.get('lint'), 'march_was': [x for m in marches for x in mq[m]['was']], 'march': [x for m in marches for x in mq[m]['new']],
                'march_reads': {m: 'march-q' for m in marches}, 'cold': 'OK', 'grounding': 'OK', 'stance': 0, 'missing': [], 'repeats': 0, 'lint': 'REVIEW',
                'reviews': rel(fx), 'verify': ['articles/inner-signal/humanize/fix-20261018/rf-j/%s.verify.part1.out.txt' % key], 'adjudication': rel(review),
                'emulate': g.get('emulate'), 'published': g.get('published')}
    ch = T.changed(old, new)
    preds[nm] = ('Human', 0.85 if ch < 0.18 else 0.1, 'triaged fixes of its newest stretch, %d%% of the words changed from 451g\'s Human text' % round(100 * ch))
    base = {'kind': 'emulate', 'emulate': g.get('emulate'), 'published': g.get('published'), 'fixed': (g.get('fixed') or []) + [rel(fx)], 'lint': 'REVIEW'}
    for i, t, x in I.para_texts(I.section_md(fx), seen):
        kind = 'alone' if x == t else ('next' if x.startswith(t) else ('prev' if x.endswith(t) else 'run'))
        pn = '%s-q-p%d%s' % (key, i + 1, '' if kind == 'alone' else '+' + kind)
        drafts[pn] = x
        gate[pn] = dict(base, paragraph=i + 1, check=kind, section='453g %s (this batch)' % nm)
        w = len(x.split())
        preds[pn] = ('Human', 0.70 if w < 80 else (0.77 if w < 120 else 0.79), 'paragraph %d of %s (%s), %d words' % (i + 1, key, kind, w))
print(len(drafts), 'texts:', ' '.join(drafts))
print('held:', ' '.join('%s (%s)' % x for x in held) or '-')
if '--write' in sys.argv:
    intro = ('Pangram\'s web app. Edits of HG35, HG06 and HG26 (triaged fixes of their newest stretch) with their paragraph checks, and '
             'the refix sections that are ready. Predictions written before the run.')
    write_batch(HERE, num, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
