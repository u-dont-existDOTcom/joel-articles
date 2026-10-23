# Coverage check B: guide lines 521-1019 against the article

> **Decided since (turn 102, his answers of 2026-10-23 17:53 UTC).** 95.2 A, temporary distance on purpose (line 543): it read 100% AI in the Untangling paragraph in three shapes, so the paragraph is as it was and the point is question 96. 95.3 B and 95.4 B: the two signs (535, 537) and the safe adult's sentence (661) stay out. Borrow Hindsight (643) was fixed in turn 101.

Read-only check, 2026-10-23 (after 14:45 UTC). This file is the only thing written.

## Basis and how to read it

- Guide: `source/inner-child-guide-2026-10-04-r4.txt`, lines 521 to 1019, read in full.
- Article: `experiments/t101-coverage/ARTICLE-NOCOMMENTS.md` (written 14:08 UTC), read in full before comparing, so a point carried in another section counts as carried. Article line numbers below (l.) are that file's.
- `HUMANIZED-ARTICLE-SO-FAR.md` (changed 14:14:59 UTC) differs from that snapshot in four places (Borrow One Competency reordered under a new h3, "Instead of Blame", two Ask God for a Loan lines). None of them removes a point in this range (the Borrow One Competency reorder keeps every point of the guide's When Love Still Feels Missing).
- Paths are relative to `/home/claude/joel-articles/articles/inner-child-therapy/`.
- I started from turn 71's seven items (`experiments/t71-guide/COVERAGE-r4-B.md`, `TRACE-r4-B.md`), re-checked each against today's article, then went through every guide paragraph in the range again for anything new.
- Records searched: `OWNER-EDITS.json`, `OWNER-QUESTIONS.md` (current, and old versions through read-only `git show`), Joel's answer files in `experiments/t*-answers/`, and the dedup, repeats and tells reports.
- DECIDED means Joel cut or changed the point, or wrote the replacement text himself. A cut that only Claude made (dedup, repeats check, AI-window rework) with no word from Joel is a REAL GAP, even when a report calls the point "SAID" elsewhere. Joel's rule "you can only cut if it isn't losing important meaning or there's no good way to merge" dates from 2026-10-17 02:07 UTC, after the turn-54 cuts in items 1 and 2.
- Not listed: wording differences, swapped examples, tone. Rule E162: no dosing, recipe or preparation line in this range is missing, so none is listed.

## 1. Guide lines 535, 537: PARTLY CARRIED (minor)

- Guide: "Your preferences, beliefs, and feelings change dramatically with the people around you." and "You don’t know what you would choose without the fear of disappointing somebody." (two of the five "Possible signs")
- Closest article passage: "It might feel wrong somehow to like something before you've checked anyone's face." (l.624, From Survival to Experimental Play). Also "still being recognizably yourself wherever you are (maybe louder in some places)" (l.670, Four Pairs That Commonly Hook the Child).
- Missing: The signs list is gone. The sign that your preferences, beliefs and feelings swing with whoever is around is told only from its healthy side, and "can't say what you'd choose without fear of disappointing someone" is only approximated by the "checked anyone's face" line. The other three signs are carried in other words (the h1 opener, "nobody's around to take your cues from", the guessed answer).
- Record: No word from Joel. Claude took the signs out in the turn-54 repeats check (E172, 2026-10-14). `experiments/t71-guide/TRACE-r4-B.md` item 1: "Author's OK for this cut: none recorded." `OWNER-EDITS.json` id `survival-p4-signs-20261011c` carries Joel's "12. continue" (2026-10-11 23:33 UTC), a go-ahead to write the paragraph three days before the cut. I searched his answer files and `OWNER-QUESTIONS.md` again: nothing on these signs.
- Verdict: REAL GAP.

## 2. Guide line 543: PARTLY CARRIED

- Guide: "Some people also benefit from temporary, intentional distance long enough for the conditioning to quiet down and authentic preferences to surface."
- Closest article passage: "If a family, group or relationship won't let you do this while you're still part of it, temporary distance may be necessary." (l.673, Four Pairs That Commonly Hook the Child)
- Missing: The article offers temporary distance only as a way out of a system that blocks differentiation. It never offers deliberate, temporary distance as a way to let the conditioning quiet down so your own preferences can surface.
- Record: No word from Joel. Claude cut it in turn 54 as a repeat of Joel's line: `experiments/t54-repeats/REVIEWS.md` l.17, "P6's temporary distance (Joel's B228 says it better) ... Cut"; the same turn's `REPEATS-REPORT.md` l.49 says the cut sentence "adds a purpose (letting conditioning quiet down so real preferences surface)". `OWNER-EDITS.json` id `survival-p6-focusing-20261012b` carries Joel's "continue" (2026-10-12 03:13 UTC), a go-ahead that predates the cut. See also `experiments/t71-guide/TRACE-r4-B.md` item 2.
- Verdict: REAL GAP.

## 3. Guide line 555: PARTLY CARRIED (minor)

- Guide: "Beauty, intelligence, achievement, and caretaking can all be real gifts. They become belonging bargains when failure in the arena feels like loss of self."
- Closest article passage: "That might be beauty, athleticism, sexual desirability, intelligence or grades." (l.636, Untangling the Belonging Bargains) and "The question is whether losing one of them would feel like losing yourself." (l.661, Four Pairs That Commonly Hook the Child).
- Missing: The article never says these arenas can be real gifts, and the test "it is a bargain only when failure feels like loss of self" is applied to pleasure, praise, gain and belonging but not to beauty, intelligence, achievement or caretaking.
- Record: `experiments/t56-answers/JOEL-20261015-1215.md` (2026-10-15 12:15 UTC): "the first line of P3 is referencing gifts which are way before so it doesn't flow from P2 to P3. ok this passes and i think fixes those probs", followed by his own P2 and a shorter P3 with no gifts line (`OWNER-EDITS.json` id `untangling-joel-20261015b`, must_not_contain "These can all be real gifts."). His 2026-10-13 version (id `q17-p3-fix-20261012d`) had the line in his words.
- Verdict: DECIDED (his own text).

## 4. Guide line 611: MISSING (minor)

- Guide: "MN 20 gives practitioners several ways to work with unskillful thoughts when they arise"
- Closest article passage: "In one discourse (sutta), AN 6.63, the Buddha defines karma in terms of intention (so if you didn't mean to cause harm, your mind is not poisoned)." (l.701, The Inner Guide)
- Missing: The MN 20 source and its point, that the suttas give several ways to work with unskillful thoughts as they arise. The article cites AN 6.63 and DN 2 only.
- Record: `experiments/t60-answers/JOEL-20261016-2137.md` (2026-10-16 21:37 UTC): "ok let me give you an example of how i would do P8 simply (passes human, reads better)". His paragraph cites AN 6.63 and DN 2 only and is in the article word for word (`OWNER-EDITS.json` id `inner-guide-p7-joel-20261016`). It replaced a Claude draft that had MN 20.
- Verdict: DECIDED (his own text).

## 5. Guide line 643: PARTLY CARRIED (minor)

- Guide: "Sometimes I see the situation differently, feel more like that wiser version of myself, or feel accompanied by them. More than one can happen together. This is a fallible perspective to borrow, not proof that a perfect Higher Self is waiting underneath everything."
- Closest article passage: "It's a question borrowed from your future self, and I wouldn't take their answer as gospel." (l.177, Borrow Hindsight)
- Missing: What the question can do (change how the situation looks, make you feel more like the wiser version, or leave you feeling accompanied, sometimes all together) is gone, and so is the tie-in that this is a fallible view, not a perfect Higher Self. The "not gospel" half is carried.
- Record: Claude's cut; Joel has not ruled on the outcomes. Turn 65 had both ("It can change how the whole thing looks. It can also just make you feel a bit more like that person, or less alone (sometimes all at once). ... No perfect Higher Self is handing down answers."). Turn 90's AI-window rework shortened them ("two short sentences out, the best-guess point as a plain one", install note at Borrow Hindsight in `HUMANIZED-ARTICLE-SO-FAR.md`, commit `ad4887ed`) and turn 93 cut what was left (`experiments/t93-tells/TELLS-ROUND2.md` a08). His 83 (`experiments/t93-answers/JOEL-20261022-1901.md`: "i like you to try yourself IF you know what looks like AI tells") is about tells, not about this content. On the Higher Self half he ruled the other way: 49.5 (`experiments/t72-answers/JOEL-20261018-1906.md`): "it's normal that we'd say one thing in the guide and then explain it more in the section that differentiates the guide from IFS", recorded in `OWNER-QUESTIONS.md` (2026-10-18 19:06 block) as "49, 5: both stay."
- Verdict: REAL GAP (the Higher Self half goes against his 49.5).

## 6. Guide line 661: PARTLY CARRIED (minor)

- Guide: "A sincere goodwill wish may be available even without warmth. If not, borrow one simple sentence from a safe adult: “I won’t attack you while we sit here.”"
- Closest article passage: "No warmth today? Then rest your hands there and notice what you find, no faking required. Non-judgement is a place to start. It can blossom into love over time." (l.352, A Heart-to-Child Loop). Also "just promise your little one you won't be cruel to them on purpose" (l.308, Make a Simple Vow).
- Missing: The borrowed safe-adult sentence, which is the loop's last fallback when there is no warmth. The goodwill wish exists in A Smaller Doorway: Goodwill (l.205-209) but the loop doesn't point to it.
- Record: Claude's compression; the sentence was never put to Joel. `experiments/t65-guide/SP-DEDUP-REPORT.md` l.38: "G3.8 Else “I won’t attack you while we sit here.” SAID: B154 "you won't be cruel to them on purpose"." His question 40 (`experiments/t68-answers/JOEL-20261017-1658.md`) was only about "Non-judgement is a place to start"; he answered "a" and pasted the whole guide passage to show it is in the original, and ruled nothing on the safe-adult sentence. See `experiments/t71-guide/TRACE-r4-B.md` item 5.
- Verdict: REAL GAP.

## 7. Guide line 849: PARTLY CARRIED (minor)

- Guide: "A personal history of voices, paranoia, major loss of reality testing, or persistent perceptual disturbance after a psychoactive substance belongs inside this gate before planning another altered-state session, including with a different substance."
- Closest article passage: "Your own drug history matters too. If you go manic, psychotic (...), get super paranoid, or end up worse afterward than before, those are signs to reconsider trying the same thing again" (l.520, When Escape Leaves Reality Behind), pointed to from Altered States Can Deepen the Therapy: "And yes, those caution signs still count." (l.506).
- Missing: Only a history of voices is not a warning sign here. The rest is carried: paranoia, losing reality, "be careful with other drugs that mess with what's real too" (l.524), and spaced-out episodes that keep going or come back while sober (l.528).
- Record: Joel's answers of 2026-10-10 19:37 UTC (`OWNER-QUESTIONS.md`, Decided block of that time; `OWNER-EDITS.json` id `voices-and-warning-signs-20261010`): "no, that's normal to hear voices and lose sense of reality on psychedelics (not as normal for weed tho)... but if you go manic, psychotic ..., get super paranoid, or end up worse afteward than before, those are signs to reconsider trying the same thing again".
- Verdict: DECIDED (his list replaced the guide's).

## 8. Guide line 851: PARTLY CARRIED (minor)

- Guide: "But “I experienced it once,” “I can access it only in a particular state,” and “I can contact it reliably in ordinary life” are three different things."
- Closest article passage: "Keep it as a reference point, and chase it playfully, because it is already a part of you" (l.508, Altered States Can Deepen the Therapy) and "That night can't be the bar for every morning after, or regular life starts to feel like failing." (l.510).
- Missing: The three-way distinction (felt once, reachable only in that state, reachable reliably in ordinary life). The article keeps the reference-point idea and the warning that the peak is not the bar for ordinary mornings.
- Record: `OWNER-EDITS.json` id `joel-upload-20261019`; `experiments/t77-answers/JOEL-20261020-2337.md`: "also i made some changes to the article myself prior to gpt's advice...". "Now, the beautiful stuff." is his own paragraph from his 2026-10-19 upload, word for word (install note in `HUMANIZED-ARTICLE-SO-FAR.md`: "Turn 77: Joel's own text from his 2026-10-19 upload"). It replaced turn 71's version, which carried the distinction ("Feeling it once is a long way from feeling it only when you're tripping, and that's still a long way from feeling it on a regular morning while the coffee brews."; commit `7dcd62af`).
- Verdict: DECIDED (his own text).

## 9. Guide line 901: MISSING (a clause, minor)

- Guide: "That does not mean the action was harmless or that no different option existed in the abstract."
- Closest article passage: "They still have to answer for what they did, and it still hurt. Seeing how they got there doesn't make it okay." (l.815, How to Forgive Without Forgetting)
- Missing: The clause that a different option did exist in the abstract, it just wasn't available to this person. The article says "it was the only move they had" (l.813) with no such qualifier. "Harmless" is carried by "doesn't make it okay".
- Record: `experiments/t73-answers/JOEL-20261018-2158.md` (2026-10-18 21:58 UTC): "14a remove that clause it is just confusing." (`OWNER-QUESTIONS.md`, same block: "14, A: the clause is out".)
- Verdict: DECIDED.

## 10. Guide line 947: PARTLY CARRIED

- Guide: "Which capacities can become more yours? Which are healthiest when shared? Which genuinely belong inside the relationship? ... while the relationship itself can remain precious and important."
- Closest article passage: "What you're after is care your little one can count on from more than one place, while the inner relationship stays precious and important. Other jobs can go to friends or community, outsource to the tools or pros, whatever works." (l.735, Borrowed Adulthood in Relationship)
- Missing: The three sorting questions are gone, including "which genuinely belong inside the relationship", and the relationship that stays precious is now the inner one, not the one with the person who carries the adult jobs. The rest (take in some of what they do, spread other jobs across friends, community, tools and pros) is carried.
- Record: `experiments/t67-answers/JOEL-20261017-1401.md` (2026-10-17 14:01 UTC), his answer 33: "list of 3 again, lack of clarity (which relationship stays precious?)... redundancy... this version passes:", then his paragraph with "the inner relationship stays precious and important" (`OWNER-EDITS.json` id `ba-p2-joel-20261017`).
- Verdict: DECIDED (his own text). Note for the queue check: GPT's PGQ-009 asks for this same function inventory and a "precious relationship" line, which runs against his "list of 3" and "which relationship" comments, so it needs his word.

## 11. Guide line 997: PARTLY CARRIED

- Guide: "IFS “unburdening,” often done after witnessing a part’s origin story, can be powerful. It can also become dramatic, memory-focused, suggestive, or destabilizing—especially for people prone to dissociation, DID-like fragmentation, or spiritual bypass."
- Closest article passage: "Others seem to leave people more split up than when they started." (l.871, How This Relates to IFS) and "I'd also want one who doesn't put ideas in your head, and who understands dissociation." (l.839, Finding a Therapist to Borrow Adulthood)
- Missing: The unburdening technique itself, with the warning that it can be dramatic or destabilizing. The general cautions (suggestion, dissociation, fragmentation) are carried by the two passages above.
- Record: `experiments/t74-answers/JOEL-20261019-0008.md` (2026-10-19 00:08 UTC): "in the IFS section, remove this part from the original guide, because it doesn't make sense, not clear, not explaining anything exactly, and i don't see how unburdening is so diff from my approach aside from the weird terminology and exact protocols" (`OWNER-EDITS.json` id `ifs-unburdening-cut-20261019`).
- Verdict: DECIDED.

## 12. Guide line 1001: PARTLY CARRIED

- Guide: "For inner-child pain, shame, attachment wounds, self-abandonment, or the absence of a reliable inner adult, a good reparenting therapist may fit better."
- Closest article passage: "Inner Child Reparenting therapists do exist, and you can find them, although they often are not licensed" and "Schema Therapy comes closest to my approach." (l.835, l.837, Finding a Therapist to Borrow Adulthood)
- Missing: The guidance on which kinds of pain a reparenting-focused therapist may suit better than an IFS therapist. The safety half of that guide paragraph (non-suggestive, understands dissociation) is in.
- Record: `experiments/t74-answers/JOEL-20261019-0008.md`: "Let's combine the 3 appendix paragraphs on finding a therapist into a new h1 before Appendix" (his text, `OWNER-EDITS.json` id `finding-a-therapist-joel-20261019`). Question 63 (old `OWNER-QUESTIONS.md`, commit `a18430e8`) then listed this sentence as not anywhere else in the article; Joel: `experiments/t75-answers/JOEL-20261019-0026.md`, "63a" (A = add only the sentence about ideas in your head and dissociation, which is in).
- Verdict: DECIDED.

## 13. Guide line 1005: PARTLY CARRIED (minor)

- Guide: "These approaches do not all make the same claims. I borrow particular distinctions and practices rather than presenting the whole synthesis as their consensus or claiming that their research validates it as a package."
- Closest article passage: "I borrow particular ideas and practices from each of them, but the mix is mine, so please don't blame them for it." (l.875, Related Clinical Work)
- Missing: That the approaches differ in what they claim, and that their research does not validate this as a package. The article says only that the mix is his.
- Record: `experiments/t95-answers/JOEL-20261022-2135.md` (2026-10-22 21:35 UTC): "84.8a" (A = cut "or claiming that their research validates it as a package"); `experiments/t98-answers/JOEL-20261023-0229.md` (2026-10-23 02:29 UTC): "89a" (A = the wording now in the article).
- Verdict: DECIDED.

## 14. Guide line 1009: PARTLY CARRIED (minor)

- Guide: "I can’t fully endorse any of them because none follows my whole approach or has expressed interest in doing so."
- Closest article passage: "I borrow particular ideas and practices from each of them, but the mix is mine, so please don't blame them for it." and "This framework developed through the teachers and collaborators credited below and my own practice." (l.875, Related Clinical Work)
- Missing: The plain statement that he does not fully endorse the teachers he credits. "The mix is mine" is about the clinical approaches and only implies it.
- Record: `experiments/t72-answers/JOEL-20261018-1906.md` (2026-10-18 19:06 UTC), his 49.6: "dedup yeah, so just remove "Several teachers directly influenced this method. I can’t fully endorse any of them because none follows my whole approach or has expressed interest in doing so."" (`OWNER-EDITS.json` id `appendix-first-person-pending-20261018`).
- Verdict: DECIDED. He took it as a repeat of Related Clinical Work's disclaimer, which he later shortened himself (item 13).

## 15. Guide line 1011: MISSING (minor)

- Guide: "I made a Gemini thread that turns her training into an interactive tool."
- Closest article passage: "She has a book and a free one-hour YouTube training, and she's on Instagram." (l.879, Teachers and Practice Resources; links omitted)
- Missing: The Gemini thread built from Daja's training.
- Record: `experiments/t72-answers/JOEL-20261018-1906.md`: "47 a. e." (E = "Leave it out"; the thread's link opened on "Link doesn't exist"). `OWNER-QUESTIONS.md`, 2026-10-18 19:06 block: "47, A and E, with 49, 6: ... the Gemini line stays out."
- Verdict: DECIDED.

## Judged carried (not listed)

- 557 "belonging feels like life or death": "Whose approval suddenly feels like I can't live without it?" (l.657) and "so they could keep belonging" (l.430). Joel's own 2026-10-13 P3 had it in so many words; his shorter 2026-10-15 P3 does not.
- 637 "Don't let mystery outrun love indefinitely": Timing Is Individual's "Has it reached your little one yet?" (l.711) and the food-bank image (l.235).
- 787-789 (turn 71 item 6): now carried. Somatic Heart Opening (l.725) has stay with it "while you're present and still choosing", retraumatizing "mostly when nobody's with you or you've disappeared into the sadness", and slowing down once it is swamping you. "More tears are not proof of more healing" stands in the opening ("I could have kept crying forever", l.15). The guide's "not evidence for one physiological mechanism" guards a claim the article never makes ("Some feel held, in the body").
- 793 love as wishing well versus warm affection: A Smaller Doorway: Goodwill (l.205-209) and the vow (l.308).
- 801-803 spirituality not another assignment, and the fruits test: My Journey (l.59, "Maybe ordinary life already gives you enough love and meaning. Great.") and Joel's rewrite of How Much Happiness (88.1; l.721, "check out how they deal with people when things are going badly").
- 815 "I get stricter about spirituality, not looser": Joel said the guide's sentence was a paraphrase of him and gave the expansion that is in the article (`experiments/t69-answers/JOEL-20261017-1856.md`, 2026-10-17 18:56 UTC; `OWNER-EDITS.json` id `crisis-opening-joel-20261017-1856`).
- 819 "if you can already observe it, skip this step": his own paragraph (l.594) is conditional ("when the part that wants to die feels like all of you").
- 861 and 881: his own fixes at 49.2 ("it'd make sense to get a professional to weigh in for some situations", "without catastrophizing"; the demon sentence cut from Non-altered states, with the point kept at l.536, "easy targets for every kind of influence", and l.562, "getting manipulated by all kinds of evil forces").
- 887-891 shallow practice: his rewrite (88.2) plus Your Body Might Need Some Love First (l.117-119: check sleep and the next days, dream images are not evidence).
- 917-919 forgiveness inquiry: l.817, "come back to how whoever did it got to be someone who could do that, until you understand it well enough that it changes how you feel". The guide's "without ... endlessly rehearsing the same case" is not said there; the general checking warning in When Healing Turns Into Checking (l.322-324) covers the same trap.
- 961 "name what you received and do one piece for yourself": Become the Adult Apprentice (l.245), "So steal some of it ... try it before you call next time."
- 993 "A trustworthy adult function is built through care, boundaries, action, and direction": his 45 D (leave it out); the borrow-one-job path is at l.863.
- 1017 "Filter for Internal Family Systems": his own words at 49.7 and in Finding a Therapist (l.837, "You can filter them by Schema or IFS.").

## Summary

- Items: 15 (3 MISSING, 12 PARTLY CARRIED; 11 of the 15 minor).
- REAL GAP: 4, items 1, 2, 5, 6 (the signs list, deliberate temporary distance, Borrow Hindsight's outcomes with its Higher Self tie-in, the safe-adult sentence in the loop). None has a word from Joel; items 1, 2 and 6 were Claude's dedup cuts, item 5 was Claude's AI-window rework and its Higher Self half goes against his 49.5.
- DECIDED: 11, items 3, 4, 7 to 15. All rest on Joel's own text, a cut he asked for, or an option he picked.
- Turn 71's seven items: #6 (tears, guide 787/789) is now carried. #1 (signs), #2 (temporary distance) and #5 (safe-adult sentence) are still open with no word from Joel (items 1, 2, 6 here). #3 (real gifts), #4 (MN 20) and #7 (Gemini thread) are still out, by his own text or choice (items 3, 4, 15).
- New since turn 71: item 5 (REAL GAP) and items 7 to 14 (all DECIDED).
- For the parent: item 10's PGQ-009 conflicts with a recorded Joel comment; item 14 leans on a disclaimer Joel later shortened himself.
