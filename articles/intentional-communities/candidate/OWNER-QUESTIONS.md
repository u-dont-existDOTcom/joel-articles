# Community article: what I need from Joel

Last updated 2026-10-12, after your message of 17:23 UTC. **Open questions: 2.** To answer, reply in chat with the number and the letter, for example `20: A`, or in your own words. Everything else in my messages is status.

Colours: 🟣 purple, a question for you; 🟠 orange, something for you to do; 🔵 blue, next or in progress; 🟢 green, done or decided.

The master copy of this page is a file in Git, so a session in either of your accounts can read and update it. The published page "Community Article Questions" on Claude is a view of that file.

## Open questions

> [!IMPORTANT]
> Two questions for you.

**🟣 20. Register the community article in joel-articles.** Right now it lives inside the inner child article's experiments folder, so GitHub's list of articles doesn't show it. Registering it gives it its own folder and records (its master text, the published source, your locked passages, the architecture map), and it shows up in the list. It publishes nothing. The repository's rules say only you can name its master.
- A: register it now. The published Substack article is the source, and the humanized version (sections 1 to 12, all still candidates) is the working master. I'd move the lane's files in a separate pull request, with every page and record moved with them.
- B: wait until every section is humanized and you've accepted them, then register the finished article.
- C: keep it as an experiment; don't register it.

My recommendation is A: you want to find it, and the move is easier now than after section 17. If you don't answer, nothing moves.

**🟣 21. Score the examples on the [Rule Scoring Sheet](https://claude.ai/artifact/NeH9dPAYfd1vGDSMTy1fGN).** It has three short sets, and you can answer them on the page; it saves as you go.
- The 14 sweep flags in your paragraphs, each with where it came from. Did you change the meaning on purpose, is it the same meaning, or should I fix it?
- Six "it" cases: is each one clear?
- Two Pangram results I can't explain: can you say why?

Your answers become the rules' examples. In your other Claude account, press "Copy answers" and paste them into the chat.

## For you to do (no decision needed)

> [!WARNING]
> One thing for you to do.

- 🟠 Merge [pull request 166](https://github.com/u-dont-existDOTcom/joel-articles/pull/166) when you're ready (about a minute): the rules from your 05:33 and 17:23 messages. Press "Merge pull request" on that page, or run `gh pr merge 166 -R u-dont-existDOTcom/joel-articles --merge`. It worked when the page says Merged.

## Decided

> [!TIP]
> Answered, with what I did.

- 🟢 2026-10-12 17:23 UTC, on question 19: your P3 ("human, best") and P16 ("let's keep this one, best one"). Both are in as you wrote them, and the whole section now reads 100% Human (944 words). Your reasons ("for P3 it's a list of 3 that's why it's AI ... and capacity is an AI tell"; P16's lists and "the vagueness of that "not now."") are in the rules. I applied your list fix to my own P14 and P15, and a meaning check put back "absorb disruption" and "the new member's heart" in P14.
- 🟢 17:23: ""it" is ok when it's clear what "it" is". The meaning checks now say so.
- 🟢 17:23: "we can't replace "dyads" with "romance" that's not the same concept." Section 4's sentence says what the published one does again: "It covers the dyads that will form whether your founding document acknowledges romance or pretends you're all beyond it." It reads 100% Human in the section.
- 🟢 17:23: "rather than just ignoring rules that fail my prose, we should fix the rules so they don't fail my prose". The sweep now marks your sentences and leaves them alone; on the sections that had 10 flags in your text, it put none there and still caught the breaks I planted in mine. The 14 are on the scoring sheet (question 21).
- 🟢 17:23: "if you're not clear about how to apply rules you can give me a list of examples i can score. put that in the joel-articles rules." In the joel-articles rules (its main rules file and the humanization gate, pull request 166); the Rule Scoring Sheet is where the examples go.
- 🟢 17:23: "can you stop giving me paths to files that are relative to something? send that bug report to UDA". Every document now comes as a file or a link. The bug report went to the UDA lane, with a check that catches a path in a message before it's sent.
- 🟢 17:23: "regarding the prediction misses file i also don't know where that is, keep that updated". It's now the [Prediction Scorecard](https://claude.ai/artifact/Sjpy4EiZGUa21iiMstDLPv), rebuilt in every turn with Pangram checks.
- 🟢 2026-10-12 05:33 UTC: "17b 18b". In: P16 has "review by someone who wasn't part of the decision", P12 has "the same need, or even more of it,".
- 🟢 05:33: "p3 got b roken because you changed ""good enough" for community to "good enough" ... then you broke p7 by reducing it to "but it's not infinite" ? what? p16 also broke the meaning ... revert those to guide exactly." Done: P3, P7 and P16 are the guide's words again, with your sentence at the end of P16: "Even then, the power to veto membership applications based on capacity remains dangerous." What let my versions through, and what now stops it, is in pull request 166: the meaning check now treats a pronoun for a named thing, a narrower thing for a general one, and a dropped "remains", "still" or "for community" as changes (tested blind: 6 of 6 planted breaks caught, no false alarms), the cold read asks what "it" and "the power" point to, and a script checks the words each claim rests on before anything else.
- 🟢 05:33: "you can't put p22 into parentheses... that's 2 parentheticals in a row..." P22 is a plain paragraph now, and the linter fails two parentheticals in a row.
- 🟢 The same kind of break elsewhere: a sweep of sections 1 to 12 found it in three more places in my text, now fixed (section 12's "fix the cars" and P22's "people who fall into these categories" narrowed the published words; section 11's "If it needs the founder's blessing" had lost "every" and "still"). It flagged 14 places in your own paragraphs, which stay as you wrote them, and one in section 4 that I kept and shouldn't have (your "dyads" correction above). The sweep's results file came to you in chat with the 17:23 reply.

- 🟢 2026-10-11 23:12 UTC, on question 11: "a". 😂 is on the allowlist (pull request 160).
- 🟢 23:12, on question 12: "let's say a grandmother is demonizing the commune. cutting contact with her could make things way worse. i think the commune needs to intervene and help people decide on how to communicate with outsiders when it's tricky and dangerous for everyone like this. that's not advice I or anyone else can give now, it's in the moment, context by context." In, as R18b, right after the boyfriend example. My changes: "step in and help" for "intervene and help", so it doesn't read as the commune taking contact out of people's hands, and "ahead of time" for "now".
- 🟢 23:12, on question 13: "first off, "decide the process before the name" doesn't make any sense and it sounds AI. fix that." Fixed in section 13: "So work out the process before it's about anyone in particular". Two lines of the same shape there wait for that section's pass. "you are misunderstanding tho, the bar is not higher." Right: I read "naturally not belong" as removal. Your answer is in: R16 now says they'd be kicked out only if it got impossible to live with, and that nearly always people leave way before that; the new R16d says they won't be demonized, are offered compassion, that the community may make exceptions (sick and needing care), and that it's up to the people involved. In the gate: before a stance question on your paragraph goes to you, I try your plainest reading first.
- 🟢 23:12, on question 14: "nobody gives clear written terms to visiting friends, that's not how anything works. ..." In, as J4 after the marriage paragraph. I used two of your three implied terms ("be respectful and be honest"), since a list of three reads AI and "be nice" overlaps "be respectful". Say if you want "be nice" back.
- 🟢 23:12, on question 15: "it depends on the situation, in general people can have their own private practices of course, but if they start worshipping Satan, they get booted, etc." In R14. A cold reader read the Satan line as a rule with no principle, so I tied it to your balance sentence: "But some practices go too far against the communal spirit. If someone starts worshipping Satan, say, they get booted."
- 🟢 23:12, on question 16: "j1: it was said, that's why you gave it to them as the reason, right?" Yes: the reason is your next sentence, and I shouldn't have passed the readers' question on. The cold reads now look for a paragraph's reason in its other sentences, and I check it before asking you. "j3. right you can mention it's the divorce half sure." In: "Leaving a commune is the divorce half of it, where the shared resources have to get split up." "r18 ... fix the reviewers." Fixed: every reviewer that judges contradictions now reads "can't" the way people mean it. Checked blind: R18 and R19 read fine 6 times out of 6, and a contradiction I planted was caught 3 times out of 3.
- 🟢 The section with all of this reads 100% Human (1,682 words scanned, batch 233g), each changed paragraph too.
- 🟢 2026-10-11 18:35 UTC, on question 4: "4 this is redundant, i cut it". Cut. I should have seen it: the "willing to be seen" sentence repeated P14's point, and the gate already says a reviewer's "what does this term mean?" can mean the term doesn't belong. Now, before I ask you what a term means, I check whether its sentence is needed.
- 🟢 18:35, on question 8: "before critical mass, my rules apply, because it's my land, just like if i go visit a friend, their rules apply ... i decide who stays, i decide who leaves ... probationary period is already explained elsewhere int hea rticle right?" Yes: "From Visitor to Member—Slowly" covers it as "provisional membership" (period, rights, responsibilities, review, exit), later in the article. Your article version of the paragraph is in (J1 to J3), with P10, at the end of the first part.
- 🟢 18:35: "you can't just take what i say to you and publish it. it has to make sense in context." Agreed, and it's in the gate (pull request 159): an answer in chat is content for me to place and adapt, with my changes shown; text you give as article text goes in as written. What each of your changes showed I could have caught is in the same pull request, and your rule itself is with the UDA worker.
- 🟢 18:35, on P15: "you can' tsay "required as pre-reqs" that's redundant". Your rewrite has "are pre-reqs". The phrase was mine, and once pull request 159 is merged the linter fails it and its cousins ("pre-reqs are required", "a necessary prerequisite") in my text.
- 🟢 18:35: "but i'm still seeing a tension between the argument that the community should and shouldn't gatekeep. do you see that?" Yes. The stance checks flagged it in every round and I passed it to you as a contradiction in the published text instead of fixing the argument. Your rewrite resolves it ("Well, it is gatekeeping. ... a living balance must be struck."), so questions 9 and 10 are closed.
- 🟢 18:35: "\"as I'm describing may happen in my case\" is obvious so you should debug why the cold reader can't understand it." Debugged: readers get it (the same model paraphrased it right when asked), but my cold-read prompt asked for anything that "stops you", so a one-word stumble at "may happen" got reported as "can't parse". With a rule to give its best reading first, it stops flagging it (0 of 2 runs, from 4 of 4) and still asks the real questions. Underneath, this lane's cold read was a hand-written prompt that never got the shared fixes; it's now built from the shared rules (pull request 159). Checked blind: your clause read fine 4 times out of 4, and every break I planted was still caught (12 of 12).
- 🟢 18:35: "i rewrote this whole section". Your rewrite is in as R14 to R19, with one typo fixed ("ends by up treating"). The section reads 100% Human (232g).
- 🟢 2026-10-11 02:57 UTC: "1: a 2a 3a 4a 5a 6a 7 so this is not just a problem for me, it's a problem in every community, but especially in communities which form naturally over time …" Done in section 11 v10: 1 to 3 kept as they were; 5 A in P18 ("a ceremony rule the community holds, separate from the personal principles above"); 6 A in P19 ("different from the daily signs above"); 7 your paragraph in after P10, typos fixed only. 4 A waits for your words (question 4).
- 🟢 2026-10-11 02:57 UTC: "you mention that boring and quietly were in the tells list, but never checked? why is that? can we debug that? any time something is not executing as intended it should be debugged. make sure to send that to UDA worker it should be in UDA." Done: the audit found 31 of 82 checkable tells unchecked and four checks that couldn't match; fixed, with a registry and a test (pull request 157), and the lesson filed for the UDA worker.
- 🟢 2026-10-11 02:57 UTC: "you don't need my ok each time to run the GUI pangram checks i told you that before." In the gate now, in your words (pull request 157).
- 🟢 2026-10-11 02:57 UTC: "how do i give you access to joel-articles?" I attached it to this session with push access (the GitHub app already had it); pushes now go from here.
- 🟢 2026-10-10 13:53 UTC: "you can run the web checks without my OK." Done: section 11's Pangram batches ran without asking.
- 🟢 13:53 UTC: "show me the examples you got wrong and what AI tells you noticed and why you marked it human when it was AI and vice versa." Done as a misses page then; it's now the [Prediction Scorecard](https://claude.ai/artifact/Sjpy4EiZGUa21iiMstDLPv). The lesson is in rules pull request 154.
- 🟢 13:53 UTC: "i merged." Rules pull request 153 is merged.
- 🟢 About 13:00 UTC: the section 10 subheading "Federated Communities Make a Movement". Installed (section 10 v2).
- 🟢 12:22 UTC, on "boring": "it's not a full ban but please be very careful". Section 11's "Then follow the boring power" is "Then follow the practical power".

## Coming up (not a question yet)

> [!NOTE]
> What's next, and what happens if nothing changes.

- 🔵 Main's new rule (pull request 165) sends every web-app Pangram check through a gate script; this lane's batches still use their own builder, with a lint guard. I'll switch this lane over at the start of section 13.
- 🔵 Section 13, "Your Little Forming Group Already Is the Community": two lines shaped like "Decide the process before the name" wait for its pass ("Discover the group's conflict capacity before hiring a surveyor." and "Write the exit terms while departure is still hypothetical.").
- 🔵 Information on section 12, no answer needed: the chart says two of the section's sentences before the text does ("A community can absorb only as much need as its members have free resource to meet." and "The cruel paradox: small communities need new members most and can absorb them least.").
- 🔵 Information on earlier pages, no answer needed: section 10's "Make a Movement" repeats the section title; section 10 P8's stored "what happened" could expose the people in an intimate case (your published wording); an optional "why cooperation slides" sentence for section 10 P6, yours to write; section 9's stance question on your P9 and P11 against "When Somebody Has to Go" (which Zapatista body reviews local power after 2023) is on the section 9 page.
