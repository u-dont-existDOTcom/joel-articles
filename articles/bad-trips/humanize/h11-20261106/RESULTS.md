# Checks of 2026-11-06 (turn 17): round 11 in, and what turns Psychological First Aid AI

His round-11 answers, 20:51 UTC (`../../review/r11/ANSWERS-R11-20261106-2051.json`): both cards approved. The section as
the guide had it after round 11 is byte for byte the text checked last turn as fix 1 (`../h10-20261106/PFA-SECTION-try1.txt`,
[AI Generated, 100%](https://www.pangram.com/history/d84fe208-0c91-4c8e-bd31-3ac86bc7c5e5)), so it wasn't checked again.

Pangram's web app on his account, through the Claude desktop app's browser pane; predictions in `../pangram-ledger.jsonl`
(#73 to #89), each made before its check.

| text | words | result | windows | link |
|---|---|---|---|---|
| first half, the room paragraph's list of problems cut, his fixes line after its reason (`PFA-FIRST-try2.txt`) | 219 | AI Generated, 100% | AI High 219 | [result](https://www.pangram.com/history/bcf517c6-a50b-4e08-9ff2-0b8f0c7cdbe6) |
| the same without the intro line (`PFA-FIRST-try2-nointro.txt`) | 192 | AI Generated, 100% | AI High 68, Medium 52, High 72 | [result](https://www.pangram.com/history/b51d4029-7276-4669-9b4f-b7683dfb8a44) |
| his dangers paragraph alone, as he checked it on 2026-11-05 (`DANGERS-his-r06.txt`) | 113 | Human Written | Human High 61, Medium 10, High 42 | [result](https://www.pangram.com/history/a23a444a-a38c-445e-b0a4-4b0143397966) |
| the heading and his dangers paragraph (`DANGERS-with-heading.txt`) | 120 | Human Written | Human High 120 | [result](https://www.pangram.com/history/2745e050-1573-4da8-9c6a-ba510f0a80e6) |
| first half, the room said as concrete acts after "Next, look around the room, because" (`PFA-FIRST-try3.txt`) | 235 | AI Generated, 100% | AI High 235 | [result](https://www.pangram.com/history/786c4de3-8fa4-45ff-bed8-3dff78695bf0) |
| the same without the intro line (`PFA-FIRST-try3-nointro.txt`) | 208 | AI Generated, 100% | AI High 208 | [result](https://www.pangram.com/history/5b107be0-f679-4c0c-b5b3-6fbbd178e898) |
| heading, his paragraph and only the room's reason sentence (`TEST-dangers-claim.txt`) | 152 | AI Generated, 100% | AI High 49, Low 71, High 32 | [result](https://www.pangram.com/history/e4d4eedd-7aa0-4566-a3ba-a5b4df985694) |
| heading, his paragraph and only the room's acts (`TEST-dangers-acts.txt`) | 181 | AI Generated, 100% | five AI windows | [result](https://www.pangram.com/history/5a123a1a-623a-40ad-85ba-d4c6c869fe68) |
| heading, his paragraph and his fixes line, no room paragraph (`TEST-dangers-fixes.txt`) | 136 | Human Written | Human High 136 | [result](https://www.pangram.com/history/904c30a7-fe86-4630-8209-e1c049471074) |
| **the guide's first half without the room paragraph**: heading, intro, his paragraph, his fixes line (`PFA-FIRST-noroom.txt`) | 163 | **Human Written** | Human Medium 129, High 18, Medium 16 | [result](https://www.pangram.com/history/3bd48be6-3847-453b-bfb0-45e660c925f5) |
| that, plus what only the room paragraph said (someone they're wary of, heat, cold, the bathroom) (`PFA-FIRST-try4.txt`) | 190 | AI Generated, 100% | AI High 95, Low 68, Medium 27 | [result](https://www.pangram.com/history/f9b227e8-4ee5-4c26-a446-29b185e1cf4f) |
| the section after the room paragraph's cut (`PFA-SECTION-t17.txt`) | 342 | AI Generated, 100% | nine AI windows | [result](https://www.pangram.com/history/df407964-aff7-493e-bfe6-2c6abf52fe1f) |
| the Human first half with the reminder (`TEST-first-reminder.txt`) | 223 | AI Detected, 77% | five AI windows, one Human Low 52 | [result](https://www.pangram.com/history/bd7980a8-2a33-483e-84c4-3360f851e296) |
| the Human first half with the practice part (`TEST-first-practice.txt`) | 234 | AI Generated, 100% | six AI windows | [result](https://www.pangram.com/history/ff2a6888-cd9c-49c3-9152-ec0cc6b5bb45) |
| the Human first half with the last paragraph (`TEST-first-next.txt`) | 211 | AI Generated, 100% | AI High 211 | [result](https://www.pangram.com/history/0502aeef-e24d-4ac6-9af8-dd31a131ac9e) |

Checked after the desktop app came back (#88, #89):

| text | words | result | windows | link |
|---|---|---|---|---|
| the section as the guide has it after both cuts (`PFA-SECTION-t17b.txt`) | 294 | AI Generated, 100% | eight AI windows | [result](https://www.pangram.com/history/dd66404c-67eb-4243-8934-db1672f963b7) |
| try 3: the script's five lines in two sentences, the practice case said to the helper in one paragraph with its reason and the guide's own condition for food (`PFA-SECTION-try3.txt`; receipt, newcomer reads in `newcomer-second/`) | 291 | AI Generated, 100% | AI High 95, Medium 34, Low 18, High 144 | [result](https://www.pangram.com/history/58d85e07-f1ff-4f34-a6b7-e0b5433c8c89) |

What it shows.
- His dangers paragraph reads Human alone and with the heading, as on 2026-11-05. Any room paragraph after it, in all
  eleven wordings now tried, and even its first sentence alone or its acts alone, turns every window AI, his paragraph's
  included. His own fixes line doesn't: heading, intro, dangers paragraph and fixes line read Human Written.
- Every point of the room paragraph is said in its own place elsewhere in the guide (Why Bad Trips Tend to Happen, the
  Do and Don't lists, Get One Human Anchor, Touch, Consent, and Compassion), so it is cut as a repeat
  (`../../experiments/t17-room-cut/apply_t17.py`, gate E378); the two things only it said, the bathroom and someone
  they're wary of, moved to the Do list. Said again after his fixes line, they turn the first half AI (f9b227e8).
- The section's last paragraph (B246), a pointer to the next two sections plus sleep and meaning that No Rash Actions,
  When the Trip Feels Amazing and Give the Session a Beginning and an End say in full, turned the Human first half AI in
  one window by itself (0502aeef); cut the same way (`apply_t17b.py`).
- The reminder (Mixed, 77%) and the practice part (AI) each turn the first half AI. Try 3's rewording of both read AI in one
  window with the fixes line. By bad-trips-2026-11-06a the next step is to look them up across the guide before another
  wording: the reminder's points are all said again in Get One Human Anchor's scripts ("This is a wave", "We don't have to
  solve your whole life right now", "remind me where I am") and the Grounding Menu's Time and Human lists, and the practice
  part's in Why Bad Trips Tend to Happen ("stop the practice") and the aftercare section ("sleep, food, water, warmth").
