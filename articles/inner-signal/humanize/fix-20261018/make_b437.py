"""Batch 437g (2026-10-18): Emulate screens with the third samples (emu-h): each AI window of 436g (435g for HG24) sent
whole, with its headings, as one run, put in over everything earlier that it overlaps. HG24 takes 433g's base (emu-a
and emu-c read Human up to "You dissociate"), not 435g's short pieces. Never installed as they are.
Run from humanize/: python3 fix-20261018/make_b437.py"""
import pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
from assemble import assembled  # noqa: E402
from mkbatch import write_batch  # noqa: E402

PUB = 'articles/inner-signal/humanize/source/published-20260928.md'
rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
A, C, E, F, G, HH = (HERE / x for x in ('emu-a', 'emu-c', 'emu-e', 'emu-f', 'emu-g', 'emu-h'))
SKIP31 = {'emu-g/HG31-r1-s4', 'emu-g/HG31-r1-s5', 'emu-g/HG31-r1-s7', 'emu-g/HG31-r1-s8'}
P = {
 'HG04': ([A, HH], (), 'Mixed', 0.40, 'a new sample of the whole section in one run (436g\'s window covered all of it); emu-a\'s whole run read Human around one 108-word window in 431g'),
 'HG16': ([A, G, HH], (), 'Mixed', 0.40, '436g\'s 210-word window (B11-B19) from one run of its published blocks'),
 'HG29+30': ([A, G, HH], (), 'Mixed', 0.40, '436g\'s 105-word window (the scripts for daydreaming, anxiety and the rest) from one run'),
 'HG17': ([A, E, G, HH], (), 'Mixed', 0.35, 'the induction\'s two AI windows of 436g (536 and 414 words) from two whole runs; 2,500 words'),
 'HG37': ([A, C, G, HH], (), 'Mixed', 0.35, 'the hostile-presences appendix\'s two windows from two runs; Emulate dropped the headings, so its paragraphs were cut in under the published ones by word overlap'),
 'HG38+39': ([A, C, G, HH], (), 'Human', 0.45, '436g\'s two windows (176 and 101 words) from two short runs; the rest as 436g'),
 'HG31': ([E, F, G, HH], SKIP31, 'Mixed', 0.45, '436g\'s two windows (103 and 69 words) from two runs; Emulate made the second a numbered list'),
 'HG24': ([A, C, HH], (), 'Mixed', 0.45, 'troubleshooting from "You dissociate" to the end in one run (Emulate loosened it: "Go eat some food"); the start as 433g'),
}
drafts, gate, preds = {}, {}, {}
for k, (dirs, skip, mine, ch, why) in P.items():
    text, changed, files = assembled(k, dirs, skip=skip)
    name = k + '-emuH'
    drafts[name] = text
    gate[name] = {'kind': 'emulate', 'emulate': [rel(f) for f in files], 'published': PUB, 'lint': 'REVIEW',
                  'blocks_changed': sorted(changed), 'baseline': '429g ' + k, 'emu': [d.name for d in dirs], 'skip': sorted(skip)}
    preds[name] = (mine, ch, why)
intro = ('Pangram\'s web app. Emulate screens with third samples (`emu-h`): each AI window sent whole as one run. Never '
         'installed as they are. Predictions written before the run.')
write_batch(HERE, 437, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
