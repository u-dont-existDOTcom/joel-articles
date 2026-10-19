# TRACE: PGQ-027 to PGQ-039 (queue version 2026-10-18-r12) against the humanized article

Read-only trace made on 2026-10-19 by the tracing subagent. No repo file was edited; the only files written are this report and the scripts that built it (same folder).

## Sources and method

- Queue: /home/claude/u-dont-existdotcom/innersignalgraph/authoring/PENDING-PUBLIC-GUIDE-CHANGES.md, entries PGQ-027 to PGQ-039 (lines 175 to 278).
- Article: /home/claude/joel-articles/articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md, 1381 lines, md5 f988fd0d6427434972347a4df02d9b7f, last modified 2026-10-19 00:29:55 UTC, unchanged when re-checked at 01:41 UTC.
- Records read (article repo): OWNER-EDITS.json (201 entries), OWNER-QUESTIONS.md (current and its git history), experiments/WHEN-THE-ADULT-VOICE-FEELS-FAKE-20261002.md (turn log), R4-ADDITIONS-PROVENANCE-20261008.md, OPEN-OWNER-FLAGS.md, GUIDE-UPDATE-QUEUE-20261006.md, PARKED-READER-QUESTIONS.md, and Joel's messages in experiments/t44-answers to t76-answers.
- Supplementary records (innerSignalGraph repo, outside the brief's source list, labelled SIB): tasks/*/INTEGRATION.md, state/CODEX-CURRENT-STATE.md, guides/owner-amendments.json. The canonical guide r6 (guides/inner-child-guide-2026-10-11-r6.txt, tag R6) is quoted only to show what a queue entry points at.
- Paragraph numbers follow tools/humanization/para_numbers.py: a paragraph is a blank-line-separated block that is not a heading and not inside an HTML comment; P-numbers restart at every heading of any level. Anchors were taken from a comment-aware index that matches the page numbering (323 paragraphs, 0 differences).
- Quotes: every quotation below was built from the cited file by script (trace_build.py, same folder) and then re-checked in a second pass with a plain substring test against the cited line. 294 quotations checked. A quotation is the exact slice of the source: curly and straight quotes are matched as equal for finding the text, and the text is then printed exactly as the file has it. Ledger quotes are the decoded JSON string (escaped quotes print as plain quotes). A line break inside a wrapped quotation prints as one space.
- Tags: [A:n] visible article text (HTML comments removed), line n. [A-comment:n] raw article line n (an HTML comment). [Q:n] the queue. [OQ:n] OWNER-QUESTIONS.md now; [OQ@commit:n] the same file at a git commit. [TL:n] turn log. [R4P:n] R4-ADDITIONS-PROVENANCE. [OPF:n] OPEN-OWNER-FLAGS. [GUQ:n] GUIDE-UPDATE-QUEUE. [PRQ:n] PARKED-READER-QUESTIONS. [J:file:n] a Joel message file. [OE:n] OWNER-EDITS.json line n. [SIB:path:n] innerSignalGraph file. [R6:n] guide r6.
- Rating: FULL = the whole teaching point is already said. PARTIAL = at least one article sentence carries a piece or a neighbouring version of the point (what is missing is named). NONE = no sentence carries any piece; sentences next to the topic are listed separately and do not count.
- Ledger check: OWNER-EDITS.json has no entry that names any of PGQ-027 to PGQ-039 (searched for the ids), so no article passage is guarded for them. "Joel's own words" below therefore comes from the HTML comments above the paragraph and from ledger entries whose must_contain strings appear in it.

## Not checked

- Joel's own messages on GitHub (innerSignalGraph issues #168, #172, #175, #180 and the comment the PGQ-039 text points to; owner-page questions 31 to 37 and 43): GitHub access to that repo is not enabled here (a request for the #180 comment returned 403). Only the local copies of their content in the innerSignalGraph files above are quoted.
- Joel messages before turn 44 other than as the ledger, the questions page and R4P quote them.
- Whether Joel chose a public figure (PGQ-032), chose to cite Gilbert and Wilson (PGQ-033), or has had legal review done (PGQ-039): no record found in the files above.
- The main session's own drafts for this queue (experiments/t76-guide and rows 3082 to 3096 of tools/PREDICTIONS.md) were not evaluated and are not Joel records.

## Findings that cut across entries

1. Joel's only decision on the queue as a whole is a deferral, then a go-ahead. Question 58 offered `check all 22 against the article and draft the ones it doesn't say yet.` [OQ@0928272a:68] or `Not yet.` [OQ@0928272a:69] He answered `58. b` [J:JOEL-20261018-2158.md:10]; the page recorded `the innerSignalGraph queue waits.` [OQ:63] and `only the innerSignalGraph queue (58, B: not yet) is waiting.` [OQ:23] At 00:55 UTC on 19 Oct he wrote `start workin on the innerSignalGraph queue i guess, altho i already forgot what all that is` [J:JOEL-20261019-0055.md:5]. The turn log's plan line was `With 58, A: innerSignalGraph's PGQ-018 to PGQ-039 (queue r12) against the article.` [TL:968] and its closing line `the innerSignalGraph queue waits (his 58, B)` [TL:998].
2. Joel's standing rule on guide additions that other workers suggest (2026-10-08 02:23 UTC, R4P): `maybe we should somehow implement a rule that guide additions can't be suggested by other owrkers unless they are explained, what map change caused them, and how they are really needed vs superfluous to the guide.` [R4P:9] On the same subject he cut an earlier draft (the provenance table row: `Depth 1 ("That means turning the depth down…") | #126, CONTINUITY_TITRATION | **cut** (Joel, 02:23)` [R4P:56]), and the questions page records `you'd cut it on 2026-10-08` [OQ:97].
3. Shared slots: PGQ-027 and PGQ-029 go in the same place (after Urge-to-Escape P1, line 681). PGQ-030 and PGQ-039 go in the same place (after Also Look Outward P10, line 213). PGQ-031, 033 and 034 are all in Ask God for a Loan, which is Joel's own text. PGQ-037 and 038 are meant to be written together (Q:258 and Q:265).
4. Anchors named by the queue that do not exist in the article: the "paragraph on severe physical pain" (no hit in the visible article for physical pain, severe pain, chronic pain, ambulance, analges, pain relief, pain clinic, unbearable); "The Three Adult Functions" (dissolved by Joel: `16:29` [OE:256] and `The Three Adult Functions: dissolved.` [OPF:13]); "Make the Protector Visible" as a heading (the article's section is Not Every Hero Wears A Cape); "Afterward, notice where the access actually is" and "The beautiful state can become a hook too." (neither sentence is in the article; the queue's own wording for the second is the guide's, `The beautiful state can become a hook too.` [R6:859]).
5. The guide's permission not to label the work reparenting, which PGQ-037 and PGQ-038 say to keep, is not in the article: the guide has `If it does not, there is no need to label it that way.` [R6:165] and the article's Also Look Outward isolation paragraph (line 207) stops before it. The nearest article sentence about labels is in the Chicken-and-Egg section: `If the word "parent" calls up the wrong archetype for you, pick another one.` [A:39]
6. Who writes what, by the queue's own words: PGQ-034, 035 and 036 are the owner's to write himself. PGQ-031 is already the owner's text. PGQ-032, 037, 038 and 039 ask for one or two sentences in the owner's voice (039: also legal review). PGQ-027, 028, 029, 030 and 033 name no writer.

---

## PGQ-027 - Short relief must not perpetuate severe pain

At a glance: anchor found (Urge to Escape P1, line 681) | coverage NONE | Joel's own paragraph at the anchor: no | Joel decision record on the subject: none | who writes it: not stated.

**1. Anchor.**
- Queue "Where": `"When the Urge to Escape Arrives", immediately after the note about seeking support when the material exceeds capacity.` [Q:180]
- Found: yes. The note is the last sentence of the first paragraph under the heading: `If it's more than you can hold right now, I'd get someone steady with you.` [A:681] The insertion point is between that paragraph and the next one (line 691). Anchor detail: heading path `# When the Adult Voice Feels Fake > ## Start With Whatever Showed Up > ### When the Urge to Escape Arrives`; paragraph P1; article line 681; first 15 words `Sometimes the urge to get away from what's coming up gets a lot bigger. All` [A:681].
- Joel's own words at the anchor: no. The comment above the h3 says `so P1 carries only what's new` [A-comment:675] and the turn log says `P1: only what the dedup found new: the bigger forms (a drink, the ex, a new business), that it can be progress, and thanking the part with the escape plan;` [TL:506] Ledger check: no OWNER-EDITS.json entry has a must_contain string (20 characters or more) in this paragraph.

**2. Already said? NONE.**
- The four parts of the teaching point are `During an unbearable physical-pain episode, caring for yourself may mean contacting local urgent medical services for assessment and possible pain relief` [Q:177], `even when earlier investigations found no clear answer` [Q:177], and `rather than relying on a short-lived strategy known to worsen your condition.` [Q:177] No article sentence carries any of them.
- Next to the topic, not counted: `All of a sudden you need a drink, or that ex doesn't seem so bad after all.` [A:681] (an escape urge, nothing about pain or harm); `Same with something a doctor should look at.` [A:613] (about anxiety's guesses); `Same if something might be dangerous right now, or might be a medical warning sign: step away or get checked first.` [A:167] (a medical warning sign, no pain, no urgent service); `A few hours of feeling lighter, with the old feeling back the same day, is a few hours of relief.` [A:663] (the queue's own "Match the claim to the duration": it says take the relief, not that a habit worsens the condition); `Get professional help right away if any of this is severe or risky` [A:709] (about drug reactions).
- Missing: all of it (unbearable physical pain; local urgent medical services for assessment and possible relief; earlier investigations finding nothing; a short relief known to make things worse). The queue also says to keep the safeguard `Keep ordinary immediate-safety safeguards when intent or incapacity changes.` [Q:179]

**3. Records.**
- Direct record of Joel deciding, cutting or saying he would write something on this subject: none found (searched pain, analgesia, urgent, emergency, chronic, specialist and the rest of the term list in the ledger, the questions page and its history, the turn log, R4P and every t44 to t76 answer file; the only pain hit in the ledger is about emotional pain).
- Next to it, same section and same kind of advice. On "get checked" in this h3: `i can't say what someone should do, it's a caution sign, they need to figure it out, if they can't figure it out they should seek help from trusted advisors.` [OE:1650] and `what the heck does that mean?` [OE:1650] and `there's literally nobody who can tell anyone what is best for them. there are just caution signs.` [OE:1650] The page recorded it as `in P8, with no "get checked" and no "go gentler".` [OQ:267]
- On calling outside services: `13. leave it. i also don't recommend calling the cops for safety reasons at all.` [OE:1882] and the page's `"13. leave it.": the cops line stays as it is. Your reasons are noted, not for the text.` [OQ:245] The questions page that asked it stated Claude's own rule, set after his 21:10 point: `I don't offer advice you haven't given` [OQ@c25feb17:12].
- Joel on "help counts": `i'm not sure how 'getting help counts' adds something to 'get safe'` [PRQ:65]
- Supplementary (map-side, marked owner-approved in the file): `Respect established unsuccessful medical consultations, never re-offer harmful short-term self-medication, and consider appropriate live emergency/urgent pain-care triage without promising transport, drugs or cure.` [SIB:guides/owner-amendments.json:333]

**4. The queue's own note.** The entry names no writer and no owner choice. Its cause line: `owner outcome: offer a feasible acute-pain alternative when previous care did not settle the cause and known self-medication causes further harm.` [Q:176]

---

## PGQ-028 - Support is not a shortcut to romantic intimacy

At a glance: anchor found (Borrowed Adulthood in Relationship, after P1, line 1238) | coverage PARTIAL | Joel's own paragraph at the anchor: P1 no, the next paragraph (P2) yes | Joel decision record: he cut his own dating sentence from Also Look Outward | who writes it: not stated.

**1. Anchor.**
- Queue "Where": `"Borrowed Adulthood in Relationship", after the introductory paragraph.` [Q:187]
- Found: yes. The introductory paragraph is P1. Anchor detail: heading path `# Borrowed Adulthood in Relationship`; paragraph P1; article line 1238; first 15 words `Reparenting is usually talked about as something you do alone, or with a therapist. But` [A:1238]. The new text would sit between it and P2, which starts `Say they're the one who always remembers your appointments.` [A:1242]
- Joel's own words: P1 no, it is Claude's (`my own draft (writers/ba1p1-w8-p1; GROUNDING-ba01.md)` [A-comment:1236]). P2 is Joel's, word for word (`Borrowed Adulthood in Relationship P2 is Joel's, word for word (question 33, A), after P1 (ba1p1-w8-p1).` [OE:2336]; his words `this version passes` [OE:2337]). Ledger check: OWNER-EDITS.json entries with strings in this paragraph: `ba-p2-joel-20261017` (applied, 1 of 1 strings, [OE:2334]).

**2. Already said? PARTIAL.**
- Teaching point: `Friendship and reliable support can grow while active romance-seeking is paused.` [Q:184] and `Romantic or sexual intimacy arises through mutually wanted, genuine connection` [Q:184] and `not as rescue from suffering, a badge of worth, or a reward for healing.` [Q:184]; reader need includes `another reader might wrongly infer everyone must become perfectly healed before ever dating.` [Q:185]
- Carried in part: `Meeting them can turn into a kind of test--"First impressions are everything," as they say, but it could be even worse than that, if you need them to prove you're lovable.` [A:203] and `Leaning on each other is still a big part of relationships, and it goes both ways.` [A:203] (support is part of relationships; romance as a proof of being lovable). `Even, going on a date, or checking your dating profile matches, can be a version of this if what you're really after is proof that you're good and lovable.` [A:250] (dating as a search for proof). `Do you have to get yourself sorted out first, so you'll be better company? I really don't think so.` [A:207] (reaching toward people without waiting to be sorted; not about romance).
- Missing: that support can grow while romance-seeking is paused; that intimacy is not a rescue from suffering and not a reward for healing; that nobody must be perfectly healed before dating; that intimacy comes from both people wanting it.
- Note: the queue says `Existing reciprocal-practice and earned-trust guidance warns against romantic self-testing.` [Q:186] That is the line-203 paragraph; the sentence that named dating there was cut (see Records).

**3. Records.**
- Joel cut his own dating sentence from Also Look Outward: the comment above line 203 says `54, 4 and 6: his "If the real reason you're asking someone out is to prove you're lovable, or that you're sure what you want, then they've become part of the test." is out` [A-comment:201]. His message: `4keep first instance, remove 2nd one in also look outward. 5. a 6 merge them` [J:JOEL-20261018-1906.md:50] The page: `your dating sentence is out of Also Look Outward, with the reassurance machine merged into that paragraph` [OQ:85] And the date now sits in his own paragraph in When Healing Turns Into Checking (ledger `62c it's human now, i fixed it, pasted.` [OE:2644]), quoted above at line 250.
- Joel's romance guide: `I also have a romance guide i could link to at romance.u-dont-exist.com (link works even if not for you).` [OE:433] The article links it at line 193.
- Direct record of Joel deciding anything about support versus romantic readiness: none found.
- Supplementary (marked owner-approved): `support that bounded decision and cultivate honest, reciprocal connection without promising that romantic intimacy is earned, owed or curative, or imposing a universal perfect-healing prerequisite.` [SIB:guides/owner-amendments.json:339]

**4. The queue's own note.** No writer and no owner choice named. Cause line: `owner outcome: preserve a case-specific choice to defer romance while building honest reciprocal connection, without implying intimacy is owed or healing guarantees it.` [Q:183]

---

## PGQ-029 - A chronic pain pathway, not daily emergency calls

At a glance: anchor not in the article (the severe-pain paragraph it follows does not exist); nearest place is Urge to Escape P1, line 681 | coverage NONE | Joel's own paragraph there: no | Joel decision record: none | who writes it: not stated.

**1. Anchor.**
- Queue "Where": `When the Urge to Escape Arrives, immediately following the paragraph on severe physical pain; compress any France-only example without losing the conditional status.` [Q:197]
- Found: no. The paragraph on severe physical pain is what PGQ-027 would add, and it is not in the article (see finding 4). Nearest place: the same spot as PGQ-027, after the first paragraph under the heading. Anchor detail: heading path `# When the Adult Voice Feels Fake > ## Start With Whatever Showed Up > ### When the Urge to Escape Arrives`; paragraph P1; article line 681; first 15 words `Sometimes the urge to get away from what's coming up gets a lot bigger. All` [A:681].
- Joel's own words there: no (Claude's; see PGQ-027).

**2. Already said? NONE.**
- Teaching point: `Severe frequent pain deserves a continuing specialist treatment pathway and a written plan for predictable flares, with acute services as a proportionate backup.` [Q:194] `Prior normal tests need not make pain imaginary.` [Q:194] `In France a doctor can request SDC assessment and justify a priority referral if warranted; no guaranteed appointment or medication.` [Q:194]
- No article sentence carries any of it. The sentences next to the topic are the ones listed under PGQ-027 (`Same with something a doctor should look at.` [A:613], `Same if something might be dangerous right now, or might be a medical warning sign: step away or get checked first.` [A:167]); neither mentions pain, specialists, a written plan, or France.
- Missing: all of it.

**3. Records.**
- Direct record of a Joel decision on chronic pain care: none found. Next to it: the "get checked" ruling, the cops-line ruling and the "getting help counts" remark quoted under PGQ-027 apply here unchanged. The ruling that matters most for wording: `there's literally nobody who can tell anyone what is best for them. there are just caution signs.` [OE:1650]
- Supplementary (marked owner-approved, approvedAt 2026-10-11): `prioritize a feasible referral to specialist chronic pain care, a clinician-justified urgency request when local policy allows, and a written flare protocol instead of treating repeated emergency visits as a long-term strategy.` [SIB:guides/owner-amendments.json:345] The state file records the owner outcome as `Owner outcome: replace routine repeated ambulance/psychiatric-disclosure suggestions for disabling recurrent pain after prior failed or harmful interventions with sustained access to a chronic-pain specialist and a written flare plan.` [SIB:state/CODEX-CURRENT-STATE.md:127]

**4. The queue's own note.** No writer and no owner choice named. The editing instruction is `compress any France-only example without losing the conditional status.` [Q:197] The cause line says `This corrects advice that treated nearly daily severe pain as though each familiar attack should be handled by an ambulance visit.` [Q:193]

---

## PGQ-030 - Protective medical agency after coercive or harmful care

At a glance: anchor found (Also Look Outward P10, line 213) | coverage PARTIAL | Joel's own paragraph at the anchor: no (Claude's, approved by Joel) | Joel decision record: approved the paragraph this follows; cops-line ruling; none on this subject | who writes it: not stated.

**1. Anchor.**
- Queue "Where": `Also Look Outward, following the paragraph on safe graded disclosure and before general relationship/community support.` [Q:204]
- Found: yes. The graded-disclosure paragraph is P10; the community paragraph after it starts at line 217. Anchor detail: heading path `# Before You Try to Go Deep > ## Your Body Might Need Some Love First > ### Also Look Outward`; paragraph P10; article line 213; first 15 words `And reaching out doesn't mean telling strangers everything. Privacy isn't fakery. People can earn more` [A:213].
- Joel's own words: no. It is Claude's PGQ-003 paragraph (C2) that Joel approved: `Joel's yes to C2 (queue item PGQ-003, my turn-34 draft) after his C1, at the end of Also Look Outward, unchanged.` [OE:1418] with his words `C2 looks fine` [OE:1419]; a later comment says Claude changed one scene in it for the detector: `so "how they handle the smaller things you tell them" gets a scene; the rest is as it was.` [A-comment:211] Ledger check: OWNER-EDITS.json entries with strings in this paragraph: `c2-after-c1` (applied, 2 of 4 strings, [OE:1416]); `t1-t9-teaching-points` (applied, 1 of 19 strings, [OE:1432]).

**2. Already said? PARTIAL.**
- Teaching point: `A history of harmful treatment changes who is safe to approach and what information to share.` [Q:201] `Trusted voluntary support and a chosen advocate may be better than default family involvement or repeated psychiatric pathways.` [Q:201] `Pain-triggered fleeting thoughts must not be presented as a plan or a bargaining strategy for analgesia; actual imminent danger still warrants immediate protection.` [Q:201]
- Carried in part: `Privacy isn't fakery.` [A:213] and `(If telling could put you in real danger, like violence, or being outed where that isn't safe, protect yourself first.)` [A:213] (what to share depends on who is safe; unsafe relationships, not medical care). `By trusted, I mean someone you know is trustworthy from a long relationship with them` [A:707] (Joel's; choosing trusted advisors, in the drug section). `instead of taking me to a psychiatrist and pumping me full of anti-psychotic drugs, they put bars on the windows.` [A:1132] (Joel's own story: he trusted his parents with the information, and psychiatric drugs were the harm he was spared). `A crisis line or an emergency number counts, and the person on the other end can be a total stranger.` [A:1068] and `move away from that open window and get some outside support.` [A:1170] (immediate danger still means protection). `while without trance you can "freak out" in a way that might end up getting you committed to a mental hospital, thrown out of your housing, going to jail, possibly even killing yourself.` [A:1146] (Joel's trance note: being committed is named as a harm).
- Missing: that earlier harmful or coercive care changes who is safe to approach in medical settings; a chosen advocate in place of default family or the same psychiatric pathway; that pain-triggered thoughts are not a plan and not leverage for pain relief.

**3. Records.**
- Direct record of Joel deciding, cutting or saying he would write this: none found.
- Joel approved the paragraph this would follow (`C2 looks fine` [OE:1419], ledger line shown above).
- His own words on the neighbouring subject of police and outside services: `13. leave it. i also don't recommend calling the cops for safety reasons at all.` [OE:1882] and `just don't call the cops and expect it to go well in general, that's a real last resort.` [OE:1796] The article has `In general, don't call the cops and expect it to go well. That's a real last resort.` [A:701]
- His own words on psychiatric care appear in the article's Altered States section (line 1132, quoted above), which the ledger lists as `43 my words. except the last one about voice or urge directing you towards harm, that's therapy speak from AI based on my story, but it's ok if it passes.` [OE:2428] The "move away from that open window" sentence (line 1170) is the guide's wording, which he allowed ("ok if it passes").
- Joel's trance note, which is where the article's line about being committed comes from (2026-10-12 03:13 UTC): `in a way that might end up getting you commmitted to a mental hospital thrown out of your housing, going to jail, possibly even killing yourself.` [OE:1965]
- Supplementary (marked owner-approved, approvedAt 2026-10-11): `When prior psychiatric or medical care was experienced as coercive or traumatic, weigh the real potential for iatrogenic harm and preserve choice of a trusted voluntary advocate` [SIB:guides/owner-amendments.json:352] and `Never recommend suicidal disclosure as a tactic for analgesia, but do not coach falsely denying current suicidal intent` [SIB:guides/owner-amendments.json:352]

**4. The queue's own note.** No writer named. The cause line says `The owner clarified that previous psychiatric care can create real anticipated harm.` [Q:200] No owner choice named.

---

## PGQ-031 - Gratitude is essential ongoing cultivation; the child is not required to perform it

At a glance: anchor found (Ask God for a Loan, Joel's own text) | coverage FULL for the progression and the "essential, ongoing" sentence, PARTIAL for the guardrail sentences | Joel's own paragraph at the anchor: yes, word for word | Joel decision record: he wrote the section; he ruled two lines in it "not a repeat" | who writes it: already the owner's text; the queue says do not duplicate or rewrite.

**1. Anchor.**
- Queue "Where": `“Ask God for a Loan” (the existing owner-edited passage).` [Q:214]
- Found: yes, the whole section. The paragraph the entry's "one practical door" refers to is the first one under the h4. Anchor detail: heading path `# Borrow the Adult Before You Can Be the Adult > ## Borrow Love—or Borrow the Perspective of Care > ### Ask God for a Loan > #### Your Loan is PRE-APPROVED!`; paragraph P1; article line 366; first 15 words `One practical door anyone can use to slowly experience divine love is gratitude (even after` [A:366].
- Joel's own words: yes, word for word. `Joel's updated Ask God for a Loan, word for word` [A-comment:356]; ledger `Ask God for a Loan, Joel's updated section, word for word` [OE:2177] and `Ask God for a Loan, the gratitude paragraph "This is a bit tricky to put into words…": Joel's new sentence before its last, word for word.` [OE:2241] Ledger check: OWNER-EDITS.json entries with strings in this paragraph: `ask-god-update-20261014c` (applied, 1 of 7 strings, [OE:2175]).

**2. Already said? FULL (progression, essential ongoing) / PARTIAL (guardrails).**
- Step 1, ordinary good and relief: `If you have a moment right now to breathe, that’s something to be grateful for.` [A:372] and `I don’t always remember to say “thank you” when I pee now, but I try.` [A:372]
- Step 2, grateful even for suffering: `And even (or especially) when I am suffering, I try to remember to be grateful for that also, because if not for suffering, I would not even think about how much I have enjoyed not suffering as much, and how much it will help me to develop more compassion, wisdom, and gratitude in future.` [A:374]
- Step 3, notice whether it opens the heart, not a reframing: `Notice how, when you offer thanks (to the universe, to life, to God, whatever you may believe in), a space in your heart opens up.` [A:378] `There’s a tiny bit of freedom, of peace, stillness, softness.` [A:378] `I’m not talking just about changing your “glass half empty” perception to a glass “half full perception.”` [A:370]
- Step 4, invite the younger self, listen to refusal: `Once you start to feel that lovely softness of the heart, invite your little one in with you as your spiritual integration practice. They might go numb, or call BS on that.` [A:380]
- Essential and ongoing, not an optional door: `And gratitude isn’t just one way to experience divine love for the first time, or to get it back when the feeling fades. I think it’s essential if we want to live in that love instead of occasionally visiting it.` [A:366]
- Compassion for suffering beings and care for the inner child: `It connects me with the plight of the countless other beings suffering at that very moment, authentically bringing up a wellspring of compassion in my heart for all of us. And I see clearly that it is my inner child who is feeling this pain, and what an honor it is that I can be there for him.` [A:374]
- Guardrails, partly: `Of course, that’s not to say you should not try to suffer less.` [A:376] (not declining care or relief); `It might not feel immediately like you suddenly know the real meaning of Divine Love, but it’s a little spark of … something....` [A:378] (no feeling on demand, no guarantee).
- Missing: no one is required to thank an abuser or excuse harm (nothing in the section; the h3 after it says `But if you let an abuser control your appreciation of life, then you've given them an unearned win.` [A:384], which is a different point); "ongoing intention is not forcing a feeling" is only implicit; "neither felt love nor child inclusion is guaranteed" is only implicit in lines 378 and 380.
- Flag only (Joel's own wording, so not to be changed): `If so, they might just need to see if you're actually humble enough, and grateful enough for them, to listen to their rejection and be patient.` [A:380] sits against the entry's `Do not claim the child is knowingly testing the adult, and do not demand gratitude from the child.` [Q:210]

**3. Records.**
- Joel wrote the section himself and said why: `ok btw i'm replacing the ask god for a loan section with this, because i realized i never explained the importance of gratitude in finding love` [OE:2118]; then `i updated my ask god section, here's the latest` [OE:2178]; then `btw i changed this paragraph in gratitude section` [OE:2242]. The page: `Your updated Ask God for a Loan ("i updated my ask god section, here's the latest"): in, word for word.` [OQ:194]
- Joel cut: `24 you can cut botth mr rogers because i also have that before. can keep 2nd mention of spiritual love in Ask God...` [J:JOEL-ANSWERS-20261014-1951.md:41] (ledger `Borrow One Competency at a Time: both Mr. Rogers sentences cut (the Chicken-and-Egg section has him already), and with P3's, its spiritual love (Ask God for a Loan has it).` [OE:2215]).
- Joel ruled on repeats inside this section: `well i wouldn't say that fits the repeats problem. the first one is saying what we should want, the 2nd one is talking about being grateful if you know that` [J:JOEL-20261015-1215.md:5]; the page: `Your new gratitude sentence and the Biggie Smalls line: not a repeat` [OQ:182]. The roselle line: `i did mention bilharzia not just any old peeing blood issue` [OE:2133], page `The roselle tea line stays` [OQ:201]. The queue's evidence boundary is met by the text at `Miraculously, I then found some obscure ethnobotanical research` [A:372] through `Within an hour, I was cured.` [A:372]
- Supplementary: `The owner reports the public section has already been edited; the future humanizer should compare and mark incorporated,` [SIB:tasks/gratitude-love-child-20261014/INTEGRATION.md:12] and `The public article is owner-authored and isn't rewritten;` [SIB:state/CODEX-CURRENT-STATE.md:122]

**4. The queue's own note.** The text is already the owner's: `Preserve the latest exact owner text and voice.` [Q:212] The proposal must be `A minimal proposal should make the continuing necessary practice explicit without a sermon, and` [Q:212] must not duplicate the section; the humanizer's job is `disposition this entry as already incorporated when verified, not overwrite it with generic AI prose.` [Q:212] No owner choice named.

---

## PGQ-032 - A drug peak that changes nothing

At a glance: anchor not in the article as worded; the paragraph that stands for it is Altered States Can Deepen the Therapy P4, line 1118 | coverage PARTIAL | Joel's own paragraph there: no (Claude's pointer, which Joel kept) | Joel decision record: kept the paragraph ("50. keep all except for 4."); none on the public figure | who writes it: the owner's voice; public figure is his choice.

**1. Anchor.**
- Queue "Where": `“Altered States Can Deepen the Therapy,” right after the paragraph that begins “The beautiful state can become a hook too.” One or two sentences in the owner's voice. The owner's own example named a public figure; whether to name one is his choice.` [Q:221]
- Found: no sentence "The beautiful state can become a hook too." in the article. The paragraph that does that job (the beautiful state as a hook, in the guide's order) is P4. Anchor detail: heading path `# Altered States Can Deepen the Therapy`; paragraph P4; article line 1118; first 15 words `Jack Kornfield has a whole book on what comes next, [After the Ecstasy, the Laundry](https://jackkornfield.com/after-the-ecstasy-the-laundry/).` [A:1118]. The comment above it says `the guide's next-to-last paragraph of this h1, the beautiful state as a hook` [A-comment:1116].
- Joel's own words: no, Claude's (`It opens on a pointer of mine to a book on just this` [A-comment:1116]). Ledger check: no OWNER-EDITS.json entry has a must_contain string (20 characters or more) in this paragraph.

**2. Already said? PARTIAL.**
- Teaching point: `The owner's example: someone who wants enlightenment together with money, partners and everything else, as one package, can reach a drug peak (ketamine, say) without letting go of a single attachment or of the anger.` [Q:218] `A peak reached that way is not the unconditional love the practice is after, and wanting everything is the conditional gratitude the practice works on.` [Q:218] `Help readers see it for themselves rather than preach it.` [Q:218]
- Carried in part: `That night can't be the bar for every morning after, or regular life starts to feel like failing. And gorgeous as it was, it doesn't mean you're done healing.` [A:1118] (a peak is not the finish). `People very often believe you need a huge dose of it for a "full release." They go through all kinds of screaming and shaking, nearly killing themselves, with absolutely zero inner-child work being done. It's all spiritual bypassing.` [A:695] (Joel's: a drug peak with no inner-child work; the same paragraph also mentions ketamine, in a parenthesis). `The question afterward is whether it made your love deeper or wider.` [A:876] (Joel's test for an opening). `But then I squandered the opportunity to bring that love down from the heavens to my inner child` [A:693] (Joel's own peak that did not reach the child).
- Missing: wanting everything as one package; a peak reached without letting go of attachments or anger; that this is conditional gratitude; that such a peak is not the unconditional love.

**3. Records.**
- Joel kept the paragraph: `50. keep all except for 4.` [J:JOEL-20261018-1906.md:24] Question 50, item 2, was `Jack Kornfield has a whole book on what comes next, [After the Ecstasy, the Laundry](https://jackkornfield.com/after-the-ecstasy-the-laundry/).` [OQ@7410c7ac:65]; the page: `1, 2, 3, 5 and 6 stay.` [OQ:80]
- Joel's own words on ketamine and peak drugs, already in the article: `i'd say one of the most abused psychedelics (aside from ketamine if you call that a psychedelic)` [OE:1480]
- The public figure: no record of whether he chose to name one (his 14 Oct 23:26 UTC answer is on the owner page, not checked).
- Supplementary (marked owner-approved, approvedAt 2026-10-14): `Help people see for themselves by asking rather than preaching, for example whether they would be happy if they had everything they want.` [SIB:guides/owner-amendments.json:366]

**4. The queue's own note.** `One or two sentences in the owner's voice. The owner's own example named a public figure; whether to name one is his choice.` [Q:221] Owner choice named: whether to name a public figure.

---

## PGQ-033 - "If only I had X"

At a glance: anchor found (Ask God, gratitude part; line 370 chosen) | coverage PARTIAL (weak) | Joel's own paragraph at the anchor: yes | Joel decision record: ruled the nearby lines "not a repeat"; none on the survey or the citation | who writes it: not stated; source citation is the owner's choice.

**1. Anchor.**
- Queue "Where": `“Ask God for a Loan,” next to the gratitude part of the owner's October 14 revision of that section.` [Q:228]
- Found: yes. The gratitude part runs from line 366 to 378. The paragraph about thankfulness for good things only is the second one under the h4. Anchor detail: heading path `# Borrow the Adult Before You Can Be the Adult > ## Borrow Love—or Borrow the Perspective of Care > ### Ask God for a Loan > #### Your Loan is PRE-APPROVED!`; paragraph P2; article line 370; first 15 words `This is a bit tricky to put into words, but let me try anyway… You` [A:370].
- Joel's own words: yes, word for word (`btw i changed this paragraph in gratitude section` [OE:2242]). Ledger check: OWNER-EDITS.json entries with strings in this paragraph: `gratitude-sentence-joel-20261015` (applied, 1 of 1 strings, [OE:2239]).

**2. Already said? PARTIAL (weak).**
- Teaching point: `Gratitude that waits for conditions never arrives.` [Q:225] `When someone says they could be grateful “if only I had X,” ask what they would need before they could feel love or gratitude, and whether that list ever ends.` [Q:225]
- Carried in part: `We still need to remember that if we can only be thankful for the good things we have, we can fall into the trap of thinking that what we have is happiness itself.` [A:370] (thankfulness tied to having good things is a trap). `If you have a moment right now to breathe, that’s something to be grateful for.` [A:372] (a gratitude that needs no condition). `If you, like Biggie Smalls, have come to understand that having money is not real happiness, that’s a big deal! That’s something to be grateful for.` [A:376]
- Missing: the "if only I had X" case; asking what they would need first; asking whether the list ever ends; any source (survey or Gilbert and Wilson).
- A mismatch in the queue's own note: it says `“Four Pairs That Commonly Hook the Child” (“Notice when they have become conditions for having a self”) covers pleasure, praise, gain and belonging becoming conditions for a self` [Q:227] but the quoted sentence is not in the article; the meaning is at `The question is whether losing one of them would feel like losing yourself.` [A:780]

**3. Records.**
- Joel's ruling on the two neighbouring lines (the "what we have is happiness itself" sentence and the Biggie Smalls line): `the first one is saying what we should want, the 2nd one is talking about being grateful if you know that` [J:JOEL-20261015-1215.md:5]; the page: `not a repeat` [OQ:182]; the turn log: `His ruling: the gratitude sentence and the Biggie Smalls line aren't a repeat.` [TL:764]
- The survey and the Gilbert and Wilson (2000) citation: no record of any Joel decision (searched miswant, Gilbert, survey in the ledger, the questions page, the turn log, R4P and the answer files: no hits). His recall of the survey is in the queue only.
- Supplementary (marked owner-approved, approvedAt 2026-10-14): `then ask what they would want before they could feel love or gratitude, and whether that list ever ends ('if only I had X')` [SIB:guides/owner-amendments.json:366]

**4. The queue's own note.** No writer named. Owner choice named: `The owner recalls a survey in which almost nobody wished for happiness directly; no source has been found for it, so don't cite it unless one turns up.` [Q:225] and `can be cited instead if the owner wants a source.` [Q:225] (Gilbert and Wilson, 2000).

---

## PGQ-034 - Bringing gratitude in without pushing it

At a glance: anchor found (Ask God, after the gratitude part; after line 378) | coverage PARTIAL | Joel's own paragraph at the anchor: yes | Joel decision record: said on 15 Oct he will write it himself; no later change to Ask God found | who writes it: the owner.

**1. Anchor.**
- Queue "Where": `“Ask God for a Loan,” after its gratitude part. The owner said on October 15 that he will write the guide changes himself.` [Q:235]
- Found: yes. The gratitude part ends with the "Notice how..." paragraph; the next paragraph (line 380) turns to the little one. Anchor detail: heading path `# Borrow the Adult Before You Can Be the Adult > ## Borrow Love—or Borrow the Perspective of Care > ### Ask God for a Loan > #### Your Loan is PRE-APPROVED!`; paragraph P6; article line 378; first 15 words `Notice how, when you offer thanks (to the universe, to life, to God, whatever you` [A:378].
- Joel's own words: yes, word for word. The comment above the section says `Joel's updated Ask God for a Loan, word for word` [A-comment:356], and the ledger entry for that update lists a link that sits in this paragraph: `[A. Helwa’s book](https://authorahelwa.com/)` [OE:2187].

**2. Already said? PARTIAL.**
- Teaching point: `Gratitude is brought in sideways and at times, not pushed, because pushing meets resistance; if someone keeps resisting, “we can come back to this later, now may not be the time.”` [Q:232] `The owner's questions show the kind of question to ask, not a script.` [Q:232] `The author shares how much gratitude helps him rather than prescribing it.` [Q:232]
- Carried in part: `is not about imposing some kind of “spiritual discipline.”` [A:374] (not imposed). `I’m not pushing “toxic positivity.”` [A:370] (his stance, not the reply to someone who says gratitude is toxic positivity). `I don’t always remember to say “thank you” when I pee now, but I try.` [A:372] (he shares his own practice). `I hope you are able to experience this when you try it out for a while, and I’d really love to know how it works for you!` [A:378] (an invitation).
- Missing: bringing it in sideways and only at times; "we can come back to this later"; the example questions ("my life is hell", peace in this exhale, a partner, a love felt now); the reply to "toxic positivity"; working toward a contradiction like "I love everyone, I just hate my dad" from the love side. The queue says the same: `neither shows how to bring gratitude in without pushing, the example questions, the answer to toxic positivity, or working toward a contradiction from the love side.` [Q:234]

**3. Records.**
- Joel said he will write it: the queue itself, `The owner said on October 15 that he will write the guide changes himself.` [Q:235]; supplementary: `He said he will write the public-guide changes himself.` [SIB:tasks/gratitude-how-20261015/INTEGRATION.md:8] and `He writes the public-guide changes himself; the pending queue records them (PGQ-034, PGQ-035).` [SIB:state/CODEX-CURRENT-STATE.md:96] His own message is on the owner page (GitHub), not checked.
- Has he written it? No record of it. The last ledger entry for Ask God is his 10:43 UTC sentence on 15 Oct (`btw i changed this paragraph in gratitude section` [OE:2242]). The supplementary note gives no time for his statement; it places it after his 10:28 UTC message and his 11:19 UTC answers: `the owner said on 15 Oct 2026 at 10:28 UTC how he brings gratitude in, and asked for critiques. At 11:19 UTC he answered question 34` [SIB:tasks/gratitude-how-20261015/INTEGRATION.md:5-6]. Nothing about sideways introduction or example questions has been added to the section since his 10:43 UTC sentence.
- Supplementary (marked owner-approved, approvedAt 2026-10-15): `He tries not to push gratitude, because pushing meets resistance` [SIB:guides/owner-amendments.json:373]

**4. The queue's own note.** The owner writes it: `The owner said on October 15 that he will write the guide changes himself.` [Q:235] No other owner choice named.

---

## PGQ-035 - Gratitude in a calm altered state

At a glance: anchor not in the article as worded (nearest: Altered States Can Deepen the Therapy P3 and P4, lines 1114 and 1118) | coverage NONE | Joel's own paragraph there: no | Joel decision record: "will write this himself" | who writes it: the owner.

**1. Anchor.**
- Queue "Where": `“Altered States Can Deepen the Therapy,” near the “Afterward, notice where the access actually is” paragraph. The owner will write this himself.` [Q:242]
- Found: no. `“Altered States Can Deepen the Therapy” says what to notice afterward (“Afterward, notice where the access actually is…”)` [Q:241] but that sentence is not in the article. The nearest places are P3 and P4 of that h1. Anchor detail: heading path `# Altered States Can Deepen the Therapy`; paragraph P3; article line 1114; first 15 words `Now, the beautiful stuff. Say one night (on a psychedelic, in a dream, ten days` [A:1114]. P4 is the Kornfield paragraph at line 1118 (see PGQ-032).
- Joel's own words there: no (both are Claude's; P4 is the Kornfield pointer Joel kept).

**2. Already said? NONE.**
- Teaching point: `In an altered state that is calm (clear-headed, safe, medically fine), gratitude can be practiced as it is sober.` [Q:239] `While the state is overwhelming, settling comes first; with impaired capacity or a medical concern, safety and care come first.` [Q:239]
- Gratitude and thanks in the visible article: Ask God for a Loan (lines 366 to 380) and a callback at line 1288 (`the Divine Love that can start as a little spark of … something when you give thanks` [A:1288]). Unrelated uses of the word: `And don't expect a thank-you for the session, like they booked it.` [A:314] and `The thank-you you weren't waiting for might not come anyway.` [A:322] (the little one's thanks), `Thank you. Thank you for that perspective.` [A:452] (the Mr. Rogers scene) and `I'd thank whatever part of you came up with the escape plan, and slow down.` [A:681] None of the three Altered States sections (the h1 at line 1102, the h2 at line 1124 and the h4 at line 1172, lines 1102 to 1176) mentions gratitude or thanks.
- Next to the topic, not counted: `Remember those guards from the urge to escape? Same deal here, so get enough Nurturer and Protector in the room before you go deep.` [A:1110] and `I'd learn to do inner-child therapy sober first, in your ordinary mindstate, since that's the one you'll be living in.` [A:1106] (safety first; nothing on gratitude).

**3. Records.**
- "Will write this himself": `The owner will write this himself.` [Q:242] Supplementary: `question 35 ("yes": gratitude may come in during a calm altered state)` [SIB:tasks/gratitude-how-20261015/INTEGRATION.md:7-8] (his answer, 15 Oct 11:19 UTC) and `He writes the public-guide changes himself; the pending queue records them (PGQ-034, PGQ-035).` [SIB:state/CODEX-CURRENT-STATE.md:96]
- Anything Joel cut or decided in the article repo on gratitude in altered states: none found.

**4. The queue's own note.** `The owner will write this himself.` [Q:242] No other owner choice named.

---

## PGQ-036 - Hypnosis isn't ruled out by grief or an altered state

At a glance: anchor found (Urge to Escape P12, line 713; also Altered States P1, line 1106) | coverage PARTIAL (weak) | Joel's own paragraph at the anchor: mostly (his published wording, not ledger-guarded) | Joel decision record: "should mention both"; "will write this himself" | who writes it: the owner.

**1. Anchor.**
- Queue "Where": `Next to that passage on gentle meditation and self-hypnosis. The owner will write this himself.` [Q:249] The passage it names is `“Gentle meditation or self-hypnosis can still help. My warning is about intensive versions.”` [Q:248]
- Found: yes. The article's version is P12 of the Urge to Escape h3. Anchor detail: heading path `# When the Adult Voice Feels Fake > ## Start With Whatever Showed Up > ### When the Urge to Escape Arrives`; paragraph P12; article line 713; first 15 words `Gentle meditation or self-hypnosis is a different story. It can really calm your nervous system` [A:713]. Altered States P1 points back to it: `Gentle meditation or self-hypnosis can help with that from the start, like I said about the urge to escape.` [A:1106]
- Joel's own words: mostly. `P3 is mostly his published wording, and the video after it is his.` [A-comment:675] The wording was changed from the guide's (`Gentle meditation or self-hypnosis can still help. My warning is about intensive versions.` [R6:515]), and no ledger entry guards the paragraph. Ledger check: no OWNER-EDITS.json entry has a must_contain string (20 characters or more) in this paragraph.

**2. Already said? PARTIAL (weak).**
- Teaching point: `Hypnosis in general isn't incompatible with grief, nor with altered states: whether it fits depends on what kind of hypnosis, what level of grief, and what is appropriate at the moment, and above all on its purpose.` [Q:246] `Hypnosis to reach feelings someone can't access (numb after a death, no tears coming) can help; hypnosis to get away from or escape what they need to face is less beneficial.` [Q:246] `Deep inner-child work still waits until the grief is less raw.` [Q:246]
- Carried in part: `It's not something to lean on all day as a way of coping, but used as therapy it can be super effective.` [A:713] (purpose: coping versus therapy). `In trance you can basically work with the fear.` [A:1146] (Joel's trance point, in the Altered States section).
- Missing: anything about grief; anything about hypnosis with an altered state; the reaching-feelings versus escaping distinction; deep work waiting while grief is raw. The article has no sentence on hypnosis together with grief: the lines that name hypnosis or trance (701, 713, 1106, 1146, 1250) and the lines that name grief (145, 557, 605, 1032, 1232, 1254) never share a sentence.
- Next to the topic, not counted: `With your little one, and in hypnosis especially, make it easy to picture: warmth, protection, steadiness, rest, whatever's really needed to melt into your happy place.` [A:1250] (hypnosis used for picturing warmth; nothing about grief or escaping); `Grief is grief, and letting tears flow can be immensely therapeutic, as long as they don't hijack your perspective with a cemented story of what will always be true.` [A:1254] (the next paragraph; grief and tears, not tied to hypnosis); `And the love or grief that sounded like therapy talk is just obvious.` [A:557] (an altered state, MDMA or deep meditation, making grief obvious; not hypnosis).

**3. Records.**
- "Will write this himself": `The owner will write this himself.` [Q:249]
- Joel's earlier decision on the same passage: `yeah gentle meditation or self-hypnosis can help that's true should mention both` [OE:1976]; the page: `Your 03:13 "gentle meditation or self-hypnosis can help": both get mentioned there, as in When the Urge to Escape Arrives.` [OQ:310] and `his trance point (trapped, so it can feel scarier, but less dangerous, and you can work with the fear) and "gentle meditation or self-hypnosis can help", both mentioned.` [TL:635]
- Joel's trance note (2026-10-12 03:13 UTC), the nearest thing he has said about trance and altered states: `in trance you can basically work with the fear, you recognize it has no real world significance and it's purely just fear. so its' super useful that way. that's worth mentioning.` [OE:1965]
- Supplementary: `hypnosis in general isn't incompatible with grief or altered states; it depends on the kind of hypnosis, the level of grief and what is appropriate at the moment.` [SIB:state/CODEX-CURRENT-STATE.md:99] (his answer to question 36, 15 Oct 13:19 UTC); `escaping what one needs to face is less beneficial` [SIB:state/CODEX-CURRENT-STATE.md:99] (question 37, 13:38 UTC).

**4. The queue's own note.** `The owner will write this himself.` [Q:249] No other owner choice named.

---

## PGQ-037 - Reparenting is not an exercise

At a glance: anchor not in the article (the section was dissolved by Joel; nearest: Chicken-and-Egg P2, line 27) | coverage PARTIAL | Joel's own paragraph there: yes (owner-final) | Joel decision record: dissolved the section; issue #168 is his; on 2026-10-08 cut a draft that carried the "sneaking reparenting in" line | who writes it: owner's voice.

**1. Anchor.**
- Queue "Where": `“The Three Adult Functions”, right after “Reparenting begins when the present-day person occupies an adult position and cares for the child from there.” One or two sentences in the owner's voice; if PGQ-012 is still pending, share its point about leaving the exercise rather than repeating it. Keep the guide's permission not to call it reparenting when inner-child language doesn't fit (“Also Look Outward”).` [Q:258]
- Found: no. The section is gone by Joel's decision (`16:29` [OE:256], `The Three Adult Functions: dissolved.` [OPF:13]) and the sentence `Reparenting begins when the present-day person occupies an adult position and cares for the child from there.` [R6:313] is in the guide (r6) but not in the article. Nearest place: where the article first names the good inner parent. Anchor detail: heading path `# The Chicken-and-Egg Problem`; paragraph P2; article line 27; first 15 words `And I realized that it doesn't make sense to ask the child to heal itself,` [A:27].
- Joel's own words there: yes. `one added sentence in Joel's paragraph below` [A-comment:25] and `Joel's owner-final rewrite above` [A-comment:41]. Ledger check: OWNER-EDITS.json entries with strings in this paragraph: `worth-line` (applied, 2 of 3 strings, [OE:170]).

**2. Already said? PARTIAL.**
- Teaching point: `Reparenting isn't an exercise you do or finish; it's the ongoing relationship in which the adult you are now cares for, validates, protects and guides the younger, vulnerable part of you, through truthful boundaries, repair and everyday choices as much as through any meditation.` [Q:255] `Meditations, imagery, inner dialogue and affirmations are ways of practicing it, not its definition, its entry ticket or its scorecard` [Q:255]
- Carried in part: `Instead, we need to separately develop the qualities of a good inner parent for that rightly vulnerable child: the loving Nurturer, safe Protector, and wise Guide.` [A:27] (a relationship of three jobs). `Whichever stage you're at, saying the right thing when you sit down with your little one helps, but you also have to start actually doing some of it in the rest of your life.` [A:57] (PGQ-012). `Maybe the grown-up just hasn't come out of the exercise with you yet.` [A:671] and `One small thing like that can teach your little one more than ten more good meditations.` [A:671] (PGQ-013). `If these exercises start feeling like a ritual you have to complete before you're allowed to live, stop there.` [A:256] `If you did the Protector action(s), not feeling better right away is information to learn from. It doesn't mean failure.` [A:414] `Your Protector, the grown-up you, earns that protective part's trust about the same way, mostly out in ordinary life.` [A:645]
- Missing: the outright statement that reparenting is not an exercise; that feeling safe while saying what you feel, need and won't accept is the reparenting itself; that no tears or relief does not mean nothing is happening; that the right words do not mean it is done; that outside help stays its own thing. The queue says the same: `None of them says outright that reparenting isn't an exercise` [Q:257]

**3. Records.**
- Joel's correction: the queue cites `the owner's correction of 16 Oct 2026 (issue #168: “Reparenting is not an exercise”)` [Q:254]; supplementary: `Issue #168, part A, opened by the owner on 16 Oct 2026 (23:27 UTC): "Reparenting is not an exercise."` [SIB:tasks/reparenting-not-exercise-20261016/INTEGRATION.md:5] His issue text is on GitHub, not checked.
- Joel dissolved the section the queue points at (`16:29` [OE:256]); the comment above the article's replacement says `The h1 replaces the dissolved "The Three Adult Functions" (Joel's OK).` [A-comment:396]
- Joel on the label permission and on "renaming" the work: his 2026-10-08 02:23 UTC message `who is gonna be "sneaking reparenting in " thru some gentler version? we have no idea where this came from?` [R4P:9] led to a cut (finding 2). The label note was moved by his agreement: `which he agreed to move to the opening of The Three Adult Functions (2026-09-27 00:55, "agreed on moving it")` [A-comment:37]; it now stands at line 39 (quoted in the findings above).
- PGQ-012 and PGQ-013 are in the article (lines 57 and 671); Joel said of the 6 Oct queue that held them (PGQ-001 to PGQ-017): `also check your lane in github, i added a bunch of suggested guide updates from the map/rules updates` [OE:1342]. On PGQ-012 the guide-update page says `my lean is to keep it, and it's Joel's call` [GUQ:22]; no answer from him on that is recorded.
- Supplementary (marked owner-approved, approvedAt 2026-10-16): `'Reparenting is not an exercise' (the owner, 16 Oct 2026, issue #168).` [SIB:guides/owner-amendments.json:388]

**4. The queue's own note.** `One or two sentences in the owner's voice; if PGQ-012 is still pending, share its point about leaving the exercise rather than repeating it.` [Q:258] No named writer beyond "the owner's voice". No owner choice named.

---

## PGQ-038 - Keeping yourself safe is part of the work, not a separate track

At a glance: anchor not in the article as worded (nearest: Not Every Hero Wears A Cape P3, line 406) | coverage PARTIAL | Joel's own paragraph there: yes (his version) | Joel decision record: he cut the meal example from that paragraph on 2026-09-29; issue #172 and answer 43a are his | who writes it: owner's voice, together with PGQ-037.

**1. Anchor.**
- Queue "Where": `“Make the Protector Visible”, right after “Warmth can come later.” One or two sentences in the owner's voice; write it together with PGQ-037 if both are still pending, and keep the guide's permission not to call it reparenting when inner-child language doesn't fit (“Also Look Outward”).` [Q:265]
- Found: no. "Make the Protector Visible" is not a heading in the article: `Make the Protector Visible, done as of 2026-09-30 (turn 5).` [A-comment:396] The section stands as Not Every Hero Wears A Cape. The guide's `Warmth can come later.` [R6:345] is not in the article as written; the nearest sentence is in P3. Anchor detail: heading path `# Building Trust With Your Little One > ## Not Every Hero Wears A Cape`; paragraph P3; article line 406; first 15 words `Plenty of people are still at the putting-up-with part. Even with little or no warmth` [A:406].
- Joel's own words there: yes, his version. `P3 is Joel's version: the first two sentences of Claude's wA2 plus his four; the meal (nurturing, not protection) and the duplicated protection examples are gone, and the make-it-specific material is left for the next paragraph.` [OE:367] `P3 is Joel's (2026-09-29).` [A-comment:396] Ledger check: OWNER-EDITS.json entries with strings in this paragraph: `mpv-p3-joel` (applied, 2 of 2 strings, [OE:365]).

**2. Already said? PARTIAL.**
- Teaching point: `Keeping yourself safe in everyday ways, such as leaving a place where you're being hurt, resting, keeping a boundary or arranging company or a safer place, is the adult you are now protecting the younger, vulnerable part of you` [Q:262] `asking a friend to come along, or staying with someone for a while, is still your own step.` [Q:262] `Help from outside, such as a doctor, crisis care, a shelter, the police or the help another person gives, stays its own thing` [Q:262]
- Carried in part: `That looks like saying no to something that's costing you too much (money, time, whatever it is).` [A:402] (Joel's; boundaries as acts your little one can see). `Even with little or no warmth for your little one yet, the relationship can start with the Protector's plain acts and the warmth can come after` [A:406] (Joel's; the Protector's acts first). `If the room itself triggers your spidey sense, leave, or lock the door and get help.` [A:318] `But if they've actually hurt or threatened you, even once, old stuff or not, get safe first, which is not a small thing at all, I know.` [A:193]
- Missing: that practical safety is itself reparenting and not a separate track to finish first; that a friend along or a night with someone is still your own step; that outside help (doctor, crisis care, shelter, police) stays its own thing and is not an exercise; the permission not to call it reparenting.
- The queue's example list (`says care may first appear “as a locked door, a meal, a cancelled obligation, or a phone put down at midnight”` [Q:264]) is the guide's (`Care may first appear as a locked door, a meal, a cancelled obligation, or a phone put down at midnight.` [R6:345]); it is not in the article.

**3. Records.**
- Joel cut the meal from this paragraph and said why (2026-09-29 19:14 UTC): `Also you were conflating protection from nurturing (giving a meal is nurturing, throwing away moldy food is protection, and we already have that in P1). So I threw away the duplicated examples of protection, and you should have seen to do that also.` [OE:368] This matters for the queue's quoted example list, which includes "a meal".
- Joel's issue #172 and answer 43a: the queue cites `the owner's issue #172 of 17 Oct 2026` [Q:261] and `the owner's answer 43a` [Q:261]; supplementary: `owner answered 43a on 17 Oct at 17:02 UTC.` [SIB:tasks/services-boundary-20261017/INTEGRATION.md:14] His message text is on GitHub, not checked.
- Joel on renaming ordinary acts as reparenting: the 2026-10-08 cut described under PGQ-037.
- Supplementary (marked owner-approved, approvedAt 2026-10-17): `the person's own protective steps stay part of reparenting even when they sit next to a service, asking someone to come along or staying with a friend included.` [SIB:guides/owner-amendments.json:409]

**4. The queue's own note.** `One or two sentences in the owner's voice; write it together with PGQ-037 if both are still pending` [Q:265] No named writer beyond "the owner's voice". No owner choice named.

---

## PGQ-039 - Before sharing something legally or personally sensitive

At a glance: anchor found (Also Look Outward P10, line 213, same as PGQ-030) | coverage NONE for the new content | Joel's own paragraph at the anchor: no (Claude's, approved by Joel) | Joel decision record: the instruction itself (18 Oct, per the queue); cops-line rulings | who writes it: owner's voice; legal review before placement.

**1. Anchor.**
- Queue "Where": `“Also Look Outward” immediately after the graded-disclosure/earned-trust paragraph.` [Q:278]
- Found: yes, the same paragraph as PGQ-030. Anchor detail: heading path `# Before You Try to Go Deep > ## Your Body Might Need Some Love First > ### Also Look Outward`; paragraph P10; article line 213; first 15 words `And reaching out doesn't mean telling strangers everything. Privacy isn't fakery. People can earn more` [A:213].
- Joel's own words: no, Claude's C2 which Joel approved (see PGQ-030). Ledger check: OWNER-EDITS.json entries with strings in this paragraph: `c2-after-c1` (applied, 2 of 4 strings, [OE:1416]); `t1-t9-teaching-points` (applied, 1 of 19 strings, [OE:1432]).

**2. Already said? NONE (new content).**
- Teaching point, new parts: `Digital conversation content can be retained, copied, screenshotted or legally demanded; pseudonyms and deleting messages do not ensure anonymity.` [Q:272] `Police aren't confidential therapists.` [Q:272] `Readers can ask a therapist/clinician or helpline what it must report, what gets documented and who can access records,` [Q:272] `immediate danger requires prompt protection, not delays for legal/privacy optimization.` [Q:272]
- The base the queue says is covered is there: `Privacy isn't fakery.` [A:213] (PGQ-003). The queue's own note: `Neither explains online records, mandated-reporting exceptions, legal professionals, or prevention-sensitive voluntary reporting.` [Q:276] Nothing in the article does: the visible text has no hit for anonymous, pseudonym, delete, retain, screenshot or mandated, and the only hits for record, report and confidential are "track record" (lines 103, 428, 456), "reporter" (452), "rebirth reports" (1084) and the Hearthwork principle listed below.
- Next to the topic, not counted: `In general, don't call the cops and expect it to go well. That's a real last resort.` [A:701] (Joel's; his own drug-law story) and `A crisis line or an emergency number counts, and the person on the other end can be a total stranger.` [A:1068] (immediate danger). `Presence, Warmth, Discipline, Confidentiality.` [A:1266] (a peer-counseling principle; nothing on what a service must report or keep) and `So can the law, if it comes to that` [A:1206] (the law as an option against someone who hurt you; nothing about your own disclosures).

**3. Records.**
- The instruction: the queue says `owner instruction, 18 Oct 2026, broadening the reader warning proposed under generic privacy/safeguarding design issue #180.` [Q:270] and `owner-requested reader-facing editorial direction` [Q:270]; the drafted passage is at the issue comment the queue links (`https://github.com/u-dont-existDOTcom/innerSignalGraph/issues/180#issuecomment-6250178409` [Q:270]), which could not be read here (403). Joel's message itself: not checked.
- Joel on police and legal exposure, already in the article: `13. leave it. i also don't recommend calling the cops for safety reasons at all.` [OE:1882] and `just don't call the cops and expect it to go well in general, that's a real last resort.` [OE:1796] This sits against the queue's `Sometimes disclosure or reporting of past harmful actions or contemplated harm can protect victims and interrupt recurrence, even when legal consequences follow;` [Q:272] worth flagging when drafting.
- Joel approved the paragraph it follows: `C2 looks fine` [OE:1419].
- Legal review: no record that any has been done or requested in the article repo.

**4. The queue's own note.** `Humanize in the owner's voice, preserving all distinctions. Before actual public placement, obtain appropriate legal review of explicit jurisdictional statements.` [Q:278] Owner choice named: none; legal review is required before placement. Also `a pending queue entry is not publication authority.` [Q:278] and `Specific service data flows and internal safety routing remain issue #180 engineering/legal work, not public guide text.` [Q:276]

---

## Note on the main session's drafts

The git log of the article repo shows commit 4f580520 (turn 76, round a) drafting the innerSignalGraph queue's PGQ-027 to PGQ-030, 032, 033 and 037 to 039, and no draft for 031, 034, 035 or 036. Those drafts are working text, not Joel decisions, and were not used as evidence above.
