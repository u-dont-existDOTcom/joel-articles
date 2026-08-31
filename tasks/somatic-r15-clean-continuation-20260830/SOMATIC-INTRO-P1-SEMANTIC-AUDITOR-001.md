# SOMATIC INTRODUCTION P1 — SEMANTIC AUDITOR 001

Task: `somatic-r15-clean-continuation-20260830`

Strategy: `SOMATIC-DSMR-005`

Role: **fresh diagnostic reasoning context; semantic/provenance certification only**

Do not rewrite, improve, or suggest prose.

You will receive, in this order:

1. the exact authoritative source paragraph;
2. the exact frozen `SOMATIC-INTRO-P1-PRESERVATION-ESCROW-001.md`;
3. one candidate paragraph.

Audit the literal candidate against the frozen preservation units and whitelist. Keyword overlap is not enough. Treat any changed claim, scope/certainty, example function, general-to-autobiographical shift, invented mechanism/fact, or lost local definition as substantive.

Return exactly:

`PRESERVATION: PASS | FAIL`

`FORWARD_TRACEABILITY: PASS | FAIL`

`REVERSE_TRACEABILITY: PASS | FAIL`

`UNEXPLAINED_SUBSTANTIVE_DELTAS: <integer>`

`FAILED_UNITS: <comma-separated IDs or NONE>`

`GENERAL_TO_AUTOBIOGRAPHY: PASS | FAIL`

`ALL_SIX_REACTION_EXAMPLES: PASS | FAIL`

`CORRECTIVE_SLOT_ELIGIBLE: YES | NO`

`EXACT_SINGLE_CORRECTION: <one concise semantic requirement or NONE>`

`STRONGEST_DEFECT: <one concise description or NONE>`

Rules for `CORRECTIVE_SLOT_ELIGIBLE`:

- `YES` only when the entire failure can be reduced to exactly one isolated preservation unit or one exact scope/attribution defect and all other units pass.
- `NO` for two or more failed units, distributed drift, invented material that affects multiple functions, unclear equivalence, or any situation requiring a checklist or prose advice.

`EXACT_SINGLE_CORRECTION` must state only the missing/changed semantic requirement. It must not provide replacement wording.
