"""Batch 461g (2026-10-18): new samples of "Altered states" (HG36; make_emu_at.py), each section screened whole with its
paragraph checks, so Pangram and the second reader choose together (make_b459's way):
  HG36-sa/sb/sc   B9-B12 (the "Stabilize before you interpret" subsection, under its heading) from emu-at, emu-au, emu-av
  HG36-wa/wb/wc   the whole section (B1-B7, B9-B12) from emu-at, emu-au, emu-av
emu-at and emu-au are from my meaning-fixed text, emu-av from the published text; each over rf-p/HG36.fixed.json.
Run from humanize/: python3 fix-20261018/make_b461.py [--batch N] [--write]"""
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
num = int(sys.argv[sys.argv.index('--batch') + 1]) if '--batch' in sys.argv else 461
dirs = [d for d in sorted(HERE.glob('b4*')) if list(d.glob('*-results.json'))]
seen = set(PA.results(dirs))
OUT = HERE / 'rf-zc'
OUT.mkdir(exist_ok=True)
PUB = 'articles/inner-signal/humanize/source/published-20260928.md'
BASE = 'rf-p/HG36.fixed.json'
SETS = {'a': 'emu-at', 'b': 'emu-au', 'c': 'emu-av'}
WHY = ('; HG36\'s end read AI in every version since 455g (459g: three new B10-B11 samples, AI at the end of the whole); '
       'new-sample section screens since 454g: 15 of 35 Human')
PLAN = [('s', lambda f: [{'blocks': [9, 10, 11, 12], 'folder': f, 'skip': ['%s/HG36-aw1' % f]}], 0.45,
         'B9-B12 in one new run (%s)'),
        ('w', lambda f: [{'blocks': [1, 2, 3, 4, 5, 6, 7], 'folder': f, 'skip': ['%s/HG36-sw1' % f]},
                         {'blocks': [9, 10, 11, 12], 'folder': f, 'skip': ['%s/HG36-sw1' % f]}], 0.5,
         'the whole section in one new run (%s); 431g\'s first whole-section run read Human')]
drafts, gate, preds = {}, {}, {}
for tag, wins, c, why in PLAN:
    for s, folder in SETS.items():
        keep = HERE / 'rf-v' / 'HG36.units.json'  # compose_v writes here; an earlier choice's file there is kept
        was = keep.read_bytes() if keep.exists() else None
        try:
            o = CV.compose('HG36', {'base': BASE, 'windows': wins(folder)})
        except AssertionError as e:
            print('skip', tag, s, e); continue
        f = OUT / ('HG36.%s%s.json' % (tag, s))
        keep.rename(f)
        if was is not None:
            keep.write_bytes(was)
        name = 'HG36-%s%s' % (tag, s)
        text = '\n\n'.join(p for u in o['units'] for p in u['paras'])
        files = sorted({u['file'] for u in o['units'] if u.get('file') and pathlib.Path(u['file']).exists()})
        base_rec = {'kind': 'emulate', 'emulate': [rel(x) for x in files], 'fixed': [rel(HERE / BASE)], 'lint': 'REVIEW', 'published': PUB}
        drafts[name] = text
        gate[name] = dict(base_rec)
        preds[name] = ('Human' if c >= 0.5 else 'AI', c, (why % folder) + WHY)
        B.para_items('HG36', f, dict(base_rec, section='%dg %s (this batch)' % (num, name)), 'checked with its screen (%s)' % name,
                     seen, drafts, gate, preds, tag + s)
print(len(drafts), 'texts:', ' '.join(drafts))
if '--write' in sys.argv:
    intro = 'Pangram\'s web app. New samples of HG36, each screened whole with its paragraph checks. Predictions written before the run.'
    write_batch(HERE, num, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
