# Where the r4 guide's additions came from (turn 36, 2026-10-08)

Joel, 2026-10-08 02:23 UTC, on depth draft 1: "i assume it's supposed to represent some new part of the therapy map. who is gonna be "sneaking reparenting in " thru some gentler version? we have no idea where this came from? maybe we should somehow implement a rule that guide additions can't be suggested by other owrkers unless they are explained, what map change caused them, and how they are really needed vs superfluous to the guide."

This traces each waiting paragraph to the change that put it in the guide, from innerSignalGraph's own history (`git log`, its plan for the change, and its state record). A read-only clone was enough; nothing was changed there.

## How the r4 guide got its new paragraphs

This lane's `source/inner-child-guide-2026-10-04-r4.txt` is innerSignalGraph's `guides/inner-child-guide-2026-10-04-r4.txt`. Its paragraphs that aren't in the article's original guide (`master.html`) came in through four pull requests there:

| Pull request | Merged (UTC) | What it was for, in its own record | What it added to the guide | On the public-guide queue? |
|---|---|---|---|---|
| #124, "Sync Oct 3 Inner Child guide and harden certainty routing" | 2026-10-04 00:08 | It synced the Oct 3 guide versions, which have Substack captures. | Experience vs. interpretation, social practice as a test, honesty and earned trust, anxiety as a guess, and others. | Yes: bundle A, PGQ-001 to 007. |
| #126, "Refine InnerSignal continuity scaffolding" | 2026-10-04 03:45 | "Repair the routing failure exposed by a new-client test without committing private client facts." Its plan: "Create a new canonical guide text version derived from the current 2026-10-03 r3 text with minimal additions." | The depth and pause paragraphs, the pleasantness paragraphs, the isolation and community paragraphs, and the difficult-dream paragraph. | **No.** |
| #128, "Add positive-direction, listening-mode, and role-integrity guidance" | 2026-10-04 06:00 | "Make InnerSignal understandable even when the client has not read the guide", and the owner's practice of using missing someone as a cue to send love. | Missing as a cue for love, concentrated borrowed adulthood, support mode, Speak Toward What You Are Building. | Yes: bundle B, PGQ-008 to 011. |
| #130, "Route successful inner-child practice into ordinary-life transfer" | 2026-10-05 03:23 | Practice-to-life transfer. It also created the queue. | The queue's own suggested text for PGQ-012 and 013. | Yes: bundle C. |

Bundle D (PGQ-014 to 017) came from the Oct 5 and 6 changes to blocked action, support-mode continuity, memory support and practical focus.

## The #126 paragraphs are the app's rules, written as prose

#126 fixed the app. It added owner amendments AMEND.IC.CONTINUITY_TITRATION, AMEND.IC.SCAFFOLDED_CHALLENGE and AMEND.IC.COMMUNITY_REPARENTING, new map nodes, new state fields, and then the same rules as guide text. Its state record shows the match:

- **Saying no to inner-child work.**
  - App: "Decline is a deterministic planner boundary: non-safety `IC.*` nodes are removed, with no step-down ladder, reactivation condition, repeated re-offer, or reparenting relabeling."
  - Guide: "do not keep trying to sneak it back in through “gentler” exercises or by renaming ordinary tasks as reparenting."
  - The one who would sneak it back in is the app. That's why the sentence makes no sense to a reader.
- **The pause.**
  - App: the fields `ic_last_tolerated_level` and `ic_reactivation_ready`, and "re-entry requires current agreement and starts at or below the last tolerated level".
  - Guide: "make the pause specific: what made it necessary, what level was last genuinely workable, and what observable change—plus your own agreement—would make a gentle return reasonable."
- **Whether a session was too much.**
  - App: "Workable challenge requires intact orientation/stopping/return, willingness, a non-aversive appraisal, and recovery/functioning without meaningful deterioration."
  - Guide: "Ask four things: could you stop and return, do you actually want to go back toward it, did it feel difficult-but-workable rather than simply too much or unwanted, and how did you recover afterward in sleep and ordinary functioning?"
- **Community support.**
  - App: the route "includes the app in the single-point-dependency warning".
  - Guide: "…or this app the only place you can belong."

innerSignalGraph's own contract (`docs/PUBLIC-GUIDE-HUMANIZATION.md`) already covers this case:

- The queue is the handoff for reader-facing changes, and "Runtime-only mechanics do not require a public-guide entry."
- A humanizer may omit "runtime-only mechanics such as task-state bookkeeping, capability gates, persistence contracts, internal routing metadata, or approval machinery".
- When #130 made the queue the next day, it gathered "all currently pending Inner Child public-guide semantic changes" and left #126's paragraphs out.

**My error (E155).** In turn 30 I treated every r4 paragraph the queue didn't list as if it were queued ("I told Joel I'd treat them like queue items unless he says otherwise"). That is how the app's rules got drafted for the article. His OK at 01:09 ("if it has new stuff add that") rested on my description of them as new guide material.

## Status

| Paragraph | Where it came from | Status |
|---|---|---|
| Depth 1 ("That means turning the depth down…") | #126, CONTINUITY_TITRATION | **cut** (Joel, 02:23) |
| Depth 2 ("If you do want the relationship but a particular depth is too much…") | #126, CONTINUITY_TITRATION | parked |
| Depth 3 ("A complete tolerance pause is a last resort…") | #126, CONTINUITY_TITRATION | parked |
| Pleasantness 1 to 3 ("Do not use pleasantness…", "If those answers are not known yet…", "Dreams and imagery…") | #126, SCAFFOLDED_CHALLENGE | parked |
| Isolation 1 and 2 ("If isolation itself…", "Look for more than one door…", "Use the Protector here too…") | #126, COMMUNITY_REPARENTING | parked |
| The difficult-dream paragraph (When the Practice Feels Real but Stays Shallow) | #126 | parked |
| C2 ("Honesty does not mean total disclosure…") | #124, from the Oct 3 guide; queue item PGQ-003 | waiting: it passes alone (130); it could follow Joel's C1 |

"Parked" means that nothing is drafted, checked or proposed from it unless someone explains why the article's reader needs it, which is Joel's rule. The drafts and their records stay in the lane, so nothing is lost.

If Joel wants any of them back, here's my read. It isn't a proposal to draft them. Two ideas there aren't in the article and might help a reader:

- judging a hard session by the next few days, not by how pleasant it felt;
- having more than one place to belong.

The rest is the app's bookkeeping: handling a no, recording a pause, coming back.

## The rule, and where it lives

Joel's rule: guide additions aren't suggested unless they're explained: what map change caused them, and why they're really needed rather than superfluous.

- **In this lane (in force now).**
  - `reviewer.py draft` and `reviewer.py dedup` stop on any guide passage with sentences that aren't in the article's original guide, unless the target carries `"provenance"` with `"map_change"` and `"why_reader_needs_it"`. Tests cover both cases.
  - The gate (step 1) says the same, and adds that a guide change that isn't on the upstream queue is runtime-only by default.
- **For the workers who write guide additions (innerSignalGraph).** The proposed wording is in `docs/proposals/INNERSIGNALGRAPH-GUIDE-ADDITIONS-RULE-20261008.md`. Filing it there needs Joel's OK: this session couldn't get write access to innerSignalGraph or universal-dev-architecture without it.
