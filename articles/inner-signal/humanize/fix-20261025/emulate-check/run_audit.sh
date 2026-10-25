#!/bin/sh
# The guide's Emulate check (tools/humanization/emulate_artifacts.py): his published post first, then his editor HTML
# and his drafts; allowed: the new sentences he approved on 2026-10-25 and his inner child guide.
cd "$(dirname "$0")/../../../../.." || exit 1
D=articles/inner-signal/humanize/fix-20261025/emulate-check
python3 tools/humanization/emulate_artifacts.py audit "${1:-articles/inner-signal/humanize/HUMANIZED-SO-FAR.md}" \
  --source articles/inner-signal/humanize/source/published-20260928.md \
  --source articles/inner-signal/humanize/source/substack-editor-20260928.html \
  --source articles/inner-signal/source/owner-editor-original.html \
  --source articles/inner-signal/source/owner-editor-20260911.html \
  --source articles/inner-signal/source/r02-pre-sync-git.html \
  --allowed $D/ALLOWED.txt --allowed articles/inner-signal/humanize/fix-20261025/ic-align/IC-GUIDE.txt \
  --out "${2:-$D}" --parts 10
