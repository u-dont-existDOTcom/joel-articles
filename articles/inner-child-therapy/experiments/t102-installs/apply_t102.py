#!/usr/bin/env python3
"""Turn 102: Joel's answers of 2026-10-23 17:53 UTC (experiments/t102-answers/JOEL-20261023-1753.md), questions 94 and 95.

What this script installs (the two that stayed):
- 95.7 A: "and they may be able to treat it while it's happening" on his diagnostics sentence.
- 95.8 A, in his words: not my second question; his point instead, that the answer is only today's law, so assume what
  you tell won't be completely confidential, especially if it sounds dangerous.
What it installed first and I took back out by hand, after Pangram (experiments/t102-tries/REVIEWS.md):
- 94.2 A (conditional on a check): GPT's "If you have advice, let them take it in at their own pace." made old P5 read
  100% AI alone (borrow-p5#144); his two sentences are back, as they read 100% Human (#134).
- 95.2 A: the guide's temporary, intentional distance read 100% AI over the Untangling paragraph in three shapes
  (untangle-slow#146, #151 and one unscored check); the paragraph is as it was, and the point is question 96.
94.1 A changes nothing. Each changed paragraph gets a note above it. The script asserts each old text occurs once, so it
can't run twice.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
SRC = 'experiments/t102-answers/JOEL-20261023-1753.md'

CHANGES = [
    ('95.7 A: "and they may be able to treat it while it\'s happening" added (PGQ-027).',
     "And when the symptoms come and go randomly,",
     "rather than waiting until you feel well enough to make an appointment.",
     "rather than waiting until you feel well enough to make an appointment, and they may be able to treat it while it's happening."),
    ('95.8 A in his words: his point that the answer is only what the law requires now, and to assume what you tell won\'t be completely confidential, especially if it sounds dangerous, after "I wouldn\'t even bother with that"; his chat words adapted to the paragraph.',
     "So I’d ask them, before handing over any tricky specifics:",
     "Although personally I wouldn't even bother with that. You can always",
     "Although personally I wouldn't even bother with that, because whatever they tell you today, the law can change tomorrow. I'd assume that what you tell won't be completely confidential, especially if it sounds like something dangerous. You can always"),
]


def main():
    lines = ART.read_text(encoding='utf-8').split('\n')
    for what, start, old, new in CHANGES:
        hits = [k for k, l in enumerate(lines) if l.startswith(start) and old in l]
        assert len(hits) == 1, (start, hits)
        k = hits[0]
        assert lines[k].count(old) == 1
        lines[k] = lines[k].replace(old, new)
        lines[k:k] = ['<!-- Turn 102 (his answers of 2026-10-23 17:53 UTC, ' + SRC + '): ' + what + ' -->', '']
    ART.write_text('\n'.join(lines), encoding='utf-8')
    print('applied', len(CHANGES))


if __name__ == '__main__':
    main()
