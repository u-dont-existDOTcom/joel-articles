#!/bin/sh
# CONFIDENCE.md and CONFIDENCE.json for batch 483's recheck (gate E278): every window that isn't High-confidence Human,
# with whose words. Run from the repository root:  sh articles/inner-signal/humanize/fix-20261029/b483/recheck/read/confidence_483.sh
H=articles/inner-signal/humanize
R=$H/fix-20261029/b483/recheck/read
python3 tools/humanization/window_confidence.py $R/RESULT-A.json $R/RESULT-B.json --out $R/CONFIDENCE.md --json $R/CONFIDENCE.json \
  --article $H/fix-20261029/b483/CANDIDATE-MASTER.md --his $H/fix-20261029/recheck/read/HIS-28.md \
  --other "batch 483 candidate=$R/CANDIDATE-WORDS.md" \
  --other "batch 482 candidate=$H/fix-20261029/b482/recheck/read/CANDIDATE-WORDS.md" \
  --other "his inner child guide=articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md" \
  --other "his published version=$H/source/published-20260928.md"
python3 tools/humanization/part_forecast.py score $H/fix-20261029/b483/recheck/FORECAST-A.json $R/RESULT-A.json --out $R/SCORE-A.md \
  --link https://www.pangram.com/feed/d7900092-2691-46bd-b76a-d2043526509c
python3 tools/humanization/part_forecast.py score $H/fix-20261029/b483/recheck/FORECAST-B.json $R/RESULT-B.json --out $R/SCORE-B.md \
  --link https://www.pangram.com/feed/845b60a9-9b58-4824-bc34-29cb1e395efa
