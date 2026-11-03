"""READ-RECORD.json for the six paragraphs of Joel's answers of 2026-11-01 18:50 UTC that the comparison gate couldn't
match to his own words: the four approved suggestions of mine (S-14, S-20, S-636, S-782, the cards' words exactly) and
two paragraphs of his versions that carry a typo fix ("Jim Carrey" in N-238, "need to overcome" in N-580). Read by me
(the lead session, Claude Opus 5.5, not a cheaper reader: E294) beside his published version (source/published-20260928.md)
and his answers file: S-14 keeps the published point that the results show "in ordinary life" ("in your day-to-day
life"); S-20 says what you notice shapes your next invite, as the published quick start does; S-636 names the two-hand
practice instead of teaching it again; S-782 marks the study's title; the two of his say what his versions say.

  python3 articles/inner-signal/humanize/fix-20261101/applied/read/record_applied_read.py
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[2]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402

STARTS = ['“How do I do this?” you ask.', 'You\'ll follow whatever you notice', 'Do the two-hand practice from Working',
          'The study Not everybody has an inner voice', 'It\'s fine to borrow qualities such as warmth',
          'That includes not manipulating anyone to feel like their "no"']


def main():
    bl = sr.blocks((H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'))
    cov = []
    for s in STARTS:
        hits = [b for b in bl if b['text'].startswith(s)]
        assert len(hits) == 1, s
        cov.append(cr.phash(hits[0]['text']))
    cr.record(HERE, findings=[], coverage=cov, dispositions={},
              article='HUMANIZED-SO-FAR.md: six paragraphs of his answers of 2026-11-01 (four approved suggestions of '
                      'mine, two of his versions with a typo fixed), read by the lead session (E294)')
    print(len(cov), 'paragraphs recorded')


if __name__ == '__main__':
    main()
