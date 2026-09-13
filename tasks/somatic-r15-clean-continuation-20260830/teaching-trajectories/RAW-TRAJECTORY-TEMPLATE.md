# Somatic owner-teaching trajectory — raw episode ledger

Status: `TEMPLATE_ONLY`
Authority: raw experiment evidence only; never article prose authority

## Episode metadata

- episode_id:
- status: `DISCOVERY_ACTIVE`
- date_started:
- date_frozen:
- model/configuration:
- target_article: `somatic-therapies`
- target_span/function:
- starting_writer_state_path: `articles/somatic-therapies/experiments/SOMATIC-MANUAL-HUMANIZATION-WRITER-STATE-20260831.md`
- starting_writer_state_blob_sha:
- starting_task_branch_commit:
- raw_capture_rule: preserve literal turns; no cleaned lesson summaries until freeze

## Initial ordinary task

### Joel — exact

<exact opening task>

### Assistant candidate 0 — exact

<exact candidate>

- candidate_sha256:

## Turn records

### Turn 1

#### Joel — exact

<exact correction / response>

#### Literal response classification

`QUESTION | PROBE | REQUEST_FOR_EXPLANATION | HESITATION | ACCEPTANCE | REJECTION | SUBSTANTIVE_CORRECTION | MIXED`

#### Descriptive raw features only

- positive_example: yes/no
- negative_example: yes/no
- analogy: yes/no
- semantic_correction: yes/no
- literal_ai_shape_rejection: yes/no
- process_correction: yes/no
- stopping_judgment: yes/no

Do not add causal interpretation here.

#### Assistant candidate 1 — exact

<exact next candidate>

- candidate_sha256:

---

Repeat turn records without rewriting earlier entries.

## Freeze record

- freeze_command_turn:
- frozen_status: `SUCCESS_CANDIDATE_DISCOVERY_EPISODE | FAILURE_CONTROL_EPISODE | OWNER_STOPPED_UNRESOLVED`
- Joel_exact_freeze_judgment:
- final_candidate_sha256:
- nearest_preceding_failed_candidate_sha256:
- raw_ledger_commit_at_freeze:

## Exact ordered transcript

At freeze, preserve the complete exact ordered episode transcript here or in a sibling frozen-transcript artifact referenced by exact path/SHA. Include ordinary questions/probes that did not trigger an incremental GitHub write so the frozen trajectory is complete.

## Post-freeze analysis — do not fill during live teaching

### Descriptive turn tags

<post-hoc only>

### Candidate lessons

For each proposed lesson:

- exact supporting Joel turn(s):
- underlying generative mistake — model diagnosis:
- future thought-movement change:
- validation: `OWNER_CONFIRMED | PROVISIONAL | REPLAY_SUPPORTED | REPLAY_FALSIFIED | SUPERSEDED`
- promoted_to_writer_state: yes/no

### Replay status

- fresh baseline:
- exact trajectory replay:
- increasing-prefix replay:
- compressed-summary control:
- order control:
- turn ablations:
- persistence/decay probes:
- held-out transfer:

### Causal conclusion

Do not fill until replay/control evidence exists. One discovery success is not causal proof.
