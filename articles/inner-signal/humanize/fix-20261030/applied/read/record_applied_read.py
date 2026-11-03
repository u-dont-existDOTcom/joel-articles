"""READ-RECORD.json for the four paragraphs of Joel's answers of 2026-10-30 14:35 UTC that the comparison gate couldn't
match to his own words, because they carry a typo fix or the change his comment asked for: read by me (the lead session,
Claude Opus 5.5, not a cheaper reader: E294) beside his answers file (fix-20261029/b483/review/ANSWERS-20261030-1435.json)
and the guide's paragraph before them. Each says what his version says; the only changes are the ones listed in
APPLIED-483.json ("subsconscious", "awarenes", "sutble" fixed) and "First, access your" (his R-96 comment).

  python3 articles/inner-signal/humanize/fix-20261030/applied/read/record_applied_read.py
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[2]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402

STARTS = ['First, access your witnessing position', '"Keep it simple, stupid!"',
          "Does the hypnotist treat my lack of awareness", 'Keep aware of the subtle inner signal']


def main():
    bl = sr.blocks((H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'))
    cov = []
    for s in STARTS:
        hits = [b for b in bl if b['text'].startswith(s)]
        assert len(hits) == 1, s
        cov.append(cr.phash(hits[0]['text']))
    cr.record(HERE, findings=[], coverage=cov, dispositions={},
              article='HUMANIZED-SO-FAR.md: four paragraphs of his answers of 2026-10-30 with a typo fixed or his R-96 '
                      'change, read by the lead session (E294)')
    print(len(cov), 'paragraphs recorded')


if __name__ == '__main__':
    main()
