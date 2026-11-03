# What Joel's reorganization and edits show I could have done myself (turn 116)

His message of 2026-11-03 21:00 UTC, with his reorganized guide: "i'd like you to learn as much as possible from my edits
and reorgs to see all the things you could have done yourself (you often say you couldn't come up with "my own phrasing"
but you could maybe come up with something more like what i wanted to say)".

The material: his file against the guide I last gave him, sentence by sentence (`EDITS.md`, from `compare.py`: of his 1,525
sentences, 1,031 kept, 219 edited, 275 new; 356 of the guide's 1,599 cut; 98 of his 378 paragraphs moved), his links
(`LINKS.md`), and my read of the whole file in order. One chapter, Bringing Reparenting Into Real Life, got its six-section
order and three small trims from the other chat's plan (`chat/inner-child-real-life-toc-20261103`), which he accepted; what
follows from that chapter is from his own words in it, not from that plan.

Each lesson gives his change, then the rule I can apply before anything goes to him.

## 1. Structure

**Organize by the framework's own parts, in the order the framework implies, and say why in one line.** He made Building
Your Inner Adult run Borrow → Protector → Nurturer → Guide, and wrote the reason once: "first he/she wants to feel safe
(Protector), then, building on that safety, feel loved (Nurturer), and then ... trust allows the little one to be eager to
take guidance, and that's where Guide-building comes." The guide I gave him spread each role across method sections (Borrow
One Competency at a Time had For protecting, For warmth and For guiding; Building Trust and Simple Practices had the rest).
The three roles were defined in the opening; I could have proposed this order myself. *Rule:* when an article defines a
set of parts, roles or stages early, check whether the body is organized by them; if not, propose it, with the one-line
reason the framework gives.

**Put a technique under the goal it serves, not under its method.** Each "borrow" item went to the role it borrows: For
warmth became Borrow Someone Else's Love in The Nurturer, For guiding opens The Inner Guide, For protecting opens Protecting
and Building Trust. *Rule:* a section named for a method ("Borrow One Competency", "Simple Practices") is a sign its pieces
belong to the goals they serve.

**Group by the reader's situation.** Safety and Readiness (before you start), Practicing With Your Little One, Discovering
and Healing Old Patterns, When the Practice Gets Difficult, Altered States and Intensive Practice, Bringing Reparenting Into
Real Life, Finding a Therapist, Conclusion and Appendix. *Rule:* an H1 answers "where is the reader?"; troubleshooting goes
together, after the practice it troubleshoots.

**Name a move once and call it by name later.** The Lloyd scene became "the Mr. Rogers reframing trick", introduced in
Protecting from the Parent You Inherited and used again in Love Can Start Before It's Trusted ("Apply the Mr. Rogers
reframing trick here as well"). Same with "the borrowed adulthood trick" and "the chameleon". *Rule:* when a story shows a
move the guide uses again, give it a short handle where it is shown, and refer to it by that handle.

**When a paragraph moves, its pointers move with it.** He deleted the ones that no longer helped ("the way you did in Hear
the Guard First", "(see the section Hear the Guard First)", "Remember the checking from When Healing Turns Into Checking?",
"Remember those guards from The Urge to Escape, above?"), took "further down" off Timing Is Individual when it came to be
earlier, and wrote "further on" for forward pointers ("in « Untangling the Belonging Bargains » further on"). A few slipped
through ("as described in Noticing Counts", "that guard's trust", "That future you", "this cast", "my section, “meet the
protector first,”", the dog, the four pairs). *Rule and tool:* after any reorganization, run
`tools/humanization/section_refs.py` (every mention of a section's name, before or after it, or gone) and read every "that
X", "this X", "the X" whose X was set up in a paragraph that moved or went.

**Headings state the move, in his framing.** "Dip Your Toes In Before You Go Deep", "Don't Sell Your Inner Adult To Buy An
Outer Adult", "Protecting them from yourself", "Borrow Someone Else's Love" / "Borrow Your Love For Someone Else",
"Altered States Can Deepen Therapy or Escapism", "Listen To Your Body, Or Else!". *Rule:* a heading says what the reader
does or what is true, both sides when there are two; the jokes in them are his.

## 2. Sentences: what he changes in mine

**He cuts my summary, reaction and reassurance lines.** "Great." "The cushion was practice for it." "Sound familiar?"
"That's a lot of the overlap with this method, right there in the title." "That's still one grown-up with three jobs, like
back in The Chicken-and-Egg Problem." "Kids quit piano over one bad teacher, and this is way worse." "(No example? Try
another doorway.)" "Some of it just isn't known yet, and unknown isn't the same as gone." "And if nothing moves at all, don't
push it." *Rule:* a sentence that restates, reacts to, reassures about or dramatizes the one before it goes, unless it adds
a fact or a step. (Card R2 on the page is one he missed: "So warmth and safety come first for a while...".)

**He says the mechanism plainly where I compressed it into a figure.** "Love and trust don't have to come as a pair, but
they got tied together, as if one had to vouch for the other." became "Love and trust are reciprocal and intertangled, like
the Chicken and Egg problem. Without trust, the love seems fake. And without love, the trust is shallow." *Rule:* when a
sentence relates two things through a figure ("as if one had to vouch for the other"), write the relation itself: what
happens with one and without the other, in short sentences.

**His examples are specific and a little absurd; mine were stock.** "Or saying no to someone, and not texting an hour later
to take it back. That second one can be really hard." became "saying no to the 13th friend today who asked you to Google
something for them (I'm still working on that one)". He added "your DUIs in Maryland" to the envelope, and "smelling that
old food you're about to eat and then trashing it if it smells a little weird". He cut "picture the two of you washing the
dishes together". *Rule:* an example of mine gets a number, a place or an oddly exact detail, addressed to "you" (the 13th
friend, Maryland); a scene that fits every reader (dishes, a text an hour later) is stock. The asides about himself ("I'm
still working on that one") are his to add: I can leave the slot and ask.

**He says the reason.** "because a lot of the bad parenting or misdirection we originally received was likely lacking in
Protector and Nurturer functions, while over-relying on harsh guidance"; "Intentional, meaning instead of waiting for crisis
to hit to react"; "because the main benefit is for your little one"; "Usually what helped was how they just sat there
without trying to fix you". *Rule:* on the close read, every instruction or claim has its why on the page, in a clause.

**He adds the other side.** The workaholic gets "Or the opposite, when you stop procrastinating so much and clean your room";
the critical voice gets "it could also be trying to protect you from rejection or failure. It may be pointing to a real
problem, but in a cruel way."; the resentment gets "On the other hand, don't give in and start believing your love is more
conditional than it really is". *Rule:* when a paragraph describes one failure, ask whether some readers have the opposite
one, and give it a sentence.

**He picks the exact word.** "function" → "capacity"; "okay" → "permission"; "important" → "salient"; "monumental" →
"deep"; "the sense to see it, or the help" → "the sense, the support, or the skills they needed for a respectable
response"; "a boundary can still be right" → "appropriate to enforce with them"; "after all" → "even if you make excellent
progress"; "pl/ork" → "reparenting" where the sentence meant the practice in general. *Rule:* a word that would fit a dozen
other sentences ("right", "stuff", "after all") gets the one that fits only this one.

**He adds the qualifier that makes a claim true, and cuts the ones that only soften.** "what I screamed was true for a part
of me right then"; "“The CIA is mind-controlling me!” is (mostly) paranoia"; "You hopefully, eventually, recognize". But
"(openings can come that early, and yours may have been completely real)", "(stopping counts)" and "I wouldn't take their
answer as gospel" went. *Rule:* keep a qualifier when the claim is false without it; cut it when it only reassures.

**He cuts safety padding and keeps the action.** The crisis section kept "get another human being involved, and put some
distance between you and the means. A crisis line counts" and lost the reassurance and the disclaimers. *Rule:* a safety
passage is its action and its conditions; the rest goes. (Card C2 asks about one condition he cut with them.)

**He fixes who said it.** "Rumi says you have to keep breaking your heart until it stays open" became Hazrat Inayat Khan's
actual line, "God breaks the heart again and again and again until it stays open." *Rule:* check who said a famous line
before I attribute it.

## 3. What only he could add, and what I can do about it

His people and stories (Joelito, the Zendik meeting at five, Daja in Kenya, Malia, his sister, Cody, Bee, Ann, Bear, his
dad's line to suicidal people, the spanking, the med student friend, the church friend, Pink, the Ghost Buster), his views
(Schema Therapy's name, IFS's entity attachments, AI therapy apps), and his new material (the manipulation tactics, shame,
re-doing memories, discipline). I can't write those, and I shouldn't invent them. What I can do: where a principle has no
case, say so and ask for one of his ("a story of yours would go here"), and where a figure stands in for a mechanism, write
the mechanism and leave the story slot to him.

## 4. What I'm changing in my process

1. **Every file I give him to edit carries the article's links and pictures, and a check proves it first.** The Word file I
   sent in turn 115 had no links and no pictures (built from plain text); he edited it into this reorganized guide, so 55 of
   the guide's 67 links and all seven pictures and videos of the live post were gone from his file (his message of 21:45
   UTC: "yes the links were gone when you sent me the file"). `tools/humanization/file_links_check.py` compares a file's
   links and pictures with the article's and fails on any loss; lesson E337 (Inner Child).
2. **After any reorganization, the pointer check.** `tools/humanization/section_refs.py`, then a read of every "that X"
   whose X moved; lesson E338 (Inner Child).
3. **The sentence rules above are in the close read** (`docs/FIXING-AN-ARTICLE.md`, the close read for sense), so the next
   pass makes these changes before he has to.
