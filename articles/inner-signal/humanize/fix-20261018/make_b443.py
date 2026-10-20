"""Batch 443g (2026-10-18): the refix screens. Each section whose fixed version read AI in 434g, with the stretches inside
its AI windows rewritten by Emulate from my meaning-fixed text (emu-r: Plan B, after my fixes made 21 of 25 Human
sections read AI) and the rest as fixed. Built by tools/refix_runs.py assembled_fixed(). Never installed from here: a
section that reads Human goes to a second reader for the new stretches, then its paragraph checks.

Predictions: Emulate's screens read Human 36 of 71 times (430g to 440g), 18 of 22 for first samples of whole windows
(430g, 431g), the closest to a refix run (one sample of each window, its input already saying what the published text
says). Chance 0.55 for a section whose 434g windows covered nearly all of it, 0.6 when the flagged share was under half
(the rest is fixed text that read Human there). Run from humanize/: python3 fix-20261018/make_b443.py [--write]
"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
import refix_runs as R  # noqa: E402
from mkbatch import write_batch  # noqa: E402

rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
RD = HERE / 'emu-r'
runs = json.loads((RD / 'runs.json').read_text(encoding='utf-8'))
g434 = json.loads((HERE / 'b434' / 'GATE.json').read_text(encoding='utf-8'))
r434 = json.loads((HERE / 'b434' / 'b434-results.json').read_text(encoding='utf-8'))
drafts, gate, preds = {}, {}, {}
for key in sorted({m['key'] for m in runs}):
    rec = g434[key + '-fix']
    fixed = HERE / rec['reviews']
    text, files = R.assembled_fixed(fixed, [RD])
    name = key + '-refix'
    drafts[name] = text
    res = r434[key + '-fix']
    flagged_words = sum(int(w.split('(')[1].split()[0]) for w in res[6]) if res[6] else 0
    share = flagged_words / max(1, res[2])
    gate[name] = {'kind': 'emulate', 'emulate': (rec.get('emulate') or []) + [rel(f) for f in files], 'published': rec.get('published'),
                  'fixed': [rel(fixed)], 'lint': 'REVIEW', 'refix_of': '434g %s-fix, %s %.2f: https://www.pangram.com/history%s'
                  % (key, res[0], res[1], res[5]), 'runs': sorted(pathlib.Path(f).name for f in files)}
    c = 0.6 if share < 0.5 else 0.55
    preds[name] = ('Human' if c >= 0.5 else 'Mixed', c, 'the %d%% of the fixed text in 434g\'s AI windows rewritten by Emulate from '
                   'the fixed words (%d run%s); chance from first samples of whole windows (18 of 22 Human), less for a new input'
                   % (round(100 * share), len(files), '' if len(files) == 1 else 's'))
print(len(drafts), 'sections:', ' '.join(drafts))
if '--write' in sys.argv:
    intro = ('Pangram\'s web app. The refix screens: each section whose fixed version read AI in 434g, with the stretches in its AI '
             'windows rewritten by Emulate from my meaning-fixed text (`emu-r`). Never installed from here. Predictions written before the run.')
    write_batch(HERE, 443, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
