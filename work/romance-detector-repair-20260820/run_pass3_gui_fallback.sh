#!/usr/bin/env bash
set -u -o pipefail

JOEL_REPO="u-dont-existDOTcom/joel-articles"
PANGRAM_REPO="u-dont-existDOTcom/pangram-humanization-lab"
JOEL_BRANCH="task/romance-detector-repair-20260820"
EVIDENCE_BRANCH="evidence/romance-pass3-gui-20260820"
P2_SHA="c6ef42419a3db2e82b1ff4f9370fc85bca4fa8c061c61dd6a1b5d28171d9908c"
AUDIT_LEDGER="state/api-audits/romance-detector-repair-20260820-part2-pass3-gui.json"

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

ROOT="$(mktemp -d /tmp/romance-pass3-gui.XXXXXX)"
JOEL="$ROOT/joel-articles"
PANGRAM="$ROOT/pangram-humanization-lab"

echo "=== Recover exact Git-durable pass-3 candidate ==="
gh repo clone "$JOEL_REPO" "$JOEL" -- --quiet || fail "could not clone joel-articles"
cd "$JOEL" || fail "could not enter joel-articles"
git fetch origin "$JOEL_BRANCH" --quiet || fail "could not fetch Romance task branch"
git switch -C "$JOEL_BRANCH" "origin/$JOEL_BRANCH" >/dev/null || fail "could not switch to Romance task branch"

P2="$JOEL/work/romance-detector-repair-20260820/materialized-pass3/candidate-part-2.txt"
[ -f "$P2" ] || fail "Git-durable pass-3 Part 2 is missing"
printf '%s  %s\n' "$P2_SHA" "$P2" | sha256sum --check --strict \
  || fail "pass-3 Part-2 hash does not match authorized boundary"

echo "Part 2 SHA verified: $P2_SHA"
echo "Part 1 detector call: NONE"

echo
echo "=== Recover GUI evidence branch ==="
gh repo clone "$PANGRAM_REPO" "$PANGRAM" -- --quiet || fail "could not clone Pangram lab"
cd "$PANGRAM" || fail "could not enter Pangram lab"
git fetch origin "$EVIDENCE_BRANCH" --quiet || fail "could not fetch pre-reserved GUI evidence branch"
git switch -C "$EVIDENCE_BRANCH" "origin/$EVIDENCE_BRANCH" >/dev/null \
  || fail "could not switch to GUI evidence branch"

[ -f "$AUDIT_LEDGER" ] || fail "pre-reserved cross-transport audit ledger is missing"

python3 -m venv .venv || fail "could not create virtual environment"
source .venv/bin/activate
python -m pip install -q -e '.[browser]' || fail "could not install Pangram GUI dependencies"

echo
echo "=== Read-only Pangram GUI authentication check ==="
pangram-local verify || fail "Pangram GUI authentication is not ready; no detector submission was made"

echo
echo "=================================================="
echo "PANGRAM GUI FALLBACK — PART 2 ONLY"
echo "Paid measurement #3 if a new click is required"
echo "=================================================="
echo "SHA: $P2_SHA"

set +e
pangram-local run \
  --input "$P2" \
  --expect-sha "candidate-part-2.txt=$P2_SHA"
RC=$?
set -e

if [ "$RC" -ne 0 ]; then
  echo
  echo "GUI measurement did not complete cleanly."
  echo "No automatic repeat will be attempted."
  echo "Reservation/failure evidence, if created, is Git-durable on: $EVIDENCE_BRANCH"
  echo "Tell ChatGPT: done, GUI failed"
  exit 0
fi

RESULT="state/gui-runs/pangram-4/$P2_SHA/result.json"
[ -f "$RESULT" ] || fail "GUI runner returned success but result.json is missing"

python3 - "$AUDIT_LEDGER" "$RESULT" <<'PY'
import json, pathlib, sys
ledger_path=pathlib.Path(sys.argv[1])
result_path=pathlib.Path(sys.argv[2])
ledger=json.loads(ledger_path.read_text(encoding="utf-8"))
receipt=json.loads(result_path.read_text(encoding="utf-8"))
parsed=receipt.get("parsed") or {}
summary=parsed.get("summary") or {}
next_measurement=ledger.setdefault("next_measurement", {})
next_measurement.update({
    "status": "success",
    "result_path": result_path.as_posix(),
    "detector_stage": parsed.get("detector_stage"),
    "detector_version": parsed.get("detector_version"),
    "fraction_human": summary.get("fraction_human"),
    "fraction_ai": summary.get("fraction_ai"),
    "fraction_ai_assisted": summary.get("fraction_ai_assisted"),
    "transport": receipt.get("transport"),
    "exact_text_match": (receipt.get("history_api_exact_identity") or {}).get("transport_match_mode"),
})
ledger["observed_new_paid_measurements_in_this_audit_section"] = 3
ledger_path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
PY

git add -- "$AUDIT_LEDGER"
if ! git diff --cached --quiet -- "$AUDIT_LEDGER"; then
  git commit -m "Record Romance pass-3 GUI fallback result" >/dev/null \
    || fail "could not commit GUI audit result"
fi
git push origin "HEAD:refs/heads/$EVIDENCE_BRANCH" >/dev/null \
  || fail "could not push GUI audit result"

echo
echo "================ COMPLETE ================"
echo "Part 1: no call; registered exact result reused"
echo "Part 2 SHA: $P2_SHA"
echo "Evidence branch: $EVIDENCE_BRANCH"
echo "Result path: $RESULT"
echo "No automatic retries were performed."
echo "Tell ChatGPT: done"
