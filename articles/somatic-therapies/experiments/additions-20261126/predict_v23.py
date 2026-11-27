#!/usr/bin/env python3
"""predict_v23.py - the predictions for draft 23's checks (the somatic ledger), written before any of them goes to Pangram.

  python3 articles/somatic-therapies/experiments/additions-20261126/predict_v23.py
"""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles' / 'somatic-therapies' / 'humanize' / 'pangram-ledger.jsonl'
TOOL = ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'
DET = "Pangram 4.1 (web app, his account, in the desktop app's browser pane)"
HUM = ('draft 23, read by fresh Fable readers against his fixes and for need, fit and contradictions (reads/READ-21.md to '
       'READ-23.md, every mark acted on); the tell panels on the booking paragraph (panel/A1-P5-19) and on A3\'s opening (panel/A3-P1-20); '
       'every mark acted on or kept with a reason in the receipt')
FIRST = ('payoff: each text opens on the reader\'s case ("All three keep steering you back", "If the tests keep coming back '
         'normal", "If your pain has lasted months"); join: A3\'s opening and its first therapy in one paragraph; plain: '
         '"false alarm", "talk therapies", "I\'d look into"')
RUNS = [
    dict(key='ic2-13', name='IC2', lineage='IC-IC2-B', scope='paragraph', call='Human', chance=0.5, big=None,
         tells=['a 55-word sentence with a "which both" clause'],
         diag='its last try, from the near miss (ic2-9: High 38, Medium 20 over its second sentence); every change to that '
              'sentence read lower (trial counts and "see" Low, "between them" AI Low), so it is joined to the sentence it '
              'draws on, "which both", with "between them" for each therapy\'s own trial (READ-23), lesson neuro-2026-11-27e: '
              'a short last sentence that reads Medium read High joined',
         decides='whether IC2 reads High; if not, his teaching card with the six tries'),
    dict(key='a3-p1-23', name='A3-P1', lineage='ADD-A3-P1p2', scope='paragraph', call='Human', chance=0.6, big=None,
         panel=str(HERE / 'panel' / 'A3-P1-20' / 'PANEL.md'),
         tells=['"like going for walks" as a tacked-on example'],
         diag='the near miss (a3-p1-21: High 88, Medium 18 over its last sentence; "the pain" for "it" read the same, 19): '
              'the last sentence is the second way you learn it\'s a false alarm, so it is joined to the first ("and by '
              'slowly going back"), lesson neuro-2026-11-27e',
         decides='whether the opening reads High in every window; then A3 as a section'),
]


def main():
    bad = 0
    only = set(sys.argv[1:])
    for r in RUNS:
        if only and r['key'] not in only:
            continue
        txt = HERE / 'texts' / 'v23' / ('%s.txt' % r['name'])
        rec = HERE / 'receipts' / 'v23' / ('%s.receipt.json' % r['name'])
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
