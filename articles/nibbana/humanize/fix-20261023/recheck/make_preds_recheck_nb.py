"""Nibbāna's whole-article recheck prediction (2026-10-23), written before the paste, let alone the check.

  python3 articles/nibbana/humanize/fix-20261023/recheck/make_preds_recheck_nb.py   (from the repo root, after make_recheck_nb.py)

The text is DRAFT-TEXT.txt, the draft's text as the check reads it: the working copy's (EXPECTED.txt, the three embedded
notes included, which the editor rebuilt from their links on paste) with three double spaces made single, as the editor
made them on paste ("MN 56  says", "the effort  (wash", "AN 3.88  allows"). The first prediction (NB-whole#20) was written on
EXPECTED.txt before the paste; the rendered check found those three spaces and an image gallery's caption ("Real NASA
space photos!") turned into a paragraph, which was deleted from the draft, so #20 was voided and this one written on the
text the draft now shows (its rendered text hashes to DRAFT-TEXT.txt).
"""
import pathlib, subprocess, sys

X = pathlib.Path(__file__).resolve().parent
REPO = X.parents[4]
LEDGER = X.parents[1] / 'pangram-ledger.jsonl'
DETECTOR = "pangram 4.1, Pangram's check of the Substack draft (free, Joel's account)"
P = dict(
    lineage='NB-whole', scope='article', key='NB-whole-n1', batch='n1r', call='AI', chance=0.02,
    diagnosis='since the check of 2026-10-20 (Mostly Human Written, 4.5% AI, 22 AI windows; https://www.pangram.com/feed/'
              '1ffe8aed-a00a-4273-846c-635ae22b2917): four of its nine High and Medium stretches have their fixes in (windows '
              '12, 51, 120 to 122 and 126), each Human alone through the API and OK by the reader; the other five are as he '
              'wrote them (31 and 32, the near-death reports; 80 to 82, SN 22.22 and the proton; 129 and 130, the Diamond '
              'Sutra; 133, the science list; 164 and 165, the driving caution), all red in place last time and AI alone in '
              'every try; the Low-only windows (20, 24, 29, 73 and 74, 107) are untouched',
    tells='the five unchanged stretches, High last time and AI in every try alone; the Low-only windows where they were',
    human='the four fixes ("whatever pulls everything together", "a playful way of saying", "I\'m asking that last one '
          'because", "a chain of causes with no traveler riding along"); his story around them, dark green last time',
    shading='red: the five unchanged stretches; Low red or light green: windows 20, 24, 29, 73 and 74, 107; green: the four '
            'fixed stretches and his story',
    decides='whether the four fixes hold in place, which Low windows are still red for the next batch, and what goes to Joel '
            'with the five stretches that read AI in every try')


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
