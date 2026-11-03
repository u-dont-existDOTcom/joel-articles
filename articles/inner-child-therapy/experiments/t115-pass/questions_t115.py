#!/usr/bin/env python3
"""Turn 115's questions-page update: round 8 read and recorded, his question about the below-High windows answered, the pass
in the docx for him, and pull request #252 merged. No question is open; the docx is his to-do. Every open item says what
it's about (E257, Inner Child), and every file it points to is a page link.
  questions_t115.py"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
P = ROOT / 'OWNER-QUESTIONS.md'
B = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/'
DOCX = B + 't115-docx/inner-child-spots-round8.docx'
s = P.read_text(encoding='utf-8')


def rep(a, b):
    global s
    assert s.count(a) == 1, a[:80]
    s = s.replace(a, b)


rep('Last updated 2026-10-26 (turns 82 to 114). **Open questions: none.** For you to do: check the two drafts in Pangram '
    'and send me the two links, and merge pull request #252.',
    'Last updated 2026-10-26 (turns 82 to 115). **Open questions: none.** For you to do: go through the docx of round 8\'s '
    'spots and send it back.')
rep('after a turn by your other account (turns 100 to 114)', 'after a turn by your other account (turns 100 to 115)')

i = s.index('### 🟠 Round 8: check the two drafts in Pangram and send me the two links (turn 114)')
j = s.index('### 🔵 The two temporary Substack drafts')
todo = ('### 🟠 The docx: decide on my pass and work on the shaded spots, then send it back (turn 115)\n\n'
        'The [docx](%s) is the whole guide as round 8 read it. My pass is in it as tracked changes: accept or reject each one '
        '(one you leave as it is, I\'ll take as accepted). The shaded spots are what round 8 read below Human, high that the '
        'pass didn\'t change, most of them your words, each with a comment giving its reading and round 6\'s. Track Changes is '
        'on, so whatever you type shows as yours. Send it back in chat, and I\'ll put everything in for round 9. '
        '([PASS.md](%st115-pass/PASS.md) says what the pass did and why.)\n\n' % (DOCX, B))
s = s[:i] + todo + s[j:]
rep('### 🔵 The two temporary Substack drafts: keep them until round 8 is read (turn 114)\n\n'
    '"Inner Child, draft A (temp, delete after)" and "Inner Child, draft B (temp, delete after)" hold round 8, the guide as '
    'installed.',
    '### 🔵 The two temporary Substack drafts: keep them for round 9 (turn 115)\n\n'
    '"Inner Child, draft A (temp, delete after)" and "Inner Child, draft B (temp, delete after)" still hold round 8. Round 9, '
    'with the pass and your changes from the docx, goes into them next.')

decided = f'''### 🟢 Round 8 and the pass, 2026-10-26 12:24 UTC

Your message ([JOEL-20261026-1224.md]({B}t115-answers/JOEL-20261026-1224.md)) with round 8's two links. You merged pull request #252.

- **Round 8:** both halves Human Written, high (0.37% and 0.21% AI), with four AI windows, all Low, and 89 more windows below Human, high ([ROUND8.md]({B}t115-results/ROUND8.md), every one listed in [WINDOWS.md]({B}t115-results/WINDOWS.md)).
- **"have you been saving those parts? i hope you haven't been treating anything that passes the same?":** every window was saved in rounds 1, 2, 6 and 8, but rounds 3 to 5 wrote down only their AI windows. And yes, a Human window counted as passing whatever its confidence. All four of round 8's AI windows were on words round 6 had read below High, so your point holds. Lesson E276 (Inner Child) makes the below-High windows part of every read and every pass.
- **"try to get it all high conf human with one more pass, then whatever remains ... in a docx":** 12 changes in my own paragraphs, taking in all four AI windows and seven of the eight Low ones, each reviewed by three fresh readers and the five rewordings by the owner-delivery gate ([PASS.md]({B}t115-pass/PASS.md)). They're in the docx as tracked changes for you to decide; the rest is shaded there.

'''
k = s.index('### 🟢 110, 2026-10-26 00:52 UTC')
s = s[:k] + decided + s[k:]
i = s.index('### 🔵 Next: round 8\'s windows, then Untangling the Belonging Bargains (turn 114)')
j = s.index('### 🔵 Next\n')
s = s[:i] + ('### 🔵 Next: your docx, then round 9 (turn 115)\n\n'
             'When the docx is back, I put in what you accepted and wrote, run the gate on any new words of mine, and paste round '
             '9 into the two drafts. Untangling the Belonging Bargains\' first paragraph read Human in round 8, with two Medium '
             'windows on your approved version, so it is in the docx with the rest.\n\n') + s[j:]
P.write_text(s, encoding='utf-8')
print('ok')
