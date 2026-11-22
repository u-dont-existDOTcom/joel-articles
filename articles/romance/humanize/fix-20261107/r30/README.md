# r30: his Medium-page answers in the fixed version (2026-11-22)

His message of 2026-11-22 22:24 UTC and the page's export are saved word for word in
[MESSAGE-T4-20261122-2224.md](../../../review/teach-20261108/MESSAGE-T4-20261122-2224.md) and
[ANSWERS-T4.json](../../../review/teach-20261108/ANSWERS-T4.json) (rebuilt from his fields by `save_answers_t4.py`; a
fresh reader matched all 62 of his items against the page's database, field by field).

- [apply_t4.py](apply_t4.py) writes [HIS-T4.json](HIS-T4.json): his 59 revised cards as 56 changes (his merges fold
  M-77 into M-76, and M-286 and M-287 into his rewrite of "Romance Shouldn't Be Adjudicated"), four of them runs of
  paragraphs he rewrote whole ("Reverting to babyhood" 203 to 207, "Disconnect to connect" 218 to 220, "Romance
  Shouldn't Be Adjudicated" 282 to 290, and 76 with 77). The three rejected cards ("pangram bug": 264, 338, 405) change
  nothing. `../whole/build.py` lays HIS-T4.json over the checks' replacements, and `../whole/fixed_md.py` writes the
  whole fixed article as one file, [FIXED.md](../whole/FIXED.md) (and the article as it stood before his answers,
  [FIXED-R29.md](../whole/FIXED-R29.md)).
- Obvious slips fixed in his words, listed in HIS-T4.json's `slips`: "flight or flight" (108), "dow did you" (126), "to
  life me up" (285), "wan't" and "in there and then" (361), "Anyway, If" (327), a missing "not" and "the depth of your
  connection will deepen" (349), and a "don't" that turned 205's last sentence round ("I don't want to hold onto the
  actual reality of me being me": the live paragraph said "I don't want to leave the reality of me being me"). Two typos
  in the live post's own words outside his answers: "explained::" (2) and "By the the 17th century" (live 399).
- Links: "breathwork" goes to breathwork.u-dont-exist.com, as he asked (it redirects to his Vagal Blitz post); "Systema
  breathing" to the video he picked for every Systema mention (Systema Vasiliev, "Linear & Circular Breathing"); the
  live links of 220 and 223 kept. The Instagram reel he asked for at 149 (light_of_my_soul_22) is live on Instagram and
  sits after that paragraph as an EMBED note, for the live update.
- The word-for-sense read of his versions ([sense-his/](sense-his/)): all three planted errors found; its one other
  finding, the capital "If" in Two Pillars, stays (his own, kept again in his new version of the locked paragraph).
- The live post's copy of 2026-11-22: [../live-check/LIVE-POST-BLOCKS-20261122.jsonl](../live-check/LIVE-POST-BLOCKS-20261122.jsonl),
  every block of the post's API body (fetched with curl on his laptop, body SHA-256 a35d1883...), the 457 paragraphs
  matching LIVE-INDEX.txt's fingerprints.
