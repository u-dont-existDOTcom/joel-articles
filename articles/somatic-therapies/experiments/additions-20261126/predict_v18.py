#!/usr/bin/env python3
"""predict_v18.py - the predictions for draft 18's checks (the somatic ledger), written before any of them goes to Pangram.

  python3 articles/somatic-therapies/experiments/additions-20261126/predict_v18.py
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
    dict(key='a1-p1-18', name='A1-P1', lineage='ADD-A1-P1', scope='paragraph', call='AI', chance=0.45,
         panel=str(HERE / 'panel' / 'A1-P1-16' / 'PANEL.md'),
         big=('the draft-17 try read AI 97% in three windows, and the second panel (A1-P1-16) agreed on all three '
              'sentences: the "By this layer" signpost, the colon reveal with its even pair, and the invented sample line; '
              'this try drops all three and takes the shape of the AEDP paragraph, which read Human High by itself: the '
              'reader\'s case as one "if" clause, the therapy named, then what its therapist does'),
         tells=['"there\'s" naming the therapy after a long "if" clause'],
         diag='three tries read AI; the shape that read Human High in this section (the AEDP paragraph) is the case first in '
              'an "if" clause, the name, then the therapist\'s one act in plain words',
         decides='whether the opening goes in; if not, the next draft comes from a fresh writer, then a teaching card'),
    dict(key='a1-p5-18', name='A1-P5', lineage='ADD-A1-P5', scope='paragraph', call='Human', chance=0.55, big=None,
         tells=['"the kind of thing I\'d ask a water therapist"'],
         diag='the near miss (Human, Low, one window of 69 words): "and that they\'d listen" doesn\'t say to what; "hear me '
              'out" is the plain words for listening to his side',
         decides='whether two words lift the Low window'),
    dict(key='ic1-8', name='IC1', lineage='IC-IC1-SELF', scope='paragraph', call='Human', chance=0.55, big=None,
         tells=['"which I only found out about" as a relative clause'],
         human=['"which I only found out about after I wrote this section": his own fact, from his card answer of '
                '2026-11-27 00:55 UTC ("although I didn\'t know it was a therapy when i wrote about it")'],
         diag='the near miss (Human: High 33, Medium 25) twice: "the memory" in the second sentence could be any memory; '
              '"that memory" is the one too big to redo alone',
         decides='whether one word lifts the Medium window'),
    dict(key='ic2-8', name='IC2', lineage='IC-IC2-B', scope='paragraph', call='AI', chance=0.45, big=None,
         tells=['two therapy names, each with a "where" clause'],
         diag='IC2 alone read Mixed (the trial summary AI) and with his paragraph AI (his paragraph too); now 62 words, checked '
              'by itself, a lineage of its own (lesson neuro-2026-11-27a: for an answer to a text that doesn\'t read High): '
              'one sentence that says what each therapy has you do, in the words of the somatic section it points to, then '
              'his own pointer form',
         decides='whether the pain therapies paragraph goes into the inner child guide'),
    dict(key='a3-p1p2-18', name='A3-P1P2', lineage='ADD-A3-P1p2', scope='pair', call='Human', chance=0.55, big=None,
         tells=['a long "if ..., and ..., and ..." opening'],
         diag='the opening line read Human (Medium) in three one-word tries; joined to the sentence it draws on, as lesson '
              'neuro-2026-11-27e found ("join a sentence to the one it draws on")',
         decides='whether the opening reads High'),
]


def main():
    bad = 0
    only = set(sys.argv[1:])
    for r in RUNS:
        if only and r['key'] not in only:
            continue
        txt = HERE / 'texts' / 'v18' / ('%s.txt' % r['name'])
        rec = HERE / 'receipts' / 'v18' / ('%s.receipt.json' % r['name'])
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
