#!/usr/bin/env python3
"""predict_v15.py - the predictions for draft 15's checks (the somatic ledger), written before any of them goes to Pangram.

  python3 articles/somatic-therapies/experiments/additions-20261126/predict_v15.py
"""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles' / 'somatic-therapies' / 'humanize' / 'pangram-ledger.jsonl'
TOOL = ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'
DET = "Pangram 4.1 (web app, his account, in the desktop app's browser pane)"
HUM = ('drafts 10 to 14, each read by fresh Fable readers against his fixes and for need, fit and contradictions (READ-14 on '
       'draft 14, acted on in this one), every mark acted on or kept with a reason in the receipt')
FIRST = ('payoff: each text opens on the reader\'s state or the news ("Even once you can feel your body just fine", "It turns '
         'out there\'s an actual clinical therapy for this", "While the investigation goes on"); join: the case and the '
         'therapy in one run, the booking questions as one indirect question; plain: "slip away", "talk therapies", '
         '"I\'d keep looking"')
RUNS = [
    dict(key='a1-p1-15', name='A1-P1', lineage='ADD-A1-P1', scope='paragraph', call='AI', chance=0.4,
         big=('the draft-13 try read AI in both windows (Low on the summary opener "Water therapy and Brainspotting let a '
              'feeling come up on its own.", Medium on the case and the recommendation); this try drops the summary opener '
              'and opens on the reader\'s state after Layer 3, the way the AEDP paragraph that read Human High opens on the '
              'reader\'s case'),
         tells=['"For that, there\'s" naming the therapy'],
         diag='draft 13 read AI 98% (Low 12, Medium 69): a topic-sentence summary of the sections above, then a "some people" '
              'case and an "If that\'s you, look into" recommendation; now one sentence of the reader\'s own state and how '
              'it shows ("by explaining it, or by agreeing ... so you don\'t have to stay in it"), and the therapy as the '
              'answer to it',
         decides='whether the opening goes in, or gets another rewrite with a named cause'),
    dict(key='a1-p2-15', name='A1-P2', lineage='ADD-A1-P2', scope='paragraph', call='Human', chance=0.55, big=None,
         tells=['a list of three signs'],
         diag='the near miss (Human: High 41, Low 34): the Low window is the slower-version sentence; "a slower version of it" '
              'says what it is a version of, and "whenever the anxiety climbs" keeps the two "it"s apart (READ-14)',
         decides='whether two small changes lift the Low window to High'),
    dict(key='a1-p5-15', name='A1-P5', lineage='ADD-A1-P5', scope='paragraph', call='AI', chance=0.45, big=None,
         tells=['"Since in all three" as an opener'],
         diag='the booking paragraph read AI in all its windows in draft 13 (quoted questions with "what if", a verdict '
              'line); now 52 words, checked by itself: why to ask first (all three keep steering you back to your '
              'feelings), then what to ask, then when to walk away, in his "I\'d"',
         decides='whether the booking paragraph goes in'),
    dict(key='ic1-6', name='IC1', lineage='IC-IC1-SELF', scope='paragraph', call='Human', chance=0.5, big=None,
         tells=['"which I only found out about" as a relative clause'],
         human=['"which I only found out about after I wrote this section": his own fact, from his card answer of '
                '2026-11-27 00:55 UTC ("although I didn\'t know it was a therapy when i wrote about it")'],
         diag='my sentence read AI (Medium) after his J. paragraph; now 55 words, checked by itself: the reader\'s case '
              'first, then the therapy with his own aside, then what the therapist has you picture',
         decides='whether the Imagery Rescripting paragraph goes into the inner child guide'),
    dict(key='ic2-6', name='IC2', lineage='IC-IC2', scope='paragraph', call='AI', chance=0.4,
         big=('the draft-13 try read AI 100% (High 57, Low 8): two therapy names and a trial summary in the third person; '
              'this try says it in his first person ("I\'d also look into", as his "I\'d ask for a chronic pain specialist" '
              'just before) and says what the evidence can\'t tell this reader'),
         tells=['two long therapy names after a colon'],
         diag='a summary of two trials read AI; now his "I\'d" voice, the condition first, and how far the trials reach for '
              'attacks like the section\'s',
         decides='whether the pain therapies paragraph goes into the inner child guide'),
    dict(key='a3-p1p2-15', name='A3-P1P2', lineage='ADD-A3-P1p2', scope='pair', call='Human', chance=0.55, big=None,
         tells=['a short opening line'],
         diag='the near miss: the opening line alone read Human (Medium, 9 words); "in the first place" makes it the reader\'s '
              'own reason, said the way people say it',
         decides='whether the opening line reads High'),
    dict(key='a3-p5-15', name='A3-P5', lineage='ADD-A3-P5', scope='paragraph', call='Human', chance=0.55, big=None,
         tells=['percentages in two sentences'],
         diag='the near miss: the lower-bar sentence read Human (Medium); "0 or 1 out of 10" could be read as a count of '
              'people, so it says "getting your pain down to 0 or 1 out of 10"',
         decides='whether the lower-bar sentence reads High'),
    dict(key='a3-p6-15', name='A3-P6', lineage='ADD-A3-P6', scope='paragraph', call='Human', chance=0.6, big=None,
         tells=['"the second" and "the first" pointing back'],
         diag='read Human High by itself; "the two" after "the two trials\' numbers" could be read as the trials (READ-14), so '
              '"the two therapies"',
         decides='whether the one-word fix keeps it High'),
]


def main():
    bad = 0
    only = set(sys.argv[1:])
    for r in RUNS:
        if only and r['key'] not in only:
            continue
        txt = HERE / 'texts' / 'v15' / ('%s.txt' % r['name'])
        rec = HERE / 'receipts' / 'v15' / ('%s.receipt.json' % r['name'])
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
        res = subprocess.run(cmd, capture_output=True, text=True)
        print(r['key'], 'OK' if res.returncode == 0 else 'REFUSED', (res.stdout + res.stderr).strip()[:1200])
        bad += res.returncode != 0
    return bad


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
