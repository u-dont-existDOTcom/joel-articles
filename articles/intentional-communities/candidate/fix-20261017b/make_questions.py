"""The questions page after Joel's message of 2026-10-17 17:16 UTC: 43 and 44 answered (to "Decided", with what I did and the
checks), his 45 answered (the whole-article pass, done), 45's acceptance still open, and the new questions 46 to 51 at the top.
Links come from batch 415g's results. Run from candidate/: python3 fix-20261017b/make_questions.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
R = json.loads((HERE / 'b415' / 'b415-results.json').read_text(encoding='utf-8'))
L = lambda k: '[check](https://www.pangram.com/history%s)' % R[k][5]
A = lambda k: '%.2f' % R[k][1]
page = (C / 'OWNER-QUESTIONS.md').read_text(encoding='utf-8')
head_end = page.index('\nColours:')
HEAD = ('# Community article: what I need from Joel\n\n'
        'Last updated 2026-10-17 in the evening, after your message of 17:16. Your 43 and 44 are done, and so is the whole-article '
        'faithfulness pass you asked for in 45: what it fixed is under "Decided", and what only you can decide is up here. **Open '
        'questions: 7** (45 to 51). Every question is here at the top, numbered, with its options; nothing further down needs an '
        'answer. To answer, reply in chat with the number and the letter (for example "46 a"), or in your own words. Below the '
        'questions: what\'s for you to do, what you decided and what I did about it, and what\'s coming up next.\n')
V = {k: L(k) for k in R}
V.update({'a_' + k: A(k) for k in R})
OPEN = '''## Open questions

> [!IMPORTANT]
> Seven questions. Each quotes its passage; the pages sent with this message show them in place.

**🟣 45. Accept the humanized article?** The whole-article pass is done (Decided, below), and its fixes are in. Sections 13 and 14 are accepted; the rest are candidates until you say so. When you accept, I make the humanized article the registered master, with a record of what changed; your published text stays in the record.
- a) Accept it all (sections 1 to 16 and the appendix) once 46 to 51 are settled. **My pick**, after you've read the article-so-far page.
- b) Accept the sections you name; the rest wait.
- c) Not yet.

If you don't answer, nothing changes: your published text stays the master.

**🟣 46. Your anomie point, and where your screenshot goes.** It isn't in the article: the published text never says it (Decided, below, has where I looked). The place I'd put it is section 2, right after "They may disagree about politics, food, God, sex, or whether shoes are oppressive, but they agree that something about the current arrangement is starving them.", because that's where the article asks what's starving people. A draft from your own words (your instruction file's "large societies breed anomie and capture by psychopaths", your "large societies are run by psychopaths due to anomie", and your "i'm always talking about"), with your screenshot and caption after it:

> What's starving them is anomie. We evolved to live in small groups where everybody knows everybody. In a large society the shared norms and close ties that held those groups together fall apart, and that's how large societies end up run by psychopaths. (Yes, I'm always going on about this.)

"What's starving them" ties it to the sentence before; "the shared norms and close ties ... fall apart" says what anomie is, for readers who don't know the word; the bracket is your "i'm always talking about". It reads %(A46_r)s alone (%(A46)s) and %(A46n_r)s with the next paragraph (%(A46+next)s), and section 2 with it and the screenshot reads %(S2a_r)s (%(S2-A46)s). One thing a cold reader raised: with only the caption, it couldn't see what the study found or how it connects to anomie ("I can't see why the screenshot is here or what the "no, duh" is about"). A reader who sees the screenshot gets the headline, so that may be enough; it's your call.
- a) This paragraph there, with your screenshot and caption after it (they move from section 12). **My pick.**
- b) The same place, in your own words.
- c) Somewhere else (say where).
- d) Leave it out, as published; the screenshot stays in section 12, after your career-market paragraph.

If you don't answer, d: nothing changes.

**🟣 47. Section 16: two exclamations that are their paragraph's only turn (your 43: "give me the paragraph and i'll help").** Cutting either one reads fine, but then both march reads find the paragraph a run of steps, which is the structure you said Emulate covers with an exclamation:
- "Find two or three other people and meet regularly. Call it a practice group, not a commune. Practice listening and switching roles. Get through at least one disagreement too, and keep your commitments. One disagreement is enough! You can talk about a shared future later."
- "Go visit some real communities. Really, go! Twin Oaks is one. East Wind is another, and so is Acorn, ..."

My tries: "(One is plenty for now.)" for the first (still the same quip, so I'd rather you write it), and "the way I did as a kid" for the second (no reader found it a turn). And one more line in the section, from the faithfulness pass: "Trust me on this one." before "If three households keep showing up for each other like this for six months", which vouches from your own experience where the published didn't.
- a) Keep all three as they are (each reads Human in the section now). **My pick**, unless you have a better turn for either paragraph.
- b) Your lines for either paragraph (I check them alone and in the section).
- c) Cut "Trust me on this one." (the rest as it is).

If you don't answer, a.

**🟣 48. Sections 13 and 14 (accepted): exclamations, one repeat, and length.** They're accepted, so nothing changes without you. Three things:
- The exclamations, your 43 applied one by one (the list is attached): in section 13, keep 4 ("That's okay!", "(And who owns the land!)", "Being open to everybody felt so spiritual!", "(Hopefully not all at once!)"), a period for 13, and 4 phrases out ("There's lots you can do!", "Very important!", "Lots of decisions to make!", "(yes, even interns!)" without the mark). Section 14 keeps all of its own (your 37 a, and "What a relief!").
- One repeat: "But when power had crept up in their own system over the years, it took them a long review to push it back down." in section 13 says what your section 9 says ("it had crept up and consolidated itself at higher levels over time"). Under your dedup rule I'd cut it from 13.
- Length: section 13 grew from 1,327 to 2,108 words, almost none of it yours, and the whole-article reader called much of that padding (the conflict paragraph says "dealt with it" four times: "REALLY dealt with it ... But really, truly dealt with it"). A tightening pass would cut repeats inside it, with every paragraph and the section checked again.
- a) All three. **My pick.**
- b) The exclamations only.
- c) Leave both sections as accepted.
- d) Your picks.

If you don't answer, c.

**🟣 49. Section 8, your own text of 7 October: four things two readers raised.** Each is in your words, so each is yours to keep:
- The truthfulness paragraph: the published "This education must never become interrogation, punishment for uncertainty, or a reason to dismiss a report." is now "Don't let the teaching turn into interrogation or punishment when they're not sure.", after "Make sure kids understand what they say will be taken seriously if they are known to be honest." Without "or a reason to dismiss a report", a reader could take it that a child without that record may not be believed. Add "or a reason to dismiss what they report"?
- "The Door Must Open Outward": the published "If it cannot, it can still avoid punishing departure or withholding the knowledge and records a young adult needs to function elsewhere." Yours keeps the records ("They should be able to access their own records and documents"); punishing departure is gone. Add "If it can't, it can still avoid punishing departure."?
- "Amish young people, age 16, go through a 2-year period of freedom from parental control called *Rumspringa*." Rumspringa doesn't have a fixed length: it ends when they're baptized or leave. "from about 16, go through a period called *Rumspringa*"?
- "Kids in or outside of intentional communities all need to learn enough about how the money world outside operates": the published said kids who grow up without money need it especially, and "the money world outside" reads oddly for kids who already live outside. "Kids who grow up without using money especially need to learn ..."?
- a) All four. **My pick.**
- b) The first three.
- c) As you wrote it.
- d) Your picks.

If you don't answer, c.

**🟣 50. Section 11, your rewrite: may a member keep their inner life to themselves?** The published answered the spiritual failure (one person in charge of everybody's inner life) with a hard line: "Members can decline to share without producing a therapeutic explanation for the refusal." Your version balances it: "privacy also can be resistance to the communal spirit", and "if a member is avoiding the therapy process and becoming hard to deal with, they will naturally not belong at a certain point". The whole-article reader's point: the article's answer to the opening charge no longer says a member may keep their inner material to themselves; your answer seems to be that nobody holds the gate alone ("No single person or permanent group of people should handle grievances and have the power to decide who gets into or stays in the community").
- a) Keep yours; the gate line answers it. **My pick**: it's your position, rewritten on purpose.
- b) Say the difference in one sentence of your own.
- c) Bring back the published line.

If you don't answer, a.

**🟣 51. Emulate's other habits in sections 13, 15 and 16: asking and answering, and capitals.** Besides the exclamations, it asks and answers ("So which is it? Well, in a way, it's both.", "So what?", "Why bother?"; section 13 has 43 question marks against the published 6, section 15 14 against 0) and stresses with capitals ("REALLY", "VISIBILITY", "they HAVE to stay", "PLUS goats", "what the group has shown it CAN do"). Sections 1 to 12 hardly do either.
- a) The same treatment as the exclamations: keep the real ones, cut or rework the rest, and check each paragraph and section; 15 and 16 next, 13 with 48. **My pick.**
- b) Leave them.

If you don't answer, b.
'''
TODO = '''## For you to do

> [!WARNING]
> One thing, when you're back.

- 🟠 Merge when you've looked at the pages: `gh pr merge 187 -R u-dont-existDOTcom/joel-articles --merge` ([the pull request](https://github.com/u-dont-existDOTcom/joel-articles/pull/187)). It has the overnight run, this afternoon's changes and this evening's.
'''
NEW_DECIDED = '''- 🟢 2026-10-17 17:16 UTC, 43: "you can't just change ! to . if the actual wording was put in as an exclamation ... so either take out the exclamation phrases themselves, replace the exclamation marks alone only if it makes sense to, or ... ask me". Done that way in sections 15 and 16, one exclamation at a time, and a fresh reader checked each change for how it sounds:
  - kept as real reactions, or yours: "And the humor!", "Every morning!" (published), "they won't let me pay rent!", "That's fine!", your "studio apartments!" and "any of that!", and the quoted founders ("First let's get land!") and slogan ("money is impure!");
  - the mark only, where the sentence reads right with a period: "I find them so soothing.", "Spiritual graffiti still surprises me." (after the graffiti's five), "Everybody here has sheep (even me), and they are super cute.", "someone has to handle it.", "a spiritual service package.", "Less cinematic, I know.", "in one go.", "Or a sauna.", "practice before you have an audience.", and "No, not that either.", which opens the passage on the anti-gay law;
  - the phrase out: "That's it!" (your example);
  - tried and taken back: "That's fine." read curt (it's your "That's it!" shape); cutting "One disagreement is enough!" and "Really, go!" left a paragraph of steps, so those two are question 47.
  Each changed paragraph reads Human (the pages show each check), and the sections read 100%% Human: 15 (%(S15v14)s), 16 (%(S16v29)s). Sections 13 and 14 are question 48. The rule is in the shared rules now: an exclamation is content, and "!" to "." is a swap only where the sentence still reads right.
- 🟢 17:16, 44c: "i was not saying to put the prose in, i wanted the actual screenshot with the link and my caption as that quote aside to you." Done: your paragraph is back as you wrote it, and your screenshot follows it with your aside as the caption, "It's kind of a "no, duh" study.", the link on "study" ("altho" dropped, since it only joined your sentence to me). Your paragraph with the caption reads Human (%(S12v15-P2cap)s), section 12 100%% Human (%(S12v15)s). The signal I had: you'd asked to add "this link and screenshot", not words, and I wrote two sentences around them and recorded them as done, as if you'd approved my words. The rule now: material you send goes in as itself (the image, its link, your words as the caption); sentences of mine around it wait for your answer.
- 🟢 17:16, 44c: "is there no section on anomie int the article? ... pretty sure that's in the research file for the article, did i somehow leave out the key point in the actual article? if so where would that go?" No, there isn't, and yes, it's left out: the published article never mentions anomie, and "psychopath" only in the link to your shaman story; your earlier draft doesn't have it either. It is in the project's instruction file, in your words: "My core thesis: communal living is a return to our evolved ancestral pattern; large societies breed anomie and capture by psychopaths. When drafting in my byline, state this bluntly where relevant." The article carries only the first half ("People want to go back to the old way of living"). I couldn't open your public research report from here (the web reader needed your OK and timed out, and the browser route was refused), so I can't say whether the report has it too. Where it would go, and a draft: question 46.
- 🟢 17:16, 45: "we should do a final pass to make sure it's faithful to the original ... don't you agree? or you think we already basically did?" Yes, I agree, and no, we hadn't: every paragraph had a meaning check against yours and every section a stance and repeats check, but nothing had read the whole rewrite against the whole published article. Done now, by five fresh readers who hadn't seen the work: four read it beside the published, a few sections each, for lost, shifted and added points; one read both whole for the argument, callbacks, contradictions, repeats, voice and length. What they found:
  - The argument holds: "the same argument in the same order: all 17 sections, the thesis lines word for word". No published link is gone (the one new link is your study). The rewrite is 42%% longer (12,976 to 18,482 words), and 5,842 of its words are yours.
  - Fixed, with your published words: section 9's "I'm not claiming the Zapatistas already proved my whole model." (I'd cut it on 10-14 as a repeat of your money-free economy line; under your dedup rule that lost meaning, since yours covers only the economy) (%(S9v17-evid)s, section 9 %(S9v17)s); section 15's "Being in community isn't automatically liberating. It all depends on who is allowed to belong without pretending." for Emulate's "It's interesting to see that ...", and "whatever prosperity came through you later" for "whatever you made of yourself later", which said the opposite of "nobody made it alone" (%(S15v14-H3P1)s); section 16's "rather than by declaring "money is impure!"" (the rewrite mocked the belief itself, which section 4 gives as yours: "money is antagonistic to the spirit of community") (%(S16v29-H1P3)s) and "It can still change how people survive a divorce, an illness or grief." for "make a difference" (%(S16v29-H2P4+next)s); section 2's "starving" for Emulate's "starvin'", by your rule that unusual spellings are cheating (%(S2v33-P2)s, section 2 %(S2v33)s).
  - Not changed, because you'd decided them: Christian's book for the nuts and bolts, not its order (your 10-16 23:38), in section 13 and the reading list; section 13's dedup cuts, which you accepted with the section; "free resource/capacity" first in section 12 (your 10-14).
  - Yours to decide: questions 47 to 51. Everything the readers found, and what happened to each, is in the pass's record.
  - The pass also found a bug in my tool: its copy for the readers dropped closing quotes after a sentence end (the article has them all), and every earlier meaning sweep read the same damaged copy. Fixed, with a test.
- 🟢 17:16, 45: "i will also read it thru but if you didn't yet then you should first to save me time." Done first; the article so far is attached.
'''
a, b = page.index('## Open questions'), page.index('## For you to do')
d = page.index('## Decided')
dec_body_start = page.index('> Answered, with what I did.', d)
dec_body_start = page.index('\n', dec_body_start) + 1
rest = page[dec_body_start:].lstrip('\n')
coming = rest.index('## Coming up')
decided_old, coming_part = rest[:coming], rest[coming:]
coming_part = coming_part.replace('- 🔵 When you accept (question 45)', '- 🔵 When you accept (question 45)')
new = (HEAD + page[head_end:a] + OPEN % V + '\n' + TODO + '\n## Decided\n\n> [!TIP]\n> Answered, with what I did.\n\n' +
       NEW_DECIDED % V + decided_old + coming_part)
(C / 'OWNER-QUESTIONS.md').write_text(new, encoding='utf-8')
print('wrote OWNER-QUESTIONS.md', len(new))
