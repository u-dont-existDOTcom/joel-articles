"""Batch 447g (2026-10-18): the emu-t refix screens (444g's five fixed sections with their AI windows rewritten by Emulate
from my fixed text: HG16, HG17, HG31, HG37, HG38+39), with every refix section that is ready (make_b446.collect(): edit
checks of triaged fixes, paragraph checks). Predictions: a first refix sample 0.8 (20 of 25 read Human in 443g and 445g).
Run from humanize/: python3 fix-20261018/make_b447.py [--batch N] [--write]"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
sys.path.insert(0, str(HERE))
import refix_runs as R  # noqa: E402
import make_b446 as B  # noqa: E402
from mkbatch import write_batch  # noqa: E402

rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
num = int(sys.argv[sys.argv.index('--batch') + 1]) if '--batch' in sys.argv else 447
ET = HERE / 'emu-t'
g444 = json.loads((HERE / 'b444' / 'GATE.json').read_text(encoding='utf-8'))
r444 = json.loads((HERE / 'b444' / 'b444-results.json').read_text(encoding='utf-8'))
drafts, gate, preds = {}, {}, {}
for key in sorted({m['key'] for m in json.loads((ET / 'runs.json').read_text(encoding='utf-8'))}):
    rec = g444[key + '-fix']
    fixed = HERE / rec['reviews']
    text, files = R.assembled_fixed(fixed, [ET])
    name = key + '-refix'
    drafts[name] = text
    res = r444[key + '-fix']
    gate[name] = {'kind': 'emulate', 'emulate': (rec.get('emulate') or []) + [rel(f) for f in files], 'published': rec.get('published'),
                  'fixed': [rel(fixed)], 'lint': 'REVIEW', 'refix_of': '444g %s-fix, %s %.2f: https://www.pangram.com/history%s'
                  % (key, res[0], res[1], res[5]), 'runs': sorted('emu-t/' + pathlib.Path(f).name for f in files)}
    preds[name] = ('Human', 0.8, 'its 444g AI windows (%d words) rewritten by Emulate from the fixed text; first refix samples: 20 of 25 Human'
                   % sum(int(w.split('(')[1].split()[0]) for w in res[6]))
d2, g2, p2, held = B.collect()
drafts.update(d2); gate.update(g2); preds.update(p2)
print(len(drafts), 'texts:', ' '.join(drafts))
print('held:', ' '.join('%s (%s)' % x for x in held) or '-')
if '--write' in sys.argv:
    intro = ('Pangram\'s web app. The emu-t refix screens of 444g\'s five fixed sections, and the refix sections that are ready '
             '(edit checks of their triaged fixes, paragraph checks). Never installed from here. Predictions written before the run.')
    write_batch(HERE, num, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
