"""The comparative read of the paragraphs his answers of 2026-11-08 15:08 UTC put in, beside his post (gates E284, E294):
mine, sentence by sentence, for anything garbled, unclear, lost or vaguer than his.

- SC-24: only the figure changes ("less than 1/24th" to "about one-sixteenth", with Perry 2023); every other word is his.
- SC-52: "is often a fuel crisis" becomes "may partly be a fuel problem", and the insulin-resistance cause and "The engine
  is flooded" give way to the PTSD scans; both changes are the science he approved, and the paragraph still hands the
  next one its premise ("burning less sugar").
- SC-53: the switch of fuels stays as the plan in one line; ketones and PQQ are said as far as shown, mitochondria
  explained where first used; the shower sentence and "immediately" go, as he approved. Nothing garbled or vaguer.
- SC-56: "fails to save the visual details" gains "as strongly, and the memory flashes back less often"; the permanently
  reduced sting goes, as he approved, and the lab finding says what the reader can expect.
- SC-57: "more effective than simple counting" becomes untested, built on the same idea, and why to skip counting and
  word games; the method, its name and its reason stay.
- Block 51 (his new paragraph): his words with one spelling ("principal") and his three links written out; nothing else.
No finding.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/sci-cde/read_x1108b.py
Writes read/READ-RECORD.json here.
"""
import hashlib
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402

STARTS = ['We are operating on about one-sixteenth', 'While the science is focused', 'The Problem: "Brain Fog" may partly',
          'The Fix: If the brain is burning less sugar', 'The Fix ("The Jammer"):', 'Instead of Tetris (which requires']


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    bl = sr.blocks(md)
    cov = []
    for s in STARTS:
        hits = [b for b in bl if b['text'].startswith(s)]
        assert len(hits) == 1, (s, len(hits))
        cov.append(cr.phash(hits[0]['text']))
    d = HERE / 'read'
    d.mkdir(exist_ok=True)
    cr.record(d, findings=[], coverage=cov, dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: the five approved C-to-E cards and his new paragraph (block 51) read '
                      'beside his post\'s by the lead session (E284, E294)' % hashlib.sha256(md.encode('utf-8')).hexdigest()[:8])
    print('recorded', len(cov))


if __name__ == '__main__':
    main()
