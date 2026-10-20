"""Batch 452g (2026-10-18): every refix section that is ready (make_b446.collect(): HG16 and HG38+39 edits, HG15 and
HG34 paragraph checks), and HG20 with its P8 (the one paragraph that read AI alone in 450g) from emu-z2's sample c with
one small fix of mine (rf-h/HG20.review.json), as an edit of 449g's HG20-rfix, with its paragraph check.
Run from humanize/: python3 fix-20261018/make_b452.py [--batch N] [--write]"""
import json, pathlib, re, sys

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
num = int(sys.argv[sys.argv.index('--batch') + 1]) if '--batch' in sys.argv else 452
drafts, gate, preds, held = B.collect()
# HG20: the edit of P8
g449 = json.loads((HERE / 'b449' / 'GATE.json').read_text(encoding='utf-8'))['HG20-rfix']
r449 = json.loads((HERE / 'b449' / 'b449-results.json').read_text(encoding='utf-8'))['HG20-rfix']
old = '\n\n'.join(p for u in json.loads((HERE / 'rf-a' / 'HG20.fixed.json').read_text(encoding='utf-8'))['units'] for p in u['paras'])
fx = HERE / 'rf-h' / 'HG20.fixed.json'
new = '\n\n'.join(p for u in json.loads(fx.read_text(encoding='utf-8'))['units'] for p in u['paras'])
labels = dict(re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', (HERE / 'march-p' / 'march-labels.txt').read_text(encoding='utf-8'), re.M))
drafts['HG20-rfix2'] = new
gate['HG20-rfix2'] = dict(g449, was='449g HG20-rfix, 100%% Human: https://www.pangram.com/history%s' % r449[5], march_was=[labels['1']], march=[labels['2']],
                          march_reads={'HG20-B11': 'march-p'}, reviews=rel(fx), adjudication=rel(HERE / 'rf-h' / 'HG20.review.json'),
                          emulate=(g449.get('emulate') or []) + ['articles/inner-signal/humanize/fix-20261018/emu-z2/HG20-fxw1c.out.txt'],
                          notes='P8 read AI alone (450g); emu-z, emu-z2 b and c were three new samples of it; c kept the meaning best, one fix put the body signal back')
ch = T.changed(old, new)
preds['HG20-rfix2'] = ('Human', 0.85, 'one paragraph of 25 new (an Emulate sample with one small fix), %d%% of the words changed from 449g\'s Human text' % round(100 * ch))
dirs = [d for d in sorted(HERE.glob('b4*')) if list(d.glob('*-results.json'))]
seen = set(PA.results(dirs))
for i, t, x in I.para_texts(I.section_md(fx), seen):
    kind = 'alone' if x == t else ('next' if x.startswith(t) else ('prev' if x.endswith(t) else 'run'))
    pn = 'HG20-z-p%d%s' % (i + 1, '' if kind == 'alone' else '+' + kind)
    drafts[pn] = x
    gate[pn] = {'kind': 'emulate', 'emulate': gate['HG20-rfix2']['emulate'], 'published': g449.get('published'), 'fixed': [rel(HERE / 'rf-a' / 'HG20.fixed.json'), rel(fx)],
                'lint': 'REVIEW', 'paragraph': i + 1, 'check': kind, 'section': '452g HG20-rfix2 (this batch)'}
    w = len(x.split())
    preds[pn] = ('Human', 0.70 if w < 80 else 0.77, 'paragraph %d of HG20 with its new P8 (%s), %d words' % (i + 1, kind, w))
print(len(drafts), 'texts:', ' '.join(drafts))
print('held:', ' '.join('%s (%s)' % x for x in held) or '-')
if '--write' in sys.argv:
    intro = ('Pangram\'s web app. The refix sections that are ready (edit checks of their triaged fixes, paragraph checks), and HG20 '
             'with a new P8. Predictions written before the run.')
    write_batch(HERE, num, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
