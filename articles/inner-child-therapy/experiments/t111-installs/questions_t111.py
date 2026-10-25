#!/usr/bin/env python3
"""Turn 111's questions-page update: his answers of 2026-10-25 20:08 UTC from the review sheet go to Decided (107), and 108
opens: the one approved cut that turned its paragraph AI alone, and whether Just Like Me's second paragraph is meant to be
his sentence alone. Every open item says what it's about (E257, Inner Child), with my pick, and every file it points to is
a page link."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
P = ROOT / 'OWNER-QUESTIONS.md'
B = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/'
s = P.read_text(encoding='utf-8')
R = {}
for f in sorted((ROOT / 'experiments' / 't111-api').glob('API-RESULTS-*.jsonl')):
    for line in f.read_text(encoding='utf-8').splitlines():
        r = json.loads(line)
        R[r['name']] = r['dashboard_link']
human = sum(1 for f in ['API-RESULTS-1.jsonl'] for line in (ROOT / 'experiments' / 't111-api' / f).read_text(encoding='utf-8').splitlines()
            if json.loads(line)['headline'] == 'Human Written')


def rep(a, b):
    global s
    assert s.count(a) == 1, a[:80]
    s = s.replace(a, b)


rep('Last updated 2026-10-25 (turns 82 to 110). **Open questions: 107.** For you to do: merge pull request #246.',
    'Last updated 2026-10-25 (turns 82 to 111). **Open questions: 108.** For you to do: merge the turn-111 pull request.')
rep('after a turn by your other account (turns 100 to 110)', 'after a turn by your other account (turns 100 to 111)')

q = f'''### 🟣 108. One cut that turned its paragraph AI, and Just Like Me's second paragraph (turn 111)

Everything else from your answers on the review sheet is in, and {human} of the 14 paragraphs it changed read Human alone ([the checks]({B}t111-api/API-CHECKS.md)).

- **108.1, Borrow Love's third paragraph.** After the cut you approved of "The quest for self-knowledge is a life's journey, but you don't have to wait for your life to finish to figure out your best next move.", the paragraph read [100% AI alone]({R['t111_c4_borrowlove']}). With the line it read [Human]({R['t111_c4_before']}). GPT had said the line makes a point of its own: you can act before you fully know yourself.
  - **A (my pick):** put the line back. It carries the paragraph and its point.
  - **B:** keep the cut, and I find another fix after the next whole-article check shows how the paragraph reads in its section.
  - **C:** your own version of the line.
- **108.2, Just Like Me's second paragraph** is now your sentence alone, with the tonglen link it had. So "normal breathing is fine" and "Whoever hurt you might come to mind, too." went out along with the forgiving line. Where that line came from: [TRACES.md]({B}t111-answers/TRACES.md).
  - **A (my pick):** keep it as you wrote it.
  - **B:** you meant to replace only the first sentence, so the other two come back.

'''
i = s.index("### 🟣 107. The review sheet: only the changes GPT's review and mine both recommend (turn 110)")
j = s.index('## For you to do (no decision needed)')
s = s[:i] + q + s[j:]

i = s.index('### 🟠 Merge pull request #246 (turns 109 and 110)')
j = s.index('### 🔵 The two temporary Substack drafts')
s = s[:i] + ('### 🟠 Merge the pull request for turn 111\n\nTurn 111: the lane\'s [open pull request](https://github.com/u-dont-existDOTcom/joel-articles/pulls?q=is%3Apr+is%3Aopen+head%3Ahandoff%2Fclaude-dangerous-adult-20260924-1631). '
             'Open it, then click "Merge pull request" and "Confirm merge". That takes about a minute, and the page then says "Merged". (You merged #246, turns 109 and 110.)\n\n') + s[j:]
rep('### 🔵 The two temporary Substack drafts: keep them for the next whole-article check (turn 110)',
    '### 🔵 The two temporary Substack drafts: keep them for the next whole-article check (turn 111)')

decided = f'''### 🟢 107, 2026-10-25 20:08 UTC

Your answers from the review sheet ([ANSWERS-20261025-2008.json]({B}t111-answers/ANSWERS-20261025-2008.json)), and your question of 20:14 UTC about the reshape ([JOEL-20261025-2014.md]({B}t111-answers/JOEL-20261025-2014.md)). You merged pull request #246.

- **Hear the Guard First (S1):** in, in the agreed order.
- **Before You Tell the Hardest Stuff (S3):** in your version, "So I'd ask this person".
- **The cuts:** nine in. The tenth, the blessing line, stays with your sentence after it ("If it's more distributed ..."), and your cut of "Say they're the one who always remembers your appointments." is in.
- **The wording changes:** your son line and the "keep what you feel around them in mind" wording are in. Just Like Me's second paragraph is your sentence, and your cut of "Some of them make it worse ... 😅" is in. How both of those lines got in: [TRACES.md]({B}t111-answers/TRACES.md).
- **The questions:** "Once a truce is made, we can begin to let down our defenses." is in, for "What people most often say helped". "A lot of people find" stays, since its basis is people you know. "Some people find" stays, since it's what people in Re-evaluation Counseling say especially, and common therapy advice.
- **Your question, "you gave up on reshaping everything ... was that because gpt disagreed?":** no. GPT agreed with the shape ("The improvement is real") and objected only where the reshape had pulled a line away from what it belongs to. Those two fixes are what you approved. The next five sections come to you as proposals first, since GPT hadn't seen them ([AGREED.md]({B}t110-review/AGREED.md)).

'''
k = s.index('### 🟢 106, 2026-10-25 17:26 UTC')
s = s[:k] + decided + s[k:]
P.write_text(s, encoding='utf-8')
print('ok', human)
