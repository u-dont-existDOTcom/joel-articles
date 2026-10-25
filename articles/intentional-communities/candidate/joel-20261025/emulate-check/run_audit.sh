#!/bin/sh
# The community article's Emulate check (tools/humanization/emulate_artifacts.py): his published post first, then his
# own words from his messages and answers.
cd "$(dirname "$0")/../../../../.." || exit 1
D=articles/intentional-communities/candidate/joel-20261025/emulate-check
python3 tools/humanization/emulate_artifacts.py audit "${1:-articles/intentional-communities/candidate/joel-20261024/answer65/WORKING.html}" \
  --source articles/intentional-communities/original.md \
  --source $D/JOEL-TEXTS.txt --allowed $D/JOEL-EDITS-20261020.md \
  --out "${2:-$D}" --parts 8
