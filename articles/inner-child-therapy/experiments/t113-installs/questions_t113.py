#!/usr/bin/env python3
"""Turn 113's questions-page update: his answers of 2026-10-25 22:38 UTC go to Decided (109 and round 7), and 110 opens:
the review sheet with every edit proposed this turn, for him and then GPT. Every open item says what it's about (E257,
Inner Child), with my pick, and every file it points to is a page link.
  questions_t113.py [--pr N]"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
P = ROOT / 'OWNER-QUESTIONS.md'
B = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/'
SHEET = 'https://claude.ai/artifact/LTEDB18wTYzuUkgobzbUrn'
N = sys.argv[sys.argv.index('--pr') + 1] if '--pr' in sys.argv else None
PR = ('pull request #%s' % N) if N else 'the turn-113 pull request'
PR_LINK = ('[pull request #%s](https://github.com/u-dont-existDOTcom/joel-articles/pull/%s)' % (N, N)) if N else \
    '[open pull request](https://github.com/u-dont-existDOTcom/joel-articles/pulls?q=is%3Apr+is%3Aopen+head%3Ahandoff%2Fclaude-dangerous-adult-20260924-1631)'
review = json.loads((ROOT / 'experiments' / 't113-review' / 'REVIEW.json').read_text(encoding='utf-8'))
heads = [s for s in review['suggestions'] if s['type'] == 'heads']
n_heads = sum(1 for s in heads for r in s['reads'] if r.get('kind'))
n_new = sum(1 for s in heads for r in s['reads'] if r.get('kind') and r.get('new'))
s = P.read_text(encoding='utf-8')


def rep(a, b):
    global s
    assert s.count(a) == 1, a[:80]
    s = s.replace(a, b)


rep('Last updated 2026-10-25 (turns 82 to 112). **Open questions: 109.** For you to do: check the two drafts in Pangram '
    'and send me the two links, and merge pull request #250.',
    'Last updated 2026-10-26 (turns 82 to 113). **Open questions: 110.** For you to do: give GPT the review sheet, and '
    'merge %s.' % PR)
rep('after a turn by your other account (turns 100 to 112)', 'after a turn by your other account (turns 100 to 113)')

q = f'''### 🟣 110. The review sheet: case headings in {len(heads)} sections, long paragraphs split, and your 109 A wording (turn 113)

Everything is on [the review sheet]({SHEET}), the whole guide with each change in place, for you and then GPT, as you asked ("do the major edits as you suggested and then i can see what GPT thinks of all the changes"). Nothing in the guide changes until you approve. The sheet's file is [REVIEW.html]({B}t113-review/REVIEW.html) (download it and open it in a browser if the link doesn't open from your other account).

- **{n_heads} case headings in {len(heads)} sections**, over each paragraph that is its own case, so a reader can skip to theirs. {n_heads - n_new} are your own words from the paragraph under them; the other {n_new} have new words, and each passed the owner-delivery gate first ([GATE.md]({B}t113-gate/GATE.md)).
- **Long paragraphs split** where they change subject, every sentence kept: How Would You Know It's Helping? (210 words, in four) and How to Forgive Without Forgetting's last paragraph, and inside the headed sections one each in Start With Whatever Showed Up, When to Change the Strategy and Other Folks Also Have Hooks, and two in When Escape Leaves Reality Behind. In Start With Whatever Showed Up one sentence also moves up three sentences, to stay with what it's about.
- **Your 109 A**: "the blind spot behind it even has a name, Solomon’s paradox", the rest of your sentence as it is.
- **One question**: your guide's test line says "makes me more grounded, truthful, and free" in a paragraph that talks to "you". My pick: "you".

The sections I looked at and would leave as they are, with why, are in the sheet's opening. Four fresh readers read every section as it would read, and what I did with each of their notes is in [COLD-READ.md]({B}t113-shape/COLD-READ.md).

- **A (my pick):** give GPT the sheet as you planned (on the page, select all and copy), and paste its review here. I take both, as in turn 110, and the next sheet has only what we both recommend.
- **B:** decide the cards yourself now: Approve, Reject or Revise on each, then "Save / send" and "Copy my answers", and paste them here.

'''
i = s.index("### 🟣 109. Solomon's paradox in Borrow Love's third paragraph (turn 112)")
j = s.index('## For you to do (no decision needed)')
s = s[:i] + q + s[j:]

i = s.index('### 🟠 Round 7: check the two drafts in Pangram and send me the two links (turn 112)')
j = s.index('### 🔵 The two temporary Substack drafts')
todo = ('### 🟠 Merge %s (turn 113)\n\n'
        'Turn 113: the lane\'s %s. Open it, then click "Merge pull request" and "Confirm merge". That takes about a minute, '
        'and the page then says "Merged". (You merged #250, turn 112.)\n\n' % (PR, PR_LINK))
s = s[:i] + todo + s[j:]
rep('### 🔵 The two temporary Substack drafts: keep them until round 7 is read (turn 112)\n\n'
    '"Inner Child, draft A (temp, delete after)" and "Inner Child, draft B (temp, delete after)" hold round 7\'s text.',
    '### 🔵 The two temporary Substack drafts: keep them for the next check (turn 113)\n\n'
    '"Inner Child, draft A (temp, delete after)" and "Inner Child, draft B (temp, delete after)" still hold round 7\'s text. '
    'The next check puts in what you approve from the review sheet.')

decided = f'''### 🟢 109 and round 7, 2026-10-25 22:38 UTC

Your message ([JOEL-20261025-2238.md]({B}t113-answers/JOEL-20261025-2238.md)). You merged pull request #250.

- **109, "109a":** the name goes on the gap. The wording, "the blind spot behind it even has a name", passed the owner-delivery gate and is on the review sheet (question 110 above), with the rest of your sentence as it is.
- **"no point checking the drafts at this point, we are about to make major edits":** round 7 of the guide as it is was skipped, and the drafts wait for what you approve from the sheet, so the one check reads the version that goes in.
- **"do the major edits as you suggested ... (not just the headings idea but fixing the way the sections read as you did with Hear the Guard)":** on the review sheet. Of the five sections I'd planned to reshape next, Borrow One Competency at a Time already goes the plain path first and then one job a paragraph, so it gets headings; the other four keep their order, for the reasons in the sheet's opening (How to Forgive Without Forgetting gets a split).

'''
k = s.index('### 🟢 108, 2026-10-25 21:40 UTC')
s = s[:k] + decided + s[k:]
i = s.index('### 🔵 Next: headings where each paragraph is its own case (turn 112)')
j = s.index('### 🔵 Next\n')
s = s[:i] + ('### 🔵 Next: GPT\'s review, then a sheet of what we both recommend (turn 113)\n\n'
             'When GPT\'s review is in, I take its advice card by card as in turn 110, and the next sheet has only what we both '
             'recommend. What you approve goes in word for word, and then the two drafts get it for the free check.\n\n') + s[j:]
P.write_text(s, encoding='utf-8')
print('ok', len(heads), n_heads, n_new)
