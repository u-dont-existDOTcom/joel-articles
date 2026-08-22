# Somatic Therapies — Current State

Updated: 2026-08-22

## Goal

Humanize the owner-supplied Somatic Therapies Substack article while preserving its arguments, recommendations, links, native media, personal material, safety warnings, and evidence distinctions; use Pangram only as secondary localization evidence and never sacrifice fidelity to improve a detector result.

## Authority / Baseline

- Article id: `somatic-therapies`
- Status: `working`
- Registered working master: `articles/somatic-therapies/master.html`
- Revision: `r01-candidate`
- Master SHA-256: `1e7e94717f40e7a4de77974a896f600a1bf2769d9c1846cbe84275e136ff5202`
- Owner source baseline SHA-256: `0d7e03ccde3900277e7ee8e9a1f5aac3c4f780d5243396f9bb2a100ee57083f9`
- Reader-visible normalized SHA-256: `e79c3efe640dc87880e90aebaeae4eff0ad9a47cb11234a8a0144bd3eaa38677`
- Pangram-submitted reader-visible file SHA-256: `613c3514844097ee4bd31e227a4624bde37cca280e8a3a15b566c92a51b25c1e`
- Reader-visible word count: **3,412**
- Joel explicitly authorized public repository registration and public-by-default assigned work on 2026-08-22. This is working authority, not external publication approval.

## Completed

- P2S / D4 architecture-first reconstruction of the mostly AI-shaped source into r01.
- Three cold audits: AI-shape, unsupported-persona/fake-humanization, and fidelity/native-object integrity.
- 16/16 ordinary article links preserved as the same URL multiset.
- 8/8 native/editor objects preserved byte-for-byte in the same order.
- Complete required article authority family registered with exact hashes.
- Exact r01 Pangram 4 measurement: AI `0.9776151180`, Human `0.0223849081`, AI-assisted `0.0`.
- Pangram localized two High-confidence AI windows: indices `0–1529` and `2006–21309`, with only a short Human segment between them around the Professor Baby Sheep/head-shaving material.
- A 270-word natural-owner research-conversational control from Joel's cancer article returned Pangram 4 Human `1.0`, High confidence, so the Somatic failure is not explained by Pangram simply rejecting Joel's research-guide register.
- Intro audit reached its hard 6/6 section cap; every tested variant returned AI `1.0`. The lane is closed.
- Inner-child audit reached its hard 6/6 section cap; every tested variant returned AI `1.0`, including the exact owner-supplied source section. The lane is closed.
- Source-vs-r01 comparison found that the unchanged Professor Baby Sheep/play material overlaps r01's only Human region, while several regenerated sections diverged heavily from source. The production preference is therefore restoration/minimum-dose editing before fresh generation.
- Shaking Qigong r01 baseline has one paid reservation in the fixed-batch ledger for exact text SHA `0f21beb5d6c95c471a13d8b3ff2d373a4541cca61151043203c702286614a181`; no durable task-id/cache result exists.
- The first unsubmitted Shaking `r02-source-stack` failed the blocking preservation gate and is permanently rejected because it dropped supplied source obligations.
- A complete exact-owner-source Shaking diagnostic is frozen at `experiments/somatic-therapies-shaking-qigong-r02-original-source-20260822-a.json` and remains unsubmitted.
- The private Pangram executor was repaired to use lossless queued concurrency (`queue: max`).
- Read-only Pangram History recovery was added, then repaired to persist failures durably without detector submission.
- Exact Shaking recovery authenticated, inspected 10 web-History candidates, found no exact match, and made no detector submission.
- A known-success async API Somatic intro control was also absent from the same authenticated web-History surface. This proves that web-History absence is non-adjudicative for the current async API route. The Shaking reservation therefore remains counted and non-repeatable unless task-id/cache/ledger or another transport-appropriate exact record resolves it.
- The async-API/web-History boundary was promoted as a reusable Pangram safety lesson in `u-dont-existDOTcom/pangram-humanization-lab`.
- Job 1 Somatic Experiencing → trauma-sensitive/restorative yoga was tested with the earlier authorial-state-composition pilot. The preservation-proofed Test D improved live-thought continuity editorially, but both exact A/B boundaries returned Pangram AI `1.0`, High confidence. That pilot is closed negative after exactly two paid calls (`$0.10`).
- The existing Authorial Flow Graph 1.3.0-dev1 was connected to a private pre-detector review bridge that removes Pangram/Brave credentials and cannot auto-accept owner review.
- Job 1 representation inputs V2–V5 were registered as non-authoritative experimental artifacts with preservation proofs. V5 is the current exact input; its reader-visible Job 1 boundary remains owner-source text while non-output context resolves article-authority questions.
- Repeated live Authorial Flow runs exposed two reusable tooling defects rather than new article ambiguities:
  1. preservation-mode representation manufactured hypothetical owner questions about changing explicit source choices such as renaming/removing `Job 1`;
  2. after that was fixed, an explicit `None ... remaining repairs are machine-resolvable` response was still treated as an owner question because the field was nonempty.
- Tool defect 1 was fixed in the versioned Authorial Flow release by making the preservation default explicit in `represent.md` / `semantic_sanity.md` and adding regression tests. Substantive tool commit: `267a5ea5faf2a116cda374177109a350f8da789d`.
- A trusted private release-refresh envelope was added so the self-hosted runner executes only canonical versioned release-branch tips, never public PR code; it runs the full deterministic suite twice, regenerates root release metadata with the canonical builder, verifies a clean release ZIP, and pushes only `MANIFEST.json` / `SHA256SUMS.txt` after success.
- Tool defect 2 was fixed in the versioned release with representation-only normalization of explicit no-question sentinels plus an empty-string prompt contract and regressions that preserve real questions. Substantive tool commit: `18bb2354636698c863ab2b65775f74e21a884a47`.
- The release was resealed after both tooling repairs. The current release manifest is bound to substantive tool commit `18bb2354636698c863ab2b65775f74e21a884a47` and includes the owner-question normalization regression.

## Current checkpoint

`r01-candidate` remains the canonical working master. None of the detector probes, Authorial Flow representation inputs, or runtime outputs is article authority.

Three manual-generation lanes are closed as productive detector strategies:
1. intro conversational/owner-like paraphrase;
2. inner-child lived/direct/source-restoration paraphrase;
3. Job 1 authorial-state realization.

The earlier Job 1 result remains informative: changing thought route improved prose shape but did not move Pangram. Do not treat Pangram as a gradient and do not resume hand-generated synonym variants.

The Shaking reservation remains quarantined. The positive-control test established that authenticated web History cannot resolve current async API reservations, so absence there must never authorize a repeat.

The current reuse-first path remains Authorial Flow Graph, but the live work has shifted from article ambiguity to runtime validation. Runs through `-h` were pre-detector and produced no candidate; they exposed and drove the two tooling repairs above. No Pangram call was made by those reviews.

A new pre-detector review request, `somatic-job1-authorial-flow-pre-detector-20260822-i`, is durably queued in the trusted executor against:
- tool commit `18bb2354636698c863ab2b65775f74e21a884a47`;
- Joel Articles source commit `ccc0cd3545b8ad3480b19a702bf390ba1030a478`;
- V5 source SHA `85caf10bb4f973cf9130a05bf20f0fe74297a5ab467e566e327a9556ecec51f2`.

At this checkpoint the `-i` evidence branch has not yet appeared, so the immutable request has not reached evidence-branch creation. Do not duplicate or retrigger it.

## Remaining

- Read the exact `-i` pre-detector result once its evidence branch appears.
- If `candidate_available == true`, fetch the frozen candidate and run the blocking preservation proof against the exact V5 reader-visible owner-source boundary, then article architecture/paragraph-job/live-question, owner-lock, safety-function, certainty, and source-provenance audits. Do not run Pangram before those gates pass.
- If `-i` still reports a no-question owner interrupt, treat that as a tooling regression and repair the runtime; do not create V6/V7 article context merely to appease the model.
- If `-i` reports a genuine owner ambiguity, first resolve it from registered owner/source authority; ask Joel only if the ambiguity is genuinely irreducible.
- If `-i` reaches a machine failure/generation dead end, inspect its privacy-safe causal failure metadata and repair/reject the runtime path rather than hand-generating another pseudo-Joel variant.
- Only after a frozen candidate is editorially valid may a new Job 1 Pangram call be considered. The current Job 1 audit has used two paid calls; at most four additional section calls remain under the six-call cap, and every call must change the next decision.
- Never repeat the ambiguous Shaking r01 paid measurement.
- Never submit the fidelity-rejected Shaking `r02-source-stack`.
- After any accepted prose change, run article-wide semantic, architecture, fidelity, native-object, and link checks before changing the registered master.
- Claim-by-claim citation/health verification remains pending because it was not requested in this humanization pass.
- Owner-final review/publication export remains pending.

## Blockers / unresolved

- Registered r01 remains Pangram `AI Detected`, 97.76% AI fraction.
- Intro lane is closed at 6/6 with no passing candidate.
- Inner-child lane is closed at 6/6; even the exact original source section is 100% AI.
- Job 1 authorial-state A/B is closed negative at 2 calls; both variants were 100% AI.
- Shaking Qigong r01 has one irreducibly ambiguous paid reservation and must not be repeated.
- The post-repair Authorial Flow `-i` run has not yet produced an evidence branch/candidate.
- Authorial Flow Graph 1.3.0-dev1 remains a candidate editorial runtime rather than owner-accepted production authority despite the two verified tooling repairs.
- `r01-candidate` is not owner-final or published.
- Citation review remains pending.

## Evidence / artifacts

- `master.html` — registered working master and current raw-editor HTML authority
- `HUMANIZATION-REPORT.md` — reconstruction and preservation audit
- `SOURCE-EVIDENCE.json` — source/candidate provenance and exact baseline hashes
- `OWNER-LOCKS.json` — protected functions
- `ARCHITECTURE.md` — article-wide functional map
- `DETECTOR-EVIDENCE.json` — registered detector ledger
- `experiments/JOB1-AUTHORIAL-STATE-PILOT-20260822.md` — frozen Job 1 pilot design/control/test
- `experiments/JOB1-AUTHORIAL-STATE-PILOT-RESULTS-20260822.json` — closed negative A/B result
- `experiments/JOB1-AUTHORIAL-FLOW-INPUT-V5-20260822.md` — current bounded Authorial Flow input
- `experiments/JOB1-AUTHORIAL-FLOW-INPUT-V5-PRESERVATION-20260822.json` — V5 preservation proof
- Pangram fixed-batch evidence under `u-dont-existDOTcom/pangram-humanization-lab@automation/pangram-fixed-batch`
- Shaking read-only recovery evidence branch: `evidence/pangram-history-recovery/somatic-shaking-r01-20260822-b`
- Known-success async API web-History control branch: `evidence/pangram-history-recovery/somatic-intro-r08-api-control-20260822`
- Authorial Flow Graph release branch: `u-dont-existDOTcom/pangram-humanization-lab@install/authorial-flow-graph-v1-1.3.0-dev1`
- Authorial Flow diagnostics branch: `diagnostics/authorial-flow-graph-v1`
- Trusted executor: `u-dont-existDOTcom/pangram-private-executor`

## Next safe action

Do not write or measure another Somatic variant yet. Read the queued `somatic-job1-authorial-flow-pre-detector-20260822-i` result when it reaches its evidence branch. If it freezes a candidate, preservation/architecture-review that candidate before any Pangram submission; otherwise act on the exact owner/tool failure class without restarting the old manual rewrite loop.
