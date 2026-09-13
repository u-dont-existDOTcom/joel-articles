# Owner correction — thin automation, direct reasoning-chat authorship

Task: `somatic-r15-clean-continuation-20260830`

Date: 2026-08-31

## Owner observation

Joel reports that the automated Pro/Codex supervision loop produced no meaningful whole-article Pangram progress after many hours, while earlier direct Extra High reasoning chats were producing progress within a few turns.

## Controlling interpretation

The problem is not automation as a transport/tooling layer. The problem is using automation as the creative/editorial control loop.

For this humanization task:

- reasoning chats own all writing and editorial judgment;
- Codex is a thin executor only;
- no Codex-authored strategy, prose, detector diagnosis, or experiment design;
- no fragment-by-fragment detector optimization as the primary production method;
- no local Pangram-Human result counts as root-outcome progress;
- direct whole-document Pangram movement is the only detector outcome progress signal.

## Strategy correction

Supersede the pending `somatic-r15-whole-article-fresh-pro-revoice-v1` strategy before execution.

The next writing strategy is `somatic-r15-direct-extra-high-whole-article-v1`:

1. Use a genuinely fresh Extra High reasoning chat as the actual writer, not as a supervisor of Codex.
2. Give it the literal complete current article plus only the owner/fidelity/source-integrity constraints needed to preserve meaning.
3. Withhold Pangram scores, fragment experiments, local detector windows, failed phrasings, and process history from the writing chat.
4. Ask for one complete coherent whole-article revoice in a small number of turns. The article ideas/claims/examples/architecture/safety/evidence distinctions are frozen as correct; only surface realization may change.
5. Codex may only transport exact prompt/response bytes, persist artifacts, materialize the boundary, run deterministic preservation checks, and—under a separate explicit directive—perform the whole-document Pangram action.
6. No fragment detector call is authorized in this strategy.
7. Evaluate strategy efficacy only after a whole-document measurement.

## Root-level stop rule

- Candidate 1 whole-document result > prior best whole Human `0.1547368467`: direct progress; continue with at most one additional fresh Extra High whole-article pass informed only by whole-document evidence.
- Candidate 1 <= `0.1547368467`: one second materially fresh Extra High whole-article attempt may be justified, but no fragment loop.
- Two fresh Extra High whole-article candidates without improvement above `0.1547368467`: classify the AI-only direct-chat method failed and stop further AI rewrite iteration pending a genuinely different authorship method.

## Automation boundary

Automation remains useful for:

- exact copy/transport;
- hashes and provenance;
- preservation/link/native-object verification;
- Git state;
- browser operation;
- Pangram exact-input submission and recovery.

Automation is not used for:

- deciding what sounds human;
- choosing local edits;
- decomposing the article into detector experiments;
- supervising an editorial worker that itself reasons about the prose;
- converting local scores into a theory of whole-document progress.

The registered `master.html` remains unchanged until a separately validated final promotion.