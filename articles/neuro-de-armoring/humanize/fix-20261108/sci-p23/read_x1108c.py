"""The comparative read of the paragraph his answers of 2026-11-08 15:45 UTC put in, beside his post (gates E284, E294):
mine, sentence by sentence, for anything garbled, unclear, lost or vaguer than his.

- SC-97 (block 97): one sentence changes, the reason for not filling up on lean protein: "because your body turns the
  extra protein into sugar through gluconeogenesis, and that keeps you out of ketosis" becomes "since your body can only
  take so much protein: past about a third of your calories it can make you sick (Bilsborough & Mann, 2006), so the rest
  of your energy has to come from fat". The instruction, the example (chicken breast), Strategy B, its carb limit and his
  keto-flu sentence with its link are as they were; the new reason is plain and leads back to "eat fat until you're
  full". Nothing garbled, lost or vaguer.
No finding.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/sci-p23/read_x1108c.py
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

STARTS = ["For the long run there's Strategy B"]


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
              article='HUMANIZED-SO-FAR.md at %s: the approved SC-97 (block 97) read beside his post\'s by the lead '
                      'session (E284, E294)' % hashlib.sha256(md.encode('utf-8')).hexdigest()[:8])
    print('recorded', len(cov))


if __name__ == '__main__':
    main()
