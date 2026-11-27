#!/usr/bin/env python3
"""predict_v20.py - the predictions for draft 20's checks (the somatic ledger), written before any of them goes to Pangram.

  python3 articles/somatic-therapies/experiments/additions-20261126/predict_v20.py
"""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles' / 'somatic-therapies' / 'humanize' / 'pangram-ledger.jsonl'
TOOL = ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'
DET = "Pangram 4.1 (web app, his account, in the desktop app's browser pane)"
HUM = ('draft 20, read by fresh Fable readers against his fixes and for need, fit and contradictions (reads/READ-20.md and '
       'READ-20b.md, every mark acted on); the tell panels on A1\'s opening (panel/A1-P1-15, -16 and -18) and on the booking '
       'paragraph (panel/A1-P5-19); every mark acted on or kept with a reason in the receipt')
FIRST = ('payoff: each text opens on the reader\'s case ("If, as soon as a feeling starts in a session", "All three keep '
         'steering you back", "If the tests keep coming back normal", "If your pain has lasted months"); join: the case, its '
         'cause and the therapy in one paragraph, A3\'s opening and its first therapy in one paragraph; plain: "slip away", '
         '"false alarm", "talk therapies"')
RUNS = [
    dict(key='a1-p1-20', name='A1-P1', lineage='ADD-A1-P1', scope='paragraph', call='AI', chance=0.45,
         panel=str(HERE / 'panel' / 'A1-P1-18' / 'PANEL.md'),
         big=('five stand-alone openings (four of mine, one a fresh writer\'s) read AI; this last try is causally '
              'different: no stand-alone problem-then-therapy paragraph, the opening merged into the ISTDP paragraph '
              'that read Human High, so the habit, its cause and the therapy are one explanation'),
         tells=['a 41-word opening if-clause before the therapy\'s name', '"would say" giving the idea to the therapy'],
         diag='every stand-alone opening read as a pitch (the panels: "a clean problem-then-named-solution unit"); merged, the '
              'paragraph explains a mechanism: the habit, the anxiety ISTDP puts it down to, what the therapist does and the slower '
              'version (READ-20 and READ-20b: the idea given to the therapy, "In that therapy" for whose therapist)',
         decides='whether the merged ISTDP paragraph goes in; if not, his teaching card with my tries'),
    dict(key='a1-p4-20', name='A1-P4', lineage='ADD-A1-P5', scope='paragraph', call='Human', chance=0.55, big=None,
         panel=str(HERE / 'panel' / 'A1-P5-19' / 'PANEL.md'),
         tells=['the quoted sample question', '"slow down, and that they\'d listen" as a two-beat close'],
         diag='the near miss (try 17) read Human Low; try 18 changed "listen" to "hear me out" and read AI, so "listen" stays. '
              'The panel (on the draft-19 version) agreed on all three sentences, but the near-miss rule allows one small '
              'change a check, so this try changes what a reader could take two ways (READ-20): the question\'s "you" is the '
              'therapist where every "you" before it is the reader, so the question is in quotes; S1\'s "which" waits',
         decides='whether the quoted question lifts the near miss toward High; if not, the next small change is S1\'s "which"'),
    dict(key='ic2-10', name='IC2', lineage='IC-IC2-B', scope='paragraph', call='Human', chance=0.55, big=None,
         tells=['"in their trials most people ... got better"'],
         diag='the near miss (Human: High 38, Medium 20): the Medium window is the second sentence, where "they\'ve helped '
              'people" says neither how many nor in what; now how many got better, in the trials',
         decides='whether the second sentence reads High'),
    dict(key='a3-p1-20', name='A3-P1', lineage='ADD-A3-P1p2', scope='paragraph', call='Human', chance=0.5, big=None,
         tells=['"In the first," as a turn', '"It\'s real, but" as a contrast'],
         diag='the short opening paragraph read Medium as its own window in five tries; merged into the paragraph after it, '
              '"In the first," tying the two, it is no longer a short window of its own; READ-20\'s fix: the false alarm and '
              'that the pain is real are two sentences',
         decides='whether the opening reads High; if not, his teaching card'),
]


def main():
    bad = 0
    only = set(sys.argv[1:])
    for r in RUNS:
        if only and r['key'] not in only:
            continue
        txt = HERE / 'texts' / 'v20' / ('%s.txt' % r['name'])
        rec = HERE / 'receipts' / 'v20' / ('%s.receipt.json' % r['name'])
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
