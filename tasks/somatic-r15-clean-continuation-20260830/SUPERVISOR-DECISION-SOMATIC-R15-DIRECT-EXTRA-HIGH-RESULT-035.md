# SUPERVISOR_DECISION SOMATIC-R15-DIRECT-EXTRA-HIGH-RESULT-035

Task: `somatic-r15-clean-continuation-20260830`

Status: **EXTRA-HIGH RAW RESPONSE REJECTED BEFORE DETECTOR / FAILED DIRECT-PARAPHRASE DESCENDANT / PRESERVED STRATEGY EVIDENCE ONLY / SEMANTIC-PACKET RECONSTRUCTION REQUIRED**

## Decision

The fresh Extra High response at:

`tasks/somatic-r15-clean-continuation-20260830/fresh-extra-high-whole-article-001/RAW-RESPONSE-1.md`

Git blob `8ccad949a5420d759ab847a0e5570e6e06f91b25`, SHA-256 `77836dfff748fe0dc132d17a49be21343270eb1c4320547cb23910c71cd46e6d`, is **not a usable whole-article candidate and is not Pangram-eligible**.

It is preserved as `STRATEGY_EVIDENCE_ONLY`.

This does not invalidate the thin-automation topology. Codex acted only as transport/capture, and the fresh Extra High writer was the reasoning/writing surface. The failure is the generation method: the writer still received the original model-shaped realization as its primary writing input and reproduced a descendant of the prohibited direct-paraphrase/conversationalization family.

## Fail-closed gate adjudication

The controlling task-local files are:

- `HUMANIZATION-FAIL-CLOSED-CONTROL-20260831.md`;
- `HUMANIZATION-CONTROL-STATE-20260831.json`.

They landed while the writer was running and explicitly may not be silently grandfathered around.

### Provenance gate: FAIL / NOT ESTABLISHED BEFORE GENERATION

No exact `OWNER_LOCK` / `AI_TARGET` / `UNKNOWN_FROZEN` map existed for the generation boundary before the response was written. The current control states that the only presently established repair boundary is the first four Introduction paragraphs and that later material is frozen unless separately provenanced.

The direct-owner source recovery matrix independently shows that the Introduction is `OWNER_SUPPLIED_AI_SHAPED_BASELINE` for meaning/function, with no newly recovered natural-owner realization. Several later sections also remain mixed, unknown, historical-only, or without natural owner source. A whole-document rewrite cannot be accepted by assuming every source paragraph was editable.

### Semantic-packet gate: FAIL

The writer received the literal original AI-target article prose as its primary generation input. The controlling gate requires a separate reasoning pass to convert `AI_TARGET` material into a semantic/function packet and then withhold the original AI-target realization from the writer.

The response therefore cannot satisfy the semantic-packet gate retroactively even if its meaning were otherwise preserved.

### Failed-strategy lineage gate: FAIL_FAILED_STRATEGY_DESCENDANT

The response changes more topology than the preceding Pro artifact, but its dominant mechanism remains the prohibited family:

- same heading order and same source conceptual cards/order;
- most source paragraphs are still realized in the same functional sequence;
- many paragraphs remain paragraph-by-paragraph paraphrases;
- contractions, conversational substitutions, first-person skin and local cadence variation are prominent mechanisms;
- repeated significance/qualification/aftercare structures remain substantially inherited.

Examples include the four Introduction conceptual cards being rewritten in the same four-card order, the Physical State sequence remaining the same four functional paragraphs, and the major modality sections following the same paragraph-job progression.

This is enough to classify the response as a failed-strategy descendant before detector work.

### Attribution/preservation gate: FAIL_SEMANTIC_PRESERVATION

At least one concrete meaning change is present in the Shaking Qigong mechanism paragraph.

Source:

`Those are different explanations. I don't need to force one of them to prove the others.`

Extra High response:

`Those are different explanations, and I do not need to make one explanation disprove all the others.`

`prove` became `disprove`, reversing the relationship among the competing explanations. That is a substantive evidence-plane change, not a harmless surface realization.

A single unexplained substantive change is sufficient to block candidate eligibility under the preservation gate.

### Independent diagnostic validation: NOT RUN / BLOCKED UPSTREAM

A separate fresh diagnostic validator cannot rescue a candidate that already fails provenance, semantic-packet, structural-lineage, and preservation gates. Do not spend another reasoning/browser cycle validating this response as a candidate.

## Candidate classification

```text
CANDIDATE_STATUS = REJECTED_BEFORE_DETECTOR
FAILED_STRATEGY_DESCENDANT = true
PROVENANCE_GATE = FAIL
SEMANTIC_PACKET_GATE = FAIL
ATTRIBUTION_PRESERVATION_GATE = FAIL_SEMANTIC_PRESERVATION
INDEPENDENT_VALIDATION_GATE = NOT_RUN_BLOCKED_UPSTREAM
PANGRAM_SUBMISSION_ALLOWED = false
PAID_DETECTOR_CALL_ALLOWED = false
CANDIDATE_PROMOTION_ALLOWED = false
ARTIFACT_DISPOSITION = STRATEGY_EVIDENCE_ONLY
```

The raw response does **not** count as a gate-compliant Candidate 1. It does count as binding negative evidence that direct whole-article rewriting from the original AI-shaped realization—even in a fresh Extra High chat—can regenerate the failed strategy family. Do not repeat that method.

## Replacement strategy

New strategy ID:

`somatic-r15-extra-high-semantic-packet-reconstruction-v1`

The next permitted cycle follows the fail-closed control exactly and begins only with the current Introduction repair boundary:

1. A fresh Extra High **packet-builder** receives the exact first four Introduction source paragraphs plus current task-local provenance/source authorities and the fail-closed controls.
2. It produces an exact provenance map classifying every natural source span exactly once as `OWNER_LOCK`, `AI_TARGET`, or `UNKNOWN_FROZEN`.
3. For every `AI_TARGET`, it produces a semantic/function packet containing propositions, certainty, attribution, chronology/causality, examples, links/objects, rhetorical function, and only genuinely owner-authorized exact phrases.
4. It produces **no publication prose and no candidate wording**.
5. The current reasoning supervisor reviews/fixes/freezes that map and packet.
6. Only after that freeze does a different fresh Extra High writer receive the semantic packet + exact OWNER_LOCK continuity text + minimal context, with the original AI-target realization withheld.
7. A separate fresh Extra High diagnostic context then performs lineage/provenance/preservation/attribution validation without rewriting.
8. No Pangram action occurs at this Introduction cycle. Detector work remains whole-document-only under the owner correction and detector-last rule.

The Introduction is being used here as the currently authorized provenance/generation scope, **not** as a detector proxy. A passing Introduction generation method is only a method gate. It does not count as owner-outcome advancement. Before a whole article can be assembled, the same provenance classification must be established for every later span to be edited; all unclassified later material remains frozen.

## Root progress state

```text
worker_to_contract_alignment: GREEN
contract_to_owner_alignment: MATCH
outcome_advancement: REGRESSING
failed_fragment_strategy: EXHAUSTED
failed_direct_original_prose_extra_high_method: CLOSED_PRE_DETECTOR
active_strategy: somatic-r15-extra-high-semantic-packet-reconstruction-v1
completion_claim: NOT_COMPLETE
```

## Immediate action

Codex may only construct and transport the frozen Introduction provenance/semantic-packet-builder prompt to one genuinely fresh Extra High reasoning chat, capture the raw structured response and conversation URL, persist exact artifacts, and return for reasoning review.

Codex may not generate prose, open a detector family, run Pangram, create a detector reservation, modify an article candidate, modify `master.html`, or route this task to Pro.
