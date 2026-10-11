# Community article: what I need from Joel

Last updated 2026-10-11 20:30 UTC. **Open questions: 6.** To answer, reply in chat with the number and the letter, for example `1: A`, or in your own words. Everything else in my messages is status.

This file is the page's master copy (in Git, so a session in either of your accounts can read and update it). The passages each question is about are on the side-by-side pages named under it.

## Open questions

### 11. 😂 on the emoji list
The gate says you placed 😂 yourself (2026-10-06), but it isn't on the allowlist in `tools/humanization/EMOJI-LIST.md`, so the linter's new emoji check fails it in my text.
- **A. Add 😂 to the allowlist.** **B. Leave it off** (it stays yours to place).

My recommendation: A, since you use it. Default: B.

### 12. Your rights paragraph: can "don't interfere" reach a child's outside adult, or family contact?
R18 says people keep relationships outside the community "as long as those relationships don't interfere with the community as a whole". Your example (a hostile boyfriend moving in) is about who lives on site, but the condition as written covers every outside relationship. Two other sections protect some of these with no condition: a child's "trusted adult, advocate, or reporting route … reachable without going through community leadership" (Children Need Freedom Inside Real Protection), and "family contact" during a separation (When Somebody Has to Go). A community facing a complaint could call those "interfering".
- **A. Add that the condition never reaches those** (a child's outside adults, a reporting route, family contact), in your words.
- **B. Narrow the condition to who lives on site**, like your example.
- **C. Leave it.**

My recommendation: A. Default: C. Page: row R18.

### 13. "Hard to deal with": a lower bar than "When Somebody Has to Go"?
R16 says a member avoiding the therapy process and "becoming hard to deal with" will "naturally not belong at a certain point". "When Somebody Has to Go" sets the bar at serious danger, repeated violation of essential boundaries, or making shared life impossible, and says "Decide the process before the name". Two cold readers asked who decides, and whether skipping therapy costs equal respect.
- **A. Say it goes through the process the community set beforehand**, not a judgment about one person (your words).
- **B. Say "naturally" means the person usually chooses to leave.**
- **C. Leave it.**

My recommendation: A. Default: C. Page: row R16.

### 14. Before critical mass: do people on your land get written terms?
Your answer this morning was clear: before critical mass it's your land and your rules, like visiting a friend, and your new paragraphs say so. The stance check's remaining question: "From Visitor to Member—Slowly" says visitors, volunteers and renters "do not need full political membership to have rights" but need "clear terms, a way to be heard, and review", and the land section says "Write the exit terms while departure is still hypothetical". Does that apply to people living around you before you formalize?
- **A. Yes: say they get clear terms and exit terms even then** (one sentence, your words).
- **B. No: say those come with formalizing.**
- **C. Leave it.**

My recommendation: A, since the article asks it of everyone else. Default: C. Page: rows J1 to J3.

### 15. Who strikes the privacy balance?
R14: "privacy also can be resistance to the communal spirit, so there has to be a dynamic, living, always re-assessed balance". Section 4's principle says each person "keeps authority over our own practice". If the group can judge a member's privacy to be resistance, the stance check asks whether authority over what that member shares still stays with them.
- **A. Say the member still decides what to share, and the balance is about what the group can expect** (your words).
- **B. Leave it.**

My recommendation: A. Default: B. Page: row R14.

### 16. Three places readers stumbled (your text; small, optional)
- J1: "it's especially so" when a community forms naturally. Readers got the reason ("with no rules yet, nothing checks the founder") but asked for it to be said.
- J3: the divorce half of the marriage analogy. Readers got "leaving a commune also means dividing shared property", but asked what it stands for.
- R18 and R19: "can't be voted away" and then "even by a majority vote". Two readers read it as a contradiction; it's the published structure (a vote can't take the right; if one does, leave).
- And the clause you asked me to debug: readers do get "as I'm describing may happen in my case" (details below, under Decided). "as I'm saying may happen" is the more usual form of that construction, if you want it smoother.

**A. Leave all as they are.** **B. Tell me which ones to tighten** (or write the words).

My recommendation: A, except the R18/R19 one, where "If those rights are taken from you anyway" would remove the stumble. Default: A.

## For you to do (no decision needed)

1. **Merge the rules fix from your 18:35 message, pull request 159** (about one minute): `gh pr merge 159 -R u-dont-existDOTcom/joel-articles --merge`. It worked when that pull request says Merged. Why it's yours: merges are yours.
2. Nothing to do for the shared-rules lessons: they're with the UDA worker (its `uda-lane` pull request now carries your 18:35 rule too).

## Decided

- 2026-10-11 18:35 UTC, on question 4: "4 this is redundant, i cut it". Cut. I should have seen it: the "willing to be seen" sentence repeated P14's point, and the gate already says a reviewer's "what does this term mean?" can mean the term doesn't belong. Now, before I ask you what a term means, I check whether its sentence is needed.
- 18:35, on question 8: "before critical mass, my rules apply, because it's my land, just like if i go visit a friend, their rules apply ... i decide who stays, i decide who leaves ... probationary period is already explained elsewhere int hea rticle right?" Yes: "From Visitor to Member—Slowly" covers it as "provisional membership" (period, rights, responsibilities, review, exit), later in the article. Your article version of the paragraph is in (J1 to J3), with P10, at the end of the first part.
- 18:35: "you can't just take what i say to you and publish it. it has to make sense in context." Agreed, and it's in the gate (pull request 159): an answer in chat is content for me to place and adapt, with my changes shown; text you give as article text goes in as written. What each of your changes showed I could have caught is in the same pull request, and your rule itself is with the UDA worker.
- 18:35, on P15: "you can' tsay "required as pre-reqs" that's redundant". Your rewrite has "are pre-reqs". The phrase was mine, and once pull request 159 is merged the linter fails it and its cousins ("pre-reqs are required", "a necessary prerequisite") in my text.
- 18:35: "but i'm still seeing a tension between the argument that the community should and shouldn't gatekeep. do you see that?" Yes. The stance checks flagged it in every round and I passed it to you as a contradiction in the published text instead of fixing the argument. Your rewrite resolves it ("Well, it is gatekeeping. ... a living balance must be struck."), so questions 9 and 10 are closed.
- 18:35: "\"as I'm describing may happen in my case\" is obvious so you should debug why the cold reader can't understand it." Debugged: readers get it (the same model paraphrased it right when asked), but my cold-read prompt asked for anything that "stops you", so a one-word stumble at "may happen" got reported as "can't parse". With a rule to give its best reading first, it stops flagging it (0 of 2 runs, from 4 of 4) and still asks the real questions. Underneath, this lane's cold read was a hand-written prompt that never got the shared fixes; it's now built from the shared rules (pull request 159). Checked blind: your clause read fine 4 times out of 4, and every break I planted was still caught (12 of 12).
- 18:35: "i rewrote this whole section". Your rewrite is in as R14 to R19, with one typo fixed ("ends by up treating"). The section reads 100% Human (232g).
- 2026-10-11 02:57 UTC: "1: a 2a 3a 4a 5a 6a 7 so this is not just a problem for me, it's a problem in every community, but especially in communities which form naturally over time …" Done in section 11 v10: 1 to 3 kept as they were; 5 A in P18 ("a ceremony rule the community holds, separate from the personal principles above"); 6 A in P19 ("different from the daily signs above"); 7 your paragraph in after P10, typos fixed only. 4 A waits for your words (question 4).
- 2026-10-11 02:57 UTC: "you mention that boring and quietly were in the tells list, but never checked? why is that? can we debug that? any time something is not executing as intended it should be debugged. make sure to send that to UDA worker it should be in UDA." Done: the audit found 31 of 82 checkable tells unchecked and four checks that couldn't match; fixed, with a registry and a test (pull request 157), and the lesson filed for the UDA worker.
- 2026-10-11 02:57 UTC: "you don't need my ok each time to run the GUI pangram checks i told you that before." In the gate now, in your words (pull request 157).
- 2026-10-11 02:57 UTC: "how do i give you access to joel-articles?" I attached it to this session with push access (the GitHub app already had it); pushes now go from here.
- 2026-10-10 13:53 UTC: "you can run the web checks without my OK." Done: section 11's Pangram batches ran without asking.
- 13:53 UTC: "show me the examples you got wrong and what AI tells you noticed and why you marked it human when it was AI and vice versa." Done: `community-prediction-misses.html`; the lesson is in rules pull request 154.
- 13:53 UTC: "i merged." Rules pull request 153 is merged.
- About 13:00 UTC: the section 10 subheading "Federated Communities Make a Movement". Installed (section 10 v2).
- 12:22 UTC, on "boring": "it's not a full ban but please be very careful". Section 11's "Then follow the boring power" is "Then follow the practical power".

## Coming up (not a question yet)

- Section 12, "The Math of Absorption, and Who This Isn't For". Default: the same method (stance ledger, baseline, Emulate, the gate, then the section); I'll ask only about kept items and headings.
- Information on earlier pages, no answer needed: section 10's "Make a Movement" repeats the section title; section 10 P8's stored "what happened" could expose the people in an intimate case (your published wording); an optional "why cooperation slides" sentence for section 10 P6, yours to write; section 9's stance question on your P9 and P11 against "When Somebody Has to Go" (which Zapatista body reviews local power after 2023) is on the section 9 page.
