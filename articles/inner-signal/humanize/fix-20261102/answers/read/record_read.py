"""READ-RECORD.json for the lead session's read of the cards Joel approved on Hypnosis Guide Cards, 1 November (2)
(gate E284, E294): the nine paragraphs the eight approved cards changed (W-92, W-111, W-119, G-23, W-270, W-271, W-283,
W-289), at their present words, read beside his published version, his inner child guide's lines the icguide cards
restored, and the paragraphs around them, then linted (tools/humanization/tells_lint.py).

The read, 2 November: each says what its card said it would and nothing of his went missing. The lint names his own
words (his inner child guide's list of ways to make up for what you did, "fishies", "loveyhuasca", "reparent") and coach
phrases that are his instructions; no sentence of ours needed rewording. The 16 revised cards are his own texts
(ANSWERS-20261102-1643.json and EDITS-joel-20261102-pangram.json), which the comparison gate counts as his.

  python3 articles/inner-signal/humanize/fix-20261102/answers/read/record_read.py
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
F = HERE.parents[1]
H = F.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402


def main():
    rec = json.loads((F / 'APPLIED-S1101.json').read_text(encoding='utf-8'))
    review = json.loads((H / 'fix-20261101' / 'sections' / 'review' / 'REVIEW-S1101.json').read_text(encoding='utf-8'))
    bl = sr.blocks((H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'))
    now = {b['text'] for b in bl}
    approved = [s for s in review['suggestions'] if rec['fates'][s['id']].startswith('approved:')]
    after = [e['after'] for s in approved for e in s['edits']]
    missing = [a[:80] for a in after if a not in now]
    assert not missing, missing
    cov = sorted({cr.phash(a) for a in after})
    cr.record(HERE, findings=[], coverage=cov, dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: the %d paragraphs the %d cards Joel approved on 2 November changed '
                      '(%s), read by the lead session beside his published version and his inner child guide, then '
                      'linted (tells_lint.py); none needed rewording (E284, E294)'
                      % (rec['after_sha256'][:8], len(after), len(approved), ', '.join(s['id'] for s in approved)))
    print(len(cov), 'paragraphs recorded')


if __name__ == '__main__':
    main()
