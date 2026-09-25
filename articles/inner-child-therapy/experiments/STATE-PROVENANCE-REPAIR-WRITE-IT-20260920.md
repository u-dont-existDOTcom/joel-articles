# Inner Child Therapy — state/provenance repair after stale Write-It promotion

Date: 2026-09-20
Status: **AUTHORITY GAP IDENTIFIED / ROUGH P1 DEMOTED / WRITE-IT SUBSECTION UNRESOLVED**

## Owner correction

Joel corrected the working context:

> the first para after write it don't send it was not the final para we were saving, that was the rough thought you asked me for. why are things not being saved correctly?

This correction outranks the stale review assembly.

## Verified provenance chain

### 1. Owner supplied rough cognition

Artifact:
`EPISODE-008-WRITE-DONT-SEND-OWNER-ROUGH-COGNITION-20260919.md`

It explicitly labels the material:

`OWNER ROUGH THOUGHT-SHAPE / SOURCE FOR MINIMUM-CLEANUP PARAGRAPHS`

The paragraph beginning:

> Yeah, I mean, this happens all the time...

therefore originates as rough owner cognition, not article-final prose.

### 2. Candidate O normalized that rough cognition near-verbatim

Artifact:
`EPISODE-008-WRITE-DONT-SEND-OWNER-NEAR-VERBATIM-CANDIDATE-O-20260919.md`

It explicitly says:
- P1 is a near-verbatim normalization of Joel's rough cognition;
- the candidate is owner-cognition-assisted prose;
- the purpose is independent detector testing.

Candidate O P1 tested Pangram Human 1.0.

That detector result is evidence about the exact experimental paragraph. It is **not article promotion authority**.

### 3. Recovery state Q made the first bad promotion

`HUMANIZATION-RECOVERY-STATE-20260919Q.md`

Status:
`WRITE IT DON'T SEND IT P1 SOLVED HUMAN 1.0`

It instructed:
> Near-verbatim owner cognition ... leave unchanged unless Joel rejects editorially.

This incorrectly allowed detector success + absence of rejection to stand in for positive owner/article promotion authority.

### 4. Recovery state R immediately superseded Q

`HUMANIZATION-RECOVERY-STATE-20260919R.md`

It explicitly says it supersedes Q and states:

> Write It. Don't Send It Yet remains unresolved

It also clarifies:
> near-verbatim owner P1 passes Human; that proves preservation of Human thought shape, not autonomous generation.

Therefore any later state that treated Q's P1 as solved/current without reconciling R is stale.

### 5. Article-wide coverage later consumed the stale review assembly

`ARTICLE-WIDE-COVERAGE-20260919.json` stored those rough-derived bytes as `current_assembly-032` with:
- `editorial_status: preserve_current_assembly`;
- wording that made the review snapshot look like current article state.

The companion workboard also referred to a `current accepted/locked review assembly`.

That was incorrect because:
- the later recovery state had already restored the subsection to unresolved;
- Inner Child Therapy is not registered in `articles/INDEX.json`;
- no hash-bound article master or owner-lock file existed to arbitrate the conflict;
- no explicit promotion receipt exists for Candidate O P1.

## Additional chat-only state

Prior conversation recovery found at least two later first-paragraph candidates described in Chat as `saved` or `current` after the rough-cognition episode.

However no current GitHub authority record has been found that:
- identifies one of them as owner-final;
- records explicit owner acceptance;
- supersedes the other;
- binds the selected exact bytes into an article master.

Therefore **do not reconstruct the final P1 from chat memory or choose between those candidates by inference.**

Current durable status:
**exact final/saved Write-It P1 = AUTHORITY UNRESOLVED / not recovered from canonical GitHub state.**

## Causal mechanism

This was not a simple missing-save event.

The failure chain was:

`rough cognition -> near-verbatim detector experiment -> Pangram Human -> assistant "solved" state -> later state supersedes it -> stale review assembly fails to apply supersession -> article-wide inventory labels stale bytes current -> later Chat reads inventory as article context`.

Underlying control failures:

1. **Detector success was allowed to imply article-state promotion.**
2. **"Solved" did not require explicit owner acceptance/promotion evidence.**
3. **Supersession was stored in prose state files but not mechanically propagated into assemblies.**
4. **Review-snapshot labels (`current_assembly`) were semantically stronger than their actual authority.**
5. **The article remained unregistered, so no canonical master/locks blocked stale experimental prose from masquerading as current.**
6. **Later context reconstruction read the coverage inventory without resolving its source against the latest superseding state.**

## Corrective rules

### Promotion gate

Experimental prose may enter current article context only with an explicit promotion record that binds:
- exact text/hash;
- provenance class;
- owner/editorial status;
- destination paragraph/section;
- superseded text/disposition.

The following are never promotion authority by themselves:
- Pangram Human;
- assistant says `solved`;
- owner silence;
- presence in a rolling/review assembly;
- `current_assembly` label;
- owner cognition used as an experiment;
- owner acceptance of an operation but not its exact wording.

### Supersession gate

Any assembly/coverage build must resolve later superseding state before labeling prose current.

If:
- an earlier state says `solved`; and
- a later controlling state says `unresolved`;

the assembly must fail closed to `unresolved`.

### Unregistered-article gate

Until Inner Child Therapy has registered authority:
- do not call a review assembly an article master;
- use `historical_review_snapshot` / `experimental_candidate` / `owner_final` provenance explicitly;
- when exact current prose cannot be proven, say `AUTHORITY UNRESOLVED` rather than selecting the newest-looking paragraph.

### Owner-rewrite context gate

Before asking Joel to rewrite any paragraph, show the surrounding chain so he can see what functions are already covered and what should be omitted.

## Repairs applied on this branch

- `ARTICLE-WIDE-COVERAGE-20260919.json` now marks `current_assembly-032` as historical rough-cognition experiment, **not article-final authority**.
- `ARTICLE-WIDE-WORKBOARD-20260919.md` now states that `current_assembly` was a historical review-snapshot label, not authority.
- the Write-It subsection is explicitly restored to **unresolved**.
- no guessed replacement paragraph has been promoted.

## Next authority action

Recover the exact intended final/saved P1 from a source with explicit owner acceptance if one exists.

If it cannot be recovered, show Joel the relevant surrounding section plus the competing chat-only candidates and obtain an explicit current owner selection/rewrite. Then save that exact selection with a promotion receipt before any further humanization work uses it as context.
