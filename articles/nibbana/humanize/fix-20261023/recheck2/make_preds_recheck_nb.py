"""Nibbāna's second whole-article recheck prediction (2026-10-23), written before the paste, let alone the check.

  python3 articles/nibbana/humanize/fix-20261023/recheck2/make_preds_recheck_nb.py   (from the repo root, after make_recheck_nb.py)

The text is DRAFT-TEXT.txt, the draft's text as the check reads it (the working copy's, single spaces, the embedded notes
included; E233). If the rendered draft differs from it, this prediction is voided and written again on the rendered text
before Joel checks it.
"""
import pathlib, subprocess, sys

X = pathlib.Path(__file__).resolve().parent
REPO = X.parents[4]
LEDGER = X.parents[1] / 'pangram-ledger.jsonl'
DETECTOR = "pangram 4.1, Pangram's check of the Substack draft (free, Joel's account)"
P = dict(
    lineage='NB-whole', scope='article', key='NB-whole-n2', batch='n2r', call='AI', chance=0.15,
    diagnosis='since the first recheck (Mostly Human Written, 2.9% AI, 12 AI windows; https://www.pangram.com/feed/'
              '6a726359-1fce-4ec3-8a06-e957032fc91e): the four stretches that were AI there and in every try alone are now '
              'Joel\'s own rewrites (windows 30 and 31, the near-death reports; 75 and 76, SN 22.22 and the proton; 123 and '
              '124, the Diamond Sutra\'s sources; 160 and 161, the driving caution), each "dark green" in his own check; window '
              '129 (science) is try 1\'s words by his answer N1 a (Human, 0% AI, alone); window 120 (rebirth) is Emulate\'s '
              'sentence bj (Human, High, alone, where my n1 sentence was Human, Low); window 18 is reworded (Low, so the API '
              'could not screen it); window 125 ("The Diamond Sutra verse is still beautiful.") is untouched, now after his '
              'new paragraph',
    tells='window 125, untouched; window 18\'s new wording, unscreened; his rewrites were checked alone, and a stretch can '
          'read AI in place and Human alone (E215); new text moves the windows, and Low ones can turn up where it changed',
    human='his four rewrites in his own register ("btw", "the Boulder Bank", "consciousness is basically the best magic '
          'trick", "Buddhist drivers who meditated too hard"); the rebirth sentence\'s scare quotes and plain links; his '
          'story around them, dark green last time',
    shading='green: his four rewrites, the rebirth and science sentences and his story; Low red possible: window 125 and the '
            'reworded window 18, or a new Low window where the text changed',
    decides='whether his rewrites and the n2 sentences hold in place, which windows are left for him or for Emulate\'s re-run '
            'next, and whether the article can go back to him as passing')


def main():
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
                        '--lineage', P['lineage'], '--scope', P['scope'], '--text', str(X / 'DRAFT-TEXT.txt'), '--key', P['key'],
                        '--batch', P['batch'], '--call', P['call'], '--chance', str(P['chance']), '--tells', P['tells'],
                        '--human-tells', P['human'], '--diagnosis', P['diagnosis'], '--decides', P['decides'],
                        '--shading-expected', P['shading'], '--detector', DETECTOR], capture_output=True, text=True, cwd=REPO)
    print((r.stdout or r.stderr).strip()[-400:])
    return r.returncode


if __name__ == '__main__':
    sys.exit(main())
