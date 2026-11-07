#!/usr/bin/env python3
"""predict2.py - h31's second batch, written before the checks: what carried his round-23 list (two ablations of his own
paragraph), and my Don't list with the kind of specifics his has."""
import pathlib
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parents[4]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
H = 'articles/bad-trips/humanize/h31-20261107'
DET = "Pangram web app (his account, Pangram Professional), through the Claude desktop app's browser pane"
WHY = ("my four list-fix tries all read AI (DL 100%, QS 48%, DS 72%, GS 100%) though each took its list apart; his version "
       "reads Human, High alone (e1537940) and in place (f14f541b); what his has and mine lacked: absurd specifics (Judge Amos, "
       "the BMW given away and bought, 42 seconds), a hedge ('maybe don't', 'Think twice'), a trailing '...' and a slack ending")
P = []


def add(key, lineage, name, chance, cause, decides, humanized, first, tells, human, big=None):
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', lineage, '--scope', 'paragraph',
         '--text', '%s/TEST-base-%s.txt' % (H, name), '--key', key, '--call', 'Human' if chance >= 0.5 else 'AI',
         '--chance', str(chance), '--detector', DET, '--diagnosis', WHY + '; ' + cause, '--decides', decides,
         '--receipt', '%s/TEST-base-%s.receipt.json' % (H, name), '--humanized', humanized, '--first-fix', first]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    if big:
        a += ['--big-change', big]
    P.append(a)


add('bt-ab-1', "bad-trips No Rash Actions, his round-23 list ablated: its absurd specifics made generic", 'AB1', 0.6,
    "his paragraph with only Judge Amos, the BMWs and the 42 seconds made generic; his hedges, '...', sentences and ending kept",
    "whether his absurd specifics carry his list, or his structure and hedges do",
    "an ablation of his own paragraph, a measurement: three specifics made generic, nothing else changed",
    "payoff: his, unchanged; join: his, unchanged; plain: 'Judge Amos' to 'sending', 'your BMW, buying a new BMW' to 'your stuff, buying expensive stuff', '42 seconds' cut",
    ["'giving away your stuff, buying expensive stuff'"], ["'maybe don't'", "'that list of people you've been meaning to...'", "'you can still change your mind the next day'"])
add('bt-ab-3', "bad-trips No Rash Actions, his round-23 list ablated: his structure undone", 'AB3', 0.45,
    "his specifics kept in the old flat form: one don't sentence, no hedge, no slack ending",
    "whether his specifics carry the list without his structure",
    "an ablation of his own paragraph, a measurement: his three sentences put back into the old one-sentence don't list",
    "payoff: the old lock line's list; join: his three sentences made one; plain: 'maybe don't' to 'don't', 'Think twice before' cut",
    ["one flat don't sentence of fourteen items"], ["'Judge Amos'", "'give away your BMW, buy a new BMW'", "'in 42 seconds'"])
add('bt-lf-dlj', "bad-trips For the Person Helping, its Don't list, his list fix (round 23)", 'DLJ', 0.4,
    "the Don't list again with the kind of specifics his list has (the shadow in the corner as great-aunt Doris back to complain about the funeral, the universe cracked ten minutes ago), the force list in a parenthesis, and an easy ending",
    "whether absurd specifics carry my Don't list where taking it apart didn't",
    "his list fix with his kind of specifics: a picturable, funny example for the visions, the labels kept, the force list in a parenthesis, 'If they want any of it, they'll ask'",
    "payoff: the first don't, then why ('You won't talk them out of it tonight'); join: the visions made one example sentence; plain: 'cosmic conclusions' to 'what the universe is for', 'ordinary reality' to 'everybody sleeps eventually'",
    ["the five labels kept as one run (fidelity)"], ["'great-aunt Doris, back from the dead to complain about the funeral'", "'about ten minutes ago'"],
    big="the try before read AI, High as one 332-word window that took the Human base with it, so no part of it is shown to keep; this try tests the one thing his version has that it lacked, absurd specifics, which touches most sentences")
for a in P:
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip().splitlines()
    print(a[a.index('--key') + 1], '|', (out[-1] if out else r.returncode)[:300])
