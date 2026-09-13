# Owner Teaching-Trajectory — Operating Start

Updated: 2026-09-02
Status: **ACTIVE OPERATING PROCEDURE / non-authoritative experiment state**

This file operationalizes `OWNER-TEACHING-TRAJECTORY-ESCAPE-EXPERIMENT-20260902.md`. It does not change article authority, authorize Pangram, or promote experimental prose.

## Purpose

Make the Joel→Chat manual teaching loop easy to run while preserving enough exact evidence to determine later whether accumulated teaching had a reproducible, path-dependent effect.

The key separation is:

1. **raw trajectory capture during the episode** — preserve exact turns without cleaning them into rules;
2. **lesson promotion after a freeze event** — only then derive generalized generative lessons and update durable writer state.

This prevents the observer from replacing the natural teaching trajectory with its own running theory of the trajectory.

## Where to begin

Use a new ChatGPT conversation in the same Joel article Project/configuration and the same model/configuration when possible. The new chat should recover GitHub canonical article/task state as required by the Project, but Joel should not paste the experiment design, prior failure catalog, Pangram history, or a synthetic teaching script into the writer.

The intended discovery question is incremental: **given the currently durable Somatic lessons, does additional natural Joel teaching produce a cumulative writing state that the stored rules alone do not reproduce?**

## Joel's only setup message

Joel may use a short operational startup instruction that says, in substance:

- work on the Somatic Introduction/manual humanization lane;
- recover current GitHub canonical state and current manual-writer state;
- Joel will correct attempts naturally;
- after every substantive Joel correction, preserve the exact correction and the exact immediately preceding candidate in the raw trajectory ledger before writing again;
- do not convert the correction into a newly generalized writing rule during the live episode;
- when Joel says `freeze trajectory`, stop generation and freeze/analyze the episode.

The startup message should not teach the writer *how to write*. It only establishes tracking.

## Episode identity

At episode start, create one raw ledger file on this task branch:

`tasks/somatic-r15-clean-continuation-20260830/teaching-trajectories/TRAJECTORY-<YYYYMMDD>-<letter>-RAW.md`

Record:

- episode id;
- model/configuration if visible;
- start time/date;
- target article/span/function;
- GitHub writer-state SHA read before generation;
- status `DISCOVERY_ACTIVE`;
- explicit note that the ledger is raw evidence, not lesson authority.

Do not add interpretive lesson summaries at episode start.

## What is captured after each substantive Joel correction

Before the next prose attempt, append one immutable turn record containing:

- sequential turn number;
- exact immediately preceding assistant candidate, unchanged;
- candidate SHA-256 when mechanically available;
- Joel's exact correction/objection, unchanged;
- literal owner-response classification: `QUESTION`, `PROBE`, `REQUEST_FOR_EXPLANATION`, `HESITATION`, `ACCEPTANCE`, `REJECTION`, `SUBSTANTIVE_CORRECTION`, or `MIXED`;
- whether Joel supplied a positive example, negative example, analogy, conceptual correction, process correction, or stopping judgment — descriptive only, without claiming causality;
- exact next assistant candidate when it is produced.

Do **not** rewrite Joel's correction into cleaner language in the raw record. Do not delete profanity, shorthand, repetition, analogies, or apparently redundant wording: the literal trajectory is the experimental object.

Questions or reactions that contain no substantive correction need not trigger a GitHub write solely to satisfy bookkeeping; preserve them when the episode is frozen so the transcript remains exact.

## What the writer must not do during discovery

- Do not show Joel an experiment checklist after every turn.
- Do not ask Joel to classify his own correction.
- Do not teach Joel how to teach.
- Do not insert Pangram results, blinded-evaluator rationales, activation-steering conditions, or prior candidate catalogs into the writer context unless Joel naturally introduces them.
- Do not turn each correction into a growing `avoid X / do Y` prompt before the next generation.
- Do not claim a lesson is validated merely because the writer can verbalize it.
- Do not run autonomous writer/critic/rewrite loops between Joel corrections.

The exact correction itself remains in conversational context and can cumulatively influence the writer. The raw ledger protects it against later loss without replacing it with a model summary.

## Freeze command

The owner phrase **`freeze trajectory`** is the operational freeze command.

It may be used after:

- Joel sees an apparent genuine escape;
- the session has clearly stalled;
- Joel wants to stop for any reason.

On `freeze trajectory`, the writer must not generate another candidate first.

Freeze:

1. exact ordered Joel and assistant turns in the episode;
2. exact final candidate and nearest preceding failed candidate;
3. all available candidate hashes;
4. Joel's literal success/failure judgment;
5. model/configuration identity if available;
6. start/end timestamps or turn ordinals;
7. current raw-ledger commit identity.

Set episode status to one of:

- `SUCCESS_CANDIDATE_DISCOVERY_EPISODE`;
- `FAILURE_CONTROL_EPISODE`;
- `OWNER_STOPPED_UNRESOLVED`.

A success label records Joel's observed escape only; it is not causal proof or article authority.

## Post-freeze lesson promotion

Only after the raw episode is frozen:

1. descriptively tag teaching turns using the experiment's tag vocabulary;
2. identify candidate generative lessons separately from the raw transcript;
3. for each proposed lesson record:
   - exact Joel evidence/turns;
   - model diagnosis of the underlying generative mistake;
   - what future thought movement should change;
   - validation state: `OWNER_CONFIRMED`, `PROVISIONAL`, `REPLAY_SUPPORTED`, `REPLAY_FALSIFIED`, or `SUPERSEDED`;
4. update `articles/somatic-therapies/experiments/SOMATIC-MANUAL-HUMANIZATION-WRITER-STATE-20260831.md` only with lessons justified for durable reuse;
5. update the active lesson contract only when a correction actually changes an enforcement condition;
6. leave raw literal trajectory evidence in the episode file even if the later lesson interpretation changes.

The raw transcript outranks the model's post-hoc paraphrase of what Joel meant.

## Testing cumulative effect

If a success candidate is discovered, do not immediately treat the promoted lesson summary as the cause.

The next research sequence is:

1. same-task fresh-chat baseline from the pre-episode durable lesson state;
2. exact/increasing-prefix replay of Joel's teaching turns;
3. compressed-summary control containing the generalized lessons but not the original path;
4. order/turn-ablation controls around any apparent threshold;
5. persistence probes after teaching with no further correction;
6. held-out Somatic transfer prompt.

The decisive comparison for the cumulative/path hypothesis is especially:

**exact teaching trajectory vs the same lessons compressed into instructions.**

If the exact trajectory repeatedly works and the compressed summary does not, that supports a path-dependent in-context effect. If both work equally, explicit instruction content is the simpler explanation. If neither reproduces, the discovery episode is likely stochastic or task-specific.

## Pangram boundary

Do not use Pangram to decide when the live teaching trajectory has escaped. Joel's natural judgment and later blinded cold evaluation come first. Pangram may be run later only on an exact editorially credible candidate under the normal authorization/call-accounting gates.

Do not feed Pangram result language back into the learner during the discovery episode; that would change the teaching trajectory being studied.

## Owner burden

Joel's bookkeeping burden should be effectively one thing: **teach naturally**.

The Chat writer is responsible for GitHub raw capture after substantive corrections. Joel does not need to number turns, summarize lessons, tag corrections, maintain hashes, or remember where state is stored.

When Joel wants the episode frozen, he says: `freeze trajectory`.
