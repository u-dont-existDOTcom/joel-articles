# Episode 008 — parallel R17 role correction

Date: 2026-09-17
Status: **OWNER CORRECTION / WORKFLOW ROLE BOUNDARY**

## Owner correction

R17 generation/execution belongs to a separate parallel ChatGPT conversation. A supervising conversation that reads the same GitHub branch must not claim that it is the R17 worker, that it ran R17, or that it owns R17 execution merely because R17 artifacts are visible in canonical GitHub state.

## Operational rule

- Treat R17 outputs as external parallel-chat artifacts once they are durably persisted to GitHub.
- Do not issue duplicate instructions to run R17 from another supervising chat.
- Do not describe a supervisor as having generated or executed R17 unless that conversation actually did so.
- A supervisor may read and audit persisted R17 artifacts after they exist, but must keep provenance explicit.
- Shared branch state does not imply shared conversational identity or execution ownership.

This correction is about workflow provenance only. It does not alter the current article prose, preservation contract, or detector evidence.