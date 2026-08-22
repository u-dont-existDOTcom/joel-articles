#!/usr/bin/env bash
set -u -o pipefail

JOEL_REPO="u-dont-existDOTcom/joel-articles"
PANGRAM_REPO="u-dont-existDOTcom/pangram-humanization-lab"
JOEL_BRANCH="task/romance-detector-repair-20260820"
EVIDENCE_BRANCH="evidence/romance-pass2-api-20260820"
AUDIT_ID="romance-detector-repair-20260820"
SECTION_ID="part2"
MEASUREMENT_KEY="romance-detector-repair-20260820.part2.pass2"
REGISTERED_P1_SHA="ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8"
PRIOR_PASS1_P2_SHA="30f61fb0c490ec1275f3c39c834a38a956041865b63e5592c270d51cc22d5498"
PRIOR_PASS1_P2_HUMAN="0.9137498736"
MAX_PAID_POSTS=6
KNOWN_PRIOR_PART2_POSTS=1

fail() {
  echo
  echo "ERROR: $*"
  echo "No automatic Pangram retry was attempted."
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

ROOT="$(mktemp -d /tmp/romance-pass2-api.XXXXXX)"
JOEL="$ROOT/joel-articles"
PANGRAM="$ROOT/pangram-humanization-lab"
PASS1_DIR="$JOEL/work/romance-detector-repair-20260820/materialized"
PASS2_DIR="$JOEL/work/romance-detector-repair-20260820/materialized-pass2"

echo "=== Clone exact Romance task branch ==="
gh repo clone "$JOEL_REPO" "$JOEL" -- --quiet || fail "could not clone joel-articles"
cd "$JOEL" || fail "could not enter joel-articles"
git fetch origin "$JOEL_BRANCH" --quiet || fail "could not fetch Romance task branch"
git switch -C "$JOEL_BRANCH" "origin/$JOEL_BRANCH" >/dev/null || fail "could not switch to Romance task branch"

GH_LOGIN="$(gh api user -q .login)" || fail "could not read GitHub login"
GH_ID="$(gh api user -q .id)" || fail "could not read GitHub account id"
git config user.name "$GH_LOGIN"
git config user.email "${GH_ID}+${GH_LOGIN}@users.noreply.github.com"

for f in candidate-master.md candidate-part-1.txt candidate-part-2.txt candidate-manifest.json; do
  [ -f "$PASS1_DIR/$f" ] || fail "missing Git-durable pass-1 artifact: $f"
done

echo
echo "=== Materialize pass 2 ==="
rm -rf "$PASS2_DIR"
python3 work/romance-detector-repair-20260820/apply_pass2.py \
  --pass1-master "$PASS1_DIR/candidate-master.md" \
  --pass1-part1 "$PASS1_DIR/candidate-part-1.txt" \
  --pass1-part2 "$PASS1_DIR/candidate-part-2.txt" \
  --output-dir "$PASS2_DIR" \
  || fail "pass-2 materialization/invariant gate failed"

MANIFEST="$PASS2_DIR/candidate-manifest.json"
P1_SHA="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["candidate"]["part1"]["sha256"])' "$MANIFEST")" \
  || fail "could not read restored Part-1 hash"
P2_SHA="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["candidate"]["part2"]["sha256"])' "$MANIFEST")" \
  || fail "could not read pass-2 Part-2 hash"
MASTER_SHA="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["candidate"]["master"]["sha256"])' "$MANIFEST")" \
  || fail "could not read pass-2 master hash"

[ "$P1_SHA" = "$REGISTERED_P1_SHA" ] \
  || fail "Part 1 did not restore exactly to registered hash"

echo "Part 1 restored exactly: $P1_SHA"
echo "Part 2 candidate:        $P2_SHA"
echo "Candidate master:        $MASTER_SHA"
echo "Part 1 Pangram call:     NONE (existing exact result reused)"

python3 -m unittest tests.test_romance_pass2_materializer -q \
  || fail "pass-2 materializer regression test failed"

echo
echo "=== Make pass-2 candidate durable before detector work ==="
git add -- work/romance-detector-repair-20260820/materialized-pass2
if ! git diff --cached --quiet -- work/romance-detector-repair-20260820/materialized-pass2; then
  git commit -m "Materialize Romance detector-repair pass 2" >/dev/null \
    || fail "could not commit pass-2 candidate"
fi
git push origin "HEAD:refs/heads/$JOEL_BRANCH" >/dev/null \
  || fail "could not push pass-2 candidate"

echo "Pass-2 candidate is durable on GitHub."

echo
echo "=== Prepare Pangram API evidence branch ==="
gh repo clone "$PANGRAM_REPO" "$PANGRAM" -- --quiet || fail "could not clone Pangram lab"
cd "$PANGRAM" || fail "could not enter Pangram lab"
git fetch origin main --quiet || fail "could not refresh Pangram main"

if git ls-remote --exit-code --heads origin "refs/heads/$EVIDENCE_BRANCH" >/dev/null 2>&1; then
  git fetch origin "$EVIDENCE_BRANCH" --quiet || fail "could not fetch existing evidence branch"
  git switch -C "$EVIDENCE_BRANCH" "origin/$EVIDENCE_BRANCH" >/dev/null \
    || fail "could not resume evidence branch"
  echo "Resuming existing evidence branch; cache/checkpoint rules will prevent duplicate POSTs."
else
  git switch -c "$EVIDENCE_BRANCH" origin/main >/dev/null \
    || fail "could not create API evidence branch"
  git push -u origin "$EVIDENCE_BRANCH" >/dev/null \
    || fail "could not make API evidence branch durable"
fi

git config user.name "$GH_LOGIN"
git config user.email "${GH_ID}+${GH_LOGIN}@users.noreply.github.com"

mkdir -p state/api-audits
LEDGER="state/api-audits/${AUDIT_ID}-${SECTION_ID}.json"
python3 - "$LEDGER" "$P2_SHA" <<'PY'
import json, pathlib, sys
path=pathlib.Path(sys.argv[1])
sha=sys.argv[2]
value={
  "format":"pangram-api-audit-v1",
  "audit_id":"romance-detector-repair-20260820",
  "section_id":"part2",
  "model":"pangram-4",
  "expected_version":"4.0",
  "max_new_paid_posts":6,
  "known_prior_new_paid_posts_in_this_audit_section":1,
  "prior_measurement":{
    "text_sha256":"30f61fb0c490ec1275f3c39c834a38a956041865b63e5592c270d51cc22d5498",
    "fraction_human":0.9137498736,
    "transport":"local_playwright",
    "evidence_branch":"evidence/romance-pass1-retest-20260820"
  },
  "next_measurement":{
    "measurement_key":"romance-detector-repair-20260820.part2.pass2",
    "text_sha256":sha,
    "status":"authorized_pending",
    "authorized_new_paid_post_number":2
  },
  "part1":"no_new_call_exact_registered_hash_restored"
}
path.write_text(json.dumps(value,indent=2)+"\n",encoding="utf-8")
PY

git add -- "$LEDGER"
if ! git diff --cached --quiet -- "$LEDGER"; then
  git commit -m "Reserve Romance pass-2 API audit identity" >/dev/null \
    || fail "could not commit API audit ledger"
fi
git push origin "HEAD:refs/heads/$EVIDENCE_BRANCH" >/dev/null \
  || fail "could not push API audit preflight"

python3 -m venv .venv || fail "could not create virtual environment"
source .venv/bin/activate
python -m pip install -q -e . || fail "could not install Pangram lab"

P2_INPUT="$PASS2_DIR/candidate-part-2.txt"

echo
echo "=================================================="
echo "PANGRAM API — PART 2 ONLY — ONE AUTHORIZED POST"
echo "=================================================="
echo "SHA: $P2_SHA"
echo "Measurement key: $MEASUREMENT_KEY"
if [ -n "${PANGRAM_BASE_URL:-}" ]; then
  echo "API route: PANGRAM_BASE_URL from your environment"
else
  echo "API route: standard Pangram async endpoint"
fi

set +e
pangram-lab detect-file "$P2_INPUT" \
  --expect-sha "$P2_SHA" \
  --measurement-key "$MEASUREMENT_KEY" \
  --allow-public-cache
RC=$?
set -e

if [ "$RC" -ne 0 ]; then
  echo
  echo "API measurement did not complete cleanly."
  echo "No automatic second POST will be attempted."
  echo "Any cache/checkpoint/ambiguity state produced by the client was Git-synced."
  echo "Evidence branch: $EVIDENCE_BRANCH"
  echo "Tell ChatGPT: done, API failed"
  exit 0
fi

CACHE="cache/pangram-4/4.0/$P2_SHA/$MEASUREMENT_KEY.json"
[ -f "$CACHE" ] || fail "API command reported success but cache record is missing"

python3 - "$LEDGER" "$CACHE" <<'PY'
import json, pathlib, sys
ledger_path=pathlib.Path(sys.argv[1])
cache_path=pathlib.Path(sys.argv[2])
ledger=json.loads(ledger_path.read_text(encoding="utf-8"))
cache=json.loads(cache_path.read_text(encoding="utf-8"))
result=cache.get("result") or {}
ledger["next_measurement"].update({
  "status":"success",
  "cache_path":cache_path.as_posix(),
  "task_id":cache.get("task_id",""),
  "submitted_model":cache.get("submitted_model",""),
  "detector_stage":result.get("stage"),
  "detector_version":result.get("version"),
  "fraction_human":result.get("fraction_human"),
  "fraction_ai":result.get("fraction_ai"),
  "fraction_ai_assisted":result.get("fraction_ai_assisted")
})
ledger["observed_new_paid_posts_in_this_audit_section"]=2
ledger_path.write_text(json.dumps(ledger,indent=2)+"\n",encoding="utf-8")
PY

git add -- "$LEDGER"
if ! git diff --cached --quiet -- "$LEDGER"; then
  git commit -m "Record Romance pass-2 API result" >/dev/null \
    || fail "could not commit API result ledger"
fi
git push origin "HEAD:refs/heads/$EVIDENCE_BRANCH" >/dev/null \
  || fail "could not push API result ledger"

echo
echo "================ COMPLETE ================"
echo "Part 1: reused registered exact result; no call"
echo "Part 2 SHA: $P2_SHA"
echo "Evidence branch: $EVIDENCE_BRANCH"
echo "Cache: $CACHE"
echo "No automatic retries were performed."
echo "Tell ChatGPT: done"
