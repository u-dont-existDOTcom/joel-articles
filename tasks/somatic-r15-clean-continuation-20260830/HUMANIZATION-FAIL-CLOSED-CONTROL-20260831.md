# Somatic R15 — Fail-Closed Humanization Control

**Status:** CONTROLLING TASK-LOCAL CORRECTION / MECHANICALLY ENFORCED AT `prewrite_ready`
**Date:** 2026-08-31  
**Task:** `somatic-r15-clean-continuation-20260830`  
**Owner correction:** do not count owner-authored Human prose as model humanization; stop repeating previously falsified conversational/paraphrase strategies.

## 1. Failure being corrected

The failure is not primarily vocabulary. A reasoning writer repeatedly regenerated descendants of a rejected strategy even after the rejection was known:

- direct paraphrase of model-shaped prose;
- contractions / plainer wording / first-person conversationalization;
- local smoothing while preserving the source paragraph's conceptual grouping and rhythm;
- significance/preference staging rewritten rather than removed;
- tidy setup -> qualification -> conclusion architecture retained under new words;
- owner-authored Human text blended into the candidate and then implicitly counted as evidence that the rewrite became more Human.

A prior rejection or negative detector result is therefore **binding negative evidence**, not stylistic advice.

## 2. Immediate hard hold

Until all gates below pass:

```text
UNGATED_HUMANIZATION_ALLOWED = false
PANGRAM_SUBMISSION_ALLOWED = false
PAID_DETECTOR_CALL_ALLOWED = false
CANDIDATE_PROMOTION_ALLOWED = false
```

Any candidate produced by "make this more conversational", "rewrite in first person", "use contractions", "smooth this", "make it sound human", or equivalent direct-paraphrase instructions is presumptively a descendant of the failed family and must not advance.

## 3. Provenance gate

Before prose generation, every natural source span in the requested boundary must be classified exactly once as:

```text
OWNER_LOCK
AI_TARGET
UNKNOWN
```

Rules:

- `OWNER_LOCK`: owner-authored or explicitly owner-adopted language. Preserve byte-for-byte unless the owner explicitly authorizes editing it.
- `AI_TARGET`: provenance and task authority permit realization-only replacement.
- `UNKNOWN`: freeze it, withhold it from the writer, do not edit it, and do not count it as successful humanization.

No candidate may be evaluated as a humanization improvement by looking at the mixed section as a whole without separately accounting for the untouched `OWNER_LOCK` contribution.

For the current R15 Introduction test, the known AI-shape repair boundary is the first four Introduction paragraphs ending immediately before `## Your Physical State Can Change What Therapy Does`. Later material is frozen unless separately classified by provenance. The earlier chat-produced mixed rewrite is **not detector-eligible evidence**.

## 4. Semantic-packet gate

The writer does **not** receive the original AI-target prose as its primary generation input.

A reasoning pass first converts each `AI_TARGET` into a semantic/function packet containing only what must survive, including as applicable:

- propositions;
- certainty/modality;
- actor/source/epistemic attribution;
- chronology and causality;
- examples that must survive;
- required links/objects;
- rhetorical function in the surrounding article;
- owner-authorized exact phrases, if any.

The packet must not preserve the model paragraph's sentence skeleton, clause order, list completion, transition pattern, or summary architecture merely because those appeared in the source realization.

After the packet is frozen, the prose writer works from:

```text
semantic/function packet
+ exact OWNER_LOCK text needed for continuity
+ immediate article context needed for coherence
```

and not from rejected rewrite prose.

## 5. Rejected-strategy isolation

The **writer** is intentionally not primed with the full rejected-candidate corpus or a menu of detector-highlighted phrases. Those materials can anchor it back into the same solution family.

The **validator** receives:

- the new candidate;
- provenance map;
- semantic/function packet;
- original AI-target realization;
- rejected candidates and their rejection reasons;
- failed strategy-family ledger;
- applicable detector/outcome evidence.

This is asymmetric by design: the writer needs freedom from the failed realization; the validator needs the negative evidence required to detect recurrence.

## 6. Failed strategy family

Current failed family ID:

```text
SOMATIC-HUMANIZATION-DIRECT-PARAPHRASE-CONVERSATIONALIZATION
```

Fingerprint includes any candidate whose main mechanism remains substantially:

```text
same source conceptual cards/order
+ sentence-by-sentence or paragraph-by-paragraph paraphrase
+ conversational surface substitutions
+ contractions / first-person skin
+ local cadence variation
+ preserved explanatory aftercare / significance staging / balanced taxonomy
```

Changing adjectives, sentence length, punctuation, contractions, transitions, or first/third person does **not** establish a new strategy family.

## 7. Mandatory candidate justification

Every changed sentence or paragraph must name the specific model-shape defect it removes and the structural mechanism by which it is removed.

The following are invalid justifications and cause failure:

```text
sounds more human
more conversational
uses contractions
simpler wording
more personal
better flow
less formal
more varied sentence length
```

Those may occur incidentally; they cannot be the causal strategy.

## 8. Structural-lineage gate

Before any detector call, an adversarial validator asks:

> Is this substantially the old realization or a previously rejected realization with friendlier words?

The validator compares at least:

- conceptual-unit count and ordering;
- paragraph function ordering;
- triads/taxonomies/card sequences;
- setup -> qualification -> tidy conclusion rhythm;
- significance/preference staging;
- explanatory recap/aftercare;
- mirrored or balanced clauses;
- generic connective tissue;
- autobiography or attribution introduced only to sound more personal;
- preservation of source architecture without an independently justified reason.

If the answer is YES or materially uncertain:

```text
FAILED_STRATEGY_DESCENDANT = true
CANDIDATE_STATUS = REJECTED_BEFORE_DETECTOR
```

No synonym pass follows. Return to the semantic packet and generate a different realization.

## 9. Attribution and preservation gate

The candidate fails if it:

- turns a general claim into Joel autobiography without source authority;
- turns an observation into an interpretation or vice versa;
- moves uncertainty/certainty;
- changes chronology or causal direction;
- invents an anecdote, example, mechanism, fact, or safety claim;
- weakens or strengthens a substantive claim;
- imports syntax or prose from quarantined or unrelated donor material;
- edits `OWNER_LOCK` text without explicit authority.

## 10. Independent validation gate

The candidate author may perform ordinary self-review, but that does not satisfy this gate after repeated strategy recurrence.

A separate fresh reasoning context performs **diagnostic-only** lineage validation. It may return:

```text
PASS_NEW_REALIZATION
FAIL_FAILED_STRATEGY_DESCENDANT
FAIL_PROVENANCE
FAIL_SEMANTIC_PRESERVATION
FAIL_ATTRIBUTION
UNRESOLVED
```

It must not rewrite the candidate. Any FAIL or UNRESOLVED result blocks detector submission.

## 11. Detector-last rule

Pangram is downstream evidence only.

A Pangram call is allowed only after:

```text
provenance_gate = PASS
semantic_packet_gate = PASS
failed_strategy_lineage_gate = PASS
attribution_preservation_gate = PASS
independent_validation_gate = PASS
```

The exact tested boundary must be hashed and frozen before submission.

The `candidate_validated` control must also be saved as a separate hash-bound checkpoint while its detector status is still `not-run`. A later `detector_recorded` state is invalid unless it points back to that exact checkpoint and the submitted candidate hash matches it.

A negative result updates the failed-family ledger. It must not trigger synonym spinning or immediate local variants.

## 12. Next permitted cycle

For the Introduction:

1. Build exact `OWNER_LOCK` / `AI_TARGET` / `UNKNOWN_FROZEN` map.
2. Extract semantic/function packet for only the AI targets.
3. Remove the original AI realization and rejected candidates from the writer input.
4. Generate one fresh realization from the packet.
5. Run separate diagnostic-only strategy-lineage + preservation validation.
6. Show the owner only a candidate that passes those gates.
7. Pangram only after owner inspection or explicit authorization.

No further "cold pass" on the same mixed prose is an authorized strategy.

## 13. Mechanical enforcement and current state

The prose rules above are now projected into separate hash-bound artifacts:

- `HUMANIZATION-CONTROL-STATE-20260831.json` — exact provenance coverage, state machine, release block, and detector ordering;
- `INTRO-SEMANTIC-WRITER-INPUT-20260831.json` — the only input permitted to the Chat writer for this Introduction cycle;
- `INTRO-REJECTED-STRATEGY-LEDGER-20260831.json` — withheld from the writer and supplied only to the separate adversarial Chat;
- `../../scripts/validate_humanization_control.py` — mechanical identity/state validator;
- `../../tests/test_validate_humanization_control.py` — causal mutations for provenance, input leakage, strategy coverage, attribution, structural recurrence, adversarial independence, fail-closed release, and detector order.

Current workflow state is `prewrite_ready`. That is a valid control state but not a candidate pass: candidate visibility and detector eligibility remain blocked. No earlier whole-article revoice or mixed Chat rewrite is grandfathered into this cycle.

Validate mechanically from the repository root:

```bash
python3 scripts/validate_humanization_control.py \
  tasks/somatic-r15-clean-continuation-20260830/HUMANIZATION-CONTROL-STATE-20260831.json \
  --root .
```

The validator proves hashes, input isolation, recorded gate completion, and legal state transitions. It does not write prose, decide semantic equivalence, or substitute for the two required Chat reasoning contexts.
