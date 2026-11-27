#!/usr/bin/env python3
"""predict_v24.py - the prediction for IC2's last try (the somatic ledger), written before any of them goes to Pangram.

  python3 articles/somatic-therapies/experiments/additions-20261126/predict_v24.py
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
       'READ-24.md, every mark acted on); the tell panel on IC2 (panel/IC2-23); the tell panels on the booking paragraph (panel/A1-P5-19) and on A3\'s opening (panel/A3-P1-20); '
       'every mark acted on or kept with a reason in the receipt')
FIRST = ('payoff: each text opens on the reader\'s case ("All three keep steering you back", "If the tests keep coming back '
         'normal", "If your pain has lasted months"); join: A3\'s opening and its first therapy in one paragraph; plain: '
         '"false alarm", "talk therapies", "I\'d look into"')
RUNS = [
    dict(key='ic2-14', name='IC2', lineage='IC-IC2-B', scope='paragraph', call='Human', chance=0.5, big=None,
         panel=str(HERE / 'panel' / 'IC2-23' / 'PANEL.md'),
         tells=['"they\'ve helped people with" as a vague claim'],
         diag='its last try, from the near miss (ic2-9: High 38, Medium 20 over its second sentence); every change to that '
              'sentence read lower, and the tell panel on the joined form (panel/IC2-23) agreed on the reassurance as a stock '
              'phrase ("treat the pain as real"): now his own word from the section ("normal test results don\'t prove the '
              'pain is imaginary"), "Neither one sees the pain as imaginary"; the rest of ic2-9 word for word',
         decides='whether IC2 reads High; if not, his teaching card with the six tries'),
]


def main():
    bad = 0
    only = set(sys.argv[1:])
    for r in RUNS:
        if only and r['key'] not in only:
            continue
        txt = HERE / 'texts' / 'v24' / ('%s.txt' % r['name'])
        rec = HERE / 'receipts' / 'v24' / ('%s.receipt.json' % r['name'])
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
