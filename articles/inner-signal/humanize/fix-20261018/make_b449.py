"""Batch 449g (2026-10-18): the emu-v refix screens (a second sample of each AI window 447g left in HG17, HG31 and HG37,
from my fixed text again, over emu-t), with every refix section that is ready (make_b446.collect(): edit checks of
triaged fixes, paragraph checks). Predictions: a second refix sample of a window 0.6 (445g and 448g: 3 of 5 read Human).
Run from humanize/: python3 fix-20261018/make_b449.py [--batch N] [--write]"""
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
num = int(sys.argv[sys.argv.index('--batch') + 1]) if '--batch' in sys.argv else 449
ET, EV = HERE / 'emu-t', HERE / 'emu-v'
g444 = json.loads((HERE / 'b444' / 'GATE.json').read_text(encoding='utf-8'))
r444 = json.loads((HERE / 'b444' / 'b444-results.json').read_text(encoding='utf-8'))
drafts, gate, preds = {}, {}, {}
for key in sorted({m['key'] for m in json.loads((EV / 'runs.json').read_text(encoding='utf-8'))}):
    rec = g444[key + '-fix']
    fixed = HERE / rec['reviews']
    text, files = R.assembled_fixed(fixed, [ET, EV])
    name = key + '-refix2'
    drafts[name] = text
    res = r444[key + '-fix']
    gate[name] = {'kind': 'emulate', 'emulate': (rec.get('emulate') or []) + [rel(f) for f in files], 'published': rec.get('published'),
                  'fixed': [rel(fixed)], 'lint': 'REVIEW', 'refix_of': '444g %s-fix, %s %.2f: https://www.pangram.com/history%s'
                  % (key, res[0], res[1], res[5]), 'runs': sorted(pathlib.Path(f).parent.name + '/' + pathlib.Path(f).name for f in files)}
    r447 = json.loads((HERE / 'b447' / 'b447-results.json').read_text(encoding='utf-8'))[key + '-refix']
    preds[name] = ('Human', 0.6, 'a second refix sample of its 447g AI window (%d words); second samples: 3 of 5 Human so far'
                   % sum(int(w.split('(')[1].split()[0]) for w in r447[6]))
d2, g2, p2, held = B.collect()
drafts.update(d2); gate.update(g2); preds.update(p2)
print(len(drafts), 'texts:', ' '.join(drafts))
print('held:', ' '.join('%s (%s)' % x for x in held) or '-')
if '--write' in sys.argv:
    intro = ('Pangram\'s web app. The emu-v refix screens (second samples for HG17, HG31, HG37), and the refix sections that are ready '
             '(edit checks of their triaged fixes, paragraph checks). Never installed from here. Predictions written before the run.')
    write_batch(HERE, num, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
