"""Batch 445g (2026-10-18): screens with the emu-s refix runs (make_emu_s.py), predictions first.

  HG18, HG23, HG36    443g's refix screens that read AI in one window: that window again from my fixed text (emu-s over emu-r)
  HG24, HG29+30       441g's fixed sections that read AI: their AI windows rewritten from the fixed text (first refix sample)
  HG04, HG06          sections that read Human whole (441g, 434g) whose paragraphs read AI alone in 442g: those paragraphs
                      rewritten from the fixed text; the whole section and the new paragraphs' checks (para_texts)

Predictions: first refix samples read Human 17 of 21 in 443g (0.75 here); a second sample of a window that read AI in a
refix 0.55 (whole-window second samples of the screens: 9 of 20 in 437g to 440g); a whole section that read Human with
only a few paragraphs new 0.7; a new paragraph's check as in 442g (the community lane's rate for its length, 0.70 to 0.79).
Run from humanize/: python3 fix-20261018/make_b445.py [--write]"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
import refix_runs as R  # noqa: E402
import install_fixed as I  # noqa: E402
import paragraphs_alone as PA  # noqa: E402
from mkbatch import write_batch  # noqa: E402

rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
ER, ES = HERE / 'emu-r', HERE / 'emu-s'
g434 = json.loads((HERE / 'b434' / 'GATE.json').read_text(encoding='utf-8'))
g441 = json.loads((HERE / 'b441' / 'GATE.json').read_text(encoding='utf-8'))
PLAN = [  # key, gate record of its fixed version, refix folders, chance, why
    ('HG18', g434, [ER, ES], 0.55, 'a second refix sample of the one window (158 words) that read AI in 443g'),
    ('HG23', g434, [ER, ES], 0.55, 'a second refix sample of the stretch whose 78-word window read AI in 443g'),
    ('HG36', g434, [ER, ES], 0.55, 'a second refix sample of the window (217 words) that read AI in 443g'),
    ('HG24', g441, [ES], 0.75, 'its 441g AI windows (1,047 words) rewritten from the fixed text; first refix samples: 17 of 21 Human'),
    ('HG29+30', g441, [ES], 0.75, 'its 441g AI window (513 words) rewritten from the fixed text; first refix samples: 17 of 21 Human'),
    ('HG04', g441, [ES], 0.7, 'Human whole in 441g; P1 and P2, which read AI alone in 442g, rewritten from the fixed text'),
    ('HG06', g434, [ES], 0.7, 'Human whole in 434g; P3, P4 and P6, which read AI alone in 442g, rewritten from the fixed text (P5, a quotation, kept)'),
]
drafts, gate, preds = {}, {}, {}
dirs = [d for d in sorted(HERE.glob('b4*')) if list(d.glob('*-results.json'))]
seen = set(PA.results(dirs))
for key, g, folders, c, why in PLAN:
    rec = g[key + '-fix']
    fixed = HERE / rec['reviews']
    text, files = R.assembled_fixed(fixed, folders)
    name = key + '-refix' + ('2' if ER in folders and ES in folders else '')
    drafts[name] = text
    base = {'kind': 'emulate', 'emulate': (rec.get('emulate') or []) + [rel(f) for f in files], 'published': rec.get('published'),
            'fixed': [rel(fixed)], 'lint': 'REVIEW', 'runs': sorted(pathlib.Path(f).parent.name + '/' + pathlib.Path(f).name for f in files)}
    gate[name] = dict(base, refix_of='%s %s-fix' % ('434g' if g is g434 else '441g', key))
    preds[name] = ('Human' if c >= 0.5 else 'Mixed', c, why)
    if key in ('HG04', 'HG06'):
        u = R.units_fixed(fixed, folders)
        uf = HERE / 'rf-a' / ('%s.units-s.json' % key)
        uf.write_text(json.dumps(u, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        md = I.section_md(uf)
        for i, t, x in I.para_texts(md, seen):
            kind = 'alone' if x == t else ('next' if x.startswith(t) else ('prev' if x.endswith(t) else 'run'))
            pn = '%s-s-p%d%s' % (key, i + 1, '' if kind == 'alone' else '+' + kind)
            drafts[pn] = x
            gate[pn] = dict(base, paragraph=i + 1, check=kind, section='445g %s (this batch)' % name)
            w = len(x.split())
            pc = 0.70 if w < 80 else (0.77 if w < 120 else 0.79)
            preds[pn] = ('Human', pc, 'paragraph %d of %s with the emu-s stretch (%s), %d words; the community lane\'s rate for this length' % (i + 1, key, kind, w))
print(len(drafts), 'texts:', ' '.join(drafts))
if '--write' in sys.argv:
    intro = ('Pangram\'s web app. Screens with the emu-s refix runs: second samples of 443g\'s AI windows, first refix samples of '
             '441g\'s, and new versions of the paragraphs that read AI alone in 442g (with their paragraph checks). Never installed '
             'from here. Predictions written before the run.')
    write_batch(HERE, 445, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
