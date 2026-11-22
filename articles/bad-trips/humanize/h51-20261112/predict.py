#!/usr/bin/env python3
"""predict.py - this folder's predictions (pangram_ledger.py predict), written before the checks.

  python3 predict.py KEY...
"""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
DET = 'Pangram web app (his account, Pangram Professional)'
H = 'https://www.pangram.com/history/'
MOVES = ("his message of 22:34 UTC carried into his Active Seizure lists: an overdose seizure its own call line, the 5 minutes "
         "kept for a seizure on a normal dose ('you're right about over 5 minutes that's an epilepsy rule'), the heat line "
         "said with how to tell ('you can tell by touching someone's forehead'), and his explanation in a paragraph after the "
         "list, opening on which seizure the 5 minutes is for; through the needed read, the read against his fixes and the "
         "universal fit read five times")
P = {
 'callp-c3': dict(call='Human', chance=0.55, scope='paragraph', batch='h51a',
   lineage="bad-trips Active Seizure's call list with his 22:34 UTC changes, by itself (h51)",
   tells=["- They have a seizure after taking too much, or you don't know how much they took."],
   human=["- Their forehead feels very hot (not just sweaty)."],
   first=("payoff: his lead-in first ('Call medics if any of these happen:'); join: the unsure case on the overdose line, his "
          "'(or if unsure)'; plain: 'A convulsive seizure goes on for over 5 minutes' said for the seizure it is for ('A seizure "
          "on a normal dose goes on for over 5 minutes'), 'They get dangerously hot (not just regular sweating)' said with how "
          "to tell ('Their forehead feels very hot (not just sweaty)')"),
   diagnosis=("His call list read Human, High in his Active Seizure check (" + H + "5e41c575-7ebf-4b42-9059-adddbf2c5a7f). This "
              "is it with two lines changed and one added, by itself. Better: Human High in every window"),
   unchanged="his lead-in and four of his lines (19:44 UTC, 5e41c575); the overdose line, the 5-minute line's wording and the forehead are mine"),
 'explone-c5': dict(call='AI', chance=0.45, scope='paragraph', batch='h51a',
   lineage="bad-trips Active Seizure's 5-minutes paragraph, by itself (h51)",
   tells=["Their seizure is most likely less dangerous than an actual drug overdose seizure."],
   human=["Waiting the 5 minutes is only for a seizure on a normal dose."],
   first=("payoff: which seizure the 5 minutes is for, first; join: his reason in one sentence with who it is for; plain: his "
          "comparison in his words ('most likely less dangerous than an actual drug overdose seizure')"),
   diagnosis=("New: his explanation of 22:34 UTC ('explain that they can lower seizure threshold even with a normal dose and "
              "people with already low seizure thresholds might have seizures which are most likely less dangerous than an "
              "actual drug overdose seizure'), by itself. Better: Human High in every window"),
   unchanged="nothing: the paragraph is mine, from his words"),
 'seize-c10': dict(call='Human', chance=0.5, scope='section', batch='h51a',
   lineage="bad-trips Active Seizure with his 22:34 UTC changes (h51)",
   tells=["Their seizure is most likely less dangerous than an actual drug overdose seizure."],
   human=["- Their forehead feels very hot (not just sweaty)."],
   first=("the call list and the paragraph above, in the section with his first aid and his rescue paragraph"),
   diagnosis=("His Active Seizure read Human, High (" + H + "5e41c575-7ebf-4b42-9059-adddbf2c5a7f) and his rescue paragraph "
              "Human High by itself (" + H + "9320d4ec-0ca0-4d7a-a770-30d80cdadf67). This is the section with his 22:34 UTC "
              "changes. Better: Human High in every window"),
   unchanged="his first aid, four of his call lines and his rescue paragraph; the rest is mine"),
}

P['callp-c4'] = dict(P['callp-c3'], batch='h51b', chance=0.55, call='Human',
   human=["- They get dangerously hot, which you can feel on their forehead (not just regular sweating)."],
   first=("his heat line kept as he wrote it, with only how to tell added ('which you can feel on their forehead'), so the list "
          "no longer runs three 'Their ...' lines in a row"),
   diagnosis=("callp-c3 read Human with a Medium window over its last four lines (" + H + "4d0a5d11-8a2e-49fa-8539-c6c5e87989d5), "
              "my forehead line making three 'Their ...' lines in a row. Better: Human High in every window"))
P['seize-c11'] = dict(P['seize-c10'], batch='h51b', chance=0.6,
   diagnosis=("seize-c10 read Human High 265 (" + H + "c00d2cae-f984-451a-8b26-f790150280e6); this is it with the heat line of "
              "callp-c4. Better: Human High in every window"))

P['callp-c5'] = dict(P['callp-c3'], batch='h51c', chance=0.5, call='Human',
   human=["- When you touch their forehead, it's very hot, not just sweaty."],
   first=("the heat line short, and said as what the reader does and finds ('When you touch their forehead, it's very hot'), so "
          "it no longer opens like the lines around it"),
   diagnosis=("callp-c3 read Human with a Medium window over its last four lines (" + H + "4d0a5d11-8a2e-49fa-8539-c6c5e87989d5) "
              "and callp-c4, with his heat line and a clause, AI (" + H + "14de8a4b-0a31-4cf0-9be6-db18bb676461). Better: Human High "
              "in every window"))

P['callp-c6'] = dict(P['callp-c3'], batch='h51d', chance=0.5, call='Human',
   human=["- They get dangerously hot (not just regular sweating)."],
   first=("his heat line as he wrote it, which his message answers the fit read on ('you can tell by touching someone's "
          "forehead how hot it is'); only my two new lines are added, above it"),
   diagnosis=("callp-c3 and callp-c5 read Human with the same Medium window over the list's last four lines, three of them his, "
              "whatever my heat line said (" + H + "4d0a5d11-8a2e-49fa-8539-c6c5e87989d5, " + H + "639a15d5-0abf-4c09-b38d-"
              "d2637d406f80), and callp-c4 AI. This tells whether the Medium is his lines or mine. Better: Human High in every window"),
   unchanged="his lead-in and five of his lines (19:44 UTC, 5e41c575); the overdose line and the 5-minute line's wording are mine")


def predict(key):
    p = P[key]
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L,
         '--lineage', p['lineage'], '--scope', p['scope'], '--text',
         'articles/bad-trips/humanize/h51-20261112/TEST-%s.txt' % key, '--key', key, '--batch', p['batch'],
         '--call', p['call'], '--chance', str(p['chance']), '--detector', DET,
         '--receipt', 'articles/bad-trips/humanize/h51-20261112/TEST-%s.receipt.json' % key,
         '--humanized', MOVES, '--first-fix', p['first'], '--diagnosis', p['diagnosis'], '--unchanged', p['unchanged'],
         '--decides', "whether it goes into the guide: only Human High by itself (gate bad-trips-2026-11-12l)"]
    for t in p['tells']:
        a += ['--tells', t]
    for t in p['human']:
        a += ['--human-tells', t]
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(key, '|', out.splitlines()[-1] if out else r.returncode)
    if r.returncode:
        print(out)


if __name__ == '__main__':
    for k in sys.argv[1:] or list(P):
        predict(k)
