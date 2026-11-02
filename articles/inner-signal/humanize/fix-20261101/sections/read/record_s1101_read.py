"""READ-RECORD.json for the lead session's read of batch s1101's fixes (FIXES-S1101.json, both rounds): every paragraph
the fixes changed, at its present words (APPLIED-S1101.json), read beside his published version and the paragraphs
around it (E294, E306), then linted (tools/humanization/tells_lint.py) and reworded where the linter named a tell that
was really there.

Round 1 (the session of 1 November 21:14 UTC): ten windows in Sometimes start with the whole, Let the child speak, The
two-hand practice, Working with your guards and Don't rush the repair; seven of its sentences reworded after the lint.
Round 2 (the session after Joel's message of 22:27 UTC, fixes_round2.py): the rest of the windows in our words, in
eighteen sections. Each fix was written from its published passage and read again in place; the lint's named tells were
reworded where they were real (an announcing "Here's one ...", "it's good to" four times, a phrase said three times in
one paragraph, two "actually"s, a list of adult jobs given as one example, a tag list cut to two). What the lint still
names, and why it stays: lists the published passage names item by item (the eight warning signs, the five things a
presupposition may assume, the qualities, the three adults, the anchors, the nominalizations), the 1% (his published
number), "nominalization" (the term), and the paragraph openers it counts across paragraphs of different sections. The
two fixes of round 1 in Working with your guards that changed his inner child guide's words were undone (his words are
back, and the fix is his card G-23), so those paragraphs are as they were before batch s1101 and outside this record.

  python3 articles/inner-signal/humanize/fix-20261101/sections/read/record_s1101_read.py
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
    rec = json.loads((D / 'APPLIED-S1101.json').read_text(encoding='utf-8'))
    bl = sr.blocks((H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'))
    now = {b['text'] for b in bl}
    after = [a for c in rec['changed'] for a in c['after']]
    missing = [a[:80] for a in after if a not in now]
    assert not missing, missing
    cov = sorted({cr.phash(a) for a in after})
    cr.record(HERE, findings=[], coverage=cov, dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: the %d paragraphs the fixes of batch s1101 changed (FIXES-S1101.json, '
                      'rounds 1 and 2), read by the lead session beside his published version and the paragraphs around '
                      'them, then linted (tells_lint.py) and reworded where it named a tell that was there (E294, E306)'
                      % (rec['after_sha256'][:8], len(after)))
    print(len(cov), 'paragraphs recorded')


if __name__ == '__main__':
    main()
