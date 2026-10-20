"""Batch 430g (2026-10-18): the first Emulate screens of the hypnosis guide. Six sections that read AI in the baseline
(429g), each with its flagged blocks replaced by Emulate's output (emu-a, the API, one call a section, the headings kept
in the paste as lines), headings and Human-read blocks as published. Emulate texts: no word of mine (the gate checks
every block against the run outputs and the published text). Only the ones that read Human go on to the meaning
reviews; none is installed as it is. Run from humanize/: python3 fix-20261018/make_b430.py"""
import pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
from assemble import assembled  # noqa: E402
from mkbatch import write_batch  # noqa: E402

PUB = 'articles/inner-signal/humanize/source/published-20260928.md'
rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
KEYS = ['HG06', 'HG07', 'HG10', 'HG11', 'HG22', 'HG27']
drafts, gate = {}, {}
for k in KEYS:
    text, changed, files = assembled(k, [HERE / 'emu-a'])
    name = k + '-emuA'
    drafts[name] = text
    gate[name] = {'kind': 'emulate', 'emulate': [rel(f) for f in files], 'published': PUB, 'lint': 'REVIEW',
                  'blocks_changed': sorted(changed), 'baseline': '429g ' + k}
preds = {
    'HG06-emuA': ('Human', 0.60, 'Emulate\'s long, loose sentences ("etc.", "Since there are a lot of forces out there"); the quoted FTC and OECD lines are its own'),
    'HG07-emuA': ('Human', 0.55, 'his story as published (Human in 429g) and Emulate\'s closer, which is still formal ("Under no circumstances allow")'),
    'HG10-emuA': ('Human', 0.70, 'question-and-answer lines ("Is there REAL (not magical) evidence for Hypnosis? Yes."), list lines without full stops'),
    'HG11-emuA': ('Human', 0.60, 'a loose first paragraph and an exclamation at the end, but the parallel "The mind of love ... The mind of analysis" run stays'),
    'HG22-emuA': ('Human', 0.70, 'two long run-on sentences in British spelling, the dishes as a rambling clause'),
    'HG27-emuA': ('Human', 0.65, 'plain advice in long sentences ("Work on loving yourself, so that ..."), no aphorisms left'),
}
intro = ('Pangram\'s web app. Emulate screens: six sections of the hypnosis guide that read AI in the baseline (429g), with '
         'their flagged blocks replaced by Emulate\'s output (`emu-a`), headings and Human-read blocks as published. Never '
         'installed as they are; the ones that read Human go on to the meaning reviews. Predictions written before the run.')
write_batch(HERE, 430, drafts, gate, preds, intro, lint_article=H / "HUMANIZED-SO-FAR.md")
