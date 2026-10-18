"""Batch 466g (2026-10-18): HG18-wb with the safety fixes that matter most, after 465g's diagnostics (C alone read 100% Human,
dg5; the full set and the sets with B2's other fixes, or with the B4-B5 fixes, kept an AI window). Fixes as in make_b465:
A "one honest action", B "all instructions" (whoever gave them), C "neither of them keeps me in this state", F "only when
you feel steady", G "only what actually came up".
  HG18-smp1  C F          HG18-smp2  C F B        HG18-smp3  C F B G        HG18-smp4  C F B G A
Each screened whole with the paragraph checks of its changed paragraphs (make_b459's way). For question 4: an option for
Joel, not an install.
Run from humanize/: python3 fix-20261018/make_b466.py [--batch N] [--write]"""
import copy, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
sys.path.insert(0, str(HERE))
import install_fixed as I  # noqa: E402,F401
import paragraphs_alone as PA  # noqa: E402
import para_chance as PC  # noqa: E402
import make_b446 as B  # noqa: E402
from mkbatch import write_batch  # noqa: E402

B.PC = PC
rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
num = int(sys.argv[sys.argv.index('--batch') + 1]) if '--batch' in sys.argv else 466
dirs = [d for d in sorted(HERE.glob('b4*')) if list(d.glob('*-results.json'))]
seen = set(PA.results(dirs))
F = HERE / 'rf-zf'
units = json.loads((F / 'HG18.units.json').read_text(encoding='utf-8'))
tri = json.loads((F / 'HG18.triage.json').read_text(encoding='utf-8'))
fixes = [(f['block'], p) for f in tri['fixes'] for p in f['problems']]
NAMES = 'ABCDEFGH'
PLAN = [('HG18-smp1', 'CF', 0.55, 'C and F'), ('HG18-smp2', 'BCF', 0.45, 'B, C and F'),
        ('HG18-smp3', 'BCFG', 0.4, 'B, C, F and G'), ('HG18-smp4', 'ABCFG', 0.35, 'A, B, C, F and G')]
PUB = 'articles/inner-signal/humanize/source/published-20260928.md'
drafts, gate, preds = {}, {}, {}
for name, use, c, why in PLAN:
    d = copy.deepcopy(units)
    applied = []
    for (block, p), letter in zip(fixes, NAMES):
        if letter not in use:
            continue
        u = next(x for x in d['units'] if x['blocks'][0] == block)
        hits = [i for i, para in enumerate(u['paras']) if p['replace'] in para]
        assert len(hits) == 1 and u['paras'][hits[0]].count(p['replace']) == 1, (name, letter)
        u['paras'][hits[0]] = u['paras'][hits[0]].replace(p['replace'], p['with'])
        u.setdefault('fixes', []).append(dict(p, letter=letter))
        applied.append(letter)
    out = F / ('HG18.%s.json' % name.split('-')[1])
    out.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    text = '\n\n'.join(p for u in d['units'] for p in u['paras'])
    files = sorted({u['file'] for u in d['units'] if u.get('file') and pathlib.Path(u['file']).exists()})
    base = {'kind': 'emulate', 'emulate': [rel(f) for f in files], 'published': PUB, 'fixed': [rel(out)], 'lint': 'REVIEW'}
    drafts[name] = text
    gate[name] = dict(base)
    preds[name] = ('Human' if c >= 0.5 else 'AI', c, 'HG18-wb with fixes %s; 465g: C alone Human, the others kept an AI window' % why)
    B.para_items('HG18', out, dict(base, section='%dg %s (this batch)' % (num, name)), 'checked with its screen (%s)' % name,
                 seen, drafts, gate, preds, 'q' + name[-1])
print(len(drafts), 'texts:', ' '.join(drafts))
if '--write' in sys.argv:
    intro = ('Pangram\'s web app. HG18-wb with the safety fixes that matter most, four sets, each screened whole with its changed '
             'paragraphs. Predictions written before the run.')
    write_batch(HERE, num, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
