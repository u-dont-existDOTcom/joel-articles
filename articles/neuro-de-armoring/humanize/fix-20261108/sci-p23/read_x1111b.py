"""The comparative read of the paragraph his chat approval of 2026-11-11 22:44 UTC put in, beside his post (gates E284, E294):
mine, sentence by sentence, for anything garbled, unclear, lost or vaguer than his.

- SC-106e (the potassium paragraph, block 104 now that the two label blocks before it are cut): his post's paragraph
  said the KCNQ "brakes" run on potassium, that low potassium (common in high stress) makes them fail, and pictured it
  as a pedal and a car that won't stop. Mine says nerves need potassium and most people eat too little, what raising it
  has done for mood (with his two Reddit links as firsthand reports) and thinking, who needs more, blood pressure, his
  paleo view and the caution, in eight sentences. The point the post was making, that low potassium matters for a
  stressed nervous system, is kept on what holds; the brakes story and its picture go, as he approved. Each sentence
  reads on its own and in order; the target, the menu and "Eat 2 large potatoes and 2 cups of greens every single day."
  follow as before. Nothing garbled, lost from the step, or vaguer.
No finding.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/sci-p23/read_x1111b.py
Writes read-x1111b/READ-RECORD.json here.
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

STARTS = ['The Science: Your nerves need potassium to fire and reset']


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    bl = sr.blocks(md)
    cov = []
    for s in STARTS:
        hits = [b for b in bl if b['text'].startswith(s)]
        assert len(hits) == 1, (s, len(hits))
        cov.append(cr.phash(hits[0]['text']))
    d = HERE / 'read-x1111b'
    d.mkdir(exist_ok=True)
    cr.record(d, findings=[], coverage=cov, dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: SC-106e as he approved it in chat (the potassium paragraph) read beside his post\'s by the lead '
                      'session (E284, E294)' % hashlib.sha256(md.encode('utf-8')).hexdigest()[:8])
    print('recorded', len(cov))


if __name__ == '__main__':
    main()
