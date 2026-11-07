#!/usr/bin/env python3
"""predict4.py - h31's fourth batch, written before the checks: Codex's rewrites of the three paragraphs (a writer of
another family, given the tell panel's notes and his three Human, High paragraphs as his voice; tell_panel.py
rewrite-prompt, brief-*/REWRITE-PROMPT.txt)."""
import pathlib
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parents[4]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
H = 'articles/bad-trips/humanize/h31-20261107'
DET = "Pangram web app (his account, Pangram Professional), through the Claude desktop app's browser pane"
WHY = ("my drafts in his measured frame read AI after the panel (AF 70%, the paragraph Medium; DL 100%; SH 97%), so by the "
       "panel's rule the next draft comes from a writer of another family: Codex, given the panel's notes, the points to keep and "
       "his three Human, High paragraphs as his voice")
BIG = "a second writer's draft (E253, E256 (Inner Child)): it rewrites the paragraph from the brief, not from my try"
P = []


def add(key, lineage, name, chance, cause, decides, first, tells, human, panel):
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', lineage, '--scope', 'paragraph',
         '--text', '%s/TEST-base-%s.txt' % (H, name), '--key', key, '--call', 'Human' if chance >= 0.5 else 'AI',
         '--chance', str(chance), '--detector', DET, '--diagnosis', WHY + '; ' + cause, '--decides', decides,
         '--receipt', '%s/TEST-base-%s.receipt.json' % (H, name), '--humanized',
         "Codex's rewrite from tell_panel.py rewrite-prompt with his voice lines; only the standard swap applied",
         '--first-fix', first, '--panel', panel, '--big-change', BIG]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    P.append(a)


add('bt-cx-af', "bad-trips After the Storm, no another ceremony, his After the Storm moves", 'CXAF', 0.4,
    "Codex reorders it (the ceremony first), breaks the list into uneven pieces ('Leave ketamine alone too.') and ends plainly",
    "whether a writer of another family carries the no-ceremony paragraph",
    "payoff: the ceremony and the substances lead; join: the practices joined to 'Deep practice can wait'; plain: 'while destabilized' to 'while you're unsettled'",
    ["two short imperatives in a row ('Sleep and eat first.')"], ["'Leave ketamine alone too.'", "'push kundalini'"],
    'articles/bad-trips/humanize/h31-20261107/panel-AF/PANEL.md')
add('bt-cx-dl', "bad-trips For the Person Helping, its Don't list, his list fix (round 23)", 'CXDL', 0.4,
    "Codex starts from a case ('If they look away'), joins the argument and validation don'ts, and splits the labels so 'failing the medicine' stands alone",
    "whether a writer of another family carries the helper's Don't list",
    "payoff: a case leads ('If they look away'); join: the two argument don'ts made one sentence; plain: 'ordinary reality' to 'the room you're sitting in'",
    ["the force list kept whole (fidelity)"], ["'If they look away'", "'failing the medicine'"],
    'articles/bad-trips/humanize/h31-20261107/panel-DL/PANEL.md')
add('bt-cx-sh', "bad-trips Dealing With Shadow Thoughts, during a trip, his After the Storm moves", 'CXSH', 0.4,
    "Codex leads with the diagnosis, puts the script second, splits the don'ts after it, and ends on 'Check the time.'",
    "whether a writer of another family carries the shadow-thought paragraph",
    "payoff: the diagnosis don't leads; join: the don'ts split around the script; plain: 'return to room, body, human, time, and love' to 'come back to the room and your body, to love and a person. Check the time.'",
    ["the script kept (the guide's words to say)"], ["'And don't confess it to everybody.'", "'Check the time.'"],
    'articles/bad-trips/humanize/h31-20261107/panel-SH/PANEL.md')
for a in P:
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip().splitlines()
    print(a[a.index('--key') + 1], '|', (out[-1] if out else r.returncode)[:300])
