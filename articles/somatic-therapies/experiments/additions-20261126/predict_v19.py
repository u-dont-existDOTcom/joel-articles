#!/usr/bin/env python3
"""predict_v19.py - the predictions for draft 19's checks (the somatic ledger), written before any of them goes to Pangram.

  python3 articles/somatic-therapies/experiments/additions-20261126/predict_v19.py
"""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles' / 'somatic-therapies' / 'humanize' / 'pangram-ledger.jsonl'
TOOL = ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'
DET = "Pangram 4.1 (web app, his account, in the desktop app's browser pane)"
HUM = ('drafts 10 to 14, each read by fresh Fable readers against his fixes and for need, fit and contradictions (READ-14 and READ-16, acted on; the tell panel on A1\'s opening, '
       'panel/A1-P1-15 and -16), every mark acted on or kept with a reason in the receipt')
FIRST = ('payoff: each text opens on the reader\'s state or the news ("Even once you can feel your body just fine", "It turns '
         'out there\'s an actual clinical therapy for this", "While the investigation goes on"); join: the case and the '
         'therapy in one run, the booking questions as one indirect question; plain: "slip away", "talk therapies", '
         '"I\'d keep looking"')
RUNS = [
    dict(key='a1-p1-19', name='A1-P1', lineage='ADD-A1-P1', scope='paragraph', call='AI', chance=0.45,
         panel=str(HERE / 'panel' / 'A1-P1-18' / 'PANEL.md'),
         big=('four tries of mine read AI (98%, 97%, 91%), and three panels agreed on every sentence each time; per '
              'tell_panel.py, the next draft comes from another writer: a fresh Fable writer given writer/BRIEF-A1-P1.md (his '
              'fixes brief, lessons 27b and 27c, the section around it, the panels\' agreed tells) wrote it'),
         tells=['"was built around that habit"'],
         diag='my four forms (bridge opener, signpost, if-then-there\'s, sample line) all read AI; the fresh writer\'s '
              'opens on the two sections above and what they leave to the reader, says the habit in plain uneven sentences '
              'and the therapist\'s act concretely ("however many times you change the subject")',
         decides='whether the opening goes in; if not, a teaching card with my best tries'),
    dict(key='a1-p5-19', name='A1-P5', lineage='ADD-A1-P5', scope='paragraph', call='Human', chance=0.5, big=None,
         tells=['"I would ask a therapist about that before I booked"'],
         diag='back to the near miss (Human, Low; "listen"); "hear me out" read AI, splitting the window at the first '
              'sentence; now his own water-therapy frame for the question ("I would ask a water therapist about that before I '
              'booked: ...") in place of "the kind of thing I\'d ask a water therapist"',
         decides='whether his own frame lifts the Low window'),
    dict(key='ic1-9', name='IC1', lineage='IC-IC1-SELF', scope='paragraph', call='Human', chance=0.6, big=None,
         tells=['"until you learn to do that yourself" as an ending'],
         human=['"which I only found out about after I wrote this section": his own fact, from his card answer of '
                '2026-11-27 00:55 UTC', '"as the ideal adult, protecting and nurturing your inner child ... you learn to do '
                'that yourself": his own words from his Imagery Rescripting version (Human High, 36d19d5d)'],
         diag='the second sentence read Medium after two one-word tries ("back then", "that memory"); now in his own words '
              'from his A2 version, which read Human High',
         decides='whether the Imagery Rescripting paragraph reads High'),
    dict(key='ic2-9', name='IC2', lineage='IC-IC2-B', scope='paragraph', call='AI', chance=0.45,
         big=('the draft-18 try read AI (High 66, Medium 7): a definition of each therapy after a colon, built alike, then a '
              'pointer; this try is one run-on sentence in his voice from the paragraph before ("I\'d ask for ..., but '
              'don\'t let ..."), the names once, and why to try them'),
         tells=['two long therapy names after "two talk therapies I go into"'],
         diag='two forms that defined the therapies read AI; now the reason to try one and where to read about them, in his '
              'run-on first person',
         decides='whether the pain therapies sentence goes into the inner child guide'),
    dict(key='a3-p1p2-19', name='A3-P1P2', lineage='ADD-A3-P1p2', scope='pair', call='Human', chance=0.55, big=None,
         tells=['a long conditional opening'],
         diag='the hook line ("Maybe ... is what brought you here") read Medium in three one-word tries, and joined it read AI; '
              'it is cut (the heading already asks), and the sentence that read High opens the section on "If your pain"',
         decides='whether the opening reads High without the hook'),
]


def main():
    bad = 0
    only = set(sys.argv[1:])
    for r in RUNS:
        if only and r['key'] not in only:
            continue
        txt = HERE / 'texts' / 'v19' / ('%s.txt' % r['name'])
        rec = HERE / 'receipts' / 'v19' / ('%s.receipt.json' % r['name'])
        cmd = [sys.executable, str(TOOL), 'predict', str(LEDGER), '--lineage', 'somatic-therapies/' + r['lineage'],
               '--scope', r['scope'], '--text', str(txt), '--call', r['call'], '--chance', str(r['chance']),
               '--diagnosis', r['diag'], '--decides', r['decides'], '--key', r['key'], '--batch', 'add1127',
               '--detector', DET, '--receipt', str(rec), '--humanized', HUM, '--first-fix', FIRST]
        for t in r['tells']:
            cmd += ['--tells', t]
        for t in r.get('human', []):
            cmd += ['--human-tells', t]
        if r['big']:
            cmd += ['--big-change', r['big']]
        if r.get('panel'):
            cmd += ['--panel', r['panel']]
        res = subprocess.run(cmd, capture_output=True, text=True)
        print(r['key'], 'OK' if res.returncode == 0 else 'REFUSED', (res.stdout + res.stderr).strip()[:1200])
        bad += res.returncode != 0
    return bad


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
