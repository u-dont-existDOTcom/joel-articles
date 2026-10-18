"""Batch 462g (2026-10-18): HG36 with the triaged fixes of its chosen sample, screened whole, with the paragraph checks of
every paragraph its fixes changed, in the same batch (make_b460's way).

  HG36-fix  rf-zd/HG36.fixed.json   461g's HG36-wc (emu-av: the whole section in one run from the published text; 100% Human
                                    whole and in every paragraph), with its triaged fixes (rf-zd/HG36.triage.json)
Predictions: the section screen by the share of words changed (triaged edits under 18% changed: 24 of 29 Human whole); a
paragraph check by tools/para_chance.py.
Run from humanize/: python3 fix-20261018/make_b462.py [--batch N] [--write]"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
sys.path.insert(0, str(HERE))
import install_fixed as I  # noqa: E402,F401  (puts tools/humanization on the path)
import paragraphs_alone as PA  # noqa: E402
import para_chance as PC  # noqa: E402
import make_b446 as B  # noqa: E402
from mkbatch import write_batch  # noqa: E402

B.PC = PC
rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
num = int(sys.argv[sys.argv.index('--batch') + 1]) if '--batch' in sys.argv else 462
dirs = [d for d in sorted(HERE.glob('b4*')) if list(d.glob('*-results.json'))]
seen = set(PA.results(dirs))
PUB = 'articles/inner-signal/humanize/source/published-20260928.md'
import triage_apply as T  # noqa: E402
u36 = json.loads((HERE / 'rf-zd' / 'HG36.units.json').read_text(encoding='utf-8'))
f36 = json.loads((HERE / 'rf-zd' / 'HG36.fixed.json').read_text(encoding='utf-8'))
ch = T.changed('\n\n'.join(p for u in u36['units'] for p in u['paras']), '\n\n'.join(p for u in f36['units'] for p in u['paras']))
n36 = sum(len(u.get('fixes') or []) for u in f36['units'])
PLAN = [('HG36', HERE / 'rf-zd' / 'HG36.fixed.json', 'HG36-fix', 0.75 if ch < 0.08 else 0.6,
         '461g HG36-wc (100%% Human whole and in every paragraph) with its %d triaged fixes, %.1f%% of the words; triaged edits '
         'under 18%% changed: 24 of 29 Human whole; HG24-fix (0.6%%) read Human in 460g' % (n36, 100 * ch))]
drafts, gate, preds = {}, {}, {}
for key, fx, name, c, why in PLAN:
    d = json.loads(fx.read_text(encoding='utf-8'))
    text = '\n\n'.join(p for u in d['units'] for p in u['paras'])
    files = sorted({u['file'] for u in d['units'] if u.get('file') and pathlib.Path(u['file']).exists()})
    base = {'kind': 'emulate', 'emulate': [rel(f) for f in files], 'published': PUB, 'fixed': [rel(fx)], 'lint': 'REVIEW'}
    drafts[name] = text
    gate[name] = dict(base)
    preds[name] = ('Human' if c >= 0.5 else 'AI', c, why)
    B.para_items(key, fx, dict(base, section='%dg %s (this batch)' % (num, name)), 'checked with its screen (%s, this batch)' % name,
                 seen, drafts, gate, preds, 'y')
print(len(drafts), 'texts:', ' '.join(drafts))
if '--write' in sys.argv:
    intro = ('Pangram\'s web app. HG36 with the triaged fixes of its chosen sample, screened whole, and the paragraphs its fixes '
             'changed. Predictions written before the run.')
    write_batch(HERE, num, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
