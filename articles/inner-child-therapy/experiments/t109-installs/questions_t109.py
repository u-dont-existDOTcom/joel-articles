#!/usr/bin/env python3
"""Turn 109's questions-page update: his answers of 2026-10-25 14:20 UTC go to Decided, and 106 opens: the review sheet
with every decision this turn leaves him (the sections in the new shape, the Pink question, the point-of-view read). Every
open item says what it's about (E257, Inner Child), every file it points to is a page link (repo_links.py), and every
AI result has its check's link.
  questions_t109.py            the update (the pull request named generally)
  questions_t109.py --pr N     names pull request #N in the to-do item and the head line"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
P = ROOT / 'OWNER-QUESTIONS.md'
B = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/'
SHEET = 'https://claude.ai/artifact/LTEDB18wTYzuUkgobzbUrn'
s = P.read_text(encoding='utf-8')
R = {}
for f in sorted((ROOT / 'experiments' / 't109-api').glob('API-RESULTS-*.jsonl')):
    for l in f.read_text(encoding='utf-8').splitlines():
        r = json.loads(l)
        R[r['name']] = r['dashboard_link']

if '--pr' in sys.argv:
    n = sys.argv[sys.argv.index('--pr') + 1]
    assert n.isdigit()
    old = '### 🟠 Merge the pull request for turn 109'
    assert old in s, 'run the update first'
    s = s.replace(old, '### 🟠 Merge pull request #%s (turn 109)' % n)
    s = s.replace('Turn 109: the lane\'s [open pull request](https://github.com/u-dont-existDOTcom/joel-articles/pulls?q=is%3Apr+is%3Aopen+head%3Ahandoff%2Fclaude-dangerous-adult-20260924-1631).',
                  'Turn 109: https://github.com/u-dont-existDOTcom/joel-articles/pull/%s.' % n)
    s = s.replace('For you to do: merge the turn-109 pull request.', 'For you to do: merge pull request #%s.' % n)
    P.write_text(s, encoding='utf-8')
    print('named #' + n)
    sys.exit(0)

old_head = 'Last updated 2026-10-25 (turns 82 to 108). **Open questions: 104, 105.** For you to do: merge pull request #241.'
assert old_head in s
s = s.replace(old_head, 'Last updated 2026-10-25 (turns 82 to 109). **Open questions: 106.** For you to do: merge the turn-109 pull request.')
old = 'after a turn by your other account (turns 100 to 108)'
assert old in s
s = s.replace(old, 'after a turn by your other account (turns 100 to 109)')

q = f'''### 🟣 106. The review sheet: the new shapes, your friend Pink, and the point-of-view read (turn 109)

Everything turn 109 leaves for you to decide is on [the review sheet]({SHEET}), one card each with Approve, Revise, Reject or Pending and a note; when you're done, press Copy JSON and paste it into the chat, from either account. The sheet's file is [REVIEW.html]({B}t109-review/REVIEW.html) (download it and open it in a browser if the sheet's link doesn't open from your other account). Nothing in the article changes until you decide.

- **The sections in the new shape** (your "yes this makes it much more of a readable guide, good"). Before You Tell the Hardest Stuff reads Human alone and as a section. Start With Whatever Showed Up is in its second try. Hear the Guard First took four tries, since one line of yours ("It puts you into the role of the Nurturer, which alleviates the instinct to argue back.") carried whichever paragraph held it to Human and the other read AI ([the checks]({B}t109-api/API-CHECKS.md)). My pick is the second try, installed now, with a line of your own for its first paragraph if you have one.
- **Your friend Pink:** is she OK being named with her diagnosis in a public post? Your paragraph read [Human alone]({R['t109_ifs_p8']}) and [in its section]({R['t109_sec_ifs']}).
- **The point-of-view read:** 61 places flagged by eight fresh readers under the new rule; 13 cuts, 10 places where my pick gives your reason from your own words, 3 that need words only you have, and 35 I left, with why ([all 61]({B}t109-pov/POV-READ.md)).

'''
i = s.index('### 🟣 104. A simpler shape for the guide')
j = s.index('## For you to do (no decision needed)')
s = s[:i] + q + s[j:]

i = s.index('### 🟠 Merge pull request #241 (turn 108)')
j = s.index('### 🔵 The two temporary Substack drafts')
s = s[:i] + ('### 🟠 Merge the pull request for turn 109\n\nTurn 109: the lane\'s [open pull request](https://github.com/u-dont-existDOTcom/joel-articles/pulls?q=is%3Apr+is%3Aopen+head%3Ahandoff%2Fclaude-dangerous-adult-20260924-1631). '
             'Open it, then click "Merge pull request" and "Confirm merge". That takes about a minute, and the page then says "Merged". (You merged #241, turn 108.)\n\n') + s[j:]
old_d = '### 🔵 The two temporary Substack drafts: keep them for the next whole-article check (turn 108)'
assert old_d in s
s = s.replace(old_d, '### 🔵 The two temporary Substack drafts: keep them for the next whole-article check (turn 109)')
old_d2 = 'Round 6 is read, and the next whole-article check will reuse them, after your answers to 104 and 105, so they stay until its results are in.'
assert old_d2 in s
s = s.replace(old_d2, 'Round 6 is read, and the next whole-article check will reuse them once your decisions on the review sheet are in, so they stay until its results are in.')

decided = f'''### 🟢 104 and 105, 2026-10-25 14:20 UTC

Your answers (turn 109; [JOEL-20261025-1420.md]({B}t109-answers/JOEL-20261025-1420.md)). You merged pull request #241.

- **104 A, "yes this makes it much more of a readable guide, good":** Hear the Guard First is in the new shape, and so are Start With Whatever Showed Up and Before You Tell the Hardest Stuff, every sentence word for word. Two reshaped paragraphs read AI alone at first; the tries and my pick are on the review sheet (question 106 above), and so are the densest sections I left as they are, with why.
- **105.1, your paragraph about your friend Pink:** in, word for word but for "explained" (your "expalined"). It read [Human alone]({R['t109_ifs_p8']}), and How This Relates to IFS read [Human as a section]({R['t109_sec_ifs']}). Whether to name her is on the review sheet.
- **105.2, "this is the part that reads ai and it's actually redundant also":** your first sentence and your two for the start of the next paragraph are in, with "Pema Chödrön's" for "Pema Chodron's", as the article spells her name elsewhere. The paragraph read [Human alone]({R['t109_photos_p2']}) and the section [Human]({R['t109_sec_photos']}).
- **"save all the sections that pangram marked as less than human high confidence":** saved, all 111 of round 6's windows below Human with high confidence, by section, with whose words each one is and whether it's still in the article ([the list]({B}t109-windows/WINDOWS.md)): 4 AI, 17 Human with Low confidence and 90 with Medium, 21 of them seams of three words or fewer.
- **"use the new rule in the repo about marking wherever it looks like there's a lack of a real POV":** done, with the rule's omission test first (main's newer part: a line that only says again what's there is a cut, never a request for your point of view). Eight fresh readers read an eighth of the guide each and flagged 61 places ([all 61, with my check]({B}t109-pov/POV-READ.md)); the ones to decide are on the review sheet.

'''
k = s.index('### 🟢 Round 6, and your message of 2026-10-25 12:39 UTC')
s = s[:k] + decided + s[k:]
P.write_text(s, encoding='utf-8')
print('ok')
