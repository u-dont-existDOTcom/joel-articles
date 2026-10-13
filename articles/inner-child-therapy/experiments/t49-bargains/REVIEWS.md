# Turn 49: Untangling the Belonging Bargains, the rest of it (2026-10-12)

Joel's message of 17:36 UTC: his P1 with the political tribe's "which expects consistent positions and predictable reactions" put back ("never take out something important in order to pass pangram. give your best *faithful* version to me, i'll show you exactly how to fix it without doing that"), the pace ("you only did one paragraph in nearly 2 hours?"), and "continue". Lessons E168 (faithful first) and E169 (a section at a time).

Targets: `../../tools/targets/t49-g2.json` (P2) and `t49-g3.json` (P3), then `t49-g4.json` to `t49-g10.json`, the h3 Four Pairs That Commonly Hook the Child. Fresh subagents, each reading one prompt file and nothing else: Opus for the dedup, writers, cold reads, groundings and stance checks, Sonnet for march reads.

## Joel's P1

As he wrote it, apostrophes included. His own check: 100% Human (106), AI likelihood 0.107 (17:33 UTC, id 15747587). The h2 with it 100% Human (110), the h1 (800). Cold read all OK; march S S B S S.

## The h3's dedup

Pema's map is new; the child panicking over good things that might disappear is partly said (belonging, romance). The questions are partly said for other situations; "preserve a high" is new. The aim, differentiation inside a family or faith, and the ordinary-life signs are mostly partly said, as problems rather than signs; selective belonging, agreeing now and disagreeing later, returning on different terms, permanent leaving and telling the difference are new; the credit to Key is new. Overlaps to say once: leaving rather than disappearing; staying inside while staying yourself; the list of good things; approval as survival.

## What went in

| | Draft | Reviews | Pangram alone |
|---|---|---|---|
| P2, the human doer | writer 1 of three, as written | all clean; march S S S B S | 100% Human (107), 0.042 |
| P3, gifts become bargains | writer 3 of three, with the stance check's conflict out ("(and when you're small, it more or less is)") and the cold read's "resonance with what?" answered | all clean | **100% AI (103), 0.557**; two versions with no claim changed, 0.588 and 0.605. In as the faithful version, question 17 |
| Four Pairs P1, Pema's map | writer 1 of two, as written | all clean; march S S S S B | 100% Human (87), 0.001 |
| P2, the questions | writer 1's list; a grounding of writer 2's lead-in set the questions at the peak of upset, so "once you've caught your breath" | all clean | **guide's wording 0.961, reworded 0.804, as prose 0.997** (all AI). In as the faithful version (0.804), question 18 |
| P3, the aim | my rewrite: both writers' drafts failed the linter's coach register | all clean; march S S B | 100% Human (55), 0.393 |
| P4, differentiation inside | writer 1 of two, with writer 2's "If a parent used to go quiet and hurt…" (two march reads of writer 1's alone disagreed) | all clean | 100% Human (128), 0.284 |
| P5, the ordinary-life signs | rewritten as signs ("Noticing…", "Caring…"), since "You can…" five times failed the coach register; then "Their reasons can still change your mind" (stance check) and the last sign without the love it took for granted or what P4 says (groundings) | clean on the third round | 100% Human (98), 0.399 |
| P6, slow and lifelong | writer 2's, after three rounds: the tests it added (a few visits, the drive home, "Can they hear you disagree?") and "you aren't punishing anyone" out, each flagged by a grounding or a stance check; "a family, group or relationship" (stance check); "turns out to be permanent" (cold read) | clean on the fourth round | 100% Human (77), 0.329 |
| P7, Key's credit | the guide's line | grounding: ASK AUTHOR, it says what someone in his life did | not checked; question 19 |

The h3, the h2 and the h1 aren't checked with these: P3 and the questions fail alone, and a section with a paragraph that fails alone doesn't count (2026-10-01).

Predictions this turn: 8 of 14 (missed: P3 three times, the questions three times; Joel's own check of his P1 isn't counted). Installed byte-equal to the checked texts (`../../tools/pangram-runs/2026-10-12-turn49-a.json`). Gate records for every call: `GATE.json`.

## Process changes

- `pangram_gate.py` needs each draft's "missing" list; a draft that leaves a point out goes only as a probe (E168). Tests: `PangramBatchNeedsTheGate`.
- The writer prompts say to carry every point and go over the length rather than drop one, and not to add tests, verdicts or reassurances the brief doesn't give; tickets never cut a guide point.
- The march read splits a list's lead-in and items into sentences (`march_paragraphs`; test `MarchSplitsLists`): before, a lead-in and four questions read as one sentence.
