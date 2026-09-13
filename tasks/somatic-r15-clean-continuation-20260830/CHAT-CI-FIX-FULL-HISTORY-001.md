# CHAT-CI-FIX-FULL-HISTORY-001 — restore historical blob availability in hosted content-integrity CI

Task: `somatic-r15-clean-continuation-20260830`

Status: **FROZEN CHAT-AUTHORED MECHANICAL INFRASTRUCTURE PATCH / CODEX EXECUTION ONLY**

## Decision basis

PR #73's hosted content-integrity job uses the default depth-1 `actions/checkout` behavior. The Somatic direct-owner audit intentionally verifies six historical Git blob identities with `git cat-file -e`. Those blobs exist and the complete local clone passes all 117 tests, but a depth-1 hosted checkout does not contain them and reports six false `OWNER_SOURCE_BLOB_MISSING` failures.

This is not article evidence and not a reason to weaken provenance validation. The bounded repair is to give the hosted job complete Git history.

## Worker role

Mechanical executor only. Apply exactly the patch below. Do not change checker semantics, owner-source blob IDs, article prose, candidates, registered authority, or detector state.

## Exact source identities

Repository: `u-dont-existDOTcom/joel-articles`

Branch: `task/somatic-r15-clean-continuation-20260830`

Workflow:
`.github/workflows/content-integrity.yml`

Expected pre-patch workflow Git blob:
`fc698613e20978e380b75a2b1b9ac180b49fc5fe`

Direct-owner checker:
`scripts/check_somatic_r15_direct_owner.py`

Expected checker Git blob:
`15c891dda348d9ef933f6bb2f90fce7b6e20bb1e`

The checker must remain byte-identical.

## Exact workflow patch

Replace exactly this block:

```yaml
      - name: Check out repository
        uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
```

with exactly:

```yaml
      - name: Check out repository
        uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
        with:
          fetch-depth: 0
```

The old block must occur exactly once. Fail closed otherwise.

## Exact regression test

Create this new file exactly:

`tests/test_content_integrity_full_history.py`

```python
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/content-integrity.yml"


class ContentIntegrityFullHistoryTests(unittest.TestCase):
    def test_checkout_fetches_history_needed_for_blob_provenance(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        pattern = re.compile(
            r"- name: Check out repository\n"
            r"\s+uses: actions/checkout@[^\n]+\n"
            r"\s+with:\n"
            r"\s+fetch-depth:\s*0(?:\n|$)"
        )
        self.assertRegex(text, pattern)


if __name__ == "__main__":
    unittest.main()
```

## Mechanical assertions

- workflow source blob verified before edit;
- exact old block count = 1;
- exact new block count = 1 after edit;
- `fetch-depth: 0` occurs exactly once in `content-integrity.yml`;
- checker Git blob and SHA remain unchanged;
- all six `OWNER_SOURCE_BLOBS` IDs remain unchanged;
- no article or candidate file changes;
- registered `master.html` unchanged;
- no Pangram action or reservation.

## Validation

Run:

```text
python -m unittest tests.test_content_integrity_full_history
python -m unittest discover -s tests
python scripts/check_somatic_r15_direct_owner.py --candidate articles/somatic-therapies/experiments/R15-EFT-REPAIR-CANDIDATE-20260831.md --json
python scripts/validate_content_repository.py --root .
python scripts/audit_codex_github.py --root . --fail-on error
git diff --check
```

The direct-owner audit must PASS in the complete local clone. Push the workflow/test patch, then inspect the new PR #73 content-integrity run. If the run fails for another reason, report the exact job/step/log evidence; do not modify checker semantics.

## Stop boundary

After the exact patch, local validation, push, and hosted-run readback:

- stop the infrastructure subtask;
- do not alter prose;
- do not alter the detector experiment;
- do not weaken provenance checks;
- return exact before/after blobs, test outputs, workflow run/job result, and confirmation of zero article/master/detector mutations.
