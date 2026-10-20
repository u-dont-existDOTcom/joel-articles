"""Batch 465g (2026-10-18): diagnostic versions of HG18-wb (which of its eight fixes makes it read AI?). 463g's HG18-wb read
100% Human whole and in every paragraph; with its eight triaged fixes (rf-zf/HG18.fixed.json) it read AI from B2 on (464g),
and B2 alone read AI 0.82. Fixes: A "one honest action", B "all instructions" (whoever gave them), C "neither of them
keeps me in this state", D "adult judgment fully back" (all B2); E "these five steps" (B3); F "only when you feel steady",
G "only what actually came up" (B4); H "say to yourself" (B5).
  HG18-dg1  every fix but C        HG18-dg2  E F G H (none in B2)     HG18-dg3  A B C D (B2's only)
  HG18-dg4  every fix but H        HG18-dg5  C only
Whole-section screens only (a diagnostic is never installed); chances near 0.5 on purpose.
Run from humanize/: python3 fix-20261018/make_b465.py [--batch N] [--write]"""
import copy, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
sys.path.insert(0, str(HERE))
import install_fixed as I  # noqa: E402,F401
from mkbatch import write_batch  # noqa: E402

rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
num = int(sys.argv[sys.argv.index('--batch') + 1]) if '--batch' in sys.argv else 465
F = HERE / 'rf-zf'
units = json.loads((F / 'HG18.units.json').read_text(encoding='utf-8'))
tri = json.loads((F / 'HG18.triage.json').read_text(encoding='utf-8'))
fixes = [(f['block'], p) for f in tri['fixes'] for p in f['problems']]
assert len(fixes) == 8
NAMES = 'ABCDEFGH'
PLAN = [('HG18-dg1', 'ABDEFGH', 0.45, 'every fix but C ("neither of them keeps me in this state")'),
        ('HG18-dg2', 'EFGH', 0.6, 'no fix in B2'),
        ('HG18-dg3', 'ABCD', 0.3, 'only B2\'s four fixes'),
        ('HG18-dg4', 'ABCDEFG', 0.4, 'every fix but H ("say to yourself")'),
        ('HG18-dg5', 'C', 0.4, 'only C')]
PUB = 'articles/inner-signal/humanize/source/published-20260928.md'
drafts, gate, preds = {}, {}, {}
for name, use, c, why in PLAN:
    d = copy.deepcopy(units)
    for (block, p), letter in zip(fixes, NAMES):
        if letter not in use:
            continue
        u = next(x for x in d['units'] if x['blocks'][0] == block)
        hits = [i for i, para in enumerate(u['paras']) if p['replace'] in para]
        assert len(hits) == 1 and u['paras'][hits[0]].count(p['replace']) == 1, (name, letter)
        u['paras'][hits[0]] = u['paras'][hits[0]].replace(p['replace'], p['with'])
    out = F / ('HG18.%s.json' % name.split('-')[1])
    out.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    text = '\n\n'.join(p for u in d['units'] for p in u['paras'])
    files = sorted({u['file'] for u in d['units'] if u.get('file') and pathlib.Path(u['file']).exists()})
    drafts[name] = text
    gate[name] = {'kind': 'emulate', 'emulate': [rel(f) for f in files], 'published': PUB, 'fixed': [rel(out)], 'lint': 'REVIEW'}
    preds[name] = ('Human' if c >= 0.5 else 'AI', c, 'diagnostic: %s; 464g: all eight read AI from B2 on' % why)
print(len(drafts), 'texts:', ' '.join(drafts))
if '--write' in sys.argv:
    intro = ('Pangram\'s web app. Diagnostic versions of HG18-wb, each with some of its eight triaged fixes, to find which reads '
             'AI. Predictions written before the run.')
    write_batch(HERE, num, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
