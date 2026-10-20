"""Batch 433g (2026-10-18): Emulate screens of the eight largest sections from smaller heading-free runs (emu-c, emu-e:
emu_runs.py split; their first runs were restructured past placing), and second Emulate runs, from the published text,
for the stretches 431g read AI in HG04, HG16 and HG29+30 (emu-d over emu-a). Never installed as they are.
Run from humanize/: python3 fix-20261018/make_b433.py"""
import pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
from assemble import assembled  # noqa: E402
from mkbatch import write_batch  # noqa: E402

PUB = 'articles/inner-signal/humanize/source/published-20260928.md'
rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
A, C, D, E = (HERE / x for x in ('emu-a', 'emu-c', 'emu-d', 'emu-e'))
P = {  # key: (emu folders, mine, chance, why) written before the run
 'HG14': ([A, E], 'Human', 0.65, '2,114 words from 17 smaller runs; more windows, more chances of one AI window'),
 'HG17': ([A, E], 'Human', 0.60, 'the induction from 16 runs; one 36-word stretch is still published text'),
 'HG20': ([A, C], 'Human', 0.70, 'the response examples from 9 runs'),
 'HG24': ([A, C], 'Mixed', 0.35, 'troubleshooting: seven short stretches (under 40 words) are still the published scripts'),
 'HG31': ([A, E], 'Mixed', 0.35, 'the NLP appendix: eight short stretches still published, and 2,060 words'),
 'HG35': ([A, C], 'Human', 0.70, 'self-trust and guidance from 6 runs'),
 'HG37': ([A, C], 'Human', 0.70, 'the hostile-presences appendix from 8 runs'),
 'HG38+39': ([A, C], 'Human', 0.65, 'the induction library, one run per family; its short opening line stays published'),
 'HG04': ([A, D], 'Human', 0.70, '431g\'s one AI window (108 words) now from a second Emulate run of the published text'),
 'HG16': ([A, D], 'Human', 0.60, 'the 418-word AI window from three second runs'),
 'HG29+30': ([A, D], 'Human', 0.65, 'the prompt list (the 163-word AI window) from a second run'),
}
drafts, gate, preds = {}, {}, {}
for k, (dirs, mine, ch, why) in P.items():
    text, changed, files = assembled(k, dirs)
    assert changed, k
    name = k + '-emuC'
    drafts[name] = text
    gate[name] = {'kind': 'emulate', 'emulate': [rel(f) for f in files], 'published': PUB, 'lint': 'REVIEW',
                  'blocks_changed': sorted(changed), 'baseline': '429g ' + k, 'emu': [d.name for d in dirs]}
    preds[name] = (mine, ch, why)
intro = ('Pangram\'s web app. Emulate screens of the eight largest sections from smaller runs (`emu-c`, `emu-e`), and of '
         'three sections with second runs where 431g read AI (`emu-d`). Never installed as they are. Predictions written '
         'before the run.')
write_batch(HERE, 433, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
