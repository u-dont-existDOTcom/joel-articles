#!/usr/bin/env python3
"""predict.py - turn 60's predictions (pangram_ledger.py predict), written before the checks: my two additions to the
serotonin steps from his SS-ASKED answers (step 2's line on getting cyproheptadine, step 8 with niacin's reason, the
Syrian rue oil and magnesium's reason), and his round-49 step 7 and step 8 as they go into the guide.

  python3 predict.py [KEY...]
"""
import pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
REL = 'articles/bad-trips/humanize/h68-20261122/'
DET = "Pangram web app (his account), in the desktop app's browser pane"
BATCH = 'h68a'
FIRST = {
    'a3-ss2': ('payoff: the line opens on what it means for the reader ("most people won\'t have it at home"); join: tied to '
               'his "I wouldn\'t wait" with "And" and "anyway", the reason and the way to get it in the same sentence; '
               'plain: "a telehealth doctor might write one quickly"; his three sentences before it are his own, as he sent '
               'them in round 41, the ones the ledger shows reading below High were earlier wordings, not these'),
    'a3-ss8': ('payoff: each sentence opens on what to do or leave out (the remedies they may reach for, "I\'d also leave out", '
               '"Magnesium chloride is the one I would consider"); join: each tied to the one before at its start; plain: '
               'what niacin does said plainly (flushing, dizziness, low blood pressure), the oil named as this guide\'s; '
               'the sentence the ledger shows reading AI ("What I would consider instead ...") is gone, its point said his way'),
}
HUM = ('written from his SS-ASKED answers, the ways his QUIZ-1 fixes showed: each sentence ties to the one before at its start '
       '("And", "Niacin", "also", "Magnesium chloride is the one"), the payoff first (what to leave out, the remedy to '
       'consider), the reason a reader asked for said where they ask it; two rounds of the three fresh reads before the check')
P = {
    'a3-ss2': ('bad-trips serotonin step 2 with his cyproheptadine answer (h68)', 'Human', 0.6,
               ["since it needs a prescription in the US, though a telehealth doctor might write one quickly"],
               ["And most people won't have it at home anyway"], None),
    'a3-ss8': ('bad-trips serotonin step 8 with his round-49 answers (h68)', 'Human', 0.5,
               ["Magnesium chloride is the one I would consider, since many people with serotonin syndrome run low on magnesium"],
               ["I'd also leave out this guide's Syrian rue oil for now"], None),
    'r49-ss7': ('bad-trips serotonin step 7, his round-49 version (h68)', 'Human', 0.75, [],
                ["Keep track of how their breathing is doing"],
                'his version from his QUIZ-1 comment of 2026-11-22 17:21 UTC, with "they took" as he asked ("how much of each THEY TOOK, right?"); step 7 of B136 as the guide has it now'),
    'r49-ss8his': ('bad-trips serotonin step 8, his round-49 revision (h68)', 'Human', 0.7, [],
                   ["Topical magnesium chloride if they're not able to swallow."],
                   'his SS-STEP8 revision as he sent it (my step 8, Human High by itself, with his line on topical magnesium chloride); step 8 of B136 as the guide has it now'),
}


def run(key):
    lin, call, chance, tells, human, unch = P[key]
    a = ['python3', 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', lin, '--scope', 'paragraph',
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', BATCH, '--call', call, '--chance', str(chance),
         '--detector', DET, '--decides', ('whether %s reads Human High by itself; if not, the window says where to read '
                                         'it again for sense' % key)]
    if unch:
        a += ['--unchanged', unch]
    else:
        a += ['--receipt', REL + 'TEST-%s.receipt.json' % key, '--humanized', HUM, '--first-fix', FIRST[key]]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(key, '|', out[:900] if r.returncode else out.splitlines()[-1][:160])
    return r.returncode


if __name__ == '__main__':
    sys.exit(max(run(k) for k in (sys.argv[1:] or list(P))))
