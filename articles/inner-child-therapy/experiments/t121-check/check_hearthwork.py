#!/usr/bin/env python3
"""Turn 121: the section check after his aside went back into Hearthwork: Taking Turns (Joel, 2026-11-04 12:02 UTC, "ok"
to my turn-120 question; experiments/t121-answers/JOEL-20261104-1202.md).

Round 9 (experiments/t120-results/) read the guide's only AI window there: B window 24, two sentences of his, "The peer
doesn't become your permanent parent, though. They show you a capacity, ..., which is borrowed adulthood in its healthiest
form." (AI, Low, 35 words), with the section's two Low windows on either side of it ("You speak. I listen. Then we switch.",
B 18, and "Is that therapy?", B 25). In round 8 the second sentence still ended with his aside "(a driving instructor isn't
planning to drive you around forever either)" and read Human at High (38 words); he cut the aside in his reorganization
(experiments/t116-joel/EDITS.json). This is the section with the aside back: its heading and three paragraphs, 279 words,
a check the API may take (E218: a section, not more than five or six paragraphs), as Pangram sees it on the post (the
quote marks curled, the standard swap's straight ones being the master's). The prediction goes in first.

  python3 check_hearthwork.py [--dry]     writes TEXTS.json and texts/t121_hearthwork.txt; without --dry, the prediction"""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from paragraphs_alone import reader_blocks, plain  # noqa: E402
from substack_check_text import smart  # noqa: E402

ART = (ROOT / 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8')
seq = reader_blocks(re.sub(r'<!--.*?-->', '', ART, flags=re.S))
HEAD = 'Hearthwork: Taking Turns'
NAME = 't121_hearthwork'


def line(kind, b):
    t = plain(re.sub(r'^#+\s*', '', b) if kind == 'h' else b)
    return smart(t).replace('‍', '').replace('️', '')


i = [n for n, (k, b) in enumerate(seq) if k == 'h' and re.sub(r'^#+\s*', '', b) == HEAD][0]
out = [line(*seq[i])]
for k, b in seq[i + 1:]:
    if k == 'h':
        break
    out.append(line(k, b))
text = '\n'.join(out)
assert 'healthiest form (a driving instructor isn’t planning to drive you around forever either). Is that therapy?' in text, text[-400:]
assert len(out) == 4 and len(text.split()) < 400, (len(out), len(text.split()))
(HERE / 'texts').mkdir(exist_ok=True)
(HERE / 'texts' / (NAME + '.txt')).write_text(text, encoding='utf-8')
(HERE / 'TEXTS.json').write_text(json.dumps({NAME: text}, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(NAME, len(text.split()), 'words,', len(out) - 1, 'paragraphs')
if '--dry' in sys.argv:
    sys.exit(0)
cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER), '--lineage', 'ic-t121-hearthwork',
       '--scope', 'section', '--text', str(HERE / 'texts' / (NAME + '.txt')), '--call', 'Human', '--chance', '0.6',
       '--tells', 'the three-beat "You speak. I listen. Then we switch."; the capacity triplet "show you ..., help you ..., and give it back"',
       '--human-tells', 'his driving-instructor aside; "Is that therapy? Well, not the mainstream kind, but yes, for sure."',
       '--diagnosis', 'round 9 read the second paragraph\'s first two sentences AI (Low) in half B, where round 8, with his aside, read '
       'the second one Human (High); the aside is back, so the AI window should go. Alone, a section reads harsher than in the whole '
       'guide (E-records: "a paragraph alone is harsher than the article"), so a Low or Medium window on the short lines is likely',
       '--decides', 'whether his aside clears the AI window, and which of the section\'s windows go on the marking page as Low or Medium',
       '--key', NAME, '--batch', 't121-api-1']
r = subprocess.run(cmd, capture_output=True, text=True)
if r.returncode:
    sys.exit(r.stdout + r.stderr)
print(r.stdout.strip().split('\n')[-1])
