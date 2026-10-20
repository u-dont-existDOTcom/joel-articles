"""Batch 431g (2026-10-18): Emulate screens of the next 16 sections of the hypnosis guide, the same way as 430g
(make_b430.py): each section with its flagged stretches replaced by Emulate's output (emu-a), as one block for one
paragraph where Emulate kept the count, else stretch by stretch between headings (emu_runs.py back); headings, Joel's own
short lines (assemble.KEEP) and Human-read blocks as published. Never installed as they are.
Run from humanize/: python3 fix-20261018/make_b431.py"""
import pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
from assemble import assembled  # noqa: E402
from mkbatch import write_batch  # noqa: E402

PUB = 'articles/inner-signal/humanize/source/published-20260928.md'
rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))
P = {  # (mine, chance, why), written before the run
 'HG01': ('Human', 0.80, 'his opening line as published, then Emulate\'s long "How to use" paragraph (the heading ran into it)'),
 'HG02+03': ('Human', 0.80, 'his two short lines as published, the rest Emulate\'s; 6 of 6 Emulate sections read Human in 430g'),
 'HG04': ('Human', 0.80, 'Emulate\'s instructions in its loose voice; 333 words'),
 'HG12': ('Human', 0.85, 'his three middle paragraphs (Human in 429g) between Emulate\'s two stretches'),
 'HG15': ('Human', 0.70, '626 words, regrouped; long texts give Pangram more windows to flag'),
 'HG16': ('Human', 0.70, '530 words of lists and checks in Emulate\'s voice'),
 'HG18': ('Human', 0.80, 'the return instructions in Emulate\'s voice'),
 'HG19': ('Human', 0.80, 'regrouped; the scripts run into the prose ("You can say to yourself")'),
 'HG21': ('Human', 0.80, 'the daily practice, 222 words'),
 'HG23': ('Human', 0.80, 'regrouped; the rule and the scripts'),
 'HG25': ('Human', 0.75, 'a run of "do not" rules even in Emulate\'s words'),
 'HG26': ('Human', 0.75, 'safety guidance with lists of symptoms'),
 'HG28': ('Human', 0.80, 'the app description, 238 words'),
 'HG29+30': ('Human', 0.70, '579 words, the seven prompt elements as a list'),
 'HG34': ('Human', 0.80, 'regrouped; the list of actions as quoted phrases'),
 'HG36': ('Human', 0.80, 'regrouped; Emulate\'s casual altered-states note'),
}
drafts, gate = {}, {}
for k in P:
    text, changed, files = assembled(k, [HERE / 'emu-a'])
    assert changed, k
    drafts[k + '-emuA'] = text
    gate[k + '-emuA'] = {'kind': 'emulate', 'emulate': [rel(f) for f in files], 'published': PUB, 'lint': 'REVIEW',
                         'blocks_changed': sorted(changed), 'baseline': '429g ' + k}
preds = {k + '-emuA': v for k, v in P.items()}
intro = ('Pangram\'s web app. Emulate screens, as in 430g: 16 more sections of the hypnosis guide with their flagged '
         'stretches replaced by Emulate\'s output (`emu-a`). Never installed as they are. Predictions written before the run.')
write_batch(HERE, 431, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
