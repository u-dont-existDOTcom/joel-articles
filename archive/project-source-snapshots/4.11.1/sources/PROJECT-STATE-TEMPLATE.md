# Project State Template — Canonical Revision and Review State

Use one `PROJECT_STATE.md` for every active article-revision project. The last user-approved article plus this file are the authority for current state. Chat history may supply context, but it does not establish which artifact is canonical, which comments remain open, or which review features were delivered.

Update this file after every substantive pass, correction, approval, package build, or monitoring-status change. Preserve prior revision records in the changelog rather than overwriting history.

## Project identity

- **Project ID:**
- **Article title:**
- **Author/byline:** Joel Rosenblum
- **Primary task mode:** P0 / P1 / P2 / P2S / P3 / P4
- **Audience contract file or summary:**
- **Active source packet:**
- **State updated UTC:**

## Revision authority

- **Current revision ID:** `rNN-candidate` / `rNN-approved`
- **Current status:** drafting / candidate / approved / superseded / reconstructed
- **Canonical current article filename:**
- **Canonical current article SHA-256:**
- **Last user-approved revision ID:**
- **Last user-approved article filename:**
- **Last user-approved article SHA-256:**
- **Exact baseline for the current review:**
- **Baseline SHA-256:**
- **Previous delivered revision, if different:**
- **Supersedes:**
- **Reconstruction disclosure, if applicable:** none / reconstructed from specified sources because the original was unavailable

Never use `final` as a rolling filename. A candidate becomes `rNN-approved` only after Joel approves it. A conversation title, renamed chat, remembered filename, or phrase such as “the latest final” has no evidentiary value.

## Source boundary and access

- **Exact source span reviewed:**
- **Preceding heading:**
- **Following heading:**
- **Source completeness:** complete / excerpt-only / scan-PDF-only / unknown
- **Research access levels:** full text / abstract / snippet / secondhand / not applicable
- **Unreconciled neighboring material:**
- **Scope of preservation/omission claims:** global / section / supplied block only

## Section provenance and later recheck

- **Section-provenance ledger filename:**
- **Owner-authored untouched:**
- **Owner-edited final:**
- **Assistant-produced owner-accepted:**
- **Owner-final available only in scan/PDF:**
- **Superseded assistant candidates:**
- **Assistant-produced recheck queue filename/count:**
- **Cumulative omission audit filename:**
- **Unresolved assistant-created omissions:**
- **Owner-deleted/resolved items:**

Owner approval, detector status, and authorship are separate. Assistant-produced/owner-accepted sections remain in the later publication recheck queue until reviewed in full context.

## Active comments and decisions

- **Raw source-comments filename:**
- **Raw source-comments SHA-256:**
- **Raw comment count:**
- **Comment-resolution ledger filename:**
- **Implemented:**
- **Partially implemented:**
- **Needs clarification:**
- **Not implemented with reason:**
- **Superseded/retracted:**
- **Open issue count accepted by Joel:** 0 / number + approval reference
- **Keep locks:**
- **Remove decisions awaiting dependency repair:**
- **Brainstorm requests awaiting options:**

The raw comments file is immutable. Reconciliation, classification, and resolution status belong in the separate comment-resolution ledger.

## Review-interface contract

- **Review artifact filename:**
- **Interface/export format:** `joel-commentable-diff-review-v4`
- **Generator version:**
- **Baseline type:** original-vs-current / previous-delivery-vs-corrected
- **Row scope:** changed-passages-only / all-passages
- **Source label and revision:**
- **Revised label and revision:**
- **Source SHA-256 embedded in review:**
- **Revised SHA-256 embedded in review:**
- **Required features present:** selected-text comments; whole-cell comments; Keep; Remove; Brainstorm; reasoning; Humor; Technical detail; Length; Bluntness; Copy JSON; Copy Markdown; Export JSON; Export Markdown; local persistence; search; changed-only filtering
- **Last generator selftest:**
- **Last browser interaction test:**
- **Local-file/offline test:**
- **Known destination-specific limitation:**

## Locked links, media, and related assets

- **Required links:**
- **Required external assets:**
- **Native-object inventory:**
- **Captions/anchors that must remain attached:**
- **Related artifact-family ledger:**
- **Owner-approved omissions:**

## Delivery state

- **Authoritative package filename:**
- **Package SHA-256:**
- **Package built UTC:**
- **Article member:**
- **Review member(s):**
- **Source comments member:**
- **Project-state member:**
- **Changelog member:**
- **README member:**
- **Checksums member:**
- **Optional members:** comment ledger / section-provenance ledger / omission audit / assistant-recheck queue / browser-test report / helper / transfer report / artifact-family ledger / other
- **Clean-unzip verification:** pass / fail / not run
- **Checksum verification:** pass / fail / not run
- **External dependency check for review file:** pass / fail / not run

Generated sandbox paths are temporary. Deliver the ZIP in the same working pass and ensure this state file and checksums make continuation possible in a new conversation.

## External monitoring status

Use only when Joel requests a watch, alert, or scheduled retrieval.

- **Source URL or thread:**
- **Retrieval from execution environment:** verified / failed / not tested
- **Baseline stable IDs or highest post number:**
- **Deduplication method:**
- **Schedule enabled:** yes / no
- **Successful dry run:** yes / no / not run
- **Notification channel enabled and confirmed:** yes / no
- **Operational status:** operational only when all four components above are verified; otherwise not operational
- **Last verified UTC:**
- **Failure/limitation:**

A runnable script does not prove network retrieval. A schedule does not prove notifications. Do not mark the watch operational when any component is missing.

## Article purpose and developmental architecture

- **Mystery/problem:**
- **Destination:**
- **Why the route is necessary:**
- **Payoff:**
- **Opening promise/stakes:**
- **Distinctive material that must arrive before generic theory:**
- **Highest credibility-cost claims and intended placement:**
- **Heading-tree / table-of-contents status:** accurate / repair pending
- **Section-autonomy status:** pass / repair pending
- **Intended ending function:**
- **Main-article / appendix division:**

### External developmental advice

| Advice ID | Recommendation | Underlying concern | Joel decision | Corrected purpose/judgment | Analogous advice affected | Implementation status |
|---|---|---|---|---|---|---|

## Current master, body access, and correction closure

- **Current master filename:**
- **Current master SHA-256:**
- **Master status:** propagated / pending reconstruction / stale / unavailable
- **Assembly-gap markers:** none / list
- **Authoritative section bodies missing:** none / list
- **Owner deletions verified absent:** yes / no
- **Correction register:** passing / open count
- **Provenance state complete:** yes / no
- **Detector state complete where required:** yes / no / not applicable
- **Source gaps:** none / list
- **Link gaps:** none / list

### Body access

| Artifact/section | reference known | partially retrieved | fully retrieved | installed | verified | exact location/hash | gap |
|---|---|---|---|---|---|---|---|

### Correction closure

| Correction ID | captured | classified | applied to master | verified in master | dependency audit complete | detector status determined | closed | blocker |
|---|---|---|---|---|---|---|---|---|

## Epistemic and quality gates

- **Four epistemic planes separated:** yes / no
- **Source support vs author inference:** pass / citation absorption found
- **Originality/lost-key falsifiability:** complete / not applicable / self-sealing risk
- **Abductive claims:** calibrated / proof inflation / not applicable
- **Point-and-move operations:** none / complete / incomplete
- **Experience-mechanism-ontology-universality-reader prediction:** separated / conflated
- **Quality floor:** fidelity pass; coherence no regression; editorial/article-function no regression; owner preference no regression when available
- **Detector role:** secondary diagnostic / improperly controlling

## Unresolved questions and next step

- **Unresolved questions:**
- **Largest remaining weakness:**
- **Best next step:**
- **Expected marginal gain:** small / moderate / large
- **Over-editing risk:** low / medium / high
- **Fresh-conversation recommendation:** no / yes + reason

## Worker-chat outcome

- **Distinct outcome or related pass sequence owned by this worker:**
- **Outcome complete:** yes / no
- **Authoritative state changed:** yes / no
- **Continue in current worker:** yes / no + reason
- **Immediate repair still belongs in this worker:** yes / no + defect
- **Handoff trigger:** not needed / Joel requested / materially separate outcome / branch ambiguity / context risk / checkpoint requested
- **Handoff format:** none / compact current-file-plus-`CONTINUATION.md` / full ZIP
- **Continuation handover member or location:**
- **Full validated ZIP produced:** yes / no / not required
- **Next section located independently:** yes / no / retrieval failed
- **Next source analysis or question set:**
- **Full-handoff provenance/omission/recheck files present:** yes / no / not applicable

A completed pass may remain in the current worker. Do not create a handoff package merely because authoritative state changed. When an actual transfer occurs, use the least burdensome format that makes the current state unambiguous.

## Continuation rule

Continue related passes in the current worker while the baseline, current artifact, and revision branch remain clear. Start a fresh worker when Joel requests it, when the next outcome is materially separate, or when branch/context ambiguity creates a real accuracy risk. At the start of a new worker, read the latest authoritative artifact, this state file when present, the newest raw comments file, and the compact or full handoff before older branches. A simple project may use the current file plus `CONTINUATION.md`; a complex multi-file family may use a full ZIP. Immediate repair stays in the worker that produced the delivery. Do not ask Joel to repeat a recorded decision.
