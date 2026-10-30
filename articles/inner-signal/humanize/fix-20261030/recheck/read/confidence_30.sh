#!/bin/sh
# CONFIDENCE.md and CONFIDENCE.json for the recheck of 30 October (gate E278): every window that isn't High-confidence
# Human, with whose words; and the forecasts' scores. Run from the repository root after spots_30.py (it writes HIS-30.md):
#   sh articles/inner-signal/humanize/fix-20261030/recheck/read/confidence_30.sh
H=articles/inner-signal/humanize
R=$H/fix-20261030/recheck/read
python3 tools/humanization/window_confidence.py $R/RESULT-A.json $R/RESULT-B.json --out $R/CONFIDENCE.md --json $R/CONFIDENCE.json \
  --article $H/fix-20261030/recheck/CANDIDATE-MASTER.md --his $R/HIS-30.md \
  --other "his inner child guide=articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md" \
  --other "his published version=$H/source/published-20260928.md"
python3 tools/humanization/part_forecast.py score $H/fix-20261030/recheck/FORECAST-A.json $R/RESULT-A.json --out $R/SCORE-A.md \
  --link https://www.pangram.com/feed/fc1d8dae-ed2b-4050-9c0b-5c1571dc3548
python3 tools/humanization/part_forecast.py score $H/fix-20261030/recheck/FORECAST-B.json $R/RESULT-B.json --out $R/SCORE-B.md \
  --link https://www.pangram.com/feed/48eed31c-7ff5-4392-887c-92663cd6aea8
