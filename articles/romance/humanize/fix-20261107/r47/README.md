# r47: step 2 opens with what it asks (the game's v0.9.2)

His message, 2026-11-27 15:45 UTC, answering the question put to him with v0.9.1 ("Should I make "What is this answer
based on?" the heading and show the question smaller underneath?"):

> YES

Nothing in the article changed. Everything below is in his private repository `love-honestly`, on the branch of
[its draft pull request](https://github.com/u-dont-existDOTcom/love-honestly/pull/2), which now carries v0.6.0 to
v0.9.2. Nothing is merged or deployed: his site still serves v0.5.4.

## v0.9.2

- Step 2 of a card, for two people and for one: the heading, and the biggest text, is now **"What is this answer based
  on?"**. Under it, after "Your answer to", comes the card's question, smaller, in the typeface it has on step 1 (for
  one person, its one-person wording). The instruction keeps its words ("These labels are not your answer. Choose the
  most honest basis for the answer you just formed.") as the line above the labels it talks about.
- The only new words are "Your answer to", so the question reads as the one the answer was to, not a second question.
  The seven labels and what each says are unchanged; no card, step or rule changes.
- Seen while building, at 1440 pixels: the question ran as one line of about 150 characters. It is held to 720 pixels,
  as the line under a heading is.
- [What changed in v0.9.2](https://github.com/u-dont-existDOTcom/love-honestly/blob/claude/v0.6.0-article-update/versions/v0.9.2/CHANGES.md).

## Checks

- `build.py --check`; `check.mjs --mutants`: seven deliberate breakages caught (the question as heading again for two
  people; the one-person screen left as it was; the question gone; the two-person screen showing the one-person
  wording; the instruction's words changed; the new style rules gone; an evidence label changed).
- `browser-check.mjs`: 146 checks, 43 of them new, run twice. Its new section 11 measures step 2 for one person and for
  two at 320, 375, 414, 768, 1024 and 1440 pixels and at 200% zoom: the heading is the first and biggest text, the
  question under it is the one answered on step 1, smaller and in its typeface, the instruction sits above the seven
  labels, the three start at the same left edge, and nothing is wider than the screen.
- Not run: the repository's container gate (needs Docker).
- SHA-256 of v0.9.2: `018b0efd161fbdc69ed89f1ad52a6c0760513bc3f1befad5814512dd020ab74e`.

## Sent to him

The file in chat (`love-honestly-v0.9.2-candidate.html`), a before-and-after picture of step 2 on a phone, and the
game as a private page of the account that ran this turn (the file with its title changed and `viewport-fit=cover`
taken out of the viewport line).

## Next

His OK on a version (v0.9.2 carries v0.9.1's changes too), or his changes to it; then the pull request is merged, the
innerself site vendors the file, and the site is deployed with his go-ahead.
