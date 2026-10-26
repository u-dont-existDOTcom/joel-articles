#!/usr/bin/env python3
"""Turn 115, API batch 1, predictions first: each block the pass changed (experiments/t115-pass/fixes.py), as it would read
with the change, a heading with its paragraphs up to the next heading (the way earlier turns checked a section), from
CANDIDATE-ARTICLE.md. The target is every window Human with High confidence (E276 (Inner Child)), so record.py lists the
windows below High as well as the AI ones. The whole-guide check comes after Joel's answers in the docx.

--chance is my chance of a 100% Human result (pangram_ledger.py).

  python3 batch1.py [--dry]      writes TEXTS-1.json and texts/, and the predictions (batch t115-api-1)"""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
BATCH = 't115-api-1'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from paragraphs_alone import reader_blocks, plain  # noqa: E402
from substack_check_text import smart  # noqa: E402

CAND = (HERE.parent / 't115-pass' / 'CANDIDATE-ARTICLE.md').read_text(encoding='utf-8')


class Texts:
    def __init__(self, md):
        self.seq = reader_blocks(re.sub(r'<!--.*?-->', '', md, flags=re.S))

    @staticmethod
    def line(kind, b):
        t = plain(re.sub(r'^#+\s*', '', b) if kind == 'h' else b)
        return smart(t).replace('‍', '').replace('️', '')

    def h2(self, heading):
        hits = [i for i, (k, b) in enumerate(self.seq) if k == 'h' and re.sub(r'^#+\s*', '', b) == heading]
        assert len(hits) == 1, (heading, hits)
        i = hits[0]
        out = [self.line(*self.seq[i])]
        for k, b in self.seq[i + 1:]:
            if k == 'h':
                break
            if k == 'p':
                out.append(self.line(k, b))
        return '\n'.join(out)


T = Texts(CAND)
texts, names, preds, fixes_of = {}, {}, {}, {}


def add(key, heading, fixes, chance, diagnosis, human):
    name = 't115_' + key
    texts[name], names[name], fixes_of[name] = T.h2(heading), '%s, with %s' % (heading, ' and '.join(fixes)), fixes
    preds[name] = ('ic-t115-' + key, 'section', chance, diagnosis, human)


add('borrow', 'Borrow Love—or Borrow the Perspective of Care', ['F01', 'F02'], 0.6,
    'try 1 for P2 and P4: P2 without its short tidy instruction between the image and the reassurance (Low 0.829 in round 8); '
    'P4 with its image, filler, packaged example and reassuring follow-up out (AI Low 0.668 and Medium 0.933). Target: every window High',
    'his P1 (the chocolate river) and his P3 (Solomon\'s paradox)')
add('lovewait', "Love Doesn't Have to Wait for Trust ❤️", ['F03'], 0.7,
    'try 1 for P7: its short balanced instruction and its tidy prediction cut (Low 0.503 and 0.848 in round 8); answering what\'s '
    'serious stays in P5\'s question and the Mr. Rogers paragraph. Target: every window High', 'his bedtime story; the Mr. Rogers scene')
add('crisis', 'If You Want to Kill Yourself', ['F04'], 0.5,
    'try 1 for P1 (safety): the question answered by a knock-down made one condition of the same instruction, and the disclaimer '
    'with its reframe made one plain statement of what the steps are for (three AI Low windows in round 8). His P2 is in the block '
    'unchanged (Low 0.805 in round 8). Target: every window High', 'his P2 ("before getting all philosophical", "the adult lending library")')
add('writeit', "Write It. Don't Send It Yet.", ['F05'], 0.7,
    'try 1 for the last paragraph: its balanced inversion said plainly (Low 0.868 in round 8). Target: every window High',
    'his Tyler story and his Lao Tsu line')
add('forgive', 'How to Forgive Without Forgetting', ['F06'], 0.65,
    'try 1 for P3: its short knock-down joined to the sentence before as a clause about the people (Low 0.855, Medium 0.961). '
    'Target: every window High', 'his first sentence of P2 and his guide\'s limitations line')
add('worthy', 'You Are Worthy of Love. Always.', ['F07'], 0.55,
    'try 1: the follow-up that explains his guide\'s line and the short reassurance cut (Low 0.829, Medium 0.909). A short block, '
    'so the confidence may stay below High on length alone. Target: every window High', 'his guide\'s "You are more than your pain and your past."')
add('stages', 'Five Stages of Reparenting', ['F08'], 0.65,
    'try 1: the aphoristic closer cut from the paragraph after the stages (Medium 0.950). Target: every window High',
    'his five stages, in his words')
add('lovecoming', "If the Love Isn't Coming Yet", ['F09'], 0.6,
    'try 1: "That doesn\'t close the door, though, it just means" cut to "That just means" (not-X, it-just-Y; Medium 0.986). '
    'Target: every window High', 'his truce sentence in P3')
add('remember', 'Remember When You Already Did It', ['F10'], 0.65,
    'try 1: the parenthetical question and its short answer said as one condition (Medium 0.981). Target: every window High',
    'his father\'s suggestion and his sister\'s line')
add('notice', 'Notice the Part That Came Here', ['F11', 'F12'], 0.6,
    'try 1: P1\'s stock phrase and its restating follow-up made one instruction (Medium 0.943); P2\'s reassuring permission cut '
    '(Medium 0.974). Target: every window High', '"No. I hate myself."')

(HERE / 'TEXTS-1.json').write_text(json.dumps(texts, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
(HERE / 'texts').mkdir(exist_ok=True)
for n, x in texts.items():
    (HERE / 'texts' / (n + '.txt')).write_text(x, encoding='utf-8')
(HERE / 'NAMES.json').write_text(json.dumps({'names': names, 'fixes': fixes_of}, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
for n, x in texts.items():
    print('%-18s %4d words | %s' % (n, len(x.split()), x[:70].replace('\n', ' / ')))
print(sum(len(x.split()) for x in texts.values()), 'words in all')
if '--dry' in sys.argv:
    sys.exit(0)
for n, (lin, scope, chance, diag, human) in preds.items():
    cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER), '--lineage', lin, '--scope', scope,
           '--text', str(HERE / 'texts' / (n + '.txt')), '--call', 'Human', '--chance', str(chance), '--tells', 'none named after the change',
           '--human-tells', human, '--diagnosis', diag, '--decides', 'whether the turn-115 change goes in, and what stays shaded in the docx',
           '--key', n, '--batch', BATCH]
    out = subprocess.run(cmd, capture_output=True, text=True)
    if out.returncode:
        sys.exit(out.stdout + out.stderr)
    print(out.stdout.strip().split('\n')[-1])
