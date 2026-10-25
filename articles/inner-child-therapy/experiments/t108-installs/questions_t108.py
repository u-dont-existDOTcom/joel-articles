#!/usr/bin/env python3
"""Turn 108's questions-page update: round 6 and his message of 2026-10-25 12:39 UTC go to Decided, and 104 (a simpler
shape for the guide) and 105 (round 6's two windows) open. Every open item says what it's about (E257, Inner Child), every
file it points to is a page link (repo_links.py; no folder links), and every AI result has its check's link.
  questions_t108.py            the update (the pull request named generally)
  questions_t108.py --pr N     names pull request #N in the to-do item and the head line"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
P = ROOT / 'OWNER-QUESTIONS.md'
B = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/'
A6 = 'https://www.pangram.com/feed/41dfb451-494d-4a13-a76c-335d372dbd4a'
B6 = 'https://www.pangram.com/feed/64c71597-3987-48a7-8431-c8bdc70fddcc'
s = P.read_text(encoding='utf-8')

if '--pr' in sys.argv:
    n = sys.argv[sys.argv.index('--pr') + 1]
    assert n.isdigit()
    old = '### 🟠 Merge the pull request for turn 108'
    assert old in s, 'run the update first'
    s = s.replace(old, '### 🟠 Merge pull request #%s (turn 108)' % n)
    s = s.replace('Turn 108: the lane\'s [open pull request](https://github.com/u-dont-existDOTcom/joel-articles/pulls?q=is%3Apr+is%3Aopen+head%3Ahandoff%2Fclaude-dangerous-adult-20260924-1631).',
                  'Turn 108: https://github.com/u-dont-existDOTcom/joel-articles/pull/%s.' % n)
    s = s.replace('For you to do: merge the turn-108 pull request.', 'For you to do: merge pull request #%s.' % n)
    P.write_text(s, encoding='utf-8')
    print('named #' + n)
    sys.exit(0)

old_head = ('Last updated 2026-10-25 (turns 82 to 107). **Open questions: none.** For you to do: merge pull request #239, and send '
            'round 6\'s two result links.')
assert old_head in s
s = s.replace(old_head, 'Last updated 2026-10-25 (turns 82 to 108). **Open questions: 104, 105.** For you to do: merge the turn-108 pull request.')
old = 'after a turn by your other account (turns 100 to 107)'
assert old in s
s = s.replace(old, 'after a turn by your other account (turns 100 to 108)')

q = f'''### 🟣 104. A simpler shape for the guide, keeping its cases (turn 108)

You wrote that if you had written the guide yourself it would be "much simpler", and asked how it could read as engagingly as your own writing without losing the important complexities. [The density page]({B}t108-shape/DENSITY.md) counts the turns (but, if, or, maybe and the like): about 3.5 a paragraph here against about one in Lucia Capacchione's book, with four or more in 42% of the paragraphs here and in 4% of hers. Some of the densest sections are ones you rewrote yourself, like When to Change the Strategy, so it comes from the content, advice for many different cases, more than from the wording.

So my suggestion keeps every case and changes where it sits: the plain path first, as if nothing goes wrong, and then one situation a paragraph, the way your When to Change the Strategy gives each situation its own paragraph. A reader who's fine takes the first paragraph and moves on, and a reader who's stuck finds their case. [The worked example]({B}t108-shape/DEMO.md) does it to Hear the Guard First with every sentence kept word for word; only their order and the paragraph breaks change.

- **104.1 A (my pick):** do it section by section, the densest first. Each one comes to you beside what it was, checked alone and in its section, and where a section has nothing of yours in it (a story of yours, say, or your own verdict), I'll mark the place, since only you can add one.
- **104.1 B:** only the sections you pick from the density page.
- **104.1 C:** keep the shape as it is, and keep going line by line.

### 🟣 105. Round 6's two windows (turn 108)

Both halves read Human Written, [half A at 0.20% AI]({A6}) and [half B at 0.39% AI]({B6}), each with High confidence, and 18 of my 19 calls were right ([the round 6 page]({B}t108-results/ROUND6.md)). Your My Journey and your Not Every Hero paragraphs read Human inside the half, and so did every section you rewrote. Two windows are left, both on sentences of mine.

- **105.1 How This Relates to IFS, the end of its last paragraph.** "Some practitioners are gentle about it and walk you through the maze just fine. Others seem to leave people more split up than when they started. I wouldn't trust a model more just because there's a big institute behind it handing out certificates." read [Low, Low and Medium inside half B]({B6}), where round 5 had flagged the version before it. These are your guide's points from its IFS paragraph, in my words. Three fresh readers flagged nearly every sentence ([their notes]({B}t108-panel/ifs-p7/PANEL.md)), and the second writer's new version got the same notes ([its panel]({B}t108-panel/ifs-p7-codex1/PANEL.md)), so I didn't spend a check on it. What all of them miss is somebody's actual case: as written it's a summary, and the reason behind it is yours. Have you seen IFS done well, or seen someone come out of it more split up?
  - **A (my pick):** your words, a line or two of what you saw or why you say it. I fit them in and check the paragraph alone, in its section and in the next whole-article check.
  - **B:** end the paragraph at the maze, without the practitioner and institute lines.
  - **C:** leave it; half B reads Human Written as it is.
- **105.2 Use Childhood Photographs Gently, its first sentence.** The opener you picked in turn 95, "If picturing your little one feels fake, like you're just making it up, a real photo of you as a child can help, since there's no face or posture to invent.", read [Low inside half A]({A6}), right after the last line of One Intention in the Morning, One Review at Night. It's the first time, and the section read [Human through the API]({'https://www.pangram.com/history/4634e2ff-63e7-4e15-863d-90fcea18266c'}) in turn 106.
  - **A (my pick):** watch it in the next whole-article check before changing anything (gate E231).
  - **B:** your words for it.
  - **C:** I try a new version now.

'''
old_open = 'None right now. Round 6, below, needs two links from you.\n\n'
assert old_open in s
s = s.replace(old_open, q)

i = s.index('### 🟠 Merge pull request #239 (turn 107)')
j = s.index('### 🔵 The two temporary Substack drafts')
s = s[:i] + ('### 🟠 Merge the pull request for turn 108\n\nTurn 108: the lane\'s [open pull request](https://github.com/u-dont-existDOTcom/joel-articles/pulls?q=is%3Apr+is%3Aopen+head%3Ahandoff%2Fclaude-dangerous-adult-20260924-1631). '
             'Open it, then click "Merge pull request" and "Confirm merge". That takes about a minute, and the page then says "Merged". (You merged #239, turn 107.)\n\n') + s[j:]
old_d = '### 🔵 The two temporary Substack drafts: keep them until round 6 is read (turn 107)'
assert old_d in s
s = s.replace(old_d, '### 🔵 The two temporary Substack drafts: keep them for the next whole-article check (turn 108)')
old_d2 = 'They stay until its results are read.'
assert old_d2 in s
s = s.replace(old_d2, 'Round 6 is read, and the next whole-article check will reuse them, after your answers to 104 and 105, so they stay until its results are in.')

decided = f'''### 🟢 Round 6, and your message of 2026-10-25 12:39 UTC

Your message (turn 108; [JOEL-20261025-1239.md]({B}t108-answers/JOEL-20261025-1239.md)). You merged pull request #239.

- **Round 6:** your two links are read and recorded ([the round 6 page]({B}t108-results/ROUND6.md)): [half A]({A6}) and [half B]({B6}) both Human Written. What the two windows left are is question 105.
- **"those were just repeats of the questions you already asked me? well, edit wasn't even a page, it was a directory":** yes. The two folders held the readers' raw notes, and the ideas page was what you'd already answered, so I shouldn't have linked them at all. My final message's check now refuses a link to a folder.
- **Your comparison with Lucia's book, and Emotional Alchemy:** my answer, with a worked example, is question 104.

'''
k = s.index('### 🟢 103, 2026-10-25 00:24 UTC')
s = s[:k] + decided + s[k:]
P.write_text(s, encoding='utf-8')
print('ok')
