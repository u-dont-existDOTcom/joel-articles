#!/usr/bin/env python3
"""Turn 122: the section check of his own Hearthwork section, which replaced the one turn 121 found AI alone (his
marking-page answer HW-1, 2026-11-04 13:44 UTC: "i rewrote teh whole section, so remove and replace the whole hearthwork
section. it tests human and sounds better"; experiments/t122-answers/). He checked it himself and gave no link, so this
records its windows with their confidence (E278), as Pangram sees it on the post: its heading and four paragraphs, the quote
marks curled. It is a section of 275 words, which the API may take (E218). The prediction goes in first.

  python3 check_his_hearthwork.py [--dry]     writes TEXTS.json and texts/t122_hearthwork_his.txt; without --dry, the prediction"""
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
HEAD = 'Hearthwork: Taking Turns Lending & Borrowing Adulthood'
NAME = 't122_hearthwork_his'


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
assert len(out) == 5 and text.startswith(HEAD + '\nHearthwork is what I call my peer-counseling framework'), out[:2]
(HERE / 'texts').mkdir(exist_ok=True)
(HERE / 'texts' / (NAME + '.txt')).write_text(text, encoding='utf-8')
(HERE / 'TEXTS.json').write_text(json.dumps({NAME: text}, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(NAME, len(text.split()), 'words,', len(out) - 1, 'paragraphs')
if '--dry' in sys.argv:
    sys.exit(0)
cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER), '--lineage', 'ic-t122-hearthwork-his',
       '--scope', 'section', '--text', str(HERE / 'texts' / (NAME + '.txt')), '--call', 'Human', '--chance', '0.75',
       '--tells', 'his "There\'s also no pressure to answer." after a long sentence; "Modern life rarely gives us anything like this"',
       '--human-tells', 'his own explanations, the "middle path" between friendship and therapy, "clienting", "It\'s hard sometimes, but"',
       '--diagnosis', 'his rewrite of the section that read AI alone in turn 121 (every window AI): the premise list is now a sentence '
       'of his, the three jobs his own wording, the borrowed-adulthood paragraph gone; he checked it himself and says it reads Human',
       '--decides', 'which of his section\'s windows read below High, for the record and the next marking page if any',
       '--key', NAME, '--batch', 't122-api-1']
r = subprocess.run(cmd, capture_output=True, text=True)
if r.returncode:
    sys.exit(r.stdout + r.stderr)
print(r.stdout.strip().split('\n')[-1])
