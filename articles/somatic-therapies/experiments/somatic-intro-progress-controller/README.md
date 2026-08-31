# Somatic Introduction progress controller

Status: article-scoped mechanical pilot; no prose or article authority.

This controller separates disposable generation, external comparative adjudication, and monotonic promotion. It stores semantic judgments supplied by the reasoning Chat and a verifier; it does not make those judgments itself.

The registered `articles/somatic-therapies/master.html` is outside this controller and is never modified by it. Pangram is also outside this workflow.

## Durable objects

- `frontier.json` — the authoritative promoted frontier, cleared dimensions, unresolved defect vector, and one bounded next search target.
- `samples/<sample-id>/candidate.txt` — exact immutable quarantined sample bytes.
- `samples/<sample-id>/record.json` — sample identity, SHA-256, writer/context marker, authority identities, and creation time.
- `samples/<sample-id>/status.json` — current quarantine/adjudication/promotion status and verifier-receipt binding.
- `adjudications/<receipt-id>.json` — canonical immutable comparative verifier receipt.
- `promotions/<promotion-id>.json` — immutable from-state/to-state transition receipt.
- `decisions/<decision-id>.json` — explicit reasoning-Chat search-state decision that cannot replace the promoted candidate.
- `history/*.jsonl` — append-only identity/event indexes.

Raw samples are disposable evidence. Reading a sample file does not make it owner-facing. The only controller operation that emits owner-facing prose is `emit-owner-facing-candidate`, and it fails unless the exact sample is the verified promoted frontier.

## Command surface

Run from the repository root:

```bash
python scripts/somatic_intro_progress_controller.py init
python scripts/somatic_intro_progress_controller.py show

python scripts/somatic_intro_progress_controller.py register-sample \
  --sample-id <sample-id> \
  --candidate <local-utf8-file> \
  --created-at <rfc3339-time> \
  --writer-identity <writer-id> \
  --writer-context <writer-context-id>

python scripts/somatic_intro_progress_controller.py emit-verifier-packet \
  --sample-id <sample-id> \
  --output <packet.json>

python scripts/somatic_intro_progress_controller.py record-verifier-receipt \
  --receipt <completed-receipt.json>

python scripts/somatic_intro_progress_controller.py attempt-promotion \
  --receipt-id <receipt-id>

python scripts/somatic_intro_progress_controller.py emit-writer-packet \
  --output <packet.json>

python scripts/somatic_intro_progress_controller.py emit-owner-facing-candidate \
  --output <candidate.md>
```

The checked-in frontier begins at `CONTROLLER_REVIEW`. `emit-writer-packet` deliberately fails until the reasoning Chat reviews this implementation and applies an explicit `GENERATION` target with `apply-search-decision`.

## Comparative verifier receipt

`emit-verifier-packet` returns the exact candidate, exact current promoted candidate when one exists, semantic task, active lesson contract, all identities/hashes, and a machine-readable receipt template. A completed receipt must contain:

```json
{
  "schema_version": 1,
  "receipt_id": "unique-receipt-id",
  "candidate": {"sample_id": "sample-id", "sha256": "<64 lowercase hex>"},
  "current_frontier": {"sample_id": null, "sha256": null},
  "semantic_task": {"path": "<repo path>", "sha256": "<64 lowercase hex>"},
  "active_lesson_contract": {"path": "<repo path>", "sha256": "<64 lowercase hex>"},
  "hard_constraints": "PASS",
  "regressions": [],
  "improvements": [
    {"dimension_id": "dimension-id", "description": "Comparative semantic judgment."}
  ],
  "cleared_dimensions_after": ["dimension-id"],
  "unresolved_defects": [
    {"rank": 1, "dimension_id": "remaining-id", "description": "Ranked remaining defect."}
  ],
  "strongest_blocking_defect": "Explicit diagnosis, or an explicit statement that none remains.",
  "strongest_known_generative_failure_pattern_after": "Externally supplied failure pattern.",
  "frontier_comparison": "DOMINATES",
  "next_search_target": {
    "id": "next-target-id",
    "kind": "GENERATION",
    "description": "One bounded changed search operation."
  },
  "promotion": "ALLOW",
  "verifier": {"identity": "verifier-id", "context_id": "verifier-context-id"}
}
```

The controller validates and stores this judgment. It does not populate any semantic field.

## Promotion interlock

An owner-facing frontier replacement occurs only when:

- the candidate bytes match the quarantined sample SHA-256;
- the receipt matches the sample and exact current promoted frontier;
- the receipt's semantic-task and active-lesson hashes match current repository bytes;
- hard constraints pass and the external verifier explicitly allows promotion;
- an existing frontier is replaced only by `DOMINATES`;
- no already-cleared dimension regresses or disappears from `cleared_dimensions_after`;
- all required receipt fields and writer/verifier separation markers validate.

`REGRESSES`, `INCOMPARABLE`, and `NONDOMINATED` cannot replace an existing owner-facing frontier. A failed promotion does not rewrite `frontier.json`. Recency, timestamps, detector results, filenames, branch order, and model confidence are never promotion inputs.

Promotion writes an immutable transition receipt and then atomically replaces `frontier.json`. Replaying the exact registration, receipt, or completed promotion is idempotent; reusing an identity with different bytes fails closed.

## Search-state decision after review or rejection

The reasoning Chat can change unresolved-defect/search state without changing the promoted candidate by supplying a decision to:

```bash
python scripts/somatic_intro_progress_controller.py apply-search-decision \
  --decision <decision.json>
```

Required decision shape:

```json
{
  "schema_version": 1,
  "decision_id": "unique-decision-id",
  "current_frontier": {"sample_id": null, "sha256": null},
  "semantic_task": {"path": "<repo path>", "sha256": "<64 lowercase hex>"},
  "active_lesson_contract": {"path": "<repo path>", "sha256": "<64 lowercase hex>"},
  "cleared_dimensions": [],
  "unresolved_defects": [
    {"rank": 1, "dimension_id": "defect-id", "description": "Externally judged defect."}
  ],
  "strongest_known_generative_failure_pattern": "Externally judged pattern.",
  "next_search_target": {
    "id": "bounded-target-id",
    "kind": "GENERATION",
    "description": "One bounded changed generation/search operation."
  },
  "decision_maker": {"identity": "reasoning-chat-id", "context_id": "context-id"},
  "source_verifier_receipt": null
}
```

When the decision follows a verifier receipt, `source_verifier_receipt` must contain that receipt's exact `receipt_id` and SHA-256. The decision may not remove a cleared dimension or replace the current candidate. It gives the next writer only the promoted frontier identity/hash, cleared constraints, unresolved defects, one search target, semantic authority, and source-integrity prohibitions. No rejected sample or verifier rationale enters the writer packet.

## Required first handoff

Before registering any real Somatic candidate, the reasoning Chat reviews this controller and either accepts its mechanics or identifies a mechanical defect. If accepted, it supplies the first hash-bound search decision. Only then can the controller emit a writer packet.
