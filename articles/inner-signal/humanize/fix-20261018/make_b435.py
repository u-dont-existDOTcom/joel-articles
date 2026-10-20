"""Batch 435g (2026-10-18): Emulate screens with the redo runs (emu-f): the introduction in four pieces (HG02+03), the
closing's first paragraph (HG27), the de-hypnosis checklist in six pieces (HG32), the anxiety appendix's three AI
stretches (HG33), and the short stretches of HG24 and HG31 with their headings. Never installed as they are.
Run from humanize/: python3 fix-20261018/make_b435.py"""
import pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
from assemble import assembled  # noqa: E402
from mkbatch import write_batch  # noqa: E402

PUB = 'articles/inner-signal/humanize/source/published-20260928.md'
rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
A, B, C, E, F = (HERE / x for x in ('emu-a', 'emu-b', 'emu-c', 'emu-e', 'emu-f'))
P = {
 'HG02+03': ([A, F], 'Human', 0.70, 'the introduction from four smaller runs; his two lines as published; his note read AI low as the first 40 words in 431g'),
 'HG27': ([A, F], 'Human', 0.75, 'the closing\'s first two paragraphs from a new run, the third Emulate\'s from 430g (Human)'),
 'HG32': ([B, F], 'Mixed', 0.40, 'the checklist from six smaller runs; 432g read Emulate\'s first version AI throughout; lists of short questions'),
 'HG33': ([B, F], 'Human', 0.60, 'the anxiety appendix with its two AI stretches from new runs'),
 'HG24': ([C, F], 'Human', 0.55, 'troubleshooting with two of its short-script stretches now Emulate\'s (with their headings); three are still published'),
 'HG31': ([E, F], 'Mixed', 0.45, 'the NLP appendix with three short stretches now Emulate\'s; 433g\'s 766-word AI window is not redone here'),
}
drafts, gate, preds = {}, {}, {}
for k, (dirs, mine, ch, why) in P.items():
    text, changed, files = assembled(k, dirs)
    name = k + '-emuF'
    drafts[name] = text
    gate[name] = {'kind': 'emulate', 'emulate': [rel(f) for f in files], 'published': PUB, 'lint': 'REVIEW',
                  'blocks_changed': sorted(changed), 'baseline': '429g ' + k, 'emu': [d.name for d in dirs]}
    preds[name] = (mine, ch, why)
intro = ('Pangram\'s web app. Emulate screens with the redo runs (`emu-f`). Never installed as they are. Predictions '
         'written before the run.')
write_batch(HERE, 435, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
