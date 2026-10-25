# Owner-facing humanization delivery gate

**Status: executable local gate.** This binds the existing `SKILL.md` owner-delivery requirement, the numbered tell inventory, and issue #245. It adds no phrase blacklist.

## When to use

Before exposing **model-written Joel-byline prose** as a ready candidate, export it with `tools/humanization/owner_delivery_gate.py deliver`. This is separate from experimental Pangram screening, direct owner writing and exact source quotations. Never use the gate to imply Pangram has certified a text.

It writes the exact model candidate to the owner-facing destination **only after** checking the unmodified source, natural context, current tell catalog, mechanical linter, full T/C ledger, and independent review artifact files.

It cannot intercept arbitrary text an assistant directly types into chat. The operating rule is therefore **do not paste model-drafted article prose into chat unless its exact saved bytes have passed the delivery command**. CI protects the exported-file path, not the ChatGPT renderer.

## Workflow

Save the original source, model candidate and natural reading context in distinct files. The context must include the literal candidate exactly once.

```bash
python3 tools/humanization/owner_delivery_gate.py init \
  --draft work/candidate.txt --context work/section.txt \
  --source work/source.txt --manifest work/admission.json
```

`init` always writes `status: PENDING`, even if mechanical lint is FAIL (for failure evidence). To submit a candidate, record the actual writer and context ID, set `status: READY_FOR_CHECK` after review, fill one exact-evidence `ABSENT` or `PRESENT` judgment for **each** current `Txx`/`Cxx` inventory row, and resolve every finding:

- `UNCERTAIN` is always blocking.
- `PRESENT` can be `JUSTIFIED_KEEP` only when an independent reviewer explicitly confirms the source-grounded rationale; a legitimate em dash or meaningful contrast is not blanket-banned.
- An actual mechanical `FAIL` can **never** be waived for model prose.
- A mechanical `REVIEW` needs a specific `JUSTIFIED_KEEP` rationale for each exact lint finding. Each separately saved reviewer report must list every accepted exact lint label in `resolved_lint_labels`.
- Three separately saved source-bound reports are required: `preservation`, `cold_read_1`, `cold_read_2`. Paths in `review_files` are relative to the manifest.

Review artifacts have the following shape (replace every placeholder with actual evidence):

```json
{
  "schema": "JOEL_COLD_REVIEW_V1",
  "role": "cold_read_1",
  "candidate_sha256": "<SHA-256 from init>",
  "context_sha256": "<SHA-256 from init>",
  "source_sha256": "<SHA-256 from init>",
  "verdict": "PASS",
  "unresolved": [],
  "reviewer": {
    "name": "Actual independent reviewer/model",
    "context_id": "unique actual reviewer context",
    "origin": "run provenance / external evidence source"
  },
  "evidence": "Specific critical evaluation of the literal source, context and candidate.",
  "resolved_tell_ids": [],
  "resolved_lint_labels": []
}
```

Do not invent reviewer identities. A claim of fresh context or a separate file does not *create* independence. The program checks unique reviewer context IDs and identical source/draft/context bytes; **it cannot cryptographically prove reviewer provenance or competency**.

```bash
python3 tools/humanization/owner_delivery_gate.py check \
  --draft work/candidate.txt --context work/section.txt \
  --source work/source.txt --manifest work/admission.json

python3 tools/humanization/owner_delivery_gate.py deliver \
  --draft work/candidate.txt --context work/section.txt \
  --source work/source.txt --manifest work/admission.json \
  --out work/for-joel.txt --proof work/for-joel.proof.json
```

On a block the program exits **2** and produces **no owner-facing file**. It refuses to overwrite nonidentical existing files. A PASS proof records candidate/context/source/inventory identities, current linter result and report digests. Changed bytes or stale checks cannot be reused; generate fresh evidence instead.

## Validation and scope

```bash
python3 -m unittest discover -s tests -p test_owner_delivery_gate.py -v
```

- The exact user-rejected mettā sentence must be refused with the existing **E41** coach-density FAIL, **E186** “X can ... without Y” and **O25** “even” findings, even if other reports claim PASS.
- Legitimate source-relevant contrast and an ordinary em dash must remain admissible when the source and cold reads justify them.
- Missing/duplicated tell IDs, `UNCERTAIN` statuses, stale candidate/review hashes, missing reviewers, identical writer/reviewer contexts and attempted file overwrites must fail.

This guards **model-generated owner-facing artifacts**. It does not override Joel's final editorial authority, article master registration, independent critical judgment, Pangram credit/History gates, or the source-preservation requirements.
