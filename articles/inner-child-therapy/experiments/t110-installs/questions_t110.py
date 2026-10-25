#!/usr/bin/env python3
"""Turn 110's questions-page update: his message of 2026-10-25 17:26 UTC goes to Decided (Pink settled; GPT's review
sent), and 107 replaces 106: the review sheet, now only the changes GPT's review and mine both recommend, in place in the
whole guide. Every open item says what it's about (E257, Inner Child) and every file it points to is a page link."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
P = ROOT / 'OWNER-QUESTIONS.md'
B = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/'
SHEET = 'https://claude.ai/artifact/LTEDB18wTYzuUkgobzbUrn'
s = P.read_text(encoding='utf-8')


def rep(a, b):
    global s
    assert s.count(a) == 1, a[:80]
    s = s.replace(a, b)


rep('Last updated 2026-10-25 (turns 82 to 109). **Open questions: 106.** For you to do: merge pull request #246.',
    'Last updated 2026-10-25 (turns 82 to 110). **Open questions: 107.** For you to do: merge pull request #246.')
rep('after a turn by your other account (turns 100 to 109)', 'after a turn by your other account (turns 100 to 110)')

q = f'''### 🟣 107. The review sheet: only the changes GPT's review and mine both recommend (turn 110)

Everything to decide is on [the review sheet]({SHEET}), now the whole guide with each change in place: Approve, Reject or Revise on each, and a box for each question. When you're done, press "Save / send", then "Copy my answers", and paste them into the chat from either account. The sheet's file is [REVIEW.html]({B}t110-review/REVIEW.html) (download it and open it in a browser if the link doesn't open from your other account). Nothing in the article changes until you approve.

- **Two sections in a new order.** Hear the Guard First keeps your question, what the part might say and your reply "Tell me what you remember, I'm listening." together, in your own order from before turn 109. Before You Tell the Hardest Stuff puts your two danger lines back after the dream line they limit. Both read Human in Pangram as they'd read ([the checks]({B}t110-api/API-CHECKS.md)).
- **Ten cuts and three small wording changes**, among them your line about your son (your answer of 2026-10-02) and GPT's wording for "I'd keep whatever you feel around them".
- **Three questions:** what "most often", "A lot of people find" and "Some people find" are based on. A few words each, no story needed.

GPT's review and mine, card by card: [AGREED.md]({B}t110-review/AGREED.md). Everything else on the turn-109 sheet, both of us would leave as it is.

'''
i = s.index('### 🟣 106. The review sheet: the new shapes, your friend Pink, and the point-of-view read (turn 109)')
j = s.index('## For you to do (no decision needed)')
s = s[:i] + q + s[j:]

rep('### 🟠 Merge pull request #246 (turn 109)\n\nTurn 109: https://github.com/u-dont-existDOTcom/joel-articles/pull/246.',
    '### 🟠 Merge pull request #246 (turns 109 and 110)\n\nTurns 109 and 110: https://github.com/u-dont-existDOTcom/joel-articles/pull/246.')
rep('### 🔵 The two temporary Substack drafts: keep them for the next whole-article check (turn 109)',
    '### 🔵 The two temporary Substack drafts: keep them for the next whole-article check (turn 110)')

decided = f'''### 🟢 106, 2026-10-25 17:26 UTC

Your message (turn 110; [JOEL-20261025-1726.md]({B}t110-answers/JOEL-20261025-1726.md)), with GPT's review of the turn-109 sheet ([GPT-REVIEW-20261025.md]({B}t110-answers/GPT-REVIEW-20261025.md)).

- **Your friend Pink, "don't worry, "Pink" is not her real name":** your paragraph in How This Relates to IFS stays as you wrote it.
- **GPT's review, "prob no point until you can agree":** I took its advice on every card ([AGREED.md]({B}t110-review/AGREED.md)), and the sheet now has only the changes we both recommend (question 107 above). Its two section rearrangements read Human as they'd read, and a fresh reader's cold read added two small fixes to Hear the Guard First ([COLD-READ.md]({B}t110-review/COLD-READ.md)).

'''
k = s.index('### 🟢 104 and 105, 2026-10-25 14:20 UTC')
s = s[:k] + decided + s[k:]
P.write_text(s, encoding='utf-8')
print('ok')
