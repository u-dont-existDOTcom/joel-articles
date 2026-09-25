# Episode 008 — correction: detector feedback must remain inside the convergence loop

Date: 2026-09-18
Status: **OWNER PROCESS CORRECTION / STALE OWNER-VISUAL GATE REMOVED / GUI FEEDBACK RESTORED**

## Trigger

Joel asked why the assistant kept talking about Pangram instead of using it after he had already:
- supplied detector screenshots;
- explicitly authorized/preferred the cheaper GUI path for future tests;
- suggested Remote Desktop as a practical route;
- explained that API balance was low.

## Causal failure

The active plan still carried a stale checkpoint:

`model repair -> owner visual judgment -> Pangram`

That checkpoint came from the earlier no-detector-before-admissibility phase.

After the owner explicitly authorized the GUI path and the campaign entered detector-guided Phase B, the owner-visual checkpoint no longer changed whether a GUI localization/retest should occur.

This was a **phase/gate carry-through failure**:
the workflow advanced, but the old gate remained active.

It was not a missing permission problem.

## Repair

For the current Phase-B convergence loop:

`localized red-region repair -> preservation check -> basic negative blocker -> GUI Pangram -> use result -> repeat`

Owner visual judgment remains higher editorial authority, but it is not a mandatory precondition for every cheap GUI detector measurement once:
- the candidate is preservation-clean;
- exact identity is frozen;
- detector evidence can change the next edit.

## Execution evidence

After this correction Chat used Remote Desktop Commander directly on Joel's laptop.

The first attempt exposed a dirty/diverged historical local Pangram branch. No paid submission occurred.

Chat then:
- created a clean dedicated Pangram evidence branch/worktree;
- reused the dedicated authenticated Pangram browser profile;
- used local Playwright GUI transport in headless browser mode;
- did not use the API.

Results:
- Candidate F: AI 0.5329530835 / Human 0.4670468867;
- Candidate G: AI 0.4243027866 / Human 0.5756971836;
- Candidate H: AI 0.0 / Human 1.0.

This is direct evidence that restoring detector feedback inside the localized convergence loop materially advanced the owner outcome.

## Durable rule

Do not retain an owner-review gate merely because it existed in an earlier phase.

At every phase transition, re-check whether each gate still changes the next decision.

When Joel has already authorized the same low-cost detector route for the same purpose, do not repeatedly stop to ask or talk about using it. Execute it and report the result.