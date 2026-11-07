#!/usr/bin/env python3
"""predict.py - the predictions for h31 (his list fix carried to four long lists), written before the checks."""
import pathlib
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parents[4]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
H = 'articles/bad-trips/humanize/h31-20261107'
DET = "Pangram web app (his account, Pangram Professional), through the Claude desktop app's browser pane"
MOVE = ("his list fix (round 23, SKILL.md fix 5) carried after a fresh reader's sense read (sense/SENSE-READ.md) and the "
        "linter: the list taken apart, not reworded around; at most a short list, the rest in sentences built differently, "
        "each item something a reader can picture; the fidelity keys kept (PASS before the check)")
WHY = ("his own No Rash Actions list read Human, High on his first try (e1537940) and in place (f14f541b) by taking the list "
       "apart: a short list of plain verbs, two sentences built differently, picturable items, 'maybe don't', a slack ending; "
       "my three tries after his message kept their lists whole and read AI (SH3 99%, AB3 68%, QF 82%)")
P = []


def add(key, lineage, name, chance, before, cause, decides, first, tells, human, panel=None):
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', lineage, '--scope', 'paragraph',
         '--text', '%s/TEST-base-%s.txt' % (H, name), '--key', key, '--call', 'Human' if chance >= 0.5 else 'AI',
         '--chance', str(chance), '--detector', DET, '--diagnosis', WHY + '; ' + before + '; ' + cause, '--decides', decides,
         '--receipt', '%s/TEST-base-%s.receipt.json' % (H, name), '--humanized', MOVE, '--first-fix', first]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    if panel:
        a += ['--panel', panel]
    P.append(a)


add('bt-lf-dl', "bad-trips For the Person Helping, its Don't list, his list fix (round 23)", 'DL', 0.4,
    "the Do and Don't lists read AI, 100% (73d75463), the Don't list 100% (771b2b52)",
    "this turns three packed don'ts into a paragraph: what the visions might be, pictured; what to say instead; the labels; and what not to force, said as whose call each thing is",
    "whether his list fix carries the helper's Don't list",
    "payoff: the first don't leads, then what to do instead ('Reflect the feeling', with an example); join: the force list made three sentences of whose call each thing is; plain: 'cosmic conclusions' to 'what the universe is for', 'ordinary reality' to 'the night ends with sleep'",
    ["the five labels kept as one run (fidelity)"], ["'That argument can wait until tomorrow, or forever.'", "'if it comes at all'"])
add('bt-lf-qs', "bad-trips After the Storm, the questions with the facts merged in (MVI cut as a repeat)", 'QS', 0.4,
    "the questions paragraph read AI as the guide has it (seven short questions), and my merge with the facts read 82% (b9142e56)",
    "this says what to write down first, then goes through it with examples a reader can picture (the cannabis, the crowded room, prophecy at 3 a.m.) and ends on plain fixes",
    "whether his list fix carries the questions and the facts to write down",
    "payoff: write it down once slept leads; join: the seven questions made examples in three sentences; plain: 'plain practical action' to 'a better sitter, or a bottle of water within reach'",
    ["the facts to write down kept as a short list"], ["'prophecy at 3 a.m.'", "'a bottle of water within reach next time'"])
add('bt-lf-ds', "bad-trips Why Bad Trips Tend to Happen, the distortions, his list fix (round 23)", 'DS', 0.35,
    "the distortions read AI in every wording, after the tell panel too (its agreed tells: the opening, the last three items, the even template)",
    "this takes the bulleted list apart into sentences built differently, each distortion said as what it sounds or feels like, and says what CBT's names are for",
    "whether taking the list apart carries the distortions",
    "payoff: what the distortions are and what they do leads; join: seven bullets made six sentences of different shapes; plain: 'Cognitive distortions' to 'the ways a frightened mind twists what it sees'",
    ["each distortion's quote kept"], ["'Catastrophizing is the voice that says'", "'Then there's spiritual bypassing'"],
    panel='articles/bad-trips/humanize/h22-20261107/panel-DISTORT/PANEL.md')
add('bt-lf-gs', "bad-trips Give the Session a Beginning and an End, its list, his list fix (round 23)", 'GS', 0.35,
    "the section read AI, 100% (3530eb57), 70% after the Human section, its list AI with or without its repeat",
    "this takes the six labelled bullets apart into a paragraph in the order of a session (before, during, the end, after), with the fresh reader's unclear terms said plainly",
    "whether his list fix carries Give the Session's list",
    "payoff: plan the start and end before taking anything leads; join: six labelled bullets made sentences in the session's order; plain: 'low-directivity support' to 'keeps you safe and offers you choices', 'return to the room and date' to 'check where you are and what day it is'",
    ["a paragraph of instructions (its job)"], ["'some normal company'", "'without a wish list of revelations, buried memories, good cries or spiritual breakthroughs'"])
for a in P:
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip().splitlines()
    print(a[a.index('--key') + 1], '|', (out[-1] if out else r.returncode)[:300])
