"""Batch 463g (2026-10-18): the fast path for "Come all the way back" (HG18; make_emu_aw.py), each sample's section screened
whole with its paragraph checks, so Pangram and the second reader choose together (make_b461's way):
  HG18-wa/wb/wc   the whole section (B1-B6, under its heading) from emu-aw, emu-ax (the published text), emu-ay (my fixed text)
Each over rev-b/HG18.fixed.json (every block is replaced). For question 4: an option for Joel, not an install.
Run from humanize/: python3 fix-20261018/make_b463.py [--batch N] [--write]"""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools')); sys.path.insert(0, str(HERE))
import install_fixed as I  # noqa: E402,F401
import paragraphs_alone as PA  # noqa: E402
import para_chance as PC  # noqa: E402
import make_b446 as B  # noqa: E402
import compose_v as CV  # noqa: E402
from mkbatch import write_batch  # noqa: E402

B.PC = PC
rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
num = int(sys.argv[sys.argv.index('--batch') + 1]) if '--batch' in sys.argv else 463
dirs = [d for d in sorted(HERE.glob('b4*')) if list(d.glob('*-results.json'))]
seen = set(PA.results(dirs))
OUT = HERE / 'rf-ze'
OUT.mkdir(exist_ok=True)
PUB = 'articles/inner-signal/humanize/source/published-20260928.md'
BASE = 'rev-b/HG18.fixed.json'
SETS = {'a': 'emu-aw', 'b': 'emu-ax', 'c': 'emu-ay'}
WHY = ('; HG18 read AI in every version but one (459g HG18-ma, which lost four safety statements); one run over a stuck '
       'section: 4 of 6 Human in 459g-461g')
PLAN = [('w', lambda f: [{'blocks': [1, 2, 3, 4, 5, 6], 'folder': f}], 0.5, 'the whole section in one new run (%s)')]
drafts, gate, preds = {}, {}, {}
for tag, wins, c, why in PLAN:
    for s, folder in SETS.items():
        keep = HERE / 'rf-v' / 'HG18.units.json'  # compose_v writes here; an earlier choice's file there is kept
        was = keep.read_bytes() if keep.exists() else None
        try:
            o = CV.compose('HG18', {'base': BASE, 'windows': wins(folder)})
        except AssertionError as e:
            print('skip', tag, s, e); continue
        f = OUT / ('HG18.%s%s.json' % (tag, s))
        keep.rename(f)
        if was is not None:
            keep.write_bytes(was)
        name = 'HG18-%s%s' % (tag, s)
        text = '\n\n'.join(p for u in o['units'] for p in u['paras'])
        files = sorted({u['file'] for u in o['units'] if u.get('file') and pathlib.Path(u['file']).exists()})
        base_rec = {'kind': 'emulate', 'emulate': [rel(x) for x in files], 'fixed': [rel(HERE / BASE)], 'lint': 'REVIEW', 'published': PUB}
        drafts[name] = text
        gate[name] = dict(base_rec)
        preds[name] = ('Human' if c >= 0.5 else 'AI', c, (why % folder) + WHY)
        B.para_items('HG18', f, dict(base_rec, section='%dg %s (this batch)' % (num, name)), 'checked with its screen (%s)' % name,
                     seen, drafts, gate, preds, tag + s)
print(len(drafts), 'texts:', ' '.join(drafts))
if '--write' in sys.argv:
    intro = 'Pangram\'s web app. New samples of HG18, each screened whole with its paragraph checks. Predictions written before the run.'
    write_batch(HERE, num, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
