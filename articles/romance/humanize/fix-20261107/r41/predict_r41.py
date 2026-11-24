#!/usr/bin/env python3
"""Predictions for r41's checks, before any check: the Labels section with Q-C1's words (mine), part 1 of "Primal
attraction" with his Q-S5 answer, and his own version of "Muses & Directors" in its two parts (new lineages: his words,
checked as he sent them)."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
LEDGER = ROOT / 'articles/romance/humanize/pangram-ledger.jsonl'
DET = "pangram 4.1, the web app (Joel's account, GUI credits)"
COMMON = ['--scope', 'section', '--call', 'Human', '--batch', 'romance-r41', '--detector', DET]
JOBS = [
    ('09', ['--lineage', 'romance-e307-09', '--receipt', str(HERE / 'receipts' / 'R-r41-09.json'), '--chance', '0.85',
            '--tells', 'the changed sentence: if a promise had to stand in for that closeness',
            '--human-tells', 'the rest of the section, which read Human High in its last check (#319)',
            '--first-fix', 'payoff: the sentence says first he needs no promise on paper; join: the condition joined to it with '
                           '"and if"; plain: "that closeness" for the hours of talk just described, nothing else added',
            '--humanized', 'one clause of his paragraph said from his Q-C1 answer',
            '--after-fix', 'the section as #319 read it, with one clause changed',
            '--diagnosis', 'the contradictions check found this red flag against the vows section; his answer says the red '
                           'flag is a promise standing in for the closeness',
            '--decides', 'whether the Labels section still reads Human High in every window with the clause said']),
    ('52', ['--lineage', 'romance-r40-primal-p1', '--receipt', str(HERE / 'receipts' / 'R-r41-52.json'), '--chance', '0.9',
            '--tells', 'none: his new opening, two words changed on his answer', '--human-tells', 'his asides and jokes, the video',
            '--first-fix', 'payoff: his own words; join: his own words; plain: "in recent years" on his answer',
            '--humanized', 'his own words, not rewritten', '--after-fix', 'his new opening as #339 read it, with "in recent years"',
            '--diagnosis', 'his Q-S5 answer: "change it"',
            '--decides', 'whether part 1 of his new opening still reads Human High with "in recent years"']),
    ('54', ['--lineage', 'romance-r41-muses-p1', '--chance', '0.8', '--tells', 'none: his own version',
            '--human-tells', '"Woops...", his engine and steering wheel, "a game to anyone on the outside"',
            '--unchanged', 'his version of Muses & Directors as he sent it on the ninth page (Q-C7), part 1',
            '--decides', 'whether his version of the section reads Human High in every window, part 1']),
    ('55', ['--lineage', 'romance-r41-muses-p2', '--chance', '0.85', '--tells', 'none: his own version',
            '--human-tells', 'Key teleporting him outside the galaxy, the TV remote, poetry and prose, "tho"',
            '--unchanged', 'his version of Muses & Directors as he sent it on the ninth page (Q-C7), part 2',
            '--decides', 'whether his version of the section reads Human High in every window, part 2']),
]
for k, extra in JOBS:
    text = next((HERE / 'checks').glob('CHECK-r41-%s-*.txt' % k))
    cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER), '--text', str(text),
           '--key', text.stem[len('CHECK-'):]] + COMMON + extra
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    out = (r.stdout + r.stderr).strip().splitlines()
    print(k, 'refused' if r.returncode else 'ok', out[-1][:300] if out else '')
