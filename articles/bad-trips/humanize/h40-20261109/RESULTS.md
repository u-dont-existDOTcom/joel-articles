# What belongs in each section: the read, and each proposal's fate (2026-11-09)

His next step after the contents (HELPER-NOW, 2026-11-09 17:22 UTC): "make sure the ToC is optimized then we can make
sure the stuff in each section is what belongs there rather than merging or moving?" Round 30's contents went in at his
answer of 18:43 UTC, round 31 at 18:59 UTC; this read is on the guide after both.

**How it was read.** `tools/humanization/clarity_read.py make` split the guide into three parts
([section-read/PART-1..3.txt](section-read/)); each went to a fresh reader with [BRIEF-k.txt](section-read/), asking,
section by section, whether each paragraph belongs under its heading, and to propose a move, a heading, or a cut of a
repeat, with what it keeps. Their answers are [READER-1.md](section-read/READER-1.md),
[READER-2.md](section-read/READER-2.md) and [READER-3.md](section-read/READER-3.md): 18 proposals.

**What came of them.** Five went in without a card ([fix_sections.py](fix_sections.py)): each moves whole paragraphs, word
for word, so the meaning stays and nothing is lost (gate bad-trips-2026-11-07a; his 2026-11-07 12:08 UTC "you're asking
me to approve things that are clearly good"). Three are on round 32's page, with one more card of mine that follows from
one of them. Ten are left, mostly because they would move or cut what he wrote where he put it.

| # | Reader's proposal | Fate | Why |
|---|---|---|---|
| R1-1 | Active Seizure: a heading before the aura paragraph, "Beyond Rescue Medicine: Aura Tricks, Magnesium, CBD, THC and DMSO" | Round 32, SEIZE-HEAD (a question) | New words, so his call; shown with two wordings and no heading. "Tricks" left out: it reads light for a seizure. |
| R1-2 | Active Seizure: "Call medics for a convulsive seizure ..." up, after the rescue medicine | Made (fix_sections.py 2) | First aid, rescue medicine and when to call medics now come first, ahead of six paragraphs on what else may help; no word changes. |
| R1-3 | The bridge "Once the body is stable and those tools have done what they can ..." to the end of the remedies | Made (fix_sections.py 1) | Round 30's contents moved Some Remedies Require More Caution to the top of the remedies, and the bridge, its picture and dividers went with it, so it said "those tools" before them. Back where his post had it, before Tripsitting Yourself or Others. |
| R1-4 | Zeolite: "Most sober people don't feel much from zeolite ... I put a spoonful into water" before the three preparation paragraphs, with a label "Preparing the zeolite" | Made without the label (fix_sections.py 3) | How he takes it now comes before how he prepares it; the order alone does what the label would, with no new words. |
| R1-5 | Cut "The hierarchy appears before the mystical sections because love doesn't require us to ignore the body." | Left | He approved putting this sentence of his post back in round 27 (BACK-HIERARCHY-WHY). |
| R2-1 | Shungite: cut "Aged ozonated-charcoal water is different from zeolite and from swallowing charcoal." | Left | His post's sentence. The section sits among the mental stabilizers, sections after Zeolite and Actual Activated Charcoal; it tells a reader this water is neither before the section says how, and "That water doesn't fix the gut the way zeolite does." covers only zeolite. |
| R2-2 | Shungite: a heading "No Purifier: Boiled Charcoal Water and Shungite" over the last paragraph | Left | The section's heading already names shungite and boiled charcoal water; a fourth level over one paragraph adds more than it helps. |
| R2-3 | First five minutes: the "calm, caring anchor ... not the witch doctor guru" paragraph to For the Person Helping | Left | His round-27 first five minutes, sent as one piece and placed whole where he wrote it (lesson b; OWNER-EDITS r27-his-versions). |
| R2-4 | First five minutes: his story of the commanding voice to No Rash Actions | Left | The same piece. |
| R2-5 | First five minutes: the demon paragraph to Demons, Jinn, Entities, and Shadow Forces | Left | The same piece. |
| R2-6 | "A useful order is room → body → human → time → meaning. ..." from Stillness or Movement? to the Grounding Menu | Round 32, GROUND-ORDER | It belongs with the menu, but it puts "love becomes practical first" three sentences after "Grounding is love becoming practical.", so he weighs the repeat. GROUND-ROOM (mine) follows from it: Room first in the menu, as in the order he chose (Q-5). |
| R2-7 | The Movement evidence note to the end of Stillness or Movement? | Made (fix_sections.py 4) | The post wrote it for the menu's movement lines (Body's two minutes of movement, Ordinary world's pacing), which the deduplication cut from the menu because Stillness or Movement? says them; the Buteyko note stays with the breath lines. |
| R2-8 | No Rash Actions: cut "But more likely you had an experience, and it can wait until the state has passed." | Left | His round-22 turn, the feeling said as it feels and then "But more likely" (OWNER-EDITS h28-experience-content), which also read Human. |
| R3-1 | (Re)defining "Bad Trip": "Sometimes focusing on what we want makes the blockage visible:" to Dealing With Shadow Thoughts | Left | The colon is completed by the picture under it ("Universe Sends What You Need"), which the reader's text didn't show. |
| R3-2 | The Other Bypass: a heading "Why Shadow Work Comes First" before "Modern people carry so much trauma ..." | Round 32, SHADOW-START (a question) | Shown with my alternative as my pick: the definition ("Shadow work to me is neither BDSM nor ...") and where to begin open the Shadow Work part, which since the contents opens straight into Sorrow; his post had The Other Bypass before those sections. |
| R3-3 | What Kind of Aftermath Is This?: "No "another ceremony will fix this" reflex." and the three paragraphs after it to After the Storm | Made (fix_sections.py 5), after the opening paragraph | They are for everyone after a hard trip; the aftermath section keeps the kinds of lingering symptoms, and Bring in mental-health support when: now follows them directly (his round-31 AFT-PLACE answer, "c", kept). His round-27 aftermath version is the list, which stays as it is. |
| R3-4 | Planning a Trip or Ceremony?: cut "And train before you need it, ..." | Left | He approved it in round 31 (MW-PREP): the practice his next sentence counts on. |
| R3-5 | Spiritual ≠ "Getting Your Ass Kicked": cut "That is tripsitting, shadow work, and the path becoming practical." | Left | His post's closing line for the section; the reader marked it the weakest of its five. |

**Checks after the moves.** Every word of the guide is the same before and after (fix_sections.py asserts it). Fidelity
keys R30 PASS; owner edits 69 passed, 3 waiting; keep-as-is 24 kept; no characters to swap; section mentions 11, none
flagged; repo links PASS.
