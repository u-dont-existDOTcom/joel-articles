#!/usr/bin/env python3
"""Turn 121: Hearthwork: Taking Turns read AI as a section alone (t121_hearthwork, every window AI; check_hearthwork.py), so
it is narrowed to its three paragraphs before anything in it is tried again (gate E343). Each paragraph alone, as Pangram
sees it on the post; predictions first.

  python3 check_paragraphs.py [--dry]     writes TEXTS-2.json and texts/t121_hw_p<N>.txt; without --dry, the predictions"""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
SEC = (HERE / 'texts' / 't121_hearthwork.txt').read_text(encoding='utf-8').split('\n')
assert SEC[0] == 'Hearthwork: Taking Turns' and len(SEC) == 4
CALLS = {
    1: ('AI', 0.3, 'the fragment run "Equal time. Attention without ... You speak. I listen. Then we switch. Presence, Warmth, Discipline, '
                   'Confidentiality."; "because modern life rarely gives you anything like it"',
        'his "kind of a third type of relationship"',
        'the section\'s first window (its heading and this paragraph\'s list, 32 words) read AI Medium; the list of fragments and the '
        'triple beat are the likeliest carriers'),
    2: ('AI', 0.3, 'the job-by-job mapping ("lend you the Nurturer", "lends you the Protector", "don\'t act as your Guide"); "If you say no, '
                   'they don\'t push. But ..."',
        'the two quoted thoughts, "Oh, I know what this is about" and "Here\'s what you should do"',
        'its windows read AI at Low, High, Medium, High, Medium and High in the section; the schematic one-job-a-sentence mapping reads '
        'as a model\'s explanation'),
    3: ('AI', 0.4, 'the triplet "show you a capacity, help you get the hang of it, and give it back to you"; the balanced closer '
                   '"Professional therapy\'s still useful for what it does, and peers and community do something else"',
        'his aside about the driving instructor; "Is that therapy? Well, not the mainstream kind, but yes, for sure."',
        'in the section its windows read AI at Medium, High (the aside\'s sentence), Low and Medium; in round 8\'s whole half the same '
        'sentences read Human, so the paragraph may still read AI alone'),
}
texts = {}
for n in (1, 2, 3):
    name = 't121_hw_p%d' % n
    texts[name] = SEC[n]
    (HERE / 'texts' / (name + '.txt')).write_text(SEC[n], encoding='utf-8')
(HERE / 'TEXTS-2.json').write_text(json.dumps(texts, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
for k, v in texts.items():
    print(k, len(v.split()), 'words')
if '--dry' in sys.argv:
    sys.exit(0)
for n, (call, chance, tells, human, diag) in CALLS.items():
    name = 't121_hw_p%d' % n
    cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER), '--lineage', 'ic-t121-hw-p%d' % n,
           '--scope', 'paragraph', '--text', str(HERE / 'texts' / (name + '.txt')), '--call', call, '--chance', str(chance),
           '--tells', tells, '--human-tells', human, '--diagnosis', diag,
           '--decides', 'which of the section\'s paragraphs carry its AI reading, for the marking page', '--key', name,
           '--batch', 't121-api-2']
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stdout + r.stderr)
    print(r.stdout.strip().split('\n')[-1])
