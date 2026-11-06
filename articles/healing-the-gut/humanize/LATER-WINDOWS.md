# Windows below High left for later

Joel, 2026-11-06 20:13 UTC: "if it's "low" we should fix it, medium you could try to fix but if it's too difficult we
can put that as a later todo when we want to learn more, and some things are not worth fixing, pangram has some bugs,
like "Why?" often reads as medium, etc." (gate gut-2026-11-06a).

Every Low window in the gut article that reads as the text's own is fixed (batch 12, r17). The three old AI Low windows
gate E354 still named (Phase 1's heading with its first sentence, and the stacks list) had already read Human, High in
later checks of their sections, whose window text the ledger hadn't kept (gut-2026-11-06c). What's below is left on purpose.

## The whole article, draft B (2026-11-06)

His extension read draft B [Human Written](https://www.pangram.com/feed/bb64a934-cf2c-47b3-ae93-af2a363a0644):
no AI window, 9 Human High, 8 Medium, 4 Low (`fix-20261103/r17/draft-b-check/CONFIDENCE.md`).

- **To fix (Low):** Phase 5's first paragraphs: "Start by re-seeding with Davis's high-dose “SIBO Yogurt”,
  fermented for 36 hours." (Low, 15 words), "It contains L. reuteri ... kill SIBO. / Then feed the new healthy
  bacteria." (Low, 26) and "Bulsiewicz says to slowly titrate plant diversity back into your diet, aiming for 30+
  different plants per week." (Low, 18). They read AI in the live post (#142), so they have come up, but not to High.
  Tries so far: 1 (`fix-20261103/r19/`, joined each step to what it does) read worse in the cut of Phases 4 and 5
  ([#184](https://www.pangram.com/history/00f07f88-96d7-48c8-accf-24249c02731c), 59% AI, against its control
  [#186](https://www.pangram.com/history/d8911a47-187f-4603-9bf2-3133571457fa), 30%); 2 (`fix-20261103/r20/`, the
  reader's situation first) read as its control did in the cut of Phases 3 to 6
  ([#188](https://www.pangram.com/history/072c7249-a3db-44f6-bd44-a2be6bca3a35), 28.3%, against
  [#187](https://www.pangram.com/history/fd9ef004-3ba4-4386-bf49-fdb31df764ea), 27.8%). Both cuts read the steps AI
  unchanged, so they can't judge a fix (gut-2026-11-06f): tries 2 and 3 (`fix-20261103/r21/`, each term glossed as his
  Phase 1 fix does) go to the whole article as drafts C (#189) and D (#190).
- **To try (Medium):** Phase 4's "If it's Bile Acid Diarrhea, the test is SeHCAT, and the treatment is bile
  binders." (16 words), High in its own stretch (#176). Its one try (`fix-20261103/r19/`: what Bile Acid Diarrhea is,
  joined to its test and treatment) read AI High in the cut of Phases 4 and 5, where the control read it AI Low (#184,
  #186), so it stays as it is, a later todo (gut-2026-11-06a), until there's a diagnosis worth another try.
- **Pangram's bugs, left:** the splits at "Dr." ("This one's from Dr.", "Dr." twice, "William Davis is back for
  that, along with Dr. Will Bulsiewicz (Fiber Fueled)."), and short lines on their own: "And no snacking!", his
  "Does anyone count their plants?", "Check your environment (Nathan)." and "Then check the brain."

## Pangram's bugs, not worth fixing

Pangram splits the text at an abbreviation's period and reads the 1- to 6-word piece Medium on its own, or AI Low when
the text before it reads AI:

| check | window | words |
|---|---|---|
| [B, #156](https://www.pangram.com/history/7b694c0d-d080-4b92-888f-57f4ce851842) | "For H." | 2 |
| [I, #163](https://www.pangram.com/history/6474197b-1c7e-41e7-b613-c915a69bbfd0) | "Michael Ruscio." (after "Dr."), "diff) during the kill phase." (after "C.") | 2, 5 |
| [K, #165](https://www.pangram.com/history/0468d290-7082-4a9b-b49c-cc83e257c2ce) | "Dr.", "It contains L." | 1, 3 |
| [L, #177](https://www.pangram.com/history/8ff3fe60-b777-4eb0-b49a-01db1fbe7d6a) | "Dr." | 1 |
| [r18-P, #179](https://www.pangram.com/history/dcfc1cd4-912e-4a21-865a-2e297f278f35) | "This part is from T.C." (AI Low, after my rewritten sentence read AI Medium) | 6 |

## To learn from later

- Phase 2 whole ([#171](https://www.pangram.com/history/31e8d763-563d-4c55-aa5f-04218bf2a721)): Pangram split the
  opening at both "Dr."s into windows of 21, 8 and 5 words, and the 46-word window after them ("Either way you stop
  feeding the bacteria ... sweep your gut clean in between.") read Human Medium. The same paragraphs without the split-up
  opening read High ([#169](https://www.pangram.com/history/c7517cd3-0b56-4a28-b2d0-b8c2de287a48)). Whether the split
  alone lowers the window after it would take a pair of checks: the stretch with "Dr." and without it.
- Group cuts that start at a heading or a list's intro. On 2026-11-04 the checks of r12 in groups read Phase 1's heading
  with its first sentence AI Low ([#125](https://www.pangram.com/history/d11abfe4-40c5-485d-8f91-c715510881b3)) and the
  stacks list's intro with its first item AI Low ([#131](https://www.pangram.com/history/80b7a95e-3c65-4943-8824-31d1ee228a7b),
  [#136](https://www.pangram.com/history/63b206c5-ade8-46a0-a2ed-6c96ca97901c)), while the same words read Human, High
  in their own sections ([#139](https://www.pangram.com/history/e2b76d46-7dda-4141-b156-6aef920b7306),
  [#137](https://www.pangram.com/history/3513e03a-c513-4ab7-992b-ff9ead34a379)) and in the whole live post
  ([#142](https://www.pangram.com/feed/e3a65841-a626-4b34-aad7-62b9dfa48ada), which leaves headings out). My rewrites of
  them read worse in their sections' cuts: Phase 1's sentence AI Medium
  ([#179](https://www.pangram.com/history/dcfc1cd4-912e-4a21-865a-2e297f278f35)), the list AI High at 99.99% with the
  intro and kits ([#180](https://www.pangram.com/history/579da364-48c8-490e-bd68-3cf167311fdd)). The old words stay.
  The same two cuts with the old words are frozen as #181 and #182, for when Pangram's web app is signed in again:
  they tell whether #180 was my list or the cut.
- The kits paragraph's end ("Ruscio's Leaky Gut Support Kit ... with it.") read AI in every cut that ended with it
  ([#131](https://www.pangram.com/history/80b7a95e-3c65-4943-8824-31d1ee228a7b),
  [#136](https://www.pangram.com/history/63b206c5-ade8-46a0-a2ed-6c96ca97901c),
  [#180](https://www.pangram.com/history/579da364-48c8-490e-bd68-3cf167311fdd)) and Human, High in every cut that went
  on past it ([#137](https://www.pangram.com/history/3513e03a-c513-4ab7-992b-ff9ead34a379),
  [#177](https://www.pangram.com/history/8ff3fe60-b777-4eb0-b49a-01db1fbe7d6a)). Whether a text's last window is read
  harder would take a pair of checks: the same paragraph at the end of a cut and inside one.
- Old results kept without their windows' text: the ledger's older web-app results kept only the AI windows' text, so
  gate E354 can't see which old windows they cleared (`pangram_ledger.py` now names them in its refusal, gut-2026-11-06c). Adding
  their text from Pangram's history, as #137 and #139 now have, needs the web app signed in.
