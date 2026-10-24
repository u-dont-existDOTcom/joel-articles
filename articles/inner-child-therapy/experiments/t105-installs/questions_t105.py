#!/usr/bin/env python3
"""Turn 105's questions-page update: 101 moves to Decided with Joel's answer of 2026-10-24 18:40 UTC, and 102 opens."""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
P = ROOT / 'OWNER-QUESTIONS.md'
G = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments'

s = P.read_text(encoding='utf-8')

old_head = 'Last updated 2026-10-24 (turns 82 to 104). **Open questions: 101.** For you to do: merge pull request #233.'
assert old_head in s
s = s.replace(old_head, 'Last updated 2026-10-24 (turns 82 to 105). **Open questions: 102.** For you to do: merge pull request #233.')

i = s.index('### 🟣 101. What the tell panel and Pangram showed (turn 104)')
j = s.index('## For you to do (no decision needed)')
q101 = s[i:j].rstrip('\n')
q101_asked = q101.replace('### 🟣 101. What the tell panel and Pangram showed (turn 104)', '#### 101. What the tell panel and Pangram showed (turn 104)', 1)
m = re.search(r'- \*\*101\.4 Four sections with Low windows \(your 100\.6, still open\)\.\*\* (.*?)\n  - \*\*A \(my pick\):\*\* (.*?)\n  - \*\*B:\*\* (.*?)$', q101, flags=re.S)
assert m, '101.4'
sections, a4, b4 = m.group(1), m.group(2), m.group(3)

q102 = f'''### 🟣 102. 98.7, your 98.2, four sections, and ideas for the rest (turn 105)

How I fix a paragraph now is under 101 in Decided ([try by try]({G}/t105-tries/REVIEWS.md); [every check]({G}/t105-api/API-CHECKS.md)).

- **102.1 98.7, When to Change the Strategy P5 (mine).** All six tries are used. Codex's rewrite from the readers' notes read [70% AI](https://www.pangram.com/history/48f0fd74-ff73-47e1-ac6c-8d222700dccc). d5, the draft that read [100% Human alone](https://www.pangram.com/history/64778cfd-d4f4-482f-94ee-0735b6110c68), read [100% AI](https://www.pangram.com/history/33d1a7d3-ca17-4331-b566-85743cc55238) once its "I wouldn't try going deeper next time" and "I'd guess" were said flat. So without the asides it reads as an AI coach to Pangram, and with them it has the careful voice you called AI in 97.8 ([the readers' notes]({G}/t104-panel/98_7-current/PANEL.md)). In the same check your own lines in P4 read High Human ([P3 to P5](https://www.pangram.com/history/62b492c4-0820-45bf-bf09-9138d56edbfa)).
  - **A (my pick):** cut it. The Chicken-and-Egg Problem's ending carries the point about doing it in your life ("The cushion was practice for it."), and P2 here already says more of the same isn't the fix.
  - **B:** d5 in, and round 6 reads it in the whole article.
  - **C:** your words, or GPT's, the way 97.8 went.
- **102.2 98.2, your Not Every Hero Wears A Cape P5.** My d3 reads [Human alone](https://www.pangram.com/history/80cf31a3-87e1-4620-83c1-154549c287c0), and the whole section reads [Human](https://www.pangram.com/history/f034ed48-3ce7-4059-a6ec-9d857ccb28e6) with it: "After the day, look at what actually happened. Say you did the Protector action(s) and you don't feel any better, or you feel worse. Standing up for yourself can do that at first. Not doing it is harder to figure out. Fear is the first guess. But did you know how to do it, and why? Were you worn out? Maybe whoever said they'd help couldn't make it. 🤗" The causes are questions now, and "information to learn from", "Healing is nonlinear" and "Hey, we've all been there." are out, since all three readers called them stock lines ([record]({G}/t104-panel/98_2-current/PANEL.md)). Your emoji stays.
  - **A (my pick):** d3 in.
  - **B:** keep yours as it is.
- **102.3 Four sections with Low windows (your 100.6, still open).** {sections}
  - **A (my pick):** {a4}
  - **B:** {b4}
- **102.4 Ideas for the other sections, for GPT.** [The ideas page]({G}/t105-readers-edit/IDEAS.md) has two fresh readers' passes over the whole article, with the way Lucia Capacchione's book reads in mind ([the comparison]({G}/t105-readers-edit/ENGAGING.md)): a reader's edit (headings, moves and cuts, so a reader has less to work through at once) and a hedge read (the may, might and maybe lines a reader doesn't need, her biggest difference from this article). I checked each one against the article and your earlier answers, and each has my pick. Nothing is in yet or checked in Pangram.
  - **A (my pick):** send the page to GPT, then reply "102.4: your picks", or with the numbers you'd change. Each change gets its checks before it goes in.
  - **B:** leave the other sections for round 6.

'''
s = s[:i] + q102 + s[j:]

s = s.replace('### 🟠 Merge pull request #233 (turn 104)\n\nTurn 104: https://github.com/u-dont-existDOTcom/joel-articles/pull/233.',
              '### 🟠 Merge pull request #233 (turns 104 and 105)\n\nTurns 104 and 105: https://github.com/u-dont-existDOTcom/joel-articles/pull/233.')
assert 'turns 104 and 105' in s
old_r6 = 'It waits for your answers to 101, so one check covers turns 100 to 104 and whatever those answers change.'
assert old_r6 in s
s = s.replace(old_r6, 'It waits for your answers to 102, so one check covers turns 100 to 105 and whatever those answers change.')

decided = f'''### 🟢 101, 2026-10-24 18:40 UTC

Your message (turn 105; `experiments/t105-answers/JOEL-20261024-1840.md`, with your readers' notes beside it as `READERS-20261024.txt`).

- **101.1:** GPT's paragraph is in, word for word, and in its stretch it reads [Human, 0.0000% AI](https://www.pangram.com/history/a1020230-e26e-4b94-b483-5497dc674885). You were right: your Haiku had listed the tells I said I couldn't find, and so had my own panel. What was going wrong:
  - I stopped at the guide's own instructions, as if a flag on one meant the instruction had to go. The readers were flagging how they were worded, so the content stays and the wording changes.
  - My drafts kept my shape: a careful "I'd ..." aside around each instruction, the cases lined up in parallel, and a closing line. GPT says each instruction plainly, starts from one case ("Say you keep coming back from trips ..."), and ends on a plain fact.
  - I took readers' "human" picks on my own phrases as human tells, like "I'd count the milder stuff too", which you hear as AI.
  - My panel's summary matched quotes only, so Haiku's "Even, tidy rhythm" never reached a draft.

  The fixes are E256 (Inner Child) in the gate. The panel now asks about each paragraph as a whole, and after two failed drafts of mine, Codex writes the next one from the readers' notes. It didn't crack 98.7, though (102.1).
- **"do the others":** 102.1 and 102.2.
- **Lucia's book:** mostly yes, in a plain, warm way ([how it reads beside this article]({G}/t105-readers-edit/ENGAGING.md)). Her own story comes first, and you're doing an exercise within a page or two, with other people's drawings and letters as the examples. Her sentences are plain and sure of themselves: one in twenty-five has a hedge like may, might or sometimes, against one in five here. It isn't witty, and it comes back to the same method in every chapter.
- **"go thru all the other sections":** 102.4.

<details><summary>101 as it was asked</summary>

{q101_asked}

</details>

'''
k = s.index('### 🟢 100, 2026-10-23 23:21 UTC')
s = s[:k] + decided + s[k:]
P.write_text(s, encoding='utf-8')
print('ok')
