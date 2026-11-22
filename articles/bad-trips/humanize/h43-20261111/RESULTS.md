# The humanize pass's first fixes (2026-11-11, turn 34)

Every fix is his five first (SKILL.md, "Writing for Pangram"), checked in his Pangram account after its prediction (`predict.py`), its making-sense receipt (`make_receipts.py`, with each fresh reader's needed read in `NEEDED-READ.md`) and the linter. The tests are `TEST-*.txt` (`build_tests.py`); what went into the guide is `apply_h43.py`. A section whose first check read Mixed was checked a paragraph at a time first (E343).

| batch | test | what | result | windows (label, confidence, words) | link | fate |
|---|---|---|---|---|---|---|
| h43a | h42-08-fix1 | Active Seizure 2, the Low sentence ("So it might help ...") | Mostly Human Written, 10% AI | Human, High, 62; Human, Medium, 10; Human, High, 136; AI-Generated, Low, 24 | [a0b91061](https://www.pangram.com/history/a0b91061-d4c0-4eb5-9d57-5436e3099381) | out: AI Low, worse than the guide's Human Low |
| h43a | h42-17-fix1 | Nausea Smoothers, the Low sentence | Human Written, 0% AI | Human, High, 76; Human, Medium, 6; Human, High, 27 | [d00c127c](https://www.pangram.com/history/d00c127c-6a07-4d03-af6e-cf7fd9eae9c7) | in (Low to High) |
| h43a | h42-30-fix1 | Grounding Menu 2, going outside and exercise | Human Written, 0% AI | Human, Medium, 6; Human, High, 157; Human, Medium, 15 | [7fd43eaf](https://www.pangram.com/history/7fd43eaf-b126-4b77-a6f9-53b4456044e2) | in (Low to Medium; the Medium one is mine, on the list for him) |
| h43b | h42-08-fix2 | Active Seizure 2, second try ("While a seizure continues ...") | Human Written, 0% AI | Human, High, 208; Human, Medium, 21 | [83f4caef](https://www.pangram.com/history/83f4caef-593d-4931-af86-fdb8c79f53db) | out: Human Medium, but it drops "adjunct remedy" (KEEP-AS-IS K12): round 34's ADJUNCT card |
| h43b | h42-20-p-fix1 | DMSO's contraindications, the seizure item (paragraph check, E343) | Human Written, 0% AI | Human, High, 61 | [4d3214e7](https://www.pangram.com/history/4d3214e7-ee0f-4940-9654-442fe51a0520) | in with the section |
| h43b | h42-22-p-fix1 | Ocean water's touch and effect (paragraph check) | Human Written, 0% AI | Human, High, 93 | [c6065c63](https://www.pangram.com/history/c6065c63-c667-44f8-bfcf-deca95b61e4d) | in with the section |
| h43b | h42-25-p-fix1 | Niacin's B3 forms and the bridge to tripsitting, the list taken apart | AI Detected, 46% AI | Human, High, 33; AI-Generated, High, 37 | [fd6713de](https://www.pangram.com/history/fd6713de-0bf3-4ca3-bf5d-23f1b2e0351b) | out: the bridge AI High |
| h43c | h42-20-fix1 | Mental Stabilizers 3 (DMSO's interactions and contraindications), the whole section | Human Written, 0% AI | Human, High, 163 | [f0dd7b3f](https://www.pangram.com/history/f0dd7b3f-af71-4078-9c23-ff4d6de8a714) | in (AI to Human High throughout) |
| h43c | h42-22-fix1 | Mental Stabilizers 5 (ocean water and the charcoal waters), the whole section | Human Written, 0% AI | Human, High, 307 | [913f21aa](https://www.pangram.com/history/913f21aa-5675-4649-b12e-9ee80fe5b7ff) | in (AI to Human High throughout) |
| h43c | h42-25-p-fix2 | The bridge to tripsitting, without its list | AI Detected, 36% AI | Human, High, 22; Human, Medium, 11; AI-Generated, High, 25 | [60f2bff5](https://www.pangram.com/history/60f2bff5-892f-4b7a-a487-92fb9f2779c2) | out: the bridge AI High; next: the tell panel |
| h43c | anchor-a1 | Get One Human Anchor, its first two paragraphs | Human Written, 0% AI | Human, High, 37; Human, Medium, 20; Human, High, 46 | [3a3fd073](https://www.pangram.com/history/3a3fd073-98e1-46ea-9e5d-342bd7c7ee67) | in (AI to Human; 38 earlier wordings read AI) |
| h43c | harm-b1 | Risk of Harm, its first paragraph, the nine reasons taken apart | AI Generated, 100% AI | AI-Generated, High, 117 | [4c6f1bf6](https://www.pangram.com/history/4c6f1bf6-513b-4f95-8a5c-35d9916efd43) | teaching card (round 34, TEACH-HARM) |
| h43d | h42-08-fix3 | Active Seizure 2, third try, "adjunct remedy" kept | AI Detected, 11% AI | Human, High, 62; Human, Medium, 10; Human, High, 136; AI-Generated, Low, 23 | [5f6a6b57](https://www.pangram.com/history/5f6a6b57-47ce-4db7-ac73-5746241a5d28) | out: AI Low |
| h43d | h42-41-p-fix1 | Dealing With Shadow Thoughts, the during-a-trip lines in his list frame | AI Detected, 61% AI | Human, High, 30; Human, Medium, 13; AI-Generated, Low, 23; AI-Generated, Medium, 54 | [79d1ab12](https://www.pangram.com/history/79d1ab12-5d62-4b06-8480-da6a052d9c13) | out: AI Low and Medium, worse than the guide's two AI Low |
| h43d | harm-b3 | Risk of Harm, third wording, from the tell panel's notes (panel-harm-b2/PANEL.md) | AI Generated, 100% AI | AI-Generated, High, 167 | [52763d5d](https://www.pangram.com/history/52763d5d-523d-4c61-baba-c9e66c5fd445) | teaching card (round 34, TEACH-HARM) |

## Every window that isn't Human High

### h42-08-fix1 ([result](https://www.pangram.com/history/a0b91061-d4c0-4eb5-9d57-5436e3099381))

- AI-Generated Low (24 words): So it might help alongside rescue medicine, but it's still experimental, and I wouldn't wait on it while a seizure keeps going.
- Human Medium (10 words): As for topical CBD, it hasn't been well-studied.

### h42-17-fix1 ([result](https://www.pangram.com/history/d00c127c-6a07-4d03-af6e-cf7fd9eae9c7))

- Human Medium (6 words): It may also extend the trip.

### h42-30-fix1 ([result](https://www.pangram.com/history/7fd43eaf-b126-4b77-a6f9-53b4456044e2))

- Human Medium (6 words): Music / Use familiar music when possible.
- Human Medium (15 words): The same goes after a stimulant or an unknown mixture, or with any medical concern.

### h42-08-fix2 ([result](https://www.pangram.com/history/83f4caef-593d-4931-af86-fdb8c79f53db))

- Human Medium (21 words): While a seizure continues, the rescue medicine comes first, and I'd still consider DMSO alongside it, although that's experimental.

### h42-25-p-fix1 ([result](https://www.pangram.com/history/fd6713de-0bf3-4ca3-bf5d-23f1b2e0351b))

- AI-Generated High (37 words): Even once the body is stable and those tools have done what they can, somebody still needs to sit with whatever the altered mind has opened up, the fear or grief, an old memory, a sudden certainty...

### h42-25-p-fix2 ([result](https://www.pangram.com/history/60f2bff5-892f-4b7a-a487-92fb9f2779c2))

- AI-Generated High (25 words): Once the body has settled and those tools have done what they can, whatever the trip stirred up still needs somebody to sit with it.
- Human Medium (11 words): Avoid sustained-release niacin and the useless non-flush hexanicotinate form.

### anchor-a1 ([result](https://www.pangram.com/history/3a3fd073-98e1-46ea-9e5d-342bd7c7ee67))

- Human Medium (20 words): So have one calm person be the anchor and take the lead. One person can only handle so much, though.

### harm-b1 ([result](https://www.pangram.com/history/4c6f1bf6-513b-4f95-8a5c-35d9916efd43))

- AI-Generated High (117 words): Risk of Harm: When Peer Support Isn't Enough / Get urgent help the moment somebody might hurt themselves or anyone else, or you can't keep them physically safe, like when they keep heading for roads and high places, or water for that matter. Voices telling them what to do are a reason too, and so is a fixed, terrifying belief they've started acting on. Get help just as fast if they turn violent or they're so severely confused they're unreachable. Dangerous physical symptoms count, and so does going so long without sleep that their judgment is falling apart. And if it's more than you can safely handle, call for help then too.

### h42-08-fix3 ([result](https://www.pangram.com/history/5f6a6b57-47ce-4db7-ac73-5746241a5d28))

- AI-Generated Low (23 words): While a seizure continues, the rescue medicine comes first, and I'd treat DMSO as a plausible adjunct remedy, although that's experimental.
- Human Medium (10 words): As for topical CBD, it hasn't been well-studied.

### h42-41-p-fix1 ([result](https://www.pangram.com/history/79d1ab12-5d62-4b06-8480-da6a052d9c13))

- AI-Generated Low (23 words): While you're still tripping, maybe don't take every shadow thought as the truth about you, or try to suppress it either.
- AI-Generated Medium (54 words): Confessing it to everyone in the room can wait, and so can turning it into some permanent diagnosis... You can just notice it instead, something like "this is a thought and a feeling, and it's intense, but it isn't the whole of me." Then return to room, body, human, time, and love.
- Human Medium (13 words): In the subconscious world of concepts, however, two sides are often considered together.

### harm-b3 ([result](https://www.pangram.com/history/52763d5d-523d-4c61-baba-c9e66c5fd445))

- AI-Generated High (167 words): Risk of Harm: When Peer Support Isn't Enough / You can sit through a lot with someone, but not everything. The moment you think they might hurt themselves or anybody else, get urgent help, even if you're not sure. I'd get help too if I couldn't keep them physically safe, like when they keep heading for the road or the water, or trying to get up somewhere high. It's time as well when voices are telling them what to do, or they've started acting on some terrifying belief they won't let go of, and any violence means calling right away. Someone so severely confused that they're unreachable needs more than a friend can give. So does someone whose body is showing dangerous signs, like trouble breathing or overheating, or who hasn't slept in so long that their judgment is going. If you find yourself wondering whether this is more than you can safely handle, it probably is, so call.

## What I learned

- His five fixes carried where his voice was already around the window: the remedies (DMSO, ocean water) went to Human High throughout, and Get One Human Anchor's opening read Human for the first time in 39 wordings once its point was said as what makes a trip worse and the crowd's four acts became two.
- They didn't carry in a firm call-for-help list (Risk of Harm: AI 100% in each wording, after a tell panel that flagged its whole shape), nor in his J69 list frame with my words (Shadow Thoughts), as SKILL.md's fifth fix already says. The call-for-help list is round 34's teaching card.
- A word on his keep list can hold a sentence at Low: Active Seizure's "adjunct remedy" read Medium without it and AI with it in my order, so the choice is his (round 34's ADJUNCT card).

