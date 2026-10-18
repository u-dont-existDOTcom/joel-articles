"""Batch 432g (2026-10-18): Emulate screens of four sections whose first runs Emulate restructured (HG13, HG32, HG33,
HG40), now from smaller heading-free runs (emu-b, emu_runs.py split), and a probe of Joel's table-of-contents note (the
40-word AI window of 431g's HG02+03) after the first section instead of before the introduction.
Run from humanize/: python3 fix-20261018/make_b432.py"""
import pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
from assemble import assembled, kb  # noqa: E402
from mkbatch import write_batch  # noqa: E402

PUB = 'articles/inner-signal/humanize/source/published-20260928.md'
rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
EMU = [HERE / 'emu-a', HERE / 'emu-b']
P = {
 'HG13': ('Human', 0.75, 'the map of the mind from three smaller runs; its scripts are short quoted lines'),
 'HG32': ('Human', 0.75, 'the de-hypnosis checklist, its questions run as Emulate wrote them'),
 'HG33': ('Human', 0.70, 'the anxiety appendix; one 38-word stretch is still the published text (under Emulate\'s minimum)'),
 'HG40': ('Human', 0.75, 'the sources, one run a paragraph; book titles and page numbers as they were'),
}
drafts, gate = {}, {}
for k in P:
    text, changed, files = assembled(k, EMU)
    assert changed, k
    drafts[k + '-emuB'] = text
    gate[k + '-emuB'] = {'kind': 'emulate', 'emulate': [rel(f) for f in files], 'published': PUB, 'lint': 'REVIEW',
                         'blocks_changed': sorted(changed), 'baseline': '429g ' + k}
preds = {k + '-emuB': v for k, v in P.items()}
# the probe: his note (heading and line, as published) after section 1's Emulate text, the way it sits in the guide
t1, ch1, f1 = assembled('HG01', [HERE / 'emu-a'])
toc = '\n\n'.join(p for _, p, _ in kb()['HG02+03'][:2])
drafts['HG01+TOC-probe'] = t1 + '\n\n' + toc
gate['HG01+TOC-probe'] = {'kind': 'emulate', 'emulate': [rel(f) for f in f1], 'published': PUB, 'lint': 'REVIEW',
                          'probe': 'his table-of-contents note with the section before it, not as the first 40 words of a text'}
preds['HG01+TOC-probe'] = ('Human', 0.65, 'his casual note ("kinda") read AI low only as the first 40 words of 431g\'s text; after 157 Human words it is inside a longer window')
intro = ('Pangram\'s web app. Emulate screens of four sections from smaller runs (`emu-b`), and a probe of Joel\'s '
         'table-of-contents note after section 1. Never installed as they are. Predictions written before the run.')
write_batch(HERE, 432, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
