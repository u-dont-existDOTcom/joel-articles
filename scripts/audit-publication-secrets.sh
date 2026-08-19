#!/usr/bin/env bash
set -euo pipefail
EXPECTED_REPOSITORY="u-dont-existDOTcom/joel-articles"
GITLEAKS_VERSION="8.29.1"
GITLEAKS_SHA256="e4eb209d04e20339d77122a3bdf9cd41351255cfb27ebcb75e85325e04f88924"
GITLEAKS_URL="https://github.com/gitleaks/gitleaks/releases/download/v${GITLEAKS_VERSION}/gitleaks_${GITLEAKS_VERSION}_linux_x64.tar.gz"
repository="${GITHUB_REPOSITORY:-$EXPECTED_REPOSITORY}"
[[ "$repository" == "$EXPECTED_REPOSITORY" ]] || { echo 'publication-audit: unexpected repository' >&2; exit 2; }
umask 077
work="$(mktemp -d /tmp/joel-articles-publication-audit.XXXXXX)"
trap 'rm -rf -- "$work"' EXIT
mkdir -p "$work/hosted/actions" "$work/hosted/reviews"
# Keep audit-only PR heads separate from actions/checkout's pull/<n>/merge namespace.
git fetch --force --no-tags origin '+refs/heads/*:refs/remotes/origin/*' '+refs/tags/*:refs/tags/*' '+refs/pull/*/head:refs/remotes/pull-heads/*'
git for-each-ref --format='%(refname)' > "$work/hosted/ref-names.txt"
git log --all --format='%H%n%B%n---END-COMMIT---' > "$work/hosted/commit-messages.txt"
archive="$work/gitleaks.tar.gz"
curl --fail --location --silent --show-error "$GITLEAKS_URL" --output "$archive"
printf '%s  %s\n' "$GITLEAKS_SHA256" "$archive" | sha256sum --check --status || exit 2
tar -xzf "$archive" -C "$work" --no-same-owner --no-same-permissions gitleaks
chmod 700 "$work/gitleaks"
[[ -n "${GH_TOKEN:-}" ]] || { echo 'publication-audit: GH_TOKEN required' >&2; exit 2; }
gh issue list --repo "$repository" --state all --limit 1000 --json number,title,body > "$work/hosted/issues.json"
gh pr list --repo "$repository" --state all --limit 1000 --json number,title,body > "$work/hosted/pulls.json"
gh api --method GET --paginate "repos/$repository/issues/comments?per_page=100" > "$work/hosted/issue-comments.json"
gh api --method GET --paginate "repos/$repository/pulls/comments?per_page=100" > "$work/hosted/review-comments.json"
gh api --method GET --paginate "repos/$repository/releases?per_page=100" > "$work/hosted/releases.json"
mapfile -t pr_numbers < <(gh pr list --repo "$repository" --state all --limit 1000 --json number --jq '.[].number')
for number in "${pr_numbers[@]}"; do gh api --method GET --paginate "repos/$repository/pulls/$number/reviews?per_page=100" > "$work/hosted/reviews/pr-$number.json"; done
mapfile -t run_ids < <(gh run list --repo "$repository" --limit 1000 --json databaseId --jq '.[].databaseId')
fetched_logs=0; unavailable_logs=0
current_run_id="${GITHUB_RUN_ID:-}"
for run_id in "${run_ids[@]}"; do
  if [[ -n "$current_run_id" && "$run_id" == "$current_run_id" ]]; then
    continue
  fi
  if gh run view "$run_id" --repo "$repository" --log > "$work/hosted/actions/run-$run_id.log" 2>/dev/null; then fetched_logs=$((fetched_logs+1)); else rm -f "$work/hosted/actions/run-$run_id.log"; unavailable_logs=$((unavailable_logs+1)); fi
done
set +e
"$work/gitleaks" git --no-banner --no-color --redact=100 --report-format=json --report-path="$work/git.json" --log-opts='--all' "$PWD" >"$work/git.log" 2>&1; gs=$?
"$work/gitleaks" dir --no-banner --no-color --redact=100 --report-format=json --report-path="$work/hosted.json" "$work/hosted" >"$work/hosted.log" 2>&1; hs=$?
set -e
python3 - "$work/git.json" "$gs" "$work/hosted.json" "$hs" "$fetched_logs" "$unavailable_logs" <<'PY'
import json,sys
from pathlib import Path
def check(p,s,label):
 d=json.loads(Path(p).read_text()); s=int(s)
 if not isinstance(d,list) or s not in (0,1) or (s==0)!=(len(d)==0): raise SystemExit(f'publication-audit: invalid {label} result')
 return len(d)
g=check(sys.argv[1],sys.argv[2],'git'); h=check(sys.argv[3],sys.argv[4],'hosted')
print(json.dumps({'status':'pass' if not(g or h) else 'blocked','git_secret_findings':g,'hosted_secret_findings':h,'actions_logs_scanned':int(sys.argv[5]),'actions_logs_unavailable_or_expired':int(sys.argv[6])},sort_keys=True))
raise SystemExit(1 if g or h else 0)
PY
