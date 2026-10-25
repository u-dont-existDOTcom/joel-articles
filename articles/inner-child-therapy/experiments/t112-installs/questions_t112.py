#!/usr/bin/env python3
"""Turn 112's questions-page update: his answers of 2026-10-25 21:40 UTC go to Decided (108), 109 opens (Solomon's paradox in
his version of Borrow Love's third paragraph names the trick, where the study names the gap), round 7's check is his to-do,
and the paragraph-headings pilot is what comes next. Every open item says what it's about (E257, Inner Child), with my pick,
and every file it points to is a page link."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
P = ROOT / 'OWNER-QUESTIONS.md'
B = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/'
s = P.read_text(encoding='utf-8')


def rep(a, b):
    global s
    assert s.count(a) == 1, a[:80]
    s = s.replace(a, b)


rep('Last updated 2026-10-25 (turns 82 to 111). **Open questions: 108.** For you to do: merge pull request #249.',
    'Last updated 2026-10-25 (turns 82 to 112). **Open questions: 109.** For you to do: check the two drafts in Pangram '
    'and send me the two links, and merge the turn-112 pull request.')
rep('after a turn by your other account (turns 100 to 111)', 'after a turn by your other account (turns 100 to 112)')

q = f'''### 🟣 109. Solomon's paradox in Borrow Love's third paragraph (turn 112)

Your version of the paragraph is in, word for word, with the two links your earlier version had: "psychological trick" goes to the self-distancing study the old "cheap trick" link went to ([Kross and Grossmann, 2012](https://pubmed.ncbi.nlm.nih.gov/21728454/)), and "Solomon’s paradox" to [Grossmann and Kross, 2014](https://pubmed.ncbi.nlm.nih.gov/24916084/).

One thing in it: your sentence gives the name to the trick ("This psychological trick has a rich history around it, and even has a name, Solomon’s paradox"). In the study, Solomon's paradox is the gap the trick gets around, that people reason more wisely about other people's problems than about their own. Its title is "Exploring Solomon's paradox: self-distancing eliminates the self-other asymmetry". The old version had the name on the gap: "And the gap it gets around even has a name".

- **A (my pick):** the name goes on the gap, and the rest of your sentence stays. I bring that wording through the checks and show it to you before it goes in. The article links the study, so a reader who clicks it sees the difference.
- **B:** keep it as you wrote it. The trick and the gap are close enough that most readers won't stop on it.
- **C:** your own wording.

'''
i = s.index("### 🟣 108. One cut that turned its paragraph AI, and Just Like Me's second paragraph (turn 111)")
j = s.index('## For you to do (no decision needed)')
s = s[:i] + q + s[j:]

i = s.index('### 🟠 Merge pull request #249 (turn 111)')
j = s.index('### 🔵 The two temporary Substack drafts')
todo = ('### 🟠 Round 7: check the two drafts in Pangram and send me the two links (turn 112)\n\n'
        'The whole article is in the two temporary Substack drafts again, so this one check covers every section changed since '
        'round 6 (turns 108 to 112). In your Brave, open [draft A](https://ibogaqueen.substack.com/publish/post/221982879) and '
        '[draft B](https://ibogaqueen.substack.com/publish/post/221983135), click Preview, then "Paid subscriber view" at the top. '
        'Click the green label next to the author\'s name, then "View Full Analysis", and send me each result page\'s link '
        '("Copy shareable link to result"), as you did for round 6. The label\'s word isn\'t the result; the result page\'s '
        'windows are what I read. That takes about two minutes.\n\n'
        '### 🟠 Merge the pull request for turn 112\n\n'
        'Turn 112: the lane\'s [open pull request](https://github.com/u-dont-existDOTcom/joel-articles/pulls?q=is%3Apr+is%3Aopen+'
        'head%3Ahandoff%2Fclaude-dangerous-adult-20260924-1631). Open it, then click "Merge pull request" and "Confirm merge". '
        'That takes about a minute, and the page then says "Merged". (You merged #249, turn 111.)\n\n')
s = s[:i] + todo + s[j:]
i = s.index('### 🔵 The two temporary Substack drafts: keep them for the next whole-article check (turn 111)')
j = s.index('## Decided')
drafts = ('### 🔵 The two temporary Substack drafts: keep them until round 7 is read (turn 112)\n\n'
          '"Inner Child, draft A (temp, delete after)" and "Inner Child, draft B (temp, delete after)" hold round 7\'s text. '
          'Once its results are in, a permanent delete is one thing I leave to you: in your Substack drafts list, open each '
          'one\'s "…" menu and choose Delete. That\'s about a minute.\n\n')
s = s[:i] + drafts + s[j:]

decided = f'''### 🟢 108, 2026-10-25 21:40 UTC

Your message ([JOEL-20261025-2140.md]({B}t112-answers/JOEL-20261025-2140.md)). You merged pull request #249.

- **108.1, "this version passes":** your version of Borrow Love's third paragraph is in, word for word, with the two links your earlier version had. Question 109 is one thing in it.
- **108.2, "a":** Just Like Me's second paragraph stays your sentence alone.
- **"idk why you stopped giving me the full humanized article on each turn":** it should have gone with every turn, and it's attached again. The chat check now refuses a final message without it ([HUMANIZATION-GATE.md, E271](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/docs/HUMANIZATION-GATE.md)).
- **"it doesn't look like you kept the structure you showed me to begin with":** the italic labels on the turn-108 example were only page labels, so no headings went in. The order that went in is the turn-110 agreement, which differs from the example where a line stays with what it belongs to: "Tell me what you remember, I'm listening." answers "that part remembers", and the roommate comes just before "That part doesn't have to move out" so the move-out keeps the roommate picture ([AGREED.md]({B}t110-review/AGREED.md)).
- **"what do you think about that?" (a little heading on each paragraph):** yes where each paragraph is its own case, so a reader can skip to theirs, and no in sections that tell a story or build an argument, where a heading would cut a thought in half. The pilot on Hear the Guard First comes next, as proposals (Coming up, below).

'''
k = s.index('### 🟢 107, 2026-10-25 20:08 UTC')
s = s[:k] + decided + s[k:]

nxt = '''### 🔵 Next: headings where each paragraph is its own case (turn 112)

Your idea of 2026-10-25 21:40 UTC: a clear little heading on each paragraph, so a reader can skip the parts that don't apply. First a pilot on Hear the Guard First, shown in place in the whole article on a review page: a short heading over each case, worded the way a reader would describe their own situation, and each paragraph's first sentence changed only where it would repeat its heading. The new words go through the owner-delivery gate first and each changed paragraph through Pangram. If you like it, the other sections built the same way follow, together with the reshape batch, so each section is reworked once.

'''
k = s.index('### 🔵 Next\n')
s = s[:k] + nxt + s[k:]
P.write_text(s, encoding='utf-8')
print('ok')
