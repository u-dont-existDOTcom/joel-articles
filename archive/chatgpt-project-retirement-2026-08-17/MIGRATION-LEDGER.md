# Project retirement migration ledger — GitHub reconciliation

Date: 2026-08-17

Live repository inspected before migration: `u-dont-existDOTcom/joel-articles` at main commit `7e0d82b419f4884391cc9cb6ca27f4b360a5ac8b`.

The live repository was newer than the local migration package and intentionally remained a governance incubator with an empty article registry. This migration therefore adds the Article Skill, active Project-derived protocols/tools, exact Project retirement archive, and Substack video correction **without registering or inferring any canonical article**.

| Item | Resolution | Active destination |
|---|---|---|
| Pre-cutover Project Instructions | archived exact; operational clauses promoted into root skill | `SKILL.md`; archive `PROJECT-INSTRUCTIONS.txt` |
| `ARTIFACT-FAMILY-LEDGER-TEMPLATE.md` | exact source archived; owner-video-aware candidate promoted | `project-sources/ARTIFACT-FAMILY-LEDGER-TEMPLATE.md` |
| `CONFIRMED-SUBSTACK-HELPER.json` | exact source archived; incorrect native-video one-payload rule superseded by Joel's correction | `project-sources/CONFIRMED-SUBSTACK-HELPER.json` |
| `CANON-FACTS.md` | exact source archived and promoted | `project-sources/CANON-FACTS.md` |
| `ARGUMENT-LEDGER-QUICKSTART.md` | exact source archived and promoted | `project-sources/ARGUMENT-LEDGER-QUICKSTART.md` |
| `html_islands.py.txt` | exact source archived; tested corrected classifier promoted | `project-sources/html_islands.py.txt` |
| `ARGUMENT-AND-EVIDENCE-ARCHITECTURE.md` | exact source archived and promoted | `project-sources/ARGUMENT-AND-EVIDENCE-ARCHITECTURE.md` |
| `review_package.py.txt` | exact source archived and promoted | `project-sources/review_package.py.txt` |
| `INTERLINKING-AND-HTML-SOURCE.md` | exact source archived; native-video/video-post distinction promoted | `project-sources/INTERLINKING-AND-HTML-SOURCE.md` |
| `GITHUB-BOOTSTRAP.md` | exact source archived; superseded operationally by root `SKILL.md` + `CANONICAL-REPO-MAP.md` | archive only |
| `EMERGENCY-FALLBACK.md` | exact source archived; retired from active authority because the target design is GitHub-only | archive only |
| native-video helper implementation | new complete tested candidate promoted | `project-sources/substack_transfer_helper.py.txt` |
| native-video regression suite | 21 local tests previously passed; promoted for repository regression | `tests/test_html_islands_video.py`, `tests/test_substack_video_transfer.py`, fixtures |

## Owner-final video rule

- Native Substack-uploaded video: preserve exact archival source; never place the video object in clipboard payload; split at the exact source position; use ordered copy parts plus manual native-video reinsertion at recorded anchors.
- Substack video-post embed: separate type; preserve/reduce to its canonical post URL in source position within the current payload segment; do not split solely for it.
- YouTube: separate independent type.

## Non-loss statement

The exact ten Project Source files and exact pre-cutover Project Instructions are retained under this archive with their original SHA-256 ledger. Operationally superseded files remain available as historical evidence; they are not silently discarded.

## Deliberately not imported

No article master, article owner-lock set, source/evidence packet, citation record, detector record, or article current state was inferred from Project memory or chat. The live repository's empty `articles/INDEX.json` remains authoritative until an article is explicitly imported under repository governance.
