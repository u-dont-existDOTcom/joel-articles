#!/usr/bin/env python3
"""Turn 114's questions-page update: his answers of 2026-10-26 00:52 UTC go to Decided (110: every card approved, Q-me "you"),
no question stays open, and round 8, the installed guide in the two temporary drafts, is his to check. Every open item says
what it's about (E257, Inner Child), and every file it points to is a page link.
  questions_t114.py"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
P = ROOT / 'OWNER-QUESTIONS.md'
B = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/'
PR = 'pull request #252'
PR_LINK = '[pull request #252](https://github.com/u-dont-existDOTcom/joel-articles/pull/252)'
s = P.read_text(encoding='utf-8')


def rep(a, b):
    global s
    assert s.count(a) == 1, a[:80]
    s = s.replace(a, b)


rep('Last updated 2026-10-26 (turns 82 to 113). **Open questions: 110.** For you to do: give GPT the review sheet, and '
    'merge pull request #252.',
    'Last updated 2026-10-26 (turns 82 to 114). **Open questions: none.** For you to do: check the two drafts in Pangram '
    'and send me the two links, and merge %s.' % PR)
rep('after a turn by your other account (turns 100 to 113)', 'after a turn by your other account (turns 100 to 114)')

i = s.index('### 🟣 110. The review sheet: case headings in 8 sections')
j = s.index('## For you to do (no decision needed)')
s = s[:i] + 'None right now.\n\n' + s[j:]

i = s.index('### 🟠 Merge pull request #252 (turn 113)')
j = s.index('### 🔵 The two temporary Substack drafts')
todo = ('### 🟠 Round 8: check the two drafts in Pangram and send me the two links (turn 114)\n\n'
        'The two temporary Substack drafts now hold the guide as installed, with everything you approved from the review sheet, '
        'so the free check reads the new headings and splits in their real places. In your Brave, open '
        '[draft A](https://ibogaqueen.substack.com/publish/post/221982879) and '
        '[draft B](https://ibogaqueen.substack.com/publish/post/221983135), click Preview, then "Paid subscriber view" at the top. '
        'Click the green label next to the author\'s name, then "View Full Analysis", and send me each result page\'s link '
        '("Copy shareable link to result"). The label\'s word isn\'t the result; the result page\'s windows are what I read. '
        'That takes about two minutes.\n\n'
        '### 🟠 Merge %s (turns 113 and 114)\n\n'
        'The lane\'s %s now holds turn 113\'s review sheet and turn 114\'s install. Open it, then click "Merge pull request" and '
        '"Confirm merge". That takes about a minute, and the page then says "Merged". (You merged #250, turn 112.)\n\n' % (PR, PR_LINK))
s = s[:i] + todo + s[j:]
rep('### 🔵 The two temporary Substack drafts: keep them for the next check (turn 113)\n\n'
    '"Inner Child, draft A (temp, delete after)" and "Inner Child, draft B (temp, delete after)" still hold round 7\'s text. '
    'The next check puts in what you approve from the review sheet.',
    '### 🔵 The two temporary Substack drafts: keep them until round 8 is read (turn 114)\n\n'
    '"Inner Child, draft A (temp, delete after)" and "Inner Child, draft B (temp, delete after)" hold round 8, the guide as '
    'installed.')

decided = f'''### 🟢 110, 2026-10-26 00:52 UTC

Your message ([JOEL-20261026-0053.md]({B}t114-answers/JOEL-20261026-0053.md)), "oh yeah i didn't need gpt that was easy, it's way easier to read now", with your answers from the review sheet ([ANSWERS-20261026-0052.json]({B}t114-answers/ANSWERS-20261026-0052.json)).

- **All eleven cards approved:** every section is in as the sheet showed it, word for word: the 36 case headings, the splits, the one sentence moved up in Start With Whatever Showed Up, and your 109 A ([apply_t114.py]({B}t114-installs/apply_t114.py), which checks that the guide without its notes is exactly the sheet's version).
- **Q-me, "you":** the line now reads "The test is whether the relationship makes you more grounded, truthful, and free."
- **GPT's review:** not needed, as you said.

'''
k = s.index('### 🟢 109 and round 7, 2026-10-25 22:38 UTC')
s = s[:k] + decided + s[k:]
i = s.index('### 🔵 Next: GPT\'s review, then a sheet of what we both recommend (turn 113)')
j = s.index('### 🔵 Next\n')
s = s[:i] + ('### 🔵 Next: round 8\'s windows, then Untangling the Belonging Bargains (turn 114)\n\n'
             'When your two result links are in, I read each half\'s windows, and fix what a window shows, a diagnosed draft at a '
             'time. Then the first paragraph of Untangling the Belonging Bargains, which read AI alone.\n\n') + s[j:]
P.write_text(s, encoding='utf-8')
print('ok')
