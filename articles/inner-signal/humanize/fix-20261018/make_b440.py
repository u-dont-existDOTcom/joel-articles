"""Batch 440g (2026-10-18): Emulate screens with sixth samples (emu-k): the induction's opening (HG17 B1-B2, AI in every
sample so far) with the rest as 438g (emu-i, Mostly Human there), and the NLP appendix with its one 68-word window of
439g (B40-B43) re-run. Never installed as they are. Run from humanize/: python3 fix-20261018/make_b440.py"""
import pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
from assemble import assembled  # noqa: E402
from mkbatch import write_batch  # noqa: E402

PUB = 'articles/inner-signal/humanize/source/published-20260928.md'
rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
A, C, E, F, G, HH, I, J, K = (HERE / x for x in ('emu-a', 'emu-c', 'emu-e', 'emu-f', 'emu-g', 'emu-h', 'emu-i', 'emu-j', 'emu-k'))
SKIP31 = {'emu-g/HG31-r1-s4', 'emu-g/HG31-r1-s5', 'emu-g/HG31-r1-s7', 'emu-g/HG31-r1-s8'}
P = {
 'HG17-emuK': ('HG17', [A, E, G, HH, I, K], (), 'Mixed', 0.40, 'the opening from a sixth sample (AI in all five before), the rest as 438g (Mostly Human, AI 0.05)'),
 'HG31-emuK': ('HG31', [E, F, G, HH, I, J, K], SKIP31, 'Human', 0.45, '439g (one 68-word window, Mostly Human) with that window from a sixth sample'),
}
drafts, gate, preds = {}, {}, {}
for name, (k, dirs, skip, mine, ch, why) in P.items():
    text, changed, files = assembled(k, dirs, skip=skip)
    drafts[name] = text
    gate[name] = {'kind': 'emulate', 'emulate': [rel(f) for f in files], 'published': PUB, 'lint': 'REVIEW',
                  'blocks_changed': sorted(changed), 'baseline': '429g ' + k, 'emu': [d.name for d in dirs], 'skip': sorted(skip)}
    preds[name] = (mine, ch, why)
intro = 'Pangram\'s web app. Emulate screens with sixth samples (`emu-k`). Never installed as they are. Predictions written before the run.'
write_batch(HERE, 440, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
