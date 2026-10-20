"""Batch 460g (2026-10-18): HG24 with the triaged fixes of its chosen sample, screened whole, with the paragraph checks of
every paragraph its fixes changed, in the same batch (make_b455's way).

  HG24-fix  rf-zb/HG24.fixed.json   459g's HG24-oc (emu-as, B2-B8; 100% Human whole and in every paragraph), 3 fixes
                                    (0.6% of the words): "necessarily", "from doing this" out, a repeat said once
Predictions: the section screen 0.85 (triaged edits under 18% changed: 23 of 28 Human whole); a paragraph check by
tools/para_chance.py.
Run from humanize/: python3 fix-20261018/make_b460.py [--batch N] [--write]"""
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
num = int(sys.argv[sys.argv.index('--batch') + 1]) if '--batch' in sys.argv else 460
dirs = [d for d in sorted(HERE.glob('b4*')) if list(d.glob('*-results.json'))]
seen = set(PA.results(dirs))
PUB = 'articles/inner-signal/humanize/source/published-20260928.md'
PLAN = [('HG24', HERE / 'rf-zb' / 'HG24.fixed.json', 'HG24-fix', 0.85,
         '459g HG24-oc (100% Human whole and in every paragraph) with its 3 triaged fixes, 0.6% of the words; triaged edits '
         'under 18% changed: 23 of 28 Human whole')]
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
                 seen, drafts, gate, preds, 'x')
print(len(drafts), 'texts:', ' '.join(drafts))
if '--write' in sys.argv:
    intro = ('Pangram\'s web app. HG24 with the triaged fixes of its chosen sample, screened whole, and the paragraphs its fixes '
             'changed. Predictions written before the run.')
    write_batch(HERE, num, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
