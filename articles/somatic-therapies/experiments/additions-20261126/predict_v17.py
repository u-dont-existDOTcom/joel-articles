#!/usr/bin/env python3
"""predict_v17.py - the predictions for draft 17's checks (the somatic ledger), written before any of them goes to Pangram.

  python3 articles/somatic-therapies/experiments/additions-20261126/predict_v17.py
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
    dict(key='a1-p1-17', name='A1-P1', lineage='ADD-A1-P1', scope='paragraph', call='AI', chance=0.4,
         panel=str(HERE / 'panel' / 'A1-P1-15' / 'PANEL.md'),
         big=('the draft-13 try read AI in both windows, and the tell panel on the draft-15 wording (A1-P1-15) agreed on both '
              'its sentences: the "Even once ..., you can still" bridge, the even "by X, or by Y" pair, "For that, there\'s", '
              'the "slip away" echo and the soft "turn back toward the feeling"; this try fixes each: an opening on where the '
              'reader stands, the two ways in plain words, and what the therapist actually says'),
         tells=['"By this layer" as an opener', 'an example quote with "something like"'],
         diag='draft 13 read AI 98%; the panel agreed on every sentence of the next wording; now three sentences of uneven '
              'length, no echo, and the therapist\'s act said as words in the room ("Notice how you just started explaining?")',
         decides='whether the opening goes in, or the next draft comes from a writer of another family (tell_panel.py)'),
    dict(key='a1-p2-17', name='A1-P2', lineage='ADD-A1-P2', scope='paragraph', call='Human', chance=0.55, big=None,
         tells=['a list of three signs'],
         diag='the near miss (Human: High 41, Medium 37): "handle" was said in the Affect Phobia paragraph too; "take" is the '
              'plain word here',
         decides='whether one word lifts the Medium window to High'),
    dict(key='a1-p5-17', name='A1-P5', lineage='ADD-A1-P5', scope='paragraph', call='AI', chance=0.45,
         big=('the draft-15 try read AI 100% (High, one window): a causal opener ("Since in all three"), a compound ask and a '
              'verdict line; this try says the shared risk first, then asks in his water-therapy form as a question in his '
              'voice, then what he\'d want to hear'),
         tells=['"the kind of thing I\'d ask a water therapist"'],
         diag='a checklist of what to ask read AI; now the risk, his own form of question from the water section, and the '
              'answer he would want',
         decides='whether the booking paragraph goes in'),
    dict(key='ic1-7', name='IC1', lineage='IC-IC1-SELF', scope='paragraph', call='Human', chance=0.55, big=None,
         tells=['"which I only found out about" as a relative clause'],
         human=['"which I only found out about after I wrote this section": his own fact, from his card answer of '
                '2026-11-27 00:55 UTC ("although I didn\'t know it was a therapy when i wrote about it")'],
         diag='the near miss (Human: High 33, Medium 23): the Medium window is the second sentence; "back then" says when the '
              'adult was needed',
         decides='whether the Imagery Rescripting paragraph reads High'),
    dict(key='ic2-pair-7', name='IC2-PAIR', lineage='IC-IC2-PAIR', scope='pair', call='Human', chance=0.5, big=None,
         tells=['two long therapy names after a colon'],
         human=['his own paragraph before it, as it stands in the live inner child guide ("I\'d ask for a chronic pain '
                'specialist ... but don\'t let amelioration of symptoms be the end of the investigation.")'],
         diag='IC2 read Mixed (its first sentence Human, Low; the trial-summary sentence AI, High); the trial summary is cut, '
              'since the somatic section it links to gives the trials and their limits, as he asked ("just like a sentence '
              'or so"); at 41 words it is checked with his paragraph before it',
         decides='whether the pain therapies sentence goes into the inner child guide'),
    dict(key='a3-p1p2-17', name='A3-P1P2', lineage='ADD-A3-P1p2', scope='pair', call='Human', chance=0.55, big=None,
         tells=['a short opening line'],
         diag='the near miss: the opening line read Human (Medium) twice; "pain" could be read as emotional pain in this '
              'guide (READ-16), so "physical pain", and "here" for "to this guide"',
         decides='whether the opening line reads High'),
]


def main():
    bad = 0
    only = set(sys.argv[1:])
    for r in RUNS:
        if only and r['key'] not in only:
            continue
        txt = HERE / 'texts' / 'v17' / ('%s.txt' % r['name'])
        rec = HERE / 'receipts' / 'v17' / ('%s.receipt.json' % r['name'])
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
