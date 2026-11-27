#!/usr/bin/env python3
"""predict_v13.py - the predictions for draft 13's checks (the somatic ledger), written before any of them goes to Pangram.

  python3 articles/somatic-therapies/experiments/additions-20261126/predict_v13.py
"""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles' / 'somatic-therapies' / 'humanize' / 'pangram-ledger.jsonl'
TOOL = ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'
DET = "Pangram 4.1 (web app, his account, in the desktop app's browser pane)"
HUM = ('drafts 10 to 13, each read by fresh Fable readers against his fixes and for need, fit and contradictions, every '
       'mark acted on or kept with a reason in the receipt; A1 rebuilt the way his Imagery Rescripting rewrite opens (on '
       'what the reader already knows, the two sections above)')
FIRST = ('payoff: each sentence opens on the reader\'s case or on what the therapy does for them ("If that\'s you", "It\'s '
         'usually anxiety about the feeling", "If you can only handle a little", "And if what you can\'t let in is '
         'kindness"); join: the nine-word tag line joined into the sentence that names the first therapy, the watching and '
         'its purpose in one sentence; plain: "slip away" throughout, "tense muscles, sighing, or your thinking going foggy"')
BIG = ('A1\'s draft-7 paragraphs read AI 100% (High) and their small fixes were spent in drafts 8 and 9; after his A2 '
       'rewrite (lesson somatic-2026-11-27b) the section is rebuilt to open on the two sections above, and drafts 10 to 13 '
       'act on four rounds of fresh reads')

RUNS_A3 = [
    dict(key='a3-p%s-13' % k, lineage='ADD-A3-P%s' % k, scope=sc, call='Human', chance=ch, big=False,
         tells=[tl], diag=dg, decides='whether this paragraph of the approved section reads Human High by itself, '
         'as the rule for a paragraph of mine asks (bad-trips-2026-11-12l)')
    for k, sc, ch, tl, dg in (
        ('1p2', 'pair', 0.5, 'a short opening line', 'the opening (34 words) with the first therapy; in the near miss '
         'the opening and the first therapy\'s first sentence read Human (Medium), and the sentence is now two, "though '
         'real" and "where the doctors haven\'t found any" in the first'),
        ('2', 'paragraph', 0.5, 'a "like going for walks" example', 'the first therapy by itself; the going-back '
         'sentence read Human (Low) in the near miss'),
        ('3', 'paragraph', 0.6, 'percentages in one sentence', 'the PRT evidence, Human (High) in the near miss'),
        ('4', 'paragraph', 0.5, 'three sentences opening on the therapy', 'the EAET paragraph, Human (Low) in the near '
         'miss; "the feelings" for "those feelings"'),
        ('5', 'paragraph', 0.5, 'a colon before the numbers', 'the EAET evidence: Human (Medium) and, for the lower-bar '
         'sentence, Human (Low) in the near miss; "A 30% drop is a lower bar" for "That\'s a lower bar"'),
        ('6', 'paragraph', 0.5, '"the second" and "the first" pointing back', 'how to choose: Human (Medium) and (High) in '
         'the near miss'))
]

RUNS = [
    dict(key='a1-p1-13', lineage='ADD-A1-P1', scope='paragraph', call='AI', chance=0.4, big=True,
         tells=['a long therapy name inside the third sentence', '"If that\'s you" as a turn'],
         diag='draft 7 read AI 100% High; the new opening ties to the two sections above, as his A2 version opens on his guide',
         decides='whether the opening goes in as it is or gets one fix aimed at the window that reads below High'),
    dict(key='a1-p2-13', lineage='ADD-A1-P2', scope='paragraph', call='AI', chance=0.4, big=True,
         tells=['a list of three signs', '"like most people who try this therapy" as an aside'],
         diag='draft 7 read AI (Medium, High); rewritten from the readers\' fixes: the cause, the watching and its purpose, '
              'then the slower version, all in "you"',
         decides='whether the paragraph about how ISTDP stays bearable goes in as it is'),
    dict(key='a1-aedp-13', lineage='ADD-A1-AEDP', scope='paragraph', call='AI', chance=0.35, big=False,
         tells=['the therapy name at the end of the first sentence'],
         diag='the AEDP sentences read AI (Low) inside the draft-7 paragraph; now a paragraph of their own that opens on '
              'the case (kindness that bounces off) and says the therapist\'s one act with care',
         decides='whether the AEDP paragraph goes in as it is'),
    dict(key='a1-apt-aedp-13', lineage='ADD-A1-APT-AEDP', scope='pair', call='AI', chance=0.35, big=False,
         tells=['two paragraphs that each open on "If"/"And if"'],
         diag='the Affect Phobia sentence, word for word as it read Human High in the draft-7 near miss (b4f0fea6), is 38 '
              'words, so it is checked with the AEDP paragraph after it (the old ADD-A1-P3 lineage, split in two)',
         decides='whether the Affect Phobia paragraph still reads Human High beside its new neighbour'),
    dict(key='a1-aedp-ask-13', lineage='ADD-A1-ASK', scope='pair', call='AI', chance=0.35, big=False,
         tells=['a quoted question of two parts', '"keep looking" as an ending'],
         diag='the booking paragraph is 48 words, under the web app\'s 50, so it is checked with the AEDP paragraph before it',
         decides='whether the booking questions go in as they are'),
    dict(key='a1-sec-13', lineage='ADD-A1', scope='section', call='AI', chance=0.3, big=True,
         tells=['three named therapies in a row, each by case'],
         diag='the whole section after the paragraph checks; draft 5 read AI 100% High',
         decides='whether the section reads Human as a whole once its paragraphs do'),
    dict(key='a3-sec-13', lineage='ADD-A3', scope='section', call='Human', chance=0.5, big=False,
         tells=['the evidence numbers in two paragraphs'],
         diag='the near miss (Mostly Human, 3% AI) with five small changes for sense the readers asked for: "though real" and '
              '"where the doctors haven\'t found any" (so it rests on what the doctors found), the attention said as its own '
              'sentence "without fearing it", "the feelings", "A 30% drop is a lower bar"',
         decides='which windows still read below High, for the next one-word fix'),
    dict(key='ic1-pair-4', lineage='IC-IC1', scope='pair', call='Human', chance=0.55, big=False,
         tells=['"first ... and later" in one sentence'],
         human=['his own J. paragraph, as it stands in the live inner child guide ("Ok, that one might seem too easy, '
                'although for J, it might take years to imagine that correction.")'],
         diag='my one sentence after his J. paragraph (41 words, so checked with it)',
         decides='whether the Imagery Rescripting sentence goes into the inner child guide as it is'),
    dict(key='ic2-4', lineage='IC-IC2', scope='paragraph', call='AI', chance=0.4, big=False,
         tells=['two long therapy names in one sentence'],
         diag='three short sentences ending on his own pointer form ("For more on that, check my detox guide.")',
         decides='whether the pain therapies paragraph goes into the inner child guide as it is'),
]


def main():
    bad = 0
    for r in (RUNS_A3 if 'a3' in sys.argv[1:] else RUNS):
        base = r['key'].rsplit('-', 1)[0].upper().replace('A1-P1', 'A1-P1')
        name = {'a3-p1p2-13': 'A3-P1P2', 'a3-p2-13': 'A3-P2', 'a3-p3-13': 'A3-P3', 'a3-p4-13': 'A3-P4',
                'a3-p5-13': 'A3-P5', 'a3-p6-13': 'A3-P6', 'a1-p1-13': 'A1-P1', 'a1-p2-13': 'A1-P2', 'a1-aedp-13': 'A1-P4', 'a1-apt-aedp-13': 'A1-P3P4',
                'a1-aedp-ask-13': 'A1-P4P5', 'a1-sec-13': 'A1-SEC', 'a3-sec-13': 'A3-SEC', 'ic1-pair-4': 'IC1-PAIR',
                'ic2-4': 'IC2'}[r['key']]
        txt = HERE / 'texts' / 'v13' / ('%s.txt' % name)
        rec = HERE / 'receipts' / 'v13' / ('%s.receipt.json' % name)
        cmd = [sys.executable, str(TOOL), 'predict', str(LEDGER), '--lineage', 'somatic-therapies/' + r['lineage'],
               '--scope', r['scope'], '--text', str(txt), '--call', r['call'], '--chance', str(r['chance']),
               '--diagnosis', r['diag'], '--decides', r['decides'], '--key', r['key'], '--batch', 'add1127',
               '--detector', DET, '--receipt', str(rec), '--humanized', HUM, '--first-fix', FIRST]
        for t in r['tells']:
            cmd += ['--tells', t]
        for t in r.get('human', []):
            cmd += ['--human-tells', t]
        if r['big']:
            cmd += ['--big-change', BIG]
        res = subprocess.run(cmd, capture_output=True, text=True)
        print(r['key'], 'OK' if res.returncode == 0 else 'REFUSED', (res.stdout + res.stderr).strip()[:1500])
        bad += res.returncode != 0
    return bad


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
