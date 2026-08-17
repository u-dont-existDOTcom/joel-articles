# Review Workflow Rules — Judgment-First Corrections and Portable Review Artifacts

## 0. Use the implemented interface

`REVIEW-INTERFACE-SPEC.md` is not a deliverable by itself. For substantial reviews, generate the actual commentable side-by-side artifact with `interactive_review.py` and `review_interface_template.html`. A static yellow/collapsed diff lacks the required comments, decisions, rhetoric controls, persistence, reasoning, search, and exports and therefore does not satisfy this workflow. Preserve the last confirmed interface behavior as a locked artifact-family invariant.

Use this whenever Joel supplies comments, annotations, Keep/Remove/Brainstorm decisions, slider settings, or corrections on a draft, diff, or review interface.

## 0A. Canonical project state and revision IDs

Before substantive review work, create or update `PROJECT_STATE.md` from `PROJECT-STATE-TEMPLATE.md`. Treat the last user-approved article plus that state file as authoritative. Chat memory, a conversation title, a remembered filename, and a file called `final` do not establish project state.

Use monotonic revision IDs such as `r05-candidate` and `r05-approved`. Delivery creates a candidate, not approval. Record the exact current article, last approved article, diff baseline, previous delivery, raw comments file, interface format, row scope, unresolved issues, required links/assets, package name, and SHA-256 values. Label any reconstruction as a reconstruction rather than the original.

Generated sandbox files are temporary. Build and deliver the portable ZIP in the same pass, with project state and checksums sufficient for a new conversation to continue without relying on chat history.

## 1. Comments are judgment signals

A review comment is not automatically a literal search-and-replace command. Before applying it, identify:

- the proposition and certainty;
- the rhetorical function;
- the intended audience;
- the required definition, setup, transition, link, caption, or media anchor;
- direct dependent passages and derivative artifacts;
- the distinction or judgment Joel is protecting.

Apply that judgment throughout the affected material. Ask one narrow question only when two materially different interpretations remain.

## 2. Reconcile the complete comment history

Order comments and decisions chronologically. Later clarifications, retractions, corrections, and “never mind” instructions supersede earlier local comments. Preserve the superseded item in export history, but do not let it control the article.

A correction is dependency evidence. After applying it, inspect analogous passages and every direct dependent comparison, pronoun, transition, heading, example, conclusion, caption, link, and artifact.

## 2A. Comment-resolution ledger

Preserve the raw comments export unchanged as `review/source-comments.json`. Use `COMMENT-RESOLUTION-LEDGER-TEMPLATE.md` for interpretation and status. Every source comment receives a unique issue ID, exact target/quote, classification, underlying judgment, dependency/context note, status, and exact revised location. Allowed statuses are implemented, partially implemented, needs clarification, not implemented with reason, and superseded/retracted.

Before delivery, unresolved issue count is zero unless Joel explicitly accepts the open issue and `PROJECT_STATE.md` records that acceptance. A nearby edit does not resolve a comment by implication. After every insertion, deletion, or move, inspect the paragraph before and after it for broken transitions, orphaned pronouns, duplicated setup, displaced definitions, media-anchor damage, and conclusions that no longer follow.

## 3. Keep substantive evidence challenges outside the prose until approved

Research, guidelines, consensus, or source verification may challenge a claim during an editorial pass. That challenge does not create authority to rewrite the argument.

Until Joel approves a substantive change:

- preserve the article’s claim and epistemic force under the current edit contract;
- report the evidence problem outside the article;
- state precisely what the evidence would change;
- show an optional replacement or qualification separately;
- do not silently insert a rebuttal, debate section, safety correction, or preferred treatment hierarchy.

## 4. Lock the audience contract

Before drafting or editing, record the article’s audience contract:

- the primary reader’s role or identity;
- what that reader is expected to know already;
- the reader’s relationship to the writer and subject;
- the decision, action, understanding, or emotional task the piece is meant to support;
- the stakes and publication context;
- the intended form of address, register, and acceptable technical vocabulary;
- audiences the article is explicitly not trying to serve;
- any section that deliberately addresses a different audience.

Preserve that contract through every pass. Audience drift can occur in any genre, including:

- **role drift:** reader → clinician, lawyer, manager, investor, policymaker, reviewer, or insider;
- **expertise drift:** lay or mixed audience → specialist shorthand;
- **goal drift:** practical decision guide → literature review, advocacy brief, sales page, or abstract explainer;
- **relationship drift:** peer or witness → lecturer, therapist, institutional spokesperson, or marketing voice;
- **scope drift:** a defined community or readership → an imagined universal public;
- **action drift:** helping the reader decide or act → merely displaying information;
- **register drift:** conversational, tender, polemical, or practical prose → academic, bureaucratic, clinical, or corporate language;
- **assumed-knowledge drift:** unexplained concepts or source vocabulary the intended reader was never expected to know;
- **stakes drift:** the reader’s lived problem becomes an abstract disciplinary debate;
- **venue drift:** a Substack article begins sounding like an internal memo, grant application, journal article, or slide deck.

A source may have been written for a different audience. Translate its findings into the current article’s contract rather than importing its address, jargon, priorities, or assumptions. A hybrid article may shift audiences by section, but each shift must be deliberate, signaled, and locally justified.

For example, an end-user guide should not drift into therapist-facing `the client` or `the patient`; a public legal explainer should not become a lawyer’s memo; a community article should not become an academic sociology review; and a founder essay should not become an investor pitch unless that change was requested.

## 5. Consolidate by function, not keyword repetition

Before removing repeated material, inventory the job of every occurrence. A passage may:

- define;
- orient;
- give evidence;
- compare options;
- warn;
- summarize a sequence;
- provide a decision rule;
- close a section;
- anchor a link or native object.

Consolidate only duplicated function. Move unique material to the location where it is first needed. Report the sections combined, the destination of every unique claim/example/qualification/link/function, wording moved intact, wording merged, actual duplicate functions, and any proposed superfluous material requiring authority. After resolving owner comments, run an independent whole-article redundancy audit rather than limiting review to the passages Joel happened to mark.

## 6. Classify every changed unit semantically

Use one of these labels:

- **Rewritten**
- **Moved**
- **Consolidated**
- **Structurally removed** — the parent architecture was replaced, with unique function accounted for elsewhere
- **Owner-deleted**
- **Preserved**

A deletion marker alone is insufficient. Moved and consolidated units must name and, when possible, link to the destination. A structural removal must name the replaced parent structure and where each unique function went.

## 7. Preserve the stronger side of the comparison

Do not assume revised wording is better because it is newer or more technical. Compare original and revision for clarity, precision, rhetorical function, and voice. Restore the original when it performs the job better.

When a passage feels abrupt, test relocation before deletion or rewriting. Repair both its former transition and its destination transition.

## 8. Required post-comment audits

After implementing comments or decisions, run:

- source–meaning–context–destination reconciliation;
- orphan audit;
- transition-word, pronoun, and antecedent audit;
- heading hierarchy and table-of-contents audit;
- audience-contract audit, including role, expertise, goal, relationship, scope, action, register, assumed knowledge, stakes, and venue;
- jargon and plain-language audit;
- native-object placement audit;
- link and comparative-evidence placement audit;
- independent redundancy audit;
- artifact-family regression.

Comments must never be applied as mechanical search-and-replace instructions.

## 9. Baseline integrity and two review baselines

The source side of a new diff is the last user-approved article unless Joel explicitly selects another baseline. Record its exact filename, revision ID, and SHA-256 in `PROJECT_STATE.md`, the review metadata, and the package. Do not silently use an older source because it is easier to find. A handoff excerpt or `NEXT_SECTION_SOURCE` is a routing target; inspect the complete authoritative source and neighboring headings before claiming no omissions or section completion.

For a substantial rewrite, maintain:

1. **original source vs current revision** — shows the full transformation;
2. **previous delivered revision vs corrected revision** — shows only the repair after Joel’s latest feedback.

Never substitute the first for the second after a correction. Both use semantic blocks and preserve native objects as typed placeholders rather than editor overlay text. For a large article, omit equal rows after full alignment with `--changed-passages-only`; keep the baseline type distinct from row scope.

## 10. Fixed review-interface contract

Each semantic unit may carry:

- one editable primary comment;
- selected-text or whole-unit scope with exact quote and offsets when available;
- **Keep** — locks the current passage against casual later rewriting;
- **Remove** — authorizes deletion subject to dependency and orphan repair;
- **Brainstorm** — requests alternatives but approves none;
- **Reasoning** — discloses classification, reason, origin, controlling rule, claim/certainty effect, destination, and uncertainty;
- **Humor, Technical detail, Length, Bluntness** — rhetoric settings only.

The complete interface also retains Copy JSON, Copy Markdown, JSON/Markdown file export, local persistence, source/revised labels and hashes, search, and changed-only filtering. Preserve `joel-commentable-diff-review-v4` compatibility unless Joel explicitly approves a migration. Performance optimization means changed passages only plus the complete interface; it never means silently removing controls.

Sliders never authorize changes to claims, evidence, certainty, recommendations, attribution, causal meaning, links, or native-object placement.

## 11. Portable artifact-family delivery

For substantial annotated review work, one ZIP is the authoritative delivery unless Joel explicitly requests another form. The base package is:

```text
article/<article-rNN-candidate.html>
review/<commentable-diff-rNN.html>
review/source-comments.json
project/PROJECT_STATE.md
project/CHANGELOG.md
project/README.md
project/MANIFEST.json
project/SHA256SUMS.txt
```

Add the second review baseline, comment-resolution ledger, section-provenance ledger, cumulative omission audit, assistant-produced recheck queue, artifact-family ledger, browser-test report, transfer helper/report, and other family members when applicable. The provenance/omission/recheck files are mandatory when the ZIP is also a full worker handoff. Do not reconstruct an unavailable authoritative source merely to fill the ZIP. State the omission.

Use `review_package.py` to build and statically verify the package when available. The continuation state records the exact authoritative candidate filename and revision; source, revised, editor-body, payload, helper, and package hashes when applicable; superseded files; locked decisions and Keep states; pending destination tests; known weakness; best next step; expected marginal gain; and over-editing risk.

Do not call a file merely `latest` or `final`. Name it, date it, hash it, and state what it supersedes. Preserve the original comments JSON unchanged.

## 11A. Exact-package regression

Follow `REVIEW-PACKAGE-REGRESSION.md`. Unzip the exact candidate package into a clean directory, open the article and review locally, block network access for the review, exercise selected-text and whole-cell comments, all decisions and sliders, Copy JSON/Markdown, file exports, persistence, search, filtering, reasoning, JSON parsing, links, and checksums. Run `interactive_review.py --selftest`, `review_interface_browser_test.py` on the exact review, and `review_package.py verify` on the exact ZIP when the tools are available.

State validation planes separately: generator-selftested, interaction-tested, local-file confirmed, offline confirmed, and destination-confirmed. Do not say `tested` when only a working copy, source hash, ZIP creation, or static inspection was checked.

## 11B. Context-length defense

At the start of a new pass, read the last approved ZIP, `PROJECT_STATE.md`, and the newest raw comments file before older branches. Do not ask Joel to repeat a decision already recorded there. Recommend a fresh conversation after several substantial passes, whenever multiple files are mislabeled as final, or when revision branches are ambiguous. Context length is a risk factor; the package is the defense.

## 12. Delivery boundary

Article, manual, diff, helper, and review-interface HTML are file deliverables only. Never render or open them in chat. Multi-file review families are ZIP deliverables by default.


## 13. Worker-chat continuation boundary

A worker may handle successive closely related review and repair passes while the baseline and current candidate remain unambiguous. Do not build a handoff ZIP or force a fresh chat merely because the authoritative article, review state, comment ledger, or derivative changed. Create a handoff only when Joel requests one, a materially separate outcome should move elsewhere, or context/branch ambiguity creates a real accuracy risk. Use a full ZIP when the substantial review family is itself the requested delivery; otherwise a compact current-file-plus-`CONTINUATION.md` handoff may suffice. Immediate repair remains in the same worker. See `WORKER-CHAT-HANDOFF-RULES.md`.

## 14. External developmental advice is evidence, not authority

For substantial whole-article review, separate the developmental reviewer from the controlled implementer. The reviewer diagnoses promise, destination, stakes, pacing, hierarchy, distinctiveness, credibility timing, recurrence, section autonomy, appendix division, and ending without rewriting. Record the recommendation, underlying concern, Joel's acceptance/rejection/qualification, corrected purpose or judgment, and analogous advice affected.

A rejected operation may still reveal a real problem. Preserve the diagnosis while discarding the wrong solution. Before implementation, test every accepted recommendation against the operational article-purpose statement. Implement through the smallest authorized move, trim, pointer, hierarchy repair, or connective sentence. Then inspect the complete article independently before detector testing.

When a claim is firm but the evidence is badly timed, classify the change as `Point and move`; do not rewrite conviction into uncertainty. When recurrence supports section autonomy for skimmers, retain the smallest local orientation and point to the full proof.
