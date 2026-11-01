"""READ-RECORD.json for my read of the fixes of the second full read (VERIFY-PAIRS.md: every changed paragraph, before
and after, 130 changes, 190 paragraphs after), read by me (the lead session, Claude Opus 5.5, not a cheaper reader:
E294) beside his published version and the paragraphs around each one. The read found seven new sentences that the
linter called tells ("not Y" tails, "doesn't prove", "capacity", "it" at a paragraph start) and one clumsy parenthetical;
each was reworded in FIXES-n.json or apply_fullread2.py and the guide rebuilt from the read's text, and the reworded
paragraphs were read again. Two fixes then turned out to change paragraphs he rewrote on 30 October (N-276, the
fingers script; R-561, Reframing): the first went to him as a card (F7.5) and the second keeps his words, with only
quotation marks (straight, like his) and a comma (F13.19); both paragraphs were read again as they now stand.
Coverage is every paragraph the fixes changed, at its present words (VERIFY-PAIRS.md, read/verify_pairs.py).

  python3 articles/inner-signal/humanize/fix-20261101/fullread2/read/record_fix_read.py
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
D = HERE.parent
H = D.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402


def main():
    rec = json.loads((D / 'APPLIED-FULLREAD2.json').read_text(encoding='utf-8'))
    bl = sr.blocks((H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'))
    now = {b['text'] for b in bl}
    after = [a for c in rec['changed'] for a in c['after']]
    missing = [a[:80] for a in after if a not in now]
    assert not missing, missing
    cov = sorted({cr.phash(a) for a in after})
    cr.record(HERE, findings=[], coverage=cov, dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: the %d paragraphs the second full read\'s fixes changed, read by the '
                      'lead session beside his published version (E294)' % (rec['after_sha256'][:8], len(after)))
    print(len(cov), 'paragraphs recorded')


if __name__ == '__main__':
    main()
