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
MOVES = ("his round-38 brain checks (lesson bad-trips-2026-11-12i; ../../experiments/t38-answers/JOEL-TRIES-TEACH-BRAIN.md): "
         "each line of a list the kind of thing its lead-in says it holds (his one-line fix of a sign of health in a list of "
         "warning signs took eleven AI windows to seven Human, ed86bddc), 'safe' said with how ('If you can safely hold them "
         "as they try', 7158fa13), a line that doesn't follow the one before on its own line, the action in the lead-in, and "
         "the last line saying when to call for help (4739068c, Human, High 174)")
P = {
 'brainopen-c1': dict(call='AI', chance=0.4, scope='section', batch='h49a',
   lineage="bad-trips My Brain Feels Damaged's opening, his round-38 lessons carried (h49)",
   tells=["Don't dismiss someone who says their brain feels damaged just because they're high or can't explain what they "
          "feel in medical language, since something could really be going wrong in their brain."],
   human=["If you can safely hold them as they try, have them stand and walk a few steps to see if they keep their balance.",
          "I usually know within about a minute whether it is helping."],
   first=("payoff: the paragraph opens on what to do with the report ('Don't dismiss ...'), and DMSO is said second instead "
          "of fourth; join: B103's three opening sentences one, the two 'It may be ...' sentences folded into its reason; "
          "plain: 'acute neurological dysfunction' said as 'something could really be going wrong in their brain', 'that "
          "report' said as 'someone who says their brain feels damaged'"),
   diagnosis=("h42a read the section AI Detected, 65% (" + H + "4076db14-325a-4854-88b1-fc3c82da040a), its first window AI "
              "High 57 over the heading and B103's three opening sentences ('Do not dismiss that report ... It may be anxiety "
              "... It may also be acute neurological dysfunction ...'). His checks after it read Human, High 174 (4739068c). "
              "This says B103's opening once, plainly, with what it points to named. Better: the opening's window reads "
              "Human"),
   his="the heading, B103's remedy lines, his electrolytes reason (from his round-38 comment) and his checks and closing "
       "line, round 38 (4739068c): his own; the opening sentence is mine"),
 'seize-c3': dict(call='AI', chance=0.4, scope='pair', batch='h49a',
   lineage="bad-trips Active Seizure's first aid and call list, his round-38 lessons carried (h49)",
   tells=['Turn them gently onto their side, which helps them breathe.', 'Blue or gray lips are another sign.'],
   human=['They get dangerously hot (not just regular sweating).'],
   first=("payoff: the lead-in says what to do while it lasts ('Time the seizure, and while it lasts:') and the call list "
          "says its action first ('Call medics if any of these happen:'), moved to follow the first aid; join: one step or "
          "sign a line, the two don'ts apart; plain: 'when practical' said as what to do and why ('Turn them gently onto "
          "their side, which helps them breathe.'), 'Protect the person from injury, clear dangerous objects' as 'Move any "
          "dangerous objects away from them, especially anything hard or sharp', the vague signs said the way the Call "
          "medics list says them ('not just regular sweating', 'blue or gray')"),
   diagnosis=("h42a read Active Seizure (1 of 2) AI Detected, 31% (" + H + "6280b126-8af7-4def-9ae2-f8d11b722990), its first "
              "aid (B109) and call line (B112) in AI High windows. This is them in his brain-checks form. Better: Human "
              "windows over both lists")),
}

P['seize-c4'] = dict(P['seize-c3'], batch='h49b', chance=0.6, call='Human',
   tells=["- They get dangerously hot (not just regular sweating)."],
   human=["- Lips turning blue or gray, which means they aren't getting enough air."],
   first=("payoff: the line says what the sign means ('which means they aren't getting enough air'); join: nothing else "
          "changed; plain: 'Blue or gray lips are another sign.' said as what it shows"),
   diagnosis=("seize-c3 read Human Written (" + H + "36fbfa7d-9ed5-4c41-a09b-509637ae1053) with one Low window, 'Blue or gray "
              "lips are another sign.', the line the third read against his fixes marked as saying a sign of nothing and I "
              "kept. This changes only that line. Better: no Low window"))

P['seize-c5'] = dict(P['seize-c3'], batch='h49c', chance=0.45, call='AI',
   tells=["- Their breathing gets slow and shallow.", "- Their lips turn blue or gray."],
   human=["- They get dangerously hot (not just regular sweating)."],
   first=("payoff: unchanged from seize-c3; join: nothing; plain: the Low line said as what happens ('Their lips turn blue "
          "or gray.'), the plain clause the second draft had"),
   diagnosis=("seize-c3 read Human Written with one Low window over 'Blue or gray lips are another sign.' (" + H +
              "36fbfa7d-9ed5-4c41-a09b-509637ae1053); the read's fix, a clause saying what it means, read worse (" + H +
              "c61ad5f7-54b9-4796-a4f6-f6cf2c6b74fb, AI Detected, 39%). This puts the plain clause there instead. Better: "
              "no Low window; if worse than seize-c3, seize-c3 goes in as it is"))

P['er-c1'] = dict(call='Human', chance=0.55, scope='pair', batch='h49d',
   lineage="bad-trips Acute Medical's emergency room paragraph, his round-38 lessons carried (h49)",
   tells=['Those only sometimes help with psychosis, and in some people they bring on more agitation or fear instead, a '
          'paradoxical reaction.'],
   human=["In an emergency room, a scared, psychotic-feeling person will often get a benzodiazepine."],
   first=("payoff: the paragraph opens on what the emergency room would do ('In an emergency room, a scared, "
          "psychotic-feeling person will often get a benzodiazepine'), its 'is not magic' opening gone as a repeat of "
          "acute-c1's last sentence; join: one drug a sentence; plain: 'don't reliably address psychosis' as 'only sometimes "
          "help with psychosis', 'paradoxical agitation or fear' as 'more agitation or fear instead, a paradoxical reaction', "
          "'often administered by someone who doesn't know' as 'the staff giving them often don't know'"),
   diagnosis=("h42a read Acute Medical and Neurological Rescue AI Generated, 100% (" + H + "0df121e8-abda-428e-aa4f-a93887e4bf18), "
              "its AI High 130 window over B77; acute-c1 before it read Human, High 62 (97bf9589) and is in. This is B77 "
              "with the lessons of rounds 37 and 38, checked with acute-c1 as it now stands. Better: Human windows over B77"))

P['er-c2'] = dict(P['er-c1'],
   tells=["Don't count on it helping with psychosis, since in some people it does the opposite and brings on more agitation "
          "or fear, which is called a paradoxical reaction."],
   human=["The staff also often have no idea what was taken, if anything, so if you do end up there, tell them."],
   first=("payoff: the paragraph opens on what the emergency room would do and ends on what the reader does there ('tell "
          "them'), its 'is not magic' opening gone as a repeat of acute-c1's last sentence; join: the comma pair joined "
          "('scared and psychotic-feeling'); plain: 'those drugs don't reliably address psychosis' as 'Don't count on it "
          "helping with psychosis', 'paradoxical agitation or fear' said where the term is used, 'often administered by "
          "someone who doesn't know' as 'The staff also often have no idea what was taken'"))

P['er-c3'] = dict(P['er-c2'],
   tells=["Don't count on it helping with psychosis, since in some people it brings on a paradoxical reaction, with more "
          "agitation or fear."])


def predict(key):
    p = P[key]
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L,
         '--lineage', p['lineage'], '--scope', p['scope'], '--text',
         'articles/bad-trips/humanize/h49-20261112/TEST-%s.txt' % key, '--key', key, '--batch', p['batch'],
         '--call', p['call'], '--chance', str(p['chance']), '--detector', DET,
         '--receipt', 'articles/bad-trips/humanize/h49-20261112/TEST-%s.receipt.json' % key,
         '--humanized', MOVES, '--first-fix', p['first'], '--diagnosis', p['diagnosis'],
         '--decides', "whether it goes into the guide (round 38's card: I carry what it teaches to the sections above and "
                      "test them)"]
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
