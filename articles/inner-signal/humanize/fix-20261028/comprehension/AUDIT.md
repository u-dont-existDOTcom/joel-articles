# The hypnosis guide's comprehension audit (2026-10-28)

Joel, 2026-10-28 15:20 UTC: "i started on it, but the guide itself is now too incomprehensible, we went wrong somewhere" ([his message](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/inner-signal/humanize/fix-20261028/joel-20261028-1520-message.txt)).

Fresh readers each had one part of the guide twice, as it was when he wrote (commit 0a44911d) and as he published it ([published](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/inner-signal/humanize/source/published-20260928.md)), and went through the part sentence by sentence for every place it reads worse than his: **garbled** (doesn't parse, a word that doesn't fit), **unclear** (a reader has to reread or guess), **lost** (a point, step, condition or contrast he made is gone) or **vaguer**. Then I checked every finding against the whole guide and his own decisions: his terms (the Guide, guard), the cautions and repeats he cut on 25 October, the lines his newer inner child guide put in. Eleven parts of about 2,500 words; six were read again in halves when their first readers ran out of room ([how the parts were made](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/inner-signal/humanize/fix-20261028/comprehension/make_chunks.py), [the halves](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/inner-signal/humanize/fix-20261028/comprehension/make_halves.py)).

## The numbers

- **281 findings** from the readers (6 at their severity 3, 100 at 2, 175 at 1).
- **41 real problems** by my check, in **38 of the guide's 591 paragraphs (6%)**: 6 where a reader won't get it or it now says something else, 35 where most readers would stumble. By kind: garbled 14, unclear 13, lost 10, vaguer 4.
- **118 small snags** (a vaguer word, a lost nuance, an unclear "it") in 95 more paragraphs (16%).
- **6 in his own words**: his call, on the fix page as passages to keep or edit.
- **116 not problems** (41% of the findings): as clear as his, his own terms or decisions, or explained elsewhere in the guide.
- **When the real problems came in** (the first version of the guide in Git with their words): 18 Oct (the overnight Emulate run), 23; 20-23 Oct (installs of the induction section, the NLP appendix and his answers), 13; 25 Oct (the answers of his first marking page), 4; as he published it, 1.
- **Seen before and left:** 29 of the 41 real problems had been flagged by the strict Emulate check's readers on 25 October, rated "small" and left; 11 had been named by the 18 October second readers and let stand as wording or tone.

## By part

| Part | From | To | Real | Snags | His | Not |
|---|---|---|---|---|---|---|
| 1 | (start) | Why doing it myself worked better for me | 8 | 8 | 1 | 2 |
| 2 | A useful map of the mind | The Protector | 0 | 8 | 0 | 17 |
| 3 | The Guide | When “your voice” is everybody else’s voice | 3 | 6 | 2 | 15 |
| 4 | Belonging without betraying yourself | Already open? Contain before you deepen | 1 | 15 | 0 | 10 |
| 5 | Stay awake when your mind likes to escape | Finding your own words | 6 | 8 | 0 | 3 |
| 6 | Let the response change the invitation | It feels fake | 3 | 13 | 1 | 26 |
| 7 | The subconscious will not answer | Survey and consultation | 2 | 9 | 0 | 13 |
| 8 | Appendices | Sensory, state, and strategy tools | 4 | 16 | 0 | 10 |
| 9 | What I will not use NLP for | Finding a hypnotist who can work with you | 5 | 12 | 2 | 10 |
| 10 | When the subconscious speaks like an oracle | The cosmic-download humility test | 4 | 8 | 0 | 5 |
| 11 | Don’t become an entity hobbyist | Memory, support, and choosing a practitioner | 5 | 15 | 0 | 5 |

## The real problems (41)

**F1.5** · lost · Introduction, P8 · a real problem

Now:

> I combine this with inner child reparenting (a clever suggestion won’t heal a hurt young part), and also aspects of prompt engineering, as well as helping people to be literate in the domain of what’s hypnotizing them.

Published:

> I borrow from prompt engineering because the shape of a question changes the kind of answer we can hear. And I include influence literacy because hypnosis is hardly the only thing hypnotizing us.

Reader: The reasons are gone (the shape of a question changes the kind of answer we can hear; hypnosis is hardly the only thing hypnotizing us), so "prompt engineering" arrives unexplained and "literate in the domain of what’s hypnotizing them" is hard to place.

My check: Why prompt engineering and influence literacy are there is gone; 'literate in the domain of what's hypnotizing them' is hard to place

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (1.26, rated small)_

**F1.10** · garbled · Protecting Yourself from Hypnotists, P3 · a real problem (settled by his own version)

Now:

> Conscious agreement, unconscious receptivity, emotional compliance, legal and ethical consent. Can people have their minds influenced without conscious agreement of their adult self?

Published:

> Conscious agreement is one thing. Unconscious receptivity is another. Emotional compliance is another. Legal and ethical consent is another. A mind can be influenced without the adult self having clearly chosen the influence.

Reader: A verbless list stands as a sentence without saying that these four are different things, and the published statement that a mind can be influenced without the adult self having chosen it has become an open question.

My check: The four kinds of agreement as a list with no verb; his HG-S15 version of today replaces the paragraph

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (1.41, rated small)_

**F1.11** · garbled · Protecting Yourself from Hypnotists, P4 · a real problem

Now:

> As associated with the Silva Mind Control method:

Published:

> A line associated with the Silva Mind Control tradition says it plainly:

Reader: It is a fragment that never says a quoted line follows.

My check: 'As associated with ...' doesn't parse (he flagged it today); the words are Emulate's, in his 25 Oct quote-mark answer

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (1.43, rated small)_

**F1.13** · unclear · What to Use Self-Hypnosis For, and What Not To, P3 · a real problem

Now:

> DO NOT use Self Hypnosis to help you: force yourself to remember trauma, force yourself to prove trauma through memories, suppress medical symptoms, de-stabilize your self, or NOT seek correct treatment.

Published:

> Do not use it to force trauma memories, prove what happened, suppress medical symptoms, destabilize yourself, or replace appropriate clinical care.

Reader: The last item is a second negative inside a "DO NOT" list ("to help you ... NOT seek correct treatment") that a reader must untangle, and "correct treatment" is vaguer than "appropriate clinical care".

My check: 'DO NOT use ... to help you ... NOT seek correct treatment' is a double negative

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (1.52, rated small)_

**F1.15** · lost · Forget the left-brain/right-brain cartoon, P5 · a real problem

Now:

> And it’s got to lead somewhere!

Published:

> A powerful state matters only if something survives it: kinder behavior, more humility, better judgment, real service, or a more workable ordinary life.

Reader: "It" has no clear referent, and the point that a powerful state matters only if something survives it (kinder behavior, humility, better judgment, service, a workable ordinary life) is reduced to an exhortation.

My check: 'it's got to lead somewhere!' replaces what has to survive a powerful state (kinder behaviour, humility, judgment, service, a workable life)

_came in: 18 Oct (the overnight Emulate run)_

**F1.16** · unclear · Why doing it myself worked better for me, P4 · a real problem

Now:

> I found that especially amplified with loveyhuasca.

Published:

> Self-hypnosis simply has one advantage nobody outside can duplicate: immediate dialogue with the system itself. I found that especially amplified with loveyhuasca.

Reader: "That" pointed to the one advantage of immediate dialogue with the system itself, a sentence NOW dropped, so it now follows a parenthetical about a skilled guide's advantages and has no clear referent.

My check: His published sentence, but the sentence before it ('one advantage nobody outside can duplicate: immediate dialogue with the system itself') is gone, so 'that' now points at a skilled guide's advantages

_came in: as he published it; flagged on 25 Oct (1.62, rated small)_

**F1.18** · unclear · Why doing it myself worked better for me, P9 · a real problem

Now:

> In the same vein, self-hypnosis seemed to extend a short chrunga trip for what felt like a long time, and it feels like if I needed to I could have continued for an arbitrary amount of time. Only because of life did I have to talk to people, etc.

Published:

> I’ve also had self-hypnosis seem to extend a short chrunga trip far beyond its normal duration. Subjectively, it felt as though the state might have continued indefinitely if ordinary life hadn’t required communication and interruption.

Reader: "Only because of life did I have to talk to people, etc." never says that the talking and interruption are what ended the extended state, which PUBLISHED stated as a condition ("might have continued indefinitely if ordinary life hadn’t required communication and interruption").

My check: 'Only because of life did I have to talk to people, etc.' doesn't say that talking and interruptions ended the state

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (1.63, rated small)_

**F1.19** · garbled · Why doing it myself worked better for me, P9 · a real problem

Now:

> Phenomenologically, this is very important. Although I'm not recommending that anyone prolong an altered state forever, because it's better to integrate, etc.

Published:

> I find that phenomenologically important. I’m not recommending that anyone prolong an altered state forever; integration is healthier than trying to live inside the extension.

Reader: The "Although" clause is a fragment with no main clause, and "better to integrate, etc." no longer says what integration is being preferred to.

My check: 'Although I'm not recommending ...' is a fragment

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (1.64, rated small)_

**F3a.3** · unclear · Working with your guards, P3 · a real problem

Now:

> Often they are you experiencing a very charming guard.

Reader: "They are you experiencing a very charming guard" is hard to parse, and "charming" doesn't say what the guard does.

My check: 'Often they are you experiencing a very charming guard' doesn't parse (my 22 Oct wording around his answer 9, cut down on 25 Oct)

_came in: 25 Oct (the answers of his first marking page)_

**F3a.4** · unclear · Working with your guards, P6 · a real problem

Now:

> Tell them that it makes sense that they want to protect you and that they don’t have to stop protecting you, but that you want to know what could make them trust you 1% more that you can do that.

Reader: "Do that" has no clear referent (protect you, stop protecting you, or something else), so the reader can't tell what the guard is being asked to trust.

My check: 'trust you 1% more that you can do that' doesn't say do what (protect yourself)

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (2.60, rated small)_

**F3a.10** · garbled · Don’t rush the repair, P2 · a real problem

Now:

> Just tell you what they need to not be alone anymore.

Published:

> I only want to know what would help you feel less alone.

Reader: "Just tell you" reads as an instruction to the reader, and the missing subject (the child) means the sentence doesn't parse on its own.

My check: 'Just tell you what they need' doesn't parse: who tells whom

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (2.84, rated small)_

**F4a.3** · lost · If you sense you are being influenced, P6 · a real problem

Now:

> This is a good guide to help engage your adult in the conversation. The more powerful the state the more you will need to make use of these.

Published:

> A useful guide leaves the adult self more present. Powerful states need stronger boundaries.

Reader: PUBLISHED gives a test for any guide (it should leave the adult self more present) and says powerful states need stronger boundaries, but NOW makes the list of questions the "guide" and leaves "the conversation" and "these" without a clear referent.

My check: 'This is a good guide' now means the list, and 'these' has no clear referent; his point was that a good guide leaves the adult more present

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (3.69, rated small)_

**F5.2** · garbled · Make the hypnosis more active, P1 · a real problem

Now:

> As you move one of your hands, you're going to move deliberately, and as soon as you stop moving deliberately, you'll focus on what you've got.

Published:

> Keep the eyes open and pair a small repeated hand movement with increasing clarity; stop the movement and notice what remains without trying to disappear inward.

Reader: "Move deliberately" and "focus on what you've got" are circular and vague, so the instruction no longer says to repeat a small movement while clarity increases, or to notice what remains once it stops.

My check: The hand-movement step doesn't parse; the published step (pair a small repeated movement with growing clarity, stop and notice what remains) is gone

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (4.55, rated small)_

**F5.4** · lost · Optional fractionation: practice coming back, P1 · a real problem

Now:

> At some point in time you can add this, but you must say you are doing it before doing it.

Published:

> Fractionation means returning toward ordinary awareness and then deciding whether to enter absorption again. Used openly, it teaches that trance has a door in both directions. Name the technique before using it; every answer cannot secretly mean “deeper.”

Reader: NOW never says what fractionation is or why it must be announced, so "this" has no clear referent and the reason (no answer may secretly mean "deeper") is gone.

My check: 'add this' points at a script below it, and what fractionation is and why you name it first are gone

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (4.62, rated small)_

**F5.5** · garbled · Optional trance depth check, P1 · a real problem

Now:

> As you wait and release the responsibility of making it happen

Published:

> As I wait, I give up the responsibility of making anything happen.

Reader: A dependent clause stands alone with no main clause, and "it" has no antecedent until the next paragraph.

My check: One sentence of the script is split across two paragraphs, so the first reads as a fragment

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (4.66, rated small)_

**F5.7** · garbled · A shortcut back into hypnosis, P2 · a real problem

Now:

> Say the word and/ or do the phrase while doing the motion (if applicable).

Published:

> Choose a distinctive word, phrase, or optional gesture.

Reader: A phrase is said, not "done", so a reader can't tell what to say, what to do and what to combine; the cue was a word, a phrase or an optional gesture.

My check: 'do the phrase' doesn't parse: a phrase is said

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers)_

**F5.8** · lost · A shortcut back into hypnosis, P4 · a real problem

Now:

> When you pick the time and place (it needs to be an appropriate time and place), say the word and/ or do the phrase to begin going into this state that you picked, and are familiar with. It's fine to change the direction you are going in, or stop this at any point.

Published:

> When I’ve set aside time, settled somewhere appropriate, and deliberately use my cue to begin, I can return to this familiar way of listening. I can change direction or finish.

Reader: PUBLISHED has the reader attach this wording to the cue as its meaning ("Give it the meaning you choose:"), but NOW gives it as a usage instruction, so the step of giving the cue its meaning and conditions is lost.

My check: The cue's meaning (the suggestion you give it) became an instruction to the reader; 'do the phrase' again

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (5.5, rated small)_

**F5.16** · unclear · Notice, meaning, and your thoughts on the meaning, P2 · a real problem

Now:

> It's also ok to use phrases that you didn't think in your head - if something comes up that you're analyzing, it's still good to analyze, even if it's not in your head already.

Published:

> A sentence you find now can help examine the meaning without being a sentence you thought then.

Reader: "Phrases that you didn't think in your head" and "even if it's not in your head already" are circular and never say that wording found now can be used to examine a meaning that arrived wordlessly.

My check: Circular ('phrases that you didn't think in your head ... even if it's not in your head already'); the point that words found now can examine a wordless meaning is gone

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers)_

**F6a.4** · unclear · Let the response change the invitation, P3 · a real problem

Now:

> Neither is automatically a guard, and just being silent doesn't mean there's a process.

Published:

> Skepticism is not automatically a protector, and silence is not proof that a hidden process is working.

Reader: "Neither" and "guard" point at nothing the reader has been told about (PUBLISHED says skepticism is not automatically a protector), and "there's a process" no longer says what process or that it is hidden and working.

My check: 'just being silent doesn't mean there's a process' doesn't say a hidden process working, and 'neither' is hard to place

_came in: 25 Oct (the answers of his first marking page)_

**F6a.8** · unclear · Look at the situation too, P2 · a real problem

Now:

> On the other hand, you may find that you have acted inappropriately and you feel guilty. Having feelings of guilt does not mean that you have done something wrong or that you have been manipulated.

Published:

> Notice your side too. Guilt doesn’t prove wrongdoing or manipulation.

Reader: The first sentence asserts you have acted inappropriately and the next says guilt doesn't mean you did anything wrong, so the two seem to contradict each other, and PUBLISHED's plain "Notice your side too" is lost.

My check: 'you may find that you have acted inappropriately' then 'guilt does not mean that you have done something wrong' reads as a contradiction

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (5.40, rated small)_

**F6a.14** · garbled · Change the amount of contact, P3 · a real problem

Now:

> If you have trouble orienting yourself and it lasts for a prolonged period of time, please get some human help rather than trying a stronger induction back to the here and now.

Published:

> Persistent disorientation needs human help rather than a stronger induction.

Reader: An induction takes you into hypnosis, so "a stronger induction back to the here and now" does not make sense and hides the point that you should not try going deeper to fix disorientation.

My check: 'a stronger induction back to the here and now' doesn't make sense: an induction takes you in

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (5.45, rated small)_

**F7.7** · vaguer · You become too analytical, P1 · a real problem

Now:

> You’re being too analytical. “What if you didn’t try to improve it?”

Published:

> When the practice turns into a technical performance, stop improving it.

Reader: A firm instruction to stop improving the practice becomes a quoted question with no speaker, and "it" no longer points to the practice.

My check: 'improve it' doesn't say the practice, and the instruction became a question with no speaker

_came in: 18 Oct (the overnight Emulate run)_

**F7.23** · unclear · Try it in the Inner Signal app, P1 · a real problem

Now:

> You can download Inner Signal App for voice hypnosis, information, to learn the language, and for feedback on what you report.

Published:

> Use the Inner Signal app to get voice hypnosis sessions, learn the method, develop your own language, reflect on what you report, and ask questions about a hypnotist’s approach.

Reader: "Learn the language" does not say which language, "learn the method" and "develop your own language" are lost, and the list mixes nouns and infinitives.

My check: A list that mixes nouns and 'to learn the language' (which language?); 'develop your own language' is gone

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (7.2, rated small)_

**F8a.7** · unclear · Appendix B: NLP without turning yourself into a sales seminar, P2 · a real problem

Now:

> You do not need to know this stuff to do it but if you want to freshen up on your skills in the art of working with imagery, body states, behavioral rehearsal, talking to yourself in effective sentences etc then it might be useful, when it helps the system listen.

Published:

> You can practice the core method without learning one term of Neuro-Linguistic Programming. Read this appendix when you want more precision about imagery, bodily states, rehearsal, and sentence design. NLP is useful when it helps the system listen; it becomes a bag of tricks when technique replaces love, truth, contact, or consent.

Reader: "To do it" never says it means the core method, and the sentence runs on with a dangling "when it helps the system listen", so a reader must reread to see what is optional and when NLP is useful.

My check: 'then it might be useful, when it helps the system listen' runs on and 'to do it' doesn't say the core method

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (7.36, rated small)_

**F8a.13** · lost · Pattern 5: Embedded invitations, P1 · a real problem

Now:

> ie. "And I can allow myself to experience..."

Published:

> An embedded invitation places a small direction inside a larger sentence. It should invite a modest inner movement, not hide a demand.

Reader: The pattern is never defined (a small direction placed inside a larger sentence, inviting a modest movement, not hiding a demand), so "ie." introduces examples of nothing stated.

My check: The section opens 'ie.' with no definition; what an embedded invitation is, and that it mustn't hide a demand, are gone

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers)_

**F8a.14** · garbled · Pattern 5: Embedded invitations, P3 · a real problem

Now:

> Or, something similar that you might use when working with inner child type of parts.

Published:

> “The child does not have to trust me all at once; it can simply notice I am still here.”

Reader: This is a fragment that points to an inner-child example instead of giving one, so the third example (the child need not trust all at once) is missing.

My check: A fragment pointing to an inner child example that isn't there

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers)_

**F8b.14** · vaguer · Perceptual positions — self, other, witness, universal heart, P2 · a real problem

Now:

> Perceptual Positions: 1) seeing from Self, 2) then seeing from Other, 3) then seeing from Witness, and 4) then seeing from Universal Heart. I do this to see the situation with more accuracy.

Published:

> First: what do I feel from inside myself? Second: if I sit inside the other person, what might they be feeling or protecting? Third: if I watched this from across the room, what would I notice? Fourth: from the universal heart, what serves truth, love, boundaries, and the good of everyone involved?

Reader: The four positions shrink to bare labels, so what each one asks (what the other feels or protects, the view from across the room, what serves truth, love, boundaries and everyone involved) is lost and "Other", "Witness" and "Universal Heart" are never explained.

My check: The four positions are bare labels; what each one asks (what the other feels, the view from across the room, what serves everyone) is gone

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (8.53, rated small)_

**F9.1** · lost · What I will not use NLP for, P2 · a real problem

Now:

> I do not deny people's legitimate signals.

Published:

> To talk myself out of a real signal.

Reader: The published point (not talking myself out of a real signal with NLP) became "deny people's legitimate signals", which names a different act and a different person and no longer says NLP is the means.

My check: Says something else: his published line is about talking himself out of a real signal, not denying other people's

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (8.64, rated small)_

**F9.4** · lost · What I will not use NLP for, P10 · a real problem

Now:

> I do not use NLP with people when there isn't enough time.

Published:

> To create urgency where time is needed.

Reader: The published rule is not to manufacture urgency where a person needs time, but NOW says not to start when time is short, which is a different rule and drops the urgency point.

My check: Says something else: the published rule is not to create urgency where a person needs time; now it says not to start when time is short

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (8.71, rated small)_

**F9.7** · lost · Running the whole NLP sequence, P10 · a real problem

Now:

> Have them check in with their body for changes and look for evidence to support their new interpretation of the situation.

Published:

> Check the fit and the evidence. What changes in the body? Is the response kind and doable? What supports the interpretation beyond how it feels?

Reader: The "is the response kind and doable" check and the test of what supports the interpretation beyond how it feels are gone, and "look for evidence to support" now reads as seeking confirmation rather than testing.

My check: 'look for evidence to support their new interpretation' now reads as looking for confirmation; 'is the response kind and doable' is gone

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (9.6, rated matters)_

**F9.27** · garbled · Finding a hypnotist who can work with you, P1 · a real problem

Now:

> What they are trained in (what they can treat) How they use hypnosis What they will do if things don't fit (if they are treating trauma, did they have specific training on trauma and dissociation? Having hypnosis certifications matters, but doesn't mean they are trained in trauma care)

Published:

> Ask what they are trained to treat, how they use hypnosis, and how they respond when a suggestion doesn’t fit. For trauma work, ask about actual trauma and dissociation training, not only a hypnosis certificate. Credentials matter without guaranteeing competent care.

Reader: Three unpunctuated verbless items, with no "ask" and no stated purpose, leave the reader to guess that these are things to find out about a hypnotist.

My check: A list whose line breaks were lost, so its items run together with no punctuation

_came in: 18 Oct (the overnight Emulate run)_

**F9.28** · garbled · Finding a hypnotist who can work with you, P2 · a real problem

Now:

> What has/hasn't worked for you in the past How direct you want them to be What kind of touch (if any) you are ok with What kind of imagery (if any) you are ok with What you want them to do if you want them to stop What they will do if things go unexpected during or after the session What they do if you aren't sure if something is a memory or not How they will do the full return (coming out of hypnosis) at the end of the session You should be able to be firmly encouraged, but not forced to continue if you don't want to.

Published:

> Describe what has helped, what hasn’t, your preferred directness, acceptable touch and imagery, and how you’ll stop. Ask about unexpected reactions, uncertain memories, and the full return. Firm encouragement can fit; refusal still ends it.

Reader: Eight unpunctuated verbless items run into a sentence, and the published split between what you tell the hypnotist and what you ask them is gone, so the reader cannot tell what to do with the list.

My check: The same: eight list items run into one sentence

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (9.66, rated small)_

**F10a.3** · garbled · Forgiving yourself, P2 · a real problem

Now:

> Be specific about the action you took, and the impact it had, feel the remorse, do what you can to rectify or keep it from happening again, and then stop holding yourself hostage, and the responsibility stays.

Published:

> Then move through responsibility, remorse, rectify, release: name the action and impact; allow the remorse; repair or prevent repetition where possible; and stop holding yourself hostage after responsibility has been faced.

Reader: The last clause "and the responsibility stays" is tacked on and does not connect to what precedes it, so the published point (stop holding yourself hostage once responsibility has been faced) is lost and the named four-step sequence is gone.

My check: A run-on that ends 'and the responsibility stays', tacked on (my 25 Oct alignment card joined his inner child guide's two sentences with commas)

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (9.81, rated small)_

**F10a.8** · lost · Appendix G: Altered states, P3 · a real problem

Now:

> Let that experience inform what you OPEN yourself up to.

Published:

> Let the experience widen what seems possible while you build usable access.

Reader: The published instruction to treat the past opening as a resource that widens what seems possible while you build usable everyday access (not a state to reproduce) is replaced by "inform what you OPEN yourself up to", which no longer says what to do.

My check: 'Let that experience inform what you OPEN yourself up to' no longer says what to do: let it widen what seems possible while you build everyday access

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (9.87, rated small)_

**F10b.6** · garbled · The cosmic-download humility test, P1 · a real problem

Now:

> Finally, presences, shadow forces, or grandiose parts may try to respond by giving you a sense that you’re special, trying to “download cosmic info” to you, try to give you a special mission, make you feel doing the dishes is beneath you, etc.

Published:

> Hostile presences, shadow forces, grandiose parts, and altered-state imagery don’t always attack through fear. Sometimes they seduce through importance: a cosmic secret, a special mission, a vast download, a feeling of being uniquely chosen, or a revelation that makes washing dishes seem beneath your new rank.

Reader: The list shifts verb forms ("giving", "trying", "try", "make") and "respond" has nothing to respond to, and PUBLISHED's contrast that these presences don’t only attack through fear but also seduce through importance is gone.

My check: 'may try to respond by giving you ..., trying to ..., try to ..., make you ...' doesn't parse as one list, and 'respond' has nothing to respond to

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (10b.3, rated small)_

**F10b.7** · unclear · The cosmic-download humility test, P2 · a real problem

Now:

> Unless the “guidance” you’re trying to give me can help me be more beautiful, honest, relational, humble, and useful in my everyday life, I don’t need it.”

Published:

> Guidance worth keeping should make ordinary life more beautiful, honest, relational, humble, reliable, and useful to other people.

Reader: It nearly repeats the "Unless … I don’t need it" sentence just before it, closes a quotation that this paragraph never opened, and turns PUBLISHED's general principle about guidance into "help me be more beautiful", so a reader can’t tell whether it is more of the script or the author’s own rule.

My check: A near-repeat of the line before it, ending with a closing quote mark that nothing opened

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (10b.21, rated small)_

**F11.13** · vaguer · 8. Resource embodiment, P1 · a real problem

Now:

> Resource: pick a resource quality.

Published:

> Choose qualities you understand: warmth, boundary, steadiness, curiosity, or dignity.

Reader: "Resource quality" is never explained and the examples and the "qualities you understand" condition are gone, so the reader does not know what to pick.

My check: 'pick a resource quality' with no examples: the reader doesn't know what to pick

_came in: 18 Oct (the overnight Emulate run)_

**F11.14** · unclear · 8. Resource embodiment, P1 · a real problem

Now:

> Imagine yourself accessing 1% more of that quality (or just sense yourself).

Published:

> Imagine posture, voice, or attention with 1% more access to one quality. Observe rather than embody it when preferred.

Reader: "Or just sense yourself" does not say sense what, and the published option to observe the quality rather than embody it is lost.

My check: '(or just sense yourself)' doesn't say sense what; observing instead of embodying is gone

_came in: 18 Oct (the overnight Emulate run)_

**F11.16** · vaguer · 9. No-trance inner contact, P1 · a real problem

Now:

> Autonomous: write whatever you get.

Published:

> Autonomous signal: Record a word, sensation, impulse, objection, or silence without interpreting it as proof.

Reader: "Autonomous" has lost its noun (signal), "whatever you get" does not say what is being received, and the caution not to read it as proof is gone.

My check: 'Autonomous:' lost its noun (signal) and the guide never uses the word elsewhere

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (10b.0, rated matters)_

**F11.18** · garbled · 9. No-trance inner contact, P1 · a real problem

Now:

> Integration/exit: reality test the autonomous, do one small thing based on it, stop doing it.

Published:

> Integration and exit: Reality-test the signal and do one small action. Because no altered state was cultivated, simply close the exercise and continue the day.

Reader: "The autonomous" has no noun, "stop doing it" could mean stopping the small action or the exercise, and the step "because no altered state was cultivated, simply close the exercise and continue the day" (no waking return needed) is missing.

My check: 'reality test the autonomous ... stop doing it' doesn't parse

_came in: 18 Oct (the overnight Emulate run)_

**F11.21** · unclear · Indirect language and re-entry cues, P1 · a real problem

Now:

> The information on these techniques comes from these sources, not because they necessarily validate some aspects of NLP, or because every example suits trauma work (Nimja did not write or endorse this guide), but because I was adapting the language used for my own purposes, and I deliberately used a sequence that would be easy to use for re-entry.

Published:

> They are technique sources, not evidence that every NLP claim is established or every example suits trauma work. The original wording and deliberately chosen re-entry sequence here are adaptations; Nimja did not write or endorse this guide.

Reader: The long not-because/but-because sentence with a parenthesis in the middle reads as if the information comes from these sources because the author was adapting the language, which muddles the plain point that they are technique sources, not evidence, and that the wording and re-entry sequence are the author's own adaptations.

My check: A long 'not because ... but because' sentence that reads as if the sources were chosen because he was adapting them

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (10b.38, rated small)_


## In his own words (6)

**F1.8** · unclear · Quick start: do this first, P3 · in his own words (his call)

Now:

> You'll follow whatever you notice - sensation, image, phrase, feeling, objection, silence - as you're invited. Vary the invites as needed to be responsive & warm, to create a boundary, to give direction or more time, etc.

Published:

> As you listen, a sensation, image, phrase, feeling, objection, or silence may become noticeable. Let the next invitation follow that response. Use warmth, a boundary, direction, or more time as needed.

Reader: It is not said who invites you or what "the invites" are, and the point that the next invitation should follow whichever response arises is blurred into "follow whatever you notice".

My check: 'as you're invited' and 'the invites' don't say who invites (you do); he kept these sentences in his ED-A3 version today

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (1.33, rated small)_

**F3a.5** · unclear · Working with your guards, P6 · in his own words (his call)

Now:

> If it says no, I’d listen, and if it says no to going deeper in this work or to an altered state, I’d stop there and not test it, even when it sounds like a prediction.

Reader: The first "no" has no stated object, and "not test it, even when it sounds like a prediction" doesn't say what is being tested or what the prediction is.

My check: His inner child guide's line (under a heading there that says when); here 'not test it, even when it sounds like a prediction' is hard to place

_came in: 25 Oct (the answers of his first marking page)_

**F3b.9** · unclear · When “your voice” is everybody else’s voice, P11 · in his own words (his call)

Now:

> As you differentiate, you learn to tell which of those apply.

Reader: "As you differentiate" is undefined (differentiate what, from whom?) and "which of those apply" points back across a long sentence at two options the reader has to reconstruct.

My check: His inner child guide's sentence (IC-A21): 'as you differentiate' isn't introduced in this guide

_came in: 25 Oct (the answers of his first marking page)_

**F6a.27** · unclear · Throughout the exercise, P1 · in his own words (his call)

Now:

> If it says no to going deeper, or tells you to stop doing the exercise, I’d stop there and not test it, even when it sounds like a prediction.

Published:

> Keep the analytical mind available throughout: you can question, disagree, and stop.

Reader: "not test it" and "even when it sounds like a prediction" do not say what is being tested or what is predicted, so the reader has to guess what the instruction means.

My check: His inner child guide's line (as F3a.5)

_came in: 25 Oct (the answers of his first marking page)_

**F9.15** · unclear · Appendix C: The extended de-hypnosis checklist, P3 · in his own words (his call)

Now:

> try to seduce/scare/rescue your child

Published:

> Is the child part being seduced, scared, or rescued?

Reader: "your child" reads as the reader's own child, where the published "child part" means the inner child.

My check: His own Appendix C (23 Oct): 'your child' can read as the reader's own child, not the inner child

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers)_

**F9.16** · unclear · Appendix D: Anxiety — body first, P2 · in his own words (his call)

Now:

> Remember that often the anxiety comes from a childhood guard part of you. It’s what protects you when your consciously installed parental Protector isn’t functioning, the same as in childhood.

Published:

> Anxiety is often a Protector trying to prevent danger, shame, abandonment, failure, exposure, illness, rejection, loss of control, or a feeling it believes would be unbearable.

Reader: "consciously installed parental Protector" is an undefined term set against a "childhood guard part" (the published text just says a Protector), and "the same as in childhood" has no clear referent, so the reader has to guess.

My check: His own phrase (his answer 9, 22 Oct: 'the consciously installed parental Protector'); a reader didn't know the term. If you like, 'your inner adult's Protector' says it with the guide's term

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (9.19, rated matters)_


## The small snags (118)

**F1.1** · unclear · How to use this very large guide, P1 · a small snag

Now:

> To make it easier, you can begin with the Quick start section, then learn one of the inductions and the whole return sequence. Then, you can read the Let the next response guide you section, for the part of the practice no recording can decide in advance.

Published:

> Begin with Quick start, learn one induction and the complete return, then use Let the next response guide you for the part no recording can decide in advance.

Reader: "To make it easier" has no clear "it", and "the Let the next response guide you section" runs the section title into the sentence so it is hard to parse.

My check: A section's title run into the sentence ('the Let the next response guide you section')

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (1.0, rated small)_

**F1.2** · unclear · Introduction, P2 · a small snag

Now:

> Have you ever realized that you were born with an incredible brain/mind that has many layers of consciousness: dream, protect, analyze, imitate, love, remember, hide, show, heal, etc, etc?

Published:

> You were born with a mind that can dream, protect, analyze, imitate, love, remember, hide, reveal, and heal.

Reader: A list of bare verbs follows "layers of consciousness:", so it reads as if the layers are named "dream", "protect" and so on, where PUBLISHED said the mind can do these things.

My check: The verbs after 'layers of consciousness:' read as the layers' names

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (1.3, rated small)_

**F1.3** · lost · Introduction, P3 · a small snag

Now:

> Yet no one taught those layers to talk to each other, instead you were taught (or you figured out) that the way to grow up and be an adult is to push through, repress, suppress, pretend you’re confident, follow authority, go against authority, etc etc etc, and mind you, the deeper mind is still running all of the programs it’s running: child mind, guard mind (childhood protector parts, the protective reactions learned as a child), body mind, intuitive mind, fantasy mind (trying to become guidance mind), etc etc

Published:

> Instead, most of us learned to push through, suppress emotion, perform confidence, obey or rebel against authority, and call that adulthood. Meanwhile, the deeper mind kept running its own programs: the child wanting safety, the guard expecting danger, the body remembering what the intellect had explained away, the intuition speaking before language, and the fantasy trying to become guidance.

Reader: The list names the parts but drops what each one wants or does (the child wanting safety, the guard expecting danger, the body remembering what the intellect had explained away, the intuition speaking before language), and "all of the programs it’s running" says nothing on its own.

My check: A long run-on, and what each part wants is gone; the paragraph came up on his 25 Oct page (quote marks)

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (1.5, rated small)_

**F1.6** · vaguer · Quick start: do this first, P1 · a small snag

Now:

> To work on difficulties or cultivate positive qualities (love, curiosity, play, confidence, etc.), simply do these steps, in order: 1) Attention; 2) Notice; 3) Offer one fitting response; 4) Wait; 5) Come all the way back.

Published:

> Gather attention, notice what is here, offer one fitting response, wait, then come all the way back.

Reader: The first two steps shrink to the bare labels "Attention" and "Notice", so what to do with attention and what to notice (what is here) is no longer said.

My check: 'Attention' and 'Notice' as bare labels

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (1.28, rated small)_

**F1.7** · lost · Quick start: do this first, P2 · a small snag

Now:

> Give yourself a chunk of time when you can be physically secure for the time it takes. Put this screen on the shelf and conduct the practice.

Published:

> Set aside time somewhere physically secure. Choose one purpose and what you are leaving alone today. Then put the screen aside; the practice is something you learn to conduct, not a checklist to keep reading.

Reader: The step of choosing one purpose and what to leave alone today is gone, as is the reason for putting the screen away.

My check: The 'choose one purpose' step was a repeat he approved cutting on 25 Oct (RP-1.3); 'put this screen on the shelf' is odd

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (1.30, rated matters)_

**F1.9** · unclear · Quick start: do this first, P4 · a small snag

Now:

> If at any point you feel panicky, disoriented, more unreal, or less functional, this is not about bravely sticking with difficult feelings (that's another choice, made freely & while staying present). Stop deepening, return to the room & get appropriate support.

Published:

> When you become panicky, disoriented, increasingly unreal, or less able to function, stop deepening and return to the room and appropriate support. A difficult feeling you freely choose to stay with while present is a different situation.

Reader: The instruction to stop comes after a negated "this is not about..." and a parenthetical "that's another choice", so the reader must work out what "this" and "that" refer to before reaching what to do.

My check: The instruction to stop comes after 'this is not about...' and 'that's another choice'

_came in: 18 Oct (the overnight Emulate run)_

**F1.12** · unclear · Protecting Yourself from Hypnotists, P6 · a small snag

Now:

> With self-hypnosis you can do much of the same thing from the inside, by befriending and listening to the deeper part of your mind.

Published:

> Advertising, fear, craving, screens, tribe, resentment, authority, loneliness, and repetition are already training the mind. Self-hypnosis lets you practice from inside it: befriending the deeper layers, listening closely, and making adult choice more available.

Reader: "The same thing" has no clear referent now that the sentence saying advertising, fear, craving and the rest are already training the mind is gone, and "do the same thing" (control? influence?) fits poorly with "befriending and listening".

My check: His approved cut of 25 Oct (RP-1.4) took the sentence 'the same thing' leaned on; the Silva quote above half carries it

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (1.44, rated small)_

**F1.14** · unclear · Forget the left-brain/right-brain cartoon, P3 · a small snag

Now:

> The mind of intuition and the mind of rationality can BOTH be there - intuitive signals and testing of those signals without dogma or killing them.

Published:

> The intuitive mind offers signals without becoming dogma. The rational mind tests signals without killing them.

Reader: "Without dogma or killing them" folds two separate points into one phrase (intuition offers signals without becoming dogma; testing happens without killing the signals), so it is not clear what is without what.

My check: 'without dogma or killing them' folds two points into one phrase

_came in: 18 Oct (the overnight Emulate run)_

**F2a.2** · lost · A useful map of the mind, P5 · a small snag

Now:

> If you need to work with the ecology in the subconscious (child parts, guards, critic, fantasy making parts, body memories, social part, spiritual part (God/source/best benefit of all beings part) wiser part etc etc) then:

Published:

> When you need precision, notice the different tendencies inside it: the child wanting love, the protector wanting safety, the critic wanting standards, the fantasy-maker wanting possibility, the body memory wanting recognition, the social self wanting belonging, the spiritual self wanting God or source or the benefit of all beings, and the wiser part wanting what is true.

Reader: What each part wants is gone, and the nested parenthetical with no comma before "wiser part" tangles the list, so the parts are named but not made recognizable.

My check: What each part wants is gone, and the nested brackets tangle the list

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (1.74, rated small)_

**F2a.7** · unclear · When the adult role is not available yet, P7 · a small snag

Now:

> This is a borrowed figure, so you’re still making the choice.

Published:

> The borrowed figure stays beside your judgment rather than replacing it.

Reader: "This" has no clear referent, "borrowed figure" has not been introduced as a term in NOW, and why borrowing leaves the choice with you is left for the reader to guess.

My check: 'This is a borrowed figure' leans on the adult hat two lines up

_came in: 18 Oct (the overnight Emulate run)_

**F2a.8** · garbled · When the adult role is not available yet, P8 · a small snag

Now:

> If you can’t imagine good, or just imagining a caring grown-up makes you feel more threatened, or lonelier, start smaller, with the least cruel response you can believe.

Published:

> Begin with the least cruel response you can believe if warmth is unavailable.

Reader: "Imagine good" is missing its object, so the reader has to guess whether it means a good adult or a good response.

My check: 'If you can't imagine good' is missing its noun (a good adult)

_came in: 25 Oct (the answers of his first marking page)_

**F2a.10** · unclear · Let the child speak without handing over the steering wheel, P1 · a small snag

Now:

> In this way, you can access all of the positive aspects of what it can be like to feel younger such as feeling wonder, silliness, approaching things through the senses more, feeling it’s ok to be vulnerable, to let someone take care of you, to feel need, and to want to offload some decision making.

Published:

> Wonder, play, vivid sensation, vulnerability, honest need, or the wish to carry fewer decisions can all come forward while the internal adult remains present.

Reader: "To let someone take care of you" reads against the opening "without handing over the adult part of you to the caretaker in another person", and the list no longer says the adult stays present while these come forward.

My check: 'to let someone take care of you' sits against 'without handing over the adult part of you to the caretaker in another person'

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (2.24, rated small)_

**F2b.6** · unclear · The two-hand practice, P1 · a small snag

Now:

> Just place one hand in the center of your chest which is physically connecting you to your love and then place your other hand just below that which is your solar plexus and where your child can be.

Published:

> Place one hand at the center of the chest as a physical connection to love. Put the other at the solar plexus, just beneath the chest, where you can relate to the vulnerable child.

Reader: "just below that which is your solar plexus" can be read as below the solar plexus rather than at it, and the two "which" clauses make the reader sort out what each one refers to.

My check: 'just below that which is your solar plexus' can read as below the solar plexus

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (2.37, rated small)_

**F2b.9** · unclear · The Nurturer, P1 · a small snag

Now:

> You don't have to move their feelings, just sit back and enjoy them.

Published:

> The Nurturer brings warmth without trying to rush the feeling away, and takes pleasure in the child’s company: “I’m glad you’re here.” The child needs to be enjoyed, not only comforted when hurt.

Reader: "Move their feelings" is vague (published: not rushing the feeling away) and "enjoy them" reads as enjoying the feelings, painful ones included, rather than the child's company.

My check: 'enjoy them' can read as enjoying their feelings, not their company

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (2.40, rated small)_

**F2b.12** · lost · The Protector, P2 · a small snag

Now:

> A lot of times, inner child work doesn't work because people are doing all the fluffy stuff but then they go and text the person who is destabilizing them, or they don't eat, or they don't do whatever it is they're supposed to be doing.

Published:

> This is where inner-child practice often turns decorative. The voice says loving things while the adult sends the destabilizing message, skips the meal, avoids the task, and breaks the promise. Trust begins when you handle the consequence.

Reader: The conclusion that trust begins when you handle the consequence is gone, so the passage states the failure but not what builds trust.

My check: 'trust begins when you handle the consequence' is gone

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (2.45, rated matters)_

**F2b.13** · unclear · The Protector, P3 · a small snag

Now:

> Make sure they're small enough that you can actually do them.

Published:

> Make it small enough to carry out and review what actually happened.

Reader: "They" follows "your inner child" and so reads as the child being small, and the published step of reviewing what actually happened is not given.

My check: 'they're small enough' can read as the child (the 18 Oct triage let this one stand)

_came in: 18 Oct (the overnight Emulate run)_

**F3a.11** · vaguer · Don’t rush the repair, P3 · a small snag

Now:

> What does the child need? warmth, to play, to be protected, to mourn, to be angry, food, rest, boundaries, better relationships, to stop fantasizing, to stop working their butt off, that you keep a promise to them for one day, etc. etc.

Published:

> The need may be warmth, play, protection, grief, anger, food, rest, a boundary, a safer relationship, less fantasy, less overwork, or one adult promise kept today.

Reader: "Keep a promise to them for one day" can be read as keeping a promise for a day rather than following through on one promise today.

My check: 'keep a promise to them for one day' can read as keeping it for a day

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (2.85, rated small)_

**F3a.13** · garbled · Don’t rush the repair, P9 · a small snag

Now:

> Give yourself some time to let what you did sink in- it may take some time, it may take you to go to sleep, etc.

Published:

> Wait: let the response settle. Some changes need quiet, sleep, or ordinary time.

Reader: "It may take you to go to sleep" doesn't parse, and the reader has to guess it means sleeping on it.

My check: 'it may take you to go to sleep' doesn't parse

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (3.0, rated small)_

**F3b.1** · garbled · Play and rest still need an adult present, P1 · a small snag

Now:

> Whether that means touching things of different textures, drawing, exercising, roleplaying with a plushie in a different voice, etc.

Published:

> A younger state may respond to texture, drawing, movement, a plushie with a voice, or whatever feels interesting.

Reader: A "Whether" clause with no main clause stands as a sentence, so the reader has to reattach it to the sentence before.

My check: A 'Whether that means ...' fragment after the sentence it belongs to

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (3.12, rated small)_

**F3b.2** · lost · Play and rest still need an adult present, P2 · a small snag

Now:

> Now, before you get to resting, it’s okay to limit the amount of decisions you are going to be making for a certain amount of time, it’s okay to put the things you might not get to on a list and it’s okay to let your inner adult keep watch for a while.

Published:

> Rest also doesn’t require helplessness. Reduce decisions for a defined period, put unfinished tasks somewhere visible, and let the internal adult keep watch. You remain able to move, stop, and return.

Reader: NOW drops "Rest also doesn't require helplessness" and "You remain able to move, stop, and return", so the three "it's okay to" permissions no longer say what the inner adult's watch is for or that you stay in control.

My check: 'rest doesn't require helplessness' and 'you remain able to move, stop and return' are gone

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (3.13, rated matters)_

**F3b.5** · lost · When “your voice” is everybody else’s voice, P1 · a small snag

Now:

> So you can do reparenting and finding yourself in parallel. For others, it is very easy to work with the inner child, they can feel it easily.

Published:

> Reparenting and identity-building can proceed together. For some people the child-self is already easy to feel. For others, creating enough safety for preference, curiosity, and experimentation is part of how that self becomes easier to hear.

Reader: NOW drops PUBLISHED's point that, for people without a developed private self, creating safety for preference, curiosity and experimentation is part of how the child-self becomes easier to hear, so "in parallel" has no stated reason.

My check: Why reparenting and finding yourself go together is gone

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (3.26, rated matters)_

**F3b.7** · lost · When “your voice” is everybody else’s voice, P10 · a small snag

Now:

> One way of explaining this is that in your childhood you didn’t spend enough attention in finding out what you like and what you want to try out and who you are when nobody is grading you. You were too busy avoiding pain, reading what was dangerous and what you had to do to stay in a good bond, etc.

Published:

> A useful developmental explanation is that when childhood is organized around avoiding pain and preserving attachment, attention goes into reading danger, meeting expectations, and keeping the bond. That can leave less room for the ordinary experiments that answer, “What do I like? What do I want to try? Who am I when nobody is grading me?” This is a practical model, not a claim about one specific brain system.

Reader: NOW drops PUBLISHED's hedge ("can leave less room") and its closing caveat that this is a practical model, not a claim about one specific brain system, and states the explanation as flat fact about the reader's own childhood.

My check: 'a practical model, not a claim about one brain system' is gone

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (3.33, rated matters)_

**F4a.2** · lost · If you sense you are being influenced, P3 · a small snag

Now:

> You will soon realize that I am right …. Or you may, in time, decide to admit that …. Or the only reason you do not agree is …. Or part of you already knows …. Or your higher self wants …. Or everyone who is awake knows …. Or the reason you do not believe that is true is because your ego does not want you to …

Published:

> The grammar assumes the conclusion, turns resistance into proof, and makes obedience feel like awakening.

Reader: NOW gives the example phrases without PUBLISHED's sentence saying what they do (assume the conclusion, turn resistance into proof, make obedience feel like awakening), so the reader is left to work out what makes each one manipulative.

My check: The sentence saying what these phrases do (assume the conclusion, turn resistance into proof) is gone

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (3.62, rated small)_

**F4a.4** · unclear · Soft language can still take away choice, P1 · a small snag

Now:

> Be aware that even when using permissive language, you can still take away choice.

Published:

> Permissive words can still conceal coercion. I watch for the following:

Reader: The previous section addressed "you" as the person being influenced, so "you can still take away choice" (followed by the new term "the subject") leaves it unclear whether the reader is giving or receiving the suggestions.

My check: 'you can still take away choice' doesn't say whose

_came in: 18 Oct (the overnight Emulate run)_

**F4a.5** · lost · Soft language can still take away choice, P5 · a small snag

Now:

> 3) Including phrases such as whether or not you notice etc etc

Published:

> “Whether you notice it or not” binds: uncertainty is converted into invisible success that cannot be checked.

Reader: NOW drops why this phrase is a problem (uncertainty is turned into invisible success that cannot be checked), so the item names a phrase and trails off with "etc etc" without saying what to watch for.

My check: Why 'whether or not you notice' is a bind is gone

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (3.76, rated small)_

**F4a.7** · lost · What an induction is actually doing, P2 · a small snag

Now:

> Test: Are you getting the response you want out of this already? If so, you might not need to deepen.

Published:

> For a simple, chosen target, you can test the suggestion before deepening. If the useful response is already happening, build from it. An induction helps you find a receptive way of listening; you don’t need to complete a ceremony before you’re allowed to respond.

Reader: NOW drops what is being tested (the suggestion, for a simple chosen target) and what to do when the response is already happening (build from it), leaving "this" and "the response you want" with nothing to refer to.

My check: 'the response you want out of this' doesn't say the suggestion, for a simple chosen target

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (4.8, rated matters)_

**F4b.3** · lost · Please don’t put six metaphors in one trance, P2 · a small snag

Now:

> You can use whatever form of signal makes sense to you (feelings, rhythms, movements, words, spatial, simple knowing, lack of signal, whatever) but if you're using words, try to keep them related to whatever world you're creating.

Published:

> A signal may arrive through sensation, rhythm, movement, words, spatial sense, simple knowing, or no response at all. Keep the language in the world you chose: let a count mark something meaningful there, and reverse the journey when you finish.

Reader: PUBLISHED says a signal arrives in varied forms or not at all, but NOW has the reader "use" a form of signal without saying what a signal is, and leaves "spatial" and "the world you're creating" bare.

My check: 'whatever form of signal makes sense to you' doesn't say a signal can come in any form, or not at all

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (4.13, rated small)_

**F4b.4** · vaguer · Please don’t put six metaphors in one trance, P2 · a small snag

Now:

> (You can borrow qualities, but don't change who you are.)

Published:

> Borrow qualities such as warmth or steadiness without replacing your identity.

Reader: Without "such as warmth or steadiness" a reader can't tell what "qualities" are or what they are borrowed from.

My check: 'borrow qualities' without an example (warmth, steadiness)

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (4.14, rated small)_

**F4b.5** · lost · Please don’t put six metaphors in one trance, P3 · a small snag

Now:

> When you're writing this, think about what the verb you're using is, what the sensory quality is, what the short refrain is, and how you're going to transition between ideas. Read it out loud as you're writing it.

Published:

> Pick one central verb, one sensory quality, one short refrain, and one transition phrase, then read the script aloud; long elegant sentences become soup during an induction.

Reader: The instruction to pick one verb, one sensory quality, one refrain and one transition phrase becomes "think about" them, and "this" and "it" never name the script.

My check: 'think about what the verb is' for 'pick one verb, one sensory quality, one refrain'

_came in: 25 Oct (the answers of his first marking page)_

**F4b.7** · garbled · Before you begin, P4 · a small snag

Now:

> Deciding to do it. How will you coax yourself to do this? Make it spacious? Make it warm and held? Something else?

Published:

> Decide what kind of encouragement is welcome: spacious listening, warm company, or a firmer invitation to stay with a feeling.

Reader: "Deciding to do it." is a fragment, "Make it" has no clear "it", and the question shifts from what kind of encouragement is welcome to how you will talk yourself into starting, with the "firmer invitation" option reduced to "Something else?".

My check: 'Deciding to do it.' stands as a fragment, and the firmer-invitation option is gone

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (4.23, rated small)_

**F4b.8** · vaguer · Before you begin, P4 · a small snag

Now:

> If you are going to use a recording, read the script if you can.

Published:

> For a recording, read the script beforehand when possible.

Reader: Without "beforehand" a reader can't tell when to read the script, or why, if a recording will be playing.

My check: 'read the script' without 'beforehand'

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (4.24, rated small)_

**F4b.9** · unclear · Before you begin, P5 · a small snag

Now:

> You don't have to watch yourself all the time, but for the first time, make sure you can change state.

Published:

> Once you know how to change direction, you don’t need to supervise every moment.

Reader: "For the first time" doesn't say first time doing what, and "change state" replaces "change direction", so the condition that supervision can relax once you know how to change course becomes a vague caution.

My check: 'for the first time' doesn't say the first few sessions

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (4.29, rated small)_

**F4b.10** · unclear · Before you begin, P6 · a small snag

Now:

> Utilize. Use what you have to go to the next place, whatever it is.

Published:

> Utilization means working with what actually happens: a thought, sound, movement, or objection may change where the practice goes.

Reader: "Utilize." is an undefined one-word imperative, and "what you have" and "the next place" replace the examples (thought, sound, movement, objection) that explained it.

My check: 'Utilize.' is a bare technical word

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (4.30, rated small)_

**F4b.11** · unclear · Before you begin, P6 · a small snag

Now:

> Learn how to notice if there is no change, and that no change is not a positive change.

Published:

> Notice what actually happens; no change doesn’t mean secret success.

Reader: "No change is not a positive change" reads as a tautology and loses "doesn't mean secret success", so the warning against taking silence for progress is blurred.

My check: 'no change is not a positive change' for 'no change doesn't mean secret success'

_came in: 25 Oct (the answers of his first marking page)_

**F4b.13** · garbled · Sober induction: 3–5 minutes, P1 · a small snag

Now:

> You can read this slowly to yourself on your recorder, you can read it out loud or say it to yourself if you are good at that.

Published:

> Read this slowly into a recorder, speak it aloud, or learn its movement and use silent words if that comes easily.

Reader: "Read this slowly to yourself on your recorder" mixes silent reading with recording, and "say it to yourself" drops "learn its movement", so three ways of delivering the script blur into two overlapping ones.

My check: 'read this slowly to yourself on your recorder' mixes reading and recording

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (4.32, rated small)_

**F4b.14** · vaguer · Sober induction: 3–5 minutes, P1 · a small snag

Now:

> Choose a sound, or a contact, or the two hands thing (below) or something to anchor yourself, and choose the thing you will say to open it up.

Published:

> Choose one anchor—a sound, bodily contact, or your two-hand practice—and an opening phrase.

Reader: "The two hands thing (below)" points to something this part never describes, "something to anchor yourself" is circular, and "the thing you will say to open it up" no longer says it is an opening phrase or what "it" is.

My check: 'the two hands thing (below)': the two-hand practice is above, not below

_came in: 25 Oct (the answers of his first marking page)_

**F4b.17** · unclear · Sober induction: 3–5 minutes, P7 · a small snag

Now:

> You might notice something that you are doing that holds your interest, something about the sound, or sensation, or listening or something else.

Published:

> And as you return, you may find one detail that holds your interest … something about the sound, or the contact, or that particular way of listening … and let attention stay with it long enough to become curious.

Reader: "Something that you are doing that holds your interest" stacks two "that"s and names an action while the examples (sound, sensation) are things noticed, and the step of staying with it until curious is gone.

My check: 'something that you are doing that holds your interest' is awkward

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (4.38, rated matters)_

**F5.3** · lost · The two-hand induction, P5 · a small snag

Now:

> Sending my love down to my Child. If some comes back up, I let it, and send it on down again. If nothing comes back, I just keep sending mine.

Published:

> I send love to the child. I receive the child’s signal. I send love again. I listen again.

Reader: Receiving the child's signal and listening again become "if some [love] comes back up", so the listening step and the idea of a signal are gone and "some" and "it" are unanchored.

My check: The listening step is softened to 'if some comes back up'; the script still works

_came in: 25 Oct (the answers of his first marking page)_

**F5.6** · vaguer · A shortcut back into hypnosis, P1 · a small snag

Now:

> Once you have learned the above induction and how to come back down at the end, you can do the following….

Published:

> Learn a useful induction and the full return below before developing a shortcut.

Reader: "The above induction" does not say which of the several inductions, and the pointer to the full return, which comes further down, is lost.

My check: 'the above induction' doesn't say which of the inductions

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers)_

**F5.10** · unclear · Turning the shortcut off, or keeping it, P1 · a small snag

Now:

> For now, though, once you come out of this trance, it'll be over for today.

Published:

> Any retained cue is for a future, separately chosen session; today’s altered state ends with the return.

Reader: "It" could mean the trance, the cue or the work, and the point that a kept cue belongs only to a later, separately chosen session is not stated.

My check: 'it' could be the trance or the cue

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers)_

**F5.11** · unclear · Come all the way back, P2 · a small snag

Now:

> All the instructions you have given me to carry me deeper into this session or keep me in this state are now finished.

Published:

> All instructions to deepen or remain in this session are finished.

Reader: In a first-person script, "you have given me" brings in an unidentified "you" (a narrator? a part?) that the published version avoids.

My check: 'you have given me' in a self-hypnosis script brings in an unnamed speaker

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers)_

**F5.13** · lost · Let the next response guide you, P1 · a small snag

Now:

> Read through these sections, and then try doing the inner meeting without looking at the screen.

Published:

> The induction and inner meeting bring you to a place where you can listen. From here, learn to answer what happens instead of reciting a speech that has already decided what every part will say. Read these examples before practicing, then put the screen aside.

Reader: The section's point, to answer what happens rather than recite a speech that has already decided what every part will say, is not stated, so the reader isn't told why to put the screen aside.

My check: The reason to put the screen aside is gone, though the next paragraph carries most of it

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (5.23, rated matters)_

**F5.14** · vaguer · Let the next response guide you, P2 · a small snag

Now:

> The notice and invitation don't need to take all those forms, just notice and invite what happens.

Published:

> A sensation can lead to an image, a gesture, a feeling, or words; you don’t need to fill every category.

Reader: "Take all those forms" is hard to read as "you needn't go through every kind of response", and the idea that one thing can lead to the next is dropped.

My check: His own words; 'take all those forms' is a little hard to read

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (5.28, rated small)_

**F5.15** · vaguer · Finding your own words, P3 · a small snag

Now:

> You can be pretty straightforward when that's the help you chose - "Let the explanation wait a moment. What do I feel as I say that?" can be a perfectly valid thing to say to yourself, and help you focus. As long as you're still present, and able to change if you want to, and happy to carry on, a sad feeling or tension or whatever doesn't mean it's not ok.

Published:

> Directness can focus attention without deciding the answer. A difficult feeling needn’t become pleasant before you can stay with it. When you remain present, can change direction, and want to continue, sadness or tension alone doesn’t require an exit.

Reader: "Doesn't mean it's not ok" has no clear "it" and replaces "doesn't require an exit" (no need to stop), and the caution that directness focuses attention without deciding the answer is dropped.

My check: 'it's not ok' has no clear 'it'

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (5.30, rated small)_

**F5.17** · vaguer · Notice, meaning, and your thoughts on the meaning, P2 · a small snag

Now:

> Nonverbal thoughts and early thoughts aren't necessarily any better or worse than other thoughts.

Published:

> Nonverbal doesn’t mean deeper or truer; earlier doesn’t mean more reliable.

Reader: "Better or worse" doesn't name the measure (deeper, truer, more reliable) on which the published sentence says these impressions do not win.

My check: 'better or worse' doesn't say deeper, truer or more reliable

_came in: 18 Oct (the overnight Emulate run)_

**F6a.3** · lost · Let the response change the invitation, P3 · a small snag

Now:

> Sometimes it just isn't right - sometimes it's something you hadn't thought of.

Published:

> Sometimes the sentence was simply wrong. Sometimes an unfamiliar possibility brings a feeling worth meeting. You don’t have to decide which before making space to find out.

Reader: "it" has no referent (the sentence or invitation), the unfamiliar possibility no longer "brings a feeling worth meeting", and the point that you needn't decide which case it is before making space to find out is dropped.

My check: 'Sometimes it just isn't right' doesn't say what 'it' is

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (5.39, rated small)_

**F6a.6** · vaguer · Look at the situation too, P1 · a small snag

Now:

> Are they able to communicate in a mature fashion?

Published:

> Can they hear disagreement, take responsibility, and make room for your experience?

Reader: Three concrete behaviors to look for became "communicate in a mature fashion", which gives the reader nothing to observe and invites the very maturity judgment the next sentences warn against.

My check: 'communicate in a mature fashion' for 'hear disagreement, take responsibility, make room for your experience'

_came in: 18 Oct (the overnight Emulate run)_

**F6a.7** · unclear · Look at the situation too, P1 · a small snag

Now:

> You don’t need to subject yourself to something that may be dangerous to determine if this is the case.

Published:

> You don’t need repeated exposure to danger before protecting yourself.

Reader: "this" could mean that they are emotionally immature or that it is dangerous, and the point changed from "protect yourself without waiting for repeated exposure to danger" to "don't risk danger to test whether they are immature".

My check: 'to determine if this is the case' has no clear 'this'

_came in: 18 Oct (the overnight Emulate run)_

**F6a.11** · garbled · Look at the situation too, P2 · a small snag

Now:

> Do you need to end the interaction prematurely?

Published:

> Sometimes it is mutual understanding; sometimes it is conveying information, saying no, or ending the exchange.

Reader: "Prematurely" does not fit, since PUBLISHED presents ending the exchange as a legitimate purpose and "premature" suggests ending it too early.

My check: 'end the interaction prematurely' makes ending it sound like a mistake

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (5.41, rated small)_

**F6a.12** · lost · Change the amount of contact, P1 · a small snag

Now:

> Keep moving back and forth between the difficult thing and the easier thing. This is called pendulation and titration.

Published:

> Let that support become noticeable alongside the difficulty. Moving between difficult and more manageable experience is often called pendulation; approaching in smaller amounts is titration.

Reader: Two different things (pendulation is moving between, titration is approaching in smaller amounts) became one label for one action, so titration is never explained, and the idea of noticing support alongside the difficulty is gone.

My check: Pendulation and titration given as one thing

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (5.42, rated small)_

**F6a.13** · lost · Change the amount of contact, P2 · a small snag

Now:

> Ok, I think that is enough for now.

Published:

> I can let this much be here and notice the support beside it.

Reader: The quoted self-statement about letting a small amount be here with support beside it is replaced by an unquoted "enough for now" that reads as a stray line and says stop instead of staying with a little plus support.

My check: A self-talk line standing alone with no lead-in

_came in: 18 Oct (the overnight Emulate run)_

**F6a.16** · unclear · If you feel an urge to move, P1 · a small snag

Now:

> You do not need to act out the urge, feel that you need to move, shake, release, etc.

Published:

> You’re not obliged to enact an impulse, shake, or produce a release.

Reader: The list mixes "act out the urge" with "feel that you need to move, shake, release", so it is unclear whether you needn't do these things or needn't feel they are needed.

My check: 'act out the urge, feel that you need to move' mixes doing and feeling

_came in: 18 Oct (the overnight Emulate run)_

**F6a.22** · unclear · Offer the care that is actually wanted, P5 · a small snag

Now:

> Allow yourself to see where the metaphor takes you.

Published:

> A metaphor can develop before you decide what it means.

Reader: "the metaphor" has no antecedent in this part (the image only appears in the question that follows), and "before you decide what it means" is lost.

My check: 'the metaphor' comes before any metaphor is named

_came in: 18 Oct (the overnight Emulate run)_

**F6a.24** · garbled · Finish without forcing a revelation, P1 · a small snag

Now:

> Ending the session.

Reader: A fragment standing as a sentence right under a heading that already says it, which reads as a stray label rather than part of the prose.

My check: A stray label repeating the heading

_came in: 18 Oct (the overnight Emulate run)_

**F6b.2** · lost · The 15-minute daily practice, P1 · a small snag

Now:

> You are simply practicing for fifteen minutes or so.

Published:

> Fifteen minutes is a convenient appointment with yourself, not a therapeutic dose or a timetable your feelings must follow.

Reader: The point that fifteen minutes is a convenience and not a prescribed dose or a schedule for your feelings is gone, so the length now reads as the instruction.

My check: 'fifteen minutes is a convenience, not a dose your feelings must follow' is gone

_came in: 18 Oct (the overnight Emulate run)_

**F6b.3** · unclear · The 15-minute daily practice, P2 · a small snag

Now:

> You can also try other ways of inducing yourself such as becoming aware of 3 things you can see, 3 things you can hear, 3 things you can feel in your body; then 2 of each, 1 of each, counting from 5 to 1 and beginning to listen.

Published:

> Another simple entry is to notice three things you see, three you hear, and three bodily sensations; then two of each, then one. Count from five to one and begin listening.

Reader: "counting from 5 to 1" is run on to the 3-2-1 senses sequence, so a reader can't tell it is a separate countdown to do after it.

My check: The 5-to-1 countdown runs on from the 3-2-1 senses list

_came in: 18 Oct (the overnight Emulate run)_

**F6b.6** · unclear · The 15-minute daily practice, P4 · a small snag

Now:

> As you come out of the process ask yourself what you learned needed warmth, what needed to be protected, what you need to do differently to be more in accord with truth and love and life.

Published:

> Afterward, ask what needed warmth, what needed protection, and what direction serves truth, love, and life.

Reader: "what you learned needed warmth" is an awkward embedded clause a reader has to reparse (what needed warmth, and what did you learn?), and the three items of the list no longer match in form.

My check: 'what you learned needed warmth' has to be read twice

_came in: 18 Oct (the overnight Emulate run)_

**F6b.14** · unclear · It feels fake, P1 · a small snag

Now:

> If it feels like you are being asked to do something you don't want to do then correct this.

Published:

> Correct an explicitly unwanted invitation.

Reader: "Correct this" doesn't say what is to be corrected or who is asking, and "if it feels like" replaces "explicitly unwanted".

My check: 'correct this' doesn't say what to correct

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (6.19, rated small)_

**F7.5** · vaguer · You dissociate or feel unreal, P1 · a small snag

Now:

> Open your eyes, move around, feel something textured, name 5 things that you can see, and end your work for the day.

Published:

> Open your eyes. Move. Touch something textured. Name five objects. End the deeper practice for the day.

Reader: "End your work for the day" could be read as stopping your job, where PUBLISHED said to end the deeper practice.

My check: 'end your work for the day' can read as your job

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (6.37, rated small)_

**F7.6** · unclear · You become grandiose, P2 · a small snag

Now:

> What do you say to yourself in that moment? “If it’s really there, it’ll still be here after a good night’s sleep, some food, some time, etc, and some subsequent humility, feedback, etc, etc.”

Published:

> “If this insight is real, it will survive sleep, food, time, humility, and feedback.”

Reader: The insight is never named, so "it" and "there" have no referent, and the list with "etc, ... etc, etc" is hard to follow.

My check: 'it' is the insight the heading implies; the 'etc, etc' is noise

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (6.38, rated small)_

**F7.10** · vaguer · You get stuck in spiritual bypass, P2 · a small snag

Now:

> Maybe when you prayed it seemed like you were being abandoned and condemned. Maybe you felt betrayed by a spiritual teacher. It may be worth exploring these, but you might not want to do more of the same.

Published:

> Prayer can also evoke abandonment or condemnation, or a teacher’s betrayal can damage something sacred. Ask what was lost and what needs questioning; more of the same practice isn’t automatically the answer.

Reader: The concrete step "ask what was lost and what needs questioning" becomes "exploring these", and "more of the same" no longer says more of what.

My check: 'more of the same' doesn't say more of what

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (6.45, rated small)_

**F7.11** · vaguer · You get stuck in endless processing, P2 · a small snag

Now:

> You don’t have to do any certain thing before you start your life.

Published:

> You don’t have to hold an inner meeting every time a thought appears or complete a ritual before you’re allowed to live.

Reader: "Complete a ritual" becomes the awkward and vague "any certain thing".

My check: 'any certain thing' is awkward

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (6.53, rated small)_

**F7.13** · unclear · What not to do, P1 · a small snag

Now:

> DO NOT: View your inner experiences as anything but internal happenings that need to be reality tested at all times.

Published:

> Do not treat inner voices, images, autonomous movements, or body signals as commands or proof. Listen, then reality-test.

Reader: The double negative "do not view as anything but" forces a reread, and "commands or proof" and the "listen" step are lost.

My check: A double negative; 'not commands' is gone

_came in: 18 Oct (the overnight Emulate run)_

**F7.20** · unclear · Methods to explore with a trained person present, P1 · a small snag

Now:

> Ask any potential person what they would do and how they deal with uncertainty and unexpected reactions.

Published:

> Ask what is intended and how uncertainty and unexpected reactions will be handled.

Reader: "Any potential person" is an odd stand-in for a prospective clinician.

My check: 'any potential person' for someone you're thinking of working with

_came in: 18 Oct (the overnight Emulate run)_

**F7.21** · unclear · Closing, P1 · a small snag

Now:

> Start from the basis that the subconscious, the body, the sharp mind, and the guy who’s tensed up and ready for the other shoe to drop for a long time are all not your enemies.

Published:

> The subconscious isn’t the enemy. Neither are the body, the sharp analytical mind, or the protector that has been braced for years.

Reader: "The guy" replaces "the protector", so a reader may not realise it means the inner protector part from the earlier sections.

My check: 'the guy who's tensed up' may not read as the protective part

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (6.78, rated small)_

**F7.22** · lost · Closing, P1 · a small snag

Now:

> Most of them are actually trying to help you.

Published:

> Most of them have been trying to help without ever being properly introduced.

Reader: The point that these parts have been trying to help without ever being acknowledged or introduced is dropped.

My check: 'without ever being properly introduced' is gone

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (6.77, rated small)_

**F7.24** · vaguer · Try it in the Inner Signal app, P1 · a small snag

Now:

> You may want to find someone, but it is not required to graduate.

Published:

> Self-hypnosis doesn’t require an app, and finding a practitioner is an option rather than a graduation requirement.

Reader: "Find someone" does not say a practitioner, and "graduate" is left without any context.

My check: 'not required to graduate' has no context

_came in: 18 Oct (the overnight Emulate run)_

**F8a.1** · lost · Appendix A: How to ask the subconscious a useful question, P1 · a small snag

Now:

> However, there is a bit of overlap in the way you can ask questions to both. So, if you know how to do prompt engineering for AI, this can be very useful to help you be more present, honest, loving etc. On the other hand, you should NEVER use it to be more controlling.

Published:

> The subconscious isn’t an AI model, but prompt engineering offers one useful lesson: the shape of a question changes what kind of answer can appear. A prompt should make you more present, honest, loving, and able to hear the next signal—never more controlling.

Reader: NOW drops the one lesson prompt engineering gives (the shape of a question changes what kind of answer can appear), leaving only "a bit of overlap" and an unanchored "this" and "it".

My check: The one lesson prompt engineering gives (the shape of a question changes the answer) is gone; 'this' and 'it' lean on it

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (7.9, rated small)_

**F8a.2** · vaguer · Appendix A: How to ask the subconscious a useful question, P6 · a small snag

Now:

> Constraint: What do you need to do to make sure your asking is safe, true, kind etc.

Published:

> Constraint: safety, truth, kindness, no forcing, no false certainty, and capacity before content.

Reader: Three of the constraints (no forcing, no false certainty, capacity before content) are gone and the list shrinks to "safe, true, kind etc."

My check: Three of the constraints (no forcing, no false certainty, capacity before content) are gone

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (7.15, rated small)_

**F8a.4** · lost · Appendix A: How to ask the subconscious a useful question, P11 · a small snag

Now:

> A peaceful silence would be a successful answer to my question.

Published:

> Sometimes nothing answers because nothing is happening. Sometimes the answer is not yet, rest first, build capacity, or do the ordinary thing you already know to do.

Reader: The published guidance on what silence can mean (nothing is happening, not yet, rest first, build capacity, do the ordinary thing) has no counterpart anywhere after this sentence in NOW.

My check: What silence can mean (nothing is happening, not yet, rest first) is gone

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (7.20, rated small)_

**F8a.6** · lost · Core prompts, P7 · a small snag

Now:

> Let my body give me feedback as to the difference.

Published:

> “If this daydream is useful, reveal the guidance inside it. If it is avoidance, bring me gently into the present and help me deal with what I need to deal with.” “What is anxiety trying to protect, and what would help it trust the adult self?” “If the full truth would overwhelm me, please do not reveal it all. Show me the capacity before the content.”

Reader: The prompts for daydreaming (useful guidance versus avoidance), anxiety and hidden truth are dropped, so those situations no longer have a script.

My check: Three example prompts (daydream, anxiety, hidden truth) are gone

_came in: 18 Oct (the overnight Emulate run)_

**F8a.9** · unclear · The Milton Model, minus the covert sales seminar, P1 · a small snag

Now:

> To do this we are going to use a model that’s called the Milton model.

Published:

> The Milton Model concerns the architecture of the sentence.

Reader: "To do this" has no antecedent as the first sentence under the heading, so a reader cannot tell what the model is for.

My check: 'To do this' opens the section with nothing to point to

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers)_

**F8a.11** · lost · Pattern 3: Presuppositions, P1 · a small snag

Now:

> Presumption is a powerful thing, so please don’t use it except to presume that we will have the choice of when it will happen, that we will be able to do it, that we are safe, that we are loved and that our adult can lead us.

Published:

> A presupposition hides an assumption inside a sentence. Use that power only to presume choice, timing, capacity, safety, love, and adult leadership. Don’t smuggle in obedience.

Reader: NOW never says what a presupposition is or gives an example, drops "Don’t smuggle in obedience", and "when it will happen" and "able to do it" have no referent.

My check: What a presupposition is and 'don't smuggle in obedience' are gone; 'when it will happen' has no referent

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (7.55, rated matters)_

**F8a.12** · lost · Pattern 4: Gentle cause-effect bridges, P1 · a small snag

Now:

> However, even if you say them in a lovely gentle voice it doesn’t mean that it’s true if it isn’t! It’s not very likely that just by breathing in and out that your trauma is going to go away!

Published:

> A gentle voice doesn’t make a false causal claim true. Too strong: “Because I breathe, the trauma leaves.” Better: “As I breathe, the adult self may become present enough to hear one small piece of what the wound needs.”

Reader: NOW gives only the false causal claim and drops the "Better" gentle phrasing and "Use them carefully", so a reader is told what not to say but not what to say, and "it doesn’t mean that it’s true if it isn’t" leaves "it" unanchored.

My check: The better wording to use is gone; 'it doesn't mean that it's true if it isn't' is loose

_came in: 25 Oct (the answers of his first marking page)_

**F8b.1** · lost · Submodalities — editing the form, not denying the truth, P2 · a small snag

Now:

> How is this represented for you? Can you allow yourself to move that image back a couple of feet? Can you soften the edges of that image? Can you turn the volume down on that voice in your head? Etc.

Published:

> Ask how the experience is represented. What changes when the image moves two feet back, the voice gets quieter, or the edge becomes less sharp?

Reader: The published question "what changes" (noticing the effect of each adjustment) is gone, leaving only a list of adjustments, and "that image" and "that voice" appear with no earlier mention.

My check: 'what changes' when you adjust the image is gone

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (8.14, rated small)_

**F8b.3** · lost · Anchoring — giving the body a doorway back, P1 · a small snag

Now:

> There are many ways to do this. Put your hand on your heart, touch two fingers together, use a breath, a word, a particular body posture, smell, song, whatever.

Published:

> An anchor is a cue connected to a state: a hand on the heart, two fingers touching, a breath, a word, a posture, scent, or song.

Reader: The definition of an anchor (a cue connected to a state) is dropped, so "this" in "many ways to do this" has nothing to refer to.

My check: What an anchor is (a cue connected to a state) is gone; the heading carries 'this'

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (8.20, rated small)_

**F8b.4** · unclear · Anchoring — giving the body a doorway back, P1 · a small snag

Now:

> Feel a state that you have got to in reality that you want to be able to get to easily when you need to. Do your anchor thing and say to yourself that this is available to you. Do make sure you do it when you have clearly got it.

Published:

> Find a real state you want easier access to, feel it, and pair the cue while it is clearly present with the phrase, “This is available.”

Reader: The key step of pairing the cue with the phrase while the state is clearly present is spread across loose wording ("got to in reality", "your anchor thing", "do it", "got it") that a reader has to decode.

My check: 'do your anchor thing ... when you have clearly got it' is loose: pair the cue while the state is clearly there

_came in: 25 Oct (the answers of his first marking page)_

**F8b.5** · vaguer · Anchoring — giving the body a doorway back, P1 · a small snag

Now:

> To get yourself back into a good hypnosis state easily, don’t go for a peak state but for a good hypnotic state.

Published:

> For hypnotic re-entry, choose a usable receptive state rather than peak emotional intensity; follow “A shortcut back into hypnosis” in the main induction section.

Reader: "Peak state" is never said to mean peak emotional intensity and "a good hypnotic state" doesn't say what makes it good, so the contrast with a usable receptive state is vague.

My check: 'peak state' vs 'a good hypnotic state' is vague

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (8.22, rated small)_

**F8b.6** · garbled · Using synchronicity as your own wake-up bell, P1 · a small snag

Now:

> Using synchronicity (The synchronicity wake up cue)

Reader: A verbless fragment sits under the heading and repeats it without saying what it is for.

My check: A stray label repeating the heading

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (8.25, rated small)_

**F8b.7** · lost · Using synchronicity as your own wake-up bell, P2 · a small snag

Now:

> People often ask what the synchronicity means. Sometimes they get a great insight from it, but other times they get obsessed trying to work out patterns etc. I am using the noticing of the synchronicity to WAKE UP.

Published:

> People notice a synchronicity and immediately ask what it means. Sometimes that opens insight; sometimes it starts compulsive pattern-hunting. I prefer using the moment of noticing as a wake-up bell. The coincidence doesn’t have to contain a message. It has already captured attention, which is enough.

Reader: The reason the noticing works as a bell, that the coincidence needn't contain a message and has already captured attention, is dropped.

My check: Why noticing works as a bell (the coincidence needn't carry a message) is gone

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (8.26, rated matters)_

**F8b.8** · unclear · Using synchronicity as your own wake-up bell, P4 · a small snag

Now:

> From that state I feel my feelings. If I am in a negative state, I check if it is a message from my Inner Child or from a childhood guard part, or if I just need to grieve.

Published:

> A negative state may still contain an inner-child need, a Protector warning, grief, a bodily problem, or a real demand for action.

Reader: "that state" (the highest state just described) is followed at once by "a negative state" with no sign whether that is the original mood or the highest state, so a reader can't tell which state the checks apply to.

My check: 'a negative state' right after 'that state' (the highest one)

_came in: 25 Oct (the answers of his first marking page)_

**F8b.11** · lost · Installing the synchronicity cue, P10 · a small snag

Now:

> This is very similar to implementation intention. I'm not aware of research into implementation intention for this specific thing, but the general mechanisms appear to work; Gollwitzer’s paper explains how and why they work.

Published:

> Psychologically, this resembles an implementation intention: an advance “if X, then Y” plan that links a recognizable cue with a chosen response. Gollwitzer’s foundational paper supports the general mechanism. This particular use of synchronicity hasn’t been studied directly.

Reader: "Implementation intention" is used without the "if X, then Y" explanation, "this specific thing" doesn't say what the specific thing is, and "explains how and why they work" claims more than "supports the general mechanism".

My check: 'implementation intention' isn't explained until later, and 'this specific thing' is vague

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (8.41, rated matters)_

**F8b.16** · lost · The Swish, softened, P1 · a small snag

Now:

> Swish Variation: 2) I use an NLP technique called a "Swish Pattern" (it swaps a picture of an old reaction for a picture of a new one), but I will allow my old pattern to be there, while also holding my new pattern in my awareness. I feel what comes up somatically, and compare the differences between the future scenarios of my old and new patterns.

Published:

> Classic NLP uses the Swish to replace an old self-image with a new one. Done mechanically, it can feel like an inner eviction. Here, the old pattern stays visible, the new possibility stands beside it, and I notice the body’s response while comparing what each future would actually require.

Reader: The reason for the softened version (done mechanically it can feel like an inner eviction) is dropped, and "what each future would actually require" became the vaguer "compare the differences".

My check: Why the softened Swish (done mechanically it feels like an inner eviction) is gone

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (8.57, rated small)_

**F9.2** · vaguer · What I will not use NLP for, P5 · a small snag

Now:

> I do not use NLP to manipulate other people or convince myself of my intuition.

Published:

> To manipulate anyone else. To convince myself an intuition is true.

Reader: "convince myself of my intuition" no longer says an intuition is being made to feel true, so it can be read as convincing myself that I have one.

My check: 'convince myself of my intuition' can read as convincing myself I have one

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (8.67, rated small)_

**F9.5** · vaguer · Running the whole NLP sequence, P3 · a small snag

Now:

> Ask for their permission.

Published:

> Ask permission. Is it useful to work with this image, feeling, or pattern today?

Reader: The question that says what the permission is for (working with this image, feeling, or pattern today) is gone, leaving a bare step.

My check: What the permission is for is gone

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (8.74, rated small)_

**F9.8** · vaguer · Running the whole NLP sequence, P11 · a small snag

Now:

> Get the person out of the altered state (bring them back to the room and have them do something).

Published:

> Exit and act. Come back to the room. Do one ordinary thing.

Reader: "do one ordinary thing" (a grounding return to ordinary life) became "do something", which could mean any action.

My check: 'do something' for 'do one ordinary thing'

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (9.8, rated small)_

**F9.17** · lost · Appendix D: Anxiety — body first, P2 · a small snag

Now:

> It’s trying to help, making a guess about what’s coming: that you are in danger, or may be shamed, or abandoned, or fail, or be exposed, or be sick, or be rejected, or lose control, or whatever.

Published:

> Anxiety is often a Protector trying to prevent danger, shame, abandonment, failure, exposure, illness, rejection, loss of control, or a feeling it believes would be unbearable.

Reader: The published last item, "a feeling it believes would be unbearable", is gone and replaced by "or whatever".

My check: 'or whatever' for 'a feeling it believes would be unbearable'

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (9.20, rated small)_

**F9.18** · vaguer · Appendix D: Anxiety — body first, P2 · a small snag

Now:

> Therefore, instead of interrogating that part, start with yourself:

Published:

> Don’t begin by cross-examining it. Help the body first.

Reader: "Help the body first" became "start with yourself", and the "Therefore" ties it to the preceding sentences by a link that does not obviously follow.

My check: 'start with yourself' for 'help the body first'

_came in: 18 Oct (the overnight Emulate run)_

**F9.19** · unclear · Somatic Experiencing, P1 · a small snag

Now:

> In somatic experiencing (SE), you are not thrusting into the trauma.

Published:

> Don’t turn the exercise into trauma excavation.

Reader: "thrusting into the trauma" is an odd word choice a reader must decode as "forcing your way into it", where the published text said not to turn the exercise into trauma excavation.

My check: 'thrusting into the trauma' is an odd word

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (9.33, rated small)_

**F9.20** · lost · Body supports, P1 · a small snag

Now:

> There are many other somatic approaches you can try, like heat, pressure, a weighted blanket, darkness, your favorite calming music, a careful use of a massage gun, etc.

Published:

> Use the support that actually helps rather than assembling a tiny wellness trade show around the anxiety.

Reader: The published advice to use only what actually helps rather than piling on supports is dropped, and NOW instead invites trying many more.

My check: His line about using what actually helps, not 'a tiny wellness trade show', is gone

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (9.38, rated small)_

**F9.22** · vaguer · Anxiety script, P4 · a small snag

Now:

> I’m not going to abandon you but I’m not going to worship you, I will listen to what you have to say and reality test it and then take some action.

Published:

> I will not abandon the signal. I will not worship the signal. I will listen, test, and act.

Reader: The object changed from "the signal" to "you" (the guard or little one), so "worship you" is odd to say to a frightened part and the signal-versus-oracle point is less exact.

My check: 'I'm not going to worship you' said to a frightened part, where his line was about the signal

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (9.51, rated small)_

**F9.23** · lost · Appendix E: Is the daydream helping or replacing your life?, P5 · a small snag

Now:

> If it is taking you away from life then change your body position by sitting upright, open your eyes, feel your feet and ask your subconscious to help you.

Published:

> When it seems to be pulling you away, change the body before debating the story. Sit upright. Open the eyes a little. Feel the feet.

Reader: "before debating the story" is dropped, so the point that you change the body first rather than argue with the daydream is gone.

My check: 'before debating the story' is gone

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (9.59, rated small)_

**F9.24** · vaguer · Appendix E: Is the daydream helping or replacing your life?, P5 · a small snag

Now:

> If what you are showing me is helpful then please also show me the helpfulness in it.

Published:

> If this daydream is useful, please reveal the guidance inside it.

Reader: "the guidance inside it" became the circular "show me the helpfulness in it", which no longer matches the earlier question about what the guidance is.

My check: 'show me the helpfulness in it' is circular

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (9.60, rated small)_

**F9.26** · garbled · Appendix F: Self-trust, outside guidance, and oracle-like states, P2 · a small snag

Now:

> Being able to follow up immediately, to correct something in real time, to have a line of communication with guards, etc.

Published:

> Self-hypnosis gives you instant follow-up, real-time correction, and a private line to your own protectors.

Reader: A verbless fragment that never says whose advantages it lists, so the reader must infer it means the benefits of doing it yourself.

My check: A fragment listing the advantages of doing it yourself

_came in: 25 Oct (the answers of his first marking page)_

**F9.29** · unclear · Finding a hypnotist who can work with you, P3 · a small snag

Now:

> You might even be able to use this app or ask around to see if someone can tell you what the things the person did meant. They probably won't be able to tell you if the person was certified in them or not, though.

Published:

> Ask the app or another informed person for explanation, without expecting a practitioner to be certified from a brief account.

Reader: "what the things the person did meant" and "certified in them" are tangled phrasings with an unclear "They", so the reader has to work out that a helper can explain the methods but cannot confirm certification.

My check: 'what the things the person did meant' and 'certified in them' are tangled

_came in: 25 Oct (the answers of his first marking page)_

**F10a.1** · vaguer · When the subconscious speaks like an oracle, P2 · a small snag

Now:

> Especially if it's a big thing, or something that can't be easily undone, slow it down to the scale of the thing. Look at it with your adult's eyes, and take it to council.

Published:

> When the message has large or irreversible consequences, slow the action to the scale of those consequences, ask the adult questions, and bring the message to a council.

Reader: "it" and "the thing" are circular and never say that the action is to be slowed in proportion to the consequences, and the concrete step "ask the adult questions" has become the looser "look at it with your adult's eyes".

My check: 'slow it down to the scale of the thing' doesn't say to slow the action to the size of its consequences

_came in: 18 Oct (the overnight Emulate run)_

**F10a.4** · unclear · Forgiving yourself, P2 · a small snag

Now:

> Every so often, come back to how whoever did it got to be someone who could do that, until you understand it well enough that it changes how you feel.

Reader: In a section about forgiving yourself, "whoever did it" reads as another or unknown person and never says it means your past self.

My check: 'whoever did it' in a section about forgiving yourself

_came in: 25 Oct (the answers of his first marking page)_

**F10a.5** · garbled · Appendix G: Altered states, P1 · a small snag

Now:

> Borrowed is fine, as long as it’s from someone steady who won’t try to run your trip for you.

Reader: "Borrowed" is a fragment with its noun dropped (presumably Nurturer and Protector from a sitter), so the reader must guess what is being borrowed and, with "trip" in the sentence, could take it to be about borrowed substances.

My check: 'Borrowed is fine' comes after a parenthesis, so what is borrowed (Nurturer and Protector) is hard to see

_came in: 25 Oct (the answers of his first marking page)_

**F10a.6** · unclear · Appendix G: Altered states, P2 · a small snag

Now:

> Do not do it to try to FORCE yourself to get to a certain revelation about yourself, but rather to help yourself become more in tune with love and to better your life.

Published:

> Do not use altered states to force revelation. Use them to deepen listening, strengthen love, and improve ordinary life.

Reader: "it" has no clear referent after the sentences about sober inner child work and borrowing, whereas the published text names altered states as the thing not to use this way.

My check: 'Do not do it' doesn't say altered states

_came in: 25 Oct (the answers of his first marking page)_

**F10a.7** · vaguer · Appendix G: Altered states, P3 · a small snag

Now:

> A lot of people have OPENED themselves up to something at one point in their life. If you've had a similar experience, know that there is a difference between having experienced it at one point, or only being able to access it in a certain state, and being able to get to it at any point in your life.

Published:

> A past opening can be a resource without becoming a state you must reproduce. Having experienced love once, being able to access it only in a particular state, and contacting it reliably in daily life are different things.

Reader: "something" and the repeated "it" never say that what was opened to is love, so the paragraph's central contrast (once, only in a certain state, at any point in life) is about an unnamed thing.

My check: 'opened themselves up to something' never says love until the end of the paragraph

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (9.84, rated small)_

**F10a.9** · unclear · Appendix G: Altered states, P3 · a small snag

Now:

> (If you can't give it to the child, try to deal with why you can't, instead of trying to ramp up the experience.

Published:

> If the child cannot receive it, meet the difficulty rather than escalating the intensity.

Reader: "give it to the child" does not say what "it" is (love, in the published text), so the reader has to guess whether it means the experience or something else.

My check: 'give it to the child' doesn't say love

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (9.86, rated small)_

**F10b.2** · lost · A response check, not a verdict about what it is, P4 · a small snag

Now:

> You don’t have to find out if it’s a guard immediately, and you may not be able to comfort it quickly.

Published:

> Neither response establishes its origin. A protective part needn’t reveal its fear quickly; a comforting response doesn’t prove an interpretation either.

Reader: PUBLISHED's point that neither response (comforting it or keeping distance) proves what the presence is has become a different point about not rushing, and "a guard" appears with no introduction where PUBLISHED said "a protective part".

My check: The point that neither response proves what it is now lives only in the heading

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (10a.26, rated small)_

**F10b.3** · vaguer · Do not fight from fear, P1 · a small snag

Now:

> Your first instinct may be to fight it, banish it, hate it, show it that you’re more powerful than it is, argue with it, panic, become your own lesser self in fear of it, etc.

Published:

> The first impulse may be to fight, banish, hate, prove power, argue, panic, or identify completely with the threatened self.

Reader: "become your own lesser self in fear of it" leaves the reader guessing what "lesser self" means and no longer says PUBLISHED's "identify completely with the threatened self" (collapsing into the frightened part).

My check: 'become your own lesser self in fear of it' is vague

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (10a.29, rated small)_

**F11.1** · vaguer · Appendix J: A practical induction library, P1 · a small snag

Now:

> Practise! Work out in advance which one you want to do and what you want to use it for (pick just one) and whether or not you want to do it at all!

Published:

> Preview the sequence, choose one purpose, and decide whether you want to begin.

Reader: The step of previewing the sequence has become a bare "Practise!", and "which one" and "(pick just one)" no longer say clearly that you choose one induction and one purpose.

My check: 'Practise!' (Emulate's British spelling) stands for 'preview the sequence'

_came in: 18 Oct (the overnight Emulate run)_

**F11.2** · unclear · Appendix J: A practical induction library, P1 · a small snag

Now:

> Any of these families of induction can be done as light inductions, with eyes open, or instead of trance you can just do them as a contact.

Published:

> Each family can be light, eyes-open, or replaced by no-trance contact.

Reader: "Do them as a contact" no longer says what the contact is (the no-trance inner contact of exercise 9), so a reader has to guess.

My check: 'do them as a contact' doesn't point to the no-trance inner contact (9)

_came in: 18 Oct (the overnight Emulate run)_

**F11.3** · garbled · Appendix J: A practical induction library, P2 · a small snag

Now:

> Once you start an induction, you will want to notice what’s going on (even if nothing changes) and work out what to do next, move, imagine something else, change the sensory channel you’re using, do nothing, stop the induction sequence and do something else…

Published:

> Notice the actual response—including no change—and let it determine the next move. Move, imagine, change the sensory channel, remain still, or stop.

Reader: The options are strung on after "work out what to do next" with commas and no "or", so they read as a run of actions to do in order (including "do nothing" and "stop"), and the point that the noticed response decides the next move is lost.

My check: The options after 'work out what to do next' read as steps in a row; a colon would fix it

_came in: 18 Oct (the overnight Emulate run)_

**F11.4** · vaguer · 1. Stretch and release, P1 · a small snag

Now:

> Think of it as releasing as you go through the sequence.

Published:

> Repeat with no more than three areas, letting “release” guide the sequence.

Reader: "It" has no clear referent and "releasing as you go" no longer says that release is what guides the sequence.

My check: 'think of it as releasing' doesn't say that release guides the sequence

_came in: 18 Oct (the overnight Emulate run)_

**F11.5** · unclear · 1. Stretch and release, P1 · a small snag

Now:

> Which bit of your body, or voice, needs this? What do you need to support it?

Published:

> Which area or inner voice wants attention? What support is needed?

Reader: "Needs this" has no clear referent (the published asks what wants attention) and "voice" has lost "inner", so it can read as your speaking voice.

My check: 'or voice' can read as your speaking voice

_came in: 18 Oct (the overnight Emulate run)_

**F11.6** · unclear · 2. Supported floating, P1 · a small snag

Now:

> Tell yourself you are going to do this before you do it.

Published:

> You may deliberately alternate attention toward ordinary awareness on the inhale and support on the exhale; name this fractionation beforehand.

Reader: "This" could mean the whole exercise or the breath-alternating fractionation just described, where the published names the fractionation.

My check: 'do this' could be the whole exercise or the fractionation

_came in: 18 Oct (the overnight Emulate run)_

**F11.7** · lost · 2. Supported floating, P1 · a small snag

Now:

> Bring yourself back to normal feeling of support and return.

Published:

> Keep the support, regain chosen weight and firm contact, then return.

Reader: The closing step of keeping the support is gone, so the exercise ends with only a plain return to normal.

My check: 'keep the support' is gone from the close

_came in: 18 Oct (the overnight Emulate run)_

**F11.10** · garbled · 5. Sensory journey, P1 · a small snag

Now:

> When you feel you have enough of your attention, imagine the scenery changing until you are in a place where you can talk to whoever you need to (or you can just cut to the chase, if you prefer).

Published:

> Use footsteps, textures, or landmarks to gather attention. Change scenery or skip directly to dialogue when useful.

Reader: "Have enough of your attention" does not parse (the published gathers attention with footsteps, textures or landmarks), so the cue for when to change the scenery is unclear.

My check: 'when you feel you have enough of your attention' is odd

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (10b.29, rated small)_

**F11.11** · vaguer · 6. Gradual wave, P1 · a small snag

Now:

> Gradual wave: start with a very small neutral area, feel into it a little and then imagine a wave spreading out to a new area that is still ok.

Published:

> Start with a small neutral area and what is already there. Imagine warmth, steadiness, or attention spreading to the next comfortable area, or keep it localized.

Reader: "A wave" never says what spreads (the published names warmth, steadiness, or attention), so the reader does not know what to imagine moving.

My check: 'a wave' doesn't say what spreads (warmth, steadiness or attention)

_came in: 18 Oct (the overnight Emulate run)_

**F11.15** · unclear · 8. Resource embodiment, P1 · a small snag

Now:

> Come back, keeping the quality and one positive action that you would do with it, but leaving the imagined "person" behind, saying "I am me".

Published:

> Keep the quality and one useful action, release the role, affirm “I am myself,” and return.

Reader: No "person" has been introduced earlier, so the reader must guess that it means the imagined self carrying the quality (the published calls it the role).

My check: The imagined 'person' was never introduced

_came in: 25 Oct (the answers of his first marking page)_

**F11.17** · lost · 9. No-trance inner contact, P1 · a small snag

Now:

> Deepener: none.

Published:

> Deepener: None. Full alertness is not an inferior version of the practice.

Reader: The statement that full alertness is a legitimate version of the practice and not a lesser one is dropped.

My check: 'full alertness is not an inferior version of the practice' is gone

_came in: as he published it; flagged on 25 Oct (10b.33, rated small)_

**F11.19** · unclear · Appendix K: Sources and further reading, P1 · a small snag

Now:

> The personal accounts and the way I arrange this practice are my own, especially if it involves adaptations like the one I'm doing here where I am combining body-oriented work and hypnotic work.

Published:

> The personal accounts and the way I arrange this practice are mine. The revised teaching brings them together with body-oriented and hypnotic approaches described below.

Reader: "Especially if it involves" has no clear "it" and makes the adaptation sound conditional, where the published states plainly that combining body-oriented and hypnotic approaches is the adaptation.

My check: 'especially if it involves adaptations' is awkward

_came in: 25 Oct (the answers of his first marking page)_

**F11.20** · lost · Appendix K: Sources and further reading, P1 · a small snag

Now:

> This is not a validated form of treatment at this time.

Published:

> That combination is an adaptation, not a treatment validated as a whole. These notes are for readers who want to follow an idea further; you don’t need them open while practicing.

Reader: "This" does not say what is not validated (the published says the combination, as a whole), and the note saying what the appendix is for and that it need not be open while practicing is dropped.

My check: 'this is not a validated form of treatment' doesn't say what 'this' is (the note after it he cut on 25 Oct, CV-8.5)

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (10b.35, rated small)_

**F11.23** · unclear · Inner-child care and adult capacities, P1 · a small snag

Now:

> For information about all of these things, see Inner Child Self-Love Reparenting Guide.

Published:

> The companion Inner Child Self-Love Reparenting Guide gives the fuller treatment of borrowed adulthood, love without compulsory trust, practical and relational repair, spiritual struggle, differentiation, and mutual peer support.

Reader: "All of these things" points at nothing, and the topics the companion guide covers are no longer listed.

My check: 'all of these things' leans on the heading

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (10b.39, rated small)_

**F11.25** · lost · Inner speech and putting experience into words, P1 · a small snag

Now:

> The questions in the quick start are a practical way of seeing for yourself how you are.

Published:

> The questions in Quick start are a practical self-check, not a validated screening instrument or a test of hypnotic ability.

Reader: "How you are" does not say what is being checked, and the statement that the questions are not a validated screening instrument or a hypnotic-ability test is dropped.

My check: 'how you are' is vague (the 'not a validated test' part he cut on 25 Oct, CV-8.9)

_came in: 25 Oct (the answers of his first marking page)_


## Not problems (116)

**F1.4** · vaguer · Introduction, P8 · not a problem

Now:

> I work with the subconscious as if it were an ecology, and often begin hypnosis working with the Higher Self (universal heart) and only separate into parts when needed.

Published:

> I treat the subconscious as a living ecology of parts, memories, impulses, images, protections, and wisdom. I bring in inner-child reparenting because a wounded young part won’t be repaired by a clever suggestion. I begin with Higher Self or the universal heart when the system needs coherence, and separate into parts only when that helps.

Reader: "An ecology" is no longer said to be of parts, memories, impulses, images, protections and wisdom, and beginning with the Higher Self is no longer tied to "when the system needs coherence".

My check: As clear, less detailed

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (1.25, rated small)_

**F1.17** · unclear · Why doing it myself worked better for me, P8 · not a problem

Now:

> Normal interaction with people made it wear off, but for a while it showed me that my mind and heart may allow this when the desire is sincere.

Published:

> Ordinary interaction dissolved the state, but for a while it showed me a possibility my mind and heart may permit when the desire is sincere.

Reader: "This" replaces the named "possibility", so the reader must guess it means the "perfected" love state.

My check: 'this' is the state just described

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers)_

**F2a.1** · vaguer · A useful map of the mind, P2 · not a problem

Now:

> Working with parts: Precision. Working with Higher Self: Coherence. Doing both: Communion.

Published:

> Parts give precision. Higher Self gives coherence. Communion is the movement between them.

Reader: The verbless labels never say that parts give precision or that Higher Self gives coherence, and "Doing both" replaces communion as "the movement between them".

My check: Labels, but clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (1.70, rated small)_

**F2a.3** · vaguer · A useful map of the mind, P6 · not a problem

Now:

> It’s usually a good idea to start with unity.

Published:

> Begin with unity when the system feels scattered:

Reader: The trigger "when the system feels scattered" becomes "usually a good idea", so a reader no longer knows when to start with unity, and it sits oddly with the later heading "Sometimes start with the whole".

My check: As clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (1.77, rated small)_

**F2a.4** · vaguer · Sometimes start with the whole, P1 · not a problem

Now:

> So it’s better to start from the Sacred.

Published:

> Start with the sacred whole when that happens.

Reader: "When that happens" is dropped, so this reads as a blanket rule under a heading that says "Sometimes", and "the Sacred" is not tied to "the whole" until the next paragraph.

My check: As clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (1.81, rated small)_

**F2a.5** · vaguer · Sometimes start with the whole, P4 · not a problem

Now:

> So even though it can be useful to talk about your Higher Self, it doesn’t mean you already have all the good inner parenting functions etc that you need.

Published:

> Higher Self language can help you gather around a meaningful source of care; it doesn’t establish that a perfectly capable inner parent is already available.

Reader: "It can be useful to talk about your Higher Self" no longer says what it is useful for (gathering around a source of care), which is what the contrast with "doesn’t mean you already have" depends on.

My check: As clear

_came in: 18 Oct (the overnight Emulate run)_

**F2a.6** · garbled · When the adult role is not available yet, P4 · not a problem

Now:

> If you have a safe adult in your life you can borrow from them, if not borrow from a mentor, older brother/sister, imagine your future self, your god/goddess or higher power, a value you have, a plan you have written, etc.

Published:

> Choose a safe adult, mentor, older sibling, future self, spiritual figure, value, or written plan.

Reader: The run-on switches from "borrow from" to "imagine" to bare noun phrases with nothing marking the options, so a reader has to reread to see they are all things to borrow from.

My check: A casual run-on, but it reads

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (2.13, rated small)_

**F2a.9** · vaguer · When the adult role is not available yet, P8 · not a problem

Now:

> Once you’ve found something good, try it, don’t keep doing the exercise.

Published:

> Once you find one usable sentence or action, try it rather than repeating the exercise in different words.

Reader: "Something good" and "don’t keep doing the exercise" lose the concrete trigger (one usable sentence or action) and the point of not re-wording the exercise, and could be read as "stop the practice".

My check: As clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (2.21, rated small)_

**F2a.11** · vaguer · Let the child speak without handing over the steering wheel, P3 · not a problem

Now:

> This way you get the benefits of being young: curiosity, spontaneity, play, sensation, the ability to state your needs, to feel easily etc without any of the negatives of being a child, like obeying, being helpless, being scolded, the lack of good judgement etc.

Published:

> That distinction lets you recover curiosity, spontaneity, play, sensory freshness, honest need, and quick emotional movement without pairing those gifts with obedience, helplessness, scolding, or weakened judgment.

Reader: "To feel easily" is a vague stand-in for "quick emotional movement" (feel what, easily?), and the list runs straight from "etc" into "without any of the negatives".

My check: As clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (2.28, rated small)_

**F2b.1** · lost · Love doesn’t have to wait for trust, P1 · not a problem

Now:

> It is possible for trust to question your promises, remember when you failed to protect them, and take its time.

Published:

> Trust can question your promises, remember failures of protection, and take its time. Love can remain present while that happens.

Reader: The contrast that love can stay present while trust questions and takes its time is no longer stated, so this reads as a bare possibility.

My check: His inner child guide's words, lined up on 25 Oct

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (2.30, rated small)_

**F2b.2** · unclear · Love doesn’t have to wait for trust, P3 · not a problem

Now:

> You don't have to accept every conclusion they reach about you, but do listen for the concrete complaint without fighting the yelling and swearing around it, because even if they are coming from a place that is not completely "right," there will likely be something true in what they are saying.

Published:

> Listen for what is true in it and answer seriously.

Reader: "They" shifts between the little one and the complaints, and "coming from a place that is not completely 'right'" never says what it means, so the reader has to guess.

My check: His inner child guide's words, lined up on 25 Oct

_came in: 25 Oct (the answers of his first marking page)_

**F2b.3** · vaguer · Love doesn’t have to wait for trust, P3 · not a problem

Now:

> Finding other ways to show your love for them (this might include taking care of them, such as by buying and cooking food for them, setting limits for them, taking them to the doctor when they need it, and doing what you said you would do).

Published:

> Hearing anger without retaliation, admitting a real failure, and repairing after an internal attack are evidence alongside meals, boundaries, appointments, and kept promises.

Reader: "Boundaries" became "setting limits for them", which reads as restricting the child rather than protecting them.

My check: His inner child guide's words, lined up on 25 Oct

_came in: 25 Oct (the answers of his first marking page)_

**F2b.4** · unclear · Love doesn’t have to wait for trust, P3 · not a problem

Now:

> Just not hitting back is enough to start being the adult, even if it isn't enough yet for them to trust you. That takes warmth, and if there isn't any yet, borrow some.

Published:

> Non-retaliation expresses love; it shouldn’t replace love with a colder performance of good behavior.

Reader: "That" has no clear referent and "borrow some" does not say how to borrow warmth, while the published point that non-retaliation must not stand in for love is no longer stated.

My check: His inner child guide's words; borrowing warmth is explained in its own section

_came in: 25 Oct (the answers of his first marking page)_

**F2b.5** · unclear · Instead of blame, P1 · not a problem

Now:

> Their age might not be your chronological age.

Published:

> Don’t decide from the person’s chronological age.

Reader: "Their" has no clear referent, and the published instruction not to decide from chronological age whether the voices are separate, the same, or a blend is gone.

My check: 'their' is the positions just named

_came in: 25 Oct (the answers of his first marking page)_

**F2b.7** · unclear · The two-hand practice, P2 · not a problem

Now:

> If some comes back up, let it, and send it on down again, so it goes around like a loop. That part's a gift from them, and they don't owe it to you, so if nothing comes back, just keep sending yours.

Published:

> Notice whatever comes back—a sensation, image, feeling, resistance, or nothing—and answer with warmth again.

Reader: "some" has no noun and "That part" has no clear referent, so the reader must work out that both mean the love coming back from the child.

My check: His inner child guide's words, lined up on 25 Oct

_came in: 25 Oct (the answers of his first marking page)_

**F2b.8** · lost · The two-hand practice, P2 · not a problem

Now:

> This is a conversation with your child from your heart.

Published:

> Love above. Child below. Adult present.

Reader: The closing frame of love above, child below, adult present is dropped, so NOW no longer says the adult stays present alongside the two hands.

My check: A tagline he wouldn't want back

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (2.39, rated small)_

**F2b.10** · vaguer · The Protector, P1 · not a problem

Now:

> As the Protector, work with setting boundaries together.

Published:

> The Protector turns warmth into something the child can believe.

Reader: It no longer says what the Protector is for (making warmth something the child can believe), and "together" does not say with whom.

My check: As clear

_came in: 18 Oct (the overnight Emulate run)_

**F2b.11** · vaguer · The Protector, P1 · not a problem

Now:

> It can be trust-related boundaries like, "I'm going to keep the promise to myself" or "I'm not going to leave you to do adult things by yourself."

Published:

> “I will keep a small promise.” “I will not leave the child alone with adult consequences.”

Reader: "The promise to myself" drops "small" and "adult things" replaces "adult consequences", which changes what the child is being left alone with.

My check: As clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (2.43, rated small)_

**F2b.14** · lost · The Protector, P3 · not a problem

Now:

> Don't make it so that doing it successfully means you have to feel good about it, or be able to check it off a list.

Published:

> Completion without immediate relief isn’t automatically failure, and a tick on a list doesn’t prove the action helped.

Reader: The two separate points (finishing without relief is not failure; a ticked list does not prove the action helped) became one convoluted rule about what success must mean, and the second point is changed.

My check: As clear

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (2.47, rated small)_

**F3a.1** · lost · The Guide, P4 · not a problem

Now:

> Even if you start with protection and can’t do the warmth stuff yet, make sure the direction you’re being led in is appropriate for your inner child’s growth (i.e. not depriving them of things they need, like play or support, etc.)

Published:

> If warmth is unavailable, a protective act can begin the relationship. Make it small enough to carry out and review what actually happened. A missed action might reflect fear, exhaustion, missing skills, a practical barrier, or a poor plan. Completion without immediate relief isn’t automatically failure, and a tick on a list doesn’t prove the action helped.

Reader: PUBLISHED says a small protective act can start the relationship when warmth is missing and then gets reviewed, but NOW turns that condition into a warning about the Guide's direction, and "Even if" has no clear contrast.

My check: Clear in its own section (the reader matched a published passage from another one)

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (2.51, rated small)_

**F3a.2** · unclear · Working with your guards, P1 · not a problem

Now:

> Often, we see a sensation or a distraction or an objection as something that needs to be explored, when in fact it might just be hunger, or reasonable skepticism about something, or a sentence that doesn’t fit.

Reader: "A sentence that doesn't fit" doesn't say which sentence or what it fails to fit, so the third example is hard to picture.

My check: As clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (2.54, rated small)_

**F3a.6** · lost · Working with your guards, P7 · not a problem

Now:

> Most of the time the guard wants you to do certain things, set boundaries, do whatever you are supposed to do, eat, not text someone, keep a promise, go to sleep, talk to the therapist, admit that you owe someone money, write something down, etc.

Published:

> This is where inner-child practice often turns decorative. The voice says loving things while the adult sends the destabilizing message, skips the meal, avoids the task, and breaks the promise. Trust begins when you handle the consequence.

Reader: The same list of protective acts now only says what a guard wants, so PUBLISHED's point that loving words stay decorative until the adult acts, and that trust begins there, is gone.

My check: Clear in its own words

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (2.62, rated small)_

**F3a.7** · lost · Protection that knows when to stop scanning, P1 · not a problem

Now:

> Do you want to embody your Protector? Then you could practice this:

Published:

> The Protector is more than an inner voice saying no. You can practice it as a bodily sequence:

Reader: NOW drops PUBLISHED's contrast that the Protector is more than an inner voice saying no.

My check: As clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (2.69, rated small)_

**F3a.8** · vaguer · Protection that knows when to stop scanning, P4 · not a problem

Now:

> set boundaries (start with one and make it relative to the danger; move, stop, delay, ask, leave, get support, etc.)

Published:

> Set one proportionate boundary: move, stop, delay, ask, leave, or get support.

Reader: "Relative to the danger" doesn't say the boundary should be proportionate, meaning matched in size to the danger.

My check: As clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (2.72, rated small)_

**F3a.9** · vaguer · Protection that knows when to stop scanning, P5 · not a problem

Now:

> verify if it is safe enough

Published:

> Verify enough safety: not perfect certainty, just enough reality-based evidence for the next step.

Reader: NOW drops "not perfect certainty, just enough reality-based evidence for the next step", so "safe enough" no longer says what counts as enough.

My check: A terse list item, but it reads

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (2.73, rated small)_

**F3a.12** · vaguer · Don’t rush the repair, P8 · not a problem

Now:

> Give them what you can- don't feel like you have to fix it all.

Published:

> Respond to one need: do the smallest useful thing rather than attempting a total repair.

Reader: "What you can" replaces the concrete instruction to answer one need with the smallest useful thing, so the step no longer says how small to go.

My check: As clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (2.88, rated small)_

**F3a.14** · lost · Don’t rush the repair, P11 · not a problem

Now:

> Rest, and reconnect with them later to see what was helpful.

Published:

> Rest: stop before care becomes another performance.

Reader: NOW drops the reason for resting (stop before care becomes another performance), so "Rest" no longer says what to stop or why.

My check: As clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (3.5, rated small)_

**F3a.15** · lost · Don’t rush the repair, P12 · not a problem

Now:

> Remember the goal isn't to make yourself good as new but to make yourself good as you- more supported and connected to yourself.

Published:

> The goal isn’t “good as new,” as though history should disappear. Aim for good as you: more supported and connected while still recognizably yourself.

Reader: NOW drops why "good as new" is the wrong goal (history shouldn't disappear) and "still recognizably yourself", so "good as you" has little to contrast with.

My check: As clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (3.6, rated small)_

**F3a.16** · unclear · Don’t rush the repair, P12 · not a problem

Now:

> If you don't like the idea of part work or it makes you feel more divided, you can substitute whatever part you're working with for a signal or a feeling, or an imaginary younger you that you feel embodies the issue you're having.

Published:

> If parts language makes you feel more divided, use signals, feelings, younger states, or another metaphor that helps.

Reader: "Substitute the part for a signal" literally says the opposite direction (using the part instead of a signal), so the reader has to flip it.

My check: A common way to say it

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (3.8, rated small)_

**F3b.3** · unclear · Non-dominant hand dialogue, P1 · not a problem

Now:

> Tell your child/ guard to write with your nondominant hand, and talk to them with your dominant.

Published:

> Let the non-dominant hand speak for the child or protector, awkward handwriting and all. Answer with the dominant hand as the adult.

Reader: "guard" replaces PUBLISHED's "protector" with no explanation, so a reader may not know it means a protective inner part.

My check: His term (guard)

_came in: 25 Oct (the answers of his first marking page)_

**F3b.4** · vaguer · Non-dominant hand dialogue, P1 · not a problem

Now:

> So for example, they might say "I don't trust you" with your nondominant hand, and you can say with your dominant hand "I know you don't trust me right now but I love you and I want to know how I've fucked up. I don't expect you to trust me but I want to hear you out and give you a promise I can keep today" and they can say "what promise?" and you can say "I'm going to make sure I eat today/ clear off my desk/ not text so-and-so".

Published:

> Dominant hand: “I will eat, clean the desk, and not text the person who makes us feel unsafe.”

Reader: "so-and-so" replaces "the person who makes us feel unsafe", so the reader is no longer told that the promise is about keeping away from someone who makes them feel unsafe.

My check: As clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (3.19, rated small)_

**F3b.6** · unclear · When “your voice” is everybody else’s voice, P2 · not a problem

Now:

> You are in the first camp if:

Published:

> This may apply when:

Reader: "The first camp" is never introduced as a label and the paragraph above ends on the "others" who find it easy, so the reader has to work out which group is meant.

My check: His approved fix of 25 Oct (RR-3.9)

_came in: 25 Oct (the answers of his first marking page)_

**F3b.8** · lost · When “your voice” is everybody else’s voice, P11 · not a problem

Now:

> Some people come back later on different terms, and sometimes the break has to be long-term because the pattern of losing yourself with them is deeply entrenched.

Published:

> Sometimes a temporary, intentional period of distance from the people or group supplying the answers helps quieter preferences surface. Use that distance only long enough to tell your own signal from the social echo; prolonged isolation would undermine the purpose.

Reader: PUBLISHED limits the distance to "only long enough to tell your own signal from the social echo" and warns that prolonged isolation would undermine the purpose, but NOW says the break sometimes has to be long-term, so it now says something else and clashes with its own "Temporary Separation" label.

My check: His inner child guide's newer stance, brought in by his approved card IC-A21 (25 Oct)

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (3.36, rated matters)_

**F3b.10** · garbled · When “your voice” is everybody else’s voice, P21 · not a problem

Now:

> Because often your inherited parent script tells your inner child that it is supposed to be good at something as soon as it starts doing it, which is humiliating.

Published:

> The inherited parent may demand immediate talent.

Reader: A "Because" clause stands as its own sentence after an examples list, so the reader has to reattach it to the opening sentence to see what it explains.

My check: His own sentence (his edit of 21 Oct)

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (3.42, rated small)_

**F4a.1** · unclear · De-hypnosis: wake up inside the influence, P1 · not a problem

Now:

> But there are also the older, more mundane influences: erotic imprinting (as if breast implants are actually sexy), religious fear, which tags along with shame, charismatic authority and pressure to belong.

Published:

> Screens, advertising, politics, religious fear, erotic imprinting, charismatic authority, belonging pressure, shame, urgency, and repetition all do it.

Reader: A reader can't tell whether "charismatic authority and pressure to belong" are further items in the list or things religious fear "tags along with", so the list has to be reparsed.

My check: His own paragraph (23 Oct)

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (3.53, rated small)_

**F4a.6** · vaguer · Induction: gathering attention without disappearing, P1 · not a problem

Now:

> If on the other hand, you're already pretty trancey for whatever reason, skip straight to "Already open? Contain before you deepen" rather than going deeper.

Published:

> When meditation, loveyhuasca, lucid dreaming, grief, music, prayer, fatigue, or another intense opening has already made you trancey, begin with orientation and containment instead of adding depth.

Reader: The concrete step (begin with orientation and containment) and the examples of what opens you are replaced by a pointer to a section title that does not appear in this part, so the reader can't tell here what to do.

My check: The section it points to is in the guide

_came in: 25 Oct (the answers of his first marking page)_

**F4b.1** · vaguer · Please don’t put six metaphors in one trance, P1 · not a problem

Now:

> One thing you're doing, one anchor/image you're going with at first, one way of coming back, and feel free to set a tone (warm, bounded, directed, neutral witnessing, whatever) for yourself.

Published:

> Choose one purpose, one starting anchor or image, and a way back. Decide whether warmth, a firm boundary, direction, or neutral witnessing would help.

Reader: "One thing you're doing" no longer says it is the purpose of the session, the verbless list runs on into "feel free to set a tone", and the choice of tone becomes an optional extra.

My check: Casual, under 'Keep it simple'

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers)_

**F4b.2** · lost · Please don’t put six metaphors in one trance, P1 · not a problem

Now:

> If you're going to use metaphors just do one, and if you switch metaphors, do it in a way that's conscious.

Published:

> Floating, stairs, gardens, inner rooms, colored light, and child dialogue do not all need to report for duty at once. Switch consciously when the metaphor stops helping.

Reader: The example metaphors that the heading's "six" points to and the cue to switch "when the metaphor stops helping" are gone, and "just do one" sits against "if you switch" without saying one at a time.

My check: As clear

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (4.11, rated small)_

**F4b.6** · vaguer · Before you begin, P2 · not a problem

Now:

> Get clear on what it is you want to do during the induction. What do you want not to do today?

Published:

> Choose the question or quality you want to explore, what you’re leaving alone today, and how much time you have.

Reader: "What you want to do" no longer names a question or quality to explore, and "what do you want not to do today" reads as things to avoid rather than topics to leave alone.

My check: As clear

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (4.18, rated small)_

**F4b.12** · lost · Before you begin, P6 · not a problem

Now:

> For more on language you can use, see Appendix B, or keep reading below for information on using the tools after induction in Let the next response guide you. Either way, keep the instructions about how to stay safe and how to get out plain.

Published:

> Keep safety and exit instructions plain. Appendix B teaches the richer language tools, and Let the next response guide you shows how to use them after the induction.

Reader: "Appendix B teaches the tools, and the later section shows how to use them" becomes alternatives ("or ... Either way"), and "the tools" loses its antecedent.

My check: As clear

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (4.31, rated small)_

**F4b.15** · lost · Sober induction: 3–5 minutes, P3 · not a problem

Now:

> You can allow your eyes to rest on something in the room for a bit, and let what's already there come into view.

Published:

> Let your eyes settle somewhere in the room, somewhere they can rest for a little while, and notice the difference between looking for something and letting what is already there come into view.

Reader: The contrast between looking for something and letting what is already there come into view is dropped, so "what's already there" has nothing to be set against.

My check: As clear

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers)_

**F4b.16** · lost · Sober induction: 3–5 minutes, P4 · not a problem

Now:

> Or maybe there is a sound, or something else to notice.

Published:

> And while you notice that, a sound may reach you, or a breath may draw your attention, without needing you to arrange either one.

Reader: A sound or breath that arrives on its own while you notice the contact, with nothing for you to arrange, becomes just another thing you might choose to notice.

My check: As clear

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (4.36, rated small)_

**F4b.18** · garbled · Sober induction: 3–5 minutes, P12 · not a problem

Now:

> Let your attention come back to your chosen anchor. 4. Let more of your attention come to what you've found. 3. Leave a little space. 2. See if you can listen to a space after the words without preparing an answer. 1. Take your time.

Published:

> Five. Notice your chosen anchor again. Four. Let attention gather around what you find. Three. Leave a little space after the words. Two. Listen into that space, without preparing an answer. One. Stay here for a moment.

Reader: The first step has no number, so the count looks as if it starts at 4 instead of 5.

My check: The guide has '5.' at the start of that line as a list number (the page and the Substack draft show it, <ol start="5">); the reader's plain text dropped it

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers)_

**F4b.19** · lost · Already open? Contain before you deepen, P2 · not a problem

Now:

> Know that you're already open, you just need to aim and stabilize it, and keep it kind.

Published:

> “The state is already open. I do not need to intensify it. I need to aim it, stabilize it, and keep it kind.”

Reader: The explicit "I do not need to intensify it" is gone, so the rule against deepening an already open state is only implied by "just".

My check: As clear

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (4.48, rated small)_

**F5.1** · garbled · Stay awake when your mind likes to escape, P2 · not a problem

Now:

> Ask yourself why you're daydreaming. Is it to get guidance, or because you're working through something, or are you avoiding something?

Published:

> “Is this daydream guidance, emotional digestion, or avoidance?”

Reader: The question changes grammar twice ("Is it to get guidance, or because ..., or are you ...") so the three options don't line up as one question.

My check: As clear: a casual spoken question with three options

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (4.52, rated small)_

**F5.9** · lost · A shortcut back into hypnosis, P6 · not a problem

Now:

> Don't use this to go into hypnosis faster for things that you shouldn't be working on yet.

Published:

> Faster entry doesn’t determine what material you can handle.

Reader: The point that quick entry is no sign you can handle heavier material became a prohibition that assumes the reader already knows what they shouldn't work on yet.

My check: As clear: says not to use quick entry for material you're not ready for

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers)_

**F5.12** · vaguer · The actual inner meeting, P3 · not a problem

Now:

> I invoke my Higher Self, universal heart-mind, wise subconscious mind, intelligence in my body, inner child(ren), inner adult(s), guard(s) and all that is of truth and love to help me know what I need to know, only in a form and at a time that will be useful, kind, stabilizing and real for me.

Published:

> Higher Self, universal heart-mind, wise subconscious, body intelligence, inner child, inner adults, protective parts, and all that serves truth and love: please help me understand what I need to know, only in the form and timing that is useful, kind, stabilizing, and real.

Reader: "guard(s)" (and "child or guard" later) replaces "protective parts" and is never introduced, while NOW elsewhere calls the same kind of figure the "Protector".

My check: His term: a protective part from childhood is a guard (gate E274)

_came in: 25 Oct (the answers of his first marking page)_

**F6a.1** · lost · Let the response change the invitation, P1 · not a problem

Now:

> Your shoulders tightening, or 'hmm, that feels kind of wrong', is a signal to investigate further, but 'No! That is Not Right!' is a signal to stop what you're doing and change it.

Published:

> “My shoulders tightened” and “that wording feels wrong” are different observations. Tightening alone doesn’t explain itself. Ask what happened and whether the invitation fits. An explicit no needs no further justification; change the words, the pace, or the approach.

Reader: PUBLISHED contrasts a body sensation with a judgment about the wording, while NOW lumps the sensation and "feels kind of wrong" together as one weak signal against a strong "No!", so the contrast the passage was built on is gone.

My check: Clear guidance in its own words

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (5.36, rated small)_

**F6a.2** · vaguer · Let the response change the invitation, P1 · not a problem

Now:

> If you don't feel like it fits, don't keep doing it. Just change it. You don't need any other reason.

Published:

> An explicit no needs no further justification; change the words, the pace, or the approach. Don’t repeat an unwelcome suggestion more persuasively.

Reader: "it" is never named as the invitation or wording, and the concrete options (change the words, the pace, the approach) and the warning against repeating the suggestion more persuasively shrink to "just change it".

My check: 'it' is what you're doing

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (5.37, rated small)_

**F6a.5** · lost · Look at the situation too, P1 · not a problem

Now:

> If there is another person involved in the situation, it may be a good idea to look at what they are doing as well.

Published:

> When another person is involved, notice what they actually do before making the whole problem an inner-child reaction.

Reader: The caution to look at the other person's behavior before treating the whole problem as your inner-child reaction is gone, so "as well" no longer says as well as what.

My check: As clear

_came in: 18 Oct (the overnight Emulate run)_

**F6a.10** · vaguer · Look at the situation too, P2 · not a problem

Now:

> What do you want to do or achieve the next time you interact with this person?

Published:

> Choose a realistic purpose for the next interaction. Sometimes it is mutual understanding; sometimes it is conveying information, saying no, or ending the exchange.

Reader: The instruction to choose a realistic purpose became an open question about what you want, so "realistic" is gone.

My check: As clear

_came in: 18 Oct (the overnight Emulate run)_

**F6a.9** · lost · Look at the situation too, P2 · not a problem

Now:

> On the other hand, did you give in to someone else just to keep them from being disappointed in you?

Published:

> Did you cause harm that needs repair, abandon your position to make their disappointment go away, or both?

Reader: "On the other hand" makes the two possibilities exclusive alternatives, dropping PUBLISHED's "or both".

My check: As clear

_came in: 18 Oct (the overnight Emulate run)_

**F6a.15** · vaguer · If you feel an urge to move, P1 · not a problem

Now:

> If you feel an urge to move, turn, reach, push, or change your body’s position, feel free to either actually do something that will not cause your body pain or discomfort, or just imagine doing what you feel you need to do, and see what happens next.

Published:

> An impulse to turn, reach, push away, or change posture can also be explored through a small, voluntary, physically comfortable movement—or imagined without moving. Notice what follows.

Reader: "a small, voluntary, physically comfortable movement" became "do something that will not cause pain", so "small" and "voluntary" are gone and "do something" is nonspecific.

My check: As clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (5.47, rated small)_

**F6a.17** · vaguer · Offer the care that is actually wanted, P2 · not a problem

Now:

> If you feel that it would be useful to bring in your Nurturer, Protector or Guide to help you either change the tone of the interaction, set boundaries, or find your way toward the life you want, feel free to do so.

Published:

> The Nurturer can change the tone; the Protector can carry out a boundary; the Leader can point toward the life you want.

Reader: The roles and their jobs are no longer paired (a list of three roles and a list of three jobs), and the third role is called "Guide" where PUBLISHED calls it "Leader".

My check: His term (the Guide); clear

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (5.51, rated small)_

**F6a.18** · unclear · Offer the care that is actually wanted, P2 · not a problem

Now:

> You don’t have to talk to them, just use the one whose job you need, and if you can’t do it yet, borrow it.

Published:

> They don’t each need a speech. When a capacity isn’t available, borrow that one function.

Reader: "borrow it" does not say what is borrowed or from whom (PUBLISHED: borrow that one function when the capacity isn't available), and "You don't have to talk to them" replaces "they don't each need a speech".

My check: Borrowing a function is explained in its own section

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers)_

**F6a.19** · vaguer · Offer the care that is actually wanted, P3 · not a problem

Now:

> Try some different ideas as to what might be helpful for this inner part to feel better (being welcomed by you, visualizing someone else, giving them the sort of words they would like to hear, you placing yourself in a different body position, you moving further away etc).

Published:

> You can also deliberately try support: a welcome hand placement, an imagined presence, words you’d like to hear, a different posture, or more distance.

Reader: The concrete "welcome hand placement" became "being welcomed by you", which is a different and less specific idea.

My check: As clear

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (5.56, rated small)_

**F6a.20** · lost · Offer the care that is actually wanted, P3 · not a problem

Now:

> Only try one idea at a time to see if it works.

Published:

> Introduce one change and discover its effect. A comforting-sounding resource earns its place by helping this person now.

Reader: The point that a resource that merely sounds comforting must earn its place by helping now is dropped.

My check: As clear

_came in: 18 Oct (the overnight Emulate run)_

**F6a.21** · lost · Offer the care that is actually wanted, P4 · not a problem

Now:

> If this happens, allow yourself to respond for as long as you want to do so, and for as long as you can stay there (ie remain in the process).

Published:

> Stay with the response when you want to and can remain present; more tears don’t prove more healing.

Reader: "more tears don't prove more healing" is gone, "remain present" became "remain in the process", and "respond" has no stated object.

My check: As clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (5.57, rated small)_

**F6a.23** · lost · Offer the care that is actually wanted, P6 · not a problem

Now:

> Alternatively, you may want to use the session to develop a capacity that you want to develop (ie love, play, courage, curiosity etc). You can also use it to rehearse something that you have decided to do.

Published:

> Or spend the session developing love, play, courage, or curiosity. Let a pleasant experience have time to grow. Rehearse a chosen action and notice what it would take to carry it out. Hypnosis can invite something new as well as listen to what is already present.

Reader: Letting a pleasant experience grow, noticing what it would take to carry out the rehearsed action, and the point that hypnosis can invite something new as well as listen to what is present are all dropped.

My check: As clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (5.66, rated small)_

**F6a.25** · lost · Finish without forcing a revelation, P1 · not a problem

Now:

> When you have done as much as you want to do, it is a good idea to find out if there is anything that you need to do to make sure that you can leave things where they are for the time being.

Published:

> When you’ve received enough, stop opening new questions. Ask what would help you leave this here for now.

Reader: The instruction to stop opening new questions once you have received enough is gone.

My check: As clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (5.68, rated small)_

**F6a.26** · lost · Finish without forcing a revelation, P2 · not a problem

Now:

> Just jot down the essentials (what was there before you started, what you have done to change things, what you are unsure about, any phrases that were said, any body signals, any information that the inner child said that it needed, anything that a guard wanted you to know, any boundaries that you put in place, any repairs that you did, anything that you learnt about what it is a mistake to try and force etc).

Published:

> Afterwards, write a few lines: what was there before; what I tried; what happened; what remains uncertain. Include a phrase, bodily signal, child’s need, protector’s concern, boundary, repair, or what not to force only when it actually appeared.

Reader: "what happened" (the result of what you tried) is missing from the list, and "what it is a mistake to try and force" is a hard-to-parse version of "what not to force".

My check: As clear

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (5.73, rated small)_

**F6b.1** · vaguer · The 15-minute daily practice, P1 · not a problem

Now:

> Notice there is no need to learn a second script! The process is the same.

Published:

> Use the same practice rather than learning a second script: gather attention, listen, respond, wait, return.

Reader: "The process" no longer names the five steps (gather attention, listen, respond, wait, return), so the reader is not told what stays the same.

My check: As clear

_came in: 18 Oct (the overnight Emulate run)_

**F6b.4** · vaguer · The 15-minute daily practice, P3 · not a problem

Now:

> Once you have practiced listening a few times with the recordings, you may want to shorten them to speed up your induction, or even practice without playing them back at all.

Published:

> After familiar runs, shorten a recording to the cues you still need, then try practicing without playback.

Reader: "Shorten them to speed up your induction" no longer says what to cut down to (the cues you still need), and "or even" replaces the sequence of shortening first and then trying without playback.

My check: As clear

_came in: 18 Oct (the overnight Emulate run)_

**F6b.5** · lost · The 15-minute daily practice, P3 · not a problem

Now:

> On the other hand, if you like using the recordings, there is no reason to stop!

Published:

> Keep recordings when you enjoy them; independence means being able to guide yourself, not having to refuse help.

Reader: The reason it is fine to keep using recordings (independence means being able to guide yourself, not refusing help) is dropped, leaving only the permission.

My check: As clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (5.77, rated small)_

**F6b.7** · lost · The 15-minute daily practice, P4 · not a problem

Now:

> And most importantly, what can you carry with you as you move forward from this?

Published:

> What can you carry yourself now?

Reader: PUBLISHED asks what you can now carry yourself (what you can hold on your own, following "capacity to build"), while NOW asks what you take with you going forward, which is a different question.

My check: A fair question in its own words

_came in: 18 Oct (the overnight Emulate run)_

**F6b.8** · unclear · The weekly deeper practice, P1 · not a problem

Now:

> It’s good to give this more time once or twice a week, when that’s useful.

Published:

> Once or twice a week, give the same practice more time when that is useful.

Reader: "this" replaces "the same practice", and under a heading about a deeper practice a reader may not know whether it means the daily practice or the deeper one.

My check: 'this' is the practice the section is about

_came in: 18 Oct (the overnight Emulate run)_

**F6b.9** · lost · The weekly deeper practice, P1 · not a problem

Now:

> It’s also good to bring in some adult function to make sure nothing is being bypassed and so that at the end of the exercise, when the experience is over, there is the possibility of coming out completely and doing whatever normal thing needs doing.

Published:

> Start from Higher Self or neutral witnessing, follow what appears, borrow an adult function when needed, and ask whether anything important is being bypassed. Leave room for the full exit and any ordinary action needed afterward.

Reader: "When needed" and the separate step of asking whether anything important is being bypassed are gone, and "leave room for the full exit" becomes a result of bringing in an adult function instead of an instruction.

My check: As clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (5.82, rated small)_

**F6b.10** · vaguer · The weekly deeper practice, P2 · not a problem

Now:

> If possible, it’s good to do the normal thing immediately after the exercise, so that the subconscious sees that the adult heard and acted. Otherwise, the dishes won’t get done.

Published:

> Do the ordinary action immediately when possible. That teaches the subconscious that the adult heard and acted, instead of staging another beautiful internal meeting and then leaving the dishes exactly where they were.

Reader: The contrast with staging another beautiful internal meeting and leaving the task undone is dropped, so "the dishes" reads as a literal chore and the point about what talking without acting teaches the subconscious is lost.

My check: His dishes line, casual but clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (5.83, rated small)_

**F6b.11** · unclear · Capacity before content, P1 · not a problem

Now:

> NOTE: If it is medically unsafe or you are in a place of panic, sleep deprivation, nausea, deep destabilization, mania, psychosis-like symptoms, feeling overwhelmed by chemicals etc. then first focus on stabilizing and then look for what your subconscious needs you to know!

Published:

> Altered-state rule: do not ask for hidden truth while medically unsafe, panicking, sleep-deprived, nauseated, destabilized, manic, psychosis-like, or chemically overwhelmed. First stabilize.

Reader: "If it is medically unsafe" has no clear "it" (the situation, the practice, you?), unlike PUBLISHED's "while medically unsafe", which describes the person's state.

My check: 'it' is the situation; clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (6.0, rated small)_

**F6b.12** · lost · Capacity before content, P5 · not a problem

Now:

> When you are flooded, it is much harder to access your adult capacities so focus on being able to regulate and getting support!

Published:

> Flooding can make the adult capacities needed for pausing, comparing options, reality-testing, planning, and choosing much harder to reach. In that state, regulation and support come before deeper dialogue. Silence may be protection when the adult lacks enough regulation, support, humility, or practical capacity to receive the material.

Reader: NOW drops the point that silence from the subconscious may be protection when the adult cannot yet receive the material, and it no longer says which adult capacities flooding makes hard to reach.

My check: The section's first paragraph says it (what needs destabilizing to know isn't meant for you now)

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (6.5, rated small)_

**F6b.13** · vaguer · Capacity before content, P9 · not a problem

Now:

> The mind makes it symbolic, squashes things together, distorts, dramatizes, pulls from cultural influences, fears etc. So, treat it like an image and get some help outside of yourself!

Published:

> The mind symbolizes, compresses, distorts, dramatizes, and borrows from culture and fear. Around trauma and memory especially, treat an image as an image and involve outside support when needed.

Reader: "Especially around trauma and memory" and "when needed" are dropped from the advice, so getting help outside yourself now reads as required for every hypnotic image.

My check: The sentence before says 'especially if it relates to trauma and memory'

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (6.15, rated small)_

**F6b.15** · unclear · It feels fake, P2 · not a problem

Now:

> If it says yes, that one can sting, because there could be something to it.

Reader: "that one" doesn't say which of the three questions the yes answers, so the reader has to guess until the next sentence ("Maybe you've fooled yourself before").

My check: His inner child guide's words, lined up on 25 Oct

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (6.20, rated small)_

**F6b.16** · lost · It feels fake, P3 · not a problem

Now:

> Find out what rule it is enforcing. Comfort your little one before you answer any of it. Your answers can be firm or funny, as long as they aren’t mean.

Published:

> Don’t argue with it. Ask which rule it is enforcing and what ordinary evidence would make the new adult voice more believable.

Reader: "Don't argue with it" is dropped and replaced by permission to answer the parent voice firmly or funnily, and "your little one" and "any of it" have no antecedent in this part.

My check: His inner child guide's words, lined up on 25 Oct

_came in: 25 Oct (the answers of his first marking page)_

**F7.1** · lost · The subconscious will not answer, P1 · not a problem

Now:

> Some examples of answers might be “I need to know you will set boundaries” “I need to know you will do what you said you will do” “I need to know you won’t keep leaving” “I need to know you won’t think that knowing something means that you don’t need to do anything about it” etc.

Published:

> The reply may be extremely un-mystical: “Will you set the boundary?” “Will you keep the promise?” “Will you stop abandoning us?” “Will you stop substituting insight for action?”

Reader: PUBLISHED's point that the subconscious's replies are ordinary, practical demands rather than mystical revelations is gone, leaving a bare run of quotes.

My check: As clear: the examples carry the un-mystical point

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (6.29, rated small)_

**F7.2** · unclear · The inner child will not appear, P1 · not a problem

Now:

> You can say to the guard “You don’t have to let me in, just tell me what I need to do to make it safe”.

Published:

> “You do not have to let me in. Just tell me what would make the doorway safer.”

Reader: With the doorway gone, "make it safe" has no clear referent, and the guard now tells "me what I need to do" instead of what would make the entry safer.

My check: As clear in speech: 'make it safe' is letting me in

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (6.30, rated small)_

**F7.3** · lost · The inner child will not appear, P1 · not a problem

Now:

> You can work on your preferences or something that you’re curious about or something that you’re willing to try as a beginner etc. and see how it goes.

Published:

> If no clear child-state appears, use the session to notice one preference, curiosity, or beginner experiment instead of forcing an image.

Reader: "Instead of forcing an image" is dropped and the concrete step "notice one preference" becomes the vaguer "work on your preferences".

My check: As clear, more casual

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (6.31, rated small)_

**F7.4** · lost · The inner child will not appear, P1 · not a problem

Now:

> Work on developing a sense of who you are and reparent yourself as best you can.

Published:

> Identity-building and reparenting can happen in the same practice.

Reader: The point that identity-building and reparenting can go together in one practice becomes two separate commands.

My check: Both points are there

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (6.32, rated small)_

**F7.8** · vaguer · You become too analytical, P1 · not a problem

Now:

> Maybe it’s silence, resting, or doing something. Whatever it is, just do it.

Published:

> Silence may be the answer. Rest may be the answer. One honest action may be the answer. Take the answer that actually arrived.

Reader: "One honest action" becomes "doing something", and "take the answer that actually arrived" becomes a generic "just do it".

My check: His wish: 'ONE HONEST ACTION sounds super ai' (2026-10-21 17:56 UTC)

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (6.42, rated small)_

**F7.9** · vaguer · You become too blissful or diffuse, P1 · not a problem

Now:

> “What’s the smallest, most specific thing you can do to demonstrate the love you’re feeling?”

Published:

> “What task, boundary, meal, rest, repair, or conversation does love require next?”

Reader: The concrete menu and the question of what love requires next are replaced by a general prompt to demonstrate the love you feel.

My check: As clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (6.43, rated small)_

**F7.12** · unclear · You get stuck in endless processing, P3 · not a problem

Now:

> What would the Guide choose to do now?

Published:

> “What direction would the Leader choose now?”

Reader: The role the PUBLISHED guide calls "the Leader" is now "the Guide", which does not match the earlier name and collides with "the guide" meaning this document.

My check: His term: the Guide is one of the inner adult's roles, with its own section

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (6.54, rated small)_

**F7.14** · lost · What not to do, P6 · not a problem

Now:

> DO NOT: “Extend” the duration of altered states indefinitely.

Published:

> Do not prolong altered states indefinitely or treat intuition as fact without testing it.

Reader: The second rule, not treating intuition as fact without testing it, is dropped.

My check: The list's first line already says to reality-test

_came in: 18 Oct (the overnight Emulate run)_

**F7.15** · unclear · What not to do, P7 · not a problem

Now:

> DO NOT: Allow various internal roles to get out of proportion (e.g., allow the Inner Child to run your adult life, the Protector to shut out all love, the Nurturer to disregard consequences, the Guide to ignore the needs of the Child). You are capable of analysis, as well as tenderness.

Published:

> Keep the inner roles in proportion: the child does not lead adult life; the Protector cannot exclude all love; the Nurturer cannot erase consequences; the Leader cannot bypass the child; analysis and tenderness both remain available.

Reader: "The Guide" replaces the role PUBLISHED calls "the Leader", so a reader who met "Leader" earlier cannot match it, and it clashes with "the guide" meaning the document.

My check: His own words and his term (the Guide)

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (6.59, rated small)_

**F7.16** · lost · What not to do, P13 · not a problem

Now:

> Nor should you allow anyone to activate these commands in you without your knowledge, or use them to make you do something you don’t want to do, to make you into someone you don’t want to be, to give you amnesia, etc.

Published:

> End every waking session with ordinary identity, movement, orientation, judgment, and a direct statement that the session has ended.

Reader: NOW has no counterpart to the closing-the-session step (identity, movement, orientation, judgment, and a direct statement that it has ended), leaving only "make sure you come back out" later.

My check: The reader matched the wrong published line; the return is its own section

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (6.68, rated small)_

**F7.17** · lost · When this needs more support than a guide can provide, P1 · not a problem

Now:

> You should also seek professional help promptly if you are experiencing new or worsening suicidal thoughts, severe insomnia, new or worsening manic or psychotic symptoms, or if dissociative symptoms are impacting your ability to function.

Published:

> New or worsening suicidal thoughts, severe insomnia, mania-like or psychosis-like symptoms, or dissociation that disrupts functioning need prompt professional assessment, not a four-to-twelve-week practice schedule.

Reader: The contrast that these call for assessment instead of continuing the practice schedule is dropped.

My check: As clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (6.69, rated matters)_

**F7.18** · unclear · When this needs more support than a guide can provide, P3 · not a problem

Now:

> You probably don't need any more support than this if you keep the practice shorter, make it warm, pick a small and tractable subject, make sure you come back out, and then see how it affects a specific target (anxiety, daydreaming, helping a relationship, facing a task you've been avoiding, helping you sleep, being less reactive emotionally, improving your intuitive accuracy, etc) for a week or two.

Published:

> For ordinary learning, start with shorter sessions, warmth, a manageable subject, and a full return. Over a week or two, track one target—anxiety, daydreaming, relationship repair, an avoided task, sleep, emotional regulation, or intuitive accuracy.

Reader: "Than this" has no clear referent, and an instruction for ordinary learning becomes a reassurance that you probably need no more support, which says something different.

My check: The heading anchors 'this' (a guide)

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (6.72, rated matters)_

**F7.19** · lost · Methods to explore with a trained person present, P1 · not a problem

Now:

> If you want to deliberately do trauma-focused regression (going backwards in your memory or imagination to times when you were younger), or affect and somatic bridging (following associations from an emotional or somatic experience to find the origin of that experience, particularly if it was a traumatic experience you don't know about), or if you find that you're having substantial flashbacks or dissociative reactions, then you should do this with a trauma-informed clinician present.

Published:

> Either can have different uses, including resourcing.

Reader: NOW drops the nuance that regression and bridging can also serve other uses such as resourcing, so they read as trauma tools only.

My check: He cut that aside on 25 Oct (CV-5.7)

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (6.73, rated small)_

**F8a.3** · vaguer · Appendix A: How to ask the subconscious a useful question, P10 · not a problem

Now:

> Most importantly, you always need to make your prompt safe, otherwise the analytical part of your mind will make up an answer just so it fits with your prompt.

Published:

> Always include a safe fallback so the analytical mind doesn’t treat silence as failure and manufacture an answer.

Reader: "Make your prompt safe" does not say the step is to add a fallback that allows silence, and it blurs with the Constraint element just listed.

My check: The prompt line after it shows what 'safe' means

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (7.18, rated small)_

**F8a.5** · unclear · Core prompts, P7 · not a problem

Now:

> I ask my wise subconscious mind to help me see if the intuition or impulse I have about …is coming from my universal heart or from my family, my religion, marketing, erotic programming, my political tribe, my trauma response or an old deal I did as a child to belong.

Published:

> Wise subconscious, please help me look at this impulse clearly.

Reader: "about …is coming" leaves a gap with no instruction to fill in the thing you are asking about, so the sentence does not parse as written.

My check: A template's blank

_came in: 18 Oct (the overnight Emulate run)_

**F8a.8** · vaguer · The four NLP layers, P4 · not a problem

Now:

> Strategy level of NLP: practising a better response.

Published:

> Strategy NLP rehearses a better response: when this cue appears, the adult does this.

Reader: The concrete form (when this cue appears, the adult does this) becomes the general "practising a better response".

My check: As clear

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (7.37, rated small)_

**F8a.10** · unclear · The Milton Model, minus the covert sales seminar, P5 · not a problem

Now:

> We paced it; we opened up awareness; we validated the reason for the reaction; we presumed we could do it; we used a bridge word to make it easier and we invited one thing.

Published:

> Pace reality. Open awareness. Validate function. Presuppose capacity. Bridge gently. Invite one small movement. Test with the body.

Reader: "it" in "paced it" and "do it", and "the reaction", have no antecedent in the example sentence, so a reader cannot match the steps to it (and "pace" and "bridge word" are not yet explained).

My check: 'it' is the example sentence just above

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers)_

**F8b.2** · vaguer · Submodalities — editing the form, not denying the truth, P3 · not a problem

Now:

> And I can allow myself to know that I am not deleting the message, just turning down the volume so that I am able to be present enough to hear what it is.

Published:

> I am not deleting the signal. I am adjusting the volume so I can listen without being overwhelmed.

Reader: "hear what it is" leaves out what the message is saying, and the reason for lowering the volume, to listen without being overwhelmed, is gone.

My check: As clear

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (8.15, rated small)_

**F8b.9** · lost · Installing the synchronicity cue, P6 · not a problem

Now:

> Ask yourself: "What does my Nurturer think about this?", "What does my Protector think about this?", "What does my Guide think about this?"

Published:

> Ask the Nurturer, Protector, and Leader what each sees.

Reader: The third part is called "Guide" instead of "Leader" with no introduction, so a reader who knows the Nurturer, Protector and Leader would not know who this is.

My check: His term (the Guide)

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (8.35, rated matters)_

**F8b.10** · lost · Installing the synchronicity cue, P9 · not a problem

Now:

> These cues do not authorize you to make a decision. They do not stop you from hearing the message of your intuition if it is warning you about something.

Published:

> The cue remains self-authored, visible, reversible, and limited to orientation. It can’t authorize a decision, prove an intuition, suppress a warning, or let another person control the response.

Reader: The limits are cut to two, dropping that the cue is self-authored, visible, reversible and limited to orientation, that it can't prove an intuition, and that no one else may control the response.

My check: He cut those limits on 25 Oct (CV-6.5 to 6.8)

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (8.38, rated matters)_

**F8b.12** · lost · False positives, and turning the cue off, P3 · not a problem

Now:

> You can do that by not rehearsing them anymore and by saying to yourself (when you are fully awake) that you don't want to use synchronicity as a cue anymore (e.g. "From now on, I am no longer going to use noticing synchronicity as a cue for waking up. I let go of this association, coincidences can go back to being just coincidences."). Saying this is just you deciding, it doesn't mean the association is gone straight away.

Published:

> To retire it, stop rehearsing it and say while fully awake: “Synchronicity is no longer a cue. I release this association and return coincidence to ordinary uncertainty.” Remove it from the written cue list and stop rehearsing it. The statement expresses your decision; it does not prove the association has vanished immediately.

Reader: The concrete step of removing the cue from the written cue list is dropped, and no written cue list is mentioned anywhere else in NOW.

My check: A small step the guide's cue list never had (25 Oct check: stays)

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (8.48, rated matters)_

**F8b.13** · lost · Reframing — changing the meaning without lying, P1 · not a problem

Now:

> Instead ask yourself: What else might be true? or What is this part trying to do for me? or How might my Nurturer reframe this? or How might my Protector reframe this? or How might my Guide reframe this? etc., etc.

Published:

> “What would the Nurturer, the Protector, and the Leader each say about this?”

Reader: The Leader is again renamed "Guide" with no introduction.

My check: His term (the Guide)

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (8.50, rated matters)_

**F8b.15** · vaguer · Future pacing — let the future test the insight, P1; Future pacing — let the future test the insight, P2; Running the whole NLP sequence, P9 · not a problem

Now:

> Future Pacing: 1) Once I have seen the situation more clearly, I will imagine future scenarios where my old behavior would have triggered, to test out if my new insight is working. If these scenarios come up, I will choose new small behaviors using an Implementation Intention (If...then... statement)

Published:

> Don’t end with “I understand.” Ask where life will test the understanding, picture the actual cue, and rehearse the smallest better response. “If [cue], then I [small action].”

Reader: "If these scenarios come up" doesn't say whether the imagined scenarios or real ones are meant, and the steps of picturing the actual cue and rehearsing the smallest better response became "choose new small behaviors".

My check: As clear

_came in: 18 Oct (the overnight Emulate run)_

**F9.3** · vaguer · What I will not use NLP for, P7 · not a problem

Now:

> I do not use NLP on people who are panicked, destabilized, manic, having a psychosis-like state, or are too high/dissociated to reality test.

Published:

> While panicking, destabilized, manic, psychosis-like, chemically overwhelmed, or too dissociated to reality-test.

Reader: "chemically overwhelmed" became "too high/dissociated", which narrows the substance condition and fuses it with dissociation into one slashed state.

My check: Clear ('too high/dissociated' for 'chemically overwhelmed or too dissociated')

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (8.68, rated small)_

**F9.6** · unclear · Running the whole NLP sequence, P7 · not a problem

Now:

> Put 3 good adults in with the person (Nurturer to warm, Protector to make it safe, and Guide to point a direction).

Published:

> Bring in the three adults. Nurturer warms, Protector makes it safe, Leader points a direction.

Reader: The third adult is renamed from Leader to Guide, which no longer matches the published trio and collides with "a good guide" and "a bad guide" (an outside person) in Appendix C below.

My check: His term (the Guide)

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (9.1, rated small)_

**F9.10** · lost · Appendix C: The extended de-hypnosis checklist, P1 · not a problem

Now:

> What is my body telling me to do about this (how does my body feel)?

Published:

> I can notice what my body is signaling without assuming what it proves.

Reader: The caution "without assuming what it proves" is gone and the body is now treated as giving instructions ("telling me to do"), which says something different from noticing a signal.

My check: His own Appendix C

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (9.11, rated matters)_

**F9.11** · vaguer · Appendix C: The extended de-hypnosis checklist, P1 · not a problem

Now:

> What would life have me do here?

Published:

> I can ask what love, truth, humility, and ordinary life would require.

Reader: "ordinary life" became plain "life", which is more abstract and drops the guide's recurring point about ordinary life.

My check: His own Appendix C

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (9.12, rated small)_

**F9.9** · lost · Appendix C: The extended de-hypnosis checklist, P1 · not a problem

Now:

> What would this thing influence me to believe that isn’t true in order to get what it wants from me?

Published:

> I can ask what is being presupposed. I can ask who benefits.

Reader: Two open questions (what is being presupposed, who benefits) became one convoluted question that presumes the influence is false and no longer asks who benefits.

My check: His own Appendix C (23 Oct), clear

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (9.10, rated matters)_

**F9.12** · unclear · Appendix C: The extended de-hypnosis checklist, P2 · not a problem

Now:

> If what you’re investigating is true, it can take your questioning (as the police like to say).

Published:

> If this is true, it will survive questions.

Reader: A reader cannot tell what "as the police like to say" refers to or how it fits "it can take your questioning".

My check: His own aside

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers); flagged on 25 Oct (9.14, rated matters)_

**F9.13** · unclear · Appendix C: The extended de-hypnosis checklist, P3 · not a problem

Now:

> Before you do what it wants you to do, see if it does any of the following: create a sense of urgency, secrecy, shame, threat of exclusion if you don’t do what it says, specialness, sexual charge, spiritual superiority, ask you for money, ask you for sex, ask you for loyalty, ask you to be quiet, ask you to obey it, try to limit your choices, make it seem like it’s bad to question it, act like not obeying it is a problem that needs to be solved, make normal life seem boring/stupid/irrelevant in its presence, try to seduce/scare/rescue your child, not let your adult self say no.

Published:

> Before acting, ask: Is there urgency? Is there secrecy? Is there shame? Is there a threat of exclusion? Is there a promise of specialness? Is there sexual charge? Is there spiritual superiority? Is there a demand for money, sex, loyalty, silence, or obedience? Is there a narrowing of choices? Is questioning treated as betrayal? Is resistance pathologized? Is ordinary life being downgraded? Is the child part being seduced, scared, or rescued? Is the adult self still allowed to say no?

Reader: Fourteen separate yes/no questions became one eighteen-clause sentence that mixes noun phrases and verb phrases and ends with "not let your adult self say no", which does not attach to "does", so the reader must re-parse it.

My check: His own list, long but it reads

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers)_

**F9.14** · vaguer · Appendix C: The extended de-hypnosis checklist, P3 · not a problem

Now:

> ask you for money, ask you for sex, ask you for loyalty, ask you to be quiet, ask you to obey it

Published:

> Is there a demand for money, sex, loyalty, silence, or obedience?

Reader: "a demand for" became "ask you for", so an ordinary request such as a fee now reads as a warning sign and the pressure that made it one is gone.

My check: His own Appendix C

_came in: 20-23 Oct (installs of the induction section, the NLP appendix and his answers)_

**F9.21** · lost · Body supports, P2 · not a problem

Now:

> But neither one of those products is necessary. All you really need is to stabilize yourself, and then listen to the messages from your inner realm, reality test those messages, and then take one grounded action.

Published:

> These remain optional supports. They don’t prove that any inner signal is true. Stabilize the body, listen gently, reality-test, and return to one grounded action.

Reader: The published point that these products do not prove any inner signal is true is gone.

My check: He cut that caution on 25 Oct (CV-7.4)

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (9.39, rated small)_

**F9.25** · vaguer · Appendix F: Self-trust, outside guidance, and oracle-like states, P2 · not a problem

Now:

> One of the issues here is that people vary dramatically in how suggestible they are, both internally and externally, and different people vary in how suggestible they are in different states. Different types of suggestion (commands, imagery, music, metaphors, spiritual, etc) can be very different for different people.

Published:

> Suggestibility varies wildly. Some people open more with an external hypnotist, some with themselves, some only in particular states, and some barely respond to commands while responding deeply to imagery, music, metaphor, or spiritual feeling.

Reader: "open more with an external hypnotist, some with themselves" became the bare "both internally and externally", and the contrast between commands and imagery, music, metaphor or spiritual feeling became "can be very different for different people".

My check: As clear, less detailed

_came in: 18 Oct (the overnight Emulate run)_

**F10a.2** · unclear · Forgiveness without bypass, P1 · not a problem

Now:

> They really did hurt us and they still have to answer for it, and our boundary with them still matters, but one day we may find that we have forgiven them, or at least that we’re not being run by the resentment anymore.

Published:

> All of these can remain true together: the harm happened, the boundary still matters, the person remains accountable, and forgiveness may come later when your relationship to the event changes on its own.

Reader: "They" is the first mention of the person who caused the harm (the paragraph so far speaks only of "we" and "the injury"), so the reader has to guess who "they" are.

My check: 'they' follows 'the injury'; clear

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (9.76, rated small)_

**F10a.10** · lost · Appendix G: Altered states, P7 · not a problem

Now:

> In other words, if using self-hypnosis while you're in an altered state of consciousness is NOT helping you become MORE loving, MORE grounded, MORE honest with yourself, helping you SLEEP, become MORE communicative, MORE able to do your everyday responsibilities, etc, then stop trying to go DEEPER into your altered state of consciousness, and start working on integrating what you've already gotten from it.

Published:

> If the state makes you less loving, less grounded, less honest, less able to sleep, less able to communicate, or less able to meet ordinary responsibilities, stop deepening and start integrating.

Reader: The trigger changes from the state making you less loving, grounded and so on (getting worse) to it merely not helping you become more of each, and the list loses its parallel form midway ("helping you SLEEP, become MORE communicative").

My check: His own capitals and rule (the 25 Oct check found the same and kept it)

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (10a.0, rated matters)_

**F10b.1** · vaguer · Start with the room, the body, and basic safety, P2 · not a problem

Now:

> If you need to, open your eyes, ground yourself in your body and your environment, remove yourself from any bad influence you’re surrounding yourself with, stop stimulating your mind.

Published:

> Open the eyes, feel the feet, name the room, lower stimulation, leave hostile company, and stop adding prompts.

Reader: Concrete steps became general ones: "feel the feet, name the room" became "ground yourself in your body and your environment", and "leave hostile company" and "stop adding prompts" became the less exact "remove yourself from any bad influence you’re surrounding yourself with" and "stop stimulating your mind".

My check: As clear, less detailed

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (10a.21, rated small)_

**F10b.4** · garbled · Do not fight from fear, P1 · not a problem

Now:

> But if you’re fighting it out of fear…

Published:

> But fighting from fear can fasten attention more tightly to the thing you want gone.

Reader: The sentence stops at an ellipsis with no result clause, so PUBLISHED's claim that fighting from fear tightens attention on the thing is left for the reader to infer from the next paragraph.

My check: The ellipsis leads into the next paragraph, which gives the result

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (10a.28, rated small)_

**F10b.5** · vaguer · A bodily boundary: compassion present, door closed, P2 · not a problem

Now:

> This is especially a good idea if the presence you’re experiencing seems even the slightest bit hostile, cold, alien, parasitic, etc. It’s not really helpful to approach it with the kind of soft, sentimental love that you’d use if you were inviting it to stay for tea, but it can be useful to approach it with love while also making it clear that it needs to respect your boundaries.

Published:

> When the presence feels hostile, cold, alien, parasitic, or boundary-violating, don’t offer soft sentimental love as though inviting it in for tea. Use love with a boundary.

Reader: PUBLISHED's rules ("don’t offer soft sentimental love", "Use love with a boundary") became hints ("not really helpful", "it can be useful"), and "especially a good idea" blurs whether closing the door is for hostile presences only or for any presence.

My check: As clear

_came in: 25 Oct (the answers of his first marking page); flagged on 25 Oct (10a.32, rated small)_

**F11.8** · unclear · 3. Rhythmic breath or pulse, P1 · not a problem

Now:

> Notice what you become aware of in the first beat – you don’t need to make your mind blank, just notice what comes up.

Published:

> Stop the deliberate rhythm and notice the first quiet beat, without trying to become blank.

Reader: "The first beat" no longer says it is the first quiet beat after the deliberate rhythm stops, so a reader may take it for the first beat of the rhythm.

My check: 'the first beat' follows 'then stop saying it'

_came in: 18 Oct (the overnight Emulate run)_

**F11.9** · lost · 4. Unwinding object, P1 · not a problem

Now:

> How many did you put down?

Published:

> Count only strands you actually set down; nothing is erased.

Reader: The condition that only strands actually set down are counted and the reassurance that nothing is erased are dropped.

My check: As clear

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (10b.28, rated small)_

**F11.12** · lost · 6. Gradual wave, P1 · not a problem

Now:

> See if there is anything different at each step.

Published:

> Pause at each step and notice what changes without claiming medical repair.

Reader: The caution to notice what changes without claiming medical repair, and the pause at each step, are dropped.

My check: He cut that caution on 25 Oct (CV-8.3)

_came in: 18 Oct (the overnight Emulate run)_

**F11.22** · lost · Body awareness and changing the amount of contact, P1 · not a problem

Now:

> These sources talk about the key concepts of tracking what is happening in the body, resources, titration, pendulation, and the range of foci available when working, from sensation and imagery to behavior, emotions, and meaning, etc.

Published:

> The invitation to try a movement or image is not a claim that a particular physiological repair has occurred.

Reader: The closing caution that trying a movement or image is not a claim that physiological repair has occurred is dropped.

My check: He cut that caution on 25 Oct (CV-8.8)

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (10b.2, rated matters)_

**F11.24** · unclear · Inner speech and putting experience into words, P1 · not a problem

Now:

> Not everybody has an inner voice (Nedergaard and Lupyan 2024) is not about self hypnosis adaptations, but about people with different amounts of inner speech.

Published:

> Nedergaard and Lupyan’s Not Everybody Has an Inner Voice (2024) studied people reporting different amounts of inner speech, not self-hypnosis adaptations.

Reader: The title is the sentence's subject in plain sentence case with no italics or quote marks, so the sentence first reads as a claim followed by "is not about".

My check: The title is a link on the page

_came in: 18 Oct (the overnight Emulate run); flagged on 25 Oct (10b.16, rated small)_

