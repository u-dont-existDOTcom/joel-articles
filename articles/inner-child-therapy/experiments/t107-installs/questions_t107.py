#!/usr/bin/env python3
"""Turn 107's questions-page update: 103 moves to Decided with Joel's answers of 2026-10-25 00:24 UTC; no question is open.
Pull request #233 is merged (2026-10-24 23:45 UTC), so the to-do item names the turn-107 pull request once it's open:
  questions_t107.py            the update (the pull request named generally)
  questions_t107.py --pr N     names pull request #N in the to-do item and the head line
Every file the page points to is a link (tools/humanization/repo_links.py; questions_page.py refuses a path)."""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
P = ROOT / 'OWNER-QUESTIONS.md'
B = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/'
T = 'https://github.com/u-dont-existDOTcom/joel-articles/tree/handoff/claude-dangerous-adult-20260924-1631/'
E = B + 'articles/inner-child-therapy/experiments/'
UDA = 'https://github.com/u-dont-existDOTcom/universal-dev-architecture/blob/main/patterns/'
s = P.read_text(encoding='utf-8')

if '--pr' in sys.argv:
    n = sys.argv[sys.argv.index('--pr') + 1]
    assert n.isdigit()
    old = '### 🟠 Merge the pull request for turn 107'
    assert old in s, 'run the update first'
    s = s.replace(old, '### 🟠 Merge pull request #%s (turn 107)' % n)
    s = s.replace('Turn 107: the lane\'s [open pull request](https://github.com/u-dont-existDOTcom/joel-articles/pulls?q=is%3Apr+is%3Aopen+head%3Ahandoff%2Fclaude-dangerous-adult-20260924-1631).',
                  'Turn 107: https://github.com/u-dont-existDOTcom/joel-articles/pull/%s.' % n)
    s = s.replace('For you to do: merge the turn-107 pull request.', 'For you to do: merge pull request #%s.' % n)
    P.write_text(s, encoding='utf-8')
    print('named #' + n)
    sys.exit(0)

old_head = 'Last updated 2026-10-24 (turns 82 to 106). **Open questions: 103.** For you to do: merge pull request #233.'
assert old_head in s
s = s.replace(old_head, 'Last updated 2026-10-25 (turns 82 to 107). **Open questions: none.** For you to do: merge the turn-107 pull request.')
for old, new in (
        ('rebuilt after every change (`tools/questions_page.py`)',
         'rebuilt after every change ([questions_page.py](%sarticles/inner-child-therapy/tools/questions_page.py))' % B),
        ('(UDA `patterns/owner-questions-page.md`, `patterns/cross-account-continuity.md`)',
         '(UDA [owner-questions-page.md](%sowner-questions-page.md), [cross-account-continuity.md](%scross-account-continuity.md))' % (UDA, UDA)),
        ('after a turn by your other account (turns 100 to 106)', 'after a turn by your other account (turns 100 to 107)')):
    assert s.count(old) == 1, old
    s = s.replace(old, new)

i = s.index('### 🟣 103. ')
j = s.index('## For you to do (no decision needed)')
q103_asked = s[i:j].rstrip('\n').replace('### 🟣 103. ', '#### 103. ', 1)
s = s[:i] + 'None right now. Round 6, below, comes next.\n\n' + s[j:]

old_pr = ('### 🟠 Merge pull request #233 (turns 104 to 106)\n\nTurns 104 to 106: https://github.com/u-dont-existDOTcom/joel-articles/pull/233. '
          'Open it, then click "Merge pull request" and "Confirm merge". That takes about a minute, and the page then says "Merged". (You merged #229.)')
assert old_pr in s
s = s.replace(old_pr, '### 🟠 Merge the pull request for turn 107\n\nTurn 107: the lane\'s [open pull request](https://github.com/u-dont-existDOTcom/joel-articles/pulls?q=is%3Apr+is%3Aopen+head%3Ahandoff%2Fclaude-dangerous-adult-20260924-1631). '
              'Open it, then click "Merge pull request" and "Confirm merge". That takes about a minute, and the page then says "Merged". (You merged #233, turns 104 to 106.)')
old_r6 = ('### 🔵 Round 6, the next whole-article check (turn 101)\n\nYour picks from the ideas page are in, so it comes next: one whole-article '
          'check through the two temporary Substack drafts, covering everything since round 5.')
assert old_r6 in s
s = s.replace(old_r6, '### 🔵 Round 6, the next whole-article check (turn 107)\n\nYour two sections and your answers on the acacia line and the typo are in, so it comes next: one whole-article check '
              'through the two temporary Substack drafts, covering everything since round 5 (turns 100 to 107).')

decided = f'''### 🟢 103, 2026-10-25 00:24 UTC

Your message (turn 107; [JOEL-20261025-0024.md]({E}t107-answers/JOEL-20261025-0024.md)).

- **103.1:** your My Journey is in, word for word, with its bypassing paragraph second. Your paste was plain text, so each link and the two italic words (*Understandable* and *Unforgivable*) are back on the same words, and each of your lines is its own paragraph, as the article had them.
- **"you put in some of my things too verbatim":** three of the lines you rewrote were answers you had typed to me, which I had put in close to as you typed them: your clarification for the My Journey tension ("stop in the sense of ... like I might still kind of allow the exercise to play out somehow"), how you found Daja, and "in general and map it out completely". The rule against that was already in the gate, and it didn't fire because you had picked "your words to tie them together", which I took as you giving me the line. Now, when an answer of yours explains something, I write the article sentence from it and show it beside your words (E261, Inner Child). What else your two rewrites do is in [LESSONS.md]({E}t107-answers/LESSONS.md), with a search of your saved messages for other answers that went in as typed.
- **103.2:** your first three paragraphs of Not Every Hero Wears A Cape are in, word for word. Make It Intentional and its two paragraphs stay.
- **103.3 A:** your acacia sentence stays as you wrote it.
- **103.4 A:** "But do notice if progress is stagnating."
- **"i have no idea where the 3 files are":** ENGAGING.md named them by their places in the repository, which your app shows as text. They are [BOOKS.md]({E}t102-safety/BOOKS.md), on how three books, hers among them, keep safety in one place, and the folders of the two reads' notes, [caveats/]({T}articles/inner-child-therapy/experiments/t105-readers-edit/caveats) and [edit/]({T}articles/inner-child-therapy/experiments/t105-readers-edit/edit). You don't need to read the folders: what their readers proposed is all on the ideas page, [IDEAS.md]({E}t105-readers-edit/IDEAS.md), which you answered on 2026-10-24. [ENGAGING.md]({E}t105-readers-edit/ENGAGING.md) links them now, and so does turn 106's lessons file. A new check, [repo_links.py]({B}tools/humanization/repo_links.py), finds a file named that way in anything I send you, and this page refuses one.

<details><summary>103 as it was asked</summary>

{q103_asked}

</details>

'''
k = s.index('### 🟢 102, 2026-10-24 22:55 UTC')
s = s[:k] + decided + s[k:]
P.write_text(s, encoding='utf-8')
print('ok')
