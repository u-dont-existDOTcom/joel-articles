#!/usr/bin/env python3
"""predict_v22.py - the predictions for draft 22's checks (the somatic ledger), written before any of them goes to Pangram.

  python3 articles/somatic-therapies/experiments/additions-20261126/predict_v22.py
"""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles' / 'somatic-therapies' / 'humanize' / 'pangram-ledger.jsonl'
TOOL = ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'
DET = "Pangram 4.1 (web app, his account, in the desktop app's browser pane)"
HUM = ('draft 22, read by fresh Fable readers against his fixes and for need, fit and contradictions (reads/READ-21.md and '
       'READ-22.md, every mark acted on); the tell panels on the booking paragraph (panel/A1-P5-19) and on A3\'s opening (panel/A3-P1-20); '
       'every mark acted on or kept with a reason in the receipt')
FIRST = ('payoff: each text opens on the reader\'s case ("All three keep steering you back", "If the tests keep coming back '
         'normal", "If your pain has lasted months"); join: A3\'s opening and its first therapy in one paragraph; plain: '
         '"false alarm", "talk therapies", "I\'d look into"')
RUNS = [
    dict(key='a1-p5-22', name='A1-P5', lineage='ADD-A1-P5', scope='paragraph', call='Human', chance=0.55, big=None,
         panel=str(HERE / 'panel' / 'A1-P5-19' / 'PANEL.md'),
         tells=['the quoted sample question'],
         diag='its sixth and last try, from try 20 (Human Low 69; try 21\'s cut close read 22% AI, so the close stays): the '
              'panel agreed on S1 ("All three keep steering you back toward your feelings": which feelings, and "which" '
              'could point at the steering); now "the feelings you\'d rather slip away from", the section\'s own words',
         decides='whether the booking paragraph reads High; if not, his teaching card with the six tries'),
    dict(key='ic2-12', name='IC2', lineage='IC-IC2-B', scope='paragraph', call='Human', chance=0.6, big=None,
         tells=['"they\'ve helped people with" as a vague claim'],
         diag='from the near miss (ic2-9: High 38, Medium 20); ic2-10 and ic2-11 changed the second sentence and read Low; '
              'READ-21: "They both ... helped people with back, muscle and joint pain" can be read as each therapy helping all '
              'three, where each has its own trial\'s pain: "between them", two words',
         decides='whether the second sentence reads High'),
    dict(key='a3-p1-22', name='A3-P1', lineage='ADD-A3-P1p2', scope='paragraph', call='Human', chance=0.6, big=None,
         panel=str(HERE / 'panel' / 'A3-P1-20' / 'PANEL.md'),
         tells=['"like going for walks" as a tacked-on example'],
         diag='the near miss (a3-p1-21: High 88, Medium 18 over the last sentence); its "it" ("avoiding because of it") '
              'could be the pain or the fear the sentence before ends on: "the pain", one word',
         decides='whether the opening reads High in every window; then A3 as a section'),
]


def main():
    bad = 0
    only = set(sys.argv[1:])
    for r in RUNS:
        if only and r['key'] not in only:
            continue
        txt = HERE / 'texts' / 'v22' / ('%s.txt' % r['name'])
        rec = HERE / 'receipts' / 'v22' / ('%s.receipt.json' % r['name'])
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
