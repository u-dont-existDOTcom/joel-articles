#!/usr/bin/env python3
"""Turn 106's questions-page update: 102 moves to Decided with Joel's answers of 2026-10-24 22:55 UTC, and 103 opens. Every
open item says what it's about, never only an earlier question's number (E257 (Inner Child); questions_page.py checks it)."""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
P = ROOT / 'OWNER-QUESTIONS.md'
G = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments'
H = 'https://www.pangram.com/history/'

s = P.read_text(encoding='utf-8')
old_head = 'Last updated 2026-10-24 (turns 82 to 105). **Open questions: 102.** For you to do: merge pull request #233.'
assert old_head in s
s = s.replace(old_head, 'Last updated 2026-10-24 (turns 82 to 106). **Open questions: 103.** For you to do: merge pull request #233.')
s = s.replace('after a turn by your other account (turns 100 to 105)', 'after a turn by your other account (turns 100 to 106)')

i = s.index('### 🟣 102. ')
j = s.index('## For you to do (no decision needed)')
q102_asked = s[i:j].rstrip('\n').replace('### 🟣 102. ', '#### 102. ', 1)

q103 = f'''### 🟣 103. What the checks of your picks found (turn 106)

Every check is on [this turn's API page]({G}/t106-api/API-CHECKS.md). Your picks and your five sections are in, and these four are what's left.

- **103.1 My Journey's paragraph on spiritual bypassing** ("I think most people who chase spiritual freedom ..."). It reads AI on its own [before your cut]({H}ad0fb776-b643-4ecb-9754-b0a947fdfc9b) and [after it]({H}23800590-b449-4804-9dac-4b17d8926d18), so the cut of "It doesn't mean you're stupid or crazy." isn't what does it. In its section it read [Human before the cut]({H}9048981d-8ee6-47a5-a7b0-59a115f929bf) and [0.26% AI after it]({H}b6e45715-fbfe-4847-9993-7253918dc5d9), with no AI window.
  - **A (my pick):** keep your cut. The section shows no AI window, and round 6 reads it in the whole article.
  - **B:** put the line back.
- **103.2 Not Every Hero Wears A Cape, now that "Make It Intentional" heads its last two paragraphs.** Its first three paragraphs read [2.65% AI with no AI window]({H}5105656f-4f96-45af-b7b5-5bab9fd6d771), and Make It Intentional reads [Human]({H}4df175bf-a64a-4b86-86df-dc14061f7474). The whole section read [Human]({H}f034ed48-3ce7-4059-a6ec-9d857ccb28e6) without the heading.
  - **A (my pick):** keep the heading, since there's no AI window; round 6 reads it in context.
  - **B:** take the heading out.
- **103.3 Your acacia sentence.** It's in, and its paragraph reads [Human]({H}23b42f15-b667-4516-8ae7-881b8b98b635): "I also learned that mixing acacia confusa with mimosa hostilis is very destabilizing and challenging, but excellent if you want to know how it feels to be painfully autistic + schizo!" One thing to weigh: "schizo" is a slur to many people with schizophrenia, and autistic readers may hear "painfully autistic" as the joke being on them.
  - **A:** keep it as you wrote it.
  - **B (my pick):** your words for the punchline.
- **103.4 A typo in your When to Change the Strategy.** "But do notice if it progress is stagnating." I left it as you wrote it.
  - **A (my pick):** "But do notice if progress is stagnating."
  - **B:** leave it.

'''
s = s[:i] + q103 + s[j:]

s = s.replace('### 🟠 Merge pull request #233 (turns 104 and 105)\n\nTurns 104 and 105: https://github.com/u-dont-existDOTcom/joel-articles/pull/233.',
              '### 🟠 Merge pull request #233 (turns 104 to 106)\n\nTurns 104 to 106: https://github.com/u-dont-existDOTcom/joel-articles/pull/233.')
assert 'turns 104 to 106' in s
old_r6 = 'It waits for your answers to 102, so one check covers turns 100 to 105 and whatever those answers change.'
assert old_r6 in s
s = s.replace(old_r6, 'Your picks from the ideas page are in, so it comes next: one whole-article check through the two temporary Substack drafts, covering everything since round 5.')

decided = f'''### 🟢 102, 2026-10-24 22:55 UTC

Your message (turn 106; `experiments/t106-answers/JOEL-20261024-2255.md`).

- **The questions page:** fixed for good. The page tool now refuses an open question or a to-do item that points to an earlier question by its number alone, like "your 100.6", so each one says what it's about (E257, Inner Child; `tools/questions_page.py`, with a test). Question 103 is written that way.
- **102.1:** your When to Change the Strategy is in, word for word. 98.7's own paragraph is gone, and its point is your P3's texting example. What your five rewrites teach, and how my picks did against your answers, is in [LESSONS.md]({G}/t106-answers/LESSONS.md): 28 of 33 and 32 of 39 matched, and 8 of my 12 misses were lines of yours I kept only because they were yours (E258, Inner Child).
- **102.2 A:** d3 is in.
- **102.3:** your You Don't Need an Inner Monologue is in, word for word, and so are your crisis stretch, First Social Connections, Done Right, and Speak Toward What You Are Building, without its last paragraph. One change to your characters: your Forbes link had a space between "]" and "(", which would have shown the brackets and the address, so it's a link now.
- **102.4:** your picks are in, and The Chicken-and-Egg Problem keeps its heading (e1 b). Your rewrites changed four of them: 98.7's move (e17) went with 98.7, the pain paragraph (e22) has nothing to move since your h26 cuts it, and h6 and h35 are in your new paragraphs as you wrote them. "Ask What Kind of Company They Want" (e30) now heads one paragraph, since you took out the last one. The paragraph break you said I could try (e5) is in: your section read Human through the API [as you wrote it]({H}6cf7d182-2fb4-42d4-80da-3da81329a123) and [with the break]({H}35250e68-04b0-4eb5-8aee-70764bd81362). The h22 cut has your "These are just", and h23 has your merged sentence. Of 34 checks, 29 read Human. Of the other five, three are in 103, You Belong Everywhere and Nowhere reads [0.0137% AI with no AI window]({H}4ee5effc-70d2-473c-9d01-3b00d7b42840), which Pangram calls Human Written, and one is fixed:
  - Timing Is Individual's second paragraph (mine) read [48% AI with your line]({H}c9ded038-bbf2-4b44-b8aa-5b49a31442f4) and [51% without it]({H}7c606adb-0eb5-4440-9de2-82634becc011), so your cut wasn't the cause. After the tell panel, my two drafts read Human in the section and AI alone, and the second writer's (Codex's) reads [Human alone]({H}49c729e5-d393-4d2c-94f3-f3c0eaafc1b7) and [in the section]({H}bf9b0e54-369e-49ad-b049-1f08aea91a62). It's in ([try by try]({G}/t106-tries/REVIEWS.md)).
- **"saving all our trials and errors":** yes. Every Pangram check is in the ledger with my prediction before it and the result after, each turn's drafts, panels and checks are in its own folder, your messages are saved word for word, and the lessons are in the gate. [LESSONS.md]({G}/t106-answers/LESSONS.md) adds how my picks did against your answers, so my misses are on record too.
- **ENGAGING.md:** it's with this turn's files.

<details><summary>102 as it was asked</summary>

{q102_asked}

</details>

'''
k = s.index('### 🟢 101, 2026-10-24 18:40 UTC')
s = s[:k] + decided + s[k:]
P.write_text(s, encoding='utf-8')
print('ok')
