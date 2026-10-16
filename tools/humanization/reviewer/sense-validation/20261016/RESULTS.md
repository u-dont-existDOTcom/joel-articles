# The cold read's opener rule: validation of 2026-10-16

Why: Joel, 2026-10-16 18:22 UTC, on section 13's "From Visitor to Member—Slowly", where a paragraph opened with my "How do you know?" right after a paragraph of questions to write down: "i would cut the first sentence "How do you know?" ... why did the reviewer not cut that, what's that? know what? doesn't seem to follow...". Four cold reads in three rounds had paused there and settled it from the next sentence, which the prompt then told them was not a break. `../../sense_section.txt` now has a rule for a paragraph's first sentence and a "Paused:" line that `../../../pause_tally.py` counts across rounds.

The rule had two wordings. The first: a paragraph's first sentence has to follow from what comes before it; when it asks or answers something the paragraph before doesn't set up, give it its line, even when the next sentence lets you work it out. The refined one adds: "A first sentence that picks up something from a paragraph or two back, or that turns against what came just before (with a "though" or a "but"), follows, even when the link is in other words." Fresh Sonnet readers, one per prompt, nothing else in their context.

| read | text | wording | what it had to do | what it did |
|---|---|---|---|---|
| V1 | section 13 v22, which has "How do you know?" (P20) | first | flag P20 | flagged P20 ("know what? ... P19 only lists terms to write down") |
| V2 | section 13 v22 | first | flag P20 | flagged P20 |
| V3 | section 13 v22 | refined | flag P20 | flagged P20 |
| H1 | section 12 with a planted opener, "How much is enough?" (P13, `s12-planted.md`) | first | flag P13 | flagged P13 |
| H2 | the same | refined | flag P13 | flagged P13 |
| C1 | Joel's own section 11, two of whose openers pick up an earlier paragraph or turn with "though" | first | flag nothing | flagged two of his openers (P9 "Remember, it's not an override unless ...", P16 "Friends who come to visit don't get written terms, though.") |
| C2 | the same | refined | flag nothing | flagged nothing |

Result: the refined wording found the target and the planted opener and flagged none of Joel's openers (3 of 3); the first wording found both but flagged two of his (3 of 4 reads right, one with two false flags). `sense_section.txt` has the refined wording.

The "Paused:" lines of these reads, with the cold reads of rounds r1 to r16, are what `pause_tally.py` counts. Two sweeps of the article's other sections with the refined rule (`articles/intentional-communities/candidate/sweep-20261016/`, prompts G1 for sections 1 to 6 and G2 for the rest) found no opener that doesn't follow.
