# Romance detector repair — semantic fidelity audit — 2026-08-21

Status: **blocking closeout gate on task branch**. Canonical `main` remains unchanged.

## Why this audit exists

The detector-repair materializers correctly protected headings, links, named owner locks, and several exact anchors, but those invariants were not sufficient to prove that the article's full arguments survived. The current Part-1 r5 candidate reached Pangram 4 Human `0.9838229417800903`, but detector score is subordinate to owner fidelity.

A whole-article semantic closeout against registered canonical `main` found unapproved functional losses. Therefore r5 is **rejected as an article candidate even if its detector result is useful diagnostically**.

## Blocking semantic losses in Part 1

### 1. `Talk about making love before you do it` — BLOCKING

The r1 repair replaced the registered ~406-word section with a ~269-word father-question spine. Restoring Joel's father-derived question was correct and owner-required, but the replacement also removed existing functions that were not superseded:

- talk about sexual wants before the couple is already naked;
- bodily preferences / what relaxes and opens each person;
- ability to say kinky needs aloud;
- effects of sexual history on wants and avoidance;
- permission not to know yet;
- sex may mean bonding, play, sacredness, or ordinary decompression at different times;
- sex-drive mismatch changes over time and can create quiet resentment;
- test whether honesty survives once the couple is actually naked and disappointment is possible;
- bodies fitting is not enough; pre-sex conversation practices trust, attention, and being seen.

Disposition: **restore these functions while keeping the father question as the governing owner spine.** Do not revert to a detached comprehensive curriculum; make the additional sexual conversation grow out of the father/readiness question and lived honesty problem.

### 2. `Affection and the simmer` — BLOCKING

The r2 compression cut the section from ~268 words to ~132. It retained Toft/no-agenda touch, Anami/simmer, a brief barometer sentence, and personal responsibility, but dropped or materially weakened:

- concrete simmer examples between encounters;
- the explicit need for both safe nonsexual affection and a living erotic current;
- the point that the simmer must not become relationship homework;
- the full `if sex changed, what else changed?` diagnostic movement;
- the argument that sex deserves intentional time rather than exhausted leftovers.

Disposition: **restore all functions.** Existing local attempts show that merely reinstating a balanced Toft-vs-Anami outline is detector-hostile, so preserve the functions without rebuilding a symmetrical mini-essay.

### 3. `Can Casual Sex or a Situationship Actually Be Honest?` — RESTORE UNIQUE FUNCTIONS

The current section has useful detector evidence, including a full natural-section realization at 100% Human, but two r1 deletions removed meaning rather than only repetition:

- `The person getting more of what they want may think the arrangement is fulfilling. Usually they’re just less aware that it isn’t.`
- the closing free-love-community consequence that people are not disposable, bonds can be acknowledged, and any children have a village.

The second passage overlaps the earlier claim that honest casual sex is almost impossible outside a loving poly community or tribe, but its child/village consequence is not fully duplicated.

Disposition: restore the unique claim/consequence; later detector work may move/compress them, but may not silently delete them.

### 4. Patient/caregiver passage — RESTORE NUANCE

The r2 patient edit changed:

`Of course I helped. Saying, “I’m not your doctor or therapist,” every time would have been cold. But enough moments become a pattern.`

into a shorter explanation that Joel usually had an answer and therefore answered. The shorter version preserves why he helped but loses the explicit distinction between humane help in an individual moment and an unhealthy role emerging cumulatively.

Disposition: restore that distinction.

## Part-1 changes that pass semantic review

- Crucible safety rewrite: function preserved — terror/control is not mutual wounded triggering; fear of saying no/truth/leaving exits the mutual communication frame; involve others and prioritize safety.
- ordinary-time rewrite: same epistemic claim, with ordinary behavior still outranking self-description.
- slow/community → Gandarussa rewrite: keeps lack-of-tribal-brakes claim and strengthens the personal causal link to self-imposed brakes/Gandarussa.
- STI/attachment r5 restoration: exact natural Casual section wording returned to the previously measured 100%-Human realization.

## Part-2 local repairs

Semantic review found no blocking owner-argument loss in the three latest local repairs:

- `Not A Performance`: the removed generalized female-side mirror was assistant-originated symmetry in a Joel-accepted provisional passage; the owner masculine-performance argument, Toft/Anami receiving examples, choice, invitation, and crisis-manufacture point remain.
- `Two Pillars`: same causal claim remains; detached summary was folded into the lived friend-circle → two-person-backup-system movement.
- psychedelic discernment: ordinary-life limitation remains as `the intimacy can be completely real without telling you whether the two of you actually work together sober`; the removed irritation/jealousy/money/boredom list was elaboration, not a distinct conclusion.

## Detector/cost state discovered during closeout

Part-1 aggregate r5 exact candidate SHA:
`e6b9e546bb2f07af8e18fc65fb6883d27bf0106d93f5f02d6674a88e034d572d`

Pangram 4 result:

- Human `0.9838229417800903`
- AI `0.01617708057165146`
- one 156-word AI window spanning the end of `Affection and the simmer` into the opening of `Casual Sex`.

This reinforces the existing composition/boundary finding: the Casual section itself has a previously measured exact 100%-Human natural realization, while the aggregate can still label a cross-boundary span AI.

The r5 aggregate paid reservation occurred at `2026-08-21T18:09:08.607420+00:00` before the supersession commit landed, so its 10-credit call is real and remains counted. The live public r5 spec was then tombstoned to prevent any future reuse of that rejected semantic candidate; the former exact spec remains in Git history.

## Decision

**Do not promote Part-1 r5.**

Next candidate must restore the four semantic-loss groups above first. Only after semantic invariants pass should detector optimization continue. Detector edits may change realization, ordering inside a section, or redundancy, but every distinct owner/canonical argumentative function needs an explicit preserved/moved/superseded disposition.

## Durable process lesson

Named-anchor and structure invariants are necessary but not sufficient for editorial fidelity. A detector candidate can pass every mechanical invariant while deleting unlabeled argumentative functions. Final closeout therefore needs a **semantic function ledger**: for every changed span, identify the source functions and mark each `preserved`, `moved`, `owner-superseded`, or `lost`. Any `lost` function blocks promotion unless Joel explicitly supersedes it.
