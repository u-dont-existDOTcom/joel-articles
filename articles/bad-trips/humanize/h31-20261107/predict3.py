#!/usr/bin/env python3
"""predict3.py - h31's third batch, written before the checks: his list frame as the ablations measured it, after the tell
panels on the three paragraphs (panel-AF, panel-DL, panel-SH)."""
import pathlib
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parents[4]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
H = 'articles/bad-trips/humanize/h31-20261107'
DET = "Pangram web app (his account, Pangram Professional), through the Claude desktop app's browser pane"
WHY = ("the ablations measured what carries his list: without Judge Amos, the BMWs and the 42 seconds it still reads Human "
       "(AB1, 72aadf13), and with them but in the old flat form it reads AI (AB3, 95be4d7e); so his frame carries it (a hedged "
       "don't, a list ending on something from the reader's own life with a trailing '...', 'Think twice before', a slack "
       "ending), and my funnier Don't list read AI (DLJ); the tell panels agree on every sentence of these paragraphs, as an "
       "even run of imperatives and abstract lists closed by a neat line")
BIG = ("the paragraph read AI twice in this lineage and the panel agrees on every sentence, so there is no part to keep by "
       "window; this try is his measured frame, which touches every sentence")
P = []


def add(key, lineage, name, chance, cause, decides, first, tells, human, panel):
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', lineage, '--scope', 'paragraph',
         '--text', '%s/TEST-base-%s.txt' % (H, name), '--key', key, '--call', 'Human' if chance >= 0.5 else 'AI',
         '--chance', str(chance), '--detector', DET, '--diagnosis', WHY + '; ' + cause, '--decides', decides,
         '--receipt', '%s/TEST-base-%s.receipt.json' % (H, name), '--humanized',
         "his list frame as measured (AB1 against AB3), after the tell panel: a hedged don't, the list ending on the reader's own life with '...', 'Think twice before' or a firm don't where safety needs it, and a slack ending; the panel's human tells kept",
         '--first-fix', first, '--panel', panel, '--big-change', BIG]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    P.append(a)


add('bt-fr-af', "bad-trips After the Storm, no another ceremony, his After the Storm moves", 'AFF', 0.45,
    "the panel's agreed tells: the even prohibition list, 'Stabilize through ... ordinary body, and ordinary world', the floor aphorism; its human tells kept: 'fast' as a bare verb, 'push kundalini', the quoted 'another ceremony to fix it'",
    "whether his measured frame carries the no-ceremony paragraph",
    "payoff: what to hold off on while shaky leads; join: the remedies made one sentence with what follows ('and the deep practice will keep'); plain: 'while destabilized' to 'While you're still shaky', 'until the floor is back' to 'until you're back on your feet'",
    ["a list of nine still"], ["'push kundalini'", "'another ceremony to fix it'", "'whoever's hosting this weekend'"],
    'articles/bad-trips/humanize/h31-20261107/panel-AF/PANEL.md')
add('bt-fr-dl', "bad-trips For the Person Helping, its Don't list, his list fix (round 23)", 'DLF', 0.45,
    "the panel's agreed tells: every 'Don't' line a list, 'redirect toward safety, non-harm, sleep, and ordinary reality', the abstract 'Don't validate harmful conclusions' with no example; its human tells kept: 'failing the medicine', 'try to win an argument with'",
    "whether his measured frame carries the helper's Don't list",
    "payoff: the first don't leads, hedged; join: the labels and the force list made one sentence; plain: 'harmful conclusions' given an example ('a plan that ends with somebody getting hurt'), 'redirect toward ... ordinary reality' to 'nudge them back toward the room and the idea of sleep'",
    ["the force list still eight items (fidelity)"], ["'failing the medicine'", "'whatever cosmic conclusions they reached ten minutes ago...'"],
    'articles/bad-trips/humanize/h31-20261107/panel-DL/PANEL.md')
add('bt-fr-sh', "bad-trips Dealing With Shadow Thoughts, during a trip, his After the Storm moves", 'SHF', 0.45,
    "the panel's agreed tells: the four parallel don'ts, the script's even frame, and 'return to room, body, human, time, and love'; its human tell kept: 'confess it to everybody'",
    "whether his measured frame carries the shadow-thought paragraph",
    "payoff: what not to do with a shadow thought leads, hedged; join: the five return points made acts in one sentence; plain: 'identify with' to 'believe', 'convert it into a permanent diagnosis' to 'turn it into that permanent diagnosis you've half been expecting'",
    ["the script kept (the guide's own words to say)"], ["'confess it to everybody'", "'you've half been expecting...'", "'feel your feet on the floor'"],
    'articles/bad-trips/humanize/h31-20261107/panel-SH/PANEL.md')
for a in P:
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip().splitlines()
    print(a[a.index('--key') + 1], '|', (out[-1] if out else r.returncode)[:300])
