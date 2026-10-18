"""Batch 438g (2026-10-18): Emulate screens with the fourth samples (emu-i), after 437g: HG17, HG37 and HG31 with their 437g
window as one run again; HG29+30 whole; HG38+39 from Appendix I to the second family (B0-B8). Never installed as they are.
Run from humanize/: python3 fix-20261018/make_b438.py"""
import pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
from assemble import assembled  # noqa: E402
from mkbatch import write_batch  # noqa: E402

PUB = 'articles/inner-signal/humanize/source/published-20260928.md'
rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
A, C, E, F, G, HH, I = (HERE / x for x in ('emu-a', 'emu-c', 'emu-e', 'emu-f', 'emu-g', 'emu-h', 'emu-i'))
SKIP31 = {'emu-g/HG31-r1-s4', 'emu-g/HG31-r1-s5', 'emu-g/HG31-r1-s7', 'emu-g/HG31-r1-s8'}
P = {
 'HG17': ([A, E, G, HH, I], (), 'Mixed', 0.35, 'the induction\'s opening window (B0-B13, AI in 433g, 436g and 437g) from a fourth sample; the rest as 437g'),
 'HG37': ([A, C, G, HH, I], (), 'Mixed', 0.35, 'the boundary and psychosis part (B17-B32, AI in 436g and 437g) from a fourth sample, cut in by word overlap'),
 'HG31': ([E, F, G, HH, I], SKIP31, 'Human', 0.45, '437g\'s one 202-word window (parts integration and the NLP refusals) from one run; the rest as 437g (Human there)'),
 'HG29+30': ([A, G, HH, I], (), 'Mixed', 0.40, 'Appendix A whole from one run: its prompt scripts read AI in every piece-run so far'),
 'HG38+39': ([A, C, G, HH, I], (), 'Human', 0.45, 'Appendix I to the second family (B0-B8) from one run: B3 read AI in every sample so far'),
}
drafts, gate, preds = {}, {}, {}
for k, (dirs, skip, mine, ch, why) in P.items():
    text, changed, files = assembled(k, dirs, skip=skip)
    name = k + '-emuI'
    drafts[name] = text
    gate[name] = {'kind': 'emulate', 'emulate': [rel(f) for f in files], 'published': PUB, 'lint': 'REVIEW',
                  'blocks_changed': sorted(changed), 'baseline': '429g ' + k, 'emu': [d.name for d in dirs], 'skip': sorted(skip)}
    preds[name] = (mine, ch, why)
intro = ('Pangram\'s web app. Emulate screens with fourth samples (`emu-i`). Never installed as they are. Predictions '
         'written before the run.')
write_batch(HERE, 438, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
