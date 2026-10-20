"""Batch 439g (2026-10-18): Emulate screens with the fifth samples (emu-j) of 438g's small windows (HG17, HG37, HG38+39,
HG31), and Appendix A (HG29+30) as 438g read it but mapped right: the mapper had taken Emulate's "Iteration (revise the
prompt...)" for the heading "Core prompts", so that line was lost and the fallback paragraphs sat under the wrong heading.
Never installed as they are. Run from humanize/: python3 fix-20261018/make_b439.py"""
import pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
from assemble import assembled  # noqa: E402
from mkbatch import write_batch  # noqa: E402

PUB = 'articles/inner-signal/humanize/source/published-20260928.md'
rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
A, C, E, F, G, HH, I, J = (HERE / x for x in ('emu-a', 'emu-c', 'emu-e', 'emu-f', 'emu-g', 'emu-h', 'emu-i', 'emu-j'))
SKIP31 = {'emu-g/HG31-r1-s4', 'emu-g/HG31-r1-s5', 'emu-g/HG31-r1-s7', 'emu-g/HG31-r1-s8'}
P = {
 'HG17-emuJ': ('HG17', [A, E, G, HH, I, J], (), 'Human', 0.50, '438g read Mostly Human with one 117-word Medium window (the opening, B0-B2), now from a fifth sample'),
 'HG37-emuJ': ('HG37', [A, C, G, HH, I, J], (), 'Human', 0.50, '438g\'s one 40-word window (the mantra, B17) from a fifth sample'),
 'HG38+39-emuJ': ('HG38+39', [A, C, G, HH, I, J], (), 'Mixed', 0.40, 'the Appendix J opening (B3-B6), AI in every sample so far, from a fifth'),
 'HG31-emuJ': ('HG31', [E, F, G, HH, I, J], SKIP31, 'Mixed', 0.40, '438g\'s three small windows (20, 68 and 112 words) from fifth samples; windows have moved each round'),
 'HG29+30-emuI2': ('HG29+30', [A, G, HH, I], (), 'Human', 0.70, '438g\'s Human version with the Iteration line back and the heading where it belongs'),
}
drafts, gate, preds = {}, {}, {}
for name, (k, dirs, skip, mine, ch, why) in P.items():
    text, changed, files = assembled(k, dirs, skip=skip)
    drafts[name] = text
    gate[name] = {'kind': 'emulate', 'emulate': [rel(f) for f in files], 'published': PUB, 'lint': 'REVIEW',
                  'blocks_changed': sorted(changed), 'baseline': '429g ' + k, 'emu': [d.name for d in dirs], 'skip': sorted(skip)}
    preds[name] = (mine, ch, why)
intro = ('Pangram\'s web app. Emulate screens with fifth samples (`emu-j`), and Appendix A mapped right. Never installed '
         'as they are. Predictions written before the run.')
write_batch(HERE, 439, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
