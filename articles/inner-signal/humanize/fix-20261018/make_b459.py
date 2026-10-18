"""Batch 459g (2026-10-18): the new samples of what is still open (emu-aq, emu-ar, emu-as), every sample's section
screened whole with its paragraph checks, so Pangram and the second reader choose together:
  HG24-oa/ob/oc   B2-B8 (its opening; B1 and B4 are headings) from each set, over rf-v/HG24.fixed.json
  HG36-ea/eb/ec   B10-B11 from each set (emu-aq and emu-as from the published text, emu-ar from my fixed text)
  HG17-ma/mb      the listening script in three medium windows (B17-B21, B22-B26, B27-B31), over rf-j/HG17.fixed.json
  HG18-ma/mb      the return steps in two medium windows (B1-B3, B4-B6), over rev-b/HG18.fixed.json
Run from humanize/: python3 fix-20261018/make_b459.py [--batch N] [--write]"""
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
num = int(sys.argv[sys.argv.index('--batch') + 1]) if '--batch' in sys.argv else 459
dirs = [d for d in sorted(HERE.glob('b4*')) if list(d.glob('*-results.json'))]
seen = set(PA.results(dirs))
g444 = json.loads((HERE / 'b444' / 'GATE.json').read_text(encoding='utf-8'))
OUT = HERE / 'rf-za'
OUT.mkdir(exist_ok=True)
SETS = {'a': 'emu-aq', 'b': 'emu-ar', 'c': 'emu-as'}
LINKS = {'HG17': 'rf-v/HG17.fixed.json', 'HG24': 'rf-v/HG24.fixed.json', 'HG36': 'rf-p/HG36.fixed.json'}
PLAN = [('HG24', 'rf-v/HG24.fixed.json', [[2, 3, 5, 6, 7, 8]], 'abc', 'o', 0.45, 'its opening from a new sample; its opening read AI with and without its fixes (457g)'),  # B1, B4 are headings
        ('HG36', 'rf-p/HG36.fixed.json', [[10, 11]], 'abc', 'e', 0.5, 'B10-B11 from a new sample; a 52-56-word AI window stayed at the end in 456g and 457g'),
        ('HG17', 'rf-j/HG17.fixed.json', [list(range(17, 22)), list(range(22, 27)), list(range(27, 32))], 'ab', 'm', 0.4,
         'the listening script in three medium windows; one window lost its steps (451g), seven small ones read AI as a run (457g)'),
        ('HG18', 'rev-b/HG18.fixed.json', [[1, 2, 3], [4, 5, 6]], 'ab', 'm', 0.3, 'the return steps in two medium windows; every earlier version read AI')]
drafts, gate, preds = {}, {}, {}
for key, base, windows, sets, tag, c, why in PLAN:
    for s in sets:
        spec = {'base': base, 'windows': [{'blocks': w, 'folder': SETS[s]} for w in windows]}
        keep = HERE / 'rf-v' / ('%s.units.json' % key)  # compose_v writes here; an earlier choice's file there is kept
        was = keep.read_bytes() if keep.exists() else None
        try:
            o = CV.compose(key, spec)
        except AssertionError as e:
            print('skip', key, s, e); continue
        f = OUT / ('%s.%s%s.json' % (key, tag, s))
        keep.rename(f)
        if was is not None:
            keep.write_bytes(was)
        src = LINKS.get(key)  # the base's units lost their "links" records in rf-j; copy them from the file that has them
        if src:
            have = {tuple(u['blocks']): u['links'] for u in json.loads((HERE / src).read_text(encoding='utf-8'))['units'] if u.get('links')}
            d = json.loads(f.read_text(encoding='utf-8'))
            for u in d['units']:
                if tuple(u['blocks']) in have and not u.get('links'):
                    u['links'] = have[tuple(u['blocks'])]
            f.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        name = '%s-%s%s' % (key, tag, s)
        text = '\n\n'.join(p for u in o['units'] for p in u['paras'])
        files = sorted({u['file'] for u in o['units'] if u.get('file') and pathlib.Path(u['file']).exists()})
        base_rec = {'kind': 'emulate', 'emulate': [rel(x) for x in files], 'fixed': [rel(HERE / base)], 'lint': 'REVIEW',
                    'published': 'articles/inner-signal/humanize/source/published-20260928.md'}
        drafts[name] = text
        gate[name] = dict(base_rec)
        preds[name] = ('Human' if c >= 0.5 else 'AI', c, why + ' (%s); new-sample section screens since 454g: 11 of 25 Human' % SETS[s])
        B.para_items(key, f, dict(base_rec, section='%dg %s (this batch)' % (num, name)), 'checked with its screen (%s)' % name,
                     seen, drafts, gate, preds, tag + s)
print(len(drafts), 'texts:', ' '.join(drafts))
if '--write' in sys.argv:
    intro = 'Pangram\'s web app. New samples of the open sections, each screened whole with its paragraph checks. Predictions written before the run.'
    write_batch(HERE, num, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
