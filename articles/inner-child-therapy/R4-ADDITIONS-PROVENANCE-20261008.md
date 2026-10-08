# Where the r4 guide's additions came from (turn 36, 2026-10-08)

**Correction, turn 37 (Joel, 2026-10-08 03:57 UTC: "the guide updates were sent to you due to map changes which GPT believed should be reflected in the guide, because the guide and map are supposed to complement each other and agree with each other ... did you think none of that stuff needed saying in the guide even tho it needed to be in the map?").** The trace below stands, but two conclusions in it were wrong:
- I called the #126 paragraphs "the app's rules" and parked them all because they weren't on the queue. #126's plan made them guide text on purpose, so the guide would agree with the map; the queue missing them looks like an oversight (it has #128's additions from the same day).
- I wrote that a change not on the queue is "runtime-only by default".

What holds is narrower: a few lines in them are about the app's own behavior toward a client (not re-offering after a no, the pause bookkeeping, "this app"), and those stay in the AI guide. The rest is back on the list as teaching points T1 to T9 for Joel to tick (`docs/proposals/MAP-TO-GUIDE-ARCHITECTURE-20261008.md`, section 7). Lesson E156.

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

## The #126 paragraphs restate the map's new rules, partly from the app's side

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

**What went wrong in the drafting (E155, corrected by E156).** In turn 30 I drafted the r4 paragraphs whole, as written for the app's model, instead of first asking what a reader needs from each. That's how a line about the app's own behavior ("do not keep trying to sneak it back in") ended up in reader prose. In turn 36 I then over-corrected and treated "not on the queue" as "not for readers".

## Status

| Paragraph | Where it came from | Status |
|---|---|---|
| Depth 1 ("That means turning the depth down…") | #126, CONTINUITY_TITRATION | **cut** (Joel, 02:23) |
| Depth 2 ("If you do want the relationship but a particular depth is too much…") | #126, CONTINUITY_TITRATION | teaching points T1 to T3 (turn 37) |
| Depth 3 ("A complete tolerance pause is a last resort…") | #126, CONTINUITY_TITRATION | teaching points T1 to T3 (turn 37) |
| Pleasantness 1 to 3 ("Do not use pleasantness…", "If those answers are not known yet…", "Dreams and imagery…") | #126, SCAFFOLDED_CHALLENGE | teaching points T4 to T7 (turn 37) |
| Isolation 1 and 2 ("If isolation itself…", "Look for more than one door…", "Use the Protector here too…") | #126, COMMUNITY_REPARENTING | teaching points T8 and T9 (turn 37) |
| The difficult-dream paragraph (When the Practice Feels Real but Stays Shallow) | #126 | with T7, when that section comes up |
| C2 ("Honesty does not mean total disclosure…") | #124, from the Oct 3 guide; queue item PGQ-003 | waiting: it passes alone (130); it could follow Joel's C1 |

Turn 36 parked them; turn 37 brought them back as teaching points (see the correction at the top). The drafts and their records stay in the lane, so nothing is lost.

Turn 36's read, kept for the record. It's now part of the teaching points: two ideas there weren't in the article and might help a reader:

- judging a hard session by the next few days, not by how pleasant it felt;
- having more than one place to belong.

The rest is the app's bookkeeping: handling a no, recording a pause, coming back.

## The rule, and where it lives

Joel's rule: guide additions aren't suggested unless they're explained: what map change caused them, and why they're really needed rather than superfluous.

- **In this lane (in force now).**
  - `reviewer.py draft` and `reviewer.py dedup` stop on any guide passage with sentences that aren't in the article's original guide, unless the target carries `"provenance"` with `"map_change"` and `"why_reader_needs_it"`. Tests cover both cases.
  - The gate (step 1) says the same. Turn 36 also had it treat an unqueued guide change as runtime-only; turn 37 withdrew that (E156): a reader need is written as a teaching point instead.
- **For the workers who write guide additions (innerSignalGraph).** Turn 36's proposal is superseded by `docs/proposals/MAP-TO-GUIDE-ARCHITECTURE-20261008.md` (teaching points on the queue for every map change). Filing it there needs Joel's OK: this session couldn't get write access to innerSignalGraph or universal-dev-architecture without it.
