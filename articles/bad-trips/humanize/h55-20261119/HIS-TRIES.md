# His round-40 tries on Chest Pain's evidence paragraph (exported 2026-11-19 00:52 UTC), read back from his history

Each check read from his Pangram history (web.pangram.com's API, in the desktop app's browser pane, 2026-11-19), in the
order his comment gives them, with what changed. My version on the card was cp-c4's line of tries (round 40,
`../../review/r40/REVIEW-R40.md`); his first check starts from my sentences with his second sentence reworded.

| Check | What changed | Read |
|---|---|---|
| [bba48851](https://www.pangram.com/history/bba48851-f3b5-4124-8f57-d4620703bb06) | his second sentence: "When they gave DMSO to rats ..., those rats lost about three quarters less heart muscle than the rats who didn't get DMSO, though that study didn't try giving it after the attack had started" | AI Detected, 99.6% (AI-Generated Low 94) |
| [6e5f6c98](https://www.pangram.com/history/6e5f6c98-f9fe-4ab0-b021-bcaab17f8e6d) | "had started" made "started" | AI Assisted, 50% (AI-Assisted Low 93) |
| [fa73d444](https://www.pangram.com/history/fa73d444-fe86-48a6-91a9-46a6761dfd65) | "gave DMSO" made "gave it" (DMSO no longer in three sentences in a row) | AI Generated, 100% (Low 15, Medium 42, Low 36) |
| [78ac0487](https://www.pangram.com/history/78ac0487-88fb-4d18-868f-42a848bc3e54) | "So far" moved first | AI Generated, 100% (Medium 57, Low 36) |
| [e8688033](https://www.pangram.com/history/e8688033-21f1-4b0c-bc76-bdae42a7bdfd) | "and only as a prophylactic (preventative treatment)" in the first sentence; the "though that study didn't try ..." clause gone | Human Written, Human High 88 (one window) |
| [fc846803](https://www.pangram.com/history/fc846803-fedb-47b8-a3d2-01dfb087df4f) | only that change made to my version: "The heart research on DMSO has only been in animals and lab dishes so far, as a preventative treatment." | Human Written: High 19, Medium 30, Low 36 |

His last check is his version, word for word as the page's box and database hold it: in the guide (`../../review/r40/apply_r40.py`).
What it teaches is lesson bad-trips-2026-11-19a (`docs/lessons/2026-11-19-0052-bad-trips.md`): the limit that decides
whether the findings bear on the reader's case goes in the first sentence; and the linter's O75 (past perfect) and O76 (one
abbreviation in three sentences in a row).
