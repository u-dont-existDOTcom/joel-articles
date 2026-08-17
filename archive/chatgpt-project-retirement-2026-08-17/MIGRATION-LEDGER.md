# Project retirement migration ledger — GitHub reconciliation

Date: 2026-08-17

Live repository inspected before migration: `u-dont-existDOTcom/joel-articles` at main commit `7e0d82b419f4884391cc9cb6ca27f4b360a5ac8b`.

The live repository was newer than the local migration package and intentionally remained a governance incubator with an empty article registry. This migration adds the Article Skill, active Project-derived protocols/tools, exact Project retirement archive, and Substack video correction **without registering or inferring any canonical article**.

| Item | Resolution | Active destination | Migration status |
|---|---|---|---|
| Pre-cutover Project Instructions | archived exact; operational clauses promoted into root skill | `SKILL.md`; archive `PROJECT-INSTRUCTIONS.txt` | resolved |
| `ARTIFACT-FAMILY-LEDGER-TEMPLATE.md` | exact original blob archived; owner-video-aware tested candidate promoted | `project-sources/ARTIFACT-FAMILY-LEDGER-TEMPLATE.md` | resolved |
| `CONFIRMED-SUBSTACK-HELPER.json` | exact original blob archived; incorrect native-video one-payload rule superseded by Joel's correction | `project-sources/CONFIRMED-SUBSTACK-HELPER.json` | resolved |
| `CANON-FACTS.md` | exact source archived and promoted | `project-sources/CANON-FACTS.md` | resolved |
| `ARGUMENT-LEDGER-QUICKSTART.md` | exact source archived and promoted | `project-sources/ARGUMENT-LEDGER-QUICKSTART.md` | resolved |
| `html_islands.py.txt` | exact original blob archived; tested corrected classifier promoted | `project-sources/html_islands.py.txt` | resolved |
| `ARGUMENT-AND-EVIDENCE-ARCHITECTURE.md` | exact source archived and promoted | `project-sources/ARGUMENT-AND-EVIDENCE-ARCHITECTURE.md` | resolved |
| `review_package.py.txt` | exact source archived and promoted | `project-sources/review_package.py.txt` | resolved |
| `INTERLINKING-AND-HTML-SOURCE.md` | exact original blob archived; native-video/video-post distinction promoted | `project-sources/INTERLINKING-AND-HTML-SOURCE.md` | resolved |
| `GITHUB-BOOTSTRAP.md` | exact source archived; superseded operationally by root `SKILL.md` + `CANONICAL-REPO-MAP.md` | archive only | resolved |
| `EMERGENCY-FALLBACK.md` | exact source archived; retired from active authority because the target Project design is GitHub-only | archive only | resolved |
| native-video helper implementation | complete tested candidate promoted | `project-sources/substack_transfer_helper.py.txt` | resolved |
| native-video regression suite | 21 local tests previously passed; exact tested files promoted | `tests/test_html_islands_video.py`, `tests/test_substack_video_transfer.py`, fixtures | resolved |
| pared-down ChatGPT Project instructions | GitHub-only loader written; contains no duplicate editorial protocol | `MINIMAL-PROJECT-INSTRUCTIONS.md` | resolved |

## Byte-level archive audit

The retirement archive contains all ten original Project Source files as exact Git blobs corresponding to the local pre-cutover snapshot. The source-content SHA-256 values remain recorded in `SHA256SUMS.txt`. A tree audit caught and repaired an initially non-identical historical copy of `ARTIFACT-FAMILY-LEDGER-TEMPLATE.md`; the final archived blob is the exact source blob rather than the manually reconstructed copy.

The active corrected Substack classifier, transfer helper, transfer protocol, compatibility profile, video regression tests, and five fixtures were compared by Git blob identity with the previously locally tested migration package. The active artifact-family ledger was also corrected to the exact tested-package blob after a one-newline discrepancy was detected.

## Owner-final video rule

- Native Substack-uploaded video: preserve exact archival source; never place the video object in clipboard payload; split at the exact source position; use ordered copy parts plus manual native-video reinsertion at recorded anchors.
- Substack video-post embed: separate type; preserve/reduce to its canonical post URL in source position within the current payload segment; do not split solely for it.
- YouTube: separate independent type.

## Non-loss statement

**Project-source unresolved count: 0.**

The exact ten Project Source files and exact pre-cutover Project Instructions are retained under this archive with their original SHA-256 ledger. Operationally superseded files remain available as historical evidence; they are not silently discarded.

## Deliberately not imported

No article master, article owner-lock set, source/evidence packet, citation record, detector record, or article current state was inferred from Project memory or chat. The live repository's empty `articles/INDEX.json` remains authoritative until an article is explicitly imported under repository governance.

## Validation status

The pre-GitHub migration package passed 21 Substack regression tests, the Substack helper self-test, the review-package self-test, patch/application guards, and clean-ZIP verification. GitHub's repository workflow is configured to run full unit-test discovery plus the content-authority, architecture-map, and Codex/GitHub policy validators on pull requests. GitHub Actions had not instantiated a PR workflow run at the time this ledger was updated, so **absence of a reported check is not recorded as a passing CI result**. The PR must not be called fully validated or merged solely on the basis of an empty Actions status.
