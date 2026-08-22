# Humanization Preservation Proof Gate

Status: **BLOCKING** for substantial Joel-byline reconstruction and detector repair.

This gate exists because a rewrite can be fluent, coherent, Pangram-green, and still be wrong by silently deleting, generalizing, moving, reassigning, or reinterpreting something Joel meant to preserve.

The governing shift is:

> **Do not generate and then hope the fidelity audit catches losses. Freeze what must survive, restrict what may change, validate the exact transformation, then spend detector calls.**

This protocol composes established requirements-traceability/change-control practice with per-transformation validation and the repository's existing source–meaning–context–destination ledgers. It does not create a new semantic-similarity score.

## 1. Applicability

Run the full gate for:

- P2S style-only reconstruction of an existing article;
- P3 developmental editing that changes, moves, consolidates, or deletes substantive material;
- D3 sectional reconstruction and D4 article-wide rewriting;
- any detector-driven edit that changes reader-visible semantics, attribution, structure, or placement;
- any repair following a discovered semantic/provenance loss.

Use a reduced gate for a bounded D2/local repair: freeze the exact local source span, enumerate the protected units touched by the edit, and run the same forward/reverse validation on that scope.

Pure P1/D1 mechanical corrections are exempt when they do not change visible semantic wording, sentence structure, paragraphing, order, link-anchor text, attribution, or tested boundaries.

## 2. Authority freeze — before drafting

Before producing replacement prose, record:

- authoritative article/source path and exact revision/SHA-256;
- exact natural section or changed boundary;
- preceding/following headings or other dependency context;
- current owner instruction and owner-final corrections;
- registered owner locks/protected functions that touch the boundary;
- source/evidence/provenance records needed to distinguish quotation, memory, later interpretation, inference, and model reconstruction;
- prior accepted candidate only when it is actually authoritative for the unit being changed.

Historical detector-green prose, stale assistant candidates, handoff summaries, and detached packets are not authority.

If authority is unresolved, stop content transformation rather than synthesizing a compromise master.

## 3. Preservation-unit ledger — before drafting

Decompose **the changed natural section plus load-bearing dependencies**, not the entire unchanged article, into stable preservation units.

A preservation unit may be:

- proposition/argument;
- certainty or scope modifier;
- attribution/provenance assignment;
- actor → action → object relation;
- chronology or causality;
- exact memory/quotation/formula/title;
- unique example/anecdote/joke;
- owner judgment or emotional evaluation;
- rhetorical/protected function;
- necessary recurrence whose function differs from an earlier occurrence;
- link, media, native object, caption, heading relationship, or other semantic publication object;
- required context/antecedent without which another unit changes meaning.

Minimum record:

| Field | Requirement |
|---|---|
| `unit_id` | Stable ID, e.g. `PU-TALK-07` |
| `source` | Exact path + span/anchor + source revision/hash |
| `authority` | owner-final / registered / owner-authored / approved source / other explicit provenance |
| `type` | claim / certainty / attribution / agency / chronology / memory / example / function / object / context |
| `meaning` | Exact proposition/function that must survive |
| `required_context` | Antecedent, qualification, neighboring claim, destination, or object needed for correct meaning |
| `allowed_disposition` | One of the controlled dispositions below |
| `candidate_mapping` | Filled after drafting with exact destination span or authorized non-preservation disposition |
| `status` | pending / preserved / moved / owner-superseded / owner-deleted / consolidated / FAIL |

### Controlled dispositions

Before drafting, every unit receives one of:

- `must-remain-here`;
- `may-move:<named destination>`;
- `may-reword-semantically`;
- `must-remain-exact`;
- `owner-superseded:<authority>`;
- `owner-deleted:<authority>`;
- `duplicate-function-consolidation:<named surviving realization and destination>`.

There is **no generic `omit`, `inferable`, `redundant`, `smoother`, `not needed`, or `better for Pangram` disposition** available to the assistant.

If a unit seems genuinely dispensable but no existing authority permits its removal, preserve it or make an explicit deletion proposal to Joel.

## 4. Change whitelist — before drafting

Write the authorized delta for the operation. The whitelist answers: **what is this edit actually allowed to change?**

Examples:

- sentence architecture/cadence only;
- remove one false attribution while preserving the underlying later interpretation separately;
- move one protected function to a named section;
- consolidate two genuinely duplicate explanations into one named surviving realization;
- repair a specific detector-localized transition without changing the surrounding claims;
- restore a named owner-final sentence.

Anything not covered by the whitelist is presumed invariant.

The whitelist should name forbidden side effects when risk is obvious, e.g.:

- `may correct father attribution; may not delete later readiness/co-parenting question`;
- `may shorten recap; may not remove unique causal mechanism`;
- `may move example; may not change who performed the action`.

## 5. Draft inside the authorized delta

Only after the preservation units and whitelist are frozen may substantial replacement prose be generated.

Use the existing coherence architecture card and idiolect/minimum-dose rules. Prefer intact owner prose, movement, deletion of unauthorized assistant aftercare, and local repair over broad regeneration.

The ledger is a constraint on meaning, not an instruction to preserve old sentence order or produce bureaucratic prose.

## 6. Forward traceability — source → candidate

Before detector submission, map **every** preservation unit to the candidate.

A unit passes only when its actual meaning/function survives with the required context and authority. Keyword overlap is insufficient.

Check explicitly for:

- polarity/negation changes;
- stronger or weaker certainty;
- narrower or broader scope;
- source wording becoming Joel's assertion or vice versa;
- remembered quotation becoming retrospective interpretation or vice versa;
- actor/object swaps;
- causal claims becoming mere sequence or mere sequence becoming causality;
- unique examples disappearing because the conclusion seems inferable;
- recurrence being removed even though its function differs at the second location;
- links/media/native objects surviving while their semantic anchor disappears;
- a moved unit losing the setup that made it mean the same thing.

Any unsuperseded `pending` or `FAIL` unit blocks the candidate.

## 7. Reverse traceability — candidate → authority

Forward coverage catches losses. Reverse traceability catches unauthorized inventions and semantic drift.

Compare the candidate against the authoritative source and classify every substantive delta:

- added proposition;
- deleted proposition;
- changed certainty/scope;
- changed attribution/provenance;
- changed actor/action/object;
- changed chronology/causality;
- moved material;
- consolidated material;
- new explanation/bridge/metaphor/moral;
- changed recurring-function placement;
- changed link/media/native-object relationship.

Every delta must map to:

1. an item in the frozen change whitelist; or
2. a direct current owner instruction/owner-final correction; or
3. a previously authorized source correction with exact provenance.

An **unexplained substantive delta is a hard failure**, even if the new sentence sounds better and even if the detector likes it.

## 8. Preservation proof condition

The candidate may advance only when all are true:

- authoritative source identity is frozen;
- changed-scope preservation ledger is complete;
- every unsuperseded preservation unit is mapped and passes;
- every substantive candidate delta is authorized;
- there are **zero unexplained deltas**;
- required context/antecedents survive;
- owner locks and protected functions pass;
- source wording, later interpretation, and synthesis remain correctly attributed;
- orphan/dependency and whole-argument checks pass;
- architecture/coherence and stopping-point gates pass.

This is a **translation-validation gate for the exact rewrite**. A good prompt or historically reliable worker is not evidence that the current transformation passed.

## 9. Detector submission gate

**No paid or certification Pangram call may be made on substantive rewritten text until the preservation proof condition passes.**

Diagnostic detector work on an intentionally synthetic semantic-loss mutant is allowed only when explicitly labeled as validator/detector research and kept outside article authority.

If a candidate has already been submitted and later fails preservation review:

- mark the detector result `diagnostic-only / fidelity-rejected`;
- do not promote its prose even if it is 100% Human;
- preserve the paid-call evidence and call accounting;
- repair from the highest-authority source, not from the detector-green failure.

## 10. After every detector-driven semantic edit

A prior preservation pass does not transfer automatically to the next candidate.

After each detector-driven edit:

1. update the change whitelist if and only if the new operation is authorized;
2. re-run forward traceability for the affected preservation units;
3. re-run reverse-delta classification on the exact new candidate;
4. re-run article-wide dependency/architecture checks required by `HUMANIZATION-ARCHITECTURE-GATE.md`;
5. require zero unexplained deltas again before another paid call.

Do not narrow review to the Pangram red window. A local detector edit can delete or alter a dependency elsewhere.

## 11. Consolidation and deletion rules

Deletion/consolidation requires a proof stronger than `the reader can infer it`.

For each removed source unit record one of:

- exact surviving equivalent span and why it performs the same function;
- named destination after movement;
- owner-superseded authority;
- owner-deleted authority.

If two passages are called duplicates, compare **proposition + certainty + attribution + rhetorical function + reader state + destination**. Similar topic is not duplication.

A later example may make an abstract preview unnecessary; the ledger still records that the preview's unique function, if any, was performed by the example before deletion is allowed.

## 12. Scope control — prevent ledger bureaucracy

Use the smallest scope that can reveal the failure:

- local D2 repair: changed paragraph/section + direct dependencies;
- D3 section reconstruction: complete natural section + cross-section antecedents/callbacks;
- D4/article-wide rewrite: article-wide preservation ledger, normally built from existing architecture/claim/protected-function records rather than atomizing every sentence.

Do not create one unit per sentence when several sentences perform one inseparable semantic function. Do split a single sentence when it contains two independently losable claims or provenance assignments.

## 13. Validator regression / semantic mutation testing

When tooling is added or changed, test the gate with deliberate semantic mutants. At minimum include fixtures that:

- delete one unique claim;
- delete a qualification while retaining the main clause;
- convert an owner's later interpretation into an attributed quotation;
- swap actor and recipient;
- strengthen `may/can/seemed` into certainty;
- collapse two distinct recurring functions as `duplicate`;
- remove a unique example while leaving its abstract conclusion;
- add an unsupported explanatory bridge;
- move a protected unit without its required antecedent.

The validator should fail each mutant. If it does not, improve the gate before trusting it on live article work.

Mutation tests validate the **preservation gate**, not Pangram.

## 14. Relationship to existing gates

This gate does not replace:

- `project-sources/EDIT-CONTRACT-AND-LEDGERS.md` — source/meaning/context/destination and permission authority;
- `project-sources/HUMANIZATION-AND-COHERENCE.md` — thought recovery and coherent reconstruction;
- `docs/HUMANIZATION-ARCHITECTURE-GATE.md` — whole-article architecture regression;
- `project-sources/IDIOLECT-PRESERVATION-PROTOCOL.md` — minimum edit dose and authorship-signal retention;
- Pangram exact-boundary rules — detector acceptance.

Order for substantive humanization:

**authority → preservation units + change whitelist → coherent draft → bidirectional preservation proof → architecture/cold audits → Pangram → repeat preservation/architecture proof after each detector-driven edit.**

## 15. Required pass receipt

For each substantive changed boundary, record:

```text
Authoritative source: <path/revision/SHA-256>
Changed scope: <section/boundary>
Edit dose/mode: <P2S/P3/P4, D2/D3/D4>
Preservation units: <count>
Forward traceability: PASS / FAIL; unresolved units: <IDs>
Substantive candidate deltas: <count>
Reverse traceability: PASS / FAIL; unexplained deltas: <IDs or none>
Owner/provenance separation: PASS / FAIL
Architecture/dependency gate: PASS / FAIL
Detector eligibility: ELIGIBLE / BLOCKED
Pangram: <exact result or not run>
Substantive claim changes: none / exact authorized list
Largest remaining weakness: <exact>
```

Do not call a humanization pass complete when the receipt is missing or contains an unexplained delta.

## Research basis and design choice

This gate is an **adaptation/composition**, not a claimed novel formal method. It draws on:

- requirements baselines, bidirectional traceability, change-impact analysis, and orphan detection in requirements engineering;
- translation validation's per-output correctness check rather than trust in the translator;
- mutation testing for validator/test adequacy;
- text-style-transfer research that treats content preservation separately from style and naturalness and cautions against relying on a single automatic similarity metric.

Design/rationale and bounded prior-art scan: `HUMANIZATION-PRESERVATION-GATE-DESIGN-2026-08-22.md`.
