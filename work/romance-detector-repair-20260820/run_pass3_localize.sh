#!/usr/bin/env bash
set -u -o pipefail

JOEL_REPO="u-dont-existDOTcom/joel-articles"
PANGRAM_REPO="u-dont-existDOTcom/pangram-humanization-lab"
JOEL_BRANCH="task/romance-detector-repair-20260820"
EVIDENCE_BRANCH="evidence/romance-pass3-gui-20260820"
P2_SHA="c6ef42419a3db2e82b1ff4f9370fc85bca4fa8c061c61dd6a1b5d28171d9908c"

fail() {
  echo
  echo "ERROR: $*"
  echo "No Pangram detector submission was made by this localization command."
  exit 1
}

need() {
  command -v "$1" >/dev/null 2>&1 || fail "missing required command: $1"
}

need gh
need git
need python3
need sha256sum

gh auth setup-git >/dev/null 2>&1 || fail "GitHub authentication/setup failed"

ROOT="$(mktemp -d /tmp/romance-pass3-localize.XXXXXX)"
JOEL="$ROOT/joel-articles"
PANGRAM="$ROOT/pangram-humanization-lab"

echo "=== Recover exact pass-3 Part 2 ==="
gh repo clone "$JOEL_REPO" "$JOEL" -- --quiet || fail "could not clone joel-articles"
cd "$JOEL" || fail "could not enter joel-articles"
git fetch origin "$JOEL_BRANCH" --quiet || fail "could not fetch Romance task branch"
git switch -C "$JOEL_BRANCH" "origin/$JOEL_BRANCH" >/dev/null || fail "could not switch to Romance task branch"

P2="$JOEL/work/romance-detector-repair-20260820/materialized-pass3/candidate-part-2.txt"
[ -f "$P2" ] || fail "Git-durable pass-3 Part 2 is missing"
printf '%s  %s\n' "$P2_SHA" "$P2" | sha256sum --check --strict \
  || fail "pass-3 Part-2 hash does not match the already-paid result"

echo "Pass-3 SHA verified: $P2_SHA"
echo "Detector submission path: NONE — History localization only"

echo
echo "=== Recover exact already-paid Pangram evidence ==="
gh repo clone "$PANGRAM_REPO" "$PANGRAM" -- --quiet || fail "could not clone Pangram lab"
cd "$PANGRAM" || fail "could not enter Pangram lab"
git fetch origin "$EVIDENCE_BRANCH" --quiet || fail "could not fetch pass-3 GUI evidence branch"
git switch -C "$EVIDENCE_BRANCH" "origin/$EVIDENCE_BRANCH" >/dev/null \
  || fail "could not switch to pass-3 GUI evidence branch"

GH_LOGIN="$(gh api user -q .login)" || fail "could not read GitHub login"
GH_ID="$(gh api user -q .id)" || fail "could not read GitHub account id"
git config user.name "$GH_LOGIN"
git config user.email "${GH_ID}+${GH_LOGIN}@users.noreply.github.com"

RESULT="state/gui-runs/pangram-4/$P2_SHA/result.json"
[ -f "$RESULT" ] || fail "pass-3 exact result receipt is missing"

REPORT_URL="$(python3 - "$RESULT" <<'PY'
import json, sys
value=json.load(open(sys.argv[1], encoding='utf-8'))
print(value.get('report_url') or '')
PY
)" || fail "could not read stored Pangram report route"
[ -n "$REPORT_URL" ] || fail "stored result does not contain a report route"

python3 -m venv .venv || fail "could not create virtual environment"
source .venv/bin/activate
python -m pip install -q -e '.[browser]' || fail "could not install Pangram GUI dependencies"

echo
echo "=== Read-only Pangram authentication check ==="
pangram-local verify || fail "Pangram GUI authentication is not ready"

echo
echo "=== Localize already-paid pass-3 History result ==="
set +e
pangram-local localize \
  --input "$P2" \
  --expect-sha "candidate-part-2.txt=$P2_SHA" \
  --report-url "$REPORT_URL"
RC=$?
set -e

if [ "$RC" -ne 0 ]; then
  echo
  echo "Read-only localization did not complete cleanly."
  echo "No detector submission occurred."
  echo "Failure evidence was persisted on: $EVIDENCE_BRANCH"
  echo "Tell ChatGPT: done, localization failed"
  exit 0
fi

LOCALIZATION="state/gui-runs/pangram-4/$P2_SHA/localization.json"
[ -f "$LOCALIZATION" ] || fail "localizer returned success but localization.json is missing"

python3 - "$LOCALIZATION" <<'PY'
import json, sys
value=json.load(open(sys.argv[1], encoding='utf-8'))
spans=value.get('spans') or []
ai=[]
for s in spans:
    evidence=s.get('evidence') or []
    labels=[]
    for e in evidence:
        meta=e.get('scalar_metadata') or {}
        if meta.get('label'):
            labels.append(str(meta['label']))
    if any('AI' in label.upper() for label in labels):
        ai.append((s.get('char_start_0'), s.get('char_end_0_exclusive'), labels))
print(f"localized_span_count={value.get('localized_span_count')}")
print(f"collection_validated_overall_window_count={value.get('collection_validated_overall_window_count')}")
print(f"AI-labeled localized spans/windows={len(ai)}")
PY

echo
echo "================ COMPLETE ================"necho "No detector call was made."
echo "Exact pass-3 localization is durable on: $EVIDENCE_BRANCH"
echo "Tell ChatGPT: done"
