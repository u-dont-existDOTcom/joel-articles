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
MOVE = ("his round-37 Chest Pain fix (lesson bad-trips-2026-11-12h): the action said before the list it serves ('For the "
        "following more serious signs (or if unsure), I'd also call medics:'), which alone took my chest-c3 from AI "
        "Generated, 100% to Human Written (his try 7, " + H + "8f2d89bb-89e9-4764-aa02-e49f5e1331b4)")
P = {
 'brain-p1': dict(call='AI', chance=0.3, scope='pair', batch='h48a',
   lineage="bad-trips My Brain Feels Damaged's checks, written against his fixes (h46)",
   tells=['Several of these checks look for recognized stroke warning signs.', "- Feel whether they're very hot."],
   human=["If any check turns up a problem (or they're too out of it to answer you), keep the DMSO going while someone "
          "calls medics:", 'Wetting or soiling themselves is another sign to watch for.'],
   first=("payoff: the action ('keep the DMSO going while someone calls medics') said before the checks instead of after "
          "them, as his try 7 on chest-c3; join: the can't-answer case in brackets in the same sentence, like his '(or if "
          "unsure)'; plain: nothing else changed, the checks and the last line as brain-c3 had them"),
   diagnosis=("brain-c3 read AI Generated, 100% (" + H + "0eeefa6e-c72f-4ea6-b74e-fab541aca12f), its action said after the "
              "checks ('So if you see any of these signs, keep the DMSO going while someone calls medics.'). This changes only "
              "that, the way his try 7 changed my chest-c3 and read Human. Better: the windows over the lead-in and the end "
              "read Human; if the list's middle still reads AI, the move is not enough there by itself")),
 'acute-c1': dict(call='AI', chance=0.45, scope='paragraph', batch='h48a',
   lineage="bad-trips Acute Medical and Neurological Rescue's opening, his round-37 move carried (h48)",
   tells=['Even from a severe trip, they can come down faster that way than after an ambulance ride and hours in an '
          'emergency room.'],
   human=["I'd calm and stabilize the trip right where they are, as long as none of the signs on the Call medics list above "
          "show up and I can keep them from getting hurt."],
   first=("payoff: what to do first ('I'd calm and stabilize the trip right where they are'), its conditions after it ('as "
          "long as ...'), as his Chest Pain line ('I'd just use DMSO ..., as long as they're fully alert'); join: B100 and B76 "
          "one paragraph; plain: 'field rescue' said as 'right where they are', B76's six conditions as the Call medics list "
          "they repeat"),
   diagnosis=("my two carries of his round-35 moves read AI Generated, 100% (" + H + "eedc2eec-ceb0-493b-a41b-366d703ab11c, "
              + H + "49d3772f-dead-4b30-a92e-72051c07b5dd), both saying the action after the checks ('If all that checks out, "
              "calming and stabilizing the trip may be enough.') and the checks the Call medics list already has. This says "
              "the action first and points to the list. Better: Human windows")),
}


def predict(key):
    p = P[key]
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L,
         '--lineage', p['lineage'], '--scope', p['scope'], '--text',
         'articles/bad-trips/humanize/h48-20261112/TEST-%s.txt' % key, '--key', key, '--batch', p['batch'],
         '--call', p['call'], '--chance', str(p['chance']), '--detector', DET,
         '--receipt', 'articles/bad-trips/humanize/h48-20261112/TEST-%s.receipt.json' % key,
         '--humanized', MOVE, '--first-fix', p['first'], '--diagnosis', p['diagnosis'],
         '--decides', "whether it goes into the guide (MEDICAL-HOW: I carry what he does to other sections and test them) "
                      "and whether his payoff move carries by itself, as his try 7 showed on chest-c3"]
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
