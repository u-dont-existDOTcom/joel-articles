#!/usr/bin/env python3
"""predict_v21.py - the predictions for draft 21's checks (the somatic ledger), written before any of them goes to Pangram.

  python3 articles/somatic-therapies/experiments/additions-20261126/predict_v21.py
"""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles' / 'somatic-therapies' / 'humanize' / 'pangram-ledger.jsonl'
TOOL = ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'
DET = "Pangram 4.1 (web app, his account, in the desktop app's browser pane)"
HUM = ('draft 21, read by fresh Fable readers against his fixes and for need, fit and contradictions (reads/READ-21.md, its '
       'mark acted on); the tell panels on the booking paragraph (panel/A1-P5-19) and on A3\'s opening (panel/A3-P1-20); '
       'every mark acted on or kept with a reason in the receipt')
FIRST = ('payoff: each text opens on the reader\'s case ("All three keep steering you back", "If the tests keep coming back '
         'normal", "If your pain has lasted months"); join: A3\'s opening and its first therapy in one paragraph; plain: '
         '"false alarm", "talk therapies", "I\'d look into"')
RUNS = [
    dict(key='a1-p5-21', name='A1-P5', lineage='ADD-A1-P5', scope='paragraph', call='Human', chance=0.55, big=None,
         panel=str(HERE / 'panel' / 'A1-P5-19' / 'PANEL.md'),
         tells=['the quoted sample question'],
         diag='the near miss read Human Low twice (try 17; try 20 with the question in quotes, 19:47 UTC); try 18\'s "hear me '
              'out" read AI, so S3 moves Pangram: the panel\'s agreed two-beat close ("they\'d slow down, and that they\'d '
              'listen") is cut to "they\'d slow down and listen", two words, the meaning kept',
         decides='whether the booking paragraph reads High; if not, S1\'s "which" is the next small change'),
    dict(key='ic2-11', name='IC2', lineage='IC-IC2-B', scope='paragraph', call='Human', chance=0.6, big=None,
         tells=['"they\'ve helped people with" as a vague claim'],
         diag='from the near miss (ic2-9: High 38, Medium 20); ic2-10\'s trial line read Low, so it goes back; "treat the pain '
              'as real" can be read as treating the pain (the therapy) where it means taking the pain as real: "see", one word',
         decides='whether the second sentence reads High; if not, "between them" (READ-21\'s note) is the next small change'),
    dict(key='a3-p1-21', name='A3-P1', lineage='ADD-A3-P1p2', scope='paragraph', call='AI', chance=0.45, big=None,
         panel=str(HERE / 'panel' / 'A3-P1-20' / 'PANEL.md'),
         tells=['"there are two therapies I\'d look into" as a signpost', '"false alarm" as a stock metaphor'],
         diag='the short opening read Medium as its own window in five tries, and with the PRT paragraph after it the last two '
              'sentences read Medium and Low (13) or AI Low (19); the panel agreed on all five sentences: the signpost rating '
              'the therapies ("worth knowing about") is now his "I\'d look into", the "It\'s real, but" reframe a clause '
              '("your brain is making real pain", READ-21), "Part of how you learn that" names what is learned, and "Then, a '
              'little at a time" is "You also slowly"',
         decides='whether the opening reads High; this is its last try, so if not, his teaching card with the six tries'),
]


def main():
    bad = 0
    only = set(sys.argv[1:])
    for r in RUNS:
        if only and r['key'] not in only:
            continue
        txt = HERE / 'texts' / 'v21' / ('%s.txt' % r['name'])
        rec = HERE / 'receipts' / 'v21' / ('%s.receipt.json' % r['name'])
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
