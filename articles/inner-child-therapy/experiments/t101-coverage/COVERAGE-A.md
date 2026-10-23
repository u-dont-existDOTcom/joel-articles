# Coverage check A (turn 101): guide lines 1-520 against the humanized article

Question 95 on OWNER-QUESTIONS.md, from Joel's 92a (2026-10-23 14:05 UTC): one fresh coverage check that brings him only the real gaps.

**Result: 22 entries. 2 are REAL GAP (entry 3, guide line 75; entry 9, guide line 157). 20 are DECIDED.**

## Scope and method

- Guide: `source/inner-child-guide-2026-10-04-r4.txt`, lines 1-520 of 1,020. COVERAGE-B.md covers lines 521-1019 and COVERAGE-QUEUE.md the queue entries.
- Article: `HUMANIZED-ARTICLE-SO-FAR.md` as it stood at 2026-10-23 15:11:38 UTC, HTML comments removed. Sections are cited by heading, because line numbers move. The 14:08 snapshot in this folder (ARTICLE-NOCOMMENTS.md) differs from that text in four blocks of paragraphs: the warmth, protecting and Guide paragraphs of Borrow One Competency at a Time and the paragraphs after them in If the Love Isn't Coming Yet (reordered, one cut, one reworded), and two paragraphs of Your Loan is PRE-APPROVED!. None of the four holds a point used below, and every quotation below was checked against the 15:11:38 text. The article changed once more at 16:12:40 UTC, after that check: one sentence about a perfect Higher Self was added to Borrow Hindsight and the header note was reworded. Neither touches a point used below, and the article line numbers cited here (l.183, l.191, l.193) still hold.
- Paths are relative to `articles/inner-child-therapy/`. "l." is a line number in the file named; for OWNER-QUESTIONS.md it is the page as committed at 86a3707c (2026-10-23 14:18 UTC), because the page changes every turn and the same lines now sit at other numbers (`git show 86a3707c:articles/inner-child-therapy/OWNER-QUESTIONS.md`). Joel's quotes are word for word with his typos kept; guide quotes are shortened with "...".
- Method: (1) rechecked the 39 entries of the turn-71 check (`experiments/t71-guide/COVERAGE-r4-A.md` with `experiments/t71-guide/TRACE-r4-A.md`) against the live article; (2) re-read guide lines 1-524 against the article, paragraph by paragraph; (3) ran a sentence-overlap scan (idf-weighted) of about 550 guide sentences against the article and read every low- and medium-overlap sentence that carries a caveat, which found two points the turn-71 list did not have (entries 17 and 18) and one more sub-point in entry 6; (4) for each gap, searched the records for a decision by Joel: OWNER-EDITS.json, OWNER-QUESTIONS.md (and earlier versions through read-only `git show`), `experiments/t*-answers/*.md`, the trace, draft and receipt files, and OWNER-LOCKS.json.
- Not listed: wording differences, swapped examples, tone; dosing amounts, recipes and preparation details (rule E162).
- An item is an entry only when the article lacks a specific instruction, safeguard, distinction or caveat of the guide's anywhere. When the article says the whole point in other words anywhere, the item is not an entry; the turn-71 table below shows where each one went.

## Verdict marks

- **REAL GAP**: no word of Joel's reaches the omitted point, and either an explicit instruction of his conflicts with the omission or a question put to him about it went unanswered.
- **DECIDED (named)**: Joel's own words cut, reject or flag the point or its paragraph ("in part" where his words name only some of the sub-points).
- **DECIDED (own text)**: the passage was replaced by text Joel wrote (or was asked to write), and his words do not mention the omission.
- **DECIDED (general OK)**: only a general or section-level OK from Joel, plus a drafter's note saying what was cut.

Drafters' notes (whitelists, gap notices, ledger lines, "owner-deleted" lines written by drafters) are not Joel's decisions. They are cited only to show what was done.

## Entries (guide order)

## 1. Guide line 17: PARTLY CARRIED (minor)

- Guide: "Treat the complete sequence as a provisional synthesis: some components have direct research behind them, while the full arrangement is my own"
- Closest article passage: "For now, I think of the whole path in five fairly predictable stages." (The Chicken-and-Egg Problem). The appendix has "I borrow particular ideas and practices from each of them, but the mix is mine, so please don't blame them for it." (Related Clinical Work)
- Missing: That the five-stage sequence is a provisional arrangement and only some of its parts have research behind them. The appendix line says the mix is the author's, but nothing ties that to this sequence or calls it provisional.
- Record: `experiments/EPISODE-006-OWNER-FINAL-LISTICLE-RESULT-20260916.json` l.10 (Joel's final five-stage text, recorded instruction "keep this exact final version") and l.12 (the file's note that the final text "omits the earlier explicit research/provisional-synthesis disclaimer"). `HUMANIZATION-WRITER-STATE-20260916.md` l.29-31 (drafter): "those differences are authorized owner changes. Do not restore the superseded source units". Joel's answer "53 b" (`experiments/t72-answers/JOEL-20261018-1906.md` l.49; OWNER-QUESTIONS.md l.402) chose only the "whole path" wording.
- Verdict: DECIDED (own text). The stage list is Joel's final text; his words do not mention the disclaimer.

## 2. Guide lines 71, 75 (end) and 163: MISSING

- Guide: "A no to the frame is not a pacing problem to solve. If you do not want inner-child work, stop using that language and do not keep trying to sneak it back in through “gentler” exercises or by renaming ordinary tasks as reparenting. Care, protection, guidance, and human support can continue in whatever language actually fits you." Also, end of 75: "this approach does not override your choice about whether to use inner-child framing at all." And 163: "If it does not, there is no need to label it that way."
- Closest article passage: "Not wanting to do it anymore is a reason too, but if that "nope" sounds like a part of you that's trying to protect you, I'd hear it out first. If it still says no, that's your answer." (When to Change the Strategy)
- Missing: That declining the inner-child frame itself is a fine answer, not a pacing problem, and that care, protection, guidance and human support can go on in other words. The article lets a reader stop a practice but never says the frame can be dropped while its purposes are kept.
- Record: `R4-ADDITIONS-PROVENANCE-20261008.md` l.9: Joel, 2026-10-08 02:23 UTC, on the draft of this paragraph ("Depth 1"): “who is gonna be "sneaking reparenting in " thru some gentler version? we have no idea where this came from?” Its status table (l.56) marks Depth 1 "cut (Joel, 02:23)", and l.7 says the lines about the app's own behavior "stay in the AI guide". OWNER-QUESTIONS.md l.416 (drafter): the sentence was in the article for a while on 2026-10-18 and "it's out again".
- Verdict: DECIDED (named). Joel cut the L71 paragraph; the end of L75 and L163 repeat its point and his words do not address them separately.

## 3. Guide line 75: PARTLY CARRIED

- Guide: "A complete tolerance pause is a last resort, and a safety problem can require a pause whether or not you want one."
- Closest article passage: "If you need a break from the communion, simply jot down the reason and the progress made so far. Then come back later, once that reason has changed and you feel comfortable." (Before You Try to Go Deep). Also "Bring the challenge back gradually, and only when you want to and you're recovering well." (Your Body Might Need Some Love First)
- Missing: That a full break is a last resort, and that a safety problem can force a pause whether or not the reader wants one. No other passage carries it; the only "last resort" left in the article is about calling the police.
- Record: Joel, 2026-10-18 19:06 UTC, question 54 item 9, as asked at commit d5451e22 (the page was replaced in turn 72, commit 0928272a; read it with `git show d5451e22:articles/inner-child-therapy/OWNER-QUESTIONS.md`) (the guide's sentence above, and "no testing gentler versions while it lasts"): “9b keep first one remove 2nd one.” (`experiments/t72-answers/JOEL-20261018-1906.md` l.50). The article followed: OWNER-QUESTIONS.md l.407 ("the full break as a last resort is first in P3 now, and the no-testing part is out"); install comment in `HUMANIZED-ARTICLE-SO-FAR.md` l.183. The Before You Try section Joel pasted on 2026-10-19 still contained “A full break from your little one is a last resort. Sometimes it isn't up to you, though, like when something's actually unsafe.” (`experiments/t74-guide/joel-before-you-try-20261019-0008.txt` l.7; `experiments/t74-guide/REVIEWS.md` l.5 says his paste differed from the article in three other paragraphs only). On 2026-10-22 23:54 UTC he replaced that paragraph with the one quoted above (`experiments/t97-answers/JOEL-20261022-2354.md` l.10; install comment `HUMANIZED-ARTICLE-SO-FAR.md` l.191: "This paragraph is his; it replaces mine"). The old line it replaced read "A full break from your little one is a last resort, unless something's actually unsafe." (`experiments/t97-installs/apply_t97.py` l.17-22). His message does not mention the two dropped sentences. The no-testing part is DECIDED (named): cut by 9b.
- Verdict: REAL GAP. His explicit "keep first one" covers the last-resort and safety-forces-a-pause sentence, it is a safeguard, and the article no longer has it. Contrary reading, for completeness: he replaced the whole paragraph with his own on purpose, which could be read as DECIDED (own text); but his message says nothing about these sentences.

## 4. Guide lines 79 and 83 (also the opening of 81): PARTLY CARRIED

- Guide: L83: "This is not a religion test. A religious label, an unusual belief, an intrusive thought, anger, a past harmful act, or an unwanted fantasy does not by itself establish current harmful intent." and "Listen without flattering cruelty, arguing theology, or helping somebody become more effective at exploiting people." L79: "do not invite the child forward—not even briefly to find out how the child reacts. The child’s fear is not a diagnostic test"
- Closest article passage: "Everybody gets scary thoughts they'd rather not have sometimes, and they don't make you a bad person"; "If some of it turns out to be malice they actually want to act on, the inner child can wait."; "their little one stays out of it" (When the Present-Day Adult Is Dangerous to the Child)
- Missing: Only intrusive thoughts are covered. Lost: that a religious label, unusual belief, anger, a past harmful act or an unwanted fantasy does not by itself show harmful intent; the guardrails for a helper (do not flatter cruelty, argue theology, or help someone exploit people better); and "not even briefly to find out how the child reacts" with "The child’s fear is not a diagnostic test". From L81: the opening questions (what help do you want, why are you here, is the identity producing the life you expected) and "Sovereignty begins with the ability to pause, question, refuse, and revise" are not stated as such; the article keeps "what the identity gets them and what it costs" and the sovereign-but-obeying-an-urge line, which are Joel's own.
- Record: `experiments/DANGEROUS-ADULT-H2-PROMOTION-RECEIPT-20260925.json` l.36-37: lists "the child is not a diagnostic test (P4)" and "beliefs/identity alone not the gate" as implicit only, and records "Joel 2026-09-24: the last two source paragraphs 'could mostly be deleted'" and that he proceeded ("good continue", 03:28 UTC) without asking for the implicit points to be made explicit. `experiments/DANGEROUS-ADULT-OWNER-FINAL-P1-20260924.md` l.355-359: Joel, 2026-09-25 20:24 UTC: “for P1, the reason i'm thinking there's no need to talk about people who use therapy to manipulate people is because i don't think those people can be dealt with. they will simply manipulate anyone who tries to help them. they are not part of what i can help with.” The same file, l.277, has his P2 wording “it sounds mor elike slavery”. The lock file OWNER-LOCKS.json names "dangerous-present-adult-safety-gate"; the drafter's disposition (l.359) records it as narrowed by that decision.
- Verdict: DECIDED (named, in part). L83 falls under his "could mostly be deleted"; the manipulation-through-therapy guardrails under his 20:24 statement. The "diagnostic test" point was recorded as implicit only and he did not name it.

## 5. Guide lines 91 and 93: PARTLY CARRIED (minor)

- Guide: "Plain analysis is not automatically avoidance, and a feeling is not beyond analysis because it arrived without words. Neither form is inherently deeper or truer." Also "A quiet mind is not, by itself, resistance or failed contact."
- Closest article passage: "If words are there, speak or write them." and "And it might not be the same order all the time." (You Don’t Need an Inner Monologue)
- Missing: That neither a worded analysis nor a wordless feeling is more genuine than the other, that analysing is not automatically avoiding, and that a quiet mind is not by itself resistance or failed contact. The article says only that words are fine when they come and that the order can vary.
- Record: `experiments/EPISODE-008-R10-PRESERVATION-AND-COLD-AUDIT-20260916.json` l.19-21 (drafter): Joel's three-paragraph version removes "the separate vivid-imagery/resistance reassurance" and "the separate polished model closure that explicitly said plain analysis is not avoidance / preverbal feeling is not inherently truer". `HUMANIZATION-WRITER-STATE-20260917A.md` l.20 (drafter): "Episode 008 inner-monologue three-paragraph owner realization: Human/high; keep exact."
- Verdict: DECIDED (own text). The section is Joel's own realization; his words do not mention these sentences.

## 6. Guide lines 105, 107 and 109: PARTLY CARRIED

- Guide: "But “I stayed oriented” is not enough by itself either. Ask four things: could you stop and return, do you actually want to go back toward it, did it feel difficult-but-workable rather than simply too much or unwanted, and how did you recover afterward in sleep and ordinary functioning?" Also "do not rush to classify the experience as healing or harmful" and "if distress is climbing, change several things at once".
- Closest article passage: "Do you want to go back toward what came up, or is some part of you saying no?" (Your Body Might Need Some Love First); "So can you stop in the middle and come back to the room?" (Before You Try to Go Deep); "Going at it harder isn't as useful as going at it with more wisdom and compassion." (When Healing Turns Into Checking)
- Missing: (a) That staying present or oriented through a session does not show it was not too much. (b) The question whether it felt hard but workable or simply too much. (c) "Change several things at once" when distress is climbing. (e) Not rushing to call an unclear session healing or harm. ("Intensity by itself is not progress" is carried in other words by the Checking line above and by "Some people try to toughen themselves up in a cauldron, but what you're looking for is the edge where you can actually learn." in Your Body Might Need Some Love First.)
- Record: (c) Joel, 2026-10-18 19:06 UTC, question 54 item 8: “8b, humanize that in before you try to go deep, and we can remove the "change several things at once" version in the other section since that sounds too vague to be useful.” (`experiments/t72-answers/JOEL-20261018-1906.md` l.50). On "intensity by itself is not progress" (item 10 as asked at commit d5451e22) he answered “10a that's what we are putting back into 8.” (a), (b) and (e) were in the article's Your Body Might Need Some Love First ("or by whether you stayed present through it", "(And was it hard but doable, or just too much?)", "I wouldn't rush to call it healing or harm") until Joel's 2026-10-22 23:54 UTC rewrite. His message calls the earlier text “the ai section” and pastes “the all dark green version” without them (`experiments/t97-answers/JOEL-20261022-2354.md` l.16-24); it does not mention these three points. They are new losses since the turn-71 check.
- Verdict: DECIDED (named for c; own text for a, b and e, where the omission was not weighed in his message).

## 7. Guide line 137: PARTLY CARRIED (minor)

- Guide: "If you put the experience into words now, distinguish words that were actually present then from the translation you are making now."
- Closest article passage: "Just because your stomach tightened up doesn't mean their boundary crossing indicates “They're evil.”" (Catch the Hook Before the Story Takes Over)
- Missing: The distinction between words that were really there in the moment and the translation made afterwards. The article keeps the sensation-versus-judgment distinction only.
- Record: `HUMANIZATION-WRITER-STATE-20260916W.md` l.56-62 (drafter): "do **not** reinsert this nuance into Catch-the-Hook by default"; "If later editorial review finds the specific event-record-versus-retrospective-translation distinction still uniquely necessary, surface it to Joel as a narrow question rather than inserting it" (repeated in `HUMANIZATION-WRITER-STATE-20260917A.md` l.78). That question was never asked (`experiments/t71-guide/TRACE-r4-A.md` item 15: "I found no such question asked"). The drafter's reason was that the inner-monologue section sat right before Catch the Hook; in the live article it is in the first half, well before Simple Practices. Joel's final Catch the Hook block is "owner-final" (`HUMANIZATION-WRITER-STATE-20260917A.md` l.20), and he rewrote the following paragraphs on 2026-10-07 16:46 UTC: “B2 was really bad, i rewrote it b1-b2. It's hum, high conf” (OWNER-EDITS.json id `pgq-001-joel-rewrite`, l.1379; superseded 2026-10-20 by his upload, id `joel-upload-20261019`). GUIDE-UPDATE-QUEUE-20261006.md l.11 marks the queue item "in" on that basis.
- Verdict: DECIDED (own text). The block is Joel's own; the drafter's standing condition to ask him narrowly was never used.

## 8. Guide line 141: PARTLY CARRIED (minor)

- Guide: "Don’t dismiss your own genuine attraction, orientation, gender identity, or another meaningful part of your experience as “just intrusive” or “not the real you” merely because it is unwanted, stigmatized, confusing, or conflicts with personal, family, community, or religious expectations."
- Closest article passage: "The opposite extreme of our pendulum, throwing everything transient away, as some people do with "thought-noting" practice, also isn't healthy, except as a meditation exercise. Transient feelings and thoughts can be meaningful signals." and ""I feel attracted" or "I feel ashamed" is real as a feeling, but it doesn't settle who you are, or who you love." (Catch the Hook Before the Story Takes Over)
- Missing: The specific warning not to write off a genuine attraction, orientation or gender identity as "just intrusive" or "not the real you" because it is unwanted, stigmatized or against family, community or religious expectations. The article's "opposite extreme" covers transient feelings in general.
- Record: GUIDE-UPDATE-QUEUE-20261006.md l.11: queue item PGQ-001 ("an experience isn't its own interpretation; orientation and gender not steered either way"), marked "in" by "Joel's own rewrite of B1 and B2 (2026-10-07 16:46, "It's hum, high conf")". OWNER-EDITS.json ids `boundary-paragraph-joel` (l.1365) and `pgq-001-joel-rewrite` (l.1379), superseded by `joel-upload-20261019`. `experiments/t71-guide/TRACE-r4-A.md` item 16: his B2 "has no clause about "just intrusive", "not the real you", or family, community or religious expectations, and I found no statement of his about those clauses."
- Verdict: DECIDED (own text). Joel rewrote the passage that answers this queue item; the omission was not weighed in his words.

## 9. Guide line 157: PARTLY CARRIED (minor)

- Guide: "Before the next interaction, choose a realistic outcome. Mutual understanding may be possible. Sometimes success is conveying information, saying no, or ending an exchange without forty minutes of self-defense. You do not have to make somebody understand you before you can act."
- Closest article passage: "it makes more sense to count on what they keep showing you they can do than on the right words finally getting through to them" and "And if it fails again, and you've said what you mean, well, you can't guarantee they'll understand it." (Other Folks Also Have Hooks)
- Missing: The instruction to pick a realistic outcome before the next conversation (for example passing on information, saying no, or leaving without a long defense), and the general permission to act without the other person's understanding. The article has the second idea only for a repeated apology.
- Record: No cut record. `experiments/t71-guide/TRACE-r4-A.md` l.324-344 (item 17): "For "Before the next interaction, choose a realistic outcome." there is no cut record". Joel accepted the September compression with “oh wow ok perfect” (`experiments/EPISODE-008-ALSO-LOOK-OUTWARD-OWNER-ACCEPTANCE-20260918.md` l.25), which `experiments/OWNER-PUNCHLIST-20260927.md` l.44 says was "accepted on its Pangram result ... without a sense read". His later rewrite of the apology paragraph (OWNER-EDITS.json id `also-look-outward-run-joel`, l.1408, 2026-10-07 23:18 UTC: “Here i fixed the red sections for you, this is human high conf learn some lessons”) does not mention this sentence. DEDUP-PASS-20261008.md l.28-29 offered him the guide's line “You do not have to make somebody understand you before you can act.” as "Your call"; no reply is on record.
- Verdict: REAL GAP (minor, borderline). Contrary reading: the turn-71 trace filed this as his own text, since the passage after it is his rewrite. It is listed because no record ties his rewrite to this sentence and the question put to him about it was never answered.

## 10. Guide line 183: PARTLY CARRIED (minor)

- Guide: "Ask: “Is this helping me feel or understand something more clearly, make a decision, or respond differently—or am I checking the same question for reassurance?”"
- Closest article passage: "Going back can still matter, even when nothing new turns up. But returning to the same wound can also become a search for certainty in an inherently uncertain existence." and "What is this practice supposed to help, and how would I know if it's helping?" (When Healing Turns Into Checking)
- Missing: The sharper test question that separates a helpful revisit from reassurance-seeking (does it help me feel, understand, decide or respond differently, or am I checking the same question for reassurance). The article names the pattern and asks what the practice is for, but gives no outcomes to check against.
- Record: `experiments/CHECKING-R13-R14-RESULT-OWNER-HELP-GATE-20260920.md` l.56-70: Joel was shown the source paragraph and asked for "one free same-meaning rewrite of the stubborn discrimination paragraph". `experiments/CHECKING-P3-OWNER-ACCEPTANCE-PROMOTION-20260921.json` l.8, 14, 54: his paragraph accepted 2026-09-21 ("Direct current-chat response: accepted"), replacing the placeholder. `experiments/t71-guide/TRACE-r4-A.md` item 22: "Its omission is not a recorded decision; his replacement paragraphs came first."
- Verdict: DECIDED (own text). The section is Joel's own rewrite of the paragraph that held this question.

## 11. Guide line 189: MISSING

- Guide: "Avoidance can serve the same certainty loop from the other side. If you are doing exposure, including clinician-guided ERP, keep the useful exposure and drop the checking rather than fleeing the situation or escalating it into a bigger test." Also "Exploring sexuality, orientation, gender, attraction, or relationship fit is not “checking” merely because the answer is uncertain" and "Do the action when it serves a life you actually choose".
- Closest article passage: "if you don't want to be touched, say no now and work out what it means later. Same if something might be dangerous right now, or might be a medical warning sign: step away or get checked first." (Catch the Hook Before the Story Takes Over). This carries the guide's limits on exposure, not the advice itself.
- Missing: Nearly all of it: avoidance as the same certainty loop from the other side; keeping the exposure and dropping the checking; that exploring sexuality, orientation or gender is not checking just because the answer is uncertain; and doing the action for a life you choose rather than to force certainty.
- Record: Joel, 2026-10-18 19:06 UTC, question 54 item 5, as asked at commit d5451e22 (this exposure paragraph; the options for items 1 to 7 were A, leave it out; B, put it back; C, your words): “5. a” (`experiments/t72-answers/JOEL-20261018-1906.md` l.50; OWNER-QUESTIONS.md l.403: "54, 1, 2, 3 and 5, A: left as they are").
- Verdict: DECIDED (named).

## 12. Guide lines 235 and 241-243: PARTLY CARRIED (minor)

- Guide: "In that case, imagine somebody whose intention is simply to take good care of you: an ideal parent, wise aunt, decent therapist, fictional character, future self, or an adult you invent for the purpose." and "Simply feeling accompanied can be the useful function." L241-243: "If nobody usable comes to mind, ask: ... “What would somebody who genuinely wanted to take good care of me say or do next?”"
- Closest article passage: "Then go smaller still, to the least cruel response a decent adult could offer your little one. It's scaffolding, and it isn't a test of whether you were loved enough." (If the Love Isn't Coming Yet); "And there's always your future healed self if you can imagine that." (Borrow One Competency at a Time); "remember watching Mr. Rogers or Sesame Street? Those adult role models are what we're looking for at this stage." (The Chicken-and-Egg Problem)
- Missing: The fallback for someone with no usable figure: imagine a caring person who is simply made up, borrowing a caring function without proving such a person existed, and "feeling accompanied can be enough". Also the second question to ask when nobody usable comes to mind.
- Record: `experiments/BORROW-LOVE-DRAFTS-20260926.md` l.232-236: Joel, 17:10: “what is this whole paragraph doing why are we repeating so much advice”; the drafter's reading: "Sense call: P3 is cut. BL-U5 becomes duplicate-function-consolidation" (BL-U5 is this invented-adult unit, l.37). L.339 (drafter): the second question folds into Borrow One Competency's fallback line, "the survivor is Borrow P4". Joel then cut that line: 2026-10-14 19:51 UTC, answer 24: “you can cut botth mr rogers because i also have that before. can keep 2nd mention of spiritual love in Ask God...” (OWNER-EDITS.json id `borrow-mr-rogers-cut-20261014`, l.2228; OWNER-QUESTIONS.md l.515). `PARKED-READER-QUESTIONS.md` l.53 quotes the cut line: "If nobody comes to mind, you can look to examples like Mr. Rogers, or spiritual love you've felt".
- Verdict: DECIDED (named, in part). His 17:10 comment and his answer 24 are his; the invented-adult idea itself is named only in the drafter's reading of the first, and in the sentence he cut with the second.

## 13. Guide line 249: PARTLY CARRIED (minor)

- Guide: "Advice to other people can become too idealistic because the adviser does not have to pay the cost. Keep the part that is compassionate, sane, realistic, and based on the person’s actual options."
- Closest article passage: "Or put somebody you care about into your exact life, your family, your bank account and all, and then step outside it and ask what you'd tell them." (Borrow Love—or Borrow the Perspective of Care)
- Missing: The caution that advice meant for other people runs idealistic, so keep only the part that is realistic for the person's actual options. The article keeps the "exact life" instruction but not the caution.
- Record: `experiments/BORROW-LOVE-DRAFTS-20260926.md` l.613: Joel, 18:47: “ok well first of all P4 doesn't even make sense. you can't see that? then P5 tries to rescue it but P5 looks like we could trash it entirely if P4 made sense”. L.624 (drafter): "P5, owner-deleted (Joel, 18:47)", its point going into P4 "as one clause". L.647 (drafter): "The generosity and idealism wording and the study are owner-deleted with P5." P5 was the paragraph with this caution.
- Verdict: DECIDED (named).

## 14. Guide lines 253 and 255: MISSING (minor)

- Guide: "Then imagine that the person shrugs, rejects the advice, or says, “Big whoop.” Which part remains true without requiring their gratitude, trust, or agreement?" and "Once you find one usable sentence or action, stop repeating the thought experiment in different words. Try the sentence or do the action."
- Closest article passage: "And don't expect a thank-you for the session, like they booked it." (If the Love Isn't Coming Yet); "Then take a small piece of whatever you'd tell them and hand it to yourself." (Borrow Love—or Borrow the Perspective of Care)
- Missing: The imagine-them-rejecting-it step (which part of the advice still holds without their gratitude, trust or agreement) and the instruction to stop re-wording the exercise once you have one usable sentence and act on it.
- Record: `experiments/BORROW-LOVE-DRAFTS-20260926.md` l.788 (drafter): "Sense call: BL-U11, the "Big whoop" test, is consolidated" under the 17:10 comment quoted in entry 12. L.874: Joel, 2026-09-26 20:44 UTC, on the paragraph's last sentences: “i didn't understand what your last sentences were doing and this looked a lot better to me, but still tested AI”; l.894 (drafter's reading): "The stop-rerunning point (BL-U12) goes."
- Verdict: DECIDED (named for L255, through the drafter's reading of his words; general OK only for L253).

## 15. Guide line 283: PARTLY CARRIED

- Guide: "Prayer may evoke abandonment or condemnation; a teacher’s betrayal may damage trust in what once felt sacred. Don’t automatically call this bypass, lack of faith, or disguised parental conflict. Ask what has been lost, what needs questioning, and what is still worth preserving. You may need to grieve or change a relationship, practice, or understanding."
- Closest article passage: "If a spiritual teacher you trusted betrayed you, even sitting down to meditate can feel like it belongs to them now." and "But if you let an abuser control your appreciation of life, then you've given them an unearned win." (When the Spiritual Relationship Hurts)
- Missing: The prayer case (prayer that brings up abandonment or condemnation); the caution not to label such difficulty as bypass, lack of faith or disguised parental conflict; and the advice to ask what was lost, what needs questioning and what is worth keeping, with permission to grieve or change a practice.
- Record: `experiments/BORROW-LOVE-DRAFTS-20260926.md` l.1473-1495: Joel, 23:15: “it did read ai. Ai stuff overuses "i wouldn't call that X" and the 3 part conditional syntax. Then you have the instruction manual features and the ending is bringing it all together in the most defensible way possible. here's mine which is human, and i like it better:”, followed by his paragraph. The drafter lists the prayer case, the don't-label clause and the ask, grieve and change points as "owner-deleted".
- Verdict: DECIDED (own text). His stated reasons are about AI patterns, not about this content.

## 16. Guide line 303: PARTLY CARRIED

- Guide: "Look for ordinary signs that the capacity is becoming yours: you can do one protective act without the helper present; disagree with them without losing your ground; recover after missing a practice; ask for help without handing over judgment; and leave a relationship or method that starts demanding obedience." and "Once you can carry five percent, test that five percent in daily life."
- Closest article passage: "over time there are more and more of those little parts you can do yourself" (The Chicken-and-Egg Problem); "Ten seconds of sitting with yourself like that is good enough for a start, so try it before you call next time." (Become the Adult Apprentice)
- Missing: The list of signs that borrowed adulthood is becoming your own, including being able to leave a helper or method that demands obedience, and the instruction to test your five percent in daily life.
- Record: `experiments/ADULT-APPRENTICE-DRAFTS-20260927.md` l.3, l.75 (AA-U5: "The list of signs is compressed to one or two"), l.315-330: the drafter proposed to cut the section's second paragraph and consolidate its points; Joel, 2026-09-27 01:19 UTC: “yes ok to cut it”.
- Verdict: DECIDED (named).

## 17. Guide line 333: PARTLY CARRIED (minor). New since the turn-71 check.

- Guide: "Intuition and analysis are different instruments. ... Neither gets unilateral control. A strong intuitive click is information, not proof."
- Closest article passage: "I'd keep whatever you feel around them, and look at their track record." (Don’t Give the Inner Adult Away); "It should make sense, too." (Start With Whatever Showed Up)
- Missing: The pairing of intuition and analysis as two checks on each other, and that a strong intuitive click is information, not proof. The article carries the track-record check on a helper and "It should make sense, too."
- Record: `experiments/t95-installs/CUT-start-with-p8.md` l.3: Joel, 2026-10-22 21:35 UTC: “as for p8 start with, it looked like fluff, i cut it.” The cut paragraph was the intuition-and-analysis one (OWNER-EDITS.json id `joel-95-20261022`, l.3014).
- Verdict: DECIDED (named). The paragraph was in the article at turn 71, which is why it was not on that list.

## 18. Guide line 345: PARTLY CARRIED (minor). New in this check.

- Guide: "Completing it without immediate relief is not automatically failure, and completion alone does not prove it helped. Adjust the action to what it actually contributes to safety, connection, competence, or enjoyment—not just to whether it earns a tick."
- Closest article passage: "not feeling better right away is information to learn from. It doesn't mean failure." (Not Every Hero Wears A Cape); "What is this practice supposed to help, and how would I know if it's helping?" (When Healing Turns Into Checking)
- Missing: That finishing the chosen act does not prove it helped, and the instruction to adjust the act to what it actually adds to safety, connection, competence or enjoyment rather than to whether it earns a tick.
- Record: Joel, 2026-10-21 16:01 UTC, question 72 b: “b)a.” (`experiments/t79-answers/JOEL-20261021-1601.md` l.6). OWNER-QUESTIONS.md l.310: "72b, A: your question "What is this practice supposed to help, and how would I know if it's helping?" is now only in When Healing Turns Into Checking." So his A took that check out of Not Every Hero Wears A Cape (DEDUP-PASS-20261021.md l.28).
- Verdict: DECIDED (named, in part). His A removed the repeated question; it did not name the instruction to adjust the act.

## 19. Guide line 411: MISSING

- Guide: "Choose what it means while you’re sober and regulated. ... It doesn’t speak for the child, contain secret wisdom, or become an oracle. Your adult judgment stays in charge."
- Closest article passage: "Whatever helps you feel connected to the Nurturer and Protector you've been practicing." (Remind Yourself)
- Missing: That the reminder object is not the child's voice and not an oracle, that adult judgment stays in charge, and that its meaning is chosen while sober and regulated.
- Record: `experiments/DANGEROUS-ADULT-SELF-AUDIT-RULES-20260924.md` l.426 (E113): Joel, 2026-10-02 00:16 UTC: “The original was saying that the childhood toy doesn't speak for the child, contain secret wisdom or become an oracle. ... I would simply cut out the last 2 sentences entirely. I don't think people will be confusing the stuffed animal with an oracle.” `PARKED-READER-QUESTIONS.md` l.58: "He cut the caution ... so the section has none (E113)." The sober-and-regulated clause is not named in his words.
- Verdict: DECIDED (named).

## 20. Guide line 481: PARTLY CARRIED (minor)

- Guide: "Respond to what has become available instead of restarting the original exercise. When a need becomes clear, try offering that kind of care and notice how it lands. ... A useful shift may be small; more intensity is not the only way forward."
- Closest article passage: "keep an eye on that part too, for any change at all. If it's been calling all this stupid, it might turn out to be scared of getting its hopes up." (Hear the Guard First)
- Missing: What to do once something shifts: respond to what has become available instead of restarting the exercise, offer the kind of care the new need calls for, and a small shift is enough. The article says to watch for any change and gives one example.
- Record: `experiments/WHEN-THE-ADULT-VOICE-FEELS-FAKE-20261002.md` l.224 (the shortening proposal), l.231 (Joel, 2026-10-04 01:33 UTC: “yes i agree with your shortening sugggestions.”), l.234 (what was cut: the other two examples and "You don't need an age ...").
- Verdict: DECIDED (general OK). This is the weakest basis in the list: his OK is general, and the proposal he agreed to did not list the cut sentences.

## 21. Guide lines 489 and 493: PARTLY CARRIED (minor)

- Guide: "don’t define “I did it correctly” as “it worked.” And don’t add a new invisible prerequisite every time it disappoints you. The point of reviewing the strategy is to learn what is actually helping, what is blocked, and what should change next—not to make the method impossible to disprove." L489: "decide beforehand what small change would tell you it helped".
- Closest article passage: "And if you keep following the reparenting steps correctly without getting the expected results, consider if you have a unique case these steps don't match yet." (When to Change the Strategy)
- Missing: The unfalsifiability caution (doing it correctly is not the same as it working; no new hidden prerequisite after each disappointment; reviewing is for learning, not for making the method impossible to disprove) and deciding beforehand what small change would show the adjusted version helped.
- Record: OWNER-EDITS.json id `wcs-p3-cut` (l.1223): Joel, 2026-10-06 19:04 UTC: “P3 honestly looks like it could be cut.” That paragraph held the trap point (`experiments/t71-guide/TRACE-r4-A.md` item 38). The decide-beforehand sentence was cut by a drafter as a repeat; no OK of Joel's names it.
- Verdict: DECIDED (named for the trap paragraph; the decide-beforehand sentence has no naming OK).

## 22. Guide line 505: PARTLY CARRIED

- Guide: "One episode of voices, paranoia, major loss of reality testing, or a perceptual disturbance that persists beyond the expected intoxication is already enough reason not to retest that substance without professional assessment, even if you later feel stable."
- Closest article passage: "those are signs to reconsider trying the same thing again, and try to figure out why that happened. Don't try again until you understand what would make it safe." (When Escape Leaves Reality Behind)
- Missing: The firm rule that even one such episode is reason not to retest that substance without professional assessment. The article softens it to "reconsider" and "get someone qualified to help" if you can't understand what happened. The rest of L505 is carried. (No amounts or preparation details are involved.)
- Record: OWNER-EDITS.json id `voices-and-warning-signs-20261010` (l.1515): “which replaces the guide's one-episode rule”; Joel, 2026-10-10 19:37 UTC: “no, that's normal to hear voices and lose sense of reality on psychedelics (not as normal for weed tho)... but if you go manic, psychotic ... get super paranoid, or end up worse afteward than before, those are signs to reconsider trying the same thing again, and try to figure out why that happened.” His answer 80.3 A ("77.5yes") added “Don't try again until you understand what would make it safe.” (OWNER-QUESTIONS.md l.255; OWNER-EDITS.json id `joel-88-20261022`).
- Verdict: DECIDED (named).

## The turn-71 list, item by item

The 39 entries of `experiments/t71-guide/COVERAGE-r4-A.md`, and where each stands in the 15:11:38 article. "Carried now" means the turn-71 check listed it as a gap and the live article carries it, mostly through Joel's answers of 2026-10-18 (question 54). "Carried in other words" means the article says the point in other words, so it is not an entry.

| # | Guide lines | Point (turn-71 wording, shortened) | Today |
|---|---|---|---|
| 1 | 17 | Sequence is a provisional synthesis | Entry 1 |
| 2 | 29 | Not stopping being the child; the suggested sentence | Carried in other words: stage 5, "The child isn't pushed away, but doesn't have to run the whole life alone." The suggested sentence is not used (wording) |
| 3 | 37, 39 | Feasting while the baby starves; embodied healing, not an escape hatch | Carried in other words: My Journey, "you're eating all of it yourself while baby you is still starving. Unforgivable." |
| 4 | 53, 301, 335 | Limits on a helper's authority; checks on a conclusion | Carried now: Don’t Give the Inner Adult Away ("they can know things you don't and still be wrong about you"; track record, "Do they respect a no ... what happens when you disagree?"; "Borrow adulthood. Do not surrender it.") |
| 5 | 71 (75 end, 163) | A no to the frame | Entry 2 |
| 6 | 73, 105, 145 | Come outward first; do not test another technique to prove tolerance | Carried now: Before You Try to Go Deep ("come all the way back out first", "Some people try one technique after another instead, to prove to themselves they can take it") |
| 7 | 75 | Last-resort pause; safety forces it; no testing while paused | Entry 3 |
| 8 | 79 | Never bring the child forward, even as a test | Carried in other words: "their little one stays out of it", "before they bring their inner child anywhere near it"; the diagnostic-test line is in entry 4 |
| 9 | 81 | Sovereignty; the opening questions | Carried in other words: Joel's own P2 ("what the identity gets them and what it costs", the sovereign-but-obeying-an-urge line); the residue is in entry 4 |
| 10 | 83 | Not a religion test; helper guardrails | Entry 4 |
| 11 | 91, 93 | Plain analysis is not avoidance; quiet mind | Entry 5 (still not carried) |
| 12 | 107 | "Could you stop and return?" | Carried now: Before You Try to Go Deep |
| 13 | 109 | What to change when calibrating | Carried now: Your Body Might Need Some Love First ("variables like shorter session length, or shallower diving, time of day, keeping eyes open, having a friend around"); the residue is in entry 6 |
| 14 | 133, 135 | Acute versus meaning work | Carried in other words: Catch the Hook ("Maybe forget the parts detective work for a minute. You can figure that out later."; "say no now and work out what it means later") |
| 15 | 137 | Words then versus translation now | Entry 7 |
| 16 | 141 | Do not dismiss genuine attraction as "just intrusive" | Entry 8 |
| 17 | 157 | Choose a realistic outcome | Entry 9 |
| 18 | 161 | Another person is not a reassurance machine; support is normal | Carried now: First Social Connections, Done Right ("Nobody's a reassurance machine."; "In a real crisis, getting a safe person involved can be exactly the right move.") |
| 19 | 167 | Belonging does not make a group good | Carried now: Joel's wording from 54.12 C, "if any group, or any one person, starts acting like they should be your only support, that's where I'd want the Protector paying attention" |
| 20 | 169 | One-line Witness, Protector, Guide triad | Carried in other words: the three jobs appear separately (The Chicken-and-Egg Problem; The Inner Guide); no one-line triad |
| 21 | 173-177 | The caring-editor step; inward care first | Carried in other words: Write It. Don't Send It Yet. |
| 22 | 183 | Test question for revisiting versus reassurance | Entry 10 |
| 23 | 187 | Checking moves into behavior | Carried now: When Healing Turns Into Checking ("A body scan can turn into one, or a confession ... going on a date") |
| 24 | 189 | Exposure, ERP, exploring is not checking | Entry 11 |
| 25 | 223 | The research paragraph | Carried now: When the Adult Voice Feels Fake (compassion-threat studies; the Ideal Parent Figure pilot; "feeling fake could mean you need a bridge") |
| 26 | 233 | What to do when closeness feels intrusive | Carried in other words: Borrow Love ("the way kids squirm away from an aunt they barely know ... don't push it") |
| 27 | 235 | Invent an adult; feeling accompanied | Entry 12 |
| 28 | 241-245 | Fallback question; what to ask the stand-in | The first question is carried in Joel's wording; the fallback question is in entry 12 |
| 29 | 249 | Advice to others runs idealistic | Entry 13 |
| 30 | 253, 255 | The "Big whoop" step; stop re-wording | Entry 14 |
| 31 | 267 | Goodwill is not access | Carried in other words: Just Like Me ("Getting in touch is a separate decision, for a much calmer day"); How to Forgive Without Forgetting |
| 32 | 283 | Prayer that evokes abandonment | Entry 15 |
| 33 | 303 | The signs list | Entry 16 |
| 34 | 305 | "Parent" as the wrong archetype | Carried now: The Chicken-and-Egg Problem ("If the phrase “inner parent” calls up the wrong archetype for you, pick another one.") |
| 35 | 411 | Reminder object is not an oracle | Entry 19 |
| 36 | 451 | Protective purpose is a hypothesis | Carried in other words: Start With Whatever Showed Up (Joel's own text: "propelling you toward, and away from"; "I'd only do it if it's loving and leaves you free. It should make sense, too.") |
| 37 | 481 | Respond to what shifts | Entry 20 |
| 38 | 489, 493 | Unfalsifiability trap; decide beforehand | Entry 21 |
| 39 | 505 | One-episode rule | Entry 22 |

New since the turn-71 list: entries 17 and 18, and entry 6 (a), (b) and (e).

## Also checked, found carried (no entry)

- L11 and L69 (the safety gate): When the Present-Day Adult Is Dangerous to the Child.
- L49: Catch the Hook ("Somebody may really have crossed a boundary") and Altered States Can Require Reparenting ("Loving someone does not mean you leave the front door unlocked").
- L51-55: Don’t Give the Inner Adult Away (the no-self teaching that sounds like "what you want doesn't matter"; a therapist who calls "No, that's not right for me" resistance).
- L89 and L91: You Don’t Need an Inner Monologue ("don't invent one"; small figures on a table).
- L97-99: Your Body Might Need Some Love First (the list of bottom-up therapies).
- L161: First Social Connections, Done Right.
- L199-207: Noticing Counts (the witness, own name, lab studies, "Don't keep drilling it").
- L227-229: Borrow Love ("Just feel that love you can feel for others for a minute, in your body, before you try to redirect anything").
- L265: If the Love Isn't Coming Yet ("Taking the hostility out makes room for warmth"; "People still have to earn your trust").
- L273: Ask God for a Loan ("don't shrink it down to a thought experiment about a friend").
- L315: Borrow Love ("Sometimes show up just to say "I'm glad you're here," and then enjoy them for a minute").
- L321: The Chicken-and-Egg Problem ("a misperception that there is something wrong with the inner child") and You Are Worthy of Love. Always.
- L357: Love Doesn't Have to Wait for Trust ("try not to turn "But I love you" into a line you say on cue").
- L371-375: Instead of Blame.
- L391-393: Love Doesn't Have to Wait for Trust (the "Big fuckity whoopty doo" answer).
- L397: the vow gate has no sentence of its own in Make a Simple Vow. The dangerous-adult section carries the rule that such a person's little one stays out of it, and Joel's 2026-09-25 20:24 UTC decision ("if they fall into the simpler category of people with malice then they are already covered", `experiments/DANGEROUS-ADULT-OWNER-FINAL-P1-20260924.md` l.357) is the record behind scoping the vow gate the same way (l.359).
- L413-415: Remind Yourself (the note on the stuffed animal; "a calm pet").
- L419-433: When the Adult Voice Feels Fake and The Parent You Inherited.
- L439: Start With Whatever Showed Up ("the simpler the better"; "Let a stray thought go as just thinking").
- L467: Start With Whatever Showed Up ("I see you ...") and Hear the Guard First ("borrow it from someone who's been safe for you").
- L509: When Escape Leaves Reality Behind (gentle meditation, the mantra).
- L513-517: Sometimes There Isn't a Clear Child Yet.
- L43, L119, L139, L149-155, L181: carried (My Journey; Catch the Hook; Other Folks Also Have Hooks, "they're allowed to say no to you", "If they promise to change, that's probably as useful as their prior promises were", "get safe first", "Guilt may keep shouting at you"; When Healing Turns Into Checking).
- L491: "the target turns out to be wrong" is one item in a list of reasons to change course; it is not listed as a gap.

## Summary

- **22 entries** (guide lines 1-520). **2 REAL GAP**: entry 3 (L75) and entry 9 (L157). **20 DECIDED**: 13 rest on Joel's naming words, some in part (entries 2, 4, 6, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22); 6 rest on text Joel wrote (entries 1, 5, 7, 8, 10, 15); 1 rests on a general OK (entry 20).
- **Entry 3** is the clear one: Joel's "keep first one" for the last-resort and safety-forces-a-pause sentence was followed, and his own rewrite of that paragraph on 2026-10-22 dropped it without mentioning it. **Entry 9** is minor and borderline: no record ties his rewrite to the sentence, and the question offered to him about it was never answered.
- Weakest DECIDED bases: entry 20 (general OK only); entry 14's L253 half and entry 12's invented-adult idea (they rest on a drafter's reading of Joel's 17:10 comment); the six own-text entries and entry 6's points a, b and e, where Joel's replacement text came first and no word of his weighs the omission. Entry 7 carries a drafter's standing condition to ask him narrowly, never asked.
- **Turn-71 items now carried: 4, 6, 12, 13, 18, 19, 23, 25 and 34** (9 of 39). 11 more are carried in other words (2, 3, 8, 9, 14, 20, 21, 26, 28, 31, 36). 19 are still entries (1, 5, 7, 10, 11, 15, 16, 17, 22, 24, 27, 29, 30, 32, 33, 35, 37, 38, 39). Turn-71 item 11 (L91, L93) is still not carried; it is entry 5.
