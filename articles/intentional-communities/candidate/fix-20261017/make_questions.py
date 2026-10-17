"""The questions page after Joel's message of 2026-10-17 13:11 UTC: 39 to 42 answered (to "Decided", with what I did and the
checks), his corrections and his study recorded, and the new questions 43 to 45 at the top. Links come from the results files of
batches 410g to 413g. Run from candidate/: python3 fix-20261017/make_questions.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
R = {}
for b in ('b410', 'b411', 'b412', 'b413', 'b414'):
    if (HERE / b / ('%s-results.json' % b)).exists():
        R.update(json.loads((HERE / b / ('%s-results.json' % b)).read_text(encoding='utf-8')))
L = lambda k: '[check](https://www.pangram.com/history%s)' % R[k][5]
page = (C / 'OWNER-QUESTIONS.md').read_text(encoding='utf-8')
head_end = page.index('\nColours:')
HEAD = ('# Community article: what I need from Joel\n\n'
        'Last updated 2026-10-17 in the afternoon, after your message of 13:11. Section 16 is in the article with your lines, so '
        'every section is in now. Your corrections in sections 15 and 16 are in, the PsyPost study is in section 12, and each '
        'correction you showed has a check now that would have caught it. **Open questions: 3** (43 to 45). Every question is here '
        'at the top, numbered, with its options; nothing further down needs an answer. To answer, reply in chat with the number '
        'and the letter (for example "43 a"), or in your own words. Below the questions: what\'s for you to do, what you decided '
        'and what I did about it, and what\'s coming up next.\n')
OPEN = '''## Open questions

> [!IMPORTANT]
> Three questions. Each quotes its passage; the pages sent with this message show them in place.

**🟣 43. Exclamation marks in sections 13 to 16.** Sections 1 to 12 end 2 of their 697 sentences with "!". Sections 13 to 16, which Emulate rewrote, end 38 of their 313 sentences that way, about one in eight: section 13 has 18, section 14 has 2, section 15 has 9 and section 16 has 9. In section 16, for example: "Don't try and fly right to the economic destination in one go!", "That's fine!", "That's it!", "Or a sauna!", "And practice before you have an audience!", "One disagreement is enough!", "Really, go!". The new check stops what you caught (three in four sentences); for the rate it only raises a flag.
- a) Bring sections 15 and 16 (not accepted yet) toward the rest of the article: keep the exclamations that are a real reaction, end the others with a period, and check each changed paragraph and both sections in Pangram. Sections 13 and 14 are accepted, so I'd list theirs for you to decide. **My pick**: Emulate brought these in, and your own sections hardly use them.
- b) Keep them as they are: these sections talk to the reader about what to do, and a livelier tone can suit that. The check still stops a run like the one you caught.
- c) Something else (a rough number per section you're comfortable with, say).

If you don't answer, they stay as they are (b).

**🟣 44. Where the PsyPost study went.** In section 12, at the end of your paragraph about the career market: "Instead we optimize to fit the career market with all the little energy we've got. A new study found that where relationships are easy to make and break, people even feel less on the same page with whoever doesn't help them reach their goals. Kind of a "no, duh" study, but still." The link is on "new study", and your screenshot comes right after the paragraph. As a paragraph of its own, two cold reads couldn't see why it was there, and it cut your "So then a lot of people end up thinking they aren't "good enough" for community" off from what it follows. At the end of your paragraph, the third read found every paragraph OK. The paragraph reads Human alone (%(p2)s), and the section 100%% Human (%(s12)s).
- a) Keep it there. **My pick**: the study backs your career-market point, and your "So then" follows from it.
- b) The same, without "Kind of a "no, duh" study, but still." (your aside to me).
- c) Somewhere else, or your own words for it.

If you don't answer, a.

**🟣 45. Accept the humanized article?** Every section is in the article now. Sections 13 and 14 are accepted; the rest are candidates until you say so. When you accept, I make the humanized article the registered master, with a record of what changed; your published text stays in the record.
- a) Accept it all (sections 1 to 16 and the appendix) once 43 and 44 are settled. **My pick**, when you've read the article-so-far page.
- b) Accept the sections you name; the rest wait.
- c) Not yet.

If you don't answer, nothing changes: your published text stays the master.
'''
TODO = '''## For you to do

> [!WARNING]
> One thing, when you're back.

- 🟠 Merge when you've looked at the pages: `gh pr merge 187 -R u-dont-existDOTcom/joel-articles --merge` ([the pull request](https://github.com/u-dont-existDOTcom/joel-articles/pull/187)). It has the overnight run and today's changes.
'''
NEW_DECIDED = '''- 🟢 2026-10-17 13:11 UTC, 39: "i'd say it's the practical logistical foundation that gets built once the architects can work well together, does that work?" It does: it says the container is built once the people building it can work together, which is section 16's order, so the two sections agree. In section 4, after "The first three parts are the inside of the container, and this container is what gives those a stable place to manifest.": "It's the practical logistical foundation that gets built once the architects can work well together." ("I'd say" dropped; "the architects" fits the house diagram above it.) Human with the paragraph before (%(s4a)s) and after (%(s4b)s); section 4 100%% Human (%(s4)s).
- 🟢 13:11, 40 a: "so much is taken care of by" stays. And your question, "so "often" is an ai tell?": partly. One word at a time: your sentence with "often" added and nothing else changed reads AI (0.71, %(q1)s), but the AI wording with its "often" taken out still reads AI (0.72, %(q2)s). So "often" was enough to tip that sentence, and the rest of the other wording's problem was the generic "things go through X and Y, alongside Z". It fits the hedging pattern you named: a general claim softened by a frequency word, where yours commits to what you saw.
- 🟢 13:11, 41 a: the reading list's breaks stay. And your "we need rules that are more flexible depending on the style of the article needed": each article now has a style profile (its register, which kinds of break suit it, whether list entries need one, and its exclamation range, measured from the article). In a formal article a reaction or an exclamation no longer counts as a break, and list entries skip the break rule.
- 🟢 13:11, 42: your lines are in ("And whether communal showers feel liberating, or make you start looking at studio apartments! No manifesto is going to tell you any of that!" and "Look before you leap. It will really save you some time & money.", which stays its own short paragraph where the land line was). Section 16 is in the article: every changed paragraph Human (%(h7a)s, %(h7b)s), the whole section 100%% Human (%(s16)s). You're right about the three exclamations: section 16 ended 11 of its 66 sentences with "!", where sections 1 to 12 end 2 of 697 that way. The signal was there, and nothing checked the article's range: the new check fails more exclamations in four sentences than the article ever has (question 43 is about the rate). "Do those three things" was your published sentence, and so was "quietly"; the linter had exempted published wording that was still in the article, so neither was judged. Now it judges published wording like new wording, fails a count pointing back at the advice, and fails "quietly" unless it's how a sound or a movement was made. And you're right about Emulate's voice: its exclamations and reactions now have to stay inside the article's range like mine.
- 🟢 13:11, section 16's opening: "quietly" is out ("That sounds kind of weird when somebody else is paying the tax bill."). Human alone (%(h3)s).
- 🟢 13:11, section 15's "All is not well in paradise": "public advocacy for homosexuality", without quotes, and the financing clause is out. A cold read paused at "apology" twice (two rounds), and my notes only listed it; the pause tally now needs a fix or a reason for each repeated pause, and a list doesn't count. Human alone (%(p15a)s).
- 🟢 13:11, section 15's Black Tax paragraph: "This is also" is back. The meaning check had called "It" the same as your "This"; it now marks that as a shift, and the linter fails it. The same check found two more: section 15's "This is the most joking culture" (your published "This") and section 1's "That's the sort of thing" (your published "These are the questions"), both back. Human alone (%(p15b)s, %(p15c)s, %(s1p)s); sections 15 (%(s15)s) and 1 (%(s1)s) 100%% Human.
- 🟢 13:11, the Zapatista paragraph: your sentence is in: "I understand the motivation to negotiate like that, but I think it's not a full solution either." I'd added "I like that." as the paragraph's pause, and the meaning check let it through because it was told a short reaction is there on purpose. A pause can't state an opinion you didn't give now; the check calls it an addition, and the linter fails it. Human alone (%(p15d)s).
- 🟢 13:11, the sweep of your "quietly" rule: section 8's "Older kids can't be allowed to boss the younger ones around there." without it. Human with either neighbor (%(s8p)s); section 8 100%% Human (%(s8)s).
- 🟢 13:11, the PsyPost study and your screenshot: in section 12 (question 44).
- 🟢 13:11: "you said to read stuff before i merge so i didn't merge, i assume that was right?" Yes. It's still waiting for you, now with today's changes too.
'''
vals = {'p2': L('S12v14-P2'), 's12': L('S12v14'), 's4a': L('S4v114-container+prev'), 's4b': L('S4v114-container+next'),
        's4': L('S4v114'), 'q1': L('Q40-c-plus-often'), 'q2': L('Q40-g-minus-often'), 'h7a': L('S16v28-H3P7+prev'),
        'h7b': L('S16v28-H3P7+next'), 's16': L('S16v28'), 'h3': L('S16v28-H1P3'), 'p15a': L('S15v13-H2P2'),
        'p15b': L('S15v13-H3P3'), 'p15c': L('S15v13-H1P3'), 's1p': L('S1sw-EastWind'), 's15': L('S15v13'), 's1': L('S1sw'),
        'p15d': L('S15v13-H3P5'), 's8p': L('S8v30-safeguards+prev'), 's8': L('S8v30')}
a, b = page.index('## Open questions'), page.index('## For you to do')
c, d = b, page.index('## Decided')
dec_body_start = page.index('> Answered, with what I did.', d)
dec_body_start = page.index('\n', dec_body_start) + 1
rest = page[dec_body_start:]
rest = rest.lstrip('\n')
coming = rest.index('## Coming up')
decided_old, coming_part = rest[:coming], rest[coming:]
coming_part = re.sub(r'- 🔵 Section 16, "Practice Comes Before Property".*?\n', '', coming_part)
coming_part = coming_part.replace('- 🔵 Image 7:', '- 🔵 When you accept (question 45): the humanized article becomes the registered master, with a record of the change.\n- 🔵 Image 7:')
new = (HEAD + page[head_end:a] + OPEN % vals + '\n' + TODO + '\n## Decided\n\n> [!TIP]\n> Answered, with what I did.\n\n' +
       NEW_DECIDED % vals + decided_old + coming_part)
(C / 'OWNER-QUESTIONS.md').write_text(new, encoding='utf-8')
print('wrote OWNER-QUESTIONS.md', len(new))
