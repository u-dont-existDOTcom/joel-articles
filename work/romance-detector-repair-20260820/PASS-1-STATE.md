# Romance detector repair — pass 1 state

Updated: 2026-08-20

## Authority boundary

- Canonical authority remains `main:articles/romance/master.md` at SHA-256 `af50b7b93662daf00d484ad83faa0453ff0a2a4fda2867ecfd467166b4c984fe`.
- This task branch is candidate work only and does not establish `owner_final`, publication, or replacement article authority.
- Joel's `ok` on 2026-08-20 authorizes applying the six preserved surgical repairs in `PASS-1-CANDIDATES.md` to the **task candidate** and proceeding through fidelity/architecture validation and exact-half Pangram retesting. It does not by itself merge the candidate to `main`.

## Accepted candidate scope

The pass is intentionally surgical:

1. simplify the sex-drive mismatch paragraph without changing its practical recommendation;
2. combine the Anami/jade-egg source progression without changing source roles or claims;
3. reduce explanatory repetition in `Muses & Directors` while preserving the masculine/feminine, intuition, and Crucible-safety claims;
4. remove the economy analogy while preserving the unequal-role/complementarity argument;
5. remove the earlier duplicate surrender explanation and one repeated `gently`, preserving the later concrete surrender paragraph;
6. make the opening of `After leaving` more direct while preserving every substantive judgment, uncertainty, agency assignment, Devadatta example, and Mr. Rogers ending.

## Blocking architecture/fidelity gate before materialization

- Section order/headings: unchanged by design.
- `coercion-exits-mutual-crucible`: untouched.
- `primal-owner-argument`: preserved; no neutralization of polarity, leadership, surrender, or masculine/feminine claims.
- `opening-father-question`, `bear-terminal-callback`, `children-survive-romance`, `gandarussa-preserved`, and `identity-hale-not-heidi`: outside the edited spans and protected by materializer anchors.
- Native-object marker identity/order: unchanged by design and verified by the materializer.
- Markdown link destinations: unchanged by design and verified by the materializer.
- Claims added: none intended.
- Claims deleted: none intended; one duplicate surrender explanation is removed because the proposition remains in the later concrete paragraph.
- Certainty, actor assignment, chronology, causality, entity identity: no intended changes.

## Deterministic materialization

Current materializer:

`work/romance-detector-repair-20260820/apply_pass1.py`

It fails closed unless the registered source master and both historical Pangram halves match their exact SHA-256 values, every replacement source occurs exactly once, and the candidate master preserves headings, native markers, Markdown link destinations, and protected anchors.

Expected generated candidate family:

- `candidate-master.md`
- `candidate-part-1.txt`
- `candidate-part-2.txt`
- `candidate-manifest.json`

All remain `candidate_not_owner_final` until later owner acceptance and registered-authority reconciliation.

## Detector boundary

- No new Pangram submission has yet been made for pass 1.
- Do not run isolated-sentence detector probes first.
- After materialization and Git durability, measure exactly the two candidate halves at their fixed historical split locations.
- If a paid action becomes ambiguous, recover before repeat; never automatically buy another call.
- Historical localization tool issue #110 remains a separate tooling issue and does not block the article retest.

## Pending

1. PR/CI validates the task branch and materializer regression tests.
2. Materialize the candidate family from the exact registered master and exact historical halves.
3. Push candidate artifacts before detector calls.
4. Run exactly one Pangram-4 measurement per candidate half.
5. Read detector evidence from GitHub and rerun the article-wide semantic/architecture/fidelity gate before any authority change.
