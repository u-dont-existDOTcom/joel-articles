# Worker-Chat Outcome and Handoff Rules

## Governing rule

A worker chat may handle a sequence of closely related passes while the context, baseline, and current authoritative artifact remain clear. Completing a pass or changing authoritative state does **not** by itself require a new conversation or a handoff package. Conversation length and state changes are risk signals, not automatic triggers.

## Stay in the current worker by default

Continue in the same chat for iterative editing, testing, author-intent interviews, detector localization, immediate repairs, and closely related follow-ups when:

- the work concerns the same article, artifact family, or defined outcome;
- the active baseline and current candidate are unambiguous;
- no competing revision branch has appeared;
- Joel has not requested a handoff or fresh chat;
- the remaining context is still reliable enough to work accurately.

Do not generate a handoff ZIP merely because a candidate changed, a pass completed, or another turn began.

## When a handoff is warranted

Create a handoff only when one of these applies:

- Joel explicitly asks to hand off, start a fresh worker, pause with a checkpoint, or continue elsewhere;
- a new outcome is materially separate from the current one and carrying it in the same worker would create branch confusion;
- context length, conflicting baselines, mislabeled artifacts, or revision ambiguity creates a material accuracy risk;
- a substantial multi-file artifact family is already being delivered as a ZIP and Joel also wants the next worker prepared.

Before forcing a fresh conversation because of context risk, state the reason. Continue in the current worker when Joel prefers that and the state can still be kept reliable.

## Use the least burdensome handoff format

Choose the smallest format that preserves the actual state:

1. **No handoff:** continue in the same worker and deliver only the requested artifact or answer.
2. **Compact handoff:** for a simple project, provide the current authoritative file plus a short `CONTINUATION.md`, or a concise text handoff when there is no file artifact.
3. **Full handoff ZIP:** use for a complex multi-file family, an annotated review package, a publication artifact family, or when Joel explicitly requests a self-contained archive.

A single-file project does not need to be wrapped in a ZIP solely for continuity. Accumulate related intermediate changes and create one cumulative handoff only when an actual transfer occurs.

## Intermediate-pass delivery

For related passes that remain in the same worker:

- deliver the requested current artifact or changed files only;
- update `PROJECT_STATE.md` when the project genuinely needs persistent revision authority;
- do not create manifests, checksums, browser-test reports, or package scaffolding solely to satisfy a handoff ritual;
- still run any validation required by the artifact itself, especially final review interfaces, transfer helpers, or publication files;
- do not repeat a full package build after a small repair unless the repaired package itself is the requested deliverable.

A substantial annotated review or multi-file publication family may still require one ZIP as its **delivery format**. That requirement does not automatically end the conversation or force the next pass into a fresh worker.

## Immediate-repair rule

Repair of the just-delivered artifact stays in the existing worker. This includes a missing image, broken export, clipped slider, omitted comment, wrong link, failed helper, packaging defect, or local correction attributable to that delivery.

After repair, replace the defective deliverable in the least burdensome valid form. Rebuild the whole family only when the changed member affects the family or when the family ZIP is the authoritative requested deliverable.

## Handoff minimum

When an actual handoff occurs, record only what the next worker needs. A full handoff also includes the current section-provenance ledger, cumulative omission audit, and assistant-produced/owner-accepted recheck queue:

- exact authoritative filename and revision ID;
- approval state;
- superseded artifact, when relevant;
- unresolved issues and locked decisions;
- substantive claim changes or `none`;
- tests completed and tests still pending;
- largest remaining weakness and the next defined outcome.

Add SHA-256 values when they materially prevent confusion or are already part of the artifact workflow. Do not calculate them merely as ceremony for a simple continuation.

A handoff's `NEXT_SECTION_SOURCE` is a routing aid. The receiving worker must reconcile it with the complete authoritative source and neighboring headings before making omission, consolidation, or completion claims. It must also locate the next section independently before asking Joel to resend material already available.

## Authority rule

The latest authoritative artifact and recorded decisions control. A full ZIP is strongest when the state is complex, but it is not mandatory for every pass. A compact handoff may carry simple state, and the same worker may continue without any handoff while the project remains unambiguous.
