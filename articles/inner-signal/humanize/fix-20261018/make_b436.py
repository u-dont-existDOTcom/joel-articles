"""Batch 436g (2026-10-18): Emulate screens with the second samples (emu-g) of the runs inside the AI windows of the
last screens: HG04, HG16 and HG29+30 (431g's windows, emu-a around them; emu-d's first samples read worse in 433g and
are left out), HG17 (433g, emu-a and emu-e), HG37 and HG38+39 (433g, emu-a and emu-c), and HG31 (435g's one 166-word
window: only the two samples inside it; its four others sit in stretches that read Human in 435g). Never installed as
they are. Run from humanize/: python3 fix-20261018/make_b436.py"""
import pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
from assemble import assembled  # noqa: E402
from mkbatch import write_batch  # noqa: E402

PUB = 'articles/inner-signal/humanize/source/published-20260928.md'
rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
A, C, E, F, G = (HERE / x for x in ('emu-a', 'emu-c', 'emu-e', 'emu-f', 'emu-g'))
SKIP31 = {'emu-g/HG31-r1-s4', 'emu-g/HG31-r1-s5', 'emu-g/HG31-r1-s7', 'emu-g/HG31-r1-s8'}
P = {
 'HG04': ([A, G], (), 'Mixed', 0.35, '431g\'s one AI window (B3-B4) from a second sample of the run whose first sample read AI throughout in 433g'),
 'HG16': ([A, G], (), 'Mixed', 0.30, '431g\'s 418-word AI window from second samples of three runs; their first samples read AI throughout in 433g'),
 'HG29+30': ([A, G], (), 'Mixed', 0.35, 'the prompt list (431g\'s 163-word window) from a second sample; the first read worse in 433g'),
 'HG17': ([A, E, G], (), 'Mixed', 0.30, 'the induction: ten second samples in 433g\'s three AI windows (1,283 words); 2,500 words gives Pangram many windows'),
 'HG37': ([A, C, G], (), 'Mixed', 0.35, 'the hostile-presences appendix: five second samples in 433g\'s 804-word AI window'),
 'HG38+39': ([A, C, G], (), 'Mixed', 0.35, 'the induction library: seven second samples in 433g\'s 711-word AI window'),
 'HG31': ([E, F, G], SKIP31, 'Mixed', 0.40, 'the NLP appendix as 435g (Mostly Human) with two second samples in its one 166-word AI window; three blocks of that window are not re-run'),
}
drafts, gate, preds = {}, {}, {}
for k, (dirs, skip, mine, ch, why) in P.items():
    text, changed, files = assembled(k, dirs, skip=skip)
    name = k + '-emuG'
    drafts[name] = text
    gate[name] = {'kind': 'emulate', 'emulate': [rel(f) for f in files], 'published': PUB, 'lint': 'REVIEW',
                  'blocks_changed': sorted(changed), 'baseline': '429g ' + k, 'emu': [d.name for d in dirs], 'skip': sorted(skip)}
    preds[name] = (mine, ch, why)
intro = ('Pangram\'s web app. Emulate screens with second samples (`emu-g`) of the runs inside the last screens\' AI windows. '
         'Never installed as they are. Predictions written before the run.')
write_batch(HERE, 436, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
