# Turn 54 (h62): his answers to C1 to C4, checked and in

His message, 2026-11-20 22:40 UTC: "C1 a C2a C3 a C4 a / short tags on headings could be good / best systema breathing vid i
have seen so far: https://www.youtube.com/shorts/Nar2-nvomAk / i'm also wondering if we should create or adopt some system
for my whole substack ...".

## The checks (batch h62a, Pangram web app, his account, in the desktop app's browser pane)

| Test | What | Read | Windows | Link |
|---|---|---|---|---|
| c1-ss-steps-1 | the serotonin steps (B136) with C1 a: "Call emergency help and arrange transport." | AI Generated, 100% | AI High 326 | [2d3e8386](https://www.pangram.com/history/2d3e8386-31e3-45f8-8968-f875710a2470) |
| c2-lock-1 | the lock line with C2 a, beside his list of don'ts (B317, B318) | Human Written, 0% | Human High 106 | [a09a7d77](https://www.pangram.com/history/a09a7d77-b413-4ef0-afd2-0ee11b5cad90) |
| c3-ozone-1 | the ozone story (B197) with C3 a: "The mistake suggested that ..." | AI Detected, 26.7% | Human Medium 17, Human Low 21, Human Low 6, AI Low 15 (the last line) | [4cf06939](https://www.pangram.com/history/4cf06939-0a68-4076-b07b-27a892b3e8f0) |
| c4-humic-1 | My Brain Feels Damaged's protocol (B144) with C4 a: "Smell humic acid; ..." | AI Generated, 100% | AI Medium 2 ("DMSO immediately."), AI High 113 | [ebd3cfe6](https://www.pangram.com/history/ebd3cfe6-ee48-40b1-852c-46b37fdc60dc) |

Predictions ([predict.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/humanize/h62-20261120/predict.py)): c1, c3 and c4 AI, right; c2 AI at 0.40, a miss (explained in the ledger: the 12-word line read
inside his list's Human High window; the old 9-word line had read AI Low by itself between the AI High opening paragraph
and his list, h59 a09).

## What went in ([apply_c.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/humanize/h62-20261120/apply_c.py))

- **C1:** step 3 of the serotonin steps is "Call emergency help and arrange transport." ("for moderate or severe signs"
  out), so it agrees with his "So if you see any of these patterns, call medics." Words out, none added: in whatever the
  steps read. They read AI High by themselves, as the whole section did in h42; this is the steps' first check by
  themselves, the baseline for their own humanizing, with the three fresh reads of them kept ([reads/need-c1-ss-steps-1.txt](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/humanize/h62-20261120/reads/need-c1-ss-steps-1.txt),
  [reads/his-c1-ss-steps-1.txt](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/humanize/h62-20261120/reads/his-c1-ss-steps-1.txt), [reads/fit-c1-ss-steps-1.txt](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/humanize/h62-20261120/reads/fit-c1-ss-steps-1.txt):
  cyproheptadine is prescription-only and the line doesn't say what to do without it; akathisia and rhabdomyolysis
  unexplained; "DMSO is also not part of this branch" reads like an editor's note; the magnesium chloride line reads as a
  step to do first; the hospital list and the evidence history are lines the reader can lose).
- **C2:** "Put yourself on an action lock: nothing life-changing for 24–72 hours." (Human High 106 with his list; the apply
  gate passed). His answer's words were "nothing big until you've slept and eaten, and nothing life-changing for 24–72
  hours"; the read against his fixes marked the two limits packed in one line and his list after it restating the first
  ("Until you have slept and eaten, maybe don't ..."), so the line keeps the longer clock and his list the shorter, each
  said once, as his answer meant.
- **C3:** "The mistake suggested that DMSO and aged ozonated-charcoal water address different kinds of overload." The
  story reads below High by itself: its last line AI Low, the middle Human Low. All three reads found the last line gives
  the reader nothing to act on ("different kinds of overload" never says which). The paragraph is now on the list of units
  below High; its next try ends the line on what to do (when one doesn't help, try the other), the use its receipt names.
- **C4:** "DMSO immediately. Smell humic acid; if that doesn't help, take a 5mg lick of it." The smell still comes before
  the lick, his round-6 rule ("smell it first for sure, that's like an allergy test"); OWNER-EDITS q1-smell-first is
  superseded by c4-humic-no-first. The protocol reads AI as before (h57 a01): it stays on the list.
- **The Systema video:** "a video" in his Systema breathing line links https://www.youtube.com/shorts/Nar2-nvomAk ("Linear &
  Circular Breathing", Systema Vasiliev). A link, no words changed.

Checks after: owner edits 117 pass (3 waiting, as before); keep-as-is 23 kept, 12 meant cuts, none gone or back; fidelity
PASS (the keys of round 44, with the lock line's "24–72 hours" recorded as his change); the contradictions check `--done` PASS
(14 items: answered 5, explained 6, not a conflict 3). The guide: 13,747 words.

## The receipts

C2 and C3 add words of mine, so each had the three fresh reads and a receipt ([fill_receipts.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/humanize/h62-20261120/fill_receipts.py); both receipts pass). C1 and C4 only take words out, so they were
checked as they will stand (`--unchanged`).
